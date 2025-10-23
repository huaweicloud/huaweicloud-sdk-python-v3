# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateComplianceRuleRequestBodyLocalBackupFrequency:

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
        'interval': 'int',
        'times_per_day': 'int',
        'days_of_week': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'interval': 'interval',
        'times_per_day': 'times_per_day',
        'days_of_week': 'days_of_week'
    }

    def __init__(self, type=None, interval=None, times_per_day=None, days_of_week=None):
        r"""UpdateComplianceRuleRequestBodyLocalBackupFrequency

        The model defined in huaweicloud sdk

        :param type: 备份频率类型，可选daily weekly
        :type type: str
        :param interval: daily类型下，间隔多少天，默认值：1
        :type interval: int
        :param times_per_day: 每日执行次数
        :type times_per_day: int
        :param days_of_week: 如果type是weekly必选，表示一周内那些天备份 如：[\&quot;MO\&quot;, \&quot;TU\&quot;, \&quot;WE\&quot;, \&quot;TH\&quot;, \&quot;FR\&quot;, \&quot;SA\&quot;, \&quot;SU\&quot;]
        :type days_of_week: list[str]
        """
        
        

        self._type = None
        self._interval = None
        self._times_per_day = None
        self._days_of_week = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if interval is not None:
            self.interval = interval
        self.times_per_day = times_per_day
        if days_of_week is not None:
            self.days_of_week = days_of_week

    @property
    def type(self):
        r"""Gets the type of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.

        备份频率类型，可选daily weekly

        :return: The type of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.

        备份频率类型，可选daily weekly

        :param type: The type of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.
        :type type: str
        """
        self._type = type

    @property
    def interval(self):
        r"""Gets the interval of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.

        daily类型下，间隔多少天，默认值：1

        :return: The interval of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.

        daily类型下，间隔多少天，默认值：1

        :param interval: The interval of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.
        :type interval: int
        """
        self._interval = interval

    @property
    def times_per_day(self):
        r"""Gets the times_per_day of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.

        每日执行次数

        :return: The times_per_day of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.
        :rtype: int
        """
        return self._times_per_day

    @times_per_day.setter
    def times_per_day(self, times_per_day):
        r"""Sets the times_per_day of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.

        每日执行次数

        :param times_per_day: The times_per_day of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.
        :type times_per_day: int
        """
        self._times_per_day = times_per_day

    @property
    def days_of_week(self):
        r"""Gets the days_of_week of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.

        如果type是weekly必选，表示一周内那些天备份 如：[\"MO\", \"TU\", \"WE\", \"TH\", \"FR\", \"SA\", \"SU\"]

        :return: The days_of_week of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.
        :rtype: list[str]
        """
        return self._days_of_week

    @days_of_week.setter
    def days_of_week(self, days_of_week):
        r"""Sets the days_of_week of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.

        如果type是weekly必选，表示一周内那些天备份 如：[\"MO\", \"TU\", \"WE\", \"TH\", \"FR\", \"SA\", \"SU\"]

        :param days_of_week: The days_of_week of this UpdateComplianceRuleRequestBodyLocalBackupFrequency.
        :type days_of_week: list[str]
        """
        self._days_of_week = days_of_week

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
        if not isinstance(other, UpdateComplianceRuleRequestBodyLocalBackupFrequency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
