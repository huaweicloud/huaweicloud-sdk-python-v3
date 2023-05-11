# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperationDefinitionRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'day_backups': 'int',
        'max_backups': 'int',
        'month_backups': 'int',
        'retention_duration_days': 'int',
        'timezone': 'str',
        'week_backups': 'int',
        'year_backups': 'int'
    }

    attribute_map = {
        'day_backups': 'day_backups',
        'max_backups': 'max_backups',
        'month_backups': 'month_backups',
        'retention_duration_days': 'retention_duration_days',
        'timezone': 'timezone',
        'week_backups': 'week_backups',
        'year_backups': 'year_backups'
    }

    def __init__(self, day_backups=None, max_backups=None, month_backups=None, retention_duration_days=None, timezone=None, week_backups=None, year_backups=None):
        """OperationDefinitionRequestInfo

        The model defined in huaweicloud sdk

        :param day_backups: 保留日备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。最小值：0,最大值：100
        :type day_backups: int
        :param max_backups: 单个备份对象自动备份的最大备份数。取值为-1或0-99999。-1代表不按备份数清理。若该字段和retention_duration_days字段同时为空，备份会永久保留。最小值：1,最大值：99999,缺省值：-1
        :type max_backups: int
        :param month_backups: 保留月备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。最小值：0, 最大值：100
        :type month_backups: int
        :param retention_duration_days: 备份保留时长，单位天。最长支持99999天。-1代表不按时间清理。若该字段和max_backups 参数同时为空，备份会永久保留。最小值：1, 最大值：99999, 缺省值：-1
        :type retention_duration_days: int
        :param timezone: 用户所在时区,格式形如UTC+08:00,若没有选择年备，月备，周备，日备中任一参数，则不能选择该参数。
        :type timezone: str
        :param week_backups: 保留周备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。
        :type week_backups: int
        :param year_backups: 保留年备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。最小值：0，最大值：100
        :type year_backups: int
        """
        
        

        self._day_backups = None
        self._max_backups = None
        self._month_backups = None
        self._retention_duration_days = None
        self._timezone = None
        self._week_backups = None
        self._year_backups = None
        self.discriminator = None

        if day_backups is not None:
            self.day_backups = day_backups
        if max_backups is not None:
            self.max_backups = max_backups
        if month_backups is not None:
            self.month_backups = month_backups
        if retention_duration_days is not None:
            self.retention_duration_days = retention_duration_days
        if timezone is not None:
            self.timezone = timezone
        if week_backups is not None:
            self.week_backups = week_backups
        if year_backups is not None:
            self.year_backups = year_backups

    @property
    def day_backups(self):
        """Gets the day_backups of this OperationDefinitionRequestInfo.

        保留日备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。最小值：0,最大值：100

        :return: The day_backups of this OperationDefinitionRequestInfo.
        :rtype: int
        """
        return self._day_backups

    @day_backups.setter
    def day_backups(self, day_backups):
        """Sets the day_backups of this OperationDefinitionRequestInfo.

        保留日备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。最小值：0,最大值：100

        :param day_backups: The day_backups of this OperationDefinitionRequestInfo.
        :type day_backups: int
        """
        self._day_backups = day_backups

    @property
    def max_backups(self):
        """Gets the max_backups of this OperationDefinitionRequestInfo.

        单个备份对象自动备份的最大备份数。取值为-1或0-99999。-1代表不按备份数清理。若该字段和retention_duration_days字段同时为空，备份会永久保留。最小值：1,最大值：99999,缺省值：-1

        :return: The max_backups of this OperationDefinitionRequestInfo.
        :rtype: int
        """
        return self._max_backups

    @max_backups.setter
    def max_backups(self, max_backups):
        """Sets the max_backups of this OperationDefinitionRequestInfo.

        单个备份对象自动备份的最大备份数。取值为-1或0-99999。-1代表不按备份数清理。若该字段和retention_duration_days字段同时为空，备份会永久保留。最小值：1,最大值：99999,缺省值：-1

        :param max_backups: The max_backups of this OperationDefinitionRequestInfo.
        :type max_backups: int
        """
        self._max_backups = max_backups

    @property
    def month_backups(self):
        """Gets the month_backups of this OperationDefinitionRequestInfo.

        保留月备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。最小值：0, 最大值：100

        :return: The month_backups of this OperationDefinitionRequestInfo.
        :rtype: int
        """
        return self._month_backups

    @month_backups.setter
    def month_backups(self, month_backups):
        """Sets the month_backups of this OperationDefinitionRequestInfo.

        保留月备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。最小值：0, 最大值：100

        :param month_backups: The month_backups of this OperationDefinitionRequestInfo.
        :type month_backups: int
        """
        self._month_backups = month_backups

    @property
    def retention_duration_days(self):
        """Gets the retention_duration_days of this OperationDefinitionRequestInfo.

        备份保留时长，单位天。最长支持99999天。-1代表不按时间清理。若该字段和max_backups 参数同时为空，备份会永久保留。最小值：1, 最大值：99999, 缺省值：-1

        :return: The retention_duration_days of this OperationDefinitionRequestInfo.
        :rtype: int
        """
        return self._retention_duration_days

    @retention_duration_days.setter
    def retention_duration_days(self, retention_duration_days):
        """Sets the retention_duration_days of this OperationDefinitionRequestInfo.

        备份保留时长，单位天。最长支持99999天。-1代表不按时间清理。若该字段和max_backups 参数同时为空，备份会永久保留。最小值：1, 最大值：99999, 缺省值：-1

        :param retention_duration_days: The retention_duration_days of this OperationDefinitionRequestInfo.
        :type retention_duration_days: int
        """
        self._retention_duration_days = retention_duration_days

    @property
    def timezone(self):
        """Gets the timezone of this OperationDefinitionRequestInfo.

        用户所在时区,格式形如UTC+08:00,若没有选择年备，月备，周备，日备中任一参数，则不能选择该参数。

        :return: The timezone of this OperationDefinitionRequestInfo.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this OperationDefinitionRequestInfo.

        用户所在时区,格式形如UTC+08:00,若没有选择年备，月备，周备，日备中任一参数，则不能选择该参数。

        :param timezone: The timezone of this OperationDefinitionRequestInfo.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def week_backups(self):
        """Gets the week_backups of this OperationDefinitionRequestInfo.

        保留周备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。

        :return: The week_backups of this OperationDefinitionRequestInfo.
        :rtype: int
        """
        return self._week_backups

    @week_backups.setter
    def week_backups(self, week_backups):
        """Sets the week_backups of this OperationDefinitionRequestInfo.

        保留周备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。

        :param week_backups: The week_backups of this OperationDefinitionRequestInfo.
        :type week_backups: int
        """
        self._week_backups = week_backups

    @property
    def year_backups(self):
        """Gets the year_backups of this OperationDefinitionRequestInfo.

        保留年备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。最小值：0，最大值：100

        :return: The year_backups of this OperationDefinitionRequestInfo.
        :rtype: int
        """
        return self._year_backups

    @year_backups.setter
    def year_backups(self, year_backups):
        """Sets the year_backups of this OperationDefinitionRequestInfo.

        保留年备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。最小值：0，最大值：100

        :param year_backups: The year_backups of this OperationDefinitionRequestInfo.
        :type year_backups: int
        """
        self._year_backups = year_backups

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
        if not isinstance(other, OperationDefinitionRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
