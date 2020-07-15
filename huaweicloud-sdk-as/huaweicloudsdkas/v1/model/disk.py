# coding: utf-8

import pprint
import re

import six





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
        'size': 'int',
        'volume_type': 'str',
        'disk_type': 'str',
        'dedicate_storage_id': 'str',
        'data_disk_image_id': 'str',
        'snapshot_id': 'str'
    }

    attribute_map = {
        'size': 'size',
        'volume_type': 'volume_type',
        'disk_type': 'disk_type',
        'dedicate_storage_id': 'dedicate_storage_id',
        'data_disk_image_id': 'data_disk_image_id',
        'snapshot_id': 'snapshot_id'
    }

    def __init__(self, size=None, volume_type='SATA', disk_type='SYS', dedicate_storage_id=None, data_disk_image_id=None, snapshot_id=None):
        """Disk - a model defined in huaweicloud sdk"""
        
        

        self._size = None
        self._volume_type = None
        self._disk_type = None
        self._dedicate_storage_id = None
        self._data_disk_image_id = None
        self._snapshot_id = None
        self.discriminator = None

        self.size = size
        self.volume_type = volume_type
        self.disk_type = disk_type
        if dedicate_storage_id is not None:
            self.dedicate_storage_id = dedicate_storage_id
        if data_disk_image_id is not None:
            self.data_disk_image_id = data_disk_image_id
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id

    @property
    def size(self):
        """Gets the size of this Disk.

        磁盘大小，容量单位为GB。系统盘输入大小范围为40~32768，且不小于镜像中系统盘的最小(min_disk属性)值。数据盘输入大小范围为10~32768。

        :return: The size of this Disk.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Disk.

        磁盘大小，容量单位为GB。系统盘输入大小范围为40~32768，且不小于镜像中系统盘的最小(min_disk属性)值。数据盘输入大小范围为10~32768。

        :param size: The size of this Disk.
        :type: int
        """
        self._size = size

    @property
    def volume_type(self):
        """Gets the volume_type of this Disk.

        云服务器数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。磁盘类型枚举值：SATA：普通IO磁盘类型。SAS：高IO磁盘类型。SSD：超高IO磁盘类型。co-pl：高IO (性能优化Ⅰ型)磁盘类型。uh-l1：超高 IO (时延优化)磁盘类型。说明：对于HANA云服务器和HL1型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。

        :return: The volume_type of this Disk.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this Disk.

        云服务器数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。磁盘类型枚举值：SATA：普通IO磁盘类型。SAS：高IO磁盘类型。SSD：超高IO磁盘类型。co-pl：高IO (性能优化Ⅰ型)磁盘类型。uh-l1：超高 IO (时延优化)磁盘类型。说明：对于HANA云服务器和HL1型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。

        :param volume_type: The volume_type of this Disk.
        :type: str
        """
        self._volume_type = volume_type

    @property
    def disk_type(self):
        """Gets the disk_type of this Disk.

        系统盘还是数据盘，DATA表示为数据盘，SYS表示为系统盘。

        :return: The disk_type of this Disk.
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this Disk.

        系统盘还是数据盘，DATA表示为数据盘，SYS表示为系统盘。

        :param disk_type: The disk_type of this Disk.
        :type: str
        """
        self._disk_type = disk_type

    @property
    def dedicate_storage_id(self):
        """Gets the dedicate_storage_id of this Disk.

        云服务器的磁盘可指定创建在用户的专属存储中，需要指定专属存储ID。说明：同一个伸缩配置中的磁盘需统一指定或统一不指定专属存储，不支持混用；当指定专属存储时，所有专属存储需要属于同一个可用分区，且每个磁盘选择的专属存储支持的磁盘类型都需要和参数volume_type保持一致。

        :return: The dedicate_storage_id of this Disk.
        :rtype: str
        """
        return self._dedicate_storage_id

    @dedicate_storage_id.setter
    def dedicate_storage_id(self, dedicate_storage_id):
        """Sets the dedicate_storage_id of this Disk.

        云服务器的磁盘可指定创建在用户的专属存储中，需要指定专属存储ID。说明：同一个伸缩配置中的磁盘需统一指定或统一不指定专属存储，不支持混用；当指定专属存储时，所有专属存储需要属于同一个可用分区，且每个磁盘选择的专属存储支持的磁盘类型都需要和参数volume_type保持一致。

        :param dedicate_storage_id: The dedicate_storage_id of this Disk.
        :type: str
        """
        self._dedicate_storage_id = dedicate_storage_id

    @property
    def data_disk_image_id(self):
        """Gets the data_disk_image_id of this Disk.

        云服务器的数据盘可指定从数据盘镜像导出，需要指定数据盘镜像ID。

        :return: The data_disk_image_id of this Disk.
        :rtype: str
        """
        return self._data_disk_image_id

    @data_disk_image_id.setter
    def data_disk_image_id(self, data_disk_image_id):
        """Sets the data_disk_image_id of this Disk.

        云服务器的数据盘可指定从数据盘镜像导出，需要指定数据盘镜像ID。

        :param data_disk_image_id: The data_disk_image_id of this Disk.
        :type: str
        """
        self._data_disk_image_id = data_disk_image_id

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this Disk.

        当选择使用整机镜像时，云服务器的系统盘及数据盘将通过整机备份恢复，需要指定磁盘备份的快照ID。说明：磁盘备份的快照ID可通过镜像的整机备份ID在CSBS查询备份详情获得；一个伸缩配置中的每一个disk需要通过snapshot_id和整机备份中的磁盘备份一一对应。

        :return: The snapshot_id of this Disk.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this Disk.

        当选择使用整机镜像时，云服务器的系统盘及数据盘将通过整机备份恢复，需要指定磁盘备份的快照ID。说明：磁盘备份的快照ID可通过镜像的整机备份ID在CSBS查询备份详情获得；一个伸缩配置中的每一个disk需要通过snapshot_id和整机备份中的磁盘备份一一对应。

        :param snapshot_id: The snapshot_id of this Disk.
        :type: str
        """
        self._snapshot_id = snapshot_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Disk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
