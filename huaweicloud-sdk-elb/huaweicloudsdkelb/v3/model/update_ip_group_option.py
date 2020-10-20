# coding: utf-8

import pprint
import re

import six





class UpdateIpGroupOption:


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
        'name': 'str',
        'ip_list': 'list[UpadateIpGroupIpOption]'
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'ip_list': 'ip_list'
    }

    def __init__(self, description=None, name=None, ip_list=None):
        """UpdateIpGroupOption - a model defined in huaweicloud sdk"""
        
        

        self._description = None
        self._name = None
        self._ip_list = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if ip_list is not None:
            self.ip_list = ip_list

    @property
    def description(self):
        """Gets the description of this UpdateIpGroupOption.

        IP地址组的描述信息

        :return: The description of this UpdateIpGroupOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateIpGroupOption.

        IP地址组的描述信息

        :param description: The description of this UpdateIpGroupOption.
        :type: str
        """
        self._description = description

    @property
    def name(self):
        """Gets the name of this UpdateIpGroupOption.

        IP地址组的名称

        :return: The name of this UpdateIpGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateIpGroupOption.

        IP地址组的名称

        :param name: The name of this UpdateIpGroupOption.
        :type: str
        """
        self._name = name

    @property
    def ip_list(self):
        """Gets the ip_list of this UpdateIpGroupOption.

        IP地址组中包含的ip列表。

        :return: The ip_list of this UpdateIpGroupOption.
        :rtype: list[UpadateIpGroupIpOption]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        """Sets the ip_list of this UpdateIpGroupOption.

        IP地址组中包含的ip列表。

        :param ip_list: The ip_list of this UpdateIpGroupOption.
        :type: list[UpadateIpGroupIpOption]
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
        if not isinstance(other, UpdateIpGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
