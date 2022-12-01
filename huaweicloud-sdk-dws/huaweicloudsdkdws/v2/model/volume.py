# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Volume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume': 'str',
        'capacity': 'int'
    }

    attribute_map = {
        'volume': 'volume',
        'capacity': 'capacity'
    }

    def __init__(self, volume=None, capacity=None):
        """Volume

        The model defined in huaweicloud sdk

        :param volume: 磁盘名称，取值范围为 SSD（超高IO）,高IO（SAS），普通IO（SATA）
        :type volume: str
        :param capacity: 磁盘容量
        :type capacity: int
        """
        
        

        self._volume = None
        self._capacity = None
        self.discriminator = None

        if volume is not None:
            self.volume = volume
        if capacity is not None:
            self.capacity = capacity

    @property
    def volume(self):
        """Gets the volume of this Volume.

        磁盘名称，取值范围为 SSD（超高IO）,高IO（SAS），普通IO（SATA）

        :return: The volume of this Volume.
        :rtype: str
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this Volume.

        磁盘名称，取值范围为 SSD（超高IO）,高IO（SAS），普通IO（SATA）

        :param volume: The volume of this Volume.
        :type volume: str
        """
        self._volume = volume

    @property
    def capacity(self):
        """Gets the capacity of this Volume.

        磁盘容量

        :return: The capacity of this Volume.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this Volume.

        磁盘容量

        :param capacity: The capacity of this Volume.
        :type capacity: int
        """
        self._capacity = capacity

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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
