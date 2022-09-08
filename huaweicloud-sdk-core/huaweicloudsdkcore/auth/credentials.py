# coding: utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

import re
import os
from abc import abstractmethod

from huaweicloudsdkcore.auth.internal import Iam, Metadata
from huaweicloudsdkcore.exceptions.exceptions import ApiValueError, ServiceResponseException
from huaweicloudsdkcore.signer.signer import Signer, DerivationAKSKSigner
from huaweicloudsdkcore.auth.cache import AuthCache
from huaweicloudsdkcore.utils import time_utils, six_utils


class DerivedCredentials(six_utils.get_abstract_meta_class()):
    _DEFAULT_ENDPOINT_REG = "^[a-z][a-z0-9-]+(\\.[a-z]{2,}-[a-z]+-\\d{1,2})?\\.(my)?(huaweicloud|myhwclouds).(com|cn)"

    @abstractmethod
    def _process_derived_auth_params(self, derived_auth_service_name, region_id):
        pass

    @abstractmethod
    def with_derived_predicate(self, derived_predicate):
        pass

    @abstractmethod
    def _is_derived_auth(self, request):
        pass

    @classmethod
    def get_default_derived_predicate(cls):
        return lambda request: False if re.match(cls._DEFAULT_ENDPOINT_REG, request.host) else True


class TempCredentials(six_utils.get_abstract_meta_class()):
    @abstractmethod
    def _need_update_security_token(self):
        pass

    @abstractmethod
    def update_security_token_from_metadata(self):
        pass


class FederalCredentials(six_utils.get_abstract_meta_class()):
    @abstractmethod
    def _need_update_auth_token(self):
        pass

    @abstractmethod
    def _update_auth_token_by_id_token(self, http_client):
        pass


class Credentials(DerivedCredentials, TempCredentials, FederalCredentials):
    _TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
    _X_SECURITY_TOKEN = "X-Security-Token"
    _X_AUTH_TOKEN = "X-Auth-Token"

    def __init__(self, ak=None, sk=None):
        self.ak = ak
        self.sk = sk
        self.idp_id = None
        self.id_token_file = None
        self.iam_endpoint = None
        self.security_token = None
        self._derived_auth_service_name = None
        self._derived_predicate = None
        self._expired_at = None
        self._auth_token = None
        self._region_id = None

    def with_ak(self, ak):
        self.ak = ak
        return self

    def with_sk(self, sk):
        self.sk = sk
        return self

    def with_idp_id(self, idp_id):
        self.idp_id = idp_id
        return self

    def with_id_token_file(self, id_token_file):
        self.id_token_file = id_token_file
        return self

    def with_iam_endpoint(self, endpoint):
        self.iam_endpoint = endpoint
        return self

    def with_security_token(self, token):
        self.security_token = token
        return self

    def get_update_path_params(self):
        pass

    def process_auth_params(self, http_client, region_id):
        pass

    def process_auth_request(self, request, http_client):
        if self._need_update_auth_token():
            self._update_auth_token_by_id_token(http_client)
        elif self._need_update_security_token():
            self.update_security_token_from_metadata()

        return http_client.executor.submit(self.sign_request, request)

    def sign_request(self, request):
        if self._auth_token:
            request.header_params[self._X_AUTH_TOKEN] = self._auth_token
            Signer.process_request_uri(request)
            return request
        if self.security_token is not None:
            request.header_params["X-Security-Token"] = self.security_token

        if "Content-Type" in request.header_params and not request.header_params["Content-Type"].startswith(
                "application/json"):
            request.header_params["X-Sdk-Content-Sha256"] = "UNSIGNED-PAYLOAD"

        return DerivationAKSKSigner(self).sign(request, self._derived_auth_service_name, self._region_id) \
            if self._is_derived_auth(request) else Signer(self).sign(request)

    def _is_derived_auth(self, request):
        if not self._derived_predicate:
            return False

        return self._derived_predicate(request)

    def with_derived_predicate(self, derived_predicate):
        self._derived_predicate = derived_predicate
        return self

    def _process_derived_auth_params(self, derived_auth_service_name, region_id):
        pass

    def _need_update_security_token(self):
        if not self._expired_at or not self.security_token:
            return False
        return self._expired_at - time_utils.get_timestamp_utc() < 60

    def update_security_token_from_metadata(self):
        credential = Metadata.get_credential_from_metadata()

        self.ak = credential.get("access")
        self.sk = credential.get("secret")
        self.security_token = credential.get("securitytoken")
        self._expired_at = time_utils.get_timestamp_from_str(credential.get("expires_at"), self._TIME_FORMAT)

    def _need_update_auth_token(self):
        if not self.idp_id or not self.id_token_file:
            return False
        if not self._auth_token or not self._expired_at:
            return True
        return self._expired_at - time_utils.get_timestamp_utc() < 60

    def _update_auth_token_by_id_token(self, http_client):
        pass

    def _get_id_token(self):
        if not os.path.exists(self.id_token_file):
            raise ApiValueError("id_token_file '{}' does not exist".format(self.id_token_file))

        with open(self.id_token_file, "r") as f:
            id_token = f.read()
        if not id_token:
            raise ApiValueError("id_token is empty in id_token_file '{}'".format(self.id_token_file))
        return id_token


