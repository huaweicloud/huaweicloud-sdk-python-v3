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

import pytest

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.region.region import Region
from tests.mocker.project_response_mocker import MOCK_ENDPOINT
from tests.model.service.service_client import ServiceClient
from tests.model.service.service_region import ServiceRegion

OVERRIDE_ENDPOINT = "https://service.cn-north-x.myhuaweicloud.com"

config = HttpConfig.get_default_config()
config.ignore_ssl_verification = True

credentials = BasicCredentials("ak", "sk", "project_id")


def test_endpoint_with_region_1():
    client = ServiceClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_region(ServiceRegion.CN_NORTH_7) \
        .build()

    assert hasattr(client, "_endpoints") is True
    assert getattr(client, "_endpoints")[0] == MOCK_ENDPOINT


def test_endpoint_with_region_2():
    client = ServiceClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_region(ServiceRegion.value_of("cn-north-7")) \
        .build()

    assert hasattr(client, "_endpoints") is True
    assert getattr(client, "_endpoints")[0] == MOCK_ENDPOINT


def test_endpoint_with_region_3():
    client = ServiceClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_region(Region("cn-north-7", MOCK_ENDPOINT)) \
        .build()

    assert hasattr(client, "_endpoints") is True
    assert getattr(client, "_endpoints")[0] == MOCK_ENDPOINT


def test_endpoint_with_region_override_1():
    client = ServiceClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_region(ServiceRegion.CN_NORTH_7.with_endpoint_override(OVERRIDE_ENDPOINT)) \
        .build()

    assert hasattr(client, "_endpoints") is True
    assert getattr(client, "_endpoints")[0] == OVERRIDE_ENDPOINT


def test_endpoint_with_region_override_2():
    client = ServiceClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_region(ServiceRegion.value_of("cn-north-7").with_endpoint_override(OVERRIDE_ENDPOINT)) \
        .build()

    assert hasattr(client, "_endpoints") is True
    assert getattr(client, "_endpoints")[0] == OVERRIDE_ENDPOINT


def test_region_value_of_empty():
    try:
        ServiceClient.new_builder() \
            .with_http_config(config) \
            .with_credentials(credentials) \
            .with_region(ServiceRegion.value_of("")) \
            .build()
    except KeyError as e:
        assert e.args[0] == "Unexpected empty parameter: regionId."


def test_region_value_of_wrong():
    try:
        ServiceClient.new_builder() \
            .with_http_config(config) \
            .with_credentials(credentials) \
            .with_region(ServiceRegion.value_of("cn-north-404")) \
            .build()
    except KeyError as e:
        assert e.args[0] == "Unexpected regionId: cn-north-404"


if __name__ == "__main__":
    pytest.main()
