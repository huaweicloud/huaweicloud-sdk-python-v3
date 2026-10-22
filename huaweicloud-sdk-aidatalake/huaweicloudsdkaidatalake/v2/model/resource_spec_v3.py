# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceSpecV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'cpu': 'int',
        'memory': 'int',
        'npu': 'float',
        'gpu': 'float'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'cpu': 'cpu',
        'memory': 'memory',
        'npu': 'npu',
        'gpu': 'gpu'
    }

    def __init__(self, spec_code=None, cpu=None, memory=None, npu=None, gpu=None):
        r"""ResourceSpecV3

        The model defined in huaweicloud sdk

        :param spec_code: **参数解释**：资源规格。 **取值范围**：不涉及。 
        :type spec_code: str
        :param cpu: **参数解释**：CPU核数量，单位为毫核。 **约束限制**：不涉及。 **取值范围**：0~1000000。 **默认取值**：0。
        :type cpu: int
        :param memory: **参数解释**：内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：0~10000000。 **默认取值**：0。
        :type memory: int
        :param npu: **参数解释**：昇腾卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~100。 **默认取值**：0。
        :type npu: float
        :param gpu: **参数解释**：GPU卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~100。 **默认取值**：0。
        :type gpu: float
        """
        
        

        self._spec_code = None
        self._cpu = None
        self._memory = None
        self._npu = None
        self._gpu = None
        self.discriminator = None

        self.spec_code = spec_code
        self.cpu = cpu
        self.memory = memory
        if npu is not None:
            self.npu = npu
        if gpu is not None:
            self.gpu = gpu

    @property
    def spec_code(self):
        r"""Gets the spec_code of this ResourceSpecV3.

        **参数解释**：资源规格。 **取值范围**：不涉及。 

        :return: The spec_code of this ResourceSpecV3.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this ResourceSpecV3.

        **参数解释**：资源规格。 **取值范围**：不涉及。 

        :param spec_code: The spec_code of this ResourceSpecV3.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def cpu(self):
        r"""Gets the cpu of this ResourceSpecV3.

        **参数解释**：CPU核数量，单位为毫核。 **约束限制**：不涉及。 **取值范围**：0~1000000。 **默认取值**：0。

        :return: The cpu of this ResourceSpecV3.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ResourceSpecV3.

        **参数解释**：CPU核数量，单位为毫核。 **约束限制**：不涉及。 **取值范围**：0~1000000。 **默认取值**：0。

        :param cpu: The cpu of this ResourceSpecV3.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this ResourceSpecV3.

        **参数解释**：内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：0~10000000。 **默认取值**：0。

        :return: The memory of this ResourceSpecV3.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ResourceSpecV3.

        **参数解释**：内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：0~10000000。 **默认取值**：0。

        :param memory: The memory of this ResourceSpecV3.
        :type memory: int
        """
        self._memory = memory

    @property
    def npu(self):
        r"""Gets the npu of this ResourceSpecV3.

        **参数解释**：昇腾卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~100。 **默认取值**：0。

        :return: The npu of this ResourceSpecV3.
        :rtype: float
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        r"""Sets the npu of this ResourceSpecV3.

        **参数解释**：昇腾卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~100。 **默认取值**：0。

        :param npu: The npu of this ResourceSpecV3.
        :type npu: float
        """
        self._npu = npu

    @property
    def gpu(self):
        r"""Gets the gpu of this ResourceSpecV3.

        **参数解释**：GPU卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~100。 **默认取值**：0。

        :return: The gpu of this ResourceSpecV3.
        :rtype: float
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this ResourceSpecV3.

        **参数解释**：GPU卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~100。 **默认取值**：0。

        :param gpu: The gpu of this ResourceSpecV3.
        :type gpu: float
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
        if not isinstance(other, ResourceSpecV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
