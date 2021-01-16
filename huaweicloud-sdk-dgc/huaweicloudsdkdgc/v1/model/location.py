# coding: utf-8

import pprint
import re

import six





class Location:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x': 'int',
        'y': 'int'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y'
    }

    def __init__(self, x=None, y=None):
        """Location - a model defined in huaweicloud sdk"""
        
        

        self._x = None
        self._y = None
        self.discriminator = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @property
    def x(self):
        """Gets the x of this Location.


        :return: The x of this Location.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this Location.


        :param x: The x of this Location.
        :type: int
        """
        self._x = x

    @property
    def y(self):
        """Gets the y of this Location.


        :return: The y of this Location.
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this Location.


        :param y: The y of this Location.
        :type: int
        """
        self._y = y

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
        if not isinstance(other, Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
