# coding: utf-8

import pprint
import re

import six





class RootVolume:


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
        'cluster_id': 'str',
        'cluster_type': 'str'
    }

    attribute_map = {
        'volumetype': 'volumetype',
        'size': 'size',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type'
    }

    def __init__(self, volumetype=None, size=None, cluster_id=None, cluster_type=None):
        """RootVolume - a model defined in huaweicloud sdk"""
        
        

        self._volumetype = None
        self._size = None
        self._cluster_id = None
        self._cluster_type = None
        self.discriminator = None

        self.volumetype = volumetype
        self.size = size
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type

    @property
    def volumetype(self):
        """Gets the volumetype of this RootVolume.

        裸金属服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。SATA：普通IO磁盘类型SAS：高IO磁盘类型SSD：超高IO磁盘类型

        :return: The volumetype of this RootVolume.
        :rtype: str
        """
        return self._volumetype

    @volumetype.setter
    def volumetype(self, volumetype):
        """Sets the volumetype of this RootVolume.

        裸金属服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。SATA：普通IO磁盘类型SAS：高IO磁盘类型SSD：超高IO磁盘类型

        :param volumetype: The volumetype of this RootVolume.
        :type: str
        """
        self._volumetype = volumetype

    @property
    def size(self):
        """Gets the size of this RootVolume.

        系统盘大小，容量单位为GB，输入大小范围为[40-1024]。约束：系统盘大小取值应不小于镜像中系统盘的最小值（min_disk属性）。

        :return: The size of this RootVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this RootVolume.

        系统盘大小，容量单位为GB，输入大小范围为[40-1024]。约束：系统盘大小取值应不小于镜像中系统盘的最小值（min_disk属性）。

        :param size: The size of this RootVolume.
        :type: int
        """
        self._size = size

    @property
    def cluster_id(self):
        """Gets the cluster_id of this RootVolume.

        裸金属服务器系统盘对应的存储池的ID。 说明：使用专属分布式存储时需要该字段。存储池ID可以从管理控制台或者参考《专属分布式存储API参考》的“获取专属分布式存储池详情列表”章节获取。

        :return: The cluster_id of this RootVolume.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this RootVolume.

        裸金属服务器系统盘对应的存储池的ID。 说明：使用专属分布式存储时需要该字段。存储池ID可以从管理控制台或者参考《专属分布式存储API参考》的“获取专属分布式存储池详情列表”章节获取。

        :param cluster_id: The cluster_id of this RootVolume.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        """Gets the cluster_type of this RootVolume.

        裸金属服务器系统盘对应的磁盘存储类型。磁盘存储类型枚举值：DSS（专属分布式存储）。 说明：使用专属分布式存储时需要该字段。存储池类型可以从管理控制台或者参考《专属分布式存储API参考》的“获取专属分布式存储池详情列表”章节获取。

        :return: The cluster_type of this RootVolume.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this RootVolume.

        裸金属服务器系统盘对应的磁盘存储类型。磁盘存储类型枚举值：DSS（专属分布式存储）。 说明：使用专属分布式存储时需要该字段。存储池类型可以从管理控制台或者参考《专属分布式存储API参考》的“获取专属分布式存储池详情列表”章节获取。

        :param cluster_type: The cluster_type of this RootVolume.
        :type: str
        """
        self._cluster_type = cluster_type

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
        if not isinstance(other, RootVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
