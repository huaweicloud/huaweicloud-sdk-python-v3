# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TargetPhysicalVolumes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'device_use': 'str',
        'file_system': 'str',
        'index': 'int',
        'mount_point': 'str',
        'name': 'str',
        'size': 'int',
        'used_size': 'int',
        'uuid': 'str',
        'relation_name': 'str',
        'free_size': 'int'
    }

    attribute_map = {
        'id': 'id',
        'device_use': 'device_use',
        'file_system': 'file_system',
        'index': 'index',
        'mount_point': 'mount_point',
        'name': 'name',
        'size': 'size',
        'used_size': 'used_size',
        'uuid': 'uuid',
        'relation_name': 'relation_name',
        'free_size': 'free_size'
    }

    def __init__(self, id=None, device_use=None, file_system=None, index=None, mount_point=None, name=None, size=None, used_size=None, uuid=None, relation_name=None, free_size=None):
        r"""TargetPhysicalVolumes

        The model defined in huaweicloud sdk

        :param id: 逻辑卷ID
        :type id: int
        :param device_use: 分区类型 NORMAL:平常 OS：系统设备 BOOT：BOOT设备
        :type device_use: str
        :param file_system: 文件系统
        :type file_system: str
        :param index: 编号
        :type index: int
        :param mount_point: 挂载点
        :type mount_point: str
        :param name: 名称
        :type name: str
        :param size: 大小
        :type size: int
        :param used_size: 使用大小
        :type used_size: int
        :param uuid: uuid
        :type uuid: str
        :param relation_name: Linux系统 目的端ECS中与源端关联的磁盘名称
        :type relation_name: str
        :param free_size: 分区空闲大小
        :type free_size: int
        """
        
        

        self._id = None
        self._device_use = None
        self._file_system = None
        self._index = None
        self._mount_point = None
        self._name = None
        self._size = None
        self._used_size = None
        self._uuid = None
        self._relation_name = None
        self._free_size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if device_use is not None:
            self.device_use = device_use
        if file_system is not None:
            self.file_system = file_system
        if index is not None:
            self.index = index
        if mount_point is not None:
            self.mount_point = mount_point
        if name is not None:
            self.name = name
        if size is not None:
            self.size = size
        if used_size is not None:
            self.used_size = used_size
        if uuid is not None:
            self.uuid = uuid
        if relation_name is not None:
            self.relation_name = relation_name
        if free_size is not None:
            self.free_size = free_size

    @property
    def id(self):
        r"""Gets the id of this TargetPhysicalVolumes.

        逻辑卷ID

        :return: The id of this TargetPhysicalVolumes.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TargetPhysicalVolumes.

        逻辑卷ID

        :param id: The id of this TargetPhysicalVolumes.
        :type id: int
        """
        self._id = id

    @property
    def device_use(self):
        r"""Gets the device_use of this TargetPhysicalVolumes.

        分区类型 NORMAL:平常 OS：系统设备 BOOT：BOOT设备

        :return: The device_use of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._device_use

    @device_use.setter
    def device_use(self, device_use):
        r"""Sets the device_use of this TargetPhysicalVolumes.

        分区类型 NORMAL:平常 OS：系统设备 BOOT：BOOT设备

        :param device_use: The device_use of this TargetPhysicalVolumes.
        :type device_use: str
        """
        self._device_use = device_use

    @property
    def file_system(self):
        r"""Gets the file_system of this TargetPhysicalVolumes.

        文件系统

        :return: The file_system of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._file_system

    @file_system.setter
    def file_system(self, file_system):
        r"""Sets the file_system of this TargetPhysicalVolumes.

        文件系统

        :param file_system: The file_system of this TargetPhysicalVolumes.
        :type file_system: str
        """
        self._file_system = file_system

    @property
    def index(self):
        r"""Gets the index of this TargetPhysicalVolumes.

        编号

        :return: The index of this TargetPhysicalVolumes.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this TargetPhysicalVolumes.

        编号

        :param index: The index of this TargetPhysicalVolumes.
        :type index: int
        """
        self._index = index

    @property
    def mount_point(self):
        r"""Gets the mount_point of this TargetPhysicalVolumes.

        挂载点

        :return: The mount_point of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        r"""Sets the mount_point of this TargetPhysicalVolumes.

        挂载点

        :param mount_point: The mount_point of this TargetPhysicalVolumes.
        :type mount_point: str
        """
        self._mount_point = mount_point

    @property
    def name(self):
        r"""Gets the name of this TargetPhysicalVolumes.

        名称

        :return: The name of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TargetPhysicalVolumes.

        名称

        :param name: The name of this TargetPhysicalVolumes.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        r"""Gets the size of this TargetPhysicalVolumes.

        大小

        :return: The size of this TargetPhysicalVolumes.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this TargetPhysicalVolumes.

        大小

        :param size: The size of this TargetPhysicalVolumes.
        :type size: int
        """
        self._size = size

    @property
    def used_size(self):
        r"""Gets the used_size of this TargetPhysicalVolumes.

        使用大小

        :return: The used_size of this TargetPhysicalVolumes.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        r"""Sets the used_size of this TargetPhysicalVolumes.

        使用大小

        :param used_size: The used_size of this TargetPhysicalVolumes.
        :type used_size: int
        """
        self._used_size = used_size

    @property
    def uuid(self):
        r"""Gets the uuid of this TargetPhysicalVolumes.

        uuid

        :return: The uuid of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this TargetPhysicalVolumes.

        uuid

        :param uuid: The uuid of this TargetPhysicalVolumes.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def relation_name(self):
        r"""Gets the relation_name of this TargetPhysicalVolumes.

        Linux系统 目的端ECS中与源端关联的磁盘名称

        :return: The relation_name of this TargetPhysicalVolumes.
        :rtype: str
        """
        return self._relation_name

    @relation_name.setter
    def relation_name(self, relation_name):
        r"""Sets the relation_name of this TargetPhysicalVolumes.

        Linux系统 目的端ECS中与源端关联的磁盘名称

        :param relation_name: The relation_name of this TargetPhysicalVolumes.
        :type relation_name: str
        """
        self._relation_name = relation_name

    @property
    def free_size(self):
        r"""Gets the free_size of this TargetPhysicalVolumes.

        分区空闲大小

        :return: The free_size of this TargetPhysicalVolumes.
        :rtype: int
        """
        return self._free_size

    @free_size.setter
    def free_size(self, free_size):
        r"""Sets the free_size of this TargetPhysicalVolumes.

        分区空闲大小

        :param free_size: The free_size of this TargetPhysicalVolumes.
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
        if not isinstance(other, TargetPhysicalVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
