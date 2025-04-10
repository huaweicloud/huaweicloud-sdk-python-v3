# coding: utf-8

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
        'size': 'str',
        'used': 'str'
    }

    attribute_map = {
        'size': 'size',
        'used': 'used'
    }

    def __init__(self, size=None, used=None):
        r"""Volume

        The model defined in huaweicloud sdk

        :param size: 磁盘大小。单位：GB。
        :type size: str
        :param used: 磁盘使用量。单位：GB。
        :type used: str
        """
        
        

        self._size = None
        self._used = None
        self.discriminator = None

        self.size = size
        self.used = used

    @property
    def size(self):
        r"""Gets the size of this Volume.

        磁盘大小。单位：GB。

        :return: The size of this Volume.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this Volume.

        磁盘大小。单位：GB。

        :param size: The size of this Volume.
        :type size: str
        """
        self._size = size

    @property
    def used(self):
        r"""Gets the used of this Volume.

        磁盘使用量。单位：GB。

        :return: The used of this Volume.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this Volume.

        磁盘使用量。单位：GB。

        :param used: The used of this Volume.
        :type used: str
        """
        self._used = used

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
