# coding: utf-8

import pprint
import re

import six





class RulesRemote:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'any_one_of': 'list[str]',
        'not_any_of': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'any_one_of': 'any_one_of',
        'not_any_of': 'not_any_of'
    }

    def __init__(self, type=None, any_one_of=None, not_any_of=None):
        """RulesRemote - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._any_one_of = None
        self._not_any_of = None
        self.discriminator = None

        self.type = type
        if any_one_of is not None:
            self.any_one_of = any_one_of
        if not_any_of is not None:
            self.not_any_of = not_any_of

    @property
    def type(self):
        """Gets the type of this RulesRemote.

        表示IdP断言中的属性。

        :return: The type of this RulesRemote.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RulesRemote.

        表示IdP断言中的属性。

        :param type: The type of this RulesRemote.
        :type: str
        """
        self._type = type

    @property
    def any_one_of(self):
        """Gets the any_one_of of this RulesRemote.

        输入属性值中包含指定值才生效，并返回布尔值，返回值不能用于local块中的占位符。在同一个remote数组元素中，any_one_of与not_any_of互斥，两者至多填写一个，不能同时填写。

        :return: The any_one_of of this RulesRemote.
        :rtype: list[str]
        """
        return self._any_one_of

    @any_one_of.setter
    def any_one_of(self, any_one_of):
        """Sets the any_one_of of this RulesRemote.

        输入属性值中包含指定值才生效，并返回布尔值，返回值不能用于local块中的占位符。在同一个remote数组元素中，any_one_of与not_any_of互斥，两者至多填写一个，不能同时填写。

        :param any_one_of: The any_one_of of this RulesRemote.
        :type: list[str]
        """
        self._any_one_of = any_one_of

    @property
    def not_any_of(self):
        """Gets the not_any_of of this RulesRemote.

        输入属性值中不包含指定值才生效，并返回布尔值，返回值不能用于local块中的占位符。在同一个remote数组元素中，any_one_of与not_any_of互斥，两者至多填写一个，不能同时填写。

        :return: The not_any_of of this RulesRemote.
        :rtype: list[str]
        """
        return self._not_any_of

    @not_any_of.setter
    def not_any_of(self, not_any_of):
        """Sets the not_any_of of this RulesRemote.

        输入属性值中不包含指定值才生效，并返回布尔值，返回值不能用于local块中的占位符。在同一个remote数组元素中，any_one_of与not_any_of互斥，两者至多填写一个，不能同时填写。

        :param not_any_of: The not_any_of of this RulesRemote.
        :type: list[str]
        """
        self._not_any_of = not_any_of

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
        if not isinstance(other, RulesRemote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
