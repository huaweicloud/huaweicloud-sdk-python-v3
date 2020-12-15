# coding: utf-8

import pprint
import re

import six





class Taint:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'effect': 'str',
        'key': 'str',
        'value': 'str'
    }

    attribute_map = {
        'effect': 'effect',
        'key': 'key',
        'value': 'value'
    }

    def __init__(self, effect=None, key=None, value=None):
        """Taint - a model defined in huaweicloud sdk"""
        
        

        self._effect = None
        self._key = None
        self._value = None
        self.discriminator = None

        if effect is not None:
            self.effect = effect
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value

    @property
    def effect(self):
        """Gets the effect of this Taint.

        作用效果

        :return: The effect of this Taint.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this Taint.

        作用效果

        :param effect: The effect of this Taint.
        :type: str
        """
        self._effect = effect

    @property
    def key(self):
        """Gets the key of this Taint.

        键

        :return: The key of this Taint.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Taint.

        键

        :param key: The key of this Taint.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this Taint.

        值

        :return: The value of this Taint.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Taint.

        值

        :param value: The value of this Taint.
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
        if not isinstance(other, Taint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
