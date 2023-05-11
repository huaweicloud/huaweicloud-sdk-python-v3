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
from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.http.http_config import HttpConfig
from tests.mocker.project_response_mocker import MOCK_ENDPOINT, mock_keystone_list_projects
from tests.test_region_with_project_id import ServiceRegion

REGION_ID = "cn-north-7"


def test_project_id_with_region(mocker):
    mock_credential = BasicCredentials("ak", "sk").with_iam_endpoint(MOCK_ENDPOINT)
    client = Client().with_credentials(mock_credential).with_config(HttpConfig.get_default_config())
    client.init_http_client()
    http_client = client.get_http_client()

    mocker.patch.object(http_client, 'do_request_sync', return_value=mock_keystone_list_projects(REGION_ID))

    result_credential = mock_credential.process_auth_params(http_client, ServiceRegion.CN_NORTH_7.id)
    assert result_credential.project_id == "123456789"


def test_project_id_with_value_of(mocker):
    mock_credential = BasicCredentials("ak", "sk").with_iam_endpoint(MOCK_ENDPOINT)
    client = Client().with_credentials(mock_credential).with_config(HttpConfig.get_default_config())
    client.init_http_client()
    http_client = client.get_http_client()

    mocker.patch.object(http_client, 'do_request_sync', return_value=mock_keystone_list_projects(REGION_ID))

    result_credential = mock_credential.process_auth_params(http_client, ServiceRegion.value_of("cn-north-7").id)
    assert result_credential.project_id == "123456789"


if __name__ == "__main__":
    pytest.main()
