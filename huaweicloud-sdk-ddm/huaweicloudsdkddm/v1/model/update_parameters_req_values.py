# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateParametersReqValues:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bind_table': 'str',
        'character_set_server': 'str',
        'collation_server': 'str',
        'concurrent_execution_level': 'str',
        'connection_idle_timeout': 'str',
        'enable_table_recycle': 'str',
        'insert_to_load_data': 'str',
        'live_transaction_timeout_on_shutdown': 'str',
        'long_query_time': 'str',
        'max_allowed_packet': 'str',
        'max_backend_connections': 'str',
        'max_connections': 'str',
        'min_backend_connections': 'str',
        'not_from_pushdown': 'str',
        'seconds_behind_master': 'str',
        'sql_audit': 'str',
        'sql_execute_timeout': 'str',
        'support_ddl_binlog_hint': 'str',
        'transaction_policy': 'str',
        'ultimate_optimize': 'str'
    }

    attribute_map = {
        'bind_table': 'bind_table',
        'character_set_server': 'character_set_server',
        'collation_server': 'collation_server',
        'concurrent_execution_level': 'concurrent_execution_level',
        'connection_idle_timeout': 'connection_idle_timeout',
        'enable_table_recycle': 'enable_table_recycle',
        'insert_to_load_data': 'insert_to_load_data',
        'live_transaction_timeout_on_shutdown': 'live_transaction_timeout_on_shutdown',
        'long_query_time': 'long_query_time',
        'max_allowed_packet': 'max_allowed_packet',
        'max_backend_connections': 'max_backend_connections',
        'max_connections': 'max_connections',
        'min_backend_connections': 'min_backend_connections',
        'not_from_pushdown': 'not_from_pushdown',
        'seconds_behind_master': 'seconds_behind_master',
        'sql_audit': 'sql_audit',
        'sql_execute_timeout': 'sql_execute_timeout',
        'support_ddl_binlog_hint': 'support_ddl_binlog_hint',
        'transaction_policy': 'transaction_policy',
        'ultimate_optimize': 'ultimate_optimize'
    }

    def __init__(self, bind_table=None, character_set_server=None, collation_server=None, concurrent_execution_level=None, connection_idle_timeout=None, enable_table_recycle=None, insert_to_load_data=None, live_transaction_timeout_on_shutdown=None, long_query_time=None, max_allowed_packet=None, max_backend_connections=None, max_connections=None, min_backend_connections=None, not_from_pushdown=None, seconds_behind_master=None, sql_audit=None, sql_execute_timeout=None, support_ddl_binlog_hint=None, transaction_policy=None, ultimate_optimize=None):
        r"""UpdateParametersReqValues

        The model defined in huaweicloud sdk

        :param bind_table: 用于描述多个拆分表的内在数据关联性，用于告知优化器在处理join时，把join下推到MySQL层执行。格式为:[{tb.col1,tb2.col2},{tb.col2,tb3.col1},...]。
        :type bind_table: str
        :param character_set_server: DDM服务端字符集，如果需要存储emoji表情符号，请选择utf8mb4,并设置RDS字符集也为utf8mb4。修改DDM服务端字符集时，DDM服务端字符序必须同步修改为对应类型的值。
        :type character_set_server: str
        :param collation_server: DDM服务端字符序。修改DDM服务端字符序时，DDM服务端字符集必须同步修改为对应类型的值。
        :type collation_server: str
        :param concurrent_execution_level: 逻辑表扫描时的分片并发执行级别: DATA_NODE: 分库间并行扫描，同一分库内各分片串行扫描;RDS_INSTANCE: RDS实例间并行扫描，同一RDS实例内各分片串行扫描;PHY_TABLE: 各物理分片全部并行扫描。
        :type concurrent_execution_level: str
        :param connection_idle_timeout: 服务器关闭连接之前等待连接活动的秒数，以秒为单位，取值范围为60-28800，默认值28800，表示服务器关闭连接之前等待28800秒后，关闭连接。
        :type connection_idle_timeout: str
        :param enable_table_recycle: 是否开启表回收站。
        :type enable_table_recycle: str
        :param insert_to_load_data: insert 常量值使用load data执行。
        :type insert_to_load_data: str
        :param live_transaction_timeout_on_shutdown: 在途事务等待时间窗口，以秒为单位，取值范围为0-100，默认值为1，表示服务器关闭前端连接之前等待1秒后关闭连接。
        :type live_transaction_timeout_on_shutdown: str
        :param long_query_time: 记录慢查询的最小秒数,以秒为单位，取值范围为0.01-10，默认值为1，表示如果sql执行大于等于1秒就定义为慢sql。
        :type long_query_time: str
        :param max_allowed_packet: 包或任何生成的中间字符串的最大值。包缓冲区初始化为net_buffer_length字节，但需要时可以增长到max_allowed_packet字节。该值默认很小，以捕获大的（可能是错误的）数据包。该值必须设置为1024的倍数。取值范围为1024~1073741824，默认值为16777216。
        :type max_allowed_packet: str
        :param max_backend_connections: 允许每个DDM节点同时连接RDS的最大客户端总数。0为默认值标识符,实际值等于(RDS的最大连接数-20)/DDM节点数。取值范围为0-10000000。
        :type max_backend_connections: str
        :param max_connections: 允许同时连接的客户端总数。与后端RDS规格及数量有关。以个数为单位，取值范围为10-40000，默认值为20000，表示允许同时连接的客户端总数不能超过40000。
        :type max_connections: str
        :param min_backend_connections: 允许每个DDM节点同时连接RDS的最小客户端总数。默认值为10。取值范围为0-10000000。
        :type min_backend_connections: str
        :param not_from_pushdown: 是否强制下推查询语句中不含from的语句。
        :type not_from_pushdown: str
        :param seconds_behind_master: 主从rds节点延迟时间阈值，以秒为单位，取值范围为0-7200，默认值为30，表示主rds与从rds之间的数据同步时间值不能超过30秒，如果超过30s，读数据指令就不走当前读节点。
        :type seconds_behind_master: str
        :param sql_audit: 开启或关闭SQL审计。
        :type sql_audit: str
        :param sql_execute_timeout: SQL执行超时秒数，以秒为单位，取值范围为100-28800，默认值28800，表示sql执行大于等于28800秒超时。
        :type sql_execute_timeout: str
        :param support_ddl_binlog_hint: DDL语句添加binlog hint。
        :type support_ddl_binlog_hint: str
        :param transaction_policy: XA：XA 事务，保证原子性，保证可见性；FREE：允许多写，不保证原子性，无性能损耗；NO_DTX：单分片事务。
        :type transaction_policy: str
        :param ultimate_optimize: 开启或关闭优化器中的极致下推优化功能。
        :type ultimate_optimize: str
        """
        
        

        self._bind_table = None
        self._character_set_server = None
        self._collation_server = None
        self._concurrent_execution_level = None
        self._connection_idle_timeout = None
        self._enable_table_recycle = None
        self._insert_to_load_data = None
        self._live_transaction_timeout_on_shutdown = None
        self._long_query_time = None
        self._max_allowed_packet = None
        self._max_backend_connections = None
        self._max_connections = None
        self._min_backend_connections = None
        self._not_from_pushdown = None
        self._seconds_behind_master = None
        self._sql_audit = None
        self._sql_execute_timeout = None
        self._support_ddl_binlog_hint = None
        self._transaction_policy = None
        self._ultimate_optimize = None
        self.discriminator = None

        if bind_table is not None:
            self.bind_table = bind_table
        if character_set_server is not None:
            self.character_set_server = character_set_server
        if collation_server is not None:
            self.collation_server = collation_server
        if concurrent_execution_level is not None:
            self.concurrent_execution_level = concurrent_execution_level
        if connection_idle_timeout is not None:
            self.connection_idle_timeout = connection_idle_timeout
        if enable_table_recycle is not None:
            self.enable_table_recycle = enable_table_recycle
        if insert_to_load_data is not None:
            self.insert_to_load_data = insert_to_load_data
        if live_transaction_timeout_on_shutdown is not None:
            self.live_transaction_timeout_on_shutdown = live_transaction_timeout_on_shutdown
        if long_query_time is not None:
            self.long_query_time = long_query_time
        if max_allowed_packet is not None:
            self.max_allowed_packet = max_allowed_packet
        if max_backend_connections is not None:
            self.max_backend_connections = max_backend_connections
        if max_connections is not None:
            self.max_connections = max_connections
        if min_backend_connections is not None:
            self.min_backend_connections = min_backend_connections
        if not_from_pushdown is not None:
            self.not_from_pushdown = not_from_pushdown
        if seconds_behind_master is not None:
            self.seconds_behind_master = seconds_behind_master
        if sql_audit is not None:
            self.sql_audit = sql_audit
        if sql_execute_timeout is not None:
            self.sql_execute_timeout = sql_execute_timeout
        if support_ddl_binlog_hint is not None:
            self.support_ddl_binlog_hint = support_ddl_binlog_hint
        if transaction_policy is not None:
            self.transaction_policy = transaction_policy
        if ultimate_optimize is not None:
            self.ultimate_optimize = ultimate_optimize

    @property
    def bind_table(self):
        r"""Gets the bind_table of this UpdateParametersReqValues.

        用于描述多个拆分表的内在数据关联性，用于告知优化器在处理join时，把join下推到MySQL层执行。格式为:[{tb.col1,tb2.col2},{tb.col2,tb3.col1},...]。

        :return: The bind_table of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._bind_table

    @bind_table.setter
    def bind_table(self, bind_table):
        r"""Sets the bind_table of this UpdateParametersReqValues.

        用于描述多个拆分表的内在数据关联性，用于告知优化器在处理join时，把join下推到MySQL层执行。格式为:[{tb.col1,tb2.col2},{tb.col2,tb3.col1},...]。

        :param bind_table: The bind_table of this UpdateParametersReqValues.
        :type bind_table: str
        """
        self._bind_table = bind_table

    @property
    def character_set_server(self):
        r"""Gets the character_set_server of this UpdateParametersReqValues.

        DDM服务端字符集，如果需要存储emoji表情符号，请选择utf8mb4,并设置RDS字符集也为utf8mb4。修改DDM服务端字符集时，DDM服务端字符序必须同步修改为对应类型的值。

        :return: The character_set_server of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._character_set_server

    @character_set_server.setter
    def character_set_server(self, character_set_server):
        r"""Sets the character_set_server of this UpdateParametersReqValues.

        DDM服务端字符集，如果需要存储emoji表情符号，请选择utf8mb4,并设置RDS字符集也为utf8mb4。修改DDM服务端字符集时，DDM服务端字符序必须同步修改为对应类型的值。

        :param character_set_server: The character_set_server of this UpdateParametersReqValues.
        :type character_set_server: str
        """
        self._character_set_server = character_set_server

    @property
    def collation_server(self):
        r"""Gets the collation_server of this UpdateParametersReqValues.

        DDM服务端字符序。修改DDM服务端字符序时，DDM服务端字符集必须同步修改为对应类型的值。

        :return: The collation_server of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._collation_server

    @collation_server.setter
    def collation_server(self, collation_server):
        r"""Sets the collation_server of this UpdateParametersReqValues.

        DDM服务端字符序。修改DDM服务端字符序时，DDM服务端字符集必须同步修改为对应类型的值。

        :param collation_server: The collation_server of this UpdateParametersReqValues.
        :type collation_server: str
        """
        self._collation_server = collation_server

    @property
    def concurrent_execution_level(self):
        r"""Gets the concurrent_execution_level of this UpdateParametersReqValues.

        逻辑表扫描时的分片并发执行级别: DATA_NODE: 分库间并行扫描，同一分库内各分片串行扫描;RDS_INSTANCE: RDS实例间并行扫描，同一RDS实例内各分片串行扫描;PHY_TABLE: 各物理分片全部并行扫描。

        :return: The concurrent_execution_level of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._concurrent_execution_level

    @concurrent_execution_level.setter
    def concurrent_execution_level(self, concurrent_execution_level):
        r"""Sets the concurrent_execution_level of this UpdateParametersReqValues.

        逻辑表扫描时的分片并发执行级别: DATA_NODE: 分库间并行扫描，同一分库内各分片串行扫描;RDS_INSTANCE: RDS实例间并行扫描，同一RDS实例内各分片串行扫描;PHY_TABLE: 各物理分片全部并行扫描。

        :param concurrent_execution_level: The concurrent_execution_level of this UpdateParametersReqValues.
        :type concurrent_execution_level: str
        """
        self._concurrent_execution_level = concurrent_execution_level

    @property
    def connection_idle_timeout(self):
        r"""Gets the connection_idle_timeout of this UpdateParametersReqValues.

        服务器关闭连接之前等待连接活动的秒数，以秒为单位，取值范围为60-28800，默认值28800，表示服务器关闭连接之前等待28800秒后，关闭连接。

        :return: The connection_idle_timeout of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._connection_idle_timeout

    @connection_idle_timeout.setter
    def connection_idle_timeout(self, connection_idle_timeout):
        r"""Sets the connection_idle_timeout of this UpdateParametersReqValues.

        服务器关闭连接之前等待连接活动的秒数，以秒为单位，取值范围为60-28800，默认值28800，表示服务器关闭连接之前等待28800秒后，关闭连接。

        :param connection_idle_timeout: The connection_idle_timeout of this UpdateParametersReqValues.
        :type connection_idle_timeout: str
        """
        self._connection_idle_timeout = connection_idle_timeout

    @property
    def enable_table_recycle(self):
        r"""Gets the enable_table_recycle of this UpdateParametersReqValues.

        是否开启表回收站。

        :return: The enable_table_recycle of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._enable_table_recycle

    @enable_table_recycle.setter
    def enable_table_recycle(self, enable_table_recycle):
        r"""Sets the enable_table_recycle of this UpdateParametersReqValues.

        是否开启表回收站。

        :param enable_table_recycle: The enable_table_recycle of this UpdateParametersReqValues.
        :type enable_table_recycle: str
        """
        self._enable_table_recycle = enable_table_recycle

    @property
    def insert_to_load_data(self):
        r"""Gets the insert_to_load_data of this UpdateParametersReqValues.

        insert 常量值使用load data执行。

        :return: The insert_to_load_data of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._insert_to_load_data

    @insert_to_load_data.setter
    def insert_to_load_data(self, insert_to_load_data):
        r"""Sets the insert_to_load_data of this UpdateParametersReqValues.

        insert 常量值使用load data执行。

        :param insert_to_load_data: The insert_to_load_data of this UpdateParametersReqValues.
        :type insert_to_load_data: str
        """
        self._insert_to_load_data = insert_to_load_data

    @property
    def live_transaction_timeout_on_shutdown(self):
        r"""Gets the live_transaction_timeout_on_shutdown of this UpdateParametersReqValues.

        在途事务等待时间窗口，以秒为单位，取值范围为0-100，默认值为1，表示服务器关闭前端连接之前等待1秒后关闭连接。

        :return: The live_transaction_timeout_on_shutdown of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._live_transaction_timeout_on_shutdown

    @live_transaction_timeout_on_shutdown.setter
    def live_transaction_timeout_on_shutdown(self, live_transaction_timeout_on_shutdown):
        r"""Sets the live_transaction_timeout_on_shutdown of this UpdateParametersReqValues.

        在途事务等待时间窗口，以秒为单位，取值范围为0-100，默认值为1，表示服务器关闭前端连接之前等待1秒后关闭连接。

        :param live_transaction_timeout_on_shutdown: The live_transaction_timeout_on_shutdown of this UpdateParametersReqValues.
        :type live_transaction_timeout_on_shutdown: str
        """
        self._live_transaction_timeout_on_shutdown = live_transaction_timeout_on_shutdown

    @property
    def long_query_time(self):
        r"""Gets the long_query_time of this UpdateParametersReqValues.

        记录慢查询的最小秒数,以秒为单位，取值范围为0.01-10，默认值为1，表示如果sql执行大于等于1秒就定义为慢sql。

        :return: The long_query_time of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._long_query_time

    @long_query_time.setter
    def long_query_time(self, long_query_time):
        r"""Sets the long_query_time of this UpdateParametersReqValues.

        记录慢查询的最小秒数,以秒为单位，取值范围为0.01-10，默认值为1，表示如果sql执行大于等于1秒就定义为慢sql。

        :param long_query_time: The long_query_time of this UpdateParametersReqValues.
        :type long_query_time: str
        """
        self._long_query_time = long_query_time

    @property
    def max_allowed_packet(self):
        r"""Gets the max_allowed_packet of this UpdateParametersReqValues.

        包或任何生成的中间字符串的最大值。包缓冲区初始化为net_buffer_length字节，但需要时可以增长到max_allowed_packet字节。该值默认很小，以捕获大的（可能是错误的）数据包。该值必须设置为1024的倍数。取值范围为1024~1073741824，默认值为16777216。

        :return: The max_allowed_packet of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._max_allowed_packet

    @max_allowed_packet.setter
    def max_allowed_packet(self, max_allowed_packet):
        r"""Sets the max_allowed_packet of this UpdateParametersReqValues.

        包或任何生成的中间字符串的最大值。包缓冲区初始化为net_buffer_length字节，但需要时可以增长到max_allowed_packet字节。该值默认很小，以捕获大的（可能是错误的）数据包。该值必须设置为1024的倍数。取值范围为1024~1073741824，默认值为16777216。

        :param max_allowed_packet: The max_allowed_packet of this UpdateParametersReqValues.
        :type max_allowed_packet: str
        """
        self._max_allowed_packet = max_allowed_packet

    @property
    def max_backend_connections(self):
        r"""Gets the max_backend_connections of this UpdateParametersReqValues.

        允许每个DDM节点同时连接RDS的最大客户端总数。0为默认值标识符,实际值等于(RDS的最大连接数-20)/DDM节点数。取值范围为0-10000000。

        :return: The max_backend_connections of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._max_backend_connections

    @max_backend_connections.setter
    def max_backend_connections(self, max_backend_connections):
        r"""Sets the max_backend_connections of this UpdateParametersReqValues.

        允许每个DDM节点同时连接RDS的最大客户端总数。0为默认值标识符,实际值等于(RDS的最大连接数-20)/DDM节点数。取值范围为0-10000000。

        :param max_backend_connections: The max_backend_connections of this UpdateParametersReqValues.
        :type max_backend_connections: str
        """
        self._max_backend_connections = max_backend_connections

    @property
    def max_connections(self):
        r"""Gets the max_connections of this UpdateParametersReqValues.

        允许同时连接的客户端总数。与后端RDS规格及数量有关。以个数为单位，取值范围为10-40000，默认值为20000，表示允许同时连接的客户端总数不能超过40000。

        :return: The max_connections of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        r"""Sets the max_connections of this UpdateParametersReqValues.

        允许同时连接的客户端总数。与后端RDS规格及数量有关。以个数为单位，取值范围为10-40000，默认值为20000，表示允许同时连接的客户端总数不能超过40000。

        :param max_connections: The max_connections of this UpdateParametersReqValues.
        :type max_connections: str
        """
        self._max_connections = max_connections

    @property
    def min_backend_connections(self):
        r"""Gets the min_backend_connections of this UpdateParametersReqValues.

        允许每个DDM节点同时连接RDS的最小客户端总数。默认值为10。取值范围为0-10000000。

        :return: The min_backend_connections of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._min_backend_connections

    @min_backend_connections.setter
    def min_backend_connections(self, min_backend_connections):
        r"""Sets the min_backend_connections of this UpdateParametersReqValues.

        允许每个DDM节点同时连接RDS的最小客户端总数。默认值为10。取值范围为0-10000000。

        :param min_backend_connections: The min_backend_connections of this UpdateParametersReqValues.
        :type min_backend_connections: str
        """
        self._min_backend_connections = min_backend_connections

    @property
    def not_from_pushdown(self):
        r"""Gets the not_from_pushdown of this UpdateParametersReqValues.

        是否强制下推查询语句中不含from的语句。

        :return: The not_from_pushdown of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._not_from_pushdown

    @not_from_pushdown.setter
    def not_from_pushdown(self, not_from_pushdown):
        r"""Sets the not_from_pushdown of this UpdateParametersReqValues.

        是否强制下推查询语句中不含from的语句。

        :param not_from_pushdown: The not_from_pushdown of this UpdateParametersReqValues.
        :type not_from_pushdown: str
        """
        self._not_from_pushdown = not_from_pushdown

    @property
    def seconds_behind_master(self):
        r"""Gets the seconds_behind_master of this UpdateParametersReqValues.

        主从rds节点延迟时间阈值，以秒为单位，取值范围为0-7200，默认值为30，表示主rds与从rds之间的数据同步时间值不能超过30秒，如果超过30s，读数据指令就不走当前读节点。

        :return: The seconds_behind_master of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._seconds_behind_master

    @seconds_behind_master.setter
    def seconds_behind_master(self, seconds_behind_master):
        r"""Sets the seconds_behind_master of this UpdateParametersReqValues.

        主从rds节点延迟时间阈值，以秒为单位，取值范围为0-7200，默认值为30，表示主rds与从rds之间的数据同步时间值不能超过30秒，如果超过30s，读数据指令就不走当前读节点。

        :param seconds_behind_master: The seconds_behind_master of this UpdateParametersReqValues.
        :type seconds_behind_master: str
        """
        self._seconds_behind_master = seconds_behind_master

    @property
    def sql_audit(self):
        r"""Gets the sql_audit of this UpdateParametersReqValues.

        开启或关闭SQL审计。

        :return: The sql_audit of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._sql_audit

    @sql_audit.setter
    def sql_audit(self, sql_audit):
        r"""Sets the sql_audit of this UpdateParametersReqValues.

        开启或关闭SQL审计。

        :param sql_audit: The sql_audit of this UpdateParametersReqValues.
        :type sql_audit: str
        """
        self._sql_audit = sql_audit

    @property
    def sql_execute_timeout(self):
        r"""Gets the sql_execute_timeout of this UpdateParametersReqValues.

        SQL执行超时秒数，以秒为单位，取值范围为100-28800，默认值28800，表示sql执行大于等于28800秒超时。

        :return: The sql_execute_timeout of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._sql_execute_timeout

    @sql_execute_timeout.setter
    def sql_execute_timeout(self, sql_execute_timeout):
        r"""Sets the sql_execute_timeout of this UpdateParametersReqValues.

        SQL执行超时秒数，以秒为单位，取值范围为100-28800，默认值28800，表示sql执行大于等于28800秒超时。

        :param sql_execute_timeout: The sql_execute_timeout of this UpdateParametersReqValues.
        :type sql_execute_timeout: str
        """
        self._sql_execute_timeout = sql_execute_timeout

    @property
    def support_ddl_binlog_hint(self):
        r"""Gets the support_ddl_binlog_hint of this UpdateParametersReqValues.

        DDL语句添加binlog hint。

        :return: The support_ddl_binlog_hint of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._support_ddl_binlog_hint

    @support_ddl_binlog_hint.setter
    def support_ddl_binlog_hint(self, support_ddl_binlog_hint):
        r"""Sets the support_ddl_binlog_hint of this UpdateParametersReqValues.

        DDL语句添加binlog hint。

        :param support_ddl_binlog_hint: The support_ddl_binlog_hint of this UpdateParametersReqValues.
        :type support_ddl_binlog_hint: str
        """
        self._support_ddl_binlog_hint = support_ddl_binlog_hint

    @property
    def transaction_policy(self):
        r"""Gets the transaction_policy of this UpdateParametersReqValues.

        XA：XA 事务，保证原子性，保证可见性；FREE：允许多写，不保证原子性，无性能损耗；NO_DTX：单分片事务。

        :return: The transaction_policy of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._transaction_policy

    @transaction_policy.setter
    def transaction_policy(self, transaction_policy):
        r"""Sets the transaction_policy of this UpdateParametersReqValues.

        XA：XA 事务，保证原子性，保证可见性；FREE：允许多写，不保证原子性，无性能损耗；NO_DTX：单分片事务。

        :param transaction_policy: The transaction_policy of this UpdateParametersReqValues.
        :type transaction_policy: str
        """
        self._transaction_policy = transaction_policy

    @property
    def ultimate_optimize(self):
        r"""Gets the ultimate_optimize of this UpdateParametersReqValues.

        开启或关闭优化器中的极致下推优化功能。

        :return: The ultimate_optimize of this UpdateParametersReqValues.
        :rtype: str
        """
        return self._ultimate_optimize

    @ultimate_optimize.setter
    def ultimate_optimize(self, ultimate_optimize):
        r"""Sets the ultimate_optimize of this UpdateParametersReqValues.

        开启或关闭优化器中的极致下推优化功能。

        :param ultimate_optimize: The ultimate_optimize of this UpdateParametersReqValues.
        :type ultimate_optimize: str
        """
        self._ultimate_optimize = ultimate_optimize

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
        if not isinstance(other, UpdateParametersReqValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
