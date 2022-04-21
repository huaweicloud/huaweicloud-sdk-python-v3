# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlJobRunDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sql_type': 'str',
        'start_time': 'str',
        'duration': 'int',
        'input_row_count': 'int',
        'bad_row_count': 'int',
        'input_size': 'int',
        'result_count': 'int',
        'table_name': 'str',
        'with_column_header': 'bool',
        'detail': 'str',
        'statement': 'str',
        'message': 'str'
    }

    attribute_map = {
        'sql_type': 'sql_type',
        'start_time': 'start_time',
        'duration': 'duration',
        'input_row_count': 'input_row_count',
        'bad_row_count': 'bad_row_count',
        'input_size': 'input_size',
        'result_count': 'result_count',
        'table_name': 'table_name',
        'with_column_header': 'with_column_header',
        'detail': 'detail',
        'statement': 'statement',
        'message': 'message'
    }

    def __init__(self, sql_type=None, start_time=None, duration=None, input_row_count=None, bad_row_count=None, input_size=None, result_count=None, table_name=None, with_column_header=None, detail=None, statement=None, message=None):
        """SqlJobRunDetail

        The model defined in huaweicloud sdk

        :param sql_type: 作业类型。
        :type sql_type: str
        :param start_time: 作业开始的时间。时间格式为ISO日期时间格式yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;
        :type start_time: str
        :param duration: 作业运行时长，单位毫秒。
        :type duration: int
        :param input_row_count: Insert作业执行过程中扫描的记录条数。
        :type input_row_count: int
        :param bad_row_count: Insert作业执行过程中扫描到的错误记录数。
        :type bad_row_count: int
        :param input_size: 作业执行过程中扫描文件的大小。
        :type input_size: int
        :param result_count: 当前作业返回的结果总条数或insert作业插入的总条数。
        :type result_count: int
        :param table_name: 记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。
        :type table_name: str
        :param with_column_header: Import类型的作业，记录其导入的数据是否包括列名。
        :type with_column_header: bool
        :param detail: SQL查询的相关列信息的Json字符串。
        :type detail: str
        :param statement: 作业执行的SQL语句。
        :type statement: str
        :param message: 系统提示信息。运行失败时，失败原因。
        :type message: str
        """
        
        

        self._sql_type = None
        self._start_time = None
        self._duration = None
        self._input_row_count = None
        self._bad_row_count = None
        self._input_size = None
        self._result_count = None
        self._table_name = None
        self._with_column_header = None
        self._detail = None
        self._statement = None
        self._message = None
        self.discriminator = None

        if sql_type is not None:
            self.sql_type = sql_type
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if input_row_count is not None:
            self.input_row_count = input_row_count
        if bad_row_count is not None:
            self.bad_row_count = bad_row_count
        if input_size is not None:
            self.input_size = input_size
        if result_count is not None:
            self.result_count = result_count
        if table_name is not None:
            self.table_name = table_name
        if with_column_header is not None:
            self.with_column_header = with_column_header
        if detail is not None:
            self.detail = detail
        if statement is not None:
            self.statement = statement
        if message is not None:
            self.message = message

    @property
    def sql_type(self):
        """Gets the sql_type of this SqlJobRunDetail.

        作业类型。

        :return: The sql_type of this SqlJobRunDetail.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        """Sets the sql_type of this SqlJobRunDetail.

        作业类型。

        :param sql_type: The sql_type of this SqlJobRunDetail.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def start_time(self):
        """Gets the start_time of this SqlJobRunDetail.

        作业开始的时间。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :return: The start_time of this SqlJobRunDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SqlJobRunDetail.

        作业开始的时间。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss'Z'

        :param start_time: The start_time of this SqlJobRunDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this SqlJobRunDetail.

        作业运行时长，单位毫秒。

        :return: The duration of this SqlJobRunDetail.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SqlJobRunDetail.

        作业运行时长，单位毫秒。

        :param duration: The duration of this SqlJobRunDetail.
        :type duration: int
        """
        self._duration = duration

    @property
    def input_row_count(self):
        """Gets the input_row_count of this SqlJobRunDetail.

        Insert作业执行过程中扫描的记录条数。

        :return: The input_row_count of this SqlJobRunDetail.
        :rtype: int
        """
        return self._input_row_count

    @input_row_count.setter
    def input_row_count(self, input_row_count):
        """Sets the input_row_count of this SqlJobRunDetail.

        Insert作业执行过程中扫描的记录条数。

        :param input_row_count: The input_row_count of this SqlJobRunDetail.
        :type input_row_count: int
        """
        self._input_row_count = input_row_count

    @property
    def bad_row_count(self):
        """Gets the bad_row_count of this SqlJobRunDetail.

        Insert作业执行过程中扫描到的错误记录数。

        :return: The bad_row_count of this SqlJobRunDetail.
        :rtype: int
        """
        return self._bad_row_count

    @bad_row_count.setter
    def bad_row_count(self, bad_row_count):
        """Sets the bad_row_count of this SqlJobRunDetail.

        Insert作业执行过程中扫描到的错误记录数。

        :param bad_row_count: The bad_row_count of this SqlJobRunDetail.
        :type bad_row_count: int
        """
        self._bad_row_count = bad_row_count

    @property
    def input_size(self):
        """Gets the input_size of this SqlJobRunDetail.

        作业执行过程中扫描文件的大小。

        :return: The input_size of this SqlJobRunDetail.
        :rtype: int
        """
        return self._input_size

    @input_size.setter
    def input_size(self, input_size):
        """Sets the input_size of this SqlJobRunDetail.

        作业执行过程中扫描文件的大小。

        :param input_size: The input_size of this SqlJobRunDetail.
        :type input_size: int
        """
        self._input_size = input_size

    @property
    def result_count(self):
        """Gets the result_count of this SqlJobRunDetail.

        当前作业返回的结果总条数或insert作业插入的总条数。

        :return: The result_count of this SqlJobRunDetail.
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """Sets the result_count of this SqlJobRunDetail.

        当前作业返回的结果总条数或insert作业插入的总条数。

        :param result_count: The result_count of this SqlJobRunDetail.
        :type result_count: int
        """
        self._result_count = result_count

    @property
    def table_name(self):
        """Gets the table_name of this SqlJobRunDetail.

        记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。

        :return: The table_name of this SqlJobRunDetail.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this SqlJobRunDetail.

        记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。

        :param table_name: The table_name of this SqlJobRunDetail.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def with_column_header(self):
        """Gets the with_column_header of this SqlJobRunDetail.

        Import类型的作业，记录其导入的数据是否包括列名。

        :return: The with_column_header of this SqlJobRunDetail.
        :rtype: bool
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        """Sets the with_column_header of this SqlJobRunDetail.

        Import类型的作业，记录其导入的数据是否包括列名。

        :param with_column_header: The with_column_header of this SqlJobRunDetail.
        :type with_column_header: bool
        """
        self._with_column_header = with_column_header

    @property
    def detail(self):
        """Gets the detail of this SqlJobRunDetail.

        SQL查询的相关列信息的Json字符串。

        :return: The detail of this SqlJobRunDetail.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this SqlJobRunDetail.

        SQL查询的相关列信息的Json字符串。

        :param detail: The detail of this SqlJobRunDetail.
        :type detail: str
        """
        self._detail = detail

    @property
    def statement(self):
        """Gets the statement of this SqlJobRunDetail.

        作业执行的SQL语句。

        :return: The statement of this SqlJobRunDetail.
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this SqlJobRunDetail.

        作业执行的SQL语句。

        :param statement: The statement of this SqlJobRunDetail.
        :type statement: str
        """
        self._statement = statement

    @property
    def message(self):
        """Gets the message of this SqlJobRunDetail.

        系统提示信息。运行失败时，失败原因。

        :return: The message of this SqlJobRunDetail.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SqlJobRunDetail.

        系统提示信息。运行失败时，失败原因。

        :param message: The message of this SqlJobRunDetail.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, SqlJobRunDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
