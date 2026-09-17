# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlertRuleDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_type': 'str',
        'threshold_value': 'int',
        'severity': 'str',
        'is_enabled': 'bool'
    }

    attribute_map = {
        'rule_type': 'ruleType',
        'threshold_value': 'thresholdValue',
        'severity': 'severity',
        'is_enabled': 'isEnabled'
    }

    def __init__(self, rule_type=None, threshold_value=None, severity=None, is_enabled=None):
        r"""AlertRuleDTO

        The model defined in huaweicloud sdk

        :param rule_type: **参数解释**： 规则类型。 **约束限制**： 不涉及。 **取值范围**： - CONCURRENCY：并发数。 - FAIL_COUNT：失败次数。 - QUEUE_BACKLOG：队列积压。 **默认取值**： 不涉及。 
        :type rule_type: str
        :param threshold_value: **参数解释**： 阈值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type threshold_value: int
        :param severity: **参数解释**： 严重级别。 **约束限制**： 不涉及。 **取值范围**： - GENERAL：一般。 - WARNING：警告。 - MAJOR：严重。 **默认取值**： 不涉及。 
        :type severity: str
        :param is_enabled: **参数解释**： 是否启用。 **约束限制**： 不涉及。 **取值范围**： - true：启用。 - false：禁用。 **默认取值**： 不涉及。 
        :type is_enabled: bool
        """
        
        

        self._rule_type = None
        self._threshold_value = None
        self._severity = None
        self._is_enabled = None
        self.discriminator = None

        if rule_type is not None:
            self.rule_type = rule_type
        if threshold_value is not None:
            self.threshold_value = threshold_value
        if severity is not None:
            self.severity = severity
        if is_enabled is not None:
            self.is_enabled = is_enabled

    @property
    def rule_type(self):
        r"""Gets the rule_type of this AlertRuleDTO.

        **参数解释**： 规则类型。 **约束限制**： 不涉及。 **取值范围**： - CONCURRENCY：并发数。 - FAIL_COUNT：失败次数。 - QUEUE_BACKLOG：队列积压。 **默认取值**： 不涉及。 

        :return: The rule_type of this AlertRuleDTO.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this AlertRuleDTO.

        **参数解释**： 规则类型。 **约束限制**： 不涉及。 **取值范围**： - CONCURRENCY：并发数。 - FAIL_COUNT：失败次数。 - QUEUE_BACKLOG：队列积压。 **默认取值**： 不涉及。 

        :param rule_type: The rule_type of this AlertRuleDTO.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def threshold_value(self):
        r"""Gets the threshold_value of this AlertRuleDTO.

        **参数解释**： 阈值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The threshold_value of this AlertRuleDTO.
        :rtype: int
        """
        return self._threshold_value

    @threshold_value.setter
    def threshold_value(self, threshold_value):
        r"""Sets the threshold_value of this AlertRuleDTO.

        **参数解释**： 阈值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param threshold_value: The threshold_value of this AlertRuleDTO.
        :type threshold_value: int
        """
        self._threshold_value = threshold_value

    @property
    def severity(self):
        r"""Gets the severity of this AlertRuleDTO.

        **参数解释**： 严重级别。 **约束限制**： 不涉及。 **取值范围**： - GENERAL：一般。 - WARNING：警告。 - MAJOR：严重。 **默认取值**： 不涉及。 

        :return: The severity of this AlertRuleDTO.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this AlertRuleDTO.

        **参数解释**： 严重级别。 **约束限制**： 不涉及。 **取值范围**： - GENERAL：一般。 - WARNING：警告。 - MAJOR：严重。 **默认取值**： 不涉及。 

        :param severity: The severity of this AlertRuleDTO.
        :type severity: str
        """
        self._severity = severity

    @property
    def is_enabled(self):
        r"""Gets the is_enabled of this AlertRuleDTO.

        **参数解释**： 是否启用。 **约束限制**： 不涉及。 **取值范围**： - true：启用。 - false：禁用。 **默认取值**： 不涉及。 

        :return: The is_enabled of this AlertRuleDTO.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        r"""Sets the is_enabled of this AlertRuleDTO.

        **参数解释**： 是否启用。 **约束限制**： 不涉及。 **取值范围**： - true：启用。 - false：禁用。 **默认取值**： 不涉及。 

        :param is_enabled: The is_enabled of this AlertRuleDTO.
        :type is_enabled: bool
        """
        self._is_enabled = is_enabled

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
        if not isinstance(other, AlertRuleDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
