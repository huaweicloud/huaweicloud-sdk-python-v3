# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OneClickAlarmPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_policy_id': 'str',
        'metric_name': 'str',
        'period': 'Period',
        'filter': 'str',
        'comparison_operator': 'str',
        'value': 'float',
        'unit': 'str',
        'count': 'int',
        'suppress_duration': 'SuppressDuration',
        'level': 'int',
        'enabled': 'bool'
    }

    attribute_map = {
        'alarm_policy_id': 'alarm_policy_id',
        'metric_name': 'metric_name',
        'period': 'period',
        'filter': 'filter',
        'comparison_operator': 'comparison_operator',
        'value': 'value',
        'unit': 'unit',
        'count': 'count',
        'suppress_duration': 'suppress_duration',
        'level': 'level',
        'enabled': 'enabled'
    }

    def __init__(self, alarm_policy_id=None, metric_name=None, period=None, filter=None, comparison_operator=None, value=None, unit=None, count=None, suppress_duration=None, level=None, enabled=None):
        """OneClickAlarmPolicy

        The model defined in huaweicloud sdk

        :param alarm_policy_id: 告警策略ID。
        :type alarm_policy_id: str
        :param metric_name: 资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type metric_name: str
        :param period: 
        :type period: :class:`huaweicloudsdkces.v2.Period`
        :param filter: 聚合方式, 支持的值为(average|min|max|sum)
        :type filter: str
        :param comparison_operator: 告警阈值的比较条件，支持的值为(&gt;|&lt;|&gt;&#x3D;|&lt;&#x3D;|&#x3D;|!&#x3D;|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动
        :type comparison_operator: str
        :param value: 阈值
        :type value: float
        :param unit: 单位
        :type unit: str
        :param count: 次数
        :type count: int
        :param suppress_duration: 
        :type suppress_duration: :class:`huaweicloudsdkces.v2.SuppressDuration`
        :param level: 告警级别, 1为紧急，2为重要，3为次要，4为提示
        :type level: int
        :param enabled: 开关
        :type enabled: bool
        """
        
        

        self._alarm_policy_id = None
        self._metric_name = None
        self._period = None
        self._filter = None
        self._comparison_operator = None
        self._value = None
        self._unit = None
        self._count = None
        self._suppress_duration = None
        self._level = None
        self._enabled = None
        self.discriminator = None

        self.alarm_policy_id = alarm_policy_id
        self.metric_name = metric_name
        self.period = period
        self.filter = filter
        self.comparison_operator = comparison_operator
        self.value = value
        if unit is not None:
            self.unit = unit
        self.count = count
        if suppress_duration is not None:
            self.suppress_duration = suppress_duration
        if level is not None:
            self.level = level
        self.enabled = enabled

    @property
    def alarm_policy_id(self):
        """Gets the alarm_policy_id of this OneClickAlarmPolicy.

        告警策略ID。

        :return: The alarm_policy_id of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._alarm_policy_id

    @alarm_policy_id.setter
    def alarm_policy_id(self, alarm_policy_id):
        """Sets the alarm_policy_id of this OneClickAlarmPolicy.

        告警策略ID。

        :param alarm_policy_id: The alarm_policy_id of this OneClickAlarmPolicy.
        :type alarm_policy_id: str
        """
        self._alarm_policy_id = alarm_policy_id

    @property
    def metric_name(self):
        """Gets the metric_name of this OneClickAlarmPolicy.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The metric_name of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this OneClickAlarmPolicy.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param metric_name: The metric_name of this OneClickAlarmPolicy.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def period(self):
        """Gets the period of this OneClickAlarmPolicy.

        :return: The period of this OneClickAlarmPolicy.
        :rtype: :class:`huaweicloudsdkces.v2.Period`
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this OneClickAlarmPolicy.

        :param period: The period of this OneClickAlarmPolicy.
        :type period: :class:`huaweicloudsdkces.v2.Period`
        """
        self._period = period

    @property
    def filter(self):
        """Gets the filter of this OneClickAlarmPolicy.

        聚合方式, 支持的值为(average|min|max|sum)

        :return: The filter of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this OneClickAlarmPolicy.

        聚合方式, 支持的值为(average|min|max|sum)

        :param filter: The filter of this OneClickAlarmPolicy.
        :type filter: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this OneClickAlarmPolicy.

        告警阈值的比较条件，支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动

        :return: The comparison_operator of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this OneClickAlarmPolicy.

        告警阈值的比较条件，支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动

        :param comparison_operator: The comparison_operator of this OneClickAlarmPolicy.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        """Gets the value of this OneClickAlarmPolicy.

        阈值

        :return: The value of this OneClickAlarmPolicy.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OneClickAlarmPolicy.

        阈值

        :param value: The value of this OneClickAlarmPolicy.
        :type value: float
        """
        self._value = value

    @property
    def unit(self):
        """Gets the unit of this OneClickAlarmPolicy.

        单位

        :return: The unit of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this OneClickAlarmPolicy.

        单位

        :param unit: The unit of this OneClickAlarmPolicy.
        :type unit: str
        """
        self._unit = unit

    @property
    def count(self):
        """Gets the count of this OneClickAlarmPolicy.

        次数

        :return: The count of this OneClickAlarmPolicy.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this OneClickAlarmPolicy.

        次数

        :param count: The count of this OneClickAlarmPolicy.
        :type count: int
        """
        self._count = count

    @property
    def suppress_duration(self):
        """Gets the suppress_duration of this OneClickAlarmPolicy.

        :return: The suppress_duration of this OneClickAlarmPolicy.
        :rtype: :class:`huaweicloudsdkces.v2.SuppressDuration`
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        """Sets the suppress_duration of this OneClickAlarmPolicy.

        :param suppress_duration: The suppress_duration of this OneClickAlarmPolicy.
        :type suppress_duration: :class:`huaweicloudsdkces.v2.SuppressDuration`
        """
        self._suppress_duration = suppress_duration

    @property
    def level(self):
        """Gets the level of this OneClickAlarmPolicy.

        告警级别, 1为紧急，2为重要，3为次要，4为提示

        :return: The level of this OneClickAlarmPolicy.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this OneClickAlarmPolicy.

        告警级别, 1为紧急，2为重要，3为次要，4为提示

        :param level: The level of this OneClickAlarmPolicy.
        :type level: int
        """
        self._level = level

    @property
    def enabled(self):
        """Gets the enabled of this OneClickAlarmPolicy.

        开关

        :return: The enabled of this OneClickAlarmPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this OneClickAlarmPolicy.

        开关

        :param enabled: The enabled of this OneClickAlarmPolicy.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, OneClickAlarmPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
