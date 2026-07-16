# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomResourceSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gpu': 'float',
        'memory': 'int',
        'cpu': 'float',
        'ascend': 'int',
        'arch': 'str'
    }

    attribute_map = {
        'gpu': 'gpu',
        'memory': 'memory',
        'cpu': 'cpu',
        'ascend': 'ascend',
        'arch': 'arch'
    }

    def __init__(self, gpu=None, memory=None, cpu=None, ascend=None, arch=None):
        r"""CustomResourceSpec

        The model defined in huaweicloud sdk

        :param gpu: **参数解释：** GPU个数。 **约束限制：** 不涉及。 **取值范围：** 支持配置小数，输入值不能小于0（最多支持2位小数，小数点后第3位做四舍五入处理）。 **默认取值：** 不涉及。
        :type gpu: float
        :param memory: **参数解释：** 内存，单位为MB。 **约束限制：** 不涉及。 **取值范围：** 仅支持整数。 **默认取值：** 不涉及。
        :type memory: int
        :param cpu: **参数解释：** CPU核数。 **约束限制：** 不涉及。 **取值范围：** 支持配置小数，输入值不能小于0.01（最多支持2位小数，小数点后第3位做四舍五入处理）。 **默认取值：** 不涉及。
        :type cpu: float
        :param ascend: **参数解释：** Ascend芯片个数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type ascend: int
        :param arch: **参数解释：** 架构类型。 **约束限制：** 不涉及。 **取值范围：** 枚举值：x86 | arm64。 **默认取值：** 不涉及。
        :type arch: str
        """
        
        

        self._gpu = None
        self._memory = None
        self._cpu = None
        self._ascend = None
        self._arch = None
        self.discriminator = None

        if gpu is not None:
            self.gpu = gpu
        if memory is not None:
            self.memory = memory
        if cpu is not None:
            self.cpu = cpu
        if ascend is not None:
            self.ascend = ascend
        if arch is not None:
            self.arch = arch

    @property
    def gpu(self):
        r"""Gets the gpu of this CustomResourceSpec.

        **参数解释：** GPU个数。 **约束限制：** 不涉及。 **取值范围：** 支持配置小数，输入值不能小于0（最多支持2位小数，小数点后第3位做四舍五入处理）。 **默认取值：** 不涉及。

        :return: The gpu of this CustomResourceSpec.
        :rtype: float
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this CustomResourceSpec.

        **参数解释：** GPU个数。 **约束限制：** 不涉及。 **取值范围：** 支持配置小数，输入值不能小于0（最多支持2位小数，小数点后第3位做四舍五入处理）。 **默认取值：** 不涉及。

        :param gpu: The gpu of this CustomResourceSpec.
        :type gpu: float
        """
        self._gpu = gpu

    @property
    def memory(self):
        r"""Gets the memory of this CustomResourceSpec.

        **参数解释：** 内存，单位为MB。 **约束限制：** 不涉及。 **取值范围：** 仅支持整数。 **默认取值：** 不涉及。

        :return: The memory of this CustomResourceSpec.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this CustomResourceSpec.

        **参数解释：** 内存，单位为MB。 **约束限制：** 不涉及。 **取值范围：** 仅支持整数。 **默认取值：** 不涉及。

        :param memory: The memory of this CustomResourceSpec.
        :type memory: int
        """
        self._memory = memory

    @property
    def cpu(self):
        r"""Gets the cpu of this CustomResourceSpec.

        **参数解释：** CPU核数。 **约束限制：** 不涉及。 **取值范围：** 支持配置小数，输入值不能小于0.01（最多支持2位小数，小数点后第3位做四舍五入处理）。 **默认取值：** 不涉及。

        :return: The cpu of this CustomResourceSpec.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this CustomResourceSpec.

        **参数解释：** CPU核数。 **约束限制：** 不涉及。 **取值范围：** 支持配置小数，输入值不能小于0.01（最多支持2位小数，小数点后第3位做四舍五入处理）。 **默认取值：** 不涉及。

        :param cpu: The cpu of this CustomResourceSpec.
        :type cpu: float
        """
        self._cpu = cpu

    @property
    def ascend(self):
        r"""Gets the ascend of this CustomResourceSpec.

        **参数解释：** Ascend芯片个数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The ascend of this CustomResourceSpec.
        :rtype: int
        """
        return self._ascend

    @ascend.setter
    def ascend(self, ascend):
        r"""Sets the ascend of this CustomResourceSpec.

        **参数解释：** Ascend芯片个数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param ascend: The ascend of this CustomResourceSpec.
        :type ascend: int
        """
        self._ascend = ascend

    @property
    def arch(self):
        r"""Gets the arch of this CustomResourceSpec.

        **参数解释：** 架构类型。 **约束限制：** 不涉及。 **取值范围：** 枚举值：x86 | arm64。 **默认取值：** 不涉及。

        :return: The arch of this CustomResourceSpec.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this CustomResourceSpec.

        **参数解释：** 架构类型。 **约束限制：** 不涉及。 **取值范围：** 枚举值：x86 | arm64。 **默认取值：** 不涉及。

        :param arch: The arch of this CustomResourceSpec.
        :type arch: str
        """
        self._arch = arch

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
        if not isinstance(other, CustomResourceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
