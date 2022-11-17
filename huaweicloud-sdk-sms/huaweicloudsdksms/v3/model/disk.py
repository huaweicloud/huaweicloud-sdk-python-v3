# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Disk:

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
        'partition_style': 'str',
        'device_use': 'str',
        'size': 'int',
        'used_size': 'int',
        'physical_volumes': 'list[PhysicalVolumes]',
        'disk_id': 'str',
        'os_disk': 'bool',
        'relation_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'partition_style': 'partition_style',
        'device_use': 'device_use',
        'size': 'size',
        'used_size': 'used_size',
        'physical_volumes': 'physical_volumes',
        'disk_id': 'disk_id',
        'os_disk': 'os_disk',
        'relation_name': 'relation_name'
    }

    def __init__(self, name=None, partition_style=None, device_use=None, size=None, used_size=None, physical_volumes=None, disk_id=None, os_disk=None, relation_name=None):
        """Disk

        The model defined in huaweicloud sdk

        :param name: 磁盘名称
        :type name: str
        :param partition_style: 磁盘的分区类型，添加源端时源端磁盘必选 MBR：mbr格式 GPT：gpt格式
        :type partition_style: str
        :param device_use: 磁盘类型 BOOT：BOOT设备 OS：系统设备
        :type device_use: str
        :param size: 磁盘总大小，以字节为单位
        :type size: int
        :param used_size: 磁盘已使用大小，以字节为单位
        :type used_size: int
        :param physical_volumes: 磁盘上的物理分区信息
        :type physical_volumes: list[:class:`huaweicloudsdksms.v3.PhysicalVolumes`]
        :param disk_id: 创建任务时，如果选择已有虚拟机，此参数必选
        :type disk_id: str
        :param os_disk: 是否为系统盘
        :type os_disk: bool
        :param relation_name: Linux系统 目的端ECS中与源端关联的磁盘名称
        :type relation_name: str
        """
        
        

        self._name = None
        self._partition_style = None
        self._device_use = None
        self._size = None
        self._used_size = None
        self._physical_volumes = None
        self._disk_id = None
        self._os_disk = None
        self._relation_name = None
        self.discriminator = None

        self.name = name
        if partition_style is not None:
            self.partition_style = partition_style
        self.device_use = device_use
        self.size = size
        self.used_size = used_size
        self.physical_volumes = physical_volumes
        if disk_id is not None:
            self.disk_id = disk_id
        if os_disk is not None:
            self.os_disk = os_disk
        if relation_name is not None:
            self.relation_name = relation_name

    @property
    def name(self):
        """Gets the name of this Disk.

        磁盘名称

        :return: The name of this Disk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Disk.

        磁盘名称

        :param name: The name of this Disk.
        :type name: str
        """
        self._name = name

    @property
    def partition_style(self):
        """Gets the partition_style of this Disk.

        磁盘的分区类型，添加源端时源端磁盘必选 MBR：mbr格式 GPT：gpt格式

        :return: The partition_style of this Disk.
        :rtype: str
        """
        return self._partition_style

    @partition_style.setter
    def partition_style(self, partition_style):
        """Sets the partition_style of this Disk.

        磁盘的分区类型，添加源端时源端磁盘必选 MBR：mbr格式 GPT：gpt格式

        :param partition_style: The partition_style of this Disk.
        :type partition_style: str
        """
        self._partition_style = partition_style

    @property
    def device_use(self):
        """Gets the device_use of this Disk.

        磁盘类型 BOOT：BOOT设备 OS：系统设备

        :return: The device_use of this Disk.
        :rtype: str
        """
        return self._device_use

    @device_use.setter
    def device_use(self, device_use):
        """Sets the device_use of this Disk.

        磁盘类型 BOOT：BOOT设备 OS：系统设备

        :param device_use: The device_use of this Disk.
        :type device_use: str
        """
        self._device_use = device_use

    @property
    def size(self):
        """Gets the size of this Disk.

        磁盘总大小，以字节为单位

        :return: The size of this Disk.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Disk.

        磁盘总大小，以字节为单位

        :param size: The size of this Disk.
        :type size: int
        """
        self._size = size

    @property
    def used_size(self):
        """Gets the used_size of this Disk.

        磁盘已使用大小，以字节为单位

        :return: The used_size of this Disk.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        """Sets the used_size of this Disk.

        磁盘已使用大小，以字节为单位

        :param used_size: The used_size of this Disk.
        :type used_size: int
        """
        self._used_size = used_size

    @property
    def physical_volumes(self):
        """Gets the physical_volumes of this Disk.

        磁盘上的物理分区信息

        :return: The physical_volumes of this Disk.
        :rtype: list[:class:`huaweicloudsdksms.v3.PhysicalVolumes`]
        """
        return self._physical_volumes

    @physical_volumes.setter
    def physical_volumes(self, physical_volumes):
        """Sets the physical_volumes of this Disk.

        磁盘上的物理分区信息

        :param physical_volumes: The physical_volumes of this Disk.
        :type physical_volumes: list[:class:`huaweicloudsdksms.v3.PhysicalVolumes`]
        """
        self._physical_volumes = physical_volumes

    @property
    def disk_id(self):
        """Gets the disk_id of this Disk.

        创建任务时，如果选择已有虚拟机，此参数必选

        :return: The disk_id of this Disk.
        :rtype: str
        """
        return self._disk_id

    @disk_id.setter
    def disk_id(self, disk_id):
        """Sets the disk_id of this Disk.

        创建任务时，如果选择已有虚拟机，此参数必选

        :param disk_id: The disk_id of this Disk.
        :type disk_id: str
        """
        self._disk_id = disk_id

    @property
    def os_disk(self):
        """Gets the os_disk of this Disk.

        是否为系统盘

        :return: The os_disk of this Disk.
        :rtype: bool
        """
        return self._os_disk

    @os_disk.setter
    def os_disk(self, os_disk):
        """Sets the os_disk of this Disk.

        是否为系统盘

        :param os_disk: The os_disk of this Disk.
        :type os_disk: bool
        """
        self._os_disk = os_disk

    @property
    def relation_name(self):
        """Gets the relation_name of this Disk.

        Linux系统 目的端ECS中与源端关联的磁盘名称

        :return: The relation_name of this Disk.
        :rtype: str
        """
        return self._relation_name

    @relation_name.setter
    def relation_name(self, relation_name):
        """Sets the relation_name of this Disk.

        Linux系统 目的端ECS中与源端关联的磁盘名称

        :param relation_name: The relation_name of this Disk.
        :type relation_name: str
        """
        self._relation_name = relation_name

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
        if not isinstance(other, Disk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
