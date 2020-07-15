# coding: utf-8

import pprint
import re

import six





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
        'hwpassthrough': 'bool',
        'cluster_type': 'str',
        'cluster_id': 'str',
        'extendparam': 'PostPaidServerRootVolumeExtendParam'
    }

    attribute_map = {
        'volumetype': 'volumetype',
        'size': 'size',
        'hwpassthrough': 'hw:passthrough',
        'cluster_type': 'cluster_type',
        'cluster_id': 'cluster_id',
        'extendparam': 'extendparam'
    }

    def __init__(self, volumetype=None, size=None, hwpassthrough=False, cluster_type=None, cluster_id=None, extendparam=None):
        """PostPaidServerRootVolume - a model defined in huaweicloud sdk"""
        
        

        self._volumetype = None
        self._size = None
        self._hwpassthrough = None
        self._cluster_type = None
        self._cluster_id = None
        self._extendparam = None
        self.discriminator = None

        self.volumetype = volumetype
        if size is not None:
            self.size = size
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if extendparam is not None:
            self.extendparam = extendparam

    @property
    def volumetype(self):
        """Gets the volumetype of this PostPaidServerRootVolume.

        云服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SATA：普通IO磁盘类型。 - SAS：高IO磁盘类型。 - SSD：超高IO磁盘类型。 - co-p1：高IO (性能优化Ⅰ型) - uh-l1：超高IO (时延优化)  > 说明： >  > 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。

        :return: The volumetype of this PostPaidServerRootVolume.
        :rtype: str
        """
        return self._volumetype

    @volumetype.setter
    def volumetype(self, volumetype):
        """Sets the volumetype of this PostPaidServerRootVolume.

        云服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。  - SATA：普通IO磁盘类型。 - SAS：高IO磁盘类型。 - SSD：超高IO磁盘类型。 - co-p1：高IO (性能优化Ⅰ型) - uh-l1：超高IO (时延优化)  > 说明： >  > 对于HANA云服务器、HL1型云服务器、HL2型云服务器，需使用co-p1和uh-l1两种磁盘类型。对于其他类型的云服务器，不能使用co-p1和uh-l1两种磁盘类型。

        :param volumetype: The volumetype of this PostPaidServerRootVolume.
        :type: str
        """
        self._volumetype = volumetype

    @property
    def size(self):
        """Gets the size of this PostPaidServerRootVolume.

        系统盘大小，容量单位为GB， 输入大小范围为[1,1024]。  约束：  - 系统盘大小取值应不小于镜像支持的系统盘的最小值(镜像的min_disk属性)。 - 若该参数没有指定或者指定为0时，系统盘大小默认取值为镜像中系统盘的最小值(镜像的min_disk属性)。  > 说明： >  > 镜像系统盘的最小值(镜像的min_disk属性)可在控制台中点击镜像详情查看。或通过调用“查询镜像详情（OpenStack原生）”API获取，详细操作请参考《镜像服务API参考》中“查询镜像详情（OpenStack原生）”章节。

        :return: The size of this PostPaidServerRootVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PostPaidServerRootVolume.

        系统盘大小，容量单位为GB， 输入大小范围为[1,1024]。  约束：  - 系统盘大小取值应不小于镜像支持的系统盘的最小值(镜像的min_disk属性)。 - 若该参数没有指定或者指定为0时，系统盘大小默认取值为镜像中系统盘的最小值(镜像的min_disk属性)。  > 说明： >  > 镜像系统盘的最小值(镜像的min_disk属性)可在控制台中点击镜像详情查看。或通过调用“查询镜像详情（OpenStack原生）”API获取，详细操作请参考《镜像服务API参考》中“查询镜像详情（OpenStack原生）”章节。

        :param size: The size of this PostPaidServerRootVolume.
        :type: int
        """
        self._size = size

    @property
    def hwpassthrough(self):
        """Gets the hwpassthrough of this PostPaidServerRootVolume.

        使用SDI规格创建虚拟机时请关注该参数，如果该参数值为true，说明创建的为scsi类型的卷  > 说明： >  > 此参数为boolean类型，若传入非boolean类型字符，程序将按照false方式处理。

        :return: The hwpassthrough of this PostPaidServerRootVolume.
        :rtype: bool
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        """Sets the hwpassthrough of this PostPaidServerRootVolume.

        使用SDI规格创建虚拟机时请关注该参数，如果该参数值为true，说明创建的为scsi类型的卷  > 说明： >  > 此参数为boolean类型，若传入非boolean类型字符，程序将按照false方式处理。

        :param hwpassthrough: The hwpassthrough of this PostPaidServerRootVolume.
        :type: bool
        """
        self._hwpassthrough = hwpassthrough

    @property
    def cluster_type(self):
        """Gets the cluster_type of this PostPaidServerRootVolume.

        云服务器系统盘对应的磁盘存储类型。 磁盘存储类型枚举值： DSS：专属存储类型

        :return: The cluster_type of this PostPaidServerRootVolume.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this PostPaidServerRootVolume.

        云服务器系统盘对应的磁盘存储类型。 磁盘存储类型枚举值： DSS：专属存储类型

        :param cluster_type: The cluster_type of this PostPaidServerRootVolume.
        :type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this PostPaidServerRootVolume.

        使用SDI规格创建虚拟机时请关注该参数，如果该参数值为true，说明创建的为scsi类型的卷

        :return: The cluster_id of this PostPaidServerRootVolume.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this PostPaidServerRootVolume.

        使用SDI规格创建虚拟机时请关注该参数，如果该参数值为true，说明创建的为scsi类型的卷

        :param cluster_id: The cluster_id of this PostPaidServerRootVolume.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def extendparam(self):
        """Gets the extendparam of this PostPaidServerRootVolume.


        :return: The extendparam of this PostPaidServerRootVolume.
        :rtype: PostPaidServerRootVolumeExtendParam
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        """Sets the extendparam of this PostPaidServerRootVolume.


        :param extendparam: The extendparam of this PostPaidServerRootVolume.
        :type: PostPaidServerRootVolumeExtendParam
        """
        self._extendparam = extendparam

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
        if not isinstance(other, PostPaidServerRootVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
