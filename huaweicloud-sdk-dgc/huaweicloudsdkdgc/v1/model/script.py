# coding: utf-8

import pprint
import re

import six





class Script:


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
        'path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path'
    }

    def __init__(self, name=None, path=None):
        """Script - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._path = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if path is not None:
            self.path = path

    @property
    def name(self):
        """Gets the name of this Script.


        :return: The name of this Script.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Script.


        :param name: The name of this Script.
        :type: str
        """
        self._name = name

    @property
    def path(self):
        """Gets the path of this Script.


        :return: The path of this Script.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Script.


        :param path: The path of this Script.
        :type: str
        """
        self._path = path

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
        if not isinstance(other, Script):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
