# coding: utf-8

import pprint
import re

import six





class ShowVersionAliasRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'name': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'name': 'name'
    }

    def __init__(self, function_urn=None, name=None):
        """ShowVersionAliasRequest - a model defined in huaweicloud sdk"""
        
        

        self._function_urn = None
        self._name = None
        self.discriminator = None

        self.function_urn = function_urn
        self.name = name

    @property
    def function_urn(self):
        """Gets the function_urn of this ShowVersionAliasRequest.


        :return: The function_urn of this ShowVersionAliasRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this ShowVersionAliasRequest.


        :param function_urn: The function_urn of this ShowVersionAliasRequest.
        :type: str
        """
        self._function_urn = function_urn

    @property
    def name(self):
        """Gets the name of this ShowVersionAliasRequest.


        :return: The name of this ShowVersionAliasRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowVersionAliasRequest.


        :param name: The name of this ShowVersionAliasRequest.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, ShowVersionAliasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
