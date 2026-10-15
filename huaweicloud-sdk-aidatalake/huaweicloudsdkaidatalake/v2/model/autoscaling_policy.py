# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoscalingPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'vertex_max_parallelism': 'int',
        'quota_cpu': 'int',
        'quota_memory': 'int',
        'custom_config': 'dict(str, str)'
    }

    attribute_map = {
        'enabled': 'enabled',
        'vertex_max_parallelism': 'vertex_max_parallelism',
        'quota_cpu': 'quota_cpu',
        'quota_memory': 'quota_memory',
        'custom_config': 'custom_config'
    }

    def __init__(self, enabled=None, vertex_max_parallelism=None, quota_cpu=None, quota_memory=None, custom_config=None):
        r"""AutoscalingPolicy

        The model defined in huaweicloud sdk

        :param enabled: **参数解释**：自动调优开关。 **约束限制**：不涉及。 **取值范围**：   - true：开启自动调优。   - false：关闭自动调优。 **默认取值**：false。
        :type enabled: bool
        :param vertex_max_parallelism: **参数解释**：算子最大并行度。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：1000。
        :type vertex_max_parallelism: int
        :param quota_cpu: **参数解释**：CPU配额（单位：毫核）。 **约束限制**：不涉及。 **取值范围**：500~40000000。 **默认取值**：16000。
        :type quota_cpu: int
        :param quota_memory: **参数解释**：内存配额（单位：MB）。 **约束限制**：不涉及。 **取值范围**：2048~81920000。 **默认取值**：65536。
        :type quota_memory: int
        :param custom_config: **参数解释**：用户自定义的自动调优配置参数，为键值对形式，传入Flink Kubernetes Operator支持的job.autoscaler.*参数。最多支持50个参数，每个值长度为1~1024个字符。 **约束限制**：采用全量替换模式，传入该字段时以本次传入内容为准；不传该字段时不修改自定义自动调优配置。参数名必须以job.autoscaler.开头。结构化字段同名键（job.autoscaler.enabled、job.autoscaler.vertex.max-parallelism、job.autoscaler.quota.cpu、job.autoscaler.quota.memory）配置不生效。
        :type custom_config: dict(str, str)
        """
        
        

        self._enabled = None
        self._vertex_max_parallelism = None
        self._quota_cpu = None
        self._quota_memory = None
        self._custom_config = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if vertex_max_parallelism is not None:
            self.vertex_max_parallelism = vertex_max_parallelism
        if quota_cpu is not None:
            self.quota_cpu = quota_cpu
        if quota_memory is not None:
            self.quota_memory = quota_memory
        if custom_config is not None:
            self.custom_config = custom_config

    @property
    def enabled(self):
        r"""Gets the enabled of this AutoscalingPolicy.

        **参数解释**：自动调优开关。 **约束限制**：不涉及。 **取值范围**：   - true：开启自动调优。   - false：关闭自动调优。 **默认取值**：false。

        :return: The enabled of this AutoscalingPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this AutoscalingPolicy.

        **参数解释**：自动调优开关。 **约束限制**：不涉及。 **取值范围**：   - true：开启自动调优。   - false：关闭自动调优。 **默认取值**：false。

        :param enabled: The enabled of this AutoscalingPolicy.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def vertex_max_parallelism(self):
        r"""Gets the vertex_max_parallelism of this AutoscalingPolicy.

        **参数解释**：算子最大并行度。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：1000。

        :return: The vertex_max_parallelism of this AutoscalingPolicy.
        :rtype: int
        """
        return self._vertex_max_parallelism

    @vertex_max_parallelism.setter
    def vertex_max_parallelism(self, vertex_max_parallelism):
        r"""Sets the vertex_max_parallelism of this AutoscalingPolicy.

        **参数解释**：算子最大并行度。 **约束限制**：不涉及。 **取值范围**：1~1000。 **默认取值**：1000。

        :param vertex_max_parallelism: The vertex_max_parallelism of this AutoscalingPolicy.
        :type vertex_max_parallelism: int
        """
        self._vertex_max_parallelism = vertex_max_parallelism

    @property
    def quota_cpu(self):
        r"""Gets the quota_cpu of this AutoscalingPolicy.

        **参数解释**：CPU配额（单位：毫核）。 **约束限制**：不涉及。 **取值范围**：500~40000000。 **默认取值**：16000。

        :return: The quota_cpu of this AutoscalingPolicy.
        :rtype: int
        """
        return self._quota_cpu

    @quota_cpu.setter
    def quota_cpu(self, quota_cpu):
        r"""Sets the quota_cpu of this AutoscalingPolicy.

        **参数解释**：CPU配额（单位：毫核）。 **约束限制**：不涉及。 **取值范围**：500~40000000。 **默认取值**：16000。

        :param quota_cpu: The quota_cpu of this AutoscalingPolicy.
        :type quota_cpu: int
        """
        self._quota_cpu = quota_cpu

    @property
    def quota_memory(self):
        r"""Gets the quota_memory of this AutoscalingPolicy.

        **参数解释**：内存配额（单位：MB）。 **约束限制**：不涉及。 **取值范围**：2048~81920000。 **默认取值**：65536。

        :return: The quota_memory of this AutoscalingPolicy.
        :rtype: int
        """
        return self._quota_memory

    @quota_memory.setter
    def quota_memory(self, quota_memory):
        r"""Sets the quota_memory of this AutoscalingPolicy.

        **参数解释**：内存配额（单位：MB）。 **约束限制**：不涉及。 **取值范围**：2048~81920000。 **默认取值**：65536。

        :param quota_memory: The quota_memory of this AutoscalingPolicy.
        :type quota_memory: int
        """
        self._quota_memory = quota_memory

    @property
    def custom_config(self):
        r"""Gets the custom_config of this AutoscalingPolicy.

        **参数解释**：用户自定义的自动调优配置参数，为键值对形式，传入Flink Kubernetes Operator支持的job.autoscaler.*参数。最多支持50个参数，每个值长度为1~1024个字符。 **约束限制**：采用全量替换模式，传入该字段时以本次传入内容为准；不传该字段时不修改自定义自动调优配置。参数名必须以job.autoscaler.开头。结构化字段同名键（job.autoscaler.enabled、job.autoscaler.vertex.max-parallelism、job.autoscaler.quota.cpu、job.autoscaler.quota.memory）配置不生效。

        :return: The custom_config of this AutoscalingPolicy.
        :rtype: dict(str, str)
        """
        return self._custom_config

    @custom_config.setter
    def custom_config(self, custom_config):
        r"""Sets the custom_config of this AutoscalingPolicy.

        **参数解释**：用户自定义的自动调优配置参数，为键值对形式，传入Flink Kubernetes Operator支持的job.autoscaler.*参数。最多支持50个参数，每个值长度为1~1024个字符。 **约束限制**：采用全量替换模式，传入该字段时以本次传入内容为准；不传该字段时不修改自定义自动调优配置。参数名必须以job.autoscaler.开头。结构化字段同名键（job.autoscaler.enabled、job.autoscaler.vertex.max-parallelism、job.autoscaler.quota.cpu、job.autoscaler.quota.memory）配置不生效。

        :param custom_config: The custom_config of this AutoscalingPolicy.
        :type custom_config: dict(str, str)
        """
        self._custom_config = custom_config

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
        if not isinstance(other, AutoscalingPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
