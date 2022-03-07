# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Policy:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'period': 'int',
        'filter': 'str',
        'comparison_operator': 'str',
        'value': 'float',
        'unit': 'str',
        'count': 'int',
        'type': 'str',
        'suppress_duration': 'int',
        'level': 'int'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'period': 'period',
        'filter': 'filter',
        'comparison_operator': 'comparison_operator',
        'value': 'value',
        'unit': 'unit',
        'count': 'count',
        'type': 'type',
        'suppress_duration': 'suppress_duration',
        'level': 'level'
    }

    def __init__(self, metric_name=None, period=None, filter=None, comparison_operator=None, value=None, unit=None, count=None, type=None, suppress_duration=None, level=None):
        """Policy - a model defined in huaweicloud sdk"""
        
        

        self._metric_name = None
        self._period = None
        self._filter = None
        self._comparison_operator = None
        self._value = None
        self._unit = None
        self._count = None
        self._type = None
        self._suppress_duration = None
        self._level = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if period is not None:
            self.period = period
        if filter is not None:
            self.filter = filter
        if comparison_operator is not None:
            self.comparison_operator = comparison_operator
        if value is not None:
            self.value = value
        if unit is not None:
            self.unit = unit
        if count is not None:
            self.count = count
        if type is not None:
            self.type = type
        if suppress_duration is not None:
            self.suppress_duration = suppress_duration
        if level is not None:
            self.level = level

    @property
    def metric_name(self):
        """Gets the metric_name of this Policy.

        指标名称

        :return: The metric_name of this Policy.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this Policy.

        指标名称

        :param metric_name: The metric_name of this Policy.
        :type: str
        """
        self._metric_name = metric_name

    @property
    def period(self):
        """Gets the period of this Policy.

        周期

        :return: The period of this Policy.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Policy.

        周期

        :param period: The period of this Policy.
        :type: int
        """
        self._period = period

    @property
    def filter(self):
        """Gets the filter of this Policy.

        聚合方式

        :return: The filter of this Policy.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Policy.

        聚合方式

        :param filter: The filter of this Policy.
        :type: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this Policy.

        阈值符号

        :return: The comparison_operator of this Policy.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this Policy.

        阈值符号

        :param comparison_operator: The comparison_operator of this Policy.
        :type: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        """Gets the value of this Policy.

        阈值

        :return: The value of this Policy.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Policy.

        阈值

        :param value: The value of this Policy.
        :type: float
        """
        self._value = value

    @property
    def unit(self):
        """Gets the unit of this Policy.

        单位

        :return: The unit of this Policy.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Policy.

        单位

        :param unit: The unit of this Policy.
        :type: str
        """
        self._unit = unit

    @property
    def count(self):
        """Gets the count of this Policy.

        次数

        :return: The count of this Policy.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Policy.

        次数

        :param count: The count of this Policy.
        :type: int
        """
        self._count = count

    @property
    def type(self):
        """Gets the type of this Policy.

        类型

        :return: The type of this Policy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Policy.

        类型

        :param type: The type of this Policy.
        :type: str
        """
        self._type = type

    @property
    def suppress_duration(self):
        """Gets the suppress_duration of this Policy.

        抑制方式

        :return: The suppress_duration of this Policy.
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        """Sets the suppress_duration of this Policy.

        抑制方式

        :param suppress_duration: The suppress_duration of this Policy.
        :type: int
        """
        self._suppress_duration = suppress_duration

    @property
    def level(self):
        """Gets the level of this Policy.

        告警级别

        :return: The level of this Policy.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Policy.

        告警级别

        :param level: The level of this Policy.
        :type: int
        """
        self._level = level

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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
