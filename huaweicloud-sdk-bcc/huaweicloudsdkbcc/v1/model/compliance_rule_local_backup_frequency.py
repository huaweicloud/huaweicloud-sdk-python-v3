# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComplianceRuleLocalBackupFrequency:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'times_per_day': 'int',
        'interval': 'int',
        'days_of_week': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'times_per_day': 'times_per_day',
        'interval': 'interval',
        'days_of_week': 'days_of_week'
    }

    def __init__(self, type=None, times_per_day=None, interval=None, days_of_week=None):
        r"""ComplianceRuleLocalBackupFrequency

        The model defined in huaweicloud sdk

        :param type: 备份频率类型，可选daily weekly
        :type type: str
        :param times_per_day: 每日执行次数
        :type times_per_day: int
        :param interval: daily类型下，间隔多少天，默认值：1
        :type interval: int
        :param days_of_week: 如果type是weekly必选，表示一周内那些天备份 如：[\&quot;MO\&quot;, \&quot;TU\&quot;, \&quot;WE\&quot;, \&quot;TH\&quot;, \&quot;FR\&quot;, \&quot;SA\&quot;, \&quot;SU\&quot;]
        :type days_of_week: list[str]
        """
        
        

        self._type = None
        self._times_per_day = None
        self._interval = None
        self._days_of_week = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.times_per_day = times_per_day
        if interval is not None:
            self.interval = interval
        if days_of_week is not None:
            self.days_of_week = days_of_week

    @property
    def type(self):
        r"""Gets the type of this ComplianceRuleLocalBackupFrequency.

        备份频率类型，可选daily weekly

        :return: The type of this ComplianceRuleLocalBackupFrequency.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ComplianceRuleLocalBackupFrequency.

        备份频率类型，可选daily weekly

        :param type: The type of this ComplianceRuleLocalBackupFrequency.
        :type type: str
        """
        self._type = type

    @property
    def times_per_day(self):
        r"""Gets the times_per_day of this ComplianceRuleLocalBackupFrequency.

        每日执行次数

        :return: The times_per_day of this ComplianceRuleLocalBackupFrequency.
        :rtype: int
        """
        return self._times_per_day

    @times_per_day.setter
    def times_per_day(self, times_per_day):
        r"""Sets the times_per_day of this ComplianceRuleLocalBackupFrequency.

        每日执行次数

        :param times_per_day: The times_per_day of this ComplianceRuleLocalBackupFrequency.
        :type times_per_day: int
        """
        self._times_per_day = times_per_day

    @property
    def interval(self):
        r"""Gets the interval of this ComplianceRuleLocalBackupFrequency.

        daily类型下，间隔多少天，默认值：1

        :return: The interval of this ComplianceRuleLocalBackupFrequency.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this ComplianceRuleLocalBackupFrequency.

        daily类型下，间隔多少天，默认值：1

        :param interval: The interval of this ComplianceRuleLocalBackupFrequency.
        :type interval: int
        """
        self._interval = interval

    @property
    def days_of_week(self):
        r"""Gets the days_of_week of this ComplianceRuleLocalBackupFrequency.

        如果type是weekly必选，表示一周内那些天备份 如：[\"MO\", \"TU\", \"WE\", \"TH\", \"FR\", \"SA\", \"SU\"]

        :return: The days_of_week of this ComplianceRuleLocalBackupFrequency.
        :rtype: list[str]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        r"""Sets the days_of_week of this ComplianceRuleLocalBackupFrequency.

        如果type是weekly必选，表示一周内那些天备份 如：[\"MO\", \"TU\", \"WE\", \"TH\", \"FR\", \"SA\", \"SU\"]

        :param days_of_week: The days_of_week of this ComplianceRuleLocalBackupFrequency.
        :type days_of_week: list[str]
        """
        self._days_of_week = days_of_week

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
        if not isinstance(other, ComplianceRuleLocalBackupFrequency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
