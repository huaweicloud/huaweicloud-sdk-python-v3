# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateDesktopSnapshotReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]',
        'disk_type': 'str',
        'system_disk_snapshot': 'DiskSnapshotInfo',
        'data_disk_snapshot': 'DiskSnapshotInfo'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'disk_type': 'disk_type',
        'system_disk_snapshot': 'system_disk_snapshot',
        'data_disk_snapshot': 'data_disk_snapshot'
    }

    def __init__(self, desktop_ids=None, disk_type=None, system_disk_snapshot=None, data_disk_snapshot=None):
        r"""BatchCreateDesktopSnapshotReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 桌面id数组，最多支持100。
        :type desktop_ids: list[str]
        :param disk_type: 快照类型。 - SYSTEM_DISK 系统盘。 - DATA_DISKS 数据盘。 - ALL 系统盘和数据盘。
        :type disk_type: str
        :param system_disk_snapshot: 
        :type system_disk_snapshot: :class:`huaweicloudsdkworkspace.v2.DiskSnapshotInfo`
        :param data_disk_snapshot: 
        :type data_disk_snapshot: :class:`huaweicloudsdkworkspace.v2.DiskSnapshotInfo`
        """
        
        

        self._desktop_ids = None
        self._disk_type = None
        self._system_disk_snapshot = None
        self._data_disk_snapshot = None
        self.discriminator = None

        if desktop_ids is not None:
            self.desktop_ids = desktop_ids
        if disk_type is not None:
            self.disk_type = disk_type
        if system_disk_snapshot is not None:
            self.system_disk_snapshot = system_disk_snapshot
        if data_disk_snapshot is not None:
            self.data_disk_snapshot = data_disk_snapshot

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this BatchCreateDesktopSnapshotReq.

        桌面id数组，最多支持100。

        :return: The desktop_ids of this BatchCreateDesktopSnapshotReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this BatchCreateDesktopSnapshotReq.

        桌面id数组，最多支持100。

        :param desktop_ids: The desktop_ids of this BatchCreateDesktopSnapshotReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def disk_type(self):
        r"""Gets the disk_type of this BatchCreateDesktopSnapshotReq.

        快照类型。 - SYSTEM_DISK 系统盘。 - DATA_DISKS 数据盘。 - ALL 系统盘和数据盘。

        :return: The disk_type of this BatchCreateDesktopSnapshotReq.
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        r"""Sets the disk_type of this BatchCreateDesktopSnapshotReq.

        快照类型。 - SYSTEM_DISK 系统盘。 - DATA_DISKS 数据盘。 - ALL 系统盘和数据盘。

        :param disk_type: The disk_type of this BatchCreateDesktopSnapshotReq.
        :type disk_type: str
        """
        self._disk_type = disk_type

    @property
    def system_disk_snapshot(self):
        r"""Gets the system_disk_snapshot of this BatchCreateDesktopSnapshotReq.

        :return: The system_disk_snapshot of this BatchCreateDesktopSnapshotReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DiskSnapshotInfo`
        """
        return self._system_disk_snapshot

    @system_disk_snapshot.setter
    def system_disk_snapshot(self, system_disk_snapshot):
        r"""Sets the system_disk_snapshot of this BatchCreateDesktopSnapshotReq.

        :param system_disk_snapshot: The system_disk_snapshot of this BatchCreateDesktopSnapshotReq.
        :type system_disk_snapshot: :class:`huaweicloudsdkworkspace.v2.DiskSnapshotInfo`
        """
        self._system_disk_snapshot = system_disk_snapshot

    @property
    def data_disk_snapshot(self):
        r"""Gets the data_disk_snapshot of this BatchCreateDesktopSnapshotReq.

        :return: The data_disk_snapshot of this BatchCreateDesktopSnapshotReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DiskSnapshotInfo`
        """
        return self._data_disk_snapshot

    @data_disk_snapshot.setter
    def data_disk_snapshot(self, data_disk_snapshot):
        r"""Sets the data_disk_snapshot of this BatchCreateDesktopSnapshotReq.

        :param data_disk_snapshot: The data_disk_snapshot of this BatchCreateDesktopSnapshotReq.
        :type data_disk_snapshot: :class:`huaweicloudsdkworkspace.v2.DiskSnapshotInfo`
        """
        self._data_disk_snapshot = data_disk_snapshot

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
        if not isinstance(other, BatchCreateDesktopSnapshotReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
