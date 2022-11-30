# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupPolicy:

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
        'differential_priod': 'str',
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
        'differential_priod': 'differential_priod',
        'differential_period': 'differential_period',
        'rate_limit': 'rate_limit',
        'prefetch_block': 'prefetch_block',
        'filesplit_size': 'filesplit_size',
        'file_split_size': 'file_split_size',
        'enable_standby_backup': 'enable_standby_backup'
    }

    def __init__(self, keep_days=None, start_time=None, period=None, differential_priod=None, differential_period=None, rate_limit=None, prefetch_block=None, filesplit_size=None, file_split_size=None, enable_standby_backup=None):
        """ShowBackupPolicy

        The model defined in huaweicloud sdk

        :param keep_days: 全量备份文件可以保存的天数。
        :type keep_days: int
        :param start_time: 全量备份时间段。自动备份将在该时间段内触发。除关闭自动备份策略外，必选。  取值范围：格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。  - HH取值必须比hh大1。 - mm和MM取值必须相同，且取值必须为00。
        :type start_time: str
        :param period: 全量备份周期配置。自动备份将在每星期指定的天进行。  取值范围：格式为逗号隔开的数字，数字代表星期。
        :type period: str
        :param differential_priod: 差量备份周期配置。自动差量备份将每隔周期分钟执行(废弃)。
        :type differential_priod: str
        :param differential_period: 差量备份周期配置。自动差量备份将每隔周期分钟执行。
        :type differential_period: str
        :param rate_limit: 备份时备份数据上传OBS的速度，单位为MB/s。范围为0~1024MB/s，默认75MB/s，0MB/s表示不限速。
        :type rate_limit: int
        :param prefetch_block: 控制差量备份时读取磁盘上表文件差量修改页面的预取页面个数，可设置范围为1~8192，默认64。
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
        self._differential_priod = None
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
        if differential_priod is not None:
            self.differential_priod = differential_priod
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
        """Gets the keep_days of this ShowBackupPolicy.

        全量备份文件可以保存的天数。

        :return: The keep_days of this ShowBackupPolicy.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this ShowBackupPolicy.

        全量备份文件可以保存的天数。

        :param keep_days: The keep_days of this ShowBackupPolicy.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def start_time(self):
        """Gets the start_time of this ShowBackupPolicy.

        全量备份时间段。自动备份将在该时间段内触发。除关闭自动备份策略外，必选。  取值范围：格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。  - HH取值必须比hh大1。 - mm和MM取值必须相同，且取值必须为00。

        :return: The start_time of this ShowBackupPolicy.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowBackupPolicy.

        全量备份时间段。自动备份将在该时间段内触发。除关闭自动备份策略外，必选。  取值范围：格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。  - HH取值必须比hh大1。 - mm和MM取值必须相同，且取值必须为00。

        :param start_time: The start_time of this ShowBackupPolicy.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def period(self):
        """Gets the period of this ShowBackupPolicy.

        全量备份周期配置。自动备份将在每星期指定的天进行。  取值范围：格式为逗号隔开的数字，数字代表星期。

        :return: The period of this ShowBackupPolicy.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ShowBackupPolicy.

        全量备份周期配置。自动备份将在每星期指定的天进行。  取值范围：格式为逗号隔开的数字，数字代表星期。

        :param period: The period of this ShowBackupPolicy.
        :type period: str
        """
        self._period = period

    @property
    def differential_priod(self):
        """Gets the differential_priod of this ShowBackupPolicy.

        差量备份周期配置。自动差量备份将每隔周期分钟执行(废弃)。

        :return: The differential_priod of this ShowBackupPolicy.
        :rtype: str
        """
        return self._differential_priod

    @differential_priod.setter
    def differential_priod(self, differential_priod):
        """Sets the differential_priod of this ShowBackupPolicy.

        差量备份周期配置。自动差量备份将每隔周期分钟执行(废弃)。

        :param differential_priod: The differential_priod of this ShowBackupPolicy.
        :type differential_priod: str
        """
        self._differential_priod = differential_priod

    @property
    def differential_period(self):
        """Gets the differential_period of this ShowBackupPolicy.

        差量备份周期配置。自动差量备份将每隔周期分钟执行。

        :return: The differential_period of this ShowBackupPolicy.
        :rtype: str
        """
        return self._differential_period

    @differential_period.setter
    def differential_period(self, differential_period):
        """Sets the differential_period of this ShowBackupPolicy.

        差量备份周期配置。自动差量备份将每隔周期分钟执行。

        :param differential_period: The differential_period of this ShowBackupPolicy.
        :type differential_period: str
        """
        self._differential_period = differential_period

    @property
    def rate_limit(self):
        """Gets the rate_limit of this ShowBackupPolicy.

        备份时备份数据上传OBS的速度，单位为MB/s。范围为0~1024MB/s，默认75MB/s，0MB/s表示不限速。

        :return: The rate_limit of this ShowBackupPolicy.
        :rtype: int
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """Sets the rate_limit of this ShowBackupPolicy.

        备份时备份数据上传OBS的速度，单位为MB/s。范围为0~1024MB/s，默认75MB/s，0MB/s表示不限速。

        :param rate_limit: The rate_limit of this ShowBackupPolicy.
        :type rate_limit: int
        """
        self._rate_limit = rate_limit

    @property
    def prefetch_block(self):
        """Gets the prefetch_block of this ShowBackupPolicy.

        控制差量备份时读取磁盘上表文件差量修改页面的预取页面个数，可设置范围为1~8192，默认64。

        :return: The prefetch_block of this ShowBackupPolicy.
        :rtype: int
        """
        return self._prefetch_block

    @prefetch_block.setter
    def prefetch_block(self, prefetch_block):
        """Sets the prefetch_block of this ShowBackupPolicy.

        控制差量备份时读取磁盘上表文件差量修改页面的预取页面个数，可设置范围为1~8192，默认64。

        :param prefetch_block: The prefetch_block of this ShowBackupPolicy.
        :type prefetch_block: int
        """
        self._prefetch_block = prefetch_block

    @property
    def filesplit_size(self):
        """Gets the filesplit_size of this ShowBackupPolicy.

        废弃。

        :return: The filesplit_size of this ShowBackupPolicy.
        :rtype: int
        """
        return self._filesplit_size

    @filesplit_size.setter
    def filesplit_size(self, filesplit_size):
        """Sets the filesplit_size of this ShowBackupPolicy.

        废弃。

        :param filesplit_size: The filesplit_size of this ShowBackupPolicy.
        :type filesplit_size: int
        """
        self._filesplit_size = filesplit_size

    @property
    def file_split_size(self):
        """Gets the file_split_size of this ShowBackupPolicy.

        全量、差量备份时产生的备份文件会根据分片大小进行拆分，可设置范围为0~1024GB，设置需为4的倍数，默认4GB，0GB表示不限制大小。  取值范围：0 ~ 1024

        :return: The file_split_size of this ShowBackupPolicy.
        :rtype: int
        """
        return self._file_split_size

    @file_split_size.setter
    def file_split_size(self, file_split_size):
        """Sets the file_split_size of this ShowBackupPolicy.

        全量、差量备份时产生的备份文件会根据分片大小进行拆分，可设置范围为0~1024GB，设置需为4的倍数，默认4GB，0GB表示不限制大小。  取值范围：0 ~ 1024

        :param file_split_size: The file_split_size of this ShowBackupPolicy.
        :type file_split_size: int
        """
        self._file_split_size = file_split_size

    @property
    def enable_standby_backup(self):
        """Gets the enable_standby_backup of this ShowBackupPolicy.

        是否启用备机备份。  取值范围：true|false

        :return: The enable_standby_backup of this ShowBackupPolicy.
        :rtype: bool
        """
        return self._enable_standby_backup

    @enable_standby_backup.setter
    def enable_standby_backup(self, enable_standby_backup):
        """Sets the enable_standby_backup of this ShowBackupPolicy.

        是否启用备机备份。  取值范围：true|false

        :param enable_standby_backup: The enable_standby_backup of this ShowBackupPolicy.
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
        if not isinstance(other, ShowBackupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
