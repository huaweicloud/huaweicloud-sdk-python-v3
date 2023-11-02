# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataobjectSearchConditionData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filed': 'str',
        'expression': 'str',
        'value': 'str'
    }

    attribute_map = {
        'filed': 'filed',
        'expression': 'expression',
        'value': 'value'
    }

    def __init__(self, filed=None, expression=None, value=None):
        """DataobjectSearchConditionData

        The model defined in huaweicloud sdk

        :param filed: 字段
        :type filed: str
        :param expression: 逻辑表达式
        :type expression: str
        :param value: 字段值
        :type value: str
        """
        
        

        self._filed = None
        self._expression = None
        self._value = None
        self.discriminator = None

        if filed is not None:
            self.filed = filed
        if expression is not None:
            self.expression = expression
        if value is not None:
            self.value = value

    @property
    def filed(self):
        """Gets the filed of this DataobjectSearchConditionData.

        字段

        :return: The filed of this DataobjectSearchConditionData.
        :rtype: str
        """
        return self._filed

    @filed.setter
    def filed(self, filed):
        """Sets the filed of this DataobjectSearchConditionData.

        字段

        :param filed: The filed of this DataobjectSearchConditionData.
        :type filed: str
        """
        self._filed = filed

    @property
    def expression(self):
        """Gets the expression of this DataobjectSearchConditionData.

        逻辑表达式

        :return: The expression of this DataobjectSearchConditionData.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this DataobjectSearchConditionData.

        逻辑表达式

        :param expression: The expression of this DataobjectSearchConditionData.
        :type expression: str
        """
        self._expression = expression

    @property
    def value(self):
        """Gets the value of this DataobjectSearchConditionData.

        字段值

        :return: The value of this DataobjectSearchConditionData.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DataobjectSearchConditionData.

        字段值

        :param value: The value of this DataobjectSearchConditionData.
        :type value: str
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
        if not isinstance(other, DataobjectSearchConditionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
