# coding: utf-8

import pprint
import re

import six


class BatchAddServerNicOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'subnet_id': 'str',
        'security_groups': 'list[ServerNicSecurityGroup]',
        'ip_address': 'str'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'security_groups': 'security_groups',
        'ip_address': 'ip_address'
    }

    def __init__(self, subnet_id=None, security_groups=None, ip_address=None):  # noqa: E501
        """BatchAddServerNicOption - a model defined in huaweicloud sdk"""

        self._subnet_id = None
        self._security_groups = None
        self._ip_address = None
        self.discriminator = None

        self.subnet_id = subnet_id
        if security_groups is not None:
            self.security_groups = security_groups
        if ip_address is not None:
            self.ip_address = ip_address

    @property
    def subnet_id(self):
        """Gets the subnet_id of this BatchAddServerNicOption.

        云服务器添加网卡的信息。  需要指定云服务器所属虚拟私有云下已创建的网络（network）的ID，UUID格式。

        :return: The subnet_id of this BatchAddServerNicOption.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this BatchAddServerNicOption.

        云服务器添加网卡的信息。  需要指定云服务器所属虚拟私有云下已创建的网络（network）的ID，UUID格式。

        :param subnet_id: The subnet_id of this BatchAddServerNicOption.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_groups(self):
        """Gets the security_groups of this BatchAddServerNicOption.

        添加网卡的安全组信息

        :return: The security_groups of this BatchAddServerNicOption.
        :rtype: list[ServerNicSecurityGroup]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this BatchAddServerNicOption.

        添加网卡的安全组信息

        :param security_groups: The security_groups of this BatchAddServerNicOption.
        :type: list[ServerNicSecurityGroup]
        """
        self._security_groups = security_groups

    @property
    def ip_address(self):
        """Gets the ip_address of this BatchAddServerNicOption.

        IP地址，无该参数表示自动分配IP地址。

        :return: The ip_address of this BatchAddServerNicOption.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this BatchAddServerNicOption.

        IP地址，无该参数表示自动分配IP地址。

        :param ip_address: The ip_address of this BatchAddServerNicOption.
        :type: str
        """
        self._ip_address = ip_address

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
        if not isinstance(other, BatchAddServerNicOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
