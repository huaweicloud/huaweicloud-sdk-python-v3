# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskResult:

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
        'dedicated_storage_id': 'str',
        'data_disk_image_id': 'str',
        'snapshot_id': 'str',
        'metadata': 'MetaData',
        'iops': 'int',
        'throughput': 'int'
    }

    attribute_map = {
        'size': 'size',
        'volume_type': 'volume_type',
        'disk_type': 'disk_type',
        'dedicated_storage_id': 'dedicated_storage_id',
        'data_disk_image_id': 'data_disk_image_id',
        'snapshot_id': 'snapshot_id',
        'metadata': 'metadata',
        'iops': 'iops',
        'throughput': 'throughput'
    }

    def __init__(self, size=None, volume_type=None, disk_type=None, dedicated_storage_id=None, data_disk_image_id=None, snapshot_id=None, metadata=None, iops=None, throughput=None):
        """DiskResult

        The model defined in huaweicloud sdk

        :param size: 磁盘大小，容量单位为GB。
        :type size: int
        :param volume_type: 磁盘类型。
        :type volume_type: str
        :param disk_type: 系统盘还是数据盘，DATA表示为数据盘，SYS表示为系统盘。
        :type disk_type: str
        :param dedicated_storage_id: 磁盘所属的专属存储ID。
        :type dedicated_storage_id: str
        :param data_disk_image_id: 导入数据盘的数据盘镜像ID。
        :type data_disk_image_id: str
        :param snapshot_id: 磁盘备份的快照ID。
        :type snapshot_id: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkas.v1.MetaData`
        :param iops: 云硬盘iops
        :type iops: int
        :param throughput: 云硬盘吞吐量
        :type throughput: int
        """
        
        

        self._size = None
        self._volume_type = None
        self._disk_type = None
        self._dedicated_storage_id = None
        self._data_disk_image_id = None
        self._snapshot_id = None
        self._metadata = None
        self._iops = None
        self._throughput = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if volume_type is not None:
            self.volume_type = volume_type
        if disk_type is not None:
            self.disk_type = disk_type
        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id
        if data_disk_image_id is not None:
            self.data_disk_image_id = data_disk_image_id
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if metadata is not None:
            self.metadata = metadata
        if iops is not None:
            self.iops = iops
        if throughput is not None:
            self.throughput = throughput

    @property
    def size(self):
        """Gets the size of this DiskResult.

        磁盘大小，容量单位为GB。

        :return: The size of this DiskResult.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DiskResult.

        磁盘大小，容量单位为GB。

        :param size: The size of this DiskResult.
        :type size: int
        """
        self._size = size

    @property
    def volume_type(self):
        """Gets the volume_type of this DiskResult.

        磁盘类型。

        :return: The volume_type of this DiskResult.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this DiskResult.

        磁盘类型。

        :param volume_type: The volume_type of this DiskResult.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def disk_type(self):
        """Gets the disk_type of this DiskResult.

        系统盘还是数据盘，DATA表示为数据盘，SYS表示为系统盘。

        :return: The disk_type of this DiskResult.
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this DiskResult.

        系统盘还是数据盘，DATA表示为数据盘，SYS表示为系统盘。

        :param disk_type: The disk_type of this DiskResult.
        :type disk_type: str
        """
        self._disk_type = disk_type

    @property
    def dedicated_storage_id(self):
        """Gets the dedicated_storage_id of this DiskResult.

        磁盘所属的专属存储ID。

        :return: The dedicated_storage_id of this DiskResult.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        """Sets the dedicated_storage_id of this DiskResult.

        磁盘所属的专属存储ID。

        :param dedicated_storage_id: The dedicated_storage_id of this DiskResult.
        :type dedicated_storage_id: str
        """
        self._dedicated_storage_id = dedicated_storage_id

    @property
    def data_disk_image_id(self):
        """Gets the data_disk_image_id of this DiskResult.

        导入数据盘的数据盘镜像ID。

        :return: The data_disk_image_id of this DiskResult.
        :rtype: str
        """
        return self._data_disk_image_id

    @data_disk_image_id.setter
    def data_disk_image_id(self, data_disk_image_id):
        """Sets the data_disk_image_id of this DiskResult.

        导入数据盘的数据盘镜像ID。

        :param data_disk_image_id: The data_disk_image_id of this DiskResult.
        :type data_disk_image_id: str
        """
        self._data_disk_image_id = data_disk_image_id

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this DiskResult.

        磁盘备份的快照ID。

        :return: The snapshot_id of this DiskResult.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this DiskResult.

        磁盘备份的快照ID。

        :param snapshot_id: The snapshot_id of this DiskResult.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    @property
    def metadata(self):
        """Gets the metadata of this DiskResult.

        :return: The metadata of this DiskResult.
        :rtype: :class:`huaweicloudsdkas.v1.MetaData`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DiskResult.

        :param metadata: The metadata of this DiskResult.
        :type metadata: :class:`huaweicloudsdkas.v1.MetaData`
        """
        self._metadata = metadata

    @property
    def iops(self):
        """Gets the iops of this DiskResult.

        云硬盘iops

        :return: The iops of this DiskResult.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this DiskResult.

        云硬盘iops

        :param iops: The iops of this DiskResult.
        :type iops: int
        """
        self._iops = iops

    @property
    def throughput(self):
        """Gets the throughput of this DiskResult.

        云硬盘吞吐量

        :return: The throughput of this DiskResult.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this DiskResult.

        云硬盘吞吐量

        :param throughput: The throughput of this DiskResult.
        :type throughput: int
        """
        self._throughput = throughput

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
        if not isinstance(other, DiskResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
