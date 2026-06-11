# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopSql:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sample_time': 'str',
        'count': 'int',
        'database_name': 'str',
        'user_name': 'str',
        'sql_statement': 'str',
        'query_id': 'str'
    }

    attribute_map = {
        'sample_time': 'sample_time',
        'count': 'count',
        'database_name': 'database_name',
        'user_name': 'user_name',
        'sql_statement': 'sql_statement',
        'query_id': 'query_id'
    }

    def __init__(self, sample_time=None, count=None, database_name=None, user_name=None, sql_statement=None, query_id=None):
        r"""TopSql

        The model defined in huaweicloud sdk

        :param sample_time: 采样时间
        :type sample_time: str
        :param count: 个数
        :type count: int
        :param database_name: 数据库名
        :type database_name: str
        :param user_name: 用户名
        :type user_name: str
        :param sql_statement: SQL语句
        :type sql_statement: str
        :param query_id: Query ID
        :type query_id: str
        """
        
        

        self._sample_time = None
        self._count = None
        self._database_name = None
        self._user_name = None
        self._sql_statement = None
        self._query_id = None
        self.discriminator = None

        if sample_time is not None:
            self.sample_time = sample_time
        if count is not None:
            self.count = count
        if database_name is not None:
            self.database_name = database_name
        if user_name is not None:
            self.user_name = user_name
        if sql_statement is not None:
            self.sql_statement = sql_statement
        if query_id is not None:
            self.query_id = query_id

    @property
    def sample_time(self):
        r"""Gets the sample_time of this TopSql.

        采样时间

        :return: The sample_time of this TopSql.
        :rtype: str
        """
        return self._sample_time

    @sample_time.setter
    def sample_time(self, sample_time):
        r"""Sets the sample_time of this TopSql.

        采样时间

        :param sample_time: The sample_time of this TopSql.
        :type sample_time: str
        """
        self._sample_time = sample_time

    @property
    def count(self):
        r"""Gets the count of this TopSql.

        个数

        :return: The count of this TopSql.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this TopSql.

        个数

        :param count: The count of this TopSql.
        :type count: int
        """
        self._count = count

    @property
    def database_name(self):
        r"""Gets the database_name of this TopSql.

        数据库名

        :return: The database_name of this TopSql.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this TopSql.

        数据库名

        :param database_name: The database_name of this TopSql.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def user_name(self):
        r"""Gets the user_name of this TopSql.

        用户名

        :return: The user_name of this TopSql.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this TopSql.

        用户名

        :param user_name: The user_name of this TopSql.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this TopSql.

        SQL语句

        :return: The sql_statement of this TopSql.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this TopSql.

        SQL语句

        :param sql_statement: The sql_statement of this TopSql.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def query_id(self):
        r"""Gets the query_id of this TopSql.

        Query ID

        :return: The query_id of this TopSql.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this TopSql.

        Query ID

        :param query_id: The query_id of this TopSql.
        :type query_id: str
        """
        self._query_id = query_id

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
        if not isinstance(other, TopSql):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
