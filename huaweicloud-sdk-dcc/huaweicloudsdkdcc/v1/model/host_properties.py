# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu_cores': 'int',
        'memory_mb': 'int',
        'cpu_speed': 'str'
    }

    attribute_map = {
        'cpu_cores': 'cpu_cores',
        'memory_mb': 'memory_mb',
        'cpu_speed': 'cpu_speed'
    }

    def __init__(self, cpu_cores=None, memory_mb=None, cpu_speed=None):
        r"""HostProperties

        The model defined in huaweicloud sdk

        :param cpu_cores: 核数。
        :type cpu_cores: int
        :param memory_mb: 内存。
        :type memory_mb: int
        :param cpu_speed: 主频。
        :type cpu_speed: str
        """
        
        

        self._cpu_cores = None
        self._memory_mb = None
        self._cpu_speed = None
        self.discriminator = None

        if cpu_cores is not None:
            self.cpu_cores = cpu_cores
        if memory_mb is not None:
            self.memory_mb = memory_mb
        if cpu_speed is not None:
            self.cpu_speed = cpu_speed

    @property
    def cpu_cores(self):
        r"""Gets the cpu_cores of this HostProperties.

        核数。

        :return: The cpu_cores of this HostProperties.
        :rtype: int
        """
        return self._cpu_cores

    @cpu_cores.setter
    def cpu_cores(self, cpu_cores):
        r"""Sets the cpu_cores of this HostProperties.

        核数。

        :param cpu_cores: The cpu_cores of this HostProperties.
        :type cpu_cores: int
        """
        self._cpu_cores = cpu_cores

    @property
    def memory_mb(self):
        r"""Gets the memory_mb of this HostProperties.

        内存。

        :return: The memory_mb of this HostProperties.
        :rtype: int
        """
        return self._memory_mb

    @memory_mb.setter
    def memory_mb(self, memory_mb):
        r"""Sets the memory_mb of this HostProperties.

        内存。

        :param memory_mb: The memory_mb of this HostProperties.
        :type memory_mb: int
        """
        self._memory_mb = memory_mb

    @property
    def cpu_speed(self):
        r"""Gets the cpu_speed of this HostProperties.

        主频。

        :return: The cpu_speed of this HostProperties.
        :rtype: str
        """
        return self._cpu_speed

    @cpu_speed.setter
    def cpu_speed(self, cpu_speed):
        r"""Sets the cpu_speed of this HostProperties.

        主频。

        :param cpu_speed: The cpu_speed of this HostProperties.
        :type cpu_speed: str
        """
        self._cpu_speed = cpu_speed

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
        if not isinstance(other, HostProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
