# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProductVolumeUsedResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_type': 'str',
        'volume_num': 'int',
        'capacity': 'int',
        'volume_size': 'int'
    }

    attribute_map = {
        'volume_type': 'volume_type',
        'volume_num': 'volume_num',
        'capacity': 'capacity',
        'volume_size': 'volume_size'
    }

    def __init__(self, volume_type=None, volume_num=None, capacity=None, volume_size=None):
        r"""ProductVolumeUsedResp

        The model defined in huaweicloud sdk

        :param volume_type: **参数解释**： 节点使用存储类型。 **取值范围**： HIGH：SAS盘； ULTRAHIGH：SSD云盘； COMMON：SATA盘； LOCAL_DISK：本地盘；
        :type volume_type: str
        :param volume_num: **参数解释**： 节点使用的磁盘数量信息。 **取值范围**： 不涉及。
        :type volume_num: int
        :param capacity: **参数解释**： 集群单节点的可用存储容量。 **取值范围**： 不涉及。
        :type capacity: int
        :param volume_size: **参数解释**： 集群节点上单数据磁盘的物理存储容量。 **取值范围**： 不涉及。
        :type volume_size: int
        """
        
        

        self._volume_type = None
        self._volume_num = None
        self._capacity = None
        self._volume_size = None
        self.discriminator = None

        if volume_type is not None:
            self.volume_type = volume_type
        if volume_num is not None:
            self.volume_num = volume_num
        if capacity is not None:
            self.capacity = capacity
        if volume_size is not None:
            self.volume_size = volume_size

    @property
    def volume_type(self):
        r"""Gets the volume_type of this ProductVolumeUsedResp.

        **参数解释**： 节点使用存储类型。 **取值范围**： HIGH：SAS盘； ULTRAHIGH：SSD云盘； COMMON：SATA盘； LOCAL_DISK：本地盘；

        :return: The volume_type of this ProductVolumeUsedResp.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this ProductVolumeUsedResp.

        **参数解释**： 节点使用存储类型。 **取值范围**： HIGH：SAS盘； ULTRAHIGH：SSD云盘； COMMON：SATA盘； LOCAL_DISK：本地盘；

        :param volume_type: The volume_type of this ProductVolumeUsedResp.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def volume_num(self):
        r"""Gets the volume_num of this ProductVolumeUsedResp.

        **参数解释**： 节点使用的磁盘数量信息。 **取值范围**： 不涉及。

        :return: The volume_num of this ProductVolumeUsedResp.
        :rtype: int
        """
        return self._volume_num

    @volume_num.setter
    def volume_num(self, volume_num):
        r"""Sets the volume_num of this ProductVolumeUsedResp.

        **参数解释**： 节点使用的磁盘数量信息。 **取值范围**： 不涉及。

        :param volume_num: The volume_num of this ProductVolumeUsedResp.
        :type volume_num: int
        """
        self._volume_num = volume_num

    @property
    def capacity(self):
        r"""Gets the capacity of this ProductVolumeUsedResp.

        **参数解释**： 集群单节点的可用存储容量。 **取值范围**： 不涉及。

        :return: The capacity of this ProductVolumeUsedResp.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this ProductVolumeUsedResp.

        **参数解释**： 集群单节点的可用存储容量。 **取值范围**： 不涉及。

        :param capacity: The capacity of this ProductVolumeUsedResp.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def volume_size(self):
        r"""Gets the volume_size of this ProductVolumeUsedResp.

        **参数解释**： 集群节点上单数据磁盘的物理存储容量。 **取值范围**： 不涉及。

        :return: The volume_size of this ProductVolumeUsedResp.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        r"""Sets the volume_size of this ProductVolumeUsedResp.

        **参数解释**： 集群节点上单数据磁盘的物理存储容量。 **取值范围**： 不涉及。

        :param volume_size: The volume_size of this ProductVolumeUsedResp.
        :type volume_size: int
        """
        self._volume_size = volume_size

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
        if not isinstance(other, ProductVolumeUsedResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
