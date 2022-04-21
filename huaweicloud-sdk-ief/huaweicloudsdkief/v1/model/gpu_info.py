# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GpuInfo:

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
        'capacity': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'capacity': 'capacity'
    }

    def __init__(self, name=None, type=None, capacity=None):
        """GpuInfo

        The model defined in huaweicloud sdk

        :param name: GPU名称
        :type name: str
        :param type: GPU类型
        :type type: str
        :param capacity: GPU memory大小，单位MB
        :type capacity: str
        """
        
        

        self._name = None
        self._type = None
        self._capacity = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if capacity is not None:
            self.capacity = capacity

    @property
    def name(self):
        """Gets the name of this GpuInfo.

        GPU名称

        :return: The name of this GpuInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GpuInfo.

        GPU名称

        :param name: The name of this GpuInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this GpuInfo.

        GPU类型

        :return: The type of this GpuInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GpuInfo.

        GPU类型

        :param type: The type of this GpuInfo.
        :type type: str
        """
        self._type = type

    @property
    def capacity(self):
        """Gets the capacity of this GpuInfo.

        GPU memory大小，单位MB

        :return: The capacity of this GpuInfo.
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this GpuInfo.

        GPU memory大小，单位MB

        :param capacity: The capacity of this GpuInfo.
        :type capacity: str
        """
        self._capacity = capacity

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
        if not isinstance(other, GpuInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
