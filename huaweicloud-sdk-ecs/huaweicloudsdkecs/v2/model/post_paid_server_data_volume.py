# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServerDataVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volumetype': 'str',
        'size': 'int',
        'iops': 'int',
        'throughput': 'int',
        'shareable': 'bool',
        'multiattach': 'bool',
        'hwpassthrough': 'bool',
        'extendparam': 'PostPaidServerDataVolumeExtendParam',
        'cluster_type': 'str',
        'cluster_id': 'str',
        'metadata': 'PostPaidServerDataVolumeMetadata',
        'data_image_id': 'str',
        'delete_on_termination': 'bool'
    }

    attribute_map = {
        'volumetype': 'volumetype',
        'size': 'size',
        'iops': 'iops',
        'throughput': 'throughput',
        'shareable': 'shareable',
        'multiattach': 'multiattach',
        'hwpassthrough': 'hw:passthrough',
        'extendparam': 'extendparam',
        'cluster_type': 'cluster_type',
        'cluster_id': 'cluster_id',
        'metadata': 'metadata',
        'data_image_id': 'data_image_id',
        'delete_on_termination': 'delete_on_termination'
    }

    def __init__(self, volumetype=None, size=None, iops=None, throughput=None, shareable=None, multiattach=None, hwpassthrough=None, extendparam=None, cluster_type=None, cluster_id=None, metadata=None, data_image_id=None, delete_on_termination=None):
        """PostPaidServerDataVolume

        The model defined in huaweicloud sdk

        :param volumetype: 云服务器数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。   - SATA：普通IO磁盘类型。  - SAS：高IO磁盘类型。  - SSD：超高IO磁盘类型。  - GPSSD：为通用型SSD磁盘类型。  - co-p1：高IO (性能优化Ⅰ型)。  - uh-l1：超高IO (时延优化)。  - ESSD：为极速IO磁盘类型。  - GPSSD2：通用型SSD V2磁盘类型。  - ESSD2：极速型SSD V2磁盘类型。   &gt; 说明： &gt;  &gt; 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。  了解不同磁盘类型的详细信息，请参见 [磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。  获取region可用的卷类型，请参见[查询云硬盘类型列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;EVS&amp;api&#x3D;CinderListVolumeTypes)
        :type volumetype: str
        :param size: 数据盘大小，容量单位为GB，输入大小范围为[10,32768]。
        :type size: int
        :param iops: 给云硬盘配置iops，购买GPSSD2、ESSD2类型的云硬盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2、ESSD2类型的iops大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。
        :type iops: int
        :param throughput: 给云硬盘配置吞吐量，单位是MiB/s，购买GPSSD2类型云盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2类型的吞吐量大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。
        :type throughput: int
        :param shareable: 是否为共享磁盘。true为共享盘，false为普通云硬盘。  &gt; 说明： &gt;  &gt; 该字段已废弃，请使用multiattach。
        :type shareable: bool
        :param multiattach: 创建共享磁盘的信息。  - true：创建的磁盘为共享盘。 - false：创建的磁盘为普通云硬盘。  &gt; 说明： &gt;  &gt; shareable当前为废弃字段，如果确实需要同时使用shareable字段和multiattach字段，此时，请确保两个字段的参数值相同。当不指定该字段时，系统默认创建普通云硬盘。
        :type multiattach: bool
        :param hwpassthrough: 数据卷是否使用SCSI锁。  - true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。 - false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。 - 该字段不存在时，云硬盘默认为VBD类型。  &gt; 说明： &gt;  &gt; 此参数为boolean类型，若传入非boolean类型字符，程序将按照【false】方式处理。
        :type hwpassthrough: bool
        :param extendparam: 
        :type extendparam: :class:`huaweicloudsdkecs.v2.PostPaidServerDataVolumeExtendParam`
        :param cluster_type: 云服务器数据盘对应的磁盘存储类型。 磁盘存储类型枚举值： DSS：专属存储类型
        :type cluster_type: str
        :param cluster_id: 云服务器数据盘对应的存储池的ID。
        :type cluster_id: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkecs.v2.PostPaidServerDataVolumeMetadata`
        :param data_image_id: 数据镜像的ID，UUID格式。  如果使用数据盘镜像创建数据盘，则data_image_id为必选参数，且不支持使用metadata。
        :type data_image_id: str
        :param delete_on_termination: 数据盘随实例释放策略。  true：数据盘随实例释放。 false：数据盘不随实例释放。 默认值：false。
        :type delete_on_termination: bool
        """
        
        

        self._volumetype = None
        self._size = None
        self._iops = None
        self._throughput = None
        self._shareable = None
        self._multiattach = None
        self._hwpassthrough = None
        self._extendparam = None
        self._cluster_type = None
        self._cluster_id = None
        self._metadata = None
        self._data_image_id = None
        self._delete_on_termination = None
        self.discriminator = None

        self.volumetype = volumetype
        self.size = size
        if iops is not None:
            self.iops = iops
        if throughput is not None:
            self.throughput = throughput
        if shareable is not None:
            self.shareable = shareable
        if multiattach is not None:
            self.multiattach = multiattach
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough
        if extendparam is not None:
            self.extendparam = extendparam
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if metadata is not None:
            self.metadata = metadata
        if data_image_id is not None:
            self.data_image_id = data_image_id
        if delete_on_termination is not None:
            self.delete_on_termination = delete_on_termination

    @property
    def volumetype(self):
        """Gets the volumetype of this PostPaidServerDataVolume.

        云服务器数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。   - SATA：普通IO磁盘类型。  - SAS：高IO磁盘类型。  - SSD：超高IO磁盘类型。  - GPSSD：为通用型SSD磁盘类型。  - co-p1：高IO (性能优化Ⅰ型)。  - uh-l1：超高IO (时延优化)。  - ESSD：为极速IO磁盘类型。  - GPSSD2：通用型SSD V2磁盘类型。  - ESSD2：极速型SSD V2磁盘类型。   > 说明： >  > 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。  了解不同磁盘类型的详细信息，请参见 [磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。  获取region可用的卷类型，请参见[查询云硬盘类型列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=EVS&api=CinderListVolumeTypes)

        :return: The volumetype of this PostPaidServerDataVolume.
        :rtype: str
        """
        return self._volumetype

    @volumetype.setter
    def volumetype(self, volumetype):
        """Sets the volumetype of this PostPaidServerDataVolume.

        云服务器数据盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。   - SATA：普通IO磁盘类型。  - SAS：高IO磁盘类型。  - SSD：超高IO磁盘类型。  - GPSSD：为通用型SSD磁盘类型。  - co-p1：高IO (性能优化Ⅰ型)。  - uh-l1：超高IO (时延优化)。  - ESSD：为极速IO磁盘类型。  - GPSSD2：通用型SSD V2磁盘类型。  - ESSD2：极速型SSD V2磁盘类型。   > 说明： >  > 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。  了解不同磁盘类型的详细信息，请参见 [磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。  获取region可用的卷类型，请参见[查询云硬盘类型列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=EVS&api=CinderListVolumeTypes)

        :param volumetype: The volumetype of this PostPaidServerDataVolume.
        :type volumetype: str
        """
        self._volumetype = volumetype

    @property
    def size(self):
        """Gets the size of this PostPaidServerDataVolume.

        数据盘大小，容量单位为GB，输入大小范围为[10,32768]。

        :return: The size of this PostPaidServerDataVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PostPaidServerDataVolume.

        数据盘大小，容量单位为GB，输入大小范围为[10,32768]。

        :param size: The size of this PostPaidServerDataVolume.
        :type size: int
        """
        self._size = size

    @property
    def iops(self):
        """Gets the iops of this PostPaidServerDataVolume.

        给云硬盘配置iops，购买GPSSD2、ESSD2类型的云硬盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2、ESSD2类型的iops大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。

        :return: The iops of this PostPaidServerDataVolume.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this PostPaidServerDataVolume.

        给云硬盘配置iops，购买GPSSD2、ESSD2类型的云硬盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2、ESSD2类型的iops大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。

        :param iops: The iops of this PostPaidServerDataVolume.
        :type iops: int
        """
        self._iops = iops

    @property
    def throughput(self):
        """Gets the throughput of this PostPaidServerDataVolume.

        给云硬盘配置吞吐量，单位是MiB/s，购买GPSSD2类型云盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2类型的吞吐量大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。

        :return: The throughput of this PostPaidServerDataVolume.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """Sets the throughput of this PostPaidServerDataVolume.

        给云硬盘配置吞吐量，单位是MiB/s，购买GPSSD2类型云盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2类型的吞吐量大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。

        :param throughput: The throughput of this PostPaidServerDataVolume.
        :type throughput: int
        """
        self._throughput = throughput

    @property
    def shareable(self):
        """Gets the shareable of this PostPaidServerDataVolume.

        是否为共享磁盘。true为共享盘，false为普通云硬盘。  > 说明： >  > 该字段已废弃，请使用multiattach。

        :return: The shareable of this PostPaidServerDataVolume.
        :rtype: bool
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        """Sets the shareable of this PostPaidServerDataVolume.

        是否为共享磁盘。true为共享盘，false为普通云硬盘。  > 说明： >  > 该字段已废弃，请使用multiattach。

        :param shareable: The shareable of this PostPaidServerDataVolume.
        :type shareable: bool
        """
        self._shareable = shareable

    @property
    def multiattach(self):
        """Gets the multiattach of this PostPaidServerDataVolume.

        创建共享磁盘的信息。  - true：创建的磁盘为共享盘。 - false：创建的磁盘为普通云硬盘。  > 说明： >  > shareable当前为废弃字段，如果确实需要同时使用shareable字段和multiattach字段，此时，请确保两个字段的参数值相同。当不指定该字段时，系统默认创建普通云硬盘。

        :return: The multiattach of this PostPaidServerDataVolume.
        :rtype: bool
        """
        return self._multiattach

    @multiattach.setter
    def multiattach(self, multiattach):
        """Sets the multiattach of this PostPaidServerDataVolume.

        创建共享磁盘的信息。  - true：创建的磁盘为共享盘。 - false：创建的磁盘为普通云硬盘。  > 说明： >  > shareable当前为废弃字段，如果确实需要同时使用shareable字段和multiattach字段，此时，请确保两个字段的参数值相同。当不指定该字段时，系统默认创建普通云硬盘。

        :param multiattach: The multiattach of this PostPaidServerDataVolume.
        :type multiattach: bool
        """
        self._multiattach = multiattach

    @property
    def hwpassthrough(self):
        """Gets the hwpassthrough of this PostPaidServerDataVolume.

        数据卷是否使用SCSI锁。  - true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。 - false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。 - 该字段不存在时，云硬盘默认为VBD类型。  > 说明： >  > 此参数为boolean类型，若传入非boolean类型字符，程序将按照【false】方式处理。

        :return: The hwpassthrough of this PostPaidServerDataVolume.
        :rtype: bool
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        """Sets the hwpassthrough of this PostPaidServerDataVolume.

        数据卷是否使用SCSI锁。  - true表示云硬盘的设备类型为SCSI类型，即允许ECS操作系统直接访问底层存储介质。支持SCSI锁命令。 - false表示云硬盘的设备类型为VBD (虚拟块存储设备 , Virtual Block Device)类型，即为默认类型，VBD只能支持简单的SCSI读写命令。 - 该字段不存在时，云硬盘默认为VBD类型。  > 说明： >  > 此参数为boolean类型，若传入非boolean类型字符，程序将按照【false】方式处理。

        :param hwpassthrough: The hwpassthrough of this PostPaidServerDataVolume.
        :type hwpassthrough: bool
        """
        self._hwpassthrough = hwpassthrough

    @property
    def extendparam(self):
        """Gets the extendparam of this PostPaidServerDataVolume.

        :return: The extendparam of this PostPaidServerDataVolume.
        :rtype: :class:`huaweicloudsdkecs.v2.PostPaidServerDataVolumeExtendParam`
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this PostPaidServerDataVolume.

        :param extendparam: The extendparam of this PostPaidServerDataVolume.
        :type extendparam: :class:`huaweicloudsdkecs.v2.PostPaidServerDataVolumeExtendParam`
        """
        self._extendparam = extendparam

    @property
    def cluster_type(self):
        """Gets the cluster_type of this PostPaidServerDataVolume.

        云服务器数据盘对应的磁盘存储类型。 磁盘存储类型枚举值： DSS：专属存储类型

        :return: The cluster_type of this PostPaidServerDataVolume.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this PostPaidServerDataVolume.

        云服务器数据盘对应的磁盘存储类型。 磁盘存储类型枚举值： DSS：专属存储类型

        :param cluster_type: The cluster_type of this PostPaidServerDataVolume.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this PostPaidServerDataVolume.

        云服务器数据盘对应的存储池的ID。

        :return: The cluster_id of this PostPaidServerDataVolume.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this PostPaidServerDataVolume.

        云服务器数据盘对应的存储池的ID。

        :param cluster_id: The cluster_id of this PostPaidServerDataVolume.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def metadata(self):
        """Gets the metadata of this PostPaidServerDataVolume.

        :return: The metadata of this PostPaidServerDataVolume.
        :rtype: :class:`huaweicloudsdkecs.v2.PostPaidServerDataVolumeMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PostPaidServerDataVolume.

        :param metadata: The metadata of this PostPaidServerDataVolume.
        :type metadata: :class:`huaweicloudsdkecs.v2.PostPaidServerDataVolumeMetadata`
        """
        self._metadata = metadata

    @property
    def data_image_id(self):
        """Gets the data_image_id of this PostPaidServerDataVolume.

        数据镜像的ID，UUID格式。  如果使用数据盘镜像创建数据盘，则data_image_id为必选参数，且不支持使用metadata。

        :return: The data_image_id of this PostPaidServerDataVolume.
        :rtype: str
        """
        return self._data_image_id

    @data_image_id.setter
    def data_image_id(self, data_image_id):
        """Sets the data_image_id of this PostPaidServerDataVolume.

        数据镜像的ID，UUID格式。  如果使用数据盘镜像创建数据盘，则data_image_id为必选参数，且不支持使用metadata。

        :param data_image_id: The data_image_id of this PostPaidServerDataVolume.
        :type data_image_id: str
        """
        self._data_image_id = data_image_id

    @property
    def delete_on_termination(self):
        """Gets the delete_on_termination of this PostPaidServerDataVolume.

        数据盘随实例释放策略。  true：数据盘随实例释放。 false：数据盘不随实例释放。 默认值：false。

        :return: The delete_on_termination of this PostPaidServerDataVolume.
        :rtype: bool
        """
        return self._delete_on_termination

    @delete_on_termination.setter
    def delete_on_termination(self, delete_on_termination):
        """Sets the delete_on_termination of this PostPaidServerDataVolume.

        数据盘随实例释放策略。  true：数据盘随实例释放。 false：数据盘不随实例释放。 默认值：false。

        :param delete_on_termination: The delete_on_termination of this PostPaidServerDataVolume.
        :type delete_on_termination: bool
        """
        self._delete_on_termination = delete_on_termination

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
        if not isinstance(other, PostPaidServerDataVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
