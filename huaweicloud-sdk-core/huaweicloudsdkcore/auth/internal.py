# coding: utf-8
"""
 Copyright 2022 Huawei Technologies Co.,Ltd.

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
import os
import time
import warnings

import requests
from requests.exceptions import HTTPError
from six.moves.urllib.parse import urlparse
from urllib3.exceptions import SSLError, NewConnectionError

from huaweicloudsdkcore.auth.endpoint import get_iam_endpoint_by_id
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.utils.six_utils import JSON_DECODE_ERROR

_NO_DOMAIN_ID_ERR_MSG = '''no domain id found, please select one of the following solutions:
  1. Manually specify domain_id when initializing the credentials, credentials = GlobalCredentials(ak, sk, domain_id)
  2. Use the domain account to grant IAM read permission to the current account
  3. Replace the ak/sk of the IAM account with the ak/sk of the domain account'''

_NO_PROJECT_ID_ERR_MSG = '''no project id found, please select one of the following solutions:
  1. Manually specify project_id when initializing the credentials, credentials = BasicCredentials(ak, sk, project_id)
  2. Use the domain account to grant IAM read permission to the current account
  3. Replace the ak/sk of the IAM account with the ak/sk of the domain account'''


class MetadataAccessor(object):
    METADATA_ENDPOINT = "http://169.254.169.254"
    GET_TOKEN_PATH = "/meta-data/latest/api/token"
    GET_SECURITY_KEY_PATH = "/openstack/latest/securitykey"
    X_METADATA_TOKEN = "X-Metadata-Token"
    X_METADATA_TOKEN_TTL_SECONDS = "X-Metadata-Token-Ttl-Seconds"
    CONFIG_AGENCY_ERROR = "Please configure Cloud Service Agency first"
    DEFAULT_TOKEN_TTL_SECONDS = 6 * 60 * 60  # 6h
    DEFAULT_CHECK_TOKEN_DURATION_SECONDS = 24 * 60 * 60  # 24h
    DEFAULT_TIME_OUT = (3, 3)

    def __init__(self):
        self._last_call_seconds = None
        self._token = None

    def _get_token(self):
        url = self.METADATA_ENDPOINT + self.GET_TOKEN_PATH
        headers = {self.X_METADATA_TOKEN_TTL_SECONDS: str(self.DEFAULT_TOKEN_TTL_SECONDS)}
        return requests.put(url=url, headers=headers, timeout=self.DEFAULT_TIME_OUT)

    def _try_update_token(self, raise_on_failure):
        self._last_call_seconds = time.time()
        resp = self._get_token()
        if resp.status_code == 200:
            self._token = resp.text
        elif resp.status_code in (404, 405):
            if raise_on_failure:
                sdk_error = exceptions.SdkError("", resp.status_code, resp.text)
                raise exceptions.ClientRequestException(resp.status_code, sdk_error)
            else:
                self._token = None
        else:
            sdk_error = exceptions.SdkError("", resp.status_code, resp.text)
            raise exceptions.ClientRequestException(resp.status_code, sdk_error)

    def get_credentials(self):
        if not self._token and (not self._last_call_seconds or
                                time.time() - self._last_call_seconds > self.DEFAULT_CHECK_TOKEN_DURATION_SECONDS):
            self._try_update_token(False)

        url = self.METADATA_ENDPOINT + self.GET_SECURITY_KEY_PATH
        headers = {}
        if self._token:
            headers[self.X_METADATA_TOKEN] = self._token

        resp = requests.get(url=url, headers=headers, timeout=self.DEFAULT_TIME_OUT)
        if resp.status_code == 401 and self.CONFIG_AGENCY_ERROR not in resp.text:
            self._try_update_token(True)
            headers[self.X_METADATA_TOKEN] = self._token
            resp = requests.get(url=url, headers=headers, timeout=self.DEFAULT_TIME_OUT)

        if resp.status_code >= 400:
            sdk_error = exceptions.SdkError("", resp.status_code, resp.text)
            raise exceptions.ClientRequestException(resp.status_code, sdk_error)

        return json.loads(resp.text).get("credential")


class Iam(object):
    DEFAULT_ENDPOINT = "https://iam.myhuaweicloud.com"
    KEYSTONE_LIST_PROJECT_URI = "/v3/projects"
    KEYSTONE_LIST_AUTH_DOMAINS_URI = "/v3/auth/domains"
    CREATE_TOKEN_BY_ID_TOKEN_URI = "/v3.0/OS-AUTH/id-token/tokens"
    IAM_ENDPOINT_ENV_NAME = "HUAWEICLOUD_SDK_IAM_ENDPOINT"
    __ENDPOINTS = None

    @classmethod
    def get_iam_endpoint(cls, region_id=None):
        env = os.getenv(cls.IAM_ENDPOINT_ENV_NAME)
        if env:
            return env

        return get_iam_endpoint_by_id(region_id, cls.DEFAULT_ENDPOINT)

    @classmethod
    def get_keystone_list_projects_request(cls, config, iam_endpoint=None, region_id=None):
        url_parse_result = urlparse(iam_endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc
        resource_path = cls.KEYSTONE_LIST_PROJECT_URI
        query_params = [('name', region_id)]

        sdk_request = SdkRequest(method="GET",
                                 schema=schema,
                                 host=host,
                                 resource_path=resource_path,
                                 header_params={"User-Agent": "huaweicloud-usdk-python/3.0"},
                                 query_params=query_params,
                                 body="",
                                 signing_algorithm=config.signing_algorithm)

        return sdk_request

    @staticmethod
    def get_create_token_by_id_token_request(config, iam_endpoint, idp_id, id_token, project_id=None, domain_id=None):
        scope, _id = ("project", project_id) if project_id else ("domain", domain_id)
        request_body = {
            "auth": {
                "id_token": {
                    "id": id_token
                },
                "scope": {
                    scope: {
                        "id": _id,
                    }
                }
            }
        }
        url_parse_result = urlparse(iam_endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc
        resource_path = Iam.CREATE_TOKEN_BY_ID_TOKEN_URI
        header_params = {"X-Idp-Id": idp_id,
                         "Content-Type": "application/json;charset=UTF-8", "User-Agent": "huaweicloud-usdk-python/3.0"}
        return SdkRequest(method="POST",
                          schema=schema,
                          host=host,
                          resource_path=resource_path,
                          uri=resource_path,
                          header_params=header_params,
                          query_params=[],
                          body=json.dumps(request_body),
                          stream=False,
                          signing_algorithm=config.signing_algorithm)

    @classmethod
    def create_token_by_id_token(cls, http_client, request):
        resp = http_client.do_request_sync(request)
        if not resp or not resp.content or "X-Subject-Token" not in resp.headers:
            raise exceptions.ApiValueError("Failed to get token by id_token")

        token = resp.headers.get("X-Subject-Token")
        expired_str = json.loads(resp.content).get("token").get("expires_at")
        return token, expired_str

    @classmethod
    def keystone_list_projects(cls, http_client, request):
        warnings.warn("This method is for internal use only and is deprecated. "
                      "It will be removed in a future version.", DeprecationWarning)
        try:
            http_response = http_client.do_request_sync(request)
        except exceptions.ServiceResponseException as e:
            raise e

        if not hasattr(http_response, "content"):
            raise exceptions.ApiValueError(_NO_PROJECT_ID_ERR_MSG)

        content = json.loads(http_response.content)
        projects = content.get("projects")
        if not projects:
            raise exceptions.ApiValueError("Result projects is null. " + _NO_PROJECT_ID_ERR_MSG)
        if len(projects) > 1:
            project_ids = ",".join((project.get("id") for project in projects))
            raise exceptions.ApiValueError("multiple project ids found: [%s], "
                                           "please specify one when initializing the credentials, "
                                           "credentials = BasicCredentials(ak, sk, project_id)" % project_ids)
        return projects[0]["id"]

    @classmethod
    def get_keystone_list_auth_domains_request(cls, config, iam_endpoint=None):
        url_parse_result = urlparse(iam_endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc
        resource_path = cls.KEYSTONE_LIST_AUTH_DOMAINS_URI

        sdk_request = SdkRequest(method="GET",
                                 schema=schema,
                                 host=host,
                                 resource_path=resource_path,
                                 header_params={"User-Agent": "huaweicloud-usdk-python/3.0"},
                                 query_params=[],
                                 body="",
                                 signing_algorithm=config.signing_algorithm)

        return sdk_request

    @classmethod
    def keystone_list_auth_domains(cls, http_client, request):
        warnings.warn("This method is for internal use only and is deprecated. "
                      "It will be removed in a future version.", DeprecationWarning)
        try:
            http_response = http_client.do_request_sync(request)
        except exceptions.ServiceResponseException as e:
            raise e

        if not hasattr(http_response, "content"):
            raise exceptions.ApiValueError(_NO_DOMAIN_ID_ERR_MSG)

        content = json.loads(http_response.content)
        domains = content.get("domains")
        if not domains:
            raise exceptions.ApiValueError("result domains is null. " + _NO_DOMAIN_ID_ERR_MSG)
        if len(domains) > 1:
            domain_ids = ",".join((domain.get("id") for domain in domains))
            raise exceptions.ApiValueError("multiple domain ids found: [%s], "
                                           "please specify one when initializing the credentials, "
                                           "credentials = GlobalCredentials(ak, sk, domain_id)" % domain_ids)
        return domains[0]["id"]
