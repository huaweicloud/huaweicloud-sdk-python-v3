# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTopSqlsResult:

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
        'statement': 'str',
        'query': 'str',
        'db_name': 'str',
        'execution_count': 'str',
        'execution_count_percent': 'str',
        'total_cpu_time': 'str',
        'total_cpu_time_percent': 'str',
        'avg_cpu_time': 'str',
        'avg_cpu_time_percent': 'str',
        'total_duration_time': 'str',
        'total_duration_time_percent': 'str',
        'avg_duration_time': 'str',
        'avg_duration_time_percent': 'str',
        'total_rows': 'str',
        'total_rows_percent': 'str',
        'avg_rows': 'str',
        'avg_rows_percent': 'str',
        'total_logical_reads': 'str',
        'total_logical_reads_percent': 'str',
        'avg_logical_reads': 'str',
        'avg_logical_reads_percent': 'str',
        'avg_logical_write': 'str',
        'avg_logical_write_percent': 'str',
        'total_logical_write': 'str',
        'total_logical_write_percent': 'str',
        'avg_physical_reads': 'str',
        'avg_physical_reads_percent': 'str',
        'total_physical_reads': 'str',
        'total_physical_reads_percent': 'str',
        'last_execution_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'statement': 'statement',
        'query': 'query',
        'db_name': 'db_name',
        'execution_count': 'execution_count',
        'execution_count_percent': 'execution_count_percent',
        'total_cpu_time': 'total_cpu_time',
        'total_cpu_time_percent': 'total_cpu_time_percent',
        'avg_cpu_time': 'avg_cpu_time',
        'avg_cpu_time_percent': 'avg_cpu_time_percent',
        'total_duration_time': 'total_duration_time',
        'total_duration_time_percent': 'total_duration_time_percent',
        'avg_duration_time': 'avg_duration_time',
        'avg_duration_time_percent': 'avg_duration_time_percent',
        'total_rows': 'total_rows',
        'total_rows_percent': 'total_rows_percent',
        'avg_rows': 'avg_rows',
        'avg_rows_percent': 'avg_rows_percent',
        'total_logical_reads': 'total_logical_reads',
        'total_logical_reads_percent': 'total_logical_reads_percent',
        'avg_logical_reads': 'avg_logical_reads',
        'avg_logical_reads_percent': 'avg_logical_reads_percent',
        'avg_logical_write': 'avg_logical_write',
        'avg_logical_write_percent': 'avg_logical_write_percent',
        'total_logical_write': 'total_logical_write',
        'total_logical_write_percent': 'total_logical_write_percent',
        'avg_physical_reads': 'avg_physical_reads',
        'avg_physical_reads_percent': 'avg_physical_reads_percent',
        'total_physical_reads': 'total_physical_reads',
        'total_physical_reads_percent': 'total_physical_reads_percent',
        'last_execution_time': 'last_execution_time'
    }

    def __init__(self, id=None, statement=None, query=None, db_name=None, execution_count=None, execution_count_percent=None, total_cpu_time=None, total_cpu_time_percent=None, avg_cpu_time=None, avg_cpu_time_percent=None, total_duration_time=None, total_duration_time_percent=None, avg_duration_time=None, avg_duration_time_percent=None, total_rows=None, total_rows_percent=None, avg_rows=None, avg_rows_percent=None, total_logical_reads=None, total_logical_reads_percent=None, avg_logical_reads=None, avg_logical_reads_percent=None, avg_logical_write=None, avg_logical_write_percent=None, total_logical_write=None, total_logical_write_percent=None, avg_physical_reads=None, avg_physical_reads_percent=None, total_physical_reads=None, total_physical_reads_percent=None, last_execution_time=None):
        r"""QueryTopSqlsResult

        The model defined in huaweicloud sdk

        :param id: 对查询计算的二进制哈希值，用于标识具有类似逻辑的查询。
        :type id: str
        :param statement: 当前执行的SQL语句。
        :type statement: str
        :param query: SQL全文。
        :type query: str
        :param db_name: 数据库名称。
        :type db_name: str
        :param execution_count: 执行总次数。
        :type execution_count: str
        :param execution_count_percent: 执行总次数百分比，范围0.0000-1.0000。
        :type execution_count_percent: str
        :param total_cpu_time: 总CPU耗时，单位ms。
        :type total_cpu_time: str
        :param total_cpu_time_percent: 总CPU耗时百分比，范围0.0000-1.0000。
        :type total_cpu_time_percent: str
        :param avg_cpu_time: 平均CPU耗时，单位ms。
        :type avg_cpu_time: str
        :param avg_cpu_time_percent: 平均CPU耗时百分比，范围0.0000-1.0000。
        :type avg_cpu_time_percent: str
        :param total_duration_time: 总执行耗时。
        :type total_duration_time: str
        :param total_duration_time_percent: 总执行耗时百分比，范围0.0000-1.0000。
        :type total_duration_time_percent: str
        :param avg_duration_time: 平均执行耗时。
        :type avg_duration_time: str
        :param avg_duration_time_percent: 平均执行耗时百分比，范围0.0000-1.0000。
        :type avg_duration_time_percent: str
        :param total_rows: 总返回行。
        :type total_rows: str
        :param total_rows_percent: 总返回行百分比，范围0.0000-1.0000。
        :type total_rows_percent: str
        :param avg_rows: 平均返回行。
        :type avg_rows: str
        :param avg_rows_percent: 平均返回行百分比，范围0.0000-1.0000。
        :type avg_rows_percent: str
        :param total_logical_reads: 总逻辑读消耗。
        :type total_logical_reads: str
        :param total_logical_reads_percent: 总逻辑读百分比，范围0.0000-1.0000。
        :type total_logical_reads_percent: str
        :param avg_logical_reads: 平均逻辑读消耗。
        :type avg_logical_reads: str
        :param avg_logical_reads_percent: 平均逻辑读百分比，范围0.0000-1.0000。
        :type avg_logical_reads_percent: str
        :param avg_logical_write: 平均逻辑写消耗。
        :type avg_logical_write: str
        :param avg_logical_write_percent: 平均逻辑写百分比，范围0.0000-1.0000。
        :type avg_logical_write_percent: str
        :param total_logical_write: 总逻辑写消耗。
        :type total_logical_write: str
        :param total_logical_write_percent: 总逻辑写百分比，范围0.0000-1.0000。
        :type total_logical_write_percent: str
        :param avg_physical_reads: 平均物理读消耗。
        :type avg_physical_reads: str
        :param avg_physical_reads_percent: 平均物理读百分比，范围0.0000-1.0000。
        :type avg_physical_reads_percent: str
        :param total_physical_reads: 总物理读消耗。
        :type total_physical_reads: str
        :param total_physical_reads_percent: 总物理读百分比，范围0.0000-1.0000。
        :type total_physical_reads_percent: str
        :param last_execution_time: 上次执行时间。
        :type last_execution_time: str
        """
        
        

        self._id = None
        self._statement = None
        self._query = None
        self._db_name = None
        self._execution_count = None
        self._execution_count_percent = None
        self._total_cpu_time = None
        self._total_cpu_time_percent = None
        self._avg_cpu_time = None
        self._avg_cpu_time_percent = None
        self._total_duration_time = None
        self._total_duration_time_percent = None
        self._avg_duration_time = None
        self._avg_duration_time_percent = None
        self._total_rows = None
        self._total_rows_percent = None
        self._avg_rows = None
        self._avg_rows_percent = None
        self._total_logical_reads = None
        self._total_logical_reads_percent = None
        self._avg_logical_reads = None
        self._avg_logical_reads_percent = None
        self._avg_logical_write = None
        self._avg_logical_write_percent = None
        self._total_logical_write = None
        self._total_logical_write_percent = None
        self._avg_physical_reads = None
        self._avg_physical_reads_percent = None
        self._total_physical_reads = None
        self._total_physical_reads_percent = None
        self._last_execution_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if statement is not None:
            self.statement = statement
        if query is not None:
            self.query = query
        if db_name is not None:
            self.db_name = db_name
        if execution_count is not None:
            self.execution_count = execution_count
        if execution_count_percent is not None:
            self.execution_count_percent = execution_count_percent
        if total_cpu_time is not None:
            self.total_cpu_time = total_cpu_time
        if total_cpu_time_percent is not None:
            self.total_cpu_time_percent = total_cpu_time_percent
        if avg_cpu_time is not None:
            self.avg_cpu_time = avg_cpu_time
        if avg_cpu_time_percent is not None:
            self.avg_cpu_time_percent = avg_cpu_time_percent
        if total_duration_time is not None:
            self.total_duration_time = total_duration_time
        if total_duration_time_percent is not None:
            self.total_duration_time_percent = total_duration_time_percent
        if avg_duration_time is not None:
            self.avg_duration_time = avg_duration_time
        if avg_duration_time_percent is not None:
            self.avg_duration_time_percent = avg_duration_time_percent
        if total_rows is not None:
            self.total_rows = total_rows
        if total_rows_percent is not None:
            self.total_rows_percent = total_rows_percent
        if avg_rows is not None:
            self.avg_rows = avg_rows
        if avg_rows_percent is not None:
            self.avg_rows_percent = avg_rows_percent
        if total_logical_reads is not None:
            self.total_logical_reads = total_logical_reads
        if total_logical_reads_percent is not None:
            self.total_logical_reads_percent = total_logical_reads_percent
        if avg_logical_reads is not None:
            self.avg_logical_reads = avg_logical_reads
        if avg_logical_reads_percent is not None:
            self.avg_logical_reads_percent = avg_logical_reads_percent
        if avg_logical_write is not None:
            self.avg_logical_write = avg_logical_write
        if avg_logical_write_percent is not None:
            self.avg_logical_write_percent = avg_logical_write_percent
        if total_logical_write is not None:
            self.total_logical_write = total_logical_write
        if total_logical_write_percent is not None:
            self.total_logical_write_percent = total_logical_write_percent
        if avg_physical_reads is not None:
            self.avg_physical_reads = avg_physical_reads
        if avg_physical_reads_percent is not None:
            self.avg_physical_reads_percent = avg_physical_reads_percent
        if total_physical_reads is not None:
            self.total_physical_reads = total_physical_reads
        if total_physical_reads_percent is not None:
            self.total_physical_reads_percent = total_physical_reads_percent
        if last_execution_time is not None:
            self.last_execution_time = last_execution_time

    @property
    def id(self):
        r"""Gets the id of this QueryTopSqlsResult.

        对查询计算的二进制哈希值，用于标识具有类似逻辑的查询。

        :return: The id of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QueryTopSqlsResult.

        对查询计算的二进制哈希值，用于标识具有类似逻辑的查询。

        :param id: The id of this QueryTopSqlsResult.
        :type id: str
        """
        self._id = id

    @property
    def statement(self):
        r"""Gets the statement of this QueryTopSqlsResult.

        当前执行的SQL语句。

        :return: The statement of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this QueryTopSqlsResult.

        当前执行的SQL语句。

        :param statement: The statement of this QueryTopSqlsResult.
        :type statement: str
        """
        self._statement = statement

    @property
    def query(self):
        r"""Gets the query of this QueryTopSqlsResult.

        SQL全文。

        :return: The query of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this QueryTopSqlsResult.

        SQL全文。

        :param query: The query of this QueryTopSqlsResult.
        :type query: str
        """
        self._query = query

    @property
    def db_name(self):
        r"""Gets the db_name of this QueryTopSqlsResult.

        数据库名称。

        :return: The db_name of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this QueryTopSqlsResult.

        数据库名称。

        :param db_name: The db_name of this QueryTopSqlsResult.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def execution_count(self):
        r"""Gets the execution_count of this QueryTopSqlsResult.

        执行总次数。

        :return: The execution_count of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._execution_count

    @execution_count.setter
    def execution_count(self, execution_count):
        r"""Sets the execution_count of this QueryTopSqlsResult.

        执行总次数。

        :param execution_count: The execution_count of this QueryTopSqlsResult.
        :type execution_count: str
        """
        self._execution_count = execution_count

    @property
    def execution_count_percent(self):
        r"""Gets the execution_count_percent of this QueryTopSqlsResult.

        执行总次数百分比，范围0.0000-1.0000。

        :return: The execution_count_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._execution_count_percent

    @execution_count_percent.setter
    def execution_count_percent(self, execution_count_percent):
        r"""Sets the execution_count_percent of this QueryTopSqlsResult.

        执行总次数百分比，范围0.0000-1.0000。

        :param execution_count_percent: The execution_count_percent of this QueryTopSqlsResult.
        :type execution_count_percent: str
        """
        self._execution_count_percent = execution_count_percent

    @property
    def total_cpu_time(self):
        r"""Gets the total_cpu_time of this QueryTopSqlsResult.

        总CPU耗时，单位ms。

        :return: The total_cpu_time of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_cpu_time

    @total_cpu_time.setter
    def total_cpu_time(self, total_cpu_time):
        r"""Sets the total_cpu_time of this QueryTopSqlsResult.

        总CPU耗时，单位ms。

        :param total_cpu_time: The total_cpu_time of this QueryTopSqlsResult.
        :type total_cpu_time: str
        """
        self._total_cpu_time = total_cpu_time

    @property
    def total_cpu_time_percent(self):
        r"""Gets the total_cpu_time_percent of this QueryTopSqlsResult.

        总CPU耗时百分比，范围0.0000-1.0000。

        :return: The total_cpu_time_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_cpu_time_percent

    @total_cpu_time_percent.setter
    def total_cpu_time_percent(self, total_cpu_time_percent):
        r"""Sets the total_cpu_time_percent of this QueryTopSqlsResult.

        总CPU耗时百分比，范围0.0000-1.0000。

        :param total_cpu_time_percent: The total_cpu_time_percent of this QueryTopSqlsResult.
        :type total_cpu_time_percent: str
        """
        self._total_cpu_time_percent = total_cpu_time_percent

    @property
    def avg_cpu_time(self):
        r"""Gets the avg_cpu_time of this QueryTopSqlsResult.

        平均CPU耗时，单位ms。

        :return: The avg_cpu_time of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_cpu_time

    @avg_cpu_time.setter
    def avg_cpu_time(self, avg_cpu_time):
        r"""Sets the avg_cpu_time of this QueryTopSqlsResult.

        平均CPU耗时，单位ms。

        :param avg_cpu_time: The avg_cpu_time of this QueryTopSqlsResult.
        :type avg_cpu_time: str
        """
        self._avg_cpu_time = avg_cpu_time

    @property
    def avg_cpu_time_percent(self):
        r"""Gets the avg_cpu_time_percent of this QueryTopSqlsResult.

        平均CPU耗时百分比，范围0.0000-1.0000。

        :return: The avg_cpu_time_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_cpu_time_percent

    @avg_cpu_time_percent.setter
    def avg_cpu_time_percent(self, avg_cpu_time_percent):
        r"""Sets the avg_cpu_time_percent of this QueryTopSqlsResult.

        平均CPU耗时百分比，范围0.0000-1.0000。

        :param avg_cpu_time_percent: The avg_cpu_time_percent of this QueryTopSqlsResult.
        :type avg_cpu_time_percent: str
        """
        self._avg_cpu_time_percent = avg_cpu_time_percent

    @property
    def total_duration_time(self):
        r"""Gets the total_duration_time of this QueryTopSqlsResult.

        总执行耗时。

        :return: The total_duration_time of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_duration_time

    @total_duration_time.setter
    def total_duration_time(self, total_duration_time):
        r"""Sets the total_duration_time of this QueryTopSqlsResult.

        总执行耗时。

        :param total_duration_time: The total_duration_time of this QueryTopSqlsResult.
        :type total_duration_time: str
        """
        self._total_duration_time = total_duration_time

    @property
    def total_duration_time_percent(self):
        r"""Gets the total_duration_time_percent of this QueryTopSqlsResult.

        总执行耗时百分比，范围0.0000-1.0000。

        :return: The total_duration_time_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_duration_time_percent

    @total_duration_time_percent.setter
    def total_duration_time_percent(self, total_duration_time_percent):
        r"""Sets the total_duration_time_percent of this QueryTopSqlsResult.

        总执行耗时百分比，范围0.0000-1.0000。

        :param total_duration_time_percent: The total_duration_time_percent of this QueryTopSqlsResult.
        :type total_duration_time_percent: str
        """
        self._total_duration_time_percent = total_duration_time_percent

    @property
    def avg_duration_time(self):
        r"""Gets the avg_duration_time of this QueryTopSqlsResult.

        平均执行耗时。

        :return: The avg_duration_time of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_duration_time

    @avg_duration_time.setter
    def avg_duration_time(self, avg_duration_time):
        r"""Sets the avg_duration_time of this QueryTopSqlsResult.

        平均执行耗时。

        :param avg_duration_time: The avg_duration_time of this QueryTopSqlsResult.
        :type avg_duration_time: str
        """
        self._avg_duration_time = avg_duration_time

    @property
    def avg_duration_time_percent(self):
        r"""Gets the avg_duration_time_percent of this QueryTopSqlsResult.

        平均执行耗时百分比，范围0.0000-1.0000。

        :return: The avg_duration_time_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_duration_time_percent

    @avg_duration_time_percent.setter
    def avg_duration_time_percent(self, avg_duration_time_percent):
        r"""Sets the avg_duration_time_percent of this QueryTopSqlsResult.

        平均执行耗时百分比，范围0.0000-1.0000。

        :param avg_duration_time_percent: The avg_duration_time_percent of this QueryTopSqlsResult.
        :type avg_duration_time_percent: str
        """
        self._avg_duration_time_percent = avg_duration_time_percent

    @property
    def total_rows(self):
        r"""Gets the total_rows of this QueryTopSqlsResult.

        总返回行。

        :return: The total_rows of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        r"""Sets the total_rows of this QueryTopSqlsResult.

        总返回行。

        :param total_rows: The total_rows of this QueryTopSqlsResult.
        :type total_rows: str
        """
        self._total_rows = total_rows

    @property
    def total_rows_percent(self):
        r"""Gets the total_rows_percent of this QueryTopSqlsResult.

        总返回行百分比，范围0.0000-1.0000。

        :return: The total_rows_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_rows_percent

    @total_rows_percent.setter
    def total_rows_percent(self, total_rows_percent):
        r"""Sets the total_rows_percent of this QueryTopSqlsResult.

        总返回行百分比，范围0.0000-1.0000。

        :param total_rows_percent: The total_rows_percent of this QueryTopSqlsResult.
        :type total_rows_percent: str
        """
        self._total_rows_percent = total_rows_percent

    @property
    def avg_rows(self):
        r"""Gets the avg_rows of this QueryTopSqlsResult.

        平均返回行。

        :return: The avg_rows of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_rows

    @avg_rows.setter
    def avg_rows(self, avg_rows):
        r"""Sets the avg_rows of this QueryTopSqlsResult.

        平均返回行。

        :param avg_rows: The avg_rows of this QueryTopSqlsResult.
        :type avg_rows: str
        """
        self._avg_rows = avg_rows

    @property
    def avg_rows_percent(self):
        r"""Gets the avg_rows_percent of this QueryTopSqlsResult.

        平均返回行百分比，范围0.0000-1.0000。

        :return: The avg_rows_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_rows_percent

    @avg_rows_percent.setter
    def avg_rows_percent(self, avg_rows_percent):
        r"""Sets the avg_rows_percent of this QueryTopSqlsResult.

        平均返回行百分比，范围0.0000-1.0000。

        :param avg_rows_percent: The avg_rows_percent of this QueryTopSqlsResult.
        :type avg_rows_percent: str
        """
        self._avg_rows_percent = avg_rows_percent

    @property
    def total_logical_reads(self):
        r"""Gets the total_logical_reads of this QueryTopSqlsResult.

        总逻辑读消耗。

        :return: The total_logical_reads of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_logical_reads

    @total_logical_reads.setter
    def total_logical_reads(self, total_logical_reads):
        r"""Sets the total_logical_reads of this QueryTopSqlsResult.

        总逻辑读消耗。

        :param total_logical_reads: The total_logical_reads of this QueryTopSqlsResult.
        :type total_logical_reads: str
        """
        self._total_logical_reads = total_logical_reads

    @property
    def total_logical_reads_percent(self):
        r"""Gets the total_logical_reads_percent of this QueryTopSqlsResult.

        总逻辑读百分比，范围0.0000-1.0000。

        :return: The total_logical_reads_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_logical_reads_percent

    @total_logical_reads_percent.setter
    def total_logical_reads_percent(self, total_logical_reads_percent):
        r"""Sets the total_logical_reads_percent of this QueryTopSqlsResult.

        总逻辑读百分比，范围0.0000-1.0000。

        :param total_logical_reads_percent: The total_logical_reads_percent of this QueryTopSqlsResult.
        :type total_logical_reads_percent: str
        """
        self._total_logical_reads_percent = total_logical_reads_percent

    @property
    def avg_logical_reads(self):
        r"""Gets the avg_logical_reads of this QueryTopSqlsResult.

        平均逻辑读消耗。

        :return: The avg_logical_reads of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_logical_reads

    @avg_logical_reads.setter
    def avg_logical_reads(self, avg_logical_reads):
        r"""Sets the avg_logical_reads of this QueryTopSqlsResult.

        平均逻辑读消耗。

        :param avg_logical_reads: The avg_logical_reads of this QueryTopSqlsResult.
        :type avg_logical_reads: str
        """
        self._avg_logical_reads = avg_logical_reads

    @property
    def avg_logical_reads_percent(self):
        r"""Gets the avg_logical_reads_percent of this QueryTopSqlsResult.

        平均逻辑读百分比，范围0.0000-1.0000。

        :return: The avg_logical_reads_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_logical_reads_percent

    @avg_logical_reads_percent.setter
    def avg_logical_reads_percent(self, avg_logical_reads_percent):
        r"""Sets the avg_logical_reads_percent of this QueryTopSqlsResult.

        平均逻辑读百分比，范围0.0000-1.0000。

        :param avg_logical_reads_percent: The avg_logical_reads_percent of this QueryTopSqlsResult.
        :type avg_logical_reads_percent: str
        """
        self._avg_logical_reads_percent = avg_logical_reads_percent

    @property
    def avg_logical_write(self):
        r"""Gets the avg_logical_write of this QueryTopSqlsResult.

        平均逻辑写消耗。

        :return: The avg_logical_write of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_logical_write

    @avg_logical_write.setter
    def avg_logical_write(self, avg_logical_write):
        r"""Sets the avg_logical_write of this QueryTopSqlsResult.

        平均逻辑写消耗。

        :param avg_logical_write: The avg_logical_write of this QueryTopSqlsResult.
        :type avg_logical_write: str
        """
        self._avg_logical_write = avg_logical_write

    @property
    def avg_logical_write_percent(self):
        r"""Gets the avg_logical_write_percent of this QueryTopSqlsResult.

        平均逻辑写百分比，范围0.0000-1.0000。

        :return: The avg_logical_write_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_logical_write_percent

    @avg_logical_write_percent.setter
    def avg_logical_write_percent(self, avg_logical_write_percent):
        r"""Sets the avg_logical_write_percent of this QueryTopSqlsResult.

        平均逻辑写百分比，范围0.0000-1.0000。

        :param avg_logical_write_percent: The avg_logical_write_percent of this QueryTopSqlsResult.
        :type avg_logical_write_percent: str
        """
        self._avg_logical_write_percent = avg_logical_write_percent

    @property
    def total_logical_write(self):
        r"""Gets the total_logical_write of this QueryTopSqlsResult.

        总逻辑写消耗。

        :return: The total_logical_write of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_logical_write

    @total_logical_write.setter
    def total_logical_write(self, total_logical_write):
        r"""Sets the total_logical_write of this QueryTopSqlsResult.

        总逻辑写消耗。

        :param total_logical_write: The total_logical_write of this QueryTopSqlsResult.
        :type total_logical_write: str
        """
        self._total_logical_write = total_logical_write

    @property
    def total_logical_write_percent(self):
        r"""Gets the total_logical_write_percent of this QueryTopSqlsResult.

        总逻辑写百分比，范围0.0000-1.0000。

        :return: The total_logical_write_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_logical_write_percent

    @total_logical_write_percent.setter
    def total_logical_write_percent(self, total_logical_write_percent):
        r"""Sets the total_logical_write_percent of this QueryTopSqlsResult.

        总逻辑写百分比，范围0.0000-1.0000。

        :param total_logical_write_percent: The total_logical_write_percent of this QueryTopSqlsResult.
        :type total_logical_write_percent: str
        """
        self._total_logical_write_percent = total_logical_write_percent

    @property
    def avg_physical_reads(self):
        r"""Gets the avg_physical_reads of this QueryTopSqlsResult.

        平均物理读消耗。

        :return: The avg_physical_reads of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_physical_reads

    @avg_physical_reads.setter
    def avg_physical_reads(self, avg_physical_reads):
        r"""Sets the avg_physical_reads of this QueryTopSqlsResult.

        平均物理读消耗。

        :param avg_physical_reads: The avg_physical_reads of this QueryTopSqlsResult.
        :type avg_physical_reads: str
        """
        self._avg_physical_reads = avg_physical_reads

    @property
    def avg_physical_reads_percent(self):
        r"""Gets the avg_physical_reads_percent of this QueryTopSqlsResult.

        平均物理读百分比，范围0.0000-1.0000。

        :return: The avg_physical_reads_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._avg_physical_reads_percent

    @avg_physical_reads_percent.setter
    def avg_physical_reads_percent(self, avg_physical_reads_percent):
        r"""Sets the avg_physical_reads_percent of this QueryTopSqlsResult.

        平均物理读百分比，范围0.0000-1.0000。

        :param avg_physical_reads_percent: The avg_physical_reads_percent of this QueryTopSqlsResult.
        :type avg_physical_reads_percent: str
        """
        self._avg_physical_reads_percent = avg_physical_reads_percent

    @property
    def total_physical_reads(self):
        r"""Gets the total_physical_reads of this QueryTopSqlsResult.

        总物理读消耗。

        :return: The total_physical_reads of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_physical_reads

    @total_physical_reads.setter
    def total_physical_reads(self, total_physical_reads):
        r"""Sets the total_physical_reads of this QueryTopSqlsResult.

        总物理读消耗。

        :param total_physical_reads: The total_physical_reads of this QueryTopSqlsResult.
        :type total_physical_reads: str
        """
        self._total_physical_reads = total_physical_reads

    @property
    def total_physical_reads_percent(self):
        r"""Gets the total_physical_reads_percent of this QueryTopSqlsResult.

        总物理读百分比，范围0.0000-1.0000。

        :return: The total_physical_reads_percent of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._total_physical_reads_percent

    @total_physical_reads_percent.setter
    def total_physical_reads_percent(self, total_physical_reads_percent):
        r"""Sets the total_physical_reads_percent of this QueryTopSqlsResult.

        总物理读百分比，范围0.0000-1.0000。

        :param total_physical_reads_percent: The total_physical_reads_percent of this QueryTopSqlsResult.
        :type total_physical_reads_percent: str
        """
        self._total_physical_reads_percent = total_physical_reads_percent

    @property
    def last_execution_time(self):
        r"""Gets the last_execution_time of this QueryTopSqlsResult.

        上次执行时间。

        :return: The last_execution_time of this QueryTopSqlsResult.
        :rtype: str
        """
        return self._last_execution_time

    @last_execution_time.setter
    def last_execution_time(self, last_execution_time):
        r"""Sets the last_execution_time of this QueryTopSqlsResult.

        上次执行时间。

        :param last_execution_time: The last_execution_time of this QueryTopSqlsResult.
        :type last_execution_time: str
        """
        self._last_execution_time = last_execution_time

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
        if not isinstance(other, QueryTopSqlsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
