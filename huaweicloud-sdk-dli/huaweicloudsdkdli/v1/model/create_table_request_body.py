# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTableRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'data_location': 'str',
        'description': 'str',
        'columns': 'list[Column]',
        'data_type': 'str',
        'data_path': 'str',
        'with_column_header': 'bool',
        'delimiter': 'str',
        'quote_char': 'str',
        'escape_char': 'str',
        'date_format': 'str',
        'timestamp_format': 'str',
        'select_statement': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'table_name': 'table_name',
        'data_location': 'data_location',
        'description': 'description',
        'columns': 'columns',
        'data_type': 'data_type',
        'data_path': 'data_path',
        'with_column_header': 'with_column_header',
        'delimiter': 'delimiter',
        'quote_char': 'quote_char',
        'escape_char': 'escape_char',
        'date_format': 'date_format',
        'timestamp_format': 'timestamp_format',
        'select_statement': 'select_statement',
        'tags': 'tags'
    }

    def __init__(self, table_name=None, data_location=None, description=None, columns=None, data_type=None, data_path=None, with_column_header=None, delimiter=None, quote_char=None, escape_char=None, date_format=None, timestamp_format=None, select_statement=None, tags=None):
        """CreateTableRequestBody

        The model defined in huaweicloud sdk

        :param table_name: 新增表名称。
        :type table_name: str
        :param data_location: 数据存储的地方，分VIEW视图，OBS表和DLI表。
        :type data_location: str
        :param description: 新增表的描述信息。
        :type description: str
        :param columns: OBS表和DLI表必选参数。新增表的列。
        :type columns: list[:class:`huaweicloudsdkdli.v1.Column`]
        :param data_type: OBS表必选参数。新增OBS表数据的类型，目前支持：Parquet、ORC、CSV、JSON、Carbon和Avro格式。
        :type data_type: str
        :param data_path: OBS表必选参数。新增OBS表数据的存储路径，必须是OBS上的路径，以s3a开头。
        :type data_path: str
        :param with_column_header: OBS表非必选参数。OBS表数据是否包含表头。只有CSV类型数据具有该属性。
        :type with_column_header: bool
        :param delimiter: OBS表非必选参数。用户自定义数据分隔符。只有CSV类型数据具有该属性。
        :type delimiter: str
        :param quote_char: OBS表非必选参数。用户自定义引用字符，默认为双引号（即“\\\&quot;”）。只有CSV类型数据具有该属性。
        :type quote_char: str
        :param escape_char: OBS表非必选参数。用户自定义转义字符，默认为反斜杠（即\&quot;\\\\\&quot;）。只有CSV类型数据具有该属性。
        :type escape_char: str
        :param date_format: OBS表非必选参数。用户自定义日期类型，默认格式为“yyyy-MM-dd”。只有CSV和JSON类型数据具有该属性。
        :type date_format: str
        :param timestamp_format: OBS表非必选参数。用户自定义时间类型。默认格式为“yyyy-MM-dd HH:mm:ss”。只有CSV和JSON类型数据具有该属性。
        :type timestamp_format: str
        :param select_statement: VIEW视图必选参数，创建视图时的数据选择语句。语句中涉及表需要使用“表&#x3D;库名.表名”的格式
        :type select_statement: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        
        

        self._table_name = None
        self._data_location = None
        self._description = None
        self._columns = None
        self._data_type = None
        self._data_path = None
        self._with_column_header = None
        self._delimiter = None
        self._quote_char = None
        self._escape_char = None
        self._date_format = None
        self._timestamp_format = None
        self._select_statement = None
        self._tags = None
        self.discriminator = None

        self.table_name = table_name
        self.data_location = data_location
        if description is not None:
            self.description = description
        self.columns = columns
        if data_type is not None:
            self.data_type = data_type
        if data_path is not None:
            self.data_path = data_path
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
        if select_statement is not None:
            self.select_statement = select_statement
        if tags is not None:
            self.tags = tags

    @property
    def table_name(self):
        """Gets the table_name of this CreateTableRequestBody.

        新增表名称。

        :return: The table_name of this CreateTableRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this CreateTableRequestBody.

        新增表名称。

        :param table_name: The table_name of this CreateTableRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def data_location(self):
        """Gets the data_location of this CreateTableRequestBody.

        数据存储的地方，分VIEW视图，OBS表和DLI表。

        :return: The data_location of this CreateTableRequestBody.
        :rtype: str
        """
        return self._data_location

    @data_location.setter
    def data_location(self, data_location):
        """Sets the data_location of this CreateTableRequestBody.

        数据存储的地方，分VIEW视图，OBS表和DLI表。

        :param data_location: The data_location of this CreateTableRequestBody.
        :type data_location: str
        """
        self._data_location = data_location

    @property
    def description(self):
        """Gets the description of this CreateTableRequestBody.

        新增表的描述信息。

        :return: The description of this CreateTableRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateTableRequestBody.

        新增表的描述信息。

        :param description: The description of this CreateTableRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def columns(self):
        """Gets the columns of this CreateTableRequestBody.

        OBS表和DLI表必选参数。新增表的列。

        :return: The columns of this CreateTableRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Column`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this CreateTableRequestBody.

        OBS表和DLI表必选参数。新增表的列。

        :param columns: The columns of this CreateTableRequestBody.
        :type columns: list[:class:`huaweicloudsdkdli.v1.Column`]
        """
        self._columns = columns

    @property
    def data_type(self):
        """Gets the data_type of this CreateTableRequestBody.

        OBS表必选参数。新增OBS表数据的类型，目前支持：Parquet、ORC、CSV、JSON、Carbon和Avro格式。

        :return: The data_type of this CreateTableRequestBody.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this CreateTableRequestBody.

        OBS表必选参数。新增OBS表数据的类型，目前支持：Parquet、ORC、CSV、JSON、Carbon和Avro格式。

        :param data_type: The data_type of this CreateTableRequestBody.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def data_path(self):
        """Gets the data_path of this CreateTableRequestBody.

        OBS表必选参数。新增OBS表数据的存储路径，必须是OBS上的路径，以s3a开头。

        :return: The data_path of this CreateTableRequestBody.
        :rtype: str
        """
        return self._data_path

    @data_path.setter
    def data_path(self, data_path):
        """Sets the data_path of this CreateTableRequestBody.

        OBS表必选参数。新增OBS表数据的存储路径，必须是OBS上的路径，以s3a开头。

        :param data_path: The data_path of this CreateTableRequestBody.
        :type data_path: str
        """
        self._data_path = data_path

    @property
    def with_column_header(self):
        """Gets the with_column_header of this CreateTableRequestBody.

        OBS表非必选参数。OBS表数据是否包含表头。只有CSV类型数据具有该属性。

        :return: The with_column_header of this CreateTableRequestBody.
        :rtype: bool
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        """Sets the with_column_header of this CreateTableRequestBody.

        OBS表非必选参数。OBS表数据是否包含表头。只有CSV类型数据具有该属性。

        :param with_column_header: The with_column_header of this CreateTableRequestBody.
        :type with_column_header: bool
        """
        self._with_column_header = with_column_header

    @property
    def delimiter(self):
        """Gets the delimiter of this CreateTableRequestBody.

        OBS表非必选参数。用户自定义数据分隔符。只有CSV类型数据具有该属性。

        :return: The delimiter of this CreateTableRequestBody.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this CreateTableRequestBody.

        OBS表非必选参数。用户自定义数据分隔符。只有CSV类型数据具有该属性。

        :param delimiter: The delimiter of this CreateTableRequestBody.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def quote_char(self):
        """Gets the quote_char of this CreateTableRequestBody.

        OBS表非必选参数。用户自定义引用字符，默认为双引号（即“\\\"”）。只有CSV类型数据具有该属性。

        :return: The quote_char of this CreateTableRequestBody.
        :rtype: str
        """
        return self._quote_char

    @quote_char.setter
    def quote_char(self, quote_char):
        """Sets the quote_char of this CreateTableRequestBody.

        OBS表非必选参数。用户自定义引用字符，默认为双引号（即“\\\"”）。只有CSV类型数据具有该属性。

        :param quote_char: The quote_char of this CreateTableRequestBody.
        :type quote_char: str
        """
        self._quote_char = quote_char

    @property
    def escape_char(self):
        """Gets the escape_char of this CreateTableRequestBody.

        OBS表非必选参数。用户自定义转义字符，默认为反斜杠（即\"\\\\\"）。只有CSV类型数据具有该属性。

        :return: The escape_char of this CreateTableRequestBody.
        :rtype: str
        """
        return self._escape_char

    @escape_char.setter
    def escape_char(self, escape_char):
        """Sets the escape_char of this CreateTableRequestBody.

        OBS表非必选参数。用户自定义转义字符，默认为反斜杠（即\"\\\\\"）。只有CSV类型数据具有该属性。

        :param escape_char: The escape_char of this CreateTableRequestBody.
        :type escape_char: str
        """
        self._escape_char = escape_char

    @property
    def date_format(self):
        """Gets the date_format of this CreateTableRequestBody.

        OBS表非必选参数。用户自定义日期类型，默认格式为“yyyy-MM-dd”。只有CSV和JSON类型数据具有该属性。

        :return: The date_format of this CreateTableRequestBody.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this CreateTableRequestBody.

        OBS表非必选参数。用户自定义日期类型，默认格式为“yyyy-MM-dd”。只有CSV和JSON类型数据具有该属性。

        :param date_format: The date_format of this CreateTableRequestBody.
        :type date_format: str
        """
        self._date_format = date_format

    @property
    def timestamp_format(self):
        """Gets the timestamp_format of this CreateTableRequestBody.

        OBS表非必选参数。用户自定义时间类型。默认格式为“yyyy-MM-dd HH:mm:ss”。只有CSV和JSON类型数据具有该属性。

        :return: The timestamp_format of this CreateTableRequestBody.
        :rtype: str
        """
        return self._timestamp_format

    @timestamp_format.setter
    def timestamp_format(self, timestamp_format):
        """Sets the timestamp_format of this CreateTableRequestBody.

        OBS表非必选参数。用户自定义时间类型。默认格式为“yyyy-MM-dd HH:mm:ss”。只有CSV和JSON类型数据具有该属性。

        :param timestamp_format: The timestamp_format of this CreateTableRequestBody.
        :type timestamp_format: str
        """
        self._timestamp_format = timestamp_format

    @property
    def select_statement(self):
        """Gets the select_statement of this CreateTableRequestBody.

        VIEW视图必选参数，创建视图时的数据选择语句。语句中涉及表需要使用“表=库名.表名”的格式

        :return: The select_statement of this CreateTableRequestBody.
        :rtype: str
        """
        return self._select_statement

    @select_statement.setter
    def select_statement(self, select_statement):
        """Sets the select_statement of this CreateTableRequestBody.

        VIEW视图必选参数，创建视图时的数据选择语句。语句中涉及表需要使用“表=库名.表名”的格式

        :param select_statement: The select_statement of this CreateTableRequestBody.
        :type select_statement: str
        """
        self._select_statement = select_statement

    @property
    def tags(self):
        """Gets the tags of this CreateTableRequestBody.

        标签

        :return: The tags of this CreateTableRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateTableRequestBody.

        标签

        :param tags: The tags of this CreateTableRequestBody.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
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
        if not isinstance(other, CreateTableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
