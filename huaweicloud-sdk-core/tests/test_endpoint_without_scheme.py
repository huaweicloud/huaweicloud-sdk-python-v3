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
from tests.data.project_response_mocker import MOCK_ENDPOINT, MOCK_ENDPOINT_WITHOUT_SCHEME
from tests.model.service.service_client import ServiceClient

config = HttpConfig.get_default_config()
config.ignore_ssl_verification = True

credentials = BasicCredentials("ak", "sk", "project_id")


def test_endpoint_without_scheme():
    client = ServiceClient.new_builder() \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(MOCK_ENDPOINT_WITHOUT_SCHEME) \
        .build()

    assert hasattr(client, "_endpoint") is True
    assert getattr(client, "_endpoint") == MOCK_ENDPOINT


if __name__ == "__main__":
    pytest.main()
