# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkerGroupConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'spec_code': 'str',
        'cpu': 'int',
        'memory': 'int',
        'gpu': 'float',
        'npu': 'float',
        'image': 'ImageVersionInfo'
    }

    attribute_map = {
        'name': 'name',
        'spec_code': 'spec_code',
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu': 'gpu',
        'npu': 'npu',
        'image': 'image'
    }

    def __init__(self, name=None, spec_code=None, cpu=None, memory=None, gpu=None, npu=None, image=None):
        r"""WorkerGroupConfig

        The model defined in huaweicloud sdk

        :param name: **参数解释**：工作组名称。 **约束限制**：已有工作组名称不支持修改，需和当前工作组名称保持一致；新增工作组该字段必填。 **取值范围**：长度为1~63个字符，支持字母、数字和中划线的组合。 **默认取值**：不涉及。
        :type name: str
        :param spec_code: **参数解释**：节点规格。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点及连字符，长度为1~64个字符。 **默认取值**：不涉及。
        :type spec_code: str
        :param cpu: **参数解释**：通算CPU大小，单位毫核。 **约束限制**：不涉及。 **取值范围**：0~2147483647。 **默认取值**：不涉及。
        :type cpu: int
        :param memory: **参数解释**：通算内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：0~2147483647。 **默认取值**：不涉及。
        :type memory: int
        :param gpu: **参数解释**：GPU卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~2147483647。 **默认取值**：不涉及。
        :type gpu: float
        :param npu: **参数解释**：NPU卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~2147483647。 **默认取值**：不涉及。
        :type npu: float
        :param image: 
        :type image: :class:`huaweicloudsdkaidatalake.v2.ImageVersionInfo`
        """
        
        

        self._name = None
        self._spec_code = None
        self._cpu = None
        self._memory = None
        self._gpu = None
        self._npu = None
        self._image = None
        self.discriminator = None

        self.name = name
        self.spec_code = spec_code
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if gpu is not None:
            self.gpu = gpu
        if npu is not None:
            self.npu = npu
        if image is not None:
            self.image = image

    @property
    def name(self):
        r"""Gets the name of this WorkerGroupConfig.

        **参数解释**：工作组名称。 **约束限制**：已有工作组名称不支持修改，需和当前工作组名称保持一致；新增工作组该字段必填。 **取值范围**：长度为1~63个字符，支持字母、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The name of this WorkerGroupConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkerGroupConfig.

        **参数解释**：工作组名称。 **约束限制**：已有工作组名称不支持修改，需和当前工作组名称保持一致；新增工作组该字段必填。 **取值范围**：长度为1~63个字符，支持字母、数字和中划线的组合。 **默认取值**：不涉及。

        :param name: The name of this WorkerGroupConfig.
        :type name: str
        """
        self._name = name

    @property
    def spec_code(self):
        r"""Gets the spec_code of this WorkerGroupConfig.

        **参数解释**：节点规格。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点及连字符，长度为1~64个字符。 **默认取值**：不涉及。

        :return: The spec_code of this WorkerGroupConfig.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this WorkerGroupConfig.

        **参数解释**：节点规格。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点及连字符，长度为1~64个字符。 **默认取值**：不涉及。

        :param spec_code: The spec_code of this WorkerGroupConfig.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def cpu(self):
        r"""Gets the cpu of this WorkerGroupConfig.

        **参数解释**：通算CPU大小，单位毫核。 **约束限制**：不涉及。 **取值范围**：0~2147483647。 **默认取值**：不涉及。

        :return: The cpu of this WorkerGroupConfig.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this WorkerGroupConfig.

        **参数解释**：通算CPU大小，单位毫核。 **约束限制**：不涉及。 **取值范围**：0~2147483647。 **默认取值**：不涉及。

        :param cpu: The cpu of this WorkerGroupConfig.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this WorkerGroupConfig.

        **参数解释**：通算内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：0~2147483647。 **默认取值**：不涉及。

        :return: The memory of this WorkerGroupConfig.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this WorkerGroupConfig.

        **参数解释**：通算内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：0~2147483647。 **默认取值**：不涉及。

        :param memory: The memory of this WorkerGroupConfig.
        :type memory: int
        """
        self._memory = memory

    @property
    def gpu(self):
        r"""Gets the gpu of this WorkerGroupConfig.

        **参数解释**：GPU卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~2147483647。 **默认取值**：不涉及。

        :return: The gpu of this WorkerGroupConfig.
        :rtype: float
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this WorkerGroupConfig.

        **参数解释**：GPU卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~2147483647。 **默认取值**：不涉及。

        :param gpu: The gpu of this WorkerGroupConfig.
        :type gpu: float
        """
        self._gpu = gpu

    @property
    def npu(self):
        r"""Gets the npu of this WorkerGroupConfig.

        **参数解释**：NPU卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~2147483647。 **默认取值**：不涉及。

        :return: The npu of this WorkerGroupConfig.
        :rtype: float
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        r"""Sets the npu of this WorkerGroupConfig.

        **参数解释**：NPU卡数量。 **约束限制**：暂时只支持整数。 **取值范围**：0~2147483647。 **默认取值**：不涉及。

        :param npu: The npu of this WorkerGroupConfig.
        :type npu: float
        """
        self._npu = npu

    @property
    def image(self):
        r"""Gets the image of this WorkerGroupConfig.

        :return: The image of this WorkerGroupConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ImageVersionInfo`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this WorkerGroupConfig.

        :param image: The image of this WorkerGroupConfig.
        :type image: :class:`huaweicloudsdkaidatalake.v2.ImageVersionInfo`
        """
        self._image = image

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
        if not isinstance(other, WorkerGroupConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
