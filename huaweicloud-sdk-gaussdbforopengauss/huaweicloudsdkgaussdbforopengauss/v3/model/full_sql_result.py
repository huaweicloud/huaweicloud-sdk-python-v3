# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullSqlResult:

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
        'instance_id': 'str',
        'node_id': 'str',
        'component_id': 'str',
        'db_name': 'str',
        'schema_name': 'str',
        'username': 'str',
        'application_name': 'str',
        'client_addr': 'str',
        'client_port': 'str',
        'sql_id': 'str',
        'sql_exec_id': 'str',
        'transaction_id': 'str',
        'trace_id': 'str',
        'query': 'str',
        'sql': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'all_time': 'int',
        'db_time': 'int',
        'cpu_time': 'int',
        'data_io_time': 'int',
        'execution_time': 'int',
        'scan_lines': 'int',
        'insert_rows': 'int',
        'update_rows': 'int',
        'delete_rows': 'int',
        'is_slow_sql': 'bool',
        'start_timestamp': 'int',
        'finish_timestamp': 'int',
        'hit_rate': 'float'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'component_id': 'component_id',
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'username': 'username',
        'application_name': 'application_name',
        'client_addr': 'client_addr',
        'client_port': 'client_port',
        'sql_id': 'sql_id',
        'sql_exec_id': 'sql_exec_id',
        'transaction_id': 'transaction_id',
        'trace_id': 'trace_id',
        'query': 'query',
        'sql': 'sql',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'all_time': 'all_time',
        'db_time': 'db_time',
        'cpu_time': 'cpu_time',
        'data_io_time': 'data_io_time',
        'execution_time': 'execution_time',
        'scan_lines': 'scan_lines',
        'insert_rows': 'insert_rows',
        'update_rows': 'update_rows',
        'delete_rows': 'delete_rows',
        'is_slow_sql': 'is_slow_sql',
        'start_timestamp': 'start_timestamp',
        'finish_timestamp': 'finish_timestamp',
        'hit_rate': 'hit_rate'
    }

    def __init__(self, id=None, instance_id=None, node_id=None, component_id=None, db_name=None, schema_name=None, username=None, application_name=None, client_addr=None, client_port=None, sql_id=None, sql_exec_id=None, transaction_id=None, trace_id=None, query=None, sql=None, begin_time=None, end_time=None, all_time=None, db_time=None, cpu_time=None, data_io_time=None, execution_time=None, scan_lines=None, insert_rows=None, update_rows=None, delete_rows=None, is_slow_sql=None, start_timestamp=None, finish_timestamp=None, hit_rate=None):
        r"""FullSqlResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**: SQL记录唯一键ID。 **取值范围**: 不涉及。
        :type id: str
        :param instance_id: **参数解释**: 实例ID。 **取值范围**: 不涉及。
        :type instance_id: str
        :param node_id: **参数解释**: 节点ID。 **取值范围**: 不涉及。
        :type node_id: str
        :param component_id: **参数解释**: 组件ID。 **取值范围**: 不涉及。
        :type component_id: str
        :param db_name: **参数解释**: 数据库名称。 **取值范围**: 不涉及。
        :type db_name: str
        :param schema_name: **参数解释**: schema名称。 **取值范围**: 不涉及。
        :type schema_name: str
        :param username: **参数解释**: 用户名称。 **取值范围**: 不涉及。
        :type username: str
        :param application_name: **参数解释**: 用户发起的请求的应用程序名称。 **取值范围**: 不涉及。
        :type application_name: str
        :param client_addr: **参数解释**: 用户发起的请求的客户端地址。 **取值范围**: 不涉及。
        :type client_addr: str
        :param client_port: **参数解释**: 用户发起请求的客户端端口。 **取值范围**: 不涉及。
        :type client_port: str
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
        :param sql: **参数解释**: 解析后的原始SQL文本。 **取值范围**: 开启track_stmt_parameter参数后，会把SQL文本中的变量替换成真实值，展示原始的SQL。对于track_stmt_parameter参数关闭时采集的SQL文本，无法获取到SQL参数变量的值，展示的内容为空。
        :type sql: str
        :param begin_time: **参数解释**: 开始时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。
        :type begin_time: str
        :param end_time: **参数解释**: 结束时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。
        :type end_time: str
        :param all_time: **参数解释**: 执行总时间（单位：微秒）。 **取值范围**: 不涉及。
        :type all_time: int
        :param db_time: **参数解释**: 有效DB时间（单位：微秒）。 **取值范围**: 不涉及。
        :type db_time: int
        :param cpu_time: **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。
        :type cpu_time: int
        :param data_io_time: **参数解释**: IO时间（单位：微秒）。 **取值范围**: 不涉及。
        :type data_io_time: int
        :param execution_time: **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。
        :type execution_time: int
        :param scan_lines: **参数解释**: 扫描行。 **取值范围**: 不涉及。
        :type scan_lines: int
        :param insert_rows: **参数解释**: 插入行。 **取值范围**: 不涉及。
        :type insert_rows: int
        :param update_rows: **参数解释**: 更新行。 **取值范围**: 不涉及。
        :type update_rows: int
        :param delete_rows: **参数解释**: 删除行。 **取值范围**: 不涉及。
        :type delete_rows: int
        :param is_slow_sql: **参数解释**: 是否慢SQL。 **取值范围**: 不涉及。
        :type is_slow_sql: bool
        :param start_timestamp: **参数解释**: SQL开始时间。格式为13位标准时间戳，如1754647168354。 **取值范围**: 不涉及。
        :type start_timestamp: int
        :param finish_timestamp: **参数解释**: SQL结束时间，格式为13位标准时间戳，如1754647168355。 **取值范围**: 不涉及。
        :type finish_timestamp: int
        :param hit_rate: **参数解释**: SQL命中率。 计划即将下线，请勿使用。 **取值范围**: 不涉及。
        :type hit_rate: float
        """
        
        

        self._id = None
        self._instance_id = None
        self._node_id = None
        self._component_id = None
        self._db_name = None
        self._schema_name = None
        self._username = None
        self._application_name = None
        self._client_addr = None
        self._client_port = None
        self._sql_id = None
        self._sql_exec_id = None
        self._transaction_id = None
        self._trace_id = None
        self._query = None
        self._sql = None
        self._begin_time = None
        self._end_time = None
        self._all_time = None
        self._db_time = None
        self._cpu_time = None
        self._data_io_time = None
        self._execution_time = None
        self._scan_lines = None
        self._insert_rows = None
        self._update_rows = None
        self._delete_rows = None
        self._is_slow_sql = None
        self._start_timestamp = None
        self._finish_timestamp = None
        self._hit_rate = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if component_id is not None:
            self.component_id = component_id
        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if username is not None:
            self.username = username
        if application_name is not None:
            self.application_name = application_name
        if client_addr is not None:
            self.client_addr = client_addr
        if client_port is not None:
            self.client_port = client_port
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
        if sql is not None:
            self.sql = sql
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if all_time is not None:
            self.all_time = all_time
        if db_time is not None:
            self.db_time = db_time
        if cpu_time is not None:
            self.cpu_time = cpu_time
        if data_io_time is not None:
            self.data_io_time = data_io_time
        if execution_time is not None:
            self.execution_time = execution_time
        if scan_lines is not None:
            self.scan_lines = scan_lines
        if insert_rows is not None:
            self.insert_rows = insert_rows
        if update_rows is not None:
            self.update_rows = update_rows
        if delete_rows is not None:
            self.delete_rows = delete_rows
        if is_slow_sql is not None:
            self.is_slow_sql = is_slow_sql
        if start_timestamp is not None:
            self.start_timestamp = start_timestamp
        if finish_timestamp is not None:
            self.finish_timestamp = finish_timestamp
        if hit_rate is not None:
            self.hit_rate = hit_rate

    @property
    def id(self):
        r"""Gets the id of this FullSqlResult.

        **参数解释**: SQL记录唯一键ID。 **取值范围**: 不涉及。

        :return: The id of this FullSqlResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this FullSqlResult.

        **参数解释**: SQL记录唯一键ID。 **取值范围**: 不涉及。

        :param id: The id of this FullSqlResult.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this FullSqlResult.

        **参数解释**: 实例ID。 **取值范围**: 不涉及。

        :return: The instance_id of this FullSqlResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this FullSqlResult.

        **参数解释**: 实例ID。 **取值范围**: 不涉及。

        :param instance_id: The instance_id of this FullSqlResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this FullSqlResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :return: The node_id of this FullSqlResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this FullSqlResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :param node_id: The node_id of this FullSqlResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def component_id(self):
        r"""Gets the component_id of this FullSqlResult.

        **参数解释**: 组件ID。 **取值范围**: 不涉及。

        :return: The component_id of this FullSqlResult.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this FullSqlResult.

        **参数解释**: 组件ID。 **取值范围**: 不涉及。

        :param component_id: The component_id of this FullSqlResult.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def db_name(self):
        r"""Gets the db_name of this FullSqlResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :return: The db_name of this FullSqlResult.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this FullSqlResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :param db_name: The db_name of this FullSqlResult.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this FullSqlResult.

        **参数解释**: schema名称。 **取值范围**: 不涉及。

        :return: The schema_name of this FullSqlResult.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this FullSqlResult.

        **参数解释**: schema名称。 **取值范围**: 不涉及。

        :param schema_name: The schema_name of this FullSqlResult.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def username(self):
        r"""Gets the username of this FullSqlResult.

        **参数解释**: 用户名称。 **取值范围**: 不涉及。

        :return: The username of this FullSqlResult.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this FullSqlResult.

        **参数解释**: 用户名称。 **取值范围**: 不涉及。

        :param username: The username of this FullSqlResult.
        :type username: str
        """
        self._username = username

    @property
    def application_name(self):
        r"""Gets the application_name of this FullSqlResult.

        **参数解释**: 用户发起的请求的应用程序名称。 **取值范围**: 不涉及。

        :return: The application_name of this FullSqlResult.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this FullSqlResult.

        **参数解释**: 用户发起的请求的应用程序名称。 **取值范围**: 不涉及。

        :param application_name: The application_name of this FullSqlResult.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def client_addr(self):
        r"""Gets the client_addr of this FullSqlResult.

        **参数解释**: 用户发起的请求的客户端地址。 **取值范围**: 不涉及。

        :return: The client_addr of this FullSqlResult.
        :rtype: str
        """
        return self._client_addr

    @client_addr.setter
    def client_addr(self, client_addr):
        r"""Sets the client_addr of this FullSqlResult.

        **参数解释**: 用户发起的请求的客户端地址。 **取值范围**: 不涉及。

        :param client_addr: The client_addr of this FullSqlResult.
        :type client_addr: str
        """
        self._client_addr = client_addr

    @property
    def client_port(self):
        r"""Gets the client_port of this FullSqlResult.

        **参数解释**: 用户发起请求的客户端端口。 **取值范围**: 不涉及。

        :return: The client_port of this FullSqlResult.
        :rtype: str
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this FullSqlResult.

        **参数解释**: 用户发起请求的客户端端口。 **取值范围**: 不涉及。

        :param client_port: The client_port of this FullSqlResult.
        :type client_port: str
        """
        self._client_port = client_port

    @property
    def sql_id(self):
        r"""Gets the sql_id of this FullSqlResult.

        **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **取值范围**: 不涉及。

        :return: The sql_id of this FullSqlResult.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this FullSqlResult.

        **参数解释**: 归一化SQL ID，对应内核字段：unique_sql_id。 **取值范围**: 不涉及。

        :param sql_id: The sql_id of this FullSqlResult.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def sql_exec_id(self):
        r"""Gets the sql_exec_id of this FullSqlResult.

        **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **取值范围**: 不涉及。

        :return: The sql_exec_id of this FullSqlResult.
        :rtype: str
        """
        return self._sql_exec_id

    @sql_exec_id.setter
    def sql_exec_id(self, sql_exec_id):
        r"""Sets the sql_exec_id of this FullSqlResult.

        **参数解释**: 唯一SQL ID，对应内核字段：debug_query_id。 **取值范围**: 不涉及。

        :param sql_exec_id: The sql_exec_id of this FullSqlResult.
        :type sql_exec_id: str
        """
        self._sql_exec_id = sql_exec_id

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this FullSqlResult.

        **参数解释**: 事务ID，对应内核字段：debug_query_id。 **取值范围**: 不涉及。

        :return: The transaction_id of this FullSqlResult.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this FullSqlResult.

        **参数解释**: 事务ID，对应内核字段：debug_query_id。 **取值范围**: 不涉及。

        :param transaction_id: The transaction_id of this FullSqlResult.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def trace_id(self):
        r"""Gets the trace_id of this FullSqlResult.

        **参数解释**: 链路ID。 **取值范围**: 不涉及。

        :return: The trace_id of this FullSqlResult.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this FullSqlResult.

        **参数解释**: 链路ID。 **取值范围**: 不涉及。

        :param trace_id: The trace_id of this FullSqlResult.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def query(self):
        r"""Gets the query of this FullSqlResult.

        **参数解释**: 归一化SQL。 **取值范围**: 不涉及。

        :return: The query of this FullSqlResult.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this FullSqlResult.

        **参数解释**: 归一化SQL。 **取值范围**: 不涉及。

        :param query: The query of this FullSqlResult.
        :type query: str
        """
        self._query = query

    @property
    def sql(self):
        r"""Gets the sql of this FullSqlResult.

        **参数解释**: 解析后的原始SQL文本。 **取值范围**: 开启track_stmt_parameter参数后，会把SQL文本中的变量替换成真实值，展示原始的SQL。对于track_stmt_parameter参数关闭时采集的SQL文本，无法获取到SQL参数变量的值，展示的内容为空。

        :return: The sql of this FullSqlResult.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this FullSqlResult.

        **参数解释**: 解析后的原始SQL文本。 **取值范围**: 开启track_stmt_parameter参数后，会把SQL文本中的变量替换成真实值，展示原始的SQL。对于track_stmt_parameter参数关闭时采集的SQL文本，无法获取到SQL参数变量的值，展示的内容为空。

        :param sql: The sql of this FullSqlResult.
        :type sql: str
        """
        self._sql = sql

    @property
    def begin_time(self):
        r"""Gets the begin_time of this FullSqlResult.

        **参数解释**: 开始时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。

        :return: The begin_time of this FullSqlResult.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this FullSqlResult.

        **参数解释**: 开始时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。

        :param begin_time: The begin_time of this FullSqlResult.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this FullSqlResult.

        **参数解释**: 结束时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。

        :return: The end_time of this FullSqlResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this FullSqlResult.

        **参数解释**: 结束时间，格式为“yyyy-mm-ddThh:mm:ss.SSSSSZ”。 **取值范围**: 不涉及。

        :param end_time: The end_time of this FullSqlResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def all_time(self):
        r"""Gets the all_time of this FullSqlResult.

        **参数解释**: 执行总时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The all_time of this FullSqlResult.
        :rtype: int
        """
        return self._all_time

    @all_time.setter
    def all_time(self, all_time):
        r"""Sets the all_time of this FullSqlResult.

        **参数解释**: 执行总时间（单位：微秒）。 **取值范围**: 不涉及。

        :param all_time: The all_time of this FullSqlResult.
        :type all_time: int
        """
        self._all_time = all_time

    @property
    def db_time(self):
        r"""Gets the db_time of this FullSqlResult.

        **参数解释**: 有效DB时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The db_time of this FullSqlResult.
        :rtype: int
        """
        return self._db_time

    @db_time.setter
    def db_time(self, db_time):
        r"""Sets the db_time of this FullSqlResult.

        **参数解释**: 有效DB时间（单位：微秒）。 **取值范围**: 不涉及。

        :param db_time: The db_time of this FullSqlResult.
        :type db_time: int
        """
        self._db_time = db_time

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this FullSqlResult.

        **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The cpu_time of this FullSqlResult.
        :rtype: int
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this FullSqlResult.

        **参数解释**: CPU时间（单位：微秒）。 **取值范围**: 不涉及。

        :param cpu_time: The cpu_time of this FullSqlResult.
        :type cpu_time: int
        """
        self._cpu_time = cpu_time

    @property
    def data_io_time(self):
        r"""Gets the data_io_time of this FullSqlResult.

        **参数解释**: IO时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The data_io_time of this FullSqlResult.
        :rtype: int
        """
        return self._data_io_time

    @data_io_time.setter
    def data_io_time(self, data_io_time):
        r"""Sets the data_io_time of this FullSqlResult.

        **参数解释**: IO时间（单位：微秒）。 **取值范围**: 不涉及。

        :param data_io_time: The data_io_time of this FullSqlResult.
        :type data_io_time: int
        """
        self._data_io_time = data_io_time

    @property
    def execution_time(self):
        r"""Gets the execution_time of this FullSqlResult.

        **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :return: The execution_time of this FullSqlResult.
        :rtype: int
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        r"""Sets the execution_time of this FullSqlResult.

        **参数解释**: 执行器内执行时间（单位：微秒）。 **取值范围**: 不涉及。

        :param execution_time: The execution_time of this FullSqlResult.
        :type execution_time: int
        """
        self._execution_time = execution_time

    @property
    def scan_lines(self):
        r"""Gets the scan_lines of this FullSqlResult.

        **参数解释**: 扫描行。 **取值范围**: 不涉及。

        :return: The scan_lines of this FullSqlResult.
        :rtype: int
        """
        return self._scan_lines

    @scan_lines.setter
    def scan_lines(self, scan_lines):
        r"""Sets the scan_lines of this FullSqlResult.

        **参数解释**: 扫描行。 **取值范围**: 不涉及。

        :param scan_lines: The scan_lines of this FullSqlResult.
        :type scan_lines: int
        """
        self._scan_lines = scan_lines

    @property
    def insert_rows(self):
        r"""Gets the insert_rows of this FullSqlResult.

        **参数解释**: 插入行。 **取值范围**: 不涉及。

        :return: The insert_rows of this FullSqlResult.
        :rtype: int
        """
        return self._insert_rows

    @insert_rows.setter
    def insert_rows(self, insert_rows):
        r"""Sets the insert_rows of this FullSqlResult.

        **参数解释**: 插入行。 **取值范围**: 不涉及。

        :param insert_rows: The insert_rows of this FullSqlResult.
        :type insert_rows: int
        """
        self._insert_rows = insert_rows

    @property
    def update_rows(self):
        r"""Gets the update_rows of this FullSqlResult.

        **参数解释**: 更新行。 **取值范围**: 不涉及。

        :return: The update_rows of this FullSqlResult.
        :rtype: int
        """
        return self._update_rows

    @update_rows.setter
    def update_rows(self, update_rows):
        r"""Sets the update_rows of this FullSqlResult.

        **参数解释**: 更新行。 **取值范围**: 不涉及。

        :param update_rows: The update_rows of this FullSqlResult.
        :type update_rows: int
        """
        self._update_rows = update_rows

    @property
    def delete_rows(self):
        r"""Gets the delete_rows of this FullSqlResult.

        **参数解释**: 删除行。 **取值范围**: 不涉及。

        :return: The delete_rows of this FullSqlResult.
        :rtype: int
        """
        return self._delete_rows

    @delete_rows.setter
    def delete_rows(self, delete_rows):
        r"""Sets the delete_rows of this FullSqlResult.

        **参数解释**: 删除行。 **取值范围**: 不涉及。

        :param delete_rows: The delete_rows of this FullSqlResult.
        :type delete_rows: int
        """
        self._delete_rows = delete_rows

    @property
    def is_slow_sql(self):
        r"""Gets the is_slow_sql of this FullSqlResult.

        **参数解释**: 是否慢SQL。 **取值范围**: 不涉及。

        :return: The is_slow_sql of this FullSqlResult.
        :rtype: bool
        """
        return self._is_slow_sql

    @is_slow_sql.setter
    def is_slow_sql(self, is_slow_sql):
        r"""Sets the is_slow_sql of this FullSqlResult.

        **参数解释**: 是否慢SQL。 **取值范围**: 不涉及。

        :param is_slow_sql: The is_slow_sql of this FullSqlResult.
        :type is_slow_sql: bool
        """
        self._is_slow_sql = is_slow_sql

    @property
    def start_timestamp(self):
        r"""Gets the start_timestamp of this FullSqlResult.

        **参数解释**: SQL开始时间。格式为13位标准时间戳，如1754647168354。 **取值范围**: 不涉及。

        :return: The start_timestamp of this FullSqlResult.
        :rtype: int
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        r"""Sets the start_timestamp of this FullSqlResult.

        **参数解释**: SQL开始时间。格式为13位标准时间戳，如1754647168354。 **取值范围**: 不涉及。

        :param start_timestamp: The start_timestamp of this FullSqlResult.
        :type start_timestamp: int
        """
        self._start_timestamp = start_timestamp

    @property
    def finish_timestamp(self):
        r"""Gets the finish_timestamp of this FullSqlResult.

        **参数解释**: SQL结束时间，格式为13位标准时间戳，如1754647168355。 **取值范围**: 不涉及。

        :return: The finish_timestamp of this FullSqlResult.
        :rtype: int
        """
        return self._finish_timestamp

    @finish_timestamp.setter
    def finish_timestamp(self, finish_timestamp):
        r"""Sets the finish_timestamp of this FullSqlResult.

        **参数解释**: SQL结束时间，格式为13位标准时间戳，如1754647168355。 **取值范围**: 不涉及。

        :param finish_timestamp: The finish_timestamp of this FullSqlResult.
        :type finish_timestamp: int
        """
        self._finish_timestamp = finish_timestamp

    @property
    def hit_rate(self):
        r"""Gets the hit_rate of this FullSqlResult.

        **参数解释**: SQL命中率。 计划即将下线，请勿使用。 **取值范围**: 不涉及。

        :return: The hit_rate of this FullSqlResult.
        :rtype: float
        """
        return self._hit_rate

    @hit_rate.setter
    def hit_rate(self, hit_rate):
        r"""Sets the hit_rate of this FullSqlResult.

        **参数解释**: SQL命中率。 计划即将下线，请勿使用。 **取值范围**: 不涉及。

        :param hit_rate: The hit_rate of this FullSqlResult.
        :type hit_rate: float
        """
        self._hit_rate = hit_rate

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
        if not isinstance(other, FullSqlResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
