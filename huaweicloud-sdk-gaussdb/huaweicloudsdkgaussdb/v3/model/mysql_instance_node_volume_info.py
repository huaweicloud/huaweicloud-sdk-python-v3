# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlInstanceNodeVolumeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'used': 'str',
        'size': 'int'
    }

    attribute_map = {
        'type': 'type',
        'used': 'used',
        'size': 'size'
    }

    def __init__(self, type=None, used=None, size=None):
        """MysqlInstanceNodeVolumeInfo

        The model defined in huaweicloud sdk

        :param type: 磁盘类型。
        :type type: str
        :param used: 已使用磁盘大小，单位GB。
        :type used: str
        :param size: 包周期购买的存储空间大小，单位GB。
        :type size: int
        """
        
        

        self._type = None
        self._used = None
        self._size = None
        self.discriminator = None

        self.type = type
        self.used = used
        self.size = size

    @property
    def type(self):
        """Gets the type of this MysqlInstanceNodeVolumeInfo.

        磁盘类型。

        :return: The type of this MysqlInstanceNodeVolumeInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MysqlInstanceNodeVolumeInfo.

        磁盘类型。

        :param type: The type of this MysqlInstanceNodeVolumeInfo.
        :type type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this MysqlInstanceNodeVolumeInfo.

        已使用磁盘大小，单位GB。

        :return: The used of this MysqlInstanceNodeVolumeInfo.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this MysqlInstanceNodeVolumeInfo.

        已使用磁盘大小，单位GB。

        :param used: The used of this MysqlInstanceNodeVolumeInfo.
        :type used: str
        """
        self._used = used

    @property
    def size(self):
        """Gets the size of this MysqlInstanceNodeVolumeInfo.

        包周期购买的存储空间大小，单位GB。

        :return: The size of this MysqlInstanceNodeVolumeInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MysqlInstanceNodeVolumeInfo.

        包周期购买的存储空间大小，单位GB。

        :param size: The size of this MysqlInstanceNodeVolumeInfo.
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
        if not isinstance(other, MysqlInstanceNodeVolumeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
