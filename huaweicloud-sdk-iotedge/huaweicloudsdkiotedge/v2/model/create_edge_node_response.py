# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeNodeResponse(SdkResponse):

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
        'instance_id': 'str',
        'space_id': 'str',
        'product_id': 'str',
        'product_name': 'str',
        'state': 'str',
        'type': 'str',
        'installer_version': 'str',
        'base_path': 'BasePathDTO',
        'resource_ids': 'list[str]',
        'ips': 'list[str]',
        'create_time': 'str',
        'hardware_model': 'str',
        'device_data_format': 'str',
        'automatic_upgrade': 'str',
        'device_data_record': 'DeviceDataRecord',
        'metric_report': 'str'
    }

    attribute_map = {
        'edge_node_id': 'edge_node_id',
        'name': 'name',
        'instance_id': 'instance_id',
        'space_id': 'space_id',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'state': 'state',
        'type': 'type',
        'installer_version': 'installer_version',
        'base_path': 'base_path',
        'resource_ids': 'resource_ids',
        'ips': 'ips',
        'create_time': 'create_time',
        'hardware_model': 'hardware_model',
        'device_data_format': 'device_data_format',
        'automatic_upgrade': 'automatic_upgrade',
        'device_data_record': 'device_data_record',
        'metric_report': 'metric_report'
    }

    def __init__(self, edge_node_id=None, name=None, instance_id=None, space_id=None, product_id=None, product_name=None, state=None, type=None, installer_version=None, base_path=None, resource_ids=None, ips=None, create_time=None, hardware_model=None, device_data_format=None, automatic_upgrade=None, device_data_record=None, metric_report=None):
        r"""CreateEdgeNodeResponse

        The model defined in huaweicloud sdk

        :param edge_node_id: 边缘节点ID
        :type edge_node_id: str
        :param name: 边缘节点名称
        :type name: str
        :param instance_id: 实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。
        :type instance_id: str
        :param space_id: 资源空间id，对应IOTDA云服务接口参数中的app_id。
        :type space_id: str
        :param product_id: 边缘节点关联的产品ID，用于唯一标识一个产品模型。
        :type product_id: str
        :param product_name: 边缘节点关联的产品名称。
        :type product_name: str
        :param state: 边缘节点状态UNINSTALLED|INSTALLED|OFFLINE|ONLINE|DELETING|FROZEN
        :type state: str
        :param type: 节点所属资源类型：advanced|standard
        :type type: str
        :param installer_version: 安装文件版本
        :type installer_version: str
        :param base_path: 
        :type base_path: :class:`huaweicloudsdkiotedge.v2.BasePathDTO`
        :param resource_ids: 资源id列表，创建节点时需绑定已购买的资源包，可以叠加节点功能。
        :type resource_ids: list[str]
        :param ips: 边缘节点ip列表
        :type ips: list[str]
        :param create_time: 边缘节点创建时间
        :type create_time: str
        :param hardware_model: 注册节点网关配置
        :type hardware_model: str
        :param device_data_format: 节点使用的数据格式，默认为iotda物模型1.0格式，可以选择属性平铺数据格式flat_json
        :type device_data_format: str
        :param automatic_upgrade: 自动升级系统应用的节点开关，默认为关闭：OFF，IMMEDIATE表示节点开关打开
        :type automatic_upgrade: str
        :param device_data_record: 
        :type device_data_record: :class:`huaweicloudsdkiotedge.v2.DeviceDataRecord`
        :param metric_report: omagent监控运维工具是否上报指标
        :type metric_report: str
        """
        
        super(CreateEdgeNodeResponse, self).__init__()

        self._edge_node_id = None
        self._name = None
        self._instance_id = None
        self._space_id = None
        self._product_id = None
        self._product_name = None
        self._state = None
        self._type = None
        self._installer_version = None
        self._base_path = None
        self._resource_ids = None
        self._ips = None
        self._create_time = None
        self._hardware_model = None
        self._device_data_format = None
        self._automatic_upgrade = None
        self._device_data_record = None
        self._metric_report = None
        self.discriminator = None

        if edge_node_id is not None:
            self.edge_node_id = edge_node_id
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if space_id is not None:
            self.space_id = space_id
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if installer_version is not None:
            self.installer_version = installer_version
        if base_path is not None:
            self.base_path = base_path
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if ips is not None:
            self.ips = ips
        if create_time is not None:
            self.create_time = create_time
        if hardware_model is not None:
            self.hardware_model = hardware_model
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
        r"""Gets the edge_node_id of this CreateEdgeNodeResponse.

        边缘节点ID

        :return: The edge_node_id of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._edge_node_id

    @edge_node_id.setter
    def edge_node_id(self, edge_node_id):
        r"""Sets the edge_node_id of this CreateEdgeNodeResponse.

        边缘节点ID

        :param edge_node_id: The edge_node_id of this CreateEdgeNodeResponse.
        :type edge_node_id: str
        """
        self._edge_node_id = edge_node_id

    @property
    def name(self):
        r"""Gets the name of this CreateEdgeNodeResponse.

        边缘节点名称

        :return: The name of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateEdgeNodeResponse.

        边缘节点名称

        :param name: The name of this CreateEdgeNodeResponse.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateEdgeNodeResponse.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateEdgeNodeResponse.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this CreateEdgeNodeResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def space_id(self):
        r"""Gets the space_id of this CreateEdgeNodeResponse.

        资源空间id，对应IOTDA云服务接口参数中的app_id。

        :return: The space_id of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        r"""Sets the space_id of this CreateEdgeNodeResponse.

        资源空间id，对应IOTDA云服务接口参数中的app_id。

        :param space_id: The space_id of this CreateEdgeNodeResponse.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def product_id(self):
        r"""Gets the product_id of this CreateEdgeNodeResponse.

        边缘节点关联的产品ID，用于唯一标识一个产品模型。

        :return: The product_id of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this CreateEdgeNodeResponse.

        边缘节点关联的产品ID，用于唯一标识一个产品模型。

        :param product_id: The product_id of this CreateEdgeNodeResponse.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        r"""Gets the product_name of this CreateEdgeNodeResponse.

        边缘节点关联的产品名称。

        :return: The product_name of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this CreateEdgeNodeResponse.

        边缘节点关联的产品名称。

        :param product_name: The product_name of this CreateEdgeNodeResponse.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def state(self):
        r"""Gets the state of this CreateEdgeNodeResponse.

        边缘节点状态UNINSTALLED|INSTALLED|OFFLINE|ONLINE|DELETING|FROZEN

        :return: The state of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CreateEdgeNodeResponse.

        边缘节点状态UNINSTALLED|INSTALLED|OFFLINE|ONLINE|DELETING|FROZEN

        :param state: The state of this CreateEdgeNodeResponse.
        :type state: str
        """
        self._state = state

    @property
    def type(self):
        r"""Gets the type of this CreateEdgeNodeResponse.

        节点所属资源类型：advanced|standard

        :return: The type of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateEdgeNodeResponse.

        节点所属资源类型：advanced|standard

        :param type: The type of this CreateEdgeNodeResponse.
        :type type: str
        """
        self._type = type

    @property
    def installer_version(self):
        r"""Gets the installer_version of this CreateEdgeNodeResponse.

        安装文件版本

        :return: The installer_version of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._installer_version

    @installer_version.setter
    def installer_version(self, installer_version):
        r"""Sets the installer_version of this CreateEdgeNodeResponse.

        安装文件版本

        :param installer_version: The installer_version of this CreateEdgeNodeResponse.
        :type installer_version: str
        """
        self._installer_version = installer_version

    @property
    def base_path(self):
        r"""Gets the base_path of this CreateEdgeNodeResponse.

        :return: The base_path of this CreateEdgeNodeResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.BasePathDTO`
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        r"""Sets the base_path of this CreateEdgeNodeResponse.

        :param base_path: The base_path of this CreateEdgeNodeResponse.
        :type base_path: :class:`huaweicloudsdkiotedge.v2.BasePathDTO`
        """
        self._base_path = base_path

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this CreateEdgeNodeResponse.

        资源id列表，创建节点时需绑定已购买的资源包，可以叠加节点功能。

        :return: The resource_ids of this CreateEdgeNodeResponse.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this CreateEdgeNodeResponse.

        资源id列表，创建节点时需绑定已购买的资源包，可以叠加节点功能。

        :param resource_ids: The resource_ids of this CreateEdgeNodeResponse.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def ips(self):
        r"""Gets the ips of this CreateEdgeNodeResponse.

        边缘节点ip列表

        :return: The ips of this CreateEdgeNodeResponse.
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        r"""Sets the ips of this CreateEdgeNodeResponse.

        边缘节点ip列表

        :param ips: The ips of this CreateEdgeNodeResponse.
        :type ips: list[str]
        """
        self._ips = ips

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateEdgeNodeResponse.

        边缘节点创建时间

        :return: The create_time of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateEdgeNodeResponse.

        边缘节点创建时间

        :param create_time: The create_time of this CreateEdgeNodeResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def hardware_model(self):
        r"""Gets the hardware_model of this CreateEdgeNodeResponse.

        注册节点网关配置

        :return: The hardware_model of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._hardware_model

    @hardware_model.setter
    def hardware_model(self, hardware_model):
        r"""Sets the hardware_model of this CreateEdgeNodeResponse.

        注册节点网关配置

        :param hardware_model: The hardware_model of this CreateEdgeNodeResponse.
        :type hardware_model: str
        """
        self._hardware_model = hardware_model

    @property
    def device_data_format(self):
        r"""Gets the device_data_format of this CreateEdgeNodeResponse.

        节点使用的数据格式，默认为iotda物模型1.0格式，可以选择属性平铺数据格式flat_json

        :return: The device_data_format of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._device_data_format

    @device_data_format.setter
    def device_data_format(self, device_data_format):
        r"""Sets the device_data_format of this CreateEdgeNodeResponse.

        节点使用的数据格式，默认为iotda物模型1.0格式，可以选择属性平铺数据格式flat_json

        :param device_data_format: The device_data_format of this CreateEdgeNodeResponse.
        :type device_data_format: str
        """
        self._device_data_format = device_data_format

    @property
    def automatic_upgrade(self):
        r"""Gets the automatic_upgrade of this CreateEdgeNodeResponse.

        自动升级系统应用的节点开关，默认为关闭：OFF，IMMEDIATE表示节点开关打开

        :return: The automatic_upgrade of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._automatic_upgrade

    @automatic_upgrade.setter
    def automatic_upgrade(self, automatic_upgrade):
        r"""Sets the automatic_upgrade of this CreateEdgeNodeResponse.

        自动升级系统应用的节点开关，默认为关闭：OFF，IMMEDIATE表示节点开关打开

        :param automatic_upgrade: The automatic_upgrade of this CreateEdgeNodeResponse.
        :type automatic_upgrade: str
        """
        self._automatic_upgrade = automatic_upgrade

    @property
    def device_data_record(self):
        r"""Gets the device_data_record of this CreateEdgeNodeResponse.

        :return: The device_data_record of this CreateEdgeNodeResponse.
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeviceDataRecord`
        """
        return self._device_data_record

    @device_data_record.setter
    def device_data_record(self, device_data_record):
        r"""Sets the device_data_record of this CreateEdgeNodeResponse.

        :param device_data_record: The device_data_record of this CreateEdgeNodeResponse.
        :type device_data_record: :class:`huaweicloudsdkiotedge.v2.DeviceDataRecord`
        """
        self._device_data_record = device_data_record

    @property
    def metric_report(self):
        r"""Gets the metric_report of this CreateEdgeNodeResponse.

        omagent监控运维工具是否上报指标

        :return: The metric_report of this CreateEdgeNodeResponse.
        :rtype: str
        """
        return self._metric_report

    @metric_report.setter
    def metric_report(self, metric_report):
        r"""Sets the metric_report of this CreateEdgeNodeResponse.

        omagent监控运维工具是否上报指标

        :param metric_report: The metric_report of this CreateEdgeNodeResponse.
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
        if not isinstance(other, CreateEdgeNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
