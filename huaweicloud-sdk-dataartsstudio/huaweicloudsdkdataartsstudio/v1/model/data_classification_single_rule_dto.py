# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataClassificationSingleRuleDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_code': 'str',
        'algorithm_type': 'str',
        'match_type': 'str',
        'expression': 'str',
        'builtin_rule_id': 'str'
    }

    attribute_map = {
        'rule_code': 'rule_code',
        'algorithm_type': 'algorithm_type',
        'match_type': 'match_type',
        'expression': 'expression',
        'builtin_rule_id': 'builtin_rule_id'
    }

    def __init__(self, rule_code=None, algorithm_type=None, match_type=None, expression=None, builtin_rule_id=None):
        r"""DataClassificationSingleRuleDTO

        The model defined in huaweicloud sdk

        :param rule_code: 规则序号,大写字母
        :type rule_code: str
        :param algorithm_type: 算法类型, REGEX,REGEX_INSENSITIVE,GROOVY,LENGTH_EQ,LENGTH_GT,LENGTH_LT,BUILTIN
        :type algorithm_type: str
        :param match_type: 匹配类型, CONTENT,COLUMN,COMMIT,TABLE_NAME,TABLE_COMMENT,DATABASE_NAME
        :type match_type: str
        :param expression: expression
        :type expression: str
        :param builtin_rule_id: 内置规则ID
        :type builtin_rule_id: str
        """
        
        

        self._rule_code = None
        self._algorithm_type = None
        self._match_type = None
        self._expression = None
        self._builtin_rule_id = None
        self.discriminator = None

        self.rule_code = rule_code
        self.algorithm_type = algorithm_type
        self.match_type = match_type
        self.expression = expression
        if builtin_rule_id is not None:
            self.builtin_rule_id = builtin_rule_id

    @property
    def rule_code(self):
        r"""Gets the rule_code of this DataClassificationSingleRuleDTO.

        规则序号,大写字母

        :return: The rule_code of this DataClassificationSingleRuleDTO.
        :rtype: str
        """
        return self._rule_code

    @rule_code.setter
    def rule_code(self, rule_code):
        r"""Sets the rule_code of this DataClassificationSingleRuleDTO.

        规则序号,大写字母

        :param rule_code: The rule_code of this DataClassificationSingleRuleDTO.
        :type rule_code: str
        """
        self._rule_code = rule_code

    @property
    def algorithm_type(self):
        r"""Gets the algorithm_type of this DataClassificationSingleRuleDTO.

        算法类型, REGEX,REGEX_INSENSITIVE,GROOVY,LENGTH_EQ,LENGTH_GT,LENGTH_LT,BUILTIN

        :return: The algorithm_type of this DataClassificationSingleRuleDTO.
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        r"""Sets the algorithm_type of this DataClassificationSingleRuleDTO.

        算法类型, REGEX,REGEX_INSENSITIVE,GROOVY,LENGTH_EQ,LENGTH_GT,LENGTH_LT,BUILTIN

        :param algorithm_type: The algorithm_type of this DataClassificationSingleRuleDTO.
        :type algorithm_type: str
        """
        self._algorithm_type = algorithm_type

    @property
    def match_type(self):
        r"""Gets the match_type of this DataClassificationSingleRuleDTO.

        匹配类型, CONTENT,COLUMN,COMMIT,TABLE_NAME,TABLE_COMMENT,DATABASE_NAME

        :return: The match_type of this DataClassificationSingleRuleDTO.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this DataClassificationSingleRuleDTO.

        匹配类型, CONTENT,COLUMN,COMMIT,TABLE_NAME,TABLE_COMMENT,DATABASE_NAME

        :param match_type: The match_type of this DataClassificationSingleRuleDTO.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def expression(self):
        r"""Gets the expression of this DataClassificationSingleRuleDTO.

        expression

        :return: The expression of this DataClassificationSingleRuleDTO.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this DataClassificationSingleRuleDTO.

        expression

        :param expression: The expression of this DataClassificationSingleRuleDTO.
        :type expression: str
        """
        self._expression = expression

    @property
    def builtin_rule_id(self):
        r"""Gets the builtin_rule_id of this DataClassificationSingleRuleDTO.

        内置规则ID

        :return: The builtin_rule_id of this DataClassificationSingleRuleDTO.
        :rtype: str
        """
        return self._builtin_rule_id

    @builtin_rule_id.setter
    def builtin_rule_id(self, builtin_rule_id):
        r"""Sets the builtin_rule_id of this DataClassificationSingleRuleDTO.

        内置规则ID

        :param builtin_rule_id: The builtin_rule_id of this DataClassificationSingleRuleDTO.
        :type builtin_rule_id: str
        """
        self._builtin_rule_id = builtin_rule_id

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
        if not isinstance(other, DataClassificationSingleRuleDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
