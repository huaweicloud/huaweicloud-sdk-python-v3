# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CpuOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hw_cpu_threads': 'int'
    }

    attribute_map = {
        'hw_cpu_threads': 'hw_cpu_threads'
    }

    def __init__(self, hw_cpu_threads=None):
        r"""CpuOptions

        The model defined in huaweicloud sdk

        :param hw_cpu_threads: 是否关闭实例超线程，1是关闭，2是开启
        :type hw_cpu_threads: int
        """
        
        

        self._hw_cpu_threads = None
        self.discriminator = None

        if hw_cpu_threads is not None:
            self.hw_cpu_threads = hw_cpu_threads

    @property
    def hw_cpu_threads(self):
        r"""Gets the hw_cpu_threads of this CpuOptions.

        是否关闭实例超线程，1是关闭，2是开启

        :return: The hw_cpu_threads of this CpuOptions.
        :rtype: int
        """
        return self._hw_cpu_threads

    @hw_cpu_threads.setter
    def hw_cpu_threads(self, hw_cpu_threads):
        r"""Sets the hw_cpu_threads of this CpuOptions.

        是否关闭实例超线程，1是关闭，2是开启

        :param hw_cpu_threads: The hw_cpu_threads of this CpuOptions.
        :type hw_cpu_threads: int
        """
        self._hw_cpu_threads = hw_cpu_threads

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
        if not isinstance(other, CpuOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
