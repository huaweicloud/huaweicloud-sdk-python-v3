# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomRuleValueInfo:

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
        'hash_type': 'str',
        'auto_block': 'int',
        'rule_values': 'list[str]'
    }

    attribute_map = {
        'rule_type': 'rule_type',
        'hash_type': 'hash_type',
        'auto_block': 'auto_block',
        'rule_values': 'rule_values'
    }

    def __init__(self, rule_type=None, hash_type=None, auto_block=None, rule_values=None):
        r"""CustomRuleValueInfo

        The model defined in huaweicloud sdk

        :param rule_type: **参数解释**： 规则类型 **约束限制**： 必填 **取值范围**： - black_hash：黑hash  **默认取值**： 不涉及 
        :type rule_type: str
        :param hash_type: **参数解释**： hash类型 **约束限制**： 必填 **取值范围**： - SHA-256：sha256sum - MD5：md5sum - SHA-1：sha1sum  **默认取值**： 不涉及 
        :type hash_type: str
        :param auto_block: **参数解释**： 是否自动阻断告警 **约束限制**： 必填 **取值范围**： - 0：不自动阻断告警 - 1：自动阻断告警  **默认取值**： 不涉及 
        :type auto_block: int
        :param rule_values: **参数解释**： 规则集列表 **约束限制**: 必填 **取值范围**: 1-1000个规则值 **默认取值**: 不涉及 
        :type rule_values: list[str]
        """
        
        

        self._rule_type = None
        self._hash_type = None
        self._auto_block = None
        self._rule_values = None
        self.discriminator = None

        self.rule_type = rule_type
        self.hash_type = hash_type
        self.auto_block = auto_block
        self.rule_values = rule_values

    @property
    def rule_type(self):
        r"""Gets the rule_type of this CustomRuleValueInfo.

        **参数解释**： 规则类型 **约束限制**： 必填 **取值范围**： - black_hash：黑hash  **默认取值**： 不涉及 

        :return: The rule_type of this CustomRuleValueInfo.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this CustomRuleValueInfo.

        **参数解释**： 规则类型 **约束限制**： 必填 **取值范围**： - black_hash：黑hash  **默认取值**： 不涉及 

        :param rule_type: The rule_type of this CustomRuleValueInfo.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def hash_type(self):
        r"""Gets the hash_type of this CustomRuleValueInfo.

        **参数解释**： hash类型 **约束限制**： 必填 **取值范围**： - SHA-256：sha256sum - MD5：md5sum - SHA-1：sha1sum  **默认取值**： 不涉及 

        :return: The hash_type of this CustomRuleValueInfo.
        :rtype: str
        """
        return self._hash_type

    @hash_type.setter
    def hash_type(self, hash_type):
        r"""Sets the hash_type of this CustomRuleValueInfo.

        **参数解释**： hash类型 **约束限制**： 必填 **取值范围**： - SHA-256：sha256sum - MD5：md5sum - SHA-1：sha1sum  **默认取值**： 不涉及 

        :param hash_type: The hash_type of this CustomRuleValueInfo.
        :type hash_type: str
        """
        self._hash_type = hash_type

    @property
    def auto_block(self):
        r"""Gets the auto_block of this CustomRuleValueInfo.

        **参数解释**： 是否自动阻断告警 **约束限制**： 必填 **取值范围**： - 0：不自动阻断告警 - 1：自动阻断告警  **默认取值**： 不涉及 

        :return: The auto_block of this CustomRuleValueInfo.
        :rtype: int
        """
        return self._auto_block

    @auto_block.setter
    def auto_block(self, auto_block):
        r"""Sets the auto_block of this CustomRuleValueInfo.

        **参数解释**： 是否自动阻断告警 **约束限制**： 必填 **取值范围**： - 0：不自动阻断告警 - 1：自动阻断告警  **默认取值**： 不涉及 

        :param auto_block: The auto_block of this CustomRuleValueInfo.
        :type auto_block: int
        """
        self._auto_block = auto_block

    @property
    def rule_values(self):
        r"""Gets the rule_values of this CustomRuleValueInfo.

        **参数解释**： 规则集列表 **约束限制**: 必填 **取值范围**: 1-1000个规则值 **默认取值**: 不涉及 

        :return: The rule_values of this CustomRuleValueInfo.
        :rtype: list[str]
        """
        return self._rule_values

    @rule_values.setter
    def rule_values(self, rule_values):
        r"""Sets the rule_values of this CustomRuleValueInfo.

        **参数解释**： 规则集列表 **约束限制**: 必填 **取值范围**: 1-1000个规则值 **默认取值**: 不涉及 

        :param rule_values: The rule_values of this CustomRuleValueInfo.
        :type rule_values: list[str]
        """
        self._rule_values = rule_values

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
        if not isinstance(other, CustomRuleValueInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
