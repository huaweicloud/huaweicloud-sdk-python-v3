# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RackInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'power': 'int',
        'size': 'str',
        'has_lock': 'bool'
    }

    attribute_map = {
        'power': 'power',
        'size': 'size',
        'has_lock': 'has_lock'
    }

    def __init__(self, power=None, size=None, has_lock=None):
        r"""RackInfo

        The model defined in huaweicloud sdk

        :param power: 机柜功率，单位：w
        :type power: int
        :param size: 机柜尺寸，如100\\*200\\*200，单位：cm
        :type size: str
        :param has_lock: 是否有机柜锁。
        :type has_lock: bool
        """
        
        

        self._power = None
        self._size = None
        self._has_lock = None
        self.discriminator = None

        if power is not None:
            self.power = power
        if size is not None:
            self.size = size
        if has_lock is not None:
            self.has_lock = has_lock

    @property
    def power(self):
        r"""Gets the power of this RackInfo.

        机柜功率，单位：w

        :return: The power of this RackInfo.
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power):
        r"""Sets the power of this RackInfo.

        机柜功率，单位：w

        :param power: The power of this RackInfo.
        :type power: int
        """
        self._power = power

    @property
    def size(self):
        r"""Gets the size of this RackInfo.

        机柜尺寸，如100\\*200\\*200，单位：cm

        :return: The size of this RackInfo.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this RackInfo.

        机柜尺寸，如100\\*200\\*200，单位：cm

        :param size: The size of this RackInfo.
        :type size: str
        """
        self._size = size

    @property
    def has_lock(self):
        r"""Gets the has_lock of this RackInfo.

        是否有机柜锁。

        :return: The has_lock of this RackInfo.
        :rtype: bool
        """
        return self._has_lock

    @has_lock.setter
    def has_lock(self, has_lock):
        r"""Sets the has_lock of this RackInfo.

        是否有机柜锁。

        :param has_lock: The has_lock of this RackInfo.
        :type has_lock: bool
        """
        self._has_lock = has_lock

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
        if not isinstance(other, RackInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
