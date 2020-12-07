# coding: utf-8

import pprint
import re

import six





class UpdateTopicAttributeRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'value': 'str'
    }

    attribute_map = {
        'value': 'value'
    }

    def __init__(self, value=None):
        """UpdateTopicAttributeRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._value = None
        self.discriminator = None

        self.value = value

    @property
    def value(self):
        """Gets the value of this UpdateTopicAttributeRequestBody.

        1. 当请求参数name为access_policy时，value为Topic属性值，最大支持30KB。  2. 当请求参数name为introduction时，value为topic简介，最大长度120B。

        :return: The value of this UpdateTopicAttributeRequestBody.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdateTopicAttributeRequestBody.

        1. 当请求参数name为access_policy时，value为Topic属性值，最大支持30KB。  2. 当请求参数name为introduction时，value为topic简介，最大长度120B。

        :param value: The value of this UpdateTopicAttributeRequestBody.
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
        if not isinstance(other, UpdateTopicAttributeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
