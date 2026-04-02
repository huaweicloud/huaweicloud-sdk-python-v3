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
import os

import pytest
import requests
import responses
from urllib3.exceptions import NewConnectionError

from huaweicloudsdkcore.auth import endpoint
from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.auth.internal import IamHelper
from huaweicloudsdkcore.auth.provider import MetadataCredentialProvider, PodIdentityCredentialProvider
from huaweicloudsdkcore.exceptions.exception_handler import DefaultExceptionHandler
from huaweicloudsdkcore.exceptions.exceptions import SdkException, ServiceResponseException, ApiValueError
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.http.http_handler import HttpHandler
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer.algorithm import SigningAlgorithm
from tests.util.response_registry import OrderedRegistry

TEST_TOKEN_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "test_token.txt")


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


class TestAkskSignCredentials:
    def test_basic_credentials_sign_with_perm_aksk(self, sdk_request):
        credentials = BasicCredentials("ak", "sk")
        result = credentials.sign_request(sdk_request)
        assert "Authorization" in result.header_params

    def test_basic_credentials_sign_with_temp_aksk(self, sdk_request):
        credentials = BasicCredentials("ak", "sk")
        credentials.security_token = "token"
        result = credentials.sign_request(sdk_request)
        assert result.header_params.get("X-Security-Token") == "token"
        assert "Authorization" in result.header_params

    def test_global_credentials_sign_with_perm_aksk(self, sdk_request):
        credentials = GlobalCredentials("ak", "sk")
        result = credentials.sign_request(sdk_request)
        assert "Authorization" in result.header_params

    def test_global_credentials_sign_with_temp_aksk(self, sdk_request):
        credentials = GlobalCredentials("ak", "sk")
        credentials.security_token = "token"
        result = credentials.sign_request(sdk_request)
        assert result.header_params.get("X-Security-Token") == "token"
        assert "Authorization" in result.header_params


class TestBasicCredentialsGetProjectId:
    @responses.activate
    def test_auto_get_project_id(self, mocked_http_client):
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
    def test_empty_project_id(self, mocked_http_client):
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
    def test_multiple_project_ids(self, mocked_http_client):
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


class TestGlobalCredentialsGetDomainId:
    @responses.activate
    def test_auto_get_domain_id(self, mocked_http_client):
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

    def test_empty_domain_id(self, mocked_http_client, mocked_empty_domain_responses):
        credentials = GlobalCredentials("ak2", "sk2")
        try:
            credentials.process_auth_params(mocked_http_client, "region-id")
            raise AssertionError("Should have thrown a SdkException: Failed to get domain id...")
        except SdkException as e:
            assert ("Failed to get domain id, X-IAM-Trace-Id=trace-id. "
                    "Please confirm that you have 'iam:users:getUser' permission, "
                    "or set domain id: GlobalCredentials(ak, sk, domain_id)") == e.error_msg

    def test_get_domain_id_v5(self, mock_sts_endpoint, mocked_http_client, mocked_empty_domain_responses):
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

    def test_get_domain_id_v5_unknown_host(self, mock_sts_endpoint, mocked_http_client, mocked_empty_domain_responses):
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

    def test_get_domain_id_v5_status_404(self, mock_sts_endpoint, mocked_http_client, mocked_empty_domain_responses):
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

    def test_get_domain_id_v5_status_500(self, mock_sts_endpoint, mocked_http_client, mocked_empty_domain_responses):
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


class TestMetadataCredentials:
    @responses.activate
    def test_get_credentials_from_metadata_status_500(self):
        responses.add(
            method=responses.PUT,
            url="http://169.254.169.254/meta-data/latest/api/token",
            content_type="application/json",
            body='{"error_message":"internal error"}',
            status=500
        )

        provider = MetadataCredentialProvider.get_basic_credential_metadata_provider()
        try:
            provider.get_credentials()
            assert False, "should raise ServiceResponseException"
        except ServiceResponseException as exc:
            assert exc.status_code == 500

    @responses.activate
    def test_get_credentials_from_metadata_v1(self):
        responses.add(
            method=responses.PUT,
            url="http://169.254.169.254/meta-data/latest/api/token",
            content_type="application/json",
            body='{"error_message":"error"}',
            status=405
        )

        responses.add(
            method=responses.GET,
            url="http://169.254.169.254/openstack/latest/securitykey",
            content_type="application/json",
            body='{"credential": '
                 '{"access": "ak","expires_at": "2020-01-08T03:50:07.574000Z","secret": "sk","securitytoken": "st"}}'
        )

        provider = MetadataCredentialProvider.get_basic_credential_metadata_provider()
        credentials = provider.get_credentials()
        assert credentials.ak == "ak"
        assert credentials.sk == "sk"
        assert credentials.security_token == "st"

    @responses.activate
    def test_get_credentials_from_metadata_v2(self):
        responses.add(
            method=responses.PUT,
            url="http://169.254.169.254/meta-data/latest/api/token",
            match=[responses.matchers.header_matcher({"X-Metadata-Token-Ttl-Seconds": "21600"})],
            body="token",
        )
        responses.add(
            method=responses.GET,
            url="http://169.254.169.254/openstack/latest/securitykey",
            match=[responses.matchers.header_matcher({"X-Metadata-Token": "token"})],
            content_type="application/json",
            body='{"credential": '
                 '{"access": "ak","expires_at": "2020-01-08T03:50:07.574000Z","secret": "sk","securitytoken": "st"}}'
        )

        provider = MetadataCredentialProvider.get_basic_credential_metadata_provider()
        credentials = provider.get_credentials()
        assert credentials.ak == "ak"
        assert credentials.sk == "sk"
        assert credentials.security_token == "st"


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


