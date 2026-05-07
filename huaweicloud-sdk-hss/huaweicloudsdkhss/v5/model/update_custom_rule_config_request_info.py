# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomRuleConfigRequestInfo:

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
        'is_all_host': 'bool',
        'custom_rule_value_info': 'CustomRuleValueInfo',
        'agent_ids': 'list[str]',
        'rule_id': 'str'
    }

    attribute_map = {
        'rule_name': 'rule_name',
        'is_all_host': 'is_all_host',
        'custom_rule_value_info': 'custom_rule_value_info',
        'agent_ids': 'agent_ids',
        'rule_id': 'rule_id'
    }

    def __init__(self, rule_name=None, is_all_host=None, custom_rule_value_info=None, agent_ids=None, rule_id=None):
        r"""UpdateCustomRuleConfigRequestInfo

        The model defined in huaweicloud sdk

        :param rule_name: **参数解释**： 规则名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 
        :type rule_name: str
        :param is_all_host: **参数解释**: 是否选择所有主机 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: false 
        :type is_all_host: bool
        :param custom_rule_value_info: 
        :type custom_rule_value_info: :class:`huaweicloudsdkhss.v5.CustomRuleValueInfo`
        :param agent_ids: **参数解释**: agent列表 **约束限制**: 不涉及 **取值范围**: 1-1000个agentID **默认取值**: 不涉及 
        :type agent_ids: list[str]
        :param rule_id: **参数解释**： 规则ID **约束限制**： 必填 **取值范围**： 字符长度1-36位 **默认取值**： 不涉及 
        :type rule_id: str
        """
        
        

        self._rule_name = None
        self._is_all_host = None
        self._custom_rule_value_info = None
        self._agent_ids = None
        self._rule_id = None
        self.discriminator = None

        self.rule_name = rule_name
        if is_all_host is not None:
            self.is_all_host = is_all_host
        self.custom_rule_value_info = custom_rule_value_info
        if agent_ids is not None:
            self.agent_ids = agent_ids
        self.rule_id = rule_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this UpdateCustomRuleConfigRequestInfo.

        **参数解释**： 规则名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :return: The rule_name of this UpdateCustomRuleConfigRequestInfo.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this UpdateCustomRuleConfigRequestInfo.

        **参数解释**： 规则名称 **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :param rule_name: The rule_name of this UpdateCustomRuleConfigRequestInfo.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def is_all_host(self):
        r"""Gets the is_all_host of this UpdateCustomRuleConfigRequestInfo.

        **参数解释**: 是否选择所有主机 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: false 

        :return: The is_all_host of this UpdateCustomRuleConfigRequestInfo.
        :rtype: bool
        """
        return self._is_all_host

    @is_all_host.setter
    def is_all_host(self, is_all_host):
        r"""Sets the is_all_host of this UpdateCustomRuleConfigRequestInfo.

        **参数解释**: 是否选择所有主机 **约束限制**: 不涉及 **取值范围**: - true：是 - false：否  **默认取值**: false 

        :param is_all_host: The is_all_host of this UpdateCustomRuleConfigRequestInfo.
        :type is_all_host: bool
        """
        self._is_all_host = is_all_host

    @property
    def custom_rule_value_info(self):
        r"""Gets the custom_rule_value_info of this UpdateCustomRuleConfigRequestInfo.

        :return: The custom_rule_value_info of this UpdateCustomRuleConfigRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.CustomRuleValueInfo`
        """
        return self._custom_rule_value_info

    @custom_rule_value_info.setter
    def custom_rule_value_info(self, custom_rule_value_info):
        r"""Sets the custom_rule_value_info of this UpdateCustomRuleConfigRequestInfo.

        :param custom_rule_value_info: The custom_rule_value_info of this UpdateCustomRuleConfigRequestInfo.
        :type custom_rule_value_info: :class:`huaweicloudsdkhss.v5.CustomRuleValueInfo`
        """
        self._custom_rule_value_info = custom_rule_value_info

    @property
    def agent_ids(self):
        r"""Gets the agent_ids of this UpdateCustomRuleConfigRequestInfo.

        **参数解释**: agent列表 **约束限制**: 不涉及 **取值范围**: 1-1000个agentID **默认取值**: 不涉及 

        :return: The agent_ids of this UpdateCustomRuleConfigRequestInfo.
        :rtype: list[str]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        r"""Sets the agent_ids of this UpdateCustomRuleConfigRequestInfo.

        **参数解释**: agent列表 **约束限制**: 不涉及 **取值范围**: 1-1000个agentID **默认取值**: 不涉及 

        :param agent_ids: The agent_ids of this UpdateCustomRuleConfigRequestInfo.
        :type agent_ids: list[str]
        """
        self._agent_ids = agent_ids

    @property
    def rule_id(self):
        r"""Gets the rule_id of this UpdateCustomRuleConfigRequestInfo.

        **参数解释**： 规则ID **约束限制**： 必填 **取值范围**： 字符长度1-36位 **默认取值**： 不涉及 

        :return: The rule_id of this UpdateCustomRuleConfigRequestInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this UpdateCustomRuleConfigRequestInfo.

        **参数解释**： 规则ID **约束限制**： 必填 **取值范围**： 字符长度1-36位 **默认取值**： 不涉及 

        :param rule_id: The rule_id of this UpdateCustomRuleConfigRequestInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

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
        if not isinstance(other, UpdateCustomRuleConfigRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
