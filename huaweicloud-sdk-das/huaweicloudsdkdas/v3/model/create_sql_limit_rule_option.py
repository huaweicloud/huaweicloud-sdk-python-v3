# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSqlLimitRuleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_type': 'str',
        'max_concurrency': 'int',
        'pattern': 'str'
    }

    attribute_map = {
        'sql_type': 'sql_type',
        'max_concurrency': 'max_concurrency',
        'pattern': 'pattern'
    }

    def __init__(self, sql_type=None, max_concurrency=None, pattern=None):
        """CreateSqlLimitRuleOption

        The model defined in huaweicloud sdk

        :param sql_type: SQL类型
        :type sql_type: str
        :param max_concurrency: 最大并发数
        :type max_concurrency: int
        :param pattern: SQL限流规则。限流规则以~分隔关键字，例如select~a。规则举例详细说明：例如关键字是\&quot;select~a\&quot;, 含义为：select以及a为该并发控制所包含的两个关键字，~为关键字间隔符，即若执行SQL命令包含select与a两个关键字视为命中此条并发控制规则。
        :type pattern: str
        """
        
        

        self._sql_type = None
        self._max_concurrency = None
        self._pattern = None
        self.discriminator = None

        self.sql_type = sql_type
        self.max_concurrency = max_concurrency
        self.pattern = pattern

    @property
    def sql_type(self):
        """Gets the sql_type of this CreateSqlLimitRuleOption.

        SQL类型

        :return: The sql_type of this CreateSqlLimitRuleOption.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        """Sets the sql_type of this CreateSqlLimitRuleOption.

        SQL类型

        :param sql_type: The sql_type of this CreateSqlLimitRuleOption.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def max_concurrency(self):
        """Gets the max_concurrency of this CreateSqlLimitRuleOption.

        最大并发数

        :return: The max_concurrency of this CreateSqlLimitRuleOption.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        """Sets the max_concurrency of this CreateSqlLimitRuleOption.

        最大并发数

        :param max_concurrency: The max_concurrency of this CreateSqlLimitRuleOption.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

    @property
    def pattern(self):
        """Gets the pattern of this CreateSqlLimitRuleOption.

        SQL限流规则。限流规则以~分隔关键字，例如select~a。规则举例详细说明：例如关键字是\"select~a\", 含义为：select以及a为该并发控制所包含的两个关键字，~为关键字间隔符，即若执行SQL命令包含select与a两个关键字视为命中此条并发控制规则。

        :return: The pattern of this CreateSqlLimitRuleOption.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this CreateSqlLimitRuleOption.

        SQL限流规则。限流规则以~分隔关键字，例如select~a。规则举例详细说明：例如关键字是\"select~a\", 含义为：select以及a为该并发控制所包含的两个关键字，~为关键字间隔符，即若执行SQL命令包含select与a两个关键字视为命中此条并发控制规则。

        :param pattern: The pattern of this CreateSqlLimitRuleOption.
        :type pattern: str
        """
        self._pattern = pattern

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
        if not isinstance(other, CreateSqlLimitRuleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
