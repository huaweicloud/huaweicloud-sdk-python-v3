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

import six

from huaweicloudsdkcore.signer.algorithm import SigningAlgorithm


class HttpConfig(object):
    def __init__(self, proxy_protocol=None, proxy_host=None, proxy_port=None, proxy_user=None, proxy_password=None,
                 ignore_ssl_verification=False, ssl_ca_cert=None, cert_file=None, key_file=None, timeout=(60, 120),
                 retry_times=0, pool_connections=10, pool_maxsize=10, allow_redirects=False,
                 ignore_content_type_for_get_request=False, signing_algorithm=SigningAlgorithm.get_default()):
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
        """
        self.proxy_protocol = proxy_protocol
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_user = proxy_user
        self.proxy_password = proxy_password

        self.ignore_ssl_verification = ignore_ssl_verification
        self.allow_redirects = allow_redirects

        self.ssl_ca_cert = ssl_ca_cert
        self.cert_file = cert_file
        self.key_file = key_file

        self.timeout = timeout
        self.retry_times = retry_times
        self.pool_connections = pool_connections
        self.pool_maxsize = pool_maxsize
        self.ignore_content_type_for_get_request = ignore_content_type_for_get_request
        self.signing_algorithm = signing_algorithm

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
