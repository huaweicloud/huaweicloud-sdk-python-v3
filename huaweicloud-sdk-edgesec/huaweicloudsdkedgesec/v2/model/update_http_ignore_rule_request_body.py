# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpIgnoreRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'status': 'int',
        'url': 'str',
        'rule': 'str',
        'mode': 'int',
        'domains': 'list[str]',
        'url_logic': 'str',
        'advanced': 'HttpIgnoreRuleCondition',
        'conditions': 'list[HttpIgnoreRuleCondition]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'url': 'url',
        'rule': 'rule',
        'mode': 'mode',
        'domains': 'domains',
        'url_logic': 'url_logic',
        'advanced': 'advanced',
        'conditions': 'conditions'
    }

    def __init__(self, name=None, description=None, status=None, url=None, rule=None, mode=None, domains=None, url_logic=None, advanced=None, conditions=None):
        r"""UpdateHttpIgnoreRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param description: 规则描述，最长512字符
        :type description: str
        :param status: 规则开关状态
        :type status: int
        :param url: 误报路径
        :type url: str
        :param rule: 需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略-&gt;策略名称-&gt;Web基础防护的高级设置-&gt;防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xss攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass
        :type rule: str
        :param mode: 误报屏蔽模式，默认为0即旧模式
        :type mode: int
        :param domains: 防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效
        :type domains: list[str]
        :param url_logic: 屏蔽规则url类型（前缀：prefix，等于：equal）
        :type url_logic: str
        :param advanced: 
        :type advanced: :class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`
        :param conditions: 命中条件
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`]
        """
        
        

        self._name = None
        self._description = None
        self._status = None
        self._url = None
        self._rule = None
        self._mode = None
        self._domains = None
        self._url_logic = None
        self._advanced = None
        self._conditions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url
        self.rule = rule
        self.mode = mode
        self.domains = domains
        if url_logic is not None:
            self.url_logic = url_logic
        if advanced is not None:
            self.advanced = advanced
        self.conditions = conditions

    @property
    def name(self):
        r"""Gets the name of this UpdateHttpIgnoreRuleRequestBody.

        规则名称

        :return: The name of this UpdateHttpIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateHttpIgnoreRuleRequestBody.

        规则名称

        :param name: The name of this UpdateHttpIgnoreRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateHttpIgnoreRuleRequestBody.

        规则描述，最长512字符

        :return: The description of this UpdateHttpIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateHttpIgnoreRuleRequestBody.

        规则描述，最长512字符

        :param description: The description of this UpdateHttpIgnoreRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this UpdateHttpIgnoreRuleRequestBody.

        规则开关状态

        :return: The status of this UpdateHttpIgnoreRuleRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateHttpIgnoreRuleRequestBody.

        规则开关状态

        :param status: The status of this UpdateHttpIgnoreRuleRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def url(self):
        r"""Gets the url of this UpdateHttpIgnoreRuleRequestBody.

        误报路径

        :return: The url of this UpdateHttpIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this UpdateHttpIgnoreRuleRequestBody.

        误报路径

        :param url: The url of this UpdateHttpIgnoreRuleRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def rule(self):
        r"""Gets the rule of this UpdateHttpIgnoreRuleRequestBody.

        需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护的高级设置->防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xss攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass

        :return: The rule of this UpdateHttpIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this UpdateHttpIgnoreRuleRequestBody.

        需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护的高级设置->防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xss攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass

        :param rule: The rule of this UpdateHttpIgnoreRuleRequestBody.
        :type rule: str
        """
        self._rule = rule

    @property
    def mode(self):
        r"""Gets the mode of this UpdateHttpIgnoreRuleRequestBody.

        误报屏蔽模式，默认为0即旧模式

        :return: The mode of this UpdateHttpIgnoreRuleRequestBody.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this UpdateHttpIgnoreRuleRequestBody.

        误报屏蔽模式，默认为0即旧模式

        :param mode: The mode of this UpdateHttpIgnoreRuleRequestBody.
        :type mode: int
        """
        self._mode = mode

    @property
    def domains(self):
        r"""Gets the domains of this UpdateHttpIgnoreRuleRequestBody.

        防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效

        :return: The domains of this UpdateHttpIgnoreRuleRequestBody.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        r"""Sets the domains of this UpdateHttpIgnoreRuleRequestBody.

        防护域名或防护网站，数组长度为0时，代表规则对全部域名或防护网站生效

        :param domains: The domains of this UpdateHttpIgnoreRuleRequestBody.
        :type domains: list[str]
        """
        self._domains = domains

    @property
    def url_logic(self):
        r"""Gets the url_logic of this UpdateHttpIgnoreRuleRequestBody.

        屏蔽规则url类型（前缀：prefix，等于：equal）

        :return: The url_logic of this UpdateHttpIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._url_logic

    @url_logic.setter
    def url_logic(self, url_logic):
        r"""Sets the url_logic of this UpdateHttpIgnoreRuleRequestBody.

        屏蔽规则url类型（前缀：prefix，等于：equal）

        :param url_logic: The url_logic of this UpdateHttpIgnoreRuleRequestBody.
        :type url_logic: str
        """
        self._url_logic = url_logic

    @property
    def advanced(self):
        r"""Gets the advanced of this UpdateHttpIgnoreRuleRequestBody.

        :return: The advanced of this UpdateHttpIgnoreRuleRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        r"""Sets the advanced of this UpdateHttpIgnoreRuleRequestBody.

        :param advanced: The advanced of this UpdateHttpIgnoreRuleRequestBody.
        :type advanced: :class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`
        """
        self._advanced = advanced

    @property
    def conditions(self):
        r"""Gets the conditions of this UpdateHttpIgnoreRuleRequestBody.

        命中条件

        :return: The conditions of this UpdateHttpIgnoreRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this UpdateHttpIgnoreRuleRequestBody.

        命中条件

        :param conditions: The conditions of this UpdateHttpIgnoreRuleRequestBody.
        :type conditions: list[:class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`]
        """
        self._conditions = conditions

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
        if not isinstance(other, UpdateHttpIgnoreRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
