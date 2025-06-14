# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIgnoreRuleRequestBody:

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
        r"""CreateIgnoreRuleRequestBody

        The model defined in huaweicloud sdk

        :param domain: 防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效。当防护域名的接入模式为云模式-ELB接入时，该参数需以&lt;域名&gt;:&lt;id&gt;格式填写（如www.example.com:id），若域名绑定的负载均衡器（ELB）下所有监听器都接入WAF防护，填入的id为负载均衡器（ELB）id，否则填入的id为指定监听器id；可在WAF控制台域名详情页查询与该域名绑定的ELB实例id，在ELB侧监听器页签下查询其监听器id
        :type domain: list[str]
        :param conditions: 条件列表
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        :param mode: 固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建
        :type mode: int
        :param rule: 需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略-&gt;策略名称-&gt;Web基础防护的高级设置-&gt;防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xss攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass
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
        r"""Gets the domain of this CreateIgnoreRuleRequestBody.

        防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效。当防护域名的接入模式为云模式-ELB接入时，该参数需以<域名>:<id>格式填写（如www.example.com:id），若域名绑定的负载均衡器（ELB）下所有监听器都接入WAF防护，填入的id为负载均衡器（ELB）id，否则填入的id为指定监听器id；可在WAF控制台域名详情页查询与该域名绑定的ELB实例id，在ELB侧监听器页签下查询其监听器id

        :return: The domain of this CreateIgnoreRuleRequestBody.
        :rtype: list[str]
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this CreateIgnoreRuleRequestBody.

        防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效。当防护域名的接入模式为云模式-ELB接入时，该参数需以<域名>:<id>格式填写（如www.example.com:id），若域名绑定的负载均衡器（ELB）下所有监听器都接入WAF防护，填入的id为负载均衡器（ELB）id，否则填入的id为指定监听器id；可在WAF控制台域名详情页查询与该域名绑定的ELB实例id，在ELB侧监听器页签下查询其监听器id

        :param domain: The domain of this CreateIgnoreRuleRequestBody.
        :type domain: list[str]
        """
        self._domain = domain

    @property
    def conditions(self):
        r"""Gets the conditions of this CreateIgnoreRuleRequestBody.

        条件列表

        :return: The conditions of this CreateIgnoreRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this CreateIgnoreRuleRequestBody.

        条件列表

        :param conditions: The conditions of this CreateIgnoreRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.CreateCondition`]
        """
        self._conditions = conditions

    @property
    def mode(self):
        r"""Gets the mode of this CreateIgnoreRuleRequestBody.

        固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建

        :return: The mode of this CreateIgnoreRuleRequestBody.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateIgnoreRuleRequestBody.

        固定值为1,代表v2版本误报屏蔽规则，v1版本仅用于兼容旧版本，不支持创建

        :param mode: The mode of this CreateIgnoreRuleRequestBody.
        :type mode: int
        """
        self._mode = mode

    @property
    def rule(self):
        r"""Gets the rule of this CreateIgnoreRuleRequestBody.

        需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护的高级设置->防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xss攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass

        :return: The rule of this CreateIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this CreateIgnoreRuleRequestBody.

        需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护的高级设置->防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xss攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass

        :param rule: The rule of this CreateIgnoreRuleRequestBody.
        :type rule: str
        """
        self._rule = rule

    @property
    def advanced(self):
        r"""Gets the advanced of this CreateIgnoreRuleRequestBody.

        :return: The advanced of this CreateIgnoreRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.IgnoreAdvanced`
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        r"""Sets the advanced of this CreateIgnoreRuleRequestBody.

        :param advanced: The advanced of this CreateIgnoreRuleRequestBody.
        :type advanced: :class:`huaweicloudsdkwaf.v1.IgnoreAdvanced`
        """
        self._advanced = advanced

    @property
    def description(self):
        r"""Gets the description of this CreateIgnoreRuleRequestBody.

        屏蔽规则描述

        :return: The description of this CreateIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateIgnoreRuleRequestBody.

        屏蔽规则描述

        :param description: The description of this CreateIgnoreRuleRequestBody.
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
        if not isinstance(other, CreateIgnoreRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
