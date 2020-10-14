# coding: utf-8

import pprint
import re

import six





class Whitelist:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'ip_list': 'list[str]'
    }

    attribute_map = {
        'group_name': 'group_name',
        'ip_list': 'ip_list'
    }

    def __init__(self, group_name=None, ip_list=None):
        """Whitelist - a model defined in huaweicloud sdk"""
        
        

        self._group_name = None
        self._ip_list = None
        self.discriminator = None

        self.group_name = group_name
        self.ip_list = ip_list

    @property
    def group_name(self):
        """Gets the group_name of this Whitelist.

        白名单分组名称，每个实例支持创建4个分组。

        :return: The group_name of this Whitelist.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this Whitelist.

        白名单分组名称，每个实例支持创建4个分组。

        :param group_name: The group_name of this Whitelist.
        :type: str
        """
        self._group_name = group_name

    @property
    def ip_list(self):
        """Gets the ip_list of this Whitelist.

        白名单分组下的IP列表,每个实例最多可以添加20个IP地址/地址段。如果有多个，可以用逗号分隔。不支持的IP和地址段：0.0.0.0和0.0.0.0/0

        :return: The ip_list of this Whitelist.
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this Whitelist.

        白名单分组下的IP列表,每个实例最多可以添加20个IP地址/地址段。如果有多个，可以用逗号分隔。不支持的IP和地址段：0.0.0.0和0.0.0.0/0

        :param ip_list: The ip_list of this Whitelist.
        :type: list[str]
        """
        self._ip_list = ip_list

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Whitelist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
