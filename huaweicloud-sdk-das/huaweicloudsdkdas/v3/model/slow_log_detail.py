# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLogDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'occurrence_time': 'int',
        'sql_template_id': 'str',
        'original_sql': 'str',
        'db_name': 'str',
        'client': 'str',
        'user': 'str',
        'execute_time': 'float',
        'lock_wait_time': 'float',
        'rows_examined': 'int',
        'rows_sent': 'int',
        'tunable': 'bool',
        'end_time': 'int',
        'app_name': 'str',
        'rows_affected': 'int',
        'cpu_time': 'float',
        'logical_reads': 'int',
        'physical_reads': 'int',
        'writes': 'int',
        'sql_type': 'str',
        'collection': 'str',
        'key_examined': 'int',
        'node_id': 'str',
        'node_name': 'str',
        'killed': 'str'
    }

    attribute_map = {
        'occurrence_time': 'occurrence_time',
        'sql_template_id': 'sql_template_id',
        'original_sql': 'original_sql',
        'db_name': 'db_name',
        'client': 'client',
        'user': 'user',
        'execute_time': 'execute_time',
        'lock_wait_time': 'lock_wait_time',
        'rows_examined': 'rows_examined',
        'rows_sent': 'rows_sent',
        'tunable': 'tunable',
        'end_time': 'end_time',
        'app_name': 'app_name',
        'rows_affected': 'rows_affected',
        'cpu_time': 'cpu_time',
        'logical_reads': 'logical_reads',
        'physical_reads': 'physical_reads',
        'writes': 'writes',
        'sql_type': 'sql_type',
        'collection': 'collection',
        'key_examined': 'key_examined',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'killed': 'killed'
    }

    def __init__(self, occurrence_time=None, sql_template_id=None, original_sql=None, db_name=None, client=None, user=None, execute_time=None, lock_wait_time=None, rows_examined=None, rows_sent=None, tunable=None, end_time=None, app_name=None, rows_affected=None, cpu_time=None, logical_reads=None, physical_reads=None, writes=None, sql_type=None, collection=None, key_examined=None, node_id=None, node_name=None, killed=None):
        r"""SlowLogDetail

        The model defined in huaweicloud sdk

        :param occurrence_time: 执行时间(sqlserver、mongodb：结束时间；其他引擎：开始时间)（Unix timestamp），单位：毫秒
        :type occurrence_time: int
        :param sql_template_id: SQL模板ID
        :type sql_template_id: str
        :param original_sql: 原始SQL语句
        :type original_sql: str
        :param db_name: 数据库名
        :type db_name: str
        :param client: 客户端
        :type client: str
        :param user: 用户
        :type user: str
        :param execute_time: 执行耗时（秒）
        :type execute_time: float
        :param lock_wait_time: 锁等待耗时（秒）
        :type lock_wait_time: float
        :param rows_examined: 扫描行数
        :type rows_examined: int
        :param rows_sent: 返回行数
        :type rows_sent: int
        :param tunable: 是否可诊断优化
        :type tunable: bool
        :param end_time: sqlserver：执行完成时间（Unix timestamp），单位：毫秒
        :type end_time: int
        :param app_name: sqlserver：应用名
        :type app_name: str
        :param rows_affected: sqlserver：影响行数
        :type rows_affected: int
        :param cpu_time: sqlserver：CPU耗时（ms）
        :type cpu_time: float
        :param logical_reads: sqlserver：IO逻辑读
        :type logical_reads: int
        :param physical_reads: sqlserver：IO物理读
        :type physical_reads: int
        :param writes: sqlserver：IO写
        :type writes: int
        :param sql_type: SQL操作类型
        :type sql_type: str
        :param collection: mongodb：数据库表
        :type collection: str
        :param key_examined: mongodb：扫描索引数
        :type key_examined: int
        :param node_id: 节点ID
        :type node_id: str
        :param node_name: 节点名称
        :type node_name: str
        :param killed: 执行状态
        :type killed: str
        """
        
        

        self._occurrence_time = None
        self._sql_template_id = None
        self._original_sql = None
        self._db_name = None
        self._client = None
        self._user = None
        self._execute_time = None
        self._lock_wait_time = None
        self._rows_examined = None
        self._rows_sent = None
        self._tunable = None
        self._end_time = None
        self._app_name = None
        self._rows_affected = None
        self._cpu_time = None
        self._logical_reads = None
        self._physical_reads = None
        self._writes = None
        self._sql_type = None
        self._collection = None
        self._key_examined = None
        self._node_id = None
        self._node_name = None
        self._killed = None
        self.discriminator = None

        if occurrence_time is not None:
            self.occurrence_time = occurrence_time
        if sql_template_id is not None:
            self.sql_template_id = sql_template_id
        if original_sql is not None:
            self.original_sql = original_sql
        if db_name is not None:
            self.db_name = db_name
        if client is not None:
            self.client = client
        if user is not None:
            self.user = user
        if execute_time is not None:
            self.execute_time = execute_time
        if lock_wait_time is not None:
            self.lock_wait_time = lock_wait_time
        if rows_examined is not None:
            self.rows_examined = rows_examined
        if rows_sent is not None:
            self.rows_sent = rows_sent
        if tunable is not None:
            self.tunable = tunable
        if end_time is not None:
            self.end_time = end_time
        if app_name is not None:
            self.app_name = app_name
        if rows_affected is not None:
            self.rows_affected = rows_affected
        if cpu_time is not None:
            self.cpu_time = cpu_time
        if logical_reads is not None:
            self.logical_reads = logical_reads
        if physical_reads is not None:
            self.physical_reads = physical_reads
        if writes is not None:
            self.writes = writes
        if sql_type is not None:
            self.sql_type = sql_type
        if collection is not None:
            self.collection = collection
        if key_examined is not None:
            self.key_examined = key_examined
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if killed is not None:
            self.killed = killed

    @property
    def occurrence_time(self):
        r"""Gets the occurrence_time of this SlowLogDetail.

        执行时间(sqlserver、mongodb：结束时间；其他引擎：开始时间)（Unix timestamp），单位：毫秒

        :return: The occurrence_time of this SlowLogDetail.
        :rtype: int
        """
        return self._occurrence_time

    @occurrence_time.setter
    def occurrence_time(self, occurrence_time):
        r"""Sets the occurrence_time of this SlowLogDetail.

        执行时间(sqlserver、mongodb：结束时间；其他引擎：开始时间)（Unix timestamp），单位：毫秒

        :param occurrence_time: The occurrence_time of this SlowLogDetail.
        :type occurrence_time: int
        """
        self._occurrence_time = occurrence_time

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this SlowLogDetail.

        SQL模板ID

        :return: The sql_template_id of this SlowLogDetail.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this SlowLogDetail.

        SQL模板ID

        :param sql_template_id: The sql_template_id of this SlowLogDetail.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def original_sql(self):
        r"""Gets the original_sql of this SlowLogDetail.

        原始SQL语句

        :return: The original_sql of this SlowLogDetail.
        :rtype: str
        """
        return self._original_sql

    @original_sql.setter
    def original_sql(self, original_sql):
        r"""Sets the original_sql of this SlowLogDetail.

        原始SQL语句

        :param original_sql: The original_sql of this SlowLogDetail.
        :type original_sql: str
        """
        self._original_sql = original_sql

    @property
    def db_name(self):
        r"""Gets the db_name of this SlowLogDetail.

        数据库名

        :return: The db_name of this SlowLogDetail.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this SlowLogDetail.

        数据库名

        :param db_name: The db_name of this SlowLogDetail.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def client(self):
        r"""Gets the client of this SlowLogDetail.

        客户端

        :return: The client of this SlowLogDetail.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        r"""Sets the client of this SlowLogDetail.

        客户端

        :param client: The client of this SlowLogDetail.
        :type client: str
        """
        self._client = client

    @property
    def user(self):
        r"""Gets the user of this SlowLogDetail.

        用户

        :return: The user of this SlowLogDetail.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this SlowLogDetail.

        用户

        :param user: The user of this SlowLogDetail.
        :type user: str
        """
        self._user = user

    @property
    def execute_time(self):
        r"""Gets the execute_time of this SlowLogDetail.

        执行耗时（秒）

        :return: The execute_time of this SlowLogDetail.
        :rtype: float
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this SlowLogDetail.

        执行耗时（秒）

        :param execute_time: The execute_time of this SlowLogDetail.
        :type execute_time: float
        """
        self._execute_time = execute_time

    @property
    def lock_wait_time(self):
        r"""Gets the lock_wait_time of this SlowLogDetail.

        锁等待耗时（秒）

        :return: The lock_wait_time of this SlowLogDetail.
        :rtype: float
        """
        return self._lock_wait_time

    @lock_wait_time.setter
    def lock_wait_time(self, lock_wait_time):
        r"""Sets the lock_wait_time of this SlowLogDetail.

        锁等待耗时（秒）

        :param lock_wait_time: The lock_wait_time of this SlowLogDetail.
        :type lock_wait_time: float
        """
        self._lock_wait_time = lock_wait_time

    @property
    def rows_examined(self):
        r"""Gets the rows_examined of this SlowLogDetail.

        扫描行数

        :return: The rows_examined of this SlowLogDetail.
        :rtype: int
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        r"""Sets the rows_examined of this SlowLogDetail.

        扫描行数

        :param rows_examined: The rows_examined of this SlowLogDetail.
        :type rows_examined: int
        """
        self._rows_examined = rows_examined

    @property
    def rows_sent(self):
        r"""Gets the rows_sent of this SlowLogDetail.

        返回行数

        :return: The rows_sent of this SlowLogDetail.
        :rtype: int
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        r"""Sets the rows_sent of this SlowLogDetail.

        返回行数

        :param rows_sent: The rows_sent of this SlowLogDetail.
        :type rows_sent: int
        """
        self._rows_sent = rows_sent

    @property
    def tunable(self):
        r"""Gets the tunable of this SlowLogDetail.

        是否可诊断优化

        :return: The tunable of this SlowLogDetail.
        :rtype: bool
        """
        return self._tunable

    @tunable.setter
    def tunable(self, tunable):
        r"""Sets the tunable of this SlowLogDetail.

        是否可诊断优化

        :param tunable: The tunable of this SlowLogDetail.
        :type tunable: bool
        """
        self._tunable = tunable

    @property
    def end_time(self):
        r"""Gets the end_time of this SlowLogDetail.

        sqlserver：执行完成时间（Unix timestamp），单位：毫秒

        :return: The end_time of this SlowLogDetail.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SlowLogDetail.

        sqlserver：执行完成时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this SlowLogDetail.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def app_name(self):
        r"""Gets the app_name of this SlowLogDetail.

        sqlserver：应用名

        :return: The app_name of this SlowLogDetail.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this SlowLogDetail.

        sqlserver：应用名

        :param app_name: The app_name of this SlowLogDetail.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def rows_affected(self):
        r"""Gets the rows_affected of this SlowLogDetail.

        sqlserver：影响行数

        :return: The rows_affected of this SlowLogDetail.
        :rtype: int
        """
        return self._rows_affected

    @rows_affected.setter
    def rows_affected(self, rows_affected):
        r"""Sets the rows_affected of this SlowLogDetail.

        sqlserver：影响行数

        :param rows_affected: The rows_affected of this SlowLogDetail.
        :type rows_affected: int
        """
        self._rows_affected = rows_affected

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this SlowLogDetail.

        sqlserver：CPU耗时（ms）

        :return: The cpu_time of this SlowLogDetail.
        :rtype: float
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this SlowLogDetail.

        sqlserver：CPU耗时（ms）

        :param cpu_time: The cpu_time of this SlowLogDetail.
        :type cpu_time: float
        """
        self._cpu_time = cpu_time

    @property
    def logical_reads(self):
        r"""Gets the logical_reads of this SlowLogDetail.

        sqlserver：IO逻辑读

        :return: The logical_reads of this SlowLogDetail.
        :rtype: int
        """
        return self._logical_reads

    @logical_reads.setter
    def logical_reads(self, logical_reads):
        r"""Sets the logical_reads of this SlowLogDetail.

        sqlserver：IO逻辑读

        :param logical_reads: The logical_reads of this SlowLogDetail.
        :type logical_reads: int
        """
        self._logical_reads = logical_reads

    @property
    def physical_reads(self):
        r"""Gets the physical_reads of this SlowLogDetail.

        sqlserver：IO物理读

        :return: The physical_reads of this SlowLogDetail.
        :rtype: int
        """
        return self._physical_reads

    @physical_reads.setter
    def physical_reads(self, physical_reads):
        r"""Sets the physical_reads of this SlowLogDetail.

        sqlserver：IO物理读

        :param physical_reads: The physical_reads of this SlowLogDetail.
        :type physical_reads: int
        """
        self._physical_reads = physical_reads

    @property
    def writes(self):
        r"""Gets the writes of this SlowLogDetail.

        sqlserver：IO写

        :return: The writes of this SlowLogDetail.
        :rtype: int
        """
        return self._writes

    @writes.setter
    def writes(self, writes):
        r"""Sets the writes of this SlowLogDetail.

        sqlserver：IO写

        :param writes: The writes of this SlowLogDetail.
        :type writes: int
        """
        self._writes = writes

    @property
    def sql_type(self):
        r"""Gets the sql_type of this SlowLogDetail.

        SQL操作类型

        :return: The sql_type of this SlowLogDetail.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        r"""Sets the sql_type of this SlowLogDetail.

        SQL操作类型

        :param sql_type: The sql_type of this SlowLogDetail.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def collection(self):
        r"""Gets the collection of this SlowLogDetail.

        mongodb：数据库表

        :return: The collection of this SlowLogDetail.
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        r"""Sets the collection of this SlowLogDetail.

        mongodb：数据库表

        :param collection: The collection of this SlowLogDetail.
        :type collection: str
        """
        self._collection = collection

    @property
    def key_examined(self):
        r"""Gets the key_examined of this SlowLogDetail.

        mongodb：扫描索引数

        :return: The key_examined of this SlowLogDetail.
        :rtype: int
        """
        return self._key_examined

    @key_examined.setter
    def key_examined(self, key_examined):
        r"""Sets the key_examined of this SlowLogDetail.

        mongodb：扫描索引数

        :param key_examined: The key_examined of this SlowLogDetail.
        :type key_examined: int
        """
        self._key_examined = key_examined

    @property
    def node_id(self):
        r"""Gets the node_id of this SlowLogDetail.

        节点ID

        :return: The node_id of this SlowLogDetail.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SlowLogDetail.

        节点ID

        :param node_id: The node_id of this SlowLogDetail.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this SlowLogDetail.

        节点名称

        :return: The node_name of this SlowLogDetail.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this SlowLogDetail.

        节点名称

        :param node_name: The node_name of this SlowLogDetail.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def killed(self):
        r"""Gets the killed of this SlowLogDetail.

        执行状态

        :return: The killed of this SlowLogDetail.
        :rtype: str
        """
        return self._killed

    @killed.setter
    def killed(self, killed):
        r"""Sets the killed of this SlowLogDetail.

        执行状态

        :param killed: The killed of this SlowLogDetail.
        :type killed: str
        """
        self._killed = killed

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
        if not isinstance(other, SlowLogDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
