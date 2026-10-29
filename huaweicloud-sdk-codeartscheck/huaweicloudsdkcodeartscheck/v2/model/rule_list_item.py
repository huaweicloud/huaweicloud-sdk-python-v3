# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleListItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_set': 'str',
        'rule_id': 'str',
        'rule_language': 'str',
        'rule_name': 'str',
        'rule_severity': 'str',
        'rule_tages': 'str',
        'right_example': 'str',
        'error_example': 'str',
        'revise_opinion': 'str',
        'rule_desc': 'str'
    }

    attribute_map = {
        'rule_set': 'rule_set',
        'rule_id': 'rule_id',
        'rule_language': 'rule_language',
        'rule_name': 'rule_name',
        'rule_severity': 'rule_severity',
        'rule_tages': 'rule_tages',
        'right_example': 'right_example',
        'error_example': 'error_example',
        'revise_opinion': 'revise_opinion',
        'rule_desc': 'rule_desc'
    }

    def __init__(self, rule_set=None, rule_id=None, rule_language=None, rule_name=None, rule_severity=None, rule_tages=None, right_example=None, error_example=None, revise_opinion=None, rule_desc=None):
        r"""RuleListItem

        The model defined in huaweicloud sdk

        :param rule_set: **参数解释：** 业务类型分类。 **取值范围:** - common：通用。 - common_standard_recommend：通用建议。 - common_standard_rule：通用规则。 - security：安全。 - security_standard_recommend：安全建议。 - security_standard_rule：安全规则。
        :type rule_set: str
        :param rule_id: **参数解释:** 规则ID。 **取值范围:** 32位UUID。
        :type rule_id: str
        :param rule_language: **参数解释:** 规则所属语言。 **取值范围:** 当前支持的语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES
        :type rule_language: str
        :param rule_name: **参数解释:** 规则名称。 **取值范围:** 不涉及。
        :type rule_name: str
        :param rule_severity: **参数解释:** 规则问题级别。 **取值范围:** - 0：致命。 - 1：严重。 - 2：一般。 - 3：提示。
        :type rule_severity: str
        :param rule_tages: **参数解释:** 规则标签。 **取值范围:** - huawei - iso5055 - cert - cwe - top10 - top25 - misra - GJB - autosar - PCI DSS
        :type rule_tages: str
        :param right_example: **参数解释:** 正确示例。 **取值范围:** 代码块或者文字示例等。
        :type right_example: str
        :param error_example: **参数解释:** 错误示例。 **取值范围:** 代码块或者文字示例等。
        :type error_example: str
        :param revise_opinion: **参数解释:** 修改建议。 **取值范围:** 代码块或者文字示例等。
        :type revise_opinion: str
        :param rule_desc: **参数解释:** 规则描述。 **取值范围:** 不涉及。
        :type rule_desc: str
        """
        
        

        self._rule_set = None
        self._rule_id = None
        self._rule_language = None
        self._rule_name = None
        self._rule_severity = None
        self._rule_tages = None
        self._right_example = None
        self._error_example = None
        self._revise_opinion = None
        self._rule_desc = None
        self.discriminator = None

        if rule_set is not None:
            self.rule_set = rule_set
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_language is not None:
            self.rule_language = rule_language
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_severity is not None:
            self.rule_severity = rule_severity
        if rule_tages is not None:
            self.rule_tages = rule_tages
        if right_example is not None:
            self.right_example = right_example
        if error_example is not None:
            self.error_example = error_example
        if revise_opinion is not None:
            self.revise_opinion = revise_opinion
        if rule_desc is not None:
            self.rule_desc = rule_desc

    @property
    def rule_set(self):
        r"""Gets the rule_set of this RuleListItem.

        **参数解释：** 业务类型分类。 **取值范围:** - common：通用。 - common_standard_recommend：通用建议。 - common_standard_rule：通用规则。 - security：安全。 - security_standard_recommend：安全建议。 - security_standard_rule：安全规则。

        :return: The rule_set of this RuleListItem.
        :rtype: str
        """
        return self._rule_set

    @rule_set.setter
    def rule_set(self, rule_set):
        r"""Sets the rule_set of this RuleListItem.

        **参数解释：** 业务类型分类。 **取值范围:** - common：通用。 - common_standard_recommend：通用建议。 - common_standard_rule：通用规则。 - security：安全。 - security_standard_recommend：安全建议。 - security_standard_rule：安全规则。

        :param rule_set: The rule_set of this RuleListItem.
        :type rule_set: str
        """
        self._rule_set = rule_set

    @property
    def rule_id(self):
        r"""Gets the rule_id of this RuleListItem.

        **参数解释:** 规则ID。 **取值范围:** 32位UUID。

        :return: The rule_id of this RuleListItem.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this RuleListItem.

        **参数解释:** 规则ID。 **取值范围:** 32位UUID。

        :param rule_id: The rule_id of this RuleListItem.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_language(self):
        r"""Gets the rule_language of this RuleListItem.

        **参数解释:** 规则所属语言。 **取值范围:** 当前支持的语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES

        :return: The rule_language of this RuleListItem.
        :rtype: str
        """
        return self._rule_language

    @rule_language.setter
    def rule_language(self, rule_language):
        r"""Sets the rule_language of this RuleListItem.

        **参数解释:** 规则所属语言。 **取值范围:** 当前支持的语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES

        :param rule_language: The rule_language of this RuleListItem.
        :type rule_language: str
        """
        self._rule_language = rule_language

    @property
    def rule_name(self):
        r"""Gets the rule_name of this RuleListItem.

        **参数解释:** 规则名称。 **取值范围:** 不涉及。

        :return: The rule_name of this RuleListItem.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this RuleListItem.

        **参数解释:** 规则名称。 **取值范围:** 不涉及。

        :param rule_name: The rule_name of this RuleListItem.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_severity(self):
        r"""Gets the rule_severity of this RuleListItem.

        **参数解释:** 规则问题级别。 **取值范围:** - 0：致命。 - 1：严重。 - 2：一般。 - 3：提示。

        :return: The rule_severity of this RuleListItem.
        :rtype: str
        """
        return self._rule_severity

    @rule_severity.setter
    def rule_severity(self, rule_severity):
        r"""Sets the rule_severity of this RuleListItem.

        **参数解释:** 规则问题级别。 **取值范围:** - 0：致命。 - 1：严重。 - 2：一般。 - 3：提示。

        :param rule_severity: The rule_severity of this RuleListItem.
        :type rule_severity: str
        """
        self._rule_severity = rule_severity

    @property
    def rule_tages(self):
        r"""Gets the rule_tages of this RuleListItem.

        **参数解释:** 规则标签。 **取值范围:** - huawei - iso5055 - cert - cwe - top10 - top25 - misra - GJB - autosar - PCI DSS

        :return: The rule_tages of this RuleListItem.
        :rtype: str
        """
        return self._rule_tages

    @rule_tages.setter
    def rule_tages(self, rule_tages):
        r"""Sets the rule_tages of this RuleListItem.

        **参数解释:** 规则标签。 **取值范围:** - huawei - iso5055 - cert - cwe - top10 - top25 - misra - GJB - autosar - PCI DSS

        :param rule_tages: The rule_tages of this RuleListItem.
        :type rule_tages: str
        """
        self._rule_tages = rule_tages

    @property
    def right_example(self):
        r"""Gets the right_example of this RuleListItem.

        **参数解释:** 正确示例。 **取值范围:** 代码块或者文字示例等。

        :return: The right_example of this RuleListItem.
        :rtype: str
        """
        return self._right_example

    @right_example.setter
    def right_example(self, right_example):
        r"""Sets the right_example of this RuleListItem.

        **参数解释:** 正确示例。 **取值范围:** 代码块或者文字示例等。

        :param right_example: The right_example of this RuleListItem.
        :type right_example: str
        """
        self._right_example = right_example

    @property
    def error_example(self):
        r"""Gets the error_example of this RuleListItem.

        **参数解释:** 错误示例。 **取值范围:** 代码块或者文字示例等。

        :return: The error_example of this RuleListItem.
        :rtype: str
        """
        return self._error_example

    @error_example.setter
    def error_example(self, error_example):
        r"""Sets the error_example of this RuleListItem.

        **参数解释:** 错误示例。 **取值范围:** 代码块或者文字示例等。

        :param error_example: The error_example of this RuleListItem.
        :type error_example: str
        """
        self._error_example = error_example

    @property
    def revise_opinion(self):
        r"""Gets the revise_opinion of this RuleListItem.

        **参数解释:** 修改建议。 **取值范围:** 代码块或者文字示例等。

        :return: The revise_opinion of this RuleListItem.
        :rtype: str
        """
        return self._revise_opinion

    @revise_opinion.setter
    def revise_opinion(self, revise_opinion):
        r"""Sets the revise_opinion of this RuleListItem.

        **参数解释:** 修改建议。 **取值范围:** 代码块或者文字示例等。

        :param revise_opinion: The revise_opinion of this RuleListItem.
        :type revise_opinion: str
        """
        self._revise_opinion = revise_opinion

    @property
    def rule_desc(self):
        r"""Gets the rule_desc of this RuleListItem.

        **参数解释:** 规则描述。 **取值范围:** 不涉及。

        :return: The rule_desc of this RuleListItem.
        :rtype: str
        """
        return self._rule_desc

    @rule_desc.setter
    def rule_desc(self, rule_desc):
        r"""Sets the rule_desc of this RuleListItem.

        **参数解释:** 规则描述。 **取值范围:** 不涉及。

        :param rule_desc: The rule_desc of this RuleListItem.
        :type rule_desc: str
        """
        self._rule_desc = rule_desc

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
        if not isinstance(other, RuleListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
