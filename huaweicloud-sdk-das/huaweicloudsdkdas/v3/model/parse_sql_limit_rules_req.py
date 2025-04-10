# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParseSqlLimitRulesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str',
        'original_sql': 'str',
        'use_template': 'bool',
        'keep_operators': 'bool'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'original_sql': 'original_sql',
        'use_template': 'use_template',
        'keep_operators': 'keep_operators'
    }

    def __init__(self, datastore_type=None, original_sql=None, use_template=None, keep_operators=None):
        r"""ParseSqlLimitRulesReq

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库类型，目前支持MySQL、MariaDB、GaussDB(for MySQL)三种引擎。
        :type datastore_type: str
        :param original_sql: 原始SQL语句
        :type original_sql: str
        :param use_template: 是否校验SQL语句
        :type use_template: bool
        :param keep_operators: 是否保留操作符
        :type keep_operators: bool
        """
        
        

        self._datastore_type = None
        self._original_sql = None
        self._use_template = None
        self._keep_operators = None
        self.discriminator = None

        self.datastore_type = datastore_type
        self.original_sql = original_sql
        self.use_template = use_template
        self.keep_operators = keep_operators

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ParseSqlLimitRulesReq.

        数据库类型，目前支持MySQL、MariaDB、GaussDB(for MySQL)三种引擎。

        :return: The datastore_type of this ParseSqlLimitRulesReq.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ParseSqlLimitRulesReq.

        数据库类型，目前支持MySQL、MariaDB、GaussDB(for MySQL)三种引擎。

        :param datastore_type: The datastore_type of this ParseSqlLimitRulesReq.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def original_sql(self):
        r"""Gets the original_sql of this ParseSqlLimitRulesReq.

        原始SQL语句

        :return: The original_sql of this ParseSqlLimitRulesReq.
        :rtype: str
        """
        return self._original_sql

    @original_sql.setter
    def original_sql(self, original_sql):
        r"""Sets the original_sql of this ParseSqlLimitRulesReq.

        原始SQL语句

        :param original_sql: The original_sql of this ParseSqlLimitRulesReq.
        :type original_sql: str
        """
        self._original_sql = original_sql

    @property
    def use_template(self):
        r"""Gets the use_template of this ParseSqlLimitRulesReq.

        是否校验SQL语句

        :return: The use_template of this ParseSqlLimitRulesReq.
        :rtype: bool
        """
        return self._use_template

    @use_template.setter
    def use_template(self, use_template):
        r"""Sets the use_template of this ParseSqlLimitRulesReq.

        是否校验SQL语句

        :param use_template: The use_template of this ParseSqlLimitRulesReq.
        :type use_template: bool
        """
        self._use_template = use_template

    @property
    def keep_operators(self):
        r"""Gets the keep_operators of this ParseSqlLimitRulesReq.

        是否保留操作符

        :return: The keep_operators of this ParseSqlLimitRulesReq.
        :rtype: bool
        """
        return self._keep_operators

    @keep_operators.setter
    def keep_operators(self, keep_operators):
        r"""Sets the keep_operators of this ParseSqlLimitRulesReq.

        是否保留操作符

        :param keep_operators: The keep_operators of this ParseSqlLimitRulesReq.
        :type keep_operators: bool
        """
        self._keep_operators = keep_operators

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
        if not isinstance(other, ParseSqlLimitRulesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
