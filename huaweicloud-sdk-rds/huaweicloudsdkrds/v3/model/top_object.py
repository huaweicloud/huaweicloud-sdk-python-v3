# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'row_id': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'object_name': 'str',
        'object_id': 'str',
        'object_type': 'str',
        'sql_statement': 'str',
        'execution_count': 'str',
        'plan_generation_num': 'str',
        'last_execution_time': 'str',
        'avg_worker_time': 'str',
        'total_worker_time': 'str',
        'last_worker_time': 'str',
        'min_worker_time': 'str',
        'max_worker_time': 'str',
        'avg_logical_reads': 'str',
        'total_logical_reads': 'str',
        'last_logical_reads': 'str',
        'min_logical_reads': 'str',
        'max_logical_reads': 'str',
        'avg_logical_writes': 'str',
        'total_logical_writes': 'str',
        'last_logical_writes': 'str',
        'min_logical_writes': 'str',
        'max_logical_writes': 'str',
        'avg_logical_io': 'str',
        'total_logical_io': 'str',
        'last_logical_io': 'str',
        'min_logical_io': 'str',
        'max_logical_io': 'str',
        'avg_physical_reads': 'str',
        'total_physical_reads': 'str',
        'last_physical_reads': 'str',
        'min_physical_reads': 'str',
        'max_physical_reads': 'str',
        'avg_elapsed_time': 'str',
        'total_elapsed_time': 'str',
        'last_elapsed_time': 'str',
        'min_elapsed_time': 'str',
        'max_elapsed_time': 'str',
        'avg_rows': 'str',
        'total_rows': 'str',
        'last_rows': 'str',
        'min_rows': 'str',
        'max_rows': 'str'
    }

    attribute_map = {
        'row_id': 'row_id',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'object_name': 'object_name',
        'object_id': 'object_id',
        'object_type': 'object_type',
        'sql_statement': 'sql_statement',
        'execution_count': 'execution_count',
        'plan_generation_num': 'plan_generation_num',
        'last_execution_time': 'last_execution_time',
        'avg_worker_time': 'avg_worker_time',
        'total_worker_time': 'total_worker_time',
        'last_worker_time': 'last_worker_time',
        'min_worker_time': 'min_worker_time',
        'max_worker_time': 'max_worker_time',
        'avg_logical_reads': 'avg_logical_reads',
        'total_logical_reads': 'total_logical_reads',
        'last_logical_reads': 'last_logical_reads',
        'min_logical_reads': 'min_logical_reads',
        'max_logical_reads': 'max_logical_reads',
        'avg_logical_writes': 'avg_logical_writes',
        'total_logical_writes': 'total_logical_writes',
        'last_logical_writes': 'last_logical_writes',
        'min_logical_writes': 'min_logical_writes',
        'max_logical_writes': 'max_logical_writes',
        'avg_logical_io': 'avg_logical_io',
        'total_logical_io': 'total_logical_io',
        'last_logical_io': 'last_logical_io',
        'min_logical_io': 'min_logical_io',
        'max_logical_io': 'max_logical_io',
        'avg_physical_reads': 'avg_physical_reads',
        'total_physical_reads': 'total_physical_reads',
        'last_physical_reads': 'last_physical_reads',
        'min_physical_reads': 'min_physical_reads',
        'max_physical_reads': 'max_physical_reads',
        'avg_elapsed_time': 'avg_elapsed_time',
        'total_elapsed_time': 'total_elapsed_time',
        'last_elapsed_time': 'last_elapsed_time',
        'min_elapsed_time': 'min_elapsed_time',
        'max_elapsed_time': 'max_elapsed_time',
        'avg_rows': 'avg_rows',
        'total_rows': 'total_rows',
        'last_rows': 'last_rows',
        'min_rows': 'min_rows',
        'max_rows': 'max_rows'
    }

    def __init__(self, row_id=None, database_name=None, schema_name=None, object_name=None, object_id=None, object_type=None, sql_statement=None, execution_count=None, plan_generation_num=None, last_execution_time=None, avg_worker_time=None, total_worker_time=None, last_worker_time=None, min_worker_time=None, max_worker_time=None, avg_logical_reads=None, total_logical_reads=None, last_logical_reads=None, min_logical_reads=None, max_logical_reads=None, avg_logical_writes=None, total_logical_writes=None, last_logical_writes=None, min_logical_writes=None, max_logical_writes=None, avg_logical_io=None, total_logical_io=None, last_logical_io=None, min_logical_io=None, max_logical_io=None, avg_physical_reads=None, total_physical_reads=None, last_physical_reads=None, min_physical_reads=None, max_physical_reads=None, avg_elapsed_time=None, total_elapsed_time=None, last_elapsed_time=None, min_elapsed_time=None, max_elapsed_time=None, avg_rows=None, total_rows=None, last_rows=None, min_rows=None, max_rows=None):
        r"""TopObject

        The model defined in huaweicloud sdk

        :param row_id: id
        :type row_id: str
        :param database_name: 数据库名
        :type database_name: str
        :param schema_name: 模式
        :type schema_name: str
        :param object_name: 对象名
        :type object_name: str
        :param object_id: 对象id
        :type object_id: str
        :param object_type: 对象类型
        :type object_type: str
        :param sql_statement: sql文本
        :type sql_statement: str
        :param execution_count: 执行次数
        :type execution_count: str
        :param plan_generation_num: 获取执行计划次数
        :type plan_generation_num: str
        :param last_execution_time: 最近执行时间
        :type last_execution_time: str
        :param avg_worker_time: 平均cpu耗时(单位为毫秒)
        :type avg_worker_time: str
        :param total_worker_time: 总cpu耗时(单位为毫秒)
        :type total_worker_time: str
        :param last_worker_time: 最近cpu耗时(单位为毫秒)
        :type last_worker_time: str
        :param min_worker_time: 最小cpu耗时(单位为毫秒)
        :type min_worker_time: str
        :param max_worker_time: 最大cpu耗时(单位为毫秒)
        :type max_worker_time: str
        :param avg_logical_reads: 平均逻辑读
        :type avg_logical_reads: str
        :param total_logical_reads: 总共逻辑读
        :type total_logical_reads: str
        :param last_logical_reads: 最近逻辑读
        :type last_logical_reads: str
        :param min_logical_reads: 最小逻辑读
        :type min_logical_reads: str
        :param max_logical_reads: 最大逻辑读
        :type max_logical_reads: str
        :param avg_logical_writes: 平均逻辑写
        :type avg_logical_writes: str
        :param total_logical_writes: 总共逻辑写
        :type total_logical_writes: str
        :param last_logical_writes: 最近逻辑写
        :type last_logical_writes: str
        :param min_logical_writes: 最小逻辑写
        :type min_logical_writes: str
        :param max_logical_writes: 最大逻辑写
        :type max_logical_writes: str
        :param avg_logical_io: 平均逻辑io
        :type avg_logical_io: str
        :param total_logical_io: 总共逻辑io
        :type total_logical_io: str
        :param last_logical_io: 最近逻辑io
        :type last_logical_io: str
        :param min_logical_io: 最小逻辑io
        :type min_logical_io: str
        :param max_logical_io: 最大逻辑io
        :type max_logical_io: str
        :param avg_physical_reads: 平均物理读
        :type avg_physical_reads: str
        :param total_physical_reads: 总共物理读
        :type total_physical_reads: str
        :param last_physical_reads: 最近物理读
        :type last_physical_reads: str
        :param min_physical_reads: 最小物理读
        :type min_physical_reads: str
        :param max_physical_reads: 最大物理读
        :type max_physical_reads: str
        :param avg_elapsed_time: 平均执行耗时
        :type avg_elapsed_time: str
        :param total_elapsed_time: 总共执行耗时
        :type total_elapsed_time: str
        :param last_elapsed_time: 最近执行耗时
        :type last_elapsed_time: str
        :param min_elapsed_time: 最小执行耗时
        :type min_elapsed_time: str
        :param max_elapsed_time: 最大执行耗时
        :type max_elapsed_time: str
        :param avg_rows: 平均返回行
        :type avg_rows: str
        :param total_rows: 总返回行
        :type total_rows: str
        :param last_rows: 最近返回行
        :type last_rows: str
        :param min_rows: 最小返回行
        :type min_rows: str
        :param max_rows: 最大返回行
        :type max_rows: str
        """
        
        

        self._row_id = None
        self._database_name = None
        self._schema_name = None
        self._object_name = None
        self._object_id = None
        self._object_type = None
        self._sql_statement = None
        self._execution_count = None
        self._plan_generation_num = None
        self._last_execution_time = None
        self._avg_worker_time = None
        self._total_worker_time = None
        self._last_worker_time = None
        self._min_worker_time = None
        self._max_worker_time = None
        self._avg_logical_reads = None
        self._total_logical_reads = None
        self._last_logical_reads = None
        self._min_logical_reads = None
        self._max_logical_reads = None
        self._avg_logical_writes = None
        self._total_logical_writes = None
        self._last_logical_writes = None
        self._min_logical_writes = None
        self._max_logical_writes = None
        self._avg_logical_io = None
        self._total_logical_io = None
        self._last_logical_io = None
        self._min_logical_io = None
        self._max_logical_io = None
        self._avg_physical_reads = None
        self._total_physical_reads = None
        self._last_physical_reads = None
        self._min_physical_reads = None
        self._max_physical_reads = None
        self._avg_elapsed_time = None
        self._total_elapsed_time = None
        self._last_elapsed_time = None
        self._min_elapsed_time = None
        self._max_elapsed_time = None
        self._avg_rows = None
        self._total_rows = None
        self._last_rows = None
        self._min_rows = None
        self._max_rows = None
        self.discriminator = None

        self.row_id = row_id
        self.database_name = database_name
        self.schema_name = schema_name
        if object_name is not None:
            self.object_name = object_name
        if object_id is not None:
            self.object_id = object_id
        if object_type is not None:
            self.object_type = object_type
        if sql_statement is not None:
            self.sql_statement = sql_statement
        if execution_count is not None:
            self.execution_count = execution_count
        if plan_generation_num is not None:
            self.plan_generation_num = plan_generation_num
        if last_execution_time is not None:
            self.last_execution_time = last_execution_time
        if avg_worker_time is not None:
            self.avg_worker_time = avg_worker_time
        if total_worker_time is not None:
            self.total_worker_time = total_worker_time
        if last_worker_time is not None:
            self.last_worker_time = last_worker_time
        if min_worker_time is not None:
            self.min_worker_time = min_worker_time
        if max_worker_time is not None:
            self.max_worker_time = max_worker_time
        if avg_logical_reads is not None:
            self.avg_logical_reads = avg_logical_reads
        if total_logical_reads is not None:
            self.total_logical_reads = total_logical_reads
        if last_logical_reads is not None:
            self.last_logical_reads = last_logical_reads
        if min_logical_reads is not None:
            self.min_logical_reads = min_logical_reads
        if max_logical_reads is not None:
            self.max_logical_reads = max_logical_reads
        if avg_logical_writes is not None:
            self.avg_logical_writes = avg_logical_writes
        if total_logical_writes is not None:
            self.total_logical_writes = total_logical_writes
        if last_logical_writes is not None:
            self.last_logical_writes = last_logical_writes
        if min_logical_writes is not None:
            self.min_logical_writes = min_logical_writes
        if max_logical_writes is not None:
            self.max_logical_writes = max_logical_writes
        if avg_logical_io is not None:
            self.avg_logical_io = avg_logical_io
        if total_logical_io is not None:
            self.total_logical_io = total_logical_io
        if last_logical_io is not None:
            self.last_logical_io = last_logical_io
        if min_logical_io is not None:
            self.min_logical_io = min_logical_io
        if max_logical_io is not None:
            self.max_logical_io = max_logical_io
        if avg_physical_reads is not None:
            self.avg_physical_reads = avg_physical_reads
        if total_physical_reads is not None:
            self.total_physical_reads = total_physical_reads
        if last_physical_reads is not None:
            self.last_physical_reads = last_physical_reads
        if min_physical_reads is not None:
            self.min_physical_reads = min_physical_reads
        if max_physical_reads is not None:
            self.max_physical_reads = max_physical_reads
        if avg_elapsed_time is not None:
            self.avg_elapsed_time = avg_elapsed_time
        if total_elapsed_time is not None:
            self.total_elapsed_time = total_elapsed_time
        if last_elapsed_time is not None:
            self.last_elapsed_time = last_elapsed_time
        if min_elapsed_time is not None:
            self.min_elapsed_time = min_elapsed_time
        if max_elapsed_time is not None:
            self.max_elapsed_time = max_elapsed_time
        if avg_rows is not None:
            self.avg_rows = avg_rows
        if total_rows is not None:
            self.total_rows = total_rows
        if last_rows is not None:
            self.last_rows = last_rows
        if min_rows is not None:
            self.min_rows = min_rows
        if max_rows is not None:
            self.max_rows = max_rows

    @property
    def row_id(self):
        r"""Gets the row_id of this TopObject.

        id

        :return: The row_id of this TopObject.
        :rtype: str
        """
        return self._row_id

    @row_id.setter
    def row_id(self, row_id):
        r"""Sets the row_id of this TopObject.

        id

        :param row_id: The row_id of this TopObject.
        :type row_id: str
        """
        self._row_id = row_id

    @property
    def database_name(self):
        r"""Gets the database_name of this TopObject.

        数据库名

        :return: The database_name of this TopObject.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this TopObject.

        数据库名

        :param database_name: The database_name of this TopObject.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this TopObject.

        模式

        :return: The schema_name of this TopObject.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this TopObject.

        模式

        :param schema_name: The schema_name of this TopObject.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def object_name(self):
        r"""Gets the object_name of this TopObject.

        对象名

        :return: The object_name of this TopObject.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this TopObject.

        对象名

        :param object_name: The object_name of this TopObject.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def object_id(self):
        r"""Gets the object_id of this TopObject.

        对象id

        :return: The object_id of this TopObject.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this TopObject.

        对象id

        :param object_id: The object_id of this TopObject.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def object_type(self):
        r"""Gets the object_type of this TopObject.

        对象类型

        :return: The object_type of this TopObject.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this TopObject.

        对象类型

        :param object_type: The object_type of this TopObject.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this TopObject.

        sql文本

        :return: The sql_statement of this TopObject.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this TopObject.

        sql文本

        :param sql_statement: The sql_statement of this TopObject.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def execution_count(self):
        r"""Gets the execution_count of this TopObject.

        执行次数

        :return: The execution_count of this TopObject.
        :rtype: str
        """
        return self._execution_count

    @execution_count.setter
    def execution_count(self, execution_count):
        r"""Sets the execution_count of this TopObject.

        执行次数

        :param execution_count: The execution_count of this TopObject.
        :type execution_count: str
        """
        self._execution_count = execution_count

    @property
    def plan_generation_num(self):
        r"""Gets the plan_generation_num of this TopObject.

        获取执行计划次数

        :return: The plan_generation_num of this TopObject.
        :rtype: str
        """
        return self._plan_generation_num

    @plan_generation_num.setter
    def plan_generation_num(self, plan_generation_num):
        r"""Sets the plan_generation_num of this TopObject.

        获取执行计划次数

        :param plan_generation_num: The plan_generation_num of this TopObject.
        :type plan_generation_num: str
        """
        self._plan_generation_num = plan_generation_num

    @property
    def last_execution_time(self):
        r"""Gets the last_execution_time of this TopObject.

        最近执行时间

        :return: The last_execution_time of this TopObject.
        :rtype: str
        """
        return self._last_execution_time

    @last_execution_time.setter
    def last_execution_time(self, last_execution_time):
        r"""Sets the last_execution_time of this TopObject.

        最近执行时间

        :param last_execution_time: The last_execution_time of this TopObject.
        :type last_execution_time: str
        """
        self._last_execution_time = last_execution_time

    @property
    def avg_worker_time(self):
        r"""Gets the avg_worker_time of this TopObject.

        平均cpu耗时(单位为毫秒)

        :return: The avg_worker_time of this TopObject.
        :rtype: str
        """
        return self._avg_worker_time

    @avg_worker_time.setter
    def avg_worker_time(self, avg_worker_time):
        r"""Sets the avg_worker_time of this TopObject.

        平均cpu耗时(单位为毫秒)

        :param avg_worker_time: The avg_worker_time of this TopObject.
        :type avg_worker_time: str
        """
        self._avg_worker_time = avg_worker_time

    @property
    def total_worker_time(self):
        r"""Gets the total_worker_time of this TopObject.

        总cpu耗时(单位为毫秒)

        :return: The total_worker_time of this TopObject.
        :rtype: str
        """
        return self._total_worker_time

    @total_worker_time.setter
    def total_worker_time(self, total_worker_time):
        r"""Sets the total_worker_time of this TopObject.

        总cpu耗时(单位为毫秒)

        :param total_worker_time: The total_worker_time of this TopObject.
        :type total_worker_time: str
        """
        self._total_worker_time = total_worker_time

    @property
    def last_worker_time(self):
        r"""Gets the last_worker_time of this TopObject.

        最近cpu耗时(单位为毫秒)

        :return: The last_worker_time of this TopObject.
        :rtype: str
        """
        return self._last_worker_time

    @last_worker_time.setter
    def last_worker_time(self, last_worker_time):
        r"""Sets the last_worker_time of this TopObject.

        最近cpu耗时(单位为毫秒)

        :param last_worker_time: The last_worker_time of this TopObject.
        :type last_worker_time: str
        """
        self._last_worker_time = last_worker_time

    @property
    def min_worker_time(self):
        r"""Gets the min_worker_time of this TopObject.

        最小cpu耗时(单位为毫秒)

        :return: The min_worker_time of this TopObject.
        :rtype: str
        """
        return self._min_worker_time

    @min_worker_time.setter
    def min_worker_time(self, min_worker_time):
        r"""Sets the min_worker_time of this TopObject.

        最小cpu耗时(单位为毫秒)

        :param min_worker_time: The min_worker_time of this TopObject.
        :type min_worker_time: str
        """
        self._min_worker_time = min_worker_time

    @property
    def max_worker_time(self):
        r"""Gets the max_worker_time of this TopObject.

        最大cpu耗时(单位为毫秒)

        :return: The max_worker_time of this TopObject.
        :rtype: str
        """
        return self._max_worker_time

    @max_worker_time.setter
    def max_worker_time(self, max_worker_time):
        r"""Sets the max_worker_time of this TopObject.

        最大cpu耗时(单位为毫秒)

        :param max_worker_time: The max_worker_time of this TopObject.
        :type max_worker_time: str
        """
        self._max_worker_time = max_worker_time

    @property
    def avg_logical_reads(self):
        r"""Gets the avg_logical_reads of this TopObject.

        平均逻辑读

        :return: The avg_logical_reads of this TopObject.
        :rtype: str
        """
        return self._avg_logical_reads

    @avg_logical_reads.setter
    def avg_logical_reads(self, avg_logical_reads):
        r"""Sets the avg_logical_reads of this TopObject.

        平均逻辑读

        :param avg_logical_reads: The avg_logical_reads of this TopObject.
        :type avg_logical_reads: str
        """
        self._avg_logical_reads = avg_logical_reads

    @property
    def total_logical_reads(self):
        r"""Gets the total_logical_reads of this TopObject.

        总共逻辑读

        :return: The total_logical_reads of this TopObject.
        :rtype: str
        """
        return self._total_logical_reads

    @total_logical_reads.setter
    def total_logical_reads(self, total_logical_reads):
        r"""Sets the total_logical_reads of this TopObject.

        总共逻辑读

        :param total_logical_reads: The total_logical_reads of this TopObject.
        :type total_logical_reads: str
        """
        self._total_logical_reads = total_logical_reads

    @property
    def last_logical_reads(self):
        r"""Gets the last_logical_reads of this TopObject.

        最近逻辑读

        :return: The last_logical_reads of this TopObject.
        :rtype: str
        """
        return self._last_logical_reads

    @last_logical_reads.setter
    def last_logical_reads(self, last_logical_reads):
        r"""Sets the last_logical_reads of this TopObject.

        最近逻辑读

        :param last_logical_reads: The last_logical_reads of this TopObject.
        :type last_logical_reads: str
        """
        self._last_logical_reads = last_logical_reads

    @property
    def min_logical_reads(self):
        r"""Gets the min_logical_reads of this TopObject.

        最小逻辑读

        :return: The min_logical_reads of this TopObject.
        :rtype: str
        """
        return self._min_logical_reads

    @min_logical_reads.setter
    def min_logical_reads(self, min_logical_reads):
        r"""Sets the min_logical_reads of this TopObject.

        最小逻辑读

        :param min_logical_reads: The min_logical_reads of this TopObject.
        :type min_logical_reads: str
        """
        self._min_logical_reads = min_logical_reads

    @property
    def max_logical_reads(self):
        r"""Gets the max_logical_reads of this TopObject.

        最大逻辑读

        :return: The max_logical_reads of this TopObject.
        :rtype: str
        """
        return self._max_logical_reads

    @max_logical_reads.setter
    def max_logical_reads(self, max_logical_reads):
        r"""Sets the max_logical_reads of this TopObject.

        最大逻辑读

        :param max_logical_reads: The max_logical_reads of this TopObject.
        :type max_logical_reads: str
        """
        self._max_logical_reads = max_logical_reads

    @property
    def avg_logical_writes(self):
        r"""Gets the avg_logical_writes of this TopObject.

        平均逻辑写

        :return: The avg_logical_writes of this TopObject.
        :rtype: str
        """
        return self._avg_logical_writes

    @avg_logical_writes.setter
    def avg_logical_writes(self, avg_logical_writes):
        r"""Sets the avg_logical_writes of this TopObject.

        平均逻辑写

        :param avg_logical_writes: The avg_logical_writes of this TopObject.
        :type avg_logical_writes: str
        """
        self._avg_logical_writes = avg_logical_writes

    @property
    def total_logical_writes(self):
        r"""Gets the total_logical_writes of this TopObject.

        总共逻辑写

        :return: The total_logical_writes of this TopObject.
        :rtype: str
        """
        return self._total_logical_writes

    @total_logical_writes.setter
    def total_logical_writes(self, total_logical_writes):
        r"""Sets the total_logical_writes of this TopObject.

        总共逻辑写

        :param total_logical_writes: The total_logical_writes of this TopObject.
        :type total_logical_writes: str
        """
        self._total_logical_writes = total_logical_writes

    @property
    def last_logical_writes(self):
        r"""Gets the last_logical_writes of this TopObject.

        最近逻辑写

        :return: The last_logical_writes of this TopObject.
        :rtype: str
        """
        return self._last_logical_writes

    @last_logical_writes.setter
    def last_logical_writes(self, last_logical_writes):
        r"""Sets the last_logical_writes of this TopObject.

        最近逻辑写

        :param last_logical_writes: The last_logical_writes of this TopObject.
        :type last_logical_writes: str
        """
        self._last_logical_writes = last_logical_writes

    @property
    def min_logical_writes(self):
        r"""Gets the min_logical_writes of this TopObject.

        最小逻辑写

        :return: The min_logical_writes of this TopObject.
        :rtype: str
        """
        return self._min_logical_writes

    @min_logical_writes.setter
    def min_logical_writes(self, min_logical_writes):
        r"""Sets the min_logical_writes of this TopObject.

        最小逻辑写

        :param min_logical_writes: The min_logical_writes of this TopObject.
        :type min_logical_writes: str
        """
        self._min_logical_writes = min_logical_writes

    @property
    def max_logical_writes(self):
        r"""Gets the max_logical_writes of this TopObject.

        最大逻辑写

        :return: The max_logical_writes of this TopObject.
        :rtype: str
        """
        return self._max_logical_writes

    @max_logical_writes.setter
    def max_logical_writes(self, max_logical_writes):
        r"""Sets the max_logical_writes of this TopObject.

        最大逻辑写

        :param max_logical_writes: The max_logical_writes of this TopObject.
        :type max_logical_writes: str
        """
        self._max_logical_writes = max_logical_writes

    @property
    def avg_logical_io(self):
        r"""Gets the avg_logical_io of this TopObject.

        平均逻辑io

        :return: The avg_logical_io of this TopObject.
        :rtype: str
        """
        return self._avg_logical_io

    @avg_logical_io.setter
    def avg_logical_io(self, avg_logical_io):
        r"""Sets the avg_logical_io of this TopObject.

        平均逻辑io

        :param avg_logical_io: The avg_logical_io of this TopObject.
        :type avg_logical_io: str
        """
        self._avg_logical_io = avg_logical_io

    @property
    def total_logical_io(self):
        r"""Gets the total_logical_io of this TopObject.

        总共逻辑io

        :return: The total_logical_io of this TopObject.
        :rtype: str
        """
        return self._total_logical_io

    @total_logical_io.setter
    def total_logical_io(self, total_logical_io):
        r"""Sets the total_logical_io of this TopObject.

        总共逻辑io

        :param total_logical_io: The total_logical_io of this TopObject.
        :type total_logical_io: str
        """
        self._total_logical_io = total_logical_io

    @property
    def last_logical_io(self):
        r"""Gets the last_logical_io of this TopObject.

        最近逻辑io

        :return: The last_logical_io of this TopObject.
        :rtype: str
        """
        return self._last_logical_io

    @last_logical_io.setter
    def last_logical_io(self, last_logical_io):
        r"""Sets the last_logical_io of this TopObject.

        最近逻辑io

        :param last_logical_io: The last_logical_io of this TopObject.
        :type last_logical_io: str
        """
        self._last_logical_io = last_logical_io

    @property
    def min_logical_io(self):
        r"""Gets the min_logical_io of this TopObject.

        最小逻辑io

        :return: The min_logical_io of this TopObject.
        :rtype: str
        """
        return self._min_logical_io

    @min_logical_io.setter
    def min_logical_io(self, min_logical_io):
        r"""Sets the min_logical_io of this TopObject.

        最小逻辑io

        :param min_logical_io: The min_logical_io of this TopObject.
        :type min_logical_io: str
        """
        self._min_logical_io = min_logical_io

    @property
    def max_logical_io(self):
        r"""Gets the max_logical_io of this TopObject.

        最大逻辑io

        :return: The max_logical_io of this TopObject.
        :rtype: str
        """
        return self._max_logical_io

    @max_logical_io.setter
    def max_logical_io(self, max_logical_io):
        r"""Sets the max_logical_io of this TopObject.

        最大逻辑io

        :param max_logical_io: The max_logical_io of this TopObject.
        :type max_logical_io: str
        """
        self._max_logical_io = max_logical_io

    @property
    def avg_physical_reads(self):
        r"""Gets the avg_physical_reads of this TopObject.

        平均物理读

        :return: The avg_physical_reads of this TopObject.
        :rtype: str
        """
        return self._avg_physical_reads

    @avg_physical_reads.setter
    def avg_physical_reads(self, avg_physical_reads):
        r"""Sets the avg_physical_reads of this TopObject.

        平均物理读

        :param avg_physical_reads: The avg_physical_reads of this TopObject.
        :type avg_physical_reads: str
        """
        self._avg_physical_reads = avg_physical_reads

    @property
    def total_physical_reads(self):
        r"""Gets the total_physical_reads of this TopObject.

        总共物理读

        :return: The total_physical_reads of this TopObject.
        :rtype: str
        """
        return self._total_physical_reads

    @total_physical_reads.setter
    def total_physical_reads(self, total_physical_reads):
        r"""Sets the total_physical_reads of this TopObject.

        总共物理读

        :param total_physical_reads: The total_physical_reads of this TopObject.
        :type total_physical_reads: str
        """
        self._total_physical_reads = total_physical_reads

    @property
    def last_physical_reads(self):
        r"""Gets the last_physical_reads of this TopObject.

        最近物理读

        :return: The last_physical_reads of this TopObject.
        :rtype: str
        """
        return self._last_physical_reads

    @last_physical_reads.setter
    def last_physical_reads(self, last_physical_reads):
        r"""Sets the last_physical_reads of this TopObject.

        最近物理读

        :param last_physical_reads: The last_physical_reads of this TopObject.
        :type last_physical_reads: str
        """
        self._last_physical_reads = last_physical_reads

    @property
    def min_physical_reads(self):
        r"""Gets the min_physical_reads of this TopObject.

        最小物理读

        :return: The min_physical_reads of this TopObject.
        :rtype: str
        """
        return self._min_physical_reads

    @min_physical_reads.setter
    def min_physical_reads(self, min_physical_reads):
        r"""Sets the min_physical_reads of this TopObject.

        最小物理读

        :param min_physical_reads: The min_physical_reads of this TopObject.
        :type min_physical_reads: str
        """
        self._min_physical_reads = min_physical_reads

    @property
    def max_physical_reads(self):
        r"""Gets the max_physical_reads of this TopObject.

        最大物理读

        :return: The max_physical_reads of this TopObject.
        :rtype: str
        """
        return self._max_physical_reads

    @max_physical_reads.setter
    def max_physical_reads(self, max_physical_reads):
        r"""Sets the max_physical_reads of this TopObject.

        最大物理读

        :param max_physical_reads: The max_physical_reads of this TopObject.
        :type max_physical_reads: str
        """
        self._max_physical_reads = max_physical_reads

    @property
    def avg_elapsed_time(self):
        r"""Gets the avg_elapsed_time of this TopObject.

        平均执行耗时

        :return: The avg_elapsed_time of this TopObject.
        :rtype: str
        """
        return self._avg_elapsed_time

    @avg_elapsed_time.setter
    def avg_elapsed_time(self, avg_elapsed_time):
        r"""Sets the avg_elapsed_time of this TopObject.

        平均执行耗时

        :param avg_elapsed_time: The avg_elapsed_time of this TopObject.
        :type avg_elapsed_time: str
        """
        self._avg_elapsed_time = avg_elapsed_time

    @property
    def total_elapsed_time(self):
        r"""Gets the total_elapsed_time of this TopObject.

        总共执行耗时

        :return: The total_elapsed_time of this TopObject.
        :rtype: str
        """
        return self._total_elapsed_time

    @total_elapsed_time.setter
    def total_elapsed_time(self, total_elapsed_time):
        r"""Sets the total_elapsed_time of this TopObject.

        总共执行耗时

        :param total_elapsed_time: The total_elapsed_time of this TopObject.
        :type total_elapsed_time: str
        """
        self._total_elapsed_time = total_elapsed_time

    @property
    def last_elapsed_time(self):
        r"""Gets the last_elapsed_time of this TopObject.

        最近执行耗时

        :return: The last_elapsed_time of this TopObject.
        :rtype: str
        """
        return self._last_elapsed_time

    @last_elapsed_time.setter
    def last_elapsed_time(self, last_elapsed_time):
        r"""Sets the last_elapsed_time of this TopObject.

        最近执行耗时

        :param last_elapsed_time: The last_elapsed_time of this TopObject.
        :type last_elapsed_time: str
        """
        self._last_elapsed_time = last_elapsed_time

    @property
    def min_elapsed_time(self):
        r"""Gets the min_elapsed_time of this TopObject.

        最小执行耗时

        :return: The min_elapsed_time of this TopObject.
        :rtype: str
        """
        return self._min_elapsed_time

    @min_elapsed_time.setter
    def min_elapsed_time(self, min_elapsed_time):
        r"""Sets the min_elapsed_time of this TopObject.

        最小执行耗时

        :param min_elapsed_time: The min_elapsed_time of this TopObject.
        :type min_elapsed_time: str
        """
        self._min_elapsed_time = min_elapsed_time

    @property
    def max_elapsed_time(self):
        r"""Gets the max_elapsed_time of this TopObject.

        最大执行耗时

        :return: The max_elapsed_time of this TopObject.
        :rtype: str
        """
        return self._max_elapsed_time

    @max_elapsed_time.setter
    def max_elapsed_time(self, max_elapsed_time):
        r"""Sets the max_elapsed_time of this TopObject.

        最大执行耗时

        :param max_elapsed_time: The max_elapsed_time of this TopObject.
        :type max_elapsed_time: str
        """
        self._max_elapsed_time = max_elapsed_time

    @property
    def avg_rows(self):
        r"""Gets the avg_rows of this TopObject.

        平均返回行

        :return: The avg_rows of this TopObject.
        :rtype: str
        """
        return self._avg_rows

    @avg_rows.setter
    def avg_rows(self, avg_rows):
        r"""Sets the avg_rows of this TopObject.

        平均返回行

        :param avg_rows: The avg_rows of this TopObject.
        :type avg_rows: str
        """
        self._avg_rows = avg_rows

    @property
    def total_rows(self):
        r"""Gets the total_rows of this TopObject.

        总返回行

        :return: The total_rows of this TopObject.
        :rtype: str
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        r"""Sets the total_rows of this TopObject.

        总返回行

        :param total_rows: The total_rows of this TopObject.
        :type total_rows: str
        """
        self._total_rows = total_rows

    @property
    def last_rows(self):
        r"""Gets the last_rows of this TopObject.

        最近返回行

        :return: The last_rows of this TopObject.
        :rtype: str
        """
        return self._last_rows

    @last_rows.setter
    def last_rows(self, last_rows):
        r"""Sets the last_rows of this TopObject.

        最近返回行

        :param last_rows: The last_rows of this TopObject.
        :type last_rows: str
        """
        self._last_rows = last_rows

    @property
    def min_rows(self):
        r"""Gets the min_rows of this TopObject.

        最小返回行

        :return: The min_rows of this TopObject.
        :rtype: str
        """
        return self._min_rows

    @min_rows.setter
    def min_rows(self, min_rows):
        r"""Sets the min_rows of this TopObject.

        最小返回行

        :param min_rows: The min_rows of this TopObject.
        :type min_rows: str
        """
        self._min_rows = min_rows

    @property
    def max_rows(self):
        r"""Gets the max_rows of this TopObject.

        最大返回行

        :return: The max_rows of this TopObject.
        :rtype: str
        """
        return self._max_rows

    @max_rows.setter
    def max_rows(self, max_rows):
        r"""Sets the max_rows of this TopObject.

        最大返回行

        :param max_rows: The max_rows of this TopObject.
        :type max_rows: str
        """
        self._max_rows = max_rows

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
        if not isinstance(other, TopObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
