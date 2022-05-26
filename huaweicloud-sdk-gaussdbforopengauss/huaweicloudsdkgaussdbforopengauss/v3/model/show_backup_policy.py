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
        'differential_priod': 'str'
    }

    attribute_map = {
        'keep_days': 'keep_days',
        'start_time': 'start_time',
        'period': 'period',
        'differential_priod': 'differential_priod'
    }

    def __init__(self, keep_days=None, start_time=None, period=None, differential_priod=None):
        """ShowBackupPolicy

        The model defined in huaweicloud sdk

        :param keep_days: 全量备份文件可以保存的天数。
        :type keep_days: int
        :param start_time: 全量备份时间段。自动备份将在该时间段内触发。除关闭自动备份策略外，必选。  取值范围：格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。  - HH取值必须比hh大1。 - mm和MM取值必须相同，且取值必须为00。
        :type start_time: str
        :param period: 全量备份周期配置。自动备份将在每星期指定的天进行。  取值范围：格式为逗号隔开的数字，数字代表星期。
        :type period: str
        :param differential_priod: 差量备份周期配置。自动差量备份将每隔周期分钟执行。
        :type differential_priod: str
        """
        
        

        self._keep_days = None
        self._start_time = None
        self._period = None
        self._differential_priod = None
        self.discriminator = None

        self.keep_days = keep_days
        self.start_time = start_time
        self.period = period
        if differential_priod is not None:
            self.differential_priod = differential_priod

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

        差量备份周期配置。自动差量备份将每隔周期分钟执行。

        :return: The differential_priod of this ShowBackupPolicy.
        :rtype: str
        """
        return self._differential_priod

    @differential_priod.setter
    def differential_priod(self, differential_priod):
        """Sets the differential_priod of this ShowBackupPolicy.

        差量备份周期配置。自动差量备份将每隔周期分钟执行。

        :param differential_priod: The differential_priod of this ShowBackupPolicy.
        :type differential_priod: str
        """
        self._differential_priod = differential_priod

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
