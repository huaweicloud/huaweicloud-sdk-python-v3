# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionsFilterPolicy:

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
        'string_equals': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'string_equals': 'string_equals'
    }

    def __init__(self, name=None, string_equals=None):
        r"""SubscriptionsFilterPolicy

        The model defined in huaweicloud sdk

        :param name: 过滤策略名称。 包含小写英文字母([a-z])、数字([0-9])、下划线(_)，下划线不得开始、结尾或连续出现），长度限制{1,32}，不能是smn_开头。
        :type name: str
        :param string_equals: 字符串精确匹配数组。数组长度[1, 10]，数组内容不能重复，值不能为null或者空字符串“ ”，长度限制[1,32]，中英文、数字、下划线
        :type string_equals: list[str]
        """
        
        

        self._name = None
        self._string_equals = None
        self.discriminator = None

        self.name = name
        self.string_equals = string_equals

    @property
    def name(self):
        r"""Gets the name of this SubscriptionsFilterPolicy.

        过滤策略名称。 包含小写英文字母([a-z])、数字([0-9])、下划线(_)，下划线不得开始、结尾或连续出现），长度限制{1,32}，不能是smn_开头。

        :return: The name of this SubscriptionsFilterPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubscriptionsFilterPolicy.

        过滤策略名称。 包含小写英文字母([a-z])、数字([0-9])、下划线(_)，下划线不得开始、结尾或连续出现），长度限制{1,32}，不能是smn_开头。

        :param name: The name of this SubscriptionsFilterPolicy.
        :type name: str
        """
        self._name = name

    @property
    def string_equals(self):
        r"""Gets the string_equals of this SubscriptionsFilterPolicy.

        字符串精确匹配数组。数组长度[1, 10]，数组内容不能重复，值不能为null或者空字符串“ ”，长度限制[1,32]，中英文、数字、下划线

        :return: The string_equals of this SubscriptionsFilterPolicy.
        :rtype: list[str]
        """
        return self._string_equals

    @string_equals.setter
    def string_equals(self, string_equals):
        r"""Sets the string_equals of this SubscriptionsFilterPolicy.

        字符串精确匹配数组。数组长度[1, 10]，数组内容不能重复，值不能为null或者空字符串“ ”，长度限制[1,32]，中英文、数字、下划线

        :param string_equals: The string_equals of this SubscriptionsFilterPolicy.
        :type string_equals: list[str]
        """
        self._string_equals = string_equals

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SubscriptionsFilterPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
