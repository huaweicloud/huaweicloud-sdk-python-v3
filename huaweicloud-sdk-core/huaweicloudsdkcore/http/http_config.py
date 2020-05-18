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


class HttpConfig:
    def __init__(self):
        self.proxy_protocol = None
        self.proxy_host = None
        self.proxy_port = None
        self.proxy_user = None
        self.proxy_password = None
        self.ignore_ssl_verification = False
        self.ssl_ca_cert = None
        self.cert_file = None
        self.key_file = None
        self.assert_hostname = None
        self.timeout = 3
        self.preload_content = True
        self.return_http_data_only = True

    def get_proxy(self):
        if self.proxy_host is None:
            return None

        if self.proxy_port is not None:
            return {
                "http": "{}://{}:{}@{}:{}".format(
                    self.proxy_protocol, self.proxy_user, self.proxy_password, self.proxy_host, self.proxy_port),
                "https": "{}://{}:{}@{}:{}".format(
                    self.proxy_protocol, self.proxy_user, self.proxy_password, self.proxy_host, self.proxy_port)
            }
        else:
            return {
                "http": "{}://{}:{}@{}".format(
                    self.proxy_protocol, self.proxy_user, self.proxy_password, self.proxy_host),
                "https": "{}://{}:{}@{}".format(
                    self.proxy_protocol, self.proxy_user, self.proxy_password, self.proxy_host)
            }

    @staticmethod
    def get_default_config():
        return HttpConfig()

    def with_proxy_protocol(self, protocol):
        self.proxy_protocol = protocol
        return self

    def with_proxy_host(self, host):
        self.proxy_host = host
        return self

    def with_proxy_port(self, port):
        self.proxy_port = port
        return self

    def with_proxy_user(self, username):
        self.proxy_user = username
        return self

    def with_proxy_password(self, password):
        self.proxy_password = password
        return self

    def with_ignore_ssl_verification(self, ignore):
        self.ignore_ssl_verification = ignore
        return self

    def with_ssl_ca_cert(self, ca_cert):
        self.ssl_ca_cert = ca_cert
        return self

    def with_cert_file(self, cert_file):
        self.cert_file = cert_file
        return self

    def with_key_file(self, key_file):
        self.key_file = key_file
        return self

    def with_assert_hostname(self, assert_hostname):
        self.assert_hostname = assert_hostname
        return self

    def with_timeout(self, timeout):
        self.timeout = timeout
        return self

    def with_preload_content(self, preload_content):
        self.preload_content = preload_content
        return self

    def with_return_http_data_only(self, return_http_data_only):
        self.return_http_data_only = return_http_data_only
        return self
