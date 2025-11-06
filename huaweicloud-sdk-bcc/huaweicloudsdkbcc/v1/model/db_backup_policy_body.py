# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbBackupPolicyBody:

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
        'differential_period': 'str'
    }

    attribute_map = {
        'keep_days': 'keep_days',
        'start_time': 'start_time',
        'period': 'period',
        'differential_period': 'differential_period'
    }

    def __init__(self, keep_days=None, start_time=None, period=None, differential_period=None):
        r"""DbBackupPolicyBody

        The model defined in huaweicloud sdk

        :param keep_days: 备份文件可以保存的天数。取值范围：1-36500天。
        :type keep_days: int
        :param start_time: 备份时间段。自动备份将在该时间段内触发。取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。HH取值必须比hh大1，mm和MM取值必须相同，且取值必须为00。取值示例：21:00-22:00
        :type start_time: str
        :param period: 全量备份周期配置。自动全量备份将在每周对应的UTC日期进行。取值范围：格式为逗号隔开的数字，数字代表星期，取1~7。
        :type period: str
        :param differential_period: 差异备份间隔时间配置。每次自动差异备份的间隔时间。取值范围15、30、60、180、360、720、1440。单位：分钟
        :type differential_period: str
        """
        
        

        self._keep_days = None
        self._start_time = None
        self._period = None
        self._differential_period = None
        self.discriminator = None

        self.keep_days = keep_days
        self.start_time = start_time
        self.period = period
        if differential_period is not None:
            self.differential_period = differential_period

    @property
    def keep_days(self):
        r"""Gets the keep_days of this DbBackupPolicyBody.

        备份文件可以保存的天数。取值范围：1-36500天。

        :return: The keep_days of this DbBackupPolicyBody.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this DbBackupPolicyBody.

        备份文件可以保存的天数。取值范围：1-36500天。

        :param keep_days: The keep_days of this DbBackupPolicyBody.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def start_time(self):
        r"""Gets the start_time of this DbBackupPolicyBody.

        备份时间段。自动备份将在该时间段内触发。取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。HH取值必须比hh大1，mm和MM取值必须相同，且取值必须为00。取值示例：21:00-22:00

        :return: The start_time of this DbBackupPolicyBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DbBackupPolicyBody.

        备份时间段。自动备份将在该时间段内触发。取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。HH取值必须比hh大1，mm和MM取值必须相同，且取值必须为00。取值示例：21:00-22:00

        :param start_time: The start_time of this DbBackupPolicyBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def period(self):
        r"""Gets the period of this DbBackupPolicyBody.

        全量备份周期配置。自动全量备份将在每周对应的UTC日期进行。取值范围：格式为逗号隔开的数字，数字代表星期，取1~7。

        :return: The period of this DbBackupPolicyBody.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this DbBackupPolicyBody.

        全量备份周期配置。自动全量备份将在每周对应的UTC日期进行。取值范围：格式为逗号隔开的数字，数字代表星期，取1~7。

        :param period: The period of this DbBackupPolicyBody.
        :type period: str
        """
        self._period = period

    @property
    def differential_period(self):
        r"""Gets the differential_period of this DbBackupPolicyBody.

        差异备份间隔时间配置。每次自动差异备份的间隔时间。取值范围15、30、60、180、360、720、1440。单位：分钟

        :return: The differential_period of this DbBackupPolicyBody.
        :rtype: str
        """
        return self._differential_period

    @differential_period.setter
    def differential_period(self, differential_period):
        r"""Sets the differential_period of this DbBackupPolicyBody.

        差异备份间隔时间配置。每次自动差异备份的间隔时间。取值范围15、30、60、180、360、720、1440。单位：分钟

        :param differential_period: The differential_period of this DbBackupPolicyBody.
        :type differential_period: str
        """
        self._differential_period = differential_period

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
        if not isinstance(other, DbBackupPolicyBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
