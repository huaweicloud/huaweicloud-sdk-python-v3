# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmHistoryItemV2Condition:

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
        r"""AlarmHistoryItemV2Condition

        The model defined in huaweicloud sdk

        :param period: **参数解释**： 指标周期，单位是秒。如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”。 **取值范围**： 0是默认值，例如事件类告警该字段就用0即可； 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算； 300代表指标按5分钟聚合周期为一个数据点参与告警计算； 1200代表指标按20分钟聚合周期为一个数据点参与告警计算； 3600代表指标按60分钟聚合周期为一个数据点参与告警计算； 14400代表指标按4小时聚合周期为一个数据点参与告警计算； 86400代表指标按1天聚合周期为一个数据点参与告警计算。 
        :type period: int
        :param filter: **参数解释**： 聚合方式。 **取值范围**： 枚举值。average：平均值，min：最小值，max：最大值，sum：求和，tp99：99百分位数，tp95：95百分位数，tp90：90百分位数。字符长度在 1 到 15之间。 
        :type filter: str
        :param comparison_operator: **参数解释**： 阈值符号。 **取值范围**： 枚举值。支持的值为(&gt;|&lt;|&gt;&#x3D;|&lt;&#x3D;|&#x3D;|!&#x3D;|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。字符长度在 1 到 10之间。 
        :type comparison_operator: str
        :param value: **参数解释**： 告警阈值。 **取值范围**： 具体阈值取值请参见附录中各服务监控指标中取值范围，如[支持监控的服务列表](ces_03_0059.xml)中ECS的CPU使用率cpu_util取值范围可配置80。最小值为0，最大值为1.7976931348623157e+108。 
        :type value: float
        :param unit: **参数解释**： 数据的单位。 **取值范围**： 字符串长度最大为 32。 
        :type unit: str
        :param count: **参数解释**： 告警连续触发次数。 **取值范围**： 字符串长度在 1 到 180 之间。 
        :type count: int
        :param suppress_duration: **参数解释**： 告警抑制时间（告警周期），单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题。 **取值范围**： 0代表不抑制，满足条件即告警； 300代表满足告警触发条件后每5分钟告警一次； 600代表满足告警触发条件后每10分钟告警一次； 900代表满足告警触发条件后每15分钟告警一次； 1800代表满足告警触发条件后每30分钟告警一次； 3600代表满足告警触发条件后每60分钟告警一次； 10800代表满足告警触发条件后每3小时告警一次； 21600代表满足告警触发条件后每6小时告警一次； 43200代表满足告警触发条件后每12小时告警一次； 8600代表满足告警触发条件后每一天告警一次； 
        :type suppress_duration: int
        """
        
        

        self._period = None
        self._filter = None
        self._comparison_operator = None
        self._value = None
        self._unit = None
        self._count = None
        self._suppress_duration = None
        self.discriminator = None

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
        if suppress_duration is not None:
            self.suppress_duration = suppress_duration

    @property
    def period(self):
        r"""Gets the period of this AlarmHistoryItemV2Condition.

        **参数解释**： 指标周期，单位是秒。如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”。 **取值范围**： 0是默认值，例如事件类告警该字段就用0即可； 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算； 300代表指标按5分钟聚合周期为一个数据点参与告警计算； 1200代表指标按20分钟聚合周期为一个数据点参与告警计算； 3600代表指标按60分钟聚合周期为一个数据点参与告警计算； 14400代表指标按4小时聚合周期为一个数据点参与告警计算； 86400代表指标按1天聚合周期为一个数据点参与告警计算。 

        :return: The period of this AlarmHistoryItemV2Condition.
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this AlarmHistoryItemV2Condition.

        **参数解释**： 指标周期，单位是秒。如想了解各个云服务的指标原始周期可以参考“[支持服务列表](ces_03_0059.xml)”。 **取值范围**： 0是默认值，例如事件类告警该字段就用0即可； 1代表指标的原始周期，比如RDS监控指标原始周期是60s，表示该RDS指标按60s周期为一个数据点参与告警计算； 300代表指标按5分钟聚合周期为一个数据点参与告警计算； 1200代表指标按20分钟聚合周期为一个数据点参与告警计算； 3600代表指标按60分钟聚合周期为一个数据点参与告警计算； 14400代表指标按4小时聚合周期为一个数据点参与告警计算； 86400代表指标按1天聚合周期为一个数据点参与告警计算。 

        :param period: The period of this AlarmHistoryItemV2Condition.
        :type period: int
        """
        self._period = period

    @property
    def filter(self):
        r"""Gets the filter of this AlarmHistoryItemV2Condition.

        **参数解释**： 聚合方式。 **取值范围**： 枚举值。average：平均值，min：最小值，max：最大值，sum：求和，tp99：99百分位数，tp95：95百分位数，tp90：90百分位数。字符长度在 1 到 15之间。 

        :return: The filter of this AlarmHistoryItemV2Condition.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this AlarmHistoryItemV2Condition.

        **参数解释**： 聚合方式。 **取值范围**： 枚举值。average：平均值，min：最小值，max：最大值，sum：求和，tp99：99百分位数，tp95：95百分位数，tp90：90百分位数。字符长度在 1 到 15之间。 

        :param filter: The filter of this AlarmHistoryItemV2Condition.
        :type filter: str
        """
        self._filter = filter

    @property
    def comparison_operator(self):
        r"""Gets the comparison_operator of this AlarmHistoryItemV2Condition.

        **参数解释**： 阈值符号。 **取值范围**： 枚举值。支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。字符长度在 1 到 10之间。 

        :return: The comparison_operator of this AlarmHistoryItemV2Condition.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        r"""Sets the comparison_operator of this AlarmHistoryItemV2Condition.

        **参数解释**： 阈值符号。 **取值范围**： 枚举值。支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。字符长度在 1 到 10之间。 

        :param comparison_operator: The comparison_operator of this AlarmHistoryItemV2Condition.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def value(self):
        r"""Gets the value of this AlarmHistoryItemV2Condition.

        **参数解释**： 告警阈值。 **取值范围**： 具体阈值取值请参见附录中各服务监控指标中取值范围，如[支持监控的服务列表](ces_03_0059.xml)中ECS的CPU使用率cpu_util取值范围可配置80。最小值为0，最大值为1.7976931348623157e+108。 

        :return: The value of this AlarmHistoryItemV2Condition.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this AlarmHistoryItemV2Condition.

        **参数解释**： 告警阈值。 **取值范围**： 具体阈值取值请参见附录中各服务监控指标中取值范围，如[支持监控的服务列表](ces_03_0059.xml)中ECS的CPU使用率cpu_util取值范围可配置80。最小值为0，最大值为1.7976931348623157e+108。 

        :param value: The value of this AlarmHistoryItemV2Condition.
        :type value: float
        """
        self._value = value

    @property
    def unit(self):
        r"""Gets the unit of this AlarmHistoryItemV2Condition.

        **参数解释**： 数据的单位。 **取值范围**： 字符串长度最大为 32。 

        :return: The unit of this AlarmHistoryItemV2Condition.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this AlarmHistoryItemV2Condition.

        **参数解释**： 数据的单位。 **取值范围**： 字符串长度最大为 32。 

        :param unit: The unit of this AlarmHistoryItemV2Condition.
        :type unit: str
        """
        self._unit = unit

    @property
    def count(self):
        r"""Gets the count of this AlarmHistoryItemV2Condition.

        **参数解释**： 告警连续触发次数。 **取值范围**： 字符串长度在 1 到 180 之间。 

        :return: The count of this AlarmHistoryItemV2Condition.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this AlarmHistoryItemV2Condition.

        **参数解释**： 告警连续触发次数。 **取值范围**： 字符串长度在 1 到 180 之间。 

        :param count: The count of this AlarmHistoryItemV2Condition.
        :type count: int
        """
        self._count = count

    @property
    def suppress_duration(self):
        r"""Gets the suppress_duration of this AlarmHistoryItemV2Condition.

        **参数解释**： 告警抑制时间（告警周期），单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题。 **取值范围**： 0代表不抑制，满足条件即告警； 300代表满足告警触发条件后每5分钟告警一次； 600代表满足告警触发条件后每10分钟告警一次； 900代表满足告警触发条件后每15分钟告警一次； 1800代表满足告警触发条件后每30分钟告警一次； 3600代表满足告警触发条件后每60分钟告警一次； 10800代表满足告警触发条件后每3小时告警一次； 21600代表满足告警触发条件后每6小时告警一次； 43200代表满足告警触发条件后每12小时告警一次； 8600代表满足告警触发条件后每一天告警一次； 

        :return: The suppress_duration of this AlarmHistoryItemV2Condition.
        :rtype: int
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        r"""Sets the suppress_duration of this AlarmHistoryItemV2Condition.

        **参数解释**： 告警抑制时间（告警周期），单位为秒，对应页面上创建告警规则时告警策略最后一个字段，该字段主要为解决告警频繁的问题。 **取值范围**： 0代表不抑制，满足条件即告警； 300代表满足告警触发条件后每5分钟告警一次； 600代表满足告警触发条件后每10分钟告警一次； 900代表满足告警触发条件后每15分钟告警一次； 1800代表满足告警触发条件后每30分钟告警一次； 3600代表满足告警触发条件后每60分钟告警一次； 10800代表满足告警触发条件后每3小时告警一次； 21600代表满足告警触发条件后每6小时告警一次； 43200代表满足告警触发条件后每12小时告警一次； 8600代表满足告警触发条件后每一天告警一次； 

        :param suppress_duration: The suppress_duration of this AlarmHistoryItemV2Condition.
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
        if not isinstance(other, AlarmHistoryItemV2Condition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
