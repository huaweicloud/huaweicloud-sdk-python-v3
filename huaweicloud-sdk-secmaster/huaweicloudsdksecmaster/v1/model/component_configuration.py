# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'component_name': 'str',
        'config_status': 'str',
        'create_time': 'int',
        'fail_deploy_message': 'str',
        'ip_address': 'str',
        'list': 'list[ComponentConfigurationParam]',
        'monitor': 'Monitor',
        'node_apply_fail_enum': 'str',
        'node_expansion': 'IsapNodeExpansion',
        'node_id': 'str',
        'node_name': 'str',
        'private_ip_address': 'str',
        'region': 'str',
        'specification': 'str',
        'vpc_endpoint_address': 'str',
        'vpc_endpoint_id': 'str'
    }

    attribute_map = {
        'component_id': 'component_id',
        'component_name': 'component_name',
        'config_status': 'config_status',
        'create_time': 'create_time',
        'fail_deploy_message': 'fail_deploy_message',
        'ip_address': 'ip_address',
        'list': 'list',
        'monitor': 'monitor',
        'node_apply_fail_enum': 'node_apply_fail_enum',
        'node_expansion': 'node_expansion',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'private_ip_address': 'private_ip_address',
        'region': 'region',
        'specification': 'specification',
        'vpc_endpoint_address': 'vpc_endpoint_address',
        'vpc_endpoint_id': 'vpc_endpoint_id'
    }

    def __init__(self, component_id=None, component_name=None, config_status=None, create_time=None, fail_deploy_message=None, ip_address=None, list=None, monitor=None, node_apply_fail_enum=None, node_expansion=None, node_id=None, node_name=None, private_ip_address=None, region=None, specification=None, vpc_endpoint_address=None, vpc_endpoint_id=None):
        r"""ComponentConfiguration

        The model defined in huaweicloud sdk

        :param component_id: 组件id.
        :type component_id: str
        :param component_name: 组件名称
        :type component_name: str
        :param config_status: **参数解释**: 节点配置状态 - UN_SAVED 待保存 - SAVE_AND_UN_APPLY 待应用 - MOVE_AND_UN_APPLY 待移除 - APPLYING 应用中 - FAIL_APPLY 应用失败 - APPLIED 应用完成  **约束限制** 不涉及 **取值范围**: - UN_SAVED - SAVE_AND_UN_APPLY - MOVE_AND_UN_APPLY - APPLYING - FAIL_APPLY - APPLIED  **默认值** 不涉及
        :type config_status: str
        :param create_time: 毫秒时间戳
        :type create_time: int
        :param fail_deploy_message: 部署失败的消息
        :type fail_deploy_message: str
        :param ip_address: IP地址
        :type ip_address: str
        :param list: 组件配置参数列表
        :type list: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfigurationParam`]
        :param monitor: 
        :type monitor: :class:`huaweicloudsdksecmaster.v1.Monitor`
        :param node_apply_fail_enum: **参数解释**: 节点应用成功与否状态、原因 - COLLECTOR_USE 采集器使用中，无法移除 - NODE_OFFLINE 节点失联状态，无法应用  **约束限制** 不涉及 **取值范围**: - COLLECTOR_USE - NODE_OFFLINE  **默认值** 不涉及
        :type node_apply_fail_enum: str
        :param node_expansion: 
        :type node_expansion: :class:`huaweicloudsdksecmaster.v1.IsapNodeExpansion`
        :param node_id: 节点ID
        :type node_id: str
        :param node_name: 节点名称
        :type node_name: str
        :param private_ip_address: IP地址
        :type private_ip_address: str
        :param region: 地区
        :type region: str
        :param specification: 规范
        :type specification: str
        :param vpc_endpoint_address: VPC端点地址
        :type vpc_endpoint_address: str
        :param vpc_endpoint_id: VPC端点ID
        :type vpc_endpoint_id: str
        """
        
        

        self._component_id = None
        self._component_name = None
        self._config_status = None
        self._create_time = None
        self._fail_deploy_message = None
        self._ip_address = None
        self._list = None
        self._monitor = None
        self._node_apply_fail_enum = None
        self._node_expansion = None
        self._node_id = None
        self._node_name = None
        self._private_ip_address = None
        self._region = None
        self._specification = None
        self._vpc_endpoint_address = None
        self._vpc_endpoint_id = None
        self.discriminator = None

        if component_id is not None:
            self.component_id = component_id
        if component_name is not None:
            self.component_name = component_name
        if config_status is not None:
            self.config_status = config_status
        if create_time is not None:
            self.create_time = create_time
        if fail_deploy_message is not None:
            self.fail_deploy_message = fail_deploy_message
        if ip_address is not None:
            self.ip_address = ip_address
        if list is not None:
            self.list = list
        if monitor is not None:
            self.monitor = monitor
        if node_apply_fail_enum is not None:
            self.node_apply_fail_enum = node_apply_fail_enum
        if node_expansion is not None:
            self.node_expansion = node_expansion
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if region is not None:
            self.region = region
        if specification is not None:
            self.specification = specification
        if vpc_endpoint_address is not None:
            self.vpc_endpoint_address = vpc_endpoint_address
        if vpc_endpoint_id is not None:
            self.vpc_endpoint_id = vpc_endpoint_id

    @property
    def component_id(self):
        r"""Gets the component_id of this ComponentConfiguration.

        组件id.

        :return: The component_id of this ComponentConfiguration.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ComponentConfiguration.

        组件id.

        :param component_id: The component_id of this ComponentConfiguration.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def component_name(self):
        r"""Gets the component_name of this ComponentConfiguration.

        组件名称

        :return: The component_name of this ComponentConfiguration.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this ComponentConfiguration.

        组件名称

        :param component_name: The component_name of this ComponentConfiguration.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def config_status(self):
        r"""Gets the config_status of this ComponentConfiguration.

        **参数解释**: 节点配置状态 - UN_SAVED 待保存 - SAVE_AND_UN_APPLY 待应用 - MOVE_AND_UN_APPLY 待移除 - APPLYING 应用中 - FAIL_APPLY 应用失败 - APPLIED 应用完成  **约束限制** 不涉及 **取值范围**: - UN_SAVED - SAVE_AND_UN_APPLY - MOVE_AND_UN_APPLY - APPLYING - FAIL_APPLY - APPLIED  **默认值** 不涉及

        :return: The config_status of this ComponentConfiguration.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        r"""Sets the config_status of this ComponentConfiguration.

        **参数解释**: 节点配置状态 - UN_SAVED 待保存 - SAVE_AND_UN_APPLY 待应用 - MOVE_AND_UN_APPLY 待移除 - APPLYING 应用中 - FAIL_APPLY 应用失败 - APPLIED 应用完成  **约束限制** 不涉及 **取值范围**: - UN_SAVED - SAVE_AND_UN_APPLY - MOVE_AND_UN_APPLY - APPLYING - FAIL_APPLY - APPLIED  **默认值** 不涉及

        :param config_status: The config_status of this ComponentConfiguration.
        :type config_status: str
        """
        self._config_status = config_status

    @property
    def create_time(self):
        r"""Gets the create_time of this ComponentConfiguration.

        毫秒时间戳

        :return: The create_time of this ComponentConfiguration.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ComponentConfiguration.

        毫秒时间戳

        :param create_time: The create_time of this ComponentConfiguration.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def fail_deploy_message(self):
        r"""Gets the fail_deploy_message of this ComponentConfiguration.

        部署失败的消息

        :return: The fail_deploy_message of this ComponentConfiguration.
        :rtype: str
        """
        return self._fail_deploy_message

    @fail_deploy_message.setter
    def fail_deploy_message(self, fail_deploy_message):
        r"""Sets the fail_deploy_message of this ComponentConfiguration.

        部署失败的消息

        :param fail_deploy_message: The fail_deploy_message of this ComponentConfiguration.
        :type fail_deploy_message: str
        """
        self._fail_deploy_message = fail_deploy_message

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ComponentConfiguration.

        IP地址

        :return: The ip_address of this ComponentConfiguration.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ComponentConfiguration.

        IP地址

        :param ip_address: The ip_address of this ComponentConfiguration.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def list(self):
        r"""Gets the list of this ComponentConfiguration.

        组件配置参数列表

        :return: The list of this ComponentConfiguration.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfigurationParam`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this ComponentConfiguration.

        组件配置参数列表

        :param list: The list of this ComponentConfiguration.
        :type list: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfigurationParam`]
        """
        self._list = list

    @property
    def monitor(self):
        r"""Gets the monitor of this ComponentConfiguration.

        :return: The monitor of this ComponentConfiguration.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Monitor`
        """
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        r"""Sets the monitor of this ComponentConfiguration.

        :param monitor: The monitor of this ComponentConfiguration.
        :type monitor: :class:`huaweicloudsdksecmaster.v1.Monitor`
        """
        self._monitor = monitor

    @property
    def node_apply_fail_enum(self):
        r"""Gets the node_apply_fail_enum of this ComponentConfiguration.

        **参数解释**: 节点应用成功与否状态、原因 - COLLECTOR_USE 采集器使用中，无法移除 - NODE_OFFLINE 节点失联状态，无法应用  **约束限制** 不涉及 **取值范围**: - COLLECTOR_USE - NODE_OFFLINE  **默认值** 不涉及

        :return: The node_apply_fail_enum of this ComponentConfiguration.
        :rtype: str
        """
        return self._node_apply_fail_enum

    @node_apply_fail_enum.setter
    def node_apply_fail_enum(self, node_apply_fail_enum):
        r"""Sets the node_apply_fail_enum of this ComponentConfiguration.

        **参数解释**: 节点应用成功与否状态、原因 - COLLECTOR_USE 采集器使用中，无法移除 - NODE_OFFLINE 节点失联状态，无法应用  **约束限制** 不涉及 **取值范围**: - COLLECTOR_USE - NODE_OFFLINE  **默认值** 不涉及

        :param node_apply_fail_enum: The node_apply_fail_enum of this ComponentConfiguration.
        :type node_apply_fail_enum: str
        """
        self._node_apply_fail_enum = node_apply_fail_enum

    @property
    def node_expansion(self):
        r"""Gets the node_expansion of this ComponentConfiguration.

        :return: The node_expansion of this ComponentConfiguration.
        :rtype: :class:`huaweicloudsdksecmaster.v1.IsapNodeExpansion`
        """
        return self._node_expansion

    @node_expansion.setter
    def node_expansion(self, node_expansion):
        r"""Sets the node_expansion of this ComponentConfiguration.

        :param node_expansion: The node_expansion of this ComponentConfiguration.
        :type node_expansion: :class:`huaweicloudsdksecmaster.v1.IsapNodeExpansion`
        """
        self._node_expansion = node_expansion

    @property
    def node_id(self):
        r"""Gets the node_id of this ComponentConfiguration.

        节点ID

        :return: The node_id of this ComponentConfiguration.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ComponentConfiguration.

        节点ID

        :param node_id: The node_id of this ComponentConfiguration.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this ComponentConfiguration.

        节点名称

        :return: The node_name of this ComponentConfiguration.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ComponentConfiguration.

        节点名称

        :param node_name: The node_name of this ComponentConfiguration.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def private_ip_address(self):
        r"""Gets the private_ip_address of this ComponentConfiguration.

        IP地址

        :return: The private_ip_address of this ComponentConfiguration.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        r"""Sets the private_ip_address of this ComponentConfiguration.

        IP地址

        :param private_ip_address: The private_ip_address of this ComponentConfiguration.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def region(self):
        r"""Gets the region of this ComponentConfiguration.

        地区

        :return: The region of this ComponentConfiguration.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ComponentConfiguration.

        地区

        :param region: The region of this ComponentConfiguration.
        :type region: str
        """
        self._region = region

    @property
    def specification(self):
        r"""Gets the specification of this ComponentConfiguration.

        规范

        :return: The specification of this ComponentConfiguration.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this ComponentConfiguration.

        规范

        :param specification: The specification of this ComponentConfiguration.
        :type specification: str
        """
        self._specification = specification

    @property
    def vpc_endpoint_address(self):
        r"""Gets the vpc_endpoint_address of this ComponentConfiguration.

        VPC端点地址

        :return: The vpc_endpoint_address of this ComponentConfiguration.
        :rtype: str
        """
        return self._vpc_endpoint_address

    @vpc_endpoint_address.setter
    def vpc_endpoint_address(self, vpc_endpoint_address):
        r"""Sets the vpc_endpoint_address of this ComponentConfiguration.

        VPC端点地址

        :param vpc_endpoint_address: The vpc_endpoint_address of this ComponentConfiguration.
        :type vpc_endpoint_address: str
        """
        self._vpc_endpoint_address = vpc_endpoint_address

    @property
    def vpc_endpoint_id(self):
        r"""Gets the vpc_endpoint_id of this ComponentConfiguration.

        VPC端点ID

        :return: The vpc_endpoint_id of this ComponentConfiguration.
        :rtype: str
        """
        return self._vpc_endpoint_id

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, vpc_endpoint_id):
        r"""Sets the vpc_endpoint_id of this ComponentConfiguration.

        VPC端点ID

        :param vpc_endpoint_id: The vpc_endpoint_id of this ComponentConfiguration.
        :type vpc_endpoint_id: str
        """
        self._vpc_endpoint_id = vpc_endpoint_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ComponentConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
