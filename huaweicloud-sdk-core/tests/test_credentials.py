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
import logging

import pytest
import requests
import responses
from urllib3.exceptions import NewConnectionError

from huaweicloudsdkcore.auth import endpoint
from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.exceptions.exception_handler import DefaultExceptionHandler
from huaweicloudsdkcore.exceptions.exceptions import SdkException
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.http.http_handler import HttpHandler
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer.algorithm import SigningAlgorithm
from tests.util.response_registry import OrderedRegistry


@pytest.fixture
def sdk_request():
    yield SdkRequest(schema="https", host="service.region-1.com", resource_path="/test",
                     header_params={}, query_params=[], signing_algorithm=SigningAlgorithm.get_default())


@pytest.fixture
def mocked_empty_domain_responses():
    with responses.RequestsMock(registry=OrderedRegistry) as resps:
        resps.add(
            method=responses.GET,
            url="https://iam.myhuaweicloud.com/v3/auth/domains",
            content_type="application/json",
            headers={"X-IAM-Trace-Id": "trace-id"},
            body="{\"domains\":[]}"
        )
        yield resps
        resps.reset()


@pytest.fixture()
def mock_sts_endpoint(monkeypatch):
    monkeypatch.setattr(endpoint, "get_sts_endpoint_by_id", lambda x: "https://localhost")


@pytest.fixture
def mocked_http_client():
    http_client = HttpClient(HttpConfig.get_default_config(), HttpHandler(), DefaultExceptionHandler(),
                             logging.getLogger("test"))
    yield http_client
    http_client.close()


def test_basic_credentials_sign_with_auth_token(sdk_request):
    credentials = BasicCredentials()
    setattr(credentials, "_auth_token", "token")
    result = credentials.sign_request(sdk_request)
    assert result.header_params.get("X-Auth-Token") == "token"


def test_basic_credentials_sign_with_perm_aksk(sdk_request):
    credentials = BasicCredentials("ak", "sk")
    result = credentials.sign_request(sdk_request)
    assert "Authorization" in result.header_params


def test_basic_credentials_sign_with_temp_aksk(sdk_request):
    credentials = BasicCredentials("ak", "sk")
    credentials.security_token = "token"
    result = credentials.sign_request(sdk_request)
    assert result.header_params.get("X-Security-Token") == "token"
    assert "Authorization" in result.header_params


def test_global_credentials_sign_with_auth_token(sdk_request):
    credentials = GlobalCredentials()
    setattr(credentials, "_auth_token", "token")
    result = credentials.sign_request(sdk_request)
    assert result.header_params.get("X-Auth-Token") == "token"


def test_global_credentials_sign_with_perm_aksk(sdk_request):
    credentials = GlobalCredentials("ak", "sk")
    result = credentials.sign_request(sdk_request)
    assert "Authorization" in result.header_params


def test_global_credentials_sign_with_temp_aksk(sdk_request):
    credentials = GlobalCredentials("ak", "sk")
    credentials.security_token = "token"
    result = credentials.sign_request(sdk_request)
    assert result.header_params.get("X-Security-Token") == "token"
    assert "Authorization" in result.header_params


@responses.activate
def test_auto_get_project_id(mocked_http_client):
    responses.add(
        method=responses.GET,
        url="https://iam.myhuaweicloud.com/v3/projects",
        content_type="application/json",
        headers={"X-IAM-Trace-Id": "trace-id"},
        body="{\"projects\":[{\"id\":\"project_id\"}]}"
    )

    credentials = BasicCredentials("ak", "sk")
    credentials.process_auth_params(mocked_http_client, "region-id-1")
    assert "project_id" == credentials.project_id


@responses.activate
def test_empty_project_id(mocked_http_client):
    responses.add(
        method=responses.GET,
        url="https://iam.myhuaweicloud.com/v3/projects",
        content_type="application/json",
        headers={"X-IAM-Trace-Id": "trace-id"},
        body="{\"projects\":[]}"
    )

    credentials = BasicCredentials("ak", "sk")
    try:
        credentials.process_auth_params(mocked_http_client, "region-id-2")
        raise AssertionError("Should have thrown a SdkException: Failed to get project id...")
    except SdkException as e:
        assert ("Failed to get project id of region 'region-id-2', X-IAM-Trace-Id=trace-id. "
                "Confirm that the project exists in your account, "
                "or set project id manually: BasicCredentials(ak, sk, project_id)") == e.error_msg


@responses.activate
def test_multiple_project_ids(mocked_http_client):
    responses.add(
        method=responses.GET,
        url="https://iam.myhuaweicloud.com/v3/projects",
        content_type="application/json",
        headers={"X-IAM-Trace-Id": "trace-id"},
        body="{\"projects\":[{\"id\":\"project_id1\"},{\"id\":\"project_id2\"}]}"
    )

    credentials = BasicCredentials("ak", "sk")
    try:
        credentials.process_auth_params(mocked_http_client, "region-id-3")
        raise AssertionError("Should have thrown a SdkException: multiple project ids found...")
    except SdkException as e:
        assert ('Multiple project ids found: [project_id1,project_id2], X-IAM-Trace-Id=trace-id. '
                'Please select one when initializing the credentials: '
                'BasicCredentials(ak, sk, project_id)') == e.error_msg


