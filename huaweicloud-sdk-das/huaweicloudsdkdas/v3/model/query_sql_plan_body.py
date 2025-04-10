# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySqlPlanBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_user_id': 'str',
        'database': 'str',
        'sql': 'str'
    }

    attribute_map = {
        'db_user_id': 'db_user_id',
        'database': 'database',
        'sql': 'sql'
    }

    def __init__(self, db_user_id=None, database=None, sql=None):
        r"""QuerySqlPlanBody

        The model defined in huaweicloud sdk

        :param db_user_id: 数据库用户ID
        :type db_user_id: str
        :param database: 数据库名称
        :type database: str
        :param sql: SQL语句
        :type sql: str
        """
        
        

        self._db_user_id = None
        self._database = None
        self._sql = None
        self.discriminator = None

        if db_user_id is not None:
            self.db_user_id = db_user_id
        if database is not None:
            self.database = database
        if sql is not None:
            self.sql = sql

    @property
    def db_user_id(self):
        r"""Gets the db_user_id of this QuerySqlPlanBody.

        数据库用户ID

        :return: The db_user_id of this QuerySqlPlanBody.
        :rtype: str
        """
        return self._db_user_id

    @db_user_id.setter
    def db_user_id(self, db_user_id):
        r"""Sets the db_user_id of this QuerySqlPlanBody.

        数据库用户ID

        :param db_user_id: The db_user_id of this QuerySqlPlanBody.
        :type db_user_id: str
        """
        self._db_user_id = db_user_id

    @property
    def database(self):
        r"""Gets the database of this QuerySqlPlanBody.

        数据库名称

        :return: The database of this QuerySqlPlanBody.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this QuerySqlPlanBody.

        数据库名称

        :param database: The database of this QuerySqlPlanBody.
        :type database: str
        """
        self._database = database

    @property
    def sql(self):
        r"""Gets the sql of this QuerySqlPlanBody.

        SQL语句

        :return: The sql of this QuerySqlPlanBody.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this QuerySqlPlanBody.

        SQL语句

        :param sql: The sql of this QuerySqlPlanBody.
        :type sql: str
        """
        self._sql = sql

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
        if not isinstance(other, QuerySqlPlanBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
