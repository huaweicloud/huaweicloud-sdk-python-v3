# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Session:

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
        'blocked_process_id': 'str',
        'database_oid': 'int',
        'database_name': 'str',
        'session_id': 'int',
        'parallel_leader_id': 'int',
        'backend_user_oid': 'int',
        'user_name': 'str',
        'app_name': 'str',
        'client_ip_address': 'str',
        'client_host_name': 'str',
        'client_port': 'int',
        'session_start_time': 'str',
        'transaction_start_time': 'str',
        'transaction_execution_time': 'int',
        'query_start_time': 'str',
        'state_change_time': 'str',
        'wait_event_type': 'str',
        'wait_event_name': 'str',
        'session_status': 'str',
        'backend_xid': 'int',
        'backend_xmin': 'int',
        'query_id': 'str',
        'sql_statement': 'str',
        'process_type': 'str',
        'memory_usage': 'float',
        'process_status': 'str',
        'cpu_usage': 'float',
        'io_wait_status': 'float',
        'disk_read_rate': 'float',
        'disk_write_rate': 'float'
    }

    attribute_map = {
        'sample_time': 'sample_time',
        'blocked_process_id': 'blocked_process_id',
        'database_oid': 'database_oid',
        'database_name': 'database_name',
        'session_id': 'session_id',
        'parallel_leader_id': 'parallel_leader_id',
        'backend_user_oid': 'backend_user_oid',
        'user_name': 'user_name',
        'app_name': 'app_name',
        'client_ip_address': 'client_ip_address',
        'client_host_name': 'client_host_name',
        'client_port': 'client_port',
        'session_start_time': 'session_start_time',
        'transaction_start_time': 'transaction_start_time',
        'transaction_execution_time': 'transaction_execution_time',
        'query_start_time': 'query_start_time',
        'state_change_time': 'state_change_time',
        'wait_event_type': 'wait_event_type',
        'wait_event_name': 'wait_event_name',
        'session_status': 'session_status',
        'backend_xid': 'backend_xid',
        'backend_xmin': 'backend_xmin',
        'query_id': 'query_id',
        'sql_statement': 'sql_statement',
        'process_type': 'process_type',
        'memory_usage': 'memory_usage',
        'process_status': 'process_status',
        'cpu_usage': 'cpu_usage',
        'io_wait_status': 'io_wait_status',
        'disk_read_rate': 'disk_read_rate',
        'disk_write_rate': 'disk_write_rate'
    }

    def __init__(self, sample_time=None, blocked_process_id=None, database_oid=None, database_name=None, session_id=None, parallel_leader_id=None, backend_user_oid=None, user_name=None, app_name=None, client_ip_address=None, client_host_name=None, client_port=None, session_start_time=None, transaction_start_time=None, transaction_execution_time=None, query_start_time=None, state_change_time=None, wait_event_type=None, wait_event_name=None, session_status=None, backend_xid=None, backend_xmin=None, query_id=None, sql_statement=None, process_type=None, memory_usage=None, process_status=None, cpu_usage=None, io_wait_status=None, disk_read_rate=None, disk_write_rate=None):
        r"""Session

        The model defined in huaweicloud sdk

        :param sample_time: 采样时间
        :type sample_time: str
        :param blocked_process_id: 阻塞进程ID
        :type blocked_process_id: str
        :param database_oid: 数据库OID
        :type database_oid: int
        :param database_name: 数据库名
        :type database_name: str
        :param session_id: 会话ID
        :type session_id: int
        :param parallel_leader_id: 并行会话ID
        :type parallel_leader_id: int
        :param backend_user_oid: 后端用户OID
        :type backend_user_oid: int
        :param user_name: 用户名
        :type user_name: str
        :param app_name: 应用名
        :type app_name: str
        :param client_ip_address: 客户端地址
        :type client_ip_address: str
        :param client_host_name: 客户端名称
        :type client_host_name: str
        :param client_port: 客户端端口
        :type client_port: int
        :param session_start_time: 会话建立时间
        :type session_start_time: str
        :param transaction_start_time: 事务启动时间
        :type transaction_start_time: str
        :param transaction_execution_time: 事务执行时间(s)
        :type transaction_execution_time: int
        :param query_start_time: 查询开始时间
        :type query_start_time: str
        :param state_change_time: state改变时间
        :type state_change_time: str
        :param wait_event_type: 等待事件类型
        :type wait_event_type: str
        :param wait_event_name: 等待事件名称
        :type wait_event_name: str
        :param session_status: 会话状态
        :type session_status: str
        :param backend_xid: Backend XID
        :type backend_xid: int
        :param backend_xmin: Backend Xmin
        :type backend_xmin: int
        :param query_id: Query ID
        :type query_id: str
        :param sql_statement: SQL语句
        :type sql_statement: str
        :param process_type: 进程类型
        :type process_type: str
        :param memory_usage: 内存占比(%)
        :type memory_usage: float
        :param process_status: 进程状态
        :type process_status: str
        :param cpu_usage: 3秒内平均CPU占用率(%)
        :type cpu_usage: float
        :param io_wait_status: I/O等待时间(s)
        :type io_wait_status: float
        :param disk_read_rate: 磁盘读速率(MB/s)
        :type disk_read_rate: float
        :param disk_write_rate: 磁盘写速率(MB/s)
        :type disk_write_rate: float
        """
        
        

        self._sample_time = None
        self._blocked_process_id = None
        self._database_oid = None
        self._database_name = None
        self._session_id = None
        self._parallel_leader_id = None
        self._backend_user_oid = None
        self._user_name = None
        self._app_name = None
        self._client_ip_address = None
        self._client_host_name = None
        self._client_port = None
        self._session_start_time = None
        self._transaction_start_time = None
        self._transaction_execution_time = None
        self._query_start_time = None
        self._state_change_time = None
        self._wait_event_type = None
        self._wait_event_name = None
        self._session_status = None
        self._backend_xid = None
        self._backend_xmin = None
        self._query_id = None
        self._sql_statement = None
        self._process_type = None
        self._memory_usage = None
        self._process_status = None
        self._cpu_usage = None
        self._io_wait_status = None
        self._disk_read_rate = None
        self._disk_write_rate = None
        self.discriminator = None

        if sample_time is not None:
            self.sample_time = sample_time
        if blocked_process_id is not None:
            self.blocked_process_id = blocked_process_id
        if database_oid is not None:
            self.database_oid = database_oid
        if database_name is not None:
            self.database_name = database_name
        if session_id is not None:
            self.session_id = session_id
        if parallel_leader_id is not None:
            self.parallel_leader_id = parallel_leader_id
        if backend_user_oid is not None:
            self.backend_user_oid = backend_user_oid
        if user_name is not None:
            self.user_name = user_name
        if app_name is not None:
            self.app_name = app_name
        if client_ip_address is not None:
            self.client_ip_address = client_ip_address
        if client_host_name is not None:
            self.client_host_name = client_host_name
        if client_port is not None:
            self.client_port = client_port
        if session_start_time is not None:
            self.session_start_time = session_start_time
        if transaction_start_time is not None:
            self.transaction_start_time = transaction_start_time
        if transaction_execution_time is not None:
            self.transaction_execution_time = transaction_execution_time
        if query_start_time is not None:
            self.query_start_time = query_start_time
        if state_change_time is not None:
            self.state_change_time = state_change_time
        if wait_event_type is not None:
            self.wait_event_type = wait_event_type
        if wait_event_name is not None:
            self.wait_event_name = wait_event_name
        if session_status is not None:
            self.session_status = session_status
        if backend_xid is not None:
            self.backend_xid = backend_xid
        if backend_xmin is not None:
            self.backend_xmin = backend_xmin
        if query_id is not None:
            self.query_id = query_id
        if sql_statement is not None:
            self.sql_statement = sql_statement
        if process_type is not None:
            self.process_type = process_type
        if memory_usage is not None:
            self.memory_usage = memory_usage
        if process_status is not None:
            self.process_status = process_status
        if cpu_usage is not None:
            self.cpu_usage = cpu_usage
        if io_wait_status is not None:
            self.io_wait_status = io_wait_status
        if disk_read_rate is not None:
            self.disk_read_rate = disk_read_rate
        if disk_write_rate is not None:
            self.disk_write_rate = disk_write_rate

    @property
    def sample_time(self):
        r"""Gets the sample_time of this Session.

        采样时间

        :return: The sample_time of this Session.
        :rtype: str
        """
        return self._sample_time

    @sample_time.setter
    def sample_time(self, sample_time):
        r"""Sets the sample_time of this Session.

        采样时间

        :param sample_time: The sample_time of this Session.
        :type sample_time: str
        """
        self._sample_time = sample_time

    @property
    def blocked_process_id(self):
        r"""Gets the blocked_process_id of this Session.

        阻塞进程ID

        :return: The blocked_process_id of this Session.
        :rtype: str
        """
        return self._blocked_process_id

    @blocked_process_id.setter
    def blocked_process_id(self, blocked_process_id):
        r"""Sets the blocked_process_id of this Session.

        阻塞进程ID

        :param blocked_process_id: The blocked_process_id of this Session.
        :type blocked_process_id: str
        """
        self._blocked_process_id = blocked_process_id

    @property
    def database_oid(self):
        r"""Gets the database_oid of this Session.

        数据库OID

        :return: The database_oid of this Session.
        :rtype: int
        """
        return self._database_oid

    @database_oid.setter
    def database_oid(self, database_oid):
        r"""Sets the database_oid of this Session.

        数据库OID

        :param database_oid: The database_oid of this Session.
        :type database_oid: int
        """
        self._database_oid = database_oid

    @property
    def database_name(self):
        r"""Gets the database_name of this Session.

        数据库名

        :return: The database_name of this Session.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this Session.

        数据库名

        :param database_name: The database_name of this Session.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def session_id(self):
        r"""Gets the session_id of this Session.

        会话ID

        :return: The session_id of this Session.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this Session.

        会话ID

        :param session_id: The session_id of this Session.
        :type session_id: int
        """
        self._session_id = session_id

    @property
    def parallel_leader_id(self):
        r"""Gets the parallel_leader_id of this Session.

        并行会话ID

        :return: The parallel_leader_id of this Session.
        :rtype: int
        """
        return self._parallel_leader_id

    @parallel_leader_id.setter
    def parallel_leader_id(self, parallel_leader_id):
        r"""Sets the parallel_leader_id of this Session.

        并行会话ID

        :param parallel_leader_id: The parallel_leader_id of this Session.
        :type parallel_leader_id: int
        """
        self._parallel_leader_id = parallel_leader_id

    @property
    def backend_user_oid(self):
        r"""Gets the backend_user_oid of this Session.

        后端用户OID

        :return: The backend_user_oid of this Session.
        :rtype: int
        """
        return self._backend_user_oid

    @backend_user_oid.setter
    def backend_user_oid(self, backend_user_oid):
        r"""Sets the backend_user_oid of this Session.

        后端用户OID

        :param backend_user_oid: The backend_user_oid of this Session.
        :type backend_user_oid: int
        """
        self._backend_user_oid = backend_user_oid

    @property
    def user_name(self):
        r"""Gets the user_name of this Session.

        用户名

        :return: The user_name of this Session.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this Session.

        用户名

        :param user_name: The user_name of this Session.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def app_name(self):
        r"""Gets the app_name of this Session.

        应用名

        :return: The app_name of this Session.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this Session.

        应用名

        :param app_name: The app_name of this Session.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def client_ip_address(self):
        r"""Gets the client_ip_address of this Session.

        客户端地址

        :return: The client_ip_address of this Session.
        :rtype: str
        """
        return self._client_ip_address

    @client_ip_address.setter
    def client_ip_address(self, client_ip_address):
        r"""Sets the client_ip_address of this Session.

        客户端地址

        :param client_ip_address: The client_ip_address of this Session.
        :type client_ip_address: str
        """
        self._client_ip_address = client_ip_address

    @property
    def client_host_name(self):
        r"""Gets the client_host_name of this Session.

        客户端名称

        :return: The client_host_name of this Session.
        :rtype: str
        """
        return self._client_host_name

    @client_host_name.setter
    def client_host_name(self, client_host_name):
        r"""Sets the client_host_name of this Session.

        客户端名称

        :param client_host_name: The client_host_name of this Session.
        :type client_host_name: str
        """
        self._client_host_name = client_host_name

    @property
    def client_port(self):
        r"""Gets the client_port of this Session.

        客户端端口

        :return: The client_port of this Session.
        :rtype: int
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this Session.

        客户端端口

        :param client_port: The client_port of this Session.
        :type client_port: int
        """
        self._client_port = client_port

    @property
    def session_start_time(self):
        r"""Gets the session_start_time of this Session.

        会话建立时间

        :return: The session_start_time of this Session.
        :rtype: str
        """
        return self._session_start_time

    @session_start_time.setter
    def session_start_time(self, session_start_time):
        r"""Sets the session_start_time of this Session.

        会话建立时间

        :param session_start_time: The session_start_time of this Session.
        :type session_start_time: str
        """
        self._session_start_time = session_start_time

    @property
    def transaction_start_time(self):
        r"""Gets the transaction_start_time of this Session.

        事务启动时间

        :return: The transaction_start_time of this Session.
        :rtype: str
        """
        return self._transaction_start_time

    @transaction_start_time.setter
    def transaction_start_time(self, transaction_start_time):
        r"""Sets the transaction_start_time of this Session.

        事务启动时间

        :param transaction_start_time: The transaction_start_time of this Session.
        :type transaction_start_time: str
        """
        self._transaction_start_time = transaction_start_time

    @property
    def transaction_execution_time(self):
        r"""Gets the transaction_execution_time of this Session.

        事务执行时间(s)

        :return: The transaction_execution_time of this Session.
        :rtype: int
        """
        return self._transaction_execution_time

    @transaction_execution_time.setter
    def transaction_execution_time(self, transaction_execution_time):
        r"""Sets the transaction_execution_time of this Session.

        事务执行时间(s)

        :param transaction_execution_time: The transaction_execution_time of this Session.
        :type transaction_execution_time: int
        """
        self._transaction_execution_time = transaction_execution_time

    @property
    def query_start_time(self):
        r"""Gets the query_start_time of this Session.

        查询开始时间

        :return: The query_start_time of this Session.
        :rtype: str
        """
        return self._query_start_time

    @query_start_time.setter
    def query_start_time(self, query_start_time):
        r"""Sets the query_start_time of this Session.

        查询开始时间

        :param query_start_time: The query_start_time of this Session.
        :type query_start_time: str
        """
        self._query_start_time = query_start_time

    @property
    def state_change_time(self):
        r"""Gets the state_change_time of this Session.

        state改变时间

        :return: The state_change_time of this Session.
        :rtype: str
        """
        return self._state_change_time

    @state_change_time.setter
    def state_change_time(self, state_change_time):
        r"""Sets the state_change_time of this Session.

        state改变时间

        :param state_change_time: The state_change_time of this Session.
        :type state_change_time: str
        """
        self._state_change_time = state_change_time

    @property
    def wait_event_type(self):
        r"""Gets the wait_event_type of this Session.

        等待事件类型

        :return: The wait_event_type of this Session.
        :rtype: str
        """
        return self._wait_event_type

    @wait_event_type.setter
    def wait_event_type(self, wait_event_type):
        r"""Sets the wait_event_type of this Session.

        等待事件类型

        :param wait_event_type: The wait_event_type of this Session.
        :type wait_event_type: str
        """
        self._wait_event_type = wait_event_type

    @property
    def wait_event_name(self):
        r"""Gets the wait_event_name of this Session.

        等待事件名称

        :return: The wait_event_name of this Session.
        :rtype: str
        """
        return self._wait_event_name

    @wait_event_name.setter
    def wait_event_name(self, wait_event_name):
        r"""Sets the wait_event_name of this Session.

        等待事件名称

        :param wait_event_name: The wait_event_name of this Session.
        :type wait_event_name: str
        """
        self._wait_event_name = wait_event_name

    @property
    def session_status(self):
        r"""Gets the session_status of this Session.

        会话状态

        :return: The session_status of this Session.
        :rtype: str
        """
        return self._session_status

    @session_status.setter
    def session_status(self, session_status):
        r"""Sets the session_status of this Session.

        会话状态

        :param session_status: The session_status of this Session.
        :type session_status: str
        """
        self._session_status = session_status

    @property
    def backend_xid(self):
        r"""Gets the backend_xid of this Session.

        Backend XID

        :return: The backend_xid of this Session.
        :rtype: int
        """
        return self._backend_xid

    @backend_xid.setter
    def backend_xid(self, backend_xid):
        r"""Sets the backend_xid of this Session.

        Backend XID

        :param backend_xid: The backend_xid of this Session.
        :type backend_xid: int
        """
        self._backend_xid = backend_xid

    @property
    def backend_xmin(self):
        r"""Gets the backend_xmin of this Session.

        Backend Xmin

        :return: The backend_xmin of this Session.
        :rtype: int
        """
        return self._backend_xmin

    @backend_xmin.setter
    def backend_xmin(self, backend_xmin):
        r"""Sets the backend_xmin of this Session.

        Backend Xmin

        :param backend_xmin: The backend_xmin of this Session.
        :type backend_xmin: int
        """
        self._backend_xmin = backend_xmin

    @property
    def query_id(self):
        r"""Gets the query_id of this Session.

        Query ID

        :return: The query_id of this Session.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this Session.

        Query ID

        :param query_id: The query_id of this Session.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this Session.

        SQL语句

        :return: The sql_statement of this Session.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this Session.

        SQL语句

        :param sql_statement: The sql_statement of this Session.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def process_type(self):
        r"""Gets the process_type of this Session.

        进程类型

        :return: The process_type of this Session.
        :rtype: str
        """
        return self._process_type

    @process_type.setter
    def process_type(self, process_type):
        r"""Sets the process_type of this Session.

        进程类型

        :param process_type: The process_type of this Session.
        :type process_type: str
        """
        self._process_type = process_type

    @property
    def memory_usage(self):
        r"""Gets the memory_usage of this Session.

        内存占比(%)

        :return: The memory_usage of this Session.
        :rtype: float
        """
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, memory_usage):
        r"""Sets the memory_usage of this Session.

        内存占比(%)

        :param memory_usage: The memory_usage of this Session.
        :type memory_usage: float
        """
        self._memory_usage = memory_usage

    @property
    def process_status(self):
        r"""Gets the process_status of this Session.

        进程状态

        :return: The process_status of this Session.
        :rtype: str
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this Session.

        进程状态

        :param process_status: The process_status of this Session.
        :type process_status: str
        """
        self._process_status = process_status

    @property
    def cpu_usage(self):
        r"""Gets the cpu_usage of this Session.

        3秒内平均CPU占用率(%)

        :return: The cpu_usage of this Session.
        :rtype: float
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        r"""Sets the cpu_usage of this Session.

        3秒内平均CPU占用率(%)

        :param cpu_usage: The cpu_usage of this Session.
        :type cpu_usage: float
        """
        self._cpu_usage = cpu_usage

    @property
    def io_wait_status(self):
        r"""Gets the io_wait_status of this Session.

        I/O等待时间(s)

        :return: The io_wait_status of this Session.
        :rtype: float
        """
        return self._io_wait_status

    @io_wait_status.setter
    def io_wait_status(self, io_wait_status):
        r"""Sets the io_wait_status of this Session.

        I/O等待时间(s)

        :param io_wait_status: The io_wait_status of this Session.
        :type io_wait_status: float
        """
        self._io_wait_status = io_wait_status

    @property
    def disk_read_rate(self):
        r"""Gets the disk_read_rate of this Session.

        磁盘读速率(MB/s)

        :return: The disk_read_rate of this Session.
        :rtype: float
        """
        return self._disk_read_rate

    @disk_read_rate.setter
    def disk_read_rate(self, disk_read_rate):
        r"""Sets the disk_read_rate of this Session.

        磁盘读速率(MB/s)

        :param disk_read_rate: The disk_read_rate of this Session.
        :type disk_read_rate: float
        """
        self._disk_read_rate = disk_read_rate

    @property
    def disk_write_rate(self):
        r"""Gets the disk_write_rate of this Session.

        磁盘写速率(MB/s)

        :return: The disk_write_rate of this Session.
        :rtype: float
        """
        return self._disk_write_rate

    @disk_write_rate.setter
    def disk_write_rate(self, disk_write_rate):
        r"""Sets the disk_write_rate of this Session.

        磁盘写速率(MB/s)

        :param disk_write_rate: The disk_write_rate of this Session.
        :type disk_write_rate: float
        """
        self._disk_write_rate = disk_write_rate

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
        if not isinstance(other, Session):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
