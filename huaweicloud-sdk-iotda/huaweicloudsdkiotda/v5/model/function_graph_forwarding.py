# coding: utf-8

import pprint
import re

import six





class FunctionGraphForwarding:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'func_urn': 'str',
        'func_name': 'str'
    }

    attribute_map = {
        'func_urn': 'func_urn',
        'func_name': 'func_name'
    }

    def __init__(self, func_urn=None, func_name=None):
        """FunctionGraphForwarding - a model defined in huaweicloud sdk"""
        
        

        self._func_urn = None
        self._func_name = None
        self.discriminator = None

        self.func_urn = func_urn
        self.func_name = func_name

    @property
    def func_urn(self):
        """Gets the func_urn of this FunctionGraphForwarding.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :return: The func_urn of this FunctionGraphForwarding.
        :rtype: str
        """
        return self._func_urn

    @func_urn.setter
    def func_urn(self, func_urn):
        """Sets the func_urn of this FunctionGraphForwarding.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :param func_urn: The func_urn of this FunctionGraphForwarding.
        :type: str
        """
        self._func_urn = func_urn

    @property
    def func_name(self):
        """Gets the func_name of this FunctionGraphForwarding.

        函数名称。

        :return: The func_name of this FunctionGraphForwarding.
        :rtype: str
        """
        return self._func_name

    @func_name.setter
    def func_name(self, func_name):
        """Sets the func_name of this FunctionGraphForwarding.

        函数名称。

        :param func_name: The func_name of this FunctionGraphForwarding.
        :type: str
        """
        self._func_name = func_name

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
        if not isinstance(other, FunctionGraphForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
