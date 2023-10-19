# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationDataSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rds_id': 'str',
        'rds_db_name': 'str',
        'rds_address': 'str',
        'rds_username': 'str',
        'rds_password': 'str',
        'rds_port': 'str',
        'config_center_addr': 'str',
        'service_center_addr': 'str',
        'cse_id': 'str',
        'envs': 'dict(str, str)',
        'ip': 'str',
        'items': 'list[AccessConfigurationDataItems]',
        'max_replica_count': 'int',
        'triggers': 'list[ScaleConfigurationDataTrigger]',
        'volumes': 'list[VolumeConfigurationDataVolume]',
        'liveness_probe': 'HealthCheckConfigurationLivenessProbe',
        'startup_probe': 'HealthCheckConfigurationStartupProbe',
        'readiness_probe': 'HealthCheckConfigurationReadinessProbe',
        'post_start': 'ConfigurationDataSpecPostStart',
        'pre_stop': 'ConfigurationDataSpecPreStop',
        'log_paths': 'list[str]',
        'access_key': 'str',
        'access_value': 'str',
        'business': 'str',
        'image_pull_policy': 'str',
        'version': 'str',
        'path': 'str',
        'port': 'str',
        'metrics': 'list[str]'
    }

    attribute_map = {
        'rds_id': 'rds_id',
        'rds_db_name': 'rds_db_name',
        'rds_address': 'rds_address',
        'rds_username': 'rds_username',
        'rds_password': 'rds_password',
        'rds_port': 'rds_port',
        'config_center_addr': 'config_center_addr',
        'service_center_addr': 'service_center_addr',
        'cse_id': 'cse_id',
        'envs': 'envs',
        'ip': 'ip',
        'items': 'items',
        'max_replica_count': 'max_replica_count',
        'triggers': 'triggers',
        'volumes': 'volumes',
        'liveness_probe': 'livenessProbe',
        'startup_probe': 'startupProbe',
        'readiness_probe': 'readinessProbe',
        'post_start': 'postStart',
        'pre_stop': 'preStop',
        'log_paths': 'log_paths',
        'access_key': 'access_key',
        'access_value': 'access_value',
        'business': 'business',
        'image_pull_policy': 'image_pull_policy',
        'version': 'version',
        'path': 'path',
        'port': 'port',
        'metrics': 'metrics'
    }

    def __init__(self, rds_id=None, rds_db_name=None, rds_address=None, rds_username=None, rds_password=None, rds_port=None, config_center_addr=None, service_center_addr=None, cse_id=None, envs=None, ip=None, items=None, max_replica_count=None, triggers=None, volumes=None, liveness_probe=None, startup_probe=None, readiness_probe=None, post_start=None, pre_stop=None, log_paths=None, access_key=None, access_value=None, business=None, image_pull_policy=None, version=None, path=None, port=None, metrics=None):
        """ConfigurationDataSpec

        The model defined in huaweicloud sdk

        :param rds_id: - type为\&quot;rds\&quot;时，配置此参数。 - 参数含义：RDS数据库实例ID。
        :type rds_id: str
        :param rds_db_name: - type为\&quot;rds\&quot;时，配置此参数。 - 参数含义：RDS数据库名称。
        :type rds_db_name: str
        :param rds_address: - type为\&quot;rds\&quot;时，配置此参数。 - 参数含义：RDS数据库地址。
        :type rds_address: str
        :param rds_username: - type为\&quot;rds\&quot;时，配置此参数。 - 参数含义：RDS数据库用户名称。
        :type rds_username: str
        :param rds_password: - type为\&quot;rds\&quot;时，配置此参数。 - 参数含义：RDS数据库密码。
        :type rds_password: str
        :param rds_port: - type为\&quot;rds\&quot;时，配置此参数。 - 参数含义：RDS数据库端口
        :type rds_port: str
        :param config_center_addr: - type为\&quot;cse\&quot;时，配置此参数。 - 参数含义：CSE配置中心地址。
        :type config_center_addr: str
        :param service_center_addr: - type为\&quot;cse\&quot;时，配置此参数。 - 参数含义：CSE服务注册发现地址。
        :type service_center_addr: str
        :param cse_id: - type为\&quot;cse\&quot;时，配置此参数。 - 参数含义：CSE引擎ID。
        :type cse_id: str
        :param envs: 环境变量配置，常用环境变量如下。 - TZ: 时区设置，东八区可设置为Asia/Shanghai。 - LANG: 语言字符集设置，中文UTF8可设置为zh_CN.UTF-8。
        :type envs: dict(str, str)
        :param ip: 弹性公网IP，响应体参数，未配置域名时返回此参数。
        :type ip: str
        :param items: - type为\&quot;access\&quot;时，配置此参数。 - 参数含义：访问方式配置列表。
        :type items: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationDataItems`]
        :param max_replica_count: - type为\&quot;scaling\&quot;时，配置此参数。 - 参数含义：伸缩策略配置最大伸缩个数。
        :type max_replica_count: int
        :param triggers: - type为\&quot;scaling\&quot;时，配置此参数。 - 参数含义：伸缩策略配置触发器列表。
        :type triggers: list[:class:`huaweicloudsdkcae.v1.ScaleConfigurationDataTrigger`]
        :param volumes: - type为\&quot;volume\&quot;时，配置此参数。 - 参数含义：云存储配置列表。
        :type volumes: list[:class:`huaweicloudsdkcae.v1.VolumeConfigurationDataVolume`]
        :param liveness_probe: 
        :type liveness_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationLivenessProbe`
        :param startup_probe: 
        :type startup_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationStartupProbe`
        :param readiness_probe: 
        :type readiness_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationReadinessProbe`
        :param post_start: 
        :type post_start: :class:`huaweicloudsdkcae.v1.ConfigurationDataSpecPostStart`
        :param pre_stop: 
        :type pre_stop: :class:`huaweicloudsdkcae.v1.ConfigurationDataSpecPreStop`
        :param log_paths: - type为\&quot;log\&quot;时，配置此参数。 - 参数含义：自定义日志路径数组。
        :type log_paths: list[str]
        :param access_key: - type为\&quot;apm2\&quot;时，配置此参数。 - 参数含义：性能管理配置访问密钥Key。
        :type access_key: str
        :param access_value: - type为\&quot;apm2\&quot;时，配置此参数。 - 参数含义：性能管理配置访问密钥value。
        :type access_value: str
        :param business: - type为\&quot;apm2\&quot;时，配置此参数。 - 参数含义：性能管理配置应用。
        :type business: str
        :param image_pull_policy: - type为\&quot;apm2\&quot;时，配置此参数。 - 参数含义：性能管理配置升级策略。 - 重启自动升级：每次都尝试重新下载镜像。 - 手动升级: 如果本地有该镜像，则继续使用本地镜像，不下载镜像。
        :type image_pull_policy: str
        :param version: - type为\&quot;apm2\&quot;时，配置此参数。 - 参数含义：性能管理配置探针版本。
        :type version: str
        :param path: - type为\&quot;customMetric\&quot;时，配置此参数。 - 参数含义：自定义监控指标配置采集路径。
        :type path: str
        :param port: - type为\&quot;customMetric\&quot;时，配置此参数。 - 参数含义：自定义监控指标配置采集端口。
        :type port: str
        :param metrics: - type为\&quot;customMetric\&quot;时，配置此参数。 - 参数含义：自定义监控指标配置指标名称。
        :type metrics: list[str]
        """
        
        

        self._rds_id = None
        self._rds_db_name = None
        self._rds_address = None
        self._rds_username = None
        self._rds_password = None
        self._rds_port = None
        self._config_center_addr = None
        self._service_center_addr = None
        self._cse_id = None
        self._envs = None
        self._ip = None
        self._items = None
        self._max_replica_count = None
        self._triggers = None
        self._volumes = None
        self._liveness_probe = None
        self._startup_probe = None
        self._readiness_probe = None
        self._post_start = None
        self._pre_stop = None
        self._log_paths = None
        self._access_key = None
        self._access_value = None
        self._business = None
        self._image_pull_policy = None
        self._version = None
        self._path = None
        self._port = None
        self._metrics = None
        self.discriminator = None

        if rds_id is not None:
            self.rds_id = rds_id
        if rds_db_name is not None:
            self.rds_db_name = rds_db_name
        if rds_address is not None:
            self.rds_address = rds_address
        if rds_username is not None:
            self.rds_username = rds_username
        if rds_password is not None:
            self.rds_password = rds_password
        if rds_port is not None:
            self.rds_port = rds_port
        if config_center_addr is not None:
            self.config_center_addr = config_center_addr
        if service_center_addr is not None:
            self.service_center_addr = service_center_addr
        if cse_id is not None:
            self.cse_id = cse_id
        if envs is not None:
            self.envs = envs
        if ip is not None:
            self.ip = ip
        if items is not None:
            self.items = items
        if max_replica_count is not None:
            self.max_replica_count = max_replica_count
        if triggers is not None:
            self.triggers = triggers
        if volumes is not None:
            self.volumes = volumes
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if startup_probe is not None:
            self.startup_probe = startup_probe
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        if post_start is not None:
            self.post_start = post_start
        if pre_stop is not None:
            self.pre_stop = pre_stop
        if log_paths is not None:
            self.log_paths = log_paths
        if access_key is not None:
            self.access_key = access_key
        if access_value is not None:
            self.access_value = access_value
        if business is not None:
            self.business = business
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if version is not None:
            self.version = version
        if path is not None:
            self.path = path
        if port is not None:
            self.port = port
        if metrics is not None:
            self.metrics = metrics

    @property
    def rds_id(self):
        """Gets the rds_id of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库实例ID。

        :return: The rds_id of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._rds_id

    @rds_id.setter
    def rds_id(self, rds_id):
        """Sets the rds_id of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库实例ID。

        :param rds_id: The rds_id of this ConfigurationDataSpec.
        :type rds_id: str
        """
        self._rds_id = rds_id

    @property
    def rds_db_name(self):
        """Gets the rds_db_name of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库名称。

        :return: The rds_db_name of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._rds_db_name

    @rds_db_name.setter
    def rds_db_name(self, rds_db_name):
        """Sets the rds_db_name of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库名称。

        :param rds_db_name: The rds_db_name of this ConfigurationDataSpec.
        :type rds_db_name: str
        """
        self._rds_db_name = rds_db_name

    @property
    def rds_address(self):
        """Gets the rds_address of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库地址。

        :return: The rds_address of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._rds_address

    @rds_address.setter
    def rds_address(self, rds_address):
        """Sets the rds_address of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库地址。

        :param rds_address: The rds_address of this ConfigurationDataSpec.
        :type rds_address: str
        """
        self._rds_address = rds_address

    @property
    def rds_username(self):
        """Gets the rds_username of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库用户名称。

        :return: The rds_username of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._rds_username

    @rds_username.setter
    def rds_username(self, rds_username):
        """Sets the rds_username of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库用户名称。

        :param rds_username: The rds_username of this ConfigurationDataSpec.
        :type rds_username: str
        """
        self._rds_username = rds_username

    @property
    def rds_password(self):
        """Gets the rds_password of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库密码。

        :return: The rds_password of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._rds_password

    @rds_password.setter
    def rds_password(self, rds_password):
        """Sets the rds_password of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库密码。

        :param rds_password: The rds_password of this ConfigurationDataSpec.
        :type rds_password: str
        """
        self._rds_password = rds_password

    @property
    def rds_port(self):
        """Gets the rds_port of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库端口

        :return: The rds_port of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._rds_port

    @rds_port.setter
    def rds_port(self, rds_port):
        """Sets the rds_port of this ConfigurationDataSpec.

        - type为\"rds\"时，配置此参数。 - 参数含义：RDS数据库端口

        :param rds_port: The rds_port of this ConfigurationDataSpec.
        :type rds_port: str
        """
        self._rds_port = rds_port

    @property
    def config_center_addr(self):
        """Gets the config_center_addr of this ConfigurationDataSpec.

        - type为\"cse\"时，配置此参数。 - 参数含义：CSE配置中心地址。

        :return: The config_center_addr of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._config_center_addr

    @config_center_addr.setter
    def config_center_addr(self, config_center_addr):
        """Sets the config_center_addr of this ConfigurationDataSpec.

        - type为\"cse\"时，配置此参数。 - 参数含义：CSE配置中心地址。

        :param config_center_addr: The config_center_addr of this ConfigurationDataSpec.
        :type config_center_addr: str
        """
        self._config_center_addr = config_center_addr

    @property
    def service_center_addr(self):
        """Gets the service_center_addr of this ConfigurationDataSpec.

        - type为\"cse\"时，配置此参数。 - 参数含义：CSE服务注册发现地址。

        :return: The service_center_addr of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._service_center_addr

    @service_center_addr.setter
    def service_center_addr(self, service_center_addr):
        """Sets the service_center_addr of this ConfigurationDataSpec.

        - type为\"cse\"时，配置此参数。 - 参数含义：CSE服务注册发现地址。

        :param service_center_addr: The service_center_addr of this ConfigurationDataSpec.
        :type service_center_addr: str
        """
        self._service_center_addr = service_center_addr

    @property
    def cse_id(self):
        """Gets the cse_id of this ConfigurationDataSpec.

        - type为\"cse\"时，配置此参数。 - 参数含义：CSE引擎ID。

        :return: The cse_id of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._cse_id

    @cse_id.setter
    def cse_id(self, cse_id):
        """Sets the cse_id of this ConfigurationDataSpec.

        - type为\"cse\"时，配置此参数。 - 参数含义：CSE引擎ID。

        :param cse_id: The cse_id of this ConfigurationDataSpec.
        :type cse_id: str
        """
        self._cse_id = cse_id

    @property
    def envs(self):
        """Gets the envs of this ConfigurationDataSpec.

        环境变量配置，常用环境变量如下。 - TZ: 时区设置，东八区可设置为Asia/Shanghai。 - LANG: 语言字符集设置，中文UTF8可设置为zh_CN.UTF-8。

        :return: The envs of this ConfigurationDataSpec.
        :rtype: dict(str, str)
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        """Sets the envs of this ConfigurationDataSpec.

        环境变量配置，常用环境变量如下。 - TZ: 时区设置，东八区可设置为Asia/Shanghai。 - LANG: 语言字符集设置，中文UTF8可设置为zh_CN.UTF-8。

        :param envs: The envs of this ConfigurationDataSpec.
        :type envs: dict(str, str)
        """
        self._envs = envs

    @property
    def ip(self):
        """Gets the ip of this ConfigurationDataSpec.

        弹性公网IP，响应体参数，未配置域名时返回此参数。

        :return: The ip of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ConfigurationDataSpec.

        弹性公网IP，响应体参数，未配置域名时返回此参数。

        :param ip: The ip of this ConfigurationDataSpec.
        :type ip: str
        """
        self._ip = ip

    @property
    def items(self):
        """Gets the items of this ConfigurationDataSpec.

        - type为\"access\"时，配置此参数。 - 参数含义：访问方式配置列表。

        :return: The items of this ConfigurationDataSpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationDataItems`]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ConfigurationDataSpec.

        - type为\"access\"时，配置此参数。 - 参数含义：访问方式配置列表。

        :param items: The items of this ConfigurationDataSpec.
        :type items: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationDataItems`]
        """
        self._items = items

    @property
    def max_replica_count(self):
        """Gets the max_replica_count of this ConfigurationDataSpec.

        - type为\"scaling\"时，配置此参数。 - 参数含义：伸缩策略配置最大伸缩个数。

        :return: The max_replica_count of this ConfigurationDataSpec.
        :rtype: int
        """
        return self._max_replica_count

    @max_replica_count.setter
    def max_replica_count(self, max_replica_count):
        """Sets the max_replica_count of this ConfigurationDataSpec.

        - type为\"scaling\"时，配置此参数。 - 参数含义：伸缩策略配置最大伸缩个数。

        :param max_replica_count: The max_replica_count of this ConfigurationDataSpec.
        :type max_replica_count: int
        """
        self._max_replica_count = max_replica_count

    @property
    def triggers(self):
        """Gets the triggers of this ConfigurationDataSpec.

        - type为\"scaling\"时，配置此参数。 - 参数含义：伸缩策略配置触发器列表。

        :return: The triggers of this ConfigurationDataSpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ScaleConfigurationDataTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """Sets the triggers of this ConfigurationDataSpec.

        - type为\"scaling\"时，配置此参数。 - 参数含义：伸缩策略配置触发器列表。

        :param triggers: The triggers of this ConfigurationDataSpec.
        :type triggers: list[:class:`huaweicloudsdkcae.v1.ScaleConfigurationDataTrigger`]
        """
        self._triggers = triggers

    @property
    def volumes(self):
        """Gets the volumes of this ConfigurationDataSpec.

        - type为\"volume\"时，配置此参数。 - 参数含义：云存储配置列表。

        :return: The volumes of this ConfigurationDataSpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.VolumeConfigurationDataVolume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this ConfigurationDataSpec.

        - type为\"volume\"时，配置此参数。 - 参数含义：云存储配置列表。

        :param volumes: The volumes of this ConfigurationDataSpec.
        :type volumes: list[:class:`huaweicloudsdkcae.v1.VolumeConfigurationDataVolume`]
        """
        self._volumes = volumes

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this ConfigurationDataSpec.

        :return: The liveness_probe of this ConfigurationDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationLivenessProbe`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this ConfigurationDataSpec.

        :param liveness_probe: The liveness_probe of this ConfigurationDataSpec.
        :type liveness_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationLivenessProbe`
        """
        self._liveness_probe = liveness_probe

    @property
    def startup_probe(self):
        """Gets the startup_probe of this ConfigurationDataSpec.

        :return: The startup_probe of this ConfigurationDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationStartupProbe`
        """
        return self._startup_probe

    @startup_probe.setter
    def startup_probe(self, startup_probe):
        """Sets the startup_probe of this ConfigurationDataSpec.

        :param startup_probe: The startup_probe of this ConfigurationDataSpec.
        :type startup_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationStartupProbe`
        """
        self._startup_probe = startup_probe

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this ConfigurationDataSpec.

        :return: The readiness_probe of this ConfigurationDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationReadinessProbe`
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this ConfigurationDataSpec.

        :param readiness_probe: The readiness_probe of this ConfigurationDataSpec.
        :type readiness_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationReadinessProbe`
        """
        self._readiness_probe = readiness_probe

    @property
    def post_start(self):
        """Gets the post_start of this ConfigurationDataSpec.

        :return: The post_start of this ConfigurationDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.ConfigurationDataSpecPostStart`
        """
        return self._post_start

    @post_start.setter
    def post_start(self, post_start):
        """Sets the post_start of this ConfigurationDataSpec.

        :param post_start: The post_start of this ConfigurationDataSpec.
        :type post_start: :class:`huaweicloudsdkcae.v1.ConfigurationDataSpecPostStart`
        """
        self._post_start = post_start

    @property
    def pre_stop(self):
        """Gets the pre_stop of this ConfigurationDataSpec.

        :return: The pre_stop of this ConfigurationDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.ConfigurationDataSpecPreStop`
        """
        return self._pre_stop

    @pre_stop.setter
    def pre_stop(self, pre_stop):
        """Sets the pre_stop of this ConfigurationDataSpec.

        :param pre_stop: The pre_stop of this ConfigurationDataSpec.
        :type pre_stop: :class:`huaweicloudsdkcae.v1.ConfigurationDataSpecPreStop`
        """
        self._pre_stop = pre_stop

    @property
    def log_paths(self):
        """Gets the log_paths of this ConfigurationDataSpec.

        - type为\"log\"时，配置此参数。 - 参数含义：自定义日志路径数组。

        :return: The log_paths of this ConfigurationDataSpec.
        :rtype: list[str]
        """
        return self._log_paths

    @log_paths.setter
    def log_paths(self, log_paths):
        """Sets the log_paths of this ConfigurationDataSpec.

        - type为\"log\"时，配置此参数。 - 参数含义：自定义日志路径数组。

        :param log_paths: The log_paths of this ConfigurationDataSpec.
        :type log_paths: list[str]
        """
        self._log_paths = log_paths

    @property
    def access_key(self):
        """Gets the access_key of this ConfigurationDataSpec.

        - type为\"apm2\"时，配置此参数。 - 参数含义：性能管理配置访问密钥Key。

        :return: The access_key of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this ConfigurationDataSpec.

        - type为\"apm2\"时，配置此参数。 - 参数含义：性能管理配置访问密钥Key。

        :param access_key: The access_key of this ConfigurationDataSpec.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def access_value(self):
        """Gets the access_value of this ConfigurationDataSpec.

        - type为\"apm2\"时，配置此参数。 - 参数含义：性能管理配置访问密钥value。

        :return: The access_value of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._access_value

    @access_value.setter
    def access_value(self, access_value):
        """Sets the access_value of this ConfigurationDataSpec.

        - type为\"apm2\"时，配置此参数。 - 参数含义：性能管理配置访问密钥value。

        :param access_value: The access_value of this ConfigurationDataSpec.
        :type access_value: str
        """
        self._access_value = access_value

    @property
    def business(self):
        """Gets the business of this ConfigurationDataSpec.

        - type为\"apm2\"时，配置此参数。 - 参数含义：性能管理配置应用。

        :return: The business of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._business

    @business.setter
    def business(self, business):
        """Sets the business of this ConfigurationDataSpec.

        - type为\"apm2\"时，配置此参数。 - 参数含义：性能管理配置应用。

        :param business: The business of this ConfigurationDataSpec.
        :type business: str
        """
        self._business = business

    @property
    def image_pull_policy(self):
        """Gets the image_pull_policy of this ConfigurationDataSpec.

        - type为\"apm2\"时，配置此参数。 - 参数含义：性能管理配置升级策略。 - 重启自动升级：每次都尝试重新下载镜像。 - 手动升级: 如果本地有该镜像，则继续使用本地镜像，不下载镜像。

        :return: The image_pull_policy of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """Sets the image_pull_policy of this ConfigurationDataSpec.

        - type为\"apm2\"时，配置此参数。 - 参数含义：性能管理配置升级策略。 - 重启自动升级：每次都尝试重新下载镜像。 - 手动升级: 如果本地有该镜像，则继续使用本地镜像，不下载镜像。

        :param image_pull_policy: The image_pull_policy of this ConfigurationDataSpec.
        :type image_pull_policy: str
        """
        self._image_pull_policy = image_pull_policy

    @property
    def version(self):
        """Gets the version of this ConfigurationDataSpec.

        - type为\"apm2\"时，配置此参数。 - 参数含义：性能管理配置探针版本。

        :return: The version of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ConfigurationDataSpec.

        - type为\"apm2\"时，配置此参数。 - 参数含义：性能管理配置探针版本。

        :param version: The version of this ConfigurationDataSpec.
        :type version: str
        """
        self._version = version

    @property
    def path(self):
        """Gets the path of this ConfigurationDataSpec.

        - type为\"customMetric\"时，配置此参数。 - 参数含义：自定义监控指标配置采集路径。

        :return: The path of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ConfigurationDataSpec.

        - type为\"customMetric\"时，配置此参数。 - 参数含义：自定义监控指标配置采集路径。

        :param path: The path of this ConfigurationDataSpec.
        :type path: str
        """
        self._path = path

    @property
    def port(self):
        """Gets the port of this ConfigurationDataSpec.

        - type为\"customMetric\"时，配置此参数。 - 参数含义：自定义监控指标配置采集端口。

        :return: The port of this ConfigurationDataSpec.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ConfigurationDataSpec.

        - type为\"customMetric\"时，配置此参数。 - 参数含义：自定义监控指标配置采集端口。

        :param port: The port of this ConfigurationDataSpec.
        :type port: str
        """
        self._port = port

    @property
    def metrics(self):
        """Gets the metrics of this ConfigurationDataSpec.

        - type为\"customMetric\"时，配置此参数。 - 参数含义：自定义监控指标配置指标名称。

        :return: The metrics of this ConfigurationDataSpec.
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ConfigurationDataSpec.

        - type为\"customMetric\"时，配置此参数。 - 参数含义：自定义监控指标配置指标名称。

        :param metrics: The metrics of this ConfigurationDataSpec.
        :type metrics: list[str]
        """
        self._metrics = metrics

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConfigurationDataSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
