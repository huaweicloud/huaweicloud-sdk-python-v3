# coding: utf-8

import pprint
import re

import six





class SourceStorage:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'location': 'str',
        'parameters': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'location': 'location',
        'parameters': 'parameters',
        'type': 'type'
    }

    def __init__(self, location=None, parameters=None, type=None):
        """SourceStorage - a model defined in huaweicloud sdk"""
        
        

        self._location = None
        self._parameters = None
        self._type = None
        self.discriminator = None

        if location is not None:
            self.location = location
        if parameters is not None:
            self.parameters = parameters
        if type is not None:
            self.type = type

    @property
    def location(self):
        """Gets the location of this SourceStorage.

        位置

        :return: The location of this SourceStorage.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SourceStorage.

        位置

        :param location: The location of this SourceStorage.
        :type: str
        """
        self._location = location

    @property
    def parameters(self):
        """Gets the parameters of this SourceStorage.

        参数值

        :return: The parameters of this SourceStorage.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this SourceStorage.

        参数值

        :param parameters: The parameters of this SourceStorage.
        :type: dict(str, str)
        """
        self._parameters = parameters

    @property
    def type(self):
        """Gets the type of this SourceStorage.

        类型

        :return: The type of this SourceStorage.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SourceStorage.

        类型

        :param type: The type of this SourceStorage.
        :type: str
        """
        self._type = type

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
        if not isinstance(other, SourceStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
