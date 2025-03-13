# coding: utf-8

from __future__ import absolute_import

from configparser import ConfigParser

from huaweicloudsdkkvs.v1.model.endpoint import Endpoint


class KvsSdkConfig:
    def __init__(self, config_file_path, is_async_client, logger=None):
        self._logger = logger
        self._config = ConfigParser()
        self._config_file_path = config_file_path
        self.is_async_client = is_async_client

        self.heartbeat_interval = 1000
        self.heartbeat_thread_pool_size = 5
        self.reload_interval = 1000
        self.api_retry_count = 3
        self.endpoint_name_list = []
        self.endpoint_weight_list = []

        self.ak = ''
        self.sk = ''
        self.sts_token = ''
        self.project_id = ''
        self.ignore_ssl_verification = True
        self.ca_certificate_path = ''

        self.region_id = ''
        self.connection_timeout = 60000
        self.read_timeout = 120000
        self.proxy_protocol = ''
        self.proxy_host = ''
        self.proxy_port = -1
        self.proxy_user = ''
        self.proxy_password = ''
        self.file_log_path = ''
        self.file_log_level = "INFO"
        self.customize_http_config = None

        self.load_config()

    @property
    def is_async_client(self):
        """Gets the kvs async client switch

         kvs async client switch of multichannel sdk.

        :return: The async client switch of multichannel sdk.
        :rtype: bool
        """
        return self._is_async_client

    @is_async_client.setter
    def is_async_client(self, is_async_client):
        """Sets the kvs async client switch

         kvs async client switch of multichannel sdk.

        :param is_async_client: The async client switch of multichannel sdk.
        :type is_async_client: bool
        """
        self._is_async_client = is_async_client

    @property
    def heartbeat_interval(self):
        """Gets the heartbeat interval of sdk config.

         heartbeat check interval time for multichannel sdk.

        :return: The heartbeat interval of sdk config.
        :rtype: int
        """
        return self._heartbeat_interval

    @heartbeat_interval.setter
    def heartbeat_interval(self, heartbeat_interval):
        """Sets the heartbeat interval of sdk config.

         heartbeat check interval time for multichannel sdk.

        :param heartbeat_interval: The heartbeat interval of sdk config.
        :type heartbeat_interval: int
        """
        self._heartbeat_interval = heartbeat_interval

    @property
    def heartbeat_thread_pool_size(self):
        """Gets the heartbeat threadpool size of sdk config.

         size of heartbeat check thread pool.

        :return: The heartbeat threadpool size of sdk config.
        :rtype: int
        """
        return self._heartbeat_thread_pool_size

    @heartbeat_thread_pool_size.setter
    def heartbeat_thread_pool_size(self, heartbeat_thread_pool_size):
        """Sets the heartbeat interval of sdk config.

         size of heartbeat check thread pool.

        :param heartbeat_thread_pool_size: The heartbeat interval of sdk config.
        :type heartbeat_thread_pool_size: int
        """
        self._heartbeat_thread_pool_size = heartbeat_thread_pool_size

    @property
    def reload_interval(self):
        """Gets the reload interval of sdk config.

         interval time for multichannel sdk to reload endpoint and ak sk config.

        :return: The reload interval of sdk config.
        :rtype: int
        """
        return self._reload_interval

    @reload_interval.setter
    def reload_interval(self, reload_interval):
        """Sets the reload interval of sdk config.

         interval time for multichannel sdk to reload endpoint and ak sk config.

        :param reload_interval: The reload interval of sdk config.
        :type reload_interval: int
        """
        self._reload_interval = reload_interval

    @property
    def api_retry_count(self):
        """Gets the retry count of multichannel sdk api.

         retry count of multichannel sdk api.

        :return: The retry count of multichannel sdk api.
        :rtype: int
        """
        return self._api_retry_count

    @api_retry_count.setter
    def api_retry_count(self, api_retry_count):
        """Sets the retry count of multichannel sdk api.

         retry count of multichannel sdk api.

        :param api_retry_count: The retry count of multichannel sdk api.
        :type api_retry_count: int
        """
        self._api_retry_count = api_retry_count

    @property
    def endpoint_name_list(self):
        """Gets the endpoint name list of sdk config.

         endpoint name list for multichannel sdk.

        :return: The endpoint name list of sdk config.
        :rtype: list[str].
        """
        return self._endpoint_name_list

    @endpoint_name_list.setter
    def endpoint_name_list(self, endpoint_name_list):
        """Sets the endpoint name list of sdk config.

         endpoint name list for multichannel sdk.

        :param endpoint_name_list: The endpoint name list of sdk config.
        :type endpoint_name_list: list[str].
        """
        self._endpoint_name_list = endpoint_name_list

    @property
    def endpoint_weight_list(self):
        """Gets the endpoint weight list of sdk config.

         endpoint weight list for multichannel sdk.

        :return: The endpoint weight list of sdk config.
        :rtype: list[int].
        """
        return self._endpoint_weight_list

    @endpoint_weight_list.setter
    def endpoint_weight_list(self, endpoint_weight_list):
        """Sets the endpoint weight list of sdk config.

         endpoint weight list for multichannel sdk.

        :param endpoint_weight_list: The endpoint weight list of sdk config.
        :type endpoint_weight_list: list[int].
        """
        self._endpoint_weight_list = endpoint_weight_list

    @property
    def ak(self):
        """Gets the accessKey of sdk config.

         accessKey

        :return: The accessKey of sdk config.
        :rtype: str.
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        """Sets the accessKey of sdk config.

         accessKey

        :param ak: The accessKey of sdk config.
        :type ak: str
        """
        self._ak = ak

    @property
    def sk(self):
        """Gets the securityKey of sdk config.

         securityKey

        :return: The securityKey of sdk config.
        :rtype: str.
        """
        return self._sk

    @sk.setter
    def sk(self, sk):
        """Sets the securityKey of sdk config.

         securityKey

        :param sk: The securityKey of sdk config.
        :type sk: str
        """
        self._sk = sk

    @property
    def sts_token(self):
        """Gets the stsToken of sdk config.

         stsToken

        :return: The stsToken of sdk config.
        :rtype: str.
        """
        return self._sts_token

    @sts_token.setter
    def sts_token(self, sts_token):
        """Sets the stsToken of sdk config.

         stsToken

        :param sts_token: The stsToken of sdk config.
        :type sts_token: str
        """
        self._sts_token = sts_token

    @property
    def region_id(self):
        """Gets the regionId of sdk config.

         regionId

        :return: The regionId of sdk config.
        :rtype: str.
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the regionId of sdk config.

         regionId

        :param region_id: The regionId of sdk config.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def ignore_ssl_verification(self):
        """Gets the config switch of ssl verification.

         ignore ssl verification switch

        :return: The config switch of ssl verification.
        :rtype: str.
        """
        return self._ignore_ssl_verification

    @ignore_ssl_verification.setter
    def ignore_ssl_verification(self, ignore_ssl_verification):
        """Sets the config switch of ssl verification.

         ignore ssl verification switch

        :param ignore_ssl_verification: The proxy config switch of ssl verification.
        :type ignore_ssl_verification: bool
        """
        self._ignore_ssl_verification = ignore_ssl_verification

    @property
    def ca_certificate_path(self):
        """Gets the ca certificate file path.

         ca certificate file path

        :return: The ca certificate file path.
        :rtype: str.
        """
        return self._ca_certificate_path

    @ca_certificate_path.setter
    def ca_certificate_path(self, ca_certificate_path):
        """Sets the ca certificate file path.

         ca certificate file path

        :param ca_certificate_path: The ca certificate file path.
        :type ca_certificate_path: str
        """
        self._ca_certificate_path = ca_certificate_path

    @property
    def project_id(self):
        """Gets the projectId of sdk config.

         projectId

        :return: The projectId of sdk config.
        :rtype: str.
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the projectId of sdk config.

         projectId

        :param project_id: The projectId of sdk config.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def connection_timeout(self):
        """Gets the connection timeout time of sdk config.

         connection timeout time

        :return: The connection timeout time of sdk config.
        :rtype: int.
        """
        return self._connection_timeout

    @connection_timeout.setter
    def connection_timeout(self, connection_timeout):
        """Sets the connection timeout time of sdk config.

         connection timeout time

        :param connection_timeout: The connection timeout time of sdk config.
        :type connection_timeout: sint
        """
        self._connection_timeout = connection_timeout

    @property
    def read_timeout(self):
        """Gets the read timeout time of sdk config.

         read timeout time

        :return: The read timeout time of sdk config.
        :rtype: int.
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        """Sets the read timeout time of sdk config.

         read timeout time

        :param read_timeout: The read timeout time of sdk config.
        :type read_timeout: sint
        """
        self._read_timeout = read_timeout

    @property
    def proxy_protocol(self):
        """Gets the proxy protocol of sdk config.

         proxy protocol

        :return: The proxy protocol of sdk config.
        :rtype: str.
        """
        return self._proxy_protocol

    @proxy_protocol.setter
    def proxy_protocol(self, proxy_protocol):
        """Sets the proxy protocol of sdk config.

         proxy protocol

        :param proxy_protocol: The proxy protocol of sdk config.
        :type proxy_protocol: sint
        """
        self._proxy_protocol = proxy_protocol

    @property
    def proxy_host(self):
        """Gets the proxy host of sdk config.

         proxy host

        :return: The proxy host of sdk config.
        :rtype: str.
        """
        return self._proxy_host

    @proxy_host.setter
    def proxy_host(self, proxy_host):
        """Sets the proxy host of sdk config.

         proxy host

        :param proxy_host: The proxy host of sdk config.
        :type proxy_host: str
        """
        self._proxy_host = proxy_host

    @property
    def proxy_port(self):
        """Gets the proxy port of sdk config.

         proxy port

        :return: The proxy port of sdk config.
        :rtype: int.
        """
        return self._proxy_port

    @proxy_port.setter
    def proxy_port(self, proxy_port):
        """Sets the proxy port of sdk config.

         proxy port

        :param proxy_port: The proxy port of sdk config.
        :type proxy_port: int
        """
        self._proxy_port = proxy_port

    @property
    def proxy_user(self):
        """Gets the proxy user of sdk config.

         proxy user

        :return: The proxy user of sdk config.
        :rtype: str.
        """
        return self._proxy_user

    @proxy_user.setter
    def proxy_user(self, proxy_user):
        """Sets the proxy user of sdk config.

         proxy user

        :param proxy_user: The proxy user of sdk config.
        :type proxy_user: str
        """
        self._proxy_user = proxy_user

    @property
    def proxy_password(self):
        """Gets the proxy password of sdk config.

         proxy user

        :return: The proxy password of sdk config.
        :rtype: str.
        """
        return self._proxy_password

    @proxy_password.setter
    def proxy_password(self, proxy_password):
        """Sets the proxy password of sdk config.

         proxy user

        :param proxy_password: The proxy password of sdk config.
        :type proxy_password: str
        """
        self._proxy_password = proxy_password

    @property
    def file_log_path(self):
        """Gets the sdk file log path of sdk config.

         sdk file log path

        :return: The sdk file log path of sdk config.
        :rtype: str.
        """
        return self._file_log_path

    @file_log_path.setter
    def file_log_path(self, file_log_path):
        """Sets the sdk file log path of sdk config.

         sdk file log path

        :param file_log_path: The sdk file log path of sdk config.
        :type file_log_path: str
        """
        self._file_log_path = file_log_path

    @property
    def file_log_level(self):
        """Gets the sdk file log level of sdk config.

         sdk file log level

        :return: The sdk file log path of sdk config.
        :rtype: str.
        """
        return self._file_log_level

    @file_log_level.setter
    def file_log_level(self, file_log_level):
        """Sets the sdk file log level of sdk config.

         sdk file log level

        :param file_log_level: The sdk file log level of sdk config.
        :type file_log_level: str
        """
        self._file_log_level = file_log_level

    @property
    def customize_http_config(self):
        """Gets the customized http config.

         customized http config

        :return: The customized http config.
        :rtype: class:`huaweicloudsdkcore.http.HttpConfig`
        """
        return self._customize_http_config

    @customize_http_config.setter
    def customize_http_config(self, customize_http_config):
        """Sets the customized http config.

         customized http config

        :param customize_http_config: The customized http config.
        :type customize_http_config: class:`huaweicloudsdkcore.http.HttpConfig`
        """
        self._customize_http_config = customize_http_config

   def load_config(self):
        self._config.read(self._config_file_path, 'utf-8')
        self.load_multichannel_sdk_config()
        self.load_verification_config()
        self.load_union_sdk_config()

    def load_multichannel_sdk_config(self):
        section_name = "multichannel_sdk_config"
        heartbeat_interval = self._config.get(section_name, 'heartbeat_interval')
        if heartbeat_interval is not None and len(heartbeat_interval) != 0 and str.isdigit(heartbeat_interval) and int(
                heartbeat_interval) != 0:
            self.heartbeat_interval = int(heartbeat_interval)

        heartbeat_thread_pool_size = self._config.get(section_name, 'heartbeat_thread_pool_size')
        if heartbeat_thread_pool_size is not None and len(heartbeat_thread_pool_size) != 0 and str.isdigit(
                heartbeat_thread_pool_size) and int(heartbeat_thread_pool_size) != 0:
            self.heartbeat_thread_pool_size = int(heartbeat_thread_pool_size)

        reload_interval = self._config.get(section_name, 'config_reload_interval')
        if reload_interval is not None and len(reload_interval) != 0 and str.isdigit(reload_interval) and int(
                reload_interval) != 0:
            self.reload_interval = int(reload_interval)

        api_retry_count = self._config.get(section_name, 'api_retry_count')
        if api_retry_count is not None and len(api_retry_count) != 0 and str.isdigit(api_retry_count) and int(
                api_retry_count) != 0:
            self.api_retry_count = int(api_retry_count)
        self.load_endpoint_config(section_name)

    def load_endpoint_config(self, section_name):
        endpoint_names = self._config.get(section_name, 'endpoint_names')
        if endpoint_names is not None and len(endpoint_names) != 0:
            self.endpoint_name_list = endpoint_names.split(',')

        endpoint_weights = self._config.get(section_name, 'endpoint_weights')
        if endpoint_weights is not None and len(endpoint_weights) != 0:
            self.endpoint_weight_list = endpoint_weights.split(',')

    def load_verification_config(self):
        section_name = "verification_config"
        ak = self._config.get(section_name, 'ak')
        if ak is not None and len(ak) != 0:
            self.ak = ak

        sk = self._config.get(section_name, 'sk')
        if sk is not None and len(sk) != 0:
            self.sk = sk

        sts_token = self._config.get(section_name, 'sts_token')
        if sts_token is not None and len(sts_token) != 0:
            self.sts_token = sts_token

        ignore_ssl_verification = self._config.get(section_name, 'ignore_ssl_verification')
        if ignore_ssl_verification is not None and len(ignore_ssl_verification) != 0:
            if ignore_ssl_verification.lower() == "true":
                self.ignore_ssl_verification = True
            elif ignore_ssl_verification.lower() == "false":
                self.ignore_ssl_verification = False

        ca_certificate_path = self._config.get(section_name, 'ca_certificate_path')
        if ca_certificate_path is not None and len(ca_certificate_path) != 0:
            self.ca_certificate_path = ca_certificate_path

        project_id = self._config.get(section_name, 'project_id')
        if project_id is not None and len(project_id) != 0:
            self.project_id = project_id

    def load_union_sdk_config(self):
        section_name = "union_sdk_config"
        region_id = self._config.get(section_name, 'region_id')
        if region_id is not None and len(region_id) != 0:
            self.region_id = region_id

        connection_timeout = self._config.get(section_name, 'connection_timeout')
        if connection_timeout is not None and len(connection_timeout) != 0 and str.isdigit(connection_timeout) and int(
                connection_timeout) != 0:
            self.connection_timeout = int(connection_timeout)

        read_timeout = self._config.get(section_name, 'read_timeout')
        if read_timeout is not None and len(read_timeout) != 0 and str.isdigit(read_timeout) and int(read_timeout) != 0:
            self.read_timeout = int(read_timeout)

        file_log_path = self._config.get(section_name, 'file_log_path')
        if file_log_path is not None and len(file_log_path) != 0:
            self.file_log_path = file_log_path

        file_log_level = self._config.get(section_name, 'file_log_level')
        if file_log_level is not None and len(file_log_level) != 0:
            self.file_log_level = file_log_level

        self.load_proxy_config(section_name)

    def load_proxy_config(self, section_name):
        proxy_protocol = self._config.get(section_name, 'proxy_protocol')
        if proxy_protocol is not None and len(proxy_protocol) != 0:
            self.proxy_protocol = proxy_protocol

        proxy_host = self._config.get(section_name, 'proxy_host')
        if proxy_host is not None and len(proxy_host) != 0:
            self.proxy_host = proxy_host

        proxy_port = self._config.get(section_name, 'proxy_port')
        if proxy_port is not None and len(proxy_port) != 0 and str.isdigit(proxy_port):
            self.proxy_port = int(proxy_port)

        proxy_user = self._config.get(section_name, 'proxy_user')
        if proxy_user is not None and len(proxy_user) != 0:
            self.proxy_user = proxy_user

        proxy_password = self._config.get(section_name, 'proxy_password')
        if proxy_password is not None and len(proxy_password) != 0:
            self.proxy_password = proxy_password

    def load_endpoint_list(self):
        endpoint_list = []
        for index in range(len(self.endpoint_name_list)):
            if len(self.endpoint_weight_list) == 0:
                endpoint_list.append(Endpoint(self.endpoint_name_list[index], 1))
            elif len(self.endpoint_weight_list) > index and str.isdigit(self.endpoint_weight_list[index]):
                endpoint_list.append(Endpoint(self.endpoint_name_list[index], int(self.endpoint_weight_list[index])))
            else:
                self._logger.error("endpointWeightList or endpointNameList is error!")
                break
        return endpoint_list
