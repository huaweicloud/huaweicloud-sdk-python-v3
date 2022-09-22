# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicalVolumes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'block_count': 'int',
        'block_size': 'int',
        'file_system': 'str',
        'inode_size': 'int',
        'device_use': 'int',
        'mount_point': 'str',
        'name': 'str',
        'size': 'int',
        'used_size': 'int',
        'free_size': 'int'
    }

    attribute_map = {
        'block_count': 'block_count',
        'block_size': 'block_size',
        'file_system': 'file_system',
        'inode_size': 'inode_size',
        'device_use': 'device_use',
        'mount_point': 'mount_point',
        'name': 'name',
        'size': 'size',
        'used_size': 'used_size',
        'free_size': 'free_size'
    }

    def __init__(self, block_count=None, block_size=None, file_system=None, inode_size=None, device_use=None, mount_point=None, name=None, size=None, used_size=None, free_size=None):
        """LogicalVolumes

        The model defined in huaweicloud sdk

        :param block_count: 块数量
        :type block_count: int
        :param block_size: 块大小
        :type block_size: int
        :param file_system: 文件系统
        :type file_system: str
        :param inode_size: inode数量
        :type inode_size: int
        :param device_use: 已使用大小
        :type device_use: int
        :param mount_point: 挂载点
        :type mount_point: str
        :param name: 名称
        :type name: str
        :param size: 大小
        :type size: int
        :param used_size: 使用大小
        :type used_size: int
        :param free_size: 剩余空间
        :type free_size: int
        """
        
        

        self._block_count = None
        self._block_size = None
        self._file_system = None
        self._inode_size = None
        self._device_use = None
        self._mount_point = None
        self._name = None
        self._size = None
        self._used_size = None
        self._free_size = None
        self.discriminator = None

        if block_count is not None:
            self.block_count = block_count
        if block_size is not None:
            self.block_size = block_size
        self.file_system = file_system
        self.inode_size = inode_size
        if device_use is not None:
            self.device_use = device_use
        self.mount_point = mount_point
        self.name = name
        self.size = size
        self.used_size = used_size
        self.free_size = free_size

    @property
    def block_count(self):
        """Gets the block_count of this LogicalVolumes.

        块数量

        :return: The block_count of this LogicalVolumes.
        :rtype: int
        """
        return self._block_count

    @block_count.setter
    def block_count(self, block_count):
        """Sets the block_count of this LogicalVolumes.

        块数量

        :param block_count: The block_count of this LogicalVolumes.
        :type block_count: int
        """
        self._block_count = block_count

    @property
    def block_size(self):
        """Gets the block_size of this LogicalVolumes.

        块大小

        :return: The block_size of this LogicalVolumes.
        :rtype: int
        """
        return self._block_size

    @block_size.setter
    def block_size(self, block_size):
        """Sets the block_size of this LogicalVolumes.

        块大小

        :param block_size: The block_size of this LogicalVolumes.
        :type block_size: int
        """
        self._block_size = block_size

    @property
    def file_system(self):
        """Gets the file_system of this LogicalVolumes.

        文件系统

        :return: The file_system of this LogicalVolumes.
        :rtype: str
        """
        return self._file_system

    @file_system.setter
    def file_system(self, file_system):
        """Sets the file_system of this LogicalVolumes.

        文件系统

        :param file_system: The file_system of this LogicalVolumes.
        :type file_system: str
        """
        self._file_system = file_system

    @property
    def inode_size(self):
        """Gets the inode_size of this LogicalVolumes.

        inode数量

        :return: The inode_size of this LogicalVolumes.
        :rtype: int
        """
        return self._inode_size

    @inode_size.setter
    def inode_size(self, inode_size):
        """Sets the inode_size of this LogicalVolumes.

        inode数量

        :param inode_size: The inode_size of this LogicalVolumes.
        :type inode_size: int
        """
        self._inode_size = inode_size

    @property
    def device_use(self):
        """Gets the device_use of this LogicalVolumes.

        已使用大小

        :return: The device_use of this LogicalVolumes.
        :rtype: int
        """
        return self._device_use

    @device_use.setter
    def device_use(self, device_use):
        """Sets the device_use of this LogicalVolumes.

        已使用大小

        :param device_use: The device_use of this LogicalVolumes.
        :type device_use: int
        """
        self._device_use = device_use

    @property
    def mount_point(self):
        """Gets the mount_point of this LogicalVolumes.

        挂载点

        :return: The mount_point of this LogicalVolumes.
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """Sets the mount_point of this LogicalVolumes.

        挂载点

        :param mount_point: The mount_point of this LogicalVolumes.
        :type mount_point: str
        """
        self._mount_point = mount_point

    @property
    def name(self):
        """Gets the name of this LogicalVolumes.

        名称

        :return: The name of this LogicalVolumes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LogicalVolumes.

        名称

        :param name: The name of this LogicalVolumes.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this LogicalVolumes.

        大小

        :return: The size of this LogicalVolumes.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LogicalVolumes.

        大小

        :param size: The size of this LogicalVolumes.
        :type size: int
        """
        self._size = size

    @property
    def used_size(self):
        """Gets the used_size of this LogicalVolumes.

        使用大小

        :return: The used_size of this LogicalVolumes.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        """Sets the used_size of this LogicalVolumes.

        使用大小

        :param used_size: The used_size of this LogicalVolumes.
        :type used_size: int
        """
        self._used_size = used_size

    @property
    def free_size(self):
        """Gets the free_size of this LogicalVolumes.

        剩余空间

        :return: The free_size of this LogicalVolumes.
        :rtype: int
        """
        return self._free_size

    @free_size.setter
    def free_size(self, free_size):
        """Sets the free_size of this LogicalVolumes.

        剩余空间

        :param free_size: The free_size of this LogicalVolumes.
        :type free_size: int
        """
        self._free_size = free_size

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
        if not isinstance(other, LogicalVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
