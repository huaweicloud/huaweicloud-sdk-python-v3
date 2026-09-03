# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlItemDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'operate_type': 'str',
        'sql_template_id': 'str',
        'instance_id': 'str',
        'sql': 'str',
        'database': 'str',
        'thread_id': 'int',
        'username': 'str',
        'client_ip': 'str',
        'status': 'int',
        'execute_cost': 'float',
        'execute_at': 'float',
        'rows_affected': 'int',
        'rows_examined': 'int',
        'lock_wait_time': 'float',
        'rows_returned': 'int',
        'trx_id': 'int',
        'cpu_time': 'int',
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
        'error_no': 'int',
        'node_id': 'str',
        'logical_reads': 'int',
        'physical_reads': 'int',
        'writes': 'int',
        'app_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'operate_type': 'operate_type',
        'sql_template_id': 'sql_template_id',
        'instance_id': 'instance_id',
        'sql': 'sql',
        'database': 'database',
        'thread_id': 'thread_id',
        'username': 'username',
        'client_ip': 'client_ip',
        'status': 'status',
        'execute_cost': 'execute_cost',
        'execute_at': 'execute_at',
        'rows_affected': 'rows_affected',
        'rows_examined': 'rows_examined',
        'lock_wait_time': 'lock_wait_time',
        'rows_returned': 'rows_returned',
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
        'error_no': 'error_no',
        'node_id': 'node_id',
        'logical_reads': 'logical_reads',
        'physical_reads': 'physical_reads',
        'writes': 'writes',
        'app_name': 'app_name'
    }

    def __init__(self, id=None, operate_type=None, sql_template_id=None, instance_id=None, sql=None, database=None, thread_id=None, username=None, client_ip=None, status=None, execute_cost=None, execute_at=None, rows_affected=None, rows_examined=None, lock_wait_time=None, rows_returned=None, trx_id=None, cpu_time=None, send_bytes=None, query_tables=None, innodb_io_read_bytes=None, innodb_io_read=None, innodb_io_read_wait=None, innodb_lock_wait=None, innodb_queue_wait=None, kernel_version=None, query_time_detail=None, session_id=None, error_no=None, node_id=None, logical_reads=None, physical_reads=None, writes=None, app_name=None):
        r"""SqlItemDto

        The model defined in huaweicloud sdk

        :param id: SQL的ID值
        :type id: str
        :param operate_type: 操作类型
        :type operate_type: str
        :param sql_template_id: 模板ID
        :type sql_template_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param sql: SQL文本
        :type sql: str
        :param database: 数据库名称
        :type database: str
        :param thread_id: 线程ID
        :type thread_id: int
        :param username: 用户名称
        :type username: str
        :param client_ip: 客户端IP
        :type client_ip: str
        :param status: 执行状态
        :type status: int
        :param execute_cost: 执行耗时(ms)
        :type execute_cost: float
        :param execute_at: 执行时间点(ms)
        :type execute_at: float
        :param rows_affected: 更新行数
        :type rows_affected: int
        :param rows_examined: 扫描行数
        :type rows_examined: int
        :param lock_wait_time: 锁等待时间
        :type lock_wait_time: float
        :param rows_returned: 返回行数
        :type rows_returned: int
        :param trx_id: 事务ID
        :type trx_id: int
        :param cpu_time: CPU耗时
        :type cpu_time: int
        :param send_bytes: 网络发送字节数
        :type send_bytes: int
        :param query_tables: 查询中所有的表名（格式：库名.表名|库名.表名）
        :type query_tables: str
        :param innodb_io_read_bytes: 物理IO读字节数
        :type innodb_io_read_bytes: int
        :param innodb_io_read: 物理IO读次数
        :type innodb_io_read: int
        :param innodb_io_read_wait: 物理IO读取等待耗时（ms）
        :type innodb_io_read_wait: float
        :param innodb_lock_wait: 行锁等待耗时（ms）
        :type innodb_lock_wait: float
        :param innodb_queue_wait: 进入innodb的等待耗时（ms）
        :type innodb_queue_wait: float
        :param kernel_version: 内核版本号
        :type kernel_version: str
        :param query_time_detail: SQL执行各阶段细分耗时
        :type query_time_detail: str
        :param session_id: 会话ID
        :type session_id: str
        :param error_no: 错误码
        :type error_no: int
        :param node_id: 节点ID，实例节点的唯一标识
        :type node_id: str
        :param logical_reads: sqlserver IO逻辑读
        :type logical_reads: int
        :param physical_reads: sqlserver IO物理读
        :type physical_reads: int
        :param writes: sqlserver IO写
        :type writes: int
        :param app_name: sqlserver 应用名
        :type app_name: str
        """
        
        

        self._id = None
        self._operate_type = None
        self._sql_template_id = None
        self._instance_id = None
        self._sql = None
        self._database = None
        self._thread_id = None
        self._username = None
        self._client_ip = None
        self._status = None
        self._execute_cost = None
        self._execute_at = None
        self._rows_affected = None
        self._rows_examined = None
        self._lock_wait_time = None
        self._rows_returned = None
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
        self._error_no = None
        self._node_id = None
        self._logical_reads = None
        self._physical_reads = None
        self._writes = None
        self._app_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if operate_type is not None:
            self.operate_type = operate_type
        if sql_template_id is not None:
            self.sql_template_id = sql_template_id
        if instance_id is not None:
            self.instance_id = instance_id
        if sql is not None:
            self.sql = sql
        if database is not None:
            self.database = database
        if thread_id is not None:
            self.thread_id = thread_id
        if username is not None:
            self.username = username
        if client_ip is not None:
            self.client_ip = client_ip
        if status is not None:
            self.status = status
        if execute_cost is not None:
            self.execute_cost = execute_cost
        if execute_at is not None:
            self.execute_at = execute_at
        if rows_affected is not None:
            self.rows_affected = rows_affected
        if rows_examined is not None:
            self.rows_examined = rows_examined
        if lock_wait_time is not None:
            self.lock_wait_time = lock_wait_time
        if rows_returned is not None:
            self.rows_returned = rows_returned
        if trx_id is not None:
            self.trx_id = trx_id
        if cpu_time is not None:
            self.cpu_time = cpu_time
        if send_bytes is not None:
            self.send_bytes = send_bytes
        if query_tables is not None:
            self.query_tables = query_tables
        if innodb_io_read_bytes is not None:
            self.innodb_io_read_bytes = innodb_io_read_bytes
        if innodb_io_read is not None:
            self.innodb_io_read = innodb_io_read
        if innodb_io_read_wait is not None:
            self.innodb_io_read_wait = innodb_io_read_wait
        if innodb_lock_wait is not None:
            self.innodb_lock_wait = innodb_lock_wait
        if innodb_queue_wait is not None:
            self.innodb_queue_wait = innodb_queue_wait
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if query_time_detail is not None:
            self.query_time_detail = query_time_detail
        if session_id is not None:
            self.session_id = session_id
        if error_no is not None:
            self.error_no = error_no
        if node_id is not None:
            self.node_id = node_id
        if logical_reads is not None:
            self.logical_reads = logical_reads
        if physical_reads is not None:
            self.physical_reads = physical_reads
        if writes is not None:
            self.writes = writes
        if app_name is not None:
            self.app_name = app_name

    @property
    def id(self):
        r"""Gets the id of this SqlItemDto.

        SQL的ID值

        :return: The id of this SqlItemDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SqlItemDto.

        SQL的ID值

        :param id: The id of this SqlItemDto.
        :type id: str
        """
        self._id = id

    @property
    def operate_type(self):
        r"""Gets the operate_type of this SqlItemDto.

        操作类型

        :return: The operate_type of this SqlItemDto.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this SqlItemDto.

        操作类型

        :param operate_type: The operate_type of this SqlItemDto.
        :type operate_type: str
        """
        self._operate_type = operate_type

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this SqlItemDto.

        模板ID

        :return: The sql_template_id of this SqlItemDto.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this SqlItemDto.

        模板ID

        :param sql_template_id: The sql_template_id of this SqlItemDto.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SqlItemDto.

        实例ID

        :return: The instance_id of this SqlItemDto.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SqlItemDto.

        实例ID

        :param instance_id: The instance_id of this SqlItemDto.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def sql(self):
        r"""Gets the sql of this SqlItemDto.

        SQL文本

        :return: The sql of this SqlItemDto.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this SqlItemDto.

        SQL文本

        :param sql: The sql of this SqlItemDto.
        :type sql: str
        """
        self._sql = sql

    @property
    def database(self):
        r"""Gets the database of this SqlItemDto.

        数据库名称

        :return: The database of this SqlItemDto.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this SqlItemDto.

        数据库名称

        :param database: The database of this SqlItemDto.
        :type database: str
        """
        self._database = database

    @property
    def thread_id(self):
        r"""Gets the thread_id of this SqlItemDto.

        线程ID

        :return: The thread_id of this SqlItemDto.
        :rtype: int
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this SqlItemDto.

        线程ID

        :param thread_id: The thread_id of this SqlItemDto.
        :type thread_id: int
        """
        self._thread_id = thread_id

    @property
    def username(self):
        r"""Gets the username of this SqlItemDto.

        用户名称

        :return: The username of this SqlItemDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this SqlItemDto.

        用户名称

        :param username: The username of this SqlItemDto.
        :type username: str
        """
        self._username = username

    @property
    def client_ip(self):
        r"""Gets the client_ip of this SqlItemDto.

        客户端IP

        :return: The client_ip of this SqlItemDto.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this SqlItemDto.

        客户端IP

        :param client_ip: The client_ip of this SqlItemDto.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def status(self):
        r"""Gets the status of this SqlItemDto.

        执行状态

        :return: The status of this SqlItemDto.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SqlItemDto.

        执行状态

        :param status: The status of this SqlItemDto.
        :type status: int
        """
        self._status = status

    @property
    def execute_cost(self):
        r"""Gets the execute_cost of this SqlItemDto.

        执行耗时(ms)

        :return: The execute_cost of this SqlItemDto.
        :rtype: float
        """
        return self._execute_cost

    @execute_cost.setter
    def execute_cost(self, execute_cost):
        r"""Sets the execute_cost of this SqlItemDto.

        执行耗时(ms)

        :param execute_cost: The execute_cost of this SqlItemDto.
        :type execute_cost: float
        """
        self._execute_cost = execute_cost

    @property
    def execute_at(self):
        r"""Gets the execute_at of this SqlItemDto.

        执行时间点(ms)

        :return: The execute_at of this SqlItemDto.
        :rtype: float
        """
        return self._execute_at

    @execute_at.setter
    def execute_at(self, execute_at):
        r"""Sets the execute_at of this SqlItemDto.

        执行时间点(ms)

        :param execute_at: The execute_at of this SqlItemDto.
        :type execute_at: float
        """
        self._execute_at = execute_at

    @property
    def rows_affected(self):
        r"""Gets the rows_affected of this SqlItemDto.

        更新行数

        :return: The rows_affected of this SqlItemDto.
        :rtype: int
        """
        return self._rows_affected

    @rows_affected.setter
    def rows_affected(self, rows_affected):
        r"""Sets the rows_affected of this SqlItemDto.

        更新行数

        :param rows_affected: The rows_affected of this SqlItemDto.
        :type rows_affected: int
        """
        self._rows_affected = rows_affected

    @property
    def rows_examined(self):
        r"""Gets the rows_examined of this SqlItemDto.

        扫描行数

        :return: The rows_examined of this SqlItemDto.
        :rtype: int
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        r"""Sets the rows_examined of this SqlItemDto.

        扫描行数

        :param rows_examined: The rows_examined of this SqlItemDto.
        :type rows_examined: int
        """
        self._rows_examined = rows_examined

    @property
    def lock_wait_time(self):
        r"""Gets the lock_wait_time of this SqlItemDto.

        锁等待时间

        :return: The lock_wait_time of this SqlItemDto.
        :rtype: float
        """
        return self._lock_wait_time

    @lock_wait_time.setter
    def lock_wait_time(self, lock_wait_time):
        r"""Sets the lock_wait_time of this SqlItemDto.

        锁等待时间

        :param lock_wait_time: The lock_wait_time of this SqlItemDto.
        :type lock_wait_time: float
        """
        self._lock_wait_time = lock_wait_time

    @property
    def rows_returned(self):
        r"""Gets the rows_returned of this SqlItemDto.

        返回行数

        :return: The rows_returned of this SqlItemDto.
        :rtype: int
        """
        return self._rows_returned

    @rows_returned.setter
    def rows_returned(self, rows_returned):
        r"""Sets the rows_returned of this SqlItemDto.

        返回行数

        :param rows_returned: The rows_returned of this SqlItemDto.
        :type rows_returned: int
        """
        self._rows_returned = rows_returned

    @property
    def trx_id(self):
        r"""Gets the trx_id of this SqlItemDto.

        事务ID

        :return: The trx_id of this SqlItemDto.
        :rtype: int
        """
        return self._trx_id

    @trx_id.setter
    def trx_id(self, trx_id):
        r"""Sets the trx_id of this SqlItemDto.

        事务ID

        :param trx_id: The trx_id of this SqlItemDto.
        :type trx_id: int
        """
        self._trx_id = trx_id

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this SqlItemDto.

        CPU耗时

        :return: The cpu_time of this SqlItemDto.
        :rtype: int
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this SqlItemDto.

        CPU耗时

        :param cpu_time: The cpu_time of this SqlItemDto.
        :type cpu_time: int
        """
        self._cpu_time = cpu_time

    @property
    def send_bytes(self):
        r"""Gets the send_bytes of this SqlItemDto.

        网络发送字节数

        :return: The send_bytes of this SqlItemDto.
        :rtype: int
        """
        return self._send_bytes

    @send_bytes.setter
    def send_bytes(self, send_bytes):
        r"""Sets the send_bytes of this SqlItemDto.

        网络发送字节数

        :param send_bytes: The send_bytes of this SqlItemDto.
        :type send_bytes: int
        """
        self._send_bytes = send_bytes

    @property
    def query_tables(self):
        r"""Gets the query_tables of this SqlItemDto.

        查询中所有的表名（格式：库名.表名|库名.表名）

        :return: The query_tables of this SqlItemDto.
        :rtype: str
        """
        return self._query_tables

    @query_tables.setter
    def query_tables(self, query_tables):
        r"""Sets the query_tables of this SqlItemDto.

        查询中所有的表名（格式：库名.表名|库名.表名）

        :param query_tables: The query_tables of this SqlItemDto.
        :type query_tables: str
        """
        self._query_tables = query_tables

    @property
    def innodb_io_read_bytes(self):
        r"""Gets the innodb_io_read_bytes of this SqlItemDto.

        物理IO读字节数

        :return: The innodb_io_read_bytes of this SqlItemDto.
        :rtype: int
        """
        return self._innodb_io_read_bytes

    @innodb_io_read_bytes.setter
    def innodb_io_read_bytes(self, innodb_io_read_bytes):
        r"""Sets the innodb_io_read_bytes of this SqlItemDto.

        物理IO读字节数

        :param innodb_io_read_bytes: The innodb_io_read_bytes of this SqlItemDto.
        :type innodb_io_read_bytes: int
        """
        self._innodb_io_read_bytes = innodb_io_read_bytes

    @property
    def innodb_io_read(self):
        r"""Gets the innodb_io_read of this SqlItemDto.

        物理IO读次数

        :return: The innodb_io_read of this SqlItemDto.
        :rtype: int
        """
        return self._innodb_io_read

    @innodb_io_read.setter
    def innodb_io_read(self, innodb_io_read):
        r"""Sets the innodb_io_read of this SqlItemDto.

        物理IO读次数

        :param innodb_io_read: The innodb_io_read of this SqlItemDto.
        :type innodb_io_read: int
        """
        self._innodb_io_read = innodb_io_read

    @property
    def innodb_io_read_wait(self):
        r"""Gets the innodb_io_read_wait of this SqlItemDto.

        物理IO读取等待耗时（ms）

        :return: The innodb_io_read_wait of this SqlItemDto.
        :rtype: float
        """
        return self._innodb_io_read_wait

    @innodb_io_read_wait.setter
    def innodb_io_read_wait(self, innodb_io_read_wait):
        r"""Sets the innodb_io_read_wait of this SqlItemDto.

        物理IO读取等待耗时（ms）

        :param innodb_io_read_wait: The innodb_io_read_wait of this SqlItemDto.
        :type innodb_io_read_wait: float
        """
        self._innodb_io_read_wait = innodb_io_read_wait

    @property
    def innodb_lock_wait(self):
        r"""Gets the innodb_lock_wait of this SqlItemDto.

        行锁等待耗时（ms）

        :return: The innodb_lock_wait of this SqlItemDto.
        :rtype: float
        """
        return self._innodb_lock_wait

    @innodb_lock_wait.setter
    def innodb_lock_wait(self, innodb_lock_wait):
        r"""Sets the innodb_lock_wait of this SqlItemDto.

        行锁等待耗时（ms）

        :param innodb_lock_wait: The innodb_lock_wait of this SqlItemDto.
        :type innodb_lock_wait: float
        """
        self._innodb_lock_wait = innodb_lock_wait

    @property
    def innodb_queue_wait(self):
        r"""Gets the innodb_queue_wait of this SqlItemDto.

        进入innodb的等待耗时（ms）

        :return: The innodb_queue_wait of this SqlItemDto.
        :rtype: float
        """
        return self._innodb_queue_wait

    @innodb_queue_wait.setter
    def innodb_queue_wait(self, innodb_queue_wait):
        r"""Sets the innodb_queue_wait of this SqlItemDto.

        进入innodb的等待耗时（ms）

        :param innodb_queue_wait: The innodb_queue_wait of this SqlItemDto.
        :type innodb_queue_wait: float
        """
        self._innodb_queue_wait = innodb_queue_wait

    @property
    def kernel_version(self):
        r"""Gets the kernel_version of this SqlItemDto.

        内核版本号

        :return: The kernel_version of this SqlItemDto.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        r"""Sets the kernel_version of this SqlItemDto.

        内核版本号

        :param kernel_version: The kernel_version of this SqlItemDto.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

    @property
    def query_time_detail(self):
        r"""Gets the query_time_detail of this SqlItemDto.

        SQL执行各阶段细分耗时

        :return: The query_time_detail of this SqlItemDto.
        :rtype: str
        """
        return self._query_time_detail

    @query_time_detail.setter
    def query_time_detail(self, query_time_detail):
        r"""Sets the query_time_detail of this SqlItemDto.

        SQL执行各阶段细分耗时

        :param query_time_detail: The query_time_detail of this SqlItemDto.
        :type query_time_detail: str
        """
        self._query_time_detail = query_time_detail

    @property
    def session_id(self):
        r"""Gets the session_id of this SqlItemDto.

        会话ID

        :return: The session_id of this SqlItemDto.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this SqlItemDto.

        会话ID

        :param session_id: The session_id of this SqlItemDto.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def error_no(self):
        r"""Gets the error_no of this SqlItemDto.

        错误码

        :return: The error_no of this SqlItemDto.
        :rtype: int
        """
        return self._error_no

    @error_no.setter
    def error_no(self, error_no):
        r"""Sets the error_no of this SqlItemDto.

        错误码

        :param error_no: The error_no of this SqlItemDto.
        :type error_no: int
        """
        self._error_no = error_no

    @property
    def node_id(self):
        r"""Gets the node_id of this SqlItemDto.

        节点ID，实例节点的唯一标识

        :return: The node_id of this SqlItemDto.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SqlItemDto.

        节点ID，实例节点的唯一标识

        :param node_id: The node_id of this SqlItemDto.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def logical_reads(self):
        r"""Gets the logical_reads of this SqlItemDto.

        sqlserver IO逻辑读

        :return: The logical_reads of this SqlItemDto.
        :rtype: int
        """
        return self._logical_reads

    @logical_reads.setter
    def logical_reads(self, logical_reads):
        r"""Sets the logical_reads of this SqlItemDto.

        sqlserver IO逻辑读

        :param logical_reads: The logical_reads of this SqlItemDto.
        :type logical_reads: int
        """
        self._logical_reads = logical_reads

    @property
    def physical_reads(self):
        r"""Gets the physical_reads of this SqlItemDto.

        sqlserver IO物理读

        :return: The physical_reads of this SqlItemDto.
        :rtype: int
        """
        return self._physical_reads

    @physical_reads.setter
    def physical_reads(self, physical_reads):
        r"""Sets the physical_reads of this SqlItemDto.

        sqlserver IO物理读

        :param physical_reads: The physical_reads of this SqlItemDto.
        :type physical_reads: int
        """
        self._physical_reads = physical_reads

    @property
    def writes(self):
        r"""Gets the writes of this SqlItemDto.

        sqlserver IO写

        :return: The writes of this SqlItemDto.
        :rtype: int
        """
        return self._writes

    @writes.setter
    def writes(self, writes):
        r"""Sets the writes of this SqlItemDto.

        sqlserver IO写

        :param writes: The writes of this SqlItemDto.
        :type writes: int
        """
        self._writes = writes

    @property
    def app_name(self):
        r"""Gets the app_name of this SqlItemDto.

        sqlserver 应用名

        :return: The app_name of this SqlItemDto.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this SqlItemDto.

        sqlserver 应用名

        :param app_name: The app_name of this SqlItemDto.
        :type app_name: str
        """
        self._app_name = app_name

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
        if not isinstance(other, SqlItemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
