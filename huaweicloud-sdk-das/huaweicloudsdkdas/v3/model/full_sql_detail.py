# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullSqlDetail:

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
        'operate_type': 'str',
        'status': 'str',
        'error_no': 'str',
        'database': 'str',
        'thread_id': 'str',
        'client': 'str',
        'user': 'str',
        'execute_at': 'int',
        'query_time': 'float',
        'lock_time': 'float',
        'rows_examined': 'int',
        'rows_sent': 'int',
        'rows_affected': 'int',
        'trx_id': 'int',
        'cpu_time': 'float',
        'send_bytes': 'int',
        'query_tables': 'str',
        'innodb_io_read_bytes': 'int',
        'innodb_io_read': 'int',
        'innodb_io_read_wait': 'float',
        'innodb_lock_wait': 'float',
        'innodb_queue_wait': 'float',
        'kernel_version': 'str',
        'query_time_detail': 'str',
        'session_id': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'sql': 'sql',
        'sql_template_id': 'sql_template_id',
        'operate_type': 'operate_type',
        'status': 'status',
        'error_no': 'error_no',
        'database': 'database',
        'thread_id': 'thread_id',
        'client': 'client',
        'user': 'user',
        'execute_at': 'execute_at',
        'query_time': 'query_time',
        'lock_time': 'lock_time',
        'rows_examined': 'rows_examined',
        'rows_sent': 'rows_sent',
        'rows_affected': 'rows_affected',
        'trx_id': 'trx_id',
        'cpu_time': 'cpu_time',
        'send_bytes': 'send_bytes',
        'query_tables': 'query_tables',
        'innodb_io_read_bytes': 'innodb_io_read_bytes',
        'innodb_io_read': 'innodb_io_read',
        'innodb_io_read_wait': 'innodb_io_read_wait',
        'innodb_lock_wait': 'innodb_lock_wait',
        'innodb_queue_wait': 'innodb_queue_wait',
        'kernel_version': 'kernel_version',
        'query_time_detail': 'query_time_detail',
        'session_id': 'session_id',
        'node_id': 'node_id'
    }

    def __init__(self, sql=None, sql_template_id=None, operate_type=None, status=None, error_no=None, database=None, thread_id=None, client=None, user=None, execute_at=None, query_time=None, lock_time=None, rows_examined=None, rows_sent=None, rows_affected=None, trx_id=None, cpu_time=None, send_bytes=None, query_tables=None, innodb_io_read_bytes=None, innodb_io_read=None, innodb_io_read_wait=None, innodb_lock_wait=None, innodb_queue_wait=None, kernel_version=None, query_time_detail=None, session_id=None, node_id=None):
        r"""FullSqlDetail

        The model defined in huaweicloud sdk

        :param sql: SQL语句。
        :type sql: str
        :param sql_template_id: SQL模板ID。
        :type sql_template_id: str
        :param operate_type: 操作类型。
        :type operate_type: str
        :param status: 状态。
        :type status: str
        :param error_no: 错误码。
        :type error_no: str
        :param database: 数据库。
        :type database: str
        :param thread_id: 线程ID。
        :type thread_id: str
        :param client: 客户端。
        :type client: str
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
        :param trx_id: 事务ID。
        :type trx_id: int
        :param cpu_time: CPU耗时（微秒）。
        :type cpu_time: float
        :param send_bytes: 网络发送字节数。
        :type send_bytes: int
        :param query_tables: 查询中所有的表名（格式：库名.表名|库名.表名）。
        :type query_tables: str
        :param innodb_io_read_bytes: 物理I/O读字节数。
        :type innodb_io_read_bytes: int
        :param innodb_io_read: 物理I/O读次数。
        :type innodb_io_read: int
        :param innodb_io_read_wait: 物理I/O读取等待耗时（毫秒）。
        :type innodb_io_read_wait: float
        :param innodb_lock_wait: 行锁等待耗时（毫秒）。
        :type innodb_lock_wait: float
        :param innodb_queue_wait: 进入innodb的等待耗时（毫秒）。
        :type innodb_queue_wait: float
        :param kernel_version: 内核版本号，DDM实例使用。
        :type kernel_version: str
        :param query_time_detail: SQL执行各阶段细分耗时，DDM实例使用。
        :type query_time_detail: str
        :param session_id: 会话ID。
        :type session_id: str
        :param node_id: 节点ID。
        :type node_id: str
        """
        
        

        self._sql = None
        self._sql_template_id = None
        self._operate_type = None
        self._status = None
        self._error_no = None
        self._database = None
        self._thread_id = None
        self._client = None
        self._user = None
        self._execute_at = None
        self._query_time = None
        self._lock_time = None
        self._rows_examined = None
        self._rows_sent = None
        self._rows_affected = None
        self._trx_id = None
        self._cpu_time = None
        self._send_bytes = None
        self._query_tables = None
        self._innodb_io_read_bytes = None
        self._innodb_io_read = None
        self._innodb_io_read_wait = None
        self._innodb_lock_wait = None
        self._innodb_queue_wait = None
        self._kernel_version = None
        self._query_time_detail = None
        self._session_id = None
        self._node_id = None
        self.discriminator = None

        self.sql = sql
        self.sql_template_id = sql_template_id
        self.operate_type = operate_type
        self.status = status
        self.error_no = error_no
        self.database = database
        self.thread_id = thread_id
        self.client = client
        self.user = user
        self.execute_at = execute_at
        self.query_time = query_time
        self.lock_time = lock_time
        self.rows_examined = rows_examined
        self.rows_sent = rows_sent
        self.rows_affected = rows_affected
        self.trx_id = trx_id
        self.cpu_time = cpu_time
        self.send_bytes = send_bytes
        self.query_tables = query_tables
        self.innodb_io_read_bytes = innodb_io_read_bytes
        self.innodb_io_read = innodb_io_read
        self.innodb_io_read_wait = innodb_io_read_wait
        self.innodb_lock_wait = innodb_lock_wait
        self.innodb_queue_wait = innodb_queue_wait
        self.kernel_version = kernel_version
        self.query_time_detail = query_time_detail
        self.session_id = session_id
        self.node_id = node_id

    @property
    def sql(self):
        r"""Gets the sql of this FullSqlDetail.

        SQL语句。

        :return: The sql of this FullSqlDetail.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this FullSqlDetail.

        SQL语句。

        :param sql: The sql of this FullSqlDetail.
        :type sql: str
        """
        self._sql = sql

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this FullSqlDetail.

        SQL模板ID。

        :return: The sql_template_id of this FullSqlDetail.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this FullSqlDetail.

        SQL模板ID。

        :param sql_template_id: The sql_template_id of this FullSqlDetail.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def operate_type(self):
        r"""Gets the operate_type of this FullSqlDetail.

        操作类型。

        :return: The operate_type of this FullSqlDetail.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this FullSqlDetail.

        操作类型。

        :param operate_type: The operate_type of this FullSqlDetail.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def status(self):
        r"""Gets the status of this FullSqlDetail.

        状态。

        :return: The status of this FullSqlDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FullSqlDetail.

        状态。

        :param status: The status of this FullSqlDetail.
        :type status: str
        """
        self._status = status

    @property
    def error_no(self):
        r"""Gets the error_no of this FullSqlDetail.

        错误码。

        :return: The error_no of this FullSqlDetail.
        :rtype: str
        """
        return self._error_no

    @error_no.setter
    def error_no(self, error_no):
        r"""Sets the error_no of this FullSqlDetail.

        错误码。

        :param error_no: The error_no of this FullSqlDetail.
        :type error_no: str
        """
        self._error_no = error_no

    @property
    def database(self):
        r"""Gets the database of this FullSqlDetail.

        数据库。

        :return: The database of this FullSqlDetail.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this FullSqlDetail.

        数据库。

        :param database: The database of this FullSqlDetail.
        :type database: str
        """
        self._database = database

    @property
    def thread_id(self):
        r"""Gets the thread_id of this FullSqlDetail.

        线程ID。

        :return: The thread_id of this FullSqlDetail.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this FullSqlDetail.

        线程ID。

        :param thread_id: The thread_id of this FullSqlDetail.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def client(self):
        r"""Gets the client of this FullSqlDetail.

        客户端。

        :return: The client of this FullSqlDetail.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        r"""Sets the client of this FullSqlDetail.

        客户端。

        :param client: The client of this FullSqlDetail.
        :type client: str
        """
        self._client = client

    @property
    def user(self):
        r"""Gets the user of this FullSqlDetail.

        用户。

        :return: The user of this FullSqlDetail.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this FullSqlDetail.

        用户。

        :param user: The user of this FullSqlDetail.
        :type user: str
        """
        self._user = user

    @property
    def execute_at(self):
        r"""Gets the execute_at of this FullSqlDetail.

        执行开始时间（Unix timestamp），单位：毫秒。

        :return: The execute_at of this FullSqlDetail.
        :rtype: int
        """
        return self._execute_at

    @execute_at.setter
    def execute_at(self, execute_at):
        r"""Sets the execute_at of this FullSqlDetail.

        执行开始时间（Unix timestamp），单位：毫秒。

        :param execute_at: The execute_at of this FullSqlDetail.
        :type execute_at: int
        """
        self._execute_at = execute_at

    @property
    def query_time(self):
        r"""Gets the query_time of this FullSqlDetail.

        执行耗时（毫秒）。

        :return: The query_time of this FullSqlDetail.
        :rtype: float
        """
        return self._query_time

    @query_time.setter
    def query_time(self, query_time):
        r"""Sets the query_time of this FullSqlDetail.

        执行耗时（毫秒）。

        :param query_time: The query_time of this FullSqlDetail.
        :type query_time: float
        """
        self._query_time = query_time

    @property
    def lock_time(self):
        r"""Gets the lock_time of this FullSqlDetail.

        锁等待耗时（毫秒）。

        :return: The lock_time of this FullSqlDetail.
        :rtype: float
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this FullSqlDetail.

        锁等待耗时（毫秒）。

        :param lock_time: The lock_time of this FullSqlDetail.
        :type lock_time: float
        """
        self._lock_time = lock_time

    @property
    def rows_examined(self):
        r"""Gets the rows_examined of this FullSqlDetail.

        扫描行数。

        :return: The rows_examined of this FullSqlDetail.
        :rtype: int
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        r"""Sets the rows_examined of this FullSqlDetail.

        扫描行数。

        :param rows_examined: The rows_examined of this FullSqlDetail.
        :type rows_examined: int
        """
        self._rows_examined = rows_examined

    @property
    def rows_sent(self):
        r"""Gets the rows_sent of this FullSqlDetail.

        返回行数。

        :return: The rows_sent of this FullSqlDetail.
        :rtype: int
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        r"""Sets the rows_sent of this FullSqlDetail.

        返回行数。

        :param rows_sent: The rows_sent of this FullSqlDetail.
        :type rows_sent: int
        """
        self._rows_sent = rows_sent

    @property
    def rows_affected(self):
        r"""Gets the rows_affected of this FullSqlDetail.

        更新行数。

        :return: The rows_affected of this FullSqlDetail.
        :rtype: int
        """
        return self._rows_affected

    @rows_affected.setter
    def rows_affected(self, rows_affected):
        r"""Sets the rows_affected of this FullSqlDetail.

        更新行数。

        :param rows_affected: The rows_affected of this FullSqlDetail.
        :type rows_affected: int
        """
        self._rows_affected = rows_affected

    @property
    def trx_id(self):
        r"""Gets the trx_id of this FullSqlDetail.

        事务ID。

        :return: The trx_id of this FullSqlDetail.
        :rtype: int
        """
        return self._trx_id

    @trx_id.setter
    def trx_id(self, trx_id):
        r"""Sets the trx_id of this FullSqlDetail.

        事务ID。

        :param trx_id: The trx_id of this FullSqlDetail.
        :type trx_id: int
        """
        self._trx_id = trx_id

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this FullSqlDetail.

        CPU耗时（微秒）。

        :return: The cpu_time of this FullSqlDetail.
        :rtype: float
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this FullSqlDetail.

        CPU耗时（微秒）。

        :param cpu_time: The cpu_time of this FullSqlDetail.
        :type cpu_time: float
        """
        self._cpu_time = cpu_time

    @property
    def send_bytes(self):
        r"""Gets the send_bytes of this FullSqlDetail.

        网络发送字节数。

        :return: The send_bytes of this FullSqlDetail.
        :rtype: int
        """
        return self._send_bytes

    @send_bytes.setter
    def send_bytes(self, send_bytes):
        r"""Sets the send_bytes of this FullSqlDetail.

        网络发送字节数。

        :param send_bytes: The send_bytes of this FullSqlDetail.
        :type send_bytes: int
        """
        self._send_bytes = send_bytes

    @property
    def query_tables(self):
        r"""Gets the query_tables of this FullSqlDetail.

        查询中所有的表名（格式：库名.表名|库名.表名）。

        :return: The query_tables of this FullSqlDetail.
        :rtype: str
        """
        return self._query_tables

    @query_tables.setter
    def query_tables(self, query_tables):
        r"""Sets the query_tables of this FullSqlDetail.

        查询中所有的表名（格式：库名.表名|库名.表名）。

        :param query_tables: The query_tables of this FullSqlDetail.
        :type query_tables: str
        """
        self._query_tables = query_tables

    @property
    def innodb_io_read_bytes(self):
        r"""Gets the innodb_io_read_bytes of this FullSqlDetail.

        物理I/O读字节数。

        :return: The innodb_io_read_bytes of this FullSqlDetail.
        :rtype: int
        """
        return self._innodb_io_read_bytes

    @innodb_io_read_bytes.setter
    def innodb_io_read_bytes(self, innodb_io_read_bytes):
        r"""Sets the innodb_io_read_bytes of this FullSqlDetail.

        物理I/O读字节数。

        :param innodb_io_read_bytes: The innodb_io_read_bytes of this FullSqlDetail.
        :type innodb_io_read_bytes: int
        """
        self._innodb_io_read_bytes = innodb_io_read_bytes

    @property
    def innodb_io_read(self):
        r"""Gets the innodb_io_read of this FullSqlDetail.

        物理I/O读次数。

        :return: The innodb_io_read of this FullSqlDetail.
        :rtype: int
        """
        return self._innodb_io_read

    @innodb_io_read.setter
    def innodb_io_read(self, innodb_io_read):
        r"""Sets the innodb_io_read of this FullSqlDetail.

        物理I/O读次数。

        :param innodb_io_read: The innodb_io_read of this FullSqlDetail.
        :type innodb_io_read: int
        """
        self._innodb_io_read = innodb_io_read

    @property
    def innodb_io_read_wait(self):
        r"""Gets the innodb_io_read_wait of this FullSqlDetail.

        物理I/O读取等待耗时（毫秒）。

        :return: The innodb_io_read_wait of this FullSqlDetail.
        :rtype: float
        """
        return self._innodb_io_read_wait

    @innodb_io_read_wait.setter
    def innodb_io_read_wait(self, innodb_io_read_wait):
        r"""Sets the innodb_io_read_wait of this FullSqlDetail.

        物理I/O读取等待耗时（毫秒）。

        :param innodb_io_read_wait: The innodb_io_read_wait of this FullSqlDetail.
        :type innodb_io_read_wait: float
        """
        self._innodb_io_read_wait = innodb_io_read_wait

    @property
    def innodb_lock_wait(self):
        r"""Gets the innodb_lock_wait of this FullSqlDetail.

        行锁等待耗时（毫秒）。

        :return: The innodb_lock_wait of this FullSqlDetail.
        :rtype: float
        """
        return self._innodb_lock_wait

    @innodb_lock_wait.setter
    def innodb_lock_wait(self, innodb_lock_wait):
        r"""Sets the innodb_lock_wait of this FullSqlDetail.

        行锁等待耗时（毫秒）。

        :param innodb_lock_wait: The innodb_lock_wait of this FullSqlDetail.
        :type innodb_lock_wait: float
        """
        self._innodb_lock_wait = innodb_lock_wait

    @property
    def innodb_queue_wait(self):
        r"""Gets the innodb_queue_wait of this FullSqlDetail.

        进入innodb的等待耗时（毫秒）。

        :return: The innodb_queue_wait of this FullSqlDetail.
        :rtype: float
        """
        return self._innodb_queue_wait

    @innodb_queue_wait.setter
    def innodb_queue_wait(self, innodb_queue_wait):
        r"""Sets the innodb_queue_wait of this FullSqlDetail.

        进入innodb的等待耗时（毫秒）。

        :param innodb_queue_wait: The innodb_queue_wait of this FullSqlDetail.
        :type innodb_queue_wait: float
        """
        self._innodb_queue_wait = innodb_queue_wait

    @property
    def kernel_version(self):
        r"""Gets the kernel_version of this FullSqlDetail.

        内核版本号，DDM实例使用。

        :return: The kernel_version of this FullSqlDetail.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        r"""Sets the kernel_version of this FullSqlDetail.

        内核版本号，DDM实例使用。

        :param kernel_version: The kernel_version of this FullSqlDetail.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

    @property
    def query_time_detail(self):
        r"""Gets the query_time_detail of this FullSqlDetail.

        SQL执行各阶段细分耗时，DDM实例使用。

        :return: The query_time_detail of this FullSqlDetail.
        :rtype: str
        """
        return self._query_time_detail

    @query_time_detail.setter
    def query_time_detail(self, query_time_detail):
        r"""Sets the query_time_detail of this FullSqlDetail.

        SQL执行各阶段细分耗时，DDM实例使用。

        :param query_time_detail: The query_time_detail of this FullSqlDetail.
        :type query_time_detail: str
        """
        self._query_time_detail = query_time_detail

    @property
    def session_id(self):
        r"""Gets the session_id of this FullSqlDetail.

        会话ID。

        :return: The session_id of this FullSqlDetail.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this FullSqlDetail.

        会话ID。

        :param session_id: The session_id of this FullSqlDetail.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def node_id(self):
        r"""Gets the node_id of this FullSqlDetail.

        节点ID。

        :return: The node_id of this FullSqlDetail.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this FullSqlDetail.

        节点ID。

        :param node_id: The node_id of this FullSqlDetail.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, FullSqlDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
