# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReduceVolumeObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int'
    }

    attribute_map = {
        'size': 'size'
    }

    def __init__(self, size=None):
        r"""ReduceVolumeObject

        The model defined in huaweicloud sdk

        :param size: 缩容后实例磁盘的目标大小。每次缩容至少缩小10GB；目标大小必须为10的整数倍。 为确保实例的正常使用，根据当前磁盘的使用量情况存在磁盘容量下限，当此参数小于磁盘容量下限时，缩容会下发失败，此时请适当调大此参数。
        :type size: int
        """
        
        

        self._size = None
        self.discriminator = None

        self.size = size

    @property
    def size(self):
        r"""Gets the size of this ReduceVolumeObject.

        缩容后实例磁盘的目标大小。每次缩容至少缩小10GB；目标大小必须为10的整数倍。 为确保实例的正常使用，根据当前磁盘的使用量情况存在磁盘容量下限，当此参数小于磁盘容量下限时，缩容会下发失败，此时请适当调大此参数。

        :return: The size of this ReduceVolumeObject.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ReduceVolumeObject.

        缩容后实例磁盘的目标大小。每次缩容至少缩小10GB；目标大小必须为10的整数倍。 为确保实例的正常使用，根据当前磁盘的使用量情况存在磁盘容量下限，当此参数小于磁盘容量下限时，缩容会下发失败，此时请适当调大此参数。

        :param size: The size of this ReduceVolumeObject.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ReduceVolumeObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
