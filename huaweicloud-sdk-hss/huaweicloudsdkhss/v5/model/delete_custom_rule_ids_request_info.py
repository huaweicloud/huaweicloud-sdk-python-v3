# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCustomRuleIdsRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id_list': 'list[str]'
    }

    attribute_map = {
        'rule_id_list': 'rule_id_list'
    }

    def __init__(self, rule_id_list=None):
        r"""DeleteCustomRuleIdsRequestInfo

        The model defined in huaweicloud sdk

        :param rule_id_list: **参数解释**： 规则ID列表 **约束限制**: 必填 **取值范围**: 1-1000个规则ID **默认取值**: 不涉及 
        :type rule_id_list: list[str]
        """
        
        

        self._rule_id_list = None
        self.discriminator = None

        self.rule_id_list = rule_id_list

    @property
    def rule_id_list(self):
        r"""Gets the rule_id_list of this DeleteCustomRuleIdsRequestInfo.

        **参数解释**： 规则ID列表 **约束限制**: 必填 **取值范围**: 1-1000个规则ID **默认取值**: 不涉及 

        :return: The rule_id_list of this DeleteCustomRuleIdsRequestInfo.
        :rtype: list[str]
        """
        return self._rule_id_list

    @rule_id_list.setter
    def rule_id_list(self, rule_id_list):
        r"""Sets the rule_id_list of this DeleteCustomRuleIdsRequestInfo.

        **参数解释**： 规则ID列表 **约束限制**: 必填 **取值范围**: 1-1000个规则ID **默认取值**: 不涉及 

        :param rule_id_list: The rule_id_list of this DeleteCustomRuleIdsRequestInfo.
        :type rule_id_list: list[str]
        """
        self._rule_id_list = rule_id_list

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
        if not isinstance(other, DeleteCustomRuleIdsRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
