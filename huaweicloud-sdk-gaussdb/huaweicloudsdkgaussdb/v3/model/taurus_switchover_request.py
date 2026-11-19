# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaurusSwitchoverRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'force': 'bool'
    }

    attribute_map = {
        'node_id': 'node_id',
        'force': 'force'
    }

    def __init__(self, node_id=None, force=None):
        r"""TaurusSwitchoverRequest

        The model defined in huaweicloud sdk

        :param node_id: 只读节点ID，倒换后为主节点。
        :type node_id: str
        :param force: **参数解释**：  是否进行强制倒换。强制倒换将导致主节点重启，未提交的事务会被中断，请在业务低峰期执行该操作。  **约束限制**：  不涉及。  **取值范围**：  - true：强制倒换。 - false：普通倒换。  **默认取值**：  false。
        :type force: bool
        """
        
        

        self._node_id = None
        self._force = None
        self.discriminator = None

        self.node_id = node_id
        if force is not None:
            self.force = force

    @property
    def node_id(self):
        r"""Gets the node_id of this TaurusSwitchoverRequest.

        只读节点ID，倒换后为主节点。

        :return: The node_id of this TaurusSwitchoverRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this TaurusSwitchoverRequest.

        只读节点ID，倒换后为主节点。

        :param node_id: The node_id of this TaurusSwitchoverRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def force(self):
        r"""Gets the force of this TaurusSwitchoverRequest.

        **参数解释**：  是否进行强制倒换。强制倒换将导致主节点重启，未提交的事务会被中断，请在业务低峰期执行该操作。  **约束限制**：  不涉及。  **取值范围**：  - true：强制倒换。 - false：普通倒换。  **默认取值**：  false。

        :return: The force of this TaurusSwitchoverRequest.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        r"""Sets the force of this TaurusSwitchoverRequest.

        **参数解释**：  是否进行强制倒换。强制倒换将导致主节点重启，未提交的事务会被中断，请在业务低峰期执行该操作。  **约束限制**：  不涉及。  **取值范围**：  - true：强制倒换。 - false：普通倒换。  **默认取值**：  false。

        :param force: The force of this TaurusSwitchoverRequest.
        :type force: bool
        """
        self._force = force

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
        if not isinstance(other, TaurusSwitchoverRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
