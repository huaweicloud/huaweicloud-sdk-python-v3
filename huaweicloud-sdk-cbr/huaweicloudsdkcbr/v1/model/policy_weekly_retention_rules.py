# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyWeeklyRetentionRules:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'days_of_week': 'list[str]',
        'retention_duration_periods': 'int'
    }

    attribute_map = {
        'days_of_week': 'days_of_week',
        'retention_duration_periods': 'retention_duration_periods'
    }

    def __init__(self, days_of_week=None, retention_duration_periods=None):
        r"""PolicyWeeklyRetentionRules

        The model defined in huaweicloud sdk

        :param days_of_week: 设置每个星期中的指定天为周备备份
        :type days_of_week: list[str]
        :param retention_duration_periods: 周备的保留时间，取值范围为1-5200，以及-1，单位为周，-1代表周备策略不启用
        :type retention_duration_periods: int
        """
        
        

        self._days_of_week = None
        self._retention_duration_periods = None
        self.discriminator = None

        if days_of_week is not None:
            self.days_of_week = days_of_week
        if retention_duration_periods is not None:
            self.retention_duration_periods = retention_duration_periods

    @property
    def days_of_week(self):
        r"""Gets the days_of_week of this PolicyWeeklyRetentionRules.

        设置每个星期中的指定天为周备备份

        :return: The days_of_week of this PolicyWeeklyRetentionRules.
        :rtype: list[str]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        r"""Sets the days_of_week of this PolicyWeeklyRetentionRules.

        设置每个星期中的指定天为周备备份

        :param days_of_week: The days_of_week of this PolicyWeeklyRetentionRules.
        :type days_of_week: list[str]
        """
        self._days_of_week = days_of_week

    @property
    def retention_duration_periods(self):
        r"""Gets the retention_duration_periods of this PolicyWeeklyRetentionRules.

        周备的保留时间，取值范围为1-5200，以及-1，单位为周，-1代表周备策略不启用

        :return: The retention_duration_periods of this PolicyWeeklyRetentionRules.
        :rtype: int
        """
        return self._retention_duration_periods

    @retention_duration_periods.setter
    def retention_duration_periods(self, retention_duration_periods):
        r"""Sets the retention_duration_periods of this PolicyWeeklyRetentionRules.

        周备的保留时间，取值范围为1-5200，以及-1，单位为周，-1代表周备策略不启用

        :param retention_duration_periods: The retention_duration_periods of this PolicyWeeklyRetentionRules.
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
        if not isinstance(other, PolicyWeeklyRetentionRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
