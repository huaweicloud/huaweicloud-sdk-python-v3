# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WaitEventResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'pid': 'str',
        'wait_event': 'str',
        'wait_status': 'str',
        'database_name': 'str',
        'user_name': 'str',
        'client_addr': 'str',
        'client_port': 'str',
        'session_time': 'str',
        'xact_start': 'str',
        'transaction_time': 'str',
        'query_start': 'str',
        'state_change': 'str',
        'query_time': 'str',
        'backend_start': 'str',
        'waiting': 'str',
        'lockmode': 'str',
        'block_sessionid': 'str',
        'block_count': 'str',
        'unique_sql_id': 'str',
        'query_id': 'str',
        'query': 'str',
        'current_xid': 'str',
        'top_xid': 'str',
        'xlog_quantity': 'str',
        'state': 'str',
        'application_name': 'str',
        'connection_info': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'pid': 'pid',
        'wait_event': 'wait_event',
        'wait_status': 'wait_status',
        'database_name': 'database_name',
        'user_name': 'user_name',
        'client_addr': 'client_addr',
        'client_port': 'client_port',
        'session_time': 'session_time',
        'xact_start': 'xact_start',
        'transaction_time': 'transaction_time',
        'query_start': 'query_start',
        'state_change': 'state_change',
        'query_time': 'query_time',
        'backend_start': 'backend_start',
        'waiting': 'waiting',
        'lockmode': 'lockmode',
        'block_sessionid': 'block_sessionid',
        'block_count': 'block_count',
        'unique_sql_id': 'unique_sql_id',
        'query_id': 'query_id',
        'query': 'query',
        'current_xid': 'current_xid',
        'top_xid': 'top_xid',
        'xlog_quantity': 'xlog_quantity',
        'state': 'state',
        'application_name': 'application_name',
        'connection_info': 'connection_info'
    }

    def __init__(self, session_id=None, pid=None, wait_event=None, wait_status=None, database_name=None, user_name=None, client_addr=None, client_port=None, session_time=None, xact_start=None, transaction_time=None, query_start=None, state_change=None, query_time=None, backend_start=None, waiting=None, lockmode=None, block_sessionid=None, block_count=None, unique_sql_id=None, query_id=None, query=None, current_xid=None, top_xid=None, xlog_quantity=None, state=None, application_name=None, connection_info=None):
        r"""WaitEventResult

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**: 会话ID。 **取值范围**: 不涉及。
        :type session_id: str
        :param pid: **参数解释**: 线程ID。 **取值范围**: 不涉及。
        :type pid: str
        :param wait_event: **参数解释**: 等待事件。 参见“开发指南 &gt; 系统表和系统视图 &gt; 系统视图 &gt; 其他系统视图 &gt; PG_THREAD_WAIT_STATUS”中的wait_event字段。 **取值范围**: 不涉及。
        :type wait_event: str
        :param wait_status: **参数解释**: 等待状态。 参见“开发指南 &gt; 系统表和系统视图 &gt; 系统视图 &gt; 其他系统视图 &gt; PG_THREAD_WAIT_STATUS”中的等待状态列表。 **取值范围**: 不涉及。
        :type wait_status: str
        :param database_name: **参数解释**: 数据库名称。 **取值范围**: 不涉及。
        :type database_name: str
        :param user_name: **参数解释**: 用户名称。 **取值范围**: 不涉及。
        :type user_name: str
        :param client_addr: **参数解释**: 客户端地址。 **取值范围**: 不涉及。
        :type client_addr: str
        :param client_port: **参数解释**: 客户端用于与后台通讯的TCP端口号。 **取值范围**: 不涉及。
        :type client_port: str
        :param session_time: **参数解释**: 会话持续时间，单位：秒。 **取值范围**: 不涉及。
        :type session_time: str
        :param xact_start: **参数解释**: 会话开始时间。 **取值范围**: 不涉及。
        :type xact_start: str
        :param transaction_time: **参数解释**: 事务持续时间，单位秒。 **取值范围**: 不涉及。
        :type transaction_time: str
        :param query_start: **参数解释**: 查询开始时间。 **取值范围**: 不涉及。
        :type query_start: str
        :param state_change: **参数解释**: 上次状态改变的时间。 **取值范围**: 不涉及。
        :type state_change: str
        :param query_time: **参数解释**: 查询持续时间，单位秒。 **取值范围**: 不涉及。
        :type query_time: str
        :param backend_start: **参数解释**: 会话开始时间。 **取值范围**: 不涉及。
        :type backend_start: str
        :param waiting: **参数解释**: 是否在等待锁。 **取值范围**: 不涉及。
        :type waiting: str
        :param lockmode: **参数解释**: （等待获取的）锁模式。 **取值范围**: 不涉及。
        :type lockmode: str
        :param block_sessionid: **参数解释**: 阻塞会话ID。 **取值范围**: 不涉及。
        :type block_sessionid: str
        :param block_count: **参数解释**: 阻塞会话数。 **取值范围**: 不涉及。
        :type block_count: str
        :param unique_sql_id: **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。
        :type unique_sql_id: str
        :param query_id: **参数解释**: 查询 ID。 **取值范围**: 不涉及。
        :type query_id: str
        :param query: **参数解释**: SQL文本。 **取值范围**: 不涉及。
        :type query: str
        :param current_xid: **参数解释**: 当前事务ID。 **取值范围**: 不涉及。
        :type current_xid: str
        :param top_xid: **参数解释**: 顶层事务ID。 **取值范围**: 不涉及。
        :type top_xid: str
        :param xlog_quantity: **参数解释**: 事务当前使用的XLOG量，单位为字节。 **取值范围**: 不涉及。
        :type xlog_quantity: str
        :param state: **参数解释**: 该会话当前总体状态。 **取值范围**: -active：后台正在执行一个查询。 -idle：后台正在等待一个新的客户端命令。 -idle in transaction：后台在事务中，但事务中没有语句在执行。 -fastpath function call：后台正在执行一个fast-path函数。 -disabled：如果后台禁用track_activities，则事务显示此状态。
        :type state: str
        :param application_name: **参数解释**: 应用名称。 **取值范围**: 不涉及。
        :type application_name: str
        :param connection_info: **参数解释**: 连接信息。 **取值范围**: 不涉及。
        :type connection_info: str
        """
        
        

        self._session_id = None
        self._pid = None
        self._wait_event = None
        self._wait_status = None
        self._database_name = None
        self._user_name = None
        self._client_addr = None
        self._client_port = None
        self._session_time = None
        self._xact_start = None
        self._transaction_time = None
        self._query_start = None
        self._state_change = None
        self._query_time = None
        self._backend_start = None
        self._waiting = None
        self._lockmode = None
        self._block_sessionid = None
        self._block_count = None
        self._unique_sql_id = None
        self._query_id = None
        self._query = None
        self._current_xid = None
        self._top_xid = None
        self._xlog_quantity = None
        self._state = None
        self._application_name = None
        self._connection_info = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if pid is not None:
            self.pid = pid
        if wait_event is not None:
            self.wait_event = wait_event
        if wait_status is not None:
            self.wait_status = wait_status
        if database_name is not None:
            self.database_name = database_name
        if user_name is not None:
            self.user_name = user_name
        if client_addr is not None:
            self.client_addr = client_addr
        if client_port is not None:
            self.client_port = client_port
        if session_time is not None:
            self.session_time = session_time
        if xact_start is not None:
            self.xact_start = xact_start
        if transaction_time is not None:
            self.transaction_time = transaction_time
        if query_start is not None:
            self.query_start = query_start
        if state_change is not None:
            self.state_change = state_change
        if query_time is not None:
            self.query_time = query_time
        if backend_start is not None:
            self.backend_start = backend_start
        if waiting is not None:
            self.waiting = waiting
        if lockmode is not None:
            self.lockmode = lockmode
        if block_sessionid is not None:
            self.block_sessionid = block_sessionid
        if block_count is not None:
            self.block_count = block_count
        if unique_sql_id is not None:
            self.unique_sql_id = unique_sql_id
        if query_id is not None:
            self.query_id = query_id
        if query is not None:
            self.query = query
        if current_xid is not None:
            self.current_xid = current_xid
        if top_xid is not None:
            self.top_xid = top_xid
        if xlog_quantity is not None:
            self.xlog_quantity = xlog_quantity
        if state is not None:
            self.state = state
        if application_name is not None:
            self.application_name = application_name
        if connection_info is not None:
            self.connection_info = connection_info

    @property
    def session_id(self):
        r"""Gets the session_id of this WaitEventResult.

        **参数解释**: 会话ID。 **取值范围**: 不涉及。

        :return: The session_id of this WaitEventResult.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this WaitEventResult.

        **参数解释**: 会话ID。 **取值范围**: 不涉及。

        :param session_id: The session_id of this WaitEventResult.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def pid(self):
        r"""Gets the pid of this WaitEventResult.

        **参数解释**: 线程ID。 **取值范围**: 不涉及。

        :return: The pid of this WaitEventResult.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this WaitEventResult.

        **参数解释**: 线程ID。 **取值范围**: 不涉及。

        :param pid: The pid of this WaitEventResult.
        :type pid: str
        """
        self._pid = pid

    @property
    def wait_event(self):
        r"""Gets the wait_event of this WaitEventResult.

        **参数解释**: 等待事件。 参见“开发指南 > 系统表和系统视图 > 系统视图 > 其他系统视图 > PG_THREAD_WAIT_STATUS”中的wait_event字段。 **取值范围**: 不涉及。

        :return: The wait_event of this WaitEventResult.
        :rtype: str
        """
        return self._wait_event

    @wait_event.setter
    def wait_event(self, wait_event):
        r"""Sets the wait_event of this WaitEventResult.

        **参数解释**: 等待事件。 参见“开发指南 > 系统表和系统视图 > 系统视图 > 其他系统视图 > PG_THREAD_WAIT_STATUS”中的wait_event字段。 **取值范围**: 不涉及。

        :param wait_event: The wait_event of this WaitEventResult.
        :type wait_event: str
        """
        self._wait_event = wait_event

    @property
    def wait_status(self):
        r"""Gets the wait_status of this WaitEventResult.

        **参数解释**: 等待状态。 参见“开发指南 > 系统表和系统视图 > 系统视图 > 其他系统视图 > PG_THREAD_WAIT_STATUS”中的等待状态列表。 **取值范围**: 不涉及。

        :return: The wait_status of this WaitEventResult.
        :rtype: str
        """
        return self._wait_status

    @wait_status.setter
    def wait_status(self, wait_status):
        r"""Sets the wait_status of this WaitEventResult.

        **参数解释**: 等待状态。 参见“开发指南 > 系统表和系统视图 > 系统视图 > 其他系统视图 > PG_THREAD_WAIT_STATUS”中的等待状态列表。 **取值范围**: 不涉及。

        :param wait_status: The wait_status of this WaitEventResult.
        :type wait_status: str
        """
        self._wait_status = wait_status

    @property
    def database_name(self):
        r"""Gets the database_name of this WaitEventResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :return: The database_name of this WaitEventResult.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this WaitEventResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :param database_name: The database_name of this WaitEventResult.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def user_name(self):
        r"""Gets the user_name of this WaitEventResult.

        **参数解释**: 用户名称。 **取值范围**: 不涉及。

        :return: The user_name of this WaitEventResult.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this WaitEventResult.

        **参数解释**: 用户名称。 **取值范围**: 不涉及。

        :param user_name: The user_name of this WaitEventResult.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def client_addr(self):
        r"""Gets the client_addr of this WaitEventResult.

        **参数解释**: 客户端地址。 **取值范围**: 不涉及。

        :return: The client_addr of this WaitEventResult.
        :rtype: str
        """
        return self._client_addr

    @client_addr.setter
    def client_addr(self, client_addr):
        r"""Sets the client_addr of this WaitEventResult.

        **参数解释**: 客户端地址。 **取值范围**: 不涉及。

        :param client_addr: The client_addr of this WaitEventResult.
        :type client_addr: str
        """
        self._client_addr = client_addr

    @property
    def client_port(self):
        r"""Gets the client_port of this WaitEventResult.

        **参数解释**: 客户端用于与后台通讯的TCP端口号。 **取值范围**: 不涉及。

        :return: The client_port of this WaitEventResult.
        :rtype: str
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this WaitEventResult.

        **参数解释**: 客户端用于与后台通讯的TCP端口号。 **取值范围**: 不涉及。

        :param client_port: The client_port of this WaitEventResult.
        :type client_port: str
        """
        self._client_port = client_port

    @property
    def session_time(self):
        r"""Gets the session_time of this WaitEventResult.

        **参数解释**: 会话持续时间，单位：秒。 **取值范围**: 不涉及。

        :return: The session_time of this WaitEventResult.
        :rtype: str
        """
        return self._session_time

    @session_time.setter
    def session_time(self, session_time):
        r"""Sets the session_time of this WaitEventResult.

        **参数解释**: 会话持续时间，单位：秒。 **取值范围**: 不涉及。

        :param session_time: The session_time of this WaitEventResult.
        :type session_time: str
        """
        self._session_time = session_time

    @property
    def xact_start(self):
        r"""Gets the xact_start of this WaitEventResult.

        **参数解释**: 会话开始时间。 **取值范围**: 不涉及。

        :return: The xact_start of this WaitEventResult.
        :rtype: str
        """
        return self._xact_start

    @xact_start.setter
    def xact_start(self, xact_start):
        r"""Sets the xact_start of this WaitEventResult.

        **参数解释**: 会话开始时间。 **取值范围**: 不涉及。

        :param xact_start: The xact_start of this WaitEventResult.
        :type xact_start: str
        """
        self._xact_start = xact_start

    @property
    def transaction_time(self):
        r"""Gets the transaction_time of this WaitEventResult.

        **参数解释**: 事务持续时间，单位秒。 **取值范围**: 不涉及。

        :return: The transaction_time of this WaitEventResult.
        :rtype: str
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        r"""Sets the transaction_time of this WaitEventResult.

        **参数解释**: 事务持续时间，单位秒。 **取值范围**: 不涉及。

        :param transaction_time: The transaction_time of this WaitEventResult.
        :type transaction_time: str
        """
        self._transaction_time = transaction_time

    @property
    def query_start(self):
        r"""Gets the query_start of this WaitEventResult.

        **参数解释**: 查询开始时间。 **取值范围**: 不涉及。

        :return: The query_start of this WaitEventResult.
        :rtype: str
        """
        return self._query_start

    @query_start.setter
    def query_start(self, query_start):
        r"""Sets the query_start of this WaitEventResult.

        **参数解释**: 查询开始时间。 **取值范围**: 不涉及。

        :param query_start: The query_start of this WaitEventResult.
        :type query_start: str
        """
        self._query_start = query_start

    @property
    def state_change(self):
        r"""Gets the state_change of this WaitEventResult.

        **参数解释**: 上次状态改变的时间。 **取值范围**: 不涉及。

        :return: The state_change of this WaitEventResult.
        :rtype: str
        """
        return self._state_change

    @state_change.setter
    def state_change(self, state_change):
        r"""Sets the state_change of this WaitEventResult.

        **参数解释**: 上次状态改变的时间。 **取值范围**: 不涉及。

        :param state_change: The state_change of this WaitEventResult.
        :type state_change: str
        """
        self._state_change = state_change

    @property
    def query_time(self):
        r"""Gets the query_time of this WaitEventResult.

        **参数解释**: 查询持续时间，单位秒。 **取值范围**: 不涉及。

        :return: The query_time of this WaitEventResult.
        :rtype: str
        """
        return self._query_time

    @query_time.setter
    def query_time(self, query_time):
        r"""Sets the query_time of this WaitEventResult.

        **参数解释**: 查询持续时间，单位秒。 **取值范围**: 不涉及。

        :param query_time: The query_time of this WaitEventResult.
        :type query_time: str
        """
        self._query_time = query_time

    @property
    def backend_start(self):
        r"""Gets the backend_start of this WaitEventResult.

        **参数解释**: 会话开始时间。 **取值范围**: 不涉及。

        :return: The backend_start of this WaitEventResult.
        :rtype: str
        """
        return self._backend_start

    @backend_start.setter
    def backend_start(self, backend_start):
        r"""Sets the backend_start of this WaitEventResult.

        **参数解释**: 会话开始时间。 **取值范围**: 不涉及。

        :param backend_start: The backend_start of this WaitEventResult.
        :type backend_start: str
        """
        self._backend_start = backend_start

    @property
    def waiting(self):
        r"""Gets the waiting of this WaitEventResult.

        **参数解释**: 是否在等待锁。 **取值范围**: 不涉及。

        :return: The waiting of this WaitEventResult.
        :rtype: str
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        r"""Sets the waiting of this WaitEventResult.

        **参数解释**: 是否在等待锁。 **取值范围**: 不涉及。

        :param waiting: The waiting of this WaitEventResult.
        :type waiting: str
        """
        self._waiting = waiting

    @property
    def lockmode(self):
        r"""Gets the lockmode of this WaitEventResult.

        **参数解释**: （等待获取的）锁模式。 **取值范围**: 不涉及。

        :return: The lockmode of this WaitEventResult.
        :rtype: str
        """
        return self._lockmode

    @lockmode.setter
    def lockmode(self, lockmode):
        r"""Sets the lockmode of this WaitEventResult.

        **参数解释**: （等待获取的）锁模式。 **取值范围**: 不涉及。

        :param lockmode: The lockmode of this WaitEventResult.
        :type lockmode: str
        """
        self._lockmode = lockmode

    @property
    def block_sessionid(self):
        r"""Gets the block_sessionid of this WaitEventResult.

        **参数解释**: 阻塞会话ID。 **取值范围**: 不涉及。

        :return: The block_sessionid of this WaitEventResult.
        :rtype: str
        """
        return self._block_sessionid

    @block_sessionid.setter
    def block_sessionid(self, block_sessionid):
        r"""Sets the block_sessionid of this WaitEventResult.

        **参数解释**: 阻塞会话ID。 **取值范围**: 不涉及。

        :param block_sessionid: The block_sessionid of this WaitEventResult.
        :type block_sessionid: str
        """
        self._block_sessionid = block_sessionid

    @property
    def block_count(self):
        r"""Gets the block_count of this WaitEventResult.

        **参数解释**: 阻塞会话数。 **取值范围**: 不涉及。

        :return: The block_count of this WaitEventResult.
        :rtype: str
        """
        return self._block_count

    @block_count.setter
    def block_count(self, block_count):
        r"""Sets the block_count of this WaitEventResult.

        **参数解释**: 阻塞会话数。 **取值范围**: 不涉及。

        :param block_count: The block_count of this WaitEventResult.
        :type block_count: str
        """
        self._block_count = block_count

    @property
    def unique_sql_id(self):
        r"""Gets the unique_sql_id of this WaitEventResult.

        **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。

        :return: The unique_sql_id of this WaitEventResult.
        :rtype: str
        """
        return self._unique_sql_id

    @unique_sql_id.setter
    def unique_sql_id(self, unique_sql_id):
        r"""Sets the unique_sql_id of this WaitEventResult.

        **参数解释**: 归一化SQL ID。 **取值范围**: 不涉及。

        :param unique_sql_id: The unique_sql_id of this WaitEventResult.
        :type unique_sql_id: str
        """
        self._unique_sql_id = unique_sql_id

    @property
    def query_id(self):
        r"""Gets the query_id of this WaitEventResult.

        **参数解释**: 查询 ID。 **取值范围**: 不涉及。

        :return: The query_id of this WaitEventResult.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this WaitEventResult.

        **参数解释**: 查询 ID。 **取值范围**: 不涉及。

        :param query_id: The query_id of this WaitEventResult.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def query(self):
        r"""Gets the query of this WaitEventResult.

        **参数解释**: SQL文本。 **取值范围**: 不涉及。

        :return: The query of this WaitEventResult.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this WaitEventResult.

        **参数解释**: SQL文本。 **取值范围**: 不涉及。

        :param query: The query of this WaitEventResult.
        :type query: str
        """
        self._query = query

    @property
    def current_xid(self):
        r"""Gets the current_xid of this WaitEventResult.

        **参数解释**: 当前事务ID。 **取值范围**: 不涉及。

        :return: The current_xid of this WaitEventResult.
        :rtype: str
        """
        return self._current_xid

    @current_xid.setter
    def current_xid(self, current_xid):
        r"""Sets the current_xid of this WaitEventResult.

        **参数解释**: 当前事务ID。 **取值范围**: 不涉及。

        :param current_xid: The current_xid of this WaitEventResult.
        :type current_xid: str
        """
        self._current_xid = current_xid

    @property
    def top_xid(self):
        r"""Gets the top_xid of this WaitEventResult.

        **参数解释**: 顶层事务ID。 **取值范围**: 不涉及。

        :return: The top_xid of this WaitEventResult.
        :rtype: str
        """
        return self._top_xid

    @top_xid.setter
    def top_xid(self, top_xid):
        r"""Sets the top_xid of this WaitEventResult.

        **参数解释**: 顶层事务ID。 **取值范围**: 不涉及。

        :param top_xid: The top_xid of this WaitEventResult.
        :type top_xid: str
        """
        self._top_xid = top_xid

    @property
    def xlog_quantity(self):
        r"""Gets the xlog_quantity of this WaitEventResult.

        **参数解释**: 事务当前使用的XLOG量，单位为字节。 **取值范围**: 不涉及。

        :return: The xlog_quantity of this WaitEventResult.
        :rtype: str
        """
        return self._xlog_quantity

    @xlog_quantity.setter
    def xlog_quantity(self, xlog_quantity):
        r"""Sets the xlog_quantity of this WaitEventResult.

        **参数解释**: 事务当前使用的XLOG量，单位为字节。 **取值范围**: 不涉及。

        :param xlog_quantity: The xlog_quantity of this WaitEventResult.
        :type xlog_quantity: str
        """
        self._xlog_quantity = xlog_quantity

    @property
    def state(self):
        r"""Gets the state of this WaitEventResult.

        **参数解释**: 该会话当前总体状态。 **取值范围**: -active：后台正在执行一个查询。 -idle：后台正在等待一个新的客户端命令。 -idle in transaction：后台在事务中，但事务中没有语句在执行。 -fastpath function call：后台正在执行一个fast-path函数。 -disabled：如果后台禁用track_activities，则事务显示此状态。

        :return: The state of this WaitEventResult.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this WaitEventResult.

        **参数解释**: 该会话当前总体状态。 **取值范围**: -active：后台正在执行一个查询。 -idle：后台正在等待一个新的客户端命令。 -idle in transaction：后台在事务中，但事务中没有语句在执行。 -fastpath function call：后台正在执行一个fast-path函数。 -disabled：如果后台禁用track_activities，则事务显示此状态。

        :param state: The state of this WaitEventResult.
        :type state: str
        """
        self._state = state

    @property
    def application_name(self):
        r"""Gets the application_name of this WaitEventResult.

        **参数解释**: 应用名称。 **取值范围**: 不涉及。

        :return: The application_name of this WaitEventResult.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this WaitEventResult.

        **参数解释**: 应用名称。 **取值范围**: 不涉及。

        :param application_name: The application_name of this WaitEventResult.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def connection_info(self):
        r"""Gets the connection_info of this WaitEventResult.

        **参数解释**: 连接信息。 **取值范围**: 不涉及。

        :return: The connection_info of this WaitEventResult.
        :rtype: str
        """
        return self._connection_info

    @connection_info.setter
    def connection_info(self, connection_info):
        r"""Sets the connection_info of this WaitEventResult.

        **参数解释**: 连接信息。 **取值范围**: 不涉及。

        :param connection_info: The connection_info of this WaitEventResult.
        :type connection_info: str
        """
        self._connection_info = connection_info

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
        if not isinstance(other, WaitEventResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
