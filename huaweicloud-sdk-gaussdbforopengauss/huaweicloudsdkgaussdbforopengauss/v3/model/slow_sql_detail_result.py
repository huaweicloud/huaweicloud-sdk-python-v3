# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowSqlDetailResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'schema_name': 'str',
        'sql': 'str',
        'sql_id': 'str',
        'user_name': 'str',
        'client_ip': 'str',
        'client_port': 'str',
        'node_id': 'str',
        'node_name': 'str',
        'sql_text': 'str',
        'query_plan': 'str',
        'start_time': 'int',
        'finish_time': 'int',
        'returned_rows': 'int',
        'fetched_rows': 'int',
        'fetched_pages': 'int',
        'hit_pages': 'int',
        'total_time': 'int',
        'cpu_time': 'int',
        'plan_time': 'int',
        'io_time': 'int',
        'lock_count': 'int',
        'lock_time': 'int'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'sql': 'sql',
        'sql_id': 'sql_id',
        'user_name': 'user_name',
        'client_ip': 'client_ip',
        'client_port': 'client_port',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'sql_text': 'sql_text',
        'query_plan': 'query_plan',
        'start_time': 'start_time',
        'finish_time': 'finish_time',
        'returned_rows': 'returned_rows',
        'fetched_rows': 'fetched_rows',
        'fetched_pages': 'fetched_pages',
        'hit_pages': 'hit_pages',
        'total_time': 'total_time',
        'cpu_time': 'cpu_time',
        'plan_time': 'plan_time',
        'io_time': 'io_time',
        'lock_count': 'lock_count',
        'lock_time': 'lock_time'
    }

    def __init__(self, db_name=None, schema_name=None, sql=None, sql_id=None, user_name=None, client_ip=None, client_port=None, node_id=None, node_name=None, sql_text=None, query_plan=None, start_time=None, finish_time=None, returned_rows=None, fetched_rows=None, fetched_pages=None, hit_pages=None, total_time=None, cpu_time=None, plan_time=None, io_time=None, lock_count=None, lock_time=None):
        r"""SlowSqlDetailResult

        The model defined in huaweicloud sdk

        :param db_name: **参数解释**: 数据库名称。 **取值范围**: 不涉及。
        :type db_name: str
        :param schema_name: **参数解释**: SCHEMA名称。 **取值范围**: 不涉及。
        :type schema_name: str
        :param sql: **参数解释**: 变量替换后的完整SQL。当sql_text不返回变量值时，sql返回空字符串。 **取值范围**: 不涉及。
        :type sql: str
        :param sql_id: **参数解释**: SQL ID。 **取值范围**: 不涉及。
        :type sql_id: str
        :param user_name: **参数解释**: 用户名称。 **取值范围**: 不涉及。
        :type user_name: str
        :param client_ip: **参数解释**: 客户端IP。 **取值范围**: 不涉及。
        :type client_ip: str
        :param client_port: **参数解释**: 客户端端口。 **取值范围**: 不涉及。
        :type client_port: str
        :param node_id: **参数解释**: 节点ID。 **取值范围**: 不涉及。
        :type node_id: str
        :param node_name: **参数解释**: 节点名称。 **取值范围**: 不涉及。
        :type node_name: str
        :param sql_text: **参数解释**: SQL模版。 **取值范围**: 不涉及。
        :type sql_text: str
        :param query_plan: **参数解释**: 执行计划。 **取值范围**: 不涉及。
        :type query_plan: str
        :param start_time: **参数解释**: 开始时间UTC时间。 **取值范围**: 格式为yyyy-mm-ddThh:mm:ss+0000。
        :type start_time: int
        :param finish_time: **参数解释**: 结束时间UTC时间。 **取值范围**: 格式为yyyy-mm-ddThh:mm:ss+0000。
        :type finish_time: int
        :param returned_rows: **参数解释**: 返回行。 **取值范围**: 不涉及。
        :type returned_rows: int
        :param fetched_rows: **参数解释**: 扫描行。 **取值范围**: 不涉及。
        :type fetched_rows: int
        :param fetched_pages: **参数解释**: 扫描页。 **取值范围**: 不涉及。
        :type fetched_pages: int
        :param hit_pages: **参数解释**: 命中页。 **取值范围**: 不涉及。
        :type hit_pages: int
        :param total_time: **参数解释**: 总耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type total_time: int
        :param cpu_time: **参数解释**: CPU耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type cpu_time: int
        :param plan_time: **参数解释**: 计划耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type plan_time: int
        :param io_time: **参数解释**: IO耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type io_time: int
        :param lock_count: **参数解释**: 加锁次数。 **取值范围**: 不涉及。
        :type lock_count: int
        :param lock_time: **参数解释**: 加锁耗时(单位：微秒)。 **取值范围**: 不涉及。
        :type lock_time: int
        """
        
        

        self._db_name = None
        self._schema_name = None
        self._sql = None
        self._sql_id = None
        self._user_name = None
        self._client_ip = None
        self._client_port = None
        self._node_id = None
        self._node_name = None
        self._sql_text = None
        self._query_plan = None
        self._start_time = None
        self._finish_time = None
        self._returned_rows = None
        self._fetched_rows = None
        self._fetched_pages = None
        self._hit_pages = None
        self._total_time = None
        self._cpu_time = None
        self._plan_time = None
        self._io_time = None
        self._lock_count = None
        self._lock_time = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if sql is not None:
            self.sql = sql
        if sql_id is not None:
            self.sql_id = sql_id
        if user_name is not None:
            self.user_name = user_name
        if client_ip is not None:
            self.client_ip = client_ip
        if client_port is not None:
            self.client_port = client_port
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if sql_text is not None:
            self.sql_text = sql_text
        if query_plan is not None:
            self.query_plan = query_plan
        if start_time is not None:
            self.start_time = start_time
        if finish_time is not None:
            self.finish_time = finish_time
        if returned_rows is not None:
            self.returned_rows = returned_rows
        if fetched_rows is not None:
            self.fetched_rows = fetched_rows
        if fetched_pages is not None:
            self.fetched_pages = fetched_pages
        if hit_pages is not None:
            self.hit_pages = hit_pages
        if total_time is not None:
            self.total_time = total_time
        if cpu_time is not None:
            self.cpu_time = cpu_time
        if plan_time is not None:
            self.plan_time = plan_time
        if io_time is not None:
            self.io_time = io_time
        if lock_count is not None:
            self.lock_count = lock_count
        if lock_time is not None:
            self.lock_time = lock_time

    @property
    def db_name(self):
        r"""Gets the db_name of this SlowSqlDetailResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :return: The db_name of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this SlowSqlDetailResult.

        **参数解释**: 数据库名称。 **取值范围**: 不涉及。

        :param db_name: The db_name of this SlowSqlDetailResult.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this SlowSqlDetailResult.

        **参数解释**: SCHEMA名称。 **取值范围**: 不涉及。

        :return: The schema_name of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this SlowSqlDetailResult.

        **参数解释**: SCHEMA名称。 **取值范围**: 不涉及。

        :param schema_name: The schema_name of this SlowSqlDetailResult.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def sql(self):
        r"""Gets the sql of this SlowSqlDetailResult.

        **参数解释**: 变量替换后的完整SQL。当sql_text不返回变量值时，sql返回空字符串。 **取值范围**: 不涉及。

        :return: The sql of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this SlowSqlDetailResult.

        **参数解释**: 变量替换后的完整SQL。当sql_text不返回变量值时，sql返回空字符串。 **取值范围**: 不涉及。

        :param sql: The sql of this SlowSqlDetailResult.
        :type sql: str
        """
        self._sql = sql

    @property
    def sql_id(self):
        r"""Gets the sql_id of this SlowSqlDetailResult.

        **参数解释**: SQL ID。 **取值范围**: 不涉及。

        :return: The sql_id of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        r"""Sets the sql_id of this SlowSqlDetailResult.

        **参数解释**: SQL ID。 **取值范围**: 不涉及。

        :param sql_id: The sql_id of this SlowSqlDetailResult.
        :type sql_id: str
        """
        self._sql_id = sql_id

    @property
    def user_name(self):
        r"""Gets the user_name of this SlowSqlDetailResult.

        **参数解释**: 用户名称。 **取值范围**: 不涉及。

        :return: The user_name of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this SlowSqlDetailResult.

        **参数解释**: 用户名称。 **取值范围**: 不涉及。

        :param user_name: The user_name of this SlowSqlDetailResult.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def client_ip(self):
        r"""Gets the client_ip of this SlowSqlDetailResult.

        **参数解释**: 客户端IP。 **取值范围**: 不涉及。

        :return: The client_ip of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this SlowSqlDetailResult.

        **参数解释**: 客户端IP。 **取值范围**: 不涉及。

        :param client_ip: The client_ip of this SlowSqlDetailResult.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def client_port(self):
        r"""Gets the client_port of this SlowSqlDetailResult.

        **参数解释**: 客户端端口。 **取值范围**: 不涉及。

        :return: The client_port of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this SlowSqlDetailResult.

        **参数解释**: 客户端端口。 **取值范围**: 不涉及。

        :param client_port: The client_port of this SlowSqlDetailResult.
        :type client_port: str
        """
        self._client_port = client_port

    @property
    def node_id(self):
        r"""Gets the node_id of this SlowSqlDetailResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :return: The node_id of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SlowSqlDetailResult.

        **参数解释**: 节点ID。 **取值范围**: 不涉及。

        :param node_id: The node_id of this SlowSqlDetailResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this SlowSqlDetailResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。

        :return: The node_name of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this SlowSqlDetailResult.

        **参数解释**: 节点名称。 **取值范围**: 不涉及。

        :param node_name: The node_name of this SlowSqlDetailResult.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def sql_text(self):
        r"""Gets the sql_text of this SlowSqlDetailResult.

        **参数解释**: SQL模版。 **取值范围**: 不涉及。

        :return: The sql_text of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        r"""Sets the sql_text of this SlowSqlDetailResult.

        **参数解释**: SQL模版。 **取值范围**: 不涉及。

        :param sql_text: The sql_text of this SlowSqlDetailResult.
        :type sql_text: str
        """
        self._sql_text = sql_text

    @property
    def query_plan(self):
        r"""Gets the query_plan of this SlowSqlDetailResult.

        **参数解释**: 执行计划。 **取值范围**: 不涉及。

        :return: The query_plan of this SlowSqlDetailResult.
        :rtype: str
        """
        return self._query_plan

    @query_plan.setter
    def query_plan(self, query_plan):
        r"""Sets the query_plan of this SlowSqlDetailResult.

        **参数解释**: 执行计划。 **取值范围**: 不涉及。

        :param query_plan: The query_plan of this SlowSqlDetailResult.
        :type query_plan: str
        """
        self._query_plan = query_plan

    @property
    def start_time(self):
        r"""Gets the start_time of this SlowSqlDetailResult.

        **参数解释**: 开始时间UTC时间。 **取值范围**: 格式为yyyy-mm-ddThh:mm:ss+0000。

        :return: The start_time of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SlowSqlDetailResult.

        **参数解释**: 开始时间UTC时间。 **取值范围**: 格式为yyyy-mm-ddThh:mm:ss+0000。

        :param start_time: The start_time of this SlowSqlDetailResult.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this SlowSqlDetailResult.

        **参数解释**: 结束时间UTC时间。 **取值范围**: 格式为yyyy-mm-ddThh:mm:ss+0000。

        :return: The finish_time of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this SlowSqlDetailResult.

        **参数解释**: 结束时间UTC时间。 **取值范围**: 格式为yyyy-mm-ddThh:mm:ss+0000。

        :param finish_time: The finish_time of this SlowSqlDetailResult.
        :type finish_time: int
        """
        self._finish_time = finish_time

    @property
    def returned_rows(self):
        r"""Gets the returned_rows of this SlowSqlDetailResult.

        **参数解释**: 返回行。 **取值范围**: 不涉及。

        :return: The returned_rows of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._returned_rows

    @returned_rows.setter
    def returned_rows(self, returned_rows):
        r"""Sets the returned_rows of this SlowSqlDetailResult.

        **参数解释**: 返回行。 **取值范围**: 不涉及。

        :param returned_rows: The returned_rows of this SlowSqlDetailResult.
        :type returned_rows: int
        """
        self._returned_rows = returned_rows

    @property
    def fetched_rows(self):
        r"""Gets the fetched_rows of this SlowSqlDetailResult.

        **参数解释**: 扫描行。 **取值范围**: 不涉及。

        :return: The fetched_rows of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._fetched_rows

    @fetched_rows.setter
    def fetched_rows(self, fetched_rows):
        r"""Sets the fetched_rows of this SlowSqlDetailResult.

        **参数解释**: 扫描行。 **取值范围**: 不涉及。

        :param fetched_rows: The fetched_rows of this SlowSqlDetailResult.
        :type fetched_rows: int
        """
        self._fetched_rows = fetched_rows

    @property
    def fetched_pages(self):
        r"""Gets the fetched_pages of this SlowSqlDetailResult.

        **参数解释**: 扫描页。 **取值范围**: 不涉及。

        :return: The fetched_pages of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._fetched_pages

    @fetched_pages.setter
    def fetched_pages(self, fetched_pages):
        r"""Sets the fetched_pages of this SlowSqlDetailResult.

        **参数解释**: 扫描页。 **取值范围**: 不涉及。

        :param fetched_pages: The fetched_pages of this SlowSqlDetailResult.
        :type fetched_pages: int
        """
        self._fetched_pages = fetched_pages

    @property
    def hit_pages(self):
        r"""Gets the hit_pages of this SlowSqlDetailResult.

        **参数解释**: 命中页。 **取值范围**: 不涉及。

        :return: The hit_pages of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._hit_pages

    @hit_pages.setter
    def hit_pages(self, hit_pages):
        r"""Sets the hit_pages of this SlowSqlDetailResult.

        **参数解释**: 命中页。 **取值范围**: 不涉及。

        :param hit_pages: The hit_pages of this SlowSqlDetailResult.
        :type hit_pages: int
        """
        self._hit_pages = hit_pages

    @property
    def total_time(self):
        r"""Gets the total_time of this SlowSqlDetailResult.

        **参数解释**: 总耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The total_time of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        r"""Sets the total_time of this SlowSqlDetailResult.

        **参数解释**: 总耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param total_time: The total_time of this SlowSqlDetailResult.
        :type total_time: int
        """
        self._total_time = total_time

    @property
    def cpu_time(self):
        r"""Gets the cpu_time of this SlowSqlDetailResult.

        **参数解释**: CPU耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The cpu_time of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._cpu_time

    @cpu_time.setter
    def cpu_time(self, cpu_time):
        r"""Sets the cpu_time of this SlowSqlDetailResult.

        **参数解释**: CPU耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param cpu_time: The cpu_time of this SlowSqlDetailResult.
        :type cpu_time: int
        """
        self._cpu_time = cpu_time

    @property
    def plan_time(self):
        r"""Gets the plan_time of this SlowSqlDetailResult.

        **参数解释**: 计划耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The plan_time of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._plan_time

    @plan_time.setter
    def plan_time(self, plan_time):
        r"""Sets the plan_time of this SlowSqlDetailResult.

        **参数解释**: 计划耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param plan_time: The plan_time of this SlowSqlDetailResult.
        :type plan_time: int
        """
        self._plan_time = plan_time

    @property
    def io_time(self):
        r"""Gets the io_time of this SlowSqlDetailResult.

        **参数解释**: IO耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The io_time of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._io_time

    @io_time.setter
    def io_time(self, io_time):
        r"""Sets the io_time of this SlowSqlDetailResult.

        **参数解释**: IO耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param io_time: The io_time of this SlowSqlDetailResult.
        :type io_time: int
        """
        self._io_time = io_time

    @property
    def lock_count(self):
        r"""Gets the lock_count of this SlowSqlDetailResult.

        **参数解释**: 加锁次数。 **取值范围**: 不涉及。

        :return: The lock_count of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._lock_count

    @lock_count.setter
    def lock_count(self, lock_count):
        r"""Sets the lock_count of this SlowSqlDetailResult.

        **参数解释**: 加锁次数。 **取值范围**: 不涉及。

        :param lock_count: The lock_count of this SlowSqlDetailResult.
        :type lock_count: int
        """
        self._lock_count = lock_count

    @property
    def lock_time(self):
        r"""Gets the lock_time of this SlowSqlDetailResult.

        **参数解释**: 加锁耗时(单位：微秒)。 **取值范围**: 不涉及。

        :return: The lock_time of this SlowSqlDetailResult.
        :rtype: int
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        r"""Sets the lock_time of this SlowSqlDetailResult.

        **参数解释**: 加锁耗时(单位：微秒)。 **取值范围**: 不涉及。

        :param lock_time: The lock_time of this SlowSqlDetailResult.
        :type lock_time: int
        """
        self._lock_time = lock_time

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
        if not isinstance(other, SlowSqlDetailResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
