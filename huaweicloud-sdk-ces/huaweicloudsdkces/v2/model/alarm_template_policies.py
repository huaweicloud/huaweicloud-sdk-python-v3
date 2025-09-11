# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmTemplatePolicies:

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
        'hierarchical_value': 'HierarchicalValue',
        'unit': 'str',
        'count': 'int',
        'alarm_level': 'int',
        'suppress_duration': 'int',
        'selected_unit': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dimension_name': 'dimension_name',
        'metric_name': 'metric_name',
        'period': 'period',
        'filter': 'filter',
        'comparison_operator': 'comparison_operator',
        'value': 'value',
        'hierarchical_value': 'hierarchical_value',
        'unit': 'unit',
        'count': 'count',
        'alarm_level': 'alarm_level',
        'suppress_duration': 'suppress_duration',
        'selected_unit': 'selected_unit'
    }

    def __init__(self, namespace=None, dimension_name=None, metric_name=None, period=None, filter=None, comparison_operator=None, value=None, hierarchical_value=None, unit=None, count=None, alarm_level=None, suppress_duration=None, selected_unit=None):
        r"""AlarmTemplatePolicies

        The model defined in huaweicloud sdk

        :param namespace: **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及。 
        :type namespace: str
        :param dimension_name: **参数解释**： 资源维度。     **约束限制**： 事件告警模板DimensionName为空 **取值范围**： 必须以字母开头，多维度用\&quot;,\&quot;分隔，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32。目前最大支持4个维度。举例：单维度场景：instance_id；多维度场景：instance_id,disk        **默认取值**： 不涉及。 
        :type dimension_name: str
        :param metric_name: **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 
        :type metric_name: str
        :param period: 告警条件判断周期,单位为秒
        :type period: int
        :param filter: 数据聚合方式
        :type filter: str
        :param comparison_operator: **参数解释**： 阈值符号。     **约束限制**： 指标告警可以使用的阈值符号有&gt;、&gt;&#x3D;、&lt;、&lt;&#x3D;、&#x3D;、!&#x3D;、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为&gt;、&gt;&#x3D;、&lt;、&lt;&#x3D;、&#x3D;、!&#x3D;。 **取值范围**： 支持的值为(&gt;|&lt;|&gt;&#x3D;|&lt;&#x3D;|&#x3D;|!&#x3D;|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。           **默认取值**： 不涉及。 
        :type comparison_operator: str
        :param value: 告警阈值。单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准
        :type value: float
        :param hierarchical_value: 
        :type hierarchical_value: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        :param unit: 数据的单位字符串，长度不超过32
        :type unit: str
        :param count: **参数解释**： 告警连续触发次数。     **约束限制**： 不涉及。 **取值范围**： 事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180。          **默认取值**： 不涉及。 
        :type count: int
        :param alarm_level: **参数解释**： 告警级别。     **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。 - 1为紧急 - 2为重要 - 3为次要 - 4为提示           **默认取值**： 不涉及。 
        :type alarm_level: int
        :param suppress_duration: 告警抑制周期，单位为秒，当告警抑制周期为0时，仅发送一次告警
        :type suppress_duration: int
        :param selected_unit: **参数解释**： 用户在页面中选择的指标单位， 用于后续指标数据回显和计算。     **约束限制**： 不涉及。 **取值范围**： 长度为[0,64]个字符。        **默认取值**： 不涉及。 
        :type selected_unit: str
        """
        
        

        self._namespace = None
        self._dimension_name = None
        self._metric_name = None
        self._period = None
        self._filter = None
        self._comparison_operator = None
        self._value = None
        self._hierarchical_value = None
        self._unit = None
        self._count = None
        self._alarm_level = None
        self._suppress_duration = None
        self._selected_unit = None
        self.discriminator = None

        self.namespace = namespace
        self.dimension_name = dimension_name
        self.metric_name = metric_name
        self.period = period
        self.filter = filter
        self.comparison_operator = comparison_operator
        if value is not None:
            self.value = value
        if hierarchical_value is not None:
            self.hierarchical_value = hierarchical_value
        self.unit = unit
        self.count = count
        self.alarm_level = alarm_level
        self.suppress_duration = suppress_duration
        if selected_unit is not None:
            self.selected_unit = selected_unit

    @property
    def namespace(self):
        r"""Gets the namespace of this AlarmTemplatePolicies.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及。 

        :return: The namespace of this AlarmTemplatePolicies.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this AlarmTemplatePolicies.

        **参数解释**： 查询服务的命名空间，各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在 3 到 32个字符之间。 **默认取值**： 不涉及。 

        :param namespace: The namespace of this AlarmTemplatePolicies.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimension_name(self):
        r"""Gets the dimension_name of this AlarmTemplatePolicies.

        **参数解释**： 资源维度。     **约束限制**： 事件告警模板DimensionName为空 **取值范围**： 必须以字母开头，多维度用\",\"分隔，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32。目前最大支持4个维度。举例：单维度场景：instance_id；多维度场景：instance_id,disk        **默认取值**： 不涉及。 

        :return: The dimension_name of this AlarmTemplatePolicies.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        r"""Sets the dimension_name of this AlarmTemplatePolicies.

        **参数解释**： 资源维度。     **约束限制**： 事件告警模板DimensionName为空 **取值范围**： 必须以字母开头，多维度用\",\"分隔，只能包含0-9/a-z/A-Z/_/-，每个维度的最大长度为32。目前最大支持4个维度。举例：单维度场景：instance_id；多维度场景：instance_id,disk        **默认取值**： 不涉及。 

        :param dimension_name: The dimension_name of this AlarmTemplatePolicies.
        :type dimension_name: str
        """
        self._dimension_name = dimension_name

    @property
    def metric_name(self):
        r"""Gets the metric_name of this AlarmTemplatePolicies.

        **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 

        :return: The metric_name of this AlarmTemplatePolicies.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this AlarmTemplatePolicies.

        **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 

        :param metric_name: The metric_name of this AlarmTemplatePolicies.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def period(self):
        r"""Gets the period of this AlarmTemplatePolicies.

        告警条件判断周期,单位为秒

        :return: The period of this AlarmTemplatePolicies.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this AlarmTemplatePolicies.

        告警条件判断周期,单位为秒

        :param period: The period of this AlarmTemplatePolicies.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        r"""Gets the filter of this AlarmTemplatePolicies.

        数据聚合方式

        :return: The filter of this AlarmTemplatePolicies.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this AlarmTemplatePolicies.

        数据聚合方式

        :param filter: The filter of this AlarmTemplatePolicies.
        :type filter: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        r"""Gets the comparison_operator of this AlarmTemplatePolicies.

        **参数解释**： 阈值符号。     **约束限制**： 指标告警可以使用的阈值符号有>、>=、<、<=、=、!=、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为>、>=、<、<=、=、!=。 **取值范围**： 支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。           **默认取值**： 不涉及。 

        :return: The comparison_operator of this AlarmTemplatePolicies.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        r"""Sets the comparison_operator of this AlarmTemplatePolicies.

        **参数解释**： 阈值符号。     **约束限制**： 指标告警可以使用的阈值符号有>、>=、<、<=、=、!=、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为>、>=、<、<=、=、!=。 **取值范围**： 支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。           **默认取值**： 不涉及。 

        :param comparison_operator: The comparison_operator of this AlarmTemplatePolicies.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        r"""Gets the value of this AlarmTemplatePolicies.

        告警阈值。单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准

        :return: The value of this AlarmTemplatePolicies.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this AlarmTemplatePolicies.

        告警阈值。单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准

        :param value: The value of this AlarmTemplatePolicies.
        :type value: float
        """
        self._value = value

    @property
    def hierarchical_value(self):
        r"""Gets the hierarchical_value of this AlarmTemplatePolicies.

        :return: The hierarchical_value of this AlarmTemplatePolicies.
        :rtype: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        """
        return self._hierarchical_value

    @hierarchical_value.setter
    def hierarchical_value(self, hierarchical_value):
        r"""Sets the hierarchical_value of this AlarmTemplatePolicies.

        :param hierarchical_value: The hierarchical_value of this AlarmTemplatePolicies.
        :type hierarchical_value: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        """
        self._hierarchical_value = hierarchical_value

    @property
    def unit(self):
        r"""Gets the unit of this AlarmTemplatePolicies.

        数据的单位字符串，长度不超过32

        :return: The unit of this AlarmTemplatePolicies.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this AlarmTemplatePolicies.

        数据的单位字符串，长度不超过32

        :param unit: The unit of this AlarmTemplatePolicies.
        :type unit: str
        """
        self._unit = unit

    @property
    def count(self):
        r"""Gets the count of this AlarmTemplatePolicies.

        **参数解释**： 告警连续触发次数。     **约束限制**： 不涉及。 **取值范围**： 事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180。          **默认取值**： 不涉及。 

        :return: The count of this AlarmTemplatePolicies.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this AlarmTemplatePolicies.

        **参数解释**： 告警连续触发次数。     **约束限制**： 不涉及。 **取值范围**： 事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180。          **默认取值**： 不涉及。 

        :param count: The count of this AlarmTemplatePolicies.
        :type count: int
        """
        self._count = count

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this AlarmTemplatePolicies.

        **参数解释**： 告警级别。     **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。 - 1为紧急 - 2为重要 - 3为次要 - 4为提示           **默认取值**： 不涉及。 

        :return: The alarm_level of this AlarmTemplatePolicies.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this AlarmTemplatePolicies.

        **参数解释**： 告警级别。     **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。 - 1为紧急 - 2为重要 - 3为次要 - 4为提示           **默认取值**： 不涉及。 

        :param alarm_level: The alarm_level of this AlarmTemplatePolicies.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def suppress_duration(self):
        r"""Gets the suppress_duration of this AlarmTemplatePolicies.

        告警抑制周期，单位为秒，当告警抑制周期为0时，仅发送一次告警

        :return: The suppress_duration of this AlarmTemplatePolicies.
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        r"""Sets the suppress_duration of this AlarmTemplatePolicies.

        告警抑制周期，单位为秒，当告警抑制周期为0时，仅发送一次告警

        :param suppress_duration: The suppress_duration of this AlarmTemplatePolicies.
        :type suppress_duration: int
        """
        self._suppress_duration = suppress_duration

    @property
    def selected_unit(self):
        r"""Gets the selected_unit of this AlarmTemplatePolicies.

        **参数解释**： 用户在页面中选择的指标单位， 用于后续指标数据回显和计算。     **约束限制**： 不涉及。 **取值范围**： 长度为[0,64]个字符。        **默认取值**： 不涉及。 

        :return: The selected_unit of this AlarmTemplatePolicies.
        :rtype: str
        """
        return self._selected_unit

    @selected_unit.setter
    def selected_unit(self, selected_unit):
        r"""Sets the selected_unit of this AlarmTemplatePolicies.

        **参数解释**： 用户在页面中选择的指标单位， 用于后续指标数据回显和计算。     **约束限制**： 不涉及。 **取值范围**： 长度为[0,64]个字符。        **默认取值**： 不涉及。 

        :param selected_unit: The selected_unit of this AlarmTemplatePolicies.
        :type selected_unit: str
        """
        self._selected_unit = selected_unit

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
        if not isinstance(other, AlarmTemplatePolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
