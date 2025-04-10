# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PropertyFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'operator': 'str',
        'value': 'str',
        'in_values': 'list[str]',
        'strategy': 'Strategy'
    }

    attribute_map = {
        'path': 'path',
        'operator': 'operator',
        'value': 'value',
        'in_values': 'in_values',
        'strategy': 'strategy'
    }

    def __init__(self, path=None, operator=None, value=None, in_values=None, strategy=None):
        r"""PropertyFilter

        The model defined in huaweicloud sdk

        :param path: **参数说明**：设备属性的路径信息，格式：service_id/DataProperty，例如门磁状态为“DoorWindow/status”。
        :type path: str
        :param operator: **参数说明**：数据比较的操作符。 **取值范围**：当前支持的操作符有：&gt;，&lt;，&gt;&#x3D;，&lt;&#x3D;，&#x3D;，in:表示在指定值中匹配和between:表示数值区间。
        :type operator: str
        :param value: **参数说明**：数据比较表达式的右值。与数据比较操作符between联用时，右值表示最小值和最大值，用逗号隔开，如“20,30”表示大于等于20小于30。
        :type value: str
        :param in_values: **参数说明**：当operator为in时该字段必填，使用该字段传递比较表达式右值，上限为20个。
        :type in_values: list[str]
        :param strategy: 
        :type strategy: :class:`huaweicloudsdkiotda.v5.Strategy`
        """
        
        

        self._path = None
        self._operator = None
        self._value = None
        self._in_values = None
        self._strategy = None
        self.discriminator = None

        self.path = path
        self.operator = operator
        if value is not None:
            self.value = value
        if in_values is not None:
            self.in_values = in_values
        if strategy is not None:
            self.strategy = strategy

    @property
    def path(self):
        r"""Gets the path of this PropertyFilter.

        **参数说明**：设备属性的路径信息，格式：service_id/DataProperty，例如门磁状态为“DoorWindow/status”。

        :return: The path of this PropertyFilter.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this PropertyFilter.

        **参数说明**：设备属性的路径信息，格式：service_id/DataProperty，例如门磁状态为“DoorWindow/status”。

        :param path: The path of this PropertyFilter.
        :type path: str
        """
        self._path = path

    @property
    def operator(self):
        r"""Gets the operator of this PropertyFilter.

        **参数说明**：数据比较的操作符。 **取值范围**：当前支持的操作符有：>，<，>=，<=，=，in:表示在指定值中匹配和between:表示数值区间。

        :return: The operator of this PropertyFilter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this PropertyFilter.

        **参数说明**：数据比较的操作符。 **取值范围**：当前支持的操作符有：>，<，>=，<=，=，in:表示在指定值中匹配和between:表示数值区间。

        :param operator: The operator of this PropertyFilter.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        r"""Gets the value of this PropertyFilter.

        **参数说明**：数据比较表达式的右值。与数据比较操作符between联用时，右值表示最小值和最大值，用逗号隔开，如“20,30”表示大于等于20小于30。

        :return: The value of this PropertyFilter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this PropertyFilter.

        **参数说明**：数据比较表达式的右值。与数据比较操作符between联用时，右值表示最小值和最大值，用逗号隔开，如“20,30”表示大于等于20小于30。

        :param value: The value of this PropertyFilter.
        :type value: str
        """
        self._value = value

    @property
    def in_values(self):
        r"""Gets the in_values of this PropertyFilter.

        **参数说明**：当operator为in时该字段必填，使用该字段传递比较表达式右值，上限为20个。

        :return: The in_values of this PropertyFilter.
        :rtype: list[str]
        """
        return self._in_values

    @in_values.setter
    def in_values(self, in_values):
        r"""Sets the in_values of this PropertyFilter.

        **参数说明**：当operator为in时该字段必填，使用该字段传递比较表达式右值，上限为20个。

        :param in_values: The in_values of this PropertyFilter.
        :type in_values: list[str]
        """
        self._in_values = in_values

    @property
    def strategy(self):
        r"""Gets the strategy of this PropertyFilter.

        :return: The strategy of this PropertyFilter.
        :rtype: :class:`huaweicloudsdkiotda.v5.Strategy`
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this PropertyFilter.

        :param strategy: The strategy of this PropertyFilter.
        :type strategy: :class:`huaweicloudsdkiotda.v5.Strategy`
        """
        self._strategy = strategy

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
        if not isinstance(other, PropertyFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
