# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRuleFixValuesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_param_id': 'int',
        'fix_value': 'int'
    }

    attribute_map = {
        'rule_param_id': 'rule_param_id',
        'fix_value': 'fix_value'
    }

    def __init__(self, rule_param_id=None, fix_value=None):
        r"""CheckRuleFixValuesInfo

        The model defined in huaweicloud sdk

        :param rule_param_id: **参数解释**: 检查项的参数ID **约束限制**: 不涉及 **取值范围**: 字符串大小范围1-128 **默认取值**: 不涉及 
        :type rule_param_id: int
        :param fix_value: **参数解释**: 修复检查项参数具体值 **约束限制**: 不涉及 **取值范围**: 字符串大小范围0-512 **默认取值**: 不涉及 
        :type fix_value: int
        """
        
        

        self._rule_param_id = None
        self._fix_value = None
        self.discriminator = None

        if rule_param_id is not None:
            self.rule_param_id = rule_param_id
        if fix_value is not None:
            self.fix_value = fix_value

    @property
    def rule_param_id(self):
        r"""Gets the rule_param_id of this CheckRuleFixValuesInfo.

        **参数解释**: 检查项的参数ID **约束限制**: 不涉及 **取值范围**: 字符串大小范围1-128 **默认取值**: 不涉及 

        :return: The rule_param_id of this CheckRuleFixValuesInfo.
        :rtype: int
        """
        return self._rule_param_id

    @rule_param_id.setter
    def rule_param_id(self, rule_param_id):
        r"""Sets the rule_param_id of this CheckRuleFixValuesInfo.

        **参数解释**: 检查项的参数ID **约束限制**: 不涉及 **取值范围**: 字符串大小范围1-128 **默认取值**: 不涉及 

        :param rule_param_id: The rule_param_id of this CheckRuleFixValuesInfo.
        :type rule_param_id: int
        """
        self._rule_param_id = rule_param_id

    @property
    def fix_value(self):
        r"""Gets the fix_value of this CheckRuleFixValuesInfo.

        **参数解释**: 修复检查项参数具体值 **约束限制**: 不涉及 **取值范围**: 字符串大小范围0-512 **默认取值**: 不涉及 

        :return: The fix_value of this CheckRuleFixValuesInfo.
        :rtype: int
        """
        return self._fix_value

    @fix_value.setter
    def fix_value(self, fix_value):
        r"""Sets the fix_value of this CheckRuleFixValuesInfo.

        **参数解释**: 修复检查项参数具体值 **约束限制**: 不涉及 **取值范围**: 字符串大小范围0-512 **默认取值**: 不涉及 

        :param fix_value: The fix_value of this CheckRuleFixValuesInfo.
        :type fix_value: int
        """
        self._fix_value = fix_value

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
        if not isinstance(other, CheckRuleFixValuesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
