# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnhanceFullSqlStatisticsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'node_id': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'query': 'str',
        'sql_id': 'str',
        'sql_exec_id': 'str',
        'transaction_id': 'str',
        'trace_id': 'str',
        'db_name': 'str',
        'schema_name': 'str',
        'username': 'str',
        'client_addr': 'str',
        'client_port': 'str',
        'order_by': 'str',
        'is_slow_sql': 'bool',
        'order': 'str',
        'application_name': 'str',
        'component_id': 'str',
        'multi_queries': 'list[MultiQueryConditionOption]',
        'compare_conditions': 'list[CompareConditionOption]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'node_id': 'node_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'query': 'query',
        'sql_id': 'sql_id',
        'sql_exec_id': 'sql_exec_id',
        'transaction_id': 'transaction_id',
        'trace_id': 'trace_id',
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'username': 'username',
        'client_addr': 'client_addr',
        'client_port': 'client_port',
        'order_by': 'order_by',
        'is_slow_sql': 'is_slow_sql',
        'order': 'order',
        'application_name': 'application_name',
        'component_id': 'component_id',
        'multi_queries': 'multi_queries',
        'compare_conditions': 'compare_conditions'
    }

    def __init__(self, limit=None, offset=None, node_id=None, begin_time=None, end_time=None, query=None, sql_id=None, sql_exec_id=None, transaction_id=None, trace_id=None, db_name=None, schema_name=None, username=None, client_addr=None, client_port=None, order_by=None, is_slow_sql=None, order=None, application_name=None, component_id=None, multi_queries=None, compare_conditions=None):
        r"""ListEnhanceFullSqlStatisticsRequestBody

        The model defined in huaweicloud sdk

        :param limit: **参数解释**: 查询记录数。例如该参数设定为10，则查询结果最多只显示10条记录。 **约束限制**: 不涉及。 **取值范围**: [1, 1000] **默认取值**: 默认为10。
        :type limit: int
        :param offset: **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为0，limit指定为10，则只展示第1~10条数据。 **约束限制**: 不涉及。 **取值范围**: [0, 9223372036854774807] **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。
        :type offset: int
        :param node_id: **参数解释**: 节点ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type node_id: str
        :param begin_time: **参数解释**: 查询开始时间。 **约束限制**: ISO 8601 UTC格式。模式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如：北京时间偏移显示为+0800，begin_time&#x3D;2024-03-15T17:20:33+0800，传参时编码为begin_time&#x3D;2024-03-15T17:20:33%2B0800。 **取值范围**: 时间区间（begin_time ~ end_time）不能超过30天。 **默认取值**: 不涉及。
        :type begin_time: str
        :param end_time: **参数解释**: 查询结束时间。 **约束限制**: ISO 8601 UTC格式。模式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如：北京时间偏移显示为+0800，end_time&#x3D;2024-03-16T17:20:33+0800，传参时编码为end_time&#x3D;2024-03-16T17:20:33%2B0800。 **取值范围**: 时间区间（begin_time ~ end_time）不能超过30天。 **默认取值**: 不涉及。
        :type end_time: str
        :param query: **参数解释**: SQL文本。 **约束限制**: 不涉及。 **取值范围**: 长度1~4096。 **默认取值**: 不涉及。
        :type query: str
        :param sql_id: **参数解释**: 归一化SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_id: str
        :param sql_exec_id: **参数解释**: 唯一SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type sql_exec_id: str
        :param transaction_id: **参数解释**: 事务ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type transaction_id: str
        :param trace_id: **参数解释**: 链路ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type trace_id: str
        :param db_name: **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type db_name: str
        :param schema_name: **参数解释**: schema名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type schema_name: str
        :param username: **参数解释**: 用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type username: str
        :param client_addr: **参数解释**: 客户端地址。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type client_addr: str
        :param client_port: **参数解释**: 客户端端口。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type client_port: str
        :param order_by: **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: - sql_id - sql_count - avg_db_time - avg_cpu_time - avg_execution_time - avg_data_io_time - start_time_stamp  **默认取值**: sql_count
        :type order_by: str
        :param is_slow_sql: **参数解释**: 是否是慢SQL。 **约束限制**: 不涉及。 **取值范围**: - true：是慢SQL。 - false：不是慢SQL。  **默认取值**: 不涉及。
        :type is_slow_sql: bool
        :param order: **参数解释**: 排序方式，支持升序和降序。 **约束限制**: 不涉及。 **取值范围**: - DESC：降序。 - ASC：升序。  **默认取值**: DESC
        :type order: str
        :param application_name: **参数解释**: 应用名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type application_name: str
        :param component_id: **参数解释**: 组件ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type component_id: str
        :param multi_queries: **参数解释**: 字段汇聚查询条件列表。 **约束限制**: 只支持针对query字段全与或者全或的查询。
        :type multi_queries: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        :param compare_conditions: **参数解释**: 组合比较查询条件，可针对某个给定过滤字段，进行区间范围、大小、小于等条件合并查询。 **约束限制**: 不涉及。
        :type compare_conditions: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CompareConditionOption`]
        """
        
        

        self._limit = None
        self._offset = None
        self._node_id = None
        self._begin_time = None
        self._end_time = None
        self._query = None
        self._sql_id = None
        self._sql_exec_id = None
        self._transaction_id = None
        self._trace_id = None
        self._db_name = None
        self._schema_name = None
        self._username = None
        self._client_addr = None
        self._client_port = None
        self._order_by = None
        self._is_slow_sql = None
        self._order = None
        self._application_name = None
        self._component_id = None
        self._multi_queries = None
        self._compare_conditions = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if node_id is not None:
            self.node_id = node_id
        self.begin_time = begin_time
        self.end_time = end_time
        if query is not None:
            self.query = query
        if sql_id is not None:
            self.sql_id = sql_id
        if sql_exec_id is not None:
            self.sql_exec_id = sql_exec_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if trace_id is not None:
            self.trace_id = trace_id
        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if username is not None:
            self.username = username
        if client_addr is not None:
            self.client_addr = client_addr
        if client_port is not None:
            self.client_port = client_port
        if order_by is not None:
            self.order_by = order_by
        if is_slow_sql is not None:
            self.is_slow_sql = is_slow_sql
        if order is not None:
            self.order = order
        if application_name is not None:
            self.application_name = application_name
        if component_id is not None:
            self.component_id = component_id
        if multi_queries is not None:
            self.multi_queries = multi_queries
        if compare_conditions is not None:
            self.compare_conditions = compare_conditions

    @property
    def limit(self):
        r"""Gets the limit of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 查询记录数。例如该参数设定为10，则查询结果最多只显示10条记录。 **约束限制**: 不涉及。 **取值范围**: [1, 1000] **默认取值**: 默认为10。

        :return: The limit of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 查询记录数。例如该参数设定为10，则查询结果最多只显示10条记录。 **约束限制**: 不涉及。 **取值范围**: [1, 1000] **默认取值**: 默认为10。

        :param limit: The limit of this ListEnhanceFullSqlStatisticsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为0，limit指定为10，则只展示第1~10条数据。 **约束限制**: 不涉及。 **取值范围**: [0, 9223372036854774807] **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :return: The offset of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为0，limit指定为10，则只展示第1~10条数据。 **约束限制**: 不涉及。 **取值范围**: [0, 9223372036854774807] **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :param offset: The offset of this ListEnhanceFullSqlStatisticsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def node_id(self):
        r"""Gets the node_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 节点ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The node_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 节点ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param node_id: The node_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 查询开始时间。 **约束限制**: ISO 8601 UTC格式。模式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如：北京时间偏移显示为+0800，begin_time=2024-03-15T17:20:33+0800，传参时编码为begin_time=2024-03-15T17:20:33%2B0800。 **取值范围**: 时间区间（begin_time ~ end_time）不能超过30天。 **默认取值**: 不涉及。

        :return: The begin_time of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 查询开始时间。 **约束限制**: ISO 8601 UTC格式。模式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如：北京时间偏移显示为+0800，begin_time=2024-03-15T17:20:33+0800，传参时编码为begin_time=2024-03-15T17:20:33%2B0800。 **取值范围**: 时间区间（begin_time ~ end_time）不能超过30天。 **默认取值**: 不涉及。

        :param begin_time: The begin_time of this ListEnhanceFullSqlStatisticsRequestBody.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 查询结束时间。 **约束限制**: ISO 8601 UTC格式。模式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如：北京时间偏移显示为+0800，end_time=2024-03-16T17:20:33+0800，传参时编码为end_time=2024-03-16T17:20:33%2B0800。 **取值范围**: 时间区间（begin_time ~ end_time）不能超过30天。 **默认取值**: 不涉及。

        :return: The end_time of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 查询结束时间。 **约束限制**: ISO 8601 UTC格式。模式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如：北京时间偏移显示为+0800，end_time=2024-03-16T17:20:33+0800，传参时编码为end_time=2024-03-16T17:20:33%2B0800。 **取值范围**: 时间区间（begin_time ~ end_time）不能超过30天。 **默认取值**: 不涉及。

        :param end_time: The end_time of this ListEnhanceFullSqlStatisticsRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def query(self):
        r"""Gets the query of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: SQL文本。 **约束限制**: 不涉及。 **取值范围**: 长度1~4096。 **默认取值**: 不涉及。

        :return: The query of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: SQL文本。 **约束限制**: 不涉及。 **取值范围**: 长度1~4096。 **默认取值**: 不涉及。

        :param query: The query of this ListEnhanceFullSqlStatisticsRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def sql_id(self):
        r"""Gets the sql_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 归一化SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 归一化SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_id: The sql_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def sql_exec_id(self):
        r"""Gets the sql_exec_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 唯一SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The sql_exec_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._sql_exec_id

    @sql_exec_id.setter
    def sql_exec_id(self, sql_exec_id):
        r"""Sets the sql_exec_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 唯一SQL ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param sql_exec_id: The sql_exec_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :type sql_exec_id: str
        """
        self._sql_exec_id = sql_exec_id

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 事务ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The transaction_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 事务ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param transaction_id: The transaction_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def trace_id(self):
        r"""Gets the trace_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 链路ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The trace_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._trace_id

    @trace_id.setter
    def trace_id(self, trace_id):
        r"""Sets the trace_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 链路ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param trace_id: The trace_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :type trace_id: str
        """
        self._trace_id = trace_id

    @property
    def db_name(self):
        r"""Gets the db_name of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The db_name of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 数据库名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param db_name: The db_name of this ListEnhanceFullSqlStatisticsRequestBody.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: schema名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The schema_name of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: schema名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param schema_name: The schema_name of this ListEnhanceFullSqlStatisticsRequestBody.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def username(self):
        r"""Gets the username of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The username of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 用户名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param username: The username of this ListEnhanceFullSqlStatisticsRequestBody.
        :type username: str
        """
        self._username = username

    @property
    def client_addr(self):
        r"""Gets the client_addr of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 客户端地址。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The client_addr of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._client_addr

    @client_addr.setter
    def client_addr(self, client_addr):
        r"""Sets the client_addr of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 客户端地址。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param client_addr: The client_addr of this ListEnhanceFullSqlStatisticsRequestBody.
        :type client_addr: str
        """
        self._client_addr = client_addr

    @property
    def client_port(self):
        r"""Gets the client_port of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 客户端端口。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The client_port of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 客户端端口。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param client_port: The client_port of this ListEnhanceFullSqlStatisticsRequestBody.
        :type client_port: str
        """
        self._client_port = client_port

    @property
    def order_by(self):
        r"""Gets the order_by of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: - sql_id - sql_count - avg_db_time - avg_cpu_time - avg_execution_time - avg_data_io_time - start_time_stamp  **默认取值**: sql_count

        :return: The order_by of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: - sql_id - sql_count - avg_db_time - avg_cpu_time - avg_execution_time - avg_data_io_time - start_time_stamp  **默认取值**: sql_count

        :param order_by: The order_by of this ListEnhanceFullSqlStatisticsRequestBody.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def is_slow_sql(self):
        r"""Gets the is_slow_sql of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 是否是慢SQL。 **约束限制**: 不涉及。 **取值范围**: - true：是慢SQL。 - false：不是慢SQL。  **默认取值**: 不涉及。

        :return: The is_slow_sql of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: bool
        """
        return self._is_slow_sql

    @is_slow_sql.setter
    def is_slow_sql(self, is_slow_sql):
        r"""Sets the is_slow_sql of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 是否是慢SQL。 **约束限制**: 不涉及。 **取值范围**: - true：是慢SQL。 - false：不是慢SQL。  **默认取值**: 不涉及。

        :param is_slow_sql: The is_slow_sql of this ListEnhanceFullSqlStatisticsRequestBody.
        :type is_slow_sql: bool
        """
        self._is_slow_sql = is_slow_sql

    @property
    def order(self):
        r"""Gets the order of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 排序方式，支持升序和降序。 **约束限制**: 不涉及。 **取值范围**: - DESC：降序。 - ASC：升序。  **默认取值**: DESC

        :return: The order of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 排序方式，支持升序和降序。 **约束限制**: 不涉及。 **取值范围**: - DESC：降序。 - ASC：升序。  **默认取值**: DESC

        :param order: The order of this ListEnhanceFullSqlStatisticsRequestBody.
        :type order: str
        """
        self._order = order

    @property
    def application_name(self):
        r"""Gets the application_name of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 应用名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The application_name of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 应用名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param application_name: The application_name of this ListEnhanceFullSqlStatisticsRequestBody.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def component_id(self):
        r"""Gets the component_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 组件ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The component_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 组件ID。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param component_id: The component_id of this ListEnhanceFullSqlStatisticsRequestBody.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def multi_queries(self):
        r"""Gets the multi_queries of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 字段汇聚查询条件列表。 **约束限制**: 只支持针对query字段全与或者全或的查询。

        :return: The multi_queries of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        """
        return self._multi_queries

    @multi_queries.setter
    def multi_queries(self, multi_queries):
        r"""Sets the multi_queries of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 字段汇聚查询条件列表。 **约束限制**: 只支持针对query字段全与或者全或的查询。

        :param multi_queries: The multi_queries of this ListEnhanceFullSqlStatisticsRequestBody.
        :type multi_queries: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.MultiQueryConditionOption`]
        """
        self._multi_queries = multi_queries

    @property
    def compare_conditions(self):
        r"""Gets the compare_conditions of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 组合比较查询条件，可针对某个给定过滤字段，进行区间范围、大小、小于等条件合并查询。 **约束限制**: 不涉及。

        :return: The compare_conditions of this ListEnhanceFullSqlStatisticsRequestBody.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CompareConditionOption`]
        """
        return self._compare_conditions

    @compare_conditions.setter
    def compare_conditions(self, compare_conditions):
        r"""Sets the compare_conditions of this ListEnhanceFullSqlStatisticsRequestBody.

        **参数解释**: 组合比较查询条件，可针对某个给定过滤字段，进行区间范围、大小、小于等条件合并查询。 **约束限制**: 不涉及。

        :param compare_conditions: The compare_conditions of this ListEnhanceFullSqlStatisticsRequestBody.
        :type compare_conditions: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CompareConditionOption`]
        """
        self._compare_conditions = compare_conditions

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
        if not isinstance(other, ListEnhanceFullSqlStatisticsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
