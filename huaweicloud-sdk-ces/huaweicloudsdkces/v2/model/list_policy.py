# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicy:

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
        'extra_info': 'MetricExtraInfo',
        'period': 'int',
        'filter': 'str',
        'comparison_operator': 'str',
        'value': 'float',
        'hierarchical_value': 'HierarchicalValue',
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
        'extra_info': 'extra_info',
        'period': 'period',
        'filter': 'filter',
        'comparison_operator': 'comparison_operator',
        'value': 'value',
        'hierarchical_value': 'hierarchical_value',
        'unit': 'unit',
        'type': 'type',
        'count': 'count',
        'suppress_duration': 'suppress_duration',
        'level': 'level',
        'namespace': 'namespace',
        'dimension_name': 'dimension_name'
    }

    def __init__(self, metric_name=None, extra_info=None, period=None, filter=None, comparison_operator=None, value=None, hierarchical_value=None, unit=None, type=None, count=None, suppress_duration=None, level=None, namespace=None, dimension_name=None):
        r"""ListPolicy

        The model defined in huaweicloud sdk

        :param metric_name: 资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。
        :type metric_name: str
        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkces.v2.MetricExtraInfo`
        :param period: 指标周期，单位是秒； 0是默认值，例如事件类告警该字段就用0即可； 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算；如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”，300代表指标按5分钟聚合周期为一个数据点参与告警计算。
        :type period: int
        :param filter: 聚合方式。average： 平均值，variance：方差，min：最小值，max：最大值，sum：求和，tp99：99百分位数，tp95：95百分位数，tp90：90百分位数
        :type filter: str
        :param comparison_operator: 阈值符号, 支持的值为(&gt;|&lt;|&gt;&#x3D;|&lt;&#x3D;|&#x3D;|!&#x3D;|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动； 指标告警可以使用的阈值符号有&gt;、&gt;&#x3D;、&lt;、&lt;&#x3D;、&#x3D;、!&#x3D;、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为&gt;、&gt;&#x3D;、&lt;、&lt;&#x3D;、&#x3D;、!&#x3D;； 
        :type comparison_operator: str
        :param value: 告警阈值。单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准。 具体阈值取值请参见附录中各服务监控指标中取值范围，如支持监控的服务列表中ECS的CPU使用率cpu_util取值范围可配置80。 [具体阈值取值请参见附录中各服务监控指标中取值范围，如[支持监控的服务列表](ces_03_0059.xml)中ECS的CPU使用率cpu_util取值范围可配置80。] 
        :type value: float
        :param hierarchical_value: 
        :type hierarchical_value: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        :param unit: 数据的单位。
        :type unit: str
        :param type: 告警策略类型，已废弃，不推荐使用。
        :type type: str
        :param count: 告警连续触发次数，事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180
        :type count: int
        :param suppress_duration: 告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题，0代表不抑制，满足条件即告警；300代表满足告警触发条件后每5分钟告警一次；
        :type suppress_duration: int
        :param level: 告警级别, 1为紧急，2为重要，3为次要，4为提示。默认值为2。
        :type level: int
        :param namespace: 查看产品层级规则的策略，会同时返回该策略的namespace（服务命名空间）和dimension_name（服务维度名称）用来获取生效的策略归属。各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”
        :type namespace: str
        :param dimension_name: 查看产品层级规则的策略，会同时返回该策略的namespace（服务命名空间）和dimension_name（服务维度名称）用来获取生效的策略归属。目前最大支持4个维度，各服务资源的指标维度名称可查看：“[服务维度名称](ces_03_0059.xml)”
        :type dimension_name: str
        """
        
        

        self._metric_name = None
        self._extra_info = None
        self._period = None
        self._filter = None
        self._comparison_operator = None
        self._value = None
        self._hierarchical_value = None
        self._unit = None
        self._type = None
        self._count = None
        self._suppress_duration = None
        self._level = None
        self._namespace = None
        self._dimension_name = None
        self.discriminator = None

        self.metric_name = metric_name
        if extra_info is not None:
            self.extra_info = extra_info
        self.period = period
        self.filter = filter
        self.comparison_operator = comparison_operator
        if value is not None:
            self.value = value
        if hierarchical_value is not None:
            self.hierarchical_value = hierarchical_value
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
        r"""Gets the metric_name of this ListPolicy.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。

        :return: The metric_name of this ListPolicy.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ListPolicy.

        资源的监控指标名称，必须以字母开头，只能包含0-9/a-z/A-Z/_，字符长度最短为1，最大为64；如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率；各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。

        :param metric_name: The metric_name of this ListPolicy.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def extra_info(self):
        r"""Gets the extra_info of this ListPolicy.

        :return: The extra_info of this ListPolicy.
        :rtype: :class:`huaweicloudsdkces.v2.MetricExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        r"""Sets the extra_info of this ListPolicy.

        :param extra_info: The extra_info of this ListPolicy.
        :type extra_info: :class:`huaweicloudsdkces.v2.MetricExtraInfo`
        """
        self._extra_info = extra_info

    @property
    def period(self):
        r"""Gets the period of this ListPolicy.

        指标周期，单位是秒； 0是默认值，例如事件类告警该字段就用0即可； 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算；如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”，300代表指标按5分钟聚合周期为一个数据点参与告警计算。

        :return: The period of this ListPolicy.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ListPolicy.

        指标周期，单位是秒； 0是默认值，例如事件类告警该字段就用0即可； 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算；如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”，300代表指标按5分钟聚合周期为一个数据点参与告警计算。

        :param period: The period of this ListPolicy.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        r"""Gets the filter of this ListPolicy.

        聚合方式。average： 平均值，variance：方差，min：最小值，max：最大值，sum：求和，tp99：99百分位数，tp95：95百分位数，tp90：90百分位数

        :return: The filter of this ListPolicy.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListPolicy.

        聚合方式。average： 平均值，variance：方差，min：最小值，max：最大值，sum：求和，tp99：99百分位数，tp95：95百分位数，tp90：90百分位数

        :param filter: The filter of this ListPolicy.
        :type filter: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        r"""Gets the comparison_operator of this ListPolicy.

        阈值符号, 支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动； 指标告警可以使用的阈值符号有>、>=、<、<=、=、!=、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为>、>=、<、<=、=、!=； 

        :return: The comparison_operator of this ListPolicy.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        r"""Sets the comparison_operator of this ListPolicy.

        阈值符号, 支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动； 指标告警可以使用的阈值符号有>、>=、<、<=、=、!=、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为>、>=、<、<=、=、!=； 

        :param comparison_operator: The comparison_operator of this ListPolicy.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        r"""Gets the value of this ListPolicy.

        告警阈值。单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准。 具体阈值取值请参见附录中各服务监控指标中取值范围，如支持监控的服务列表中ECS的CPU使用率cpu_util取值范围可配置80。 [具体阈值取值请参见附录中各服务监控指标中取值范围，如[支持监控的服务列表](ces_03_0059.xml)中ECS的CPU使用率cpu_util取值范围可配置80。] 

        :return: The value of this ListPolicy.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ListPolicy.

        告警阈值。单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准。 具体阈值取值请参见附录中各服务监控指标中取值范围，如支持监控的服务列表中ECS的CPU使用率cpu_util取值范围可配置80。 [具体阈值取值请参见附录中各服务监控指标中取值范围，如[支持监控的服务列表](ces_03_0059.xml)中ECS的CPU使用率cpu_util取值范围可配置80。] 

        :param value: The value of this ListPolicy.
        :type value: float
        """
        self._value = value

    @property
    def hierarchical_value(self):
        r"""Gets the hierarchical_value of this ListPolicy.

        :return: The hierarchical_value of this ListPolicy.
        :rtype: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        """
        return self._hierarchical_value

    @hierarchical_value.setter
    def hierarchical_value(self, hierarchical_value):
        r"""Sets the hierarchical_value of this ListPolicy.

        :param hierarchical_value: The hierarchical_value of this ListPolicy.
        :type hierarchical_value: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        """
        self._hierarchical_value = hierarchical_value

    @property
    def unit(self):
        r"""Gets the unit of this ListPolicy.

        数据的单位。

        :return: The unit of this ListPolicy.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ListPolicy.

        数据的单位。

        :param unit: The unit of this ListPolicy.
        :type unit: str
        """
        self._unit = unit

    @property
    def type(self):
        r"""Gets the type of this ListPolicy.

        告警策略类型，已废弃，不推荐使用。

        :return: The type of this ListPolicy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListPolicy.

        告警策略类型，已废弃，不推荐使用。

        :param type: The type of this ListPolicy.
        :type type: str
        """
        self._type = type

    @property
    def count(self):
        r"""Gets the count of this ListPolicy.

        告警连续触发次数，事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180

        :return: The count of this ListPolicy.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListPolicy.

        告警连续触发次数，事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180

        :param count: The count of this ListPolicy.
        :type count: int
        """
        self._count = count

    @property
    def suppress_duration(self):
        r"""Gets the suppress_duration of this ListPolicy.

        告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题，0代表不抑制，满足条件即告警；300代表满足告警触发条件后每5分钟告警一次；

        :return: The suppress_duration of this ListPolicy.
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        r"""Sets the suppress_duration of this ListPolicy.

        告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题，0代表不抑制，满足条件即告警；300代表满足告警触发条件后每5分钟告警一次；

        :param suppress_duration: The suppress_duration of this ListPolicy.
        :type suppress_duration: int
        """
        self._suppress_duration = suppress_duration

    @property
    def level(self):
        r"""Gets the level of this ListPolicy.

        告警级别, 1为紧急，2为重要，3为次要，4为提示。默认值为2。

        :return: The level of this ListPolicy.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ListPolicy.

        告警级别, 1为紧急，2为重要，3为次要，4为提示。默认值为2。

        :param level: The level of this ListPolicy.
        :type level: int
        """
        self._level = level

    @property
    def namespace(self):
        r"""Gets the namespace of this ListPolicy.

        查看产品层级规则的策略，会同时返回该策略的namespace（服务命名空间）和dimension_name（服务维度名称）用来获取生效的策略归属。各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :return: The namespace of this ListPolicy.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListPolicy.

        查看产品层级规则的策略，会同时返回该策略的namespace（服务命名空间）和dimension_name（服务维度名称）用来获取生效的策略归属。各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”

        :param namespace: The namespace of this ListPolicy.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimension_name(self):
        r"""Gets the dimension_name of this ListPolicy.

        查看产品层级规则的策略，会同时返回该策略的namespace（服务命名空间）和dimension_name（服务维度名称）用来获取生效的策略归属。目前最大支持4个维度，各服务资源的指标维度名称可查看：“[服务维度名称](ces_03_0059.xml)”

        :return: The dimension_name of this ListPolicy.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        r"""Sets the dimension_name of this ListPolicy.

        查看产品层级规则的策略，会同时返回该策略的namespace（服务命名空间）和dimension_name（服务维度名称）用来获取生效的策略归属。目前最大支持4个维度，各服务资源的指标维度名称可查看：“[服务维度名称](ces_03_0059.xml)”

        :param dimension_name: The dimension_name of this ListPolicy.
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
        if not isinstance(other, ListPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
