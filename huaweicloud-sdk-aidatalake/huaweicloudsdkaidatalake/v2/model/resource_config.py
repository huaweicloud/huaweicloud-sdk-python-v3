# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cpu': 'int',
        'memory': 'int',
        'npu': 'int',
        'gpu': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'npu': 'npu',
        'gpu': 'gpu'
    }

    def __init__(self, cpu=None, memory=None, npu=None, gpu=None):
        r"""ResourceConfig

        The model defined in huaweicloud sdk

        :param cpu: **参数解释**：CPU数量（单位：毫核）  **约束限制**：不涉及。 **取值范围**：300~100000，包含边界值。 **默认取值**：不涉及。
        :type cpu: int
        :param memory: **参数解释**：内存配置（单位：兆字节）  **约束限制**：不涉及。 **取值范围**：500~204800，包含边界值。 **默认取值**：不涉及。
        :type memory: int
        :param npu: **参数解释**：NPU配置，卡数。  **约束限制**：不涉及。 **取值范围**：1~8，包含边界值。 **默认取值**：不涉及。
        :type npu: int
        :param gpu: **参数解释**：GPU配置，卡数。  **约束限制**：不涉及。 **取值范围**：1~8，包含边界值。 **默认取值**：不涉及。
        :type gpu: int
        """
        
        

        self._cpu = None
        self._memory = None
        self._npu = None
        self._gpu = None
        self.discriminator = None

        self.cpu = cpu
        self.memory = memory
        if npu is not None:
            self.npu = npu
        if gpu is not None:
            self.gpu = gpu

    @property
    def cpu(self):
        r"""Gets the cpu of this ResourceConfig.

        **参数解释**：CPU数量（单位：毫核）  **约束限制**：不涉及。 **取值范围**：300~100000，包含边界值。 **默认取值**：不涉及。

        :return: The cpu of this ResourceConfig.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ResourceConfig.

        **参数解释**：CPU数量（单位：毫核）  **约束限制**：不涉及。 **取值范围**：300~100000，包含边界值。 **默认取值**：不涉及。

        :param cpu: The cpu of this ResourceConfig.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this ResourceConfig.

        **参数解释**：内存配置（单位：兆字节）  **约束限制**：不涉及。 **取值范围**：500~204800，包含边界值。 **默认取值**：不涉及。

        :return: The memory of this ResourceConfig.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ResourceConfig.

        **参数解释**：内存配置（单位：兆字节）  **约束限制**：不涉及。 **取值范围**：500~204800，包含边界值。 **默认取值**：不涉及。

        :param memory: The memory of this ResourceConfig.
        :type memory: int
        """
        self._memory = memory

    @property
    def npu(self):
        r"""Gets the npu of this ResourceConfig.

        **参数解释**：NPU配置，卡数。  **约束限制**：不涉及。 **取值范围**：1~8，包含边界值。 **默认取值**：不涉及。

        :return: The npu of this ResourceConfig.
        :rtype: int
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        r"""Sets the npu of this ResourceConfig.

        **参数解释**：NPU配置，卡数。  **约束限制**：不涉及。 **取值范围**：1~8，包含边界值。 **默认取值**：不涉及。

        :param npu: The npu of this ResourceConfig.
        :type npu: int
        """
        self._npu = npu

    @property
    def gpu(self):
        r"""Gets the gpu of this ResourceConfig.

        **参数解释**：GPU配置，卡数。  **约束限制**：不涉及。 **取值范围**：1~8，包含边界值。 **默认取值**：不涉及。

        :return: The gpu of this ResourceConfig.
        :rtype: int
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this ResourceConfig.

        **参数解释**：GPU配置，卡数。  **约束限制**：不涉及。 **取值范围**：1~8，包含边界值。 **默认取值**：不涉及。

        :param gpu: The gpu of this ResourceConfig.
        :type gpu: int
        """
        self._gpu = gpu

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
        if not isinstance(other, ResourceConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
