# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmCondition:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'period': 'int',
        'filter': 'str',
        'comparison_operator': 'str',
        'value': 'float',
        'unit': 'str',
        'count': 'int',
        'suppress_duration': 'int'
    }

    attribute_map = {
        'period': 'period',
        'filter': 'filter',
        'comparison_operator': 'comparison_operator',
        'value': 'value',
        'unit': 'unit',
        'count': 'count',
        'suppress_duration': 'suppress_duration'
    }

    def __init__(self, period=None, filter=None, comparison_operator=None, value=None, unit=None, count=None, suppress_duration=None):
        """AlarmCondition - a model defined in huaweicloud sdk"""
        
        

        self._period = None
        self._filter = None
        self._comparison_operator = None
        self._value = None
        self._unit = None
        self._count = None
        self._suppress_duration = None
        self.discriminator = None

        self.period = period
        self.filter = filter
        self.comparison_operator = comparison_operator
        self.value = value
        if unit is not None:
            self.unit = unit
        self.count = count
        if suppress_duration is not None:
            self.suppress_duration = suppress_duration

    @property
    def period(self):
        """Gets the period of this AlarmCondition.

        告警条件判断周期，单位为秒，支持的值为1，300，1200，3600，14400，86400。说明：当period设置为1时，表示以原始的指标数据判断告警。当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为0。

        :return: The period of this AlarmCondition.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this AlarmCondition.

        告警条件判断周期，单位为秒，支持的值为1，300，1200，3600，14400，86400。说明：当period设置为1时，表示以原始的指标数据判断告警。当alarm_type为（EVENT.SYS| EVENT.CUSTOM）时允许为0。

        :param period: The period of this AlarmCondition.
        :type: int
        """
        self._period = period

    @property
    def filter(self):
        """Gets the filter of this AlarmCondition.

        聚合方式

        :return: The filter of this AlarmCondition.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this AlarmCondition.

        聚合方式

        :param filter: The filter of this AlarmCondition.
        :type: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this AlarmCondition.

        阈值符号

        :return: The comparison_operator of this AlarmCondition.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this AlarmCondition.

        阈值符号

        :param comparison_operator: The comparison_operator of this AlarmCondition.
        :type: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        """Gets the value of this AlarmCondition.

        告警阈值，取值范围[0, Number.MAX_VALUE]，Number.MAX_VALUE值为1.7976931348623157e+108。具体阈值取值请参见附录中各服务监控指标中取值范围，如支持监控的服务列表中ECS的CPU使用率cpu_util取值范围可配置80。

        :return: The value of this AlarmCondition.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AlarmCondition.

        告警阈值，取值范围[0, Number.MAX_VALUE]，Number.MAX_VALUE值为1.7976931348623157e+108。具体阈值取值请参见附录中各服务监控指标中取值范围，如支持监控的服务列表中ECS的CPU使用率cpu_util取值范围可配置80。

        :param value: The value of this AlarmCondition.
        :type: float
        """
        self._value = value

    @property
    def unit(self):
        """Gets the unit of this AlarmCondition.

        数据的单位，最大长度为32位。

        :return: The unit of this AlarmCondition.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this AlarmCondition.

        数据的单位，最大长度为32位。

        :param unit: The unit of this AlarmCondition.
        :type: str
        """
        self._unit = unit

    @property
    def count(self):
        """Gets the count of this AlarmCondition.

        次数

        :return: The count of this AlarmCondition.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this AlarmCondition.

        次数

        :param count: The count of this AlarmCondition.
        :type: int
        """
        self._count = count

    @property
    def suppress_duration(self):
        """Gets the suppress_duration of this AlarmCondition.

        发送告警的周期，值可为0, 300, 600, 900, 1800, 3600, 10800, 21600, 43200, 86400；0表示只告警一次，300表示每5分钟告警一次，600表示每10分钟告警一次，900表示每15分钟告警一次，1800表示每30分钟告警一次，3600表示每1小时告警一次，10800表示每3小时告警一次，21600表示每6小时告警一次，43200表示每12小时告警一次，86400表示每1天告警一次。

        :return: The suppress_duration of this AlarmCondition.
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        """Sets the suppress_duration of this AlarmCondition.

        发送告警的周期，值可为0, 300, 600, 900, 1800, 3600, 10800, 21600, 43200, 86400；0表示只告警一次，300表示每5分钟告警一次，600表示每10分钟告警一次，900表示每15分钟告警一次，1800表示每30分钟告警一次，3600表示每1小时告警一次，10800表示每3小时告警一次，21600表示每6小时告警一次，43200表示每12小时告警一次，86400表示每1天告警一次。

        :param suppress_duration: The suppress_duration of this AlarmCondition.
        :type: int
        """
        self._suppress_duration = suppress_duration

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
        if not isinstance(other, AlarmCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
