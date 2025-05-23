# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'job_type': 'str',
        'queue_name': 'str',
        'owner': 'str',
        'start_time': 'int',
        'duration': 'int',
        'status': 'str',
        'input_row_count': 'int',
        'bad_row_count': 'int',
        'input_size': 'int',
        'result_count': 'int',
        'database_name': 'str',
        'table_name': 'str',
        'with_column_header': 'bool',
        'detail': 'str',
        'statement': 'str',
        'tags': 'list[Tag]',
        'message': 'str',
        'end_time': 'int',
        'cpu_cost': 'str',
        'output_byte': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_type': 'job_type',
        'queue_name': 'queue_name',
        'owner': 'owner',
        'start_time': 'start_time',
        'duration': 'duration',
        'status': 'status',
        'input_row_count': 'input_row_count',
        'bad_row_count': 'bad_row_count',
        'input_size': 'input_size',
        'result_count': 'result_count',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'with_column_header': 'with_column_header',
        'detail': 'detail',
        'statement': 'statement',
        'tags': 'tags',
        'message': 'message',
        'end_time': 'end_time',
        'cpu_cost': 'cpu_cost',
        'output_byte': 'output_byte'
    }

    def __init__(self, job_id=None, job_type=None, queue_name=None, owner=None, start_time=None, duration=None, status=None, input_row_count=None, bad_row_count=None, input_size=None, result_count=None, database_name=None, table_name=None, with_column_header=None, detail=None, statement=None, tags=None, message=None, end_time=None, cpu_cost=None, output_byte=None):
        r"""SqlJob

        The model defined in huaweicloud sdk

        :param job_id: 作业ID。
        :type job_id: str
        :param job_type: 作业类型。
        :type job_type: str
        :param queue_name: 作业提交的队列。
        :type queue_name: str
        :param owner: 提交作业的用户。
        :type owner: str
        :param start_time: 作业开始的时间。是单位为“毫秒”的时间戳。
        :type start_time: int
        :param duration: 作业运行时长，单位毫秒。
        :type duration: int
        :param status: 此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。
        :type status: str
        :param input_row_count: Insert作业执行过程中扫描的记录条数。
        :type input_row_count: int
        :param bad_row_count: Insert作业执行过程中扫描到的错误记录数。
        :type bad_row_count: int
        :param input_size: 作业执行过程中扫描文件的大小。
        :type input_size: int
        :param result_count: 当前作业返回的结果总条数或insert作业插入的总条数。
        :type result_count: int
        :param database_name: 记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性。
        :type database_name: str
        :param table_name: 记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。
        :type table_name: str
        :param with_column_header: Import类型的作业，记录其导入的数据是否包括列名。
        :type with_column_header: bool
        :param detail: SQL查询的相关列信息的Json字符串。
        :type detail: str
        :param statement: 作业执行的SQL语句。
        :type statement: str
        :param tags: 作业标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        :param message: 系统提示信息。
        :type message: str
        :param end_time: 作业结束的时间。是单位为“毫秒”的时间戳。
        :type end_time: int
        :param cpu_cost: 作业的CPU累计使用量
        :type cpu_cost: str
        :param output_byte: 作业的输出字节数
        :type output_byte: str
        """
        
        

        self._job_id = None
        self._job_type = None
        self._queue_name = None
        self._owner = None
        self._start_time = None
        self._duration = None
        self._status = None
        self._input_row_count = None
        self._bad_row_count = None
        self._input_size = None
        self._result_count = None
        self._database_name = None
        self._table_name = None
        self._with_column_header = None
        self._detail = None
        self._statement = None
        self._tags = None
        self._message = None
        self._end_time = None
        self._cpu_cost = None
        self._output_byte = None
        self.discriminator = None

        self.job_id = job_id
        self.job_type = job_type
        self.queue_name = queue_name
        self.owner = owner
        self.start_time = start_time
        if duration is not None:
            self.duration = duration
        self.status = status
        if input_row_count is not None:
            self.input_row_count = input_row_count
        if bad_row_count is not None:
            self.bad_row_count = bad_row_count
        self.input_size = input_size
        self.result_count = result_count
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if with_column_header is not None:
            self.with_column_header = with_column_header
        self.detail = detail
        self.statement = statement
        if tags is not None:
            self.tags = tags
        if message is not None:
            self.message = message
        if end_time is not None:
            self.end_time = end_time
        if cpu_cost is not None:
            self.cpu_cost = cpu_cost
        if output_byte is not None:
            self.output_byte = output_byte

    @property
    def job_id(self):
        r"""Gets the job_id of this SqlJob.

        作业ID。

        :return: The job_id of this SqlJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SqlJob.

        作业ID。

        :param job_id: The job_id of this SqlJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this SqlJob.

        作业类型。

        :return: The job_type of this SqlJob.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this SqlJob.

        作业类型。

        :param job_type: The job_type of this SqlJob.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def queue_name(self):
        r"""Gets the queue_name of this SqlJob.

        作业提交的队列。

        :return: The queue_name of this SqlJob.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this SqlJob.

        作业提交的队列。

        :param queue_name: The queue_name of this SqlJob.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def owner(self):
        r"""Gets the owner of this SqlJob.

        提交作业的用户。

        :return: The owner of this SqlJob.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this SqlJob.

        提交作业的用户。

        :param owner: The owner of this SqlJob.
        :type owner: str
        """
        self._owner = owner

    @property
    def start_time(self):
        r"""Gets the start_time of this SqlJob.

        作业开始的时间。是单位为“毫秒”的时间戳。

        :return: The start_time of this SqlJob.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SqlJob.

        作业开始的时间。是单位为“毫秒”的时间戳。

        :param start_time: The start_time of this SqlJob.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def duration(self):
        r"""Gets the duration of this SqlJob.

        作业运行时长，单位毫秒。

        :return: The duration of this SqlJob.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this SqlJob.

        作业运行时长，单位毫秒。

        :param duration: The duration of this SqlJob.
        :type duration: int
        """
        self._duration = duration

    @property
    def status(self):
        r"""Gets the status of this SqlJob.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。

        :return: The status of this SqlJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SqlJob.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。

        :param status: The status of this SqlJob.
        :type status: str
        """
        self._status = status

    @property
    def input_row_count(self):
        r"""Gets the input_row_count of this SqlJob.

        Insert作业执行过程中扫描的记录条数。

        :return: The input_row_count of this SqlJob.
        :rtype: int
        """
        return self._input_row_count

    @input_row_count.setter
    def input_row_count(self, input_row_count):
        r"""Sets the input_row_count of this SqlJob.

        Insert作业执行过程中扫描的记录条数。

        :param input_row_count: The input_row_count of this SqlJob.
        :type input_row_count: int
        """
        self._input_row_count = input_row_count

    @property
    def bad_row_count(self):
        r"""Gets the bad_row_count of this SqlJob.

        Insert作业执行过程中扫描到的错误记录数。

        :return: The bad_row_count of this SqlJob.
        :rtype: int
        """
        return self._bad_row_count

    @bad_row_count.setter
    def bad_row_count(self, bad_row_count):
        r"""Sets the bad_row_count of this SqlJob.

        Insert作业执行过程中扫描到的错误记录数。

        :param bad_row_count: The bad_row_count of this SqlJob.
        :type bad_row_count: int
        """
        self._bad_row_count = bad_row_count

    @property
    def input_size(self):
        r"""Gets the input_size of this SqlJob.

        作业执行过程中扫描文件的大小。

        :return: The input_size of this SqlJob.
        :rtype: int
        """
        return self._input_size

    @input_size.setter
    def input_size(self, input_size):
        r"""Sets the input_size of this SqlJob.

        作业执行过程中扫描文件的大小。

        :param input_size: The input_size of this SqlJob.
        :type input_size: int
        """
        self._input_size = input_size

    @property
    def result_count(self):
        r"""Gets the result_count of this SqlJob.

        当前作业返回的结果总条数或insert作业插入的总条数。

        :return: The result_count of this SqlJob.
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        r"""Sets the result_count of this SqlJob.

        当前作业返回的结果总条数或insert作业插入的总条数。

        :param result_count: The result_count of this SqlJob.
        :type result_count: int
        """
        self._result_count = result_count

    @property
    def database_name(self):
        r"""Gets the database_name of this SqlJob.

        记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性。

        :return: The database_name of this SqlJob.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this SqlJob.

        记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性。

        :param database_name: The database_name of this SqlJob.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this SqlJob.

        记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。

        :return: The table_name of this SqlJob.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this SqlJob.

        记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。

        :param table_name: The table_name of this SqlJob.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def with_column_header(self):
        r"""Gets the with_column_header of this SqlJob.

        Import类型的作业，记录其导入的数据是否包括列名。

        :return: The with_column_header of this SqlJob.
        :rtype: bool
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        r"""Sets the with_column_header of this SqlJob.

        Import类型的作业，记录其导入的数据是否包括列名。

        :param with_column_header: The with_column_header of this SqlJob.
        :type with_column_header: bool
        """
        self._with_column_header = with_column_header

    @property
    def detail(self):
        r"""Gets the detail of this SqlJob.

        SQL查询的相关列信息的Json字符串。

        :return: The detail of this SqlJob.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this SqlJob.

        SQL查询的相关列信息的Json字符串。

        :param detail: The detail of this SqlJob.
        :type detail: str
        """
        self._detail = detail

    @property
    def statement(self):
        r"""Gets the statement of this SqlJob.

        作业执行的SQL语句。

        :return: The statement of this SqlJob.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        r"""Sets the statement of this SqlJob.

        作业执行的SQL语句。

        :param statement: The statement of this SqlJob.
        :type statement: str
        """
        self._statement = statement

    @property
    def tags(self):
        r"""Gets the tags of this SqlJob.

        作业标签

        :return: The tags of this SqlJob.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SqlJob.

        作业标签

        :param tags: The tags of this SqlJob.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        self._tags = tags

    @property
    def message(self):
        r"""Gets the message of this SqlJob.

        系统提示信息。

        :return: The message of this SqlJob.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this SqlJob.

        系统提示信息。

        :param message: The message of this SqlJob.
        :type message: str
        """
        self._message = message

    @property
    def end_time(self):
        r"""Gets the end_time of this SqlJob.

        作业结束的时间。是单位为“毫秒”的时间戳。

        :return: The end_time of this SqlJob.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SqlJob.

        作业结束的时间。是单位为“毫秒”的时间戳。

        :param end_time: The end_time of this SqlJob.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def cpu_cost(self):
        r"""Gets the cpu_cost of this SqlJob.

        作业的CPU累计使用量

        :return: The cpu_cost of this SqlJob.
        :rtype: str
        """
        return self._cpu_cost

    @cpu_cost.setter
    def cpu_cost(self, cpu_cost):
        r"""Sets the cpu_cost of this SqlJob.

        作业的CPU累计使用量

        :param cpu_cost: The cpu_cost of this SqlJob.
        :type cpu_cost: str
        """
        self._cpu_cost = cpu_cost

    @property
    def output_byte(self):
        r"""Gets the output_byte of this SqlJob.

        作业的输出字节数

        :return: The output_byte of this SqlJob.
        :rtype: str
        """
        return self._output_byte

    @output_byte.setter
    def output_byte(self, output_byte):
        r"""Sets the output_byte of this SqlJob.

        作业的输出字节数

        :param output_byte: The output_byte of this SqlJob.
        :type output_byte: str
        """
        self._output_byte = output_byte

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
        if not isinstance(other, SqlJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
