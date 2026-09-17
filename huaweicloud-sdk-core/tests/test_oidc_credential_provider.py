# coding: utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE. You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

import json
import logging
import os
from unittest.mock import patch

import pytest
import responses

from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.auth.internal import (
    Credential,
    FederalAccessor,
    IamHelper,
    OidcStsAccessor,
    StsAccessor,
    StsHelper,
)
from huaweicloudsdkcore.auth.provider import (
    CredentialProvider,
    CredentialProviderChain,
    EnvCredentialProvider,
    OidcStsCredentialProvider,
    PodIdentityCredentialProvider,
    ProfileCredentialProvider,
    MetadataCredentialProvider,
    patch_provider_chain,
)
from huaweicloudsdkcore.exceptions.exceptions import ApiValueError, SdkException
from huaweicloudsdkcore.exceptions.exception_handler import DefaultExceptionHandler
from huaweicloudsdkcore.http.http_client import HttpClient
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.http.user_agent import user_agent_string
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer.algorithm import SigningAlgorithm

TEST_TOKEN_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data", "test_token.txt")
TOKEN_FILE_CONTENT = "token_value"

PROVIDER_URN = "iam::123456789:oidcProvider:test"
AGENCY_URN = "iam::123456789:agency:demo"
ID_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.test-token"
SESSION_NAME = "test-session"
ENDPOINT = "https://sts.cn-north-4.myhuaweicloud.com"
OIDC_API_URL = ENDPOINT + "/v5/agencies/assume-with-oidc"
PROJECT_ID = "test-project-id"
DOMAIN_ID = "test-domain-id"
DURATION_SECONDS = 3600

AK = "HSTA8D5OT1XAD1FC625D"
SK = "test-secret-access-key"
SECURITY_TOKEN = "test-security-token"
EXPIRATION = "2026-08-10T07:15:09.084Z"
FUTURE_EXPIRATION = "2099-12-31T23:59:59.000Z"

OIDC_RESPONSE_BODY = json.dumps({
    "assumed_agency": {
        "urn": "sts::123456789:assumed-agency:demo/test-session",
        "id": "123456789:test-session"
    },
    "credentials": {
        "access_key_id": AK,
        "secret_access_key": SK,
        "security_token": SECURITY_TOKEN,
        "expiration": EXPIRATION
    },
    "subject_from_id_token": "test-subject",
    "audience": "test-audience",
    "provider": PROVIDER_URN
})

OIDC_RESPONSE_BODY_FUTURE = json.dumps({
    "assumed_agency": {
        "urn": "sts::123456789:assumed-agency:demo/test-session",
        "id": "123456789:test-session"
    },
    "credentials": {
        "access_key_id": AK,
        "secret_access_key": SK,
        "security_token": SECURITY_TOKEN,
        "expiration": FUTURE_EXPIRATION
    },
    "subject_from_id_token": "test-subject",
    "audience": "test-audience",
    "provider": PROVIDER_URN
})

OIDC_ERROR_BODY = json.dumps({
    "error_code": "IAM.0001",
    "error_msg": "Invalid id_token"
})


def _clear_oidc_envs():
    keys = [
        "HUAWEICLOUD_OIDC_PROVIDER_URN",
        "HUAWEICLOUD_OIDC_AGENCY_URN",
        "HUAWEICLOUD_OIDC_ID_TOKEN",
        "HUAWEICLOUD_OIDC_TOKEN_FILE",
        "HUAWEICLOUD_OIDC_SESSION_NAME",
        "HUAWEICLOUD_OIDC_DURATION_SECONDS",
        "HUAWEICLOUD_OIDC_POLICY",
        "HUAWEICLOUD_OIDC_POLICY_IDS",
        "HUAWEICLOUD_SDK_PROJECT_ID",
        "HUAWEICLOUD_SDK_DOMAIN_ID",
        "HUAWEICLOUD_SDK_AK",
        "HUAWEICLOUD_SDK_SK",
        "HUAWEICLOUD_SDK_SECURITY_TOKEN",
        "HUAWEICLOUD_SDK_IDP_ID",
        "HUAWEICLOUD_SDK_ID_TOKEN_FILE",
        "HUAWEICLOUD_SDK_CREDENTIALS_FILE",
        "HUAWEICLOUD_SDK_IAM_ENDPOINT",
        "HUAWEICLOUD_SDK_STS_ENDPOINT",
    ]
    for key in keys:
        os.environ.pop(key, None)


def _set_oidc_envs(**overrides):
    defaults = {
        "HUAWEICLOUD_OIDC_PROVIDER_URN": PROVIDER_URN,
        "HUAWEICLOUD_OIDC_AGENCY_URN": AGENCY_URN,
        "HUAWEICLOUD_OIDC_TOKEN_FILE": TEST_TOKEN_FILE,
        "HUAWEICLOUD_OIDC_SESSION_NAME": SESSION_NAME,
        "HUAWEICLOUD_OIDC_DURATION_SECONDS": str(DURATION_SECONDS),
    }
    defaults.update(overrides)
    for k, v in defaults.items():
        os.environ[k] = v


def _create_http_client():
    config = HttpConfig.get_default_config()
    return HttpClient(config, None, DefaultExceptionHandler(), logging.getLogger("test"))


def _assert_oidc_request_body(call, expected_id_token="token_value",
                              expected_duration=DURATION_SECONDS,
                              expected_session_name=SESSION_NAME):
    body = json.loads(call.request.body)
    assert body["provider_urn"] == PROVIDER_URN
    assert body["agency_urn"] == AGENCY_URN
    assert body["agency_session_name"] == expected_session_name
    assert body["id_token"] == expected_id_token
    assert body["duration_seconds"] == expected_duration


