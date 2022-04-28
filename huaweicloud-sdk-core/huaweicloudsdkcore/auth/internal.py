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

import json
import six
from huaweicloudsdkcore.exceptions.exceptions import ApiValueError, ServiceResponseException
from huaweicloudsdkcore.sdk_request import SdkRequest
from six.moves.urllib.parse import urlparse


class Metadata(object):
    TIME_OUT = 3
    HOST = "169.254.169.254"
    ERR_MSG = "Unable to get temporary credential."
    SCHEMA = "http"
    METHOD = "GET"
    PATH = "/openstack/latest/securitykey"

    @classmethod
    def get_temporary_credential_from_metadata_request(cls):
        return SdkRequest(method="GET", schema=cls.SCHEMA, host=cls.HOST, resource_path="",
                          header_params={}, query_params={}, body="", uri=cls.PATH)

    @classmethod
    def get_temporary_credential(cls, http_client):
        time_out = http_client._timeout
        proxy = http_client._proxy

        http_client._proxy = None
        http_client._timeout = cls.TIME_OUT

        try:
            request = cls.get_temporary_credential_from_metadata_request()
            http_response = http_client.do_request_sync(request)
        except ServiceResponseException as e:
            raise e

        http_client._timeout = time_out
        http_client._proxy = proxy

        credential = json.loads(six.ensure_str(http_response.content)).get("credential")
        return credential


class Iam(object):
    DEFAULT_ENDPOINT = "https://iam.myhuaweicloud.com"
    KEYSTONE_LIST_PROJECT_URI = "/v3/projects"
    KEYSTONE_LIST_AUTH_DOMAINS_URI = "/v3/auth/domains"

    @classmethod
    def get_keystone_list_projects_request(cls, iam_endpoint=None, region_id=None):
        url_parse_result = urlparse(iam_endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc
        resource_path = cls.KEYSTONE_LIST_PROJECT_URI
        query_params = [('name', region_id)]

        sdk_request = SdkRequest(method="GET", schema=schema, host=host, resource_path=resource_path, header_params={},
                                 query_params=query_params, body="")

        return sdk_request

    @classmethod
    def keystone_list_projects(cls, http_client, request):
        try:
            http_response = http_client.do_request_sync(request)
        except ServiceResponseException as e:
            raise e
        if http_response and hasattr(http_response, "content"):
            content = getattr(http_response, "content")
            response = json.loads(six.ensure_str(content))
            if "projects" in response and len(response["projects"]) == 1:
                return response["projects"][0]["id"]
            elif "projects" in response and len(response["projects"]) > 1:
                raise ApiValueError("Multiple project ids have been returned, \
                     please specify one when initializing the credentials.")
            else:
                raise ApiValueError("No project id found, "
                                    "please specify project_id manually when initializing the credentials.")
        else:
            raise ApiValueError("No project id found, "
                                "please specify project_id manually when initializing the credentials.")

    @classmethod
    def get_keystone_list_auth_domains_request(cls, iam_endpoint=None):
        url_parse_result = urlparse(iam_endpoint)
        schema = url_parse_result.scheme
        host = url_parse_result.netloc
        resource_path = cls.KEYSTONE_LIST_AUTH_DOMAINS_URI

        sdk_request = SdkRequest(method="GET", schema=schema, host=host, resource_path=resource_path, header_params={},
                                 query_params=[], body="")

        return sdk_request

    @classmethod
    def keystone_list_auth_domains(cls, http_client, request):
        try:
            http_response = http_client.do_request_sync(request)
        except ServiceResponseException as e:
            raise e
        if http_response and hasattr(http_response, "content"):
            content = getattr(http_response, "content")
            response = json.loads(six.ensure_str(content))
            if "domains" in response and len(response["domains"]) == 1:
                return response["domains"][0]["id"]
            else:
                raise ApiValueError("No domain id found, please select one of the following solutions:\n\t"
                                    "1. Manually specify domain_id when initializing the credentials.\n\t"
                                    "2. Use the domain account to grant the current account permissions "
                                    "of the IAM service.\n\t"
                                    "3. Use AK/SK of the domain account.")
        else:
            raise ApiValueError("No domain id found, please select one of the following solutions:\n\t"
                                "1. Manually specify domain_id when initializing the credentials.\n\t"
                                "2. Use the domain account to grant the current account permissions of the IAM "
                                "service.\n\t "
                                "3. Use AK/SK of the domain account.")
