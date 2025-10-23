# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbPolicyDetailBackupPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keep_days': 'int',
        'start_time': 'str',
        'period': 'str',
        'differential_period': 'int',
        'rate_limit': 'int',
        'prefetch_block': 'int',
        'file_split_size': 'int',
        'enable_standby_backup': 'bool'
    }

    attribute_map = {
        'keep_days': 'keep_days',
        'start_time': 'start_time',
        'period': 'period',
        'differential_period': 'differential_period',
        'rate_limit': 'rate_limit',
        'prefetch_block': 'prefetch_block',
        'file_split_size': 'file_split_size',
        'enable_standby_backup': 'enable_standby_backup'
    }

    def __init__(self, keep_days=None, start_time=None, period=None, differential_period=None, rate_limit=None, prefetch_block=None, file_split_size=None, enable_standby_backup=None):
        r"""DbPolicyDetailBackupPolicy

        The model defined in huaweicloud sdk

        :param keep_days: 备份保留时长
        :type keep_days: int
        :param start_time: 备份开始时间
        :type start_time: str
        :param period: 备份周期，一周哪几天
        :type period: str
        :param differential_period: gaussdb差异备份周期
        :type differential_period: int
        :param rate_limit: gaussdb备份限速
        :type rate_limit: int
        :param prefetch_block: gaussdb预取页面个数
        :type prefetch_block: int
        :param file_split_size: gaussdb文件拆分大小
        :type file_split_size: int
        :param enable_standby_backup: gaussdb是否启用standby备份
        :type enable_standby_backup: bool
        """
        
        

        self._keep_days = None
        self._start_time = None
        self._period = None
        self._differential_period = None
        self._rate_limit = None
        self._prefetch_block = None
        self._file_split_size = None
        self._enable_standby_backup = None
        self.discriminator = None

        if keep_days is not None:
            self.keep_days = keep_days
        if start_time is not None:
            self.start_time = start_time
        if period is not None:
            self.period = period
        if differential_period is not None:
            self.differential_period = differential_period
        if rate_limit is not None:
            self.rate_limit = rate_limit
        if prefetch_block is not None:
            self.prefetch_block = prefetch_block
        if file_split_size is not None:
            self.file_split_size = file_split_size
        if enable_standby_backup is not None:
            self.enable_standby_backup = enable_standby_backup

    @property
    def keep_days(self):
        r"""Gets the keep_days of this DbPolicyDetailBackupPolicy.

        备份保留时长

        :return: The keep_days of this DbPolicyDetailBackupPolicy.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this DbPolicyDetailBackupPolicy.

        备份保留时长

        :param keep_days: The keep_days of this DbPolicyDetailBackupPolicy.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def start_time(self):
        r"""Gets the start_time of this DbPolicyDetailBackupPolicy.

        备份开始时间

        :return: The start_time of this DbPolicyDetailBackupPolicy.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DbPolicyDetailBackupPolicy.

        备份开始时间

        :param start_time: The start_time of this DbPolicyDetailBackupPolicy.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def period(self):
        r"""Gets the period of this DbPolicyDetailBackupPolicy.

        备份周期，一周哪几天

        :return: The period of this DbPolicyDetailBackupPolicy.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this DbPolicyDetailBackupPolicy.

        备份周期，一周哪几天

        :param period: The period of this DbPolicyDetailBackupPolicy.
        :type period: str
        """
        self._period = period

    @property
    def differential_period(self):
        r"""Gets the differential_period of this DbPolicyDetailBackupPolicy.

        gaussdb差异备份周期

        :return: The differential_period of this DbPolicyDetailBackupPolicy.
        :rtype: int
        """
        return self._differential_period

    @differential_period.setter
    def differential_period(self, differential_period):
        r"""Sets the differential_period of this DbPolicyDetailBackupPolicy.

        gaussdb差异备份周期

        :param differential_period: The differential_period of this DbPolicyDetailBackupPolicy.
        :type differential_period: int
        """
        self._differential_period = differential_period

    @property
    def rate_limit(self):
        r"""Gets the rate_limit of this DbPolicyDetailBackupPolicy.

        gaussdb备份限速

        :return: The rate_limit of this DbPolicyDetailBackupPolicy.
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        r"""Sets the rate_limit of this DbPolicyDetailBackupPolicy.

        gaussdb备份限速

        :param rate_limit: The rate_limit of this DbPolicyDetailBackupPolicy.
        :type rate_limit: int
        """
        self._rate_limit = rate_limit

    @property
    def prefetch_block(self):
        r"""Gets the prefetch_block of this DbPolicyDetailBackupPolicy.

        gaussdb预取页面个数

        :return: The prefetch_block of this DbPolicyDetailBackupPolicy.
        :rtype: int
        """
        return self._prefetch_block

    @prefetch_block.setter
    def prefetch_block(self, prefetch_block):
        r"""Sets the prefetch_block of this DbPolicyDetailBackupPolicy.

        gaussdb预取页面个数

        :param prefetch_block: The prefetch_block of this DbPolicyDetailBackupPolicy.
        :type prefetch_block: int
        """
        self._prefetch_block = prefetch_block

    @property
    def file_split_size(self):
        r"""Gets the file_split_size of this DbPolicyDetailBackupPolicy.

        gaussdb文件拆分大小

        :return: The file_split_size of this DbPolicyDetailBackupPolicy.
        :rtype: int
        """
        return self._file_split_size

    @file_split_size.setter
    def file_split_size(self, file_split_size):
        r"""Sets the file_split_size of this DbPolicyDetailBackupPolicy.

        gaussdb文件拆分大小

        :param file_split_size: The file_split_size of this DbPolicyDetailBackupPolicy.
        :type file_split_size: int
        """
        self._file_split_size = file_split_size

    @property
    def enable_standby_backup(self):
        r"""Gets the enable_standby_backup of this DbPolicyDetailBackupPolicy.

        gaussdb是否启用standby备份

        :return: The enable_standby_backup of this DbPolicyDetailBackupPolicy.
        :rtype: bool
        """
        return self._enable_standby_backup

    @enable_standby_backup.setter
    def enable_standby_backup(self, enable_standby_backup):
        r"""Sets the enable_standby_backup of this DbPolicyDetailBackupPolicy.

        gaussdb是否启用standby备份

        :param enable_standby_backup: The enable_standby_backup of this DbPolicyDetailBackupPolicy.
        :type enable_standby_backup: bool
        """
        self._enable_standby_backup = enable_standby_backup

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
        if not isinstance(other, DbPolicyDetailBackupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
