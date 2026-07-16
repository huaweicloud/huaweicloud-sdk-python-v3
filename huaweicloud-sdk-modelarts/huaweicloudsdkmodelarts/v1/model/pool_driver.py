# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolDriver:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gpu_version': 'str',
        'npu_version': 'str',
        'update_strategy': 'str'
    }

    attribute_map = {
        'gpu_version': 'gpuVersion',
        'npu_version': 'npuVersion',
        'update_strategy': 'updateStrategy'
    }

    def __init__(self, gpu_version=None, npu_version=None, update_strategy=None):
        r"""PoolDriver

        The model defined in huaweicloud sdk

        :param gpu_version: **参数解释**：资源池默认的GPU驱动版本。物理资源池中包含GPU规格时有效。 **取值范围**：不涉及。
        :type gpu_version: str
        :param npu_version: **参数解释**：资源池默认的NPU驱动版本。物理资源池中包含NPU规格时有效。 **取值范围**：不涉及。
        :type npu_version: str
        :param update_strategy: **参数解释**：资源池驱动升级策略。 **取值范围**：可选值如下： - force：强制升级，立即升级节点驱动，可能影响节点上正在运行的作业。 - idle：安全升级，待节点上没有作业运行时进行驱动升级。
        :type update_strategy: str
        """
        
        

        self._gpu_version = None
        self._npu_version = None
        self._update_strategy = None
        self.discriminator = None

        if gpu_version is not None:
            self.gpu_version = gpu_version
        if npu_version is not None:
            self.npu_version = npu_version
        if update_strategy is not None:
            self.update_strategy = update_strategy

    @property
    def gpu_version(self):
        r"""Gets the gpu_version of this PoolDriver.

        **参数解释**：资源池默认的GPU驱动版本。物理资源池中包含GPU规格时有效。 **取值范围**：不涉及。

        :return: The gpu_version of this PoolDriver.
        :rtype: str
        """
        return self._gpu_version

    @gpu_version.setter
    def gpu_version(self, gpu_version):
        r"""Sets the gpu_version of this PoolDriver.

        **参数解释**：资源池默认的GPU驱动版本。物理资源池中包含GPU规格时有效。 **取值范围**：不涉及。

        :param gpu_version: The gpu_version of this PoolDriver.
        :type gpu_version: str
        """
        self._gpu_version = gpu_version

    @property
    def npu_version(self):
        r"""Gets the npu_version of this PoolDriver.

        **参数解释**：资源池默认的NPU驱动版本。物理资源池中包含NPU规格时有效。 **取值范围**：不涉及。

        :return: The npu_version of this PoolDriver.
        :rtype: str
        """
        return self._npu_version

    @npu_version.setter
    def npu_version(self, npu_version):
        r"""Sets the npu_version of this PoolDriver.

        **参数解释**：资源池默认的NPU驱动版本。物理资源池中包含NPU规格时有效。 **取值范围**：不涉及。

        :param npu_version: The npu_version of this PoolDriver.
        :type npu_version: str
        """
        self._npu_version = npu_version

    @property
    def update_strategy(self):
        r"""Gets the update_strategy of this PoolDriver.

        **参数解释**：资源池驱动升级策略。 **取值范围**：可选值如下： - force：强制升级，立即升级节点驱动，可能影响节点上正在运行的作业。 - idle：安全升级，待节点上没有作业运行时进行驱动升级。

        :return: The update_strategy of this PoolDriver.
        :rtype: str
        """
        return self._update_strategy

    @update_strategy.setter
    def update_strategy(self, update_strategy):
        r"""Sets the update_strategy of this PoolDriver.

        **参数解释**：资源池驱动升级策略。 **取值范围**：可选值如下： - force：强制升级，立即升级节点驱动，可能影响节点上正在运行的作业。 - idle：安全升级，待节点上没有作业运行时进行驱动升级。

        :param update_strategy: The update_strategy of this PoolDriver.
        :type update_strategy: str
        """
        self._update_strategy = update_strategy

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
        if not isinstance(other, PoolDriver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
