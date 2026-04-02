# coding: utf-8
"""
 Copyright 2020 Huawei Technologies Co.,Ltd.

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
import json
import re
import threading
from abc import abstractmethod, ABC
from typing import Callable, Optional, Dict, Any

from huaweicloudsdkcore.auth.internal import IamHelper, MetadataAccessor, StsHelper, StsAccessor, FederalAccessor
from huaweicloudsdkcore.exceptions.exceptions import ApiValueError, ServiceResponseException, SdkException, \
    HostUnreachableException
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer.algorithm import SigningAlgorithm
from huaweicloudsdkcore.signer.signer import Signer, SM3Signer, DerivationAKSKSigner, P256SHA256Signer, SM2SM3Signer
from huaweicloudsdkcore.utils import string_utils, six_utils, time_utils


class DerivedCredentials(ABC):
    _DEFAULT_ENDPOINT_REG = "^[a-z][a-z0-9-]+(\\.[a-z]{2,}-[a-z]+-\\d{1,2})?\\.(my)?(huaweicloud|myhwclouds).(com|cn)"

    @abstractmethod
    def _process_derived_auth_params(self, derived_auth_service_name: str, region_id: str):
        pass

    @abstractmethod
    def with_derived_predicate(self, derived_predicate: Callable[[SdkRequest], bool]):
        pass

    @abstractmethod
    def _is_derived_auth(self, request: SdkRequest) -> bool:
        pass

    @classmethod
    def get_default_derived_predicate(cls) -> Callable[[SdkRequest], bool]:
        return lambda request: not bool(re.match(cls._DEFAULT_ENDPOINT_REG, request.host))


class Credentials(DerivedCredentials):
    _X_SECURITY_TOKEN = "X-Security-Token"
    _AUTHORIZATION = "Authorization"
    _DEFAULT_EXPIRATION_THRESHOLD_SECONDS = 40 * 60  # 40min
    _CACHE = {}
    _LOCK = threading.Lock()
    _SIGNER_CASE = {
        SigningAlgorithm.HMAC_SHA256: Signer,
        SigningAlgorithm.HMAC_SM3: SM3Signer,
        SigningAlgorithm.ECDSA_P256_SHA256: P256SHA256Signer,
        SigningAlgorithm.SM2_SM3: SM2SM3Signer
    }

    def __init__(self, ak: str = None, sk: str = None):
        super().__init__()
        self._ak = ak
        self._sk = sk
        self._idp_id: Optional[str] = None
        self._id_token_file: Optional[str] = None
        self._iam_endpoint: Optional[str] = None
        self._security_token: Optional[str] = None
        self._derived_auth_service_name: Optional[str] = None
        self._derived_predicate: Optional[Callable[[SdkRequest], bool]] = None
        self._region_id: Optional[str] = None
        self._sts_accessor: Optional[StsAccessor] = None
        self._expire_at: Optional[float] = 0
        self._once = six_utils.Once()

    @property
    def ak(self):
        return self._ak

    @ak.setter
    def ak(self, value: str):
        if not value:
            raise ValueError("ak cannot be None or empty")
        self._ak = value

    @property
    def sk(self):
        return self._sk

    @sk.setter
    def sk(self, value: str):
        if not value:
            raise ValueError("sk cannot be None or empty")
        self._sk = value

    @property
    def idp_id(self):
        return self._idp_id

    @idp_id.setter
    def idp_id(self, value: str):
        self._idp_id = value

    @property
    def id_token_file(self):
        return self._id_token_file

    @id_token_file.setter
    def id_token_file(self, value: str):
        self._id_token_file = value

    @property
    def iam_endpoint(self):
        return self._iam_endpoint

    @iam_endpoint.setter
    def iam_endpoint(self, value: str):
        self._iam_endpoint = value

    @property
    def security_token(self):
        return self._security_token

    @security_token.setter
    def security_token(self, value: str):
        self._security_token = value

    @property
    def sts_accessor(self):
        return self._sts_accessor

    @sts_accessor.setter
    def sts_accessor(self, value):
        self._sts_accessor = value

    def with_ak(self, ak: str):
        self.ak = ak
        return self

    def with_sk(self, sk: str):
        self.sk = sk
        return self

    def with_idp_id(self, idp_id: str):
        self.idp_id = idp_id
        return self

    def with_id_token_file(self, id_token_file: str):
        self.id_token_file = id_token_file
        return self

    def with_iam_endpoint(self, endpoint: str):
        self.iam_endpoint = endpoint
        return self

    def with_security_token(self, token: str):
        self.security_token = token
        return self

    def get_update_path_params(self) -> Dict[str, Any]:
        pass

    def process_auth_params(self, http_client: HttpClient, region_id: str):
        pass

    def process_auth_request(self, request: SdkRequest, http_client: HttpClient):
        self.process_sts(http_client)

        return http_client.executor.submit(self.sign_request, request)

    def process_sts(self, http_client: Optional[HttpClient]):
        self._once.do(self._process_accessor)

        if self._need_refresh_sts():
            iam_endpoint = self.iam_endpoint or IamHelper.get_iam_endpoint()
            credential = self.sts_accessor.get_credential(
                iam_endpoint=iam_endpoint,
                http_client=http_client,
                idp_id=self.idp_id,
                id_token_file=self.id_token_file
            )

            self.ak = credential.access
            self.sk = credential.secret
            self.security_token = credential.security_token
            self._expire_at = credential.expire_at

    def _process_accessor(self):
        if self.sts_accessor:
            return

        if self.idp_id and self.id_token_file:
            self.sts_accessor = FederalAccessor()
        elif not self.ak and not self.sk:
            self.sts_accessor = MetadataAccessor()

    def _need_refresh_sts(self) -> bool:
        return self.sts_accessor and self._is_expired()

    def _is_expired(self) -> bool:
        return self._expire_at - time_utils.get_timestamp_utc() < self._DEFAULT_EXPIRATION_THRESHOLD_SECONDS

    def sign_request(self, request: SdkRequest) -> SdkRequest:
        if self.security_token is not None:
            request.header_params["X-Security-Token"] = self.security_token

        if self._AUTHORIZATION in request.header_params:
            Signer.process_request_uri(request)
            return request

        if self._is_derived_auth(request):
            return DerivationAKSKSigner(self).sign(request, self._derived_auth_service_name, self._region_id)

        signer_cls = self._SIGNER_CASE.get(request.signing_algorithm)
        if not signer_cls:
            raise SdkException("unsupported signing algorithm: " + str(request.signing_algorithm))
        return signer_cls(self).sign(request)

    def _is_derived_auth(self, request: SdkRequest) -> bool:
        if not self._derived_predicate:
            return False

        return self._derived_predicate(request)

    def with_derived_predicate(self, derived_predicate: Callable[[SdkRequest], bool]):
        self._derived_predicate = derived_predicate
        return self

    def _process_derived_auth_params(self, derived_auth_service_name: str, region_id: str):
        pass

    def _check_required_idp_params(self):
        if self.idp_id or self.id_token_file:
            if not self.idp_id:
                raise ApiValueError("idp_id is required when using idp_id & id_token_file")
            elif not self.id_token_file:
                raise ApiValueError("id_token_file is required when using idp_id & id_token_file")


class BasicCredentials(Credentials):
    _X_PROJECT_ID = "X-Project-Id"

    def __init__(self, ak: str = None, sk: str = None, project_id: str = None):
        """For regional services' authentication

        :param ak: The access key ID for your account
        :param sk: The secret access key for your account
        :param project_id: The ID of your project depending on your region which you want to operate
        """
        super().__init__(ak, sk)
        self._project_id = project_id

    @property
    def project_id(self) -> Optional[str]:
        return self._project_id

    @project_id.setter
    def project_id(self, value: str):
        self._project_id = value

    def with_project_id(self, project_id: str):
        self.project_id = project_id
        return self

    def get_update_path_params(self) -> Dict[str, Any]:
        path_params = {}
        if self.project_id:
            path_params["project_id"] = self.project_id
        return path_params

    def _process_derived_auth_params(self, derived_auth_service_name: str, region_id: str):
        if not self._derived_auth_service_name:
            self._derived_auth_service_name = derived_auth_service_name

        if not self._region_id:
            self._region_id = region_id

    def process_auth_params(self, http_client: HttpClient, region_id: str):
        self._check_required_idp_params()

        if self.project_id:
            return self

        cache_name = None
        if self.ak:
            cache_name = self.ak + region_id
        elif self.idp_id:
            cache_name = self.idp_id + region_id

        project_id = self._CACHE.get(cache_name)
        if project_id:
            self.project_id = project_id
            return self

        derived_predicate = self._derived_predicate
        self._derived_predicate = None

        if self.iam_endpoint is None:
            self.iam_endpoint = IamHelper.get_iam_endpoint(region_id)
        req = IamHelper.get_keystone_list_projects_request(http_client.config, self.iam_endpoint, region_id=region_id)
        try:
            http_client.logger.info("project id of region '%s' not found in BasicCredentials, "
                                    "trying to get project id from IAM service: %s",
                                    region_id, self.iam_endpoint)
            response = http_client.do_request_sync(self.process_auth_request(req, http_client).result())
            trace_id = response.headers.get("X-IAM-Trace-Id")
            data = json.loads(response.content)
            projects = data.get("projects")
            if not projects:
                raise SdkException(
                    f"Failed to get project id of region '{region_id}', X-IAM-Trace-Id={trace_id}. "
                    "Confirm that the project exists in your account, "
                    "or set project id manually: BasicCredentials(ak, sk, project_id)"
                )
            elif len(projects) > 1:
                project_ids = ",".join(map(lambda project: project["id"], projects))
                raise SdkException(f"Multiple project ids found: [{project_ids}], X-IAM-Trace-Id={trace_id}. "
                                   "Please select one when initializing the credentials: "
                                   "BasicCredentials(ak, sk, project_id)")

            self.project_id = projects[0]["id"]
            http_client.logger.info("success to get project id of region '%s': %s",
                                    region_id, string_utils.mask(self.project_id))
            if cache_name:
                with self._LOCK:
                    self._CACHE[cache_name] = self.project_id
        except ServiceResponseException as e:
            raise SdkException(f"Failed to get project id of region '{region_id}', {e}")
        self._derived_predicate = derived_predicate

        return self

    def sign_request(self, request: SdkRequest) -> SdkRequest:
        if self.project_id:
            request.header_params[self._X_PROJECT_ID] = self.project_id
        return super().sign_request(request)


class GlobalCredentials(Credentials):
    _X_DOMAIN_ID = "X-Domain-Id"

    def __init__(self, ak: str = None, sk: str = None, domain_id: str = None):
        """For global services' authentication

        :param ak: The access key ID for your account
        :param sk: The secret access key for your account
        :param domain_id: The account ID of Huawei Cloud
        """
        super().__init__(ak, sk)
        self._domain_id = domain_id

    @property
    def domain_id(self) -> Optional[str]:
        return self._domain_id

    @domain_id.setter
    def domain_id(self, value: str):
        self._domain_id = value

    def with_domain_id(self, domain_id: str):
        self.domain_id = domain_id
        return self

    def get_update_path_params(self) -> Dict[str, Any]:
        path_params = {}
        if self.domain_id:
            path_params["domain_id"] = self.domain_id
        return path_params

    def process_auth_params(self, http_client: HttpClient, region_id: str):
        self._check_required_idp_params()

        if self.domain_id:
            return self

        cache_name = None
        if self.ak:
            cache_name = self.ak
        elif self.idp_id:
            cache_name = self.idp_id

        domain_id = self._CACHE.get(cache_name)
        if domain_id:
            self.domain_id = domain_id
            return self

        derived_predicate = self._derived_predicate
        self._derived_predicate = None

        self.domain_id = self.__auto_get_domain_id(http_client, region_id)

        if cache_name:
            with self._LOCK:
                self._CACHE[cache_name] = self.domain_id

        self._derived_predicate = derived_predicate

        return self

    def sign_request(self, request: SdkRequest) -> SdkRequest:
        if self.domain_id:
            request.header_params[self._X_DOMAIN_ID] = self.domain_id
        return super().sign_request(request)

    def _process_derived_auth_params(self, derived_auth_service_name: str, region_id: str):
        if not self._derived_auth_service_name:
            self._derived_auth_service_name = derived_auth_service_name

        if not self._region_id:
            self._region_id = "globe"

    def __auto_get_domain_id(self, http_client: HttpClient, region_id: str):
        failed_msg_prefix = "Failed to get domain id, "
        iam_endpoint = self.iam_endpoint or IamHelper.get_iam_endpoint(region_id)
        req = IamHelper.get_keystone_list_auth_domains_request(http_client.config, iam_endpoint)
        http_client.logger.info('domain id not found in GlobalCredentials, '
                                'trying to get domain id from %s', iam_endpoint)
        try:
            response = http_client.do_request_sync(self.process_auth_request(req, http_client).result())
        except ServiceResponseException as e:
            raise SdkException(failed_msg_prefix + str(e))
        trace_id = response.headers.get("X-IAM-Trace-Id")
        data = json.loads(response.content)
        domains = data.get("domains")
        if domains:
            domain_id = domains[0]["id"]
            http_client.logger.info('success to get domain id: %s', string_utils.mask(domain_id))
            return domain_id

        sts_endpoint = StsHelper.get_sts_endpoint(region_id)
        if not sts_endpoint:
            raise SdkException(f"{failed_msg_prefix}X-IAM-Trace-Id={trace_id}. " +
                               "Please confirm that you have 'iam:users:getUser' permission, "
                               "or set domain id: GlobalCredentials(ak, sk, domain_id)")

        req = StsHelper.get_caller_identity_request(http_client.config, sts_endpoint)
        http_client.logger.info("domains is empty, trying to get domain id from %s", sts_endpoint)
        try:
            response = http_client.do_request_sync(self.process_auth_request(req, http_client).result())
        except HostUnreachableException as hostException:
            raise SdkException(failed_msg_prefix + str(hostException))
        except ServiceResponseException as se:
            raise SdkException(failed_msg_prefix +
                               (f"{se.status_code}, requestId: {se.request_id}" if se.status_code == 404 else str(se)))

        data = json.loads(response.content)
        domain_id = data.get("account_id")
        if not domain_id:
            raise SdkException(f"{failed_msg_prefix}account_id not found")
        http_client.logger.info('success to get domain id: %s', string_utils.mask(domain_id))
        return domain_id
