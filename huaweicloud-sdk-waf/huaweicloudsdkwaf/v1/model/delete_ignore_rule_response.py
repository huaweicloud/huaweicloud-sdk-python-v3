# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteIgnoreRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'policyid': 'str',
        'timestamp': 'int',
        'description': 'str',
        'status': 'int',
        'url': 'str',
        'rule': 'str',
        'mode': 'int',
        'url_logic': 'str',
        'conditions': 'list[Condition]',
        'advanced': 'list[Advanced]',
        'domains': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'policyid': 'policyid',
        'timestamp': 'timestamp',
        'description': 'description',
        'status': 'status',
        'url': 'url',
        'rule': 'rule',
        'mode': 'mode',
        'url_logic': 'url_logic',
        'conditions': 'conditions',
        'advanced': 'advanced',
        'domains': 'domains'
    }

    def __init__(self, id=None, policyid=None, timestamp=None, description=None, status=None, url=None, rule=None, mode=None, url_logic=None, conditions=None, advanced=None, domains=None):
        """DeleteIgnoreRuleResponse

        The model defined in huaweicloud sdk

        :param id: 规则id
        :type id: str
        :param policyid: 策略id
        :type policyid: str
        :param timestamp: 创建规则的时间戳
        :type timestamp: int
        :param description: 规则描述
        :type description: str
        :param status: 规则状态，0：关闭，1：开启
        :type status: int
        :param url: 误报规则屏蔽路径，仅在mode为0的状态下有该字段
        :type url: str
        :param rule: 需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略-&gt;策略名称-&gt;Web基础防护的高级设置-&gt;防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xxs攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass
        :type rule: str
        :param mode: 版本号，0代表v1旧版本，1代表v2新版本；mode为0时，不存在conditions字段，存在url和url_logic字段；mode为1时，不存在url和url_logic字段，存在conditions字段
        :type mode: int
        :param url_logic: url匹配逻辑
        :type url_logic: str
        :param conditions: 条件
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.Condition`]
        :param advanced: 高级配置项
        :type advanced: list[:class:`huaweicloudsdkwaf.v1.Advanced`]
        :param domains: 防护域名或防护网站
        :type domains: list[str]
        """
        
        super(DeleteIgnoreRuleResponse, self).__init__()

        self._id = None
        self._policyid = None
        self._timestamp = None
        self._description = None
        self._status = None
        self._url = None
        self._rule = None
        self._mode = None
        self._url_logic = None
        self._conditions = None
        self._advanced = None
        self._domains = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if policyid is not None:
            self.policyid = policyid
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if url is not None:
            self.url = url
        if rule is not None:
            self.rule = rule
        if mode is not None:
            self.mode = mode
        if url_logic is not None:
            self.url_logic = url_logic
        if conditions is not None:
            self.conditions = conditions
        if advanced is not None:
            self.advanced = advanced
        if domains is not None:
            self.domains = domains

    @property
    def id(self):
        """Gets the id of this DeleteIgnoreRuleResponse.

        规则id

        :return: The id of this DeleteIgnoreRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteIgnoreRuleResponse.

        规则id

        :param id: The id of this DeleteIgnoreRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def policyid(self):
        """Gets the policyid of this DeleteIgnoreRuleResponse.

        策略id

        :return: The policyid of this DeleteIgnoreRuleResponse.
        :rtype: str
        """
        return self._policyid

    @policyid.setter
    def policyid(self, policyid):
        """Sets the policyid of this DeleteIgnoreRuleResponse.

        策略id

        :param policyid: The policyid of this DeleteIgnoreRuleResponse.
        :type policyid: str
        """
        self._policyid = policyid

    @property
    def timestamp(self):
        """Gets the timestamp of this DeleteIgnoreRuleResponse.

        创建规则的时间戳

        :return: The timestamp of this DeleteIgnoreRuleResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DeleteIgnoreRuleResponse.

        创建规则的时间戳

        :param timestamp: The timestamp of this DeleteIgnoreRuleResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this DeleteIgnoreRuleResponse.

        规则描述

        :return: The description of this DeleteIgnoreRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeleteIgnoreRuleResponse.

        规则描述

        :param description: The description of this DeleteIgnoreRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this DeleteIgnoreRuleResponse.

        规则状态，0：关闭，1：开启

        :return: The status of this DeleteIgnoreRuleResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeleteIgnoreRuleResponse.

        规则状态，0：关闭，1：开启

        :param status: The status of this DeleteIgnoreRuleResponse.
        :type status: int
        """
        self._status = status

    @property
    def url(self):
        """Gets the url of this DeleteIgnoreRuleResponse.

        误报规则屏蔽路径，仅在mode为0的状态下有该字段

        :return: The url of this DeleteIgnoreRuleResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DeleteIgnoreRuleResponse.

        误报规则屏蔽路径，仅在mode为0的状态下有该字段

        :param url: The url of this DeleteIgnoreRuleResponse.
        :type url: str
        """
        self._url = url

    @property
    def rule(self):
        """Gets the rule of this DeleteIgnoreRuleResponse.

        需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护的高级设置->防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xxs攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass

        :return: The rule of this DeleteIgnoreRuleResponse.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this DeleteIgnoreRuleResponse.

        需要屏蔽的规则，可屏蔽一个或者多个，屏蔽多个时使用半角符;分隔   - 当需要屏蔽某一条内置规则时，该参数值为该内置规则id,可以在Web应用防火墙控制台的防护策略->策略名称->Web基础防护的高级设置->防护规则中查询；也可以在防护事件的事件详情中查询内置规则id   - 当需要屏蔽web基础防护某一类规则时，该参数值为需要屏蔽的web基础防护某一类规则名。其中，xss：xxs攻击；webshell：网站木马；vuln：其他类型攻击；sqli：sql注入攻击；robot：恶意爬虫；rfi：远程文件包含；lfi：本地文件包含；cmdi：命令注入攻击   - 当需要屏蔽Web基础防护模块，该参数值为：all   - 当需要屏蔽规则为所有检测模块时，该参数值为：bypass

        :param rule: The rule of this DeleteIgnoreRuleResponse.
        :type rule: str
        """
        self._rule = rule

    @property
    def mode(self):
        """Gets the mode of this DeleteIgnoreRuleResponse.

        版本号，0代表v1旧版本，1代表v2新版本；mode为0时，不存在conditions字段，存在url和url_logic字段；mode为1时，不存在url和url_logic字段，存在conditions字段

        :return: The mode of this DeleteIgnoreRuleResponse.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this DeleteIgnoreRuleResponse.

        版本号，0代表v1旧版本，1代表v2新版本；mode为0时，不存在conditions字段，存在url和url_logic字段；mode为1时，不存在url和url_logic字段，存在conditions字段

        :param mode: The mode of this DeleteIgnoreRuleResponse.
        :type mode: int
        """
        self._mode = mode

    @property
    def url_logic(self):
        """Gets the url_logic of this DeleteIgnoreRuleResponse.

        url匹配逻辑

        :return: The url_logic of this DeleteIgnoreRuleResponse.
        :rtype: str
        """
        return self._url_logic

    @url_logic.setter
    def url_logic(self, url_logic):
        """Sets the url_logic of this DeleteIgnoreRuleResponse.

        url匹配逻辑

        :param url_logic: The url_logic of this DeleteIgnoreRuleResponse.
        :type url_logic: str
        """
        self._url_logic = url_logic

    @property
    def conditions(self):
        """Gets the conditions of this DeleteIgnoreRuleResponse.

        条件

        :return: The conditions of this DeleteIgnoreRuleResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.Condition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this DeleteIgnoreRuleResponse.

        条件

        :param conditions: The conditions of this DeleteIgnoreRuleResponse.
        :type conditions: list[:class:`huaweicloudsdkwaf.v1.Condition`]
        """
        self._conditions = conditions

    @property
    def advanced(self):
        """Gets the advanced of this DeleteIgnoreRuleResponse.

        高级配置项

        :return: The advanced of this DeleteIgnoreRuleResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.Advanced`]
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this DeleteIgnoreRuleResponse.

        高级配置项

        :param advanced: The advanced of this DeleteIgnoreRuleResponse.
        :type advanced: list[:class:`huaweicloudsdkwaf.v1.Advanced`]
        """
        self._advanced = advanced

    @property
    def domains(self):
        """Gets the domains of this DeleteIgnoreRuleResponse.

        防护域名或防护网站

        :return: The domains of this DeleteIgnoreRuleResponse.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        """Sets the domains of this DeleteIgnoreRuleResponse.

        防护域名或防护网站

        :param domains: The domains of this DeleteIgnoreRuleResponse.
        :type domains: list[str]
        """
        self._domains = domains

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
        if not isinstance(other, DeleteIgnoreRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
