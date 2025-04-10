# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportTableRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_path': 'str',
        'data_type': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'with_column_header': 'bool',
        'delimiter': 'str',
        'quote_char': 'str',
        'escape_char': 'str',
        'date_format': 'str',
        'bad_records_path': 'str',
        'timestamp_format': 'str',
        'queue_name': 'str',
        'overwrite': 'bool',
        'partition_spec': 'str',
        'conf': 'list[str]'
    }

    attribute_map = {
        'data_path': 'data_path',
        'data_type': 'data_type',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'with_column_header': 'with_column_header',
        'delimiter': 'delimiter',
        'quote_char': 'quote_char',
        'escape_char': 'escape_char',
        'date_format': 'date_format',
        'bad_records_path': 'bad_records_path',
        'timestamp_format': 'timestamp_format',
        'queue_name': 'queue_name',
        'overwrite': 'overwrite',
        'partition_spec': 'partition_spec',
        'conf': 'conf'
    }

    def __init__(self, data_path=None, data_type=None, database_name=None, table_name=None, with_column_header=None, delimiter=None, quote_char=None, escape_char=None, date_format=None, bad_records_path=None, timestamp_format=None, queue_name=None, overwrite=None, partition_spec=None, conf=None):
        r"""ImportTableRequestBody

        The model defined in huaweicloud sdk

        :param data_path: 导入的数据路径（当前仅支持导入OBS上的数据，且OBS路径须以s3a开头）。
        :type data_path: str
        :param data_type: 导入的数据类型（当前支持csv、parquet、orc、json、avro数据类型）。
        :type data_type: str
        :param database_name: 导入表所属的数据库名称。
        :type database_name: str
        :param table_name: 导入表的名称。
        :type table_name: str
        :param with_column_header: 导入数据中的第一行数据是否包括列名，即表头。默认为“false”，表示不包括列名。导入CSV类型数据时可指定。
        :type with_column_header: bool
        :param delimiter: 用户自定义数据分隔符，默认为逗号。导入CSV类型数据时可指定。
        :type delimiter: str
        :param quote_char: 用户自定义引用字符，默认为双引号。导入CSV类型数据时可指定。
        :type quote_char: str
        :param escape_char: 用户自定义转义字符，默认为反斜杠。导入CSV类型数据时可指定。
        :type escape_char: str
        :param date_format: 指定特定的日期格式，默认为“yyyy-MM-dd”。日期格式字符定义详见表3。导入CSV及JSON类型数据时可指定。
        :type date_format: str
        :param bad_records_path: 作业执行过程中的bad records存储目录。设置该配置项后，bad records不会导入到目标表。
        :type bad_records_path: str
        :param timestamp_format: 指定特定的时间格式，默认为“yyyy-MM-dd HH:mm:ss”。时间格式字符定义详见表3。导入CSV及JSON类型数据时可指定。
        :type timestamp_format: str
        :param queue_name: 指定执行该任务的队列。若不指定队列，将采用default队列执行操作。
        :type queue_name: str
        :param overwrite: 是否覆盖之前的数据
        :type overwrite: bool
        :param partition_spec: 表示需要导入到哪个分区
        :type partition_spec: str
        :param conf: 用于定义此配置项的参数
        :type conf: list[str]
        """
        
        

        self._data_path = None
        self._data_type = None
        self._database_name = None
        self._table_name = None
        self._with_column_header = None
        self._delimiter = None
        self._quote_char = None
        self._escape_char = None
        self._date_format = None
        self._bad_records_path = None
        self._timestamp_format = None
        self._queue_name = None
        self._overwrite = None
        self._partition_spec = None
        self._conf = None
        self.discriminator = None

        self.data_path = data_path
        self.data_type = data_type
        self.database_name = database_name
        self.table_name = table_name
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
        if bad_records_path is not None:
            self.bad_records_path = bad_records_path
        if timestamp_format is not None:
            self.timestamp_format = timestamp_format
        if queue_name is not None:
            self.queue_name = queue_name
        if overwrite is not None:
            self.overwrite = overwrite
        if partition_spec is not None:
            self.partition_spec = partition_spec
        if conf is not None:
            self.conf = conf

    @property
    def data_path(self):
        r"""Gets the data_path of this ImportTableRequestBody.

        导入的数据路径（当前仅支持导入OBS上的数据，且OBS路径须以s3a开头）。

        :return: The data_path of this ImportTableRequestBody.
        :rtype: str
        """
        return self._data_path

    @data_path.setter
    def data_path(self, data_path):
        r"""Sets the data_path of this ImportTableRequestBody.

        导入的数据路径（当前仅支持导入OBS上的数据，且OBS路径须以s3a开头）。

        :param data_path: The data_path of this ImportTableRequestBody.
        :type data_path: str
        """
        self._data_path = data_path

    @property
    def data_type(self):
        r"""Gets the data_type of this ImportTableRequestBody.

        导入的数据类型（当前支持csv、parquet、orc、json、avro数据类型）。

        :return: The data_type of this ImportTableRequestBody.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this ImportTableRequestBody.

        导入的数据类型（当前支持csv、parquet、orc、json、avro数据类型）。

        :param data_type: The data_type of this ImportTableRequestBody.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def database_name(self):
        r"""Gets the database_name of this ImportTableRequestBody.

        导入表所属的数据库名称。

        :return: The database_name of this ImportTableRequestBody.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ImportTableRequestBody.

        导入表所属的数据库名称。

        :param database_name: The database_name of this ImportTableRequestBody.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ImportTableRequestBody.

        导入表的名称。

        :return: The table_name of this ImportTableRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ImportTableRequestBody.

        导入表的名称。

        :param table_name: The table_name of this ImportTableRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def with_column_header(self):
        r"""Gets the with_column_header of this ImportTableRequestBody.

        导入数据中的第一行数据是否包括列名，即表头。默认为“false”，表示不包括列名。导入CSV类型数据时可指定。

        :return: The with_column_header of this ImportTableRequestBody.
        :rtype: bool
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        r"""Sets the with_column_header of this ImportTableRequestBody.

        导入数据中的第一行数据是否包括列名，即表头。默认为“false”，表示不包括列名。导入CSV类型数据时可指定。

        :param with_column_header: The with_column_header of this ImportTableRequestBody.
        :type with_column_header: bool
        """
        self._with_column_header = with_column_header

    @property
    def delimiter(self):
        r"""Gets the delimiter of this ImportTableRequestBody.

        用户自定义数据分隔符，默认为逗号。导入CSV类型数据时可指定。

        :return: The delimiter of this ImportTableRequestBody.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        r"""Sets the delimiter of this ImportTableRequestBody.

        用户自定义数据分隔符，默认为逗号。导入CSV类型数据时可指定。

        :param delimiter: The delimiter of this ImportTableRequestBody.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def quote_char(self):
        r"""Gets the quote_char of this ImportTableRequestBody.

        用户自定义引用字符，默认为双引号。导入CSV类型数据时可指定。

        :return: The quote_char of this ImportTableRequestBody.
        :rtype: str
        """
        return self._quote_char

    @quote_char.setter
    def quote_char(self, quote_char):
        r"""Sets the quote_char of this ImportTableRequestBody.

        用户自定义引用字符，默认为双引号。导入CSV类型数据时可指定。

        :param quote_char: The quote_char of this ImportTableRequestBody.
        :type quote_char: str
        """
        self._quote_char = quote_char

    @property
    def escape_char(self):
        r"""Gets the escape_char of this ImportTableRequestBody.

        用户自定义转义字符，默认为反斜杠。导入CSV类型数据时可指定。

        :return: The escape_char of this ImportTableRequestBody.
        :rtype: str
        """
        return self._escape_char

    @escape_char.setter
    def escape_char(self, escape_char):
        r"""Sets the escape_char of this ImportTableRequestBody.

        用户自定义转义字符，默认为反斜杠。导入CSV类型数据时可指定。

        :param escape_char: The escape_char of this ImportTableRequestBody.
        :type escape_char: str
        """
        self._escape_char = escape_char

    @property
    def date_format(self):
        r"""Gets the date_format of this ImportTableRequestBody.

        指定特定的日期格式，默认为“yyyy-MM-dd”。日期格式字符定义详见表3。导入CSV及JSON类型数据时可指定。

        :return: The date_format of this ImportTableRequestBody.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        r"""Sets the date_format of this ImportTableRequestBody.

        指定特定的日期格式，默认为“yyyy-MM-dd”。日期格式字符定义详见表3。导入CSV及JSON类型数据时可指定。

        :param date_format: The date_format of this ImportTableRequestBody.
        :type date_format: str
        """
        self._date_format = date_format

    @property
    def bad_records_path(self):
        r"""Gets the bad_records_path of this ImportTableRequestBody.

        作业执行过程中的bad records存储目录。设置该配置项后，bad records不会导入到目标表。

        :return: The bad_records_path of this ImportTableRequestBody.
        :rtype: str
        """
        return self._bad_records_path

    @bad_records_path.setter
    def bad_records_path(self, bad_records_path):
        r"""Sets the bad_records_path of this ImportTableRequestBody.

        作业执行过程中的bad records存储目录。设置该配置项后，bad records不会导入到目标表。

        :param bad_records_path: The bad_records_path of this ImportTableRequestBody.
        :type bad_records_path: str
        """
        self._bad_records_path = bad_records_path

    @property
    def timestamp_format(self):
        r"""Gets the timestamp_format of this ImportTableRequestBody.

        指定特定的时间格式，默认为“yyyy-MM-dd HH:mm:ss”。时间格式字符定义详见表3。导入CSV及JSON类型数据时可指定。

        :return: The timestamp_format of this ImportTableRequestBody.
        :rtype: str
        """
        return self._timestamp_format

    @timestamp_format.setter
    def timestamp_format(self, timestamp_format):
        r"""Sets the timestamp_format of this ImportTableRequestBody.

        指定特定的时间格式，默认为“yyyy-MM-dd HH:mm:ss”。时间格式字符定义详见表3。导入CSV及JSON类型数据时可指定。

        :param timestamp_format: The timestamp_format of this ImportTableRequestBody.
        :type timestamp_format: str
        """
        self._timestamp_format = timestamp_format

    @property
    def queue_name(self):
        r"""Gets the queue_name of this ImportTableRequestBody.

        指定执行该任务的队列。若不指定队列，将采用default队列执行操作。

        :return: The queue_name of this ImportTableRequestBody.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this ImportTableRequestBody.

        指定执行该任务的队列。若不指定队列，将采用default队列执行操作。

        :param queue_name: The queue_name of this ImportTableRequestBody.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def overwrite(self):
        r"""Gets the overwrite of this ImportTableRequestBody.

        是否覆盖之前的数据

        :return: The overwrite of this ImportTableRequestBody.
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        r"""Sets the overwrite of this ImportTableRequestBody.

        是否覆盖之前的数据

        :param overwrite: The overwrite of this ImportTableRequestBody.
        :type overwrite: bool
        """
        self._overwrite = overwrite

    @property
    def partition_spec(self):
        r"""Gets the partition_spec of this ImportTableRequestBody.

        表示需要导入到哪个分区

        :return: The partition_spec of this ImportTableRequestBody.
        :rtype: str
        """
        return self._partition_spec

    @partition_spec.setter
    def partition_spec(self, partition_spec):
        r"""Sets the partition_spec of this ImportTableRequestBody.

        表示需要导入到哪个分区

        :param partition_spec: The partition_spec of this ImportTableRequestBody.
        :type partition_spec: str
        """
        self._partition_spec = partition_spec

    @property
    def conf(self):
        r"""Gets the conf of this ImportTableRequestBody.

        用于定义此配置项的参数

        :return: The conf of this ImportTableRequestBody.
        :rtype: list[str]
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        r"""Sets the conf of this ImportTableRequestBody.

        用于定义此配置项的参数

        :param conf: The conf of this ImportTableRequestBody.
        :type conf: list[str]
        """
        self._conf = conf

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
        if not isinstance(other, ImportTableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
