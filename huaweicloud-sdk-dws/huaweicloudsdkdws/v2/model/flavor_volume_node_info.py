# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlavorVolumeNodeInfo:

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
        """FlavorVolumeNodeInfo

        The model defined in huaweicloud sdk

        :param volume_type: 节点使用存储类型
        :type volume_type: str
        :param volume_num: 节点使用的磁盘数量
        :type volume_num: int
        :param capacity: 节点去除副本后的有效容量
        :type capacity: int
        :param volume_size: 节点存的单盘容量
        :type volume_size: int
        """
        
        

        self._volume_type = None
        self._volume_num = None
        self._capacity = None
        self._volume_size = None
        self.discriminator = None

        self.volume_type = volume_type
        self.volume_num = volume_num
        self.capacity = capacity
        self.volume_size = volume_size

    @property
    def volume_type(self):
        """Gets the volume_type of this FlavorVolumeNodeInfo.

        节点使用存储类型

        :return: The volume_type of this FlavorVolumeNodeInfo.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this FlavorVolumeNodeInfo.

        节点使用存储类型

        :param volume_type: The volume_type of this FlavorVolumeNodeInfo.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def volume_num(self):
        """Gets the volume_num of this FlavorVolumeNodeInfo.

        节点使用的磁盘数量

        :return: The volume_num of this FlavorVolumeNodeInfo.
        :rtype: int
        """
        return self._volume_num

    @volume_num.setter
    def volume_num(self, volume_num):
        """Sets the volume_num of this FlavorVolumeNodeInfo.

        节点使用的磁盘数量

        :param volume_num: The volume_num of this FlavorVolumeNodeInfo.
        :type volume_num: int
        """
        self._volume_num = volume_num

    @property
    def capacity(self):
        """Gets the capacity of this FlavorVolumeNodeInfo.

        节点去除副本后的有效容量

        :return: The capacity of this FlavorVolumeNodeInfo.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this FlavorVolumeNodeInfo.

        节点去除副本后的有效容量

        :param capacity: The capacity of this FlavorVolumeNodeInfo.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def volume_size(self):
        """Gets the volume_size of this FlavorVolumeNodeInfo.

        节点存的单盘容量

        :return: The volume_size of this FlavorVolumeNodeInfo.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this FlavorVolumeNodeInfo.

        节点存的单盘容量

        :param volume_size: The volume_size of this FlavorVolumeNodeInfo.
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
        if not isinstance(other, FlavorVolumeNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
