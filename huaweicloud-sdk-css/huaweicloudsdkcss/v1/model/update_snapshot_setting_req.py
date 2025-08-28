# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSnapshotSettingReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'agency': 'str',
        'base_path': 'str',
        'max_snapshot_bytes_per_seconds': 'str',
        'max_restore_bytes_per_seconds': 'str',
        'enable': 'str',
        'indices': 'str',
        'prefix': 'str',
        'period': 'str',
        'keepday': 'int',
        'frequency': 'str',
        'delete_auto': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'agency': 'agency',
        'base_path': 'base_path',
        'max_snapshot_bytes_per_seconds': 'max_snapshot_bytes_per_seconds',
        'max_restore_bytes_per_seconds': 'max_restore_bytes_per_seconds',
        'enable': 'enable',
        'indices': 'indices',
        'prefix': 'prefix',
        'period': 'period',
        'keepday': 'keepday',
        'frequency': 'frequency',
        'delete_auto': 'delete_auto'
    }

    def __init__(self, bucket=None, agency=None, base_path=None, max_snapshot_bytes_per_seconds=None, max_restore_bytes_per_seconds=None, enable=None, indices=None, prefix=None, period=None, keepday=None, frequency=None, delete_auto=None):
        r"""UpdateSnapshotSettingReq

        The model defined in huaweicloud sdk

        :param bucket: 备份使用的OBS桶的桶名。
        :type bucket: str
        :param agency: 委托名称，委托给CSS，允许CSS调用您的其他云服务。
        :type agency: str
        :param base_path: 快照在OBS桶中的存放路径。
        :type base_path: str
        :param max_snapshot_bytes_per_seconds: 配置每个节点的最大备份速率（每秒），即当备份的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际备份速率不一定能达到该值，会受OBS、磁盘等影响。
        :type max_snapshot_bytes_per_seconds: str
        :param max_restore_bytes_per_seconds: 配置每个节点的最大恢复速率（每秒），即当恢复的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际恢复速率不一定能达到该值，会受OBS、磁盘等影响。
        :type max_restore_bytes_per_seconds: str
        :param enable: 是否开启自动创建快照策略。
        :type enable: str
        :param indices: 需要备份的索引名。
        :type indices: str
        :param prefix: 自动创建快照的名称前缀，需要用户自己手动输入。
        :type prefix: str
        :param period: 每天创建快照的时刻。
        :type period: str
        :param keepday: 自定义设置快照保留的个数。系统在半点时刻会自动删除超过保留个数的快照。过期删除策略只针对与当前自动创建快照策略相同执行频次的自动快照。
        :type keepday: int
        :param frequency: 自动创建快照的执行频次。
        :type frequency: str
        :param delete_auto: 表示关闭自动创建快照策略时，是否需要清除所有自动创建的快照。
        :type delete_auto: str
        """
        
        

        self._bucket = None
        self._agency = None
        self._base_path = None
        self._max_snapshot_bytes_per_seconds = None
        self._max_restore_bytes_per_seconds = None
        self._enable = None
        self._indices = None
        self._prefix = None
        self._period = None
        self._keepday = None
        self._frequency = None
        self._delete_auto = None
        self.discriminator = None

        self.bucket = bucket
        self.agency = agency
        self.base_path = base_path
        if max_snapshot_bytes_per_seconds is not None:
            self.max_snapshot_bytes_per_seconds = max_snapshot_bytes_per_seconds
        if max_restore_bytes_per_seconds is not None:
            self.max_restore_bytes_per_seconds = max_restore_bytes_per_seconds
        if enable is not None:
            self.enable = enable
        if indices is not None:
            self.indices = indices
        if prefix is not None:
            self.prefix = prefix
        if period is not None:
            self.period = period
        if keepday is not None:
            self.keepday = keepday
        if frequency is not None:
            self.frequency = frequency
        if delete_auto is not None:
            self.delete_auto = delete_auto

    @property
    def bucket(self):
        r"""Gets the bucket of this UpdateSnapshotSettingReq.

        备份使用的OBS桶的桶名。

        :return: The bucket of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this UpdateSnapshotSettingReq.

        备份使用的OBS桶的桶名。

        :param bucket: The bucket of this UpdateSnapshotSettingReq.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def agency(self):
        r"""Gets the agency of this UpdateSnapshotSettingReq.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :return: The agency of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this UpdateSnapshotSettingReq.

        委托名称，委托给CSS，允许CSS调用您的其他云服务。

        :param agency: The agency of this UpdateSnapshotSettingReq.
        :type agency: str
        """
        self._agency = agency

    @property
    def base_path(self):
        r"""Gets the base_path of this UpdateSnapshotSettingReq.

        快照在OBS桶中的存放路径。

        :return: The base_path of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        r"""Sets the base_path of this UpdateSnapshotSettingReq.

        快照在OBS桶中的存放路径。

        :param base_path: The base_path of this UpdateSnapshotSettingReq.
        :type base_path: str
        """
        self._base_path = base_path

    @property
    def max_snapshot_bytes_per_seconds(self):
        r"""Gets the max_snapshot_bytes_per_seconds of this UpdateSnapshotSettingReq.

        配置每个节点的最大备份速率（每秒），即当备份的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际备份速率不一定能达到该值，会受OBS、磁盘等影响。

        :return: The max_snapshot_bytes_per_seconds of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._max_snapshot_bytes_per_seconds

    @max_snapshot_bytes_per_seconds.setter
    def max_snapshot_bytes_per_seconds(self, max_snapshot_bytes_per_seconds):
        r"""Sets the max_snapshot_bytes_per_seconds of this UpdateSnapshotSettingReq.

        配置每个节点的最大备份速率（每秒），即当备份的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际备份速率不一定能达到该值，会受OBS、磁盘等影响。

        :param max_snapshot_bytes_per_seconds: The max_snapshot_bytes_per_seconds of this UpdateSnapshotSettingReq.
        :type max_snapshot_bytes_per_seconds: str
        """
        self._max_snapshot_bytes_per_seconds = max_snapshot_bytes_per_seconds

    @property
    def max_restore_bytes_per_seconds(self):
        r"""Gets the max_restore_bytes_per_seconds of this UpdateSnapshotSettingReq.

        配置每个节点的最大恢复速率（每秒），即当恢复的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际恢复速率不一定能达到该值，会受OBS、磁盘等影响。

        :return: The max_restore_bytes_per_seconds of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._max_restore_bytes_per_seconds

    @max_restore_bytes_per_seconds.setter
    def max_restore_bytes_per_seconds(self, max_restore_bytes_per_seconds):
        r"""Sets the max_restore_bytes_per_seconds of this UpdateSnapshotSettingReq.

        配置每个节点的最大恢复速率（每秒），即当恢复的速率超过该值时会被限流，避免速率太大导致资源占用过高，影响系统稳定性。实际恢复速率不一定能达到该值，会受OBS、磁盘等影响。

        :param max_restore_bytes_per_seconds: The max_restore_bytes_per_seconds of this UpdateSnapshotSettingReq.
        :type max_restore_bytes_per_seconds: str
        """
        self._max_restore_bytes_per_seconds = max_restore_bytes_per_seconds

    @property
    def enable(self):
        r"""Gets the enable of this UpdateSnapshotSettingReq.

        是否开启自动创建快照策略。

        :return: The enable of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this UpdateSnapshotSettingReq.

        是否开启自动创建快照策略。

        :param enable: The enable of this UpdateSnapshotSettingReq.
        :type enable: str
        """
        self._enable = enable

    @property
    def indices(self):
        r"""Gets the indices of this UpdateSnapshotSettingReq.

        需要备份的索引名。

        :return: The indices of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._indices

    @indices.setter
    def indices(self, indices):
        r"""Sets the indices of this UpdateSnapshotSettingReq.

        需要备份的索引名。

        :param indices: The indices of this UpdateSnapshotSettingReq.
        :type indices: str
        """
        self._indices = indices

    @property
    def prefix(self):
        r"""Gets the prefix of this UpdateSnapshotSettingReq.

        自动创建快照的名称前缀，需要用户自己手动输入。

        :return: The prefix of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this UpdateSnapshotSettingReq.

        自动创建快照的名称前缀，需要用户自己手动输入。

        :param prefix: The prefix of this UpdateSnapshotSettingReq.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def period(self):
        r"""Gets the period of this UpdateSnapshotSettingReq.

        每天创建快照的时刻。

        :return: The period of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this UpdateSnapshotSettingReq.

        每天创建快照的时刻。

        :param period: The period of this UpdateSnapshotSettingReq.
        :type period: str
        """
        self._period = period

    @property
    def keepday(self):
        r"""Gets the keepday of this UpdateSnapshotSettingReq.

        自定义设置快照保留的个数。系统在半点时刻会自动删除超过保留个数的快照。过期删除策略只针对与当前自动创建快照策略相同执行频次的自动快照。

        :return: The keepday of this UpdateSnapshotSettingReq.
        :rtype: int
        """
        return self._keepday

    @keepday.setter
    def keepday(self, keepday):
        r"""Sets the keepday of this UpdateSnapshotSettingReq.

        自定义设置快照保留的个数。系统在半点时刻会自动删除超过保留个数的快照。过期删除策略只针对与当前自动创建快照策略相同执行频次的自动快照。

        :param keepday: The keepday of this UpdateSnapshotSettingReq.
        :type keepday: int
        """
        self._keepday = keepday

    @property
    def frequency(self):
        r"""Gets the frequency of this UpdateSnapshotSettingReq.

        自动创建快照的执行频次。

        :return: The frequency of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        r"""Sets the frequency of this UpdateSnapshotSettingReq.

        自动创建快照的执行频次。

        :param frequency: The frequency of this UpdateSnapshotSettingReq.
        :type frequency: str
        """
        self._frequency = frequency

    @property
    def delete_auto(self):
        r"""Gets the delete_auto of this UpdateSnapshotSettingReq.

        表示关闭自动创建快照策略时，是否需要清除所有自动创建的快照。

        :return: The delete_auto of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._delete_auto

    @delete_auto.setter
    def delete_auto(self, delete_auto):
        r"""Sets the delete_auto of this UpdateSnapshotSettingReq.

        表示关闭自动创建快照策略时，是否需要清除所有自动创建的快照。

        :param delete_auto: The delete_auto of this UpdateSnapshotSettingReq.
        :type delete_auto: str
        """
        self._delete_auto = delete_auto

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
        if not isinstance(other, UpdateSnapshotSettingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