# ---------------------------------------------------------------------------
# 1. TestOidcStsAccessor -- basic accessor with HttpClient
# ---------------------------------------------------------------------------
class TestOidcStsAccessor:
    def setup_method(self):
        self.http_client = _create_http_client()

    def teardown_method(self):
        self.http_client.close()

    @responses.activate
    def test_get_credential_success(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
            duration_seconds=DURATION_SECONDS,
        )
        credential = accessor.get_credential(http_client=self.http_client)

        assert credential.access == AK
        assert credential.secret == SK
        assert credential.security_token == SECURITY_TOKEN
        assert credential.expire_at is not None

    def test_get_credential_missing_id_token_raises(self):
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=None,
            agency_session_name=SESSION_NAME,
        )
        with pytest.raises(SdkException) as exc_info:
            accessor.get_credential(http_client=self.http_client)
        assert "id_token is required" in str(exc_info.value)

    @responses.activate
    def test_get_credential_endpoint_fallback_to_sts_helper(self):
        fallback_url = "https://sts.cn-north-4.myhuaweicloud.com/v5/agencies/assume-with-oidc"
        responses.add(
            method=responses.POST,
            url=fallback_url,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
        )
        credential = accessor.get_credential(http_client=self.http_client)
        assert credential.access == AK

    @responses.activate
    def test_get_credential_with_sts_endpoint_kwargs(self):
        custom_endpoint = "https://custom-sts.example.com"
        responses.add(
            method=responses.POST,
            url=custom_endpoint + "/v5/agencies/assume-with-oidc",
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
        )
        credential = accessor.get_credential(
            http_client=self.http_client,
            sts_endpoint=custom_endpoint,
        )
        assert credential.access == AK

    @responses.activate
    def test_get_credential_sts_endpoint_kwargs_overrides_env(self):
        os.environ["HUAWEICLOUD_SDK_STS_ENDPOINT"] = "https://env-sts.example.com"
        try:
            custom_endpoint = "https://kwargs-sts.example.com"
            responses.add(
                method=responses.POST,
                url=custom_endpoint + "/v5/agencies/assume-with-oidc",
                content_type="application/json",
                body=OIDC_RESPONSE_BODY,
                status=200,
            )
            accessor = OidcStsAccessor(
                provider_urn=PROVIDER_URN,
                agency_urn=AGENCY_URN,
                id_token=ID_TOKEN,
                agency_session_name=SESSION_NAME,
            )
            accessor.get_credential(
                http_client=self.http_client,
                sts_endpoint=custom_endpoint,
            )
            assert responses.calls[0].request.url.startswith(custom_endpoint)
        finally:
            os.environ.pop("HUAWEICLOUD_SDK_STS_ENDPOINT", None)

    def test_get_credential_missing_http_client_raises(self):
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
        )
        with pytest.raises(SdkException) as exc_info:
            accessor.get_credential()
        assert "http_client is required" in str(exc_info.value)

    @responses.activate
    def test_get_credential_http_error_raises(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            body=OIDC_ERROR_BODY,
            status=400,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
        )
        with pytest.raises(SdkException) as exc_info:
            accessor.get_credential(http_client=self.http_client)
        assert "failed to get credential from oidc sts" in str(exc_info.value)

    @responses.activate
    def test_get_credential_default_duration_seconds(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
        )
        accessor.get_credential(http_client=self.http_client)
        body = json.loads(responses.calls[0].request.body)
        assert body["duration_seconds"] == 3600

    @responses.activate
    def test_get_credential_endpoint_with_trailing_slash(self):
        os.environ["HUAWEICLOUD_SDK_STS_ENDPOINT"] = ENDPOINT + "/"
        try:
            responses.add(
                method=responses.POST,
                url=OIDC_API_URL,
                content_type="application/json",
                body=OIDC_RESPONSE_BODY,
                status=200,
            )
            accessor = OidcStsAccessor(
                provider_urn=PROVIDER_URN,
                agency_urn=AGENCY_URN,
                id_token=ID_TOKEN,
                agency_session_name=SESSION_NAME,
            )
            credential = accessor.get_credential(http_client=self.http_client)
            assert credential.access == AK
        finally:
            os.environ.pop("HUAWEICLOUD_SDK_STS_ENDPOINT", None)

    def test_accessor_constants(self):
        assert OidcStsAccessor._ASSUME_AGENCY_WITH_OIDC_URI == "/v5/agencies/assume-with-oidc"
        assert OidcStsAccessor._DEFAULT_DURATION_SECONDS == 3600

    @responses.activate
    def test_get_credential_with_policy_and_policy_ids(self):
        policy = {"Version": "1.1"}
        policy_ids = [{"id": "pid-1"}]
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
            policy=policy,
            policy_ids=policy_ids,
        )
        accessor.get_credential(http_client=self.http_client)
        body = json.loads(responses.calls[0].request.body)
        assert body["policy"] == policy
        assert body["policy_ids"] == policy_ids


