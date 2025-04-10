# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDesktopSnapshotRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'desktop_name': 'str',
        'snapshot_name': 'str',
        'disk_type': 'str',
        'create_type': 'str',
        'status': 'str',
        'sort_field': 'str',
        'sort_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'snapshot_name': 'snapshot_name',
        'disk_type': 'disk_type',
        'create_type': 'create_type',
        'status': 'status',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, desktop_id=None, desktop_name=None, snapshot_name=None, disk_type=None, create_type=None, status=None, sort_field=None, sort_type=None, offset=None, limit=None):
        r"""ListDesktopSnapshotRequest

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面id。
        :type desktop_id: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param snapshot_name: 快照名称。
        :type snapshot_name: str
        :param disk_type: 快照类型。 - SYSTEM_DISK 系统盘。 - DATA_DISKS 数据盘。 - ALL 系统盘和数据盘。
        :type disk_type: str
        :param create_type: 快照创建类型。 - AUTO 定时任务自动创建。 - MANUALLY 手动创建。
        :type create_type: str
        :param status: 快照状态。 - creating：表示创建中。 - restoring：表示恢复中。 - create_success：表示创建成功。 - create_failed：表示创建快照失败。 - restore_success：表示快照恢复成功。 - restore_failed：表示快照恢复失败。
        :type status: str
        :param sort_field: 排序字段名称，需要结合sort_type字段一起使用。 - create_time 创建时间。 - snapshot_name 快照名称。
        :type sort_field: str
        :param sort_type: 排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。
        :type sort_type: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询。默认1000,取值范围1-1000。
        :type limit: int
        """
        
        

        self._desktop_id = None
        self._desktop_name = None
        self._snapshot_name = None
        self._disk_type = None
        self._create_type = None
        self._status = None
        self._sort_field = None
        self._sort_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if snapshot_name is not None:
            self.snapshot_name = snapshot_name
        if disk_type is not None:
            self.disk_type = disk_type
        if create_type is not None:
            self.create_type = create_type
        if status is not None:
            self.status = status
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ListDesktopSnapshotRequest.

        桌面id。

        :return: The desktop_id of this ListDesktopSnapshotRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ListDesktopSnapshotRequest.

        桌面id。

        :param desktop_id: The desktop_id of this ListDesktopSnapshotRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this ListDesktopSnapshotRequest.

        桌面名称。

        :return: The desktop_name of this ListDesktopSnapshotRequest.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this ListDesktopSnapshotRequest.

        桌面名称。

        :param desktop_name: The desktop_name of this ListDesktopSnapshotRequest.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def snapshot_name(self):
        r"""Gets the snapshot_name of this ListDesktopSnapshotRequest.

        快照名称。

        :return: The snapshot_name of this ListDesktopSnapshotRequest.
        :rtype: str
        """
        return self._snapshot_name

    @snapshot_name.setter
    def snapshot_name(self, snapshot_name):
        r"""Sets the snapshot_name of this ListDesktopSnapshotRequest.

        快照名称。

        :param snapshot_name: The snapshot_name of this ListDesktopSnapshotRequest.
        :type snapshot_name: str
        """
        self._snapshot_name = snapshot_name

    @property
    def disk_type(self):
        r"""Gets the disk_type of this ListDesktopSnapshotRequest.

        快照类型。 - SYSTEM_DISK 系统盘。 - DATA_DISKS 数据盘。 - ALL 系统盘和数据盘。

        :return: The disk_type of this ListDesktopSnapshotRequest.
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        r"""Sets the disk_type of this ListDesktopSnapshotRequest.

        快照类型。 - SYSTEM_DISK 系统盘。 - DATA_DISKS 数据盘。 - ALL 系统盘和数据盘。

        :param disk_type: The disk_type of this ListDesktopSnapshotRequest.
        :type disk_type: str
        """
        self._disk_type = disk_type

    @property
    def create_type(self):
        r"""Gets the create_type of this ListDesktopSnapshotRequest.

        快照创建类型。 - AUTO 定时任务自动创建。 - MANUALLY 手动创建。

        :return: The create_type of this ListDesktopSnapshotRequest.
        :rtype: str
        """
        return self._create_type

    @create_type.setter
    def create_type(self, create_type):
        r"""Sets the create_type of this ListDesktopSnapshotRequest.

        快照创建类型。 - AUTO 定时任务自动创建。 - MANUALLY 手动创建。

        :param create_type: The create_type of this ListDesktopSnapshotRequest.
        :type create_type: str
        """
        self._create_type = create_type

    @property
    def status(self):
        r"""Gets the status of this ListDesktopSnapshotRequest.

        快照状态。 - creating：表示创建中。 - restoring：表示恢复中。 - create_success：表示创建成功。 - create_failed：表示创建快照失败。 - restore_success：表示快照恢复成功。 - restore_failed：表示快照恢复失败。

        :return: The status of this ListDesktopSnapshotRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListDesktopSnapshotRequest.

        快照状态。 - creating：表示创建中。 - restoring：表示恢复中。 - create_success：表示创建成功。 - create_failed：表示创建快照失败。 - restore_success：表示快照恢复成功。 - restore_failed：表示快照恢复失败。

        :param status: The status of this ListDesktopSnapshotRequest.
        :type status: str
        """
        self._status = status

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListDesktopSnapshotRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - create_time 创建时间。 - snapshot_name 快照名称。

        :return: The sort_field of this ListDesktopSnapshotRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListDesktopSnapshotRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - create_time 创建时间。 - snapshot_name 快照名称。

        :param sort_field: The sort_field of this ListDesktopSnapshotRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this ListDesktopSnapshotRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :return: The sort_type of this ListDesktopSnapshotRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this ListDesktopSnapshotRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :param sort_type: The sort_type of this ListDesktopSnapshotRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def offset(self):
        r"""Gets the offset of this ListDesktopSnapshotRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListDesktopSnapshotRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDesktopSnapshotRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListDesktopSnapshotRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDesktopSnapshotRequest.

        用于分页查询。默认1000,取值范围1-1000。

        :return: The limit of this ListDesktopSnapshotRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDesktopSnapshotRequest.

        用于分页查询。默认1000,取值范围1-1000。

        :param limit: The limit of this ListDesktopSnapshotRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDesktopSnapshotRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
