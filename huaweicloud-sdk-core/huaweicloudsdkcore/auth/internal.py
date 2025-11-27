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
from typing import Dict, Optional

import requests
from six.moves.urllib.parse import urlparse

from huaweicloudsdkcore.auth import endpoint
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.http.user_agent import user_agent_string
from huaweicloudsdkcore.sdk_request import SdkRequest


class MetadataAccessor:
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

    def _get_token(self) -> requests.Response:
        url = self.METADATA_ENDPOINT + self.GET_TOKEN_PATH
        headers = {self.X_METADATA_TOKEN_TTL_SECONDS: str(self.DEFAULT_TOKEN_TTL_SECONDS)}
        return requests.put(url=url, headers=headers, timeout=self.DEFAULT_TIME_OUT)

    def _try_update_token(self, raise_on_failure: bool):
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

    def get_credentials(self) -> Dict[str, str]:
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


class StsHelper:
    STS_ENDPOINT_ENV_NAME = "HUAWEICLOUD_SDK_STS_ENDPOINT"
    GET_CALLER_IDENTITY_URI = "/v5/caller-identity"

    @classmethod
    def get_sts_endpoint(cls, region_id: str = None) -> Optional[str]:
        return os.getenv(cls.STS_ENDPOINT_ENV_NAME) or endpoint.get_sts_endpoint_by_id(region_id)

    @classmethod
    def get_caller_identity_request(cls, config: HttpConfig, sts_endpoint: str) -> SdkRequest:
        url_parse_result = urlparse(sts_endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc
        resource_path = cls.GET_CALLER_IDENTITY_URI
        return SdkRequest(
            method="GET",
            schema=schema,
            host=host,
            resource_path=resource_path,
            header_params={"User-Agent": user_agent_string},
            query_params=[],
            signing_algorithm=config.signing_algorithm
        )


class IamHelper:
    DEFAULT_ENDPOINT = "https://iam.myhuaweicloud.com"
    KEYSTONE_LIST_PROJECT_URI = "/v3/projects"
    KEYSTONE_LIST_AUTH_DOMAINS_URI = "/v3/auth/domains"
    CREATE_TOKEN_BY_ID_TOKEN_URI = "/v3.0/OS-AUTH/id-token/tokens"
    CREATE_TEMPORARY_ACCESS_KEY_BY_TOKEN_URI = "/v3.0/OS-CREDENTIAL/securitytokens"
    IAM_ENDPOINT_ENV_NAME = "HUAWEICLOUD_SDK_IAM_ENDPOINT"

    @classmethod
    def get_iam_endpoint(cls, region_id: str = None) -> str:
        env = os.getenv(cls.IAM_ENDPOINT_ENV_NAME)
        if env:
            return env

        return endpoint.get_iam_endpoint_by_id(region_id, cls.DEFAULT_ENDPOINT)

    @classmethod
    def get_keystone_list_projects_request(cls, config: HttpConfig, iam_endpoint: str, region_id: str) -> SdkRequest:
        url_parse_result = urlparse(iam_endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc
        resource_path = cls.KEYSTONE_LIST_PROJECT_URI
        query_params = [('name', region_id)]

        return SdkRequest(
            method="GET",
            schema=schema,
            host=host,
            resource_path=resource_path,
            header_params={"User-Agent": user_agent_string},
            query_params=query_params,
            body="",
            signing_algorithm=config.signing_algorithm
        )

    @classmethod
    def get_create_temporary_access_key_by_token_request(cls, config: HttpConfig, iam_endpoint: str, auth_token: str,
                                                         duration_seconds: int) -> SdkRequest:
        request_body = {
            "auth": {
                "identity": {
                    "methods": [
                        "token"
                    ],
                    "token": {
                        "id": auth_token,
                        "duration_seconds": duration_seconds
                    }
                }
            }
        }
        url_parse_result = urlparse(iam_endpoint)
        header_params = {"Content-Type": "application/json;charset=UTF-8", "User-Agent": user_agent_string}
        return SdkRequest(
            method="POST",
            schema=url_parse_result.scheme,
            host=url_parse_result.netloc,
            resource_path=cls.CREATE_TEMPORARY_ACCESS_KEY_BY_TOKEN_URI,
            uri=cls.CREATE_TEMPORARY_ACCESS_KEY_BY_TOKEN_URI,
            header_params=header_params,
            query_params=[],
            body=json.dumps(request_body),
            stream=False,
            signing_algorithm=config.signing_algorithm
        )

    @staticmethod
    def create_temporary_access_key_by_token(http_client: HttpClient, request) -> Dict[str, str]:
        resp = http_client.do_request_sync(request)
        if not resp or not resp.content:
            raise exceptions.ApiValueError("Failed to get temporary credential")

        return json.loads(resp.content).get("credential")

    @classmethod
    def get_create_unscoped_token_by_id_token_request(cls, config: HttpConfig, iam_endpoint: str, idp_id: str,
                                                      id_token: str) -> SdkRequest:
        request_body = {
            "auth": {
                "id_token": {
                    "id": id_token
                }
            }
        }
        url_parse_result = urlparse(iam_endpoint)
        header_params = {"X-Idp-Id": idp_id,
                         "Content-Type": "application/json;charset=UTF-8", "User-Agent": user_agent_string}
        return SdkRequest(
            method="POST",
            schema=url_parse_result.scheme,
            host=url_parse_result.netloc,
            resource_path=cls.CREATE_TOKEN_BY_ID_TOKEN_URI,
            uri=cls.CREATE_TOKEN_BY_ID_TOKEN_URI,
            header_params=header_params,
            query_params=[],
            body=json.dumps(request_body),
            stream=False,
            signing_algorithm=config.signing_algorithm
        )

    @staticmethod
    def create_unscoped_token_by_id_token(http_client: HttpClient, request: SdkRequest) -> str:
        resp = http_client.do_request_sync(request)
        if not resp or not resp.content or "X-Subject-Token" not in resp.headers:
            raise exceptions.ApiValueError("Failed to get token by id_token")

        return resp.headers.get("X-Subject-Token")

    @classmethod
    def get_keystone_list_auth_domains_request(cls, config: HttpConfig, iam_endpoint: str) -> SdkRequest:
        url_parse_result = urlparse(iam_endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc
        resource_path = cls.KEYSTONE_LIST_AUTH_DOMAINS_URI

        return SdkRequest(
            method="GET",
            schema=schema,
            host=host,
            resource_path=resource_path,
            header_params={"User-Agent": user_agent_string},
            query_params=[],
            body="",
            signing_algorithm=config.signing_algorithm
        )
