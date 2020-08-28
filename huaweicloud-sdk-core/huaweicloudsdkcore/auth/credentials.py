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
import importlib
import inspect
import os
from concurrent.futures.thread import ThreadPoolExecutor

from huaweicloudsdkcore.exceptions.exceptions import ApiValueError
from huaweicloudsdkcore.signer import signer
from huaweicloudsdkcore.utils.string_utils import camel_to_underline


class Credentials:
    def get_update_path_params(self):
        pass

    def process_auth_request(self, request, http_client):
        pass


class BasicCredentials(Credentials):
    def __init__(self, ak, sk, project_id):
        if ak is None or ak == "":
            raise ApiValueError("AK can not be null.")

        if sk is None or sk == "":
            raise ApiValueError("SK can not be null.")

        if project_id is None or project_id == "":
            raise ApiValueError("Project ID can not be null.")

        self.ak = ak
        self.sk = sk
        self.project_id = project_id
        self.security_token = None

    def with_security_token(self, token):
        self.security_token = token
        return self

    def get_update_path_params(self):
        path_params = {}
        if self.project_id is not None:
            path_params["project_id"] = self.project_id
        return path_params

    def process_auth_request(self, request, http_client):
        executor = ThreadPoolExecutor(max_workers=8)
        future = executor.submit(self.sign_request, request)
        return future

    def sign_request(self, request):
        request.header_params["X-Project-Id"] = self.project_id
        if self.security_token is not None:
            request.header_params["X-Security-Token"] = self.security_token

        if "Content-Type" in request.header_params and not request.header_params["Content-Type"].startswith(
                "application/json"):
            request.header_params["X-Sdk-Content-Sha256"] = "UNSIGNED-PAYLOAD"

        return signer.Signer(self).sign(request)


class GlobalCredentials(Credentials):
    def __init__(self, ak, sk, domain_id):
        if ak is None or ak == "":
            raise ApiValueError("AK can not be null.")

        if sk is None or sk == "":
            raise ApiValueError("SK can not be null.")

        if domain_id is None or domain_id == "":
            raise ApiValueError("Domain ID can not be null.")

        self.ak = ak
        self.sk = sk
        self.domain_id = domain_id
        self.security_token = None

    def with_security_token(self, token):
        self.security_token = token
        return self

    def get_update_path_params(self):
        path_params = {}
        if self.domain_id is not None:
            path_params["domain_id"] = self.domain_id
        return path_params

    def process_auth_request(self, request, http_client):
        executor = ThreadPoolExecutor(max_workers=8)
        future = executor.submit(self.sign_request, request)
        return future

    def sign_request(self, request):
        request.header_params["X-Domain-Id"] = self.domain_id
        if self.security_token is not None:
            request.header_params["X-Security-Token"] = self.security_token

        if "Content-Type" in request.header_params and not request.header_params["Content-Type"].startswith(
                "application/json"):
            request.header_params["X-Sdk-Content-Sha256"] = "UNSIGNED-PAYLOAD"

        return signer.Signer(self).sign(request)


def get_credential_from_environment(client_type, default_credentials):
    credential_type = os.environ.get("HUAWEICLOUD_SDK_TYPE")
    if not credential_type:
        credential_type = default_credentials

    credentials_clazz = _get_credentials_clazz(credential_type, client_type)
    if not credentials_clazz:
        return None

    credentials = _initialize_credentials(credentials_clazz)
    credentials = _load_optional_params(credentials)

    return credentials


def _get_credentials_clazz(credential_type, client_type):
    core_credentials_module = importlib.import_module("huaweicloudsdkcore.auth.credentials")
    if hasattr(core_credentials_module, credential_type):
        return getattr(core_credentials_module, credential_type)
    else:
        credentials_clazz_name = "%s.%s" % (client_type.__module__[:client_type.__module__.rindex('.')],
                                            camel_to_underline(credential_type))
        credentials_module = importlib.import_module(credentials_clazz_name)
        if hasattr(credentials_module, credential_type):
            return getattr(credentials_module, credential_type)
    return None


def _initialize_credentials(credentials_clazz):
    args_map = {}
    init_method = getattr(credentials_clazz, "__init__")
    args = inspect.getfullargspec(init_method).args
    for each in args:
        if each != "self":
            args_map[each] = os.environ.get("HUAWEICLOUD_SDK_%s" % each.upper())
    return credentials_clazz(**args_map)


def _load_optional_params(credentials):
    for item in credentials.__dict__:
        if getattr(credentials, item) is None:
            setattr(credentials, item, os.environ.get("HUAWEICLOUD_SDK_%s" % item.strip('_').upper()))
    return credentials
