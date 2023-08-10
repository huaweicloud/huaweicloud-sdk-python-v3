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

import pytest

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions.exceptions import SdkException
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer.signer import Signer, DerivationAKSKSigner, SM3Signer


@pytest.fixture()
def credentials():
    ak = "my ak"
    sk = "my sk"
    project_id = "my project_id"

    credentials = BasicCredentials(ak, sk, project_id)
    yield credentials


@pytest.fixture()
def sdk_request_get():
    sdk_request = SdkRequest(method="GET",
                             schema="https",
                             host="service.endpoint.myhuaweicloud.com",
                             resource_path="/resources",
                             query_params=[("size", "1")],
                             header_params={"X-Sdk-Date": "20200608T023900Z"},
                             body="")
    yield sdk_request


@pytest.fixture()
def sdk_request_post():
    sdk_request = SdkRequest(method="POST",
                             schema="https",
                             host="service.endpoint.myhuaweicloud.com",
                             resource_path="/resources",
                             query_params=[("size", "1")],
                             header_params={"X-Sdk-Date": "20200608T023900Z"},
                             body='{"name":"test","id":1}')
    yield sdk_request


def test_signer1(credentials, sdk_request_get):
    signer = Signer(credentials)
    signed_request = signer.sign(sdk_request_get)

    assert 'SDK-HMAC-SHA256 Access=my ak, SignedHeaders=host;x-sdk-date, ' \
           'Signature=6d5bc610d3d4475346aae5cd7ed8d99585e60c0430a1d3d6e2f54e2bdd633701' \
           == signed_request.header_params.get("Authorization")


def test_signer2(credentials, sdk_request_post):
    signer = Signer(credentials)
    signed_request = signer.sign(sdk_request_post)

    assert 'SDK-HMAC-SHA256 Access=my ak, SignedHeaders=host;x-sdk-date, ' \
           'Signature=098f9cbfb49f136e1eaa5cfdbb26558fcac157dc8b1f0e0f4be473ac09d02e9e' \
           == signed_request.header_params.get("Authorization")


def test_sm3_signer1(credentials, sdk_request_get):
    signer = SM3Signer(credentials)
    try:
        signed_request = signer.sign(sdk_request_get)

        assert 'SDK-HMAC-SM3 Access=my ak, SignedHeaders=host;x-sdk-date, ' \
               'Signature=bfa9c2049174fc9e2ebb9855fab2049dd1d7262de0b5bc21f6405423e7ebb53d' \
               == signed_request.header_params.get("Authorization")
    except SdkException as e:
        assert "Signing algorithm SM3 is not supported in python2" == e.error_msg


def test_sm3_signer2(credentials, sdk_request_post):
    signer = SM3Signer(credentials)
    try:
        signed_request = signer.sign(sdk_request_post)

        assert 'SDK-HMAC-SM3 Access=my ak, SignedHeaders=host;x-sdk-date, ' \
               'Signature=0bb9634b69817571c959deea4413df9fd00a461a03c226d950ac73f60b0727eb' \
               == signed_request.header_params.get("Authorization")
    except SdkException as e:
        assert "Signing algorithm SM3 is not supported in python2" == e.error_msg


def test_derived_signer1(credentials, sdk_request_get):
    signer = DerivationAKSKSigner(credentials)
    signed_request = signer.sign(sdk_request_get, derived_auth_service_name="demo", region_id="test-region-1")

    assert 'V11-HMAC-SHA256 Credential=my ak/20200608/test-region-1/demo, SignedHeaders=host;x-sdk-date, ' \
           'Signature=8f6ebdb305dedff8778a5dd3eefdcbe36698bdd63114676c6853413cfe494548' \
           == signed_request.header_params.get("Authorization")


def test_derived_signer2(credentials, sdk_request_post):
    signer = DerivationAKSKSigner(credentials)
    signed_request = signer.sign(sdk_request_post, derived_auth_service_name="demo", region_id="test-region-1")

    assert 'V11-HMAC-SHA256 Credential=my ak/20200608/test-region-1/demo, SignedHeaders=host;x-sdk-date, ' \
           'Signature=14cd56621f3bb36a382e079531388f21e2a4f1555e386ef2769eeb8dcd3840aa' \
           == signed_request.header_params.get("Authorization")


if __name__ == "__main__":
    pytest.main()
