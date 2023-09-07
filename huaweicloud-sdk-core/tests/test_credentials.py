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
from huaweicloudsdkcore.signer.algorithm import SigningAlgorithm

from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.sdk_request import SdkRequest


@pytest.fixture()
def sdk_request():
    yield SdkRequest(schema="https", host="service.region-1.com", resource_path="/test",
                     header_params={}, query_params=[], signing_algorithm=SigningAlgorithm.get_default())


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


if __name__ == '__main__':
    pytest.main()
