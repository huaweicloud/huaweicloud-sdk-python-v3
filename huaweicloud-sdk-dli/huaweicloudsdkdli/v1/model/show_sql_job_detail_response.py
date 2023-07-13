# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlJobDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'job_id': 'str',
        'owner': 'str',
        'start_time': 'int',
        'duration': 'int',
        'export_mode': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'data_path': 'str',
        'data_type': 'str',
        'with_column_header': 'bool',
        'delimiter': 'str',
        'quote_char': 'str',
        'escape_char': 'str',
        'date_format': 'str',
        'timestamp_format': 'str',
        'compress': 'str',
        'tags': 'list[TmsTagEntity]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'job_id': 'job_id',
        'owner': 'owner',
        'start_time': 'start_time',
        'duration': 'duration',
        'export_mode': 'export_mode',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'data_path': 'data_path',
        'data_type': 'data_type',
        'with_column_header': 'with_column_header',
        'delimiter': 'delimiter',
        'quote_char': 'quote_char',
        'escape_char': 'escape_char',
        'date_format': 'date_format',
        'timestamp_format': 'timestamp_format',
        'compress': 'compress',
        'tags': 'tags'
    }

    def __init__(self, is_success=None, message=None, job_id=None, owner=None, start_time=None, duration=None, export_mode=None, database_name=None, table_name=None, data_path=None, data_type=None, with_column_header=None, delimiter=None, quote_char=None, escape_char=None, date_format=None, timestamp_format=None, compress=None, tags=None):
        """ShowSqlJobDetailResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param job_id: 作业ID。
        :type job_id: str
        :param owner: 提交作业的用户。
        :type owner: str
        :param start_time: 作业开始的时间。是单位为“毫秒”的时间戳。
        :type start_time: int
        :param duration: 作业运行时长，单位毫秒。
        :type duration: int
        :param export_mode: 导出数据或保存查询结果时，指定的导出模式。
        :type export_mode: str
        :param database_name: 记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性。
        :type database_name: str
        :param table_name: 记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。
        :type table_name: str
        :param data_path: 导入或导出的文件路径。
        :type data_path: str
        :param data_type: 导入或导出的数据类型（当前仅支持csv）。
        :type data_type: str
        :param with_column_header: 导入作业时，导入的数据是否包括列名。
        :type with_column_header: bool
        :param delimiter: 导入作业时，用户自定义数据分隔符。
        :type delimiter: str
        :param quote_char: 导入作业时，用户自定义引用字符。
        :type quote_char: str
        :param escape_char: 导入作业时，用户自定义转义字符。
        :type escape_char: str
        :param date_format: 导入作业时，指定表的日期格式。
        :type date_format: str
        :param timestamp_format: 导入作业时，指定表的时间格式
        :type timestamp_format: str
        :param compress:   导出作业时，用户指定的压缩方式。
        :type compress: str
        :param tags: 作业标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        
        super(ShowSqlJobDetailResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._job_id = None
        self._owner = None
        self._start_time = None
        self._duration = None
        self._export_mode = None
        self._database_name = None
        self._table_name = None
        self._data_path = None
        self._data_type = None
        self._with_column_header = None
        self._delimiter = None
        self._quote_char = None
        self._escape_char = None
        self._date_format = None
        self._timestamp_format = None
        self._compress = None
        self._tags = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if job_id is not None:
            self.job_id = job_id
        if owner is not None:
            self.owner = owner
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if export_mode is not None:
            self.export_mode = export_mode
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if data_path is not None:
            self.data_path = data_path
        if data_type is not None:
            self.data_type = data_type
        if with_column_header is not None:
            self.with_column_header = with_column_header
        if delimiter is not None:
            self.delimiter = delimiter
        if quote_char is not None:
            self.quote_char = quote_char
        if escape_char is not None:
            self.escape_char = escape_char
        if date_format is not None:
            self.date_format = date_format
        if timestamp_format is not None:
            self.timestamp_format = timestamp_format
        if compress is not None:
            self.compress = compress
        if tags is not None:
            self.tags = tags

    @property
    def is_success(self):
        """Gets the is_success of this ShowSqlJobDetailResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ShowSqlJobDetailResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ShowSqlJobDetailResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ShowSqlJobDetailResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ShowSqlJobDetailResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowSqlJobDetailResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ShowSqlJobDetailResponse.
        :type message: str
        """
        self._message = message

    @property
    def job_id(self):
        """Gets the job_id of this ShowSqlJobDetailResponse.

        作业ID。

        :return: The job_id of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowSqlJobDetailResponse.

        作业ID。

        :param job_id: The job_id of this ShowSqlJobDetailResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def owner(self):
        """Gets the owner of this ShowSqlJobDetailResponse.

        提交作业的用户。

        :return: The owner of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowSqlJobDetailResponse.

        提交作业的用户。

        :param owner: The owner of this ShowSqlJobDetailResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def start_time(self):
        """Gets the start_time of this ShowSqlJobDetailResponse.

        作业开始的时间。是单位为“毫秒”的时间戳。

        :return: The start_time of this ShowSqlJobDetailResponse.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowSqlJobDetailResponse.

        作业开始的时间。是单位为“毫秒”的时间戳。

        :param start_time: The start_time of this ShowSqlJobDetailResponse.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def duration(self):
        """Gets the duration of this ShowSqlJobDetailResponse.

        作业运行时长，单位毫秒。

        :return: The duration of this ShowSqlJobDetailResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ShowSqlJobDetailResponse.

        作业运行时长，单位毫秒。

        :param duration: The duration of this ShowSqlJobDetailResponse.
        :type duration: int
        """
        self._duration = duration

    @property
    def export_mode(self):
        """Gets the export_mode of this ShowSqlJobDetailResponse.

        导出数据或保存查询结果时，指定的导出模式。

        :return: The export_mode of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._export_mode

    @export_mode.setter
    def export_mode(self, export_mode):
        """Sets the export_mode of this ShowSqlJobDetailResponse.

        导出数据或保存查询结果时，指定的导出模式。

        :param export_mode: The export_mode of this ShowSqlJobDetailResponse.
        :type export_mode: str
        """
        self._export_mode = export_mode

    @property
    def database_name(self):
        """Gets the database_name of this ShowSqlJobDetailResponse.

        记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性。

        :return: The database_name of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ShowSqlJobDetailResponse.

        记录其操作的表所在的数据库名称。类型为Import和Export作业才有“database_name”属性。

        :param database_name: The database_name of this ShowSqlJobDetailResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        """Gets the table_name of this ShowSqlJobDetailResponse.

        记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。

        :return: The table_name of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ShowSqlJobDetailResponse.

        记录其操作的表名称。类型为Import和Export作业才有“table_name”属性。

        :param table_name: The table_name of this ShowSqlJobDetailResponse.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def data_path(self):
        """Gets the data_path of this ShowSqlJobDetailResponse.

        导入或导出的文件路径。

        :return: The data_path of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._data_path

    @data_path.setter
    def data_path(self, data_path):
        """Sets the data_path of this ShowSqlJobDetailResponse.

        导入或导出的文件路径。

        :param data_path: The data_path of this ShowSqlJobDetailResponse.
        :type data_path: str
        """
        self._data_path = data_path

    @property
    def data_type(self):
        """Gets the data_type of this ShowSqlJobDetailResponse.

        导入或导出的数据类型（当前仅支持csv）。

        :return: The data_type of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ShowSqlJobDetailResponse.

        导入或导出的数据类型（当前仅支持csv）。

        :param data_type: The data_type of this ShowSqlJobDetailResponse.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def with_column_header(self):
        """Gets the with_column_header of this ShowSqlJobDetailResponse.

        导入作业时，导入的数据是否包括列名。

        :return: The with_column_header of this ShowSqlJobDetailResponse.
        :rtype: bool
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        """Sets the with_column_header of this ShowSqlJobDetailResponse.

        导入作业时，导入的数据是否包括列名。

        :param with_column_header: The with_column_header of this ShowSqlJobDetailResponse.
        :type with_column_header: bool
        """
        self._with_column_header = with_column_header

    @property
    def delimiter(self):
        """Gets the delimiter of this ShowSqlJobDetailResponse.

        导入作业时，用户自定义数据分隔符。

        :return: The delimiter of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this ShowSqlJobDetailResponse.

        导入作业时，用户自定义数据分隔符。

        :param delimiter: The delimiter of this ShowSqlJobDetailResponse.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def quote_char(self):
        """Gets the quote_char of this ShowSqlJobDetailResponse.

        导入作业时，用户自定义引用字符。

        :return: The quote_char of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._quote_char

    @quote_char.setter
    def quote_char(self, quote_char):
        """Sets the quote_char of this ShowSqlJobDetailResponse.

        导入作业时，用户自定义引用字符。

        :param quote_char: The quote_char of this ShowSqlJobDetailResponse.
        :type quote_char: str
        """
        self._quote_char = quote_char

    @property
    def escape_char(self):
        """Gets the escape_char of this ShowSqlJobDetailResponse.

        导入作业时，用户自定义转义字符。

        :return: The escape_char of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._escape_char

    @escape_char.setter
    def escape_char(self, escape_char):
        """Sets the escape_char of this ShowSqlJobDetailResponse.

        导入作业时，用户自定义转义字符。

        :param escape_char: The escape_char of this ShowSqlJobDetailResponse.
        :type escape_char: str
        """
        self._escape_char = escape_char

    @property
    def date_format(self):
        """Gets the date_format of this ShowSqlJobDetailResponse.

        导入作业时，指定表的日期格式。

        :return: The date_format of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this ShowSqlJobDetailResponse.

        导入作业时，指定表的日期格式。

        :param date_format: The date_format of this ShowSqlJobDetailResponse.
        :type date_format: str
        """
        self._date_format = date_format

    @property
    def timestamp_format(self):
        """Gets the timestamp_format of this ShowSqlJobDetailResponse.

        导入作业时，指定表的时间格式

        :return: The timestamp_format of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._timestamp_format

    @timestamp_format.setter
    def timestamp_format(self, timestamp_format):
        """Sets the timestamp_format of this ShowSqlJobDetailResponse.

        导入作业时，指定表的时间格式

        :param timestamp_format: The timestamp_format of this ShowSqlJobDetailResponse.
        :type timestamp_format: str
        """
        self._timestamp_format = timestamp_format

    @property
    def compress(self):
        """Gets the compress of this ShowSqlJobDetailResponse.

          导出作业时，用户指定的压缩方式。

        :return: The compress of this ShowSqlJobDetailResponse.
        :rtype: str
        """
        return self._compress

    @compress.setter
    def compress(self, compress):
        """Sets the compress of this ShowSqlJobDetailResponse.

          导出作业时，用户指定的压缩方式。

        :param compress: The compress of this ShowSqlJobDetailResponse.
        :type compress: str
        """
        self._compress = compress

    @property
    def tags(self):
        """Gets the tags of this ShowSqlJobDetailResponse.

        作业标签

        :return: The tags of this ShowSqlJobDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowSqlJobDetailResponse.

        作业标签

        :param tags: The tags of this ShowSqlJobDetailResponse.
        :type tags: list[:class:`huaweicloudsdkdli.v1.TmsTagEntity`]
        """
        self._tags = tags

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
        if not isinstance(other, ShowSqlJobDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
