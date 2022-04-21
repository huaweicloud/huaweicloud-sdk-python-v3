# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskInfo:

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
        'metadata': 'MetaData'
    }

    attribute_map = {
        'size': 'size',
        'volume_type': 'volume_type',
        'disk_type': 'disk_type',
        'dedicated_storage_id': 'dedicated_storage_id',
        'data_disk_image_id': 'data_disk_image_id',
        'snapshot_id': 'snapshot_id',
        'metadata': 'metadata'
    }

    def __init__(self, size=None, volume_type=None, disk_type=None, dedicated_storage_id=None, data_disk_image_id=None, snapshot_id=None, metadata=None):
        """DiskInfo

        The model defined in huaweicloud sdk

        :param size: 磁盘大小，容量单位为GB。系统盘输入大小范围为1~1024，且不小于镜像中系统盘的最小(min_disk属性)值。数据盘输入大小范围为10~32768。
        :type size: int
        :param volume_type: 云服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  SATA：普通IO磁盘类型。 SAS：高IO磁盘类型。 SSD：超高IO磁盘类型。 GPSSD：通用型SSD磁盘类型。 co-p1：高IO (性能优化Ⅰ型) uh-l1：超高IO (时延优化) 当指定的云硬盘类型在avaliability_zone内不存在时，则创建云硬盘失败。  说明： 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。  了解不同磁盘类型的详细信息，请参见[磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。
        :type volume_type: str
        :param disk_type: 系统盘还是数据盘，DATA表示为数据盘，SYS表示为系统盘。 说明： 系统盘不支持加密。
        :type disk_type: str
        :param dedicated_storage_id: 云服务器的磁盘可指定创建在用户的专属存储中，需要指定专属存储ID。说明：同一个伸缩配置中的磁盘需统一指定或统一不指定专属存储，不支持混用；当指定专属存储时，所有专属存储需要属于同一个可用分区，且每个磁盘选择的专属存储支持的磁盘类型都需要和参数volume_type保持一致。
        :type dedicated_storage_id: str
        :param data_disk_image_id: 云服务器的数据盘可指定从数据盘镜像导出，需要指定数据盘镜像ID。
        :type data_disk_image_id: str
        :param snapshot_id: 当选择使用整机镜像时，云服务器的系统盘及数据盘将通过整机备份恢复，需要指定磁盘备份的快照ID。说明：磁盘备份的快照ID可通过镜像的整机备份ID在CSBS查询备份详情获得；一个伸缩配置中的每一个disk需要通过snapshot_id和整机备份中的磁盘备份一一对应。
        :type snapshot_id: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkas.v1.MetaData`
        """
        
        

        self._size = None
        self._volume_type = None
        self._disk_type = None
        self._dedicated_storage_id = None
        self._data_disk_image_id = None
        self._snapshot_id = None
        self._metadata = None
        self.discriminator = None

        self.size = size
        self.volume_type = volume_type
        self.disk_type = disk_type
        if dedicated_storage_id is not None:
            self.dedicated_storage_id = dedicated_storage_id
        if data_disk_image_id is not None:
            self.data_disk_image_id = data_disk_image_id
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if metadata is not None:
            self.metadata = metadata

    @property
    def size(self):
        """Gets the size of this DiskInfo.

        磁盘大小，容量单位为GB。系统盘输入大小范围为1~1024，且不小于镜像中系统盘的最小(min_disk属性)值。数据盘输入大小范围为10~32768。

        :return: The size of this DiskInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DiskInfo.

        磁盘大小，容量单位为GB。系统盘输入大小范围为1~1024，且不小于镜像中系统盘的最小(min_disk属性)值。数据盘输入大小范围为10~32768。

        :param size: The size of this DiskInfo.
        :type size: int
        """
        self._size = size

    @property
    def volume_type(self):
        """Gets the volume_type of this DiskInfo.

        云服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  SATA：普通IO磁盘类型。 SAS：高IO磁盘类型。 SSD：超高IO磁盘类型。 GPSSD：通用型SSD磁盘类型。 co-p1：高IO (性能优化Ⅰ型) uh-l1：超高IO (时延优化) 当指定的云硬盘类型在avaliability_zone内不存在时，则创建云硬盘失败。  说明： 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。  了解不同磁盘类型的详细信息，请参见[磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。

        :return: The volume_type of this DiskInfo.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this DiskInfo.

        云服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  SATA：普通IO磁盘类型。 SAS：高IO磁盘类型。 SSD：超高IO磁盘类型。 GPSSD：通用型SSD磁盘类型。 co-p1：高IO (性能优化Ⅰ型) uh-l1：超高IO (时延优化) 当指定的云硬盘类型在avaliability_zone内不存在时，则创建云硬盘失败。  说明： 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。  了解不同磁盘类型的详细信息，请参见[磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。

        :param volume_type: The volume_type of this DiskInfo.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def disk_type(self):
        """Gets the disk_type of this DiskInfo.

        系统盘还是数据盘，DATA表示为数据盘，SYS表示为系统盘。 说明： 系统盘不支持加密。

        :return: The disk_type of this DiskInfo.
        :rtype: str
        """
        return self._disk_type

    @disk_type.setter
    def disk_type(self, disk_type):
        """Sets the disk_type of this DiskInfo.

        系统盘还是数据盘，DATA表示为数据盘，SYS表示为系统盘。 说明： 系统盘不支持加密。

        :param disk_type: The disk_type of this DiskInfo.
        :type disk_type: str
        """
        self._disk_type = disk_type

    @property
    def dedicated_storage_id(self):
        """Gets the dedicated_storage_id of this DiskInfo.

        云服务器的磁盘可指定创建在用户的专属存储中，需要指定专属存储ID。说明：同一个伸缩配置中的磁盘需统一指定或统一不指定专属存储，不支持混用；当指定专属存储时，所有专属存储需要属于同一个可用分区，且每个磁盘选择的专属存储支持的磁盘类型都需要和参数volume_type保持一致。

        :return: The dedicated_storage_id of this DiskInfo.
        :rtype: str
        """
        return self._dedicated_storage_id

    @dedicated_storage_id.setter
    def dedicated_storage_id(self, dedicated_storage_id):
        """Sets the dedicated_storage_id of this DiskInfo.

        云服务器的磁盘可指定创建在用户的专属存储中，需要指定专属存储ID。说明：同一个伸缩配置中的磁盘需统一指定或统一不指定专属存储，不支持混用；当指定专属存储时，所有专属存储需要属于同一个可用分区，且每个磁盘选择的专属存储支持的磁盘类型都需要和参数volume_type保持一致。

        :param dedicated_storage_id: The dedicated_storage_id of this DiskInfo.
        :type dedicated_storage_id: str
        """
        self._dedicated_storage_id = dedicated_storage_id

    @property
    def data_disk_image_id(self):
        """Gets the data_disk_image_id of this DiskInfo.

        云服务器的数据盘可指定从数据盘镜像导出，需要指定数据盘镜像ID。

        :return: The data_disk_image_id of this DiskInfo.
        :rtype: str
        """
        return self._data_disk_image_id

    @data_disk_image_id.setter
    def data_disk_image_id(self, data_disk_image_id):
        """Sets the data_disk_image_id of this DiskInfo.

        云服务器的数据盘可指定从数据盘镜像导出，需要指定数据盘镜像ID。

        :param data_disk_image_id: The data_disk_image_id of this DiskInfo.
        :type data_disk_image_id: str
        """
        self._data_disk_image_id = data_disk_image_id

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this DiskInfo.

        当选择使用整机镜像时，云服务器的系统盘及数据盘将通过整机备份恢复，需要指定磁盘备份的快照ID。说明：磁盘备份的快照ID可通过镜像的整机备份ID在CSBS查询备份详情获得；一个伸缩配置中的每一个disk需要通过snapshot_id和整机备份中的磁盘备份一一对应。

        :return: The snapshot_id of this DiskInfo.
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this DiskInfo.

        当选择使用整机镜像时，云服务器的系统盘及数据盘将通过整机备份恢复，需要指定磁盘备份的快照ID。说明：磁盘备份的快照ID可通过镜像的整机备份ID在CSBS查询备份详情获得；一个伸缩配置中的每一个disk需要通过snapshot_id和整机备份中的磁盘备份一一对应。

        :param snapshot_id: The snapshot_id of this DiskInfo.
        :type snapshot_id: str
        """
        self._snapshot_id = snapshot_id

    @property
    def metadata(self):
        """Gets the metadata of this DiskInfo.


        :return: The metadata of this DiskInfo.
        :rtype: :class:`huaweicloudsdkas.v1.MetaData`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DiskInfo.


        :param metadata: The metadata of this DiskInfo.
        :type metadata: :class:`huaweicloudsdkas.v1.MetaData`
        """
        self._metadata = metadata

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
        if not isinstance(other, DiskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
