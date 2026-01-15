# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConditionResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'comparison_operator': 'str',
        'count': 'int',
        'filter': 'FilterResp',
        'period': 'PeriodResp',
        'unit': 'str',
        'value': 'float',
        'suppress_duration': 'SuppressDurationResp'
    }

    attribute_map = {
        'comparison_operator': 'comparison_operator',
        'count': 'count',
        'filter': 'filter',
        'period': 'period',
        'unit': 'unit',
        'value': 'value',
        'suppress_duration': 'suppress_duration'
    }

    def __init__(self, comparison_operator=None, count=None, filter=None, period=None, unit=None, value=None, suppress_duration=None):
        r"""ConditionResp

        The model defined in huaweicloud sdk

        :param comparison_operator: **参数解释**： 阈值符号。     **取值范围**： 支持的值为(&gt;|&lt;|&gt;&#x3D;|&lt;&#x3D;|&#x3D;|!&#x3D;|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。 
        :type comparison_operator: str
        :param count: **参数解释**： 触发告警的连续发生次数。 **取值范围**： 整数，取值范围[1, 5]。 
        :type count: int
        :param filter: 
        :type filter: :class:`huaweicloudsdkces.v1.FilterResp`
        :param period: 
        :type period: :class:`huaweicloudsdkces.v1.PeriodResp`
        :param unit: **参数解释**： 数据的单位。 **取值范围**： 长度为[0,32]个字符。 
        :type unit: str
        :param value: **参数解释**： 告警阈值。具体阈值取值请参见附录中各服务监控指标中取值范围，如[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/en-us/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)中ECS的CPU使用率cpu_util取值范围可配置80。 **取值范围**： 最小值为-1.7976931348623157e+108，最大值为1.7976931348623157e+108。 
        :type value: float
        :param suppress_duration: 
        :type suppress_duration: :class:`huaweicloudsdkces.v1.SuppressDurationResp`
        """
        
        

        self._comparison_operator = None
        self._count = None
        self._filter = None
        self._period = None
        self._unit = None
        self._value = None
        self._suppress_duration = None
        self.discriminator = None

        if comparison_operator is not None:
            self.comparison_operator = comparison_operator
        if count is not None:
            self.count = count
        if filter is not None:
            self.filter = filter
        if period is not None:
            self.period = period
        if unit is not None:
            self.unit = unit
        if value is not None:
            self.value = value
        if suppress_duration is not None:
            self.suppress_duration = suppress_duration

    @property
    def comparison_operator(self):
        r"""Gets the comparison_operator of this ConditionResp.

        **参数解释**： 阈值符号。     **取值范围**： 支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。 

        :return: The comparison_operator of this ConditionResp.
        :rtype: str
        """
        return self._comparison_operator

    @comparison_operator.setter
    def comparison_operator(self, comparison_operator):
        r"""Sets the comparison_operator of this ConditionResp.

        **参数解释**： 阈值符号。     **取值范围**： 支持的值为(>|<|>=|<=|=|!=|cycle_decrease|cycle_increase|cycle_wave);cycle_decrease为环比下降,cycle_increase为环比上升,cycle_wave为环比波动。 

        :param comparison_operator: The comparison_operator of this ConditionResp.
        :type comparison_operator: str
        """
        self._comparison_operator = comparison_operator

    @property
    def count(self):
        r"""Gets the count of this ConditionResp.

        **参数解释**： 触发告警的连续发生次数。 **取值范围**： 整数，取值范围[1, 5]。 

        :return: The count of this ConditionResp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ConditionResp.

        **参数解释**： 触发告警的连续发生次数。 **取值范围**： 整数，取值范围[1, 5]。 

        :param count: The count of this ConditionResp.
        :type count: int
        """
        self._count = count

    @property
    def filter(self):
        r"""Gets the filter of this ConditionResp.

        :return: The filter of this ConditionResp.
        :rtype: :class:`huaweicloudsdkces.v1.FilterResp`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ConditionResp.

        :param filter: The filter of this ConditionResp.
        :type filter: :class:`huaweicloudsdkces.v1.FilterResp`
        """
        self._filter = filter

    @property
    def period(self):
        r"""Gets the period of this ConditionResp.

        :return: The period of this ConditionResp.
        :rtype: :class:`huaweicloudsdkces.v1.PeriodResp`
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this ConditionResp.

        :param period: The period of this ConditionResp.
        :type period: :class:`huaweicloudsdkces.v1.PeriodResp`
        """
        self._period = period

    @property
    def unit(self):
        r"""Gets the unit of this ConditionResp.

        **参数解释**： 数据的单位。 **取值范围**： 长度为[0,32]个字符。 

        :return: The unit of this ConditionResp.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ConditionResp.

        **参数解释**： 数据的单位。 **取值范围**： 长度为[0,32]个字符。 

        :param unit: The unit of this ConditionResp.
        :type unit: str
        """
        self._unit = unit

    @property
    def value(self):
        r"""Gets the value of this ConditionResp.

        **参数解释**： 告警阈值。具体阈值取值请参见附录中各服务监控指标中取值范围，如[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/en-us/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)中ECS的CPU使用率cpu_util取值范围可配置80。 **取值范围**： 最小值为-1.7976931348623157e+108，最大值为1.7976931348623157e+108。 

        :return: The value of this ConditionResp.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ConditionResp.

        **参数解释**： 告警阈值。具体阈值取值请参见附录中各服务监控指标中取值范围，如[[支持监控的服务列表](https://support.huaweicloud.com/api-ces/ces_03_0059.html)](tag:hc)[[支持监控的服务列表](https://support.huaweicloud.com/intl/en-us/api-ces/ces_03_0059.html)](tag:hk)[[支持监控的服务列表](https://support.huaweicloud.com/eu/en-us/api-ces/ces_03_0059.html)](tag:hws_eu)[[支持监控的服务列表](ces_03_0059.xml)](tag:ax,cmcc,ctc,dt,dt_test,hcso_dt,fcs,fcs_vm,mix,g42,hk_g42,hk_sbc,hk_tm,hk_vdf,hws_ocb,ocb,sbc,srg)中ECS的CPU使用率cpu_util取值范围可配置80。 **取值范围**： 最小值为-1.7976931348623157e+108，最大值为1.7976931348623157e+108。 

        :param value: The value of this ConditionResp.
        :type value: float
        """
        self._value = value

    @property
    def suppress_duration(self):
        r"""Gets the suppress_duration of this ConditionResp.

        :return: The suppress_duration of this ConditionResp.
        :rtype: :class:`huaweicloudsdkces.v1.SuppressDurationResp`
        """
        return self._suppress_duration

    @suppress_duration.setter
    def suppress_duration(self, suppress_duration):
        r"""Sets the suppress_duration of this ConditionResp.

        :param suppress_duration: The suppress_duration of this ConditionResp.
        :type suppress_duration: :class:`huaweicloudsdkces.v1.SuppressDurationResp`
        """
        self._suppress_duration = suppress_duration

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
        if not isinstance(other, ConditionResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
