# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrafficMirrorFilterRule:

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
        'description': 'str',
        'traffic_mirror_filter_id': 'str',
        'direction': 'str',
        'source_cidr_block': 'str',
        'destination_cidr_block': 'str',
        'source_port_range': 'str',
        'destination_port_range': 'str',
        'ethertype': 'str',
        'protocol': 'str',
        'action': 'str',
        'priority': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'description': 'description',
        'traffic_mirror_filter_id': 'traffic_mirror_filter_id',
        'direction': 'direction',
        'source_cidr_block': 'source_cidr_block',
        'destination_cidr_block': 'destination_cidr_block',
        'source_port_range': 'source_port_range',
        'destination_port_range': 'destination_port_range',
        'ethertype': 'ethertype',
        'protocol': 'protocol',
        'action': 'action',
        'priority': 'priority',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, project_id=None, description=None, traffic_mirror_filter_id=None, direction=None, source_cidr_block=None, destination_cidr_block=None, source_port_range=None, destination_port_range=None, ethertype=None, protocol=None, action=None, priority=None, created_at=None, updated_at=None):
        """TrafficMirrorFilterRule

        The model defined in huaweicloud sdk

        :param id: 功能说明：流量镜像筛选规则ID
        :type id: str
        :param project_id: 功能说明：项目ID
        :type project_id: str
        :param description: 功能说明：流量镜像筛选规则的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param traffic_mirror_filter_id: 功能说明：流量镜像筛选条件ID
        :type traffic_mirror_filter_id: str
        :param direction: 功能说明：流量方向 取值范围：     ingress：入方向     egress：出方向
        :type direction: str
        :param source_cidr_block: 功能说明：镜像流量的源网段
        :type source_cidr_block: str
        :param destination_cidr_block: 功能说明：镜像流量的目的网段
        :type destination_cidr_block: str
        :param source_port_range: 功能说明：流量源端口范围 取值范围：1~65535 格式：80-200
        :type source_port_range: str
        :param destination_port_range: 功能说明：流量目的端口范围 取值范围：1~65535 格式：80-200
        :type destination_port_range: str
        :param ethertype: 功能说明：镜像流量的地址协议版本 取值范围：IPv4，IPv6
        :type ethertype: str
        :param protocol: 功能说明：镜像流量的协议类型 取值范围：TCP、UDP、ICMP、ICMPV6、ALL
        :type protocol: str
        :param action: 功能说明：镜像策略 取值范围：accept（采集）、reject（不采集）
        :type action: str
        :param priority: 功能说明：镜像规则优先级 取值范围：1~65535，数字越小，优先级越高
        :type priority: int
        :param created_at: 创建时间戳
        :type created_at: datetime
        :param updated_at: 更新时间戳
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._project_id = None
        self._description = None
        self._traffic_mirror_filter_id = None
        self._direction = None
        self._source_cidr_block = None
        self._destination_cidr_block = None
        self._source_port_range = None
        self._destination_port_range = None
        self._ethertype = None
        self._protocol = None
        self._action = None
        self._priority = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.project_id = project_id
        self.description = description
        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        self.direction = direction
        self.source_cidr_block = source_cidr_block
        self.destination_cidr_block = destination_cidr_block
        self.source_port_range = source_port_range
        self.destination_port_range = destination_port_range
        self.ethertype = ethertype
        self.protocol = protocol
        self.action = action
        self.priority = priority
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this TrafficMirrorFilterRule.

        功能说明：流量镜像筛选规则ID

        :return: The id of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrafficMirrorFilterRule.

        功能说明：流量镜像筛选规则ID

        :param id: The id of this TrafficMirrorFilterRule.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this TrafficMirrorFilterRule.

        功能说明：项目ID

        :return: The project_id of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TrafficMirrorFilterRule.

        功能说明：项目ID

        :param project_id: The project_id of this TrafficMirrorFilterRule.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        """Gets the description of this TrafficMirrorFilterRule.

        功能说明：流量镜像筛选规则的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TrafficMirrorFilterRule.

        功能说明：流量镜像筛选规则的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this TrafficMirrorFilterRule.
        :type description: str
        """
        self._description = description

    @property
    def traffic_mirror_filter_id(self):
        """Gets the traffic_mirror_filter_id of this TrafficMirrorFilterRule.

        功能说明：流量镜像筛选条件ID

        :return: The traffic_mirror_filter_id of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._traffic_mirror_filter_id

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, traffic_mirror_filter_id):
        """Sets the traffic_mirror_filter_id of this TrafficMirrorFilterRule.

        功能说明：流量镜像筛选条件ID

        :param traffic_mirror_filter_id: The traffic_mirror_filter_id of this TrafficMirrorFilterRule.
        :type traffic_mirror_filter_id: str
        """
        self._traffic_mirror_filter_id = traffic_mirror_filter_id

    @property
    def direction(self):
        """Gets the direction of this TrafficMirrorFilterRule.

        功能说明：流量方向 取值范围：     ingress：入方向     egress：出方向

        :return: The direction of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TrafficMirrorFilterRule.

        功能说明：流量方向 取值范围：     ingress：入方向     egress：出方向

        :param direction: The direction of this TrafficMirrorFilterRule.
        :type direction: str
        """
        self._direction = direction

    @property
    def source_cidr_block(self):
        """Gets the source_cidr_block of this TrafficMirrorFilterRule.

        功能说明：镜像流量的源网段

        :return: The source_cidr_block of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._source_cidr_block

    @source_cidr_block.setter
    def source_cidr_block(self, source_cidr_block):
        """Sets the source_cidr_block of this TrafficMirrorFilterRule.

        功能说明：镜像流量的源网段

        :param source_cidr_block: The source_cidr_block of this TrafficMirrorFilterRule.
        :type source_cidr_block: str
        """
        self._source_cidr_block = source_cidr_block

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this TrafficMirrorFilterRule.

        功能说明：镜像流量的目的网段

        :return: The destination_cidr_block of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this TrafficMirrorFilterRule.

        功能说明：镜像流量的目的网段

        :param destination_cidr_block: The destination_cidr_block of this TrafficMirrorFilterRule.
        :type destination_cidr_block: str
        """
        self._destination_cidr_block = destination_cidr_block

    @property
    def source_port_range(self):
        """Gets the source_port_range of this TrafficMirrorFilterRule.

        功能说明：流量源端口范围 取值范围：1~65535 格式：80-200

        :return: The source_port_range of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._source_port_range

    @source_port_range.setter
    def source_port_range(self, source_port_range):
        """Sets the source_port_range of this TrafficMirrorFilterRule.

        功能说明：流量源端口范围 取值范围：1~65535 格式：80-200

        :param source_port_range: The source_port_range of this TrafficMirrorFilterRule.
        :type source_port_range: str
        """
        self._source_port_range = source_port_range

    @property
    def destination_port_range(self):
        """Gets the destination_port_range of this TrafficMirrorFilterRule.

        功能说明：流量目的端口范围 取值范围：1~65535 格式：80-200

        :return: The destination_port_range of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._destination_port_range

    @destination_port_range.setter
    def destination_port_range(self, destination_port_range):
        """Sets the destination_port_range of this TrafficMirrorFilterRule.

        功能说明：流量目的端口范围 取值范围：1~65535 格式：80-200

        :param destination_port_range: The destination_port_range of this TrafficMirrorFilterRule.
        :type destination_port_range: str
        """
        self._destination_port_range = destination_port_range

    @property
    def ethertype(self):
        """Gets the ethertype of this TrafficMirrorFilterRule.

        功能说明：镜像流量的地址协议版本 取值范围：IPv4，IPv6

        :return: The ethertype of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        """Sets the ethertype of this TrafficMirrorFilterRule.

        功能说明：镜像流量的地址协议版本 取值范围：IPv4，IPv6

        :param ethertype: The ethertype of this TrafficMirrorFilterRule.
        :type ethertype: str
        """
        self._ethertype = ethertype

    @property
    def protocol(self):
        """Gets the protocol of this TrafficMirrorFilterRule.

        功能说明：镜像流量的协议类型 取值范围：TCP、UDP、ICMP、ICMPV6、ALL

        :return: The protocol of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this TrafficMirrorFilterRule.

        功能说明：镜像流量的协议类型 取值范围：TCP、UDP、ICMP、ICMPV6、ALL

        :param protocol: The protocol of this TrafficMirrorFilterRule.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def action(self):
        """Gets the action of this TrafficMirrorFilterRule.

        功能说明：镜像策略 取值范围：accept（采集）、reject（不采集）

        :return: The action of this TrafficMirrorFilterRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this TrafficMirrorFilterRule.

        功能说明：镜像策略 取值范围：accept（采集）、reject（不采集）

        :param action: The action of this TrafficMirrorFilterRule.
        :type action: str
        """
        self._action = action

    @property
    def priority(self):
        """Gets the priority of this TrafficMirrorFilterRule.

        功能说明：镜像规则优先级 取值范围：1~65535，数字越小，优先级越高

        :return: The priority of this TrafficMirrorFilterRule.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TrafficMirrorFilterRule.

        功能说明：镜像规则优先级 取值范围：1~65535，数字越小，优先级越高

        :param priority: The priority of this TrafficMirrorFilterRule.
        :type priority: int
        """
        self._priority = priority

    @property
    def created_at(self):
        """Gets the created_at of this TrafficMirrorFilterRule.

        创建时间戳

        :return: The created_at of this TrafficMirrorFilterRule.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TrafficMirrorFilterRule.

        创建时间戳

        :param created_at: The created_at of this TrafficMirrorFilterRule.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TrafficMirrorFilterRule.

        更新时间戳

        :return: The updated_at of this TrafficMirrorFilterRule.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TrafficMirrorFilterRule.

        更新时间戳

        :param updated_at: The updated_at of this TrafficMirrorFilterRule.
        :type updated_at: datetime
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
        if not isinstance(other, TrafficMirrorFilterRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
