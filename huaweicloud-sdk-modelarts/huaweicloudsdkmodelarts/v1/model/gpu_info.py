# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GPUInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gpu': 'int',
        'gpu_memory': 'str',
        'type': 'str'
    }

    attribute_map = {
        'gpu': 'gpu',
        'gpu_memory': 'gpu_memory',
        'type': 'type'
    }

    def __init__(self, gpu=None, gpu_memory=None, type=None):
        r"""GPUInfo

        The model defined in huaweicloud sdk

        :param gpu: **参数解释**：GPU卡数。 **取值范围**：不涉及。
        :type gpu: int
        :param gpu_memory: **参数解释**：GPU内存。 **取值范围**：不涉及。
        :type gpu_memory: str
        :param type: **参数解释**：GPU类型。 **取值范围**：不涉及。
        :type type: str
        """
        
        

        self._gpu = None
        self._gpu_memory = None
        self._type = None
        self.discriminator = None

        if gpu is not None:
            self.gpu = gpu
        if gpu_memory is not None:
            self.gpu_memory = gpu_memory
        if type is not None:
            self.type = type

    @property
    def gpu(self):
        r"""Gets the gpu of this GPUInfo.

        **参数解释**：GPU卡数。 **取值范围**：不涉及。

        :return: The gpu of this GPUInfo.
        :rtype: int
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this GPUInfo.

        **参数解释**：GPU卡数。 **取值范围**：不涉及。

        :param gpu: The gpu of this GPUInfo.
        :type gpu: int
        """
        self._gpu = gpu

    @property
    def gpu_memory(self):
        r"""Gets the gpu_memory of this GPUInfo.

        **参数解释**：GPU内存。 **取值范围**：不涉及。

        :return: The gpu_memory of this GPUInfo.
        :rtype: str
        """
        return self._gpu_memory

    @gpu_memory.setter
    def gpu_memory(self, gpu_memory):
        r"""Sets the gpu_memory of this GPUInfo.

        **参数解释**：GPU内存。 **取值范围**：不涉及。

        :param gpu_memory: The gpu_memory of this GPUInfo.
        :type gpu_memory: str
        """
        self._gpu_memory = gpu_memory

    @property
    def type(self):
        r"""Gets the type of this GPUInfo.

        **参数解释**：GPU类型。 **取值范围**：不涉及。

        :return: The type of this GPUInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GPUInfo.

        **参数解释**：GPU类型。 **取值范围**：不涉及。

        :param type: The type of this GPUInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, GPUInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
