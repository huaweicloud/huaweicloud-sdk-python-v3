# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicy:

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
        'type': 'str',
        'count': 'int',
        'suppress_duration': 'int',
        'level': 'int',
        'namespace': 'str',
        'dimension_name': 'str'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'period': 'period',
        'filter': 'filter',
        'comparison_operator': 'comparison_operator',
        'value': 'value',
        'unit': 'unit',
        'type': 'type',
        'count': 'count',
        'suppress_duration': 'suppress_duration',
        'level': 'level',
        'namespace': 'namespace',
        'dimension_name': 'dimension_name'
    }

    def __init__(self, metric_name=None, period=None, filter=None, comparison_operator=None, value=None, unit=None, type=None, count=None, suppress_duration=None, level=None, namespace=None, dimension_name=None):
        """UpdatePolicy

        The model defined in huaweicloud sdk

        :param metric_name: 资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type metric_name: str
        :param period: 指标周期，单位是秒； 0是默认值，例如事件类告警该字段就用0即可； 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算；如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”，300代表指标按5分钟聚合周期为一个数据点参与告警计算。
        :type period: int
        :param filter: 聚合方式, 支持的值为(average|min|max|sum)
        :type filter: str
        :param comparison_operator: 告警阈值的比较条件，支持的值为(&gt;|&lt;|&gt;&#x3D;|&lt;&#x3D;|&#x3D;|!&#x3D;|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动
        :type comparison_operator: str
        :param value: 阈值
        :type value: float
        :param unit: 单位
        :type unit: str
        :param type: 告警策略类型，默认为空
        :type type: str
        :param count: 告警连续触发次数，事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180
        :type count: int
        :param suppress_duration: 告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题，0代表不抑制，满足条件即告警；300代表满足告警触发条件后每5分钟告警一次；
        :type suppress_duration: int
        :param level: 告警级别, 1为紧急，2为重要，3为次要，4为提示
        :type level: int
        :param namespace: 查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)
        :type namespace: str
        :param dimension_name: 资源维度，必须以字母开头，多维度用\&quot;,\&quot;分割，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32
        :type dimension_name: str
        """
        
        

        self._metric_name = None
        self._period = None
        self._filter = None
        self._comparison_operator = None
        self._value = None
        self._unit = None
        self._type = None
        self._count = None
        self._suppress_duration = None
        self._level = None
        self._namespace = None
        self._dimension_name = None
        self.discriminator = None

        self.metric_name = metric_name
        self.period = period
        self.filter = filter
        self.comparison_operator = comparison_operator
        if value is not None:
            self.value = value
        if unit is not None:
            self.unit = unit
        if type is not None:
            self.type = type
        self.count = count
        if suppress_duration is not None:
            self.suppress_duration = suppress_duration
        if level is not None:
            self.level = level
        if namespace is not None:
            self.namespace = namespace
        if dimension_name is not None:
            self.dimension_name = dimension_name

    @property
    def metric_name(self):
        """Gets the metric_name of this UpdatePolicy.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The metric_name of this UpdatePolicy.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this UpdatePolicy.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param metric_name: The metric_name of this UpdatePolicy.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def period(self):
        """Gets the period of this UpdatePolicy.

        指标周期，单位是秒； 0是默认值，例如事件类告警该字段就用0即可； 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算；如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”，300代表指标按5分钟聚合周期为一个数据点参与告警计算。

        :return: The period of this UpdatePolicy.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this UpdatePolicy.

        指标周期，单位是秒； 0是默认值，例如事件类告警该字段就用0即可； 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算；如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”，300代表指标按5分钟聚合周期为一个数据点参与告警计算。

        :param period: The period of this UpdatePolicy.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        """Gets the filter of this UpdatePolicy.

        聚合方式, 支持的值为(average|min|max|sum)

        :return: The filter of this UpdatePolicy.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this UpdatePolicy.

        聚合方式, 支持的值为(average|min|max|sum)

        :param filter: The filter of this UpdatePolicy.
        :type filter: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        """Gets the comparison_operator of this UpdatePolicy.

        告警阈值的比较条件，支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动

        :return: The comparison_operator of this UpdatePolicy.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        """Sets the comparison_operator of this UpdatePolicy.

        告警阈值的比较条件，支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave)，cycle_decrease为环比下降，cycle_increase为环比上升，cycle_wave为环比波动

        :param comparison_operator: The comparison_operator of this UpdatePolicy.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        """Gets the value of this UpdatePolicy.

        阈值

        :return: The value of this UpdatePolicy.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this UpdatePolicy.

        阈值

        :param value: The value of this UpdatePolicy.
        :type value: float
        """
        self._value = value

    @property
    def unit(self):
        """Gets the unit of this UpdatePolicy.

        单位

        :return: The unit of this UpdatePolicy.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this UpdatePolicy.

        单位

        :param unit: The unit of this UpdatePolicy.
        :type unit: str
        """
        self._unit = unit

    @property
    def type(self):
        """Gets the type of this UpdatePolicy.

        告警策略类型，默认为空

        :return: The type of this UpdatePolicy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdatePolicy.

        告警策略类型，默认为空

        :param type: The type of this UpdatePolicy.
        :type type: str
        """
        self._type = type

    @property
    def count(self):
        """Gets the count of this UpdatePolicy.

        告警连续触发次数，事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180

        :return: The count of this UpdatePolicy.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this UpdatePolicy.

        告警连续触发次数，事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180

        :param count: The count of this UpdatePolicy.
        :type count: int
        """
        self._count = count

    @property
    def suppress_duration(self):
        """Gets the suppress_duration of this UpdatePolicy.

        告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题，0代表不抑制，满足条件即告警；300代表满足告警触发条件后每5分钟告警一次；

        :return: The suppress_duration of this UpdatePolicy.
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        """Sets the suppress_duration of this UpdatePolicy.

        告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题，0代表不抑制，满足条件即告警；300代表满足告警触发条件后每5分钟告警一次；

        :param suppress_duration: The suppress_duration of this UpdatePolicy.
        :type suppress_duration: int
        """
        self._suppress_duration = suppress_duration

    @property
    def level(self):
        """Gets the level of this UpdatePolicy.

        告警级别, 1为紧急，2为重要，3为次要，4为提示

        :return: The level of this UpdatePolicy.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this UpdatePolicy.

        告警级别, 1为紧急，2为重要，3为次要，4为提示

        :param level: The level of this UpdatePolicy.
        :type level: int
        """
        self._level = level

    @property
    def namespace(self):
        """Gets the namespace of this UpdatePolicy.

        查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)

        :return: The namespace of this UpdatePolicy.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this UpdatePolicy.

        查询服务的命名空间，各服务命名空间请参考[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)

        :param namespace: The namespace of this UpdatePolicy.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimension_name(self):
        """Gets the dimension_name of this UpdatePolicy.

        资源维度，必须以字母开头，多维度用\",\"分割，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32

        :return: The dimension_name of this UpdatePolicy.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        """Sets the dimension_name of this UpdatePolicy.

        资源维度，必须以字母开头，多维度用\",\"分割，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32

        :param dimension_name: The dimension_name of this UpdatePolicy.
        :type dimension_name: str
        """
        self._dimension_name = dimension_name

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
        if not isinstance(other, UpdatePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
