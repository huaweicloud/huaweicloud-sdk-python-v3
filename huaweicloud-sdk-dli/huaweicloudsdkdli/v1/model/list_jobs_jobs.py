# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsJobs:

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
        'tags': 'list[TmsTagEntity]',
        'message': 'str',
        'end_time': 'int'
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
        'end_time': 'end_time'
    }

    def __init__(self, job_id=None, job_type=None, queue_name=None, owner=None, start_time=None, duration=None, status=None, input_row_count=None, bad_row_count=None, input_size=None, result_count=None, database_name=None, table_name=None, with_column_header=None, detail=None, statement=None, tags=None, message=None, end_time=None):
        """ListJobsJobs

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
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        :param message: 系统提示信息。
        :type message: str
        :param end_time: 作业结束的时间。是单位为“毫秒”的时间戳。
        :type end_time: int
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

    @property
    def job_id(self):
        """Gets the job_id of this ListJobsJobs.

        作业ID。

        :return: The job_id of this ListJobsJobs.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListJobsJobs.

        作业ID。

        :param job_id: The job_id of this ListJobsJobs.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this ListJobsJobs.

        作业类型。

        :return: The job_type of this ListJobsJobs.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ListJobsJobs.

        作业类型。

        :param job_type: The job_type of this ListJobsJobs.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def queue_name(self):
        """Gets the queue_name of this ListJobsJobs.

        作业提交的队列。

        :return: The queue_name of this ListJobsJobs.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ListJobsJobs.

        作业提交的队列。

        :param queue_name: The queue_name of this ListJobsJobs.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def owner(self):
        """Gets the owner of this ListJobsJobs.

        提交作业的用户。

        :return: The owner of this ListJobsJobs.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ListJobsJobs.

        提交作业的用户。

        :param owner: The owner of this ListJobsJobs.
        :type owner: str
        """
        self._owner = owner

    @property
    def start_time(self):
        """Gets the start_time of this ListJobsJobs.

        作业开始的时间。是单位为“毫秒”的时间戳。

        :return: The start_time of this ListJobsJobs.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListJobsJobs.

        作业开始的时间。是单位为“毫秒”的时间戳。

        :param start_time: The start_time of this ListJobsJobs.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this ListJobsJobs.

        作业运行时长，单位毫秒。

        :return: The duration of this ListJobsJobs.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ListJobsJobs.

        作业运行时长，单位毫秒。

        :param duration: The duration of this ListJobsJobs.
        :type duration: int
        """
        self._duration = duration

    @property
    def status(self):
        """Gets the status of this ListJobsJobs.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。

        :return: The status of this ListJobsJobs.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListJobsJobs.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）。

        :param status: The status of this ListJobsJobs.
        :type status: str
        """
        self._status = status

    @property
    def input_row_count(self):
        """Gets the input_row_count of this ListJobsJobs.

        Insert作业执行过程中扫描的记录条数。

        :return: The input_row_count of this ListJobsJobs.
        :rtype: int
        """
        return self._input_row_count

    @input_row_count.setter
    def input_row_count(self, input_row_count):
        """Sets the input_row_count of this ListJobsJobs.

        Insert作业执行过程中扫描的记录条数。

        :param input_row_count: The input_row_count of this ListJobsJobs.
        :type input_row_count: int
        """
        self._input_row_count = input_row_count

    @property
    def bad_row_count(self):
        """Gets the bad_row_count of this ListJobsJobs.

        Insert作业执行过程中扫描到的错误记录数。

        :return: The bad_row_count of this ListJobsJobs.
        :rtype: int
        """
        return self._bad_row_count

    @bad_row_count.setter
    def bad_row_count(self, bad_row_count):
        """Sets the bad_row_count of this ListJobsJobs.

        Insert作业执行过程中扫描到的错误记录数。

        :param bad_row_count: The bad_row_count of this ListJobsJobs.
        :type bad_row_count: int
        """
        self._bad_row_count = bad_row_count

    @property
    def input_size(self):
        """Gets the input_size of this ListJobsJobs.

        作业执行过程中扫描文件的大小。

        :return: The input_size of this ListJobsJobs.
        :rtype: int
        """
        return self._input_size

    @input_size.setter
    def input_size(self, input_size):
        """Sets the input_size of this ListJobsJobs.

        作业执行过程中扫描文件的大小。

        :param input_size: The input_size of this ListJobsJobs.
        :type input_size: int
        """
        self._input_size = input_size

    @property
    def result_count(self):
        """Gets the result_count of this ListJobsJobs.

        当前作业返回的结果总条数或insert作业插入的总条数。

        :return: The result_count of this ListJobsJobs.
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """Sets the result_count of this ListJobsJobs.

        当前作业返回的结果总条数或insert作业插入的总条数。

        :param result_count: The result_count of this ListJobsJobs.
        :type result_count: int
        """
        self._result_count = result_count

    @property
    def database_name(self):
        """Gets the database_name of this ListJobsJobs.

        记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性。

        :return: The database_name of this ListJobsJobs.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ListJobsJobs.

        记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性。

        :param database_name: The database_name of this ListJobsJobs.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this ListJobsJobs.

        记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。

        :return: The table_name of this ListJobsJobs.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ListJobsJobs.

        记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。

        :param table_name: The table_name of this ListJobsJobs.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def with_column_header(self):
        """Gets the with_column_header of this ListJobsJobs.

        Import类型的作业，记录其导入的数据是否包括列名。

        :return: The with_column_header of this ListJobsJobs.
        :rtype: bool
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        """Sets the with_column_header of this ListJobsJobs.

        Import类型的作业，记录其导入的数据是否包括列名。

        :param with_column_header: The with_column_header of this ListJobsJobs.
        :type with_column_header: bool
        """
        self._with_column_header = with_column_header

    @property
    def detail(self):
        """Gets the detail of this ListJobsJobs.

        SQL查询的相关列信息的Json字符串。

        :return: The detail of this ListJobsJobs.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ListJobsJobs.

        SQL查询的相关列信息的Json字符串。

        :param detail: The detail of this ListJobsJobs.
        :type detail: str
        """
        self._detail = detail

    @property
    def statement(self):
        """Gets the statement of this ListJobsJobs.

        作业执行的SQL语句。

        :return: The statement of this ListJobsJobs.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this ListJobsJobs.

        作业执行的SQL语句。

        :param statement: The statement of this ListJobsJobs.
        :type statement: str
        """
        self._statement = statement

    @property
    def tags(self):
        """Gets the tags of this ListJobsJobs.

        作业标签

        :return: The tags of this ListJobsJobs.
        :rtype: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListJobsJobs.

        作业标签

        :param tags: The tags of this ListJobsJobs.
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        self._tags = tags

    @property
    def message(self):
        """Gets the message of this ListJobsJobs.

        系统提示信息。

        :return: The message of this ListJobsJobs.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListJobsJobs.

        系统提示信息。

        :param message: The message of this ListJobsJobs.
        :type message: str
        """
        self._message = message

    @property
    def end_time(self):
        """Gets the end_time of this ListJobsJobs.

        作业结束的时间。是单位为“毫秒”的时间戳。

        :return: The end_time of this ListJobsJobs.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListJobsJobs.

        作业结束的时间。是单位为“毫秒”的时间戳。

        :param end_time: The end_time of this ListJobsJobs.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ListJobsJobs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
