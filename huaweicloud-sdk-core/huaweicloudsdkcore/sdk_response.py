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
from huaweicloudsdkcore.exceptions import exceptions
from requests.exceptions import ConnectionError
from urllib3.exceptions import SSLError, NewConnectionError


class SdkResponse(object):
    def __init__(self):
        self._status_code = None    # type: int | None
        self._raw_content = None    # type: bytes | None

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        if not self._status_code:
            self._status_code = status_code

    @property
    def raw_content(self):
        return self._raw_content

    @raw_content.setter
    def raw_content(self, raw_content):
        if not self._raw_content:
            self._raw_content = raw_content

    def to_json_object(self):
        return json.loads(self._raw_content.decode("utf-8")) if self._raw_content else None


class FutureSdkResponse:
    def __init__(self, future, logger):
        self._future = future
        self._logger = logger

    def result(self):
        try:
            future_response = self._future.result().result()
            response = future_response.data \
                if hasattr(future_response, "data") and future_response.data is not None else future_response
        except ConnectionError as connectionError:
            for each in connectionError.args:
                reason_str = str(each.reason)
                if isinstance(each.reason, SSLError):
                    self._logger.error("Sync SslHandShakeException occurred. %s", reason_str)
                    raise exceptions.SslHandShakeException(reason_str)
                if isinstance(each.reason, NewConnectionError):
                    if reason_str.endswith("getaddrinfo failed") or reason_str.endswith("Name or service not known"):
                        raise exceptions.HostUnreachableException(reason_str)
                    self._logger.error("Sync ConnectionException occurred. %s", reason_str)
                    raise exceptions.ConnectionException(reason_str)
            self._logger.error("Sync ConnectionException occurred. %s", connectionError)
            raise exceptions.ConnectionException(str(connectionError))
        return response
