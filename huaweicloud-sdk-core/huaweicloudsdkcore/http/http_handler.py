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


def default_request_handler(**kwargs):
    pass


def default_response_handler(**kwargs):
    _response = kwargs.get("response")
    kwargs.get("logger").info("\"{} {}\" {} {} {} {}".format(
        _response.request.method,
        _response.request.url, _response.status_code, len(_response.content),
        _response.elapsed, _response.headers.get("X-Request-Id") if "X-Request-Id" in _response.headers else "")
    )


class HttpHandler:
    def __init__(self):
        self._request_handlers = [default_request_handler]
        self._response_handlers = [default_response_handler]

    def add_request_handler(self, fun):
        self._request_handlers.append(fun)
        return self

    def add_response_handler(self, fun):
        self._response_handlers.append(fun)
        return self

    def process_request(self, **kwargs):
        for handler in self._request_handlers:
            handler(**kwargs)

    def process_response(self, **kwargs):
        for handler in self._response_handlers:
            handler(**kwargs)
