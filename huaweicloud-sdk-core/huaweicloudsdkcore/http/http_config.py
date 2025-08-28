# coding: utf-8
"""
 Copyright 2020 Huawei Technologies Co.,Ltd.

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

import six

from huaweicloudsdkcore.signer.algorithm import SigningAlgorithm


class HttpConfig(object):
    def __init__(self, proxy_protocol=None, proxy_host=None, proxy_port=None, proxy_user=None, proxy_password=None,
                 ignore_ssl_verification=False, ssl_ca_cert=None, cert_file=None, key_file=None, timeout=(60, 120),
                 retry_times=0, pool_connections=10, pool_maxsize=10, allow_redirects=False,
                 ignore_content_type_for_get_request=False, signing_algorithm=SigningAlgorithm.get_default(),
                 user_agent=None):
        """
        :param proxy_protocol(optional) : proxy protocol, http or https
        :type proxy_protocol: str

        :param proxy_host(optional) : hostname or ip address of proxy server
        :type proxy_host: str

        :param proxy_port(optional) : port of proxy server
        :type proxy_port: str

        :param proxy_user(optional) : username used for proxy authentication
        :type proxy_user: str

        :param proxy_password(optional) : username used for proxy authentication
        :type proxy_password: str

        :param ignore_ssl_verification: whether skip SSL certificate validation while sending https request,
         default, value is False
        :type ignore_ssl_verification: bool

        :param ssl_ca_cert: (optional) a path to a CA bundle to use
        :type ssl_ca_cert: str

        :param cert_file: (optional) a path to ssl client cert file (.pem)
        :type cert_file: str

        :param key_file: (optional) a path to a  ssl client cert key file (.key)
        :type key_file: str

        :param timeout: (optional) seconds to wait for the server to send data before giving up,
         as a float, or a :ref:`(connect timeout, read timeout) <timeouts>` tuple.
        :type timeout: float or tuple

        :param retry_times: maximum number of retries each connection should attempt,
         default, does not retry failed connections.
        :type retry_times: int

        :param pool_connections: number of urllib3 connection pools to cache,
         default, value is 10
        :type pool_connections: int

        :param pool_maxsize: maximum number of connections to save in the pool，
         default, value is 10
        :type pool_maxsize: int

        :param allow_redirects: Experimental configuration.
         Automatic redirection is allowed when turns on, which may cause some request exceptions.
         default, value is False
        :type allow_redirects: bool

        :param ignore_content_type_for_get_request: Ignore the request header Content-Type when sending a GET request,
         default, value is False
        :type ignore_ssl_verification: bool

        :param signing_algorithm: signing algorithm of request
         default, value is HMAC_SHA256
        :type signing_algorithm: SigningAlgorithm

        :param user_agent(optional): An optional custom value can be appended to the User-Agent request header.
        :type user_agent: str
        """
        self._proxy_protocol = proxy_protocol
        self._proxy_host = proxy_host
        self._proxy_port = proxy_port
        self._proxy_user = proxy_user
        self._proxy_password = proxy_password

        self._ignore_ssl_verification = ignore_ssl_verification
        self._allow_redirects = allow_redirects

        self._ssl_ca_cert = ssl_ca_cert
        self._cert_file = cert_file
        self._key_file = key_file

        self._timeout = timeout
        self._retry_times = retry_times
        self._pool_connections = pool_connections
        self._pool_maxsize = pool_maxsize
        self._ignore_content_type_for_get_request = ignore_content_type_for_get_request
        self._signing_algorithm = signing_algorithm

        self._user_agent = user_agent

    @property
    def proxy_protocol(self):
        return self._proxy_protocol

    @proxy_protocol.setter
    def proxy_protocol(self, value):
        self._proxy_protocol = value

    @property
    def proxy_host(self):
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, value):
        self._proxy_host = value

    @property
    def proxy_port(self):
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, value):
        self._proxy_port = value

    @property
    def proxy_user(self):
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, value):
        self._proxy_user = value

    @property
    def proxy_password(self):
        return self._proxy_password

    @proxy_password.setter
    def proxy_password(self, value):
        self._proxy_password = value

    @property
    def ignore_ssl_verification(self):
        return self._ignore_ssl_verification

    @ignore_ssl_verification.setter
    def ignore_ssl_verification(self, value):
        self._ignore_ssl_verification = value

    @property
    def allow_redirects(self):
        return self._allow_redirects

    @allow_redirects.setter
    def allow_redirects(self, value):
        self._allow_redirects = value

    @property
    def ssl_ca_cert(self):
        return self._ssl_ca_cert

    @ssl_ca_cert.setter
    def ssl_ca_cert(self, value):
        self._ssl_ca_cert = value

    @property
    def cert_file(self):
        return self._cert_file

    @cert_file.setter
    def cert_file(self, value):
        self._cert_file = value

    @property
    def key_file(self):
        return self._key_file

    @key_file.setter
    def key_file(self, value):
        self._key_file = value

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value

    @property
    def retry_times(self):
        return self._retry_times

    @retry_times.setter
    def retry_times(self, value):
        self._retry_times = value

    @property
    def pool_connections(self):
        return self._pool_connections

    @pool_connections.setter
    def pool_connections(self, value):
        self._pool_connections = value

    @property
    def pool_maxsize(self):
        return self._pool_maxsize

    @pool_maxsize.setter
    def pool_maxsize(self, value):
        self._pool_maxsize = value

    @property
    def ignore_content_type_for_get_request(self):
        return self._ignore_content_type_for_get_request

    @ignore_content_type_for_get_request.setter
    def ignore_content_type_for_get_request(self, value):
        self._ignore_content_type_for_get_request = value

    @property
    def signing_algorithm(self):
        return self._signing_algorithm

    @signing_algorithm.setter
    def signing_algorithm(self, value):
        self._signing_algorithm = value

    @property
    def user_agent(self):
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value):
        self._user_agent = value

    @property
    def proxy(self):
        return self.get_proxy()

    def get_proxy(self):
        if self.proxy_host is None:
            return {}

        if six.PY2:
            from urllib import quote_plus
        else:
            from urllib.parse import quote_plus

        return {
            "https": "%s://%s%s%s" % (
                self.proxy_protocol,
                "%s:%s@" % (self.proxy_user, quote_plus(self.proxy_password)) if self.proxy_user is not None else "",
                self.proxy_host,
                ":%s" % self.proxy_port if self.proxy_port is not None else ""
            )
        }

    @staticmethod
    def get_default_config():
        return HttpConfig()
