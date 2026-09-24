# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayWorkerResourceSpec:

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
        'npu': 'float',
        'worker_replicas': 'int',
        'enable_autoscaling': 'bool',
        'worker_min_replicas': 'int',
        'worker_max_replicas': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'memory': 'memory',
        'gpu': 'gpu',
        'npu': 'npu',
        'worker_replicas': 'worker_replicas',
        'enable_autoscaling': 'enable_autoscaling',
        'worker_min_replicas': 'worker_min_replicas',
        'worker_max_replicas': 'worker_max_replicas'
    }

    def __init__(self, cpu=None, memory=None, gpu=None, npu=None, worker_replicas=None, enable_autoscaling=None, worker_min_replicas=None, worker_max_replicas=None):
        r"""RayWorkerResourceSpec

        The model defined in huaweicloud sdk

        :param cpu: **参数解释**：CPU核数量，单位为毫核。 **约束限制**：不涉及。 **取值范围**：最小值为1000。 **默认取值**：不涉及。
        :type cpu: int
        :param memory: **参数解释**：内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：最小值为1024。 **默认取值**：不涉及。
        :type memory: int
        :param gpu: **参数解释**：节点的GPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。
        :type gpu: float
        :param npu: **参数解释**：节点的NPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。
        :type npu: float
        :param worker_replicas: **参数解释**：Worker副本数量。 **约束限制**：不涉及。 **取值范围**：1~64。 **默认取值**：不涉及。
        :type worker_replicas: int
        :param enable_autoscaling: **参数解释**：是否开启worker节点的弹性伸缩。 **约束限制**：不涉及。 **取值范围**：可选值有：   - true：开启弹性伸缩。取该值时worker_min_replicas和worker_max_replicas必须设置。   - false：不开启弹性伸缩。取该值时worker_replicas必须设置。 **默认取值**：false。
        :type enable_autoscaling: bool
        :param worker_min_replicas: **参数解释**：Worker最小副本数量。 **约束限制**：不涉及。 **取值范围**：0~64。 **默认取值**：不涉及。
        :type worker_min_replicas: int
        :param worker_max_replicas: **参数解释**：Worker最大副本数量。 **约束限制**：不涉及。 **取值范围**：1~64。 **默认取值**：不涉及。
        :type worker_max_replicas: int
        """
        
        

        self._cpu = None
        self._memory = None
        self._gpu = None
        self._npu = None
        self._worker_replicas = None
        self._enable_autoscaling = None
        self._worker_min_replicas = None
        self._worker_max_replicas = None
        self.discriminator = None

        self.cpu = cpu
        self.memory = memory
        if gpu is not None:
            self.gpu = gpu
        if npu is not None:
            self.npu = npu
        if worker_replicas is not None:
            self.worker_replicas = worker_replicas
        self.enable_autoscaling = enable_autoscaling
        if worker_min_replicas is not None:
            self.worker_min_replicas = worker_min_replicas
        if worker_max_replicas is not None:
            self.worker_max_replicas = worker_max_replicas

    @property
    def cpu(self):
        r"""Gets the cpu of this RayWorkerResourceSpec.

        **参数解释**：CPU核数量，单位为毫核。 **约束限制**：不涉及。 **取值范围**：最小值为1000。 **默认取值**：不涉及。

        :return: The cpu of this RayWorkerResourceSpec.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this RayWorkerResourceSpec.

        **参数解释**：CPU核数量，单位为毫核。 **约束限制**：不涉及。 **取值范围**：最小值为1000。 **默认取值**：不涉及。

        :param cpu: The cpu of this RayWorkerResourceSpec.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this RayWorkerResourceSpec.

        **参数解释**：内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：最小值为1024。 **默认取值**：不涉及。

        :return: The memory of this RayWorkerResourceSpec.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this RayWorkerResourceSpec.

        **参数解释**：内存大小，单位MB。 **约束限制**：不涉及。 **取值范围**：最小值为1024。 **默认取值**：不涉及。

        :param memory: The memory of this RayWorkerResourceSpec.
        :type memory: int
        """
        self._memory = memory

    @property
    def gpu(self):
        r"""Gets the gpu of this RayWorkerResourceSpec.

        **参数解释**：节点的GPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。

        :return: The gpu of this RayWorkerResourceSpec.
        :rtype: float
        """
        return self._gpu

    @gpu.setter
    def gpu(self, gpu):
        r"""Sets the gpu of this RayWorkerResourceSpec.

        **参数解释**：节点的GPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。

        :param gpu: The gpu of this RayWorkerResourceSpec.
        :type gpu: float
        """
        self._gpu = gpu

    @property
    def npu(self):
        r"""Gets the npu of this RayWorkerResourceSpec.

        **参数解释**：节点的NPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。

        :return: The npu of this RayWorkerResourceSpec.
        :rtype: float
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        r"""Sets the npu of this RayWorkerResourceSpec.

        **参数解释**：节点的NPU数量。 **约束限制**：不支持小于1的值或带小数部分的值（如0.5, 1.5）。 **取值范围**：需配置为大于等于1.0，且必须为整数值（如1.0, 2.0, 3.0, ...）。 **默认取值**：不涉及。

        :param npu: The npu of this RayWorkerResourceSpec.
        :type npu: float
        """
        self._npu = npu

    @property
    def worker_replicas(self):
        r"""Gets the worker_replicas of this RayWorkerResourceSpec.

        **参数解释**：Worker副本数量。 **约束限制**：不涉及。 **取值范围**：1~64。 **默认取值**：不涉及。

        :return: The worker_replicas of this RayWorkerResourceSpec.
        :rtype: int
        """
        return self._worker_replicas

    @worker_replicas.setter
    def worker_replicas(self, worker_replicas):
        r"""Sets the worker_replicas of this RayWorkerResourceSpec.

        **参数解释**：Worker副本数量。 **约束限制**：不涉及。 **取值范围**：1~64。 **默认取值**：不涉及。

        :param worker_replicas: The worker_replicas of this RayWorkerResourceSpec.
        :type worker_replicas: int
        """
        self._worker_replicas = worker_replicas

    @property
    def enable_autoscaling(self):
        r"""Gets the enable_autoscaling of this RayWorkerResourceSpec.

        **参数解释**：是否开启worker节点的弹性伸缩。 **约束限制**：不涉及。 **取值范围**：可选值有：   - true：开启弹性伸缩。取该值时worker_min_replicas和worker_max_replicas必须设置。   - false：不开启弹性伸缩。取该值时worker_replicas必须设置。 **默认取值**：false。

        :return: The enable_autoscaling of this RayWorkerResourceSpec.
        :rtype: bool
        """
        return self._enable_autoscaling

    @enable_autoscaling.setter
    def enable_autoscaling(self, enable_autoscaling):
        r"""Sets the enable_autoscaling of this RayWorkerResourceSpec.

        **参数解释**：是否开启worker节点的弹性伸缩。 **约束限制**：不涉及。 **取值范围**：可选值有：   - true：开启弹性伸缩。取该值时worker_min_replicas和worker_max_replicas必须设置。   - false：不开启弹性伸缩。取该值时worker_replicas必须设置。 **默认取值**：false。

        :param enable_autoscaling: The enable_autoscaling of this RayWorkerResourceSpec.
        :type enable_autoscaling: bool
        """
        self._enable_autoscaling = enable_autoscaling

    @property
    def worker_min_replicas(self):
        r"""Gets the worker_min_replicas of this RayWorkerResourceSpec.

        **参数解释**：Worker最小副本数量。 **约束限制**：不涉及。 **取值范围**：0~64。 **默认取值**：不涉及。

        :return: The worker_min_replicas of this RayWorkerResourceSpec.
        :rtype: int
        """
        return self._worker_min_replicas

    @worker_min_replicas.setter
    def worker_min_replicas(self, worker_min_replicas):
        r"""Sets the worker_min_replicas of this RayWorkerResourceSpec.

        **参数解释**：Worker最小副本数量。 **约束限制**：不涉及。 **取值范围**：0~64。 **默认取值**：不涉及。

        :param worker_min_replicas: The worker_min_replicas of this RayWorkerResourceSpec.
        :type worker_min_replicas: int
        """
        self._worker_min_replicas = worker_min_replicas

    @property
    def worker_max_replicas(self):
        r"""Gets the worker_max_replicas of this RayWorkerResourceSpec.

        **参数解释**：Worker最大副本数量。 **约束限制**：不涉及。 **取值范围**：1~64。 **默认取值**：不涉及。

        :return: The worker_max_replicas of this RayWorkerResourceSpec.
        :rtype: int
        """
        return self._worker_max_replicas

    @worker_max_replicas.setter
    def worker_max_replicas(self, worker_max_replicas):
        r"""Sets the worker_max_replicas of this RayWorkerResourceSpec.

        **参数解释**：Worker最大副本数量。 **约束限制**：不涉及。 **取值范围**：1~64。 **默认取值**：不涉及。

        :param worker_max_replicas: The worker_max_replicas of this RayWorkerResourceSpec.
        :type worker_max_replicas: int
        """
        self._worker_max_replicas = worker_max_replicas

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
        if not isinstance(other, RayWorkerResourceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
