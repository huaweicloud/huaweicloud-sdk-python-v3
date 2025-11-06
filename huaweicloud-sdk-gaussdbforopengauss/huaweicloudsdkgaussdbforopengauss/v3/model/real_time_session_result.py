# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RealTimeSessionResult:

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
        'unique_sql_id': 'str',
        'database_name': 'str',
        'client_ip': 'str',
        'user_name': 'str',
        'wait': 'str',
        'block_session': 'str',
        'wait_event': 'str',
        'state': 'str',
        'query_runtime': 'str',
        'query': 'str',
        'back_end_start': 'int',
        'transaction_start': 'int',
        'query_start': 'int',
        'application_name': 'str',
        'exec_time': 'str',
        'trans_num': 'str',
        'rollback_num': 'str',
        'sql_num': 'str',
        'client_port': 'str',
        'query_id': 'str',
        'transaction_time_cost': 'str',
        'trace_id': 'str',
        'global_session_id': 'str',
        'top_transaction_id': 'str',
        'current_transaction_id': 'str',
        'xlog_quantity_pretty': 'str',
        'wait_status': 'str',
        'lwt_id': 'str',
        'thread_name': 'str',
        'lock_mode': 'str',
        'parent_session_id': 'str',
        'smp_id': 'str',
        'lock_tag': 'str',
        'component_name': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'pid': 'pid',
        'unique_sql_id': 'unique_sql_id',
        'database_name': 'database_name',
        'client_ip': 'client_ip',
        'user_name': 'user_name',
        'wait': 'wait',
        'block_session': 'block_session',
        'wait_event': 'wait_event',
        'state': 'state',
        'query_runtime': 'query_runtime',
        'query': 'query',
        'back_end_start': 'back_end_start',
        'transaction_start': 'transaction_start',
        'query_start': 'query_start',
        'application_name': 'application_name',
        'exec_time': 'exec_time',
        'trans_num': 'trans_num',
        'rollback_num': 'rollback_num',
        'sql_num': 'sql_num',
        'client_port': 'client_port',
        'query_id': 'query_id',
        'transaction_time_cost': 'transaction_time_cost',
        'trace_id': 'trace_id',
        'global_session_id': 'global_session_id',
        'top_transaction_id': 'top_transaction_id',
        'current_transaction_id': 'current_transaction_id',
        'xlog_quantity_pretty': 'xlog_quantity_pretty',
        'wait_status': 'wait_status',
        'lwt_id': 'lwt_id',
        'thread_name': 'thread_name',
        'lock_mode': 'lock_mode',
        'parent_session_id': 'parent_session_id',
        'smp_id': 'smp_id',
        'lock_tag': 'lock_tag',
        'component_name': 'component_name'
    }

    def __init__(self, session_id=None, pid=None, unique_sql_id=None, database_name=None, client_ip=None, user_name=None, wait=None, block_session=None, wait_event=None, state=None, query_runtime=None, query=None, back_end_start=None, transaction_start=None, query_start=None, application_name=None, exec_time=None, trans_num=None, rollback_num=None, sql_num=None, client_port=None, query_id=None, transaction_time_cost=None, trace_id=None, global_session_id=None, top_transaction_id=None, current_transaction_id=None, xlog_quantity_pretty=None, wait_status=None, lwt_id=None, thread_name=None, lock_mode=None, parent_session_id=None, smp_id=None, lock_tag=None, component_name=None):
        r"""RealTimeSessionResult

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**： 会话ID。 **取值范围**： 不涉及。
        :type session_id: str
        :param pid: **参数解释**： 线程ID。 **取值范围**： 不涉及。
        :type pid: str
        :param unique_sql_id: **参数解释**： SQL ID。 **取值范围**： 不涉及。
        :type unique_sql_id: str
        :param database_name: **参数解释**： 数据库名称。 **取值范围**： 不涉及。
        :type database_name: str
        :param client_ip: **参数解释**： 客户端IP。 **取值范围**： 不涉及。
        :type client_ip: str
        :param user_name: **参数解释**： 用户名称。 **取值范围**： 不涉及。
        :type user_name: str
        :param wait: **参数解释**： 是否等待。 **取值范围**： 不涉及。
        :type wait: str
        :param block_session: **参数解释**： 阻塞会话。 **取值范围**： 不涉及。
        :type block_session: str
        :param wait_event: **参数解释**： 等待事件。 **取值范围**： 不涉及。
        :type wait_event: str
        :param state: **参数解释**： 状态。 **取值范围**： 不涉及。
        :type state: str
        :param query_runtime: **参数解释**： 语句执行时长。 **取值范围**： 不涉及。
        :type query_runtime: str
        :param query: **参数解释**： SQL文本。 **取值范围**： 不涉及。
        :type query: str
        :param back_end_start: **参数解释**： 会话开始时间。 **取值范围**： 不涉及。
        :type back_end_start: int
        :param transaction_start: **参数解释**： 事务开始时间。 **取值范围**： 不涉及。
        :type transaction_start: int
        :param query_start: **参数解释**： 语句开始时间。 **取值范围**： 不涉及。
        :type query_start: int
        :param application_name: **参数解释**： 应用名称。 **取值范围**： 不涉及。
        :type application_name: str
        :param exec_time: **参数解释**： 会话执行时长（单位：秒）。 **取值范围**： 不涉及。
        :type exec_time: str
        :param trans_num: **参数解释**： 会话建立事务的数量。 **取值范围**： 不涉及。
        :type trans_num: str
        :param rollback_num: **参数解释**： 会话中事务回滚的次数。 **取值范围**： 不涉及。
        :type rollback_num: str
        :param sql_num: **参数解释**： 会话执行的sql数。 **取值范围**： 不涉及。
        :type sql_num: str
        :param client_port: **参数解释**： 客户端用于与后台通讯的TCP端口号，如果使用Unix套接字，则为-1。 **取值范围**： 不涉及。
        :type client_port: str
        :param query_id: **参数解释**： 会话执行的sql数。 **取值范围**： 不涉及。
        :type query_id: str
        :param transaction_time_cost: **参数解释**： 当前用户上一次执行的事务持续时间。 **取值范围**： 不涉及。
        :type transaction_time_cost: str
        :param trace_id: **参数解释**： 驱动传入的trace id，用于标识应用的一次请求。 **取值范围**： 不涉及。
        :type trace_id: str
        :param global_session_id: **参数解释**： 当前用户上次执行的全局会话ID。 **取值范围**： 不涉及。
        :type global_session_id: str
        :param top_transaction_id: **参数解释**： 当前用户上次执行的顶层事务ID。 **取值范围**： 不涉及。
        :type top_transaction_id: str
        :param current_transaction_id: **参数解释**： 当前用户上次执行的事务ID。 **取值范围**： 不涉及。
        :type current_transaction_id: str
        :param xlog_quantity_pretty: **参数解释**： 当前用户上次执行的事务使用的XLOG量，易读格式。 **取值范围**： 不涉及。
        :type xlog_quantity_pretty: str
        :param wait_status: **参数解释**： 实例线程等待状态。 **取值范围**： 不涉及。
        :type wait_status: str
        :param lwt_id: **参数解释**： 实例线程的轻量级线程号。 **取值范围**： 不涉及。
        :type lwt_id: str
        :param thread_name: **参数解释**： 实例线程名。 **取值范围**： 不涉及。
        :type thread_name: str
        :param lock_mode: **参数解释**： 实例等锁模式。 **取值范围**： 不涉及。
        :type lock_mode: str
        :param parent_session_id: **参数解释**： 实例父会话ID。 **取值范围**： 不涉及。
        :type parent_session_id: str
        :param smp_id: **参数解释**： 实例并行线程的ID。 **取值范围**： 不涉及。
        :type smp_id: str
        :param lock_tag: **参数解释**： 实例线程正等待获取的锁的信息。 **取值范围**： 不涉及。
        :type lock_tag: str
        :param component_name: **参数解释**： 组件名称。 **取值范围**： 不涉及。
        :type component_name: str
        """
        
        

        self._session_id = None
        self._pid = None
        self._unique_sql_id = None
        self._database_name = None
        self._client_ip = None
        self._user_name = None
        self._wait = None
        self._block_session = None
        self._wait_event = None
        self._state = None
        self._query_runtime = None
        self._query = None
        self._back_end_start = None
        self._transaction_start = None
        self._query_start = None
        self._application_name = None
        self._exec_time = None
        self._trans_num = None
        self._rollback_num = None
        self._sql_num = None
        self._client_port = None
        self._query_id = None
        self._transaction_time_cost = None
        self._trace_id = None
        self._global_session_id = None
        self._top_transaction_id = None
        self._current_transaction_id = None
        self._xlog_quantity_pretty = None
        self._wait_status = None
        self._lwt_id = None
        self._thread_name = None
        self._lock_mode = None
        self._parent_session_id = None
        self._smp_id = None
        self._lock_tag = None
        self._component_name = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if pid is not None:
            self.pid = pid
        if unique_sql_id is not None:
            self.unique_sql_id = unique_sql_id
        if database_name is not None:
            self.database_name = database_name
        if client_ip is not None:
            self.client_ip = client_ip
        if user_name is not None:
            self.user_name = user_name
        if wait is not None:
            self.wait = wait
        if block_session is not None:
            self.block_session = block_session
        if wait_event is not None:
            self.wait_event = wait_event
        if state is not None:
            self.state = state
        if query_runtime is not None:
            self.query_runtime = query_runtime
        if query is not None:
            self.query = query
        if back_end_start is not None:
            self.back_end_start = back_end_start
        if transaction_start is not None:
            self.transaction_start = transaction_start
        if query_start is not None:
            self.query_start = query_start
        if application_name is not None:
            self.application_name = application_name
        if exec_time is not None:
            self.exec_time = exec_time
        if trans_num is not None:
            self.trans_num = trans_num
        if rollback_num is not None:
            self.rollback_num = rollback_num
        if sql_num is not None:
            self.sql_num = sql_num
        if client_port is not None:
            self.client_port = client_port
        if query_id is not None:
            self.query_id = query_id
        if transaction_time_cost is not None:
            self.transaction_time_cost = transaction_time_cost
        if trace_id is not None:
            self.trace_id = trace_id
        if global_session_id is not None:
            self.global_session_id = global_session_id
        if top_transaction_id is not None:
            self.top_transaction_id = top_transaction_id
        if current_transaction_id is not None:
            self.current_transaction_id = current_transaction_id
        if xlog_quantity_pretty is not None:
            self.xlog_quantity_pretty = xlog_quantity_pretty
        if wait_status is not None:
            self.wait_status = wait_status
        if lwt_id is not None:
            self.lwt_id = lwt_id
        if thread_name is not None:
            self.thread_name = thread_name
        if lock_mode is not None:
            self.lock_mode = lock_mode
        if parent_session_id is not None:
            self.parent_session_id = parent_session_id
        if smp_id is not None:
            self.smp_id = smp_id
        if lock_tag is not None:
            self.lock_tag = lock_tag
        if component_name is not None:
            self.component_name = component_name

    @property
    def session_id(self):
        r"""Gets the session_id of this RealTimeSessionResult.

        **参数解释**： 会话ID。 **取值范围**： 不涉及。

        :return: The session_id of this RealTimeSessionResult.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this RealTimeSessionResult.

        **参数解释**： 会话ID。 **取值范围**： 不涉及。

        :param session_id: The session_id of this RealTimeSessionResult.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def pid(self):
        r"""Gets the pid of this RealTimeSessionResult.

        **参数解释**： 线程ID。 **取值范围**： 不涉及。

        :return: The pid of this RealTimeSessionResult.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this RealTimeSessionResult.

        **参数解释**： 线程ID。 **取值范围**： 不涉及。

        :param pid: The pid of this RealTimeSessionResult.
        :type pid: str
        """
        self._pid = pid

    @property
    def unique_sql_id(self):
        r"""Gets the unique_sql_id of this RealTimeSessionResult.

        **参数解释**： SQL ID。 **取值范围**： 不涉及。

        :return: The unique_sql_id of this RealTimeSessionResult.
        :rtype: str
        """
        return self._unique_sql_id

    @unique_sql_id.setter
    def unique_sql_id(self, unique_sql_id):
        r"""Sets the unique_sql_id of this RealTimeSessionResult.

        **参数解释**： SQL ID。 **取值范围**： 不涉及。

        :param unique_sql_id: The unique_sql_id of this RealTimeSessionResult.
        :type unique_sql_id: str
        """
        self._unique_sql_id = unique_sql_id

    @property
    def database_name(self):
        r"""Gets the database_name of this RealTimeSessionResult.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :return: The database_name of this RealTimeSessionResult.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this RealTimeSessionResult.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :param database_name: The database_name of this RealTimeSessionResult.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def client_ip(self):
        r"""Gets the client_ip of this RealTimeSessionResult.

        **参数解释**： 客户端IP。 **取值范围**： 不涉及。

        :return: The client_ip of this RealTimeSessionResult.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this RealTimeSessionResult.

        **参数解释**： 客户端IP。 **取值范围**： 不涉及。

        :param client_ip: The client_ip of this RealTimeSessionResult.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def user_name(self):
        r"""Gets the user_name of this RealTimeSessionResult.

        **参数解释**： 用户名称。 **取值范围**： 不涉及。

        :return: The user_name of this RealTimeSessionResult.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this RealTimeSessionResult.

        **参数解释**： 用户名称。 **取值范围**： 不涉及。

        :param user_name: The user_name of this RealTimeSessionResult.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def wait(self):
        r"""Gets the wait of this RealTimeSessionResult.

        **参数解释**： 是否等待。 **取值范围**： 不涉及。

        :return: The wait of this RealTimeSessionResult.
        :rtype: str
        """
        return self._wait

    @wait.setter
    def wait(self, wait):
        r"""Sets the wait of this RealTimeSessionResult.

        **参数解释**： 是否等待。 **取值范围**： 不涉及。

        :param wait: The wait of this RealTimeSessionResult.
        :type wait: str
        """
        self._wait = wait

    @property
    def block_session(self):
        r"""Gets the block_session of this RealTimeSessionResult.

        **参数解释**： 阻塞会话。 **取值范围**： 不涉及。

        :return: The block_session of this RealTimeSessionResult.
        :rtype: str
        """
        return self._block_session

    @block_session.setter
    def block_session(self, block_session):
        r"""Sets the block_session of this RealTimeSessionResult.

        **参数解释**： 阻塞会话。 **取值范围**： 不涉及。

        :param block_session: The block_session of this RealTimeSessionResult.
        :type block_session: str
        """
        self._block_session = block_session

    @property
    def wait_event(self):
        r"""Gets the wait_event of this RealTimeSessionResult.

        **参数解释**： 等待事件。 **取值范围**： 不涉及。

        :return: The wait_event of this RealTimeSessionResult.
        :rtype: str
        """
        return self._wait_event

    @wait_event.setter
    def wait_event(self, wait_event):
        r"""Sets the wait_event of this RealTimeSessionResult.

        **参数解释**： 等待事件。 **取值范围**： 不涉及。

        :param wait_event: The wait_event of this RealTimeSessionResult.
        :type wait_event: str
        """
        self._wait_event = wait_event

    @property
    def state(self):
        r"""Gets the state of this RealTimeSessionResult.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :return: The state of this RealTimeSessionResult.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this RealTimeSessionResult.

        **参数解释**： 状态。 **取值范围**： 不涉及。

        :param state: The state of this RealTimeSessionResult.
        :type state: str
        """
        self._state = state

    @property
    def query_runtime(self):
        r"""Gets the query_runtime of this RealTimeSessionResult.

        **参数解释**： 语句执行时长。 **取值范围**： 不涉及。

        :return: The query_runtime of this RealTimeSessionResult.
        :rtype: str
        """
        return self._query_runtime

    @query_runtime.setter
    def query_runtime(self, query_runtime):
        r"""Sets the query_runtime of this RealTimeSessionResult.

        **参数解释**： 语句执行时长。 **取值范围**： 不涉及。

        :param query_runtime: The query_runtime of this RealTimeSessionResult.
        :type query_runtime: str
        """
        self._query_runtime = query_runtime

    @property
    def query(self):
        r"""Gets the query of this RealTimeSessionResult.

        **参数解释**： SQL文本。 **取值范围**： 不涉及。

        :return: The query of this RealTimeSessionResult.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this RealTimeSessionResult.

        **参数解释**： SQL文本。 **取值范围**： 不涉及。

        :param query: The query of this RealTimeSessionResult.
        :type query: str
        """
        self._query = query

    @property
    def back_end_start(self):
        r"""Gets the back_end_start of this RealTimeSessionResult.

        **参数解释**： 会话开始时间。 **取值范围**： 不涉及。

        :return: The back_end_start of this RealTimeSessionResult.
        :rtype: int
        """
        return self._back_end_start

    @back_end_start.setter
    def back_end_start(self, back_end_start):
        r"""Sets the back_end_start of this RealTimeSessionResult.

        **参数解释**： 会话开始时间。 **取值范围**： 不涉及。

        :param back_end_start: The back_end_start of this RealTimeSessionResult.
        :type back_end_start: int
        """
        self._back_end_start = back_end_start

    @property
    def transaction_start(self):
        r"""Gets the transaction_start of this RealTimeSessionResult.

        **参数解释**： 事务开始时间。 **取值范围**： 不涉及。

        :return: The transaction_start of this RealTimeSessionResult.
        :rtype: int
        """
        return self._transaction_start

    @transaction_start.setter
    def transaction_start(self, transaction_start):
        r"""Sets the transaction_start of this RealTimeSessionResult.

        **参数解释**： 事务开始时间。 **取值范围**： 不涉及。

        :param transaction_start: The transaction_start of this RealTimeSessionResult.
        :type transaction_start: int
        """
        self._transaction_start = transaction_start

    @property
    def query_start(self):
        r"""Gets the query_start of this RealTimeSessionResult.

        **参数解释**： 语句开始时间。 **取值范围**： 不涉及。

        :return: The query_start of this RealTimeSessionResult.
        :rtype: int
        """
        return self._query_start

    @query_start.setter
    def query_start(self, query_start):
        r"""Sets the query_start of this RealTimeSessionResult.

        **参数解释**： 语句开始时间。 **取值范围**： 不涉及。

        :param query_start: The query_start of this RealTimeSessionResult.
        :type query_start: int
        """
        self._query_start = query_start

    @property
    def application_name(self):
        r"""Gets the application_name of this RealTimeSessionResult.

        **参数解释**： 应用名称。 **取值范围**： 不涉及。

        :return: The application_name of this RealTimeSessionResult.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this RealTimeSessionResult.

        **参数解释**： 应用名称。 **取值范围**： 不涉及。

        :param application_name: The application_name of this RealTimeSessionResult.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def exec_time(self):
        r"""Gets the exec_time of this RealTimeSessionResult.

        **参数解释**： 会话执行时长（单位：秒）。 **取值范围**： 不涉及。

        :return: The exec_time of this RealTimeSessionResult.
        :rtype: str
        """
        return self._exec_time

    @exec_time.setter
    def exec_time(self, exec_time):
        r"""Sets the exec_time of this RealTimeSessionResult.

        **参数解释**： 会话执行时长（单位：秒）。 **取值范围**： 不涉及。

        :param exec_time: The exec_time of this RealTimeSessionResult.
        :type exec_time: str
        """
        self._exec_time = exec_time

    @property
    def trans_num(self):
        r"""Gets the trans_num of this RealTimeSessionResult.

        **参数解释**： 会话建立事务的数量。 **取值范围**： 不涉及。

        :return: The trans_num of this RealTimeSessionResult.
        :rtype: str
        """
        return self._trans_num

    @trans_num.setter
    def trans_num(self, trans_num):
        r"""Sets the trans_num of this RealTimeSessionResult.

        **参数解释**： 会话建立事务的数量。 **取值范围**： 不涉及。

        :param trans_num: The trans_num of this RealTimeSessionResult.
        :type trans_num: str
        """
        self._trans_num = trans_num

    @property
    def rollback_num(self):
        r"""Gets the rollback_num of this RealTimeSessionResult.

        **参数解释**： 会话中事务回滚的次数。 **取值范围**： 不涉及。

        :return: The rollback_num of this RealTimeSessionResult.
        :rtype: str
        """
        return self._rollback_num

    @rollback_num.setter
    def rollback_num(self, rollback_num):
        r"""Sets the rollback_num of this RealTimeSessionResult.

        **参数解释**： 会话中事务回滚的次数。 **取值范围**： 不涉及。

        :param rollback_num: The rollback_num of this RealTimeSessionResult.
        :type rollback_num: str
        """
        self._rollback_num = rollback_num

    @property
    def sql_num(self):
        r"""Gets the sql_num of this RealTimeSessionResult.

        **参数解释**： 会话执行的sql数。 **取值范围**： 不涉及。

        :return: The sql_num of this RealTimeSessionResult.
        :rtype: str
        """
        return self._sql_num

    @sql_num.setter
    def sql_num(self, sql_num):
        r"""Sets the sql_num of this RealTimeSessionResult.

        **参数解释**： 会话执行的sql数。 **取值范围**： 不涉及。

        :param sql_num: The sql_num of this RealTimeSessionResult.
        :type sql_num: str
        """
        self._sql_num = sql_num

    @property
    def client_port(self):
        r"""Gets the client_port of this RealTimeSessionResult.

        **参数解释**： 客户端用于与后台通讯的TCP端口号，如果使用Unix套接字，则为-1。 **取值范围**： 不涉及。

        :return: The client_port of this RealTimeSessionResult.
        :rtype: str
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this RealTimeSessionResult.

        **参数解释**： 客户端用于与后台通讯的TCP端口号，如果使用Unix套接字，则为-1。 **取值范围**： 不涉及。

        :param client_port: The client_port of this RealTimeSessionResult.
        :type client_port: str
        """
        self._client_port = client_port

    @property
    def query_id(self):
        r"""Gets the query_id of this RealTimeSessionResult.

        **参数解释**： 会话执行的sql数。 **取值范围**： 不涉及。

        :return: The query_id of this RealTimeSessionResult.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this RealTimeSessionResult.

        **参数解释**： 会话执行的sql数。 **取值范围**： 不涉及。

        :param query_id: The query_id of this RealTimeSessionResult.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def transaction_time_cost(self):
        r"""Gets the transaction_time_cost of this RealTimeSessionResult.

        **参数解释**： 当前用户上一次执行的事务持续时间。 **取值范围**： 不涉及。

        :return: The transaction_time_cost of this RealTimeSessionResult.
        :rtype: str
        """
        return self._transaction_time_cost

    @transaction_time_cost.setter
    def transaction_time_cost(self, transaction_time_cost):
        r"""Sets the transaction_time_cost of this RealTimeSessionResult.

        **参数解释**： 当前用户上一次执行的事务持续时间。 **取值范围**： 不涉及。

        :param transaction_time_cost: The transaction_time_cost of this RealTimeSessionResult.
        :type transaction_time_cost: str
        """
        self._transaction_time_cost = transaction_time_cost

    @property
    def trace_id(self):
        r"""Gets the trace_id of this RealTimeSessionResult.

        **参数解释**： 驱动传入的trace id，用于标识应用的一次请求。 **取值范围**： 不涉及。

        :return: The trace_id of this RealTimeSessionResult.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this RealTimeSessionResult.

        **参数解释**： 驱动传入的trace id，用于标识应用的一次请求。 **取值范围**： 不涉及。

        :param trace_id: The trace_id of this RealTimeSessionResult.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def global_session_id(self):
        r"""Gets the global_session_id of this RealTimeSessionResult.

        **参数解释**： 当前用户上次执行的全局会话ID。 **取值范围**： 不涉及。

        :return: The global_session_id of this RealTimeSessionResult.
        :rtype: str
        """
        return self._global_session_id

    @global_session_id.setter
    def global_session_id(self, global_session_id):
        r"""Sets the global_session_id of this RealTimeSessionResult.

        **参数解释**： 当前用户上次执行的全局会话ID。 **取值范围**： 不涉及。

        :param global_session_id: The global_session_id of this RealTimeSessionResult.
        :type global_session_id: str
        """
        self._global_session_id = global_session_id

    @property
    def top_transaction_id(self):
        r"""Gets the top_transaction_id of this RealTimeSessionResult.

        **参数解释**： 当前用户上次执行的顶层事务ID。 **取值范围**： 不涉及。

        :return: The top_transaction_id of this RealTimeSessionResult.
        :rtype: str
        """
        return self._top_transaction_id

    @top_transaction_id.setter
    def top_transaction_id(self, top_transaction_id):
        r"""Sets the top_transaction_id of this RealTimeSessionResult.

        **参数解释**： 当前用户上次执行的顶层事务ID。 **取值范围**： 不涉及。

        :param top_transaction_id: The top_transaction_id of this RealTimeSessionResult.
        :type top_transaction_id: str
        """
        self._top_transaction_id = top_transaction_id

    @property
    def current_transaction_id(self):
        r"""Gets the current_transaction_id of this RealTimeSessionResult.

        **参数解释**： 当前用户上次执行的事务ID。 **取值范围**： 不涉及。

        :return: The current_transaction_id of this RealTimeSessionResult.
        :rtype: str
        """
        return self._current_transaction_id

    @current_transaction_id.setter
    def current_transaction_id(self, current_transaction_id):
        r"""Sets the current_transaction_id of this RealTimeSessionResult.

        **参数解释**： 当前用户上次执行的事务ID。 **取值范围**： 不涉及。

        :param current_transaction_id: The current_transaction_id of this RealTimeSessionResult.
        :type current_transaction_id: str
        """
        self._current_transaction_id = current_transaction_id

    @property
    def xlog_quantity_pretty(self):
        r"""Gets the xlog_quantity_pretty of this RealTimeSessionResult.

        **参数解释**： 当前用户上次执行的事务使用的XLOG量，易读格式。 **取值范围**： 不涉及。

        :return: The xlog_quantity_pretty of this RealTimeSessionResult.
        :rtype: str
        """
        return self._xlog_quantity_pretty

    @xlog_quantity_pretty.setter
    def xlog_quantity_pretty(self, xlog_quantity_pretty):
        r"""Sets the xlog_quantity_pretty of this RealTimeSessionResult.

        **参数解释**： 当前用户上次执行的事务使用的XLOG量，易读格式。 **取值范围**： 不涉及。

        :param xlog_quantity_pretty: The xlog_quantity_pretty of this RealTimeSessionResult.
        :type xlog_quantity_pretty: str
        """
        self._xlog_quantity_pretty = xlog_quantity_pretty

    @property
    def wait_status(self):
        r"""Gets the wait_status of this RealTimeSessionResult.

        **参数解释**： 实例线程等待状态。 **取值范围**： 不涉及。

        :return: The wait_status of this RealTimeSessionResult.
        :rtype: str
        """
        return self._wait_status

    @wait_status.setter
    def wait_status(self, wait_status):
        r"""Sets the wait_status of this RealTimeSessionResult.

        **参数解释**： 实例线程等待状态。 **取值范围**： 不涉及。

        :param wait_status: The wait_status of this RealTimeSessionResult.
        :type wait_status: str
        """
        self._wait_status = wait_status

    @property
    def lwt_id(self):
        r"""Gets the lwt_id of this RealTimeSessionResult.

        **参数解释**： 实例线程的轻量级线程号。 **取值范围**： 不涉及。

        :return: The lwt_id of this RealTimeSessionResult.
        :rtype: str
        """
        return self._lwt_id

    @lwt_id.setter
    def lwt_id(self, lwt_id):
        r"""Sets the lwt_id of this RealTimeSessionResult.

        **参数解释**： 实例线程的轻量级线程号。 **取值范围**： 不涉及。

        :param lwt_id: The lwt_id of this RealTimeSessionResult.
        :type lwt_id: str
        """
        self._lwt_id = lwt_id

    @property
    def thread_name(self):
        r"""Gets the thread_name of this RealTimeSessionResult.

        **参数解释**： 实例线程名。 **取值范围**： 不涉及。

        :return: The thread_name of this RealTimeSessionResult.
        :rtype: str
        """
        return self._thread_name

    @thread_name.setter
    def thread_name(self, thread_name):
        r"""Sets the thread_name of this RealTimeSessionResult.

        **参数解释**： 实例线程名。 **取值范围**： 不涉及。

        :param thread_name: The thread_name of this RealTimeSessionResult.
        :type thread_name: str
        """
        self._thread_name = thread_name

    @property
    def lock_mode(self):
        r"""Gets the lock_mode of this RealTimeSessionResult.

        **参数解释**： 实例等锁模式。 **取值范围**： 不涉及。

        :return: The lock_mode of this RealTimeSessionResult.
        :rtype: str
        """
        return self._lock_mode

    @lock_mode.setter
    def lock_mode(self, lock_mode):
        r"""Sets the lock_mode of this RealTimeSessionResult.

        **参数解释**： 实例等锁模式。 **取值范围**： 不涉及。

        :param lock_mode: The lock_mode of this RealTimeSessionResult.
        :type lock_mode: str
        """
        self._lock_mode = lock_mode

    @property
    def parent_session_id(self):
        r"""Gets the parent_session_id of this RealTimeSessionResult.

        **参数解释**： 实例父会话ID。 **取值范围**： 不涉及。

        :return: The parent_session_id of this RealTimeSessionResult.
        :rtype: str
        """
        return self._parent_session_id

    @parent_session_id.setter
    def parent_session_id(self, parent_session_id):
        r"""Sets the parent_session_id of this RealTimeSessionResult.

        **参数解释**： 实例父会话ID。 **取值范围**： 不涉及。

        :param parent_session_id: The parent_session_id of this RealTimeSessionResult.
        :type parent_session_id: str
        """
        self._parent_session_id = parent_session_id

    @property
    def smp_id(self):
        r"""Gets the smp_id of this RealTimeSessionResult.

        **参数解释**： 实例并行线程的ID。 **取值范围**： 不涉及。

        :return: The smp_id of this RealTimeSessionResult.
        :rtype: str
        """
        return self._smp_id

    @smp_id.setter
    def smp_id(self, smp_id):
        r"""Sets the smp_id of this RealTimeSessionResult.

        **参数解释**： 实例并行线程的ID。 **取值范围**： 不涉及。

        :param smp_id: The smp_id of this RealTimeSessionResult.
        :type smp_id: str
        """
        self._smp_id = smp_id

    @property
    def lock_tag(self):
        r"""Gets the lock_tag of this RealTimeSessionResult.

        **参数解释**： 实例线程正等待获取的锁的信息。 **取值范围**： 不涉及。

        :return: The lock_tag of this RealTimeSessionResult.
        :rtype: str
        """
        return self._lock_tag

    @lock_tag.setter
    def lock_tag(self, lock_tag):
        r"""Sets the lock_tag of this RealTimeSessionResult.

        **参数解释**： 实例线程正等待获取的锁的信息。 **取值范围**： 不涉及。

        :param lock_tag: The lock_tag of this RealTimeSessionResult.
        :type lock_tag: str
        """
        self._lock_tag = lock_tag

    @property
    def component_name(self):
        r"""Gets the component_name of this RealTimeSessionResult.

        **参数解释**： 组件名称。 **取值范围**： 不涉及。

        :return: The component_name of this RealTimeSessionResult.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this RealTimeSessionResult.

        **参数解释**： 组件名称。 **取值范围**： 不涉及。

        :param component_name: The component_name of this RealTimeSessionResult.
        :type component_name: str
        """
        self._component_name = component_name

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
        if not isinstance(other, RealTimeSessionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
