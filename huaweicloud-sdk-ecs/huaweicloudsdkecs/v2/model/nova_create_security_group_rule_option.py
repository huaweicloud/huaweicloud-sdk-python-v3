# coding: utf-8

import pprint
import re

import six


class NovaCreateSecurityGroupRuleOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'cidr': 'str',
        'from_port': 'int',
        'group_id': 'str',
        'ip_protocol': 'str',
        'parent_group_id': 'str',
        'to_port': 'int'
    }

    attribute_map = {
        'cidr': 'cidr',
        'from_port': 'from_port',
        'group_id': 'group_id',
        'ip_protocol': 'ip_protocol',
        'parent_group_id': 'parent_group_id',
        'to_port': 'to_port'
    }

    def __init__(self, cidr=None, from_port=None, group_id=None, ip_protocol=None, parent_group_id=None, to_port=None):  # noqa: E501
        """NovaCreateSecurityGroupRuleOption - a model defined in huaweicloud sdk"""

        self._cidr = None
        self._from_port = None
        self._group_id = None
        self._ip_protocol = None
        self._parent_group_id = None
        self._to_port = None
        self.discriminator = None

        if cidr is not None:
            self.cidr = cidr
        self.from_port = from_port
        if group_id is not None:
            self.group_id = group_id
        self.ip_protocol = ip_protocol
        self.parent_group_id = parent_group_id
        self.to_port = to_port

    @property
    def cidr(self):
        """Gets the cidr of this NovaCreateSecurityGroupRuleOption.

        地址范围，CIDR格式，比如：“192.168.0.0/24”。

        :return: The cidr of this NovaCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this NovaCreateSecurityGroupRuleOption.

        地址范围，CIDR格式，比如：“192.168.0.0/24”。

        :param cidr: The cidr of this NovaCreateSecurityGroupRuleOption.
        :type: str
        """
        self._cidr = cidr

    @property
    def from_port(self):
        """Gets the from_port of this NovaCreateSecurityGroupRuleOption.

        起始端口，范围1-65535，且不大于to_port(icmp时，表示type，范围是0-255)。

        :return: The from_port of this NovaCreateSecurityGroupRuleOption.
        :rtype: int
        """
        return self._from_port

    @from_port.setter
    def from_port(self, from_port):
        """Sets the from_port of this NovaCreateSecurityGroupRuleOption.

        起始端口，范围1-65535，且不大于to_port(icmp时，表示type，范围是0-255)。

        :param from_port: The from_port of this NovaCreateSecurityGroupRuleOption.
        :type: int
        """
        self._from_port = from_port

    @property
    def group_id(self):
        """Gets the group_id of this NovaCreateSecurityGroupRuleOption.

        源安全组ID  若同时指定group_id和cidr，则以group_id为准。

        :return: The group_id of this NovaCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this NovaCreateSecurityGroupRuleOption.

        源安全组ID  若同时指定group_id和cidr，则以group_id为准。

        :param group_id: The group_id of this NovaCreateSecurityGroupRuleOption.
        :type: str
        """
        self._group_id = group_id

    @property
    def ip_protocol(self):
        """Gets the ip_protocol of this NovaCreateSecurityGroupRuleOption.

        IP协议：icmp，tcp，或者udp。

        :return: The ip_protocol of this NovaCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._ip_protocol

    @ip_protocol.setter
    def ip_protocol(self, ip_protocol):
        """Sets the ip_protocol of this NovaCreateSecurityGroupRuleOption.

        IP协议：icmp，tcp，或者udp。

        :param ip_protocol: The ip_protocol of this NovaCreateSecurityGroupRuleOption.
        :type: str
        """
        self._ip_protocol = ip_protocol

    @property
    def parent_group_id(self):
        """Gets the parent_group_id of this NovaCreateSecurityGroupRuleOption.

        相关联的安全组ID，UUID格式。

        :return: The parent_group_id of this NovaCreateSecurityGroupRuleOption.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """Sets the parent_group_id of this NovaCreateSecurityGroupRuleOption.

        相关联的安全组ID，UUID格式。

        :param parent_group_id: The parent_group_id of this NovaCreateSecurityGroupRuleOption.
        :type: str
        """
        self._parent_group_id = parent_group_id

    @property
    def to_port(self):
        """Gets the to_port of this NovaCreateSecurityGroupRuleOption.

        终止端口，范围1-65535，且不小于from_port(icmp时，表示code，范围是0-255，且如果from_port为-1，to_port为-1表示任意ICMP报文)。

        :return: The to_port of this NovaCreateSecurityGroupRuleOption.
        :rtype: int
        """
        return self._to_port

    @to_port.setter
    def to_port(self, to_port):
        """Sets the to_port of this NovaCreateSecurityGroupRuleOption.

        终止端口，范围1-65535，且不小于from_port(icmp时，表示code，范围是0-255，且如果from_port为-1，to_port为-1表示任意ICMP报文)。

        :param to_port: The to_port of this NovaCreateSecurityGroupRuleOption.
        :type: int
        """
        self._to_port = to_port

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
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NovaCreateSecurityGroupRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
