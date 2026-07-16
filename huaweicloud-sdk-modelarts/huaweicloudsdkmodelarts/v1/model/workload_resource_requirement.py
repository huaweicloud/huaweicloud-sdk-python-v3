# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkloadResourceRequirement:

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
        'nvidia_com_gpu': 'str',
        'huawei_com_ascend_310': 'str',
        'huawei_com_ascend_1980': 'str'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'nvidia_com_gpu': 'nvidia.com/gpu',
        'huawei_com_ascend_310': 'huawei.com/ascend-310',
        'huawei_com_ascend_1980': 'huawei.com/ascend-1980'
    }

    def __init__(self, cpu=None, memory=None, nvidia_com_gpu=None, huawei_com_ascend_310=None, huawei_com_ascend_1980=None):
        r"""WorkloadResourceRequirement

        The model defined in huaweicloud sdk

        :param cpu: **参数解释**：作业的运行使用的CPU资源量。 **取值范围**：不涉及。
        :type cpu: str
        :param memory: **参数解释**：作业的运行使用的内存资源量。 **取值范围**：不涉及。
        :type memory: str
        :param nvidia_com_gpu: **参数解释**：作业的运行使用的GPU资源量。 **取值范围**：不涉及。
        :type nvidia_com_gpu: str
        :param huawei_com_ascend_310: **参数解释**：作业的运行使用的snt3类型NPU资源量。 **取值范围**：不涉及
        :type huawei_com_ascend_310: str
        :param huawei_com_ascend_1980: **参数解释**：作业的运行使用的snt9类型NPU资源量。 **取值范围**：不涉及。
        :type huawei_com_ascend_1980: str
        """
        
        

        self._cpu = None
        self._memory = None
        self._nvidia_com_gpu = None
        self._huawei_com_ascend_310 = None
        self._huawei_com_ascend_1980 = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if nvidia_com_gpu is not None:
            self.nvidia_com_gpu = nvidia_com_gpu
        if huawei_com_ascend_310 is not None:
            self.huawei_com_ascend_310 = huawei_com_ascend_310
        if huawei_com_ascend_1980 is not None:
            self.huawei_com_ascend_1980 = huawei_com_ascend_1980

    @property
    def cpu(self):
        r"""Gets the cpu of this WorkloadResourceRequirement.

        **参数解释**：作业的运行使用的CPU资源量。 **取值范围**：不涉及。

        :return: The cpu of this WorkloadResourceRequirement.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this WorkloadResourceRequirement.

        **参数解释**：作业的运行使用的CPU资源量。 **取值范围**：不涉及。

        :param cpu: The cpu of this WorkloadResourceRequirement.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this WorkloadResourceRequirement.

        **参数解释**：作业的运行使用的内存资源量。 **取值范围**：不涉及。

        :return: The memory of this WorkloadResourceRequirement.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this WorkloadResourceRequirement.

        **参数解释**：作业的运行使用的内存资源量。 **取值范围**：不涉及。

        :param memory: The memory of this WorkloadResourceRequirement.
        :type memory: str
        """
        self._memory = memory

    @property
    def nvidia_com_gpu(self):
        r"""Gets the nvidia_com_gpu of this WorkloadResourceRequirement.

        **参数解释**：作业的运行使用的GPU资源量。 **取值范围**：不涉及。

        :return: The nvidia_com_gpu of this WorkloadResourceRequirement.
        :rtype: str
        """
        return self._nvidia_com_gpu

    @nvidia_com_gpu.setter
    def nvidia_com_gpu(self, nvidia_com_gpu):
        r"""Sets the nvidia_com_gpu of this WorkloadResourceRequirement.

        **参数解释**：作业的运行使用的GPU资源量。 **取值范围**：不涉及。

        :param nvidia_com_gpu: The nvidia_com_gpu of this WorkloadResourceRequirement.
        :type nvidia_com_gpu: str
        """
        self._nvidia_com_gpu = nvidia_com_gpu

    @property
    def huawei_com_ascend_310(self):
        r"""Gets the huawei_com_ascend_310 of this WorkloadResourceRequirement.

        **参数解释**：作业的运行使用的snt3类型NPU资源量。 **取值范围**：不涉及

        :return: The huawei_com_ascend_310 of this WorkloadResourceRequirement.
        :rtype: str
        """
        return self._huawei_com_ascend_310

    @huawei_com_ascend_310.setter
    def huawei_com_ascend_310(self, huawei_com_ascend_310):
        r"""Sets the huawei_com_ascend_310 of this WorkloadResourceRequirement.

        **参数解释**：作业的运行使用的snt3类型NPU资源量。 **取值范围**：不涉及

        :param huawei_com_ascend_310: The huawei_com_ascend_310 of this WorkloadResourceRequirement.
        :type huawei_com_ascend_310: str
        """
        self._huawei_com_ascend_310 = huawei_com_ascend_310

    @property
    def huawei_com_ascend_1980(self):
        r"""Gets the huawei_com_ascend_1980 of this WorkloadResourceRequirement.

        **参数解释**：作业的运行使用的snt9类型NPU资源量。 **取值范围**：不涉及。

        :return: The huawei_com_ascend_1980 of this WorkloadResourceRequirement.
        :rtype: str
        """
        return self._huawei_com_ascend_1980

    @huawei_com_ascend_1980.setter
    def huawei_com_ascend_1980(self, huawei_com_ascend_1980):
        r"""Sets the huawei_com_ascend_1980 of this WorkloadResourceRequirement.

        **参数解释**：作业的运行使用的snt9类型NPU资源量。 **取值范围**：不涉及。

        :param huawei_com_ascend_1980: The huawei_com_ascend_1980 of this WorkloadResourceRequirement.
        :type huawei_com_ascend_1980: str
        """
        self._huawei_com_ascend_1980 = huawei_com_ascend_1980

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
        if not isinstance(other, WorkloadResourceRequirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
