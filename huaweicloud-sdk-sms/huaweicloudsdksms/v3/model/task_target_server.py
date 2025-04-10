# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskTargetServer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'vm_id': 'str',
        'name': 'str',
        'ip': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'system_dir': 'str',
        'disks': 'list[TargetDisk]',
        'volume_groups': 'list[VolumeGroups]',
        'btrfs_list': 'list[str]',
        'image_disk_id': 'str',
        'cutovered_snapshot_ids': 'str'
    }

    attribute_map = {
        'id': 'id',
        'vm_id': 'vm_id',
        'name': 'name',
        'ip': 'ip',
        'os_type': 'os_type',
        'os_version': 'os_version',
        'system_dir': 'system_dir',
        'disks': 'disks',
        'volume_groups': 'volume_groups',
        'btrfs_list': 'btrfs_list',
        'image_disk_id': 'image_disk_id',
        'cutovered_snapshot_ids': 'cutovered_snapshot_ids'
    }

    def __init__(self, id=None, vm_id=None, name=None, ip=None, os_type=None, os_version=None, system_dir=None, disks=None, volume_groups=None, btrfs_list=None, image_disk_id=None, cutovered_snapshot_ids=None):
        r"""TaskTargetServer

        The model defined in huaweicloud sdk

        :param id: 目的端在SMS数据库中的ID
        :type id: str
        :param vm_id: 目的端服务器ID，自动创建虚拟机不需要这个参数
        :type vm_id: str
        :param name: 目的端服务器的名称
        :type name: str
        :param ip: 目的端服务器IP
        :type ip: str
        :param os_type: 源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选
        :type os_type: str
        :param os_version: 操作系统版本，注册必选，更新非必选
        :type os_version: str
        :param system_dir: Windows必选，系统目录
        :type system_dir: str
        :param disks: 目的端磁盘信息，一般和源端保持一致
        :type disks: list[:class:`huaweicloudsdksms.v3.TargetDisk`]
        :param volume_groups: lvm信息，一般和源端保持一致
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        :param btrfs_list: Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]
        :type btrfs_list: list[str]
        :param image_disk_id: 目的端代理镜像磁盘ID
        :type image_disk_id: str
        :param cutovered_snapshot_ids: 目的端回滚快照ID
        :type cutovered_snapshot_ids: str
        """
        
        

        self._id = None
        self._vm_id = None
        self._name = None
        self._ip = None
        self._os_type = None
        self._os_version = None
        self._system_dir = None
        self._disks = None
        self._volume_groups = None
        self._btrfs_list = None
        self._image_disk_id = None
        self._cutovered_snapshot_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vm_id is not None:
            self.vm_id = vm_id
        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip
        if os_type is not None:
            self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if system_dir is not None:
            self.system_dir = system_dir
        self.disks = disks
        if volume_groups is not None:
            self.volume_groups = volume_groups
        if btrfs_list is not None:
            self.btrfs_list = btrfs_list
        if image_disk_id is not None:
            self.image_disk_id = image_disk_id
        if cutovered_snapshot_ids is not None:
            self.cutovered_snapshot_ids = cutovered_snapshot_ids

    @property
    def id(self):
        r"""Gets the id of this TaskTargetServer.

        目的端在SMS数据库中的ID

        :return: The id of this TaskTargetServer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskTargetServer.

        目的端在SMS数据库中的ID

        :param id: The id of this TaskTargetServer.
        :type id: str
        """
        self._id = id

    @property
    def vm_id(self):
        r"""Gets the vm_id of this TaskTargetServer.

        目的端服务器ID，自动创建虚拟机不需要这个参数

        :return: The vm_id of this TaskTargetServer.
        :rtype: str
        """
        return self._vm_id

    @vm_id.setter
    def vm_id(self, vm_id):
        r"""Sets the vm_id of this TaskTargetServer.

        目的端服务器ID，自动创建虚拟机不需要这个参数

        :param vm_id: The vm_id of this TaskTargetServer.
        :type vm_id: str
        """
        self._vm_id = vm_id

    @property
    def name(self):
        r"""Gets the name of this TaskTargetServer.

        目的端服务器的名称

        :return: The name of this TaskTargetServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskTargetServer.

        目的端服务器的名称

        :param name: The name of this TaskTargetServer.
        :type name: str
        """
        self._name = name

    @property
    def ip(self):
        r"""Gets the ip of this TaskTargetServer.

        目的端服务器IP

        :return: The ip of this TaskTargetServer.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this TaskTargetServer.

        目的端服务器IP

        :param ip: The ip of this TaskTargetServer.
        :type ip: str
        """
        self._ip = ip

    @property
    def os_type(self):
        r"""Gets the os_type of this TaskTargetServer.

        源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选

        :return: The os_type of this TaskTargetServer.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this TaskTargetServer.

        源端服务器的OS类型，分为Windows和Linux，注册必选，更新非必选

        :param os_type: The os_type of this TaskTargetServer.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        r"""Gets the os_version of this TaskTargetServer.

        操作系统版本，注册必选，更新非必选

        :return: The os_version of this TaskTargetServer.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this TaskTargetServer.

        操作系统版本，注册必选，更新非必选

        :param os_version: The os_version of this TaskTargetServer.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def system_dir(self):
        r"""Gets the system_dir of this TaskTargetServer.

        Windows必选，系统目录

        :return: The system_dir of this TaskTargetServer.
        :rtype: str
        """
        return self._system_dir

    @system_dir.setter
    def system_dir(self, system_dir):
        r"""Sets the system_dir of this TaskTargetServer.

        Windows必选，系统目录

        :param system_dir: The system_dir of this TaskTargetServer.
        :type system_dir: str
        """
        self._system_dir = system_dir

    @property
    def disks(self):
        r"""Gets the disks of this TaskTargetServer.

        目的端磁盘信息，一般和源端保持一致

        :return: The disks of this TaskTargetServer.
        :rtype: list[:class:`huaweicloudsdksms.v3.TargetDisk`]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        r"""Sets the disks of this TaskTargetServer.

        目的端磁盘信息，一般和源端保持一致

        :param disks: The disks of this TaskTargetServer.
        :type disks: list[:class:`huaweicloudsdksms.v3.TargetDisk`]
        """
        self._disks = disks

    @property
    def volume_groups(self):
        r"""Gets the volume_groups of this TaskTargetServer.

        lvm信息，一般和源端保持一致

        :return: The volume_groups of this TaskTargetServer.
        :rtype: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        return self._volume_groups

    @volume_groups.setter
    def volume_groups(self, volume_groups):
        r"""Sets the volume_groups of this TaskTargetServer.

        lvm信息，一般和源端保持一致

        :param volume_groups: The volume_groups of this TaskTargetServer.
        :type volume_groups: list[:class:`huaweicloudsdksms.v3.VolumeGroups`]
        """
        self._volume_groups = volume_groups

    @property
    def btrfs_list(self):
        r"""Gets the btrfs_list of this TaskTargetServer.

        Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]

        :return: The btrfs_list of this TaskTargetServer.
        :rtype: list[str]
        """
        return self._btrfs_list

    @btrfs_list.setter
    def btrfs_list(self, btrfs_list):
        r"""Sets the btrfs_list of this TaskTargetServer.

        Linux 必选，源端的Btrfs信息。如果源端不存在Btrfs，则为[]

        :param btrfs_list: The btrfs_list of this TaskTargetServer.
        :type btrfs_list: list[str]
        """
        self._btrfs_list = btrfs_list

    @property
    def image_disk_id(self):
        r"""Gets the image_disk_id of this TaskTargetServer.

        目的端代理镜像磁盘ID

        :return: The image_disk_id of this TaskTargetServer.
        :rtype: str
        """
        return self._image_disk_id

    @image_disk_id.setter
    def image_disk_id(self, image_disk_id):
        r"""Sets the image_disk_id of this TaskTargetServer.

        目的端代理镜像磁盘ID

        :param image_disk_id: The image_disk_id of this TaskTargetServer.
        :type image_disk_id: str
        """
        self._image_disk_id = image_disk_id

    @property
    def cutovered_snapshot_ids(self):
        r"""Gets the cutovered_snapshot_ids of this TaskTargetServer.

        目的端回滚快照ID

        :return: The cutovered_snapshot_ids of this TaskTargetServer.
        :rtype: str
        """
        return self._cutovered_snapshot_ids

    @cutovered_snapshot_ids.setter
    def cutovered_snapshot_ids(self, cutovered_snapshot_ids):
        r"""Sets the cutovered_snapshot_ids of this TaskTargetServer.

        目的端回滚快照ID

        :param cutovered_snapshot_ids: The cutovered_snapshot_ids of this TaskTargetServer.
        :type cutovered_snapshot_ids: str
        """
        self._cutovered_snapshot_ids = cutovered_snapshot_ids

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
        if not isinstance(other, TaskTargetServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
