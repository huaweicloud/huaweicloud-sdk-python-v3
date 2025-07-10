# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopSnapshotDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'snapshot_id': 'str',
        'snapshot_name': 'str',
        'desktop_id': 'str',
        'desktop_name': 'str',
        'desktop_sid': 'str',
        'desktop_pool_id': 'str',
        'is_system_disk': 'bool',
        'status': 'str',
        'process': 'int',
        'description': 'str',
        'create_time': 'str',
        'create_type': 'str',
        'last_restore_time': 'str',
        'restore_fail_reason': 'str'
    }

    attribute_map = {
        'snapshot_id': 'snapshot_id',
        'snapshot_name': 'snapshot_name',
        'desktop_id': 'desktop_id',
        'desktop_name': 'desktop_name',
        'desktop_sid': 'desktop_sid',
        'desktop_pool_id': 'desktop_pool_id',
        'is_system_disk': 'is_system_disk',
        'status': 'status',
        'process': 'process',
        'description': 'description',
        'create_time': 'create_time',
        'create_type': 'create_type',
        'last_restore_time': 'last_restore_time',
        'restore_fail_reason': 'restore_fail_reason'
    }

    def __init__(self, snapshot_id=None, snapshot_name=None, desktop_id=None, desktop_name=None, desktop_sid=None, desktop_pool_id=None, is_system_disk=None, status=None, process=None, description=None, create_time=None, create_type=None, last_restore_time=None, restore_fail_reason=None):
        r"""DesktopSnapshotDetailInfo

        The model defined in huaweicloud sdk

        :param snapshot_id: 桌面快照ID。
        :type snapshot_id: str
        :param snapshot_name: 桌面快照记录名称。
        :type snapshot_name: str
        :param desktop_id: 桌面快照对应的桌面id。
        :type desktop_id: str
        :param desktop_name: 桌面快照对应的桌面名称。
        :type desktop_name: str
        :param desktop_sid: 桌面快照对应的桌面sid。
        :type desktop_sid: str
        :param desktop_pool_id: 桌面快照对应的桌面池id。
        :type desktop_pool_id: str
        :param is_system_disk: 快照对应磁盘类型，true表示系统盘，false表示数据盘。
        :type is_system_disk: bool
        :param status: 快照状态。 - creating：表示创建中。 - restoring：表示恢复中。 - create_success：表示创建成功。 - create_failed：表示创建快照失败。 - restore_success：表示快照恢复成功。 - restore_failed：表示快照恢复失败。
        :type status: str
        :param process: 快照任务进度， 取值范围0-100以及null，null表示该快照无任务，0-100表明该任务进度的百分比。
        :type process: int
        :param description: 快照描述。
        :type description: str
        :param create_time: 快照的创建时间，UTC时间，格式为：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z。&#39;
        :type create_time: str
        :param create_type: 快照创建类型。 - AUTO 定时任务自动创建。 - MANUALLY 手动创建。
        :type create_type: str
        :param last_restore_time: 快照的最近恢复时间，UTC时间，格式为：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z。&#39;
        :type last_restore_time: str
        :param restore_fail_reason: 快照恢复失败原因。
        :type restore_fail_reason: str
        """
        
        

        self._snapshot_id = None
        self._snapshot_name = None
        self._desktop_id = None
        self._desktop_name = None
        self._desktop_sid = None
        self._desktop_pool_id = None
        self._is_system_disk = None
        self._status = None
        self._process = None
        self._description = None
        self._create_time = None
        self._create_type = None
        self._last_restore_time = None
        self._restore_fail_reason = None
        self.discriminator = None

        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if snapshot_name is not None:
            self.snapshot_name = snapshot_name
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if desktop_sid is not None:
            self.desktop_sid = desktop_sid
        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if is_system_disk is not None:
            self.is_system_disk = is_system_disk
        if status is not None:
            self.status = status
        if process is not None:
            self.process = process
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if create_type is not None:
            self.create_type = create_type
        if last_restore_time is not None:
            self.last_restore_time = last_restore_time
        if restore_fail_reason is not None:
            self.restore_fail_reason = restore_fail_reason

    @property
    def snapshot_id(self):
        r"""Gets the snapshot_id of this DesktopSnapshotDetailInfo.

        桌面快照ID。

        :return: The snapshot_id of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        r"""Sets the snapshot_id of this DesktopSnapshotDetailInfo.

        桌面快照ID。

        :param snapshot_id: The snapshot_id of this DesktopSnapshotDetailInfo.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    @property
    def snapshot_name(self):
        r"""Gets the snapshot_name of this DesktopSnapshotDetailInfo.

        桌面快照记录名称。

        :return: The snapshot_name of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._snapshot_name

    @snapshot_name.setter
    def snapshot_name(self, snapshot_name):
        r"""Sets the snapshot_name of this DesktopSnapshotDetailInfo.

        桌面快照记录名称。

        :param snapshot_name: The snapshot_name of this DesktopSnapshotDetailInfo.
        :type snapshot_name: str
        """
        self._snapshot_name = snapshot_name

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this DesktopSnapshotDetailInfo.

        桌面快照对应的桌面id。

        :return: The desktop_id of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this DesktopSnapshotDetailInfo.

        桌面快照对应的桌面id。

        :param desktop_id: The desktop_id of this DesktopSnapshotDetailInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this DesktopSnapshotDetailInfo.

        桌面快照对应的桌面名称。

        :return: The desktop_name of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this DesktopSnapshotDetailInfo.

        桌面快照对应的桌面名称。

        :param desktop_name: The desktop_name of this DesktopSnapshotDetailInfo.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def desktop_sid(self):
        r"""Gets the desktop_sid of this DesktopSnapshotDetailInfo.

        桌面快照对应的桌面sid。

        :return: The desktop_sid of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._desktop_sid

    @desktop_sid.setter
    def desktop_sid(self, desktop_sid):
        r"""Sets the desktop_sid of this DesktopSnapshotDetailInfo.

        桌面快照对应的桌面sid。

        :param desktop_sid: The desktop_sid of this DesktopSnapshotDetailInfo.
        :type desktop_sid: str
        """
        self._desktop_sid = desktop_sid

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this DesktopSnapshotDetailInfo.

        桌面快照对应的桌面池id。

        :return: The desktop_pool_id of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this DesktopSnapshotDetailInfo.

        桌面快照对应的桌面池id。

        :param desktop_pool_id: The desktop_pool_id of this DesktopSnapshotDetailInfo.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def is_system_disk(self):
        r"""Gets the is_system_disk of this DesktopSnapshotDetailInfo.

        快照对应磁盘类型，true表示系统盘，false表示数据盘。

        :return: The is_system_disk of this DesktopSnapshotDetailInfo.
        :rtype: bool
        """
        return self._is_system_disk

    @is_system_disk.setter
    def is_system_disk(self, is_system_disk):
        r"""Sets the is_system_disk of this DesktopSnapshotDetailInfo.

        快照对应磁盘类型，true表示系统盘，false表示数据盘。

        :param is_system_disk: The is_system_disk of this DesktopSnapshotDetailInfo.
        :type is_system_disk: bool
        """
        self._is_system_disk = is_system_disk

    @property
    def status(self):
        r"""Gets the status of this DesktopSnapshotDetailInfo.

        快照状态。 - creating：表示创建中。 - restoring：表示恢复中。 - create_success：表示创建成功。 - create_failed：表示创建快照失败。 - restore_success：表示快照恢复成功。 - restore_failed：表示快照恢复失败。

        :return: The status of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DesktopSnapshotDetailInfo.

        快照状态。 - creating：表示创建中。 - restoring：表示恢复中。 - create_success：表示创建成功。 - create_failed：表示创建快照失败。 - restore_success：表示快照恢复成功。 - restore_failed：表示快照恢复失败。

        :param status: The status of this DesktopSnapshotDetailInfo.
        :type status: str
        """
        self._status = status

    @property
    def process(self):
        r"""Gets the process of this DesktopSnapshotDetailInfo.

        快照任务进度， 取值范围0-100以及null，null表示该快照无任务，0-100表明该任务进度的百分比。

        :return: The process of this DesktopSnapshotDetailInfo.
        :rtype: int
        """
        return self._process

    @process.setter
    def process(self, process):
        r"""Sets the process of this DesktopSnapshotDetailInfo.

        快照任务进度， 取值范围0-100以及null，null表示该快照无任务，0-100表明该任务进度的百分比。

        :param process: The process of this DesktopSnapshotDetailInfo.
        :type process: int
        """
        self._process = process

    @property
    def description(self):
        r"""Gets the description of this DesktopSnapshotDetailInfo.

        快照描述。

        :return: The description of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DesktopSnapshotDetailInfo.

        快照描述。

        :param description: The description of this DesktopSnapshotDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this DesktopSnapshotDetailInfo.

        快照的创建时间，UTC时间，格式为：yyyy-MM-dd'T'HH:mm:ss'Z。'

        :return: The create_time of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this DesktopSnapshotDetailInfo.

        快照的创建时间，UTC时间，格式为：yyyy-MM-dd'T'HH:mm:ss'Z。'

        :param create_time: The create_time of this DesktopSnapshotDetailInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def create_type(self):
        r"""Gets the create_type of this DesktopSnapshotDetailInfo.

        快照创建类型。 - AUTO 定时任务自动创建。 - MANUALLY 手动创建。

        :return: The create_type of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._create_type

    @create_type.setter
    def create_type(self, create_type):
        r"""Sets the create_type of this DesktopSnapshotDetailInfo.

        快照创建类型。 - AUTO 定时任务自动创建。 - MANUALLY 手动创建。

        :param create_type: The create_type of this DesktopSnapshotDetailInfo.
        :type create_type: str
        """
        self._create_type = create_type

    @property
    def last_restore_time(self):
        r"""Gets the last_restore_time of this DesktopSnapshotDetailInfo.

        快照的最近恢复时间，UTC时间，格式为：yyyy-MM-dd'T'HH:mm:ss'Z。'

        :return: The last_restore_time of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._last_restore_time

    @last_restore_time.setter
    def last_restore_time(self, last_restore_time):
        r"""Sets the last_restore_time of this DesktopSnapshotDetailInfo.

        快照的最近恢复时间，UTC时间，格式为：yyyy-MM-dd'T'HH:mm:ss'Z。'

        :param last_restore_time: The last_restore_time of this DesktopSnapshotDetailInfo.
        :type last_restore_time: str
        """
        self._last_restore_time = last_restore_time

    @property
    def restore_fail_reason(self):
        r"""Gets the restore_fail_reason of this DesktopSnapshotDetailInfo.

        快照恢复失败原因。

        :return: The restore_fail_reason of this DesktopSnapshotDetailInfo.
        :rtype: str
        """
        return self._restore_fail_reason

    @restore_fail_reason.setter
    def restore_fail_reason(self, restore_fail_reason):
        r"""Sets the restore_fail_reason of this DesktopSnapshotDetailInfo.

        快照恢复失败原因。

        :param restore_fail_reason: The restore_fail_reason of this DesktopSnapshotDetailInfo.
        :type restore_fail_reason: str
        """
        self._restore_fail_reason = restore_fail_reason

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
        if not isinstance(other, DesktopSnapshotDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
