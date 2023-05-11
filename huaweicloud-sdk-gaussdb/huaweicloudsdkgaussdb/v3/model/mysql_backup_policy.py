# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlBackupPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'keep_days': 'int',
        'period': 'str',
        'retention_num_backup_level1': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'keep_days': 'keep_days',
        'period': 'period',
        'retention_num_backup_level1': 'retention_num_backup_level1'
    }

    def __init__(self, start_time=None, keep_days=None, period=None, retention_num_backup_level1=None):
        """MysqlBackupPolicy

        The model defined in huaweicloud sdk

        :param start_time: 备份时间段。自动备份将在该时间段内触发。  取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。HH取值必须比hh大1。mm和MM取值必须相同，且取值必须为00。  取值示例：21:00-22:00
        :type start_time: str
        :param keep_days: 备份文件的保留天数。
        :type keep_days: int
        :param period: 备份周期配置。自动备份将在每星期指定的天进行。  取值范围：格式为逗号隔开的数字，数字代表星期。  取值示例：1,2,3,4则表示备份周期配置为星期一、星期二、星期三和星期四。
        :type period: str
        :param retention_num_backup_level1: 一级备份保留数量，默认值为0。当一级备份开关开启时，该参数值有效。取值：0或1
        :type retention_num_backup_level1: int
        """
        
        

        self._start_time = None
        self._keep_days = None
        self._period = None
        self._retention_num_backup_level1 = None
        self.discriminator = None

        self.start_time = start_time
        self.keep_days = keep_days
        self.period = period
        if retention_num_backup_level1 is not None:
            self.retention_num_backup_level1 = retention_num_backup_level1

    @property
    def start_time(self):
        """Gets the start_time of this MysqlBackupPolicy.

        备份时间段。自动备份将在该时间段内触发。  取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。HH取值必须比hh大1。mm和MM取值必须相同，且取值必须为00。  取值示例：21:00-22:00

        :return: The start_time of this MysqlBackupPolicy.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this MysqlBackupPolicy.

        备份时间段。自动备份将在该时间段内触发。  取值范围：非空，格式必须为hh:mm-HH:MM且有效，当前时间指UTC时间。HH取值必须比hh大1。mm和MM取值必须相同，且取值必须为00。  取值示例：21:00-22:00

        :param start_time: The start_time of this MysqlBackupPolicy.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def keep_days(self):
        """Gets the keep_days of this MysqlBackupPolicy.

        备份文件的保留天数。

        :return: The keep_days of this MysqlBackupPolicy.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this MysqlBackupPolicy.

        备份文件的保留天数。

        :param keep_days: The keep_days of this MysqlBackupPolicy.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def period(self):
        """Gets the period of this MysqlBackupPolicy.

        备份周期配置。自动备份将在每星期指定的天进行。  取值范围：格式为逗号隔开的数字，数字代表星期。  取值示例：1,2,3,4则表示备份周期配置为星期一、星期二、星期三和星期四。

        :return: The period of this MysqlBackupPolicy.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this MysqlBackupPolicy.

        备份周期配置。自动备份将在每星期指定的天进行。  取值范围：格式为逗号隔开的数字，数字代表星期。  取值示例：1,2,3,4则表示备份周期配置为星期一、星期二、星期三和星期四。

        :param period: The period of this MysqlBackupPolicy.
        :type period: str
        """
        self._period = period

    @property
    def retention_num_backup_level1(self):
        """Gets the retention_num_backup_level1 of this MysqlBackupPolicy.

        一级备份保留数量，默认值为0。当一级备份开关开启时，该参数值有效。取值：0或1

        :return: The retention_num_backup_level1 of this MysqlBackupPolicy.
        :rtype: int
        """
        return self._retention_num_backup_level1

    @retention_num_backup_level1.setter
    def retention_num_backup_level1(self, retention_num_backup_level1):
        """Sets the retention_num_backup_level1 of this MysqlBackupPolicy.

        一级备份保留数量，默认值为0。当一级备份开关开启时，该参数值有效。取值：0或1

        :param retention_num_backup_level1: The retention_num_backup_level1 of this MysqlBackupPolicy.
        :type retention_num_backup_level1: int
        """
        self._retention_num_backup_level1 = retention_num_backup_level1

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
        if not isinstance(other, MysqlBackupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
