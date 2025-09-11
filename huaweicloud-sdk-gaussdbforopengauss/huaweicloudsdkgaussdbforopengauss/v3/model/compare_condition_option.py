# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareConditionOption:

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
        'enable_equal': 'bool',
        'min': 'int',
        'max': 'int',
        'value': 'int'
    }

    attribute_map = {
        'name': 'name',
        'enable_equal': 'enable_equal',
        'min': 'min',
        'max': 'max',
        'value': 'value'
    }

    def __init__(self, name=None, enable_equal=None, min=None, max=None, value=None):
        r"""CompareConditionOption

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 查询字段名称，当前仅支持特定的数值字段。 **约束限制**: 不涉及。 **取值范围**: - total_sql_time: 总SQL耗时。 - sql_time：SQL执行次数。  **默认取值**: 不涉及。
        :type name: str
        :param enable_equal: **参数解释**: 是否使能包含等于，如果为true，则表示包含边界条件（min或max）的取值。 **约束限制**: 不涉及。 **取值范围**: - true - false  **默认取值**: 不涉及。
        :type enable_equal: bool
        :param min: **参数解释**: 最小值判断条件对应取值（大于条件）。 **约束限制**: 不涉及。 **取值范围**: [0, 2^63-1] **默认取值**: 不涉及。
        :type min: int
        :param max: **参数解释**: 最大值判断条件对应取值（小于条件）。 **约束限制**: 不涉及。 **取值范围**: [0, 2^63-1] **默认取值**: 不涉及。
        :type max: int
        :param value: **参数解释**: 等值判断条件对应取值（等于条件）。value的优先级最高，如果value不为空，则忽略min和max的取值设置；value为空时，才使能min和max的条件过滤。 **约束限制**: 不涉及。 **取值范围**: [0, 2^63-1] **默认取值**: 不涉及。
        :type value: int
        """
        
        

        self._name = None
        self._enable_equal = None
        self._min = None
        self._max = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if enable_equal is not None:
            self.enable_equal = enable_equal
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if value is not None:
            self.value = value

    @property
    def name(self):
        r"""Gets the name of this CompareConditionOption.

        **参数解释**: 查询字段名称，当前仅支持特定的数值字段。 **约束限制**: 不涉及。 **取值范围**: - total_sql_time: 总SQL耗时。 - sql_time：SQL执行次数。  **默认取值**: 不涉及。

        :return: The name of this CompareConditionOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CompareConditionOption.

        **参数解释**: 查询字段名称，当前仅支持特定的数值字段。 **约束限制**: 不涉及。 **取值范围**: - total_sql_time: 总SQL耗时。 - sql_time：SQL执行次数。  **默认取值**: 不涉及。

        :param name: The name of this CompareConditionOption.
        :type name: str
        """
        self._name = name

    @property
    def enable_equal(self):
        r"""Gets the enable_equal of this CompareConditionOption.

        **参数解释**: 是否使能包含等于，如果为true，则表示包含边界条件（min或max）的取值。 **约束限制**: 不涉及。 **取值范围**: - true - false  **默认取值**: 不涉及。

        :return: The enable_equal of this CompareConditionOption.
        :rtype: bool
        """
        return self._enable_equal

    @enable_equal.setter
    def enable_equal(self, enable_equal):
        r"""Sets the enable_equal of this CompareConditionOption.

        **参数解释**: 是否使能包含等于，如果为true，则表示包含边界条件（min或max）的取值。 **约束限制**: 不涉及。 **取值范围**: - true - false  **默认取值**: 不涉及。

        :param enable_equal: The enable_equal of this CompareConditionOption.
        :type enable_equal: bool
        """
        self._enable_equal = enable_equal

    @property
    def min(self):
        r"""Gets the min of this CompareConditionOption.

        **参数解释**: 最小值判断条件对应取值（大于条件）。 **约束限制**: 不涉及。 **取值范围**: [0, 2^63-1] **默认取值**: 不涉及。

        :return: The min of this CompareConditionOption.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this CompareConditionOption.

        **参数解释**: 最小值判断条件对应取值（大于条件）。 **约束限制**: 不涉及。 **取值范围**: [0, 2^63-1] **默认取值**: 不涉及。

        :param min: The min of this CompareConditionOption.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this CompareConditionOption.

        **参数解释**: 最大值判断条件对应取值（小于条件）。 **约束限制**: 不涉及。 **取值范围**: [0, 2^63-1] **默认取值**: 不涉及。

        :return: The max of this CompareConditionOption.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this CompareConditionOption.

        **参数解释**: 最大值判断条件对应取值（小于条件）。 **约束限制**: 不涉及。 **取值范围**: [0, 2^63-1] **默认取值**: 不涉及。

        :param max: The max of this CompareConditionOption.
        :type max: int
        """
        self._max = max

    @property
    def value(self):
        r"""Gets the value of this CompareConditionOption.

        **参数解释**: 等值判断条件对应取值（等于条件）。value的优先级最高，如果value不为空，则忽略min和max的取值设置；value为空时，才使能min和max的条件过滤。 **约束限制**: 不涉及。 **取值范围**: [0, 2^63-1] **默认取值**: 不涉及。

        :return: The value of this CompareConditionOption.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CompareConditionOption.

        **参数解释**: 等值判断条件对应取值（等于条件）。value的优先级最高，如果value不为空，则忽略min和max的取值设置；value为空时，才使能min和max的条件过滤。 **约束限制**: 不涉及。 **取值范围**: [0, 2^63-1] **默认取值**: 不涉及。

        :param value: The value of this CompareConditionOption.
        :type value: int
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
        if not isinstance(other, CompareConditionOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