@responses.activate
def test_auto_get_domain_id(mocked_http_client):
    responses.add(
        method=responses.GET,
        url="https://iam.myhuaweicloud.com/v3/auth/domains",
        content_type="application/json",
        headers={"X-IAM-Trace-Id": "trace-id"},
        body="{\"domains\":[{\"id\":\"domain_id\"}]}"
    )

    credentials = GlobalCredentials("ak", "sk")
    credentials.process_auth_params(mocked_http_client, "region-id")
    assert "domain_id" == credentials.domain_id


def test_empty_domain_id(mocked_http_client, mocked_empty_domain_responses):
    credentials = GlobalCredentials("ak2", "sk2")
    try:
        credentials.process_auth_params(mocked_http_client, "region-id")
        raise AssertionError("Should have thrown a SdkException: Failed to get domain id...")
    except SdkException as e:
        assert ("Failed to get domain id, X-IAM-Trace-Id=trace-id. "
                "Please confirm that you have 'iam:users:getUser' permission, "
                "or set domain id: GlobalCredentials(ak, sk, domain_id)") == e.error_msg


def test_get_domain_id_v5(mock_sts_endpoint, mocked_http_client, mocked_empty_domain_responses):
    mocked_empty_domain_responses.add(
        method=responses.GET,
        url="https://localhost/v5/caller-identity",
        content_type="application/json",
        headers={"x-request-id": "request-id"},
        body='{"account_id": "domain_id"}'
    )

    credentials = GlobalCredentials("ak", "sk")
    credentials.process_auth_params(mocked_http_client, "region-id")
    assert "domain_id" == credentials.domain_id


def test_get_domain_id_v5_unknown_host(mock_sts_endpoint, mocked_http_client, mocked_empty_domain_responses):
    class MockException(Exception):
        def __init__(self, reason):
            self.reason = reason

        def __str__(self):
            return "Name or service not known"

    mocked_empty_domain_responses.add(
        method=responses.GET,
        url="https://localhost/v5/caller-identity",
        body=requests.exceptions.ConnectionError(
            MockException(NewConnectionError(None, "Name or service not known")))
    )

    credentials = GlobalCredentials("ak", "sk")
    try:
        credentials.process_auth_params(mocked_http_client, "region-id")
    except SdkException as e:
        assert "Failed to get domain id automatically" in e.error_msg
        assert "Name or service not known" in e.error_msg


def test_get_domain_id_v5_status_404(mock_sts_endpoint, mocked_http_client, mocked_empty_domain_responses):
    mocked_empty_domain_responses.add(
        method=responses.GET,
        url="https://localhost/v5/caller-identity",
        content_type="application/json",
        headers={"x-request-id": "request-id"},
        body='{"error_code": "xxx", "error_msg": "not found"}',
        status=404
    )

    credentials = GlobalCredentials("ak", "sk")
    try:
        credentials.process_auth_params(mocked_http_client, "region-id")
    except SdkException as e:
        assert e.error_msg == "Failed to get domain id automatically, 404, requestId: request-id"


def test_get_domain_id_v5_status_500(mock_sts_endpoint, mocked_http_client, mocked_empty_domain_responses):
    mocked_empty_domain_responses.add(
        method=responses.GET,
        url="https://localhost/v5/caller-identity",
        content_type="application/json",
        headers={"x-request-id": "request-id"},
        body='{"error_code": "xxx", "error_msg": "service internal error"}',
        status=500
    )

    credentials = GlobalCredentials("ak", "sk")
    try:
        credentials.process_auth_params(mocked_http_client, "region-id")
    except SdkException as e:
        assert "Failed to get domain id automatically" in e.error_msg
        assert "service internal error" in e.error_msg


def test_new_basic_credentials():
    basic = BasicCredentials()
    basic.ak = "ak"
    basic.sk = "sk"
    basic.project_id = "project_id"
    basic.idp_id = "idp_id"
    basic.id_token_file = "id_token_file"
    basic.iam_endpoint = "iam_endpoint"

    assert basic.ak == "ak"
    assert basic.sk == "sk"
    assert basic.project_id == "project_id"
    assert basic.idp_id == "idp_id"
    assert basic.id_token_file == "id_token_file"
    assert basic.iam_endpoint == "iam_endpoint"


def test_new_global_credentials():
    glob = GlobalCredentials()
    glob.ak = "ak"
    glob.sk = "sk"
    glob.domain_id = "domain_id"
    glob.idp_id = "idp_id"
    glob.id_token_file = "id_token_file"
    glob.iam_endpoint = "iam_endpoint"

    assert glob.ak == "ak"
    assert glob.sk == "sk"
    assert glob.domain_id == "domain_id"
    assert glob.idp_id == "idp_id"
    assert glob.id_token_file == "id_token_file"
    assert glob.iam_endpoint == "iam_endpoint"


if __name__ == '__main__':
    pytest.main()
