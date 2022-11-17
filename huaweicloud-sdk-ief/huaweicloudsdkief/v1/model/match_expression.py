# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MatchExpression:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'operator': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'key': 'key',
        'operator': 'operator',
        'values': 'values'
    }

    def __init__(self, key=None, operator=None, values=None):
        """MatchExpression

        The model defined in huaweicloud sdk

        :param key: 规则的标签
        :type key: str
        :param operator: 操作符，取值如下： - In：标签值需要在values的列表中 - NotIn：标签的值不在某个列表中 - Exists：某个标签存在 - DoesNotExist：某个标签不存在 - Gt：标签的值大于某个值（字符串比较） - Lt：标签的值小于某个值（字符串比较）
        :type operator: str
        :param values: 一组标签值。 - 如果运算符为In或NotIn，则值数组必须非空。 - 如果运算符为Exists 或DoesNotExist，则值数组必须为空。 - 如果运算符是Gt或Lt，则值数组必须具有单个元素，该元素将被解释为整数。
        :type values: list[str]
        """
        
        

        self._key = None
        self._operator = None
        self._values = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if operator is not None:
            self.operator = operator
        if values is not None:
            self.values = values

    @property
    def key(self):
        """Gets the key of this MatchExpression.

        规则的标签

        :return: The key of this MatchExpression.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MatchExpression.

        规则的标签

        :param key: The key of this MatchExpression.
        :type key: str
        """
        self._key = key

    @property
    def operator(self):
        """Gets the operator of this MatchExpression.

        操作符，取值如下： - In：标签值需要在values的列表中 - NotIn：标签的值不在某个列表中 - Exists：某个标签存在 - DoesNotExist：某个标签不存在 - Gt：标签的值大于某个值（字符串比较） - Lt：标签的值小于某个值（字符串比较）

        :return: The operator of this MatchExpression.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this MatchExpression.

        操作符，取值如下： - In：标签值需要在values的列表中 - NotIn：标签的值不在某个列表中 - Exists：某个标签存在 - DoesNotExist：某个标签不存在 - Gt：标签的值大于某个值（字符串比较） - Lt：标签的值小于某个值（字符串比较）

        :param operator: The operator of this MatchExpression.
        :type operator: str
        """
        self._operator = operator

    @property
    def values(self):
        """Gets the values of this MatchExpression.

        一组标签值。 - 如果运算符为In或NotIn，则值数组必须非空。 - 如果运算符为Exists 或DoesNotExist，则值数组必须为空。 - 如果运算符是Gt或Lt，则值数组必须具有单个元素，该元素将被解释为整数。

        :return: The values of this MatchExpression.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this MatchExpression.

        一组标签值。 - 如果运算符为In或NotIn，则值数组必须非空。 - 如果运算符为Exists 或DoesNotExist，则值数组必须为空。 - 如果运算符是Gt或Lt，则值数组必须具有单个元素，该元素将被解释为整数。

        :param values: The values of this MatchExpression.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, MatchExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
