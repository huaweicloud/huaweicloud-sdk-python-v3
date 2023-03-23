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

import json
from abc import abstractmethod

import six

from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import six_utils


class ExceptionHandler(six_utils.get_abstract_meta_class()):
    @abstractmethod
    def handle_exception(self, request, response):
        pass


class DefaultExceptionHandler(ExceptionHandler):
    _X_REQUEST_ID = "X-Request-Id"
    _CODE = "code"
    _MESSAGE = "message"
    _ERROR_CODE = "error_code"
    _ERROR_MSG = "error_msg"
    _ENCODED_AUTHORIZATION_MESSAGE = "encoded_authorization_message"

    def handle_exception(self, request, response):
        request_id = response.headers.get(self._X_REQUEST_ID)
        sdk_error = exceptions.SdkError(request_id=request_id)
        try:
            sdk_error_dict = json.loads(response.text)
            if isinstance(sdk_error_dict, dict):
                self._process_sdk_error(sdk_error, sdk_error_dict)
            else:
                sdk_error.error_msg = response.text
        except json.JSONDecodeError:
            sdk_error.error_msg = response.text
        except Exception:
            sdk_error.error_msg = six.ensure_str(response.text)
            raise exceptions.ServerResponseException(response.status_code, sdk_error)

        if not sdk_error.error_msg:
            sdk_error.error_msg = response.text
        return sdk_error

    @classmethod
    def _process_sdk_error(cls, sdk_error, sdk_error_dict):
        if cls._ENCODED_AUTHORIZATION_MESSAGE in sdk_error_dict:
            sdk_error.encoded_authorization_message = sdk_error_dict.get(cls._ENCODED_AUTHORIZATION_MESSAGE)

        if cls._ERROR_CODE in sdk_error_dict and cls._ERROR_MSG in sdk_error_dict:
            sdk_error.error_code = sdk_error_dict.get(cls._ERROR_CODE)
            sdk_error.error_msg = sdk_error_dict.get(cls._ERROR_MSG)
            return

        if cls._CODE in sdk_error_dict and cls._MESSAGE in sdk_error_dict:
            sdk_error.error_code = sdk_error_dict.get(cls._CODE)
            sdk_error.error_msg = sdk_error_dict.get(cls._MESSAGE)
            return

        for value in sdk_error_dict.values():
            if not isinstance(value, dict):
                continue
            cls._process_sdk_error(sdk_error, value)
