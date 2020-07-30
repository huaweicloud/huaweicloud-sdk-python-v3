# coding: utf-8

import pprint
import re

import six





class PolicyoODCreate:


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
        'destination_project_id': 'str',
        'destination_region': 'str',
        'enable_acceleration': 'bool',
        'max_backups': 'int',
        'month_backups': 'int',
        'retention_duration_days': 'int',
        'timezone': 'str',
        'week_backups': 'int',
        'year_backups': 'int'
    }

    attribute_map = {
        'day_backups': 'day_backups',
        'destination_project_id': 'destination_project_id',
        'destination_region': 'destination_region',
        'enable_acceleration': 'enable_acceleration',
        'max_backups': 'max_backups',
        'month_backups': 'month_backups',
        'retention_duration_days': 'retention_duration_days',
        'timezone': 'timezone',
        'week_backups': 'week_backups',
        'year_backups': 'year_backups'
    }

    def __init__(self, day_backups=None, destination_project_id=None, destination_region=None, enable_acceleration=None, max_backups=-1, month_backups=None, retention_duration_days=-1, timezone=None, week_backups=None, year_backups=None):
        """PolicyoODCreate - a model defined in huaweicloud sdk"""
        
        

        self._day_backups = None
        self._destination_project_id = None
        self._destination_region = None
        self._enable_acceleration = None
        self._max_backups = None
        self._month_backups = None
        self._retention_duration_days = None
        self._timezone = None
        self._week_backups = None
        self._year_backups = None
        self.discriminator = None

        if day_backups is not None:
            self.day_backups = day_backups
        if destination_project_id is not None:
            self.destination_project_id = destination_project_id
        if destination_region is not None:
            self.destination_region = destination_region
        if enable_acceleration is not None:
            self.enable_acceleration = enable_acceleration
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
        """Gets the day_backups of this PolicyoODCreate.

        保留日备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。

        :return: The day_backups of this PolicyoODCreate.
        :rtype: int
        """
        return self._day_backups

    @day_backups.setter
    def day_backups(self, day_backups):
        """Sets the day_backups of this PolicyoODCreate.

        保留日备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。

        :param day_backups: The day_backups of this PolicyoODCreate.
        :type: int
        """
        self._day_backups = day_backups

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this PolicyoODCreate.

        复制的目标项目ID，仅在跨区域复制时才会使用并且必须指定。

        :return: The destination_project_id of this PolicyoODCreate.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this PolicyoODCreate.

        复制的目标项目ID，仅在跨区域复制时才会使用并且必须指定。

        :param destination_project_id: The destination_project_id of this PolicyoODCreate.
        :type: str
        """
        self._destination_project_id = destination_project_id

    @property
    def destination_region(self):
        """Gets the destination_region of this PolicyoODCreate.

        复制的目标区域，仅在跨区域复制时才会使用并且必须指定。长度限制：0- 255，只能由字母、数字、“_”、“-”组成

        :return: The destination_region of this PolicyoODCreate.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this PolicyoODCreate.

        复制的目标区域，仅在跨区域复制时才会使用并且必须指定。长度限制：0- 255，只能由字母、数字、“_”、“-”组成

        :param destination_region: The destination_region of this PolicyoODCreate.
        :type: str
        """
        self._destination_region = destination_region

    @property
    def enable_acceleration(self):
        """Gets the enable_acceleration of this PolicyoODCreate.

        跨区域复制时，是否启用加速从而缩减复制的时间，如果不指定，默认不启用加速。

        :return: The enable_acceleration of this PolicyoODCreate.
        :rtype: bool
        """
        return self._enable_acceleration

    @enable_acceleration.setter
    def enable_acceleration(self, enable_acceleration):
        """Sets the enable_acceleration of this PolicyoODCreate.

        跨区域复制时，是否启用加速从而缩减复制的时间，如果不指定，默认不启用加速。

        :param enable_acceleration: The enable_acceleration of this PolicyoODCreate.
        :type: bool
        """
        self._enable_acceleration = enable_acceleration

    @property
    def max_backups(self):
        """Gets the max_backups of this PolicyoODCreate.

        单个备份对象自动备份的最大备份数。取值为-1或0-99999。-1代表不按备份数清理。若该字段和retention_duration_days字段同时为空，备份会永久保留。

        :return: The max_backups of this PolicyoODCreate.
        :rtype: int
        """
        return self._max_backups

    @max_backups.setter
    def max_backups(self, max_backups):
        """Sets the max_backups of this PolicyoODCreate.

        单个备份对象自动备份的最大备份数。取值为-1或0-99999。-1代表不按备份数清理。若该字段和retention_duration_days字段同时为空，备份会永久保留。

        :param max_backups: The max_backups of this PolicyoODCreate.
        :type: int
        """
        self._max_backups = max_backups

    @property
    def month_backups(self):
        """Gets the month_backups of this PolicyoODCreate.

        保留月备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。

        :return: The month_backups of this PolicyoODCreate.
        :rtype: int
        """
        return self._month_backups

    @month_backups.setter
    def month_backups(self, month_backups):
        """Sets the month_backups of this PolicyoODCreate.

        保留月备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。

        :param month_backups: The month_backups of this PolicyoODCreate.
        :type: int
        """
        self._month_backups = month_backups

    @property
    def retention_duration_days(self):
        """Gets the retention_duration_days of this PolicyoODCreate.

        备份保留时长，单位天。最长支持99999天。-1代表不按时间清理。若该字段和max_backups 参数同时为空，备份会永久保留。

        :return: The retention_duration_days of this PolicyoODCreate.
        :rtype: int
        """
        return self._retention_duration_days

    @retention_duration_days.setter
    def retention_duration_days(self, retention_duration_days):
        """Sets the retention_duration_days of this PolicyoODCreate.

        备份保留时长，单位天。最长支持99999天。-1代表不按时间清理。若该字段和max_backups 参数同时为空，备份会永久保留。

        :param retention_duration_days: The retention_duration_days of this PolicyoODCreate.
        :type: int
        """
        self._retention_duration_days = retention_duration_days

    @property
    def timezone(self):
        """Gets the timezone of this PolicyoODCreate.

        用户所在时区,格式形如UTC+08:00,若没有选择年备，月备，周备，日备中任一参数，则不能选择该参数。

        :return: The timezone of this PolicyoODCreate.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this PolicyoODCreate.

        用户所在时区,格式形如UTC+08:00,若没有选择年备，月备，周备，日备中任一参数，则不能选择该参数。

        :param timezone: The timezone of this PolicyoODCreate.
        :type: str
        """
        self._timezone = timezone

    @property
    def week_backups(self):
        """Gets the week_backups of this PolicyoODCreate.

        保留周备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。

        :return: The week_backups of this PolicyoODCreate.
        :rtype: int
        """
        return self._week_backups

    @week_backups.setter
    def week_backups(self, week_backups):
        """Sets the week_backups of this PolicyoODCreate.

        保留周备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。

        :param week_backups: The week_backups of this PolicyoODCreate.
        :type: int
        """
        self._week_backups = week_backups

    @property
    def year_backups(self):
        """Gets the year_backups of this PolicyoODCreate.

        保留年备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。

        :return: The year_backups of this PolicyoODCreate.
        :rtype: int
        """
        return self._year_backups

    @year_backups.setter
    def year_backups(self, year_backups):
        """Sets the year_backups of this PolicyoODCreate.

        保留年备个数，该备份不受保留最大备份数限制。取值为0到100。若选择该参数，则timezone 也必选。

        :param year_backups: The year_backups of this PolicyoODCreate.
        :type: int
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyoODCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
