# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleListItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_set': 'str',
        'rule_id': 'str',
        'rule_language': 'str',
        'rule_name': 'str',
        'rule_severity': 'str',
        'rule_tages': 'str',
        'right_example': 'str',
        'error_example': 'str',
        'revise_opinion': 'str',
        'rule_desc': 'str'
    }

    attribute_map = {
        'rule_set': 'rule_set',
        'rule_id': 'rule_id',
        'rule_language': 'rule_language',
        'rule_name': 'rule_name',
        'rule_severity': 'rule_severity',
        'rule_tages': 'rule_tages',
        'right_example': 'right_example',
        'error_example': 'error_example',
        'revise_opinion': 'revise_opinion',
        'rule_desc': 'rule_desc'
    }

    def __init__(self, rule_set=None, rule_id=None, rule_language=None, rule_name=None, rule_severity=None, rule_tages=None, right_example=None, error_example=None, revise_opinion=None, rule_desc=None):
        """RuleListItem

        The model defined in huaweicloud sdk

        :param rule_set: 规则集规范分类
        :type rule_set: str
        :param rule_id: 规则id
        :type rule_id: str
        :param rule_language: 规则所属语言
        :type rule_language: str
        :param rule_name: 规则名称
        :type rule_name: str
        :param rule_severity: 规则问题级别
        :type rule_severity: str
        :param rule_tages: 规则标签
        :type rule_tages: str
        :param right_example: 正确示例
        :type right_example: str
        :param error_example: 错误示例
        :type error_example: str
        :param revise_opinion: 修改建议
        :type revise_opinion: str
        :param rule_desc: 规则描述
        :type rule_desc: str
        """
        
        

        self._rule_set = None
        self._rule_id = None
        self._rule_language = None
        self._rule_name = None
        self._rule_severity = None
        self._rule_tages = None
        self._right_example = None
        self._error_example = None
        self._revise_opinion = None
        self._rule_desc = None
        self.discriminator = None

        if rule_set is not None:
            self.rule_set = rule_set
        if rule_id is not None:
            self.rule_id = rule_id
        if rule_language is not None:
            self.rule_language = rule_language
        if rule_name is not None:
            self.rule_name = rule_name
        if rule_severity is not None:
            self.rule_severity = rule_severity
        if rule_tages is not None:
            self.rule_tages = rule_tages
        if right_example is not None:
            self.right_example = right_example
        if error_example is not None:
            self.error_example = error_example
        if revise_opinion is not None:
            self.revise_opinion = revise_opinion
        if rule_desc is not None:
            self.rule_desc = rule_desc

    @property
    def rule_set(self):
        """Gets the rule_set of this RuleListItem.

        规则集规范分类

        :return: The rule_set of this RuleListItem.
        :rtype: str
        """
        return self._rule_set

    @rule_set.setter
    def rule_set(self, rule_set):
        """Sets the rule_set of this RuleListItem.

        规则集规范分类

        :param rule_set: The rule_set of this RuleListItem.
        :type rule_set: str
        """
        self._rule_set = rule_set

    @property
    def rule_id(self):
        """Gets the rule_id of this RuleListItem.

        规则id

        :return: The rule_id of this RuleListItem.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this RuleListItem.

        规则id

        :param rule_id: The rule_id of this RuleListItem.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def rule_language(self):
        """Gets the rule_language of this RuleListItem.

        规则所属语言

        :return: The rule_language of this RuleListItem.
        :rtype: str
        """
        return self._rule_language

    @rule_language.setter
    def rule_language(self, rule_language):
        """Sets the rule_language of this RuleListItem.

        规则所属语言

        :param rule_language: The rule_language of this RuleListItem.
        :type rule_language: str
        """
        self._rule_language = rule_language

    @property
    def rule_name(self):
        """Gets the rule_name of this RuleListItem.

        规则名称

        :return: The rule_name of this RuleListItem.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this RuleListItem.

        规则名称

        :param rule_name: The rule_name of this RuleListItem.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def rule_severity(self):
        """Gets the rule_severity of this RuleListItem.

        规则问题级别

        :return: The rule_severity of this RuleListItem.
        :rtype: str
        """
        return self._rule_severity

    @rule_severity.setter
    def rule_severity(self, rule_severity):
        """Sets the rule_severity of this RuleListItem.

        规则问题级别

        :param rule_severity: The rule_severity of this RuleListItem.
        :type rule_severity: str
        """
        self._rule_severity = rule_severity

    @property
    def rule_tages(self):
        """Gets the rule_tages of this RuleListItem.

        规则标签

        :return: The rule_tages of this RuleListItem.
        :rtype: str
        """
        return self._rule_tages

    @rule_tages.setter
    def rule_tages(self, rule_tages):
        """Sets the rule_tages of this RuleListItem.

        规则标签

        :param rule_tages: The rule_tages of this RuleListItem.
        :type rule_tages: str
        """
        self._rule_tages = rule_tages

    @property
    def right_example(self):
        """Gets the right_example of this RuleListItem.

        正确示例

        :return: The right_example of this RuleListItem.
        :rtype: str
        """
        return self._right_example

    @right_example.setter
    def right_example(self, right_example):
        """Sets the right_example of this RuleListItem.

        正确示例

        :param right_example: The right_example of this RuleListItem.
        :type right_example: str
        """
        self._right_example = right_example

    @property
    def error_example(self):
        """Gets the error_example of this RuleListItem.

        错误示例

        :return: The error_example of this RuleListItem.
        :rtype: str
        """
        return self._error_example

    @error_example.setter
    def error_example(self, error_example):
        """Sets the error_example of this RuleListItem.

        错误示例

        :param error_example: The error_example of this RuleListItem.
        :type error_example: str
        """
        self._error_example = error_example

    @property
    def revise_opinion(self):
        """Gets the revise_opinion of this RuleListItem.

        修改建议

        :return: The revise_opinion of this RuleListItem.
        :rtype: str
        """
        return self._revise_opinion

    @revise_opinion.setter
    def revise_opinion(self, revise_opinion):
        """Sets the revise_opinion of this RuleListItem.

        修改建议

        :param revise_opinion: The revise_opinion of this RuleListItem.
        :type revise_opinion: str
        """
        self._revise_opinion = revise_opinion

    @property
    def rule_desc(self):
        """Gets the rule_desc of this RuleListItem.

        规则描述

        :return: The rule_desc of this RuleListItem.
        :rtype: str
        """
        return self._rule_desc

    @rule_desc.setter
    def rule_desc(self, rule_desc):
        """Sets the rule_desc of this RuleListItem.

        规则描述

        :param rule_desc: The rule_desc of this RuleListItem.
        :type rule_desc: str
        """
        self._rule_desc = rule_desc

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
        if not isinstance(other, RuleListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
