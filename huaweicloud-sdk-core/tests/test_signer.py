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
from huaweicloudsdkcore.sdk_request import SdkRequest
from huaweicloudsdkcore.signer.signer import Signer


@pytest.fixture()
def credentials():
    ak = "my ak"
    sk = "my sk"
    project_id = "my project_id"

    credentials = BasicCredentials(ak, sk, project_id)
    yield credentials


@pytest.fixture()
def sdk_request():
    sdk_request = SdkRequest(method="GET",
                             schema="https",
                             host="service.endpoint.myhuaweicloud.com",
                             resource_path="/resources",
                             query_params=[("size", "1")],
                             header_params={"X-Sdk-Date": "20200608T023900Z"},
                             body="")
    yield sdk_request


def test_signer(credentials, sdk_request):
    signer = Signer(credentials)
    signed_request = signer.sign(sdk_request)
    print(signed_request)

    assert signed_request.header_params.get("Authorization") == \
           'SDK-HMAC-SHA256 Access=my ak, ' \
           'SignedHeaders=host;x-sdk-date, ' \
           'Signature=6d5bc610d3d4475346aae5cd7ed8d99585e60c0430a1d3d6e2f54e2bdd633701'


if __name__ == "__main__":
    pytest.main()
