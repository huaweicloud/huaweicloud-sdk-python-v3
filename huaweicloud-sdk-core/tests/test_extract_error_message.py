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

from huaweicloudsdkcore.exceptions.exception_handler import DefaultExceptionHandler

EXCEPTION_HANDLER = DefaultExceptionHandler()


class MockResponse(object):
    def __init__(self, text):
        self.text = text
        self.status_code = 400
        self.headers = {"X-Request-Id": "97e2***11df"}


def test_extract_error_message1():
    error_message = '{"error_code": "XXX.0001", ' \
                    '"error_msg": "Some errors occurred.", ' \
                    '"encoded_authorization_message": "Egpjbi1ub*****GoxMzgrcA=="}'
    response = MockResponse(error_message)
    sdk_error = EXCEPTION_HANDLER.handle_exception(None, response)
    assert "Egpjbi1ub*****GoxMzgrcA==" == sdk_error.encoded_authorization_message
    assert "XXX.0001" == sdk_error.error_code
    assert "Some errors occurred." == sdk_error.error_msg
    assert "97e2***11df" == sdk_error.request_id


def test_extract_error_message2():
    error_message = '{"error": ' \
                    '{"code": "XXX.0001", ' \
                    '"message": "Some errors occurred.", ' \
                    '"encoded_authorization_message": "Egpjbi1ub*****GoxMzgrcA=="}}'
    response = MockResponse(error_message)
    sdk_error = EXCEPTION_HANDLER.handle_exception(None, response)
    assert "Egpjbi1ub*****GoxMzgrcA==" == sdk_error.encoded_authorization_message
    assert "XXX.0001" == sdk_error.error_code
    assert "Some errors occurred." == sdk_error.error_msg
    assert "97e2***11df" == sdk_error.request_id


def test_extract_error_message3():
    error_message = '{"error": ' \
                    '{"code": "XXX.0001", ' \
                    '"message": "Some errors occurred."}, ' \
                    '"error_code": "XXX.0001", "error_msg": "Some errors occurred.", ' \
                    '"encoded_authorization_message": "Egpjbi1ub*****GoxMzgrcA=="}'
    response = MockResponse(error_message)
    sdk_error = EXCEPTION_HANDLER.handle_exception(None, response)
    assert "Egpjbi1ub*****GoxMzgrcA==" == sdk_error.encoded_authorization_message
    assert "XXX.0001" == sdk_error.error_code
    assert "Some errors occurred." == sdk_error.error_msg
    assert "97e2***11df" == sdk_error.request_id


def test_extract_error_message4():
    error_message = '{"invalid_key":"invalid_value"}'
    response = MockResponse(error_message)
    sdk_error = EXCEPTION_HANDLER.handle_exception(None, response)
    assert sdk_error.encoded_authorization_message is None
    assert sdk_error.error_code is None
    assert '{"invalid_key":"invalid_value"}' == sdk_error.error_msg
    assert "97e2***11df" == sdk_error.request_id


def test_extract_error_message5():
    error_message = "invalid json data"
    response = MockResponse(error_message)
    sdk_error = EXCEPTION_HANDLER.handle_exception(None, response)
    assert sdk_error.encoded_authorization_message is None
    assert sdk_error.error_code is None
    assert "invalid json data" == sdk_error.error_msg
    assert "97e2***11df" == sdk_error.request_id


if __name__ == '__main__':
    pytest.main()
