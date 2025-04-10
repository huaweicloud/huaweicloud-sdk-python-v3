# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ASICAcceleratorInfo:

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
        'count': 'int',
        'memory_mb': 'int'
    }

    attribute_map = {
        'name': 'name',
        'count': 'count',
        'memory_mb': 'memory_mb'
    }

    def __init__(self, name=None, count=None, memory_mb=None):
        r"""ASICAcceleratorInfo

        The model defined in huaweicloud sdk

        :param name: ASIC设备名称。
        :type name: str
        :param count: ASIC设备数量。
        :type count: int
        :param memory_mb: ASIC设备的内存，单位为MB。
        :type memory_mb: int
        """
        
        

        self._name = None
        self._count = None
        self._memory_mb = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if count is not None:
            self.count = count
        if memory_mb is not None:
            self.memory_mb = memory_mb

    @property
    def name(self):
        r"""Gets the name of this ASICAcceleratorInfo.

        ASIC设备名称。

        :return: The name of this ASICAcceleratorInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ASICAcceleratorInfo.

        ASIC设备名称。

        :param name: The name of this ASICAcceleratorInfo.
        :type name: str
        """
        self._name = name

    @property
    def count(self):
        r"""Gets the count of this ASICAcceleratorInfo.

        ASIC设备数量。

        :return: The count of this ASICAcceleratorInfo.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ASICAcceleratorInfo.

        ASIC设备数量。

        :param count: The count of this ASICAcceleratorInfo.
        :type count: int
        """
        self._count = count

    @property
    def memory_mb(self):
        r"""Gets the memory_mb of this ASICAcceleratorInfo.

        ASIC设备的内存，单位为MB。

        :return: The memory_mb of this ASICAcceleratorInfo.
        :rtype: int
        """
        return self._memory_mb

    @memory_mb.setter
    def memory_mb(self, memory_mb):
        r"""Sets the memory_mb of this ASICAcceleratorInfo.

        ASIC设备的内存，单位为MB。

        :param memory_mb: The memory_mb of this ASICAcceleratorInfo.
        :type memory_mb: int
        """
        self._memory_mb = memory_mb

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
        if not isinstance(other, ASICAcceleratorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