# ---------------------------------------------------------------------------
# 2. TestOidcStsAccessorWithHttpClient -- HttpClient path emphasis
# ---------------------------------------------------------------------------
class TestOidcStsAccessorWithHttpClient:
    def setup_method(self):
        self.http_client = _create_http_client()

    def teardown_method(self):
        self.http_client.close()

    @responses.activate
    def test_success_via_http_client(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
            duration_seconds=DURATION_SECONDS,
        )
        credential = accessor.get_credential(http_client=self.http_client)

        assert credential.access == AK
        assert credential.secret == SK
        assert credential.security_token == SECURITY_TOKEN
        assert credential.expire_at is not None

    @responses.activate
    def test_error_via_http_client(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            body=OIDC_ERROR_BODY,
            status=400,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
        )
        with pytest.raises(SdkException) as exc_info:
            accessor.get_credential(http_client=self.http_client)
        assert "failed to get credential from oidc sts" in str(exc_info.value)

    @responses.activate
    def test_request_body_via_http_client(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
            duration_seconds=DURATION_SECONDS,
        )
        accessor.get_credential(http_client=self.http_client)
        _assert_oidc_request_body(responses.calls[0], expected_id_token=ID_TOKEN)

    @responses.activate
    def test_policy_in_payload(self):
        policy = {"Version": "1.1", "Statement": [{"Effect": "Allow", "Action": ["*"], "Resource": ["*"]}]}
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
            policy=policy,
        )
        accessor.get_credential(http_client=self.http_client)
        body = json.loads(responses.calls[0].request.body)
        assert body["policy"] == policy

    @responses.activate
    def test_policy_ids_in_payload(self):
        policy_ids = [{"id": "policy-id-1"}]
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
            policy_ids=policy_ids,
        )
        accessor.get_credential(http_client=self.http_client)
        body = json.loads(responses.calls[0].request.body)
        assert body["policy_ids"] == policy_ids

    @responses.activate
    def test_trailing_slash_via_http_client(self):
        os.environ["HUAWEICLOUD_SDK_STS_ENDPOINT"] = ENDPOINT + "/"
        try:
            responses.add(
                method=responses.POST,
                url=OIDC_API_URL,
                content_type="application/json",
                body=OIDC_RESPONSE_BODY,
                status=200,
            )
            accessor = OidcStsAccessor(
                provider_urn=PROVIDER_URN,
                agency_urn=AGENCY_URN,
                id_token=ID_TOKEN,
                agency_session_name=SESSION_NAME,
            )
            credential = accessor.get_credential(http_client=self.http_client)
            assert credential.access == AK
        finally:
            os.environ.pop("HUAWEICLOUD_SDK_STS_ENDPOINT", None)

    def test_no_http_client_raises(self):
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
        )
        with pytest.raises(SdkException) as exc_info:
            accessor.get_credential()
        assert "http_client is required" in str(exc_info.value)

    @responses.activate
    def test_default_duration_via_http_client(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
        )
        accessor.get_credential(http_client=self.http_client)
        body = json.loads(responses.calls[0].request.body)
        assert body["duration_seconds"] == 3600

    @responses.activate
    def test_user_agent_header(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
        )
        accessor.get_credential(http_client=self.http_client)
        sent_headers = responses.calls[0].request.headers
        assert sent_headers.get("User-Agent") == user_agent_string


