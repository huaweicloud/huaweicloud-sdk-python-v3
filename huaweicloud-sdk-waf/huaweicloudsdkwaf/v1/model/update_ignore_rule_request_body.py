# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIgnoreRuleRequestBody:

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
        'description': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'conditions': 'conditions',
        'mode': 'mode',
        'rule': 'rule',
        'advanced': 'advanced',
        'description': 'description'
    }

    def __init__(self, domain=None, conditions=None, mode=None, rule=None, advanced=None, description=None):
        """UpdateIgnoreRuleRequestBody

        The model defined in huaweicloud sdk

        :param domain: 防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效
        :type domain: list[str]
        :param conditions: 条件列表
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        :param mode: 固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建
        :type mode: int
        :param rule: 需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略-&gt;策略名称-&gt;Web基础防护的高级设置-&gt;防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xxs攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass
        :type rule: str
        :param advanced: 
        :type advanced: :class:`huaweicloudsdkwaf.v1.IgnoreAdvanced`
        :param description: 屏蔽规则描述
        :type description: str
        """
        
        

        self._domain = None
        self._conditions = None
        self._mode = None
        self._rule = None
        self._advanced = None
        self._description = None
        self.discriminator = None

        self.domain = domain
        self.conditions = conditions
        self.mode = mode
        self.rule = rule
        if advanced is not None:
            self.advanced = advanced
        if description is not None:
            self.description = description

    @property
    def domain(self):
        """Gets the domain of this UpdateIgnoreRuleRequestBody.

        防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效

        :return: The domain of this UpdateIgnoreRuleRequestBody.
        :rtype: list[str]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this UpdateIgnoreRuleRequestBody.

        防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效

        :param domain: The domain of this UpdateIgnoreRuleRequestBody.
        :type domain: list[str]
        """
        self._domain = domain

    @property
    def conditions(self):
        """Gets the conditions of this UpdateIgnoreRuleRequestBody.

        条件列表

        :return: The conditions of this UpdateIgnoreRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this UpdateIgnoreRuleRequestBody.

        条件列表

        :param conditions: The conditions of this UpdateIgnoreRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        """
        self._conditions = conditions

    @property
    def mode(self):
        """Gets the mode of this UpdateIgnoreRuleRequestBody.

        固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建

        :return: The mode of this UpdateIgnoreRuleRequestBody.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this UpdateIgnoreRuleRequestBody.

        固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建

        :param mode: The mode of this UpdateIgnoreRuleRequestBody.
        :type mode: int
        """
        self._mode = mode

    @property
    def rule(self):
        """Gets the rule of this UpdateIgnoreRuleRequestBody.

        需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护的高级设置->防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xxs攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass

        :return: The rule of this UpdateIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this UpdateIgnoreRuleRequestBody.

        需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护的高级设置->防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xxs攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass

        :param rule: The rule of this UpdateIgnoreRuleRequestBody.
        :type rule: str
        """
        self._rule = rule

    @property
    def advanced(self):
        """Gets the advanced of this UpdateIgnoreRuleRequestBody.

        :return: The advanced of this UpdateIgnoreRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.IgnoreAdvanced`
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this UpdateIgnoreRuleRequestBody.

        :param advanced: The advanced of this UpdateIgnoreRuleRequestBody.
        :type advanced: :class:`huaweicloudsdkwaf.v1.IgnoreAdvanced`
        """
        self._advanced = advanced

    @property
    def description(self):
        """Gets the description of this UpdateIgnoreRuleRequestBody.

        屏蔽规则描述

        :return: The description of this UpdateIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateIgnoreRuleRequestBody.

        屏蔽规则描述

        :param description: The description of this UpdateIgnoreRuleRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, UpdateIgnoreRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
