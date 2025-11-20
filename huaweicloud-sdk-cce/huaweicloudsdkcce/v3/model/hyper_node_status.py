# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HyperNodeStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'instance_id': 'str',
        'current_node': 'int',
        'deleting_node': 'int',
        'creating_node': 'int',
        'active_node': 'int'
    }

    attribute_map = {
        'phase': 'phase',
        'instance_id': 'instanceID',
        'current_node': 'currentNode',
        'deleting_node': 'deletingNode',
        'creating_node': 'creatingNode',
        'active_node': 'activeNode'
    }

    def __init__(self, phase=None, instance_id=None, current_node=None, deleting_node=None, creating_node=None, active_node=None):
        r"""HyperNodeStatus

        The model defined in huaweicloud sdk

        :param phase: **参数解释** 超节点状态 **取值范围** - provisioning: 创建中。 - active: 整体可用，代表超节点下所有节点都可用。 - partially-available: 超节点下存在不可用节点时会从 active 转成此状态。 - error: 错误状态。 - deleting: 删除中。 - reinstalling: 重置中。 - scaling: 扩容或缩容中。
        :type phase: str
        :param instance_id: **参数解释** 超节点实例 ID
        :type instance_id: str
        :param current_node: **参数解释** 超节点下节点总数
        :type current_node: int
        :param deleting_node: **参数解释** 超节点下处于删除中的节点数
        :type deleting_node: int
        :param creating_node: **参数解释** 超节点下处于创建中的节点数
        :type creating_node: int
        :param active_node: **参数解释** 超节点下处于可用状态的节点数
        :type active_node: int
        """
        
        

        self._phase = None
        self._instance_id = None
        self._current_node = None
        self._deleting_node = None
        self._creating_node = None
        self._active_node = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if instance_id is not None:
            self.instance_id = instance_id
        if current_node is not None:
            self.current_node = current_node
        if deleting_node is not None:
            self.deleting_node = deleting_node
        if creating_node is not None:
            self.creating_node = creating_node
        if active_node is not None:
            self.active_node = active_node

    @property
    def phase(self):
        r"""Gets the phase of this HyperNodeStatus.

        **参数解释** 超节点状态 **取值范围** - provisioning: 创建中。 - active: 整体可用，代表超节点下所有节点都可用。 - partially-available: 超节点下存在不可用节点时会从 active 转成此状态。 - error: 错误状态。 - deleting: 删除中。 - reinstalling: 重置中。 - scaling: 扩容或缩容中。

        :return: The phase of this HyperNodeStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this HyperNodeStatus.

        **参数解释** 超节点状态 **取值范围** - provisioning: 创建中。 - active: 整体可用，代表超节点下所有节点都可用。 - partially-available: 超节点下存在不可用节点时会从 active 转成此状态。 - error: 错误状态。 - deleting: 删除中。 - reinstalling: 重置中。 - scaling: 扩容或缩容中。

        :param phase: The phase of this HyperNodeStatus.
        :type phase: str
        """
        self._phase = phase

    @property
    def instance_id(self):
        r"""Gets the instance_id of this HyperNodeStatus.

        **参数解释** 超节点实例 ID

        :return: The instance_id of this HyperNodeStatus.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this HyperNodeStatus.

        **参数解释** 超节点实例 ID

        :param instance_id: The instance_id of this HyperNodeStatus.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def current_node(self):
        r"""Gets the current_node of this HyperNodeStatus.

        **参数解释** 超节点下节点总数

        :return: The current_node of this HyperNodeStatus.
        :rtype: int
        """
        return self._current_node

    @current_node.setter
    def current_node(self, current_node):
        r"""Sets the current_node of this HyperNodeStatus.

        **参数解释** 超节点下节点总数

        :param current_node: The current_node of this HyperNodeStatus.
        :type current_node: int
        """
        self._current_node = current_node

    @property
    def deleting_node(self):
        r"""Gets the deleting_node of this HyperNodeStatus.

        **参数解释** 超节点下处于删除中的节点数

        :return: The deleting_node of this HyperNodeStatus.
        :rtype: int
        """
        return self._deleting_node

    @deleting_node.setter
    def deleting_node(self, deleting_node):
        r"""Sets the deleting_node of this HyperNodeStatus.

        **参数解释** 超节点下处于删除中的节点数

        :param deleting_node: The deleting_node of this HyperNodeStatus.
        :type deleting_node: int
        """
        self._deleting_node = deleting_node

    @property
    def creating_node(self):
        r"""Gets the creating_node of this HyperNodeStatus.

        **参数解释** 超节点下处于创建中的节点数

        :return: The creating_node of this HyperNodeStatus.
        :rtype: int
        """
        return self._creating_node

    @creating_node.setter
    def creating_node(self, creating_node):
        r"""Sets the creating_node of this HyperNodeStatus.

        **参数解释** 超节点下处于创建中的节点数

        :param creating_node: The creating_node of this HyperNodeStatus.
        :type creating_node: int
        """
        self._creating_node = creating_node

    @property
    def active_node(self):
        r"""Gets the active_node of this HyperNodeStatus.

        **参数解释** 超节点下处于可用状态的节点数

        :return: The active_node of this HyperNodeStatus.
        :rtype: int
        """
        return self._active_node

    @active_node.setter
    def active_node(self, active_node):
        r"""Sets the active_node of this HyperNodeStatus.

        **参数解释** 超节点下处于可用状态的节点数

        :param active_node: The active_node of this HyperNodeStatus.
        :type active_node: int
        """
        self._active_node = active_node

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
        if not isinstance(other, HyperNodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
