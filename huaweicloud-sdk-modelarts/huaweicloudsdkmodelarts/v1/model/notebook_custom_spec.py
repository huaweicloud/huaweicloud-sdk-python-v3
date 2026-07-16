# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotebookCustomSpec:

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
        'cpu': 'float',
        'memory': 'float',
        'gpu_type': 'str',
        'arch': 'str',
        'category': 'str',
        'resource_flavor': 'str'
    }

    attribute_map = {
        'gpu': 'gpu',
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu_type': 'gpu_type',
        'arch': 'arch',
        'category': 'category',
        'resource_flavor': 'resource_flavor'
    }

    def __init__(self, gpu=None, cpu=None, memory=None, gpu_type=None, arch=None, category=None, resource_flavor=None):
        r"""NotebookCustomSpec

        The model defined in huaweicloud sdk

        :param gpu: **参数描述**：实例申请的GPU卡数。 **约束限制**：CPU专属池场景下无此字段，GPU专属池场景必填。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type gpu: float
        :param cpu: **参数描述**：实例申请的CPU核数大小。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：整数部分最多10位，小数部分最多2位，且数值不得小于0.4。 **默认取值**：不涉及。
        :type cpu: float
        :param memory: **参数描述**：实例申请的内存大小。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：必须是整数，整数部分最多10位，且数值不得小于513。 **默认取值**：不涉及。
        :type memory: float
        :param gpu_type: **参数描述**：实例申请的GPU加速卡类型。 **约束限制**：CPU专属池场景下无此字段，GPU专属池场景下必填。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type gpu_type: str
        :param arch: **参数描述**：实例申请的CPU架构。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：枚举类型，取值如下： - X86_64：x86架构 - AARCH64：ARM架构  **默认取值**：不涉及。
        :type arch: str
        :param category: **参数描述**：实例申请的规格类型。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：枚举类型，取值如下： - CPU：CPU规格。 - GPU：GPU规格。  **默认取值**：不涉及。
        :type category: str
        :param resource_flavor: **参数解释**：实例选择的目标资源池节点实例规格。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type resource_flavor: str
        """
        
        

        self._gpu = None
        self._cpu = None
        self._memory = None
        self._gpu_type = None
        self._arch = None
        self._category = None
        self._resource_flavor = None
        self.discriminator = None

        if gpu is not None:
            self.gpu = gpu
        self.cpu = cpu
        self.memory = memory
        if gpu_type is not None:
            self.gpu_type = gpu_type
        if arch is not None:
            self.arch = arch
        if category is not None:
            self.category = category
        if resource_flavor is not None:
            self.resource_flavor = resource_flavor

    @property
    def gpu(self):
        r"""Gets the gpu of this NotebookCustomSpec.

        **参数描述**：实例申请的GPU卡数。 **约束限制**：CPU专属池场景下无此字段，GPU专属池场景必填。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The gpu of this NotebookCustomSpec.
        :rtype: float
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this NotebookCustomSpec.

        **参数描述**：实例申请的GPU卡数。 **约束限制**：CPU专属池场景下无此字段，GPU专属池场景必填。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param gpu: The gpu of this NotebookCustomSpec.
        :type gpu: float
        """
        self._gpu = gpu

    @property
    def cpu(self):
        r"""Gets the cpu of this NotebookCustomSpec.

        **参数描述**：实例申请的CPU核数大小。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：整数部分最多10位，小数部分最多2位，且数值不得小于0.4。 **默认取值**：不涉及。

        :return: The cpu of this NotebookCustomSpec.
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this NotebookCustomSpec.

        **参数描述**：实例申请的CPU核数大小。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：整数部分最多10位，小数部分最多2位，且数值不得小于0.4。 **默认取值**：不涉及。

        :param cpu: The cpu of this NotebookCustomSpec.
        :type cpu: float
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this NotebookCustomSpec.

        **参数描述**：实例申请的内存大小。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：必须是整数，整数部分最多10位，且数值不得小于513。 **默认取值**：不涉及。

        :return: The memory of this NotebookCustomSpec.
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this NotebookCustomSpec.

        **参数描述**：实例申请的内存大小。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：必须是整数，整数部分最多10位，且数值不得小于513。 **默认取值**：不涉及。

        :param memory: The memory of this NotebookCustomSpec.
        :type memory: float
        """
        self._memory = memory

    @property
    def gpu_type(self):
        r"""Gets the gpu_type of this NotebookCustomSpec.

        **参数描述**：实例申请的GPU加速卡类型。 **约束限制**：CPU专属池场景下无此字段，GPU专属池场景下必填。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The gpu_type of this NotebookCustomSpec.
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        r"""Sets the gpu_type of this NotebookCustomSpec.

        **参数描述**：实例申请的GPU加速卡类型。 **约束限制**：CPU专属池场景下无此字段，GPU专属池场景下必填。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param gpu_type: The gpu_type of this NotebookCustomSpec.
        :type gpu_type: str
        """
        self._gpu_type = gpu_type

    @property
    def arch(self):
        r"""Gets the arch of this NotebookCustomSpec.

        **参数描述**：实例申请的CPU架构。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：枚举类型，取值如下： - X86_64：x86架构 - AARCH64：ARM架构  **默认取值**：不涉及。

        :return: The arch of this NotebookCustomSpec.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this NotebookCustomSpec.

        **参数描述**：实例申请的CPU架构。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：枚举类型，取值如下： - X86_64：x86架构 - AARCH64：ARM架构  **默认取值**：不涉及。

        :param arch: The arch of this NotebookCustomSpec.
        :type arch: str
        """
        self._arch = arch

    @property
    def category(self):
        r"""Gets the category of this NotebookCustomSpec.

        **参数描述**：实例申请的规格类型。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：枚举类型，取值如下： - CPU：CPU规格。 - GPU：GPU规格。  **默认取值**：不涉及。

        :return: The category of this NotebookCustomSpec.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this NotebookCustomSpec.

        **参数描述**：实例申请的规格类型。 **约束限制**：CPU/GPU专属池场景下自定义规格必填。 **取值范围**：枚举类型，取值如下： - CPU：CPU规格。 - GPU：GPU规格。  **默认取值**：不涉及。

        :param category: The category of this NotebookCustomSpec.
        :type category: str
        """
        self._category = category

    @property
    def resource_flavor(self):
        r"""Gets the resource_flavor of this NotebookCustomSpec.

        **参数解释**：实例选择的目标资源池节点实例规格。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The resource_flavor of this NotebookCustomSpec.
        :rtype: str
        """
        return self._resource_flavor

    @resource_flavor.setter
    def resource_flavor(self, resource_flavor):
        r"""Sets the resource_flavor of this NotebookCustomSpec.

        **参数解释**：实例选择的目标资源池节点实例规格。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param resource_flavor: The resource_flavor of this NotebookCustomSpec.
        :type resource_flavor: str
        """
        self._resource_flavor = resource_flavor

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
        if not isinstance(other, NotebookCustomSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
