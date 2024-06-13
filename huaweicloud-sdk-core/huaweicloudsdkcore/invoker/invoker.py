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
import time

from huaweicloudsdkcore.retry.backoff_strategy import BackoffStrategy

try:
    from typing import TypeVar, Generic
except ImportError:
    from typing_extensions import TypeVar, Generic
from typing import Callable

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.sdk_response import SdkResponse, FutureSdkResponse
from huaweicloudsdkcore.exceptions.exceptions import SdkException

_TInvoker = TypeVar("_TInvoker", bound="BaseInvoker")
_MAX_RETRIES_LIMIT = 10


class BaseInvoker(Generic[_TInvoker]):
    def __init__(self, client, http_info):
        # type: (Client, dict) -> None
        self._client = client
        self._http_info = http_info

    def add_header(self, key, value):
        # type: (str, str) -> _TInvoker
        self._http_info.setdefault("header_params", {})[key] = value
        return self

    def replace_credential_when(self, func):
        # type: (Callable) -> _TInvoker
        old_cred = self._client.get_credentials()
        new_cred = func(old_cred)
        if not new_cred or not isinstance(new_cred, old_cred.__class__):
            raise SdkException("invalid credential type: %s, expected type: %s" % (
                type(new_cred), type(old_cred)))
        self._client.with_credentials(new_cred)
        return self


class SyncInvoker(BaseInvoker["SyncInvoker"]):
    def __init__(self, client, http_info):
        super(SyncInvoker, self).__init__(client, http_info)
        self._retry_condition = None
        self._max_retries = 0
        self._backoff_strategy = None

    def invoke(self):
        # type: () -> SdkResponse
        if not self._max_retries or not self._retry_condition:
            return self._client.do_http_request(**self._http_info)

        exec_times = 0
        while True:
            try:
                resp = self._client.do_http_request(**self._http_info)
                exception = None
            except SdkException as e:
                exception = e
                resp = None
            finally:
                exec_times += 1

            if exec_times > self._max_retries or not self._retry_condition(resp, exception):
                break

            delay_ms = self._backoff_strategy.calculate_retry_delay_millis(exec_times)
            if delay_ms > 0:
                time.sleep(delay_ms / 1000)

        if exception:
            raise exception

        return resp

    def with_retry(self, retry_condition, max_retries, backoff_strategy):
        """
        Retry on condition.

        :param retry_condition: Retry condition, retry if true
        :type retry_condition: Callable[[SdkResponse, SdkException], bool]

        :param max_retries: Max retry times
        :type max_retries: int

        :param backoff_strategy: Calculate the delay before next retry
        :type backoff_strategy: BackoffStrategy
        """
        if not retry_condition:
            raise ValueError("retry condition cannot be None")
        if not backoff_strategy:
            raise ValueError("backoff strategy cannot be None")
        if max_retries > _MAX_RETRIES_LIMIT or max_retries <= 0:
            raise ValueError("max retries is not in range [1, %d]" % _MAX_RETRIES_LIMIT)
        self._retry_condition = retry_condition
        self._max_retries = max_retries
        self._backoff_strategy = backoff_strategy
        return self


class AsyncInvoker(BaseInvoker["AsyncInvoker"]):
    def __init__(self, client, http_info):
        http_info["async_request"] = True
        super(AsyncInvoker, self).__init__(client, http_info)

    def invoke(self):
        # type: () -> FutureSdkResponse
        return self._client.do_http_request(**self._http_info)
