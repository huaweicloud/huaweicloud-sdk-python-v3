# coding= utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http=//www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""
import importlib

import pytest
from requests import Response, Request

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions.exceptions import ClientRequestException, ServerResponseException
from huaweicloudsdkcore.http.http_config import HttpConfig
from tests.model.vpc import ListVpcsResponse


@pytest.fixture()
def client():
    ak = "AccessKey"
    sk = "SecretKey"
    project_id = "ProjectId"
    endpoint = "https://vpc.cn-north-x.myhuaweicloud.com"

    config = HttpConfig.get_default_config()
    config.ignore_ssl_verification = True
    credentials = BasicCredentials(ak, sk, project_id)

    client = ClientBuilder(Client) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    yield client


@pytest.fixture()
def client_err_response():
    client_err_response = Response()
    client_err_response.status_code = 400
    client_err_response.reason = "mock client error response"
    client_err_response.url = ""
    client_err_response._content = b"""
            {
                "error_code":"ERR.CLIENT_ERR",
                "error_msg":"request-client-error-001"
            }
        """
    client_err_response.headers = {"X-Request-Id": "request-client-error-001"}
    client_err_response.request = Request()
    client_err_response.request.method = "GET"
    client_err_response.request.url = ""

    yield client_err_response


@pytest.fixture()
def client_err_response_type2():
    client_err_response_type2 = Response()
    client_err_response_type2.status_code = 400
    client_err_response_type2.reason = "mock client error response"
    client_err_response_type2.url = ""
    client_err_response_type2._content = b"request-client-error-002"
    client_err_response_type2.headers = {"X-Request-Id": "request-client-error-002"}
    client_err_response_type2.request = Request()
    client_err_response_type2.request.method = "GET"
    client_err_response_type2.request.url = ""

    yield client_err_response_type2


@pytest.fixture()
def server_err_response():
    server_err_response = Response()
    server_err_response.status_code = 500
    server_err_response.reason = "mock server error response"
    server_err_response.url = ""
    server_err_response._content = b"""
            {
                "code":"ERR.SERVER_ERR",
                "message":"request-server-error-001"
            }
        """
    server_err_response.headers = {"X-Request-Id": "request-server-error-001"}
    server_err_response.request = Request()
    server_err_response.request.method = "GET"
    server_err_response.request.url = ""

    yield server_err_response


@pytest.fixture()
def server_err_response_type2():
    server_err_response_type2 = Response()
    server_err_response_type2.status_code = 500
    server_err_response_type2.reason = "mock server error response"
    server_err_response_type2.url = ""
    server_err_response_type2._content = b"""
        {
            "xxx":{
                "code":"ERR.SERVER_ERR",
                "message":"request-server-error-002"
            }
        }
        """
    server_err_response_type2.headers = {"X-Request-Id": "request-server-error-002"}
    server_err_response_type2.request = Request()
    server_err_response_type2.request.method = "GET"
    server_err_response_type2.request.url = ""

    yield server_err_response_type2


@pytest.fixture()
def list_vpc_response():
    list_vpc_response = Response()
    list_vpc_response.status_code = 200
    list_vpc_response._content = b"""
        {
            "vpcs": [
                {
                    "id": "0378f905-2ae8-4c75-a9fe-575ec11fddc9",
                    "name": "Hello123556WorldVpc",
                    "description": "",
                    "cidr": "192.168.1.0/24",
                    "status": "OK",
                    "routes": [],
                    "enterprise_project_id": "0"
                },
                {
                    "id": "27349a49-a1b8-48fc-aed5-30d183c6844b",
                    "name": "HelloWorld123Vpc",
                    "description": "6Pjkx7B0Yze81L",
                    "cidr": "192.168.1.0/24",
                    "status": "OK",
                    "routes": [],
                    "enterprise_project_id": "0"
                }
            ]
        }
        """
    list_vpc_response.headers = {"X-Request-Id": "list-vpcs-request"}
    list_vpc_response.request = Request()
    list_vpc_response.request.method = "GET"
    list_vpc_response.request.url = ""

    yield list_vpc_response


def test_client_request_exception(client, client_err_response):
    with pytest.raises(ClientRequestException) as e:
        client.get_http_client().response_error_hook_factory()(client_err_response)

    assert e.value.request_id == "request-client-error-001"
    assert e.value.error_code == "ERR.CLIENT_ERR"
    assert e.value.error_msg == "request-client-error-001"


def test_client_request_exception2(client, client_err_response_type2):
    with pytest.raises(ClientRequestException) as e:
        client.get_http_client().response_error_hook_factory()(client_err_response_type2)

    assert e.value.error_msg == "request-client-error-002"


def test_server_response_exception(client, server_err_response):
    with pytest.raises(ServerResponseException) as e:
        client.get_http_client().response_error_hook_factory()(server_err_response)

    assert e.value.request_id == "request-server-error-001"
    assert e.value.error_code == "ERR.SERVER_ERR"
    assert e.value.error_msg == "request-server-error-001"


def test_server_response_exception2(client, server_err_response_type2):
    with pytest.raises(ServerResponseException) as e:
        client.get_http_client().response_error_hook_factory()(server_err_response_type2)

    assert e.value.request_id == "request-server-error-002"
    assert e.value.error_code == "ERR.SERVER_ERR"
    assert e.value.error_msg == "request-server-error-002"


def test_response_deserialization(client, list_vpc_response):
    client.model_package = importlib.import_module("tests.model.vpc")
    response = client.sync_response_handler(list_vpc_response, "ListVpcsResponse", None, None)

    assert isinstance(response, ListVpcsResponse)
    assert len(response.vpcs) == 2
    assert response.vpcs[0].id == "0378f905-2ae8-4c75-a9fe-575ec11fddc9"


if __name__ == "__main__":
    pytest.main()
