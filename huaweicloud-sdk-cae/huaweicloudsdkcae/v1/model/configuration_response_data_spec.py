# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationResponseDataSpec:

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
        'scale_strategy': 'str',
        'max_replica_count': 'int',
        'min_replica_count': 'int',
        'advanced': 'ScaleConfigurationDataAdvanced',
        'triggers': 'list[ScaleConfigurationDataTrigger]',
        'volumes': 'list[VolumeConfigurationDataVolume]',
        'liveness_probe': 'HealthCheckConfigurationLivenessProbe',
        'startup_probe': 'HealthCheckConfigurationStartupProbe',
        'readiness_probe': 'HealthCheckConfigurationReadinessProbe',
        'post_start': 'ConfigurationResponseDataSpecPostStart',
        'pre_stop': 'ConfigurationResponseDataSpecPreStop',
        'log_paths': 'list[str]',
        'cloud_storage_log_paths': 'list[CloudStorageLogPathInfo]',
        'instrumentation': 'str',
        'apm_application': 'str',
        'type': 'str',
        'app_name': 'str',
        'instance_name': 'str',
        'env_name': 'str',
        'image_pull_policy': 'str',
        'version': 'str',
        'access_key': 'str',
        'access_value': 'str',
        'business': 'str',
        'path': 'str',
        'port': 'int',
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
        'scale_strategy': 'scale_strategy',
        'max_replica_count': 'max_replica_count',
        'min_replica_count': 'min_replica_count',
        'advanced': 'advanced',
        'triggers': 'triggers',
        'volumes': 'volumes',
        'liveness_probe': 'livenessProbe',
        'startup_probe': 'startupProbe',
        'readiness_probe': 'readinessProbe',
        'post_start': 'postStart',
        'pre_stop': 'preStop',
        'log_paths': 'log_paths',
        'cloud_storage_log_paths': 'cloud_storage_log_paths',
        'instrumentation': 'instrumentation',
        'apm_application': 'apm_application',
        'type': 'type',
        'app_name': 'app_name',
        'instance_name': 'instance_name',
        'env_name': 'env_name',
        'image_pull_policy': 'image_pull_policy',
        'version': 'version',
        'access_key': 'access_key',
        'access_value': 'access_value',
        'business': 'business',
        'path': 'path',
        'port': 'port',
        'metrics': 'metrics'
    }

    def __init__(self, rds_id=None, rds_db_name=None, rds_address=None, rds_username=None, rds_password=None, rds_port=None, config_center_addr=None, service_center_addr=None, cse_id=None, envs=None, ip=None, items=None, scale_strategy=None, max_replica_count=None, min_replica_count=None, advanced=None, triggers=None, volumes=None, liveness_probe=None, startup_probe=None, readiness_probe=None, post_start=None, pre_stop=None, log_paths=None, cloud_storage_log_paths=None, instrumentation=None, apm_application=None, type=None, app_name=None, instance_name=None, env_name=None, image_pull_policy=None, version=None, access_key=None, access_value=None, business=None, path=None, port=None, metrics=None):
        r"""ConfigurationResponseDataSpec

        The model defined in huaweicloud sdk

        :param rds_id: RDS数据库实例ID。  Configuration.type为\&quot;rds\&quot;时，返回此参数。 
        :type rds_id: str
        :param rds_db_name: RDS数据库名称。  Configuration.type为\&quot;rds\&quot;时，返回此参数。 
        :type rds_db_name: str
        :param rds_address: RDS数据库地址。  Configuration.type为\&quot;rds\&quot;时，返回此参数。 
        :type rds_address: str
        :param rds_username: RDS数据库用户名称。  Configuration.type为\&quot;rds\&quot;时，返回此参数。 
        :type rds_username: str
        :param rds_password: RDS数据库密码。  Configuration.type为\&quot;rds\&quot;时，返回此参数。 
        :type rds_password: str
        :param rds_port: RDS数据库端口。  Configuration.type为\&quot;rds\&quot;时，返回此参数。 
        :type rds_port: str
        :param config_center_addr: CSE配置中心地址。  Configuration.type为\&quot;cse\&quot;时，返回此参数。 
        :type config_center_addr: str
        :param service_center_addr: CSE服务注册发现地址。  Configuration.type为\&quot;cse\&quot;时，返回此参数。 
        :type service_center_addr: str
        :param cse_id: CSE引擎ID。  Configuration.type为\&quot;cse\&quot;时，返回此参数。 
        :type cse_id: str
        :param envs: 环境变量配置。 常用环境变量如下： - TZ: 时区设置，东八区可设置为Asia/Shanghai。 - LANG: 语言字符集设置，中文UTF8可设置为zh_CN.UTF-8。
        :type envs: dict(str, str)
        :param ip: 弹性公网IP，响应体参数，未配置域名时返回此参数。
        :type ip: str
        :param items: 访问方式配置列表。  Configuration.type为\&quot;access\&quot;时，返回此参数。 
        :type items: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationDataItems`]
        :param scale_strategy: 伸缩策略配置策略类型。  Configuration.type为\&quot;scaling\&quot;时，返回此参数。 
        :type scale_strategy: str
        :param max_replica_count: 伸缩策略配置最大伸缩个数。  Configuration.type为\&quot;scaling\&quot;时，返回此参数。 
        :type max_replica_count: int
        :param min_replica_count: 伸缩策略配置最小伸缩个数。  Configuration.type为\&quot;scaling\&quot;时，返回此参数。 
        :type min_replica_count: int
        :param advanced: 
        :type advanced: :class:`huaweicloudsdkcae.v1.ScaleConfigurationDataAdvanced`
        :param triggers: 伸缩策略配置触发器列表。  Configuration.type为\&quot;scaling\&quot;时，返回此参数。 
        :type triggers: list[:class:`huaweicloudsdkcae.v1.ScaleConfigurationDataTrigger`]
        :param volumes: 云存储配置列表。  Configuration.type为\&quot;volume\&quot;时，返回此参数。 
        :type volumes: list[:class:`huaweicloudsdkcae.v1.VolumeConfigurationDataVolume`]
        :param liveness_probe: 
        :type liveness_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationLivenessProbe`
        :param startup_probe: 
        :type startup_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationStartupProbe`
        :param readiness_probe: 
        :type readiness_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationReadinessProbe`
        :param post_start: 
        :type post_start: :class:`huaweicloudsdkcae.v1.ConfigurationResponseDataSpecPostStart`
        :param pre_stop: 
        :type pre_stop: :class:`huaweicloudsdkcae.v1.ConfigurationResponseDataSpecPreStop`
        :param log_paths: 自定义本地磁盘日志路径数组。  Configuration.type为\&quot;log\&quot;时，返回此参数。 
        :type log_paths: list[str]
        :param cloud_storage_log_paths: 自定义云存储日志路径数组。  Configuration.type为\&quot;log\&quot;时，返回此参数。 
        :type cloud_storage_log_paths: list[:class:`huaweicloudsdkcae.v1.CloudStorageLogPathInfo`]
        :param instrumentation: 探针注入方式。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type instrumentation: str
        :param apm_application: apm2应用。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type apm_application: str
        :param type: 监控系统类别，包括apm2和opentelemetry。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type type: str
        :param app_name: apm2组件。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type app_name: str
        :param instance_name: apm2实例。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type instance_name: str
        :param env_name: apm2环境。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type env_name: str
        :param image_pull_policy: 探针镜像更新策略，已废弃，迁移到监控系统。  - Always，重启自动升级：每次都尝试重新下载镜像。 - IfNotPresent，手动升级: 如果本地有该镜像，则继续使用本地镜像，不下载镜像。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type image_pull_policy: str
        :param version: 增强型探针/opentelemetry探针版本，已废弃，迁移到监控系统。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type version: str
        :param access_key: apm2访问密钥Key，已废弃，迁移到监控系统。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type access_key: str
        :param access_value: apm2访问密钥value，已废弃，迁移到监控系统。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type access_value: str
        :param business: apm2应用，同apm_application，已废弃。  Configuration.type为\&quot;apm2\&quot;时，返回此参数。 
        :type business: str
        :param path: 自定义监控指标配置采集路径。  Configuration.type为\&quot;customMetric\&quot;时，返回此参数。 
        :type path: str
        :param port: 自定义监控指标配置采集端口。  Configuration.type为\&quot;customMetric\&quot;时，返回此参数。 
        :type port: int
        :param metrics: 自定义监控指标配置指标名称。  Configuration.type为\&quot;customMetric\&quot;时，返回此参数。 
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
        self._scale_strategy = None
        self._max_replica_count = None
        self._min_replica_count = None
        self._advanced = None
        self._triggers = None
        self._volumes = None
        self._liveness_probe = None
        self._startup_probe = None
        self._readiness_probe = None
        self._post_start = None
        self._pre_stop = None
        self._log_paths = None
        self._cloud_storage_log_paths = None
        self._instrumentation = None
        self._apm_application = None
        self._type = None
        self._app_name = None
        self._instance_name = None
        self._env_name = None
        self._image_pull_policy = None
        self._version = None
        self._access_key = None
        self._access_value = None
        self._business = None
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
        if scale_strategy is not None:
            self.scale_strategy = scale_strategy
        if max_replica_count is not None:
            self.max_replica_count = max_replica_count
        if min_replica_count is not None:
            self.min_replica_count = min_replica_count
        if advanced is not None:
            self.advanced = advanced
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
        if cloud_storage_log_paths is not None:
            self.cloud_storage_log_paths = cloud_storage_log_paths
        if instrumentation is not None:
            self.instrumentation = instrumentation
        if apm_application is not None:
            self.apm_application = apm_application
        if type is not None:
            self.type = type
        if app_name is not None:
            self.app_name = app_name
        if instance_name is not None:
            self.instance_name = instance_name
        if env_name is not None:
            self.env_name = env_name
        if image_pull_policy is not None:
            self.image_pull_policy = image_pull_policy
        if version is not None:
            self.version = version
        if access_key is not None:
            self.access_key = access_key
        if access_value is not None:
            self.access_value = access_value
        if business is not None:
            self.business = business
        if path is not None:
            self.path = path
        if port is not None:
            self.port = port
        if metrics is not None:
            self.metrics = metrics

    @property
    def rds_id(self):
        r"""Gets the rds_id of this ConfigurationResponseDataSpec.

        RDS数据库实例ID。  Configuration.type为\"rds\"时，返回此参数。 

        :return: The rds_id of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._rds_id

    @rds_id.setter
    def rds_id(self, rds_id):
        r"""Sets the rds_id of this ConfigurationResponseDataSpec.

        RDS数据库实例ID。  Configuration.type为\"rds\"时，返回此参数。 

        :param rds_id: The rds_id of this ConfigurationResponseDataSpec.
        :type rds_id: str
        """
        self._rds_id = rds_id

    @property
    def rds_db_name(self):
        r"""Gets the rds_db_name of this ConfigurationResponseDataSpec.

        RDS数据库名称。  Configuration.type为\"rds\"时，返回此参数。 

        :return: The rds_db_name of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._rds_db_name

    @rds_db_name.setter
    def rds_db_name(self, rds_db_name):
        r"""Sets the rds_db_name of this ConfigurationResponseDataSpec.

        RDS数据库名称。  Configuration.type为\"rds\"时，返回此参数。 

        :param rds_db_name: The rds_db_name of this ConfigurationResponseDataSpec.
        :type rds_db_name: str
        """
        self._rds_db_name = rds_db_name

    @property
    def rds_address(self):
        r"""Gets the rds_address of this ConfigurationResponseDataSpec.

        RDS数据库地址。  Configuration.type为\"rds\"时，返回此参数。 

        :return: The rds_address of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._rds_address

    @rds_address.setter
    def rds_address(self, rds_address):
        r"""Sets the rds_address of this ConfigurationResponseDataSpec.

        RDS数据库地址。  Configuration.type为\"rds\"时，返回此参数。 

        :param rds_address: The rds_address of this ConfigurationResponseDataSpec.
        :type rds_address: str
        """
        self._rds_address = rds_address

    @property
    def rds_username(self):
        r"""Gets the rds_username of this ConfigurationResponseDataSpec.

        RDS数据库用户名称。  Configuration.type为\"rds\"时，返回此参数。 

        :return: The rds_username of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._rds_username

    @rds_username.setter
    def rds_username(self, rds_username):
        r"""Sets the rds_username of this ConfigurationResponseDataSpec.

        RDS数据库用户名称。  Configuration.type为\"rds\"时，返回此参数。 

        :param rds_username: The rds_username of this ConfigurationResponseDataSpec.
        :type rds_username: str
        """
        self._rds_username = rds_username

    @property
    def rds_password(self):
        r"""Gets the rds_password of this ConfigurationResponseDataSpec.

        RDS数据库密码。  Configuration.type为\"rds\"时，返回此参数。 

        :return: The rds_password of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._rds_password

    @rds_password.setter
    def rds_password(self, rds_password):
        r"""Sets the rds_password of this ConfigurationResponseDataSpec.

        RDS数据库密码。  Configuration.type为\"rds\"时，返回此参数。 

        :param rds_password: The rds_password of this ConfigurationResponseDataSpec.
        :type rds_password: str
        """
        self._rds_password = rds_password

    @property
    def rds_port(self):
        r"""Gets the rds_port of this ConfigurationResponseDataSpec.

        RDS数据库端口。  Configuration.type为\"rds\"时，返回此参数。 

        :return: The rds_port of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._rds_port

    @rds_port.setter
    def rds_port(self, rds_port):
        r"""Sets the rds_port of this ConfigurationResponseDataSpec.

        RDS数据库端口。  Configuration.type为\"rds\"时，返回此参数。 

        :param rds_port: The rds_port of this ConfigurationResponseDataSpec.
        :type rds_port: str
        """
        self._rds_port = rds_port

    @property
    def config_center_addr(self):
        r"""Gets the config_center_addr of this ConfigurationResponseDataSpec.

        CSE配置中心地址。  Configuration.type为\"cse\"时，返回此参数。 

        :return: The config_center_addr of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._config_center_addr

    @config_center_addr.setter
    def config_center_addr(self, config_center_addr):
        r"""Sets the config_center_addr of this ConfigurationResponseDataSpec.

        CSE配置中心地址。  Configuration.type为\"cse\"时，返回此参数。 

        :param config_center_addr: The config_center_addr of this ConfigurationResponseDataSpec.
        :type config_center_addr: str
        """
        self._config_center_addr = config_center_addr

    @property
    def service_center_addr(self):
        r"""Gets the service_center_addr of this ConfigurationResponseDataSpec.

        CSE服务注册发现地址。  Configuration.type为\"cse\"时，返回此参数。 

        :return: The service_center_addr of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._service_center_addr

    @service_center_addr.setter
    def service_center_addr(self, service_center_addr):
        r"""Sets the service_center_addr of this ConfigurationResponseDataSpec.

        CSE服务注册发现地址。  Configuration.type为\"cse\"时，返回此参数。 

        :param service_center_addr: The service_center_addr of this ConfigurationResponseDataSpec.
        :type service_center_addr: str
        """
        self._service_center_addr = service_center_addr

    @property
    def cse_id(self):
        r"""Gets the cse_id of this ConfigurationResponseDataSpec.

        CSE引擎ID。  Configuration.type为\"cse\"时，返回此参数。 

        :return: The cse_id of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._cse_id

    @cse_id.setter
    def cse_id(self, cse_id):
        r"""Sets the cse_id of this ConfigurationResponseDataSpec.

        CSE引擎ID。  Configuration.type为\"cse\"时，返回此参数。 

        :param cse_id: The cse_id of this ConfigurationResponseDataSpec.
        :type cse_id: str
        """
        self._cse_id = cse_id

    @property
    def envs(self):
        r"""Gets the envs of this ConfigurationResponseDataSpec.

        环境变量配置。 常用环境变量如下： - TZ: 时区设置，东八区可设置为Asia/Shanghai。 - LANG: 语言字符集设置，中文UTF8可设置为zh_CN.UTF-8。

        :return: The envs of this ConfigurationResponseDataSpec.
        :rtype: dict(str, str)
        """
        return self._envs

    @envs.setter
    def envs(self, envs):
        r"""Sets the envs of this ConfigurationResponseDataSpec.

        环境变量配置。 常用环境变量如下： - TZ: 时区设置，东八区可设置为Asia/Shanghai。 - LANG: 语言字符集设置，中文UTF8可设置为zh_CN.UTF-8。

        :param envs: The envs of this ConfigurationResponseDataSpec.
        :type envs: dict(str, str)
        """
        self._envs = envs

    @property
    def ip(self):
        r"""Gets the ip of this ConfigurationResponseDataSpec.

        弹性公网IP，响应体参数，未配置域名时返回此参数。

        :return: The ip of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ConfigurationResponseDataSpec.

        弹性公网IP，响应体参数，未配置域名时返回此参数。

        :param ip: The ip of this ConfigurationResponseDataSpec.
        :type ip: str
        """
        self._ip = ip

    @property
    def items(self):
        r"""Gets the items of this ConfigurationResponseDataSpec.

        访问方式配置列表。  Configuration.type为\"access\"时，返回此参数。 

        :return: The items of this ConfigurationResponseDataSpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationDataItems`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ConfigurationResponseDataSpec.

        访问方式配置列表。  Configuration.type为\"access\"时，返回此参数。 

        :param items: The items of this ConfigurationResponseDataSpec.
        :type items: list[:class:`huaweicloudsdkcae.v1.AccessConfigurationDataItems`]
        """
        self._items = items

    @property
    def scale_strategy(self):
        r"""Gets the scale_strategy of this ConfigurationResponseDataSpec.

        伸缩策略配置策略类型。  Configuration.type为\"scaling\"时，返回此参数。 

        :return: The scale_strategy of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._scale_strategy

    @scale_strategy.setter
    def scale_strategy(self, scale_strategy):
        r"""Sets the scale_strategy of this ConfigurationResponseDataSpec.

        伸缩策略配置策略类型。  Configuration.type为\"scaling\"时，返回此参数。 

        :param scale_strategy: The scale_strategy of this ConfigurationResponseDataSpec.
        :type scale_strategy: str
        """
        self._scale_strategy = scale_strategy

    @property
    def max_replica_count(self):
        r"""Gets the max_replica_count of this ConfigurationResponseDataSpec.

        伸缩策略配置最大伸缩个数。  Configuration.type为\"scaling\"时，返回此参数。 

        :return: The max_replica_count of this ConfigurationResponseDataSpec.
        :rtype: int
        """
        return self._max_replica_count

    @max_replica_count.setter
    def max_replica_count(self, max_replica_count):
        r"""Sets the max_replica_count of this ConfigurationResponseDataSpec.

        伸缩策略配置最大伸缩个数。  Configuration.type为\"scaling\"时，返回此参数。 

        :param max_replica_count: The max_replica_count of this ConfigurationResponseDataSpec.
        :type max_replica_count: int
        """
        self._max_replica_count = max_replica_count

    @property
    def min_replica_count(self):
        r"""Gets the min_replica_count of this ConfigurationResponseDataSpec.

        伸缩策略配置最小伸缩个数。  Configuration.type为\"scaling\"时，返回此参数。 

        :return: The min_replica_count of this ConfigurationResponseDataSpec.
        :rtype: int
        """
        return self._min_replica_count

    @min_replica_count.setter
    def min_replica_count(self, min_replica_count):
        r"""Sets the min_replica_count of this ConfigurationResponseDataSpec.

        伸缩策略配置最小伸缩个数。  Configuration.type为\"scaling\"时，返回此参数。 

        :param min_replica_count: The min_replica_count of this ConfigurationResponseDataSpec.
        :type min_replica_count: int
        """
        self._min_replica_count = min_replica_count

    @property
    def advanced(self):
        r"""Gets the advanced of this ConfigurationResponseDataSpec.

        :return: The advanced of this ConfigurationResponseDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.ScaleConfigurationDataAdvanced`
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        r"""Sets the advanced of this ConfigurationResponseDataSpec.

        :param advanced: The advanced of this ConfigurationResponseDataSpec.
        :type advanced: :class:`huaweicloudsdkcae.v1.ScaleConfigurationDataAdvanced`
        """
        self._advanced = advanced

    @property
    def triggers(self):
        r"""Gets the triggers of this ConfigurationResponseDataSpec.

        伸缩策略配置触发器列表。  Configuration.type为\"scaling\"时，返回此参数。 

        :return: The triggers of this ConfigurationResponseDataSpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ScaleConfigurationDataTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this ConfigurationResponseDataSpec.

        伸缩策略配置触发器列表。  Configuration.type为\"scaling\"时，返回此参数。 

        :param triggers: The triggers of this ConfigurationResponseDataSpec.
        :type triggers: list[:class:`huaweicloudsdkcae.v1.ScaleConfigurationDataTrigger`]
        """
        self._triggers = triggers

    @property
    def volumes(self):
        r"""Gets the volumes of this ConfigurationResponseDataSpec.

        云存储配置列表。  Configuration.type为\"volume\"时，返回此参数。 

        :return: The volumes of this ConfigurationResponseDataSpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.VolumeConfigurationDataVolume`]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        r"""Sets the volumes of this ConfigurationResponseDataSpec.

        云存储配置列表。  Configuration.type为\"volume\"时，返回此参数。 

        :param volumes: The volumes of this ConfigurationResponseDataSpec.
        :type volumes: list[:class:`huaweicloudsdkcae.v1.VolumeConfigurationDataVolume`]
        """
        self._volumes = volumes

    @property
    def liveness_probe(self):
        r"""Gets the liveness_probe of this ConfigurationResponseDataSpec.

        :return: The liveness_probe of this ConfigurationResponseDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationLivenessProbe`
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        r"""Sets the liveness_probe of this ConfigurationResponseDataSpec.

        :param liveness_probe: The liveness_probe of this ConfigurationResponseDataSpec.
        :type liveness_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationLivenessProbe`
        """
        self._liveness_probe = liveness_probe

    @property
    def startup_probe(self):
        r"""Gets the startup_probe of this ConfigurationResponseDataSpec.

        :return: The startup_probe of this ConfigurationResponseDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationStartupProbe`
        """
        return self._startup_probe

    @startup_probe.setter
    def startup_probe(self, startup_probe):
        r"""Sets the startup_probe of this ConfigurationResponseDataSpec.

        :param startup_probe: The startup_probe of this ConfigurationResponseDataSpec.
        :type startup_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationStartupProbe`
        """
        self._startup_probe = startup_probe

    @property
    def readiness_probe(self):
        r"""Gets the readiness_probe of this ConfigurationResponseDataSpec.

        :return: The readiness_probe of this ConfigurationResponseDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationReadinessProbe`
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        r"""Sets the readiness_probe of this ConfigurationResponseDataSpec.

        :param readiness_probe: The readiness_probe of this ConfigurationResponseDataSpec.
        :type readiness_probe: :class:`huaweicloudsdkcae.v1.HealthCheckConfigurationReadinessProbe`
        """
        self._readiness_probe = readiness_probe

    @property
    def post_start(self):
        r"""Gets the post_start of this ConfigurationResponseDataSpec.

        :return: The post_start of this ConfigurationResponseDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.ConfigurationResponseDataSpecPostStart`
        """
        return self._post_start

    @post_start.setter
    def post_start(self, post_start):
        r"""Sets the post_start of this ConfigurationResponseDataSpec.

        :param post_start: The post_start of this ConfigurationResponseDataSpec.
        :type post_start: :class:`huaweicloudsdkcae.v1.ConfigurationResponseDataSpecPostStart`
        """
        self._post_start = post_start

    @property
    def pre_stop(self):
        r"""Gets the pre_stop of this ConfigurationResponseDataSpec.

        :return: The pre_stop of this ConfigurationResponseDataSpec.
        :rtype: :class:`huaweicloudsdkcae.v1.ConfigurationResponseDataSpecPreStop`
        """
        return self._pre_stop

    @pre_stop.setter
    def pre_stop(self, pre_stop):
        r"""Sets the pre_stop of this ConfigurationResponseDataSpec.

        :param pre_stop: The pre_stop of this ConfigurationResponseDataSpec.
        :type pre_stop: :class:`huaweicloudsdkcae.v1.ConfigurationResponseDataSpecPreStop`
        """
        self._pre_stop = pre_stop

    @property
    def log_paths(self):
        r"""Gets the log_paths of this ConfigurationResponseDataSpec.

        自定义本地磁盘日志路径数组。  Configuration.type为\"log\"时，返回此参数。 

        :return: The log_paths of this ConfigurationResponseDataSpec.
        :rtype: list[str]
        """
        return self._log_paths

    @log_paths.setter
    def log_paths(self, log_paths):
        r"""Sets the log_paths of this ConfigurationResponseDataSpec.

        自定义本地磁盘日志路径数组。  Configuration.type为\"log\"时，返回此参数。 

        :param log_paths: The log_paths of this ConfigurationResponseDataSpec.
        :type log_paths: list[str]
        """
        self._log_paths = log_paths

    @property
    def cloud_storage_log_paths(self):
        r"""Gets the cloud_storage_log_paths of this ConfigurationResponseDataSpec.

        自定义云存储日志路径数组。  Configuration.type为\"log\"时，返回此参数。 

        :return: The cloud_storage_log_paths of this ConfigurationResponseDataSpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.CloudStorageLogPathInfo`]
        """
        return self._cloud_storage_log_paths

    @cloud_storage_log_paths.setter
    def cloud_storage_log_paths(self, cloud_storage_log_paths):
        r"""Sets the cloud_storage_log_paths of this ConfigurationResponseDataSpec.

        自定义云存储日志路径数组。  Configuration.type为\"log\"时，返回此参数。 

        :param cloud_storage_log_paths: The cloud_storage_log_paths of this ConfigurationResponseDataSpec.
        :type cloud_storage_log_paths: list[:class:`huaweicloudsdkcae.v1.CloudStorageLogPathInfo`]
        """
        self._cloud_storage_log_paths = cloud_storage_log_paths

    @property
    def instrumentation(self):
        r"""Gets the instrumentation of this ConfigurationResponseDataSpec.

        探针注入方式。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The instrumentation of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._instrumentation

    @instrumentation.setter
    def instrumentation(self, instrumentation):
        r"""Sets the instrumentation of this ConfigurationResponseDataSpec.

        探针注入方式。  Configuration.type为\"apm2\"时，返回此参数。 

        :param instrumentation: The instrumentation of this ConfigurationResponseDataSpec.
        :type instrumentation: str
        """
        self._instrumentation = instrumentation

    @property
    def apm_application(self):
        r"""Gets the apm_application of this ConfigurationResponseDataSpec.

        apm2应用。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The apm_application of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._apm_application

    @apm_application.setter
    def apm_application(self, apm_application):
        r"""Sets the apm_application of this ConfigurationResponseDataSpec.

        apm2应用。  Configuration.type为\"apm2\"时，返回此参数。 

        :param apm_application: The apm_application of this ConfigurationResponseDataSpec.
        :type apm_application: str
        """
        self._apm_application = apm_application

    @property
    def type(self):
        r"""Gets the type of this ConfigurationResponseDataSpec.

        监控系统类别，包括apm2和opentelemetry。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The type of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConfigurationResponseDataSpec.

        监控系统类别，包括apm2和opentelemetry。  Configuration.type为\"apm2\"时，返回此参数。 

        :param type: The type of this ConfigurationResponseDataSpec.
        :type type: str
        """
        self._type = type

    @property
    def app_name(self):
        r"""Gets the app_name of this ConfigurationResponseDataSpec.

        apm2组件。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The app_name of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ConfigurationResponseDataSpec.

        apm2组件。  Configuration.type为\"apm2\"时，返回此参数。 

        :param app_name: The app_name of this ConfigurationResponseDataSpec.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ConfigurationResponseDataSpec.

        apm2实例。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The instance_name of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ConfigurationResponseDataSpec.

        apm2实例。  Configuration.type为\"apm2\"时，返回此参数。 

        :param instance_name: The instance_name of this ConfigurationResponseDataSpec.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def env_name(self):
        r"""Gets the env_name of this ConfigurationResponseDataSpec.

        apm2环境。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The env_name of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        r"""Sets the env_name of this ConfigurationResponseDataSpec.

        apm2环境。  Configuration.type为\"apm2\"时，返回此参数。 

        :param env_name: The env_name of this ConfigurationResponseDataSpec.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def image_pull_policy(self):
        r"""Gets the image_pull_policy of this ConfigurationResponseDataSpec.

        探针镜像更新策略，已废弃，迁移到监控系统。  - Always，重启自动升级：每次都尝试重新下载镜像。 - IfNotPresent，手动升级: 如果本地有该镜像，则继续使用本地镜像，不下载镜像。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The image_pull_policy of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        r"""Sets the image_pull_policy of this ConfigurationResponseDataSpec.

        探针镜像更新策略，已废弃，迁移到监控系统。  - Always，重启自动升级：每次都尝试重新下载镜像。 - IfNotPresent，手动升级: 如果本地有该镜像，则继续使用本地镜像，不下载镜像。  Configuration.type为\"apm2\"时，返回此参数。 

        :param image_pull_policy: The image_pull_policy of this ConfigurationResponseDataSpec.
        :type image_pull_policy: str
        """
        self._image_pull_policy = image_pull_policy

    @property
    def version(self):
        r"""Gets the version of this ConfigurationResponseDataSpec.

        增强型探针/opentelemetry探针版本，已废弃，迁移到监控系统。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The version of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ConfigurationResponseDataSpec.

        增强型探针/opentelemetry探针版本，已废弃，迁移到监控系统。  Configuration.type为\"apm2\"时，返回此参数。 

        :param version: The version of this ConfigurationResponseDataSpec.
        :type version: str
        """
        self._version = version

    @property
    def access_key(self):
        r"""Gets the access_key of this ConfigurationResponseDataSpec.

        apm2访问密钥Key，已废弃，迁移到监控系统。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The access_key of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this ConfigurationResponseDataSpec.

        apm2访问密钥Key，已废弃，迁移到监控系统。  Configuration.type为\"apm2\"时，返回此参数。 

        :param access_key: The access_key of this ConfigurationResponseDataSpec.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def access_value(self):
        r"""Gets the access_value of this ConfigurationResponseDataSpec.

        apm2访问密钥value，已废弃，迁移到监控系统。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The access_value of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._access_value

    @access_value.setter
    def access_value(self, access_value):
        r"""Sets the access_value of this ConfigurationResponseDataSpec.

        apm2访问密钥value，已废弃，迁移到监控系统。  Configuration.type为\"apm2\"时，返回此参数。 

        :param access_value: The access_value of this ConfigurationResponseDataSpec.
        :type access_value: str
        """
        self._access_value = access_value

    @property
    def business(self):
        r"""Gets the business of this ConfigurationResponseDataSpec.

        apm2应用，同apm_application，已废弃。  Configuration.type为\"apm2\"时，返回此参数。 

        :return: The business of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._business

    @business.setter
    def business(self, business):
        r"""Sets the business of this ConfigurationResponseDataSpec.

        apm2应用，同apm_application，已废弃。  Configuration.type为\"apm2\"时，返回此参数。 

        :param business: The business of this ConfigurationResponseDataSpec.
        :type business: str
        """
        self._business = business

    @property
    def path(self):
        r"""Gets the path of this ConfigurationResponseDataSpec.

        自定义监控指标配置采集路径。  Configuration.type为\"customMetric\"时，返回此参数。 

        :return: The path of this ConfigurationResponseDataSpec.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ConfigurationResponseDataSpec.

        自定义监控指标配置采集路径。  Configuration.type为\"customMetric\"时，返回此参数。 

        :param path: The path of this ConfigurationResponseDataSpec.
        :type path: str
        """
        self._path = path

    @property
    def port(self):
        r"""Gets the port of this ConfigurationResponseDataSpec.

        自定义监控指标配置采集端口。  Configuration.type为\"customMetric\"时，返回此参数。 

        :return: The port of this ConfigurationResponseDataSpec.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ConfigurationResponseDataSpec.

        自定义监控指标配置采集端口。  Configuration.type为\"customMetric\"时，返回此参数。 

        :param port: The port of this ConfigurationResponseDataSpec.
        :type port: int
        """
        self._port = port

    @property
    def metrics(self):
        r"""Gets the metrics of this ConfigurationResponseDataSpec.

        自定义监控指标配置指标名称。  Configuration.type为\"customMetric\"时，返回此参数。 

        :return: The metrics of this ConfigurationResponseDataSpec.
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this ConfigurationResponseDataSpec.

        自定义监控指标配置指标名称。  Configuration.type为\"customMetric\"时，返回此参数。 

        :param metrics: The metrics of this ConfigurationResponseDataSpec.
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
        if not isinstance(other, ConfigurationResponseDataSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
