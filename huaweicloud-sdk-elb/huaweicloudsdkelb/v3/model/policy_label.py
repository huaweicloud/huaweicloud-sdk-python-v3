# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyLabel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'priority': 'str',
        'action': 'str',
        'admin_state_up': 'bool',
        'rules': 'list[L7Rule]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'priority': 'priority',
        'action': 'action',
        'admin_state_up': 'admin_state_up',
        'rules': 'rules'
    }

    def __init__(self, id=None, name=None, priority=None, action=None, admin_state_up=None, rules=None):
        r"""PolicyLabel

        The model defined in huaweicloud sdk

        :param id: **参数解释**：转发策略id。  **取值范围**：不涉及
        :type id: str
        :param name: **参数解释**：转发策略名称。  **取值范围**：不涉及
        :type name: str
        :param priority: **参数解释**：转发策略优先级。  **取值范围**：不涉及
        :type priority: str
        :param action: **参数解释**：转发策略action。  **取值范围**：不涉及
        :type action: str
        :param admin_state_up: **参数解释**：转发策略是否启用。  **取值范围**：不涉及
        :type admin_state_up: bool
        :param rules: **参数解释**：规则对象列表。
        :type rules: list[:class:`huaweicloudsdkelb.v3.L7Rule`]
        """
        
        

        self._id = None
        self._name = None
        self._priority = None
        self._action = None
        self._admin_state_up = None
        self._rules = None
        self.discriminator = None

        self.id = id
        self.name = name
        if priority is not None:
            self.priority = priority
        self.action = action
        self.admin_state_up = admin_state_up
        self.rules = rules

    @property
    def id(self):
        r"""Gets the id of this PolicyLabel.

        **参数解释**：转发策略id。  **取值范围**：不涉及

        :return: The id of this PolicyLabel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PolicyLabel.

        **参数解释**：转发策略id。  **取值范围**：不涉及

        :param id: The id of this PolicyLabel.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PolicyLabel.

        **参数解释**：转发策略名称。  **取值范围**：不涉及

        :return: The name of this PolicyLabel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PolicyLabel.

        **参数解释**：转发策略名称。  **取值范围**：不涉及

        :param name: The name of this PolicyLabel.
        :type name: str
        """
        self._name = name

    @property
    def priority(self):
        r"""Gets the priority of this PolicyLabel.

        **参数解释**：转发策略优先级。  **取值范围**：不涉及

        :return: The priority of this PolicyLabel.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this PolicyLabel.

        **参数解释**：转发策略优先级。  **取值范围**：不涉及

        :param priority: The priority of this PolicyLabel.
        :type priority: str
        """
        self._priority = priority

    @property
    def action(self):
        r"""Gets the action of this PolicyLabel.

        **参数解释**：转发策略action。  **取值范围**：不涉及

        :return: The action of this PolicyLabel.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this PolicyLabel.

        **参数解释**：转发策略action。  **取值范围**：不涉及

        :param action: The action of this PolicyLabel.
        :type action: str
        """
        self._action = action

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this PolicyLabel.

        **参数解释**：转发策略是否启用。  **取值范围**：不涉及

        :return: The admin_state_up of this PolicyLabel.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this PolicyLabel.

        **参数解释**：转发策略是否启用。  **取值范围**：不涉及

        :param admin_state_up: The admin_state_up of this PolicyLabel.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def rules(self):
        r"""Gets the rules of this PolicyLabel.

        **参数解释**：规则对象列表。

        :return: The rules of this PolicyLabel.
        :rtype: list[:class:`huaweicloudsdkelb.v3.L7Rule`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this PolicyLabel.

        **参数解释**：规则对象列表。

        :param rules: The rules of this PolicyLabel.
        :type rules: list[:class:`huaweicloudsdkelb.v3.L7Rule`]
        """
        self._rules = rules

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
        if not isinstance(other, PolicyLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
