# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesInListResp:

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
        'extra_info': 'MetricExtraInfo',
        'period': 'Period',
        'filter': 'str',
        'comparison_operator': 'str',
        'value': 'float',
        'unit': 'str',
        'count': 'int',
        'type': 'str',
        'suppress_duration': 'SuppressDuration',
        'alarm_level': 'int'
    }

    attribute_map = {
        'alarm_policy_id': 'alarm_policy_id',
        'metric_name': 'metric_name',
        'extra_info': 'extra_info',
        'period': 'period',
        'filter': 'filter',
        'comparison_operator': 'comparison_operator',
        'value': 'value',
        'unit': 'unit',
        'count': 'count',
        'type': 'type',
        'suppress_duration': 'suppress_duration',
        'alarm_level': 'alarm_level'
    }

    def __init__(self, alarm_policy_id=None, metric_name=None, extra_info=None, period=None, filter=None, comparison_operator=None, value=None, unit=None, count=None, type=None, suppress_duration=None, alarm_level=None):
        """PoliciesInListResp

        The model defined in huaweicloud sdk

        :param alarm_policy_id: 告警策略ID。
        :type alarm_policy_id: str
        :param metric_name: 资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type metric_name: str
        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkces.v2.MetricExtraInfo`
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
        :param type: 告警策略类型。
        :type type: str
        :param suppress_duration: 
        :type suppress_duration: :class:`huaweicloudsdkces.v2.SuppressDuration`
        :param alarm_level: 告警级别，1为紧急，2为重要，3为次要，4为提示
        :type alarm_level: int
        """
        
        

        self._alarm_policy_id = None
        self._metric_name = None
        self._extra_info = None
        self._period = None
        self._filter = None
        self._comparison_operator = None
        self._value = None
        self._unit = None
        self._count = None
        self._type = None
        self._suppress_duration = None
        self._alarm_level = None
        self.discriminator = None

        self.alarm_policy_id = alarm_policy_id
        self.metric_name = metric_name
        if extra_info is not None:
            self.extra_info = extra_info
        self.period = period
        self.filter = filter
        self.comparison_operator = comparison_operator
        self.value = value
        if unit is not None:
            self.unit = unit
        self.count = count
        if type is not None:
            self.type = type
        if suppress_duration is not None:
            self.suppress_duration = suppress_duration
        if alarm_level is not None:
            self.alarm_level = alarm_level

    @property
    def alarm_policy_id(self):
        """Gets the alarm_policy_id of this PoliciesInListResp.

        告警策略ID。

        :return: The alarm_policy_id of this PoliciesInListResp.
        :rtype: str
        """
        return self._alarm_policy_id

    @alarm_policy_id.setter
    def alarm_policy_id(self, alarm_policy_id):
        """Sets the alarm_policy_id of this PoliciesInListResp.

        告警策略ID。

        :param alarm_policy_id: The alarm_policy_id of this PoliciesInListResp.
        :type alarm_policy_id: str
        """
        self._alarm_policy_id = alarm_policy_id

    @property
    def metric_name(self):
        """Gets the metric_name of this PoliciesInListResp.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The metric_name of this PoliciesInListResp.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this PoliciesInListResp.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param metric_name: The metric_name of this PoliciesInListResp.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def extra_info(self):
        """Gets the extra_info of this PoliciesInListResp.

        :return: The extra_info of this PoliciesInListResp.
        :rtype: :class:`huaweicloudsdkces.v2.MetricExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        """Sets the extra_info of this PoliciesInListResp.

        :param extra_info: The extra_info of this PoliciesInListResp.
        :type extra_info: :class:`huaweicloudsdkces.v2.MetricExtraInfo`
        """
        self._extra_info = extra_info

    @property
    def period(self):
        """Gets the period of this PoliciesInListResp.

        :return: The period of this PoliciesInListResp.
        :rtype: :class:`huaweicloudsdkces.v2.Period`
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PoliciesInListResp.

        :param period: The period of this PoliciesInListResp.
        :type period: :class:`huaweicloudsdkces.v2.Period`
        """
        self._period = period

    @property
    def filter(self):
        """Gets the filter of this PoliciesInListResp.

        聚合方式, 支持的值为(average|min|max|sum)

        :return: The filter of this PoliciesInListResp.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this PoliciesInListResp.

        聚合方式, 支持的值为(average|min|max|sum)

        :param filter: The filter of this PoliciesInListResp.
        :type filter: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this PoliciesInListResp.

        告警阈值的比较条件，支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动

        :return: The comparison_operator of this PoliciesInListResp.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this PoliciesInListResp.

        告警阈值的比较条件，支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动

        :param comparison_operator: The comparison_operator of this PoliciesInListResp.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        """Gets the value of this PoliciesInListResp.

        阈值

        :return: The value of this PoliciesInListResp.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PoliciesInListResp.

        阈值

        :param value: The value of this PoliciesInListResp.
        :type value: float
        """
        self._value = value

    @property
    def unit(self):
        """Gets the unit of this PoliciesInListResp.

        单位

        :return: The unit of this PoliciesInListResp.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this PoliciesInListResp.

        单位

        :param unit: The unit of this PoliciesInListResp.
        :type unit: str
        """
        self._unit = unit

    @property
    def count(self):
        """Gets the count of this PoliciesInListResp.

        次数

        :return: The count of this PoliciesInListResp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PoliciesInListResp.

        次数

        :param count: The count of this PoliciesInListResp.
        :type count: int
        """
        self._count = count

    @property
    def type(self):
        """Gets the type of this PoliciesInListResp.

        告警策略类型。

        :return: The type of this PoliciesInListResp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PoliciesInListResp.

        告警策略类型。

        :param type: The type of this PoliciesInListResp.
        :type type: str
        """
        self._type = type

    @property
    def suppress_duration(self):
        """Gets the suppress_duration of this PoliciesInListResp.

        :return: The suppress_duration of this PoliciesInListResp.
        :rtype: :class:`huaweicloudsdkces.v2.SuppressDuration`
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        """Sets the suppress_duration of this PoliciesInListResp.

        :param suppress_duration: The suppress_duration of this PoliciesInListResp.
        :type suppress_duration: :class:`huaweicloudsdkces.v2.SuppressDuration`
        """
        self._suppress_duration = suppress_duration

    @property
    def alarm_level(self):
        """Gets the alarm_level of this PoliciesInListResp.

        告警级别，1为紧急，2为重要，3为次要，4为提示

        :return: The alarm_level of this PoliciesInListResp.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this PoliciesInListResp.

        告警级别，1为紧急，2为重要，3为次要，4为提示

        :param alarm_level: The alarm_level of this PoliciesInListResp.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

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
        if not isinstance(other, PoliciesInListResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
