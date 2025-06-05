# coding: utf-8
"""
 Copyright 2023 Huawei Technologies Co.,Ltd.

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
from requests import Request, Response
from urllib3.exceptions import SSLError, NewConnectionError

from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import six_utils


class ExceptionHandler(six_utils.get_abstract_meta_class()):
    @abstractmethod
    def handle_exception(self, request, response):
        # type: (Request|object, Response|object) -> None
        pass


class DefaultExceptionHandler(ExceptionHandler):
    _X_REQUEST_ID = "X-Request-Id"
    _CODE = "code"
    _MESSAGE = "message"
    _ERROR_CODE = "error_code"
    _ERROR_MSG = "error_msg"
    _ERROR_CODE_CAMEL = "errorCode"
    _ERROR_MSG_CAMEL = "errorMsg"
    _ENCODED_AUTHORIZATION_MESSAGE = "encoded_authorization_message"

    def handle_exception(self, request, response):
        if response.status_code < 400:
            return

        request_id = response.headers.get(self._X_REQUEST_ID)
        sdk_error = exceptions.SdkError(request_id=request_id)
        try:
            sdk_error_dict = json.loads(response.text)
            if isinstance(sdk_error_dict, dict):
                self._process_sdk_error(sdk_error, sdk_error_dict)
            else:
                sdk_error.error_msg = response.text
        except six_utils.JSON_DECODE_ERROR:
            sdk_error.error_msg = response.text
        except Exception:
            sdk_error.error_msg = six.ensure_str(response.text)
            raise exceptions.ServerResponseException(response.status_code, sdk_error)
        finally:
            if not sdk_error.error_code:
                sdk_error.error_code = str(response.status_code)
            if not sdk_error.error_msg:
                sdk_error.error_msg = response.text

        raise exceptions.ClientRequestException(response.status_code, sdk_error) if response.status_code < 500 \
            else exceptions.ServerResponseException(response.status_code, sdk_error)

    @classmethod
    def _process_sdk_error(cls, sdk_error, sdk_error_dict):
        if cls._ENCODED_AUTHORIZATION_MESSAGE in sdk_error_dict:
            sdk_error.encoded_auth_msg = sdk_error_dict.get(cls._ENCODED_AUTHORIZATION_MESSAGE)

        if cls._ERROR_CODE in sdk_error_dict and cls._ERROR_MSG in sdk_error_dict:
            sdk_error.error_code = sdk_error_dict.get(cls._ERROR_CODE)
            sdk_error.error_msg = sdk_error_dict.get(cls._ERROR_MSG)
            return
        if cls._ERROR_CODE_CAMEL in sdk_error_dict and cls._ERROR_MSG_CAMEL in sdk_error_dict:
            sdk_error.error_code = sdk_error_dict.get(cls._ERROR_CODE_CAMEL)
            sdk_error.error_msg = sdk_error_dict.get(cls._ERROR_MSG_CAMEL)
            return
        if cls._CODE in sdk_error_dict and cls._MESSAGE in sdk_error_dict:
            sdk_error.error_code = sdk_error_dict.get(cls._CODE)
            sdk_error.error_msg = sdk_error_dict.get(cls._MESSAGE)
            return

        for value in sdk_error_dict.values():
            if not isinstance(value, dict):
                continue
            cls._process_sdk_error(sdk_error, value)


def process_connection_error(connection_error, logger):
    for each in connection_error.args:
        if not hasattr(each, "reason"):
            continue

        reason_str = str(each.reason)
        if isinstance(each.reason, SSLError):
            logger.error("SslHandShakeException occurred. %s", reason_str)
            return exceptions.SslHandShakeException(reason_str)

        if isinstance(each.reason, NewConnectionError):
            if reason_str.endswith("getaddrinfo failed") or reason_str.endswith("Name or service not known"):
                logger.error("HostUnreachableException occurred. %s", reason_str)
                return exceptions.HostUnreachableException(reason_str)

            logger.error("ConnectionException occurred. %s", reason_str)
            return exceptions.ConnectionException(reason_str)
    logger.error("ConnectionException occurred. %s", connection_error)
    return exceptions.ConnectionException(str(connection_error))


def process_retry_error(retry_error, logger):
    err_msg = str(retry_error)
    logger.error("RetryError occurred. %s", err_msg)

    if "too many 429 error responses" in err_msg:
        sdk_error = exceptions.SdkError(
            request_id="",
            error_msg=err_msg,
            error_code="429"
        )
        return exceptions.ClientRequestException(status_code=429, sdk_error=sdk_error)

    return exceptions.SdkException(err_msg)
