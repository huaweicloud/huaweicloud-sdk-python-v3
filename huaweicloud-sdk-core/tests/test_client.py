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
import random
import pytest
import responses
from responses import matchers

from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.sdk_response import SdkResponse

from tests.model.vpc import Vpc, Route


class MockSdkResponse(SdkResponse):
    openapi_types = {}
    attribute_map = {}


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as resps:
        yield resps


@pytest.fixture
def mocked_client():
    credentials = random.choice([
        BasicCredentials("ak", "sk", "project_id"),
        GlobalCredentials("ak", "sk", "domain_id"),
    ])
    client = (Client()
              .with_credentials(credentials)
              .with_config(HttpConfig.get_default_config())
              .with_endpoints(["https://example.com"]))
    client.init_http_client()
    yield client
    client.close()


def test_application_json(mocked_responses, mocked_client):
    mocked_responses.add(
        method=responses.POST,
        url="https://example.com/test-content-type/application-json",
        match=[
            matchers.header_matcher({"Content-Type": "application/json"}),
            matchers.json_params_matcher({
                'cidr': 'cidr',
                'description': 'description',
                'id': 'id',
                'name': 'name',
                'routes': [
                    {
                        'destination': 'destination',
                        'nexthop': 'nexthop'
                    }
                ],
                'status': 'status'
            })
        ]
    )

    route = Route(destination="destination", nexthop='nexthop')
    vpc = Vpc(id="id", name="name", cidr="cidr", description="description", routes=[route], status="status")
    mocked_client.do_http_request(method="POST",
                                  header_params={"Content-Type": "application/json"},
                                  resource_path="/test-content-type/application-json",
                                  response_type=MockSdkResponse,
                                  body=vpc)


def test_form_urlencoded(mocked_responses, mocked_client):
    mocked_responses.add(
        method=responses.POST,
        url="https://example.com/test-content-type/x-www-form-urlencoded",
        match=[
            matchers.header_matcher({"Content-Type": "application/x-www-form-urlencoded"}),
            matchers.urlencoded_params_matcher({"str": "val", "int": "1", "bool": "true"})
        ]
    )

    mocked_client.do_http_request(method="POST",
                                  header_params={"Content-Type": "application/x-www-form-urlencoded"},
                                  resource_path="/test-content-type/x-www-form-urlencoded",
                                  response_type=MockSdkResponse,
                                  body={"str": "val", "int": 1, "bool": True})


def test_build_request_without_authorization(mocked_client):
    request = mocked_client.build_future_request(
        method="GET",
        resource_path="/resources",
        path_params={},
        query_params=[("size", "1")],
        header_params={},
        request_body=None,
        post_params={},
        cname=None,
        response_type=None,
        collection_formats={},
        progress_callback=None
    ).result()

    assert request.method == "GET"
    assert request.host == "example.com"
    assert request.query_params == [("size", "1")]
    assert request.resource_path == "/resources"
    assert request.schema == "https"
    assert request.uri == "/resources?size=1"
    assert request.url == "https://example.com/resources?size=1"
    assert "Authorization" in request.header_params


def test_build_request_with_authorization(mocked_client):
    request = mocked_client.build_future_request(
        method="GET",
        resource_path="/resources",
        path_params={},
        query_params=[("size", "1")],
        header_params={"Authorization": "test"},
        request_body=None,
        post_params={},
        cname=None,
        response_type=None,
        collection_formats={},
        progress_callback=None
    ).result()

    assert request.method == "GET"
    assert request.host == "example.com"
    assert request.query_params == [("size", "1")]
    assert request.resource_path == "/resources"
    assert request.schema == "https"
    assert request.uri == "/resources?size=1"
    assert request.url == "https://example.com/resources?size=1"
    assert "Authorization" in request.header_params


def test_build_request_with_ua_in_headers(mocked_client):
    request = mocked_client.build_future_request(
        method="GET",
        resource_path="/user-agent",
        path_params={},
        query_params=[("size", "1")],
        header_params={"User-Agent": "test"},
        request_body=None,
        post_params={},
        cname=None,
        response_type=None,
        collection_formats={},
        progress_callback=None
    ).result()

    assert request.header_params.get("User-Agent") == "huaweicloud-usdk-python/3.0; test"


if __name__ == '__main__':
    pytest.main()
