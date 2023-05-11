# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportDataRequestBody:

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
        'table_id': 'str',
        'with_column_header': 'str',
        'delimiter': 'str',
        'quote_char': 'str',
        'escape_char': 'str',
        'date_format': 'str',
        'bad_records_path': 'str',
        'timestamp_format': 'str',
        'computing_resource_id': 'str'
    }

    attribute_map = {
        'data_path': 'data_path',
        'data_type': 'data_type',
        'table_id': 'table_id',
        'with_column_header': 'with_column_header',
        'delimiter': 'delimiter',
        'quote_char': 'quote_char',
        'escape_char': 'escape_char',
        'date_format': 'date_format',
        'bad_records_path': 'bad_records_path',
        'timestamp_format': 'timestamp_format',
        'computing_resource_id': 'computing_resource_id'
    }

    def __init__(self, data_path=None, data_type=None, table_id=None, with_column_header=None, delimiter=None, quote_char=None, escape_char=None, date_format=None, bad_records_path=None, timestamp_format=None, computing_resource_id=None):
        """ImportDataRequestBody

        The model defined in huaweicloud sdk

        :param data_path: 导入的数据路径（当前仅支持导入OBS上的数据，且OBS路径须以s3a开头）。必须先把该OBS桶添加到离线数据源。
        :type data_path: str
        :param data_type: 导入的数据类型（当前支持csv、parquet、orc、json、avro数据类型）。
        :type data_type: str
        :param table_id: 表ID。
        :type table_id: str
        :param with_column_header: 导入数据中的第一行数据是否包括列名，即表头。默认为“false”，表示不包括列名。导入CSV类型数据时可指定。
        :type with_column_header: str
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
        :param computing_resource_id: 计算资源ID。
        :type computing_resource_id: str
        """
        
        

        self._data_path = None
        self._data_type = None
        self._table_id = None
        self._with_column_header = None
        self._delimiter = None
        self._quote_char = None
        self._escape_char = None
        self._date_format = None
        self._bad_records_path = None
        self._timestamp_format = None
        self._computing_resource_id = None
        self.discriminator = None

        self.data_path = data_path
        self.data_type = data_type
        self.table_id = table_id
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
        self.computing_resource_id = computing_resource_id

    @property
    def data_path(self):
        """Gets the data_path of this ImportDataRequestBody.

        导入的数据路径（当前仅支持导入OBS上的数据，且OBS路径须以s3a开头）。必须先把该OBS桶添加到离线数据源。

        :return: The data_path of this ImportDataRequestBody.
        :rtype: str
        """
        return self._data_path

    @data_path.setter
    def data_path(self, data_path):
        """Sets the data_path of this ImportDataRequestBody.

        导入的数据路径（当前仅支持导入OBS上的数据，且OBS路径须以s3a开头）。必须先把该OBS桶添加到离线数据源。

        :param data_path: The data_path of this ImportDataRequestBody.
        :type data_path: str
        """
        self._data_path = data_path

    @property
    def data_type(self):
        """Gets the data_type of this ImportDataRequestBody.

        导入的数据类型（当前支持csv、parquet、orc、json、avro数据类型）。

        :return: The data_type of this ImportDataRequestBody.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ImportDataRequestBody.

        导入的数据类型（当前支持csv、parquet、orc、json、avro数据类型）。

        :param data_type: The data_type of this ImportDataRequestBody.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def table_id(self):
        """Gets the table_id of this ImportDataRequestBody.

        表ID。

        :return: The table_id of this ImportDataRequestBody.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this ImportDataRequestBody.

        表ID。

        :param table_id: The table_id of this ImportDataRequestBody.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def with_column_header(self):
        """Gets the with_column_header of this ImportDataRequestBody.

        导入数据中的第一行数据是否包括列名，即表头。默认为“false”，表示不包括列名。导入CSV类型数据时可指定。

        :return: The with_column_header of this ImportDataRequestBody.
        :rtype: str
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        """Sets the with_column_header of this ImportDataRequestBody.

        导入数据中的第一行数据是否包括列名，即表头。默认为“false”，表示不包括列名。导入CSV类型数据时可指定。

        :param with_column_header: The with_column_header of this ImportDataRequestBody.
        :type with_column_header: str
        """
        self._with_column_header = with_column_header

    @property
    def delimiter(self):
        """Gets the delimiter of this ImportDataRequestBody.

        用户自定义数据分隔符，默认为逗号。导入CSV类型数据时可指定。

        :return: The delimiter of this ImportDataRequestBody.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this ImportDataRequestBody.

        用户自定义数据分隔符，默认为逗号。导入CSV类型数据时可指定。

        :param delimiter: The delimiter of this ImportDataRequestBody.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def quote_char(self):
        """Gets the quote_char of this ImportDataRequestBody.

        用户自定义引用字符，默认为双引号。导入CSV类型数据时可指定。

        :return: The quote_char of this ImportDataRequestBody.
        :rtype: str
        """
        return self._quote_char

    @quote_char.setter
    def quote_char(self, quote_char):
        """Sets the quote_char of this ImportDataRequestBody.

        用户自定义引用字符，默认为双引号。导入CSV类型数据时可指定。

        :param quote_char: The quote_char of this ImportDataRequestBody.
        :type quote_char: str
        """
        self._quote_char = quote_char

    @property
    def escape_char(self):
        """Gets the escape_char of this ImportDataRequestBody.

        用户自定义转义字符，默认为反斜杠。导入CSV类型数据时可指定。

        :return: The escape_char of this ImportDataRequestBody.
        :rtype: str
        """
        return self._escape_char

    @escape_char.setter
    def escape_char(self, escape_char):
        """Sets the escape_char of this ImportDataRequestBody.

        用户自定义转义字符，默认为反斜杠。导入CSV类型数据时可指定。

        :param escape_char: The escape_char of this ImportDataRequestBody.
        :type escape_char: str
        """
        self._escape_char = escape_char

    @property
    def date_format(self):
        """Gets the date_format of this ImportDataRequestBody.

        指定特定的日期格式，默认为“yyyy-MM-dd”。日期格式字符定义详见表3。导入CSV及JSON类型数据时可指定。

        :return: The date_format of this ImportDataRequestBody.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this ImportDataRequestBody.

        指定特定的日期格式，默认为“yyyy-MM-dd”。日期格式字符定义详见表3。导入CSV及JSON类型数据时可指定。

        :param date_format: The date_format of this ImportDataRequestBody.
        :type date_format: str
        """
        self._date_format = date_format

    @property
    def bad_records_path(self):
        """Gets the bad_records_path of this ImportDataRequestBody.

        作业执行过程中的bad records存储目录。设置该配置项后，bad records不会导入到目标表。

        :return: The bad_records_path of this ImportDataRequestBody.
        :rtype: str
        """
        return self._bad_records_path

    @bad_records_path.setter
    def bad_records_path(self, bad_records_path):
        """Sets the bad_records_path of this ImportDataRequestBody.

        作业执行过程中的bad records存储目录。设置该配置项后，bad records不会导入到目标表。

        :param bad_records_path: The bad_records_path of this ImportDataRequestBody.
        :type bad_records_path: str
        """
        self._bad_records_path = bad_records_path

    @property
    def timestamp_format(self):
        """Gets the timestamp_format of this ImportDataRequestBody.

        指定特定的时间格式，默认为“yyyy-MM-dd HH:mm:ss”。时间格式字符定义详见表3。导入CSV及JSON类型数据时可指定。

        :return: The timestamp_format of this ImportDataRequestBody.
        :rtype: str
        """
        return self._timestamp_format

    @timestamp_format.setter
    def timestamp_format(self, timestamp_format):
        """Sets the timestamp_format of this ImportDataRequestBody.

        指定特定的时间格式，默认为“yyyy-MM-dd HH:mm:ss”。时间格式字符定义详见表3。导入CSV及JSON类型数据时可指定。

        :param timestamp_format: The timestamp_format of this ImportDataRequestBody.
        :type timestamp_format: str
        """
        self._timestamp_format = timestamp_format

    @property
    def computing_resource_id(self):
        """Gets the computing_resource_id of this ImportDataRequestBody.

        计算资源ID。

        :return: The computing_resource_id of this ImportDataRequestBody.
        :rtype: str
        """
        return self._computing_resource_id

    @computing_resource_id.setter
    def computing_resource_id(self, computing_resource_id):
        """Sets the computing_resource_id of this ImportDataRequestBody.

        计算资源ID。

        :param computing_resource_id: The computing_resource_id of this ImportDataRequestBody.
        :type computing_resource_id: str
        """
        self._computing_resource_id = computing_resource_id

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
        if not isinstance(other, ImportDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
