# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleChangeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'id': 'str',
        'logic_operator': 'str',
        'min_match': 'int',
        'risk_level': 'int',
        'rule_content': 'str',
        'rule_desc': 'str',
        'rule_name': 'str',
        'rule_type': 'str'
    }

    attribute_map = {
        'category': 'category',
        'id': 'id',
        'logic_operator': 'logic_operator',
        'min_match': 'min_match',
        'risk_level': 'risk_level',
        'rule_content': 'rule_content',
        'rule_desc': 'rule_desc',
        'rule_name': 'rule_name',
        'rule_type': 'rule_type'
    }

    def __init__(self, category=None, id=None, logic_operator=None, min_match=None, risk_level=None, rule_content=None, rule_desc=None, rule_name=None, rule_type=None):
        r"""RuleChangeRequest

        The model defined in huaweicloud sdk

        :param category: 规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)
        :type category: str
        :param id: 规则ID
        :type id: str
        :param logic_operator: 逻辑运算符，\&quot;AND\&quot;,\&quot;OR\&quot;,\&quot;REGEX\&quot;
        :type logic_operator: str
        :param min_match: 最小匹配次数
        :type min_match: int
        :param risk_level: 风险等级
        :type risk_level: int
        :param rule_content: 规则内容
        :type rule_content: str
        :param rule_desc: 规则描述
        :type rule_desc: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param rule_type: 规则类型，关键字(KEYWORD)、正则表达式(REGEX)或自然语言(NLP)
        :type rule_type: str
        """
        
        

        self._category = None
        self._id = None
        self._logic_operator = None
        self._min_match = None
        self._risk_level = None
        self._rule_content = None
        self._rule_desc = None
        self._rule_name = None
        self._rule_type = None
        self.discriminator = None

        self.category = category
        self.id = id
        self.logic_operator = logic_operator
        self.min_match = min_match
        self.risk_level = risk_level
        self.rule_content = rule_content
        if rule_desc is not None:
            self.rule_desc = rule_desc
        self.rule_name = rule_name
        self.rule_type = rule_type

    @property
    def category(self):
        r"""Gets the category of this RuleChangeRequest.

        规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)

        :return: The category of this RuleChangeRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this RuleChangeRequest.

        规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)

        :param category: The category of this RuleChangeRequest.
        :type category: str
        """
        self._category = category

    @property
    def id(self):
        r"""Gets the id of this RuleChangeRequest.

        规则ID

        :return: The id of this RuleChangeRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RuleChangeRequest.

        规则ID

        :param id: The id of this RuleChangeRequest.
        :type id: str
        """
        self._id = id

    @property
    def logic_operator(self):
        r"""Gets the logic_operator of this RuleChangeRequest.

        逻辑运算符，\"AND\",\"OR\",\"REGEX\"

        :return: The logic_operator of this RuleChangeRequest.
        :rtype: str
        """
        return self._logic_operator

    @logic_operator.setter
    def logic_operator(self, logic_operator):
        r"""Sets the logic_operator of this RuleChangeRequest.

        逻辑运算符，\"AND\",\"OR\",\"REGEX\"

        :param logic_operator: The logic_operator of this RuleChangeRequest.
        :type logic_operator: str
        """
        self._logic_operator = logic_operator

    @property
    def min_match(self):
        r"""Gets the min_match of this RuleChangeRequest.

        最小匹配次数

        :return: The min_match of this RuleChangeRequest.
        :rtype: int
        """
        return self._min_match

    @min_match.setter
    def min_match(self, min_match):
        r"""Sets the min_match of this RuleChangeRequest.

        最小匹配次数

        :param min_match: The min_match of this RuleChangeRequest.
        :type min_match: int
        """
        self._min_match = min_match

    @property
    def risk_level(self):
        r"""Gets the risk_level of this RuleChangeRequest.

        风险等级

        :return: The risk_level of this RuleChangeRequest.
        :rtype: int
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this RuleChangeRequest.

        风险等级

        :param risk_level: The risk_level of this RuleChangeRequest.
        :type risk_level: int
        """
        self._risk_level = risk_level

    @property
    def rule_content(self):
        r"""Gets the rule_content of this RuleChangeRequest.

        规则内容

        :return: The rule_content of this RuleChangeRequest.
        :rtype: str
        """
        return self._rule_content

    @rule_content.setter
    def rule_content(self, rule_content):
        r"""Sets the rule_content of this RuleChangeRequest.

        规则内容

        :param rule_content: The rule_content of this RuleChangeRequest.
        :type rule_content: str
        """
        self._rule_content = rule_content

    @property
    def rule_desc(self):
        r"""Gets the rule_desc of this RuleChangeRequest.

        规则描述

        :return: The rule_desc of this RuleChangeRequest.
        :rtype: str
        """
        return self._rule_desc

    @rule_desc.setter
    def rule_desc(self, rule_desc):
        r"""Sets the rule_desc of this RuleChangeRequest.

        规则描述

        :param rule_desc: The rule_desc of this RuleChangeRequest.
        :type rule_desc: str
        """
        self._rule_desc = rule_desc

    @property
    def rule_name(self):
        r"""Gets the rule_name of this RuleChangeRequest.

        规则名称

        :return: The rule_name of this RuleChangeRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this RuleChangeRequest.

        规则名称

        :param rule_name: The rule_name of this RuleChangeRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_type(self):
        r"""Gets the rule_type of this RuleChangeRequest.

        规则类型，关键字(KEYWORD)、正则表达式(REGEX)或自然语言(NLP)

        :return: The rule_type of this RuleChangeRequest.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this RuleChangeRequest.

        规则类型，关键字(KEYWORD)、正则表达式(REGEX)或自然语言(NLP)

        :param rule_type: The rule_type of this RuleChangeRequest.
        :type rule_type: str
        """
        self._rule_type = rule_type

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
        if not isinstance(other, RuleChangeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
