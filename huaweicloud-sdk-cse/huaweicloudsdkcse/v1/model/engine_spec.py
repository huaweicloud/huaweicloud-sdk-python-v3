# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EngineSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'available_cpu_memory': 'str',
        'linear': 'str',
        'available_prefix': 'str'
    }

    attribute_map = {
        'available_cpu_memory': 'availableCpuMemory',
        'linear': 'linear',
        'available_prefix': 'availablePrefix'
    }

    def __init__(self, available_cpu_memory=None, linear=None, available_prefix=None):
        r"""EngineSpec

        The model defined in huaweicloud sdk

        :param available_cpu_memory: CPU及内存规格。
        :type available_cpu_memory: str
        :param linear: 是否为线性规格。
        :type linear: str
        :param available_prefix: 可用节点规格类型前缀。
        :type available_prefix: str
        """
        
        

        self._available_cpu_memory = None
        self._linear = None
        self._available_prefix = None
        self.discriminator = None

        if available_cpu_memory is not None:
            self.available_cpu_memory = available_cpu_memory
        if linear is not None:
            self.linear = linear
        if available_prefix is not None:
            self.available_prefix = available_prefix

    @property
    def available_cpu_memory(self):
        r"""Gets the available_cpu_memory of this EngineSpec.

        CPU及内存规格。

        :return: The available_cpu_memory of this EngineSpec.
        :rtype: str
        """
        return self._available_cpu_memory

    @available_cpu_memory.setter
    def available_cpu_memory(self, available_cpu_memory):
        r"""Sets the available_cpu_memory of this EngineSpec.

        CPU及内存规格。

        :param available_cpu_memory: The available_cpu_memory of this EngineSpec.
        :type available_cpu_memory: str
        """
        self._available_cpu_memory = available_cpu_memory

    @property
    def linear(self):
        r"""Gets the linear of this EngineSpec.

        是否为线性规格。

        :return: The linear of this EngineSpec.
        :rtype: str
        """
        return self._linear

    @linear.setter
    def linear(self, linear):
        r"""Sets the linear of this EngineSpec.

        是否为线性规格。

        :param linear: The linear of this EngineSpec.
        :type linear: str
        """
        self._linear = linear

    @property
    def available_prefix(self):
        r"""Gets the available_prefix of this EngineSpec.

        可用节点规格类型前缀。

        :return: The available_prefix of this EngineSpec.
        :rtype: str
        """
        return self._available_prefix

    @available_prefix.setter
    def available_prefix(self, available_prefix):
        r"""Sets the available_prefix of this EngineSpec.

        可用节点规格类型前缀。

        :param available_prefix: The available_prefix of this EngineSpec.
        :type available_prefix: str
        """
        self._available_prefix = available_prefix

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
        if not isinstance(other, EngineSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
