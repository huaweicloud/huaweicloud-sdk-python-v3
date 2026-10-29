# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigTemplateRuleSetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'rule_set_id': 'str'
    }

    attribute_map = {
        'language': 'language',
        'rule_set_id': 'ruleSetId'
    }

    def __init__(self, language=None, rule_set_id=None):
        r"""ConfigTemplateRuleSetInfo

        The model defined in huaweicloud sdk

        :param language: **参数解释：** 语言类型。 **取值范围：** 自定义语言或者系统内置语言，当前支持的系统内置语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES
        :type language: str
        :param rule_set_id: **参数解释：** 规则集ID。 **取值范围：** 长度为[1~32]个字符。
        :type rule_set_id: str
        """
        
        

        self._language = None
        self._rule_set_id = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if rule_set_id is not None:
            self.rule_set_id = rule_set_id

    @property
    def language(self):
        r"""Gets the language of this ConfigTemplateRuleSetInfo.

        **参数解释：** 语言类型。 **取值范围：** 自定义语言或者系统内置语言，当前支持的系统内置语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES

        :return: The language of this ConfigTemplateRuleSetInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ConfigTemplateRuleSetInfo.

        **参数解释：** 语言类型。 **取值范围：** 自定义语言或者系统内置语言，当前支持的系统内置语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES

        :param language: The language of this ConfigTemplateRuleSetInfo.
        :type language: str
        """
        self._language = language

    @property
    def rule_set_id(self):
        r"""Gets the rule_set_id of this ConfigTemplateRuleSetInfo.

        **参数解释：** 规则集ID。 **取值范围：** 长度为[1~32]个字符。

        :return: The rule_set_id of this ConfigTemplateRuleSetInfo.
        :rtype: str
        """
        return self._rule_set_id

    @rule_set_id.setter
    def rule_set_id(self, rule_set_id):
        r"""Sets the rule_set_id of this ConfigTemplateRuleSetInfo.

        **参数解释：** 规则集ID。 **取值范围：** 长度为[1~32]个字符。

        :param rule_set_id: The rule_set_id of this ConfigTemplateRuleSetInfo.
        :type rule_set_id: str
        """
        self._rule_set_id = rule_set_id

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
        if not isinstance(other, ConfigTemplateRuleSetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
