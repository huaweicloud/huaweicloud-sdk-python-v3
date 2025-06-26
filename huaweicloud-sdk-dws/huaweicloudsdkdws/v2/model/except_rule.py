# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExceptRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_key': 'str',
        'rule_value': 'str'
    }

    attribute_map = {
        'rule_key': 'rule_key',
        'rule_value': 'rule_value'
    }

    def __init__(self, rule_key=None, rule_value=None):
        r"""ExceptRule

        The model defined in huaweicloud sdk

        :param rule_key: **参数解释**： 规则项名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type rule_key: str
        :param rule_value: **参数解释**： 规则项数值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type rule_value: str
        """
        
        

        self._rule_key = None
        self._rule_value = None
        self.discriminator = None

        if rule_key is not None:
            self.rule_key = rule_key
        if rule_value is not None:
            self.rule_value = rule_value

    @property
    def rule_key(self):
        r"""Gets the rule_key of this ExceptRule.

        **参数解释**： 规则项名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The rule_key of this ExceptRule.
        :rtype: str
        """
        return self._rule_key

    @rule_key.setter
    def rule_key(self, rule_key):
        r"""Sets the rule_key of this ExceptRule.

        **参数解释**： 规则项名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param rule_key: The rule_key of this ExceptRule.
        :type rule_key: str
        """
        self._rule_key = rule_key

    @property
    def rule_value(self):
        r"""Gets the rule_value of this ExceptRule.

        **参数解释**： 规则项数值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The rule_value of this ExceptRule.
        :rtype: str
        """
        return self._rule_value

    @rule_value.setter
    def rule_value(self, rule_value):
        r"""Sets the rule_value of this ExceptRule.

        **参数解释**： 规则项数值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param rule_value: The rule_value of this ExceptRule.
        :type rule_value: str
        """
        self._rule_value = rule_value

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
        if not isinstance(other, ExceptRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
