# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterBackupStrategyBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period': 'str',
        'prefix': 'str',
        'keepday': 'int',
        'frequency': 'str',
        'bucket': 'str',
        'base_path': 'str',
        'agency': 'str',
        'max_snapshot_bytes_per_seconds': 'str',
        'max_restore_bytes_per_seconds': 'str'
    }

    attribute_map = {
        'period': 'period',
        'prefix': 'prefix',
        'keepday': 'keepday',
        'frequency': 'frequency',
        'bucket': 'bucket',
        'base_path': 'basePath',
        'agency': 'agency',
        'max_snapshot_bytes_per_seconds': 'maxSnapshotBytesPerSeconds',
        'max_restore_bytes_per_seconds': 'maxRestoreBytesPerSeconds'
    }

    def __init__(self, period=None, prefix=None, keepday=None, frequency=None, bucket=None, base_path=None, agency=None, max_snapshot_bytes_per_seconds=None, max_restore_bytes_per_seconds=None):
        r"""CreateClusterBackupStrategyBody

        The model defined in huaweicloud sdk

        :param period: 每天自动创建快照的时间点。只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。
        :type period: str
        :param prefix: 自动创建的快照的前缀，需要用户自己手动输入。只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。
        :type prefix: str
        :param keepday: 自动创建快照的保留天数。取值范围：1-90。
        :type keepday: int
        :param frequency: 快照速率参数。
        :type frequency: str
        :param bucket: 备份使用的OBS桶名称。
        :type bucket: str
        :param base_path: 快照在OBS桶中的存放路径。
        :type base_path: str
        :param agency: 委托名称，委托给CSS，允许CSS调用您的其他云服务。   &gt;如果bucket、basePath和agency三个参数同时为空，则系统会自动创建OBS桶和IAM代理（若创建失败，则需要手工配置正确的参数）。
        :type agency: str
        :param max_snapshot_bytes_per_seconds: 配置每个节点的最大备份速率（每秒），即当备份的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际备份速率不一定能达到该值，会受OBS、磁盘等影响。
        :type max_snapshot_bytes_per_seconds: str
        :param max_restore_bytes_per_seconds: 配置每个节点的最大恢复速率（每秒），即当恢复的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际恢复速率不一定能达到该值，会受OBS、磁盘等影响。
        :type max_restore_bytes_per_seconds: str
        """
        
        

        self._period = None
        self._prefix = None
        self._keepday = None
        self._frequency = None
        self._bucket = None
        self._base_path = None
        self._agency = None
        self._max_snapshot_bytes_per_seconds = None
        self._max_restore_bytes_per_seconds = None
        self.discriminator = None

        self.period = period
        self.prefix = prefix
        self.keepday = keepday
        if frequency is not None:
            self.frequency = frequency
        if bucket is not None:
            self.bucket = bucket
        if base_path is not None:
            self.base_path = base_path
        if agency is not None:
            self.agency = agency
        if max_snapshot_bytes_per_seconds is not None:
            self.max_snapshot_bytes_per_seconds = max_snapshot_bytes_per_seconds
        if max_restore_bytes_per_seconds is not None:
            self.max_restore_bytes_per_seconds = max_restore_bytes_per_seconds

    @property
    def period(self):
        r"""Gets the period of this CreateClusterBackupStrategyBody.

        每天自动创建快照的时间点。只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。

        :return: The period of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this CreateClusterBackupStrategyBody.

        每天自动创建快照的时间点。只支持整点，后面需加上时区，格式为“HH:mm z”，“HH:mm”表示整点时间，“z”表示时区。比如“00:00 GMT+08:00”、“01:00 GMT+08:00”等。

        :param period: The period of this CreateClusterBackupStrategyBody.
        :type period: str
        """
        self._period = period

    @property
    def prefix(self):
        r"""Gets the prefix of this CreateClusterBackupStrategyBody.

        自动创建的快照的前缀，需要用户自己手动输入。只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。

        :return: The prefix of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this CreateClusterBackupStrategyBody.

        自动创建的快照的前缀，需要用户自己手动输入。只能包含1~32位小写字母、数字、中划线或者下划线，并且以小写字母开头。

        :param prefix: The prefix of this CreateClusterBackupStrategyBody.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def keepday(self):
        r"""Gets the keepday of this CreateClusterBackupStrategyBody.

        自动创建快照的保留天数。取值范围：1-90。

        :return: The keepday of this CreateClusterBackupStrategyBody.
        :rtype: int
        """
        return self._keepday

    @keepday.setter
    def keepday(self, keepday):
        r"""Sets the keepday of this CreateClusterBackupStrategyBody.

        自动创建快照的保留天数。取值范围：1-90。

        :param keepday: The keepday of this CreateClusterBackupStrategyBody.
        :type keepday: int
        """
        self._keepday = keepday

    @property
    def frequency(self):
        r"""Gets the frequency of this CreateClusterBackupStrategyBody.

        快照速率参数。

        :return: The frequency of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this CreateClusterBackupStrategyBody.

        快照速率参数。

        :param frequency: The frequency of this CreateClusterBackupStrategyBody.
        :type frequency: str
        """
        self._frequency = frequency

    @property
    def bucket(self):
        r"""Gets the bucket of this CreateClusterBackupStrategyBody.

        备份使用的OBS桶名称。

        :return: The bucket of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this CreateClusterBackupStrategyBody.

        备份使用的OBS桶名称。

        :param bucket: The bucket of this CreateClusterBackupStrategyBody.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def base_path(self):
        r"""Gets the base_path of this CreateClusterBackupStrategyBody.

        快照在OBS桶中的存放路径。

        :return: The base_path of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        r"""Sets the base_path of this CreateClusterBackupStrategyBody.

        快照在OBS桶中的存放路径。

        :param base_path: The base_path of this CreateClusterBackupStrategyBody.
        :type base_path: str
        """
        self._base_path = base_path

    @property
    def agency(self):
        r"""Gets the agency of this CreateClusterBackupStrategyBody.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。   >如果bucket、basePath和agency三个参数同时为空，则系统会自动创建OBS桶和IAM代理（若创建失败，则需要手工配置正确的参数）。

        :return: The agency of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this CreateClusterBackupStrategyBody.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。   >如果bucket、basePath和agency三个参数同时为空，则系统会自动创建OBS桶和IAM代理（若创建失败，则需要手工配置正确的参数）。

        :param agency: The agency of this CreateClusterBackupStrategyBody.
        :type agency: str
        """
        self._agency = agency

    @property
    def max_snapshot_bytes_per_seconds(self):
        r"""Gets the max_snapshot_bytes_per_seconds of this CreateClusterBackupStrategyBody.

        配置每个节点的最大备份速率（每秒），即当备份的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际备份速率不一定能达到该值，会受OBS、磁盘等影响。

        :return: The max_snapshot_bytes_per_seconds of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._max_snapshot_bytes_per_seconds

    @max_snapshot_bytes_per_seconds.setter
    def max_snapshot_bytes_per_seconds(self, max_snapshot_bytes_per_seconds):
        r"""Sets the max_snapshot_bytes_per_seconds of this CreateClusterBackupStrategyBody.

        配置每个节点的最大备份速率（每秒），即当备份的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际备份速率不一定能达到该值，会受OBS、磁盘等影响。

        :param max_snapshot_bytes_per_seconds: The max_snapshot_bytes_per_seconds of this CreateClusterBackupStrategyBody.
        :type max_snapshot_bytes_per_seconds: str
        """
        self._max_snapshot_bytes_per_seconds = max_snapshot_bytes_per_seconds

    @property
    def max_restore_bytes_per_seconds(self):
        r"""Gets the max_restore_bytes_per_seconds of this CreateClusterBackupStrategyBody.

        配置每个节点的最大恢复速率（每秒），即当恢复的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际恢复速率不一定能达到该值，会受OBS、磁盘等影响。

        :return: The max_restore_bytes_per_seconds of this CreateClusterBackupStrategyBody.
        :rtype: str
        """
        return self._max_restore_bytes_per_seconds

    @max_restore_bytes_per_seconds.setter
    def max_restore_bytes_per_seconds(self, max_restore_bytes_per_seconds):
        r"""Sets the max_restore_bytes_per_seconds of this CreateClusterBackupStrategyBody.

        配置每个节点的最大恢复速率（每秒），即当恢复的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际恢复速率不一定能达到该值，会受OBS、磁盘等影响。

        :param max_restore_bytes_per_seconds: The max_restore_bytes_per_seconds of this CreateClusterBackupStrategyBody.
        :type max_restore_bytes_per_seconds: str
        """
        self._max_restore_bytes_per_seconds = max_restore_bytes_per_seconds

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
        if not isinstance(other, CreateClusterBackupStrategyBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
