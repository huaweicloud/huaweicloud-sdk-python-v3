# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataVolume:

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
        'volume_type': 'str'
    }

    attribute_map = {
        'size': 'size',
        'volume_type': 'volume_type'
    }

    def __init__(self, size=None, volume_type=None):
        """DataVolume

        The model defined in huaweicloud sdk

        :param size: 数据盘大小，容量单位为GB，输入大小范围为[1,500]。
        :type size: int
        :param volume_type: 边缘实例数据盘对应的磁盘类型，需要与站点所提供的磁盘类型相匹配。
        :type volume_type: str
        """
        
        

        self._size = None
        self._volume_type = None
        self.discriminator = None

        self.size = size
        self.volume_type = volume_type

    @property
    def size(self):
        """Gets the size of this DataVolume.

        数据盘大小，容量单位为GB，输入大小范围为[1,500]。

        :return: The size of this DataVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DataVolume.

        数据盘大小，容量单位为GB，输入大小范围为[1,500]。

        :param size: The size of this DataVolume.
        :type size: int
        """
        self._size = size

    @property
    def volume_type(self):
        """Gets the volume_type of this DataVolume.

        边缘实例数据盘对应的磁盘类型，需要与站点所提供的磁盘类型相匹配。

        :return: The volume_type of this DataVolume.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this DataVolume.

        边缘实例数据盘对应的磁盘类型，需要与站点所提供的磁盘类型相匹配。

        :param volume_type: The volume_type of this DataVolume.
        :type volume_type: str
        """
        self._volume_type = volume_type

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
        if not isinstance(other, DataVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