class BasicCredentials(Credentials):
    _X_PROJECT_ID = "X-Project-Id"

    def __init__(self, ak=None, sk=None, project_id=None):
        """For regional services' authentication

        :param ak: The access key ID for your account
        :param sk: The secret access key for your account
        :param project_id: The ID of your project depending on your region which you want to operate
        """
        super(BasicCredentials, self).__init__(ak, sk)
        self.project_id = project_id

    def with_project_id(self, project_id):
        self.project_id = project_id
        return self

    def get_update_path_params(self):
        path_params = {}
        if self.project_id:
            path_params["project_id"] = self.project_id
        return path_params

    def _process_derived_auth_params(self, derived_auth_service_name, region_id):
        if not self._derived_auth_service_name:
            self._derived_auth_service_name = derived_auth_service_name

        if not self._region_id:
            self._region_id = region_id

    def process_auth_params(self, http_client, region_id):
        if self.idp_id or self.id_token_file:
            if not self.idp_id:
                raise ApiValueError("idp_id is required when using idp_id & id_token_file")
            elif not self.id_token_file:
                raise ApiValueError("id_token_file is required when using idp_id & id_token_file")
            if not self.project_id:
                raise ApiValueError("project_id is required when using idp_id & id_token_file")

        if self.project_id:
            return self

        ak_with_name = self.ak + region_id
        project_id = AuthCache.get_auth(ak_with_name)
        if project_id:
            self.project_id = project_id
            return self

        derived_predicate = self._derived_predicate
        self._derived_predicate = None

        if self.iam_endpoint is None:
            self.iam_endpoint = Iam.get_iam_endpoint()
        future_request = self.process_auth_request(
            Iam.get_keystone_list_projects_request(self.iam_endpoint, region_id=region_id), http_client)
        request = future_request.result()
        try:
            self.project_id = Iam.keystone_list_projects(http_client, request)
            AuthCache.put_auth(ak_with_name, self.project_id)
        except ServiceResponseException as e:
            err_msg = e.error_msg if hasattr(e, "error_msg") else "unknown exception."
            raise ApiValueError("Failed to get project id, " + err_msg)

        self._derived_predicate = derived_predicate

        return self

    def sign_request(self, request):
        if self.project_id:
            request.header_params[self._X_PROJECT_ID] = self.project_id
        return super(BasicCredentials, self).sign_request(request)

    def _update_auth_token_by_id_token(self, http_client):
        iam_endpoint = self.iam_endpoint if self.iam_endpoint else Iam.get_iam_endpoint()
        request = Iam.get_create_token_by_id_token_request(iam_endpoint, self.idp_id, self._get_id_token(),
                                                           project_id=self.project_id)
        token, expired_str = Iam.create_token_by_id_token(http_client, request)
        self._expired_at = time_utils.get_timestamp_from_str(expired_str, self._TIME_FORMAT)
        self._auth_token = token


class GlobalCredentials(Credentials):
    _X_DOMAIN_ID = "X-Domain-Id"

    def __init__(self, ak=None, sk=None, domain_id=None):
        """For global services' authentication

        :param ak: The access key ID for your account
        :param sk: The secret access key for your account
        :param domain_id: The account ID of Huawei Cloud
        """
        super(GlobalCredentials, self).__init__(ak, sk)
        self.domain_id = domain_id

    def with_domain_id(self, domain_id):
        self.domain_id = domain_id
        return self

    def get_update_path_params(self):
        path_params = {}
        if self.domain_id:
            path_params["domain_id"] = self.domain_id
        return path_params

    def process_auth_params(self, http_client, region_id):
        if self.idp_id or self.id_token_file:
            if not self.idp_id:
                raise ApiValueError("idp_id is required when using idp_id & id_token_file")
            elif not self.id_token_file:
                raise ApiValueError("id_token_file is required when using idp_id & id_token_file")
            if not self.domain_id:
                raise ApiValueError("domain_id is required when using idp_id & id_token_file")

        if self.domain_id:
            return self

        domain_id = AuthCache.get_auth(self.ak)
        if domain_id:
            self.domain_id = domain_id
            return self

        derived_predicate = self._derived_predicate
        self._derived_predicate = None

        if self.iam_endpoint is None:
            self.iam_endpoint = Iam.get_iam_endpoint()
        future_request = self.process_auth_request(Iam.get_keystone_list_auth_domains_request(self.iam_endpoint),
                                                   http_client)
        request = future_request.result()
        try:
            self.domain_id = Iam.keystone_list_auth_domains(http_client, request)
            AuthCache.put_auth(self.ak, self.domain_id)
        except ServiceResponseException as e:
            err_msg = e.error_msg if hasattr(e, "error_msg") else "unknown exception."
            raise ApiValueError("Failed to get domain id, " + err_msg)

        self._derived_predicate = derived_predicate

        return self

    def sign_request(self, request):
        if self.domain_id:
            request.header_params[self._X_DOMAIN_ID] = self.domain_id
        return super(GlobalCredentials, self).sign_request(request)

    def _process_derived_auth_params(self, derived_auth_service_name, region_id):
        if not self._derived_auth_service_name:
            self._derived_auth_service_name = derived_auth_service_name

        if not self._region_id:
            self._region_id = "globe"

    def _update_auth_token_by_id_token(self, http_client):
        iam_endpoint = self.iam_endpoint if self.iam_endpoint else Iam.get_iam_endpoint()
        request = Iam.get_create_token_by_id_token_request(iam_endpoint, self.idp_id, self._get_id_token(),
                                                           domain_id=self.domain_id)
        token, expired_str = Iam.create_token_by_id_token(http_client, request)
        self._expired_at = time_utils.get_timestamp_from_str(expired_str, self._TIME_FORMAT)
        self._auth_token = token
