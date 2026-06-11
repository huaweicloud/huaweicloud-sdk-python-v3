# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopObjectOverview:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'avg_cpu_time': 'float',
        'avg_cpu_time_percentage': 'float',
        'avg_execution_time': 'float',
        'avg_execution_time_percentage': 'float',
        'avg_logical_io': 'float',
        'avg_logical_io_percentage': 'float',
        'avg_logical_reads': 'float',
        'avg_logical_reads_percentage': 'float',
        'avg_logical_writes': 'float',
        'avg_logical_writes_percentage': 'float',
        'avg_physical_reads': 'float',
        'avg_physical_reads_percentage': 'float',
        'avg_rows': 'float',
        'avg_rows_percentage': 'float',
        'database_name': 'str',
        'object_id': 'str',
        'object_name': 'str',
        'row_id': 'str',
        'object_type': 'str',
        'schema_name': 'str',
        'total_cpu_time': 'float',
        'total_cpu_time_percentage': 'float',
        'total_execution_time': 'float',
        'total_execution_time_percentage': 'float',
        'total_execution_count': 'float',
        'total_logical_io': 'float',
        'total_logical_io_percentage': 'float',
        'total_logical_reads': 'float',
        'total_logical_reads_percentage': 'float',
        'total_logical_writes': 'float',
        'total_logical_writes_percentage': 'float',
        'total_physical_reads': 'float',
        'total_physical_reads_percentage': 'float',
        'total_rows': 'float',
        'total_rows_percentage': 'float'
    }

    attribute_map = {
        'avg_cpu_time': 'avg_cpu_time',
        'avg_cpu_time_percentage': 'avg_cpu_time_percentage',
        'avg_execution_time': 'avg_execution_time',
        'avg_execution_time_percentage': 'avg_execution_time_percentage',
        'avg_logical_io': 'avg_logical_io',
        'avg_logical_io_percentage': 'avg_logical_io_percentage',
        'avg_logical_reads': 'avg_logical_reads',
        'avg_logical_reads_percentage': 'avg_logical_reads_percentage',
        'avg_logical_writes': 'avg_logical_writes',
        'avg_logical_writes_percentage': 'avg_logical_writes_percentage',
        'avg_physical_reads': 'avg_physical_reads',
        'avg_physical_reads_percentage': 'avg_physical_reads_percentage',
        'avg_rows': 'avg_rows',
        'avg_rows_percentage': 'avg_rows_percentage',
        'database_name': 'database_name',
        'object_id': 'object_id',
        'object_name': 'object_name',
        'row_id': 'row_id',
        'object_type': 'object_type',
        'schema_name': 'schema_name',
        'total_cpu_time': 'total_cpu_time',
        'total_cpu_time_percentage': 'total_cpu_time_percentage',
        'total_execution_time': 'total_execution_time',
        'total_execution_time_percentage': 'total_execution_time_percentage',
        'total_execution_count': 'total_execution_count',
        'total_logical_io': 'total_logical_io',
        'total_logical_io_percentage': 'total_logical_io_percentage',
        'total_logical_reads': 'total_logical_reads',
        'total_logical_reads_percentage': 'total_logical_reads_percentage',
        'total_logical_writes': 'total_logical_writes',
        'total_logical_writes_percentage': 'total_logical_writes_percentage',
        'total_physical_reads': 'total_physical_reads',
        'total_physical_reads_percentage': 'total_physical_reads_percentage',
        'total_rows': 'total_rows',
        'total_rows_percentage': 'total_rows_percentage'
    }

    def __init__(self, avg_cpu_time=None, avg_cpu_time_percentage=None, avg_execution_time=None, avg_execution_time_percentage=None, avg_logical_io=None, avg_logical_io_percentage=None, avg_logical_reads=None, avg_logical_reads_percentage=None, avg_logical_writes=None, avg_logical_writes_percentage=None, avg_physical_reads=None, avg_physical_reads_percentage=None, avg_rows=None, avg_rows_percentage=None, database_name=None, object_id=None, object_name=None, row_id=None, object_type=None, schema_name=None, total_cpu_time=None, total_cpu_time_percentage=None, total_execution_time=None, total_execution_time_percentage=None, total_execution_count=None, total_logical_io=None, total_logical_io_percentage=None, total_logical_reads=None, total_logical_reads_percentage=None, total_logical_writes=None, total_logical_writes_percentage=None, total_physical_reads=None, total_physical_reads_percentage=None, total_rows=None, total_rows_percentage=None):
        r"""TopObjectOverview

        The model defined in huaweicloud sdk

        :param avg_cpu_time: 平均cpu耗时(单位为毫秒)
        :type avg_cpu_time: float
        :param avg_cpu_time_percentage: 平均cpu耗时百分比
        :type avg_cpu_time_percentage: float
        :param avg_execution_time: 平均执行耗时(单位为毫秒)
        :type avg_execution_time: float
        :param avg_execution_time_percentage: 平均执行耗时百分比
        :type avg_execution_time_percentage: float
        :param avg_logical_io: 平均逻辑io
        :type avg_logical_io: float
        :param avg_logical_io_percentage: 平均逻辑io百分比
        :type avg_logical_io_percentage: float
        :param avg_logical_reads: 平均逻辑读
        :type avg_logical_reads: float
        :param avg_logical_reads_percentage: 平均逻辑读百分比
        :type avg_logical_reads_percentage: float
        :param avg_logical_writes: 平均逻辑写
        :type avg_logical_writes: float
        :param avg_logical_writes_percentage: 平均逻辑写百分比
        :type avg_logical_writes_percentage: float
        :param avg_physical_reads: 平均物理读
        :type avg_physical_reads: float
        :param avg_physical_reads_percentage: 平均物理读百分比
        :type avg_physical_reads_percentage: float
        :param avg_rows: 平均返回行
        :type avg_rows: float
        :param avg_rows_percentage: 平均返回行百分比
        :type avg_rows_percentage: float
        :param database_name: 数据库名
        :type database_name: str
        :param object_id: 对象id
        :type object_id: str
        :param object_name: 对象名称
        :type object_name: str
        :param row_id: id
        :type row_id: str
        :param object_type: 对象类型
        :type object_type: str
        :param schema_name: 模式
        :type schema_name: str
        :param total_cpu_time: 总cpu耗时(单位为毫秒)
        :type total_cpu_time: float
        :param total_cpu_time_percentage: 总cpu耗时百分比
        :type total_cpu_time_percentage: float
        :param total_execution_time: 总执行耗时(单位为毫秒)
        :type total_execution_time: float
        :param total_execution_time_percentage: 总执行耗时百分比
        :type total_execution_time_percentage: float
        :param total_execution_count: 总执行次数
        :type total_execution_count: float
        :param total_logical_io: 总逻辑io
        :type total_logical_io: float
        :param total_logical_io_percentage: 总逻辑io百分比
        :type total_logical_io_percentage: float
        :param total_logical_reads: 总逻辑读
        :type total_logical_reads: float
        :param total_logical_reads_percentage: 总逻辑读百分比
        :type total_logical_reads_percentage: float
        :param total_logical_writes: 总逻辑写
        :type total_logical_writes: float
        :param total_logical_writes_percentage: 总逻辑写百分比
        :type total_logical_writes_percentage: float
        :param total_physical_reads: 总物理读
        :type total_physical_reads: float
        :param total_physical_reads_percentage: 总物理读百分比
        :type total_physical_reads_percentage: float
        :param total_rows: 总返回行
        :type total_rows: float
        :param total_rows_percentage: 总返回行百分比
        :type total_rows_percentage: float
        """
        
        

        self._avg_cpu_time = None
        self._avg_cpu_time_percentage = None
        self._avg_execution_time = None
        self._avg_execution_time_percentage = None
        self._avg_logical_io = None
        self._avg_logical_io_percentage = None
        self._avg_logical_reads = None
        self._avg_logical_reads_percentage = None
        self._avg_logical_writes = None
        self._avg_logical_writes_percentage = None
        self._avg_physical_reads = None
        self._avg_physical_reads_percentage = None
        self._avg_rows = None
        self._avg_rows_percentage = None
        self._database_name = None
        self._object_id = None
        self._object_name = None
        self._row_id = None
        self._object_type = None
        self._schema_name = None
        self._total_cpu_time = None
        self._total_cpu_time_percentage = None
        self._total_execution_time = None
        self._total_execution_time_percentage = None
        self._total_execution_count = None
        self._total_logical_io = None
        self._total_logical_io_percentage = None
        self._total_logical_reads = None
        self._total_logical_reads_percentage = None
        self._total_logical_writes = None
        self._total_logical_writes_percentage = None
        self._total_physical_reads = None
        self._total_physical_reads_percentage = None
        self._total_rows = None
        self._total_rows_percentage = None
        self.discriminator = None

        if avg_cpu_time is not None:
            self.avg_cpu_time = avg_cpu_time
        if avg_cpu_time_percentage is not None:
            self.avg_cpu_time_percentage = avg_cpu_time_percentage
        if avg_execution_time is not None:
            self.avg_execution_time = avg_execution_time
        if avg_execution_time_percentage is not None:
            self.avg_execution_time_percentage = avg_execution_time_percentage
        if avg_logical_io is not None:
            self.avg_logical_io = avg_logical_io
        if avg_logical_io_percentage is not None:
            self.avg_logical_io_percentage = avg_logical_io_percentage
        if avg_logical_reads is not None:
            self.avg_logical_reads = avg_logical_reads
        if avg_logical_reads_percentage is not None:
            self.avg_logical_reads_percentage = avg_logical_reads_percentage
        if avg_logical_writes is not None:
            self.avg_logical_writes = avg_logical_writes
        if avg_logical_writes_percentage is not None:
            self.avg_logical_writes_percentage = avg_logical_writes_percentage
        if avg_physical_reads is not None:
            self.avg_physical_reads = avg_physical_reads
        if avg_physical_reads_percentage is not None:
            self.avg_physical_reads_percentage = avg_physical_reads_percentage
        if avg_rows is not None:
            self.avg_rows = avg_rows
        if avg_rows_percentage is not None:
            self.avg_rows_percentage = avg_rows_percentage
        if database_name is not None:
            self.database_name = database_name
        if object_id is not None:
            self.object_id = object_id
        if object_name is not None:
            self.object_name = object_name
        if row_id is not None:
            self.row_id = row_id
        if object_type is not None:
            self.object_type = object_type
        if schema_name is not None:
            self.schema_name = schema_name
        if total_cpu_time is not None:
            self.total_cpu_time = total_cpu_time
        if total_cpu_time_percentage is not None:
            self.total_cpu_time_percentage = total_cpu_time_percentage
        if total_execution_time is not None:
            self.total_execution_time = total_execution_time
        if total_execution_time_percentage is not None:
            self.total_execution_time_percentage = total_execution_time_percentage
        if total_execution_count is not None:
            self.total_execution_count = total_execution_count
        if total_logical_io is not None:
            self.total_logical_io = total_logical_io
        if total_logical_io_percentage is not None:
            self.total_logical_io_percentage = total_logical_io_percentage
        if total_logical_reads is not None:
            self.total_logical_reads = total_logical_reads
        if total_logical_reads_percentage is not None:
            self.total_logical_reads_percentage = total_logical_reads_percentage
        if total_logical_writes is not None:
            self.total_logical_writes = total_logical_writes
        if total_logical_writes_percentage is not None:
            self.total_logical_writes_percentage = total_logical_writes_percentage
        if total_physical_reads is not None:
            self.total_physical_reads = total_physical_reads
        if total_physical_reads_percentage is not None:
            self.total_physical_reads_percentage = total_physical_reads_percentage
        if total_rows is not None:
            self.total_rows = total_rows
        if total_rows_percentage is not None:
            self.total_rows_percentage = total_rows_percentage

    @property
    def avg_cpu_time(self):
        r"""Gets the avg_cpu_time of this TopObjectOverview.

        平均cpu耗时(单位为毫秒)

        :return: The avg_cpu_time of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_cpu_time

    @avg_cpu_time.setter
    def avg_cpu_time(self, avg_cpu_time):
        r"""Sets the avg_cpu_time of this TopObjectOverview.

        平均cpu耗时(单位为毫秒)

        :param avg_cpu_time: The avg_cpu_time of this TopObjectOverview.
        :type avg_cpu_time: float
        """
        self._avg_cpu_time = avg_cpu_time

    @property
    def avg_cpu_time_percentage(self):
        r"""Gets the avg_cpu_time_percentage of this TopObjectOverview.

        平均cpu耗时百分比

        :return: The avg_cpu_time_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_cpu_time_percentage

    @avg_cpu_time_percentage.setter
    def avg_cpu_time_percentage(self, avg_cpu_time_percentage):
        r"""Sets the avg_cpu_time_percentage of this TopObjectOverview.

        平均cpu耗时百分比

        :param avg_cpu_time_percentage: The avg_cpu_time_percentage of this TopObjectOverview.
        :type avg_cpu_time_percentage: float
        """
        self._avg_cpu_time_percentage = avg_cpu_time_percentage

    @property
    def avg_execution_time(self):
        r"""Gets the avg_execution_time of this TopObjectOverview.

        平均执行耗时(单位为毫秒)

        :return: The avg_execution_time of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_execution_time

    @avg_execution_time.setter
    def avg_execution_time(self, avg_execution_time):
        r"""Sets the avg_execution_time of this TopObjectOverview.

        平均执行耗时(单位为毫秒)

        :param avg_execution_time: The avg_execution_time of this TopObjectOverview.
        :type avg_execution_time: float
        """
        self._avg_execution_time = avg_execution_time

    @property
    def avg_execution_time_percentage(self):
        r"""Gets the avg_execution_time_percentage of this TopObjectOverview.

        平均执行耗时百分比

        :return: The avg_execution_time_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_execution_time_percentage

    @avg_execution_time_percentage.setter
    def avg_execution_time_percentage(self, avg_execution_time_percentage):
        r"""Sets the avg_execution_time_percentage of this TopObjectOverview.

        平均执行耗时百分比

        :param avg_execution_time_percentage: The avg_execution_time_percentage of this TopObjectOverview.
        :type avg_execution_time_percentage: float
        """
        self._avg_execution_time_percentage = avg_execution_time_percentage

    @property
    def avg_logical_io(self):
        r"""Gets the avg_logical_io of this TopObjectOverview.

        平均逻辑io

        :return: The avg_logical_io of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_logical_io

    @avg_logical_io.setter
    def avg_logical_io(self, avg_logical_io):
        r"""Sets the avg_logical_io of this TopObjectOverview.

        平均逻辑io

        :param avg_logical_io: The avg_logical_io of this TopObjectOverview.
        :type avg_logical_io: float
        """
        self._avg_logical_io = avg_logical_io

    @property
    def avg_logical_io_percentage(self):
        r"""Gets the avg_logical_io_percentage of this TopObjectOverview.

        平均逻辑io百分比

        :return: The avg_logical_io_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_logical_io_percentage

    @avg_logical_io_percentage.setter
    def avg_logical_io_percentage(self, avg_logical_io_percentage):
        r"""Sets the avg_logical_io_percentage of this TopObjectOverview.

        平均逻辑io百分比

        :param avg_logical_io_percentage: The avg_logical_io_percentage of this TopObjectOverview.
        :type avg_logical_io_percentage: float
        """
        self._avg_logical_io_percentage = avg_logical_io_percentage

    @property
    def avg_logical_reads(self):
        r"""Gets the avg_logical_reads of this TopObjectOverview.

        平均逻辑读

        :return: The avg_logical_reads of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_logical_reads

    @avg_logical_reads.setter
    def avg_logical_reads(self, avg_logical_reads):
        r"""Sets the avg_logical_reads of this TopObjectOverview.

        平均逻辑读

        :param avg_logical_reads: The avg_logical_reads of this TopObjectOverview.
        :type avg_logical_reads: float
        """
        self._avg_logical_reads = avg_logical_reads

    @property
    def avg_logical_reads_percentage(self):
        r"""Gets the avg_logical_reads_percentage of this TopObjectOverview.

        平均逻辑读百分比

        :return: The avg_logical_reads_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_logical_reads_percentage

    @avg_logical_reads_percentage.setter
    def avg_logical_reads_percentage(self, avg_logical_reads_percentage):
        r"""Sets the avg_logical_reads_percentage of this TopObjectOverview.

        平均逻辑读百分比

        :param avg_logical_reads_percentage: The avg_logical_reads_percentage of this TopObjectOverview.
        :type avg_logical_reads_percentage: float
        """
        self._avg_logical_reads_percentage = avg_logical_reads_percentage

    @property
    def avg_logical_writes(self):
        r"""Gets the avg_logical_writes of this TopObjectOverview.

        平均逻辑写

        :return: The avg_logical_writes of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_logical_writes

    @avg_logical_writes.setter
    def avg_logical_writes(self, avg_logical_writes):
        r"""Sets the avg_logical_writes of this TopObjectOverview.

        平均逻辑写

        :param avg_logical_writes: The avg_logical_writes of this TopObjectOverview.
        :type avg_logical_writes: float
        """
        self._avg_logical_writes = avg_logical_writes

    @property
    def avg_logical_writes_percentage(self):
        r"""Gets the avg_logical_writes_percentage of this TopObjectOverview.

        平均逻辑写百分比

        :return: The avg_logical_writes_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_logical_writes_percentage

    @avg_logical_writes_percentage.setter
    def avg_logical_writes_percentage(self, avg_logical_writes_percentage):
        r"""Sets the avg_logical_writes_percentage of this TopObjectOverview.

        平均逻辑写百分比

        :param avg_logical_writes_percentage: The avg_logical_writes_percentage of this TopObjectOverview.
        :type avg_logical_writes_percentage: float
        """
        self._avg_logical_writes_percentage = avg_logical_writes_percentage

    @property
    def avg_physical_reads(self):
        r"""Gets the avg_physical_reads of this TopObjectOverview.

        平均物理读

        :return: The avg_physical_reads of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_physical_reads

    @avg_physical_reads.setter
    def avg_physical_reads(self, avg_physical_reads):
        r"""Sets the avg_physical_reads of this TopObjectOverview.

        平均物理读

        :param avg_physical_reads: The avg_physical_reads of this TopObjectOverview.
        :type avg_physical_reads: float
        """
        self._avg_physical_reads = avg_physical_reads

    @property
    def avg_physical_reads_percentage(self):
        r"""Gets the avg_physical_reads_percentage of this TopObjectOverview.

        平均物理读百分比

        :return: The avg_physical_reads_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_physical_reads_percentage

    @avg_physical_reads_percentage.setter
    def avg_physical_reads_percentage(self, avg_physical_reads_percentage):
        r"""Sets the avg_physical_reads_percentage of this TopObjectOverview.

        平均物理读百分比

        :param avg_physical_reads_percentage: The avg_physical_reads_percentage of this TopObjectOverview.
        :type avg_physical_reads_percentage: float
        """
        self._avg_physical_reads_percentage = avg_physical_reads_percentage

    @property
    def avg_rows(self):
        r"""Gets the avg_rows of this TopObjectOverview.

        平均返回行

        :return: The avg_rows of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_rows

    @avg_rows.setter
    def avg_rows(self, avg_rows):
        r"""Sets the avg_rows of this TopObjectOverview.

        平均返回行

        :param avg_rows: The avg_rows of this TopObjectOverview.
        :type avg_rows: float
        """
        self._avg_rows = avg_rows

    @property
    def avg_rows_percentage(self):
        r"""Gets the avg_rows_percentage of this TopObjectOverview.

        平均返回行百分比

        :return: The avg_rows_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._avg_rows_percentage

    @avg_rows_percentage.setter
    def avg_rows_percentage(self, avg_rows_percentage):
        r"""Sets the avg_rows_percentage of this TopObjectOverview.

        平均返回行百分比

        :param avg_rows_percentage: The avg_rows_percentage of this TopObjectOverview.
        :type avg_rows_percentage: float
        """
        self._avg_rows_percentage = avg_rows_percentage

    @property
    def database_name(self):
        r"""Gets the database_name of this TopObjectOverview.

        数据库名

        :return: The database_name of this TopObjectOverview.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this TopObjectOverview.

        数据库名

        :param database_name: The database_name of this TopObjectOverview.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def object_id(self):
        r"""Gets the object_id of this TopObjectOverview.

        对象id

        :return: The object_id of this TopObjectOverview.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this TopObjectOverview.

        对象id

        :param object_id: The object_id of this TopObjectOverview.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def object_name(self):
        r"""Gets the object_name of this TopObjectOverview.

        对象名称

        :return: The object_name of this TopObjectOverview.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this TopObjectOverview.

        对象名称

        :param object_name: The object_name of this TopObjectOverview.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def row_id(self):
        r"""Gets the row_id of this TopObjectOverview.

        id

        :return: The row_id of this TopObjectOverview.
        :rtype: str
        """
        return self._row_id

    @row_id.setter
    def row_id(self, row_id):
        r"""Sets the row_id of this TopObjectOverview.

        id

        :param row_id: The row_id of this TopObjectOverview.
        :type row_id: str
        """
        self._row_id = row_id

    @property
    def object_type(self):
        r"""Gets the object_type of this TopObjectOverview.

        对象类型

        :return: The object_type of this TopObjectOverview.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this TopObjectOverview.

        对象类型

        :param object_type: The object_type of this TopObjectOverview.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def schema_name(self):
        r"""Gets the schema_name of this TopObjectOverview.

        模式

        :return: The schema_name of this TopObjectOverview.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this TopObjectOverview.

        模式

        :param schema_name: The schema_name of this TopObjectOverview.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def total_cpu_time(self):
        r"""Gets the total_cpu_time of this TopObjectOverview.

        总cpu耗时(单位为毫秒)

        :return: The total_cpu_time of this TopObjectOverview.
        :rtype: float
        """
        return self._total_cpu_time

    @total_cpu_time.setter
    def total_cpu_time(self, total_cpu_time):
        r"""Sets the total_cpu_time of this TopObjectOverview.

        总cpu耗时(单位为毫秒)

        :param total_cpu_time: The total_cpu_time of this TopObjectOverview.
        :type total_cpu_time: float
        """
        self._total_cpu_time = total_cpu_time

    @property
    def total_cpu_time_percentage(self):
        r"""Gets the total_cpu_time_percentage of this TopObjectOverview.

        总cpu耗时百分比

        :return: The total_cpu_time_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._total_cpu_time_percentage

    @total_cpu_time_percentage.setter
    def total_cpu_time_percentage(self, total_cpu_time_percentage):
        r"""Sets the total_cpu_time_percentage of this TopObjectOverview.

        总cpu耗时百分比

        :param total_cpu_time_percentage: The total_cpu_time_percentage of this TopObjectOverview.
        :type total_cpu_time_percentage: float
        """
        self._total_cpu_time_percentage = total_cpu_time_percentage

    @property
    def total_execution_time(self):
        r"""Gets the total_execution_time of this TopObjectOverview.

        总执行耗时(单位为毫秒)

        :return: The total_execution_time of this TopObjectOverview.
        :rtype: float
        """
        return self._total_execution_time

    @total_execution_time.setter
    def total_execution_time(self, total_execution_time):
        r"""Sets the total_execution_time of this TopObjectOverview.

        总执行耗时(单位为毫秒)

        :param total_execution_time: The total_execution_time of this TopObjectOverview.
        :type total_execution_time: float
        """
        self._total_execution_time = total_execution_time

    @property
    def total_execution_time_percentage(self):
        r"""Gets the total_execution_time_percentage of this TopObjectOverview.

        总执行耗时百分比

        :return: The total_execution_time_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._total_execution_time_percentage

    @total_execution_time_percentage.setter
    def total_execution_time_percentage(self, total_execution_time_percentage):
        r"""Sets the total_execution_time_percentage of this TopObjectOverview.

        总执行耗时百分比

        :param total_execution_time_percentage: The total_execution_time_percentage of this TopObjectOverview.
        :type total_execution_time_percentage: float
        """
        self._total_execution_time_percentage = total_execution_time_percentage

    @property
    def total_execution_count(self):
        r"""Gets the total_execution_count of this TopObjectOverview.

        总执行次数

        :return: The total_execution_count of this TopObjectOverview.
        :rtype: float
        """
        return self._total_execution_count

    @total_execution_count.setter
    def total_execution_count(self, total_execution_count):
        r"""Sets the total_execution_count of this TopObjectOverview.

        总执行次数

        :param total_execution_count: The total_execution_count of this TopObjectOverview.
        :type total_execution_count: float
        """
        self._total_execution_count = total_execution_count

    @property
    def total_logical_io(self):
        r"""Gets the total_logical_io of this TopObjectOverview.

        总逻辑io

        :return: The total_logical_io of this TopObjectOverview.
        :rtype: float
        """
        return self._total_logical_io

    @total_logical_io.setter
    def total_logical_io(self, total_logical_io):
        r"""Sets the total_logical_io of this TopObjectOverview.

        总逻辑io

        :param total_logical_io: The total_logical_io of this TopObjectOverview.
        :type total_logical_io: float
        """
        self._total_logical_io = total_logical_io

    @property
    def total_logical_io_percentage(self):
        r"""Gets the total_logical_io_percentage of this TopObjectOverview.

        总逻辑io百分比

        :return: The total_logical_io_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._total_logical_io_percentage

    @total_logical_io_percentage.setter
    def total_logical_io_percentage(self, total_logical_io_percentage):
        r"""Sets the total_logical_io_percentage of this TopObjectOverview.

        总逻辑io百分比

        :param total_logical_io_percentage: The total_logical_io_percentage of this TopObjectOverview.
        :type total_logical_io_percentage: float
        """
        self._total_logical_io_percentage = total_logical_io_percentage

    @property
    def total_logical_reads(self):
        r"""Gets the total_logical_reads of this TopObjectOverview.

        总逻辑读

        :return: The total_logical_reads of this TopObjectOverview.
        :rtype: float
        """
        return self._total_logical_reads

    @total_logical_reads.setter
    def total_logical_reads(self, total_logical_reads):
        r"""Sets the total_logical_reads of this TopObjectOverview.

        总逻辑读

        :param total_logical_reads: The total_logical_reads of this TopObjectOverview.
        :type total_logical_reads: float
        """
        self._total_logical_reads = total_logical_reads

    @property
    def total_logical_reads_percentage(self):
        r"""Gets the total_logical_reads_percentage of this TopObjectOverview.

        总逻辑读百分比

        :return: The total_logical_reads_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._total_logical_reads_percentage

    @total_logical_reads_percentage.setter
    def total_logical_reads_percentage(self, total_logical_reads_percentage):
        r"""Sets the total_logical_reads_percentage of this TopObjectOverview.

        总逻辑读百分比

        :param total_logical_reads_percentage: The total_logical_reads_percentage of this TopObjectOverview.
        :type total_logical_reads_percentage: float
        """
        self._total_logical_reads_percentage = total_logical_reads_percentage

    @property
    def total_logical_writes(self):
        r"""Gets the total_logical_writes of this TopObjectOverview.

        总逻辑写

        :return: The total_logical_writes of this TopObjectOverview.
        :rtype: float
        """
        return self._total_logical_writes

    @total_logical_writes.setter
    def total_logical_writes(self, total_logical_writes):
        r"""Sets the total_logical_writes of this TopObjectOverview.

        总逻辑写

        :param total_logical_writes: The total_logical_writes of this TopObjectOverview.
        :type total_logical_writes: float
        """
        self._total_logical_writes = total_logical_writes

    @property
    def total_logical_writes_percentage(self):
        r"""Gets the total_logical_writes_percentage of this TopObjectOverview.

        总逻辑写百分比

        :return: The total_logical_writes_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._total_logical_writes_percentage

    @total_logical_writes_percentage.setter
    def total_logical_writes_percentage(self, total_logical_writes_percentage):
        r"""Sets the total_logical_writes_percentage of this TopObjectOverview.

        总逻辑写百分比

        :param total_logical_writes_percentage: The total_logical_writes_percentage of this TopObjectOverview.
        :type total_logical_writes_percentage: float
        """
        self._total_logical_writes_percentage = total_logical_writes_percentage

    @property
    def total_physical_reads(self):
        r"""Gets the total_physical_reads of this TopObjectOverview.

        总物理读

        :return: The total_physical_reads of this TopObjectOverview.
        :rtype: float
        """
        return self._total_physical_reads

    @total_physical_reads.setter
    def total_physical_reads(self, total_physical_reads):
        r"""Sets the total_physical_reads of this TopObjectOverview.

        总物理读

        :param total_physical_reads: The total_physical_reads of this TopObjectOverview.
        :type total_physical_reads: float
        """
        self._total_physical_reads = total_physical_reads

    @property
    def total_physical_reads_percentage(self):
        r"""Gets the total_physical_reads_percentage of this TopObjectOverview.

        总物理读百分比

        :return: The total_physical_reads_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._total_physical_reads_percentage

    @total_physical_reads_percentage.setter
    def total_physical_reads_percentage(self, total_physical_reads_percentage):
        r"""Sets the total_physical_reads_percentage of this TopObjectOverview.

        总物理读百分比

        :param total_physical_reads_percentage: The total_physical_reads_percentage of this TopObjectOverview.
        :type total_physical_reads_percentage: float
        """
        self._total_physical_reads_percentage = total_physical_reads_percentage

    @property
    def total_rows(self):
        r"""Gets the total_rows of this TopObjectOverview.

        总返回行

        :return: The total_rows of this TopObjectOverview.
        :rtype: float
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        r"""Sets the total_rows of this TopObjectOverview.

        总返回行

        :param total_rows: The total_rows of this TopObjectOverview.
        :type total_rows: float
        """
        self._total_rows = total_rows

    @property
    def total_rows_percentage(self):
        r"""Gets the total_rows_percentage of this TopObjectOverview.

        总返回行百分比

        :return: The total_rows_percentage of this TopObjectOverview.
        :rtype: float
        """
        return self._total_rows_percentage

    @total_rows_percentage.setter
    def total_rows_percentage(self, total_rows_percentage):
        r"""Sets the total_rows_percentage of this TopObjectOverview.

        总返回行百分比

        :param total_rows_percentage: The total_rows_percentage of this TopObjectOverview.
        :type total_rows_percentage: float
        """
        self._total_rows_percentage = total_rows_percentage

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
        if not isinstance(other, TopObjectOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
