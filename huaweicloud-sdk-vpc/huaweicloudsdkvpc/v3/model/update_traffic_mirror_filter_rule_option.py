# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTrafficMirrorFilterRuleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'protocol': 'str',
        'ethertype': 'str',
        'source_cidr_block': 'str',
        'destination_cidr_block': 'str',
        'source_port_range': 'str',
        'destination_port_range': 'str',
        'priority': 'int',
        'action': 'str'
    }

    attribute_map = {
        'description': 'description',
        'protocol': 'protocol',
        'ethertype': 'ethertype',
        'source_cidr_block': 'source_cidr_block',
        'destination_cidr_block': 'destination_cidr_block',
        'source_port_range': 'source_port_range',
        'destination_port_range': 'destination_port_range',
        'priority': 'priority',
        'action': 'action'
    }

    def __init__(self, description=None, protocol=None, ethertype=None, source_cidr_block=None, destination_cidr_block=None, source_port_range=None, destination_port_range=None, priority=None, action=None):
        """UpdateTrafficMirrorFilterRuleOption

        The model defined in huaweicloud sdk

        :param description: 功能说明：流量镜像筛选规则的描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param protocol: 功能说明：镜像流量的协议类型 取值范围：TCP、UDP、ICMP、ICMPV6、ALL
        :type protocol: str
        :param ethertype: 功能说明：镜像流量的地址协议版本 取值范围：IPv4，IPv6
        :type ethertype: str
        :param source_cidr_block: 功能说明：镜像流量的源网段
        :type source_cidr_block: str
        :param destination_cidr_block: 功能说明：镜像流量的目的网段
        :type destination_cidr_block: str
        :param source_port_range: 功能说明：流量源端口范围 取值范围：1~65535 格式：80-200
        :type source_port_range: str
        :param destination_port_range: 功能说明：流量目的端口范围 取值范围：1~65535 格式：80-200
        :type destination_port_range: str
        :param priority: 功能说明：镜像规则优先级 取值范围：1~65535，数字越小，优先级越高
        :type priority: int
        :param action: 功能说明：镜像策略 取值范围：accept（采集）、reject（不采集）
        :type action: str
        """
        
        

        self._description = None
        self._protocol = None
        self._ethertype = None
        self._source_cidr_block = None
        self._destination_cidr_block = None
        self._source_port_range = None
        self._destination_port_range = None
        self._priority = None
        self._action = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if protocol is not None:
            self.protocol = protocol
        if ethertype is not None:
            self.ethertype = ethertype
        if source_cidr_block is not None:
            self.source_cidr_block = source_cidr_block
        if destination_cidr_block is not None:
            self.destination_cidr_block = destination_cidr_block
        if source_port_range is not None:
            self.source_port_range = source_port_range
        if destination_port_range is not None:
            self.destination_port_range = destination_port_range
        if priority is not None:
            self.priority = priority
        if action is not None:
            self.action = action

    @property
    def description(self):
        """Gets the description of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：流量镜像筛选规则的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this UpdateTrafficMirrorFilterRuleOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：流量镜像筛选规则的描述信息 取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this UpdateTrafficMirrorFilterRuleOption.
        :type description: str
        """
        self._description = description

    @property
    def protocol(self):
        """Gets the protocol of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像流量的协议类型 取值范围：TCP、UDP、ICMP、ICMPV6、ALL

        :return: The protocol of this UpdateTrafficMirrorFilterRuleOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像流量的协议类型 取值范围：TCP、UDP、ICMP、ICMPV6、ALL

        :param protocol: The protocol of this UpdateTrafficMirrorFilterRuleOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def ethertype(self):
        """Gets the ethertype of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像流量的地址协议版本 取值范围：IPv4，IPv6

        :return: The ethertype of this UpdateTrafficMirrorFilterRuleOption.
        :rtype: str
        """
        return self._ethertype

    @ethertype.setter
    def ethertype(self, ethertype):
        """Sets the ethertype of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像流量的地址协议版本 取值范围：IPv4，IPv6

        :param ethertype: The ethertype of this UpdateTrafficMirrorFilterRuleOption.
        :type ethertype: str
        """
        self._ethertype = ethertype

    @property
    def source_cidr_block(self):
        """Gets the source_cidr_block of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像流量的源网段

        :return: The source_cidr_block of this UpdateTrafficMirrorFilterRuleOption.
        :rtype: str
        """
        return self._source_cidr_block

    @source_cidr_block.setter
    def source_cidr_block(self, source_cidr_block):
        """Sets the source_cidr_block of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像流量的源网段

        :param source_cidr_block: The source_cidr_block of this UpdateTrafficMirrorFilterRuleOption.
        :type source_cidr_block: str
        """
        self._source_cidr_block = source_cidr_block

    @property
    def destination_cidr_block(self):
        """Gets the destination_cidr_block of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像流量的目的网段

        :return: The destination_cidr_block of this UpdateTrafficMirrorFilterRuleOption.
        :rtype: str
        """
        return self._destination_cidr_block

    @destination_cidr_block.setter
    def destination_cidr_block(self, destination_cidr_block):
        """Sets the destination_cidr_block of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像流量的目的网段

        :param destination_cidr_block: The destination_cidr_block of this UpdateTrafficMirrorFilterRuleOption.
        :type destination_cidr_block: str
        """
        self._destination_cidr_block = destination_cidr_block

    @property
    def source_port_range(self):
        """Gets the source_port_range of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：流量源端口范围 取值范围：1~65535 格式：80-200

        :return: The source_port_range of this UpdateTrafficMirrorFilterRuleOption.
        :rtype: str
        """
        return self._source_port_range

    @source_port_range.setter
    def source_port_range(self, source_port_range):
        """Sets the source_port_range of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：流量源端口范围 取值范围：1~65535 格式：80-200

        :param source_port_range: The source_port_range of this UpdateTrafficMirrorFilterRuleOption.
        :type source_port_range: str
        """
        self._source_port_range = source_port_range

    @property
    def destination_port_range(self):
        """Gets the destination_port_range of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：流量目的端口范围 取值范围：1~65535 格式：80-200

        :return: The destination_port_range of this UpdateTrafficMirrorFilterRuleOption.
        :rtype: str
        """
        return self._destination_port_range

    @destination_port_range.setter
    def destination_port_range(self, destination_port_range):
        """Sets the destination_port_range of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：流量目的端口范围 取值范围：1~65535 格式：80-200

        :param destination_port_range: The destination_port_range of this UpdateTrafficMirrorFilterRuleOption.
        :type destination_port_range: str
        """
        self._destination_port_range = destination_port_range

    @property
    def priority(self):
        """Gets the priority of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像规则优先级 取值范围：1~65535，数字越小，优先级越高

        :return: The priority of this UpdateTrafficMirrorFilterRuleOption.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像规则优先级 取值范围：1~65535，数字越小，优先级越高

        :param priority: The priority of this UpdateTrafficMirrorFilterRuleOption.
        :type priority: int
        """
        self._priority = priority

    @property
    def action(self):
        """Gets the action of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像策略 取值范围：accept（采集）、reject（不采集）

        :return: The action of this UpdateTrafficMirrorFilterRuleOption.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateTrafficMirrorFilterRuleOption.

        功能说明：镜像策略 取值范围：accept（采集）、reject（不采集）

        :param action: The action of this UpdateTrafficMirrorFilterRuleOption.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, UpdateTrafficMirrorFilterRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
