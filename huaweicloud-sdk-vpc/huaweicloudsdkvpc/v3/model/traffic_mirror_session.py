# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrafficMirrorSession:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'project_id': 'str',
        'name': 'str',
        'description': 'str',
        'traffic_mirror_filter_id': 'str',
        'traffic_mirror_sources': 'list[str]',
        'traffic_mirror_target_id': 'str',
        'traffic_mirror_target_type': 'str',
        'virtual_network_id': 'int',
        'packet_length': 'int',
        'priority': 'int',
        'enabled': 'bool',
        'type': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'traffic_mirror_filter_id': 'traffic_mirror_filter_id',
        'traffic_mirror_sources': 'traffic_mirror_sources',
        'traffic_mirror_target_id': 'traffic_mirror_target_id',
        'traffic_mirror_target_type': 'traffic_mirror_target_type',
        'virtual_network_id': 'virtual_network_id',
        'packet_length': 'packet_length',
        'priority': 'priority',
        'enabled': 'enabled',
        'type': 'type',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, project_id=None, name=None, description=None, traffic_mirror_filter_id=None, traffic_mirror_sources=None, traffic_mirror_target_id=None, traffic_mirror_target_type=None, virtual_network_id=None, packet_length=None, priority=None, enabled=None, type=None, created_at=None, updated_at=None):
        """TrafficMirrorSession

        The model defined in huaweicloud sdk

        :param id: 功能说明：流量镜像会话ID
        :type id: str
        :param project_id: 功能说明：项目ID
        :type project_id: str
        :param name: 功能说明：流量镜像会话名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：流量镜像会话的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param traffic_mirror_filter_id: 功能说明：流量镜像筛选条件ID
        :type traffic_mirror_filter_id: str
        :param traffic_mirror_sources: 功能说明：镜像源ID列表，支持弹性网卡作为镜像源。 约束：一个镜像会话默认最大支持10个镜像源。
        :type traffic_mirror_sources: list[str]
        :param traffic_mirror_target_id: 功能说明：镜像目的ID
        :type traffic_mirror_target_id: str
        :param traffic_mirror_target_type: 功能说明：镜像目的类型 取值范围：     eni：弹性网卡     elb：私网弹性负载均衡
        :type traffic_mirror_target_type: str
        :param virtual_network_id: 功能说明：指定VNI，用于区分不同会话的镜像流量 取值范围：0~16777215 默认值：1
        :type virtual_network_id: int
        :param packet_length: 功能说明：最大传输单元MTU 取值范围：1~1460 默认值：96
        :type packet_length: int
        :param priority: 功能说明：会话优先级 取值范围：1~32766
        :type priority: int
        :param enabled: 功能说明：是否开启会话 取值范围：true、false 默认值：false
        :type enabled: bool
        :param type: 功能说明：支持的镜像源类型 取值范围：     eni：弹性网卡
        :type type: str
        :param created_at: 功能说明：创建时间戳
        :type created_at: str
        :param updated_at: 功能说明：更新时间戳
        :type updated_at: str
        """
        
        

        self._id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._traffic_mirror_filter_id = None
        self._traffic_mirror_sources = None
        self._traffic_mirror_target_id = None
        self._traffic_mirror_target_type = None
        self._virtual_network_id = None
        self._packet_length = None
        self._priority = None
        self._enabled = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.name = name
        self.description = description
        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        self.traffic_mirror_sources = traffic_mirror_sources
        self.traffic_mirror_target_id = traffic_mirror_target_id
        self.traffic_mirror_target_type = traffic_mirror_target_type
        self.virtual_network_id = virtual_network_id
        self.packet_length = packet_length
        self.priority = priority
        self.enabled = enabled
        self.type = type
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this TrafficMirrorSession.

        功能说明：流量镜像会话ID

        :return: The id of this TrafficMirrorSession.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrafficMirrorSession.

        功能说明：流量镜像会话ID

        :param id: The id of this TrafficMirrorSession.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this TrafficMirrorSession.

        功能说明：项目ID

        :return: The project_id of this TrafficMirrorSession.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TrafficMirrorSession.

        功能说明：项目ID

        :param project_id: The project_id of this TrafficMirrorSession.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this TrafficMirrorSession.

        功能说明：流量镜像会话名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this TrafficMirrorSession.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrafficMirrorSession.

        功能说明：流量镜像会话名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this TrafficMirrorSession.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this TrafficMirrorSession.

        功能说明：流量镜像会话的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this TrafficMirrorSession.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TrafficMirrorSession.

        功能说明：流量镜像会话的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this TrafficMirrorSession.
        :type description: str
        """
        self._description = description

    @property
    def traffic_mirror_filter_id(self):
        """Gets the traffic_mirror_filter_id of this TrafficMirrorSession.

        功能说明：流量镜像筛选条件ID

        :return: The traffic_mirror_filter_id of this TrafficMirrorSession.
        :rtype: str
        """
        return self._traffic_mirror_filter_id

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, traffic_mirror_filter_id):
        """Sets the traffic_mirror_filter_id of this TrafficMirrorSession.

        功能说明：流量镜像筛选条件ID

        :param traffic_mirror_filter_id: The traffic_mirror_filter_id of this TrafficMirrorSession.
        :type traffic_mirror_filter_id: str
        """
        self._traffic_mirror_filter_id = traffic_mirror_filter_id

    @property
    def traffic_mirror_sources(self):
        """Gets the traffic_mirror_sources of this TrafficMirrorSession.

        功能说明：镜像源ID列表，支持弹性网卡作为镜像源。 约束：一个镜像会话默认最大支持10个镜像源。

        :return: The traffic_mirror_sources of this TrafficMirrorSession.
        :rtype: list[str]
        """
        return self._traffic_mirror_sources

    @traffic_mirror_sources.setter
    def traffic_mirror_sources(self, traffic_mirror_sources):
        """Sets the traffic_mirror_sources of this TrafficMirrorSession.

        功能说明：镜像源ID列表，支持弹性网卡作为镜像源。 约束：一个镜像会话默认最大支持10个镜像源。

        :param traffic_mirror_sources: The traffic_mirror_sources of this TrafficMirrorSession.
        :type traffic_mirror_sources: list[str]
        """
        self._traffic_mirror_sources = traffic_mirror_sources

    @property
    def traffic_mirror_target_id(self):
        """Gets the traffic_mirror_target_id of this TrafficMirrorSession.

        功能说明：镜像目的ID

        :return: The traffic_mirror_target_id of this TrafficMirrorSession.
        :rtype: str
        """
        return self._traffic_mirror_target_id

    @traffic_mirror_target_id.setter
    def traffic_mirror_target_id(self, traffic_mirror_target_id):
        """Sets the traffic_mirror_target_id of this TrafficMirrorSession.

        功能说明：镜像目的ID

        :param traffic_mirror_target_id: The traffic_mirror_target_id of this TrafficMirrorSession.
        :type traffic_mirror_target_id: str
        """
        self._traffic_mirror_target_id = traffic_mirror_target_id

    @property
    def traffic_mirror_target_type(self):
        """Gets the traffic_mirror_target_type of this TrafficMirrorSession.

        功能说明：镜像目的类型 取值范围：     eni：弹性网卡     elb：私网弹性负载均衡

        :return: The traffic_mirror_target_type of this TrafficMirrorSession.
        :rtype: str
        """
        return self._traffic_mirror_target_type

    @traffic_mirror_target_type.setter
    def traffic_mirror_target_type(self, traffic_mirror_target_type):
        """Sets the traffic_mirror_target_type of this TrafficMirrorSession.

        功能说明：镜像目的类型 取值范围：     eni：弹性网卡     elb：私网弹性负载均衡

        :param traffic_mirror_target_type: The traffic_mirror_target_type of this TrafficMirrorSession.
        :type traffic_mirror_target_type: str
        """
        self._traffic_mirror_target_type = traffic_mirror_target_type

    @property
    def virtual_network_id(self):
        """Gets the virtual_network_id of this TrafficMirrorSession.

        功能说明：指定VNI，用于区分不同会话的镜像流量 取值范围：0~16777215 默认值：1

        :return: The virtual_network_id of this TrafficMirrorSession.
        :rtype: int
        """
        return self._virtual_network_id

    @virtual_network_id.setter
    def virtual_network_id(self, virtual_network_id):
        """Sets the virtual_network_id of this TrafficMirrorSession.

        功能说明：指定VNI，用于区分不同会话的镜像流量 取值范围：0~16777215 默认值：1

        :param virtual_network_id: The virtual_network_id of this TrafficMirrorSession.
        :type virtual_network_id: int
        """
        self._virtual_network_id = virtual_network_id

    @property
    def packet_length(self):
        """Gets the packet_length of this TrafficMirrorSession.

        功能说明：最大传输单元MTU 取值范围：1~1460 默认值：96

        :return: The packet_length of this TrafficMirrorSession.
        :rtype: int
        """
        return self._packet_length

    @packet_length.setter
    def packet_length(self, packet_length):
        """Sets the packet_length of this TrafficMirrorSession.

        功能说明：最大传输单元MTU 取值范围：1~1460 默认值：96

        :param packet_length: The packet_length of this TrafficMirrorSession.
        :type packet_length: int
        """
        self._packet_length = packet_length

    @property
    def priority(self):
        """Gets the priority of this TrafficMirrorSession.

        功能说明：会话优先级 取值范围：1~32766

        :return: The priority of this TrafficMirrorSession.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TrafficMirrorSession.

        功能说明：会话优先级 取值范围：1~32766

        :param priority: The priority of this TrafficMirrorSession.
        :type priority: int
        """
        self._priority = priority

    @property
    def enabled(self):
        """Gets the enabled of this TrafficMirrorSession.

        功能说明：是否开启会话 取值范围：true、false 默认值：false

        :return: The enabled of this TrafficMirrorSession.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this TrafficMirrorSession.

        功能说明：是否开启会话 取值范围：true、false 默认值：false

        :param enabled: The enabled of this TrafficMirrorSession.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def type(self):
        """Gets the type of this TrafficMirrorSession.

        功能说明：支持的镜像源类型 取值范围：     eni：弹性网卡

        :return: The type of this TrafficMirrorSession.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TrafficMirrorSession.

        功能说明：支持的镜像源类型 取值范围：     eni：弹性网卡

        :param type: The type of this TrafficMirrorSession.
        :type type: str
        """
        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this TrafficMirrorSession.

        功能说明：创建时间戳

        :return: The created_at of this TrafficMirrorSession.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TrafficMirrorSession.

        功能说明：创建时间戳

        :param created_at: The created_at of this TrafficMirrorSession.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TrafficMirrorSession.

        功能说明：更新时间戳

        :return: The updated_at of this TrafficMirrorSession.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TrafficMirrorSession.

        功能说明：更新时间戳

        :param updated_at: The updated_at of this TrafficMirrorSession.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, TrafficMirrorSession):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
