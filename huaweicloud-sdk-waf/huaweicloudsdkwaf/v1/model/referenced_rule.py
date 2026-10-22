# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReferencedRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'rule_name': 'str',
        'policy_id': 'str',
        'policy_name': 'str',
        'detect_opts_type': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'detect_opts_type': 'detect_opts_type'
    }

    def __init__(self, rule_id=None, rule_name=None, policy_id=None, policy_name=None, detect_opts_type=None):
        r"""ReferencedRule

        The model defined in huaweicloud sdk

        :param rule_id: 规则ID
        :type rule_id: str
        :param rule_name: 策略名称
        :type rule_name: str
        :param policy_id: 引用该代答库的规则所属策略ID
        :type policy_id: str
        :param policy_name: 引用该代答库的规则所属策略名称
        :type policy_name: str
        :param detect_opts_type: 规则检测选项类型，可选：lexicon(词库检测), compliance(合规检测), inject(注入检测), immunity_lexicon(豁免词库), supported_language(语言检测), pii(PII检测), abuse(算力滥用检测), topic_detect(话题检测)等
        :type detect_opts_type: str
        """
        
        

        self._rule_id = None
        self._rule_name = None
        self._policy_id = None
        self._policy_name = None
        self._detect_opts_type = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if detect_opts_type is not None:
            self.detect_opts_type = detect_opts_type

    @property
    def rule_id(self):
        r"""Gets the rule_id of this ReferencedRule.

        规则ID

        :return: The rule_id of this ReferencedRule.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this ReferencedRule.

        规则ID

        :param rule_id: The rule_id of this ReferencedRule.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ReferencedRule.

        策略名称

        :return: The rule_name of this ReferencedRule.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ReferencedRule.

        策略名称

        :param rule_name: The rule_name of this ReferencedRule.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ReferencedRule.

        引用该代答库的规则所属策略ID

        :return: The policy_id of this ReferencedRule.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ReferencedRule.

        引用该代答库的规则所属策略ID

        :param policy_id: The policy_id of this ReferencedRule.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this ReferencedRule.

        引用该代答库的规则所属策略名称

        :return: The policy_name of this ReferencedRule.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this ReferencedRule.

        引用该代答库的规则所属策略名称

        :param policy_name: The policy_name of this ReferencedRule.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def detect_opts_type(self):
        r"""Gets the detect_opts_type of this ReferencedRule.

        规则检测选项类型，可选：lexicon(词库检测), compliance(合规检测), inject(注入检测), immunity_lexicon(豁免词库), supported_language(语言检测), pii(PII检测), abuse(算力滥用检测), topic_detect(话题检测)等

        :return: The detect_opts_type of this ReferencedRule.
        :rtype: str
        """
        return self._detect_opts_type

    @detect_opts_type.setter
    def detect_opts_type(self, detect_opts_type):
        r"""Sets the detect_opts_type of this ReferencedRule.

        规则检测选项类型，可选：lexicon(词库检测), compliance(合规检测), inject(注入检测), immunity_lexicon(豁免词库), supported_language(语言检测), pii(PII检测), abuse(算力滥用检测), topic_detect(话题检测)等

        :param detect_opts_type: The detect_opts_type of this ReferencedRule.
        :type detect_opts_type: str
        """
        self._detect_opts_type = detect_opts_type

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
        if not isinstance(other, ReferencedRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
