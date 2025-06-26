# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddExceptRuleReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_name': 'str',
        'except_rules': 'list[ExceptRule]'
    }

    attribute_map = {
        'rule_name': 'rule_name',
        'except_rules': 'except_rules'
    }

    def __init__(self, rule_name=None, except_rules=None):
        r"""AddExceptRuleReq

        The model defined in huaweicloud sdk

        :param rule_name: **参数解释**： 异常规则名称。 **约束限制**： 名称不能为空。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type rule_name: str
        :param except_rules: **参数解释**： 异常规则配置项。 **约束限制**： 不能为空。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type except_rules: list[:class:`huaweicloudsdkdws.v2.ExceptRule`]
        """
        
        

        self._rule_name = None
        self._except_rules = None
        self.discriminator = None

        if rule_name is not None:
            self.rule_name = rule_name
        if except_rules is not None:
            self.except_rules = except_rules

    @property
    def rule_name(self):
        r"""Gets the rule_name of this AddExceptRuleReq.

        **参数解释**： 异常规则名称。 **约束限制**： 名称不能为空。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The rule_name of this AddExceptRuleReq.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this AddExceptRuleReq.

        **参数解释**： 异常规则名称。 **约束限制**： 名称不能为空。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param rule_name: The rule_name of this AddExceptRuleReq.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def except_rules(self):
        r"""Gets the except_rules of this AddExceptRuleReq.

        **参数解释**： 异常规则配置项。 **约束限制**： 不能为空。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The except_rules of this AddExceptRuleReq.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ExceptRule`]
        """
        return self._except_rules

    @except_rules.setter
    def except_rules(self, except_rules):
        r"""Sets the except_rules of this AddExceptRuleReq.

        **参数解释**： 异常规则配置项。 **约束限制**： 不能为空。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param except_rules: The except_rules of this AddExceptRuleReq.
        :type except_rules: list[:class:`huaweicloudsdkdws.v2.ExceptRule`]
        """
        self._except_rules = except_rules

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
        if not isinstance(other, AddExceptRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
