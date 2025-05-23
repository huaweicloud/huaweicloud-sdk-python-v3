# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostPaidServerRootVolume:

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
        'hwpassthrough': 'bool',
        'cluster_type': 'str',
        'cluster_id': 'str',
        'extendparam': 'PostPaidServerRootVolumeExtendParam',
        'metadata': 'PostPaidServerRootVolumeMetadata'
    }

    attribute_map = {
        'volumetype': 'volumetype',
        'size': 'size',
        'iops': 'iops',
        'throughput': 'throughput',
        'hwpassthrough': 'hw:passthrough',
        'cluster_type': 'cluster_type',
        'cluster_id': 'cluster_id',
        'extendparam': 'extendparam',
        'metadata': 'metadata'
    }

    def __init__(self, volumetype=None, size=None, iops=None, throughput=None, hwpassthrough=None, cluster_type=None, cluster_id=None, extendparam=None, metadata=None):
        r"""PostPaidServerRootVolume

        The model defined in huaweicloud sdk

        :param volumetype: 云服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。   - SATA：普通IO磁盘类型。  - SAS：高IO磁盘类型。  - SSD：超高IO磁盘类型。  - GPSSD：为通用型SSD磁盘类型。  - co-p1：高IO (性能优化Ⅰ型)。  - uh-l1：超高IO (时延优化)。  - ESSD：为极速IO磁盘类型。  - GPSSD2：通用型SSD V2磁盘类型。  - ESSD2：极速型SSD V2磁盘类型。   &gt; 说明： &gt;  &gt; 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。  了解不同磁盘类型的详细信息，请参见 [磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。  获取region可用的卷类型，请参见[查询云硬盘类型列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;EVS&amp;api&#x3D;CinderListVolumeTypes)
        :type volumetype: str
        :param size: 系统盘大小，容量单位为GB， 输入大小范围为[1,1024]。  约束：  - 系统盘大小取值应不小于镜像支持的系统盘的最小值(镜像的min_disk属性)。 - 若该参数没有指定或者指定为0时，系统盘大小默认取值为镜像中系统盘的最小值(镜像的min_disk属性)。  &gt; 说明： &gt; &gt; 镜像系统盘的最小值(镜像的min_disk属性)可在控制台中点击镜像详情查看。或通过调用“查询镜像详情（OpenStack原生）”API获取，详细操作请参考[《镜像服务API参考》](https://support.huaweicloud.com/api-ims/ims_03_0702.html)中“查询镜像详情（OpenStack原生）”章节。
        :type size: int
        :param iops: 给云硬盘配置iops，购买GPSSD2、ESSD2类型的云硬盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2、ESSD2类型的iops大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。
        :type iops: int
        :param throughput: 给云硬盘配置吞吐量，单位是MiB/s，购买GPSSD2类型云盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2类型的吞吐量大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。
        :type throughput: int
        :param hwpassthrough: 使用SDI规格创建虚拟机时请关注该参数，如果该参数值为true，说明创建的为scsi类型的卷  &gt; 说明： &gt;  &gt; 此参数为boolean类型，若传入非boolean类型字符，程序将按照false方式处理。
        :type hwpassthrough: bool
        :param cluster_type: 云服务器系统盘对应的磁盘存储类型。 磁盘存储类型枚举值： DSS：专属存储类型
        :type cluster_type: str
        :param cluster_id: 云服务器数据盘对应的存储池的ID。
        :type cluster_id: str
        :param extendparam: 
        :type extendparam: :class:`huaweicloudsdkecs.v2.PostPaidServerRootVolumeExtendParam`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkecs.v2.PostPaidServerRootVolumeMetadata`
        """
        
        

        self._volumetype = None
        self._size = None
        self._iops = None
        self._throughput = None
        self._hwpassthrough = None
        self._cluster_type = None
        self._cluster_id = None
        self._extendparam = None
        self._metadata = None
        self.discriminator = None

        self.volumetype = volumetype
        if size is not None:
            self.size = size
        if iops is not None:
            self.iops = iops
        if throughput is not None:
            self.throughput = throughput
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if extendparam is not None:
            self.extendparam = extendparam
        if metadata is not None:
            self.metadata = metadata

    @property
    def volumetype(self):
        r"""Gets the volumetype of this PostPaidServerRootVolume.

        云服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。   - SATA：普通IO磁盘类型。  - SAS：高IO磁盘类型。  - SSD：超高IO磁盘类型。  - GPSSD：为通用型SSD磁盘类型。  - co-p1：高IO (性能优化Ⅰ型)。  - uh-l1：超高IO (时延优化)。  - ESSD：为极速IO磁盘类型。  - GPSSD2：通用型SSD V2磁盘类型。  - ESSD2：极速型SSD V2磁盘类型。   > 说明： >  > 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。  了解不同磁盘类型的详细信息，请参见 [磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。  获取region可用的卷类型，请参见[查询云硬盘类型列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=EVS&api=CinderListVolumeTypes)

        :return: The volumetype of this PostPaidServerRootVolume.
        :rtype: str
        """
        return self._volumetype

    @volumetype.setter
    def volumetype(self, volumetype):
        r"""Sets the volumetype of this PostPaidServerRootVolume.

        云服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。   - SATA：普通IO磁盘类型。  - SAS：高IO磁盘类型。  - SSD：超高IO磁盘类型。  - GPSSD：为通用型SSD磁盘类型。  - co-p1：高IO (性能优化Ⅰ型)。  - uh-l1：超高IO (时延优化)。  - ESSD：为极速IO磁盘类型。  - GPSSD2：通用型SSD V2磁盘类型。  - ESSD2：极速型SSD V2磁盘类型。   > 说明： >  > 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。  了解不同磁盘类型的详细信息，请参见 [磁盘类型及性能介绍](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。  获取region可用的卷类型，请参见[查询云硬盘类型列表](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=EVS&api=CinderListVolumeTypes)

        :param volumetype: The volumetype of this PostPaidServerRootVolume.
        :type volumetype: str
        """
        self._volumetype = volumetype

    @property
    def size(self):
        r"""Gets the size of this PostPaidServerRootVolume.

        系统盘大小，容量单位为GB， 输入大小范围为[1,1024]。  约束：  - 系统盘大小取值应不小于镜像支持的系统盘的最小值(镜像的min_disk属性)。 - 若该参数没有指定或者指定为0时，系统盘大小默认取值为镜像中系统盘的最小值(镜像的min_disk属性)。  > 说明： > > 镜像系统盘的最小值(镜像的min_disk属性)可在控制台中点击镜像详情查看。或通过调用“查询镜像详情（OpenStack原生）”API获取，详细操作请参考[《镜像服务API参考》](https://support.huaweicloud.com/api-ims/ims_03_0702.html)中“查询镜像详情（OpenStack原生）”章节。

        :return: The size of this PostPaidServerRootVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this PostPaidServerRootVolume.

        系统盘大小，容量单位为GB， 输入大小范围为[1,1024]。  约束：  - 系统盘大小取值应不小于镜像支持的系统盘的最小值(镜像的min_disk属性)。 - 若该参数没有指定或者指定为0时，系统盘大小默认取值为镜像中系统盘的最小值(镜像的min_disk属性)。  > 说明： > > 镜像系统盘的最小值(镜像的min_disk属性)可在控制台中点击镜像详情查看。或通过调用“查询镜像详情（OpenStack原生）”API获取，详细操作请参考[《镜像服务API参考》](https://support.huaweicloud.com/api-ims/ims_03_0702.html)中“查询镜像详情（OpenStack原生）”章节。

        :param size: The size of this PostPaidServerRootVolume.
        :type size: int
        """
        self._size = size

    @property
    def iops(self):
        r"""Gets the iops of this PostPaidServerRootVolume.

        给云硬盘配置iops，购买GPSSD2、ESSD2类型的云硬盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2、ESSD2类型的iops大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。

        :return: The iops of this PostPaidServerRootVolume.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        r"""Sets the iops of this PostPaidServerRootVolume.

        给云硬盘配置iops，购买GPSSD2、ESSD2类型的云硬盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2、ESSD2类型的iops大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。

        :param iops: The iops of this PostPaidServerRootVolume.
        :type iops: int
        """
        self._iops = iops

    @property
    def throughput(self):
        r"""Gets the throughput of this PostPaidServerRootVolume.

        给云硬盘配置吞吐量，单位是MiB/s，购买GPSSD2类型云盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2类型的吞吐量大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。

        :return: The throughput of this PostPaidServerRootVolume.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        r"""Sets the throughput of this PostPaidServerRootVolume.

        给云硬盘配置吞吐量，单位是MiB/s，购买GPSSD2类型云盘时必填，其他类型不能设置。  说明： 1、了解GPSSD2类型的吞吐量大小范围，请参见 [云硬盘类型及性能介绍里面的云硬盘性能数据表](https://support.huaweicloud.com/productdesc-evs/zh-cn_topic_0044524691.html)。 2、只支持按需计费。

        :param throughput: The throughput of this PostPaidServerRootVolume.
        :type throughput: int
        """
        self._throughput = throughput

    @property
    def hwpassthrough(self):
        r"""Gets the hwpassthrough of this PostPaidServerRootVolume.

        使用SDI规格创建虚拟机时请关注该参数，如果该参数值为true，说明创建的为scsi类型的卷  > 说明： >  > 此参数为boolean类型，若传入非boolean类型字符，程序将按照false方式处理。

        :return: The hwpassthrough of this PostPaidServerRootVolume.
        :rtype: bool
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        r"""Sets the hwpassthrough of this PostPaidServerRootVolume.

        使用SDI规格创建虚拟机时请关注该参数，如果该参数值为true，说明创建的为scsi类型的卷  > 说明： >  > 此参数为boolean类型，若传入非boolean类型字符，程序将按照false方式处理。

        :param hwpassthrough: The hwpassthrough of this PostPaidServerRootVolume.
        :type hwpassthrough: bool
        """
        self._hwpassthrough = hwpassthrough

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this PostPaidServerRootVolume.

        云服务器系统盘对应的磁盘存储类型。 磁盘存储类型枚举值： DSS：专属存储类型

        :return: The cluster_type of this PostPaidServerRootVolume.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this PostPaidServerRootVolume.

        云服务器系统盘对应的磁盘存储类型。 磁盘存储类型枚举值： DSS：专属存储类型

        :param cluster_type: The cluster_type of this PostPaidServerRootVolume.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this PostPaidServerRootVolume.

        云服务器数据盘对应的存储池的ID。

        :return: The cluster_id of this PostPaidServerRootVolume.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this PostPaidServerRootVolume.

        云服务器数据盘对应的存储池的ID。

        :param cluster_id: The cluster_id of this PostPaidServerRootVolume.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def extendparam(self):
        r"""Gets the extendparam of this PostPaidServerRootVolume.

        :return: The extendparam of this PostPaidServerRootVolume.
        :rtype: :class:`huaweicloudsdkecs.v2.PostPaidServerRootVolumeExtendParam`
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        r"""Sets the extendparam of this PostPaidServerRootVolume.

        :param extendparam: The extendparam of this PostPaidServerRootVolume.
        :type extendparam: :class:`huaweicloudsdkecs.v2.PostPaidServerRootVolumeExtendParam`
        """
        self._extendparam = extendparam

    @property
    def metadata(self):
        r"""Gets the metadata of this PostPaidServerRootVolume.

        :return: The metadata of this PostPaidServerRootVolume.
        :rtype: :class:`huaweicloudsdkecs.v2.PostPaidServerRootVolumeMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this PostPaidServerRootVolume.

        :param metadata: The metadata of this PostPaidServerRootVolume.
        :type metadata: :class:`huaweicloudsdkecs.v2.PostPaidServerRootVolumeMetadata`
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
        if not isinstance(other, PostPaidServerRootVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
