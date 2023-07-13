# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeNodeCreation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_node_id': 'str',
        'name': 'str',
        'type': 'str',
        'verify_code': 'str',
        'time_out': 'int',
        'arch': 'str',
        'os_type': 'str',
        'instance_id': 'str',
        'space_id': 'str',
        'resource_ids': 'list[str]',
        'security_level': 'str',
        'reliability_level': 'str',
        'storage_period': 'int',
        'ai_card_type': 'str',
        'npu_library_path': 'str',
        'base_path': 'BasePathDTO',
        'log_configs': 'list[LogConfigDTO]',
        'apps': 'list[EdgeAppInstanceDTO]',
        'network_access_point': 'str',
        'hardware_model': 'str',
        'offline_cache_configs': 'OfflineCacheConfigsDTO',
        'device_auth_info': 'DeviceAuthInfoDTO',
        'device_data_format': 'str',
        'automatic_upgrade': 'str',
        'device_data_record': 'DeviceDataRecord',
        'metric_report': 'str'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'name': 'name',
        'type': 'type',
        'verify_code': 'verify_code',
        'time_out': 'time_out',
        'arch': 'arch',
        'os_type': 'os_type',
        'instance_id': 'instance_id',
        'space_id': 'space_id',
        'resource_ids': 'resource_ids',
        'security_level': 'security_level',
        'reliability_level': 'reliability_level',
        'storage_period': 'storage_period',
        'ai_card_type': 'ai_card_type',
        'npu_library_path': 'npu_library_path',
        'base_path': 'base_path',
        'log_configs': 'log_configs',
        'apps': 'apps',
        'network_access_point': 'network_access_point',
        'hardware_model': 'hardware_model',
        'offline_cache_configs': 'offline_cache_configs',
        'device_auth_info': 'device_auth_info',
        'device_data_format': 'device_data_format',
        'automatic_upgrade': 'automatic_upgrade',
        'device_data_record': 'device_data_record',
        'metric_report': 'metric_report'
    }

    def __init__(self, edge_node_id=None, name=None, type=None, verify_code=None, time_out=None, arch=None, os_type=None, instance_id=None, space_id=None, resource_ids=None, security_level=None, reliability_level=None, storage_period=None, ai_card_type=None, npu_library_path=None, base_path=None, log_configs=None, apps=None, network_access_point=None, hardware_model=None, offline_cache_configs=None, device_auth_info=None, device_data_format=None, automatic_upgrade=None, device_data_record=None, metric_report=None):
        """EdgeNodeCreation

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param name: 边缘节点名称，只允许中、数字、英文大小写、中划线、下划线
        :type name: str
        :param type: 节点所属资源类型：advanced|standard
        :type type: str
        :param verify_code: 边缘节点注册使用的验证码，如果不输入则平台随机生成。
        :type verify_code: str
        :param time_out: 验证码的有效时间单位秒，默认1800秒，范围为1~864000，过期后平台会随机生成。
        :type time_out: int
        :param arch: 系统架构。包括：arm64，arm32，x86_64。
        :type arch: str
        :param os_type: 系统类型。包括：generalLinux通用系统，openHarmony。
        :type os_type: str
        :param instance_id: 实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param space_id: 资源空间id，对应IOTDA云服务接口参数中的app_id。
        :type space_id: str
        :param resource_ids: 资源id列表，创建节点时需绑定已购买的资源包，资源可叠加。
        :type resource_ids: list[str]
        :param security_level: 节点的安全等级，MEDIUM表示本地明文存储，HIGH表示本地加密存储。
        :type security_level: str
        :param reliability_level: 节点的可靠性等级。
        :type reliability_level: str
        :param storage_period: 节点的存储周期，默认0天，取值范围0~7天，0天则不存储。
        :type storage_period: int
        :param ai_card_type: AI加速卡类型，如华为昇腾AI加速卡NPU、图像处理加速卡GPU。
        :type ai_card_type: str
        :param npu_library_path: npu驱动动态库路径
        :type npu_library_path: str
        :param base_path: 
        :type base_path: :class:`huaweicloudsdkiotedge.v2.BasePathDTO`
        :param log_configs: 边缘节点在IEF日志配置参数，仅高级版支持。
        :type log_configs: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        :param apps: 用户预置第三方边缘应用
        :type apps: list[:class:`huaweicloudsdkiotedge.v2.EdgeAppInstanceDTO`]
        :param network_access_point: 网络接入方式类型
        :type network_access_point: str
        :param hardware_model: 网关型号
        :type hardware_model: str
        :param offline_cache_configs: 
        :type offline_cache_configs: :class:`huaweicloudsdkiotedge.v2.OfflineCacheConfigsDTO`
        :param device_auth_info: 
        :type device_auth_info: :class:`huaweicloudsdkiotedge.v2.DeviceAuthInfoDTO`
        :param device_data_format: 节点使用的数据格式，默认为iotda物模型1.0格式，可以选择属性平铺数据格式flat_json
        :type device_data_format: str
        :param automatic_upgrade: 自动升级系统应用的节点开关，默认为关闭：OFF，IMMEDIATE表示节点开关打开
        :type automatic_upgrade: str
        :param device_data_record: 
        :type device_data_record: :class:`huaweicloudsdkiotedge.v2.DeviceDataRecord`
        :param metric_report: omagent监控运维工具是否上报指标
        :type metric_report: str
        """
        
        

        self._edge_node_id = None
        self._name = None
        self._type = None
        self._verify_code = None
        self._time_out = None
        self._arch = None
        self._os_type = None
        self._instance_id = None
        self._space_id = None
        self._resource_ids = None
        self._security_level = None
        self._reliability_level = None
        self._storage_period = None
        self._ai_card_type = None
        self._npu_library_path = None
        self._base_path = None
        self._log_configs = None
        self._apps = None
        self._network_access_point = None
        self._hardware_model = None
        self._offline_cache_configs = None
        self._device_auth_info = None
        self._device_data_format = None
        self._automatic_upgrade = None
        self._device_data_record = None
        self._metric_report = None
        self.discriminator = None

        if edge_node_id is not None:
            self.edge_node_id = edge_node_id
        self.name = name
        self.type = type
        if verify_code is not None:
            self.verify_code = verify_code
        if time_out is not None:
            self.time_out = time_out
        if arch is not None:
            self.arch = arch
        if os_type is not None:
            self.os_type = os_type
        if instance_id is not None:
            self.instance_id = instance_id
        if space_id is not None:
            self.space_id = space_id
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if security_level is not None:
            self.security_level = security_level
        if reliability_level is not None:
            self.reliability_level = reliability_level
        if storage_period is not None:
            self.storage_period = storage_period
        if ai_card_type is not None:
            self.ai_card_type = ai_card_type
        if npu_library_path is not None:
            self.npu_library_path = npu_library_path
        if base_path is not None:
            self.base_path = base_path
        if log_configs is not None:
            self.log_configs = log_configs
        if apps is not None:
            self.apps = apps
        if network_access_point is not None:
            self.network_access_point = network_access_point
        if hardware_model is not None:
            self.hardware_model = hardware_model
        if offline_cache_configs is not None:
            self.offline_cache_configs = offline_cache_configs
        if device_auth_info is not None:
            self.device_auth_info = device_auth_info
        if device_data_format is not None:
            self.device_data_format = device_data_format
        if automatic_upgrade is not None:
            self.automatic_upgrade = automatic_upgrade
        if device_data_record is not None:
            self.device_data_record = device_data_record
        if metric_report is not None:
            self.metric_report = metric_report

    @property
    def edge_node_id(self):
        """Gets the edge_node_id of this EdgeNodeCreation.

        边缘节点ID

        :return: The edge_node_id of this EdgeNodeCreation.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        """Sets the edge_node_id of this EdgeNodeCreation.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this EdgeNodeCreation.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def name(self):
        """Gets the name of this EdgeNodeCreation.

        边缘节点名称，只允许中、数字、英文大小写、中划线、下划线

        :return: The name of this EdgeNodeCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EdgeNodeCreation.

        边缘节点名称，只允许中、数字、英文大小写、中划线、下划线

        :param name: The name of this EdgeNodeCreation.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this EdgeNodeCreation.

        节点所属资源类型：advanced|standard

        :return: The type of this EdgeNodeCreation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EdgeNodeCreation.

        节点所属资源类型：advanced|standard

        :param type: The type of this EdgeNodeCreation.
        :type type: str
        """
        self._type = type

    @property
    def verify_code(self):
        """Gets the verify_code of this EdgeNodeCreation.

        边缘节点注册使用的验证码，如果不输入则平台随机生成。

        :return: The verify_code of this EdgeNodeCreation.
        :rtype: str
        """
        return self._verify_code

    @verify_code.setter
    def verify_code(self, verify_code):
        """Sets the verify_code of this EdgeNodeCreation.

        边缘节点注册使用的验证码，如果不输入则平台随机生成。

        :param verify_code: The verify_code of this EdgeNodeCreation.
        :type verify_code: str
        """
        self._verify_code = verify_code

    @property
    def time_out(self):
        """Gets the time_out of this EdgeNodeCreation.

        验证码的有效时间单位秒，默认1800秒，范围为1~864000，过期后平台会随机生成。

        :return: The time_out of this EdgeNodeCreation.
        :rtype: int
        """
        return self._time_out

    @time_out.setter
    def time_out(self, time_out):
        """Sets the time_out of this EdgeNodeCreation.

        验证码的有效时间单位秒，默认1800秒，范围为1~864000，过期后平台会随机生成。

        :param time_out: The time_out of this EdgeNodeCreation.
        :type time_out: int
        """
        self._time_out = time_out

    @property
    def arch(self):
        """Gets the arch of this EdgeNodeCreation.

        系统架构。包括：arm64，arm32，x86_64。

        :return: The arch of this EdgeNodeCreation.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this EdgeNodeCreation.

        系统架构。包括：arm64，arm32，x86_64。

        :param arch: The arch of this EdgeNodeCreation.
        :type arch: str
        """
        self._arch = arch

    @property
    def os_type(self):
        """Gets the os_type of this EdgeNodeCreation.

        系统类型。包括：generalLinux通用系统，openHarmony。

        :return: The os_type of this EdgeNodeCreation.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this EdgeNodeCreation.

        系统类型。包括：generalLinux通用系统，openHarmony。

        :param os_type: The os_type of this EdgeNodeCreation.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def instance_id(self):
        """Gets the instance_id of this EdgeNodeCreation.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this EdgeNodeCreation.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this EdgeNodeCreation.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this EdgeNodeCreation.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def space_id(self):
        """Gets the space_id of this EdgeNodeCreation.

        资源空间id，对应IOTDA云服务接口参数中的app_id。

        :return: The space_id of this EdgeNodeCreation.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this EdgeNodeCreation.

        资源空间id，对应IOTDA云服务接口参数中的app_id。

        :param space_id: The space_id of this EdgeNodeCreation.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def resource_ids(self):
        """Gets the resource_ids of this EdgeNodeCreation.

        资源id列表，创建节点时需绑定已购买的资源包，资源可叠加。

        :return: The resource_ids of this EdgeNodeCreation.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this EdgeNodeCreation.

        资源id列表，创建节点时需绑定已购买的资源包，资源可叠加。

        :param resource_ids: The resource_ids of this EdgeNodeCreation.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def security_level(self):
        """Gets the security_level of this EdgeNodeCreation.

        节点的安全等级，MEDIUM表示本地明文存储，HIGH表示本地加密存储。

        :return: The security_level of this EdgeNodeCreation.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this EdgeNodeCreation.

        节点的安全等级，MEDIUM表示本地明文存储，HIGH表示本地加密存储。

        :param security_level: The security_level of this EdgeNodeCreation.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def reliability_level(self):
        """Gets the reliability_level of this EdgeNodeCreation.

        节点的可靠性等级。

        :return: The reliability_level of this EdgeNodeCreation.
        :rtype: str
        """
        return self._reliability_level

    @reliability_level.setter
    def reliability_level(self, reliability_level):
        """Sets the reliability_level of this EdgeNodeCreation.

        节点的可靠性等级。

        :param reliability_level: The reliability_level of this EdgeNodeCreation.
        :type reliability_level: str
        """
        self._reliability_level = reliability_level

    @property
    def storage_period(self):
        """Gets the storage_period of this EdgeNodeCreation.

        节点的存储周期，默认0天，取值范围0~7天，0天则不存储。

        :return: The storage_period of this EdgeNodeCreation.
        :rtype: int
        """
        return self._storage_period

    @storage_period.setter
    def storage_period(self, storage_period):
        """Sets the storage_period of this EdgeNodeCreation.

        节点的存储周期，默认0天，取值范围0~7天，0天则不存储。

        :param storage_period: The storage_period of this EdgeNodeCreation.
        :type storage_period: int
        """
        self._storage_period = storage_period

    @property
    def ai_card_type(self):
        """Gets the ai_card_type of this EdgeNodeCreation.

        AI加速卡类型，如华为昇腾AI加速卡NPU、图像处理加速卡GPU。

        :return: The ai_card_type of this EdgeNodeCreation.
        :rtype: str
        """
        return self._ai_card_type

    @ai_card_type.setter
    def ai_card_type(self, ai_card_type):
        """Sets the ai_card_type of this EdgeNodeCreation.

        AI加速卡类型，如华为昇腾AI加速卡NPU、图像处理加速卡GPU。

        :param ai_card_type: The ai_card_type of this EdgeNodeCreation.
        :type ai_card_type: str
        """
        self._ai_card_type = ai_card_type

    @property
    def npu_library_path(self):
        """Gets the npu_library_path of this EdgeNodeCreation.

        npu驱动动态库路径

        :return: The npu_library_path of this EdgeNodeCreation.
        :rtype: str
        """
        return self._npu_library_path

    @npu_library_path.setter
    def npu_library_path(self, npu_library_path):
        """Sets the npu_library_path of this EdgeNodeCreation.

        npu驱动动态库路径

        :param npu_library_path: The npu_library_path of this EdgeNodeCreation.
        :type npu_library_path: str
        """
        self._npu_library_path = npu_library_path

    @property
    def base_path(self):
        """Gets the base_path of this EdgeNodeCreation.

        :return: The base_path of this EdgeNodeCreation.
        :rtype: :class:`huaweicloudsdkiotedge.v2.BasePathDTO`
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this EdgeNodeCreation.

        :param base_path: The base_path of this EdgeNodeCreation.
        :type base_path: :class:`huaweicloudsdkiotedge.v2.BasePathDTO`
        """
        self._base_path = base_path

    @property
    def log_configs(self):
        """Gets the log_configs of this EdgeNodeCreation.

        边缘节点在IEF日志配置参数，仅高级版支持。

        :return: The log_configs of this EdgeNodeCreation.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        """Sets the log_configs of this EdgeNodeCreation.

        边缘节点在IEF日志配置参数，仅高级版支持。

        :param log_configs: The log_configs of this EdgeNodeCreation.
        :type log_configs: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        """
        self._log_configs = log_configs

    @property
    def apps(self):
        """Gets the apps of this EdgeNodeCreation.

        用户预置第三方边缘应用

        :return: The apps of this EdgeNodeCreation.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.EdgeAppInstanceDTO`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this EdgeNodeCreation.

        用户预置第三方边缘应用

        :param apps: The apps of this EdgeNodeCreation.
        :type apps: list[:class:`huaweicloudsdkiotedge.v2.EdgeAppInstanceDTO`]
        """
        self._apps = apps

    @property
    def network_access_point(self):
        """Gets the network_access_point of this EdgeNodeCreation.

        网络接入方式类型

        :return: The network_access_point of this EdgeNodeCreation.
        :rtype: str
        """
        return self._network_access_point

    @network_access_point.setter
    def network_access_point(self, network_access_point):
        """Sets the network_access_point of this EdgeNodeCreation.

        网络接入方式类型

        :param network_access_point: The network_access_point of this EdgeNodeCreation.
        :type network_access_point: str
        """
        self._network_access_point = network_access_point

    @property
    def hardware_model(self):
        """Gets the hardware_model of this EdgeNodeCreation.

        网关型号

        :return: The hardware_model of this EdgeNodeCreation.
        :rtype: str
        """
        return self._hardware_model

    @hardware_model.setter
    def hardware_model(self, hardware_model):
        """Sets the hardware_model of this EdgeNodeCreation.

        网关型号

        :param hardware_model: The hardware_model of this EdgeNodeCreation.
        :type hardware_model: str
        """
        self._hardware_model = hardware_model

    @property
    def offline_cache_configs(self):
        """Gets the offline_cache_configs of this EdgeNodeCreation.

        :return: The offline_cache_configs of this EdgeNodeCreation.
        :rtype: :class:`huaweicloudsdkiotedge.v2.OfflineCacheConfigsDTO`
        """
        return self._offline_cache_configs

    @offline_cache_configs.setter
    def offline_cache_configs(self, offline_cache_configs):
        """Sets the offline_cache_configs of this EdgeNodeCreation.

        :param offline_cache_configs: The offline_cache_configs of this EdgeNodeCreation.
        :type offline_cache_configs: :class:`huaweicloudsdkiotedge.v2.OfflineCacheConfigsDTO`
        """
        self._offline_cache_configs = offline_cache_configs

    @property
    def device_auth_info(self):
        """Gets the device_auth_info of this EdgeNodeCreation.

        :return: The device_auth_info of this EdgeNodeCreation.
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeviceAuthInfoDTO`
        """
        return self._device_auth_info

    @device_auth_info.setter
    def device_auth_info(self, device_auth_info):
        """Sets the device_auth_info of this EdgeNodeCreation.

        :param device_auth_info: The device_auth_info of this EdgeNodeCreation.
        :type device_auth_info: :class:`huaweicloudsdkiotedge.v2.DeviceAuthInfoDTO`
        """
        self._device_auth_info = device_auth_info

    @property
    def device_data_format(self):
        """Gets the device_data_format of this EdgeNodeCreation.

        节点使用的数据格式，默认为iotda物模型1.0格式，可以选择属性平铺数据格式flat_json

        :return: The device_data_format of this EdgeNodeCreation.
        :rtype: str
        """
        return self._device_data_format

    @device_data_format.setter
    def device_data_format(self, device_data_format):
        """Sets the device_data_format of this EdgeNodeCreation.

        节点使用的数据格式，默认为iotda物模型1.0格式，可以选择属性平铺数据格式flat_json

        :param device_data_format: The device_data_format of this EdgeNodeCreation.
        :type device_data_format: str
        """
        self._device_data_format = device_data_format

    @property
    def automatic_upgrade(self):
        """Gets the automatic_upgrade of this EdgeNodeCreation.

        自动升级系统应用的节点开关，默认为关闭：OFF，IMMEDIATE表示节点开关打开

        :return: The automatic_upgrade of this EdgeNodeCreation.
        :rtype: str
        """
        return self._automatic_upgrade

    @automatic_upgrade.setter
    def automatic_upgrade(self, automatic_upgrade):
        """Sets the automatic_upgrade of this EdgeNodeCreation.

        自动升级系统应用的节点开关，默认为关闭：OFF，IMMEDIATE表示节点开关打开

        :param automatic_upgrade: The automatic_upgrade of this EdgeNodeCreation.
        :type automatic_upgrade: str
        """
        self._automatic_upgrade = automatic_upgrade

    @property
    def device_data_record(self):
        """Gets the device_data_record of this EdgeNodeCreation.

        :return: The device_data_record of this EdgeNodeCreation.
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeviceDataRecord`
        """
        return self._device_data_record

    @device_data_record.setter
    def device_data_record(self, device_data_record):
        """Sets the device_data_record of this EdgeNodeCreation.

        :param device_data_record: The device_data_record of this EdgeNodeCreation.
        :type device_data_record: :class:`huaweicloudsdkiotedge.v2.DeviceDataRecord`
        """
        self._device_data_record = device_data_record

    @property
    def metric_report(self):
        """Gets the metric_report of this EdgeNodeCreation.

        omagent监控运维工具是否上报指标

        :return: The metric_report of this EdgeNodeCreation.
        :rtype: str
        """
        return self._metric_report

    @metric_report.setter
    def metric_report(self, metric_report):
        """Sets the metric_report of this EdgeNodeCreation.

        omagent监控运维工具是否上报指标

        :param metric_report: The metric_report of this EdgeNodeCreation.
        :type metric_report: str
        """
        self._metric_report = metric_report

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
        if not isinstance(other, EdgeNodeCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
