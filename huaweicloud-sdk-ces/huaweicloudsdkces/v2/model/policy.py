# coding: utf-8

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
        'hierarchical_value': 'HierarchicalValue',
        'unit': 'str',
        'count': 'int',
        'suppress_duration': 'int',
        'level': 'int',
        'namespace': 'str',
        'dimension_name': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
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
        'namespace': 'namespace',
        'dimension_name': 'dimension_name',
        'enabled': 'enabled'
    }

    def __init__(self, metric_name=None, period=None, filter=None, comparison_operator=None, value=None, hierarchical_value=None, unit=None, count=None, suppress_duration=None, level=None, namespace=None, dimension_name=None, enabled=None):
        r"""Policy

        The model defined in huaweicloud sdk

        :param metric_name: **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 
        :type metric_name: str
        :param period: **参数解释**： 指标周期，单位是秒。如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - 0代表立即触发，仅限事件场景使用。 - 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算。 - 300代表指标按5分钟聚合周期为一个数据点参与告警计算。 - 1200代表指标按20分钟聚合周期为一个数据点参与告警计算。 - 3600代表指标按1小时聚合周期为一个数据点参与告警计算。 - 14400代表指标按4小时聚合周期为一个数据点参与告警计算。 - 86400代表指标按1天聚合周期为一个数据点参与告警计算。 **默认取值**：  不涉及。 
        :type period: int
        :param filter: **参数解释**： 聚合方式。         **约束限制**： 不涉及。 **取值范围**： average： 平均值，variance：方差，min：最小值，max：最大值，sum：求和。           **默认取值**： 不涉及。 
        :type filter: str
        :param comparison_operator: **参数解释**： 阈值符号。     **约束限制**： 指标告警可以使用的阈值符号有&gt;、&gt;&#x3D;、&lt;、&lt;&#x3D;、&#x3D;、!&#x3D;、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为&gt;、&gt;&#x3D;、&lt;、&lt;&#x3D;、&#x3D;、!&#x3D;。 **取值范围**： 支持的值为(&gt;|&lt;|&gt;&#x3D;|&lt;&#x3D;|&#x3D;|!&#x3D;|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。           **默认取值**： 不涉及。 
        :type comparison_operator: str
        :param value: **参数解释**： 告警阈值。具体阈值取值请参见附录中各服务监控指标中取值范围。    **约束限制**： 单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准。 **取值范围**： 最小值为-1.7976931348623157e+108，最大值为1.7976931348623157e+108。           **默认取值**： 不涉及。 
        :type value: float
        :param hierarchical_value: 
        :type hierarchical_value: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        :param unit: **参数解释**： 数据的单位。    **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。         **默认取值**： 不涉及。 
        :type unit: str
        :param count: **参数解释**： 告警连续触发次数。     **约束限制**： 不涉及。 **取值范围**： 事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180。          **默认取值**： 不涉及。 
        :type count: int
        :param suppress_duration: **参数解释**： 告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能为0、300、600、900、1800、3600、10800、21600、43200、86400。 - 0：在立即触发场景中，0代表不抑制；在累计触发场景，0代表只告警一次。 - 300代表满足告警触发条件后每5分钟告警一次。 - 600代表满足告警触发条件后每10分钟告警一次。 - 900代表满足告警触发条件后每15分钟告警一次。 - 1800代表满足告警触发条件后每30分钟告警一次。 - 3600代表满足告警触发条件后每60分钟告警一次。 - 10800代表满足告警触发条件后每3小时告警一次。 - 21600代表满足告警触发条件后每6小时告警一次。 - 43200代表满足告警触发条件后每12小时告警一次。 - 86000代表满足告警触发条件后每一天告警一次。 **默认取值**： 不涉及。 
        :type suppress_duration: int
        :param level: **参数解释**： 告警级别。    **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。1为紧急，2为重要，3为次要，4为提示。         **默认取值**： 2 
        :type level: int
        :param namespace: **参数解释**： 产品层级规则增加namespace（服务命名空间）和dimension_name（服务维度名称，用于指明生效策略的资源归属。各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在0到32个字符之间。 **默认取值**： 不涉及。 
        :type namespace: str
        :param dimension_name: **参数解释**： 指标维度名称，各服务资源的指标维度名称可查看：“[服务维度名称](ces_03_0059.xml)”。产品层级规则需要增加namespace（服务命名空间）和dimension_name（服务维度名称），用于指明策略生效的资源归属。 **约束限制**： 不涉及。 **取值范围**： 目前最大支持4个维度。举例：单维度场景：instance_id；多维度场景：instance_id,disk           **默认取值**： 不涉及。 
        :type dimension_name: str
        :param enabled: **参数解释**: 告警策略是否生效。true：策略生效，false：策略无效。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 
        :type enabled: bool
        """
        
        

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
        self._namespace = None
        self._dimension_name = None
        self._enabled = None
        self.discriminator = None

        self.metric_name = metric_name
        self.period = period
        self.filter = filter
        self.comparison_operator = comparison_operator
        if value is not None:
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
        if namespace is not None:
            self.namespace = namespace
        if dimension_name is not None:
            self.dimension_name = dimension_name
        if enabled is not None:
            self.enabled = enabled

    @property
    def metric_name(self):
        r"""Gets the metric_name of this Policy.

        **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 

        :return: The metric_name of this Policy.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this Policy.

        **参数解释**： 资源的监控指标名称，各服务的指标名称可查看：“[服务指标名称](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 必须以字母开头，只能包含0-9/a-z/A-Z/_/-。字符长度最短为1，最大为96。如：弹性云服务器中的监控指标cpu_util，表示弹性服务器的CPU使用率；文档数据库中的指标mongo001_command_ps，表示command执行频率。         **默认取值**： 不涉及。 

        :param metric_name: The metric_name of this Policy.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def period(self):
        r"""Gets the period of this Policy.

        **参数解释**： 指标周期，单位是秒。如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - 0代表立即触发，仅限事件场景使用。 - 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算。 - 300代表指标按5分钟聚合周期为一个数据点参与告警计算。 - 1200代表指标按20分钟聚合周期为一个数据点参与告警计算。 - 3600代表指标按1小时聚合周期为一个数据点参与告警计算。 - 14400代表指标按4小时聚合周期为一个数据点参与告警计算。 - 86400代表指标按1天聚合周期为一个数据点参与告警计算。 **默认取值**：  不涉及。 

        :return: The period of this Policy.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this Policy.

        **参数解释**： 指标周期，单位是秒。如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 枚举值。 - 0代表立即触发，仅限事件场景使用。 - 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算。 - 300代表指标按5分钟聚合周期为一个数据点参与告警计算。 - 1200代表指标按20分钟聚合周期为一个数据点参与告警计算。 - 3600代表指标按1小时聚合周期为一个数据点参与告警计算。 - 14400代表指标按4小时聚合周期为一个数据点参与告警计算。 - 86400代表指标按1天聚合周期为一个数据点参与告警计算。 **默认取值**：  不涉及。 

        :param period: The period of this Policy.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        r"""Gets the filter of this Policy.

        **参数解释**： 聚合方式。         **约束限制**： 不涉及。 **取值范围**： average： 平均值，variance：方差，min：最小值，max：最大值，sum：求和。           **默认取值**： 不涉及。 

        :return: The filter of this Policy.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this Policy.

        **参数解释**： 聚合方式。         **约束限制**： 不涉及。 **取值范围**： average： 平均值，variance：方差，min：最小值，max：最大值，sum：求和。           **默认取值**： 不涉及。 

        :param filter: The filter of this Policy.
        :type filter: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        r"""Gets the comparison_operator of this Policy.

        **参数解释**： 阈值符号。     **约束限制**： 指标告警可以使用的阈值符号有>、>=、<、<=、=、!=、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为>、>=、<、<=、=、!=。 **取值范围**： 支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。           **默认取值**： 不涉及。 

        :return: The comparison_operator of this Policy.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        r"""Sets the comparison_operator of this Policy.

        **参数解释**： 阈值符号。     **约束限制**： 指标告警可以使用的阈值符号有>、>=、<、<=、=、!=、cycle_decrease、cycle_increase、cycle_wave； 事件告警可以使用的阈值符号为>、>=、<、<=、=、!=。 **取值范围**： 支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。           **默认取值**： 不涉及。 

        :param comparison_operator: The comparison_operator of this Policy.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        r"""Gets the value of this Policy.

        **参数解释**： 告警阈值。具体阈值取值请参见附录中各服务监控指标中取值范围。    **约束限制**： 单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准。 **取值范围**： 最小值为-1.7976931348623157e+108，最大值为1.7976931348623157e+108。           **默认取值**： 不涉及。 

        :return: The value of this Policy.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Policy.

        **参数解释**： 告警阈值。具体阈值取值请参见附录中各服务监控指标中取值范围。    **约束限制**： 单一阈值时value和alarm_level配对使用，当hierarchical_value和value同时使用时以hierarchical_value为准。 **取值范围**： 最小值为-1.7976931348623157e+108，最大值为1.7976931348623157e+108。           **默认取值**： 不涉及。 

        :param value: The value of this Policy.
        :type value: float
        """
        self._value = value

    @property
    def hierarchical_value(self):
        r"""Gets the hierarchical_value of this Policy.

        :return: The hierarchical_value of this Policy.
        :rtype: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        """
        return self._hierarchical_value

    @hierarchical_value.setter
    def hierarchical_value(self, hierarchical_value):
        r"""Sets the hierarchical_value of this Policy.

        :param hierarchical_value: The hierarchical_value of this Policy.
        :type hierarchical_value: :class:`huaweicloudsdkces.v2.HierarchicalValue`
        """
        self._hierarchical_value = hierarchical_value

    @property
    def unit(self):
        r"""Gets the unit of this Policy.

        **参数解释**： 数据的单位。    **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。         **默认取值**： 不涉及。 

        :return: The unit of this Policy.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this Policy.

        **参数解释**： 数据的单位。    **约束限制**： 不涉及。 **取值范围**： 长度为[0,32]个字符。         **默认取值**： 不涉及。 

        :param unit: The unit of this Policy.
        :type unit: str
        """
        self._unit = unit

    @property
    def count(self):
        r"""Gets the count of this Policy.

        **参数解释**： 告警连续触发次数。     **约束限制**： 不涉及。 **取值范围**： 事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180。          **默认取值**： 不涉及。 

        :return: The count of this Policy.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this Policy.

        **参数解释**： 告警连续触发次数。     **约束限制**： 不涉及。 **取值范围**： 事件告警时参数值为1~180（包括1和180）；指标告警和站点告警时，次数采用枚举值，枚举值分别为：1、2、3、4、5、10、15、30、60、90、120、180。          **默认取值**： 不涉及。 

        :param count: The count of this Policy.
        :type count: int
        """
        self._count = count

    @property
    def suppress_duration(self):
        r"""Gets the suppress_duration of this Policy.

        **参数解释**： 告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能为0、300、600、900、1800、3600、10800、21600、43200、86400。 - 0：在立即触发场景中，0代表不抑制；在累计触发场景，0代表只告警一次。 - 300代表满足告警触发条件后每5分钟告警一次。 - 600代表满足告警触发条件后每10分钟告警一次。 - 900代表满足告警触发条件后每15分钟告警一次。 - 1800代表满足告警触发条件后每30分钟告警一次。 - 3600代表满足告警触发条件后每60分钟告警一次。 - 10800代表满足告警触发条件后每3小时告警一次。 - 21600代表满足告警触发条件后每6小时告警一次。 - 43200代表满足告警触发条件后每12小时告警一次。 - 86000代表满足告警触发条件后每一天告警一次。 **默认取值**： 不涉及。 

        :return: The suppress_duration of this Policy.
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        r"""Sets the suppress_duration of this Policy.

        **参数解释**： 告警抑制时间，单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题。 **约束限制**： 不涉及。 **取值范围**： 枚举值，只能为0、300、600、900、1800、3600、10800、21600、43200、86400。 - 0：在立即触发场景中，0代表不抑制；在累计触发场景，0代表只告警一次。 - 300代表满足告警触发条件后每5分钟告警一次。 - 600代表满足告警触发条件后每10分钟告警一次。 - 900代表满足告警触发条件后每15分钟告警一次。 - 1800代表满足告警触发条件后每30分钟告警一次。 - 3600代表满足告警触发条件后每60分钟告警一次。 - 10800代表满足告警触发条件后每3小时告警一次。 - 21600代表满足告警触发条件后每6小时告警一次。 - 43200代表满足告警触发条件后每12小时告警一次。 - 86000代表满足告警触发条件后每一天告警一次。 **默认取值**： 不涉及。 

        :param suppress_duration: The suppress_duration of this Policy.
        :type suppress_duration: int
        """
        self._suppress_duration = suppress_duration

    @property
    def level(self):
        r"""Gets the level of this Policy.

        **参数解释**： 告警级别。    **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。1为紧急，2为重要，3为次要，4为提示。         **默认取值**： 2 

        :return: The level of this Policy.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this Policy.

        **参数解释**： 告警级别。    **约束限制**： 不涉及。 **取值范围**： 只能为1、2、3、4。1为紧急，2为重要，3为次要，4为提示。         **默认取值**： 2 

        :param level: The level of this Policy.
        :type level: int
        """
        self._level = level

    @property
    def namespace(self):
        r"""Gets the namespace of this Policy.

        **参数解释**： 产品层级规则增加namespace（服务命名空间）和dimension_name（服务维度名称，用于指明生效策略的资源归属。各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在0到32个字符之间。 **默认取值**： 不涉及。 

        :return: The namespace of this Policy.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this Policy.

        **参数解释**： 产品层级规则增加namespace（服务命名空间）和dimension_name（服务维度名称，用于指明生效策略的资源归属。各服务命名空间请参考“[服务命名空间](ces_03_0059.xml)”。 **约束限制**： 不涉及。 **取值范围**： 格式为service.item；service和item必须是字符串，必须以字母开头，只能包含0-9/a-z/A-Z/_。字符串的长度必须在0到32个字符之间。 **默认取值**： 不涉及。 

        :param namespace: The namespace of this Policy.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dimension_name(self):
        r"""Gets the dimension_name of this Policy.

        **参数解释**： 指标维度名称，各服务资源的指标维度名称可查看：“[服务维度名称](ces_03_0059.xml)”。产品层级规则需要增加namespace（服务命名空间）和dimension_name（服务维度名称），用于指明策略生效的资源归属。 **约束限制**： 不涉及。 **取值范围**： 目前最大支持4个维度。举例：单维度场景：instance_id；多维度场景：instance_id,disk           **默认取值**： 不涉及。 

        :return: The dimension_name of this Policy.
        :rtype: str
        """
        return self._dimension_name

    @dimension_name.setter
    def dimension_name(self, dimension_name):
        r"""Sets the dimension_name of this Policy.

        **参数解释**： 指标维度名称，各服务资源的指标维度名称可查看：“[服务维度名称](ces_03_0059.xml)”。产品层级规则需要增加namespace（服务命名空间）和dimension_name（服务维度名称），用于指明策略生效的资源归属。 **约束限制**： 不涉及。 **取值范围**： 目前最大支持4个维度。举例：单维度场景：instance_id；多维度场景：instance_id,disk           **默认取值**： 不涉及。 

        :param dimension_name: The dimension_name of this Policy.
        :type dimension_name: str
        """
        self._dimension_name = dimension_name

    @property
    def enabled(self):
        r"""Gets the enabled of this Policy.

        **参数解释**: 告警策略是否生效。true：策略生效，false：策略无效。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :return: The enabled of this Policy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this Policy.

        **参数解释**: 告警策略是否生效。true：策略生效，false：策略无效。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。 

        :param enabled: The enabled of this Policy.
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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
