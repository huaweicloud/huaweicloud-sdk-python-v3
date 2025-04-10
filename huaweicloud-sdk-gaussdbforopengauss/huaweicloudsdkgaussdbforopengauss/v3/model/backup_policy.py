# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupPolicy:

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
        'differential_period': 'str',
        'rate_limit': 'int',
        'prefetch_block': 'int',
        'filesplit_size': 'int',
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
        'filesplit_size': 'filesplit_size',
        'file_split_size': 'file_split_size',
        'enable_standby_backup': 'enable_standby_backup'
    }

    def __init__(self, keep_days=None, start_time=None, period=None, differential_period=None, rate_limit=None, prefetch_block=None, filesplit_size=None, file_split_size=None, enable_standby_backup=None):
        r"""BackupPolicy

        The model defined in huaweicloud sdk

        :param keep_days: 备份文件可以保存的天数。  取值范围：1-732天。
        :type keep_days: int
        :param start_time: 备份时间段。自动备份将在该时间段内触发。  取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。  HH取值必须比hh大1，mm和MM取值必须相同，且取值必须为00。  取值示例：  21:00-22:00
        :type start_time: str
        :param period: 全量备份周期配置。自动全量备份将在每星期指定的天进行。取值范围：格式为逗号隔开的数字，数字代表星期。取值示例：1,2,3,4则表示备份周期配置为星期一、星期二、星期三和星期四。
        :type period: str
        :param differential_period: 差异备份间隔时间配置。每次自动差异备份的间隔时间。  取值范围：15、30、60、180、360、720、1440。单位：分钟。  取值示例：30
        :type differential_period: str
        :param rate_limit: 备份限速  取值范围：0 ~ 1024
        :type rate_limit: int
        :param prefetch_block: 控制差量备份时读取磁盘上表文件差量修改页面的预取页面个数。当差量修改页面非常集中时（如数据导入场景），可以适当调大该值；当差量修改页面非常分散时（如随机更新），可以适当调小该值。  取值范围：1 ~ 8192
        :type prefetch_block: int
        :param filesplit_size: 废弃。
        :type filesplit_size: int
        :param file_split_size: 全量、差量备份时产生的备份文件会根据分片大小进行拆分，可设置范围为0~1024GB，设置需为4的倍数，默认4GB，0GB表示不限制大小。  取值范围：0 ~ 1024
        :type file_split_size: int
        :param enable_standby_backup: 是否启用备机备份。  取值范围：true|false
        :type enable_standby_backup: bool
        """
        
        

        self._keep_days = None
        self._start_time = None
        self._period = None
        self._differential_period = None
        self._rate_limit = None
        self._prefetch_block = None
        self._filesplit_size = None
        self._file_split_size = None
        self._enable_standby_backup = None
        self.discriminator = None

        self.keep_days = keep_days
        self.start_time = start_time
        self.period = period
        self.differential_period = differential_period
        if rate_limit is not None:
            self.rate_limit = rate_limit
        if prefetch_block is not None:
            self.prefetch_block = prefetch_block
        if filesplit_size is not None:
            self.filesplit_size = filesplit_size
        if file_split_size is not None:
            self.file_split_size = file_split_size
        if enable_standby_backup is not None:
            self.enable_standby_backup = enable_standby_backup

    @property
    def keep_days(self):
        r"""Gets the keep_days of this BackupPolicy.

        备份文件可以保存的天数。  取值范围：1-732天。

        :return: The keep_days of this BackupPolicy.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this BackupPolicy.

        备份文件可以保存的天数。  取值范围：1-732天。

        :param keep_days: The keep_days of this BackupPolicy.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def start_time(self):
        r"""Gets the start_time of this BackupPolicy.

        备份时间段。自动备份将在该时间段内触发。  取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。  HH取值必须比hh大1，mm和MM取值必须相同，且取值必须为00。  取值示例：  21:00-22:00

        :return: The start_time of this BackupPolicy.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BackupPolicy.

        备份时间段。自动备份将在该时间段内触发。  取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。  HH取值必须比hh大1，mm和MM取值必须相同，且取值必须为00。  取值示例：  21:00-22:00

        :param start_time: The start_time of this BackupPolicy.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def period(self):
        r"""Gets the period of this BackupPolicy.

        全量备份周期配置。自动全量备份将在每星期指定的天进行。取值范围：格式为逗号隔开的数字，数字代表星期。取值示例：1,2,3,4则表示备份周期配置为星期一、星期二、星期三和星期四。

        :return: The period of this BackupPolicy.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this BackupPolicy.

        全量备份周期配置。自动全量备份将在每星期指定的天进行。取值范围：格式为逗号隔开的数字，数字代表星期。取值示例：1,2,3,4则表示备份周期配置为星期一、星期二、星期三和星期四。

        :param period: The period of this BackupPolicy.
        :type period: str
        """
        self._period = period

    @property
    def differential_period(self):
        r"""Gets the differential_period of this BackupPolicy.

        差异备份间隔时间配置。每次自动差异备份的间隔时间。  取值范围：15、30、60、180、360、720、1440。单位：分钟。  取值示例：30

        :return: The differential_period of this BackupPolicy.
        :rtype: str
        """
        return self._differential_period

    @differential_period.setter
    def differential_period(self, differential_period):
        r"""Sets the differential_period of this BackupPolicy.

        差异备份间隔时间配置。每次自动差异备份的间隔时间。  取值范围：15、30、60、180、360、720、1440。单位：分钟。  取值示例：30

        :param differential_period: The differential_period of this BackupPolicy.
        :type differential_period: str
        """
        self._differential_period = differential_period

    @property
    def rate_limit(self):
        r"""Gets the rate_limit of this BackupPolicy.

        备份限速  取值范围：0 ~ 1024

        :return: The rate_limit of this BackupPolicy.
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        r"""Sets the rate_limit of this BackupPolicy.

        备份限速  取值范围：0 ~ 1024

        :param rate_limit: The rate_limit of this BackupPolicy.
        :type rate_limit: int
        """
        self._rate_limit = rate_limit

    @property
    def prefetch_block(self):
        r"""Gets the prefetch_block of this BackupPolicy.

        控制差量备份时读取磁盘上表文件差量修改页面的预取页面个数。当差量修改页面非常集中时（如数据导入场景），可以适当调大该值；当差量修改页面非常分散时（如随机更新），可以适当调小该值。  取值范围：1 ~ 8192

        :return: The prefetch_block of this BackupPolicy.
        :rtype: int
        """
        return self._prefetch_block

    @prefetch_block.setter
    def prefetch_block(self, prefetch_block):
        r"""Sets the prefetch_block of this BackupPolicy.

        控制差量备份时读取磁盘上表文件差量修改页面的预取页面个数。当差量修改页面非常集中时（如数据导入场景），可以适当调大该值；当差量修改页面非常分散时（如随机更新），可以适当调小该值。  取值范围：1 ~ 8192

        :param prefetch_block: The prefetch_block of this BackupPolicy.
        :type prefetch_block: int
        """
        self._prefetch_block = prefetch_block

    @property
    def filesplit_size(self):
        r"""Gets the filesplit_size of this BackupPolicy.

        废弃。

        :return: The filesplit_size of this BackupPolicy.
        :rtype: int
        """
        return self._filesplit_size

    @filesplit_size.setter
    def filesplit_size(self, filesplit_size):
        r"""Sets the filesplit_size of this BackupPolicy.

        废弃。

        :param filesplit_size: The filesplit_size of this BackupPolicy.
        :type filesplit_size: int
        """
        self._filesplit_size = filesplit_size

    @property
    def file_split_size(self):
        r"""Gets the file_split_size of this BackupPolicy.

        全量、差量备份时产生的备份文件会根据分片大小进行拆分，可设置范围为0~1024GB，设置需为4的倍数，默认4GB，0GB表示不限制大小。  取值范围：0 ~ 1024

        :return: The file_split_size of this BackupPolicy.
        :rtype: int
        """
        return self._file_split_size

    @file_split_size.setter
    def file_split_size(self, file_split_size):
        r"""Sets the file_split_size of this BackupPolicy.

        全量、差量备份时产生的备份文件会根据分片大小进行拆分，可设置范围为0~1024GB，设置需为4的倍数，默认4GB，0GB表示不限制大小。  取值范围：0 ~ 1024

        :param file_split_size: The file_split_size of this BackupPolicy.
        :type file_split_size: int
        """
        self._file_split_size = file_split_size

    @property
    def enable_standby_backup(self):
        r"""Gets the enable_standby_backup of this BackupPolicy.

        是否启用备机备份。  取值范围：true|false

        :return: The enable_standby_backup of this BackupPolicy.
        :rtype: bool
        """
        return self._enable_standby_backup

    @enable_standby_backup.setter
    def enable_standby_backup(self, enable_standby_backup):
        r"""Sets the enable_standby_backup of this BackupPolicy.

        是否启用备机备份。  取值范围：true|false

        :param enable_standby_backup: The enable_standby_backup of this BackupPolicy.
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
        if not isinstance(other, BackupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
