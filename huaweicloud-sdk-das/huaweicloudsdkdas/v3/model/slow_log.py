# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLog:

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
        'database': 'str',
        'client': 'str',
        'user': 'str',
        'execute_at': 'int',
        'query_time': 'float',
        'lock_time': 'float',
        'rows_examined': 'int',
        'rows_sent': 'int'
    }

    attribute_map = {
        'sql': 'sql',
        'database': 'database',
        'client': 'client',
        'user': 'user',
        'execute_at': 'execute_at',
        'query_time': 'query_time',
        'lock_time': 'lock_time',
        'rows_examined': 'rows_examined',
        'rows_sent': 'rows_sent'
    }

    def __init__(self, sql=None, database=None, client=None, user=None, execute_at=None, query_time=None, lock_time=None, rows_examined=None, rows_sent=None):
        """SlowLog

        The model defined in huaweicloud sdk

        :param sql: SQL语句。
        :type sql: str
        :param database: 数据库名。
        :type database: str
        :param client: 客户端。
        :type client: str
        :param user: 用户。
        :type user: str
        :param execute_at: 执行开始时间（Unix timestamp），单位：毫秒。
        :type execute_at: int
        :param query_time: 执行耗时（秒）。
        :type query_time: float
        :param lock_time: 锁等待耗时（秒）。
        :type lock_time: float
        :param rows_examined: 扫描行数。
        :type rows_examined: int
        :param rows_sent: 返回行数。
        :type rows_sent: int
        """
        
        

        self._sql = None
        self._database = None
        self._client = None
        self._user = None
        self._execute_at = None
        self._query_time = None
        self._lock_time = None
        self._rows_examined = None
        self._rows_sent = None
        self.discriminator = None

        self.sql = sql
        self.database = database
        self.client = client
        self.user = user
        self.execute_at = execute_at
        self.query_time = query_time
        self.lock_time = lock_time
        self.rows_examined = rows_examined
        self.rows_sent = rows_sent

    @property
    def sql(self):
        """Gets the sql of this SlowLog.

        SQL语句。

        :return: The sql of this SlowLog.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this SlowLog.

        SQL语句。

        :param sql: The sql of this SlowLog.
        :type sql: str
        """
        self._sql = sql

    @property
    def database(self):
        """Gets the database of this SlowLog.

        数据库名。

        :return: The database of this SlowLog.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SlowLog.

        数据库名。

        :param database: The database of this SlowLog.
        :type database: str
        """
        self._database = database

    @property
    def client(self):
        """Gets the client of this SlowLog.

        客户端。

        :return: The client of this SlowLog.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this SlowLog.

        客户端。

        :param client: The client of this SlowLog.
        :type client: str
        """
        self._client = client

    @property
    def user(self):
        """Gets the user of this SlowLog.

        用户。

        :return: The user of this SlowLog.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SlowLog.

        用户。

        :param user: The user of this SlowLog.
        :type user: str
        """
        self._user = user

    @property
    def execute_at(self):
        """Gets the execute_at of this SlowLog.

        执行开始时间（Unix timestamp），单位：毫秒。

        :return: The execute_at of this SlowLog.
        :rtype: int
        """
        return self._execute_at

    @execute_at.setter
    def execute_at(self, execute_at):
        """Sets the execute_at of this SlowLog.

        执行开始时间（Unix timestamp），单位：毫秒。

        :param execute_at: The execute_at of this SlowLog.
        :type execute_at: int
        """
        self._execute_at = execute_at

    @property
    def query_time(self):
        """Gets the query_time of this SlowLog.

        执行耗时（秒）。

        :return: The query_time of this SlowLog.
        :rtype: float
        """
        return self._query_time

    @query_time.setter
    def query_time(self, query_time):
        """Sets the query_time of this SlowLog.

        执行耗时（秒）。

        :param query_time: The query_time of this SlowLog.
        :type query_time: float
        """
        self._query_time = query_time

    @property
    def lock_time(self):
        """Gets the lock_time of this SlowLog.

        锁等待耗时（秒）。

        :return: The lock_time of this SlowLog.
        :rtype: float
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this SlowLog.

        锁等待耗时（秒）。

        :param lock_time: The lock_time of this SlowLog.
        :type lock_time: float
        """
        self._lock_time = lock_time

    @property
    def rows_examined(self):
        """Gets the rows_examined of this SlowLog.

        扫描行数。

        :return: The rows_examined of this SlowLog.
        :rtype: int
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        """Sets the rows_examined of this SlowLog.

        扫描行数。

        :param rows_examined: The rows_examined of this SlowLog.
        :type rows_examined: int
        """
        self._rows_examined = rows_examined

    @property
    def rows_sent(self):
        """Gets the rows_sent of this SlowLog.

        返回行数。

        :return: The rows_sent of this SlowLog.
        :rtype: int
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        """Sets the rows_sent of this SlowLog.

        返回行数。

        :param rows_sent: The rows_sent of this SlowLog.
        :type rows_sent: int
        """
        self._rows_sent = rows_sent

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
        if not isinstance(other, SlowLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
