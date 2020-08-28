# coding: utf-8

import pprint
import re

import six





class StartPipelineBuildParams:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):
        """StartPipelineBuildParams - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._value = None
        self.discriminator = None

        self.name = name
        self.value = value

    @property
    def name(self):
        """Gets the name of this StartPipelineBuildParams.

        构建参数名

        :return: The name of this StartPipelineBuildParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StartPipelineBuildParams.

        构建参数名

        :param name: The name of this StartPipelineBuildParams.
        :type: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this StartPipelineBuildParams.

        构建参数值，最大长度为8192

        :return: The value of this StartPipelineBuildParams.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StartPipelineBuildParams.

        构建参数值，最大长度为8192

        :param value: The value of this StartPipelineBuildParams.
        :type: str
        """
        self._value = value

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
        if not isinstance(other, StartPipelineBuildParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