class TestFederalCredentials:

    def test_basic_credentials(self):
        credentials = BasicCredentials().with_idp_id("idp_id").with_id_token_file("file").with_project_id("project_id")
        credentials.process_auth_params(None, None)

    def test_basic_credentials_without_idp_id(self):
        credentials = BasicCredentials().with_id_token_file("file")
        try:
            credentials.process_auth_params(None, None)
        except ApiValueError as e:
            assert "idp_id is required when using idp_id & id_token_file" == str(e)

    def test_basic_credentials_without_id_token_file(self):
        credentials = BasicCredentials().with_idp_id("idp_id")
        try:
            credentials.process_auth_params(None, None)
        except ApiValueError as e:
            assert "id_token_file is required when using idp_id & id_token_file" == str(e)

    def test_global_credentials(self):
        credentials = GlobalCredentials().with_idp_id("idp_id").with_id_token_file("file").with_domain_id("domain_id")
        credentials.process_auth_params(None, None)

    def test_global_credentials_without_idp_id(self):
        credentials = GlobalCredentials().with_id_token_file("file")
        try:
            credentials.process_auth_params(None, None)
        except ApiValueError as e:
            assert "idp_id is required when using idp_id & id_token_file" == str(e)

    def test_global_credentials_without_id_token_file(self):
        credentials = GlobalCredentials().with_idp_id("idp_id")
        try:
            credentials.process_auth_params(None, None)
        except ApiValueError as e:
            assert "id_token_file is required when using idp_id & id_token_file" == str(e)

    @responses.activate(registry=OrderedRegistry)
    def test_federal_credentials(self):
        responses.add(
            method=responses.POST,
            url=IamHelper.get_iam_endpoint() + "/v3.0/OS-AUTH/id-token/tokens",
            adding_headers={
                "Content-Type": "application/json",
                "X-IAM-Trace-Id": "trace-id",
                "X-Subject-Token": "auth-token"
            },
            body="{\"token\":{\"expires_at\":\"2018-03-13T03:00:01.168000Z\",\"methods\":[\"mapped\"]}}",
            status=200,
            match=[
                responses.matchers.header_matcher({"X-Idp-Id": "idp_id"}),
                responses.matchers.json_params_matcher({"auth": {"id_token": {"id": "token_value"}}})
            ]
        )
        responses.add(
            method=responses.POST,
            url=IamHelper.get_iam_endpoint() + "/v3.0/OS-CREDENTIAL/securitytokens",
            adding_headers={
                "Content-Type": "application/json",
                "X-IAM-Trace-Id": "trace-id"
            },
            body="{\"credential\":{\"access\":\"ak\"," +
                 "\"expires_at\":\"2020-01-08T03:50:07.574000Z\"," +
                 "\"secret\":\"sk\"," +
                 "\"securitytoken\":\"sec-token\"}}",
            status=200,
            match=[responses.matchers.json_params_matcher(
                {"auth": {
                    "identity": {"methods": ["token"], "token": {"id": "auth-token", "duration_seconds": 21600}}}})]
        )

        cred = BasicCredentials().with_idp_id("idp_id").with_id_token_file(TEST_TOKEN_FILE)
        http_client = HttpClient(HttpConfig.get_default_config(), HttpHandler(), DefaultExceptionHandler(),
                                 logging.getLogger("test_federal"))
        cred.process_sts(http_client)

        assert cred.ak == "ak"
        assert cred.sk == "sk"
        assert cred.security_token == "sec-token"


class TestPodIdentityCredentials:
    @classmethod
    def setup_class(cls):
        os.environ["HC_CONTAINER_CREDENTIALS_FULL_URI"] = "http://127.0.0.1/v1/credentials"
        os.environ["HC_CONTAINER_AUTHORIZATION_TOKEN_FILE"] = TEST_TOKEN_FILE

    @classmethod
    def teardown_class(cls):
        os.unsetenv("HC_CONTAINER_CREDENTIALS_FULL_URI")
        os.unsetenv("HC_CONTAINER_AUTHORIZATION_TOKEN_FILE")

    @responses.activate
    def test_pod_identity_credentials_200(self):
        responses.add(
            method=responses.POST,
            url="http://127.0.0.1/v1/credentials",
            adding_headers={"Content-Type": "application/json"},
            body="{\"assumedAgency\":{\"urn\":\"\",\"id\":\"\"}," +
                 "\"audience\":\"\",\"credentials\":" +
                 "{\"accessKeyId\":\"ak\",\"secretAccessKey\":\"sk\"," +
                 "\"securityToken\":\"st\",\"expiration\":\"2020-01-08T03:50:07.574000Z\"}," +
                 "\"podIdentityAssociationId\":\"\",\"subject\":" +
                 "{\"namespace\":\"\",\"serviceAccount\":\"\"}}",
            status=200,
            match=[
                responses.matchers.json_params_matcher({}),
                responses.matchers.header_matcher({"Authorization": "token_value"})
            ]
        )

        provider = PodIdentityCredentialProvider.get_basic()
        credentials = provider.get_credentials()
        assert credentials.ak == "ak"
        assert credentials.sk == "sk"
        assert credentials.security_token == "st"

    @responses.activate
    def test_pod_identity_credentials_404(self):
        responses.add(
            method=responses.POST,
            url="http://127.0.0.1/v1/credentials",
            body="{\"error_message\":\"not found\"}",
            status=404
        )

        provider = PodIdentityCredentialProvider.get_global()
        try:
            provider.get_credentials()
            assert False, "should raise SdkException"
        except SdkException as e:
            assert e.error_msg == ('failed to get credential from pod identity,'
                                   ' detail: 404 Client Error: Not Found for url: http://127.0.0.1/v1/credentials')


if __name__ == '__main__':
    pytest.main()
