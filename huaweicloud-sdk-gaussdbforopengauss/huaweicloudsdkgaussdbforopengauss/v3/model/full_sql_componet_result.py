# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullSqlComponetResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'db_name': 'str',
        'schema_name': 'str',
        'origin_node': 'str',
        'username': 'str',
        'application_name': 'str',
        'client_addr': 'str',
        'client_port': 'str',
        'parent_sql_id': 'str',
        'sql_id': 'str',
        'sql_exec_id': 'str',
        'transaction_id': 'str',
        'trace_id': 'str',
        'query': 'str',
        'thread_id': 'str',
        'session_id': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'slow_query_threshold': 'int',
        'n_soft_parse': 'int',
        'n_hard_parse': 'int',
        'query_plan': 'str',
        'n_return_rows': 'int',
        'n_tuples_fetched': 'int',
        'n_tuples_returned': 'int',
        'n_tuples_inserted': 'int',
        'n_tuples_updated': 'int',
        'n_tuples_deleted': 'int',
        'n_blocks_fetched': 'int',
        'n_blocks_hit': 'int',
        'db_time': 'int',
        'cpu_time': 'int',
        'execution_time': 'int',
        'parse_time': 'int',
        'plan_time': 'int',
        'rewrite_time': 'int',
        'pl_execution_time': 'int',
        'pl_compilation_time': 'int',
        'data_io_time': 'int',
        'lock_count': 'int',
        'lock_time': 'int',
        'lock_wait_count': 'int',
        'lock_wait_time': 'int',
        'details': 'str',
        'is_slow_sql': 'bool',
        'advise': 'str',
        'finish_status': 'str',
        'net_send_info': 'str',
        'net_recv_info': 'str',
        'net_stream_send_info': 'str',
        'net_stream_recv_info': 'str'
    }

    attribute_map = {
        'component_id': 'component_id',
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'origin_node': 'origin_node',
        'username': 'username',
        'application_name': 'application_name',
        'client_addr': 'client_addr',
        'client_port': 'client_port',
        'parent_sql_id': 'parent_sql_id',
        'sql_id': 'sql_id',
        'sql_exec_id': 'sql_exec_id',
        'transaction_id': 'transaction_id',
        'trace_id': 'trace_id',
        'query': 'query',
        'thread_id': 'thread_id',
        'session_id': 'session_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'slow_query_threshold': 'slow_query_threshold',
        'n_soft_parse': 'n_soft_parse',
        'n_hard_parse': 'n_hard_parse',
        'query_plan': 'query_plan',
        'n_return_rows': 'n_return_rows',
        'n_tuples_fetched': 'n_tuples_fetched',
        'n_tuples_returned': 'n_tuples_returned',
        'n_tuples_inserted': 'n_tuples_inserted',
        'n_tuples_updated': 'n_tuples_updated',
        'n_tuples_deleted': 'n_tuples_deleted',
        'n_blocks_fetched': 'n_blocks_fetched',
        'n_blocks_hit': 'n_blocks_hit',
        'db_time': 'db_time',
        'cpu_time': 'cpu_time',
        'execution_time': 'execution_time',
        'parse_time': 'parse_time',
        'plan_time': 'plan_time',
        'rewrite_time': 'rewrite_time',
        'pl_execution_time': 'pl_execution_time',
        'pl_compilation_time': 'pl_compilation_time',
        'data_io_time': 'data_io_time',
        'lock_count': 'lock_count',
        'lock_time': 'lock_time',
        'lock_wait_count': 'lock_wait_count',
        'lock_wait_time': 'lock_wait_time',
        'details': 'details',
        'is_slow_sql': 'is_slow_sql',
        'advise': 'advise',
        'finish_status': 'finish_status',
        'net_send_info': 'net_send_info',
        'net_recv_info': 'net_recv_info',
        'net_stream_send_info': 'net_stream_send_info',
        'net_stream_recv_info': 'net_stream_recv_info'
    }

    def __init__(self, component_id=None, db_name=None, schema_name=None, origin_node=None, username=None, application_name=None, client_addr=None, client_port=None, parent_sql_id=None, sql_id=None, sql_exec_id=None, transaction_id=None, trace_id=None, query=None, thread_id=None, session_id=None, begin_time=None, end_time=None, slow_query_threshold=None, n_soft_parse=None, n_hard_parse=None, query_plan=None, n_return_rows=None, n_tuples_fetched=None, n_tuples_returned=None, n_tuples_inserted=None, n_tuples_updated=None, n_tuples_deleted=None, n_blocks_fetched=None, n_blocks_hit=None, db_time=None, cpu_time=None, execution_time=None, parse_time=None, plan_time=None, rewrite_time=None, pl_execution_time=None, pl_compilation_time=None, data_io_time=None, lock_count=None, lock_time=None, lock_wait_count=None, lock_wait_time=None, details=None, is_slow_sql=None, advise=None, finish_status=None, net_send_info=None, net_recv_info=None, net_stream_send_info=None, net_stream_recv_info=None):
        r"""FullSqlComponetResult

        The model defined in huaweicloud sdk

        :param component_id: **参数解释**: 组件ID。 **取值范围**: 不涉及。
        :type component_id: str
        :param db_name: **参数解释**: 数据库名称。 **取值范围**: 不涉及。
        :type db_name: str
        :param schema_name: **参数解释**: schema名称。 **取值范围**: 不涉及。
        :type schema_name: str
        :param origin_node: **参数解释**: 原始节点。 **取值范围**: 不涉及。
        :type origin_node: str
        :param username: **参数解释**: 用户名。 **取值范围**: 不涉及。
        :type username: str
        :param application_name: **参数解释**: 用户发起的请求的应用程序名称。 **取值范围**: 不涉及。
        :type application_name: str
        :param client_addr: **参数解释**: 用户发起的请求的客户端地址。 **取值范围**: 不涉及。
        :type client_addr: str
        :param client_port: **参数解释**: 用户发起请求的客户端端口。 **取值范围**: 不涉及。
        :type client_port: str
        :param parent_sql_id: **参数解释**: 当前语句的外层SQL的归一化SQL ID。 **取值范围**: 不涉及。
        :type parent_sql_id: str
        :param sql_id: **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **取值范围**: 不涉及。
        :type sql_id: str
        :param sql_exec_id: **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **取值范围**: 不涉及。
        :type sql_exec_id: str
        :param transaction_id: **参数解释**: 事务ID，对应内核字段：debug_query_id。 **取值范围**: 不涉及。
        :type transaction_id: str
        :param trace_id: **参数解释**: 链路ID。 **取值范围**: 不涉及。
        :type trace_id: str
        :param query: **参数解释**: 归一化SQL。 **取值范围**: 不涉及。
        :type query: str
        :param thread_id: **参数解释**: 线程ID。 **取值范围**: 不涉及。
        :type thread_id: str
        :param session_id: **参数解释**: 会话ID。 **取值范围**: 不涉及。
        :type session_id: str
        :param begin_time: **参数解释**: 开始时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。
        :type begin_time: str
        :param end_time: **参数解释**: 结束时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。
        :type end_time: str
        :param slow_query_threshold: **参数解释**: 慢SQL阈值。 **取值范围**: 不涉及。
        :type slow_query_threshold: int
        :param n_soft_parse: **参数解释**: 软解析次数。 **取值范围**: 不涉及。
        :type n_soft_parse: int
        :param n_hard_parse: **参数解释**: 硬解析次数。 **取值范围**: 不涉及。
        :type n_hard_parse: int
        :param query_plan: **参数解释**: 执行计划。 **取值范围**: 不涉及。
        :type query_plan: str
        :param n_return_rows: **参数解释**: SELECT语句的返回结果集行数。 **取值范围**: 不涉及。
        :type n_return_rows: int
        :param n_tuples_fetched: **参数解释**: 随机扫描行。 **取值范围**: 不涉及。
        :type n_tuples_fetched: int
        :param n_tuples_returned: **参数解释**: 顺序扫描行。 **取值范围**: 不涉及。
        :type n_tuples_returned: int
        :param n_tuples_inserted: **参数解释**: 插入行。 **取值范围**: 不涉及。
        :type n_tuples_inserted: int
        :param n_tuples_updated: **参数解释**: 更新行。 **取值范围**: 不涉及。
        :type n_tuples_updated: int
        :param n_tuples_deleted: **参数解释**: 删除行。 **取值范围**: 不涉及。
        :type n_tuples_deleted: int
        :param n_blocks_fetched: **参数解释**: buffer的块访问次数。 **取值范围**: 不涉及。\&quot;\&quot;
        :type n_blocks_fetched: int
        :param n_blocks_hit: **参数解释**: buffer的块命中次数。 **取值范围**: 不涉及。
        :type n_blocks_hit: int
        :param db_time: **参数解释**: 有效DB时间花费。 **取值范围**: 不涉及。
        :type db_time: int
        :param cpu_time: **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。
        :type cpu_time: int
        :param execution_time: **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。
        :type execution_time: int
        :param parse_time: **参数解释**: SQL解析时间（单位：微秒）。 **取值范围**: 不涉及。
        :type parse_time: int
        :param plan_time: **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。
        :type plan_time: int
        :param rewrite_time: **参数解释**: SQL重写时间（单位：微秒）。 **取值范围**: 不涉及。
        :type rewrite_time: int
        :param pl_execution_time: **参数解释**: plpgsql上的执行时间（单位：微秒）。 **取值范围**: 不涉及。
        :type pl_execution_time: int
        :param pl_compilation_time: **参数解释**: plpgsql上的编译时间（单位：微秒）。 **取值范围**: 不涉及。
        :type pl_compilation_time: int
        :param data_io_time: **参数解释**: IO时间（单位：微秒）。 **取值范围**: 不涉及。
        :type data_io_time: int
        :param lock_count: **参数解释**: 加锁次数。 **取值范围**: 不涉及。
        :type lock_count: int
        :param lock_time: **参数解释**: 加锁耗时。 **取值范围**: 不涉及。
        :type lock_time: int
        :param lock_wait_count: **参数解释**: 加锁等待次数。 **取值范围**: 不涉及。
        :type lock_wait_count: int
        :param lock_wait_time: **参数解释**: 加锁等待时间。 **取值范围**: 不涉及。
        :type lock_wait_time: int
        :param details: **参数解释**: 详细列表。 **取值范围**: 不涉及。
        :type details: str
        :param is_slow_sql: **参数解释**: 是否慢SQL。 **取值范围**: 不涉及。
        :type is_slow_sql: bool
        :param advise: **参数解释**: 可能导致该SQL为慢SQL的风险信息。 **取值范围**: 不涉及。
        :type advise: str
        :param finish_status: **参数解释**: 语句完成状态。 **取值范围**: 不涉及。
        :type finish_status: str
        :param net_send_info: **参数解释**: 通过物理连接发送消息的网络状态。 **取值范围**: 不涉及。
        :type net_send_info: str
        :param net_recv_info: **参数解释**: 通过物理连接接收消息的网络状态。 **取值范围**: 不涉及。
        :type net_recv_info: str
        :param net_stream_send_info: **参数解释**: 通过逻辑连接发送消息的网络状态。 **取值范围**: 不涉及。
        :type net_stream_send_info: str
        :param net_stream_recv_info: **参数解释**: 通过逻辑连接接收消息的网络状态。 **取值范围**: 不涉及。
        :type net_stream_recv_info: str
        """
        
        

        self._component_id = None
        self._db_name = None
        self._schema_name = None
        self._origin_node = None
        self._username = None
        self._application_name = None
        self._client_addr = None
        self._client_port = None
        self._parent_sql_id = None
        self._sql_id = None
        self._sql_exec_id = None
        self._transaction_id = None
        self._trace_id = None
        self._query = None
        self._thread_id = None
        self._session_id = None
        self._begin_time = None
        self._end_time = None
        self._slow_query_threshold = None
        self._n_soft_parse = None
        self._n_hard_parse = None
        self._query_plan = None
        self._n_return_rows = None
        self._n_tuples_fetched = None
        self._n_tuples_returned = None
        self._n_tuples_inserted = None
        self._n_tuples_updated = None
        self._n_tuples_deleted = None
        self._n_blocks_fetched = None
        self._n_blocks_hit = None
        self._db_time = None
        self._cpu_time = None
        self._execution_time = None
        self._parse_time = None
        self._plan_time = None
        self._rewrite_time = None
        self._pl_execution_time = None
        self._pl_compilation_time = None
        self._data_io_time = None
        self._lock_count = None
        self._lock_time = None
        self._lock_wait_count = None
        self._lock_wait_time = None
        self._details = None
        self._is_slow_sql = None
        self._advise = None
        self._finish_status = None
        self._net_send_info = None
        self._net_recv_info = None
        self._net_stream_send_info = None
        self._net_stream_recv_info = None
        self.discriminator = None

        if component_id is not None:
            self.component_id = component_id
        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if origin_node is not None:
            self.origin_node = origin_node
        if username is not None:
            self.username = username
        if application_name is not None:
            self.application_name = application_name
        if client_addr is not None:
            self.client_addr = client_addr
        if client_port is not None:
            self.client_port = client_port
        if parent_sql_id is not None:
            self.parent_sql_id = parent_sql_id
        if sql_id is not None:
            self.sql_id = sql_id
        if sql_exec_id is not None:
            self.sql_exec_id = sql_exec_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if trace_id is not None:
            self.trace_id = trace_id
        if query is not None:
            self.query = query
        if thread_id is not None:
            self.thread_id = thread_id
        if session_id is not None:
            self.session_id = session_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if slow_query_threshold is not None:
            self.slow_query_threshold = slow_query_threshold
        if n_soft_parse is not None:
            self.n_soft_parse = n_soft_parse
        if n_hard_parse is not None:
            self.n_hard_parse = n_hard_parse
        if query_plan is not None:
            self.query_plan = query_plan
        if n_return_rows is not None:
            self.n_return_rows = n_return_rows
        if n_tuples_fetched is not None:
            self.n_tuples_fetched = n_tuples_fetched
        if n_tuples_returned is not None:
            self.n_tuples_returned = n_tuples_returned
        if n_tuples_inserted is not None:
            self.n_tuples_inserted = n_tuples_inserted
        if n_tuples_updated is not None:
            self.n_tuples_updated = n_tuples_updated
        if n_tuples_deleted is not None:
            self.n_tuples_deleted = n_tuples_deleted
        if n_blocks_fetched is not None:
            self.n_blocks_fetched = n_blocks_fetched
        if n_blocks_hit is not None:
            self.n_blocks_hit = n_blocks_hit
        if db_time is not None:
            self.db_time = db_time
        if cpu_time is not None:
            self.cpu_time = cpu_time
        if execution_time is not None:
            self.execution_time = execution_time
        if parse_time is not None:
            self.parse_time = parse_time
        if plan_time is not None:
            self.plan_time = plan_time
        if rewrite_time is not None:
            self.rewrite_time = rewrite_time
        if pl_execution_time is not None:
            self.pl_execution_time = pl_execution_time
        if pl_compilation_time is not None:
            self.pl_compilation_time = pl_compilation_time
        if data_io_time is not None:
            self.data_io_time = data_io_time
        if lock_count is not None:
            self.lock_count = lock_count
        if lock_time is not None:
            self.lock_time = lock_time
        if lock_wait_count is not None:
            self.lock_wait_count = lock_wait_count
        if lock_wait_time is not None:
            self.lock_wait_time = lock_wait_time
        if details is not None:
            self.details = details
        if is_slow_sql is not None:
            self.is_slow_sql = is_slow_sql
        if advise is not None:
            self.advise = advise
        if finish_status is not None:
            self.finish_status = finish_status
        if net_send_info is not None:
            self.net_send_info = net_send_info
        if net_recv_info is not None:
            self.net_recv_info = net_recv_info
        if net_stream_send_info is not None:
            self.net_stream_send_info = net_stream_send_info
        if net_stream_recv_info is not None:
            self.net_stream_recv_info = net_stream_recv_info

    @property
    def component_id(self):
        r"""Gets the component_id of this FullSqlComponetResult.

        **参数解释**: 组件ID。 **取值范围**: 不涉及。

        :return: The component_id of this FullSqlComponetResult.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this FullSqlComponetResult.

        **参数解释**: 组件ID。 **取值范围**: 不涉及。

        :param component_id: The component_id of this FullSqlComponetResult.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def db_name(self):
        r"""Gets the db_name of this FullSqlComponetResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :return: The db_name of this FullSqlComponetResult.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this FullSqlComponetResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :param db_name: The db_name of this FullSqlComponetResult.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this FullSqlComponetResult.

        **参数解释**: schema名称。 **取值范围**: 不涉及。

        :return: The schema_name of this FullSqlComponetResult.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this FullSqlComponetResult.

        **参数解释**: schema名称。 **取值范围**: 不涉及。

        :param schema_name: The schema_name of this FullSqlComponetResult.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def origin_node(self):
        r"""Gets the origin_node of this FullSqlComponetResult.

        **参数解释**: 原始节点。 **取值范围**: 不涉及。

        :return: The origin_node of this FullSqlComponetResult.
        :rtype: str
        """
        return self._origin_node

    @origin_node.setter
    def origin_node(self, origin_node):
        r"""Sets the origin_node of this FullSqlComponetResult.

        **参数解释**: 原始节点。 **取值范围**: 不涉及。

        :param origin_node: The origin_node of this FullSqlComponetResult.
        :type origin_node: str
        """
        self._origin_node = origin_node

    @property
    def username(self):
        r"""Gets the username of this FullSqlComponetResult.

        **参数解释**: 用户名。 **取值范围**: 不涉及。

        :return: The username of this FullSqlComponetResult.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this FullSqlComponetResult.

        **参数解释**: 用户名。 **取值范围**: 不涉及。

        :param username: The username of this FullSqlComponetResult.
        :type username: str
        """
        self._username = username

    @property
    def application_name(self):
        r"""Gets the application_name of this FullSqlComponetResult.

        **参数解释**: 用户发起的请求的应用程序名称。 **取值范围**: 不涉及。

        :return: The application_name of this FullSqlComponetResult.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this FullSqlComponetResult.

        **参数解释**: 用户发起的请求的应用程序名称。 **取值范围**: 不涉及。

        :param application_name: The application_name of this FullSqlComponetResult.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def client_addr(self):
        r"""Gets the client_addr of this FullSqlComponetResult.

        **参数解释**: 用户发起的请求的客户端地址。 **取值范围**: 不涉及。

        :return: The client_addr of this FullSqlComponetResult.
        :rtype: str
        """
        return self._client_addr

    @client_addr.setter
    def client_addr(self, client_addr):
        r"""Sets the client_addr of this FullSqlComponetResult.

        **参数解释**: 用户发起的请求的客户端地址。 **取值范围**: 不涉及。

        :param client_addr: The client_addr of this FullSqlComponetResult.
        :type client_addr: str
        """
        self._client_addr = client_addr

    @property
    def client_port(self):
        r"""Gets the client_port of this FullSqlComponetResult.

        **参数解释**: 用户发起请求的客户端端口。 **取值范围**: 不涉及。

        :return: The client_port of this FullSqlComponetResult.
        :rtype: str
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this FullSqlComponetResult.

        **参数解释**: 用户发起请求的客户端端口。 **取值范围**: 不涉及。

        :param client_port: The client_port of this FullSqlComponetResult.
        :type client_port: str
        """
        self._client_port = client_port

    @property
    def parent_sql_id(self):
        r"""Gets the parent_sql_id of this FullSqlComponetResult.

        **参数解释**: 当前语句的外层SQL的归一化SQL ID。 **取值范围**: 不涉及。

        :return: The parent_sql_id of this FullSqlComponetResult.
        :rtype: str
        """
        return self._parent_sql_id

    @parent_sql_id.setter
    def parent_sql_id(self, parent_sql_id):
        r"""Sets the parent_sql_id of this FullSqlComponetResult.

        **参数解释**: 当前语句的外层SQL的归一化SQL ID。 **取值范围**: 不涉及。

        :param parent_sql_id: The parent_sql_id of this FullSqlComponetResult.
        :type parent_sql_id: str
        """
        self._parent_sql_id = parent_sql_id

    @property
    def sql_id(self):
        r"""Gets the sql_id of this FullSqlComponetResult.

        **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **取值范围**: 不涉及。

        :return: The sql_id of this FullSqlComponetResult.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this FullSqlComponetResult.

        **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **取值范围**: 不涉及。

        :param sql_id: The sql_id of this FullSqlComponetResult.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def sql_exec_id(self):
        r"""Gets the sql_exec_id of this FullSqlComponetResult.

        **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **取值范围**: 不涉及。

        :return: The sql_exec_id of this FullSqlComponetResult.
        :rtype: str
        """
        return self._sql_exec_id

    @sql_exec_id.setter
    def sql_exec_id(self, sql_exec_id):
        r"""Sets the sql_exec_id of this FullSqlComponetResult.

        **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **取值范围**: 不涉及。

        :param sql_exec_id: The sql_exec_id of this FullSqlComponetResult.
        :type sql_exec_id: str
        """
        self._sql_exec_id = sql_exec_id

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this FullSqlComponetResult.

        **参数解释**: 事务ID，对应内核字段：debug_query_id。 **取值范围**: 不涉及。

        :return: The transaction_id of this FullSqlComponetResult.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this FullSqlComponetResult.

        **参数解释**: 事务ID，对应内核字段：debug_query_id。 **取值范围**: 不涉及。

        :param transaction_id: The transaction_id of this FullSqlComponetResult.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def trace_id(self):
        r"""Gets the trace_id of this FullSqlComponetResult.

        **参数解释**: 链路ID。 **取值范围**: 不涉及。

        :return: The trace_id of this FullSqlComponetResult.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this FullSqlComponetResult.

        **参数解释**: 链路ID。 **取值范围**: 不涉及。

        :param trace_id: The trace_id of this FullSqlComponetResult.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def query(self):
        r"""Gets the query of this FullSqlComponetResult.

        **参数解释**: 归一化SQL。 **取值范围**: 不涉及。

        :return: The query of this FullSqlComponetResult.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this FullSqlComponetResult.

        **参数解释**: 归一化SQL。 **取值范围**: 不涉及。

        :param query: The query of this FullSqlComponetResult.
        :type query: str
        """
        self._query = query

    @property
    def thread_id(self):
        r"""Gets the thread_id of this FullSqlComponetResult.

        **参数解释**: 线程ID。 **取值范围**: 不涉及。

        :return: The thread_id of this FullSqlComponetResult.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        r"""Sets the thread_id of this FullSqlComponetResult.

        **参数解释**: 线程ID。 **取值范围**: 不涉及。

        :param thread_id: The thread_id of this FullSqlComponetResult.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def session_id(self):
        r"""Gets the session_id of this FullSqlComponetResult.

        **参数解释**: 会话ID。 **取值范围**: 不涉及。

        :return: The session_id of this FullSqlComponetResult.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this FullSqlComponetResult.

        **参数解释**: 会话ID。 **取值范围**: 不涉及。

        :param session_id: The session_id of this FullSqlComponetResult.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this FullSqlComponetResult.

        **参数解释**: 开始时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。

        :return: The begin_time of this FullSqlComponetResult.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this FullSqlComponetResult.

        **参数解释**: 开始时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。

        :param begin_time: The begin_time of this FullSqlComponetResult.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this FullSqlComponetResult.

        **参数解释**: 结束时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。

        :return: The end_time of this FullSqlComponetResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this FullSqlComponetResult.

        **参数解释**: 结束时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。

        :param end_time: The end_time of this FullSqlComponetResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def slow_query_threshold(self):
        r"""Gets the slow_query_threshold of this FullSqlComponetResult.

        **参数解释**: 慢SQL阈值。 **取值范围**: 不涉及。

        :return: The slow_query_threshold of this FullSqlComponetResult.
        :rtype: int
        """
        return self._slow_query_threshold

    @slow_query_threshold.setter
    def slow_query_threshold(self, slow_query_threshold):
        r"""Sets the slow_query_threshold of this FullSqlComponetResult.

        **参数解释**: 慢SQL阈值。 **取值范围**: 不涉及。

        :param slow_query_threshold: The slow_query_threshold of this FullSqlComponetResult.
        :type slow_query_threshold: int
        """
        self._slow_query_threshold = slow_query_threshold

    @property
    def n_soft_parse(self):
        r"""Gets the n_soft_parse of this FullSqlComponetResult.

        **参数解释**: 软解析次数。 **取值范围**: 不涉及。

        :return: The n_soft_parse of this FullSqlComponetResult.
        :rtype: int
        """
        return self._n_soft_parse

    @n_soft_parse.setter
    def n_soft_parse(self, n_soft_parse):
        r"""Sets the n_soft_parse of this FullSqlComponetResult.

        **参数解释**: 软解析次数。 **取值范围**: 不涉及。

        :param n_soft_parse: The n_soft_parse of this FullSqlComponetResult.
        :type n_soft_parse: int
        """
        self._n_soft_parse = n_soft_parse

    @property
    def n_hard_parse(self):
        r"""Gets the n_hard_parse of this FullSqlComponetResult.

        **参数解释**: 硬解析次数。 **取值范围**: 不涉及。

        :return: The n_hard_parse of this FullSqlComponetResult.
        :rtype: int
        """
        return self._n_hard_parse

    @n_hard_parse.setter
    def n_hard_parse(self, n_hard_parse):
        r"""Sets the n_hard_parse of this FullSqlComponetResult.

        **参数解释**: 硬解析次数。 **取值范围**: 不涉及。

        :param n_hard_parse: The n_hard_parse of this FullSqlComponetResult.
        :type n_hard_parse: int
        """
        self._n_hard_parse = n_hard_parse

    @property
    def query_plan(self):
        r"""Gets the query_plan of this FullSqlComponetResult.

        **参数解释**: 执行计划。 **取值范围**: 不涉及。

        :return: The query_plan of this FullSqlComponetResult.
        :rtype: str
        """
        return self._query_plan

    @query_plan.setter
    def query_plan(self, query_plan):
        r"""Sets the query_plan of this FullSqlComponetResult.

        **参数解释**: 执行计划。 **取值范围**: 不涉及。

        :param query_plan: The query_plan of this FullSqlComponetResult.
        :type query_plan: str
        """
        self._query_plan = query_plan

    @property
    def n_return_rows(self):
        r"""Gets the n_return_rows of this FullSqlComponetResult.

        **参数解释**: SELECT语句的返回结果集行数。 **取值范围**: 不涉及。

        :return: The n_return_rows of this FullSqlComponetResult.
        :rtype: int
        """
        return self._n_return_rows

    @n_return_rows.setter
    def n_return_rows(self, n_return_rows):
        r"""Sets the n_return_rows of this FullSqlComponetResult.

        **参数解释**: SELECT语句的返回结果集行数。 **取值范围**: 不涉及。

        :param n_return_rows: The n_return_rows of this FullSqlComponetResult.
        :type n_return_rows: int
        """
        self._n_return_rows = n_return_rows

    @property
    def n_tuples_fetched(self):
        r"""Gets the n_tuples_fetched of this FullSqlComponetResult.

        **参数解释**: 随机扫描行。 **取值范围**: 不涉及。

        :return: The n_tuples_fetched of this FullSqlComponetResult.
        :rtype: int
        """
        return self._n_tuples_fetched

    @n_tuples_fetched.setter
    def n_tuples_fetched(self, n_tuples_fetched):
        r"""Sets the n_tuples_fetched of this FullSqlComponetResult.

        **参数解释**: 随机扫描行。 **取值范围**: 不涉及。

        :param n_tuples_fetched: The n_tuples_fetched of this FullSqlComponetResult.
        :type n_tuples_fetched: int
        """
        self._n_tuples_fetched = n_tuples_fetched

    @property
    def n_tuples_returned(self):
        r"""Gets the n_tuples_returned of this FullSqlComponetResult.

        **参数解释**: 顺序扫描行。 **取值范围**: 不涉及。

        :return: The n_tuples_returned of this FullSqlComponetResult.
        :rtype: int
        """
        return self._n_tuples_returned

    @n_tuples_returned.setter
    def n_tuples_returned(self, n_tuples_returned):
        r"""Sets the n_tuples_returned of this FullSqlComponetResult.

        **参数解释**: 顺序扫描行。 **取值范围**: 不涉及。

        :param n_tuples_returned: The n_tuples_returned of this FullSqlComponetResult.
        :type n_tuples_returned: int
        """
        self._n_tuples_returned = n_tuples_returned

    @property
    def n_tuples_inserted(self):
        r"""Gets the n_tuples_inserted of this FullSqlComponetResult.

        **参数解释**: 插入行。 **取值范围**: 不涉及。

        :return: The n_tuples_inserted of this FullSqlComponetResult.
        :rtype: int
        """
        return self._n_tuples_inserted

    @n_tuples_inserted.setter
    def n_tuples_inserted(self, n_tuples_inserted):
        r"""Sets the n_tuples_inserted of this FullSqlComponetResult.

        **参数解释**: 插入行。 **取值范围**: 不涉及。

        :param n_tuples_inserted: The n_tuples_inserted of this FullSqlComponetResult.
        :type n_tuples_inserted: int
        """
        self._n_tuples_inserted = n_tuples_inserted

    @property
    def n_tuples_updated(self):
        r"""Gets the n_tuples_updated of this FullSqlComponetResult.

        **参数解释**: 更新行。 **取值范围**: 不涉及。

        :return: The n_tuples_updated of this FullSqlComponetResult.
        :rtype: int
        """
        return self._n_tuples_updated

    @n_tuples_updated.setter
    def n_tuples_updated(self, n_tuples_updated):
        r"""Sets the n_tuples_updated of this FullSqlComponetResult.

        **参数解释**: 更新行。 **取值范围**: 不涉及。

        :param n_tuples_updated: The n_tuples_updated of this FullSqlComponetResult.
        :type n_tuples_updated: int
        """
        self._n_tuples_updated = n_tuples_updated

    @property
    def n_tuples_deleted(self):
        r"""Gets the n_tuples_deleted of this FullSqlComponetResult.

        **参数解释**: 删除行。 **取值范围**: 不涉及。

        :return: The n_tuples_deleted of this FullSqlComponetResult.
        :rtype: int
        """
        return self._n_tuples_deleted

    @n_tuples_deleted.setter
    def n_tuples_deleted(self, n_tuples_deleted):
        r"""Sets the n_tuples_deleted of this FullSqlComponetResult.

        **参数解释**: 删除行。 **取值范围**: 不涉及。

        :param n_tuples_deleted: The n_tuples_deleted of this FullSqlComponetResult.
        :type n_tuples_deleted: int
        """
        self._n_tuples_deleted = n_tuples_deleted

    @property
    def n_blocks_fetched(self):
        r"""Gets the n_blocks_fetched of this FullSqlComponetResult.

        **参数解释**: buffer的块访问次数。 **取值范围**: 不涉及。\"\"

        :return: The n_blocks_fetched of this FullSqlComponetResult.
        :rtype: int
        """
        return self._n_blocks_fetched

    @n_blocks_fetched.setter
    def n_blocks_fetched(self, n_blocks_fetched):
        r"""Sets the n_blocks_fetched of this FullSqlComponetResult.

        **参数解释**: buffer的块访问次数。 **取值范围**: 不涉及。\"\"

        :param n_blocks_fetched: The n_blocks_fetched of this FullSqlComponetResult.
        :type n_blocks_fetched: int
        """
        self._n_blocks_fetched = n_blocks_fetched

    @property
    def n_blocks_hit(self):
        r"""Gets the n_blocks_hit of this FullSqlComponetResult.

        **参数解释**: buffer的块命中次数。 **取值范围**: 不涉及。

        :return: The n_blocks_hit of this FullSqlComponetResult.
        :rtype: int
        """
        return self._n_blocks_hit

    @n_blocks_hit.setter
    def n_blocks_hit(self, n_blocks_hit):
        r"""Sets the n_blocks_hit of this FullSqlComponetResult.

        **参数解释**: buffer的块命中次数。 **取值范围**: 不涉及。

        :param n_blocks_hit: The n_blocks_hit of this FullSqlComponetResult.
        :type n_blocks_hit: int
        """
        self._n_blocks_hit = n_blocks_hit

    @property
    def db_time(self):
        r"""Gets the db_time of this FullSqlComponetResult.

        **参数解释**: 有效DB时间花费。 **取值范围**: 不涉及。

        :return: The db_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._db_time

    @db_time.setter
    def db_time(self, db_time):
        r"""Sets the db_time of this FullSqlComponetResult.

        **参数解释**: 有效DB时间花费。 **取值范围**: 不涉及。

        :param db_time: The db_time of this FullSqlComponetResult.
        :type db_time: int
        """
        self._db_time = db_time

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this FullSqlComponetResult.

        **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The cpu_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this FullSqlComponetResult.

        **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。

        :param cpu_time: The cpu_time of this FullSqlComponetResult.
        :type cpu_time: int
        """
        self._cpu_time = cpu_time

    @property
    def execution_time(self):
        r"""Gets the execution_time of this FullSqlComponetResult.

        **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The execution_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        r"""Sets the execution_time of this FullSqlComponetResult.

        **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :param execution_time: The execution_time of this FullSqlComponetResult.
        :type execution_time: int
        """
        self._execution_time = execution_time

    @property
    def parse_time(self):
        r"""Gets the parse_time of this FullSqlComponetResult.

        **参数解释**: SQL解析时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The parse_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._parse_time

    @parse_time.setter
    def parse_time(self, parse_time):
        r"""Sets the parse_time of this FullSqlComponetResult.

        **参数解释**: SQL解析时间（单位：微秒）。 **取值范围**: 不涉及。

        :param parse_time: The parse_time of this FullSqlComponetResult.
        :type parse_time: int
        """
        self._parse_time = parse_time

    @property
    def plan_time(self):
        r"""Gets the plan_time of this FullSqlComponetResult.

        **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The plan_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        r"""Sets the plan_time of this FullSqlComponetResult.

        **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :param plan_time: The plan_time of this FullSqlComponetResult.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def rewrite_time(self):
        r"""Gets the rewrite_time of this FullSqlComponetResult.

        **参数解释**: SQL重写时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The rewrite_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._rewrite_time

    @rewrite_time.setter
    def rewrite_time(self, rewrite_time):
        r"""Sets the rewrite_time of this FullSqlComponetResult.

        **参数解释**: SQL重写时间（单位：微秒）。 **取值范围**: 不涉及。

        :param rewrite_time: The rewrite_time of this FullSqlComponetResult.
        :type rewrite_time: int
        """
        self._rewrite_time = rewrite_time

    @property
    def pl_execution_time(self):
        r"""Gets the pl_execution_time of this FullSqlComponetResult.

        **参数解释**: plpgsql上的执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The pl_execution_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._pl_execution_time

    @pl_execution_time.setter
    def pl_execution_time(self, pl_execution_time):
        r"""Sets the pl_execution_time of this FullSqlComponetResult.

        **参数解释**: plpgsql上的执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :param pl_execution_time: The pl_execution_time of this FullSqlComponetResult.
        :type pl_execution_time: int
        """
        self._pl_execution_time = pl_execution_time

    @property
    def pl_compilation_time(self):
        r"""Gets the pl_compilation_time of this FullSqlComponetResult.

        **参数解释**: plpgsql上的编译时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The pl_compilation_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._pl_compilation_time

    @pl_compilation_time.setter
    def pl_compilation_time(self, pl_compilation_time):
        r"""Sets the pl_compilation_time of this FullSqlComponetResult.

        **参数解释**: plpgsql上的编译时间（单位：微秒）。 **取值范围**: 不涉及。

        :param pl_compilation_time: The pl_compilation_time of this FullSqlComponetResult.
        :type pl_compilation_time: int
        """
        self._pl_compilation_time = pl_compilation_time

    @property
    def data_io_time(self):
        r"""Gets the data_io_time of this FullSqlComponetResult.

        **参数解释**: IO时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The data_io_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._data_io_time

    @data_io_time.setter
    def data_io_time(self, data_io_time):
        r"""Sets the data_io_time of this FullSqlComponetResult.

        **参数解释**: IO时间（单位：微秒）。 **取值范围**: 不涉及。

        :param data_io_time: The data_io_time of this FullSqlComponetResult.
        :type data_io_time: int
        """
        self._data_io_time = data_io_time

    @property
    def lock_count(self):
        r"""Gets the lock_count of this FullSqlComponetResult.

        **参数解释**: 加锁次数。 **取值范围**: 不涉及。

        :return: The lock_count of this FullSqlComponetResult.
        :rtype: int
        """
        return self._lock_count

    @lock_count.setter
    def lock_count(self, lock_count):
        r"""Sets the lock_count of this FullSqlComponetResult.

        **参数解释**: 加锁次数。 **取值范围**: 不涉及。

        :param lock_count: The lock_count of this FullSqlComponetResult.
        :type lock_count: int
        """
        self._lock_count = lock_count

    @property
    def lock_time(self):
        r"""Gets the lock_time of this FullSqlComponetResult.

        **参数解释**: 加锁耗时。 **取值范围**: 不涉及。

        :return: The lock_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this FullSqlComponetResult.

        **参数解释**: 加锁耗时。 **取值范围**: 不涉及。

        :param lock_time: The lock_time of this FullSqlComponetResult.
        :type lock_time: int
        """
        self._lock_time = lock_time

    @property
    def lock_wait_count(self):
        r"""Gets the lock_wait_count of this FullSqlComponetResult.

        **参数解释**: 加锁等待次数。 **取值范围**: 不涉及。

        :return: The lock_wait_count of this FullSqlComponetResult.
        :rtype: int
        """
        return self._lock_wait_count

    @lock_wait_count.setter
    def lock_wait_count(self, lock_wait_count):
        r"""Sets the lock_wait_count of this FullSqlComponetResult.

        **参数解释**: 加锁等待次数。 **取值范围**: 不涉及。

        :param lock_wait_count: The lock_wait_count of this FullSqlComponetResult.
        :type lock_wait_count: int
        """
        self._lock_wait_count = lock_wait_count

    @property
    def lock_wait_time(self):
        r"""Gets the lock_wait_time of this FullSqlComponetResult.

        **参数解释**: 加锁等待时间。 **取值范围**: 不涉及。

        :return: The lock_wait_time of this FullSqlComponetResult.
        :rtype: int
        """
        return self._lock_wait_time

    @lock_wait_time.setter
    def lock_wait_time(self, lock_wait_time):
        r"""Sets the lock_wait_time of this FullSqlComponetResult.

        **参数解释**: 加锁等待时间。 **取值范围**: 不涉及。

        :param lock_wait_time: The lock_wait_time of this FullSqlComponetResult.
        :type lock_wait_time: int
        """
        self._lock_wait_time = lock_wait_time

    @property
    def details(self):
        r"""Gets the details of this FullSqlComponetResult.

        **参数解释**: 详细列表。 **取值范围**: 不涉及。

        :return: The details of this FullSqlComponetResult.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        r"""Sets the details of this FullSqlComponetResult.

        **参数解释**: 详细列表。 **取值范围**: 不涉及。

        :param details: The details of this FullSqlComponetResult.
        :type details: str
        """
        self._details = details

    @property
    def is_slow_sql(self):
        r"""Gets the is_slow_sql of this FullSqlComponetResult.

        **参数解释**: 是否慢SQL。 **取值范围**: 不涉及。

        :return: The is_slow_sql of this FullSqlComponetResult.
        :rtype: bool
        """
        return self._is_slow_sql

    @is_slow_sql.setter
    def is_slow_sql(self, is_slow_sql):
        r"""Sets the is_slow_sql of this FullSqlComponetResult.

        **参数解释**: 是否慢SQL。 **取值范围**: 不涉及。

        :param is_slow_sql: The is_slow_sql of this FullSqlComponetResult.
        :type is_slow_sql: bool
        """
        self._is_slow_sql = is_slow_sql

    @property
    def advise(self):
        r"""Gets the advise of this FullSqlComponetResult.

        **参数解释**: 可能导致该SQL为慢SQL的风险信息。 **取值范围**: 不涉及。

        :return: The advise of this FullSqlComponetResult.
        :rtype: str
        """
        return self._advise

    @advise.setter
    def advise(self, advise):
        r"""Sets the advise of this FullSqlComponetResult.

        **参数解释**: 可能导致该SQL为慢SQL的风险信息。 **取值范围**: 不涉及。

        :param advise: The advise of this FullSqlComponetResult.
        :type advise: str
        """
        self._advise = advise

    @property
    def finish_status(self):
        r"""Gets the finish_status of this FullSqlComponetResult.

        **参数解释**: 语句完成状态。 **取值范围**: 不涉及。

        :return: The finish_status of this FullSqlComponetResult.
        :rtype: str
        """
        return self._finish_status

    @finish_status.setter
    def finish_status(self, finish_status):
        r"""Sets the finish_status of this FullSqlComponetResult.

        **参数解释**: 语句完成状态。 **取值范围**: 不涉及。

        :param finish_status: The finish_status of this FullSqlComponetResult.
        :type finish_status: str
        """
        self._finish_status = finish_status

    @property
    def net_send_info(self):
        r"""Gets the net_send_info of this FullSqlComponetResult.

        **参数解释**: 通过物理连接发送消息的网络状态。 **取值范围**: 不涉及。

        :return: The net_send_info of this FullSqlComponetResult.
        :rtype: str
        """
        return self._net_send_info

    @net_send_info.setter
    def net_send_info(self, net_send_info):
        r"""Sets the net_send_info of this FullSqlComponetResult.

        **参数解释**: 通过物理连接发送消息的网络状态。 **取值范围**: 不涉及。

        :param net_send_info: The net_send_info of this FullSqlComponetResult.
        :type net_send_info: str
        """
        self._net_send_info = net_send_info

    @property
    def net_recv_info(self):
        r"""Gets the net_recv_info of this FullSqlComponetResult.

        **参数解释**: 通过物理连接接收消息的网络状态。 **取值范围**: 不涉及。

        :return: The net_recv_info of this FullSqlComponetResult.
        :rtype: str
        """
        return self._net_recv_info

    @net_recv_info.setter
    def net_recv_info(self, net_recv_info):
        r"""Sets the net_recv_info of this FullSqlComponetResult.

        **参数解释**: 通过物理连接接收消息的网络状态。 **取值范围**: 不涉及。

        :param net_recv_info: The net_recv_info of this FullSqlComponetResult.
        :type net_recv_info: str
        """
        self._net_recv_info = net_recv_info

    @property
    def net_stream_send_info(self):
        r"""Gets the net_stream_send_info of this FullSqlComponetResult.

        **参数解释**: 通过逻辑连接发送消息的网络状态。 **取值范围**: 不涉及。

        :return: The net_stream_send_info of this FullSqlComponetResult.
        :rtype: str
        """
        return self._net_stream_send_info

    @net_stream_send_info.setter
    def net_stream_send_info(self, net_stream_send_info):
        r"""Sets the net_stream_send_info of this FullSqlComponetResult.

        **参数解释**: 通过逻辑连接发送消息的网络状态。 **取值范围**: 不涉及。

        :param net_stream_send_info: The net_stream_send_info of this FullSqlComponetResult.
        :type net_stream_send_info: str
        """
        self._net_stream_send_info = net_stream_send_info

    @property
    def net_stream_recv_info(self):
        r"""Gets the net_stream_recv_info of this FullSqlComponetResult.

        **参数解释**: 通过逻辑连接接收消息的网络状态。 **取值范围**: 不涉及。

        :return: The net_stream_recv_info of this FullSqlComponetResult.
        :rtype: str
        """
        return self._net_stream_recv_info

    @net_stream_recv_info.setter
    def net_stream_recv_info(self, net_stream_recv_info):
        r"""Sets the net_stream_recv_info of this FullSqlComponetResult.

        **参数解释**: 通过逻辑连接接收消息的网络状态。 **取值范围**: 不涉及。

        :param net_stream_recv_info: The net_stream_recv_info of this FullSqlComponetResult.
        :type net_stream_recv_info: str
        """
        self._net_stream_recv_info = net_stream_recv_info

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
        if not isinstance(other, FullSqlComponetResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
