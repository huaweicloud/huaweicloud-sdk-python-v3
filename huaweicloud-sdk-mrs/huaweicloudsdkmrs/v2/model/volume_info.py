# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeInfo:

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
        'size': 'int',
        'count': 'int'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size',
        'count': 'count'
    }

    def __init__(self, type=None, size=None, count=None):
        r"""VolumeInfo

        The model defined in huaweicloud sdk

        :param type: 磁盘类型。 - SATA：普通IO磁盘类型。 - SAS：高IO磁盘类型。 - SSD：超高IO磁盘类型。 - GPSSD：通用型SSD磁盘类型
        :type type: str
        :param size: 磁盘大小。单位为GB。
        :type size: int
        :param count: 磁盘数量。
        :type count: int
        """
        
        

        self._type = None
        self._size = None
        self._count = None
        self.discriminator = None

        self.type = type
        self.size = size
        self.count = count

    @property
    def type(self):
        r"""Gets the type of this VolumeInfo.

        磁盘类型。 - SATA：普通IO磁盘类型。 - SAS：高IO磁盘类型。 - SSD：超高IO磁盘类型。 - GPSSD：通用型SSD磁盘类型

        :return: The type of this VolumeInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this VolumeInfo.

        磁盘类型。 - SATA：普通IO磁盘类型。 - SAS：高IO磁盘类型。 - SSD：超高IO磁盘类型。 - GPSSD：通用型SSD磁盘类型

        :param type: The type of this VolumeInfo.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this VolumeInfo.

        磁盘大小。单位为GB。

        :return: The size of this VolumeInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this VolumeInfo.

        磁盘大小。单位为GB。

        :param size: The size of this VolumeInfo.
        :type size: int
        """
        self._size = size

    @property
    def count(self):
        r"""Gets the count of this VolumeInfo.

        磁盘数量。

        :return: The count of this VolumeInfo.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this VolumeInfo.

        磁盘数量。

        :param count: The count of this VolumeInfo.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, VolumeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
