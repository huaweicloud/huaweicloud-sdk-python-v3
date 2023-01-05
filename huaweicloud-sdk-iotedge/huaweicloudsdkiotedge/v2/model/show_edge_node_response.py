# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEdgeNodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_configs': 'list[LogConfigDTO]',
        'ha_config': 'HaConfigDTO',
        'edge_node_id': 'str',
        'instance_id': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'space_id': 'str',
        'resource_spec_types': 'list[str]',
        'resource_ids': 'list[str]',
        'ips': 'list[str]',
        'name': 'str',
        'state': 'str',
        'software_version': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'os_name': 'str',
        'arch': 'str',
        'host_name': 'str',
        'nics': 'list[Nic]',
        'specification': 'str',
        'ai_card_type': 'str',
        'container_version': 'str',
        'type': 'str',
        'security_level': 'str',
        'reliability_level': 'str',
        'storage_period': 'int',
        'base_path': 'BasePathDTO',
        'hardware_model': 'str',
        'offline_cache_configs': 'OfflineCacheConfigsDTO',
        'device_auth_info': 'DeviceAuthInfoDisplayDTO'
    }

    attribute_map = {
        'log_configs': 'log_configs',
        'ha_config': 'ha_config',
        'edge_node_id': 'edge_node_id',
        'instance_id': 'instance_id',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'space_id': 'space_id',
        'resource_spec_types': 'resource_spec_types',
        'resource_ids': 'resource_ids',
        'ips': 'ips',
        'name': 'name',
        'state': 'state',
        'software_version': 'software_version',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'os_name': 'os_name',
        'arch': 'arch',
        'host_name': 'host_name',
        'nics': 'nics',
        'specification': 'specification',
        'ai_card_type': 'ai_card_type',
        'container_version': 'container_version',
        'type': 'type',
        'security_level': 'security_level',
        'reliability_level': 'reliability_level',
        'storage_period': 'storage_period',
        'base_path': 'base_path',
        'hardware_model': 'hardware_model',
        'offline_cache_configs': 'offline_cache_configs',
        'device_auth_info': 'device_auth_info'
    }

    def __init__(self, log_configs=None, ha_config=None, edge_node_id=None, instance_id=None, product_id=None, product_name=None, space_id=None, resource_spec_types=None, resource_ids=None, ips=None, name=None, state=None, software_version=None, create_time=None, update_time=None, os_name=None, arch=None, host_name=None, nics=None, specification=None, ai_card_type=None, container_version=None, type=None, security_level=None, reliability_level=None, storage_period=None, base_path=None, hardware_model=None, offline_cache_configs=None, device_auth_info=None):
        """ShowEdgeNodeResponse

        The model defined in huaweicloud sdk

        :param log_configs: 边缘节点在IEF的日志配置
        :type log_configs: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        :param ha_config: 
        :type ha_config: :class:`huaweicloudsdkiotedge.v2.HaConfigDTO`
        :param edge_node_id: 边缘节点Id
        :type edge_node_id: str
        :param instance_id: 实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param product_id: 边缘节点关联的产品ID，用于唯一标识一个产品模型。
        :type product_id: str
        :param product_name: 边缘节点关联的产品名称。
        :type product_name: str
        :param space_id: 资源空间id，对应IOTDA云服务接口参数中的app_id。
        :type space_id: str
        :param resource_spec_types: 节点所购买的资源类型的列表
        :type resource_spec_types: list[str]
        :param resource_ids: 资源id列表，创建节点时需绑定已购买的资源包，可以叠加节点功能。
        :type resource_ids: list[str]
        :param ips: 边缘节点主机ip
        :type ips: list[str]
        :param name: 边缘节点名称
        :type name: str
        :param state: 边缘节点状态
        :type state: str
        :param software_version: 边缘应用id，只允许数字、英文小写、中划线，切必须以字母或数字结尾
        :type software_version: str
        :param create_time: 边缘节点创建时间
        :type create_time: str
        :param update_time: 边缘节点更新时间
        :type update_time: str
        :param os_name: 边缘节点操作系统名称
        :type os_name: str
        :param arch: 边缘节点操作系统架构
        :type arch: str
        :param host_name: 边缘节点主机名
        :type host_name: str
        :param nics: 边缘节点网络网卡信息
        :type nics: list[:class:`huaweicloudsdkiotedge.v2.Nic`]
        :param specification: 网络规格，如4 cores | 3867 MB
        :type specification: str
        :param ai_card_type: 华为AI加速卡类型，如NPU、GPU、unEquipped
        :type ai_card_type: str
        :param container_version: 容器运行时版本
        :type container_version: str
        :param type: 节点所属资源类型：advanced|standard
        :type type: str
        :param security_level: 节点的安全等级，MEDIUM边缘节数据上报不进行加密，HIGH对数据上报进行加密。
        :type security_level: str
        :param reliability_level: 节点的可靠性等级。
        :type reliability_level: str
        :param storage_period: 节点的存储周期，默认0天，取值范围0~7天，0天则不存储。
        :type storage_period: int
        :param base_path: 
        :type base_path: :class:`huaweicloudsdkiotedge.v2.BasePathDTO`
        :param hardware_model: 注册节点网关配置
        :type hardware_model: str
        :param offline_cache_configs: 
        :type offline_cache_configs: :class:`huaweicloudsdkiotedge.v2.OfflineCacheConfigsDTO`
        :param device_auth_info: 
        :type device_auth_info: :class:`huaweicloudsdkiotedge.v2.DeviceAuthInfoDisplayDTO`
        """
        
        super(ShowEdgeNodeResponse, self).__init__()

        self._log_configs = None
        self._ha_config = None
        self._edge_node_id = None
        self._instance_id = None
        self._product_id = None
        self._product_name = None
        self._space_id = None
        self._resource_spec_types = None
        self._resource_ids = None
        self._ips = None
        self._name = None
        self._state = None
        self._software_version = None
        self._create_time = None
        self._update_time = None
        self._os_name = None
        self._arch = None
        self._host_name = None
        self._nics = None
        self._specification = None
        self._ai_card_type = None
        self._container_version = None
        self._type = None
        self._security_level = None
        self._reliability_level = None
        self._storage_period = None
        self._base_path = None
        self._hardware_model = None
        self._offline_cache_configs = None
        self._device_auth_info = None
        self.discriminator = None

        if log_configs is not None:
            self.log_configs = log_configs
        if ha_config is not None:
            self.ha_config = ha_config
        if edge_node_id is not None:
            self.edge_node_id = edge_node_id
        if instance_id is not None:
            self.instance_id = instance_id
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if space_id is not None:
            self.space_id = space_id
        if resource_spec_types is not None:
            self.resource_spec_types = resource_spec_types
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if ips is not None:
            self.ips = ips
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if software_version is not None:
            self.software_version = software_version
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if os_name is not None:
            self.os_name = os_name
        if arch is not None:
            self.arch = arch
        if host_name is not None:
            self.host_name = host_name
        if nics is not None:
            self.nics = nics
        if specification is not None:
            self.specification = specification
        if ai_card_type is not None:
            self.ai_card_type = ai_card_type
        if container_version is not None:
            self.container_version = container_version
        if type is not None:
            self.type = type
        if security_level is not None:
            self.security_level = security_level
        if reliability_level is not None:
            self.reliability_level = reliability_level
        if storage_period is not None:
            self.storage_period = storage_period
        if base_path is not None:
            self.base_path = base_path
        if hardware_model is not None:
            self.hardware_model = hardware_model
        if offline_cache_configs is not None:
            self.offline_cache_configs = offline_cache_configs
        if device_auth_info is not None:
            self.device_auth_info = device_auth_info

    @property
    def log_configs(self):
        """Gets the log_configs of this ShowEdgeNodeResponse.

        边缘节点在IEF的日志配置

        :return: The log_configs of this ShowEdgeNodeResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        """Sets the log_configs of this ShowEdgeNodeResponse.

        边缘节点在IEF的日志配置

        :param log_configs: The log_configs of this ShowEdgeNodeResponse.
        :type log_configs: list[:class:`huaweicloudsdkiotedge.v2.LogConfigDTO`]
        """
        self._log_configs = log_configs

    @property
    def ha_config(self):
        """Gets the ha_config of this ShowEdgeNodeResponse.

        :return: The ha_config of this ShowEdgeNodeResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.HaConfigDTO`
        """
        return self._ha_config

    @ha_config.setter
    def ha_config(self, ha_config):
        """Sets the ha_config of this ShowEdgeNodeResponse.

        :param ha_config: The ha_config of this ShowEdgeNodeResponse.
        :type ha_config: :class:`huaweicloudsdkiotedge.v2.HaConfigDTO`
        """
        self._ha_config = ha_config

    @property
    def edge_node_id(self):
        """Gets the edge_node_id of this ShowEdgeNodeResponse.

        边缘节点Id

        :return: The edge_node_id of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        """Sets the edge_node_id of this ShowEdgeNodeResponse.

        边缘节点Id

        :param edge_node_id: The edge_node_id of this ShowEdgeNodeResponse.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowEdgeNodeResponse.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowEdgeNodeResponse.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this ShowEdgeNodeResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def product_id(self):
        """Gets the product_id of this ShowEdgeNodeResponse.

        边缘节点关联的产品ID，用于唯一标识一个产品模型。

        :return: The product_id of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShowEdgeNodeResponse.

        边缘节点关联的产品ID，用于唯一标识一个产品模型。

        :param product_id: The product_id of this ShowEdgeNodeResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        """Gets the product_name of this ShowEdgeNodeResponse.

        边缘节点关联的产品名称。

        :return: The product_name of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ShowEdgeNodeResponse.

        边缘节点关联的产品名称。

        :param product_name: The product_name of this ShowEdgeNodeResponse.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def space_id(self):
        """Gets the space_id of this ShowEdgeNodeResponse.

        资源空间id，对应IOTDA云服务接口参数中的app_id。

        :return: The space_id of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this ShowEdgeNodeResponse.

        资源空间id，对应IOTDA云服务接口参数中的app_id。

        :param space_id: The space_id of this ShowEdgeNodeResponse.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def resource_spec_types(self):
        """Gets the resource_spec_types of this ShowEdgeNodeResponse.

        节点所购买的资源类型的列表

        :return: The resource_spec_types of this ShowEdgeNodeResponse.
        :rtype: list[str]
        """
        return self._resource_spec_types

    @resource_spec_types.setter
    def resource_spec_types(self, resource_spec_types):
        """Sets the resource_spec_types of this ShowEdgeNodeResponse.

        节点所购买的资源类型的列表

        :param resource_spec_types: The resource_spec_types of this ShowEdgeNodeResponse.
        :type resource_spec_types: list[str]
        """
        self._resource_spec_types = resource_spec_types

    @property
    def resource_ids(self):
        """Gets the resource_ids of this ShowEdgeNodeResponse.

        资源id列表，创建节点时需绑定已购买的资源包，可以叠加节点功能。

        :return: The resource_ids of this ShowEdgeNodeResponse.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this ShowEdgeNodeResponse.

        资源id列表，创建节点时需绑定已购买的资源包，可以叠加节点功能。

        :param resource_ids: The resource_ids of this ShowEdgeNodeResponse.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def ips(self):
        """Gets the ips of this ShowEdgeNodeResponse.

        边缘节点主机ip

        :return: The ips of this ShowEdgeNodeResponse.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this ShowEdgeNodeResponse.

        边缘节点主机ip

        :param ips: The ips of this ShowEdgeNodeResponse.
        :type ips: list[str]
        """
        self._ips = ips

    @property
    def name(self):
        """Gets the name of this ShowEdgeNodeResponse.

        边缘节点名称

        :return: The name of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowEdgeNodeResponse.

        边缘节点名称

        :param name: The name of this ShowEdgeNodeResponse.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        """Gets the state of this ShowEdgeNodeResponse.

        边缘节点状态

        :return: The state of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowEdgeNodeResponse.

        边缘节点状态

        :param state: The state of this ShowEdgeNodeResponse.
        :type state: str
        """
        self._state = state

    @property
    def software_version(self):
        """Gets the software_version of this ShowEdgeNodeResponse.

        边缘应用id，只允许数字、英文小写、中划线，切必须以字母或数字结尾

        :return: The software_version of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this ShowEdgeNodeResponse.

        边缘应用id，只允许数字、英文小写、中划线，切必须以字母或数字结尾

        :param software_version: The software_version of this ShowEdgeNodeResponse.
        :type software_version: str
        """
        self._software_version = software_version

    @property
    def create_time(self):
        """Gets the create_time of this ShowEdgeNodeResponse.

        边缘节点创建时间

        :return: The create_time of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowEdgeNodeResponse.

        边缘节点创建时间

        :param create_time: The create_time of this ShowEdgeNodeResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowEdgeNodeResponse.

        边缘节点更新时间

        :return: The update_time of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowEdgeNodeResponse.

        边缘节点更新时间

        :param update_time: The update_time of this ShowEdgeNodeResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def os_name(self):
        """Gets the os_name of this ShowEdgeNodeResponse.

        边缘节点操作系统名称

        :return: The os_name of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this ShowEdgeNodeResponse.

        边缘节点操作系统名称

        :param os_name: The os_name of this ShowEdgeNodeResponse.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def arch(self):
        """Gets the arch of this ShowEdgeNodeResponse.

        边缘节点操作系统架构

        :return: The arch of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ShowEdgeNodeResponse.

        边缘节点操作系统架构

        :param arch: The arch of this ShowEdgeNodeResponse.
        :type arch: str
        """
        self._arch = arch

    @property
    def host_name(self):
        """Gets the host_name of this ShowEdgeNodeResponse.

        边缘节点主机名

        :return: The host_name of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ShowEdgeNodeResponse.

        边缘节点主机名

        :param host_name: The host_name of this ShowEdgeNodeResponse.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def nics(self):
        """Gets the nics of this ShowEdgeNodeResponse.

        边缘节点网络网卡信息

        :return: The nics of this ShowEdgeNodeResponse.
        :rtype: list[:class:`huaweicloudsdkiotedge.v2.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this ShowEdgeNodeResponse.

        边缘节点网络网卡信息

        :param nics: The nics of this ShowEdgeNodeResponse.
        :type nics: list[:class:`huaweicloudsdkiotedge.v2.Nic`]
        """
        self._nics = nics

    @property
    def specification(self):
        """Gets the specification of this ShowEdgeNodeResponse.

        网络规格，如4 cores | 3867 MB

        :return: The specification of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this ShowEdgeNodeResponse.

        网络规格，如4 cores | 3867 MB

        :param specification: The specification of this ShowEdgeNodeResponse.
        :type specification: str
        """
        self._specification = specification

    @property
    def ai_card_type(self):
        """Gets the ai_card_type of this ShowEdgeNodeResponse.

        华为AI加速卡类型，如NPU、GPU、unEquipped

        :return: The ai_card_type of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._ai_card_type

    @ai_card_type.setter
    def ai_card_type(self, ai_card_type):
        """Sets the ai_card_type of this ShowEdgeNodeResponse.

        华为AI加速卡类型，如NPU、GPU、unEquipped

        :param ai_card_type: The ai_card_type of this ShowEdgeNodeResponse.
        :type ai_card_type: str
        """
        self._ai_card_type = ai_card_type

    @property
    def container_version(self):
        """Gets the container_version of this ShowEdgeNodeResponse.

        容器运行时版本

        :return: The container_version of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._container_version

    @container_version.setter
    def container_version(self, container_version):
        """Sets the container_version of this ShowEdgeNodeResponse.

        容器运行时版本

        :param container_version: The container_version of this ShowEdgeNodeResponse.
        :type container_version: str
        """
        self._container_version = container_version

    @property
    def type(self):
        """Gets the type of this ShowEdgeNodeResponse.

        节点所属资源类型：advanced|standard

        :return: The type of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowEdgeNodeResponse.

        节点所属资源类型：advanced|standard

        :param type: The type of this ShowEdgeNodeResponse.
        :type type: str
        """
        self._type = type

    @property
    def security_level(self):
        """Gets the security_level of this ShowEdgeNodeResponse.

        节点的安全等级，MEDIUM边缘节数据上报不进行加密，HIGH对数据上报进行加密。

        :return: The security_level of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """Sets the security_level of this ShowEdgeNodeResponse.

        节点的安全等级，MEDIUM边缘节数据上报不进行加密，HIGH对数据上报进行加密。

        :param security_level: The security_level of this ShowEdgeNodeResponse.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def reliability_level(self):
        """Gets the reliability_level of this ShowEdgeNodeResponse.

        节点的可靠性等级。

        :return: The reliability_level of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._reliability_level

    @reliability_level.setter
    def reliability_level(self, reliability_level):
        """Sets the reliability_level of this ShowEdgeNodeResponse.

        节点的可靠性等级。

        :param reliability_level: The reliability_level of this ShowEdgeNodeResponse.
        :type reliability_level: str
        """
        self._reliability_level = reliability_level

    @property
    def storage_period(self):
        """Gets the storage_period of this ShowEdgeNodeResponse.

        节点的存储周期，默认0天，取值范围0~7天，0天则不存储。

        :return: The storage_period of this ShowEdgeNodeResponse.
        :rtype: int
        """
        return self._storage_period

    @storage_period.setter
    def storage_period(self, storage_period):
        """Sets the storage_period of this ShowEdgeNodeResponse.

        节点的存储周期，默认0天，取值范围0~7天，0天则不存储。

        :param storage_period: The storage_period of this ShowEdgeNodeResponse.
        :type storage_period: int
        """
        self._storage_period = storage_period

    @property
    def base_path(self):
        """Gets the base_path of this ShowEdgeNodeResponse.

        :return: The base_path of this ShowEdgeNodeResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.BasePathDTO`
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this ShowEdgeNodeResponse.

        :param base_path: The base_path of this ShowEdgeNodeResponse.
        :type base_path: :class:`huaweicloudsdkiotedge.v2.BasePathDTO`
        """
        self._base_path = base_path

    @property
    def hardware_model(self):
        """Gets the hardware_model of this ShowEdgeNodeResponse.

        注册节点网关配置

        :return: The hardware_model of this ShowEdgeNodeResponse.
        :rtype: str
        """
        return self._hardware_model

    @hardware_model.setter
    def hardware_model(self, hardware_model):
        """Sets the hardware_model of this ShowEdgeNodeResponse.

        注册节点网关配置

        :param hardware_model: The hardware_model of this ShowEdgeNodeResponse.
        :type hardware_model: str
        """
        self._hardware_model = hardware_model

    @property
    def offline_cache_configs(self):
        """Gets the offline_cache_configs of this ShowEdgeNodeResponse.

        :return: The offline_cache_configs of this ShowEdgeNodeResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.OfflineCacheConfigsDTO`
        """
        return self._offline_cache_configs

    @offline_cache_configs.setter
    def offline_cache_configs(self, offline_cache_configs):
        """Sets the offline_cache_configs of this ShowEdgeNodeResponse.

        :param offline_cache_configs: The offline_cache_configs of this ShowEdgeNodeResponse.
        :type offline_cache_configs: :class:`huaweicloudsdkiotedge.v2.OfflineCacheConfigsDTO`
        """
        self._offline_cache_configs = offline_cache_configs

    @property
    def device_auth_info(self):
        """Gets the device_auth_info of this ShowEdgeNodeResponse.

        :return: The device_auth_info of this ShowEdgeNodeResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeviceAuthInfoDisplayDTO`
        """
        return self._device_auth_info

    @device_auth_info.setter
    def device_auth_info(self, device_auth_info):
        """Sets the device_auth_info of this ShowEdgeNodeResponse.

        :param device_auth_info: The device_auth_info of this ShowEdgeNodeResponse.
        :type device_auth_info: :class:`huaweicloudsdkiotedge.v2.DeviceAuthInfoDisplayDTO`
        """
        self._device_auth_info = device_auth_info

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
        if not isinstance(other, ShowEdgeNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
