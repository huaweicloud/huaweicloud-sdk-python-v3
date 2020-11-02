# coding: utf-8

import pprint
import re

import six





class Condition:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'comparison_operator': 'str',
        'count': 'int',
        'filter': 'str',
        'period': 'int',
        'unit': 'str',
        'value': 'float'
    }

    attribute_map = {
        'comparison_operator': 'comparison_operator',
        'count': 'count',
        'filter': 'filter',
        'period': 'period',
        'unit': 'unit',
        'value': 'value'
    }

    def __init__(self, comparison_operator=None, count=None, filter=None, period=None, unit=None, value=None):
        """Condition - a model defined in huaweicloud sdk"""
        
        

        self._comparison_operator = None
        self._count = None
        self._filter = None
        self._period = None
        self._unit = None
        self._value = None
        self.discriminator = None

        self.comparison_operator = comparison_operator
        self.count = count
        self.filter = filter
        self.period = period
        if unit is not None:
            self.unit = unit
        self.value = value

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this Condition.

        告警阈值的比较条件，可以是>、=、<、>=、<=。

        :return: The comparison_operator of this Condition.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this Condition.

        告警阈值的比较条件，可以是>、=、<、>=、<=。

        :param comparison_operator: The comparison_operator of this Condition.
        :type: str
        """
        self._comparison_operator = comparison_operator

    @property
    def count(self):
        """Gets the count of this Condition.

        触发告警的连续发生次数，取值范围[1, 5]。

        :return: The count of this Condition.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Condition.

        触发告警的连续发生次数，取值范围[1, 5]。

        :param count: The count of this Condition.
        :type: int
        """
        self._count = count

    @property
    def filter(self):
        """Gets the filter of this Condition.

        数据聚合的方式，支持max、min、average、sum、variance，分别表示最大值、最小值、平均值、求和值、方差值。

        :return: The filter of this Condition.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Condition.

        数据聚合的方式，支持max、min、average、sum、variance，分别表示最大值、最小值、平均值、求和值、方差值。

        :param filter: The filter of this Condition.
        :type: str
        """
        self._filter = filter

    @property
    def period(self):
        """Gets the period of this Condition.

        告警条件判断周期，单位为秒，支持的值为1，300，1200，3600，14400，86400。说明：当period设置为1时，表示以原始的指标数据判断告警。当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为0。

        :return: The period of this Condition.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Condition.

        告警条件判断周期，单位为秒，支持的值为1，300，1200，3600，14400，86400。说明：当period设置为1时，表示以原始的指标数据判断告警。当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为0。

        :param period: The period of this Condition.
        :type: int
        """
        self._period = period

    @property
    def unit(self):
        """Gets the unit of this Condition.

        数据的单位，最大长度为32位。

        :return: The unit of this Condition.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Condition.

        数据的单位，最大长度为32位。

        :param unit: The unit of this Condition.
        :type: str
        """
        self._unit = unit

    @property
    def value(self):
        """Gets the value of this Condition.

        告警阈值，取值范围[0, Number.MAX_VALUE]，Number.MAX_VALUE值为1.7976931348623157e+108。具体阈值取值请参见附录中各服务监控指标中取值范围，如支持监控的服务列表中ECS的CPU使用率cpu_util取值范围可配置80。

        :return: The value of this Condition.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Condition.

        告警阈值，取值范围[0, Number.MAX_VALUE]，Number.MAX_VALUE值为1.7976931348623157e+108。具体阈值取值请参见附录中各服务监控指标中取值范围，如支持监控的服务列表中ECS的CPU使用率cpu_util取值范围可配置80。

        :param value: The value of this Condition.
        :type: float
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
        if not isinstance(other, Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
