# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyAutoNodeExpansionPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_option': 'bool',
        'overload_node_threshold': 'int',
        'cpu_threshold': 'int',
        'mem_threshold': 'int',
        'step': 'int',
        'node_limit': 'int'
    }

    attribute_map = {
        'switch_option': 'switch_option',
        'overload_node_threshold': 'overload_node_threshold',
        'cpu_threshold': 'cpu_threshold',
        'mem_threshold': 'mem_threshold',
        'step': 'step',
        'node_limit': 'node_limit'
    }

    def __init__(self, switch_option=None, overload_node_threshold=None, cpu_threshold=None, mem_threshold=None, step=None, node_limit=None):
        r"""ModifyAutoNodeExpansionPolicyRequestBody

        The model defined in huaweicloud sdk

        :param switch_option: **参数解释：** 节点扩容是否开启。 **约束限制：** 不涉及。 **取值范围：**   true为开启。   false为关闭。 **默认取值：** 不涉及。
        :type switch_option: bool
        :param overload_node_threshold: **参数解释：** 超负载节点比例。如当前实例3个节点，需要当2个节点满足阈值时触发扩容，因2÷3≈67%，可设置为67（向上取整） **约束限制：** 不涉及。 **取值范围：** 1-100的正整数。 **默认取值：** 不涉及。
        :type overload_node_threshold: int
        :param cpu_threshold: **参数解释：** 触发节点自动扩容的CPU使用率。 **约束限制：** 不涉及。 **取值范围：** 1-100的正整数 **默认取值：** 默认为80。
        :type cpu_threshold: int
        :param mem_threshold: **参数解释：** 触发节点自动扩容的内存使用率。 **约束限制：** 不涉及。 **取值范围：** 1-100的数字 **默认取值：** 默认为80。
        :type mem_threshold: int
        :param step: **参数解释：** 每次扩容的节点个数。 **约束限制：** 不涉及。 **取值范围：** 大等于1的正整数，最大不超过可扩容的节点上限。 **默认取值：** 默认为3。
        :type step: int
        :param node_limit: **参数解释：** 自动扩容所能达到的节点上限。 **约束限制：** 不涉及。 **取值范围：** 大等于1的正整数，最大不超过当前实例可扩容的节点上限。 **默认取值：** 默认为当前实例可扩容的节点上限。
        :type node_limit: int
        """
        
        

        self._switch_option = None
        self._overload_node_threshold = None
        self._cpu_threshold = None
        self._mem_threshold = None
        self._step = None
        self._node_limit = None
        self.discriminator = None

        self.switch_option = switch_option
        if overload_node_threshold is not None:
            self.overload_node_threshold = overload_node_threshold
        if cpu_threshold is not None:
            self.cpu_threshold = cpu_threshold
        if mem_threshold is not None:
            self.mem_threshold = mem_threshold
        if step is not None:
            self.step = step
        if node_limit is not None:
            self.node_limit = node_limit

    @property
    def switch_option(self):
        r"""Gets the switch_option of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 节点扩容是否开启。 **约束限制：** 不涉及。 **取值范围：**   true为开启。   false为关闭。 **默认取值：** 不涉及。

        :return: The switch_option of this ModifyAutoNodeExpansionPolicyRequestBody.
        :rtype: bool
        """
        return self._switch_option

    @switch_option.setter
    def switch_option(self, switch_option):
        r"""Sets the switch_option of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 节点扩容是否开启。 **约束限制：** 不涉及。 **取值范围：**   true为开启。   false为关闭。 **默认取值：** 不涉及。

        :param switch_option: The switch_option of this ModifyAutoNodeExpansionPolicyRequestBody.
        :type switch_option: bool
        """
        self._switch_option = switch_option

    @property
    def overload_node_threshold(self):
        r"""Gets the overload_node_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 超负载节点比例。如当前实例3个节点，需要当2个节点满足阈值时触发扩容，因2÷3≈67%，可设置为67（向上取整） **约束限制：** 不涉及。 **取值范围：** 1-100的正整数。 **默认取值：** 不涉及。

        :return: The overload_node_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.
        :rtype: int
        """
        return self._overload_node_threshold

    @overload_node_threshold.setter
    def overload_node_threshold(self, overload_node_threshold):
        r"""Sets the overload_node_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 超负载节点比例。如当前实例3个节点，需要当2个节点满足阈值时触发扩容，因2÷3≈67%，可设置为67（向上取整） **约束限制：** 不涉及。 **取值范围：** 1-100的正整数。 **默认取值：** 不涉及。

        :param overload_node_threshold: The overload_node_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.
        :type overload_node_threshold: int
        """
        self._overload_node_threshold = overload_node_threshold

    @property
    def cpu_threshold(self):
        r"""Gets the cpu_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 触发节点自动扩容的CPU使用率。 **约束限制：** 不涉及。 **取值范围：** 1-100的正整数 **默认取值：** 默认为80。

        :return: The cpu_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.
        :rtype: int
        """
        return self._cpu_threshold

    @cpu_threshold.setter
    def cpu_threshold(self, cpu_threshold):
        r"""Sets the cpu_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 触发节点自动扩容的CPU使用率。 **约束限制：** 不涉及。 **取值范围：** 1-100的正整数 **默认取值：** 默认为80。

        :param cpu_threshold: The cpu_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.
        :type cpu_threshold: int
        """
        self._cpu_threshold = cpu_threshold

    @property
    def mem_threshold(self):
        r"""Gets the mem_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 触发节点自动扩容的内存使用率。 **约束限制：** 不涉及。 **取值范围：** 1-100的数字 **默认取值：** 默认为80。

        :return: The mem_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.
        :rtype: int
        """
        return self._mem_threshold

    @mem_threshold.setter
    def mem_threshold(self, mem_threshold):
        r"""Sets the mem_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 触发节点自动扩容的内存使用率。 **约束限制：** 不涉及。 **取值范围：** 1-100的数字 **默认取值：** 默认为80。

        :param mem_threshold: The mem_threshold of this ModifyAutoNodeExpansionPolicyRequestBody.
        :type mem_threshold: int
        """
        self._mem_threshold = mem_threshold

    @property
    def step(self):
        r"""Gets the step of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 每次扩容的节点个数。 **约束限制：** 不涉及。 **取值范围：** 大等于1的正整数，最大不超过可扩容的节点上限。 **默认取值：** 默认为3。

        :return: The step of this ModifyAutoNodeExpansionPolicyRequestBody.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 每次扩容的节点个数。 **约束限制：** 不涉及。 **取值范围：** 大等于1的正整数，最大不超过可扩容的节点上限。 **默认取值：** 默认为3。

        :param step: The step of this ModifyAutoNodeExpansionPolicyRequestBody.
        :type step: int
        """
        self._step = step

    @property
    def node_limit(self):
        r"""Gets the node_limit of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 自动扩容所能达到的节点上限。 **约束限制：** 不涉及。 **取值范围：** 大等于1的正整数，最大不超过当前实例可扩容的节点上限。 **默认取值：** 默认为当前实例可扩容的节点上限。

        :return: The node_limit of this ModifyAutoNodeExpansionPolicyRequestBody.
        :rtype: int
        """
        return self._node_limit

    @node_limit.setter
    def node_limit(self, node_limit):
        r"""Sets the node_limit of this ModifyAutoNodeExpansionPolicyRequestBody.

        **参数解释：** 自动扩容所能达到的节点上限。 **约束限制：** 不涉及。 **取值范围：** 大等于1的正整数，最大不超过当前实例可扩容的节点上限。 **默认取值：** 默认为当前实例可扩容的节点上限。

        :param node_limit: The node_limit of this ModifyAutoNodeExpansionPolicyRequestBody.
        :type node_limit: int
        """
        self._node_limit = node_limit

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
        if not isinstance(other, ModifyAutoNodeExpansionPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
