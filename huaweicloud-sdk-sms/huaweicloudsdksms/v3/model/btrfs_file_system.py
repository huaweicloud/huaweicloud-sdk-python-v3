# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BtrfsFileSystem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'label': 'str',
        'uuid': 'str',
        'device': 'str',
        'size': 'int',
        'nodesize': 'int',
        'sectorsize': 'int',
        'data_profile': 'str',
        'system_profile': 'str',
        'metadata_profile': 'str',
        'global_reserve1': 'str',
        'g_vol_used_size': 'int',
        'default_subvolid': 'str',
        'default_subvol_name': 'str',
        'default_subvol_mountpath': 'str',
        'subvolumn': 'list[BtrfsSubvolumn]'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'uuid': 'uuid',
        'device': 'device',
        'size': 'size',
        'nodesize': 'nodesize',
        'sectorsize': 'sectorsize',
        'data_profile': 'data_profile',
        'system_profile': 'system_profile',
        'metadata_profile': 'metadata_profile',
        'global_reserve1': 'global_reserve1',
        'g_vol_used_size': 'g_vol_used_size',
        'default_subvolid': 'default_subvolid',
        'default_subvol_name': 'default_subvol_name',
        'default_subvol_mountpath': 'default_subvol_mountpath',
        'subvolumn': 'subvolumn'
    }

    def __init__(self, name=None, label=None, uuid=None, device=None, size=None, nodesize=None, sectorsize=None, data_profile=None, system_profile=None, metadata_profile=None, global_reserve1=None, g_vol_used_size=None, default_subvolid=None, default_subvol_name=None, default_subvol_mountpath=None, subvolumn=None):
        """BtrfsFileSystem

        The model defined in huaweicloud sdk

        :param name: 文件系统名称
        :type name: str
        :param label: 文件系统标签，若无标签为空字符串
        :type label: str
        :param uuid: 文件系统的uuid
        :type uuid: str
        :param device: btrfs包含的设备名称
        :type device: str
        :param size: 文件系统数据占用大小
        :type size: int
        :param nodesize: btrfs节点大小
        :type nodesize: int
        :param sectorsize: 扇区大小
        :type sectorsize: int
        :param data_profile: 数据配置（RAD）
        :type data_profile: str
        :param system_profile: 文件系统配置（RAD）
        :type system_profile: str
        :param metadata_profile: 元数据配置（RAD）
        :type metadata_profile: str
        :param global_reserve1: Btrfs文件系统信息
        :type global_reserve1: str
        :param g_vol_used_size: Btrfs卷已使用空间大小
        :type g_vol_used_size: int
        :param default_subvolid: 默认子卷ID
        :type default_subvolid: str
        :param default_subvol_name: 默认子卷名称
        :type default_subvol_name: str
        :param default_subvol_mountpath: 默认子卷挂载路径/BTRFS文件系统的挂载路径
        :type default_subvol_mountpath: str
        :param subvolumn: 子卷信息
        :type subvolumn: list[:class:`huaweicloudsdksms.v3.BtrfsSubvolumn`]
        """
        
        

        self._name = None
        self._label = None
        self._uuid = None
        self._device = None
        self._size = None
        self._nodesize = None
        self._sectorsize = None
        self._data_profile = None
        self._system_profile = None
        self._metadata_profile = None
        self._global_reserve1 = None
        self._g_vol_used_size = None
        self._default_subvolid = None
        self._default_subvol_name = None
        self._default_subvol_mountpath = None
        self._subvolumn = None
        self.discriminator = None

        self.name = name
        self.label = label
        self.uuid = uuid
        self.device = device
        self.size = size
        self.nodesize = nodesize
        self.sectorsize = sectorsize
        self.data_profile = data_profile
        self.system_profile = system_profile
        self.metadata_profile = metadata_profile
        self.global_reserve1 = global_reserve1
        self.g_vol_used_size = g_vol_used_size
        self.default_subvolid = default_subvolid
        self.default_subvol_name = default_subvol_name
        self.default_subvol_mountpath = default_subvol_mountpath
        self.subvolumn = subvolumn

    @property
    def name(self):
        """Gets the name of this BtrfsFileSystem.

        文件系统名称

        :return: The name of this BtrfsFileSystem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BtrfsFileSystem.

        文件系统名称

        :param name: The name of this BtrfsFileSystem.
        :type name: str
        """
        self._name = name

    @property
    def label(self):
        """Gets the label of this BtrfsFileSystem.

        文件系统标签，若无标签为空字符串

        :return: The label of this BtrfsFileSystem.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this BtrfsFileSystem.

        文件系统标签，若无标签为空字符串

        :param label: The label of this BtrfsFileSystem.
        :type label: str
        """
        self._label = label

    @property
    def uuid(self):
        """Gets the uuid of this BtrfsFileSystem.

        文件系统的uuid

        :return: The uuid of this BtrfsFileSystem.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this BtrfsFileSystem.

        文件系统的uuid

        :param uuid: The uuid of this BtrfsFileSystem.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def device(self):
        """Gets the device of this BtrfsFileSystem.

        btrfs包含的设备名称

        :return: The device of this BtrfsFileSystem.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this BtrfsFileSystem.

        btrfs包含的设备名称

        :param device: The device of this BtrfsFileSystem.
        :type device: str
        """
        self._device = device

    @property
    def size(self):
        """Gets the size of this BtrfsFileSystem.

        文件系统数据占用大小

        :return: The size of this BtrfsFileSystem.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BtrfsFileSystem.

        文件系统数据占用大小

        :param size: The size of this BtrfsFileSystem.
        :type size: int
        """
        self._size = size

    @property
    def nodesize(self):
        """Gets the nodesize of this BtrfsFileSystem.

        btrfs节点大小

        :return: The nodesize of this BtrfsFileSystem.
        :rtype: int
        """
        return self._nodesize

    @nodesize.setter
    def nodesize(self, nodesize):
        """Sets the nodesize of this BtrfsFileSystem.

        btrfs节点大小

        :param nodesize: The nodesize of this BtrfsFileSystem.
        :type nodesize: int
        """
        self._nodesize = nodesize

    @property
    def sectorsize(self):
        """Gets the sectorsize of this BtrfsFileSystem.

        扇区大小

        :return: The sectorsize of this BtrfsFileSystem.
        :rtype: int
        """
        return self._sectorsize

    @sectorsize.setter
    def sectorsize(self, sectorsize):
        """Sets the sectorsize of this BtrfsFileSystem.

        扇区大小

        :param sectorsize: The sectorsize of this BtrfsFileSystem.
        :type sectorsize: int
        """
        self._sectorsize = sectorsize

    @property
    def data_profile(self):
        """Gets the data_profile of this BtrfsFileSystem.

        数据配置（RAD）

        :return: The data_profile of this BtrfsFileSystem.
        :rtype: str
        """
        return self._data_profile

    @data_profile.setter
    def data_profile(self, data_profile):
        """Sets the data_profile of this BtrfsFileSystem.

        数据配置（RAD）

        :param data_profile: The data_profile of this BtrfsFileSystem.
        :type data_profile: str
        """
        self._data_profile = data_profile

    @property
    def system_profile(self):
        """Gets the system_profile of this BtrfsFileSystem.

        文件系统配置（RAD）

        :return: The system_profile of this BtrfsFileSystem.
        :rtype: str
        """
        return self._system_profile

    @system_profile.setter
    def system_profile(self, system_profile):
        """Sets the system_profile of this BtrfsFileSystem.

        文件系统配置（RAD）

        :param system_profile: The system_profile of this BtrfsFileSystem.
        :type system_profile: str
        """
        self._system_profile = system_profile

    @property
    def metadata_profile(self):
        """Gets the metadata_profile of this BtrfsFileSystem.

        元数据配置（RAD）

        :return: The metadata_profile of this BtrfsFileSystem.
        :rtype: str
        """
        return self._metadata_profile

    @metadata_profile.setter
    def metadata_profile(self, metadata_profile):
        """Sets the metadata_profile of this BtrfsFileSystem.

        元数据配置（RAD）

        :param metadata_profile: The metadata_profile of this BtrfsFileSystem.
        :type metadata_profile: str
        """
        self._metadata_profile = metadata_profile

    @property
    def global_reserve1(self):
        """Gets the global_reserve1 of this BtrfsFileSystem.

        Btrfs文件系统信息

        :return: The global_reserve1 of this BtrfsFileSystem.
        :rtype: str
        """
        return self._global_reserve1

    @global_reserve1.setter
    def global_reserve1(self, global_reserve1):
        """Sets the global_reserve1 of this BtrfsFileSystem.

        Btrfs文件系统信息

        :param global_reserve1: The global_reserve1 of this BtrfsFileSystem.
        :type global_reserve1: str
        """
        self._global_reserve1 = global_reserve1

    @property
    def g_vol_used_size(self):
        """Gets the g_vol_used_size of this BtrfsFileSystem.

        Btrfs卷已使用空间大小

        :return: The g_vol_used_size of this BtrfsFileSystem.
        :rtype: int
        """
        return self._g_vol_used_size

    @g_vol_used_size.setter
    def g_vol_used_size(self, g_vol_used_size):
        """Sets the g_vol_used_size of this BtrfsFileSystem.

        Btrfs卷已使用空间大小

        :param g_vol_used_size: The g_vol_used_size of this BtrfsFileSystem.
        :type g_vol_used_size: int
        """
        self._g_vol_used_size = g_vol_used_size

    @property
    def default_subvolid(self):
        """Gets the default_subvolid of this BtrfsFileSystem.

        默认子卷ID

        :return: The default_subvolid of this BtrfsFileSystem.
        :rtype: str
        """
        return self._default_subvolid

    @default_subvolid.setter
    def default_subvolid(self, default_subvolid):
        """Sets the default_subvolid of this BtrfsFileSystem.

        默认子卷ID

        :param default_subvolid: The default_subvolid of this BtrfsFileSystem.
        :type default_subvolid: str
        """
        self._default_subvolid = default_subvolid

    @property
    def default_subvol_name(self):
        """Gets the default_subvol_name of this BtrfsFileSystem.

        默认子卷名称

        :return: The default_subvol_name of this BtrfsFileSystem.
        :rtype: str
        """
        return self._default_subvol_name

    @default_subvol_name.setter
    def default_subvol_name(self, default_subvol_name):
        """Sets the default_subvol_name of this BtrfsFileSystem.

        默认子卷名称

        :param default_subvol_name: The default_subvol_name of this BtrfsFileSystem.
        :type default_subvol_name: str
        """
        self._default_subvol_name = default_subvol_name

    @property
    def default_subvol_mountpath(self):
        """Gets the default_subvol_mountpath of this BtrfsFileSystem.

        默认子卷挂载路径/BTRFS文件系统的挂载路径

        :return: The default_subvol_mountpath of this BtrfsFileSystem.
        :rtype: str
        """
        return self._default_subvol_mountpath

    @default_subvol_mountpath.setter
    def default_subvol_mountpath(self, default_subvol_mountpath):
        """Sets the default_subvol_mountpath of this BtrfsFileSystem.

        默认子卷挂载路径/BTRFS文件系统的挂载路径

        :param default_subvol_mountpath: The default_subvol_mountpath of this BtrfsFileSystem.
        :type default_subvol_mountpath: str
        """
        self._default_subvol_mountpath = default_subvol_mountpath

    @property
    def subvolumn(self):
        """Gets the subvolumn of this BtrfsFileSystem.

        子卷信息

        :return: The subvolumn of this BtrfsFileSystem.
        :rtype: list[:class:`huaweicloudsdksms.v3.BtrfsSubvolumn`]
        """
        return self._subvolumn

    @subvolumn.setter
    def subvolumn(self, subvolumn):
        """Sets the subvolumn of this BtrfsFileSystem.

        子卷信息

        :param subvolumn: The subvolumn of this BtrfsFileSystem.
        :type subvolumn: list[:class:`huaweicloudsdksms.v3.BtrfsSubvolumn`]
        """
        self._subvolumn = subvolumn

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
        if not isinstance(other, BtrfsFileSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
