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

from huaweicloudsdkcore.exceptions.exceptions import SdkError, ServerResponseException, ClientRequestException
from huaweicloudsdkcore.exceptions.exception_handler import ExceptionHandler


class CceExceptionHandler(ExceptionHandler):
    def handle_exception(self, request, response):
        if response.status_code < 400:
            return

        sdk_error = SdkError(request_id=response.headers.get("X-Request-Id"))

        data = json.loads(response.content)
        sdk_error.error_code = data.get("error_code")
        sdk_error.error_msg = data.get("error_msg", "")
        message = data.get("message")
        if message and sdk_error.error_msg != message:
            sdk_error.error_msg += ", " + message

        raise ClientRequestException(response.status_code, sdk_error) if response.status_code < 500 \
            else ServerResponseException(response.status_code, sdk_error)
