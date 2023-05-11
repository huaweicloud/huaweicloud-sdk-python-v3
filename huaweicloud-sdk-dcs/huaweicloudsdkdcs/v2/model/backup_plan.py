# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupPlan:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timezone_offset': 'str',
        'backup_at': 'list[int]',
        'period_type': 'str',
        'begin_at': 'str'
    }

    attribute_map = {
        'timezone_offset': 'timezone_offset',
        'backup_at': 'backup_at',
        'period_type': 'period_type',
        'begin_at': 'begin_at'
    }

    def __init__(self, timezone_offset=None, backup_at=None, period_type=None, begin_at=None):
        """BackupPlan

        The model defined in huaweicloud sdk

        :param timezone_offset: 备份的时区。取值为-1200 ~+1200之间的时区。若为空则默认使用DCS-Server节点的当前时区。
        :type timezone_offset: str
        :param backup_at: 每周的周几开始备份，取值1-7，1代表周一，7代表周日。
        :type backup_at: list[int]
        :param period_type: 备份周期类型，目前支持“weekly”。
        :type period_type: str
        :param begin_at: 备份执行时间，“00:00-01:00”代表0点开始执行备份。
        :type begin_at: str
        """
        
        

        self._timezone_offset = None
        self._backup_at = None
        self._period_type = None
        self._begin_at = None
        self.discriminator = None

        if timezone_offset is not None:
            self.timezone_offset = timezone_offset
        self.backup_at = backup_at
        self.period_type = period_type
        self.begin_at = begin_at

    @property
    def timezone_offset(self):
        """Gets the timezone_offset of this BackupPlan.

        备份的时区。取值为-1200 ~+1200之间的时区。若为空则默认使用DCS-Server节点的当前时区。

        :return: The timezone_offset of this BackupPlan.
        :rtype: str
        """
        return self._timezone_offset

    @timezone_offset.setter
    def timezone_offset(self, timezone_offset):
        """Sets the timezone_offset of this BackupPlan.

        备份的时区。取值为-1200 ~+1200之间的时区。若为空则默认使用DCS-Server节点的当前时区。

        :param timezone_offset: The timezone_offset of this BackupPlan.
        :type timezone_offset: str
        """
        self._timezone_offset = timezone_offset

    @property
    def backup_at(self):
        """Gets the backup_at of this BackupPlan.

        每周的周几开始备份，取值1-7，1代表周一，7代表周日。

        :return: The backup_at of this BackupPlan.
        :rtype: list[int]
        """
        return self._backup_at

    @backup_at.setter
    def backup_at(self, backup_at):
        """Sets the backup_at of this BackupPlan.

        每周的周几开始备份，取值1-7，1代表周一，7代表周日。

        :param backup_at: The backup_at of this BackupPlan.
        :type backup_at: list[int]
        """
        self._backup_at = backup_at

    @property
    def period_type(self):
        """Gets the period_type of this BackupPlan.

        备份周期类型，目前支持“weekly”。

        :return: The period_type of this BackupPlan.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this BackupPlan.

        备份周期类型，目前支持“weekly”。

        :param period_type: The period_type of this BackupPlan.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def begin_at(self):
        """Gets the begin_at of this BackupPlan.

        备份执行时间，“00:00-01:00”代表0点开始执行备份。

        :return: The begin_at of this BackupPlan.
        :rtype: str
        """
        return self._begin_at

    @begin_at.setter
    def begin_at(self, begin_at):
        """Sets the begin_at of this BackupPlan.

        备份执行时间，“00:00-01:00”代表0点开始执行备份。

        :param begin_at: The begin_at of this BackupPlan.
        :type begin_at: str
        """
        self._begin_at = begin_at

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
        if not isinstance(other, BackupPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
