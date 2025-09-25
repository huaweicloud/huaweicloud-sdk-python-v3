# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateBotMRuleActionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_ids': 'list[str]',
        'defense_action': 'int'
    }

    attribute_map = {
        'rule_ids': 'rule_ids',
        'defense_action': 'defense_action'
    }

    def __init__(self, rule_ids=None, defense_action=None):
        r"""BatchUpdateBotMRuleActionRequestBody

        The model defined in huaweicloud sdk

        :param rule_ids: **参数解释：** 批量更新的规则ID，包含需要修改防护动作的多条BotM规则ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type rule_ids: list[str]
        :param defense_action: **参数解释：** 批量更新的防护动作对应的数字，101-拦截、102-放行、103-观察、104-验证码、201-重定向、202-返回自定义页面、301-拉黑IP **约束限制：** 不涉及 **取值范围：** - 101：拦截 - 102：放行 - 103：观察 - 104：验证码 - 201：重定向 - 202：返回自定义页面 - 301：拉黑IP **默认取值：** 不涉及
        :type defense_action: int
        """
        
        

        self._rule_ids = None
        self._defense_action = None
        self.discriminator = None

        if rule_ids is not None:
            self.rule_ids = rule_ids
        if defense_action is not None:
            self.defense_action = defense_action

    @property
    def rule_ids(self):
        r"""Gets the rule_ids of this BatchUpdateBotMRuleActionRequestBody.

        **参数解释：** 批量更新的规则ID，包含需要修改防护动作的多条BotM规则ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The rule_ids of this BatchUpdateBotMRuleActionRequestBody.
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        r"""Sets the rule_ids of this BatchUpdateBotMRuleActionRequestBody.

        **参数解释：** 批量更新的规则ID，包含需要修改防护动作的多条BotM规则ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param rule_ids: The rule_ids of this BatchUpdateBotMRuleActionRequestBody.
        :type rule_ids: list[str]
        """
        self._rule_ids = rule_ids

    @property
    def defense_action(self):
        r"""Gets the defense_action of this BatchUpdateBotMRuleActionRequestBody.

        **参数解释：** 批量更新的防护动作对应的数字，101-拦截、102-放行、103-观察、104-验证码、201-重定向、202-返回自定义页面、301-拉黑IP **约束限制：** 不涉及 **取值范围：** - 101：拦截 - 102：放行 - 103：观察 - 104：验证码 - 201：重定向 - 202：返回自定义页面 - 301：拉黑IP **默认取值：** 不涉及

        :return: The defense_action of this BatchUpdateBotMRuleActionRequestBody.
        :rtype: int
        """
        return self._defense_action

    @defense_action.setter
    def defense_action(self, defense_action):
        r"""Sets the defense_action of this BatchUpdateBotMRuleActionRequestBody.

        **参数解释：** 批量更新的防护动作对应的数字，101-拦截、102-放行、103-观察、104-验证码、201-重定向、202-返回自定义页面、301-拉黑IP **约束限制：** 不涉及 **取值范围：** - 101：拦截 - 102：放行 - 103：观察 - 104：验证码 - 201：重定向 - 202：返回自定义页面 - 301：拉黑IP **默认取值：** 不涉及

        :param defense_action: The defense_action of this BatchUpdateBotMRuleActionRequestBody.
        :type defense_action: int
        """
        self._defense_action = defense_action

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchUpdateBotMRuleActionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
