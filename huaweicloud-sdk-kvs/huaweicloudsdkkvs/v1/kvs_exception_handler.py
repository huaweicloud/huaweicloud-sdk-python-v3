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
import bson
import six

from huaweicloudsdkcore.exceptions.exception_handler import DefaultExceptionHandler
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import six_utils


class KvsExceptionHandler(DefaultExceptionHandler):
    _CONTENT_TYPE = "Content-Type"
    _APPLICATION_BSON = "application/bson"

    def handle_exception(self, request, response):
        if response.status_code < 400:
            return

        request_id = response.headers.get(self._X_REQUEST_ID)
        sdk_error = exceptions.SdkError(request_id=request_id)
        try:
            if response.headers.get(self._CONTENT_TYPE) == self._APPLICATION_BSON:
                sdk_error_dict = bson.decode(response.content)
            else:
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
