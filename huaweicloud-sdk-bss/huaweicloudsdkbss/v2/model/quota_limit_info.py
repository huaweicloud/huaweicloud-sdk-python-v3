# coding: utf-8

import pprint
import re

import six





class QuotaLimitInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit_key': 'str',
        'limit_values': 'list[LimitValue]'
    }

    attribute_map = {
        'limit_key': 'limit_key',
        'limit_values': 'limit_values'
    }

    def __init__(self, limit_key=None, limit_values=None):
        """QuotaLimitInfo - a model defined in huaweicloud sdk"""
        
        

        self._limit_key = None
        self._limit_values = None
        self.discriminator = None

        if limit_key is not None:
            self.limit_key = limit_key
        if limit_values is not None:
            self.limit_values = limit_values

    @property
    def limit_key(self):
        """Gets the limit_key of this QuotaLimitInfo.

        |参数名称：属性key值| |参数约束及描述：属性key值|

        :return: The limit_key of this QuotaLimitInfo.
        :rtype: str
        """
        return self._limit_key

    @limit_key.setter
    def limit_key(self, limit_key):
        """Sets the limit_key of this QuotaLimitInfo.

        |参数名称：属性key值| |参数约束及描述：属性key值|

        :param limit_key: The limit_key of this QuotaLimitInfo.
        :type: str
        """
        self._limit_key = limit_key

    @property
    def limit_values(self):
        """Gets the limit_values of this QuotaLimitInfo.

        |参数名称：属性值| |参数约束以及描述：属性值|

        :return: The limit_values of this QuotaLimitInfo.
        :rtype: list[LimitValue]
        """
        return self._limit_values

    @limit_values.setter
    def limit_values(self, limit_values):
        """Sets the limit_values of this QuotaLimitInfo.

        |参数名称：属性值| |参数约束以及描述：属性值|

        :param limit_values: The limit_values of this QuotaLimitInfo.
        :type: list[LimitValue]
        """
        self._limit_values = limit_values

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
        if not isinstance(other, QuotaLimitInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
