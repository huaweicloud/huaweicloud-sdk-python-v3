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
        'max_restore_bytes_per_seconds': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'agency': 'agency',
        'base_path': 'base_path',
        'max_snapshot_bytes_per_seconds': 'maxSnapshotBytesPerSeconds',
        'max_restore_bytes_per_seconds': 'maxRestoreBytesPerSeconds'
    }

    def __init__(self, bucket=None, agency=None, base_path=None, max_snapshot_bytes_per_seconds=None, max_restore_bytes_per_seconds=None):
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
        """
        
        

        self._bucket = None
        self._agency = None
        self._base_path = None
        self._max_snapshot_bytes_per_seconds = None
        self._max_restore_bytes_per_seconds = None
        self.discriminator = None

        self.bucket = bucket
        self.agency = agency
        self.base_path = base_path
        if max_snapshot_bytes_per_seconds is not None:
            self.max_snapshot_bytes_per_seconds = max_snapshot_bytes_per_seconds
        if max_restore_bytes_per_seconds is not None:
            self.max_restore_bytes_per_seconds = max_restore_bytes_per_seconds

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
