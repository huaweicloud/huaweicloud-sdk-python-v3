# coding: utf-8

import pprint
import re

import six





class StrategyConfig:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'concurrency': 'int'
    }

    attribute_map = {
        'concurrency': 'concurrency'
    }

    def __init__(self, concurrency=None):
        """StrategyConfig - a model defined in huaweicloud sdk"""
        
        

        self._concurrency = None
        self.discriminator = None

        self.concurrency = concurrency

    @property
    def concurrency(self):
        """Gets the concurrency of this StrategyConfig.

        0：函数被禁用;-1：函数被启用。

        :return: The concurrency of this StrategyConfig.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this StrategyConfig.

        0：函数被禁用;-1：函数被启用。

        :param concurrency: The concurrency of this StrategyConfig.
        :type: int
        """
        self._concurrency = concurrency

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
        if not isinstance(other, StrategyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
