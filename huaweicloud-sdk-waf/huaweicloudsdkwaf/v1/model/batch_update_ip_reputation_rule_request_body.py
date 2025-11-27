# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateIpReputationRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'policyname': 'str',
        'description': 'str',
        'action': 'BatchUpdateIpReputationRuleRequestBodyAction',
        'type': 'str',
        'tags': 'list[str]',
        'policy_rule_ids': 'list[PolicyRuleIdRequestBodyPolicyRuleIds]'
    }

    attribute_map = {
        'name': 'name',
        'policyname': 'policyname',
        'description': 'description',
        'action': 'action',
        'type': 'type',
        'tags': 'tags',
        'policy_rule_ids': 'policy_rule_ids'
    }

    def __init__(self, name=None, policyname=None, description=None, action=None, type=None, tags=None, policy_rule_ids=None):
        r"""BatchUpdateIpReputationRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param policyname: **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policyname: str
        :param description: **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.BatchUpdateIpReputationRuleRequestBodyAction`
        :param type: **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type type: str
        :param tags: **参数解释：** 标签列表，关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type tags: list[str]
        :param policy_rule_ids: **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_rule_ids: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        
        

        self._name = None
        self._policyname = None
        self._description = None
        self._action = None
        self._type = None
        self._tags = None
        self._policy_rule_ids = None
        self.discriminator = None

        self.name = name
        if policyname is not None:
            self.policyname = policyname
        if description is not None:
            self.description = description
        self.action = action
        self.type = type
        self.tags = tags
        if policy_rule_ids is not None:
            self.policy_rule_ids = policy_rule_ids

    @property
    def name(self):
        r"""Gets the name of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this BatchUpdateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 规则名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this BatchUpdateIpReputationRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def policyname(self):
        r"""Gets the policyname of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policyname of this BatchUpdateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._policyname

    @policyname.setter
    def policyname(self, policyname):
        r"""Sets the policyname of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policyname: The policyname of this BatchUpdateIpReputationRuleRequestBody.
        :type policyname: str
        """
        self._policyname = policyname

    @property
    def description(self):
        r"""Gets the description of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this BatchUpdateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this BatchUpdateIpReputationRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def action(self):
        r"""Gets the action of this BatchUpdateIpReputationRuleRequestBody.

        :return: The action of this BatchUpdateIpReputationRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.BatchUpdateIpReputationRuleRequestBodyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchUpdateIpReputationRuleRequestBody.

        :param action: The action of this BatchUpdateIpReputationRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.BatchUpdateIpReputationRuleRequestBodyAction`
        """
        self._action = action

    @property
    def type(self):
        r"""Gets the type of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The type of this BatchUpdateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 规则类型（如idc表示机房IP情报类型） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param type: The type of this BatchUpdateIpReputationRuleRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def tags(self):
        r"""Gets the tags of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 标签列表，关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The tags of this BatchUpdateIpReputationRuleRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 标签列表，关联的情报标识 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param tags: The tags of this BatchUpdateIpReputationRuleRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def policy_rule_ids(self):
        r"""Gets the policy_rule_ids of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_rule_ids of this BatchUpdateIpReputationRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        return self._policy_rule_ids

    @policy_rule_ids.setter
    def policy_rule_ids(self, policy_rule_ids):
        r"""Sets the policy_rule_ids of this BatchUpdateIpReputationRuleRequestBody.

        **参数解释：** 策略和规则id数组，关联防护策略与对应的规则集合 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_rule_ids: The policy_rule_ids of this BatchUpdateIpReputationRuleRequestBody.
        :type policy_rule_ids: list[:class:`huaweicloudsdkwaf.v1.PolicyRuleIdRequestBodyPolicyRuleIds`]
        """
        self._policy_rule_ids = policy_rule_ids

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
        if not isinstance(other, BatchUpdateIpReputationRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
