# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayHeadResourceSpec:

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
        'gpu': 'float',
        'npu': 'float'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu': 'gpu',
        'npu': 'npu'
    }

    def __init__(self, cpu=None, memory=None, gpu=None, npu=None):
        r"""RayHeadResourceSpec

        The model defined in huaweicloud sdk

        :param cpu: **参数解释**：CPU核数量，单位为毫核。 **约束限制**：不涉及。 **取值范围**：最小值为1000。 **默认取值**：不涉及。
        :type cpu: int
        :param memory: **参数解释**：单个head内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：最小值为1024。 **默认取值**：不涉及。
        :type memory: int
        :param gpu: **参数解释**：节点的GPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。
        :type gpu: float
        :param npu: **参数解释**：节点的NPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。
        :type npu: float
        """
        
        

        self._cpu = None
        self._memory = None
        self._gpu = None
        self._npu = None
        self.discriminator = None

        self.cpu = cpu
        self.memory = memory
        if gpu is not None:
            self.gpu = gpu
        if npu is not None:
            self.npu = npu

    @property
    def cpu(self):
        r"""Gets the cpu of this RayHeadResourceSpec.

        **参数解释**：CPU核数量，单位为毫核。 **约束限制**：不涉及。 **取值范围**：最小值为1000。 **默认取值**：不涉及。

        :return: The cpu of this RayHeadResourceSpec.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this RayHeadResourceSpec.

        **参数解释**：CPU核数量，单位为毫核。 **约束限制**：不涉及。 **取值范围**：最小值为1000。 **默认取值**：不涉及。

        :param cpu: The cpu of this RayHeadResourceSpec.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this RayHeadResourceSpec.

        **参数解释**：单个head内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：最小值为1024。 **默认取值**：不涉及。

        :return: The memory of this RayHeadResourceSpec.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this RayHeadResourceSpec.

        **参数解释**：单个head内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：最小值为1024。 **默认取值**：不涉及。

        :param memory: The memory of this RayHeadResourceSpec.
        :type memory: int
        """
        self._memory = memory

    @property
    def gpu(self):
        r"""Gets the gpu of this RayHeadResourceSpec.

        **参数解释**：节点的GPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。

        :return: The gpu of this RayHeadResourceSpec.
        :rtype: float
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this RayHeadResourceSpec.

        **参数解释**：节点的GPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。

        :param gpu: The gpu of this RayHeadResourceSpec.
        :type gpu: float
        """
        self._gpu = gpu

    @property
    def npu(self):
        r"""Gets the npu of this RayHeadResourceSpec.

        **参数解释**：节点的NPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。

        :return: The npu of this RayHeadResourceSpec.
        :rtype: float
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        r"""Sets the npu of this RayHeadResourceSpec.

        **参数解释**：节点的NPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。

        :param npu: The npu of this RayHeadResourceSpec.
        :type npu: float
        """
        self._npu = npu

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
        if not isinstance(other, RayHeadResourceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
