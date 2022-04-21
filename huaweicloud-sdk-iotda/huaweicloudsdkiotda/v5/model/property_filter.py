# coding: utf-8

import re
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
        'strategy': 'Strategy'
    }

    attribute_map = {
        'path': 'path',
        'operator': 'operator',
        'value': 'value',
        'strategy': 'strategy'
    }

    def __init__(self, path=None, operator=None, value=None, strategy=None):
        """PropertyFilter

        The model defined in huaweicloud sdk

        :param path: **参数说明**：设备属性的路径信息，格式：service_id/DataProperty，例如门磁状态为“DoorWindow/status”。多个属性路径之间以逗号分隔。
        :type path: str
        :param operator: **参数说明**：数据比较的操作符。 **取值范围**：当前支持的操作符有：&gt;，&lt;，&gt;&#x3D;，&lt;&#x3D;，&#x3D;和between:表示数值区间，geo.circle.in:表示圆形区域范围内，geo.circle.out:表示圆形区域范围外。
        :type operator: str
        :param value: **参数说明**：数据比较表达式的右值。与数据比较操作符between联用时，右值表示最小值和最大值，用逗号隔开，如“20,30”表示大于等于20小于30。
        :type value: str
        :param strategy: 
        :type strategy: :class:`huaweicloudsdkiotda.v5.Strategy`
        """
        
        

        self._path = None
        self._operator = None
        self._value = None
        self._strategy = None
        self.discriminator = None

        self.path = path
        self.operator = operator
        self.value = value
        if strategy is not None:
            self.strategy = strategy

    @property
    def path(self):
        """Gets the path of this PropertyFilter.

        **参数说明**：设备属性的路径信息，格式：service_id/DataProperty，例如门磁状态为“DoorWindow/status”。多个属性路径之间以逗号分隔。

        :return: The path of this PropertyFilter.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PropertyFilter.

        **参数说明**：设备属性的路径信息，格式：service_id/DataProperty，例如门磁状态为“DoorWindow/status”。多个属性路径之间以逗号分隔。

        :param path: The path of this PropertyFilter.
        :type path: str
        """
        self._path = path

    @property
    def operator(self):
        """Gets the operator of this PropertyFilter.

        **参数说明**：数据比较的操作符。 **取值范围**：当前支持的操作符有：>，<，>=，<=，=和between:表示数值区间，geo.circle.in:表示圆形区域范围内，geo.circle.out:表示圆形区域范围外。

        :return: The operator of this PropertyFilter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PropertyFilter.

        **参数说明**：数据比较的操作符。 **取值范围**：当前支持的操作符有：>，<，>=，<=，=和between:表示数值区间，geo.circle.in:表示圆形区域范围内，geo.circle.out:表示圆形区域范围外。

        :param operator: The operator of this PropertyFilter.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        """Gets the value of this PropertyFilter.

        **参数说明**：数据比较表达式的右值。与数据比较操作符between联用时，右值表示最小值和最大值，用逗号隔开，如“20,30”表示大于等于20小于30。

        :return: The value of this PropertyFilter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PropertyFilter.

        **参数说明**：数据比较表达式的右值。与数据比较操作符between联用时，右值表示最小值和最大值，用逗号隔开，如“20,30”表示大于等于20小于30。

        :param value: The value of this PropertyFilter.
        :type value: str
        """
        self._value = value

    @property
    def strategy(self):
        """Gets the strategy of this PropertyFilter.


        :return: The strategy of this PropertyFilter.
        :rtype: :class:`huaweicloudsdkiotda.v5.Strategy`
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this PropertyFilter.


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
