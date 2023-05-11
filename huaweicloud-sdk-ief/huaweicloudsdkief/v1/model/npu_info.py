# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NpuInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'capacity': 'str',
        'driver_version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'capacity': 'capacity',
        'driver_version': 'driver_version'
    }

    def __init__(self, name=None, type=None, capacity=None, driver_version=None):
        """NpuInfo

        The model defined in huaweicloud sdk

        :param name: NPU名称
        :type name: str
        :param type: NPU类型
        :type type: str
        :param capacity: NPU memory大小
        :type capacity: str
        :param driver_version: NPU驱动版本
        :type driver_version: str
        """
        
        

        self._name = None
        self._type = None
        self._capacity = None
        self._driver_version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if capacity is not None:
            self.capacity = capacity
        if driver_version is not None:
            self.driver_version = driver_version

    @property
    def name(self):
        """Gets the name of this NpuInfo.

        NPU名称

        :return: The name of this NpuInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NpuInfo.

        NPU名称

        :param name: The name of this NpuInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this NpuInfo.

        NPU类型

        :return: The type of this NpuInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NpuInfo.

        NPU类型

        :param type: The type of this NpuInfo.
        :type type: str
        """
        self._type = type

    @property
    def capacity(self):
        """Gets the capacity of this NpuInfo.

        NPU memory大小

        :return: The capacity of this NpuInfo.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this NpuInfo.

        NPU memory大小

        :param capacity: The capacity of this NpuInfo.
        :type capacity: str
        """
        self._capacity = capacity

    @property
    def driver_version(self):
        """Gets the driver_version of this NpuInfo.

        NPU驱动版本

        :return: The driver_version of this NpuInfo.
        :rtype: str
        """
        return self._driver_version

    @driver_version.setter
    def driver_version(self, driver_version):
        """Sets the driver_version of this NpuInfo.

        NPU驱动版本

        :param driver_version: The driver_version of this NpuInfo.
        :type driver_version: str
        """
        self._driver_version = driver_version

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
        if not isinstance(other, NpuInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
