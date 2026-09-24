# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyYearlyRetentionRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retention_type': 'str',
        'retention_months': 'list[str]',
        'retention_weeks': 'list[str]',
        'days_of_month': 'list[int]',
        'days_of_week': 'list[str]',
        'retention_duration_periods': 'int'
    }

    attribute_map = {
        'retention_type': 'retention_type',
        'retention_months': 'retention_months',
        'retention_weeks': 'retention_weeks',
        'days_of_month': 'days_of_month',
        'days_of_week': 'days_of_week',
        'retention_duration_periods': 'retention_duration_periods'
    }

    def __init__(self, retention_type=None, retention_months=None, retention_weeks=None, days_of_month=None, days_of_week=None, retention_duration_periods=None):
        r"""PolicyYearlyRetentionRules

        The model defined in huaweicloud sdk

        :param retention_type: 年备规则的类型
        :type retention_type: str
        :param retention_months: 将每年中指定月份的备份设置为年备备份，当retention_type为Weekly时，需要与retention_weeks和days_of_week共同设置，当retention_type为Monthly时，需要与days_of_month共同设置
        :type retention_months: list[str]
        :param retention_weeks: 将选中月份的第几个星期的备份设置为年备备份，当retention_type为Weekly时才能设置，设置时需要与retention_months和days_of_week共同设置
        :type retention_weeks: list[str]
        :param days_of_month: 表示将选中月份的指定天的备份设置为年备备份，当retention_type为Monthly时才能设置，取值范围为1-28和-1，-1代表每个月的最后一天，需要与retention_months共同设置
        :type days_of_month: list[int]
        :param days_of_week: 设置指定月份的指定星期中的指定天的备份为年备备份，当retention_type为Weekly时才能设置，设置时需要与retention_weeks和retention_months共同设置
        :type days_of_week: list[str]
        :param retention_duration_periods: 年备备份的保留时间，取值范围为1-100，以及-1，单位为年，-1代表年备策略不启用
        :type retention_duration_periods: int
        """
        
        

        self._retention_type = None
        self._retention_months = None
        self._retention_weeks = None
        self._days_of_month = None
        self._days_of_week = None
        self._retention_duration_periods = None
        self.discriminator = None

        if retention_type is not None:
            self.retention_type = retention_type
        if retention_months is not None:
            self.retention_months = retention_months
        if retention_weeks is not None:
            self.retention_weeks = retention_weeks
        if days_of_month is not None:
            self.days_of_month = days_of_month
        if days_of_week is not None:
            self.days_of_week = days_of_week
        if retention_duration_periods is not None:
            self.retention_duration_periods = retention_duration_periods

    @property
    def retention_type(self):
        r"""Gets the retention_type of this PolicyYearlyRetentionRules.

        年备规则的类型

        :return: The retention_type of this PolicyYearlyRetentionRules.
        :rtype: str
        """
        return self._retention_type

    @retention_type.setter
    def retention_type(self, retention_type):
        r"""Sets the retention_type of this PolicyYearlyRetentionRules.

        年备规则的类型

        :param retention_type: The retention_type of this PolicyYearlyRetentionRules.
        :type retention_type: str
        """
        self._retention_type = retention_type

    @property
    def retention_months(self):
        r"""Gets the retention_months of this PolicyYearlyRetentionRules.

        将每年中指定月份的备份设置为年备备份，当retention_type为Weekly时，需要与retention_weeks和days_of_week共同设置，当retention_type为Monthly时，需要与days_of_month共同设置

        :return: The retention_months of this PolicyYearlyRetentionRules.
        :rtype: list[str]
        """
        return self._retention_months

    @retention_months.setter
    def retention_months(self, retention_months):
        r"""Sets the retention_months of this PolicyYearlyRetentionRules.

        将每年中指定月份的备份设置为年备备份，当retention_type为Weekly时，需要与retention_weeks和days_of_week共同设置，当retention_type为Monthly时，需要与days_of_month共同设置

        :param retention_months: The retention_months of this PolicyYearlyRetentionRules.
        :type retention_months: list[str]
        """
        self._retention_months = retention_months

    @property
    def retention_weeks(self):
        r"""Gets the retention_weeks of this PolicyYearlyRetentionRules.

        将选中月份的第几个星期的备份设置为年备备份，当retention_type为Weekly时才能设置，设置时需要与retention_months和days_of_week共同设置

        :return: The retention_weeks of this PolicyYearlyRetentionRules.
        :rtype: list[str]
        """
        return self._retention_weeks

    @retention_weeks.setter
    def retention_weeks(self, retention_weeks):
        r"""Sets the retention_weeks of this PolicyYearlyRetentionRules.

        将选中月份的第几个星期的备份设置为年备备份，当retention_type为Weekly时才能设置，设置时需要与retention_months和days_of_week共同设置

        :param retention_weeks: The retention_weeks of this PolicyYearlyRetentionRules.
        :type retention_weeks: list[str]
        """
        self._retention_weeks = retention_weeks

    @property
    def days_of_month(self):
        r"""Gets the days_of_month of this PolicyYearlyRetentionRules.

        表示将选中月份的指定天的备份设置为年备备份，当retention_type为Monthly时才能设置，取值范围为1-28和-1，-1代表每个月的最后一天，需要与retention_months共同设置

        :return: The days_of_month of this PolicyYearlyRetentionRules.
        :rtype: list[int]
        """
        return self._days_of_month

    @days_of_month.setter
    def days_of_month(self, days_of_month):
        r"""Sets the days_of_month of this PolicyYearlyRetentionRules.

        表示将选中月份的指定天的备份设置为年备备份，当retention_type为Monthly时才能设置，取值范围为1-28和-1，-1代表每个月的最后一天，需要与retention_months共同设置

        :param days_of_month: The days_of_month of this PolicyYearlyRetentionRules.
        :type days_of_month: list[int]
        """
        self._days_of_month = days_of_month

    @property
    def days_of_week(self):
        r"""Gets the days_of_week of this PolicyYearlyRetentionRules.

        设置指定月份的指定星期中的指定天的备份为年备备份，当retention_type为Weekly时才能设置，设置时需要与retention_weeks和retention_months共同设置

        :return: The days_of_week of this PolicyYearlyRetentionRules.
        :rtype: list[str]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        r"""Sets the days_of_week of this PolicyYearlyRetentionRules.

        设置指定月份的指定星期中的指定天的备份为年备备份，当retention_type为Weekly时才能设置，设置时需要与retention_weeks和retention_months共同设置

        :param days_of_week: The days_of_week of this PolicyYearlyRetentionRules.
        :type days_of_week: list[str]
        """
        self._days_of_week = days_of_week

    @property
    def retention_duration_periods(self):
        r"""Gets the retention_duration_periods of this PolicyYearlyRetentionRules.

        年备备份的保留时间，取值范围为1-100，以及-1，单位为年，-1代表年备策略不启用

        :return: The retention_duration_periods of this PolicyYearlyRetentionRules.
        :rtype: int
        """
        return self._retention_duration_periods

    @retention_duration_periods.setter
    def retention_duration_periods(self, retention_duration_periods):
        r"""Sets the retention_duration_periods of this PolicyYearlyRetentionRules.

        年备备份的保留时间，取值范围为1-100，以及-1，单位为年，-1代表年备策略不启用

        :param retention_duration_periods: The retention_duration_periods of this PolicyYearlyRetentionRules.
        :type retention_duration_periods: int
        """
        self._retention_duration_periods = retention_duration_periods

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
        if not isinstance(other, PolicyYearlyRetentionRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
