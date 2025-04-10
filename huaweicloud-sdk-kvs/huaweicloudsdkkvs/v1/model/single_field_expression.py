# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SingleFieldExpression:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field': 'str',
        'func': 'str',
        'value': 'dict',
        'value_array': 'list[dict]'
    }

    attribute_map = {
        'field': 'field',
        'func': 'func',
        'value': 'value',
        'value_array': 'value_array'
    }

    def __init__(self, field=None, func=None, value=None, value_array=None):
        r"""SingleFieldExpression

        The model defined in huaweicloud sdk

        :param field: 条件字段。
        :type field: str
        :param func: 条件函数，取值如\&quot;$gt\&quot;, $lt\&quot;,\&quot;$gte\&quot;, $lte\&quot; \&quot;$eq\&quot;, \&quot;$ne\&quot;, \&quot;$prefix\&quot;, \&quot;$exists\&quot;。
        :type func: str
        :param value: value和value_array二选一。 - value条件值，适用于除\&quot;$in\&quot;, \&quot;$nin\&quot;外的func。 - 字段名无意义，可以传空，也可以传字段名。 - $exists值为true/false。 &gt; $prefix操作只适用于string和binary类型。
        :type value: dict
        :param value_array: \&quot;value\&quot;和\&quot;value_array\&quot;二选一。 - \&quot;value_array\&quot; 条件值列表, 值用于\&quot;$in\&quot;, \&quot;$nin\&quot;。
        :type value_array: list[dict]
        """
        
        

        self._field = None
        self._func = None
        self._value = None
        self._value_array = None
        self.discriminator = None

        self.field = field
        self.func = func
        if value is not None:
            self.value = value
        if value_array is not None:
            self.value_array = value_array

    @property
    def field(self):
        r"""Gets the field of this SingleFieldExpression.

        条件字段。

        :return: The field of this SingleFieldExpression.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this SingleFieldExpression.

        条件字段。

        :param field: The field of this SingleFieldExpression.
        :type field: str
        """
        self._field = field

    @property
    def func(self):
        r"""Gets the func of this SingleFieldExpression.

        条件函数，取值如\"$gt\", $lt\",\"$gte\", $lte\" \"$eq\", \"$ne\", \"$prefix\", \"$exists\"。

        :return: The func of this SingleFieldExpression.
        :rtype: str
        """
        return self._func

    @func.setter
    def func(self, func):
        r"""Sets the func of this SingleFieldExpression.

        条件函数，取值如\"$gt\", $lt\",\"$gte\", $lte\" \"$eq\", \"$ne\", \"$prefix\", \"$exists\"。

        :param func: The func of this SingleFieldExpression.
        :type func: str
        """
        self._func = func

    @property
    def value(self):
        r"""Gets the value of this SingleFieldExpression.

        value和value_array二选一。 - value条件值，适用于除\"$in\", \"$nin\"外的func。 - 字段名无意义，可以传空，也可以传字段名。 - $exists值为true/false。 > $prefix操作只适用于string和binary类型。

        :return: The value of this SingleFieldExpression.
        :rtype: dict
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this SingleFieldExpression.

        value和value_array二选一。 - value条件值，适用于除\"$in\", \"$nin\"外的func。 - 字段名无意义，可以传空，也可以传字段名。 - $exists值为true/false。 > $prefix操作只适用于string和binary类型。

        :param value: The value of this SingleFieldExpression.
        :type value: dict
        """
        self._value = value

    @property
    def value_array(self):
        r"""Gets the value_array of this SingleFieldExpression.

        \"value\"和\"value_array\"二选一。 - \"value_array\" 条件值列表, 值用于\"$in\", \"$nin\"。

        :return: The value_array of this SingleFieldExpression.
        :rtype: list[dict]
        """
        return self._value_array

    @value_array.setter
    def value_array(self, value_array):
        r"""Sets the value_array of this SingleFieldExpression.

        \"value\"和\"value_array\"二选一。 - \"value_array\" 条件值列表, 值用于\"$in\", \"$nin\"。

        :param value_array: The value_array of this SingleFieldExpression.
        :type value_array: list[dict]
        """
        self._value_array = value_array

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
        if not isinstance(other, SingleFieldExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
