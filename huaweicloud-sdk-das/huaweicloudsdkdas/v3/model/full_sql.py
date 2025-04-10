# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullSql:

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
        'operate_type': 'str',
        'status': 'str',
        'error_no': 'str',
        'database': 'str',
        'client': 'str',
        'thread_id': 'str',
        'user': 'str',
        'execute_at': 'int',
        'query_time': 'float',
        'lock_time': 'float',
        'rows_examined': 'int',
        'rows_sent': 'int',
        'rows_affected': 'int'
    }

    attribute_map = {
        'sql': 'sql',
        'operate_type': 'operate_type',
        'status': 'status',
        'error_no': 'error_no',
        'database': 'database',
        'client': 'client',
        'thread_id': 'thread_id',
        'user': 'user',
        'execute_at': 'execute_at',
        'query_time': 'query_time',
        'lock_time': 'lock_time',
        'rows_examined': 'rows_examined',
        'rows_sent': 'rows_sent',
        'rows_affected': 'rows_affected'
    }

    def __init__(self, sql=None, operate_type=None, status=None, error_no=None, database=None, client=None, thread_id=None, user=None, execute_at=None, query_time=None, lock_time=None, rows_examined=None, rows_sent=None, rows_affected=None):
        r"""FullSql

        The model defined in huaweicloud sdk

        :param sql: SQL语句。
        :type sql: str
        :param operate_type: 操作类型。
        :type operate_type: str
        :param status: 状态。
        :type status: str
        :param error_no: 错误码。
        :type error_no: str
        :param database: 数据库名。
        :type database: str
        :param client: 客户端。
        :type client: str
        :param thread_id: 线程ID。
        :type thread_id: str
        :param user: 用户。
        :type user: str
        :param execute_at: 执行开始时间（Unix timestamp），单位：毫秒。
        :type execute_at: int
        :param query_time: 执行耗时（毫秒）。
        :type query_time: float
        :param lock_time: 锁等待耗时（毫秒）。
        :type lock_time: float
        :param rows_examined: 扫描行数。
        :type rows_examined: int
        :param rows_sent: 返回行数。
        :type rows_sent: int
        :param rows_affected: 更新行数。
        :type rows_affected: int
        """
        
        

        self._sql = None
        self._operate_type = None
        self._status = None
        self._error_no = None
        self._database = None
        self._client = None
        self._thread_id = None
        self._user = None
        self._execute_at = None
        self._query_time = None
        self._lock_time = None
        self._rows_examined = None
        self._rows_sent = None
        self._rows_affected = None
        self.discriminator = None

        self.sql = sql
        self.operate_type = operate_type
        self.status = status
        self.error_no = error_no
        self.database = database
        self.client = client
        self.thread_id = thread_id
        self.user = user
        self.execute_at = execute_at
        self.query_time = query_time
        self.lock_time = lock_time
        self.rows_examined = rows_examined
        self.rows_sent = rows_sent
        self.rows_affected = rows_affected

    @property
    def sql(self):
        r"""Gets the sql of this FullSql.

        SQL语句。

        :return: The sql of this FullSql.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this FullSql.

        SQL语句。

        :param sql: The sql of this FullSql.
        :type sql: str
        """
        self._sql = sql

    @property
    def operate_type(self):
        r"""Gets the operate_type of this FullSql.

        操作类型。

        :return: The operate_type of this FullSql.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this FullSql.

        操作类型。

        :param operate_type: The operate_type of this FullSql.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def status(self):
        r"""Gets the status of this FullSql.

        状态。

        :return: The status of this FullSql.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FullSql.

        状态。

        :param status: The status of this FullSql.
        :type status: str
        """
        self._status = status

    @property
    def error_no(self):
        r"""Gets the error_no of this FullSql.

        错误码。

        :return: The error_no of this FullSql.
        :rtype: str
        """
        return self._error_no

    @error_no.setter
    def error_no(self, error_no):
        r"""Sets the error_no of this FullSql.

        错误码。

        :param error_no: The error_no of this FullSql.
        :type error_no: str
        """
        self._error_no = error_no

    @property
    def database(self):
        r"""Gets the database of this FullSql.

        数据库名。

        :return: The database of this FullSql.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this FullSql.

        数据库名。

        :param database: The database of this FullSql.
        :type database: str
        """
        self._database = database

    @property
    def client(self):
        r"""Gets the client of this FullSql.

        客户端。

        :return: The client of this FullSql.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        r"""Sets the client of this FullSql.

        客户端。

        :param client: The client of this FullSql.
        :type client: str
        """
        self._client = client

    @property
    def thread_id(self):
        r"""Gets the thread_id of this FullSql.

        线程ID。

        :return: The thread_id of this FullSql.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this FullSql.

        线程ID。

        :param thread_id: The thread_id of this FullSql.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def user(self):
        r"""Gets the user of this FullSql.

        用户。

        :return: The user of this FullSql.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this FullSql.

        用户。

        :param user: The user of this FullSql.
        :type user: str
        """
        self._user = user

    @property
    def execute_at(self):
        r"""Gets the execute_at of this FullSql.

        执行开始时间（Unix timestamp），单位：毫秒。

        :return: The execute_at of this FullSql.
        :rtype: int
        """
        return self._execute_at

    @execute_at.setter
    def execute_at(self, execute_at):
        r"""Sets the execute_at of this FullSql.

        执行开始时间（Unix timestamp），单位：毫秒。

        :param execute_at: The execute_at of this FullSql.
        :type execute_at: int
        """
        self._execute_at = execute_at

    @property
    def query_time(self):
        r"""Gets the query_time of this FullSql.

        执行耗时（毫秒）。

        :return: The query_time of this FullSql.
        :rtype: float
        """
        return self._query_time

    @query_time.setter
    def query_time(self, query_time):
        r"""Sets the query_time of this FullSql.

        执行耗时（毫秒）。

        :param query_time: The query_time of this FullSql.
        :type query_time: float
        """
        self._query_time = query_time

    @property
    def lock_time(self):
        r"""Gets the lock_time of this FullSql.

        锁等待耗时（毫秒）。

        :return: The lock_time of this FullSql.
        :rtype: float
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this FullSql.

        锁等待耗时（毫秒）。

        :param lock_time: The lock_time of this FullSql.
        :type lock_time: float
        """
        self._lock_time = lock_time

    @property
    def rows_examined(self):
        r"""Gets the rows_examined of this FullSql.

        扫描行数。

        :return: The rows_examined of this FullSql.
        :rtype: int
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        r"""Sets the rows_examined of this FullSql.

        扫描行数。

        :param rows_examined: The rows_examined of this FullSql.
        :type rows_examined: int
        """
        self._rows_examined = rows_examined

    @property
    def rows_sent(self):
        r"""Gets the rows_sent of this FullSql.

        返回行数。

        :return: The rows_sent of this FullSql.
        :rtype: int
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        r"""Sets the rows_sent of this FullSql.

        返回行数。

        :param rows_sent: The rows_sent of this FullSql.
        :type rows_sent: int
        """
        self._rows_sent = rows_sent

    @property
    def rows_affected(self):
        r"""Gets the rows_affected of this FullSql.

        更新行数。

        :return: The rows_affected of this FullSql.
        :rtype: int
        """
        return self._rows_affected

    @rows_affected.setter
    def rows_affected(self, rows_affected):
        r"""Sets the rows_affected of this FullSql.

        更新行数。

        :param rows_affected: The rows_affected of this FullSql.
        :type rows_affected: int
        """
        self._rows_affected = rows_affected

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
        if not isinstance(other, FullSql):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
