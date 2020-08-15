# coding: utf-8

import pprint
import re

import six





class InstanceUpdateParam:


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
        'display_name': 'str',
        'refresh_interval': 'str'
    }

    attribute_map = {
        'description': 'description',
        'display_name': 'display_name',
        'refresh_interval': 'refresh_interval'
    }

    def __init__(self, description=None, display_name=None, refresh_interval=None):
        """InstanceUpdateParam - a model defined in huaweicloud sdk"""
        
        

        self._description = None
        self._display_name = None
        self._refresh_interval = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.display_name = display_name
        self.refresh_interval = refresh_interval

    @property
    def description(self):
        """Gets the description of this InstanceUpdateParam.

        描述

        :return: The description of this InstanceUpdateParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstanceUpdateParam.

        描述

        :param description: The description of this InstanceUpdateParam.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this InstanceUpdateParam.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :return: The display_name of this InstanceUpdateParam.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InstanceUpdateParam.

        实例名。 可以输入中文、数字、字母、下划线、点、破折号。长度介于3-100之间

        :param display_name: The display_name of this InstanceUpdateParam.
        :type: str
        """
        self._display_name = display_name

    @property
    def refresh_interval(self):
        """Gets the refresh_interval of this InstanceUpdateParam.

        实例的生命周期 arm架构,生命周期只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例在到达生命周期后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止。

        :return: The refresh_interval of this InstanceUpdateParam.
        :rtype: str
        """
        return self._refresh_interval

    @refresh_interval.setter
    def refresh_interval(self, refresh_interval):
        """Sets the refresh_interval of this InstanceUpdateParam.

        实例的生命周期 arm架构,生命周期只能设置成30，60。x86架构可取值为30，60，240，1440和-1。除-1外，其它值的单位为“分钟”。实例在到达生命周期后，将会被暂停（已保存的数据不会被删除）。-1表示实例不会自动停止。

        :param refresh_interval: The refresh_interval of this InstanceUpdateParam.
        :type: str
        """
        self._refresh_interval = refresh_interval

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
        if not isinstance(other, InstanceUpdateParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
