# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClickHouseNodeInfoVolume:

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
        'size': 'str',
        'used': 'str',
        'iops': 'int'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size',
        'used': 'used',
        'iops': 'iops'
    }

    def __init__(self, type=None, size=None, used=None, iops=None):
        """ClickHouseNodeInfoVolume

        The model defined in huaweicloud sdk

        :param type: 实例节点存储类型。 取值范围： - SSD：超高IO - ESSD：极速型SSD
        :type type: str
        :param size: 实例节点存储大小。
        :type size: str
        :param used: 实例节点存储使用大小。
        :type used: str
        :param iops: 实例节点存储IOPS大小。
        :type iops: int
        """
        
        

        self._type = None
        self._size = None
        self._used = None
        self._iops = None
        self.discriminator = None

        self.type = type
        self.size = size
        if used is not None:
            self.used = used
        if iops is not None:
            self.iops = iops

    @property
    def type(self):
        """Gets the type of this ClickHouseNodeInfoVolume.

        实例节点存储类型。 取值范围： - SSD：超高IO - ESSD：极速型SSD

        :return: The type of this ClickHouseNodeInfoVolume.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClickHouseNodeInfoVolume.

        实例节点存储类型。 取值范围： - SSD：超高IO - ESSD：极速型SSD

        :param type: The type of this ClickHouseNodeInfoVolume.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        """Gets the size of this ClickHouseNodeInfoVolume.

        实例节点存储大小。

        :return: The size of this ClickHouseNodeInfoVolume.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ClickHouseNodeInfoVolume.

        实例节点存储大小。

        :param size: The size of this ClickHouseNodeInfoVolume.
        :type size: str
        """
        self._size = size

    @property
    def used(self):
        """Gets the used of this ClickHouseNodeInfoVolume.

        实例节点存储使用大小。

        :return: The used of this ClickHouseNodeInfoVolume.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ClickHouseNodeInfoVolume.

        实例节点存储使用大小。

        :param used: The used of this ClickHouseNodeInfoVolume.
        :type used: str
        """
        self._used = used

    @property
    def iops(self):
        """Gets the iops of this ClickHouseNodeInfoVolume.

        实例节点存储IOPS大小。

        :return: The iops of this ClickHouseNodeInfoVolume.
        :rtype: int
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """Sets the iops of this ClickHouseNodeInfoVolume.

        实例节点存储IOPS大小。

        :param iops: The iops of this ClickHouseNodeInfoVolume.
        :type iops: int
        """
        self._iops = iops

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
        if not isinstance(other, ClickHouseNodeInfoVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
