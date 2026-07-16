# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Value:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'str',
        'memory': 'str',
        'tnt004': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'tnt004': 'tnt004'
    }

    def __init__(self, cpu=None, memory=None, tnt004=None):
        r"""Value

        The model defined in huaweicloud sdk

        :param cpu: cpu量，即计算资源量。
        :type cpu: str
        :param memory: 内存。
        :type memory: str
        :param tnt004: GPU卡的数量。
        :type tnt004: str
        """
        
        

        self._cpu = None
        self._memory = None
        self._tnt004 = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if tnt004 is not None:
            self.tnt004 = tnt004

    @property
    def cpu(self):
        r"""Gets the cpu of this Value.

        cpu量，即计算资源量。

        :return: The cpu of this Value.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this Value.

        cpu量，即计算资源量。

        :param cpu: The cpu of this Value.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this Value.

        内存。

        :return: The memory of this Value.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this Value.

        内存。

        :param memory: The memory of this Value.
        :type memory: str
        """
        self._memory = memory

    @property
    def tnt004(self):
        r"""Gets the tnt004 of this Value.

        GPU卡的数量。

        :return: The tnt004 of this Value.
        :rtype: str
        """
        return self._tnt004

    @tnt004.setter
    def tnt004(self, tnt004):
        r"""Sets the tnt004 of this Value.

        GPU卡的数量。

        :param tnt004: The tnt004 of this Value.
        :type tnt004: str
        """
        self._tnt004 = tnt004

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Value):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
