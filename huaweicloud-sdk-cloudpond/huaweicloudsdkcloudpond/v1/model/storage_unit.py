# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageUnit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_type': 'StorageType',
        'capacity': 'int',
        'gears': 'list[int]',
        'flavor_type': 'str',
        'count': 'int'
    }

    attribute_map = {
        'storage_type': 'storage_type',
        'capacity': 'capacity',
        'gears': 'gears',
        'flavor_type': 'flavor_type',
        'count': 'count'
    }

    def __init__(self, storage_type=None, capacity=None, gears=None, flavor_type=None, count=None):
        """StorageUnit

        The model defined in huaweicloud sdk

        :param storage_type: 
        :type storage_type: :class:`huaweicloudsdkcloudpond.v1.StorageType`
        :param capacity: 存储池大小，单位：TB。
        :type capacity: int
        :param gears: 存储池销售档位
        :type gears: list[int]
        :param flavor_type: 规格类型。例如：highio-4T
        :type flavor_type: str
        :param count: 存储节点台数。
        :type count: int
        """
        
        

        self._storage_type = None
        self._capacity = None
        self._gears = None
        self._flavor_type = None
        self._count = None
        self.discriminator = None

        self.storage_type = storage_type
        self.capacity = capacity
        self.gears = gears
        self.flavor_type = flavor_type
        self.count = count

    @property
    def storage_type(self):
        """Gets the storage_type of this StorageUnit.

        :return: The storage_type of this StorageUnit.
        :rtype: :class:`huaweicloudsdkcloudpond.v1.StorageType`
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this StorageUnit.

        :param storage_type: The storage_type of this StorageUnit.
        :type storage_type: :class:`huaweicloudsdkcloudpond.v1.StorageType`
        """
        self._storage_type = storage_type

    @property
    def capacity(self):
        """Gets the capacity of this StorageUnit.

        存储池大小，单位：TB。

        :return: The capacity of this StorageUnit.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this StorageUnit.

        存储池大小，单位：TB。

        :param capacity: The capacity of this StorageUnit.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def gears(self):
        """Gets the gears of this StorageUnit.

        存储池销售档位

        :return: The gears of this StorageUnit.
        :rtype: list[int]
        """
        return self._gears

    @gears.setter
    def gears(self, gears):
        """Sets the gears of this StorageUnit.

        存储池销售档位

        :param gears: The gears of this StorageUnit.
        :type gears: list[int]
        """
        self._gears = gears

    @property
    def flavor_type(self):
        """Gets the flavor_type of this StorageUnit.

        规格类型。例如：highio-4T

        :return: The flavor_type of this StorageUnit.
        :rtype: str
        """
        return self._flavor_type

    @flavor_type.setter
    def flavor_type(self, flavor_type):
        """Sets the flavor_type of this StorageUnit.

        规格类型。例如：highio-4T

        :param flavor_type: The flavor_type of this StorageUnit.
        :type flavor_type: str
        """
        self._flavor_type = flavor_type

    @property
    def count(self):
        """Gets the count of this StorageUnit.

        存储节点台数。

        :return: The count of this StorageUnit.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this StorageUnit.

        存储节点台数。

        :param count: The count of this StorageUnit.
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
        if not isinstance(other, StorageUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
