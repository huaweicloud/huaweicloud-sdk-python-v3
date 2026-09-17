# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParseSqlLimitRuleNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'original_sql': 'str',
        'engine_type': 'str',
        'use_template': 'bool',
        'keep_operators': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'original_sql': 'original_sql',
        'engine_type': 'engine_type',
        'use_template': 'use_template',
        'keep_operators': 'keep_operators',
        'type': 'type'
    }

    def __init__(self, original_sql=None, engine_type=None, use_template=None, keep_operators=None, type=None):
        r"""ParseSqlLimitRuleNewRequestBody

        The model defined in huaweicloud sdk

        :param original_sql: 原始SQL语句
        :type original_sql: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param use_template: 是否校验SQL语句
        :type use_template: bool
        :param keep_operators: 是否保留操作符
        :type keep_operators: bool
        :param type: SQL类型
        :type type: str
        """
        
        

        self._original_sql = None
        self._engine_type = None
        self._use_template = None
        self._keep_operators = None
        self._type = None
        self.discriminator = None

        self.original_sql = original_sql
        self.engine_type = engine_type
        self.use_template = use_template
        self.keep_operators = keep_operators
        self.type = type

    @property
    def original_sql(self):
        r"""Gets the original_sql of this ParseSqlLimitRuleNewRequestBody.

        原始SQL语句

        :return: The original_sql of this ParseSqlLimitRuleNewRequestBody.
        :rtype: str
        """
        return self._original_sql

    @original_sql.setter
    def original_sql(self, original_sql):
        r"""Sets the original_sql of this ParseSqlLimitRuleNewRequestBody.

        原始SQL语句

        :param original_sql: The original_sql of this ParseSqlLimitRuleNewRequestBody.
        :type original_sql: str
        """
        self._original_sql = original_sql

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ParseSqlLimitRuleNewRequestBody.

        数据库引擎类型

        :return: The engine_type of this ParseSqlLimitRuleNewRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ParseSqlLimitRuleNewRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this ParseSqlLimitRuleNewRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def use_template(self):
        r"""Gets the use_template of this ParseSqlLimitRuleNewRequestBody.

        是否校验SQL语句

        :return: The use_template of this ParseSqlLimitRuleNewRequestBody.
        :rtype: bool
        """
        return self._use_template

    @use_template.setter
    def use_template(self, use_template):
        r"""Sets the use_template of this ParseSqlLimitRuleNewRequestBody.

        是否校验SQL语句

        :param use_template: The use_template of this ParseSqlLimitRuleNewRequestBody.
        :type use_template: bool
        """
        self._use_template = use_template

    @property
    def keep_operators(self):
        r"""Gets the keep_operators of this ParseSqlLimitRuleNewRequestBody.

        是否保留操作符

        :return: The keep_operators of this ParseSqlLimitRuleNewRequestBody.
        :rtype: bool
        """
        return self._keep_operators

    @keep_operators.setter
    def keep_operators(self, keep_operators):
        r"""Sets the keep_operators of this ParseSqlLimitRuleNewRequestBody.

        是否保留操作符

        :param keep_operators: The keep_operators of this ParseSqlLimitRuleNewRequestBody.
        :type keep_operators: bool
        """
        self._keep_operators = keep_operators

    @property
    def type(self):
        r"""Gets the type of this ParseSqlLimitRuleNewRequestBody.

        SQL类型

        :return: The type of this ParseSqlLimitRuleNewRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ParseSqlLimitRuleNewRequestBody.

        SQL类型

        :param type: The type of this ParseSqlLimitRuleNewRequestBody.
        :type type: str
        """
        self._type = type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ParseSqlLimitRuleNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
