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
from requests.exceptions import SSLError

from huaweicloudsdkcore.exceptions import exceptions


class HttpClient:
    def __init__(self, request):
        self.request = request
        self.__timeout = None
        self.__proxy = None
        self.__ignore_ssl_verification = False
        self.__ssl_ca_cert = None
        self.__cert_file = None
        self.__key_file = None
        self.__assert_hostname = None
        self.__service_spec_exception_handler = None

    def set_config(self, config):
        self.__timeout = config.timeout
        self.__proxy = config.get_proxy()
        self.__ignore_ssl_verification = config.ignore_ssl_verification
        self.__ssl_ca_cert = config.ssl_ca_cert
        self.__cert_file = config.cert_file
        self.__assert_hostname = config.assert_hostname

    def set_service_spec_exception_handler(self, handler):
        self.__service_spec_exception_handler = handler

    def do_request(self):
        fun = getattr(requests, self.request.method.lower())
        try:
            if self.__ssl_ca_cert is not None:
                verify = self.__ssl_ca_cert if not self.__ignore_ssl_verification else self.__ignore_ssl_verification
            else:
                verify = not self.__ignore_ssl_verification
            if self.__cert_file is not None and self.__key_file is not None:
                cert = (self.__cert_file, self.__key_file)
            else:
                cert = self.__cert_file
            response = fun("%s://%s%s" % (self.request.schema, self.request.host, self.request.uri),
                           timeout=self.__timeout, headers=self.request.header_params,
                           proxies=self.__proxy, verify=verify, cert=cert, data=self.request.body)
            response.raise_for_status()
        except ConnectionError as connectionError:
            raise exceptions.ConnectionException(str(connectionError))
        except SSLError as sslError:
            raise exceptions.SslHandShakeException(str(sslError))
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
        return response

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
