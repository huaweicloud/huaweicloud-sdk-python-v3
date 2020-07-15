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

import requests
from requests import HTTPError, Timeout, TooManyRedirects
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from requests.packages.urllib3.util import Retry
from requests_futures.sessions import FuturesSession
from urllib3.exceptions import SSLError, NewConnectionError

from huaweicloudsdkcore.exceptions import exceptions


class HttpClient:
    def __init__(self, config, http_handler, exception_handler, logger):
        self._logger = logger
        self._exception_handler = exception_handler
        self._http_handler = http_handler

        self._timeout = config.timeout
        self._proxy = config.get_proxy()
        self._retry_times = config.retry_times
        self._pool_connections = config.pool_connections
        self._pool_maxsize = config.pool_maxsize
        if config.ssl_ca_cert is not None:
            self._verify = config.ssl_ca_cert if not config.ignore_ssl_verification else config.ignore_ssl_verification
        else:
            self._verify = not config.ignore_ssl_verification
        if config.cert_file is not None and config.key_file is not None:
            self._cert = (config.cert_file, config.key_file)
        else:
            self._cert = config.cert_file

        self._retry_status_list = [429]
        self._session = self._init_session()

    def _init_session(self):
        sdk_session = requests.Session()
        sdk_adapter = HTTPAdapter(pool_connections=self._pool_connections, pool_maxsize=self._pool_maxsize,
                                  max_retries=Retry(total=self._retry_times, status_forcelist=self._retry_status_list))
        sdk_session.mount('https://', sdk_adapter)
        sdk_session.mount('http://', sdk_adapter)
        return sdk_session

    def do_request_sync(self, request):
        fun = getattr(self._session, request.method.lower())

        try:
            if self._http_handler is not None:
                self._http_handler.process_request(request=request, logger=self._logger)
            response = fun(
                "%s://%s%s" % (request.schema, request.host, request.uri),
                timeout=self._timeout,
                headers=request.header_params,
                proxies=self._proxy,
                verify=self._verify,
                cert=self._cert,
                data=request.body,
                stream=request.stream
            )
        except ConnectionError as connectionError:
            for each in connectionError.args:
                if isinstance(each.reason, SSLError):
                    self._logger.error("SslHandShakeException occurred. %s" % str(each.reason))
                    raise exceptions.SslHandShakeException(str(each.reason))
                if isinstance(each.reason, NewConnectionError):
                    self._logger.error("ConnectionException occurred. %s" % str(each.reason))
                    raise exceptions.ConnectionException(str(each.reason))
            self._logger.error("ConnectionException occurred. %s" % str(connectionError))
            raise exceptions.ConnectionException(str(connectionError))

        self.response_error_hook_factory()(response)
        return response

    def do_request_async(self, request, hooks):
        fun = getattr(FuturesSession(session=self._session), request.method.lower())
        hooks.append(self.response_error_hook_factory())

        future = fun(
            "%s://%s%s" % (request.schema, request.host, request.uri),
            timeout=self._timeout,
            headers=request.header_params,
            proxies=self._proxy,
            verify=self._verify,
            cert=self._cert,
            data=request.body,
            stream=request.stream,
            hooks={'response': hooks}
        )
        return future

    def response_error_hook_factory(self):
        def response_hook(resp, *args, **kwargs):
            if self._http_handler is not None:
                self._http_handler.process_response(response=resp, logger=self._logger)

            try:
                resp.raise_for_status()
            except HTTPError as httpError:
                response_status_code = httpError.response.status_code
                response_header_params = httpError.response.headers
                request_id = response_header_params["X-Request-Id"]
                response_body = httpError.response.text
                sdk_error = self.get_sdk_error_from_response(request_id, response_body, response_status_code)
                if 400 <= response_status_code < 500:
                    raise exceptions.ClientRequestException(response_status_code, sdk_error)
                else:
                    raise exceptions.ServerResponseException(response_status_code, sdk_error)
            except Timeout as timeout:
                raise exceptions.CallTimeoutException(str(timeout))
            except TooManyRedirects as tooManyRedirects:
                raise exceptions.RetryOutageException(str(tooManyRedirects))

        return response_hook

    def get_sdk_error_from_response(self, request_id, response_body, response_status_code):
        sdk_error = exceptions.SdkError()

        try:
            sdk_error_dict = json.loads(response_body)
            if "error_code" in sdk_error_dict and "error_msg" in sdk_error_dict:
                sdk_error = exceptions.SdkError(request_id, sdk_error_dict["error_code"],
                                                sdk_error_dict["error_msg"])
            elif "code" in sdk_error_dict and "message" in sdk_error_dict:
                sdk_error = exceptions.SdkError(request_id, sdk_error_dict["code"],
                                                sdk_error_dict["message"])
            else:
                for key in sdk_error_dict:
                    if type(sdk_error_dict[key]) == dict and "code" in sdk_error_dict[key] and "message" in \
                            sdk_error_dict[key]:
                        sdk_error = exceptions.SdkError(request_id, sdk_error_dict[key]["code"],
                                                        sdk_error_dict[key]["message"])
        except Exception:
            raise exceptions.ServerResponseException(response_status_code,
                                                     exceptions.SdkError(error_msg=str(response_body)))

        if sdk_error.error_msg is None or sdk_error.error_msg == "":
            if self._exception_handler is not None:
                sdk_error = self._exception_handler(response_body)
        if sdk_error.error_msg is None or sdk_error.error_msg == "":
            sdk_error = exceptions.SdkError(error_msg=response_body)

        return sdk_error
