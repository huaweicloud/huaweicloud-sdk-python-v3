# coding: utf-8

import pprint
import re

import six





class BillingUpdate:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'consistent_level': 'str',
        'size': 'int'
    }

    attribute_map = {
        'consistent_level': 'consistent_level',
        'size': 'size'
    }

    def __init__(self, consistent_level=None, size=None):
        """BillingUpdate - a model defined in huaweicloud sdk"""
        
        

        self._consistent_level = None
        self._size = None
        self.discriminator = None

        if consistent_level is not None:
            self.consistent_level = consistent_level
        if size is not None:
            self.size = size

    @property
    def consistent_level(self):
        """Gets the consistent_level of this BillingUpdate.

        存储库规格

        :return: The consistent_level of this BillingUpdate.
        :rtype: str
        """
        return self._consistent_level

    @consistent_level.setter
    def consistent_level(self, consistent_level):
        """Sets the consistent_level of this BillingUpdate.

        存储库规格

        :param consistent_level: The consistent_level of this BillingUpdate.
        :type: str
        """
        self._consistent_level = consistent_level

    @property
    def size(self):
        """Gets the size of this BillingUpdate.

        存储库大小，单位为GB

        :return: The size of this BillingUpdate.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BillingUpdate.

        存储库大小，单位为GB

        :param size: The size of this BillingUpdate.
        :type: int
        """
        self._size = size

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
        if not isinstance(other, BillingUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
