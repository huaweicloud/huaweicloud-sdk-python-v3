# coding: utf-8

import pprint
import re

import six


class NovaCreateSecurityGroupRuleResult(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'from_port': 'int',
        'group': 'object',
        'id': 'str',
        'ip_protocol': 'str',
        'ip_range': 'NovaSecurityGroupCommonIpRange',
        'parent_group_id': 'str',
        'to_port': 'int'
    }

    attribute_map = {
        'from_port': 'from_port',
        'group': 'group',
        'id': 'id',
        'ip_protocol': 'ip_protocol',
        'ip_range': 'ip_range',
        'parent_group_id': 'parent_group_id',
        'to_port': 'to_port'
    }

    def __init__(self, from_port=None, group=None, id=None, ip_protocol=None, ip_range=None, parent_group_id=None, to_port=None):  # noqa: E501
        """NovaCreateSecurityGroupRuleResult - a model defined in huaweicloud sdk"""

        self._from_port = None
        self._group = None
        self._id = None
        self._ip_protocol = None
        self._ip_range = None
        self._parent_group_id = None
        self._to_port = None
        self.discriminator = None

        self.from_port = from_port
        self.group = group
        self.id = id
        self.ip_protocol = ip_protocol
        self.ip_range = ip_range
        self.parent_group_id = parent_group_id
        self.to_port = to_port

    @property
    def from_port(self):
        """Gets the from_port of this NovaCreateSecurityGroupRuleResult.

        起始端口，范围1-65535，且不大于to_port 。当协议类型为icmp时，from_port为icmp协议的type，范围是0-255。

        :return: The from_port of this NovaCreateSecurityGroupRuleResult.
        :rtype: int
        """
        return self._from_port

    @from_port.setter
    def from_port(self, from_port):
        """Sets the from_port of this NovaCreateSecurityGroupRuleResult.

        起始端口，范围1-65535，且不大于to_port 。当协议类型为icmp时，from_port为icmp协议的type，范围是0-255。

        :param from_port: The from_port of this NovaCreateSecurityGroupRuleResult.
        :type: int
        """
        self._from_port = from_port

    @property
    def group(self):
        """Gets the group of this NovaCreateSecurityGroupRuleResult.

        固定返回空字典。

        :return: The group of this NovaCreateSecurityGroupRuleResult.
        :rtype: object
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this NovaCreateSecurityGroupRuleResult.

        固定返回空字典。

        :param group: The group of this NovaCreateSecurityGroupRuleResult.
        :type: object
        """
        self._group = group

    @property
    def id(self):
        """Gets the id of this NovaCreateSecurityGroupRuleResult.

        安全组规则ID

        :return: The id of this NovaCreateSecurityGroupRuleResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NovaCreateSecurityGroupRuleResult.

        安全组规则ID

        :param id: The id of this NovaCreateSecurityGroupRuleResult.
        :type: str
        """
        self._id = id

    @property
    def ip_protocol(self):
        """Gets the ip_protocol of this NovaCreateSecurityGroupRuleResult.

        IP协议：icmp，tcp，或者udp

        :return: The ip_protocol of this NovaCreateSecurityGroupRuleResult.
        :rtype: str
        """
        return self._ip_protocol

    @ip_protocol.setter
    def ip_protocol(self, ip_protocol):
        """Sets the ip_protocol of this NovaCreateSecurityGroupRuleResult.

        IP协议：icmp，tcp，或者udp

        :param ip_protocol: The ip_protocol of this NovaCreateSecurityGroupRuleResult.
        :type: str
        """
        self._ip_protocol = ip_protocol

    @property
    def ip_range(self):
        """Gets the ip_range of this NovaCreateSecurityGroupRuleResult.


        :return: The ip_range of this NovaCreateSecurityGroupRuleResult.
        :rtype: NovaSecurityGroupCommonIpRange
        """
        return self._ip_range

    @ip_range.setter
    def ip_range(self, ip_range):
        """Sets the ip_range of this NovaCreateSecurityGroupRuleResult.


        :param ip_range: The ip_range of this NovaCreateSecurityGroupRuleResult.
        :type: NovaSecurityGroupCommonIpRange
        """
        self._ip_range = ip_range

    @property
    def parent_group_id(self):
        """Gets the parent_group_id of this NovaCreateSecurityGroupRuleResult.

        相关联的安全组ID

        :return: The parent_group_id of this NovaCreateSecurityGroupRuleResult.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """Sets the parent_group_id of this NovaCreateSecurityGroupRuleResult.

        相关联的安全组ID

        :param parent_group_id: The parent_group_id of this NovaCreateSecurityGroupRuleResult.
        :type: str
        """
        self._parent_group_id = parent_group_id

    @property
    def to_port(self):
        """Gets the to_port of this NovaCreateSecurityGroupRuleResult.

        终止端口，范围1-65535。当协议类型为icmp时，to_port为icmp协议的code，范围是0-255。如果from_port为-1，且to_port为-1时，表示任意ICMP报文。

        :return: The to_port of this NovaCreateSecurityGroupRuleResult.
        :rtype: int
        """
        return self._to_port

    @to_port.setter
    def to_port(self, to_port):
        """Sets the to_port of this NovaCreateSecurityGroupRuleResult.

        终止端口，范围1-65535。当协议类型为icmp时，to_port为icmp协议的code，范围是0-255。如果from_port为-1，且to_port为-1时，表示任意ICMP报文。

        :param to_port: The to_port of this NovaCreateSecurityGroupRuleResult.
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
        if not isinstance(other, NovaCreateSecurityGroupRuleResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
