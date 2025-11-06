# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbrPolicyDetailResourceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_acceleration': 'bool',
        'full_backup_interval': 'int',
        'destination_project_id': 'str',
        'operation_type': 'str',
        'timezone': 'str',
        'week_backups': 'int',
        'pattern': 'str',
        'destination_region': 'str',
        'retention_duration_days': 'int',
        'enabled': 'bool',
        'day_backups': 'int',
        'associate_vaults': 'list[BccPolicyAssociateVault]',
        'start_time': 'str',
        'max_backups': 'int',
        'year_backups': 'int',
        'month_backups': 'int',
        'cross_account_urn': 'str'
    }

    attribute_map = {
        'enable_acceleration': 'enable_acceleration',
        'full_backup_interval': 'full_backup_interval',
        'destination_project_id': 'destination_project_id',
        'operation_type': 'operation_type',
        'timezone': 'timezone',
        'week_backups': 'week_backups',
        'pattern': 'pattern',
        'destination_region': 'destination_region',
        'retention_duration_days': 'retention_duration_days',
        'enabled': 'enabled',
        'day_backups': 'day_backups',
        'associate_vaults': 'associate_vaults',
        'start_time': 'start_time',
        'max_backups': 'max_backups',
        'year_backups': 'year_backups',
        'month_backups': 'month_backups',
        'cross_account_urn': 'cross_account_urn'
    }

    def __init__(self, enable_acceleration=None, full_backup_interval=None, destination_project_id=None, operation_type=None, timezone=None, week_backups=None, pattern=None, destination_region=None, retention_duration_days=None, enabled=None, day_backups=None, associate_vaults=None, start_time=None, max_backups=None, year_backups=None, month_backups=None, cross_account_urn=None):
        r"""CbrPolicyDetailResourceDetail

        The model defined in huaweicloud sdk

        :param enable_acceleration: 跨区域复制时，是否启用加速从而缩减复制的时间，如果不指定，默认不启用加速。
        :type enable_acceleration: bool
        :param full_backup_interval: 每间隔多少次执行一次全量备份，当取值为 -1 时，不执行全量备份。最小值：-1，最大值：100。
        :type full_backup_interval: int
        :param destination_project_id: 复制的目标项目ID，仅在跨区域复制时才会使用并且必须指定。
        :type destination_project_id: str
        :param operation_type: 数据保护类型
        :type operation_type: str
        :param timezone: 用户所在时区,格式形如UTC+08:00。
        :type timezone: str
        :param week_backups: 保留周备个数，该备份不受保留最大备份数限制。取值为0到100。
        :type week_backups: int
        :param pattern: pattern
        :type pattern: str
        :param destination_region: 目标region
        :type destination_region: str
        :param retention_duration_days: 备份保留时长，单位天。最长支持99999天。-1代表不按时间清理。
        :type retention_duration_days: int
        :param enabled: 是否启用
        :type enabled: bool
        :param day_backups: 保留日备个数，该备份不受保留最大备份数限制。取值为0到100。
        :type day_backups: int
        :param associate_vaults: 管理存储库列表
        :type associate_vaults: list[:class:`huaweicloudsdkbcc.v1.BccPolicyAssociateVault`]
        :param start_time: 开始时间start_time
        :type start_time: str
        :param max_backups: 最大备份数量max_backups
        :type max_backups: int
        :param year_backups: 保留年备个数，该备份不受保留最大备份数限制。取值为0到100。
        :type year_backups: int
        :param month_backups: 保留月备个数，该备份不受保留最大备份数限制。取值为0到100。
        :type month_backups: int
        :param cross_account_urn: 账号备份的账号urn
        :type cross_account_urn: str
        """
        
        

        self._enable_acceleration = None
        self._full_backup_interval = None
        self._destination_project_id = None
        self._operation_type = None
        self._timezone = None
        self._week_backups = None
        self._pattern = None
        self._destination_region = None
        self._retention_duration_days = None
        self._enabled = None
        self._day_backups = None
        self._associate_vaults = None
        self._start_time = None
        self._max_backups = None
        self._year_backups = None
        self._month_backups = None
        self._cross_account_urn = None
        self.discriminator = None

        if enable_acceleration is not None:
            self.enable_acceleration = enable_acceleration
        if full_backup_interval is not None:
            self.full_backup_interval = full_backup_interval
        if destination_project_id is not None:
            self.destination_project_id = destination_project_id
        if operation_type is not None:
            self.operation_type = operation_type
        if timezone is not None:
            self.timezone = timezone
        if week_backups is not None:
            self.week_backups = week_backups
        if pattern is not None:
            self.pattern = pattern
        if destination_region is not None:
            self.destination_region = destination_region
        if retention_duration_days is not None:
            self.retention_duration_days = retention_duration_days
        if enabled is not None:
            self.enabled = enabled
        if day_backups is not None:
            self.day_backups = day_backups
        if associate_vaults is not None:
            self.associate_vaults = associate_vaults
        if start_time is not None:
            self.start_time = start_time
        if max_backups is not None:
            self.max_backups = max_backups
        if year_backups is not None:
            self.year_backups = year_backups
        if month_backups is not None:
            self.month_backups = month_backups
        if cross_account_urn is not None:
            self.cross_account_urn = cross_account_urn

    @property
    def enable_acceleration(self):
        r"""Gets the enable_acceleration of this CbrPolicyDetailResourceDetail.

        跨区域复制时，是否启用加速从而缩减复制的时间，如果不指定，默认不启用加速。

        :return: The enable_acceleration of this CbrPolicyDetailResourceDetail.
        :rtype: bool
        """
        return self._enable_acceleration

    @enable_acceleration.setter
    def enable_acceleration(self, enable_acceleration):
        r"""Sets the enable_acceleration of this CbrPolicyDetailResourceDetail.

        跨区域复制时，是否启用加速从而缩减复制的时间，如果不指定，默认不启用加速。

        :param enable_acceleration: The enable_acceleration of this CbrPolicyDetailResourceDetail.
        :type enable_acceleration: bool
        """
        self._enable_acceleration = enable_acceleration

    @property
    def full_backup_interval(self):
        r"""Gets the full_backup_interval of this CbrPolicyDetailResourceDetail.

        每间隔多少次执行一次全量备份，当取值为 -1 时，不执行全量备份。最小值：-1，最大值：100。

        :return: The full_backup_interval of this CbrPolicyDetailResourceDetail.
        :rtype: int
        """
        return self._full_backup_interval

    @full_backup_interval.setter
    def full_backup_interval(self, full_backup_interval):
        r"""Sets the full_backup_interval of this CbrPolicyDetailResourceDetail.

        每间隔多少次执行一次全量备份，当取值为 -1 时，不执行全量备份。最小值：-1，最大值：100。

        :param full_backup_interval: The full_backup_interval of this CbrPolicyDetailResourceDetail.
        :type full_backup_interval: int
        """
        self._full_backup_interval = full_backup_interval

    @property
    def destination_project_id(self):
        r"""Gets the destination_project_id of this CbrPolicyDetailResourceDetail.

        复制的目标项目ID，仅在跨区域复制时才会使用并且必须指定。

        :return: The destination_project_id of this CbrPolicyDetailResourceDetail.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        r"""Sets the destination_project_id of this CbrPolicyDetailResourceDetail.

        复制的目标项目ID，仅在跨区域复制时才会使用并且必须指定。

        :param destination_project_id: The destination_project_id of this CbrPolicyDetailResourceDetail.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

    @property
    def operation_type(self):
        r"""Gets the operation_type of this CbrPolicyDetailResourceDetail.

        数据保护类型

        :return: The operation_type of this CbrPolicyDetailResourceDetail.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this CbrPolicyDetailResourceDetail.

        数据保护类型

        :param operation_type: The operation_type of this CbrPolicyDetailResourceDetail.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def timezone(self):
        r"""Gets the timezone of this CbrPolicyDetailResourceDetail.

        用户所在时区,格式形如UTC+08:00。

        :return: The timezone of this CbrPolicyDetailResourceDetail.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        r"""Sets the timezone of this CbrPolicyDetailResourceDetail.

        用户所在时区,格式形如UTC+08:00。

        :param timezone: The timezone of this CbrPolicyDetailResourceDetail.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def week_backups(self):
        r"""Gets the week_backups of this CbrPolicyDetailResourceDetail.

        保留周备个数，该备份不受保留最大备份数限制。取值为0到100。

        :return: The week_backups of this CbrPolicyDetailResourceDetail.
        :rtype: int
        """
        return self._week_backups

    @week_backups.setter
    def week_backups(self, week_backups):
        r"""Sets the week_backups of this CbrPolicyDetailResourceDetail.

        保留周备个数，该备份不受保留最大备份数限制。取值为0到100。

        :param week_backups: The week_backups of this CbrPolicyDetailResourceDetail.
        :type week_backups: int
        """
        self._week_backups = week_backups

    @property
    def pattern(self):
        r"""Gets the pattern of this CbrPolicyDetailResourceDetail.

        pattern

        :return: The pattern of this CbrPolicyDetailResourceDetail.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this CbrPolicyDetailResourceDetail.

        pattern

        :param pattern: The pattern of this CbrPolicyDetailResourceDetail.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def destination_region(self):
        r"""Gets the destination_region of this CbrPolicyDetailResourceDetail.

        目标region

        :return: The destination_region of this CbrPolicyDetailResourceDetail.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        r"""Sets the destination_region of this CbrPolicyDetailResourceDetail.

        目标region

        :param destination_region: The destination_region of this CbrPolicyDetailResourceDetail.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def retention_duration_days(self):
        r"""Gets the retention_duration_days of this CbrPolicyDetailResourceDetail.

        备份保留时长，单位天。最长支持99999天。-1代表不按时间清理。

        :return: The retention_duration_days of this CbrPolicyDetailResourceDetail.
        :rtype: int
        """
        return self._retention_duration_days

    @retention_duration_days.setter
    def retention_duration_days(self, retention_duration_days):
        r"""Sets the retention_duration_days of this CbrPolicyDetailResourceDetail.

        备份保留时长，单位天。最长支持99999天。-1代表不按时间清理。

        :param retention_duration_days: The retention_duration_days of this CbrPolicyDetailResourceDetail.
        :type retention_duration_days: int
        """
        self._retention_duration_days = retention_duration_days

    @property
    def enabled(self):
        r"""Gets the enabled of this CbrPolicyDetailResourceDetail.

        是否启用

        :return: The enabled of this CbrPolicyDetailResourceDetail.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CbrPolicyDetailResourceDetail.

        是否启用

        :param enabled: The enabled of this CbrPolicyDetailResourceDetail.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def day_backups(self):
        r"""Gets the day_backups of this CbrPolicyDetailResourceDetail.

        保留日备个数，该备份不受保留最大备份数限制。取值为0到100。

        :return: The day_backups of this CbrPolicyDetailResourceDetail.
        :rtype: int
        """
        return self._day_backups

    @day_backups.setter
    def day_backups(self, day_backups):
        r"""Sets the day_backups of this CbrPolicyDetailResourceDetail.

        保留日备个数，该备份不受保留最大备份数限制。取值为0到100。

        :param day_backups: The day_backups of this CbrPolicyDetailResourceDetail.
        :type day_backups: int
        """
        self._day_backups = day_backups

    @property
    def associate_vaults(self):
        r"""Gets the associate_vaults of this CbrPolicyDetailResourceDetail.

        管理存储库列表

        :return: The associate_vaults of this CbrPolicyDetailResourceDetail.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.BccPolicyAssociateVault`]
        """
        return self._associate_vaults

    @associate_vaults.setter
    def associate_vaults(self, associate_vaults):
        r"""Sets the associate_vaults of this CbrPolicyDetailResourceDetail.

        管理存储库列表

        :param associate_vaults: The associate_vaults of this CbrPolicyDetailResourceDetail.
        :type associate_vaults: list[:class:`huaweicloudsdkbcc.v1.BccPolicyAssociateVault`]
        """
        self._associate_vaults = associate_vaults

    @property
    def start_time(self):
        r"""Gets the start_time of this CbrPolicyDetailResourceDetail.

        开始时间start_time

        :return: The start_time of this CbrPolicyDetailResourceDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CbrPolicyDetailResourceDetail.

        开始时间start_time

        :param start_time: The start_time of this CbrPolicyDetailResourceDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def max_backups(self):
        r"""Gets the max_backups of this CbrPolicyDetailResourceDetail.

        最大备份数量max_backups

        :return: The max_backups of this CbrPolicyDetailResourceDetail.
        :rtype: int
        """
        return self._max_backups

    @max_backups.setter
    def max_backups(self, max_backups):
        r"""Sets the max_backups of this CbrPolicyDetailResourceDetail.

        最大备份数量max_backups

        :param max_backups: The max_backups of this CbrPolicyDetailResourceDetail.
        :type max_backups: int
        """
        self._max_backups = max_backups

    @property
    def year_backups(self):
        r"""Gets the year_backups of this CbrPolicyDetailResourceDetail.

        保留年备个数，该备份不受保留最大备份数限制。取值为0到100。

        :return: The year_backups of this CbrPolicyDetailResourceDetail.
        :rtype: int
        """
        return self._year_backups

    @year_backups.setter
    def year_backups(self, year_backups):
        r"""Sets the year_backups of this CbrPolicyDetailResourceDetail.

        保留年备个数，该备份不受保留最大备份数限制。取值为0到100。

        :param year_backups: The year_backups of this CbrPolicyDetailResourceDetail.
        :type year_backups: int
        """
        self._year_backups = year_backups

    @property
    def month_backups(self):
        r"""Gets the month_backups of this CbrPolicyDetailResourceDetail.

        保留月备个数，该备份不受保留最大备份数限制。取值为0到100。

        :return: The month_backups of this CbrPolicyDetailResourceDetail.
        :rtype: int
        """
        return self._month_backups

    @month_backups.setter
    def month_backups(self, month_backups):
        r"""Sets the month_backups of this CbrPolicyDetailResourceDetail.

        保留月备个数，该备份不受保留最大备份数限制。取值为0到100。

        :param month_backups: The month_backups of this CbrPolicyDetailResourceDetail.
        :type month_backups: int
        """
        self._month_backups = month_backups

    @property
    def cross_account_urn(self):
        r"""Gets the cross_account_urn of this CbrPolicyDetailResourceDetail.

        账号备份的账号urn

        :return: The cross_account_urn of this CbrPolicyDetailResourceDetail.
        :rtype: str
        """
        return self._cross_account_urn

    @cross_account_urn.setter
    def cross_account_urn(self, cross_account_urn):
        r"""Sets the cross_account_urn of this CbrPolicyDetailResourceDetail.

        账号备份的账号urn

        :param cross_account_urn: The cross_account_urn of this CbrPolicyDetailResourceDetail.
        :type cross_account_urn: str
        """
        self._cross_account_urn = cross_account_urn

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
        if not isinstance(other, CbrPolicyDetailResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
