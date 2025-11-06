# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobScheduleFrequencyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'freq_type': 'str',
        'freq_interval': 'int',
        'freq_interval_weekly': 'list[str]',
        'freq_interval_day_monthly': 'int',
        'freq_interval_monthly': 'str',
        'freq_relative_interval_monthly': 'str'
    }

    attribute_map = {
        'freq_type': 'freq_type',
        'freq_interval': 'freq_interval',
        'freq_interval_weekly': 'freq_interval_weekly',
        'freq_interval_day_monthly': 'freq_interval_day_monthly',
        'freq_interval_monthly': 'freq_interval_monthly',
        'freq_relative_interval_monthly': 'freq_relative_interval_monthly'
    }

    def __init__(self, freq_type=None, freq_interval=None, freq_interval_weekly=None, freq_interval_day_monthly=None, freq_interval_monthly=None, freq_relative_interval_monthly=None):
        r"""JobScheduleFrequencyInfo

        The model defined in huaweicloud sdk

        :param freq_type: 策略频率类型 daily:按天, weekly:按周, monthly_day:按月、每月按天, monthly_week:按月、每月按周。
        :type freq_type: str
        :param freq_interval: 执行间隔。取值范围1至99。
        :type freq_interval: int
        :param freq_interval_weekly: 频率类型为按周时该参数必传，不为按周时不生效。 每周执行哪几天。参数值：Monday，Tuesday … Sunday
        :type freq_interval_weekly: list[str]
        :param freq_interval_day_monthly: 频率类型为按月、每月按天时该参数必传，不为按月、每月按天时时不生效。 每月执行的日期。取值范围1-31。
        :type freq_interval_day_monthly: int
        :param freq_interval_monthly: 频率类型为按月、每月按周时该参数必传，不为按月、每月按周时时不生效。 每周执行哪几天。 Sunday, Monday,Tuesday ... Saturday, day, weekday, weekend
        :type freq_interval_monthly: str
        :param freq_relative_interval_monthly: 频率类型为按月、每月按周时该参数必传，不为按月、每月按周时时不生效。 每月在哪周执行。 first, second, third, fourth, last
        :type freq_relative_interval_monthly: str
        """
        
        

        self._freq_type = None
        self._freq_interval = None
        self._freq_interval_weekly = None
        self._freq_interval_day_monthly = None
        self._freq_interval_monthly = None
        self._freq_relative_interval_monthly = None
        self.discriminator = None

        if freq_type is not None:
            self.freq_type = freq_type
        if freq_interval is not None:
            self.freq_interval = freq_interval
        if freq_interval_weekly is not None:
            self.freq_interval_weekly = freq_interval_weekly
        if freq_interval_day_monthly is not None:
            self.freq_interval_day_monthly = freq_interval_day_monthly
        if freq_interval_monthly is not None:
            self.freq_interval_monthly = freq_interval_monthly
        if freq_relative_interval_monthly is not None:
            self.freq_relative_interval_monthly = freq_relative_interval_monthly

    @property
    def freq_type(self):
        r"""Gets the freq_type of this JobScheduleFrequencyInfo.

        策略频率类型 daily:按天, weekly:按周, monthly_day:按月、每月按天, monthly_week:按月、每月按周。

        :return: The freq_type of this JobScheduleFrequencyInfo.
        :rtype: str
        """
        return self._freq_type

    @freq_type.setter
    def freq_type(self, freq_type):
        r"""Sets the freq_type of this JobScheduleFrequencyInfo.

        策略频率类型 daily:按天, weekly:按周, monthly_day:按月、每月按天, monthly_week:按月、每月按周。

        :param freq_type: The freq_type of this JobScheduleFrequencyInfo.
        :type freq_type: str
        """
        self._freq_type = freq_type

    @property
    def freq_interval(self):
        r"""Gets the freq_interval of this JobScheduleFrequencyInfo.

        执行间隔。取值范围1至99。

        :return: The freq_interval of this JobScheduleFrequencyInfo.
        :rtype: int
        """
        return self._freq_interval

    @freq_interval.setter
    def freq_interval(self, freq_interval):
        r"""Sets the freq_interval of this JobScheduleFrequencyInfo.

        执行间隔。取值范围1至99。

        :param freq_interval: The freq_interval of this JobScheduleFrequencyInfo.
        :type freq_interval: int
        """
        self._freq_interval = freq_interval

    @property
    def freq_interval_weekly(self):
        r"""Gets the freq_interval_weekly of this JobScheduleFrequencyInfo.

        频率类型为按周时该参数必传，不为按周时不生效。 每周执行哪几天。参数值：Monday，Tuesday … Sunday

        :return: The freq_interval_weekly of this JobScheduleFrequencyInfo.
        :rtype: list[str]
        """
        return self._freq_interval_weekly

    @freq_interval_weekly.setter
    def freq_interval_weekly(self, freq_interval_weekly):
        r"""Sets the freq_interval_weekly of this JobScheduleFrequencyInfo.

        频率类型为按周时该参数必传，不为按周时不生效。 每周执行哪几天。参数值：Monday，Tuesday … Sunday

        :param freq_interval_weekly: The freq_interval_weekly of this JobScheduleFrequencyInfo.
        :type freq_interval_weekly: list[str]
        """
        self._freq_interval_weekly = freq_interval_weekly

    @property
    def freq_interval_day_monthly(self):
        r"""Gets the freq_interval_day_monthly of this JobScheduleFrequencyInfo.

        频率类型为按月、每月按天时该参数必传，不为按月、每月按天时时不生效。 每月执行的日期。取值范围1-31。

        :return: The freq_interval_day_monthly of this JobScheduleFrequencyInfo.
        :rtype: int
        """
        return self._freq_interval_day_monthly

    @freq_interval_day_monthly.setter
    def freq_interval_day_monthly(self, freq_interval_day_monthly):
        r"""Sets the freq_interval_day_monthly of this JobScheduleFrequencyInfo.

        频率类型为按月、每月按天时该参数必传，不为按月、每月按天时时不生效。 每月执行的日期。取值范围1-31。

        :param freq_interval_day_monthly: The freq_interval_day_monthly of this JobScheduleFrequencyInfo.
        :type freq_interval_day_monthly: int
        """
        self._freq_interval_day_monthly = freq_interval_day_monthly

    @property
    def freq_interval_monthly(self):
        r"""Gets the freq_interval_monthly of this JobScheduleFrequencyInfo.

        频率类型为按月、每月按周时该参数必传，不为按月、每月按周时时不生效。 每周执行哪几天。 Sunday, Monday,Tuesday ... Saturday, day, weekday, weekend

        :return: The freq_interval_monthly of this JobScheduleFrequencyInfo.
        :rtype: str
        """
        return self._freq_interval_monthly

    @freq_interval_monthly.setter
    def freq_interval_monthly(self, freq_interval_monthly):
        r"""Sets the freq_interval_monthly of this JobScheduleFrequencyInfo.

        频率类型为按月、每月按周时该参数必传，不为按月、每月按周时时不生效。 每周执行哪几天。 Sunday, Monday,Tuesday ... Saturday, day, weekday, weekend

        :param freq_interval_monthly: The freq_interval_monthly of this JobScheduleFrequencyInfo.
        :type freq_interval_monthly: str
        """
        self._freq_interval_monthly = freq_interval_monthly

    @property
    def freq_relative_interval_monthly(self):
        r"""Gets the freq_relative_interval_monthly of this JobScheduleFrequencyInfo.

        频率类型为按月、每月按周时该参数必传，不为按月、每月按周时时不生效。 每月在哪周执行。 first, second, third, fourth, last

        :return: The freq_relative_interval_monthly of this JobScheduleFrequencyInfo.
        :rtype: str
        """
        return self._freq_relative_interval_monthly

    @freq_relative_interval_monthly.setter
    def freq_relative_interval_monthly(self, freq_relative_interval_monthly):
        r"""Sets the freq_relative_interval_monthly of this JobScheduleFrequencyInfo.

        频率类型为按月、每月按周时该参数必传，不为按月、每月按周时时不生效。 每月在哪周执行。 first, second, third, fourth, last

        :param freq_relative_interval_monthly: The freq_relative_interval_monthly of this JobScheduleFrequencyInfo.
        :type freq_relative_interval_monthly: str
        """
        self._freq_relative_interval_monthly = freq_relative_interval_monthly

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
        if not isinstance(other, JobScheduleFrequencyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
