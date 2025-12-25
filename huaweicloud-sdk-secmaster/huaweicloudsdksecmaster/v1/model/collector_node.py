# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectorNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_instance_refer_count': 'int',
        'create_by': 'str',
        'custom_label': 'str',
        'description': 'str',
        'device_type': 'str',
        'ip_address': 'str',
        'monitor': 'Monitor',
        'node_expansion': 'IsapNodeExpansion',
        'node_id': 'str',
        'node_name': 'str',
        'os_type': 'str',
        'private_ip_address': 'str',
        'project_id': 'str',
        'region': 'str',
        'specification': 'str',
        'update_time': 'int',
        'vpc_endpoint_address': 'str',
        'vpc_endpoint_id': 'str',
        'vpc_id': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'channel_instance_refer_count': 'channel_instance_refer_count',
        'create_by': 'create_by',
        'custom_label': 'custom_label',
        'description': 'description',
        'device_type': 'device_type',
        'ip_address': 'ip_address',
        'monitor': 'monitor',
        'node_expansion': 'node_expansion',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'os_type': 'os_type',
        'private_ip_address': 'private_ip_address',
        'project_id': 'project_id',
        'region': 'region',
        'specification': 'specification',
        'update_time': 'update_time',
        'vpc_endpoint_address': 'vpc_endpoint_address',
        'vpc_endpoint_id': 'vpc_endpoint_id',
        'vpc_id': 'vpc_id',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, channel_instance_refer_count=None, create_by=None, custom_label=None, description=None, device_type=None, ip_address=None, monitor=None, node_expansion=None, node_id=None, node_name=None, os_type=None, private_ip_address=None, project_id=None, region=None, specification=None, update_time=None, vpc_endpoint_address=None, vpc_endpoint_id=None, vpc_id=None, workspace_id=None):
        r"""CollectorNode

        The model defined in huaweicloud sdk

        :param channel_instance_refer_count: 数值
        :type channel_instance_refer_count: int
        :param create_by: Iam用户ID
        :type create_by: str
        :param custom_label: 自定义标签
        :type custom_label: str
        :param description: 描述信息
        :type description: str
        :param device_type: 设备类型
        :type device_type: str
        :param ip_address: IP地址
        :type ip_address: str
        :param monitor: 
        :type monitor: :class:`huaweicloudsdksecmaster.v1.Monitor`
        :param node_expansion: 
        :type node_expansion: :class:`huaweicloudsdksecmaster.v1.IsapNodeExpansion`
        :param node_id: UUID
        :type node_id: str
        :param node_name: 所属租户名称
        :type node_name: str
        :param os_type: 操作系统类型
        :type os_type: str
        :param private_ip_address: IP地址
        :type private_ip_address: str
        :param project_id: 项目ID
        :type project_id: str
        :param region: 区域
        :type region: str
        :param specification: 规格
        :type specification: str
        :param update_time: 毫秒时间戳
        :type update_time: int
        :param vpc_endpoint_address: Vpc 端点地址
        :type vpc_endpoint_address: str
        :param vpc_endpoint_id: Vpc 端点ID
        :type vpc_endpoint_id: str
        :param vpc_id: UUID
        :type vpc_id: str
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        """
        
        

        self._channel_instance_refer_count = None
        self._create_by = None
        self._custom_label = None
        self._description = None
        self._device_type = None
        self._ip_address = None
        self._monitor = None
        self._node_expansion = None
        self._node_id = None
        self._node_name = None
        self._os_type = None
        self._private_ip_address = None
        self._project_id = None
        self._region = None
        self._specification = None
        self._update_time = None
        self._vpc_endpoint_address = None
        self._vpc_endpoint_id = None
        self._vpc_id = None
        self._workspace_id = None
        self.discriminator = None

        if channel_instance_refer_count is not None:
            self.channel_instance_refer_count = channel_instance_refer_count
        if create_by is not None:
            self.create_by = create_by
        if custom_label is not None:
            self.custom_label = custom_label
        if description is not None:
            self.description = description
        if device_type is not None:
            self.device_type = device_type
        if ip_address is not None:
            self.ip_address = ip_address
        if monitor is not None:
            self.monitor = monitor
        if node_expansion is not None:
            self.node_expansion = node_expansion
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if os_type is not None:
            self.os_type = os_type
        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if project_id is not None:
            self.project_id = project_id
        if region is not None:
            self.region = region
        if specification is not None:
            self.specification = specification
        if update_time is not None:
            self.update_time = update_time
        if vpc_endpoint_address is not None:
            self.vpc_endpoint_address = vpc_endpoint_address
        if vpc_endpoint_id is not None:
            self.vpc_endpoint_id = vpc_endpoint_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def channel_instance_refer_count(self):
        r"""Gets the channel_instance_refer_count of this CollectorNode.

        数值

        :return: The channel_instance_refer_count of this CollectorNode.
        :rtype: int
        """
        return self._channel_instance_refer_count

    @channel_instance_refer_count.setter
    def channel_instance_refer_count(self, channel_instance_refer_count):
        r"""Sets the channel_instance_refer_count of this CollectorNode.

        数值

        :param channel_instance_refer_count: The channel_instance_refer_count of this CollectorNode.
        :type channel_instance_refer_count: int
        """
        self._channel_instance_refer_count = channel_instance_refer_count

    @property
    def create_by(self):
        r"""Gets the create_by of this CollectorNode.

        Iam用户ID

        :return: The create_by of this CollectorNode.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this CollectorNode.

        Iam用户ID

        :param create_by: The create_by of this CollectorNode.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def custom_label(self):
        r"""Gets the custom_label of this CollectorNode.

        自定义标签

        :return: The custom_label of this CollectorNode.
        :rtype: str
        """
        return self._custom_label

    @custom_label.setter
    def custom_label(self, custom_label):
        r"""Sets the custom_label of this CollectorNode.

        自定义标签

        :param custom_label: The custom_label of this CollectorNode.
        :type custom_label: str
        """
        self._custom_label = custom_label

    @property
    def description(self):
        r"""Gets the description of this CollectorNode.

        描述信息

        :return: The description of this CollectorNode.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CollectorNode.

        描述信息

        :param description: The description of this CollectorNode.
        :type description: str
        """
        self._description = description

    @property
    def device_type(self):
        r"""Gets the device_type of this CollectorNode.

        设备类型

        :return: The device_type of this CollectorNode.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        r"""Sets the device_type of this CollectorNode.

        设备类型

        :param device_type: The device_type of this CollectorNode.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def ip_address(self):
        r"""Gets the ip_address of this CollectorNode.

        IP地址

        :return: The ip_address of this CollectorNode.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this CollectorNode.

        IP地址

        :param ip_address: The ip_address of this CollectorNode.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def monitor(self):
        r"""Gets the monitor of this CollectorNode.

        :return: The monitor of this CollectorNode.
        :rtype: :class:`huaweicloudsdksecmaster.v1.Monitor`
        """
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        r"""Sets the monitor of this CollectorNode.

        :param monitor: The monitor of this CollectorNode.
        :type monitor: :class:`huaweicloudsdksecmaster.v1.Monitor`
        """
        self._monitor = monitor

    @property
    def node_expansion(self):
        r"""Gets the node_expansion of this CollectorNode.

        :return: The node_expansion of this CollectorNode.
        :rtype: :class:`huaweicloudsdksecmaster.v1.IsapNodeExpansion`
        """
        return self._node_expansion

    @node_expansion.setter
    def node_expansion(self, node_expansion):
        r"""Sets the node_expansion of this CollectorNode.

        :param node_expansion: The node_expansion of this CollectorNode.
        :type node_expansion: :class:`huaweicloudsdksecmaster.v1.IsapNodeExpansion`
        """
        self._node_expansion = node_expansion

    @property
    def node_id(self):
        r"""Gets the node_id of this CollectorNode.

        UUID

        :return: The node_id of this CollectorNode.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CollectorNode.

        UUID

        :param node_id: The node_id of this CollectorNode.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this CollectorNode.

        所属租户名称

        :return: The node_name of this CollectorNode.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this CollectorNode.

        所属租户名称

        :param node_name: The node_name of this CollectorNode.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def os_type(self):
        r"""Gets the os_type of this CollectorNode.

        操作系统类型

        :return: The os_type of this CollectorNode.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this CollectorNode.

        操作系统类型

        :param os_type: The os_type of this CollectorNode.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def private_ip_address(self):
        r"""Gets the private_ip_address of this CollectorNode.

        IP地址

        :return: The private_ip_address of this CollectorNode.
        :rtype: str
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        r"""Sets the private_ip_address of this CollectorNode.

        IP地址

        :param private_ip_address: The private_ip_address of this CollectorNode.
        :type private_ip_address: str
        """
        self._private_ip_address = private_ip_address

    @property
    def project_id(self):
        r"""Gets the project_id of this CollectorNode.

        项目ID

        :return: The project_id of this CollectorNode.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CollectorNode.

        项目ID

        :param project_id: The project_id of this CollectorNode.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region(self):
        r"""Gets the region of this CollectorNode.

        区域

        :return: The region of this CollectorNode.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CollectorNode.

        区域

        :param region: The region of this CollectorNode.
        :type region: str
        """
        self._region = region

    @property
    def specification(self):
        r"""Gets the specification of this CollectorNode.

        规格

        :return: The specification of this CollectorNode.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this CollectorNode.

        规格

        :param specification: The specification of this CollectorNode.
        :type specification: str
        """
        self._specification = specification

    @property
    def update_time(self):
        r"""Gets the update_time of this CollectorNode.

        毫秒时间戳

        :return: The update_time of this CollectorNode.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this CollectorNode.

        毫秒时间戳

        :param update_time: The update_time of this CollectorNode.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def vpc_endpoint_address(self):
        r"""Gets the vpc_endpoint_address of this CollectorNode.

        Vpc 端点地址

        :return: The vpc_endpoint_address of this CollectorNode.
        :rtype: str
        """
        return self._vpc_endpoint_address

    @vpc_endpoint_address.setter
    def vpc_endpoint_address(self, vpc_endpoint_address):
        r"""Sets the vpc_endpoint_address of this CollectorNode.

        Vpc 端点地址

        :param vpc_endpoint_address: The vpc_endpoint_address of this CollectorNode.
        :type vpc_endpoint_address: str
        """
        self._vpc_endpoint_address = vpc_endpoint_address

    @property
    def vpc_endpoint_id(self):
        r"""Gets the vpc_endpoint_id of this CollectorNode.

        Vpc 端点ID

        :return: The vpc_endpoint_id of this CollectorNode.
        :rtype: str
        """
        return self._vpc_endpoint_id

    @vpc_endpoint_id.setter
    def vpc_endpoint_id(self, vpc_endpoint_id):
        r"""Sets the vpc_endpoint_id of this CollectorNode.

        Vpc 端点ID

        :param vpc_endpoint_id: The vpc_endpoint_id of this CollectorNode.
        :type vpc_endpoint_id: str
        """
        self._vpc_endpoint_id = vpc_endpoint_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CollectorNode.

        UUID

        :return: The vpc_id of this CollectorNode.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CollectorNode.

        UUID

        :param vpc_id: The vpc_id of this CollectorNode.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CollectorNode.

        工作空间ID

        :return: The workspace_id of this CollectorNode.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CollectorNode.

        工作空间ID

        :param workspace_id: The workspace_id of this CollectorNode.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, CollectorNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
