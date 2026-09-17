# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullSqlSampleInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql': 'str',
        'sql_template_id': 'str',
        'database': 'str',
        'client': 'str',
        'user': 'str',
        'execute_at': 'int',
        'query_time': 'float',
        'lock_time': 'float'
    }

    attribute_map = {
        'sql': 'sql',
        'sql_template_id': 'sql_template_id',
        'database': 'database',
        'client': 'client',
        'user': 'user',
        'execute_at': 'execute_at',
        'query_time': 'query_time',
        'lock_time': 'lock_time'
    }

    def __init__(self, sql=None, sql_template_id=None, database=None, client=None, user=None, execute_at=None, query_time=None, lock_time=None):
        r"""FullSqlSampleInfo

        The model defined in huaweicloud sdk

        :param sql: SQL
        :type sql: str
        :param sql_template_id: SQL模板
        :type sql_template_id: str
        :param database: 数据库名称
        :type database: str
        :param client: 客户端地址
        :type client: str
        :param user: 用户名
        :type user: str
        :param execute_at: 执行时间
        :type execute_at: int
        :param query_time: 执行耗时（ms）
        :type query_time: float
        :param lock_time: 锁等待时间（ms）
        :type lock_time: float
        """
        
        

        self._sql = None
        self._sql_template_id = None
        self._database = None
        self._client = None
        self._user = None
        self._execute_at = None
        self._query_time = None
        self._lock_time = None
        self.discriminator = None

        if sql is not None:
            self.sql = sql
        if sql_template_id is not None:
            self.sql_template_id = sql_template_id
        if database is not None:
            self.database = database
        if client is not None:
            self.client = client
        if user is not None:
            self.user = user
        if execute_at is not None:
            self.execute_at = execute_at
        if query_time is not None:
            self.query_time = query_time
        if lock_time is not None:
            self.lock_time = lock_time

    @property
    def sql(self):
        r"""Gets the sql of this FullSqlSampleInfo.

        SQL

        :return: The sql of this FullSqlSampleInfo.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this FullSqlSampleInfo.

        SQL

        :param sql: The sql of this FullSqlSampleInfo.
        :type sql: str
        """
        self._sql = sql

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this FullSqlSampleInfo.

        SQL模板

        :return: The sql_template_id of this FullSqlSampleInfo.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this FullSqlSampleInfo.

        SQL模板

        :param sql_template_id: The sql_template_id of this FullSqlSampleInfo.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def database(self):
        r"""Gets the database of this FullSqlSampleInfo.

        数据库名称

        :return: The database of this FullSqlSampleInfo.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this FullSqlSampleInfo.

        数据库名称

        :param database: The database of this FullSqlSampleInfo.
        :type database: str
        """
        self._database = database

    @property
    def client(self):
        r"""Gets the client of this FullSqlSampleInfo.

        客户端地址

        :return: The client of this FullSqlSampleInfo.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        r"""Sets the client of this FullSqlSampleInfo.

        客户端地址

        :param client: The client of this FullSqlSampleInfo.
        :type client: str
        """
        self._client = client

    @property
    def user(self):
        r"""Gets the user of this FullSqlSampleInfo.

        用户名

        :return: The user of this FullSqlSampleInfo.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this FullSqlSampleInfo.

        用户名

        :param user: The user of this FullSqlSampleInfo.
        :type user: str
        """
        self._user = user

    @property
    def execute_at(self):
        r"""Gets the execute_at of this FullSqlSampleInfo.

        执行时间

        :return: The execute_at of this FullSqlSampleInfo.
        :rtype: int
        """
        return self._execute_at

    @execute_at.setter
    def execute_at(self, execute_at):
        r"""Sets the execute_at of this FullSqlSampleInfo.

        执行时间

        :param execute_at: The execute_at of this FullSqlSampleInfo.
        :type execute_at: int
        """
        self._execute_at = execute_at

    @property
    def query_time(self):
        r"""Gets the query_time of this FullSqlSampleInfo.

        执行耗时（ms）

        :return: The query_time of this FullSqlSampleInfo.
        :rtype: float
        """
        return self._query_time

    @query_time.setter
    def query_time(self, query_time):
        r"""Sets the query_time of this FullSqlSampleInfo.

        执行耗时（ms）

        :param query_time: The query_time of this FullSqlSampleInfo.
        :type query_time: float
        """
        self._query_time = query_time

    @property
    def lock_time(self):
        r"""Gets the lock_time of this FullSqlSampleInfo.

        锁等待时间（ms）

        :return: The lock_time of this FullSqlSampleInfo.
        :rtype: float
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this FullSqlSampleInfo.

        锁等待时间（ms）

        :param lock_time: The lock_time of this FullSqlSampleInfo.
        :type lock_time: float
        """
        self._lock_time = lock_time

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
        if not isinstance(other, FullSqlSampleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
