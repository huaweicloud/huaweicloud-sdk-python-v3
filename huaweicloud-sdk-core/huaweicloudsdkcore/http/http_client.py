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
    def __init__(self, logger, enable_http_log):
        self.__timeout = None
        self.__proxy = None
        self.__retry_times = 0
        self.__pool_connections = 1
        self.__pool_maxsize = 1

        self.__verify = True
        self.__cert = None

        self.__retry_status_list = [429]
        self.__secure_headers = ('authorization', 'x-auth-token', 'x-subject-token', 'x-service-token')

        self.__logger = logger
        self.__enable_http_log = enable_http_log
        self.__service_spec_exception_handler = None

        self.__session = self._init_session()

        self.__filter_sensitive_info = False

    def _init_session(self):
        s = requests.Session()
        s.mount('https://',
                HTTPAdapter(pool_connections=self.__pool_connections, pool_maxsize=self.__pool_maxsize,
                            max_retries=Retry(total=self.__retry_times, status_forcelist=self.__retry_status_list)))
        return s

    def set_config(self, config):
        self.__timeout = config.timeout
        self.__proxy = config.get_proxy()
        self.__retry_times = config.retry_times
        self.__pool_connections = config.pool_connections
        self.__pool_maxsize = config.pool_maxsize

        if config.ssl_ca_cert is not None:
            self.__verify = config.ssl_ca_cert if not config.ignore_ssl_verification else config.ignore_ssl_verification
        else:
            self.__verify = not config.ignore_ssl_verification
        if config.cert_file is not None and config.key_file is not None:
            self.__cert = (config.cert_file, config.key_file)
        else:
            self.__cert = config.cert_file

    def set_service_spec_exception_handler(self, handler):
        self.__service_spec_exception_handler = handler

    def do_request_sync(self, request, request_sensitive_list, response_sensitive_list):
        fun = getattr(self.__session, request.method.lower())

        try:
            response = fun("%s://%s%s" % (request.schema, request.host, request.uri), timeout=self.__timeout,
                           headers=request.header_params, proxies=self.__proxy, verify=self.__verify, cert=self.__cert,
                           data=request.body)
        except ConnectionError as connectionError:
            for each in connectionError.args:
                if isinstance(each.reason, SSLError):
                    self.__logger.error("SslHandShakeException occurred. %s" % str(each.reason))
                    raise exceptions.SslHandShakeException(str(each.reason))
                if isinstance(each.reason, NewConnectionError):
                    self.__logger.error("ConnectionException occurred. %s" % str(each.reason))
                    raise exceptions.ConnectionException(str(each.reason))
            self.__logger.error("ConnectionException occurred. %s" % str(connectionError))
            raise exceptions.ConnectionException(str(connectionError))

        self.response_error_hook_factory(request_sensitive_list, response_sensitive_list)(response, host=request.host,
                                                                                          uri=request.uri)
        return response

    def do_request_async(self, request, hooks, request_sensitive_list, response_sensitive_list):
        future_session = FuturesSession(session=self.__session)
        fun = getattr(future_session, request.method.lower())
        hooks.append(self.response_error_hook_factory(request_sensitive_list, response_sensitive_list))

        future = fun("%s://%s%s" % (request.schema, request.host, request.uri), timeout=self.__timeout,
                     headers=request.header_params, proxies=self.__proxy, verify=self.__verify, cert=self.__cert,
                     data=request.body, hooks={'response': hooks})
        return future

    def response_error_hook_factory(self, request_sensitive_list, response_sensitive_list):
        def response_hook(resp, *args, **kwargs):
            request_id = resp.headers.get("X-Request-Id") if "X-Request-Id" in resp.headers else ""
            self.__logger.info("\"%s %s\" %s %s %s %s" % (resp.request.method,
                                                          resp.request.url, resp.status_code, len(resp.content),
                                                          resp.elapsed, request_id))

            if self.__enable_http_log:
                self.prepare_http_debug_log(resp.request, resp, request_sensitive_list, response_sensitive_list)

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
            raise exceptions.ServerResponseException(response_status_code, exceptions.SdkError(str(response_body)))
        if sdk_error.error_msg is None or sdk_error.error_msg == "":
            if self.__service_spec_exception_handler is not None:
                sdk_error = self.__service_spec_exception_handler(response_body)
        if sdk_error.error_msg is None or sdk_error.error_msg == "":
            sdk_error = exceptions.SdkError(error_msg=response_body)
        return sdk_error

    def prepare_http_debug_log(self, request, response, request_sensitive_list, response_sensitive_list):
        base = "> Request %s %s HTTP/1.1" % (request.method, request.path_url) + "\n"
        if len(request.headers) != 0:
            base = base + "> Headers:" + "\n"
            for each in request.headers:
                base = base + "    %s : %s" % self._process_header(each, request.headers[each],
                                                                   request_sensitive_list) + "\n"
        base = base + "> Body: %s" % self._process_body(request.body, request_sensitive_list) + "\n\n"

        base = base + "< Response HTTP/1.1 %s " % response.status_code + "\n"
        if len(response.headers) != 0:
            base = base + "< Headers:" + "\n"
            for each in response.headers:
                base = base + "    %s : %s" % self._process_header(each, response.headers[each],
                                                                   response_sensitive_list) + "\n"
        base = base + "< Body: %s" % self._process_body(response.content, response_sensitive_list)
        self.__logger.debug(base)

    def _process_header(self, key, value, sensitive_list):
        if self.__filter_sensitive_info is False:
            return key, value

        if key.lower() in self.__secure_headers or key in sensitive_list:
            return key, "****"
        return key, value

    def _process_body(self, body, sensitive_list):
        if self.__filter_sensitive_info is False:
            return body

        try:
            value = json.loads(body)
            for each in sensitive_list:
                each = each.lstrip('body.') if each.startswith('body.') else each
                value = self._get_sensitive_object(value, each)
            return json.dumps(value)
        except Exception:
            return body

    @classmethod
    def _get_sensitive_object(cls, value, path):
        temp_value = value
        sensitive_path_list = []
        for each in path.split('.'):
            if each == "[*]":
                temp_value = [i for i in temp_value]
                temp_sensitive_path_list = []
                for path in sensitive_path_list:
                    for index in range(len(temp_value)):
                        temp_sensitive_path_list.append(path + "[%s]" % index)
                sensitive_path_list = temp_sensitive_path_list
            elif each == "*":
                temp_value = [temp_value[i] for i in temp_value]
                temp_sensitive_path_list = []
                for key in temp_value:
                    for path in sensitive_path_list:
                        temp_sensitive_path_list.append(path + "[%s]" % key)
                sensitive_path_list = temp_sensitive_path_list
            else:
                if type(temp_value) == list:
                    temp_value_list = []
                    for item in temp_value:
                        if each in item:
                            temp_value_list.append(item[each])
                        else:
                            continue
                    temp_value = temp_value_list
                else:
                    temp_value = temp_value[each]

                if len(sensitive_path_list) == 0:
                    sensitive_path_list.append("value[\"%s\"]" % each)
                else:
                    sensitive_path_list = [i + "[\"%s\"]" % each for i in sensitive_path_list]

        for each in sensitive_path_list:
            try:
                exec("%s=\"****\"" % each)
            except Exception:
                pass

        return value
