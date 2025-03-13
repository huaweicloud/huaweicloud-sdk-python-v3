# coding: utf-8

from __future__ import absolute_import

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.region.region import Region

from huaweicloudsdkkvs.v1 import KvsAsyncClient
from huaweicloudsdkkvs.v1.kvs_client import KvsClient
from huaweicloudsdkkvs.v1.model.credential import Credential
from huaweicloudsdkkvs.v1.util.thread_safe_utils import AtomicBool


class ManagedKvsClient:
    def __init__(self, endpoint, config, http_handler=None, exception_handler=None):
        self._endpoint = endpoint
        self._credential = Credential(config.ak, config.sk, config.sts_token)
        self._is_async_client = config.is_async_client
        credentials = BasicCredentials(config.ak, config.sk)
        if config.project_id is not None and len(config.project_id) != 0:
            credentials.with_project_id(config.project_id)
        if config.sts_token is not None and len(config.sts_token) != 0:
            credentials.with_security_token(config.sts_token)

        endpoint = "https://" + endpoint.name + "." + config.region_id + ".myhuaweicloud.com"
        region = Region(config.region_id, endpoint)

        http_config = config.customize_http_config
        if http_config is None:
            http_config = self.get_http_config_by_sdk_config(config)

        if self._is_async_client:
            kvs_client_builder = KvsAsyncClient.new_builder()
        else:
            kvs_client_builder = KvsClient.new_builder()

        kvs_client_builder.with_credentials(credentials).with_region(region).with_http_config(http_config)
        if config.file_log_path is not None and len(config.file_log_path) != 0:
            if config.file_log_level is not None and len(config.file_log_level) != 0:
                file_log_level = config.file_log_level
            else:
                file_log_level = "INFO"
            kvs_client_builder.with_file_log(config.file_log_path, file_log_level)
        if http_handler is not None:
            kvs_client_builder.with_http_handler(http_handler)
        if exception_handler is not None:
            kvs_client_builder.with_exception_handler(exception_handler)

        self._client = kvs_client_builder.build()
        self._is_usable = AtomicBool(True)

    @property
    def is_async_client(self):
        """Gets the type of kvs client

        :return: The type of kvs client.
        :rtype: bool
        """
        return self._is_async_client

    @property
    def client(self):
        """Gets kvs client

        :return: The kvs client.
        :rtype: class: KvsClient
        """
        return self._client

    @property
    def endpoint(self):
        """Gets kvs client endpoint

        :return: The kvs client endpoint.
        :rtype: class: 'huaweicloudsdkkvs.v1.model.Endpoint'
        """
        return self._endpoint

    @property
    def credential(self):
        """Gets kvs client aksk

        :return: The kvs client aksk.
        :rtype: class: 'huaweicloudsdkkvs.v1.model.Credential'
        """
        return self._credential

    @property
    def is_usable(self):
        """Gets the usable status of kvs client.

        :return: The usable status of kvs client.
        :rtype: class:`huaweicloudsdkkvs.v1.util.ThreadSafeBool`
        """
        return self._is_usable.get()

    @is_usable.setter
    def is_usable(self, is_usable):
        """Sets the usable status of kvs client.

        :param customize_http_config: The usable status of kvs client.
        :type customize_http_config: class:`huaweicloudsdkkvs.v1.util.ThreadSafeBool`
        """
        self._is_usable.set(is_usable)

    @staticmethod
    def get_http_config_by_sdk_config(sdk_config):
        http_config = HttpConfig.get_default_config()
        if sdk_config.ignore_ssl_verification is False:
            http_config.ignore_ssl_verification = False
            http_config.ssl_ca_cert = sdk_config.ca_certificate_path
        else:
            http_config.ignore_ssl_verification = True
        http_config.timeout = (sdk_config.connection_timeout, sdk_config.read_timeout)
        if sdk_config.proxy_protocol is not None and len(sdk_config.proxy_protocol) > 0:
            http_config.proxy_protocol = sdk_config.proxy_protocol
        if sdk_config.proxy_host is not None and len(sdk_config.proxy_host) > 0:
            http_config.proxy_host = sdk_config.proxy_host
        if sdk_config.proxy_port is not None and sdk_config.proxy_port != -1:
            http_config.proxy_port = sdk_config.proxy_port
        if sdk_config.proxy_user is not None and len(sdk_config.proxy_user) > 0:
            http_config.proxy_user = sdk_config.proxy_user
        if sdk_config.proxy_password is not None and len(sdk_config.proxy_password) > 0:
            http_config.proxy_password = sdk_config.proxy_password
        return http_config
