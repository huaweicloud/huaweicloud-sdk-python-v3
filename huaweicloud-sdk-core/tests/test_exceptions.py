# coding: utf-8
"""
 Copyright 2025 Huawei Technologies Co.,Ltd.

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

from huaweicloudsdkcore.exceptions.exceptions import SdkException, SdkError, ServiceResponseException


def test_new_sdk_exception():
    exc = SdkException(error_msg="error_msg")
    assert exc.error_msg == "error_msg"


def test_new_service_response_exception():
    error = SdkError()
    error.request_id = "request_id"
    error.error_code = "error_code"
    error.error_msg = "error_msg"
    error.encoded_auth_msg = "encoded_auth_msg"

    assert error.request_id == "request_id"
    assert error.error_code == "error_code"
    assert error.error_msg == "error_msg"
    assert error.encoded_auth_msg == "encoded_auth_msg"

    exc = ServiceResponseException(status_code=400, sdk_error=error)

    assert exc.request_id == "request_id"
    assert exc.error_code == "error_code"
    assert exc.error_msg == "error_msg"
    assert exc.encoded_auth_msg == "encoded_auth_msg"
    assert exc.status_code == 400
