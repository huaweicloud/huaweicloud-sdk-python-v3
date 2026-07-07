# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockAnalysisResultRespSqlList:

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
        'occurrence_time': 'int',
        'query_time': 'int',
        'transaction_id': 'str',
        'sql_template_id': 'str',
        'node_id': 'str',
        'db_user': 'str',
        'database': 'str',
        'client': 'str',
        'sql_type': 'str',
        'status': 'int',
        'error_no': 'int',
        'rows_affected': 'int',
        'rows_sent': 'int',
        'lock_time': 'int',
        'rows_examined': 'int',
        'session_id': 'str',
        'cpu_time': 'int',
        'send_bytes': 'int',
        'query_tables': 'str',
        'innodb_io_read_bytes': 'int',
        'innodb_io_read': 'int',
        'innodb_io_read_wait': 'int',
        'innodb_lock_wait': 'int',
        'innodb_queue_wait': 'int'
    }

    attribute_map = {
        'sql': 'sql',
        'occurrence_time': 'occurrence_time',
        'query_time': 'query_time',
        'transaction_id': 'transaction_id',
        'sql_template_id': 'sql_template_id',
        'node_id': 'node_id',
        'db_user': 'db_user',
        'database': 'database',
        'client': 'client',
        'sql_type': 'sql_type',
        'status': 'status',
        'error_no': 'error_no',
        'rows_affected': 'rows_affected',
        'rows_sent': 'rows_sent',
        'lock_time': 'lock_time',
        'rows_examined': 'rows_examined',
        'session_id': 'session_id',
        'cpu_time': 'cpu_time',
        'send_bytes': 'send_bytes',
        'query_tables': 'query_tables',
        'innodb_io_read_bytes': 'innodb_io_read_bytes',
        'innodb_io_read': 'innodb_io_read',
        'innodb_io_read_wait': 'innodb_io_read_wait',
        'innodb_lock_wait': 'innodb_lock_wait',
        'innodb_queue_wait': 'innodb_queue_wait'
    }

    def __init__(self, sql=None, occurrence_time=None, query_time=None, transaction_id=None, sql_template_id=None, node_id=None, db_user=None, database=None, client=None, sql_type=None, status=None, error_no=None, rows_affected=None, rows_sent=None, lock_time=None, rows_examined=None, session_id=None, cpu_time=None, send_bytes=None, query_tables=None, innodb_io_read_bytes=None, innodb_io_read=None, innodb_io_read_wait=None, innodb_lock_wait=None, innodb_queue_wait=None):
        r"""ShowDeadLockAnalysisResultRespSqlList

        The model defined in huaweicloud sdk

        :param sql: SQL语句
        :type sql: str
        :param occurrence_time: 发生时间
        :type occurrence_time: int
        :param query_time: 执行耗时毫秒
        :type query_time: int
        :param transaction_id: 事务ID
        :type transaction_id: str
        :param sql_template_id: 模板ID
        :type sql_template_id: str
        :param node_id: 节点ID
        :type node_id: str
        :param db_user: 用户名
        :type db_user: str
        :param database: 数据库
        :type database: str
        :param client: 客户端IP
        :type client: str
        :param sql_type: SQL类型
        :type sql_type: str
        :param status: 执行状态
        :type status: int
        :param error_no: 错误码
        :type error_no: int
        :param rows_affected: 更新行数
        :type rows_affected: int
        :param rows_sent: 返回行数
        :type rows_sent: int
        :param lock_time: 锁等待时间毫秒
        :type lock_time: int
        :param rows_examined: 扫描行数
        :type rows_examined: int
        :param session_id: 线程ID
        :type session_id: str
        :param cpu_time: CPU耗时(us)
        :type cpu_time: int
        :param send_bytes: 网络发送字节数
        :type send_bytes: int
        :param query_tables: 查询中所有的表名
        :type query_tables: str
        :param innodb_io_read_bytes: 物理I/O读字节数
        :type innodb_io_read_bytes: int
        :param innodb_io_read: 物理I/O读次数
        :type innodb_io_read: int
        :param innodb_io_read_wait: 物理I/O读取等待耗时(ms)
        :type innodb_io_read_wait: int
        :param innodb_lock_wait: 物理I/O读取等待耗时(ms)
        :type innodb_lock_wait: int
        :param innodb_queue_wait: 行锁等待耗时(ms)
        :type innodb_queue_wait: int
        """
        
        

        self._sql = None
        self._occurrence_time = None
        self._query_time = None
        self._transaction_id = None
        self._sql_template_id = None
        self._node_id = None
        self._db_user = None
        self._database = None
        self._client = None
        self._sql_type = None
        self._status = None
        self._error_no = None
        self._rows_affected = None
        self._rows_sent = None
        self._lock_time = None
        self._rows_examined = None
        self._session_id = None
        self._cpu_time = None
        self._send_bytes = None
        self._query_tables = None
        self._innodb_io_read_bytes = None
        self._innodb_io_read = None
        self._innodb_io_read_wait = None
        self._innodb_lock_wait = None
        self._innodb_queue_wait = None
        self.discriminator = None

        self.sql = sql
        self.occurrence_time = occurrence_time
        self.query_time = query_time
        self.transaction_id = transaction_id
        self.sql_template_id = sql_template_id
        self.node_id = node_id
        self.db_user = db_user
        self.database = database
        self.client = client
        self.sql_type = sql_type
        self.status = status
        self.error_no = error_no
        self.rows_affected = rows_affected
        self.rows_sent = rows_sent
        self.lock_time = lock_time
        self.rows_examined = rows_examined
        self.session_id = session_id
        self.cpu_time = cpu_time
        self.send_bytes = send_bytes
        self.query_tables = query_tables
        self.innodb_io_read_bytes = innodb_io_read_bytes
        self.innodb_io_read = innodb_io_read
        self.innodb_io_read_wait = innodb_io_read_wait
        self.innodb_lock_wait = innodb_lock_wait
        self.innodb_queue_wait = innodb_queue_wait

    @property
    def sql(self):
        r"""Gets the sql of this ShowDeadLockAnalysisResultRespSqlList.

        SQL语句

        :return: The sql of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this ShowDeadLockAnalysisResultRespSqlList.

        SQL语句

        :param sql: The sql of this ShowDeadLockAnalysisResultRespSqlList.
        :type sql: str
        """
        self._sql = sql

    @property
    def occurrence_time(self):
        r"""Gets the occurrence_time of this ShowDeadLockAnalysisResultRespSqlList.

        发生时间

        :return: The occurrence_time of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._occurrence_time

    @occurrence_time.setter
    def occurrence_time(self, occurrence_time):
        r"""Sets the occurrence_time of this ShowDeadLockAnalysisResultRespSqlList.

        发生时间

        :param occurrence_time: The occurrence_time of this ShowDeadLockAnalysisResultRespSqlList.
        :type occurrence_time: int
        """
        self._occurrence_time = occurrence_time

    @property
    def query_time(self):
        r"""Gets the query_time of this ShowDeadLockAnalysisResultRespSqlList.

        执行耗时毫秒

        :return: The query_time of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._query_time

    @query_time.setter
    def query_time(self, query_time):
        r"""Sets the query_time of this ShowDeadLockAnalysisResultRespSqlList.

        执行耗时毫秒

        :param query_time: The query_time of this ShowDeadLockAnalysisResultRespSqlList.
        :type query_time: int
        """
        self._query_time = query_time

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this ShowDeadLockAnalysisResultRespSqlList.

        事务ID

        :return: The transaction_id of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this ShowDeadLockAnalysisResultRespSqlList.

        事务ID

        :param transaction_id: The transaction_id of this ShowDeadLockAnalysisResultRespSqlList.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this ShowDeadLockAnalysisResultRespSqlList.

        模板ID

        :return: The sql_template_id of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this ShowDeadLockAnalysisResultRespSqlList.

        模板ID

        :param sql_template_id: The sql_template_id of this ShowDeadLockAnalysisResultRespSqlList.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowDeadLockAnalysisResultRespSqlList.

        节点ID

        :return: The node_id of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowDeadLockAnalysisResultRespSqlList.

        节点ID

        :param node_id: The node_id of this ShowDeadLockAnalysisResultRespSqlList.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def db_user(self):
        r"""Gets the db_user of this ShowDeadLockAnalysisResultRespSqlList.

        用户名

        :return: The db_user of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        r"""Sets the db_user of this ShowDeadLockAnalysisResultRespSqlList.

        用户名

        :param db_user: The db_user of this ShowDeadLockAnalysisResultRespSqlList.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def database(self):
        r"""Gets the database of this ShowDeadLockAnalysisResultRespSqlList.

        数据库

        :return: The database of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ShowDeadLockAnalysisResultRespSqlList.

        数据库

        :param database: The database of this ShowDeadLockAnalysisResultRespSqlList.
        :type database: str
        """
        self._database = database

    @property
    def client(self):
        r"""Gets the client of this ShowDeadLockAnalysisResultRespSqlList.

        客户端IP

        :return: The client of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        r"""Sets the client of this ShowDeadLockAnalysisResultRespSqlList.

        客户端IP

        :param client: The client of this ShowDeadLockAnalysisResultRespSqlList.
        :type client: str
        """
        self._client = client

    @property
    def sql_type(self):
        r"""Gets the sql_type of this ShowDeadLockAnalysisResultRespSqlList.

        SQL类型

        :return: The sql_type of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        r"""Sets the sql_type of this ShowDeadLockAnalysisResultRespSqlList.

        SQL类型

        :param sql_type: The sql_type of this ShowDeadLockAnalysisResultRespSqlList.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def status(self):
        r"""Gets the status of this ShowDeadLockAnalysisResultRespSqlList.

        执行状态

        :return: The status of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDeadLockAnalysisResultRespSqlList.

        执行状态

        :param status: The status of this ShowDeadLockAnalysisResultRespSqlList.
        :type status: int
        """
        self._status = status

    @property
    def error_no(self):
        r"""Gets the error_no of this ShowDeadLockAnalysisResultRespSqlList.

        错误码

        :return: The error_no of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._error_no

    @error_no.setter
    def error_no(self, error_no):
        r"""Sets the error_no of this ShowDeadLockAnalysisResultRespSqlList.

        错误码

        :param error_no: The error_no of this ShowDeadLockAnalysisResultRespSqlList.
        :type error_no: int
        """
        self._error_no = error_no

    @property
    def rows_affected(self):
        r"""Gets the rows_affected of this ShowDeadLockAnalysisResultRespSqlList.

        更新行数

        :return: The rows_affected of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._rows_affected

    @rows_affected.setter
    def rows_affected(self, rows_affected):
        r"""Sets the rows_affected of this ShowDeadLockAnalysisResultRespSqlList.

        更新行数

        :param rows_affected: The rows_affected of this ShowDeadLockAnalysisResultRespSqlList.
        :type rows_affected: int
        """
        self._rows_affected = rows_affected

    @property
    def rows_sent(self):
        r"""Gets the rows_sent of this ShowDeadLockAnalysisResultRespSqlList.

        返回行数

        :return: The rows_sent of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        r"""Sets the rows_sent of this ShowDeadLockAnalysisResultRespSqlList.

        返回行数

        :param rows_sent: The rows_sent of this ShowDeadLockAnalysisResultRespSqlList.
        :type rows_sent: int
        """
        self._rows_sent = rows_sent

    @property
    def lock_time(self):
        r"""Gets the lock_time of this ShowDeadLockAnalysisResultRespSqlList.

        锁等待时间毫秒

        :return: The lock_time of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this ShowDeadLockAnalysisResultRespSqlList.

        锁等待时间毫秒

        :param lock_time: The lock_time of this ShowDeadLockAnalysisResultRespSqlList.
        :type lock_time: int
        """
        self._lock_time = lock_time

    @property
    def rows_examined(self):
        r"""Gets the rows_examined of this ShowDeadLockAnalysisResultRespSqlList.

        扫描行数

        :return: The rows_examined of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        r"""Sets the rows_examined of this ShowDeadLockAnalysisResultRespSqlList.

        扫描行数

        :param rows_examined: The rows_examined of this ShowDeadLockAnalysisResultRespSqlList.
        :type rows_examined: int
        """
        self._rows_examined = rows_examined

    @property
    def session_id(self):
        r"""Gets the session_id of this ShowDeadLockAnalysisResultRespSqlList.

        线程ID

        :return: The session_id of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this ShowDeadLockAnalysisResultRespSqlList.

        线程ID

        :param session_id: The session_id of this ShowDeadLockAnalysisResultRespSqlList.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this ShowDeadLockAnalysisResultRespSqlList.

        CPU耗时(us)

        :return: The cpu_time of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this ShowDeadLockAnalysisResultRespSqlList.

        CPU耗时(us)

        :param cpu_time: The cpu_time of this ShowDeadLockAnalysisResultRespSqlList.
        :type cpu_time: int
        """
        self._cpu_time = cpu_time

    @property
    def send_bytes(self):
        r"""Gets the send_bytes of this ShowDeadLockAnalysisResultRespSqlList.

        网络发送字节数

        :return: The send_bytes of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._send_bytes

    @send_bytes.setter
    def send_bytes(self, send_bytes):
        r"""Sets the send_bytes of this ShowDeadLockAnalysisResultRespSqlList.

        网络发送字节数

        :param send_bytes: The send_bytes of this ShowDeadLockAnalysisResultRespSqlList.
        :type send_bytes: int
        """
        self._send_bytes = send_bytes

    @property
    def query_tables(self):
        r"""Gets the query_tables of this ShowDeadLockAnalysisResultRespSqlList.

        查询中所有的表名

        :return: The query_tables of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: str
        """
        return self._query_tables

    @query_tables.setter
    def query_tables(self, query_tables):
        r"""Sets the query_tables of this ShowDeadLockAnalysisResultRespSqlList.

        查询中所有的表名

        :param query_tables: The query_tables of this ShowDeadLockAnalysisResultRespSqlList.
        :type query_tables: str
        """
        self._query_tables = query_tables

    @property
    def innodb_io_read_bytes(self):
        r"""Gets the innodb_io_read_bytes of this ShowDeadLockAnalysisResultRespSqlList.

        物理I/O读字节数

        :return: The innodb_io_read_bytes of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._innodb_io_read_bytes

    @innodb_io_read_bytes.setter
    def innodb_io_read_bytes(self, innodb_io_read_bytes):
        r"""Sets the innodb_io_read_bytes of this ShowDeadLockAnalysisResultRespSqlList.

        物理I/O读字节数

        :param innodb_io_read_bytes: The innodb_io_read_bytes of this ShowDeadLockAnalysisResultRespSqlList.
        :type innodb_io_read_bytes: int
        """
        self._innodb_io_read_bytes = innodb_io_read_bytes

    @property
    def innodb_io_read(self):
        r"""Gets the innodb_io_read of this ShowDeadLockAnalysisResultRespSqlList.

        物理I/O读次数

        :return: The innodb_io_read of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._innodb_io_read

    @innodb_io_read.setter
    def innodb_io_read(self, innodb_io_read):
        r"""Sets the innodb_io_read of this ShowDeadLockAnalysisResultRespSqlList.

        物理I/O读次数

        :param innodb_io_read: The innodb_io_read of this ShowDeadLockAnalysisResultRespSqlList.
        :type innodb_io_read: int
        """
        self._innodb_io_read = innodb_io_read

    @property
    def innodb_io_read_wait(self):
        r"""Gets the innodb_io_read_wait of this ShowDeadLockAnalysisResultRespSqlList.

        物理I/O读取等待耗时(ms)

        :return: The innodb_io_read_wait of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._innodb_io_read_wait

    @innodb_io_read_wait.setter
    def innodb_io_read_wait(self, innodb_io_read_wait):
        r"""Sets the innodb_io_read_wait of this ShowDeadLockAnalysisResultRespSqlList.

        物理I/O读取等待耗时(ms)

        :param innodb_io_read_wait: The innodb_io_read_wait of this ShowDeadLockAnalysisResultRespSqlList.
        :type innodb_io_read_wait: int
        """
        self._innodb_io_read_wait = innodb_io_read_wait

    @property
    def innodb_lock_wait(self):
        r"""Gets the innodb_lock_wait of this ShowDeadLockAnalysisResultRespSqlList.

        物理I/O读取等待耗时(ms)

        :return: The innodb_lock_wait of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._innodb_lock_wait

    @innodb_lock_wait.setter
    def innodb_lock_wait(self, innodb_lock_wait):
        r"""Sets the innodb_lock_wait of this ShowDeadLockAnalysisResultRespSqlList.

        物理I/O读取等待耗时(ms)

        :param innodb_lock_wait: The innodb_lock_wait of this ShowDeadLockAnalysisResultRespSqlList.
        :type innodb_lock_wait: int
        """
        self._innodb_lock_wait = innodb_lock_wait

    @property
    def innodb_queue_wait(self):
        r"""Gets the innodb_queue_wait of this ShowDeadLockAnalysisResultRespSqlList.

        行锁等待耗时(ms)

        :return: The innodb_queue_wait of this ShowDeadLockAnalysisResultRespSqlList.
        :rtype: int
        """
        return self._innodb_queue_wait

    @innodb_queue_wait.setter
    def innodb_queue_wait(self, innodb_queue_wait):
        r"""Sets the innodb_queue_wait of this ShowDeadLockAnalysisResultRespSqlList.

        行锁等待耗时(ms)

        :param innodb_queue_wait: The innodb_queue_wait of this ShowDeadLockAnalysisResultRespSqlList.
        :type innodb_queue_wait: int
        """
        self._innodb_queue_wait = innodb_queue_wait

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
        if not isinstance(other, ShowDeadLockAnalysisResultRespSqlList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
