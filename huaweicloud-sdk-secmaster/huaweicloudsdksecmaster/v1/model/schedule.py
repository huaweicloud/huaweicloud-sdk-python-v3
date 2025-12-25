# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Schedule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delay_interval': 'int',
        'frequency_interval': 'int',
        'frequency_unit': 'str',
        'overtime_interval': 'int',
        'period_interval': 'int',
        'period_unit': 'str'
    }

    attribute_map = {
        'delay_interval': 'delay_interval',
        'frequency_interval': 'frequency_interval',
        'frequency_unit': 'frequency_unit',
        'overtime_interval': 'overtime_interval',
        'period_interval': 'period_interval',
        'period_unit': 'period_unit'
    }

    def __init__(self, delay_interval=None, frequency_interval=None, frequency_unit=None, overtime_interval=None, period_interval=None, period_unit=None):
        r"""Schedule

        The model defined in huaweicloud sdk

        :param delay_interval: 延迟间隔
        :type delay_interval: int
        :param frequency_interval: 调度间隔
        :type frequency_interval: int
        :param frequency_unit: **参数解释**: 调度间隔单位 - MINUTE10 10分钟 - HOUR 小时 - DAY 天  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY  **默认值** 不涉及
        :type frequency_unit: str
        :param overtime_interval: 超时间隔
        :type overtime_interval: int
        :param period_interval: 时间窗口间隔
        :type period_interval: int
        :param period_unit: **参数解释**: 时间窗口单位 - MINUTE10 10分钟 - HOUR 小时 - DAY 天  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY  **默认值** 不涉及
        :type period_unit: str
        """
        
        

        self._delay_interval = None
        self._frequency_interval = None
        self._frequency_unit = None
        self._overtime_interval = None
        self._period_interval = None
        self._period_unit = None
        self.discriminator = None

        if delay_interval is not None:
            self.delay_interval = delay_interval
        self.frequency_interval = frequency_interval
        self.frequency_unit = frequency_unit
        if overtime_interval is not None:
            self.overtime_interval = overtime_interval
        self.period_interval = period_interval
        self.period_unit = period_unit

    @property
    def delay_interval(self):
        r"""Gets the delay_interval of this Schedule.

        延迟间隔

        :return: The delay_interval of this Schedule.
        :rtype: int
        """
        return self._delay_interval

    @delay_interval.setter
    def delay_interval(self, delay_interval):
        r"""Sets the delay_interval of this Schedule.

        延迟间隔

        :param delay_interval: The delay_interval of this Schedule.
        :type delay_interval: int
        """
        self._delay_interval = delay_interval

    @property
    def frequency_interval(self):
        r"""Gets the frequency_interval of this Schedule.

        调度间隔

        :return: The frequency_interval of this Schedule.
        :rtype: int
        """
        return self._frequency_interval

    @frequency_interval.setter
    def frequency_interval(self, frequency_interval):
        r"""Sets the frequency_interval of this Schedule.

        调度间隔

        :param frequency_interval: The frequency_interval of this Schedule.
        :type frequency_interval: int
        """
        self._frequency_interval = frequency_interval

    @property
    def frequency_unit(self):
        r"""Gets the frequency_unit of this Schedule.

        **参数解释**: 调度间隔单位 - MINUTE10 10分钟 - HOUR 小时 - DAY 天  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY  **默认值** 不涉及

        :return: The frequency_unit of this Schedule.
        :rtype: str
        """
        return self._frequency_unit

    @frequency_unit.setter
    def frequency_unit(self, frequency_unit):
        r"""Sets the frequency_unit of this Schedule.

        **参数解释**: 调度间隔单位 - MINUTE10 10分钟 - HOUR 小时 - DAY 天  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY  **默认值** 不涉及

        :param frequency_unit: The frequency_unit of this Schedule.
        :type frequency_unit: str
        """
        self._frequency_unit = frequency_unit

    @property
    def overtime_interval(self):
        r"""Gets the overtime_interval of this Schedule.

        超时间隔

        :return: The overtime_interval of this Schedule.
        :rtype: int
        """
        return self._overtime_interval

    @overtime_interval.setter
    def overtime_interval(self, overtime_interval):
        r"""Sets the overtime_interval of this Schedule.

        超时间隔

        :param overtime_interval: The overtime_interval of this Schedule.
        :type overtime_interval: int
        """
        self._overtime_interval = overtime_interval

    @property
    def period_interval(self):
        r"""Gets the period_interval of this Schedule.

        时间窗口间隔

        :return: The period_interval of this Schedule.
        :rtype: int
        """
        return self._period_interval

    @period_interval.setter
    def period_interval(self, period_interval):
        r"""Sets the period_interval of this Schedule.

        时间窗口间隔

        :param period_interval: The period_interval of this Schedule.
        :type period_interval: int
        """
        self._period_interval = period_interval

    @property
    def period_unit(self):
        r"""Gets the period_unit of this Schedule.

        **参数解释**: 时间窗口单位 - MINUTE10 10分钟 - HOUR 小时 - DAY 天  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY  **默认值** 不涉及

        :return: The period_unit of this Schedule.
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        r"""Sets the period_unit of this Schedule.

        **参数解释**: 时间窗口单位 - MINUTE10 10分钟 - HOUR 小时 - DAY 天  **约束限制** 不涉及 **取值范围**: - MINUTE - HOUR - DAY  **默认值** 不涉及

        :param period_unit: The period_unit of this Schedule.
        :type period_unit: str
        """
        self._period_unit = period_unit

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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
