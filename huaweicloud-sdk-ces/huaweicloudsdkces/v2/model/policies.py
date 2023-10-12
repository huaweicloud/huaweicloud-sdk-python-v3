# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Policies:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'dimension_name': 'str',
        'metric_name': 'str',
        'period': 'int',
        'filter': 'str',
        'comparison_operator': 'str',
        'value': 'float',
        'unit': 'str',
        'count': 'int',
        'alarm_level': 'int',
        'suppress_duration': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimension_name': 'dimension_name',
        'metric_name': 'metric_name',
        'period': 'period',
        'filter': 'filter',
        'comparison_operator': 'comparison_operator',
        'value': 'value',
        'unit': 'unit',
        'count': 'count',
        'alarm_level': 'alarm_level',
        'suppress_duration': 'suppress_duration'
    }

    def __init__(self, namespace=None, dimension_name=None, metric_name=None, period=None, filter=None, comparison_operator=None, value=None, unit=None, count=None, alarm_level=None, suppress_duration=None):
        """Policies

        The model defined in huaweicloud sdk

        :param namespace: 查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)
        :type namespace: str
        :param dimension_name: 资源维度，必须以字母开头，多维度用\&quot;,\&quot;分割，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32
        :type dimension_name: str
        :param metric_name: 资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type metric_name: str
        :param period: 告警条件判断周期,单位为秒
        :type period: int
        :param filter: 数据聚合方式
        :type filter: str
        :param comparison_operator: 告警阈值的比较条件，支持的值为(&gt;|&lt;|&gt;&#x3D;|&lt;&#x3D;|&#x3D;|!&#x3D;|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动
        :type comparison_operator: str
        :param value: 告警阈值(Number.MAX_VALUE)
        :type value: float
        :param unit: 数据的单位字符串，长度不超过32
        :type unit: str
        :param count: 告警连续触发次数，正整数[1, 5]
        :type count: int
        :param alarm_level: 告警级别，1为紧急，2为重要，3为次要，4为提示
        :type alarm_level: int
        :param suppress_duration: 告警抑制周期，单位为秒，当告警抑制周期为0时，仅发送一次告警
        :type suppress_duration: int
        """
        
        

        self._namespace = None
        self._dimension_name = None
        self._metric_name = None
        self._period = None
        self._filter = None
        self._comparison_operator = None
        self._value = None
        self._unit = None
        self._count = None
        self._alarm_level = None
        self._suppress_duration = None
        self.discriminator = None

        self.namespace = namespace
        self.dimension_name = dimension_name
        self.metric_name = metric_name
        self.period = period
        self.filter = filter
        self.comparison_operator = comparison_operator
        self.value = value
        if unit is not None:
            self.unit = unit
        self.count = count
        if alarm_level is not None:
            self.alarm_level = alarm_level
        self.suppress_duration = suppress_duration

    @property
    def namespace(self):
        """Gets the namespace of this Policies.

        查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)

        :return: The namespace of this Policies.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Policies.

        查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)

        :param namespace: The namespace of this Policies.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimension_name(self):
        """Gets the dimension_name of this Policies.

        资源维度，必须以字母开头，多维度用\",\"分割，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32

        :return: The dimension_name of this Policies.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        """Sets the dimension_name of this Policies.

        资源维度，必须以字母开头，多维度用\",\"分割，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32

        :param dimension_name: The dimension_name of this Policies.
        :type dimension_name: str
        """
        self._dimension_name = dimension_name

    @property
    def metric_name(self):
        """Gets the metric_name of this Policies.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The metric_name of this Policies.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this Policies.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param metric_name: The metric_name of this Policies.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def period(self):
        """Gets the period of this Policies.

        告警条件判断周期,单位为秒

        :return: The period of this Policies.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Policies.

        告警条件判断周期,单位为秒

        :param period: The period of this Policies.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        """Gets the filter of this Policies.

        数据聚合方式

        :return: The filter of this Policies.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this Policies.

        数据聚合方式

        :param filter: The filter of this Policies.
        :type filter: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this Policies.

        告警阈值的比较条件，支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动

        :return: The comparison_operator of this Policies.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this Policies.

        告警阈值的比较条件，支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动

        :param comparison_operator: The comparison_operator of this Policies.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        """Gets the value of this Policies.

        告警阈值(Number.MAX_VALUE)

        :return: The value of this Policies.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Policies.

        告警阈值(Number.MAX_VALUE)

        :param value: The value of this Policies.
        :type value: float
        """
        self._value = value

    @property
    def unit(self):
        """Gets the unit of this Policies.

        数据的单位字符串，长度不超过32

        :return: The unit of this Policies.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Policies.

        数据的单位字符串，长度不超过32

        :param unit: The unit of this Policies.
        :type unit: str
        """
        self._unit = unit

    @property
    def count(self):
        """Gets the count of this Policies.

        告警连续触发次数，正整数[1, 5]

        :return: The count of this Policies.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Policies.

        告警连续触发次数，正整数[1, 5]

        :param count: The count of this Policies.
        :type count: int
        """
        self._count = count

    @property
    def alarm_level(self):
        """Gets the alarm_level of this Policies.

        告警级别，1为紧急，2为重要，3为次要，4为提示

        :return: The alarm_level of this Policies.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        """Sets the alarm_level of this Policies.

        告警级别，1为紧急，2为重要，3为次要，4为提示

        :param alarm_level: The alarm_level of this Policies.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def suppress_duration(self):
        """Gets the suppress_duration of this Policies.

        告警抑制周期，单位为秒，当告警抑制周期为0时，仅发送一次告警

        :return: The suppress_duration of this Policies.
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        """Sets the suppress_duration of this Policies.

        告警抑制周期，单位为秒，当告警抑制周期为0时，仅发送一次告警

        :param suppress_duration: The suppress_duration of this Policies.
        :type suppress_duration: int
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
        if not isinstance(other, Policies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
