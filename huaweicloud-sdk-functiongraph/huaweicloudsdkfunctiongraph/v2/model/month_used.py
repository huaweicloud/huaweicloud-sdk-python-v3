# coding: utf-8

import pprint
import re

import six





class MonthUsed:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'value': 'int'
    }

    attribute_map = {
        'date': 'date',
        'value': 'value'
    }

    def __init__(self, date=None, value=None):
        """MonthUsed - a model defined in huaweicloud sdk"""
        
        

        self._date = None
        self._value = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if value is not None:
            self.value = value

    @property
    def date(self):
        """Gets the date of this MonthUsed.

        日期

        :return: The date of this MonthUsed.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this MonthUsed.

        日期

        :param date: The date of this MonthUsed.
        :type: str
        """
        self._date = date

    @property
    def value(self):
        """Gets the value of this MonthUsed.

        使用量

        :return: The value of this MonthUsed.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MonthUsed.

        使用量

        :param value: The value of this MonthUsed.
        :type: int
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
        if not isinstance(other, MonthUsed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
