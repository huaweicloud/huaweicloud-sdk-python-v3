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
import hashlib

import ecdsa
import pytest
from ecdsa.util import sigencode_der, sigdecode_der

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions.exceptions import SdkException
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer.gm import SM2SigningKey
from huaweicloudsdkcore.signer.signer import Signer, DerivationAKSKSigner, SM3Signer, P256SHA256Signer, SM2SM3Signer


@pytest.fixture()
def credentials():
    ak = "AccessKey"
    sk = "SecretKey"
    project_id = "ProjectId"

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

    assert 'SDK-HMAC-SHA256 Access=AccessKey, SignedHeaders=host;x-sdk-date, ' \
           'Signature=cfb4171acec81de07d50e53d57eb77edd537414d66ddb1d7d780f128e12cd842' \
           == signed_request.header_params.get("Authorization")


def test_signer2(credentials, sdk_request_post):
    signer = Signer(credentials)
    signed_request = signer.sign(sdk_request_post)

    assert 'SDK-HMAC-SHA256 Access=AccessKey, SignedHeaders=host;x-sdk-date, ' \
           'Signature=436b1ac0a1ae03705934bb70ef2f2e09f7bfed2117d731a38235053199323a1f' \
           == signed_request.header_params.get("Authorization")


def test_sm3_signer1(credentials, sdk_request_get):
    signer = SM3Signer(credentials)
    try:
        signed_request = signer.sign(sdk_request_get)

        assert 'SDK-HMAC-SM3 Access=AccessKey, SignedHeaders=host;x-sdk-date, ' \
               'Signature=f8ceb623f0be123dbccd7ad95a6211470f170d1d3c4fa9facbce716d82190e21' \
               == signed_request.header_params.get("Authorization")
    except SdkException as e:
        assert "Signing algorithm SM3 is not supported in python2" == e.error_msg


def test_sm3_signer2(credentials, sdk_request_post):
    signer = SM3Signer(credentials)
    try:
        signed_request = signer.sign(sdk_request_post)

        assert 'SDK-HMAC-SM3 Access=AccessKey, SignedHeaders=host;x-sdk-date, ' \
               'Signature=6521b276625d7870e9836c041bafb2fa8d6a7ed0df045b06f1b137243c050ed8' \
               == signed_request.header_params.get("Authorization")
    except SdkException as e:
        assert "Signing algorithm SM3 is not supported in python2" == e.error_msg


def test_derived_signer1(credentials, sdk_request_get):
    signer = DerivationAKSKSigner(credentials)
    signed_request = signer.sign(sdk_request_get, derived_auth_service_name="demo", region_id="test-region-1")

    assert 'V11-HMAC-SHA256 Credential=AccessKey/20200608/test-region-1/demo, ' \
           'SignedHeaders=host;x-sdk-date, Signature=f7dfee056692e58dede80fc80cb89bbfabf45552dd7cd8d18a0a13484455b98e' \
           == signed_request.header_params.get("Authorization")


def test_derived_signer2(credentials, sdk_request_post):
    signer = DerivationAKSKSigner(credentials)
    signed_request = signer.sign(sdk_request_post, derived_auth_service_name="demo", region_id="test-region-1")

    assert 'V11-HMAC-SHA256 Credential=AccessKey/20200608/test-region-1/demo, ' \
           'SignedHeaders=host;x-sdk-date, Signature=8e2d91eaf9656ec5d6fab27812e2d898a35aaaa5e16ee0a0365c38527ccfb3cf' \
           == signed_request.header_params.get("Authorization")


def test_p256_signing_key(credentials):
    signer = P256SHA256Signer(credentials)

    signing_key = signer.get_signing_key()
    assert isinstance(signing_key, ecdsa.SigningKey)

    data = b'HelloWorld'
    signature = signing_key.sign(data, hashfunc=hashlib.sha256, sigencode=sigencode_der)

    public_key = signing_key.get_verifying_key()
    assert public_key.verify(signature, data, hashfunc=hashlib.sha256, sigdecode=sigdecode_der)


def test_sm2_signing_key(credentials):
    signer = SM2SM3Signer(credentials)

    signing_key = signer.get_signing_key()
    assert isinstance(signing_key, SM2SigningKey)

    data = b'HelloWorld'
    signature = signing_key.sign(data)
    assert signing_key.verify(signature, data)


def test_p256_sha256_signer1(credentials, sdk_request_get):
    signer = P256SHA256Signer(credentials)
    signed_request = signer.sign(sdk_request_get)

    assert signed_request.header_params.get("Authorization").startswith("SDK-ECDSA-P256-SHA256")


def test_p256_sha256_signer2(credentials, sdk_request_post):
    signer = P256SHA256Signer(credentials)
    signed_request = signer.sign(sdk_request_post)

    assert signed_request.header_params.get("Authorization").startswith("SDK-ECDSA-P256-SHA256")


def test_sm2_sm3_signer1(credentials, sdk_request_get):
    signer = SM2SM3Signer(credentials)
    signed_request = signer.sign(sdk_request_get)

    assert signed_request.header_params.get("Authorization").startswith("SDK-SM2-SM3")


def test_sm2_sm3_signer2(credentials, sdk_request_post):
    signer = SM2SM3Signer(credentials)
    signed_request = signer.sign(sdk_request_post)

    assert signed_request.header_params.get("Authorization").startswith("SDK-SM2-SM3")


if __name__ == "__main__":
    pytest.main()
