# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotPolicyResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_enable': 'bool',
        'bak_period': 'str',
        'bak_frequency': 'str',
        'bak_keep_day': 'int'
    }

    attribute_map = {
        'backup_enable': 'backupEnable',
        'bak_period': 'bakPeriod',
        'bak_frequency': 'bakFrequency',
        'bak_keep_day': 'bakKeepDay'
    }

    def __init__(self, backup_enable=None, bak_period=None, bak_frequency=None, bak_keep_day=None):
        r"""SnapshotPolicyResp

        The model defined in huaweicloud sdk

        :param backup_enable: 集群是否开启自动快照。
        :type backup_enable: bool
        :param bak_period: 快照备份时间。
        :type bak_period: str
        :param bak_frequency: 快照备份间隔。
        :type bak_frequency: str
        :param bak_keep_day: 快照备份保留个数。
        :type bak_keep_day: int
        """
        
        

        self._backup_enable = None
        self._bak_period = None
        self._bak_frequency = None
        self._bak_keep_day = None
        self.discriminator = None

        if backup_enable is not None:
            self.backup_enable = backup_enable
        if bak_period is not None:
            self.bak_period = bak_period
        if bak_frequency is not None:
            self.bak_frequency = bak_frequency
        if bak_keep_day is not None:
            self.bak_keep_day = bak_keep_day

    @property
    def backup_enable(self):
        r"""Gets the backup_enable of this SnapshotPolicyResp.

        集群是否开启自动快照。

        :return: The backup_enable of this SnapshotPolicyResp.
        :rtype: bool
        """
        return self._backup_enable

    @backup_enable.setter
    def backup_enable(self, backup_enable):
        r"""Sets the backup_enable of this SnapshotPolicyResp.

        集群是否开启自动快照。

        :param backup_enable: The backup_enable of this SnapshotPolicyResp.
        :type backup_enable: bool
        """
        self._backup_enable = backup_enable

    @property
    def bak_period(self):
        r"""Gets the bak_period of this SnapshotPolicyResp.

        快照备份时间。

        :return: The bak_period of this SnapshotPolicyResp.
        :rtype: str
        """
        return self._bak_period

    @bak_period.setter
    def bak_period(self, bak_period):
        r"""Sets the bak_period of this SnapshotPolicyResp.

        快照备份时间。

        :param bak_period: The bak_period of this SnapshotPolicyResp.
        :type bak_period: str
        """
        self._bak_period = bak_period

    @property
    def bak_frequency(self):
        r"""Gets the bak_frequency of this SnapshotPolicyResp.

        快照备份间隔。

        :return: The bak_frequency of this SnapshotPolicyResp.
        :rtype: str
        """
        return self._bak_frequency

    @bak_frequency.setter
    def bak_frequency(self, bak_frequency):
        r"""Sets the bak_frequency of this SnapshotPolicyResp.

        快照备份间隔。

        :param bak_frequency: The bak_frequency of this SnapshotPolicyResp.
        :type bak_frequency: str
        """
        self._bak_frequency = bak_frequency

    @property
    def bak_keep_day(self):
        r"""Gets the bak_keep_day of this SnapshotPolicyResp.

        快照备份保留个数。

        :return: The bak_keep_day of this SnapshotPolicyResp.
        :rtype: int
        """
        return self._bak_keep_day

    @bak_keep_day.setter
    def bak_keep_day(self, bak_keep_day):
        r"""Sets the bak_keep_day of this SnapshotPolicyResp.

        快照备份保留个数。

        :param bak_keep_day: The bak_keep_day of this SnapshotPolicyResp.
        :type bak_keep_day: int
        """
        self._bak_keep_day = bak_keep_day

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
        if not isinstance(other, SnapshotPolicyResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
