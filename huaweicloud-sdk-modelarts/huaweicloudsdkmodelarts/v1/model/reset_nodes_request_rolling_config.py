# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetNodesRequestRollingConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'strategy': 'str',
        'max_unavailable': 'int'
    }

    attribute_map = {
        'strategy': 'strategy',
        'max_unavailable': 'maxUnavailable'
    }

    def __init__(self, strategy=None, max_unavailable=None):
        r"""ResetNodesRequestRollingConfig

        The model defined in huaweicloud sdk

        :param strategy: **参数解释**：滚动策略。 **约束限制**：不涉及。 **取值范围**：可选值如下： - RollingByNumber：表示按节点数量设置最大同时重置节点数量，例如10，表示单次最多重置10个节点 - RollingByPercent：表示按百分比设置最大同时重置节点数量。例如10，表示单次最多重置10%的节点 **默认取值**：不涉及。
        :type strategy: str
        :param max_unavailable: **参数解释**：滚动重置的节点数量或者节点比例, 当strategy为RollingByNumber时,表示允许同时重置的节点数量, 当strategy为RollingByPercent时,表示允许同时重置的最大节点比例。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type max_unavailable: int
        """
        
        

        self._strategy = None
        self._max_unavailable = None
        self.discriminator = None

        self.strategy = strategy
        self.max_unavailable = max_unavailable

    @property
    def strategy(self):
        r"""Gets the strategy of this ResetNodesRequestRollingConfig.

        **参数解释**：滚动策略。 **约束限制**：不涉及。 **取值范围**：可选值如下： - RollingByNumber：表示按节点数量设置最大同时重置节点数量，例如10，表示单次最多重置10个节点 - RollingByPercent：表示按百分比设置最大同时重置节点数量。例如10，表示单次最多重置10%的节点 **默认取值**：不涉及。

        :return: The strategy of this ResetNodesRequestRollingConfig.
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        r"""Sets the strategy of this ResetNodesRequestRollingConfig.

        **参数解释**：滚动策略。 **约束限制**：不涉及。 **取值范围**：可选值如下： - RollingByNumber：表示按节点数量设置最大同时重置节点数量，例如10，表示单次最多重置10个节点 - RollingByPercent：表示按百分比设置最大同时重置节点数量。例如10，表示单次最多重置10%的节点 **默认取值**：不涉及。

        :param strategy: The strategy of this ResetNodesRequestRollingConfig.
        :type strategy: str
        """
        self._strategy = strategy

    @property
    def max_unavailable(self):
        r"""Gets the max_unavailable of this ResetNodesRequestRollingConfig.

        **参数解释**：滚动重置的节点数量或者节点比例, 当strategy为RollingByNumber时,表示允许同时重置的节点数量, 当strategy为RollingByPercent时,表示允许同时重置的最大节点比例。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The max_unavailable of this ResetNodesRequestRollingConfig.
        :rtype: int
        """
        return self._max_unavailable

    @max_unavailable.setter
    def max_unavailable(self, max_unavailable):
        r"""Sets the max_unavailable of this ResetNodesRequestRollingConfig.

        **参数解释**：滚动重置的节点数量或者节点比例, 当strategy为RollingByNumber时,表示允许同时重置的节点数量, 当strategy为RollingByPercent时,表示允许同时重置的最大节点比例。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param max_unavailable: The max_unavailable of this ResetNodesRequestRollingConfig.
        :type max_unavailable: int
        """
        self._max_unavailable = max_unavailable

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
        if not isinstance(other, ResetNodesRequestRollingConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
