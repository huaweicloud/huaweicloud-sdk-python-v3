# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSqlLimitRulesBody:

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
        'sql_limit_rule_ids': 'list[str]',
        'database_name': 'str'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'sql_limit_rule_ids': 'sql_limit_rule_ids',
        'database_name': 'database_name'
    }

    def __init__(self, datastore_type=None, sql_limit_rule_ids=None, database_name=None):
        """DeleteSqlLimitRulesBody

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库类型
        :type datastore_type: str
        :param sql_limit_rule_ids: SQL限流规则ID
        :type sql_limit_rule_ids: list[str]
        :param database_name: 数据库名（PostgreSQL必填）
        :type database_name: str
        """
        
        

        self._datastore_type = None
        self._sql_limit_rule_ids = None
        self._database_name = None
        self.discriminator = None

        self.datastore_type = datastore_type
        self.sql_limit_rule_ids = sql_limit_rule_ids
        if database_name is not None:
            self.database_name = database_name

    @property
    def datastore_type(self):
        """Gets the datastore_type of this DeleteSqlLimitRulesBody.

        数据库类型

        :return: The datastore_type of this DeleteSqlLimitRulesBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this DeleteSqlLimitRulesBody.

        数据库类型

        :param datastore_type: The datastore_type of this DeleteSqlLimitRulesBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def sql_limit_rule_ids(self):
        """Gets the sql_limit_rule_ids of this DeleteSqlLimitRulesBody.

        SQL限流规则ID

        :return: The sql_limit_rule_ids of this DeleteSqlLimitRulesBody.
        :rtype: list[str]
        """
        return self._sql_limit_rule_ids

    @sql_limit_rule_ids.setter
    def sql_limit_rule_ids(self, sql_limit_rule_ids):
        """Sets the sql_limit_rule_ids of this DeleteSqlLimitRulesBody.

        SQL限流规则ID

        :param sql_limit_rule_ids: The sql_limit_rule_ids of this DeleteSqlLimitRulesBody.
        :type sql_limit_rule_ids: list[str]
        """
        self._sql_limit_rule_ids = sql_limit_rule_ids

    @property
    def database_name(self):
        """Gets the database_name of this DeleteSqlLimitRulesBody.

        数据库名（PostgreSQL必填）

        :return: The database_name of this DeleteSqlLimitRulesBody.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this DeleteSqlLimitRulesBody.

        数据库名（PostgreSQL必填）

        :param database_name: The database_name of this DeleteSqlLimitRulesBody.
        :type database_name: str
        """
        self._database_name = database_name

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
        if not isinstance(other, DeleteSqlLimitRulesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
