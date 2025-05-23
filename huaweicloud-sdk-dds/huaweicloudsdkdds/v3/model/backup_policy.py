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
        'keep_days': 'str',
        'start_time': 'str',
        'period': 'str',
        'enable_incremental_backup': 'bool'
    }

    attribute_map = {
        'keep_days': 'keep_days',
        'start_time': 'start_time',
        'period': 'period',
        'enable_incremental_backup': 'enable_incremental_backup'
    }

    def __init__(self, keep_days=None, start_time=None, period=None, enable_incremental_backup=None):
        r"""BackupPolicy

        The model defined in huaweicloud sdk

        :param keep_days: 指定已生成的备份文件可以保存的天数。 取值范围：0～732。取0值，表示关闭自动备份策略。
        :type keep_days: str
        :param start_time: 备份时间段。自动备份将在该时间段内触发。开启自动备份策略时，该参数必选；关闭自动备份策略时，不传该参数。 取值范围：格式必须为hh:mm-HH:MM，且有效，当前时间指UTC时间。 - HH取值必须比hh大1。 - mm和MM取值必须相同，且取值必须为00、15、30或45。 取值示例： - 08:15-09:15 - 23:00-00:00
        :type start_time: str
        :param period: 备份周期配置。自动备份将在每星期指定的天进行。取值范围：格式为半角逗号隔开的数字，数字代表星期。保留天数取值不同，备份周期约束如下： - 0天，不传该参数。 - 1～6天，备份周期全选，取值为：1,2,3,4,5,6,7。 - 7～732天，备份周期至少选择一周中的一天。示例：1,2,3,4。
        :type period: str
        :param enable_incremental_backup: 增量备份开关。不传这个参数则不对增备状态进行改动。开启增量备份后，系统会自动进行增量备份。增量备份开关的取值和约束如下： - false，代表关闭增量备份，关闭会将之前做的增量备份清理。 - true，代表开启增量备份，开启增量备份会触发一次全量备份。
        :type enable_incremental_backup: bool
        """
        
        

        self._keep_days = None
        self._start_time = None
        self._period = None
        self._enable_incremental_backup = None
        self.discriminator = None

        if keep_days is not None:
            self.keep_days = keep_days
        if start_time is not None:
            self.start_time = start_time
        if period is not None:
            self.period = period
        if enable_incremental_backup is not None:
            self.enable_incremental_backup = enable_incremental_backup

    @property
    def keep_days(self):
        r"""Gets the keep_days of this BackupPolicy.

        指定已生成的备份文件可以保存的天数。 取值范围：0～732。取0值，表示关闭自动备份策略。

        :return: The keep_days of this BackupPolicy.
        :rtype: str
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this BackupPolicy.

        指定已生成的备份文件可以保存的天数。 取值范围：0～732。取0值，表示关闭自动备份策略。

        :param keep_days: The keep_days of this BackupPolicy.
        :type keep_days: str
        """
        self._keep_days = keep_days

    @property
    def start_time(self):
        r"""Gets the start_time of this BackupPolicy.

        备份时间段。自动备份将在该时间段内触发。开启自动备份策略时，该参数必选；关闭自动备份策略时，不传该参数。 取值范围：格式必须为hh:mm-HH:MM，且有效，当前时间指UTC时间。 - HH取值必须比hh大1。 - mm和MM取值必须相同，且取值必须为00、15、30或45。 取值示例： - 08:15-09:15 - 23:00-00:00

        :return: The start_time of this BackupPolicy.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BackupPolicy.

        备份时间段。自动备份将在该时间段内触发。开启自动备份策略时，该参数必选；关闭自动备份策略时，不传该参数。 取值范围：格式必须为hh:mm-HH:MM，且有效，当前时间指UTC时间。 - HH取值必须比hh大1。 - mm和MM取值必须相同，且取值必须为00、15、30或45。 取值示例： - 08:15-09:15 - 23:00-00:00

        :param start_time: The start_time of this BackupPolicy.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def period(self):
        r"""Gets the period of this BackupPolicy.

        备份周期配置。自动备份将在每星期指定的天进行。取值范围：格式为半角逗号隔开的数字，数字代表星期。保留天数取值不同，备份周期约束如下： - 0天，不传该参数。 - 1～6天，备份周期全选，取值为：1,2,3,4,5,6,7。 - 7～732天，备份周期至少选择一周中的一天。示例：1,2,3,4。

        :return: The period of this BackupPolicy.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this BackupPolicy.

        备份周期配置。自动备份将在每星期指定的天进行。取值范围：格式为半角逗号隔开的数字，数字代表星期。保留天数取值不同，备份周期约束如下： - 0天，不传该参数。 - 1～6天，备份周期全选，取值为：1,2,3,4,5,6,7。 - 7～732天，备份周期至少选择一周中的一天。示例：1,2,3,4。

        :param period: The period of this BackupPolicy.
        :type period: str
        """
        self._period = period

    @property
    def enable_incremental_backup(self):
        r"""Gets the enable_incremental_backup of this BackupPolicy.

        增量备份开关。不传这个参数则不对增备状态进行改动。开启增量备份后，系统会自动进行增量备份。增量备份开关的取值和约束如下： - false，代表关闭增量备份，关闭会将之前做的增量备份清理。 - true，代表开启增量备份，开启增量备份会触发一次全量备份。

        :return: The enable_incremental_backup of this BackupPolicy.
        :rtype: bool
        """
        return self._enable_incremental_backup

    @enable_incremental_backup.setter
    def enable_incremental_backup(self, enable_incremental_backup):
        r"""Sets the enable_incremental_backup of this BackupPolicy.

        增量备份开关。不传这个参数则不对增备状态进行改动。开启增量备份后，系统会自动进行增量备份。增量备份开关的取值和约束如下： - false，代表关闭增量备份，关闭会将之前做的增量备份清理。 - true，代表开启增量备份，开启增量备份会触发一次全量备份。

        :param enable_incremental_backup: The enable_incremental_backup of this BackupPolicy.
        :type enable_incremental_backup: bool
        """
        self._enable_incremental_backup = enable_incremental_backup

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
