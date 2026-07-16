# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeDriver:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'update_strategy': 'str'
    }

    attribute_map = {
        'version': 'version',
        'update_strategy': 'updateStrategy'
    }

    def __init__(self, version=None, update_strategy=None):
        r"""NodeDriver

        The model defined in huaweicloud sdk

        :param version: **参数解释**：节点上驱动的版本号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type version: str
        :param update_strategy: **参数解释**：节点驱动升级策略。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type update_strategy: str
        """
        
        

        self._version = None
        self._update_strategy = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if update_strategy is not None:
            self.update_strategy = update_strategy

    @property
    def version(self):
        r"""Gets the version of this NodeDriver.

        **参数解释**：节点上驱动的版本号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The version of this NodeDriver.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this NodeDriver.

        **参数解释**：节点上驱动的版本号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param version: The version of this NodeDriver.
        :type version: str
        """
        self._version = version

    @property
    def update_strategy(self):
        r"""Gets the update_strategy of this NodeDriver.

        **参数解释**：节点驱动升级策略。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The update_strategy of this NodeDriver.
        :rtype: str
        """
        return self._update_strategy

    @update_strategy.setter
    def update_strategy(self, update_strategy):
        r"""Sets the update_strategy of this NodeDriver.

        **参数解释**：节点驱动升级策略。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param update_strategy: The update_strategy of this NodeDriver.
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
        if not isinstance(other, NodeDriver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
