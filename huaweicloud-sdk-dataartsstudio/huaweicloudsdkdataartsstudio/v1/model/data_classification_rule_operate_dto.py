# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataClassificationRuleOperateDTO:

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
        'secrecy_level_id': 'str',
        'name': 'str',
        'method': 'str',
        'content_expression': 'str',
        'column_expression': 'str',
        'commit_expression': 'str',
        'builtin_rule_id': 'str',
        'description': 'str',
        'category_id': 'str'
    }

    attribute_map = {
        'rule_type': 'rule_type',
        'secrecy_level_id': 'secrecy_level_id',
        'name': 'name',
        'method': 'method',
        'content_expression': 'content_expression',
        'column_expression': 'column_expression',
        'commit_expression': 'commit_expression',
        'builtin_rule_id': 'builtin_rule_id',
        'description': 'description',
        'category_id': 'category_id'
    }

    def __init__(self, rule_type=None, secrecy_level_id=None, name=None, method=None, content_expression=None, column_expression=None, commit_expression=None, builtin_rule_id=None, description=None, category_id=None):
        r"""DataClassificationRuleOperateDTO

        The model defined in huaweicloud sdk

        :param rule_type: 规则类型, CUSTOM, BUILTIN
        :type rule_type: str
        :param secrecy_level_id: 密级ID
        :type secrecy_level_id: str
        :param name: 规则名称
        :type name: str
        :param method: 规则方式, REGULAR, NONE, DEFAULT
        :type method: str
        :param content_expression: 内容表达式
        :type content_expression: str
        :param column_expression: 列表达式
        :type column_expression: str
        :param commit_expression: 备注表达式
        :type commit_expression: str
        :param builtin_rule_id: 内置规则id
        :type builtin_rule_id: str
        :param description: 规则描述
        :type description: str
        :param category_id: 分类ID
        :type category_id: str
        """
        
        

        self._rule_type = None
        self._secrecy_level_id = None
        self._name = None
        self._method = None
        self._content_expression = None
        self._column_expression = None
        self._commit_expression = None
        self._builtin_rule_id = None
        self._description = None
        self._category_id = None
        self.discriminator = None

        self.rule_type = rule_type
        self.secrecy_level_id = secrecy_level_id
        self.name = name
        if method is not None:
            self.method = method
        if content_expression is not None:
            self.content_expression = content_expression
        if column_expression is not None:
            self.column_expression = column_expression
        if commit_expression is not None:
            self.commit_expression = commit_expression
        if builtin_rule_id is not None:
            self.builtin_rule_id = builtin_rule_id
        if description is not None:
            self.description = description
        if category_id is not None:
            self.category_id = category_id

    @property
    def rule_type(self):
        r"""Gets the rule_type of this DataClassificationRuleOperateDTO.

        规则类型, CUSTOM, BUILTIN

        :return: The rule_type of this DataClassificationRuleOperateDTO.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this DataClassificationRuleOperateDTO.

        规则类型, CUSTOM, BUILTIN

        :param rule_type: The rule_type of this DataClassificationRuleOperateDTO.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def secrecy_level_id(self):
        r"""Gets the secrecy_level_id of this DataClassificationRuleOperateDTO.

        密级ID

        :return: The secrecy_level_id of this DataClassificationRuleOperateDTO.
        :rtype: str
        """
        return self._secrecy_level_id

    @secrecy_level_id.setter
    def secrecy_level_id(self, secrecy_level_id):
        r"""Sets the secrecy_level_id of this DataClassificationRuleOperateDTO.

        密级ID

        :param secrecy_level_id: The secrecy_level_id of this DataClassificationRuleOperateDTO.
        :type secrecy_level_id: str
        """
        self._secrecy_level_id = secrecy_level_id

    @property
    def name(self):
        r"""Gets the name of this DataClassificationRuleOperateDTO.

        规则名称

        :return: The name of this DataClassificationRuleOperateDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DataClassificationRuleOperateDTO.

        规则名称

        :param name: The name of this DataClassificationRuleOperateDTO.
        :type name: str
        """
        self._name = name

    @property
    def method(self):
        r"""Gets the method of this DataClassificationRuleOperateDTO.

        规则方式, REGULAR, NONE, DEFAULT

        :return: The method of this DataClassificationRuleOperateDTO.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this DataClassificationRuleOperateDTO.

        规则方式, REGULAR, NONE, DEFAULT

        :param method: The method of this DataClassificationRuleOperateDTO.
        :type method: str
        """
        self._method = method

    @property
    def content_expression(self):
        r"""Gets the content_expression of this DataClassificationRuleOperateDTO.

        内容表达式

        :return: The content_expression of this DataClassificationRuleOperateDTO.
        :rtype: str
        """
        return self._content_expression

    @content_expression.setter
    def content_expression(self, content_expression):
        r"""Sets the content_expression of this DataClassificationRuleOperateDTO.

        内容表达式

        :param content_expression: The content_expression of this DataClassificationRuleOperateDTO.
        :type content_expression: str
        """
        self._content_expression = content_expression

    @property
    def column_expression(self):
        r"""Gets the column_expression of this DataClassificationRuleOperateDTO.

        列表达式

        :return: The column_expression of this DataClassificationRuleOperateDTO.
        :rtype: str
        """
        return self._column_expression

    @column_expression.setter
    def column_expression(self, column_expression):
        r"""Sets the column_expression of this DataClassificationRuleOperateDTO.

        列表达式

        :param column_expression: The column_expression of this DataClassificationRuleOperateDTO.
        :type column_expression: str
        """
        self._column_expression = column_expression

    @property
    def commit_expression(self):
        r"""Gets the commit_expression of this DataClassificationRuleOperateDTO.

        备注表达式

        :return: The commit_expression of this DataClassificationRuleOperateDTO.
        :rtype: str
        """
        return self._commit_expression

    @commit_expression.setter
    def commit_expression(self, commit_expression):
        r"""Sets the commit_expression of this DataClassificationRuleOperateDTO.

        备注表达式

        :param commit_expression: The commit_expression of this DataClassificationRuleOperateDTO.
        :type commit_expression: str
        """
        self._commit_expression = commit_expression

    @property
    def builtin_rule_id(self):
        r"""Gets the builtin_rule_id of this DataClassificationRuleOperateDTO.

        内置规则id

        :return: The builtin_rule_id of this DataClassificationRuleOperateDTO.
        :rtype: str
        """
        return self._builtin_rule_id

    @builtin_rule_id.setter
    def builtin_rule_id(self, builtin_rule_id):
        r"""Sets the builtin_rule_id of this DataClassificationRuleOperateDTO.

        内置规则id

        :param builtin_rule_id: The builtin_rule_id of this DataClassificationRuleOperateDTO.
        :type builtin_rule_id: str
        """
        self._builtin_rule_id = builtin_rule_id

    @property
    def description(self):
        r"""Gets the description of this DataClassificationRuleOperateDTO.

        规则描述

        :return: The description of this DataClassificationRuleOperateDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DataClassificationRuleOperateDTO.

        规则描述

        :param description: The description of this DataClassificationRuleOperateDTO.
        :type description: str
        """
        self._description = description

    @property
    def category_id(self):
        r"""Gets the category_id of this DataClassificationRuleOperateDTO.

        分类ID

        :return: The category_id of this DataClassificationRuleOperateDTO.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        r"""Sets the category_id of this DataClassificationRuleOperateDTO.

        分类ID

        :param category_id: The category_id of this DataClassificationRuleOperateDTO.
        :type category_id: str
        """
        self._category_id = category_id

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
        if not isinstance(other, DataClassificationRuleOperateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
