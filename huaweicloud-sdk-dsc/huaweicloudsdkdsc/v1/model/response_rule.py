# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseRule:

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
        'delete_allowed': 'bool',
        'group_names': 'str',
        'id': 'str',
        'logic_operator': 'str',
        'min_match': 'int',
        'risk_level': 'int',
        'rule_content': 'str',
        'rule_desc': 'str',
        'rule_name': 'str',
        'rule_type': 'str',
        'selected': 'bool'
    }

    attribute_map = {
        'category': 'category',
        'delete_allowed': 'delete_allowed',
        'group_names': 'group_names',
        'id': 'id',
        'logic_operator': 'logic_operator',
        'min_match': 'min_match',
        'risk_level': 'risk_level',
        'rule_content': 'rule_content',
        'rule_desc': 'rule_desc',
        'rule_name': 'rule_name',
        'rule_type': 'rule_type',
        'selected': 'selected'
    }

    def __init__(self, category=None, delete_allowed=None, group_names=None, id=None, logic_operator=None, min_match=None, risk_level=None, rule_content=None, rule_desc=None, rule_name=None, rule_type=None, selected=None):
        """ResponseRule

        The model defined in huaweicloud sdk

        :param category: 规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)
        :type category: str
        :param delete_allowed: 是否允许删除
        :type delete_allowed: bool
        :param group_names: 相关的规则组
        :type group_names: str
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
        :param selected: 是否可选
        :type selected: bool
        """
        
        

        self._category = None
        self._delete_allowed = None
        self._group_names = None
        self._id = None
        self._logic_operator = None
        self._min_match = None
        self._risk_level = None
        self._rule_content = None
        self._rule_desc = None
        self._rule_name = None
        self._rule_type = None
        self._selected = None
        self.discriminator = None

        if category is not None:
            self.category = category
        if delete_allowed is not None:
            self.delete_allowed = delete_allowed
        if group_names is not None:
            self.group_names = group_names
        if id is not None:
            self.id = id
        if logic_operator is not None:
            self.logic_operator = logic_operator
        if min_match is not None:
            self.min_match = min_match
        if risk_level is not None:
            self.risk_level = risk_level
        if rule_content is not None:
            self.rule_content = rule_content
        if rule_desc is not None:
            self.rule_desc = rule_desc
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_type is not None:
            self.rule_type = rule_type
        if selected is not None:
            self.selected = selected

    @property
    def category(self):
        """Gets the category of this ResponseRule.

        规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)

        :return: The category of this ResponseRule.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ResponseRule.

        规则类别，内置规则(BUILT_IN)或自建规则(BUILT_SELF)

        :param category: The category of this ResponseRule.
        :type category: str
        """
        self._category = category

    @property
    def delete_allowed(self):
        """Gets the delete_allowed of this ResponseRule.

        是否允许删除

        :return: The delete_allowed of this ResponseRule.
        :rtype: bool
        """
        return self._delete_allowed

    @delete_allowed.setter
    def delete_allowed(self, delete_allowed):
        """Sets the delete_allowed of this ResponseRule.

        是否允许删除

        :param delete_allowed: The delete_allowed of this ResponseRule.
        :type delete_allowed: bool
        """
        self._delete_allowed = delete_allowed

    @property
    def group_names(self):
        """Gets the group_names of this ResponseRule.

        相关的规则组

        :return: The group_names of this ResponseRule.
        :rtype: str
        """
        return self._group_names

    @group_names.setter
    def group_names(self, group_names):
        """Sets the group_names of this ResponseRule.

        相关的规则组

        :param group_names: The group_names of this ResponseRule.
        :type group_names: str
        """
        self._group_names = group_names

    @property
    def id(self):
        """Gets the id of this ResponseRule.

        规则ID

        :return: The id of this ResponseRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseRule.

        规则ID

        :param id: The id of this ResponseRule.
        :type id: str
        """
        self._id = id

    @property
    def logic_operator(self):
        """Gets the logic_operator of this ResponseRule.

        逻辑运算符，\"AND\",\"OR\",\"REGEX\"

        :return: The logic_operator of this ResponseRule.
        :rtype: str
        """
        return self._logic_operator

    @logic_operator.setter
    def logic_operator(self, logic_operator):
        """Sets the logic_operator of this ResponseRule.

        逻辑运算符，\"AND\",\"OR\",\"REGEX\"

        :param logic_operator: The logic_operator of this ResponseRule.
        :type logic_operator: str
        """
        self._logic_operator = logic_operator

    @property
    def min_match(self):
        """Gets the min_match of this ResponseRule.

        最小匹配次数

        :return: The min_match of this ResponseRule.
        :rtype: int
        """
        return self._min_match

    @min_match.setter
    def min_match(self, min_match):
        """Sets the min_match of this ResponseRule.

        最小匹配次数

        :param min_match: The min_match of this ResponseRule.
        :type min_match: int
        """
        self._min_match = min_match

    @property
    def risk_level(self):
        """Gets the risk_level of this ResponseRule.

        风险等级

        :return: The risk_level of this ResponseRule.
        :rtype: int
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """Sets the risk_level of this ResponseRule.

        风险等级

        :param risk_level: The risk_level of this ResponseRule.
        :type risk_level: int
        """
        self._risk_level = risk_level

    @property
    def rule_content(self):
        """Gets the rule_content of this ResponseRule.

        规则内容

        :return: The rule_content of this ResponseRule.
        :rtype: str
        """
        return self._rule_content

    @rule_content.setter
    def rule_content(self, rule_content):
        """Sets the rule_content of this ResponseRule.

        规则内容

        :param rule_content: The rule_content of this ResponseRule.
        :type rule_content: str
        """
        self._rule_content = rule_content

    @property
    def rule_desc(self):
        """Gets the rule_desc of this ResponseRule.

        规则描述

        :return: The rule_desc of this ResponseRule.
        :rtype: str
        """
        return self._rule_desc

    @rule_desc.setter
    def rule_desc(self, rule_desc):
        """Sets the rule_desc of this ResponseRule.

        规则描述

        :param rule_desc: The rule_desc of this ResponseRule.
        :type rule_desc: str
        """
        self._rule_desc = rule_desc

    @property
    def rule_name(self):
        """Gets the rule_name of this ResponseRule.

        规则名称

        :return: The rule_name of this ResponseRule.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ResponseRule.

        规则名称

        :param rule_name: The rule_name of this ResponseRule.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_type(self):
        """Gets the rule_type of this ResponseRule.

        规则类型，关键字(KEYWORD)、正则表达式(REGEX)或自然语言(NLP)

        :return: The rule_type of this ResponseRule.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this ResponseRule.

        规则类型，关键字(KEYWORD)、正则表达式(REGEX)或自然语言(NLP)

        :param rule_type: The rule_type of this ResponseRule.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def selected(self):
        """Gets the selected of this ResponseRule.

        是否可选

        :return: The selected of this ResponseRule.
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this ResponseRule.

        是否可选

        :param selected: The selected of this ResponseRule.
        :type selected: bool
        """
        self._selected = selected

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
        if not isinstance(other, ResponseRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
