# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataVolumes:

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
        'shareable': 'bool',
        'cluster_id': 'str',
        'cluster_type': 'str'
    }

    attribute_map = {
        'volumetype': 'volumetype',
        'size': 'size',
        'shareable': 'shareable',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type'
    }

    def __init__(self, volumetype=None, size=None, shareable=None, cluster_id=None, cluster_type=None):
        """DataVolumes

        The model defined in huaweicloud sdk

        :param volumetype: 裸金属服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。SATA：普通IO磁盘类型SAS：高IO磁盘类型SSD：超高IO磁盘类型约束：在专属云中申请裸金属服务器时，须使用专属企业存储，此时该字段前缀必须是DESS_ 。枚举值如下：DESS_SAS_ISCSI：普通I/O企业存储DESS_SAS_FC：普通I/O企业存储（低延时）DESS_MIX_ISCSI：高I/O企业存储DESS_MIX_FC：高I/O企业存储（低延时）DESS_SSD_ISCSI：超高I/O企业存储DESS_SSD_FC：超高I/O企业存储（低延时）所有用户，包年包月场景下，不能挂载DESS卷。 说明：企业存储支持的存储类型说明可以从管理控制台或参考《专属企业存储服务用户指南》的“申请专属企业存储”“申请专属企业存储”章节获取。
        :type volumetype: str
        :param size: 数据盘大小，容量单位为GB，输入大小范围为[10-32768]。
        :type size: int
        :param shareable: 是否为共享磁盘。true为共享盘，false为普通云硬盘
        :type shareable: bool
        :param cluster_id: 裸金属服务器数据盘对应的存储池ID。 说明：使用专属分布式存储时需要该字段。存储池ID可以从管理控制台或者参考《专属分布式存储API参考》的“获取专属分布式存储池详情列表”章节获取。
        :type cluster_id: str
        :param cluster_type: 裸金属服务器数据盘对应的磁盘存储类型。磁盘存储类型枚举值：DSS（专属分布式存储）。 说明：使用专属分布式存储时需要该字段。存储池类型可以从管理控制台或者参考《专属分布式存储API参考》的“获取专属分布式存储池详情列表”章节获取。
        :type cluster_type: str
        """
        
        

        self._volumetype = None
        self._size = None
        self._shareable = None
        self._cluster_id = None
        self._cluster_type = None
        self.discriminator = None

        self.volumetype = volumetype
        self.size = size
        if shareable is not None:
            self.shareable = shareable
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type

    @property
    def volumetype(self):
        """Gets the volumetype of this DataVolumes.

        裸金属服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。SATA：普通IO磁盘类型SAS：高IO磁盘类型SSD：超高IO磁盘类型约束：在专属云中申请裸金属服务器时，须使用专属企业存储，此时该字段前缀必须是DESS_ 。枚举值如下：DESS_SAS_ISCSI：普通I/O企业存储DESS_SAS_FC：普通I/O企业存储（低延时）DESS_MIX_ISCSI：高I/O企业存储DESS_MIX_FC：高I/O企业存储（低延时）DESS_SSD_ISCSI：超高I/O企业存储DESS_SSD_FC：超高I/O企业存储（低延时）所有用户，包年包月场景下，不能挂载DESS卷。 说明：企业存储支持的存储类型说明可以从管理控制台或参考《专属企业存储服务用户指南》的“申请专属企业存储”“申请专属企业存储”章节获取。

        :return: The volumetype of this DataVolumes.
        :rtype: str
        """
        return self._volumetype

    @volumetype.setter
    def volumetype(self, volumetype):
        """Sets the volumetype of this DataVolumes.

        裸金属服务器系统盘对应的磁盘类型，需要与系统所提供的磁盘类型相匹配。SATA：普通IO磁盘类型SAS：高IO磁盘类型SSD：超高IO磁盘类型约束：在专属云中申请裸金属服务器时，须使用专属企业存储，此时该字段前缀必须是DESS_ 。枚举值如下：DESS_SAS_ISCSI：普通I/O企业存储DESS_SAS_FC：普通I/O企业存储（低延时）DESS_MIX_ISCSI：高I/O企业存储DESS_MIX_FC：高I/O企业存储（低延时）DESS_SSD_ISCSI：超高I/O企业存储DESS_SSD_FC：超高I/O企业存储（低延时）所有用户，包年包月场景下，不能挂载DESS卷。 说明：企业存储支持的存储类型说明可以从管理控制台或参考《专属企业存储服务用户指南》的“申请专属企业存储”“申请专属企业存储”章节获取。

        :param volumetype: The volumetype of this DataVolumes.
        :type volumetype: str
        """
        self._volumetype = volumetype

    @property
    def size(self):
        """Gets the size of this DataVolumes.

        数据盘大小，容量单位为GB，输入大小范围为[10-32768]。

        :return: The size of this DataVolumes.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DataVolumes.

        数据盘大小，容量单位为GB，输入大小范围为[10-32768]。

        :param size: The size of this DataVolumes.
        :type size: int
        """
        self._size = size

    @property
    def shareable(self):
        """Gets the shareable of this DataVolumes.

        是否为共享磁盘。true为共享盘，false为普通云硬盘

        :return: The shareable of this DataVolumes.
        :rtype: bool
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        """Sets the shareable of this DataVolumes.

        是否为共享磁盘。true为共享盘，false为普通云硬盘

        :param shareable: The shareable of this DataVolumes.
        :type shareable: bool
        """
        self._shareable = shareable

    @property
    def cluster_id(self):
        """Gets the cluster_id of this DataVolumes.

        裸金属服务器数据盘对应的存储池ID。 说明：使用专属分布式存储时需要该字段。存储池ID可以从管理控制台或者参考《专属分布式存储API参考》的“获取专属分布式存储池详情列表”章节获取。

        :return: The cluster_id of this DataVolumes.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this DataVolumes.

        裸金属服务器数据盘对应的存储池ID。 说明：使用专属分布式存储时需要该字段。存储池ID可以从管理控制台或者参考《专属分布式存储API参考》的“获取专属分布式存储池详情列表”章节获取。

        :param cluster_id: The cluster_id of this DataVolumes.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        """Gets the cluster_type of this DataVolumes.

        裸金属服务器数据盘对应的磁盘存储类型。磁盘存储类型枚举值：DSS（专属分布式存储）。 说明：使用专属分布式存储时需要该字段。存储池类型可以从管理控制台或者参考《专属分布式存储API参考》的“获取专属分布式存储池详情列表”章节获取。

        :return: The cluster_type of this DataVolumes.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this DataVolumes.

        裸金属服务器数据盘对应的磁盘存储类型。磁盘存储类型枚举值：DSS（专属分布式存储）。 说明：使用专属分布式存储时需要该字段。存储池类型可以从管理控制台或者参考《专属分布式存储API参考》的“获取专属分布式存储池详情列表”章节获取。

        :param cluster_type: The cluster_type of this DataVolumes.
        :type cluster_type: str
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
        if not isinstance(other, DataVolumes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
