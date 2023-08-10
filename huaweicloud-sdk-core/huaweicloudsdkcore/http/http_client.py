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

from concurrent.futures import ThreadPoolExecutor

import requests
from requests import HTTPError, Timeout, TooManyRedirects
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from requests.packages.urllib3.util import Retry
from urllib3.exceptions import SSLError, NewConnectionError

from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.http.future_session import FutureSession


class HttpClient(object):
    def __init__(self, config, http_handler, exception_handler, logger):
        self._logger = logger
        self._exception_handler = exception_handler
        self._http_handler = http_handler
        self._config = config
        self._proxy = config.get_proxy()

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

        self._executor = ThreadPoolExecutor(max_workers=8)

    def _init_session(self):
        sdk_session = requests.Session()
        retry = Retry(total=self._config.retry_times, status_forcelist=self._retry_status_list)
        sdk_adapter = HTTPAdapter(pool_connections=self._config.pool_connections,
                                  pool_maxsize=self._config.pool_maxsize, max_retries=retry)
        sdk_session.mount('https://', sdk_adapter)
        sdk_session.mount('http://', sdk_adapter)
        return sdk_session

    @property
    def executor(self):
        return self._executor

    @property
    def config(self):
        return self._config

    def do_request_sync(self, request):
        invoke = getattr(self._session, request.method.lower())

        try:
            if self._http_handler is not None:
                self._http_handler.process_request(request=request, logger=self._logger)
            url = "%s://%s%s" % (request.schema, request.host, request.uri)
            response = invoke(
                url,
                timeout=self._config.timeout,
                headers=request.header_params,
                proxies=self._proxy,
                verify=self._verify,
                cert=self._cert,
                data=request.body,
                stream=request.stream,
                allow_redirects=self._config.allow_redirects
            )
        except ConnectionError as connectionError:
            for each in connectionError.args:
                reason_str = str(each.reason)
                if isinstance(each.reason, SSLError):
                    self._logger.error("SslHandShakeException occurred. %s", reason_str)
                    raise exceptions.SslHandShakeException(reason_str)
                if isinstance(each.reason, NewConnectionError):
                    if reason_str.endswith("getaddrinfo failed") or reason_str.endswith("Name or service not known"):
                        raise exceptions.HostUnreachableException(reason_str)
                    self._logger.error("ConnectionException occurred. %s", reason_str)
                    raise exceptions.ConnectionException(reason_str)
            self._logger.error("ConnectionException occurred. %s", connectionError)
            raise exceptions.ConnectionException(str(connectionError))

        self.response_error_hook_factory()(response)
        return response

    def do_request_async(self, request, hooks):
        fun = getattr(FutureSession(self._session, self._executor), request.method.lower())
        hooks.append(self.response_error_hook_factory())

        future = fun(
            "%s://%s%s" % (request.schema, request.host, request.uri),
            timeout=self._config.timeout,
            headers=request.header_params,
            proxies=self._proxy,
            verify=self._verify,
            cert=self._cert,
            data=request.body,
            stream=request.stream,
            allow_redirects=self._config.allow_redirects,
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
                sdk_error = self._exception_handler.handle_exception(httpError.request, httpError.response)
                if 400 <= httpError.response.status_code < 500:
                    raise exceptions.ClientRequestException(httpError.response.status_code, sdk_error)
                else:
                    raise exceptions.ServerResponseException(httpError.response.status_code, sdk_error)
            except Timeout as timeout:
                raise exceptions.CallTimeoutException(str(timeout))
            except TooManyRedirects as tooManyRedirects:
                raise exceptions.RetryOutageException(str(tooManyRedirects))

        return response_hook
