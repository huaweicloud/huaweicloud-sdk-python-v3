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

import requests
from requests.exceptions import HTTPError
from six.moves.urllib.parse import urlparse
from urllib3.exceptions import SSLError, NewConnectionError

from huaweicloudsdkcore.utils.six_utils import JSON_DECODE_ERROR
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.sdk_request import SdkRequest

_NO_DOMAIN_ID_ERR_MSG = '''no domain id found, please select one of the following solutions:
  1. Manually specify domain_id when initializing the credentials, credentials = GlobalCredentials(ak, sk, domain_id)
  2. Use the domain account to grant IAM read permission to the current account
  3. Replace the ak/sk of the IAM account with the ak/sk of the domain account'''

_NO_PROJECT_ID_ERR_MSG = '''no project id found, please select one of the following solutions:
  1. Manually specify project_id when initializing the credentials, credentials = BasicCredentials(ak, sk, project_id)
  2. Use the domain account to grant IAM read permission to the current account
  3. Replace the ak/sk of the IAM account with the ak/sk of the domain account'''


class Metadata(object):
    TIME_OUT = 3
    URL = "http://169.254.169.254/openstack/latest/securitykey"

    @classmethod
    def get_credential_from_metadata(cls):
        resp = None
        try:
            resp = requests.get(cls.URL, timeout=cls.TIME_OUT)
            resp.raise_for_status()
        except ConnectionError as conn_err:
            for each in conn_err.args:
                if isinstance(each.reason, SSLError):
                    raise exceptions.SslHandShakeException(str(each.reason))
                if isinstance(each.reason, NewConnectionError):
                    raise exceptions.ConnectionException(str(each.reason))
        except HTTPError as http_err:
            sdk_error = exceptions.SdkError("", http_err.response.status_code, http_err.response.text)
            raise exceptions.ClientRequestException(http_err.response.status_code, sdk_error)

        if not resp or not resp.content:
            raise exceptions.ApiValueError("failed to get credential from metadata, metadata is empty")

        try:
            credential = json.loads(resp.content).get("credential")
            return credential
        except JSON_DECODE_ERROR as decode_err:
            raise exceptions.ApiValueError("failed to get credential from metadata: {}".format(decode_err))


class Iam(object):
    DEFAULT_ENDPOINT = "https://iam.myhuaweicloud.com"
    KEYSTONE_LIST_PROJECT_URI = "/v3/projects"
    KEYSTONE_LIST_AUTH_DOMAINS_URI = "/v3/auth/domains"
    CREATE_TOKEN_BY_ID_TOKEN_URI = "/v3.0/OS-AUTH/id-token/tokens"
    IAM_ENDPOINT_ENV_NAME = "HUAWEICLOUD_SDK_IAM_ENDPOINT"

    @classmethod
    def get_iam_endpoint(cls):
        return os.environ.get(cls.IAM_ENDPOINT_ENV_NAME, cls.DEFAULT_ENDPOINT)

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
            raise exceptions.ApiValueError("failed to get token by id_token")

        token = resp.headers.get("X-Subject-Token")
        expired_str = json.loads(resp.content).get("token").get("expires_at")
        return token, expired_str

    @classmethod
    def keystone_list_projects(cls, http_client, request):
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
