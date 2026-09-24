# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyMonthlyRetentionRules:

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
        'retention_weeks': 'list[str]',
        'days_of_week': 'list[str]',
        'days_of_month': 'list[int]',
        'retention_duration_periods': 'int'
    }

    attribute_map = {
        'retention_type': 'retention_type',
        'retention_weeks': 'retention_weeks',
        'days_of_week': 'days_of_week',
        'days_of_month': 'days_of_month',
        'retention_duration_periods': 'retention_duration_periods'
    }

    def __init__(self, retention_type=None, retention_weeks=None, days_of_week=None, days_of_month=None, retention_duration_periods=None):
        r"""PolicyMonthlyRetentionRules

        The model defined in huaweicloud sdk

        :param retention_type: 月备规则的类型
        :type retention_type: str
        :param retention_weeks: 将每月第几个星期的备份设置为月备备份，当retention_type为Weekly时才能设置，设置时需要与days_of_week共同设置
        :type retention_weeks: list[str]
        :param days_of_week: 设置选中的星期中的指定天的备份为月备备份，当retention_type为Weekly时才能设置，设置时需要与retention_weeks共同设置
        :type days_of_week: list[str]
        :param days_of_month: 表示将每个月中的指定天设置为月备备份，当retention_type为Monthly时才能设置，取值范围为1-28和-1，-1代表每个月的最后一天
        :type days_of_month: list[int]
        :param retention_duration_periods: 月备备份的保留时间，取值范围为1-1200，以及-1，单位为月，-1代表月备策略不启用
        :type retention_duration_periods: int
        """
        
        

        self._retention_type = None
        self._retention_weeks = None
        self._days_of_week = None
        self._days_of_month = None
        self._retention_duration_periods = None
        self.discriminator = None

        if retention_type is not None:
            self.retention_type = retention_type
        if retention_weeks is not None:
            self.retention_weeks = retention_weeks
        if days_of_week is not None:
            self.days_of_week = days_of_week
        if days_of_month is not None:
            self.days_of_month = days_of_month
        if retention_duration_periods is not None:
            self.retention_duration_periods = retention_duration_periods

    @property
    def retention_type(self):
        r"""Gets the retention_type of this PolicyMonthlyRetentionRules.

        月备规则的类型

        :return: The retention_type of this PolicyMonthlyRetentionRules.
        :rtype: str
        """
        return self._retention_type

    @retention_type.setter
    def retention_type(self, retention_type):
        r"""Sets the retention_type of this PolicyMonthlyRetentionRules.

        月备规则的类型

        :param retention_type: The retention_type of this PolicyMonthlyRetentionRules.
        :type retention_type: str
        """
        self._retention_type = retention_type

    @property
    def retention_weeks(self):
        r"""Gets the retention_weeks of this PolicyMonthlyRetentionRules.

        将每月第几个星期的备份设置为月备备份，当retention_type为Weekly时才能设置，设置时需要与days_of_week共同设置

        :return: The retention_weeks of this PolicyMonthlyRetentionRules.
        :rtype: list[str]
        """
        return self._retention_weeks

    @retention_weeks.setter
    def retention_weeks(self, retention_weeks):
        r"""Sets the retention_weeks of this PolicyMonthlyRetentionRules.

        将每月第几个星期的备份设置为月备备份，当retention_type为Weekly时才能设置，设置时需要与days_of_week共同设置

        :param retention_weeks: The retention_weeks of this PolicyMonthlyRetentionRules.
        :type retention_weeks: list[str]
        """
        self._retention_weeks = retention_weeks

    @property
    def days_of_week(self):
        r"""Gets the days_of_week of this PolicyMonthlyRetentionRules.

        设置选中的星期中的指定天的备份为月备备份，当retention_type为Weekly时才能设置，设置时需要与retention_weeks共同设置

        :return: The days_of_week of this PolicyMonthlyRetentionRules.
        :rtype: list[str]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        r"""Sets the days_of_week of this PolicyMonthlyRetentionRules.

        设置选中的星期中的指定天的备份为月备备份，当retention_type为Weekly时才能设置，设置时需要与retention_weeks共同设置

        :param days_of_week: The days_of_week of this PolicyMonthlyRetentionRules.
        :type days_of_week: list[str]
        """
        self._days_of_week = days_of_week

    @property
    def days_of_month(self):
        r"""Gets the days_of_month of this PolicyMonthlyRetentionRules.

        表示将每个月中的指定天设置为月备备份，当retention_type为Monthly时才能设置，取值范围为1-28和-1，-1代表每个月的最后一天

        :return: The days_of_month of this PolicyMonthlyRetentionRules.
        :rtype: list[int]
        """
        return self._days_of_month

    @days_of_month.setter
    def days_of_month(self, days_of_month):
        r"""Sets the days_of_month of this PolicyMonthlyRetentionRules.

        表示将每个月中的指定天设置为月备备份，当retention_type为Monthly时才能设置，取值范围为1-28和-1，-1代表每个月的最后一天

        :param days_of_month: The days_of_month of this PolicyMonthlyRetentionRules.
        :type days_of_month: list[int]
        """
        self._days_of_month = days_of_month

    @property
    def retention_duration_periods(self):
        r"""Gets the retention_duration_periods of this PolicyMonthlyRetentionRules.

        月备备份的保留时间，取值范围为1-1200，以及-1，单位为月，-1代表月备策略不启用

        :return: The retention_duration_periods of this PolicyMonthlyRetentionRules.
        :rtype: int
        """
        return self._retention_duration_periods

    @retention_duration_periods.setter
    def retention_duration_periods(self, retention_duration_periods):
        r"""Sets the retention_duration_periods of this PolicyMonthlyRetentionRules.

        月备备份的保留时间，取值范围为1-1200，以及-1，单位为月，-1代表月备策略不启用

        :param retention_duration_periods: The retention_duration_periods of this PolicyMonthlyRetentionRules.
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
        if not isinstance(other, PolicyMonthlyRetentionRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
