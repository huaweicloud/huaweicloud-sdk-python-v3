# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchLockPoolNodesRequestBody:

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
        'actions': 'list[str]'
    }

    attribute_map = {
        'node_names': 'nodeNames',
        'actions': 'actions'
    }

    def __init__(self, node_names=None, actions=None):
        r"""BatchLockPoolNodesRequestBody

        The model defined in huaweicloud sdk

        :param node_names: **参数解释**：需要变更锁状态的节点名称列表。 **约束限制**：不涉及。
        :type node_names: list[str]
        :param actions: **参数解释**：变更的功能类型。 **约束限制**：不涉及。
        :type actions: list[str]
        """
        
        

        self._node_names = None
        self._actions = None
        self.discriminator = None

        self.node_names = node_names
        self.actions = actions

    @property
    def node_names(self):
        r"""Gets the node_names of this BatchLockPoolNodesRequestBody.

        **参数解释**：需要变更锁状态的节点名称列表。 **约束限制**：不涉及。

        :return: The node_names of this BatchLockPoolNodesRequestBody.
        :rtype: list[str]
        """
        return self._node_names

    @node_names.setter
    def node_names(self, node_names):
        r"""Sets the node_names of this BatchLockPoolNodesRequestBody.

        **参数解释**：需要变更锁状态的节点名称列表。 **约束限制**：不涉及。

        :param node_names: The node_names of this BatchLockPoolNodesRequestBody.
        :type node_names: list[str]
        """
        self._node_names = node_names

    @property
    def actions(self):
        r"""Gets the actions of this BatchLockPoolNodesRequestBody.

        **参数解释**：变更的功能类型。 **约束限制**：不涉及。

        :return: The actions of this BatchLockPoolNodesRequestBody.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this BatchLockPoolNodesRequestBody.

        **参数解释**：变更的功能类型。 **约束限制**：不涉及。

        :param actions: The actions of this BatchLockPoolNodesRequestBody.
        :type actions: list[str]
        """
        self._actions = actions

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
        if not isinstance(other, BatchLockPoolNodesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
