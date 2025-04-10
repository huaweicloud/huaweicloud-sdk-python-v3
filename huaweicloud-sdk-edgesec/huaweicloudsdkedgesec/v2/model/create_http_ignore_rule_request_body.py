# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHttpIgnoreRuleRequestBody:

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
        'url': 'url',
        'rule': 'rule',
        'mode': 'mode',
        'domains': 'domains',
        'url_logic': 'url_logic',
        'advanced': 'advanced',
        'conditions': 'conditions'
    }

    def __init__(self, name=None, description=None, url=None, rule=None, mode=None, domains=None, url_logic=None, advanced=None, conditions=None):
        r"""CreateHttpIgnoreRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称
        :type name: str
        :param description: 规则描述，最长512字符
        :type description: str
        :param url: 误报路径
        :type url: str
        :param rule: 规则编号
        :type rule: str
        :param mode: 误报屏蔽模式，默认为0即旧模式
        :type mode: int
        :param domains: 域名列表
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
        r"""Gets the name of this CreateHttpIgnoreRuleRequestBody.

        规则名称

        :return: The name of this CreateHttpIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateHttpIgnoreRuleRequestBody.

        规则名称

        :param name: The name of this CreateHttpIgnoreRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateHttpIgnoreRuleRequestBody.

        规则描述，最长512字符

        :return: The description of this CreateHttpIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateHttpIgnoreRuleRequestBody.

        规则描述，最长512字符

        :param description: The description of this CreateHttpIgnoreRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def url(self):
        r"""Gets the url of this CreateHttpIgnoreRuleRequestBody.

        误报路径

        :return: The url of this CreateHttpIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this CreateHttpIgnoreRuleRequestBody.

        误报路径

        :param url: The url of this CreateHttpIgnoreRuleRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def rule(self):
        r"""Gets the rule of this CreateHttpIgnoreRuleRequestBody.

        规则编号

        :return: The rule of this CreateHttpIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        r"""Sets the rule of this CreateHttpIgnoreRuleRequestBody.

        规则编号

        :param rule: The rule of this CreateHttpIgnoreRuleRequestBody.
        :type rule: str
        """
        self._rule = rule

    @property
    def mode(self):
        r"""Gets the mode of this CreateHttpIgnoreRuleRequestBody.

        误报屏蔽模式，默认为0即旧模式

        :return: The mode of this CreateHttpIgnoreRuleRequestBody.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateHttpIgnoreRuleRequestBody.

        误报屏蔽模式，默认为0即旧模式

        :param mode: The mode of this CreateHttpIgnoreRuleRequestBody.
        :type mode: int
        """
        self._mode = mode

    @property
    def domains(self):
        r"""Gets the domains of this CreateHttpIgnoreRuleRequestBody.

        域名列表

        :return: The domains of this CreateHttpIgnoreRuleRequestBody.
        :rtype: list[str]
        """
        return self._domains

    @domains.setter
    def domains(self, domains):
        r"""Sets the domains of this CreateHttpIgnoreRuleRequestBody.

        域名列表

        :param domains: The domains of this CreateHttpIgnoreRuleRequestBody.
        :type domains: list[str]
        """
        self._domains = domains

    @property
    def url_logic(self):
        r"""Gets the url_logic of this CreateHttpIgnoreRuleRequestBody.

        屏蔽规则url类型（前缀：prefix，等于：equal）

        :return: The url_logic of this CreateHttpIgnoreRuleRequestBody.
        :rtype: str
        """
        return self._url_logic

    @url_logic.setter
    def url_logic(self, url_logic):
        r"""Sets the url_logic of this CreateHttpIgnoreRuleRequestBody.

        屏蔽规则url类型（前缀：prefix，等于：equal）

        :param url_logic: The url_logic of this CreateHttpIgnoreRuleRequestBody.
        :type url_logic: str
        """
        self._url_logic = url_logic

    @property
    def advanced(self):
        r"""Gets the advanced of this CreateHttpIgnoreRuleRequestBody.

        :return: The advanced of this CreateHttpIgnoreRuleRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        r"""Sets the advanced of this CreateHttpIgnoreRuleRequestBody.

        :param advanced: The advanced of this CreateHttpIgnoreRuleRequestBody.
        :type advanced: :class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`
        """
        self._advanced = advanced

    @property
    def conditions(self):
        r"""Gets the conditions of this CreateHttpIgnoreRuleRequestBody.

        命中条件

        :return: The conditions of this CreateHttpIgnoreRuleRequestBody.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.HttpIgnoreRuleCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this CreateHttpIgnoreRuleRequestBody.

        命中条件

        :param conditions: The conditions of this CreateHttpIgnoreRuleRequestBody.
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
        if not isinstance(other, CreateHttpIgnoreRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
