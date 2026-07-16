# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdatePoolNodesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_names': 'list[str]',
        'action': 'str',
        'ha_redundant_effect': 'str',
        'driver': 'NodeDriver',
        'tags': 'list[NodeTag]'
    }

    attribute_map = {
        'node_names': 'nodeNames',
        'action': 'action',
        'ha_redundant_effect': 'haRedundantEffect',
        'driver': 'driver',
        'tags': 'tags'
    }

    def __init__(self, node_names=None, action=None, ha_redundant_effect=None, driver=None, tags=None):
        r"""BatchUpdatePoolNodesRequestBody

        The model defined in huaweicloud sdk

        :param node_names: **参数解释**：需要更新的节点名称列表。 **约束限制**：不涉及。
        :type node_names: list[str]
        :param action: **参数解释**：节点更新的类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - openHaRedundant：开启节点的高可用冗余标签 - closeHaRedundant：关闭节点的高可用冗余标签 - createTags：批量添加节点资源标签 - deleteTags：批量删除节点资源标签 **默认取值**：不涉及。
        :type action: str
        :param ha_redundant_effect: **参数解释**：高可用冗余标签效果。 **约束限制**：不涉及。 **取值范围**：可选值如下： - NoSchedule：禁止调度 - NoExecute：禁止执行。 **默认取值**：NoSchedule。
        :type ha_redundant_effect: str
        :param driver: 
        :type driver: :class:`huaweicloudsdkmodelarts.v1.NodeDriver`
        :param tags: **参数解释**：需要批量操作的资源标签列表。 **约束限制**：不涉及。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.NodeTag`]
        """
        
        

        self._node_names = None
        self._action = None
        self._ha_redundant_effect = None
        self._driver = None
        self._tags = None
        self.discriminator = None

        self.node_names = node_names
        self.action = action
        if ha_redundant_effect is not None:
            self.ha_redundant_effect = ha_redundant_effect
        if driver is not None:
            self.driver = driver
        if tags is not None:
            self.tags = tags

    @property
    def node_names(self):
        r"""Gets the node_names of this BatchUpdatePoolNodesRequestBody.

        **参数解释**：需要更新的节点名称列表。 **约束限制**：不涉及。

        :return: The node_names of this BatchUpdatePoolNodesRequestBody.
        :rtype: list[str]
        """
        return self._node_names

    @node_names.setter
    def node_names(self, node_names):
        r"""Sets the node_names of this BatchUpdatePoolNodesRequestBody.

        **参数解释**：需要更新的节点名称列表。 **约束限制**：不涉及。

        :param node_names: The node_names of this BatchUpdatePoolNodesRequestBody.
        :type node_names: list[str]
        """
        self._node_names = node_names

    @property
    def action(self):
        r"""Gets the action of this BatchUpdatePoolNodesRequestBody.

        **参数解释**：节点更新的类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - openHaRedundant：开启节点的高可用冗余标签 - closeHaRedundant：关闭节点的高可用冗余标签 - createTags：批量添加节点资源标签 - deleteTags：批量删除节点资源标签 **默认取值**：不涉及。

        :return: The action of this BatchUpdatePoolNodesRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchUpdatePoolNodesRequestBody.

        **参数解释**：节点更新的类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - openHaRedundant：开启节点的高可用冗余标签 - closeHaRedundant：关闭节点的高可用冗余标签 - createTags：批量添加节点资源标签 - deleteTags：批量删除节点资源标签 **默认取值**：不涉及。

        :param action: The action of this BatchUpdatePoolNodesRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def ha_redundant_effect(self):
        r"""Gets the ha_redundant_effect of this BatchUpdatePoolNodesRequestBody.

        **参数解释**：高可用冗余标签效果。 **约束限制**：不涉及。 **取值范围**：可选值如下： - NoSchedule：禁止调度 - NoExecute：禁止执行。 **默认取值**：NoSchedule。

        :return: The ha_redundant_effect of this BatchUpdatePoolNodesRequestBody.
        :rtype: str
        """
        return self._ha_redundant_effect

    @ha_redundant_effect.setter
    def ha_redundant_effect(self, ha_redundant_effect):
        r"""Sets the ha_redundant_effect of this BatchUpdatePoolNodesRequestBody.

        **参数解释**：高可用冗余标签效果。 **约束限制**：不涉及。 **取值范围**：可选值如下： - NoSchedule：禁止调度 - NoExecute：禁止执行。 **默认取值**：NoSchedule。

        :param ha_redundant_effect: The ha_redundant_effect of this BatchUpdatePoolNodesRequestBody.
        :type ha_redundant_effect: str
        """
        self._ha_redundant_effect = ha_redundant_effect

    @property
    def driver(self):
        r"""Gets the driver of this BatchUpdatePoolNodesRequestBody.

        :return: The driver of this BatchUpdatePoolNodesRequestBody.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.NodeDriver`
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        r"""Sets the driver of this BatchUpdatePoolNodesRequestBody.

        :param driver: The driver of this BatchUpdatePoolNodesRequestBody.
        :type driver: :class:`huaweicloudsdkmodelarts.v1.NodeDriver`
        """
        self._driver = driver

    @property
    def tags(self):
        r"""Gets the tags of this BatchUpdatePoolNodesRequestBody.

        **参数解释**：需要批量操作的资源标签列表。 **约束限制**：不涉及。

        :return: The tags of this BatchUpdatePoolNodesRequestBody.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.NodeTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchUpdatePoolNodesRequestBody.

        **参数解释**：需要批量操作的资源标签列表。 **约束限制**：不涉及。

        :param tags: The tags of this BatchUpdatePoolNodesRequestBody.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.NodeTag`]
        """
        self._tags = tags

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
        if not isinstance(other, BatchUpdatePoolNodesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
