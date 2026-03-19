# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateIgnoreRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'list[str]',
        'conditions': 'list[CreateCondition]',
        'mode': 'int',
        'rule': 'str',
        'advanced': 'IgnoreAdvanced',
        'description': 'str',
        'policy_rule_ids': 'list[BatchUpdateIgnoreRuleRequestBodyPolicyRuleIds]'
    }

    attribute_map = {
        'domain': 'domain',
        'conditions': 'conditions',
        'mode': 'mode',
        'rule': 'rule',
        'advanced': 'advanced',
        'description': 'description',
        'policy_rule_ids': 'policy_rule_ids'
    }

    def __init__(self, domain=None, conditions=None, mode=None, rule=None, advanced=None, description=None, policy_rule_ids=None):
        r"""BatchUpdateIgnoreRuleRequestBody

        The model defined in huaweicloud sdk

        :param domain: 防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效
        :type domain: list[str]
        :param conditions: 条件列表
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        :param mode: 固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建
        :type mode: int
        :param rule: **参数解释：** 需要屏蔽的规则 **约束限制：** 参数值根据\&quot;不检测模块\&quot;变化 **取值范围：** 不检测模块: - 所有模块: bypass - Web基础防护模块按照规则类型划分:   - ID: 内置规则id，通过ListWebBasicProtectionRules接口获取ID，多个id以分号;分隔，比如：\&quot;000000;111111\&quot;   - 类别: 多个类型以分号;分隔，比如：\&quot;xss;webshell\&quot;     - xss：XSS攻击     - webshell：网站木马     - vuln：其他类型攻击     - sqli：SQL注入攻击     - robot：恶意爬虫     - rfi：远程文件包含     - lfi：本地文件包含     - cmdi：命令注入攻击   - 所有内置规则 - 非法请求: illegal **默认取值：** 不涉及
        :type rule: str
        :param advanced: 
        :type advanced: :class:`huaweicloudsdkwaf.v1.IgnoreAdvanced`
        :param description: 屏蔽规则描述
        :type description: str
        :param policy_rule_ids: **参数解释：** 策略ID和规则id数组，规则ID与规则所属的策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_rule_ids: list[:class:`huaweicloudsdkwaf.v1.BatchUpdateIgnoreRuleRequestBodyPolicyRuleIds`]
        """
        
        

        self._domain = None
        self._conditions = None
        self._mode = None
        self._rule = None
        self._advanced = None
        self._description = None
        self._policy_rule_ids = None
        self.discriminator = None

        self.domain = domain
        self.conditions = conditions
        self.mode = mode
        self.rule = rule
        if advanced is not None:
            self.advanced = advanced
        if description is not None:
            self.description = description
        self.policy_rule_ids = policy_rule_ids

    @property
    def domain(self):
        r"""Gets the domain of this BatchUpdateIgnoreRuleRequestBody.

        防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效

        :return: The domain of this BatchUpdateIgnoreRuleRequestBody.
        :rtype: list[str]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this BatchUpdateIgnoreRuleRequestBody.

        防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效

        :param domain: The domain of this BatchUpdateIgnoreRuleRequestBody.
        :type domain: list[str]
        """
        self._domain = domain

    @property
    def conditions(self):
        r"""Gets the conditions of this BatchUpdateIgnoreRuleRequestBody.

        条件列表

        :return: The conditions of this BatchUpdateIgnoreRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this BatchUpdateIgnoreRuleRequestBody.

        条件列表

        :param conditions: The conditions of this BatchUpdateIgnoreRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        """
        self._conditions = conditions

    @property
    def mode(self):
        r"""Gets the mode of this BatchUpdateIgnoreRuleRequestBody.

        固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建

        :return: The mode of this BatchUpdateIgnoreRuleRequestBody.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this BatchUpdateIgnoreRuleRequestBody.

        固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建

        :param mode: The mode of this BatchUpdateIgnoreRuleRequestBody.
        :type mode: int
        """
        self._mode = mode

    @property
    def rule(self):
        r"""Gets the rule of this BatchUpdateIgnoreRuleRequestBody.

        **参数解释：** 需要屏蔽的规则 **约束限制：** 参数值根据\"不检测模块\"变化 **取值范围：** 不检测模块: - 所有模块: bypass - Web基础防护模块按照规则类型划分:   - ID: 内置规则id，通过ListWebBasicProtectionRules接口获取ID，多个id以分号;分隔，比如：\"000000;111111\"   - 类别: 多个类型以分号;分隔，比如：\"xss;webshell\"     - xss：XSS攻击     - webshell：网站木马     - vuln：其他类型攻击     - sqli：SQL注入攻击     - robot：恶意爬虫     - rfi：远程文件包含     - lfi：本地文件包含     - cmdi：命令注入攻击   - 所有内置规则 - 非法请求: illegal **默认取值：** 不涉及

        :return: The rule of this BatchUpdateIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this BatchUpdateIgnoreRuleRequestBody.

        **参数解释：** 需要屏蔽的规则 **约束限制：** 参数值根据\"不检测模块\"变化 **取值范围：** 不检测模块: - 所有模块: bypass - Web基础防护模块按照规则类型划分:   - ID: 内置规则id，通过ListWebBasicProtectionRules接口获取ID，多个id以分号;分隔，比如：\"000000;111111\"   - 类别: 多个类型以分号;分隔，比如：\"xss;webshell\"     - xss：XSS攻击     - webshell：网站木马     - vuln：其他类型攻击     - sqli：SQL注入攻击     - robot：恶意爬虫     - rfi：远程文件包含     - lfi：本地文件包含     - cmdi：命令注入攻击   - 所有内置规则 - 非法请求: illegal **默认取值：** 不涉及

        :param rule: The rule of this BatchUpdateIgnoreRuleRequestBody.
        :type rule: str
        """
        self._rule = rule

    @property
    def advanced(self):
        r"""Gets the advanced of this BatchUpdateIgnoreRuleRequestBody.

        :return: The advanced of this BatchUpdateIgnoreRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.IgnoreAdvanced`
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        r"""Sets the advanced of this BatchUpdateIgnoreRuleRequestBody.

        :param advanced: The advanced of this BatchUpdateIgnoreRuleRequestBody.
        :type advanced: :class:`huaweicloudsdkwaf.v1.IgnoreAdvanced`
        """
        self._advanced = advanced

    @property
    def description(self):
        r"""Gets the description of this BatchUpdateIgnoreRuleRequestBody.

        屏蔽规则描述

        :return: The description of this BatchUpdateIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchUpdateIgnoreRuleRequestBody.

        屏蔽规则描述

        :param description: The description of this BatchUpdateIgnoreRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def policy_rule_ids(self):
        r"""Gets the policy_rule_ids of this BatchUpdateIgnoreRuleRequestBody.

        **参数解释：** 策略ID和规则id数组，规则ID与规则所属的策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_rule_ids of this BatchUpdateIgnoreRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.BatchUpdateIgnoreRuleRequestBodyPolicyRuleIds`]
        """
        return self._policy_rule_ids

    @policy_rule_ids.setter
    def policy_rule_ids(self, policy_rule_ids):
        r"""Sets the policy_rule_ids of this BatchUpdateIgnoreRuleRequestBody.

        **参数解释：** 策略ID和规则id数组，规则ID与规则所属的策略ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_rule_ids: The policy_rule_ids of this BatchUpdateIgnoreRuleRequestBody.
        :type policy_rule_ids: list[:class:`huaweicloudsdkwaf.v1.BatchUpdateIgnoreRuleRequestBodyPolicyRuleIds`]
        """
        self._policy_rule_ids = policy_rule_ids

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
        if not isinstance(other, BatchUpdateIgnoreRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
