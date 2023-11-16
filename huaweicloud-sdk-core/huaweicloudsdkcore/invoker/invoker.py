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

from typing import Callable

from huaweicloudsdkcore.client import Client
from huaweicloudsdkcore.exceptions.exceptions import SdkException


class BaseInvoker(object):
    def __init__(self, client, http_info):
        # type: (Client, dict) -> None
        self._client = client
        self._http_info = http_info

    def add_header(self, key, value):
        # type: (str, str) -> BaseInvoker
        self._http_info.setdefault("header_params", {})[key] = value
        return self

    def replace_credential_when(self, func):
        # type: (Callable) -> BaseInvoker
        old_cred = self._client.get_credentials()
        new_cred = func(old_cred)
        if not new_cred or not isinstance(new_cred, old_cred.__class__):
            raise SdkException("invalid credential type: %s, expected type: %s" % (
                type(new_cred), type(old_cred)))
        self._client.with_credentials(new_cred)
        return self


class SyncInvoker(BaseInvoker):
    def __init__(self, client, http_info):
        super(SyncInvoker, self).__init__(client, http_info)

    def invoke(self):
        return self._client.do_http_request(**self._http_info)


class AsyncInvoker(SyncInvoker):
    def __init__(self, client, http_info):
        http_info["async_request"] = True
        super(AsyncInvoker, self).__init__(client, http_info)
