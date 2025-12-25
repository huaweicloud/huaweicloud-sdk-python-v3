# coding: utf-8

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
        'period': 'int',
        'filter': 'str',
        'comparison_operator': 'str',
        'value': 'float',
        'hierarchical_value': 'HierarchicalValue',
        'unit': 'str',
        'count': 'int',
        'suppress_duration': 'int',
        'level': 'int',
        'enabled': 'bool',
        'selected_unit': 'str'
    }

    attribute_map = {
        'alarm_policy_id': 'alarm_policy_id',
        'metric_name': 'metric_name',
        'period': 'period',
        'filter': 'filter',
        'comparison_operator': 'comparison_operator',
        'value': 'value',
        'hierarchical_value': 'hierarchical_value',
        'unit': 'unit',
        'count': 'count',
        'suppress_duration': 'suppress_duration',
        'level': 'level',
        'enabled': 'enabled',
        'selected_unit': 'selected_unit'
    }

    def __init__(self, alarm_policy_id=None, metric_name=None, period=None, filter=None, comparison_operator=None, value=None, hierarchical_value=None, unit=None, count=None, suppress_duration=None, level=None, enabled=None, selected_unit=None):
        r"""OneClickAlarmPolicy

        The model defined in huaweicloud sdk

        :param alarm_policy_id: **参数解释**： 告警策略ID。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符，只能包含字母、数字、- **默认取值**： 不涉及。 
        :type alarm_policy_id: str
        :param metric_name: **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 
        :type metric_name: str
        :param period: **参数解释**： 告警条件判断周期,单位为秒。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - 0是默认值，事件类告警该字段用0即可。 - 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算。 - 300代表指标按5分钟聚合周期为一个数据点参与告警计算。 - 1200代表指标按20分钟聚合周期为一个数据点参与告警计算。 - 3600代表指标按1小时聚合周期为一个数据点参与告警计算。 - 14400代表指标按4小时聚合周期为一个数据点参与告警计算。 - 86400代表指标按1天聚合周期为一个数据点参与告警计算。 **默认取值**： 不涉及。 
        :type period: int
        :param filter: **参数解释**： 聚合方式。         **约束限制**： period为1（原始值）时filter字段不生效，默认为average。period大于1时filter才起作用。 **取值范围**： - average：平均值 - variance：方差 - min：最小值 - max：最大值 - sum：求和 **默认取值**： 不涉及。 
        :type filter: str
        :param comparison_operator: **参数解释**： 阈值符号。 **约束限制**： 指标告警可以使用的阈值符号有&gt;、&gt;&#x3D;、&lt;、&lt;&#x3D;、&#x3D;、!&#x3D;、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为&gt;、&gt;&#x3D;、&lt;、&lt;&#x3D;、&#x3D;、!&#x3D;。 **取值范围**： 支持的值为(&gt;|&lt;|&gt;&#x3D;|&lt;&#x3D;|&#x3D;|!&#x3D;|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。 **默认取值**： 不涉及。 
        :type comparison_operator: str
        :param value: **参数解释**： 告警阈值。具体阈值取值请参见“[支持服务列表](ces_03_0059.xml)”。    **约束限制**： 单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准。 **取值范围**： 最小值为-1.7976931348623157e+108，最大值为1.7976931348623157e+108。           **默认取值**： 不涉及。 
        :type value: float
        :param hierarchical_value: 
        :type hierarchical_value: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        :param unit: **参数解释**： 数据的单位。    **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。         **默认取值**： 不涉及。 
        :type unit: str
        :param count: **参数解释**： 告警连续触发次数。     **约束限制**： 不涉及。 **取值范围**： 事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180。          **默认取值**： 不涉及。 
        :type count: int
        :param suppress_duration: **参数解释**： 告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能为0、300、600、900、1800、3600、10800、21600、43200、86400。 - 0：对于指标类告警，0代表告警一次。对于事件类告警，在立即触发场景中，0代表不抑制；在累计触发场景，0代表只告警一次。 - 300代表满足告警触发条件后每5分钟告警一次。 - 600代表满足告警触发条件后每10分钟告警一次。 - 900代表满足告警触发条件后每15分钟告警一次。 - 1800代表满足告警触发条件后每30分钟告警一次。 - 3600代表满足告警触发条件后每60分钟告警一次。 - 10800代表满足告警触发条件后每3小时告警一次。 - 21600代表满足告警触发条件后每6小时告警一次。 - 43200代表满足告警触发条件后每12小时告警一次。 - 86400代表满足告警触发条件后每一天告警一次。 **默认取值**： 不涉及。 
        :type suppress_duration: int
        :param level: **参数解释**： 告警级别。    **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。 - 1：紧急 - 2：重要 - 3：次要 - 4：提示         **默认取值**： 2 
        :type level: int
        :param enabled: **参数解释** 是否启用一键告警 **约束限制** 不涉及 **取值范围** - true:开启 - false：关闭 **默认取值** true 
        :type enabled: bool
        :param selected_unit: **参数解释**： 用户在页面中选择的指标单位， 用于后续指标数据回显和计算。字符串最大长度为64。    **约束限制**： 不涉及。 **取值范围**： 长度为[0,64]个字符。        **默认取值**： 不涉及。 
        :type selected_unit: str
        """
        
        

        self._alarm_policy_id = None
        self._metric_name = None
        self._period = None
        self._filter = None
        self._comparison_operator = None
        self._value = None
        self._hierarchical_value = None
        self._unit = None
        self._count = None
        self._suppress_duration = None
        self._level = None
        self._enabled = None
        self._selected_unit = None
        self.discriminator = None

        self.alarm_policy_id = alarm_policy_id
        self.metric_name = metric_name
        self.period = period
        self.filter = filter
        self.comparison_operator = comparison_operator
        self.value = value
        if hierarchical_value is not None:
            self.hierarchical_value = hierarchical_value
        if unit is not None:
            self.unit = unit
        self.count = count
        if suppress_duration is not None:
            self.suppress_duration = suppress_duration
        if level is not None:
            self.level = level
        self.enabled = enabled
        if selected_unit is not None:
            self.selected_unit = selected_unit

    @property
    def alarm_policy_id(self):
        r"""Gets the alarm_policy_id of this OneClickAlarmPolicy.

        **参数解释**： 告警策略ID。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符，只能包含字母、数字、- **默认取值**： 不涉及。 

        :return: The alarm_policy_id of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._alarm_policy_id

    @alarm_policy_id.setter
    def alarm_policy_id(self, alarm_policy_id):
        r"""Sets the alarm_policy_id of this OneClickAlarmPolicy.

        **参数解释**： 告警策略ID。 **约束限制**： 不涉及。 **取值范围**： 长度为[1,64]个字符，只能包含字母、数字、- **默认取值**： 不涉及。 

        :param alarm_policy_id: The alarm_policy_id of this OneClickAlarmPolicy.
        :type alarm_policy_id: str
        """
        self._alarm_policy_id = alarm_policy_id

    @property
    def metric_name(self):
        r"""Gets the metric_name of this OneClickAlarmPolicy.

        **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 

        :return: The metric_name of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this OneClickAlarmPolicy.

        **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 

        :param metric_name: The metric_name of this OneClickAlarmPolicy.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def period(self):
        r"""Gets the period of this OneClickAlarmPolicy.

        **参数解释**： 告警条件判断周期,单位为秒。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - 0是默认值，事件类告警该字段用0即可。 - 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算。 - 300代表指标按5分钟聚合周期为一个数据点参与告警计算。 - 1200代表指标按20分钟聚合周期为一个数据点参与告警计算。 - 3600代表指标按1小时聚合周期为一个数据点参与告警计算。 - 14400代表指标按4小时聚合周期为一个数据点参与告警计算。 - 86400代表指标按1天聚合周期为一个数据点参与告警计算。 **默认取值**： 不涉及。 

        :return: The period of this OneClickAlarmPolicy.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this OneClickAlarmPolicy.

        **参数解释**： 告警条件判断周期,单位为秒。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - 0是默认值，事件类告警该字段用0即可。 - 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算。 - 300代表指标按5分钟聚合周期为一个数据点参与告警计算。 - 1200代表指标按20分钟聚合周期为一个数据点参与告警计算。 - 3600代表指标按1小时聚合周期为一个数据点参与告警计算。 - 14400代表指标按4小时聚合周期为一个数据点参与告警计算。 - 86400代表指标按1天聚合周期为一个数据点参与告警计算。 **默认取值**： 不涉及。 

        :param period: The period of this OneClickAlarmPolicy.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        r"""Gets the filter of this OneClickAlarmPolicy.

        **参数解释**： 聚合方式。         **约束限制**： period为1（原始值）时filter字段不生效，默认为average。period大于1时filter才起作用。 **取值范围**： - average：平均值 - variance：方差 - min：最小值 - max：最大值 - sum：求和 **默认取值**： 不涉及。 

        :return: The filter of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this OneClickAlarmPolicy.

        **参数解释**： 聚合方式。         **约束限制**： period为1（原始值）时filter字段不生效，默认为average。period大于1时filter才起作用。 **取值范围**： - average：平均值 - variance：方差 - min：最小值 - max：最大值 - sum：求和 **默认取值**： 不涉及。 

        :param filter: The filter of this OneClickAlarmPolicy.
        :type filter: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        r"""Gets the comparison_operator of this OneClickAlarmPolicy.

        **参数解释**： 阈值符号。 **约束限制**： 指标告警可以使用的阈值符号有>、>=、<、<=、=、!=、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为>、>=、<、<=、=、!=。 **取值范围**： 支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。 **默认取值**： 不涉及。 

        :return: The comparison_operator of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        r"""Sets the comparison_operator of this OneClickAlarmPolicy.

        **参数解释**： 阈值符号。 **约束限制**： 指标告警可以使用的阈值符号有>、>=、<、<=、=、!=、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为>、>=、<、<=、=、!=。 **取值范围**： 支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。 **默认取值**： 不涉及。 

        :param comparison_operator: The comparison_operator of this OneClickAlarmPolicy.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        r"""Gets the value of this OneClickAlarmPolicy.

        **参数解释**： 告警阈值。具体阈值取值请参见“[支持服务列表](ces_03_0059.xml)”。    **约束限制**： 单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准。 **取值范围**： 最小值为-1.7976931348623157e+108，最大值为1.7976931348623157e+108。           **默认取值**： 不涉及。 

        :return: The value of this OneClickAlarmPolicy.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OneClickAlarmPolicy.

        **参数解释**： 告警阈值。具体阈值取值请参见“[支持服务列表](ces_03_0059.xml)”。    **约束限制**： 单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准。 **取值范围**： 最小值为-1.7976931348623157e+108，最大值为1.7976931348623157e+108。           **默认取值**： 不涉及。 

        :param value: The value of this OneClickAlarmPolicy.
        :type value: float
        """
        self._value = value

    @property
    def hierarchical_value(self):
        r"""Gets the hierarchical_value of this OneClickAlarmPolicy.

        :return: The hierarchical_value of this OneClickAlarmPolicy.
        :rtype: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        """
        return self._hierarchical_value

    @hierarchical_value.setter
    def hierarchical_value(self, hierarchical_value):
        r"""Sets the hierarchical_value of this OneClickAlarmPolicy.

        :param hierarchical_value: The hierarchical_value of this OneClickAlarmPolicy.
        :type hierarchical_value: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        """
        self._hierarchical_value = hierarchical_value

    @property
    def unit(self):
        r"""Gets the unit of this OneClickAlarmPolicy.

        **参数解释**： 数据的单位。    **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。         **默认取值**： 不涉及。 

        :return: The unit of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this OneClickAlarmPolicy.

        **参数解释**： 数据的单位。    **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。         **默认取值**： 不涉及。 

        :param unit: The unit of this OneClickAlarmPolicy.
        :type unit: str
        """
        self._unit = unit

    @property
    def count(self):
        r"""Gets the count of this OneClickAlarmPolicy.

        **参数解释**： 告警连续触发次数。     **约束限制**： 不涉及。 **取值范围**： 事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180。          **默认取值**： 不涉及。 

        :return: The count of this OneClickAlarmPolicy.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this OneClickAlarmPolicy.

        **参数解释**： 告警连续触发次数。     **约束限制**： 不涉及。 **取值范围**： 事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180。          **默认取值**： 不涉及。 

        :param count: The count of this OneClickAlarmPolicy.
        :type count: int
        """
        self._count = count

    @property
    def suppress_duration(self):
        r"""Gets the suppress_duration of this OneClickAlarmPolicy.

        **参数解释**： 告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能为0、300、600、900、1800、3600、10800、21600、43200、86400。 - 0：对于指标类告警，0代表告警一次。对于事件类告警，在立即触发场景中，0代表不抑制；在累计触发场景，0代表只告警一次。 - 300代表满足告警触发条件后每5分钟告警一次。 - 600代表满足告警触发条件后每10分钟告警一次。 - 900代表满足告警触发条件后每15分钟告警一次。 - 1800代表满足告警触发条件后每30分钟告警一次。 - 3600代表满足告警触发条件后每60分钟告警一次。 - 10800代表满足告警触发条件后每3小时告警一次。 - 21600代表满足告警触发条件后每6小时告警一次。 - 43200代表满足告警触发条件后每12小时告警一次。 - 86400代表满足告警触发条件后每一天告警一次。 **默认取值**： 不涉及。 

        :return: The suppress_duration of this OneClickAlarmPolicy.
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        r"""Sets the suppress_duration of this OneClickAlarmPolicy.

        **参数解释**： 告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能为0、300、600、900、1800、3600、10800、21600、43200、86400。 - 0：对于指标类告警，0代表告警一次。对于事件类告警，在立即触发场景中，0代表不抑制；在累计触发场景，0代表只告警一次。 - 300代表满足告警触发条件后每5分钟告警一次。 - 600代表满足告警触发条件后每10分钟告警一次。 - 900代表满足告警触发条件后每15分钟告警一次。 - 1800代表满足告警触发条件后每30分钟告警一次。 - 3600代表满足告警触发条件后每60分钟告警一次。 - 10800代表满足告警触发条件后每3小时告警一次。 - 21600代表满足告警触发条件后每6小时告警一次。 - 43200代表满足告警触发条件后每12小时告警一次。 - 86400代表满足告警触发条件后每一天告警一次。 **默认取值**： 不涉及。 

        :param suppress_duration: The suppress_duration of this OneClickAlarmPolicy.
        :type suppress_duration: int
        """
        self._suppress_duration = suppress_duration

    @property
    def level(self):
        r"""Gets the level of this OneClickAlarmPolicy.

        **参数解释**： 告警级别。    **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。 - 1：紧急 - 2：重要 - 3：次要 - 4：提示         **默认取值**： 2 

        :return: The level of this OneClickAlarmPolicy.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this OneClickAlarmPolicy.

        **参数解释**： 告警级别。    **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。 - 1：紧急 - 2：重要 - 3：次要 - 4：提示         **默认取值**： 2 

        :param level: The level of this OneClickAlarmPolicy.
        :type level: int
        """
        self._level = level

    @property
    def enabled(self):
        r"""Gets the enabled of this OneClickAlarmPolicy.

        **参数解释** 是否启用一键告警 **约束限制** 不涉及 **取值范围** - true:开启 - false：关闭 **默认取值** true 

        :return: The enabled of this OneClickAlarmPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this OneClickAlarmPolicy.

        **参数解释** 是否启用一键告警 **约束限制** 不涉及 **取值范围** - true:开启 - false：关闭 **默认取值** true 

        :param enabled: The enabled of this OneClickAlarmPolicy.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def selected_unit(self):
        r"""Gets the selected_unit of this OneClickAlarmPolicy.

        **参数解释**： 用户在页面中选择的指标单位， 用于后续指标数据回显和计算。字符串最大长度为64。    **约束限制**： 不涉及。 **取值范围**： 长度为[0,64]个字符。        **默认取值**： 不涉及。 

        :return: The selected_unit of this OneClickAlarmPolicy.
        :rtype: str
        """
        return self._selected_unit

    @selected_unit.setter
    def selected_unit(self, selected_unit):
        r"""Sets the selected_unit of this OneClickAlarmPolicy.

        **参数解释**： 用户在页面中选择的指标单位， 用于后续指标数据回显和计算。字符串最大长度为64。    **约束限制**： 不涉及。 **取值范围**： 长度为[0,64]个字符。        **默认取值**： 不涉及。 

        :param selected_unit: The selected_unit of this OneClickAlarmPolicy.
        :type selected_unit: str
        """
        self._selected_unit = selected_unit

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
