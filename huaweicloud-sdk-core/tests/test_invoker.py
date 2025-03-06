# coding: utf-8
"""
 Copyright 2024 Huawei Technologies Co.,Ltd.

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

import pytest
import responses
from responses import matchers

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions.exceptions import ServerResponseException
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.invoker.invoker import SyncInvoker
from huaweicloudsdkcore.retry.backoff_strategy import BackoffStrategies
from huaweicloudsdkcore.sdk_response import SdkResponse

try:
    from responses.registries import OrderedRegistry
except ImportError:
    from responses.registries import FirstMatchRegistry


    class OrderedRegistry(FirstMatchRegistry):
        """
        responses-0.17.0(earlier than python3.8) does not have OrderedRegistry,
        the class is copied from responses-0.25.3(python 3.8+ required).
        """

        def find(self, request):
            if not self.registered:
                return None, ["No more registered responses"]

            response = self.registered.pop(0)
            match_result, reason = response.matches(request)
            if not match_result:
                self.reset()
                self.add(response)
                reason = (
                    "Next 'Response' in the order doesn't match "
                    f"due to the following reason: {reason}."
                )
                return None, [reason]

            return response, []


class MockSdkResponse(SdkResponse):
    openapi_types = {}
    attribute_map = {}


@pytest.fixture
def mocked_client():
    client = (Client()
              .with_credentials(BasicCredentials("ak", "sk", "project_id"))
              .with_config(HttpConfig.get_default_config())
              .with_endpoints(["https://example.com"]))
    client.init_http_client()
    yield client
    client.close()


@responses.activate
def test_invoker_add_header(mocked_client):
    responses.add(
        method=responses.GET,
        url="https://example.com/invoker/headers",
        match=[
            matchers.header_matcher({"x-test-header": "test-value"}),
        ]
    )
    http_info = {
        "method": "GET",
        "resource_path": "/invoker/headers",
        "response_type": MockSdkResponse,
        "path_params": {},
        "query_params": [],
        "header_params": {},
    }
    (SyncInvoker(mocked_client, http_info)
     .add_header("x-test-header", "test-value")
     .invoke())


class TestRetry(object):
    URL = "https://example.com/invoker/retry"

    @classmethod
    def mock_http_info(cls):
        return {
            "method": "GET",
            "resource_path": "/invoker/retry",
            "response_type": MockSdkResponse,
            "path_params": {},
            "query_params": [],
            "header_params": {},
        }

    @responses.activate
    def test_retry(self, mocked_client):
        """
        当发生ServerResponseException(status_code>=500)时进行重试,最大重试次数设置为3
        预期状态码为502,调用次数为4(正常调用1次+请求重试3次)
        """
        responses.add(responses.GET, self.URL, status=502)
        try:
            (SyncInvoker(mocked_client, self.mock_http_info()).
             with_retry(retry_condition=lambda _, exc: isinstance(exc, ServerResponseException),
                        max_retries=3,
                        backoff_strategy=BackoffStrategies.NONE)
             .invoke())
            assert False, "should have raised ServerResponseException"
        except ServerResponseException as e:
            assert e.status_code == 502
            assert responses.assert_call_count(self.URL, 4)

    @responses.activate(registry=OrderedRegistry)
    def test_retry2(self, mocked_client):
        """
        当发生ServerResponseException(status_code>=500)时进行重试,最大重试次数设置为10,在第二次重试服务恢复正常
        预期状态码为200,调用次数为3(正常调用1次+请求重试2次)
        """
        # first invoke
        responses.add(responses.GET, self.URL, status=502)
        # first retry
        responses.add(responses.GET, self.URL, status=502)
        responses.add(responses.GET, self.URL, status=200)

        resp = (SyncInvoker(
            client=mocked_client,
            http_info=self.mock_http_info()
        ).with_retry(retry_condition=lambda _, exc: isinstance(exc, ServerResponseException),
                     max_retries=10,
                     backoff_strategy=BackoffStrategies.NONE)
                .invoke())
        assert resp.status_code == 200
        assert responses.assert_call_count(self.URL, 3)

    @responses.activate(registry=OrderedRegistry)
    def test_retry3(self, mocked_client):
        """
        在刚好达到最大重试次数时请求成功
        预期状态码为200,调用次数为3(正常调用1次+请求重试2次)
        """
        # first invoke
        responses.add(responses.GET, self.URL, status=502)
        # first retry
        responses.add(responses.GET, self.URL, status=502)
        responses.add(responses.GET, self.URL, status=200)

        resp = (SyncInvoker(mocked_client, self.mock_http_info()).
                with_retry(retry_condition=lambda _, exc: isinstance(exc, ServerResponseException),
                           max_retries=10,
                           backoff_strategy=BackoffStrategies.NONE)
                .invoke())
        assert resp.status_code == 200
        assert responses.assert_call_count(self.URL, 3)

    @responses.activate(registry=OrderedRegistry)
    def test_retry4(self, mocked_client):
        """
        消息体内容为空进行重试,第三次调用返回非空内容
        预期状态码为200,调用次数为3(正常调用1次+请求重试2次)
        """
        headers = {"Content-Type": "application/json"}
        # first invoke
        responses.add(responses.GET, self.URL, headers=headers, json=[])
        # first retry
        responses.add(responses.GET, self.URL, headers=headers, json=[])
        responses.add(responses.GET, self.URL, headers=headers, json=[1, 2, 3])

        def retry_condition(resp, _):
            if not resp and not resp.raw_content:
                return False
            content = json.loads(resp.raw_content)
            return not content

        response = (SyncInvoker(
            client=mocked_client,
            http_info=self.mock_http_info()
        ).with_retry(retry_condition=retry_condition,
                     max_retries=5,
                     backoff_strategy=BackoffStrategies.NONE)
                    .invoke())
        assert response.status_code == 200
        assert responses.assert_call_count(self.URL, 3)

    @responses.activate
    def test_retry5(self, mocked_client):
        """
        消息体内容为空进行重试
        预期状态码为200,调用次数为6（正常调用1次+请求重试5次）
        """
        headers = {"Content-Type": "application/json"}
        responses.add(responses.GET, self.URL, headers=headers, json=[])

        def retry_condition(resp, _):
            if not resp and not resp.raw_content:
                return False
            content = json.loads(resp.raw_content)
            return not content

        response = (SyncInvoker(
            client=mocked_client,
            http_info=self.mock_http_info()
        ).with_retry(retry_condition=retry_condition,
                     max_retries=5,
                     backoff_strategy=BackoffStrategies.NONE)
                    .invoke())
        assert response.status_code == 200
        assert response.raw_content == b"[]"
        assert responses.assert_call_count(self.URL, 6)

    @responses.activate
    def test_retry6(self, mocked_client):
        """
        请求重试一次，预期调用次数为2(正常调用1次+请求重试1次)
        """
        responses.add(responses.GET, self.URL, status=502)
        try:
            (SyncInvoker(mocked_client, self.mock_http_info()).
             with_retry(retry_condition=lambda _, exc: isinstance(exc, ServerResponseException),
                        max_retries=1,
                        backoff_strategy=BackoffStrategies.NONE)
             .invoke())
            assert False, "should have raised ServerResponseException"
        except ServerResponseException as e:
            assert e.status_code == 502
            assert responses.assert_call_count(self.URL, 2)

    @responses.activate
    def test_retry7(self, mocked_client):
        """
        不满足重试条件不进行重试
        """
        responses.add(responses.GET, self.URL, status=502)
        try:
            (SyncInvoker(mocked_client, self.mock_http_info()).
             with_retry(retry_condition=lambda _, exc: False,
                        max_retries=10,
                        backoff_strategy=BackoffStrategies.NONE)
             .invoke())
            assert False, "should have raised ServerResponseException"
        except ServerResponseException as e:
            assert e.status_code == 502
            assert responses.assert_call_count(self.URL, 1)


if __name__ == "__main__":
    pytest.main()
