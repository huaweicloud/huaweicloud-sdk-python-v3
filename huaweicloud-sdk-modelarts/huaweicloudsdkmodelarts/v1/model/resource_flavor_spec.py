# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceFlavorSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'cpu_arch': 'str',
        'cpu': 'str',
        'memory': 'str',
        'gpu': 'ResourceFlavorSpecGpu',
        'npu': 'ResourceFlavorSpecNpu',
        'data_volume': 'list[ResourceFlavorSpecDataVolume]',
        'billing_modes': 'list[int]',
        'billing_code': 'str',
        'job_flavors': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'cpu_arch': 'cpuArch',
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu': 'gpu',
        'npu': 'npu',
        'data_volume': 'dataVolume',
        'billing_modes': 'billingModes',
        'billing_code': 'billingCode',
        'job_flavors': 'jobFlavors'
    }

    def __init__(self, type=None, cpu_arch=None, cpu=None, memory=None, gpu=None, npu=None, data_volume=None, billing_modes=None, billing_code=None, job_flavors=None):
        r"""ResourceFlavorSpec

        The model defined in huaweicloud sdk

        :param type: **参数解释**：资源规格类型。 **取值范围**：可选值如下： - Dedicate：物理资源规格。物理资源规格可以创建节点资源。 [- Logical：逻辑资源规格。](tag:hcso)
        :type type: str
        :param cpu_arch: **参数解释**：资源规格实例的计算架构。 **取值范围**：可选值如下： - x86：x86架构。 - arm64：ARM架构。
        :type cpu_arch: str
        :param cpu: **参数解释**：资源规格实例的CPU核心数量。 **取值范围**：不涉及。
        :type cpu: str
        :param memory: **参数解释**：资源规格实例的内存大小。以Gi为单位。 **取值范围**：不涉及。
        :type memory: str
        :param gpu: 
        :type gpu: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorSpecGpu`
        :param npu: 
        :type npu: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorSpecNpu`
        :param data_volume: **参数解释**：资源规格实例的存储资源信息。
        :type data_volume: list[:class:`huaweicloudsdkmodelarts.v1.ResourceFlavorSpecDataVolume`]
        :param billing_modes: **参数解释**：资源规格支持的计费模式。
        :type billing_modes: list[int]
        :param billing_code: **参数解释**：资源规格计费码。 **取值范围**：不涉及。
        :type billing_code: str
        :param job_flavors: **参数解释**：资源规格支持的作业类型列表。
        :type job_flavors: list[str]
        """
        
        

        self._type = None
        self._cpu_arch = None
        self._cpu = None
        self._memory = None
        self._gpu = None
        self._npu = None
        self._data_volume = None
        self._billing_modes = None
        self._billing_code = None
        self._job_flavors = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if cpu_arch is not None:
            self.cpu_arch = cpu_arch
        if cpu is not None:
            self.cpu = cpu
        if memory is not None:
            self.memory = memory
        if gpu is not None:
            self.gpu = gpu
        if npu is not None:
            self.npu = npu
        if data_volume is not None:
            self.data_volume = data_volume
        if billing_modes is not None:
            self.billing_modes = billing_modes
        if billing_code is not None:
            self.billing_code = billing_code
        if job_flavors is not None:
            self.job_flavors = job_flavors

    @property
    def type(self):
        r"""Gets the type of this ResourceFlavorSpec.

        **参数解释**：资源规格类型。 **取值范围**：可选值如下： - Dedicate：物理资源规格。物理资源规格可以创建节点资源。 [- Logical：逻辑资源规格。](tag:hcso)

        :return: The type of this ResourceFlavorSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceFlavorSpec.

        **参数解释**：资源规格类型。 **取值范围**：可选值如下： - Dedicate：物理资源规格。物理资源规格可以创建节点资源。 [- Logical：逻辑资源规格。](tag:hcso)

        :param type: The type of this ResourceFlavorSpec.
        :type type: str
        """
        self._type = type

    @property
    def cpu_arch(self):
        r"""Gets the cpu_arch of this ResourceFlavorSpec.

        **参数解释**：资源规格实例的计算架构。 **取值范围**：可选值如下： - x86：x86架构。 - arm64：ARM架构。

        :return: The cpu_arch of this ResourceFlavorSpec.
        :rtype: str
        """
        return self._cpu_arch

    @cpu_arch.setter
    def cpu_arch(self, cpu_arch):
        r"""Sets the cpu_arch of this ResourceFlavorSpec.

        **参数解释**：资源规格实例的计算架构。 **取值范围**：可选值如下： - x86：x86架构。 - arm64：ARM架构。

        :param cpu_arch: The cpu_arch of this ResourceFlavorSpec.
        :type cpu_arch: str
        """
        self._cpu_arch = cpu_arch

    @property
    def cpu(self):
        r"""Gets the cpu of this ResourceFlavorSpec.

        **参数解释**：资源规格实例的CPU核心数量。 **取值范围**：不涉及。

        :return: The cpu of this ResourceFlavorSpec.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ResourceFlavorSpec.

        **参数解释**：资源规格实例的CPU核心数量。 **取值范围**：不涉及。

        :param cpu: The cpu of this ResourceFlavorSpec.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this ResourceFlavorSpec.

        **参数解释**：资源规格实例的内存大小。以Gi为单位。 **取值范围**：不涉及。

        :return: The memory of this ResourceFlavorSpec.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ResourceFlavorSpec.

        **参数解释**：资源规格实例的内存大小。以Gi为单位。 **取值范围**：不涉及。

        :param memory: The memory of this ResourceFlavorSpec.
        :type memory: str
        """
        self._memory = memory

    @property
    def gpu(self):
        r"""Gets the gpu of this ResourceFlavorSpec.

        :return: The gpu of this ResourceFlavorSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorSpecGpu`
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this ResourceFlavorSpec.

        :param gpu: The gpu of this ResourceFlavorSpec.
        :type gpu: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorSpecGpu`
        """
        self._gpu = gpu

    @property
    def npu(self):
        r"""Gets the npu of this ResourceFlavorSpec.

        :return: The npu of this ResourceFlavorSpec.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorSpecNpu`
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        r"""Sets the npu of this ResourceFlavorSpec.

        :param npu: The npu of this ResourceFlavorSpec.
        :type npu: :class:`huaweicloudsdkmodelarts.v1.ResourceFlavorSpecNpu`
        """
        self._npu = npu

    @property
    def data_volume(self):
        r"""Gets the data_volume of this ResourceFlavorSpec.

        **参数解释**：资源规格实例的存储资源信息。

        :return: The data_volume of this ResourceFlavorSpec.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ResourceFlavorSpecDataVolume`]
        """
        return self._data_volume

    @data_volume.setter
    def data_volume(self, data_volume):
        r"""Sets the data_volume of this ResourceFlavorSpec.

        **参数解释**：资源规格实例的存储资源信息。

        :param data_volume: The data_volume of this ResourceFlavorSpec.
        :type data_volume: list[:class:`huaweicloudsdkmodelarts.v1.ResourceFlavorSpecDataVolume`]
        """
        self._data_volume = data_volume

    @property
    def billing_modes(self):
        r"""Gets the billing_modes of this ResourceFlavorSpec.

        **参数解释**：资源规格支持的计费模式。

        :return: The billing_modes of this ResourceFlavorSpec.
        :rtype: list[int]
        """
        return self._billing_modes

    @billing_modes.setter
    def billing_modes(self, billing_modes):
        r"""Sets the billing_modes of this ResourceFlavorSpec.

        **参数解释**：资源规格支持的计费模式。

        :param billing_modes: The billing_modes of this ResourceFlavorSpec.
        :type billing_modes: list[int]
        """
        self._billing_modes = billing_modes

    @property
    def billing_code(self):
        r"""Gets the billing_code of this ResourceFlavorSpec.

        **参数解释**：资源规格计费码。 **取值范围**：不涉及。

        :return: The billing_code of this ResourceFlavorSpec.
        :rtype: str
        """
        return self._billing_code

    @billing_code.setter
    def billing_code(self, billing_code):
        r"""Sets the billing_code of this ResourceFlavorSpec.

        **参数解释**：资源规格计费码。 **取值范围**：不涉及。

        :param billing_code: The billing_code of this ResourceFlavorSpec.
        :type billing_code: str
        """
        self._billing_code = billing_code

    @property
    def job_flavors(self):
        r"""Gets the job_flavors of this ResourceFlavorSpec.

        **参数解释**：资源规格支持的作业类型列表。

        :return: The job_flavors of this ResourceFlavorSpec.
        :rtype: list[str]
        """
        return self._job_flavors

    @job_flavors.setter
    def job_flavors(self, job_flavors):
        r"""Sets the job_flavors of this ResourceFlavorSpec.

        **参数解释**：资源规格支持的作业类型列表。

        :param job_flavors: The job_flavors of this ResourceFlavorSpec.
        :type job_flavors: list[str]
        """
        self._job_flavors = job_flavors

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
        if not isinstance(other, ResourceFlavorSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