# ---------------------------------------------------------------------------
# 3. TestIamHelperAssumeAgencyWithOidc -- IamHelper new methods
# ---------------------------------------------------------------------------
class TestIamHelperAssumeAgencyWithOidc:
    def setup_method(self):
        self.http_client = _create_http_client()
        self.config = self.http_client.config
        self.payload = {
            "provider_urn": PROVIDER_URN,
            "agency_urn": AGENCY_URN,
            "agency_session_name": SESSION_NAME,
            "id_token": ID_TOKEN,
            "duration_seconds": DURATION_SECONDS,
        }

    def teardown_method(self):
        self.http_client.close()

    def test_request_method_is_post(self):
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        assert request.method == "POST"

    def test_request_uri(self):
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        assert request.uri == IamHelper.ASSUME_AGENCY_WITH_OIDC_URI

    def test_request_url(self):
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        assert request.url == OIDC_API_URL

    def test_request_content_type(self):
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        assert request.header_params["Content-Type"] == "application/json;charset=UTF-8"

    def test_request_body(self):
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        body = json.loads(request.body)
        assert body == self.payload

    def test_request_host_and_schema(self):
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        assert request.host == "sts.cn-north-4.myhuaweicloud.com"
        assert request.schema == "https"

    @responses.activate
    def test_execute_success(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        content = IamHelper.assume_agency_with_oidc(self.http_client, request)
        assert content is not None
        parsed = json.loads(content)
        assert parsed["credentials"]["access_key_id"] == AK

    @responses.activate
    def test_execute_4xx_raises_sdk_exception(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            body=OIDC_ERROR_BODY,
            status=400,
        )
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        with pytest.raises(SdkException) as exc_info:
            IamHelper.assume_agency_with_oidc(self.http_client, request)
        assert "failed to get credential from oidc sts" in str(exc_info.value)

    @responses.activate
    def test_execute_5xx_raises_sdk_exception(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            body=OIDC_ERROR_BODY,
            status=500,
        )
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        with pytest.raises(SdkException) as exc_info:
            IamHelper.assume_agency_with_oidc(self.http_client, request)
        assert "failed to get credential from oidc sts" in str(exc_info.value)

    @responses.activate
    def test_execute_empty_response_raises(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            body="",
            status=200,
        )
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        with pytest.raises(SdkException) as exc_info:
            IamHelper.assume_agency_with_oidc(self.http_client, request)
        assert "empty response" in str(exc_info.value)

    def test_execute_none_response_raises(self):
        request = IamHelper.get_assume_agency_with_oidc_request(self.config, ENDPOINT, self.payload)
        with patch.object(self.http_client, "do_request_sync", return_value=None):
            with pytest.raises(SdkException) as exc_info:
                IamHelper.assume_agency_with_oidc(self.http_client, request)
        assert "empty response" in str(exc_info.value)


# ---------------------------------------------------------------------------
# 4. TestOidcStsRefreshViaHttpClient -- process_sts integration
# ---------------------------------------------------------------------------
class TestOidcStsRefreshViaHttpClient:
    def setup_method(self):
        _clear_oidc_envs()
        self.http_client = _create_http_client()

    def teardown_method(self):
        _clear_oidc_envs()
        self.http_client.close()

    @responses.activate
    def test_process_sts_gets_credential(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()
        assert credentials.ak is None

        credentials.process_sts(self.http_client)
        assert credentials.ak == AK
        assert credentials.sk == SK
        assert credentials.security_token == SECURITY_TOKEN

    @responses.activate
    def test_process_sts_not_refreshed_when_not_expired(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY_FUTURE,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        credentials.process_sts(self.http_client)
        assert credentials.ak == AK
        assert len(responses.calls) == 1

        credentials.process_sts(self.http_client)
        assert len(responses.calls) == 1

    @responses.activate
    def test_process_sts_refreshed_when_expired(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        credentials.process_sts(self.http_client)
        assert credentials.ak == AK
        assert len(responses.calls) == 1

        credentials.process_sts(self.http_client)
        assert len(responses.calls) == 2

    @responses.activate
    def test_process_sts_4xx_raises(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            body=OIDC_ERROR_BODY,
            status=400,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        with pytest.raises(SdkException) as exc_info:
            credentials.process_sts(self.http_client)
        assert "failed to get credential from oidc sts" in str(exc_info.value)

    @responses.activate
    def test_process_sts_5xx_raises(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            body=OIDC_ERROR_BODY,
            status=500,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        with pytest.raises(SdkException) as exc_info:
            credentials.process_sts(self.http_client)
        assert "failed to get credential from oidc sts" in str(exc_info.value)

    @responses.activate
    def test_process_auth_request(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        sdk_request = SdkRequest(
            method="GET",
            schema="https",
            host="service.region-1.com",
            resource_path="/test",
            header_params={},
            query_params=[],
            signing_algorithm=SigningAlgorithm.get_default(),
        )
        future = credentials.process_auth_request(sdk_request, self.http_client)
        signed_request = future.result()

        assert credentials.ak == AK
        assert credentials.sk == SK
        assert "Authorization" in signed_request.header_params

    @responses.activate
    def test_global_credentials_process_sts(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_DOMAIN_ID"] = DOMAIN_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_global()
        credentials = provider.get_credentials()
        assert isinstance(credentials, GlobalCredentials)
        assert credentials.ak is None

        credentials.process_sts(self.http_client)
        assert credentials.ak == AK
        assert credentials.sk == SK
        assert credentials.security_token == SECURITY_TOKEN
        assert credentials.domain_id == DOMAIN_ID


# ---------------------------------------------------------------------------
# 5. TestNoRegressionOnExistingAuth -- regression tests
# ---------------------------------------------------------------------------
class TestNoRegressionOnExistingAuth:
    def setup_method(self):
        _clear_oidc_envs()

    def teardown_method(self):
        _clear_oidc_envs()

    def test_iam_helper_constants_unchanged(self):
        assert IamHelper.DEFAULT_ENDPOINT == "https://iam.myhuaweicloud.com"
        assert IamHelper.KEYSTONE_LIST_PROJECT_URI == "/v3/projects"
        assert IamHelper.KEYSTONE_LIST_AUTH_DOMAINS_URI == "/v3/auth/domains"
        assert IamHelper.CREATE_TOKEN_BY_ID_TOKEN_URI == "/v3.0/OS-AUTH/id-token/tokens"
        assert IamHelper.CREATE_TEMPORARY_ACCESS_KEY_BY_TOKEN_URI == "/v3.0/OS-CREDENTIAL/securitytokens"
        assert IamHelper.IAM_ENDPOINT_ENV_NAME == "HUAWEICLOUD_SDK_IAM_ENDPOINT"

    def test_new_assume_agency_with_oidc_constant(self):
        assert IamHelper.ASSUME_AGENCY_WITH_OIDC_URI == "/v5/agencies/assume-with-oidc"

    def test_sts_helper_default_endpoint(self):
        assert StsHelper.DEFAULT_STS_ENDPOINT == "https://sts.cn-north-4.myhuaweicloud.com"

    def test_sts_helper_get_sts_endpoint_default(self):
        os.environ.pop("HUAWEICLOUD_SDK_STS_ENDPOINT", None)
        result = StsHelper.get_sts_endpoint()
        assert result == "https://sts.cn-north-4.myhuaweicloud.com"

    def test_aksk_direct_pass_through(self):
        credentials = BasicCredentials("ak", "sk")
        assert credentials.ak == "ak"
        assert credentials.sk == "sk"
        assert credentials.sts_accessor is None

    def test_federal_accessor_unchanged(self):
        assert hasattr(FederalAccessor, "_DEFAULT_DURATION_SECONDS")
        assert FederalAccessor._DEFAULT_DURATION_SECONDS == 6 * 60 * 60
        assert callable(getattr(FederalAccessor, "get_credential", None))

    def test_oidc_lazy_credential(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()
        assert credentials.ak is None
        assert credentials.sk is None
        assert credentials.sts_accessor is not None
        assert isinstance(credentials.sts_accessor, OidcStsAccessor)

    def test_sts_helper_get_sts_endpoint_with_env(self):
        os.environ["HUAWEICLOUD_SDK_STS_ENDPOINT"] = "https://custom-sts.example.com"
        result = StsHelper.get_sts_endpoint()
        assert result == "https://custom-sts.example.com"

    def test_iam_helper_get_iam_endpoint_with_env(self):
        os.environ["HUAWEICLOUD_SDK_IAM_ENDPOINT"] = "https://custom-iam.example.com"
        result = IamHelper.get_iam_endpoint()
        assert result == "https://custom-iam.example.com"

    def test_iam_helper_get_iam_endpoint_default(self):
        os.environ.pop("HUAWEICLOUD_SDK_IAM_ENDPOINT", None)
        result = IamHelper.get_iam_endpoint()
        assert result == "https://iam.myhuaweicloud.com"

    def test_oidc_provider_id_token_env_name(self):
        assert OidcStsCredentialProvider._ID_TOKEN_ENV == "HUAWEICLOUD_OIDC_ID_TOKEN"


# ---------------------------------------------------------------------------
# 6. TestProcessCredentialV5Format -- response parsing
# ---------------------------------------------------------------------------
class TestProcessCredentialV5Format:
    def test_process_credential_v5_snake_case(self):
        data = {
            "credentials": {
                "access_key_id": AK,
                "secret_access_key": SK,
                "security_token": SECURITY_TOKEN,
                "expiration": EXPIRATION,
            }
        }
        credential = StsAccessor._process_credential(data)
        assert credential.access == AK
        assert credential.secret == SK
        assert credential.security_token == SECURITY_TOKEN
        assert credential.expire_at is not None

    def test_process_credential_v5_bytes(self):
        data = json.dumps({
            "credentials": {
                "access_key_id": AK,
                "secret_access_key": SK,
                "security_token": SECURITY_TOKEN,
                "expiration": EXPIRATION,
            }
        }).encode()
        credential = StsAccessor._process_credential(data)
        assert credential.access == AK
        assert credential.secret == SK
        assert credential.security_token == SECURITY_TOKEN

    def test_process_credential_existing_camel_case_still_works(self):
        data = {
            "credential": {
                "access": "old-ak",
                "secret": "old-sk",
                "securitytoken": "old-st",
                "expires_at": EXPIRATION,
            }
        }
        credential = StsAccessor._process_credential(data)
        assert credential.access == "old-ak"
        assert credential.secret == "old-sk"
        assert credential.security_token == "old-st"

    def test_process_credential_existing_access_key_id_camel(self):
        data = {
            "credentials": {
                "accessKeyId": "camel-ak",
                "secretAccessKey": "camel-sk",
                "securityToken": "camel-st",
                "expiration": EXPIRATION,
            }
        }
        credential = StsAccessor._process_credential(data)
        assert credential.access == "camel-ak"
        assert credential.secret == "camel-sk"
        assert credential.security_token == "camel-st"

    def test_process_credential_invalid_type_raises(self):
        with pytest.raises(SdkException) as exc_info:
            StsAccessor._process_credential(12345)
        assert "failed to process credential" in str(exc_info.value)

    def test_process_credential_from_str(self):
        data = json.dumps({
            "credentials": {
                "access_key_id": AK,
                "secret_access_key": SK,
                "security_token": SECURITY_TOKEN,
                "expiration": EXPIRATION,
            }
        })
        credential = StsAccessor._process_credential(data)
        assert credential.access == AK
        assert credential.secret == SK


# ---------------------------------------------------------------------------
# 7. TestOidcStsCredentialProvider -- provider tests
# ---------------------------------------------------------------------------
class TestOidcStsCredentialProvider:
    def setup_method(self):
        _clear_oidc_envs()

    def teardown_method(self):
        _clear_oidc_envs()

    def test_missing_provider_urn_raises(self):
        _set_oidc_envs()
        os.environ.pop("HUAWEICLOUD_OIDC_PROVIDER_URN", None)
        provider = OidcStsCredentialProvider.get_basic()
        with pytest.raises(ApiValueError) as exc_info:
            provider.get_credentials()
        assert "HUAWEICLOUD_OIDC_PROVIDER_URN" in str(exc_info.value)

    def test_missing_agency_urn_raises(self):
        _set_oidc_envs()
        os.environ.pop("HUAWEICLOUD_OIDC_AGENCY_URN", None)
        provider = OidcStsCredentialProvider.get_basic()
        with pytest.raises(ApiValueError) as exc_info:
            provider.get_credentials()
        assert "HUAWEICLOUD_OIDC_AGENCY_URN" in str(exc_info.value)

    def test_missing_id_token_raises(self):
        _set_oidc_envs()
        os.environ.pop("HUAWEICLOUD_OIDC_TOKEN_FILE", None)
        os.environ.pop("HUAWEICLOUD_OIDC_ID_TOKEN", None)
        provider = OidcStsCredentialProvider.get_basic()
        with pytest.raises(ApiValueError) as exc_info:
            provider.get_credentials()
        assert "HUAWEICLOUD_OIDC_ID_TOKEN" in str(exc_info.value)
        assert "HUAWEICLOUD_OIDC_TOKEN_FILE" in str(exc_info.value)

    @responses.activate
    def test_basic_type_success(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()
        assert isinstance(credentials, BasicCredentials)
        assert credentials.project_id == PROJECT_ID
        assert credentials.sts_accessor is not None

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            assert credentials.ak == AK
            assert credentials.sk == SK
            assert credentials.security_token == SECURITY_TOKEN
        finally:
            http_client.close()

    @responses.activate
    def test_global_type_success(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_DOMAIN_ID"] = DOMAIN_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_global()
        credentials = provider.get_credentials()
        assert isinstance(credentials, GlobalCredentials)
        assert credentials.domain_id == DOMAIN_ID

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            assert credentials.ak == AK
            assert credentials.sk == SK
            assert credentials.security_token == SECURITY_TOKEN
        finally:
            http_client.close()

    @responses.activate
    def test_basic_type_without_project_id(self):
        _set_oidc_envs()
        os.environ.pop("HUAWEICLOUD_SDK_PROJECT_ID", None)
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()
        assert isinstance(credentials, BasicCredentials)
        assert credentials.project_id is None

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            assert credentials.ak == AK
        finally:
            http_client.close()

    @responses.activate
    def test_global_type_without_domain_id(self):
        _set_oidc_envs()
        os.environ.pop("HUAWEICLOUD_SDK_DOMAIN_ID", None)
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_global()
        credentials = provider.get_credentials()
        assert isinstance(credentials, GlobalCredentials)
        assert credentials.domain_id is None

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            assert credentials.ak == AK
        finally:
            http_client.close()

    @responses.activate
    def test_api_error_raises_sdk_exception(self):
        _set_oidc_envs()
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            body=OIDC_ERROR_BODY,
            status=400,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        http_client = _create_http_client()
        try:
            with pytest.raises(SdkException) as exc_info:
                credentials.process_sts(http_client)
            assert "failed to get credential from oidc sts" in str(exc_info.value)
        finally:
            http_client.close()

    @responses.activate
    def test_custom_session_name(self):
        custom_name = "my-custom-session"
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_OIDC_SESSION_NAME"] = custom_name
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            body = json.loads(responses.calls[0].request.body)
            assert body["agency_session_name"] == custom_name
        finally:
            http_client.close()

    @responses.activate
    def test_custom_duration_seconds(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_OIDC_DURATION_SECONDS"] = "1800"
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            body = json.loads(responses.calls[0].request.body)
            assert body["duration_seconds"] == 1800
        finally:
            http_client.close()

    @responses.activate
    def test_default_endpoint_when_not_set(self):
        _set_oidc_envs()
        os.environ.pop("HUAWEICLOUD_SDK_STS_ENDPOINT", None)
        default_url = StsHelper.DEFAULT_STS_ENDPOINT + "/v5/agencies/assume-with-oidc"
        responses.add(
            method=responses.POST,
            url=default_url,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            assert credentials.ak == AK
        finally:
            http_client.close()

    @responses.activate
    def test_default_session_name_when_not_set(self):
        _set_oidc_envs()
        os.environ.pop("HUAWEICLOUD_OIDC_SESSION_NAME", None)
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            body = json.loads(responses.calls[0].request.body)
            assert body["agency_session_name"] == OidcStsCredentialProvider._DEFAULT_SESSION_NAME
        finally:
            http_client.close()

    @responses.activate
    def test_default_duration_when_not_set(self):
        _set_oidc_envs()
        os.environ.pop("HUAWEICLOUD_OIDC_DURATION_SECONDS", None)
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            body = json.loads(responses.calls[0].request.body)
            assert body["duration_seconds"] == OidcStsCredentialProvider._DEFAULT_DURATION_SECONDS
        finally:
            http_client.close()

    def test_get_basic_credential_oidc_provider(self):
        provider = OidcStsCredentialProvider.get_basic_credential_oidc_provider()
        assert isinstance(provider, OidcStsCredentialProvider)

    def test_get_global_credential_oidc_provider(self):
        provider = OidcStsCredentialProvider.get_global_credential_oidc_provider()
        assert isinstance(provider, OidcStsCredentialProvider)

    @responses.activate
    def test_sts_accessor_attached_for_refresh(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()
        assert credentials.sts_accessor is not None
        assert isinstance(credentials.sts_accessor, OidcStsAccessor)

    def test_programmatic_params(self):
        _clear_oidc_envs()
        provider = OidcStsCredentialProvider(
            "basic",
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            agency_session_name=SESSION_NAME,
            duration_seconds=DURATION_SECONDS,
        )
        credentials = provider.get_credentials()
        assert isinstance(credentials, BasicCredentials)
        accessor = credentials.sts_accessor
        assert accessor._provider_urn == PROVIDER_URN
        assert accessor._agency_urn == AGENCY_URN
        assert accessor._id_token == ID_TOKEN
        assert accessor._agency_session_name == SESSION_NAME
        assert accessor._duration_seconds == DURATION_SECONDS

    def test_programmatic_sts_endpoint(self):
        _clear_oidc_envs()
        provider = OidcStsCredentialProvider(
            "basic",
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            sts_endpoint=ENDPOINT,
        )
        credentials = provider.get_credentials()
        assert credentials.sts_endpoint == ENDPOINT

    @responses.activate
    def test_credentials_sts_endpoint_used_in_process_sts(self):
        _clear_oidc_envs()
        custom_endpoint = "https://custom-sts.example.com"
        responses.add(
            method=responses.POST,
            url=custom_endpoint + "/v5/agencies/assume-with-oidc",
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider(
            "basic",
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            sts_endpoint=custom_endpoint,
        )
        credentials = provider.get_credentials()
        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            assert credentials.ak == AK
            assert responses.calls[0].request.url.startswith(custom_endpoint)
        finally:
            http_client.close()

    @responses.activate
    def test_credentials_sts_endpoint_fallback_to_sts_helper(self):
        _clear_oidc_envs()
        os.environ.pop("HUAWEICLOUD_SDK_STS_ENDPOINT", None)
        default_url = StsHelper.DEFAULT_STS_ENDPOINT + "/v5/agencies/assume-with-oidc"
        responses.add(
            method=responses.POST,
            url=default_url,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider(
            "basic",
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
        )
        credentials = provider.get_credentials()
        assert credentials.sts_endpoint is None
        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            assert credentials.ak == AK
        finally:
            http_client.close()

    @responses.activate
    def test_with_sts_endpoint_method(self):
        _clear_oidc_envs()
        custom_endpoint = "https://manual-sts.example.com"
        responses.add(
            method=responses.POST,
            url=custom_endpoint + "/v5/agencies/assume-with-oidc",
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        provider = OidcStsCredentialProvider(
            "basic",
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
        )
        credentials = provider.get_credentials()
        credentials.with_sts_endpoint(custom_endpoint)
        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            assert credentials.ak == AK
            assert responses.calls[0].request.url.startswith(custom_endpoint)
        finally:
            http_client.close()

    def test_id_token_env_var(self):
        _set_oidc_envs()
        os.environ.pop("HUAWEICLOUD_OIDC_TOKEN_FILE", None)
        os.environ["HUAWEICLOUD_OIDC_ID_TOKEN"] = ID_TOKEN
        provider = OidcStsCredentialProvider.get_basic()
        credentials = provider.get_credentials()
        accessor = credentials.sts_accessor
        assert accessor._id_token == ID_TOKEN

    def test_policy_param(self):
        _clear_oidc_envs()
        policy = {"Version": "1.1", "Statement": [{"Effect": "Allow", "Action": ["*"], "Resource": ["*"]}]}
        provider = OidcStsCredentialProvider(
            "basic",
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            policy=policy,
        )
        credentials = provider.get_credentials()
        assert credentials.sts_accessor._policy == policy

    def test_policy_ids_param(self):
        _clear_oidc_envs()
        policy_ids = [{"id": "policy-id-1"}]
        provider = OidcStsCredentialProvider(
            "basic",
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
            policy_ids=policy_ids,
        )
        credentials = provider.get_credentials()
        assert credentials.sts_accessor._policy_ids == policy_ids

    def test_policy_env_var(self):
        _clear_oidc_envs()
        policy_json = '{"Version":"1.1","Statement":[{"Effect":"Allow","Action":["*"],"Resource":["*"]}]}'
        os.environ["HUAWEICLOUD_OIDC_POLICY"] = policy_json
        try:
            provider = OidcStsCredentialProvider(
                "basic",
                provider_urn=PROVIDER_URN,
                agency_urn=AGENCY_URN,
                id_token=ID_TOKEN,
                )
            credentials = provider.get_credentials()
            assert credentials.sts_accessor._policy == policy_json
        finally:
            os.environ.pop("HUAWEICLOUD_OIDC_POLICY", None)

    def test_policy_ids_env_var(self):
        _clear_oidc_envs()
        os.environ["HUAWEICLOUD_OIDC_POLICY_IDS"] = "policy-id-1, policy-id-2, "
        try:
            provider = OidcStsCredentialProvider(
                "basic",
                provider_urn=PROVIDER_URN,
                agency_urn=AGENCY_URN,
                id_token=ID_TOKEN,
                )
            credentials = provider.get_credentials()
            assert credentials.sts_accessor._policy_ids == ["policy-id-1", "policy-id-2"]
        finally:
            os.environ.pop("HUAWEICLOUD_OIDC_POLICY_IDS", None)

    def test_policy_programmatic_overrides_env(self):
        _clear_oidc_envs()
        os.environ["HUAWEICLOUD_OIDC_POLICY"] = '{"from_env": true}'
        try:
            policy = {"from_code": True}
            provider = OidcStsCredentialProvider(
                "basic",
                provider_urn=PROVIDER_URN,
                agency_urn=AGENCY_URN,
                id_token=ID_TOKEN,
                    policy=policy,
            )
            credentials = provider.get_credentials()
            assert credentials.sts_accessor._policy == policy
        finally:
            os.environ.pop("HUAWEICLOUD_OIDC_POLICY", None)

    def test_policy_ids_programmatic_overrides_env(self):
        _clear_oidc_envs()
        os.environ["HUAWEICLOUD_OIDC_POLICY_IDS"] = "env-id-1,env-id-2"
        try:
            policy_ids = [{"id": "code-id-1"}]
            provider = OidcStsCredentialProvider(
                "basic",
                provider_urn=PROVIDER_URN,
                agency_urn=AGENCY_URN,
                id_token=ID_TOKEN,
                    policy_ids=policy_ids,
            )
            credentials = provider.get_credentials()
            assert credentials.sts_accessor._policy_ids == policy_ids
        finally:
            os.environ.pop("HUAWEICLOUD_OIDC_POLICY_IDS", None)

    def test_programmatic_id_token_file(self):
        _clear_oidc_envs()
        provider = OidcStsCredentialProvider(
            "basic",
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token_file=TEST_TOKEN_FILE,
            agency_session_name=SESSION_NAME,
        )
        credentials = provider.get_credentials()
        accessor = credentials.sts_accessor
        assert accessor._id_token == TOKEN_FILE_CONTENT

    def test_programmatic_id_token_file_not_found(self):
        _clear_oidc_envs()
        provider = OidcStsCredentialProvider(
            "basic",
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token_file="/nonexistent/path/to/token.txt",
            agency_session_name=SESSION_NAME,
        )
        with pytest.raises(ApiValueError) as exc_info:
            provider.get_credentials()
        assert "does not exist" in str(exc_info.value)

    def test_unsupported_credential_type_raises(self):
        _clear_oidc_envs()
        provider = OidcStsCredentialProvider(
            "unsupported_type",
            provider_urn=PROVIDER_URN,
            agency_urn=AGENCY_URN,
            id_token=ID_TOKEN,
        )
        with pytest.raises(Exception):
            provider.get_credentials()

    def test_get_basic_alias(self):
        provider = OidcStsCredentialProvider.get_basic()
        assert isinstance(provider, OidcStsCredentialProvider)

    def test_get_global_alias(self):
        provider = OidcStsCredentialProvider.get_global()
        assert isinstance(provider, OidcStsCredentialProvider)


# ---------------------------------------------------------------------------
# 8. TestCredentialProviderChainWithOidc -- chain tests
# ---------------------------------------------------------------------------
class TestCredentialProviderChainWithOidc:
    def setup_method(self):
        _clear_oidc_envs()

    def teardown_method(self):
        _clear_oidc_envs()

    def test_oidc_is_first_in_basic_chain(self):
        chain = CredentialProviderChain.get_basic_credential_provider_chain()
        first_provider = chain._providers[0]
        assert isinstance(first_provider, OidcStsCredentialProvider)

    def test_oidc_is_first_in_global_chain(self):
        chain = CredentialProviderChain.get_global_credential_provider_chain()
        first_provider = chain._providers[0]
        assert isinstance(first_provider, OidcStsCredentialProvider)

    def test_oidc_is_first_in_default_chain(self):
        chain = CredentialProviderChain.get_default_credential_provider_chain("basic")
        first_provider = chain._providers[0]
        assert isinstance(first_provider, OidcStsCredentialProvider)

    def test_chain_falls_through_when_oidc_not_configured(self):
        _clear_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_AK"] = "ak"
        os.environ["HUAWEICLOUD_SDK_SK"] = "sk"
        chain = CredentialProviderChain.get_basic_credential_provider_chain()
        credentials = chain.get_credentials()
        assert isinstance(credentials, BasicCredentials)
        assert credentials.ak == "ak"
        assert credentials.sk == "sk"
        os.environ.pop("HUAWEICLOUD_SDK_AK", None)
        os.environ.pop("HUAWEICLOUD_SDK_SK", None)

    @responses.activate
    def test_chain_returns_oidc_when_configured(self):
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        chain = CredentialProviderChain.get_basic_credential_provider_chain()
        credentials = chain.get_credentials()
        assert isinstance(credentials, BasicCredentials)
        assert isinstance(credentials.sts_accessor, OidcStsAccessor)

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            assert credentials.ak == AK
        finally:
            http_client.close()

    def test_chain_all_providers_present(self):
        chain = CredentialProviderChain.get_basic_credential_provider_chain()
        assert isinstance(chain._providers[0], OidcStsCredentialProvider)
        assert isinstance(chain._providers[1], EnvCredentialProvider)
        assert isinstance(chain._providers[2], ProfileCredentialProvider)
        assert isinstance(chain._providers[3], MetadataCredentialProvider)
        assert isinstance(chain._providers[4], PodIdentityCredentialProvider)

    def test_chain_global_all_providers_present(self):
        chain = CredentialProviderChain.get_global_credential_provider_chain()
        assert isinstance(chain._providers[0], OidcStsCredentialProvider)
        assert isinstance(chain._providers[1], EnvCredentialProvider)
        assert isinstance(chain._providers[2], ProfileCredentialProvider)
        assert isinstance(chain._providers[3], MetadataCredentialProvider)
        assert isinstance(chain._providers[4], PodIdentityCredentialProvider)

    def test_chain_get_default_alias(self):
        chain = CredentialProviderChain.get_default("basic")
        assert isinstance(chain._providers[0], OidcStsCredentialProvider)

    def test_chain_default_global(self):
        chain = CredentialProviderChain.get_default_credential_provider_chain("global")
        assert isinstance(chain._providers[0], OidcStsCredentialProvider)


# ---------------------------------------------------------------------------
# 9. TestPatchProviderChain -- patch tests
# ---------------------------------------------------------------------------
class TestPatchProviderChain:
    def setup_method(self):
        _clear_oidc_envs()

    def teardown_method(self):
        _clear_oidc_envs()
        patch_provider_chain()

    def test_patch_inserts_oidc_as_first(self):
        patch_provider_chain()
        chain = CredentialProviderChain.get_basic_credential_provider_chain()
        assert isinstance(chain._providers[0], OidcStsCredentialProvider)

    def test_patch_global_inserts_oidc_as_first(self):
        patch_provider_chain()
        chain = CredentialProviderChain.get_global_credential_provider_chain()
        assert isinstance(chain._providers[0], OidcStsCredentialProvider)

    def test_patch_get_basic_alias(self):
        patch_provider_chain()
        chain = CredentialProviderChain.get_basic()
        assert isinstance(chain._providers[0], OidcStsCredentialProvider)

    def test_patch_get_global_alias(self):
        patch_provider_chain()
        chain = CredentialProviderChain.get_global()
        assert isinstance(chain._providers[0], OidcStsCredentialProvider)

    @responses.activate
    def test_patched_chain_works_with_oidc(self):
        patch_provider_chain()
        _set_oidc_envs()
        os.environ["HUAWEICLOUD_SDK_PROJECT_ID"] = PROJECT_ID
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        chain = CredentialProviderChain.get_basic()
        credentials = chain.get_credentials()
        assert isinstance(credentials.sts_accessor, OidcStsAccessor)

        http_client = _create_http_client()
        try:
            credentials.process_sts(http_client)
            assert credentials.ak == AK
        finally:
            http_client.close()


# ---------------------------------------------------------------------------
# 10. TestOidcCredentialProviderMain -- module import
# ---------------------------------------------------------------------------
class TestOidcCredentialProviderMain:
    def test_main_module_importable(self):
        import huaweicloudsdkcore.auth.provider as provider_module
        assert hasattr(provider_module, "OidcStsCredentialProvider")
        assert hasattr(provider_module, "patch_provider_chain")
        assert hasattr(provider_module, "CredentialProviderChain")

    def test_main_has_required_classes(self):
        assert OidcStsCredentialProvider is not None
        assert CredentialProviderChain is not None
        assert callable(patch_provider_chain)

    def test_provider_is_subclass_of_credential_provider(self):
        assert issubclass(OidcStsCredentialProvider, CredentialProvider)

    def test_init_none_credential_type_raises(self):
        with pytest.raises(ApiValueError) as exc_info:
            OidcStsCredentialProvider(None, provider_urn=PROVIDER_URN, agency_urn=AGENCY_URN, id_token=ID_TOKEN)
        assert "credential type is empty" in str(exc_info.value)

    def test_init_empty_credential_type_raises(self):
        with pytest.raises(ApiValueError) as exc_info:
            OidcStsCredentialProvider("", provider_urn=PROVIDER_URN, agency_urn=AGENCY_URN, id_token=ID_TOKEN)
        assert "credential type is empty" in str(exc_info.value)

    def test_init_uppercase_credential_type_normalized_to_lower(self):
        provider = OidcStsCredentialProvider(
            "BASIC", provider_urn=PROVIDER_URN, agency_urn=AGENCY_URN, id_token=ID_TOKEN
        )
        assert provider._credential_type == "basic"

    def test_init_global_uppercase_normalized(self):
        provider = OidcStsCredentialProvider(
            "GLOBAL", provider_urn=PROVIDER_URN, agency_urn=AGENCY_URN, id_token=ID_TOKEN
        )
        assert provider._credential_type == "global"


# ---------------------------------------------------------------------------
# 11. TestOidcStsAccessorEndpointResolution -- sts_endpoint variable rename
# ---------------------------------------------------------------------------
class TestOidcStsAccessorEndpointResolution:
    def setup_method(self):
        self.http_client = _create_http_client()

    def teardown_method(self):
        self.http_client.close()

    @responses.activate
    def test_endpoint_from_kwargs(self):
        custom_endpoint = "https://kwargs-sts.example.com"
        responses.add(
            method=responses.POST,
            url=custom_endpoint + "/v5/agencies/assume-with-oidc",
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN, agency_urn=AGENCY_URN, id_token=ID_TOKEN, agency_session_name=SESSION_NAME
        )
        credential = accessor.get_credential(http_client=self.http_client, sts_endpoint=custom_endpoint)
        assert credential.access == AK

    @responses.activate
    def test_endpoint_fallback_to_sts_helper(self):
        responses.add(
            method=responses.POST,
            url=OIDC_API_URL,
            content_type="application/json",
            body=OIDC_RESPONSE_BODY,
            status=200,
        )
        accessor = OidcStsAccessor(
            provider_urn=PROVIDER_URN, agency_urn=AGENCY_URN, id_token=ID_TOKEN, agency_session_name=SESSION_NAME
        )
        credential = accessor.get_credential(http_client=self.http_client)
        assert credential.access == AK

    @responses.activate
    def test_endpoint_kwargs_overrides_env(self):
        os.environ["HUAWEICLOUD_SDK_STS_ENDPOINT"] = "https://env-sts.example.com"
        try:
            custom_endpoint = "https://kwargs-override.example.com"
            responses.add(
                method=responses.POST,
                url=custom_endpoint + "/v5/agencies/assume-with-oidc",
                content_type="application/json",
                body=OIDC_RESPONSE_BODY,
                status=200,
            )
            accessor = OidcStsAccessor(
                provider_urn=PROVIDER_URN, agency_urn=AGENCY_URN, id_token=ID_TOKEN, agency_session_name=SESSION_NAME
            )
            accessor.get_credential(http_client=self.http_client, sts_endpoint=custom_endpoint)
            assert responses.calls[0].request.url.startswith(custom_endpoint)
        finally:
            os.environ.pop("HUAWEICLOUD_SDK_STS_ENDPOINT", None)


if __name__ == "__main__":
    pytest.main()
