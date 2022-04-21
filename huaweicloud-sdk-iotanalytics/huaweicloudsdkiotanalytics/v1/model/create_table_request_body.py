# coding: utf-8

import re
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
        'tags': 'str',
        'table_name': 'str',
        'table_alias': 'str',
        'description': 'str',
        'columns': 'list[Column]',
        'data_type': 'str',
        'data_source': 'str',
        'data_store_id': 'str',
        'with_column_header': 'bool',
        'delimiter': 'str',
        'quote_char': 'str',
        'escape_char': 'str',
        'date_format': 'str',
        'timestamp_format': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'table_name': 'table_name',
        'table_alias': 'table_alias',
        'description': 'description',
        'columns': 'columns',
        'data_type': 'data_type',
        'data_source': 'data_source',
        'data_store_id': 'data_store_id',
        'with_column_header': 'with_column_header',
        'delimiter': 'delimiter',
        'quote_char': 'quote_char',
        'escape_char': 'escape_char',
        'date_format': 'date_format',
        'timestamp_format': 'timestamp_format'
    }

    def __init__(self, tags=None, table_name=None, table_alias=None, description=None, columns=None, data_type=None, data_source=None, data_store_id=None, with_column_header=None, delimiter=None, quote_char=None, escape_char=None, date_format=None, timestamp_format=None):
        """CreateTableRequestBody

        The model defined in huaweicloud sdk

        :param tags: 标签。只能包含数字、英文字母、中文字符、下划线、中划线、逗号以及斜杠。长度为0~128。
        :type tags: str
        :param table_name: 新增表名称。
        :type table_name: str
        :param table_alias: 新增表别名。只能包含数字、英文字母、中文字符、下划线以及中划线。长度为0~32。
        :type table_alias: str
        :param description: 新增表的描述信息。
        :type description: str
        :param columns: 新增表的描述信息。
        :type columns: list[:class:`huaweicloudsdkiotanalytics.v1.Column`]
        :param data_type: 新增表的数据类型，目前支持：Parquet、CSV格式。
        :type data_type: str
        :param data_source: 数据来源。来源类型有：pipeline, default. 默认为default.
        :type data_source: str
        :param data_store_id: 仅当数据来源为pipeline时使用。数据的Data Store ID.
        :type data_store_id: str
        :param with_column_header: 表数据是否包含表头。只有CSV类型数据具有该属性。
        :type with_column_header: bool
        :param delimiter: 用户自定义数据分隔符。只有CSV类型数据具有该属性。
        :type delimiter: str
        :param quote_char: 用户自定义引用字符，默认为双引号（即“\&quot;”）。只有CSV类型数据具有该属性。
        :type quote_char: str
        :param escape_char: 用户自定义转义字符，默认为反斜杠（即\\）。只有CSV类型数据具有该属性。
        :type escape_char: str
        :param date_format: 用户自定义日期类型，默认格式为“yyyy-MM-dd”。日期格式字符定义详见表3。只有CSV和JSON类型数据具有该属性。
        :type date_format: str
        :param timestamp_format: 用户自定义时间类型。默认格式为“yyyy-MM-dd HH:mm:ss”。时间戳格式字符定义详见表3。只有CSV和JSON类型数据具有该属性。
        :type timestamp_format: str
        """
        
        

        self._tags = None
        self._table_name = None
        self._table_alias = None
        self._description = None
        self._columns = None
        self._data_type = None
        self._data_source = None
        self._data_store_id = None
        self._with_column_header = None
        self._delimiter = None
        self._quote_char = None
        self._escape_char = None
        self._date_format = None
        self._timestamp_format = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        self.table_name = table_name
        if table_alias is not None:
            self.table_alias = table_alias
        if description is not None:
            self.description = description
        self.columns = columns
        self.data_type = data_type
        if data_source is not None:
            self.data_source = data_source
        if data_store_id is not None:
            self.data_store_id = data_store_id
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

    @property
    def tags(self):
        """Gets the tags of this CreateTableRequestBody.

        标签。只能包含数字、英文字母、中文字符、下划线、中划线、逗号以及斜杠。长度为0~128。

        :return: The tags of this CreateTableRequestBody.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateTableRequestBody.

        标签。只能包含数字、英文字母、中文字符、下划线、中划线、逗号以及斜杠。长度为0~128。

        :param tags: The tags of this CreateTableRequestBody.
        :type tags: str
        """
        self._tags = tags

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
    def table_alias(self):
        """Gets the table_alias of this CreateTableRequestBody.

        新增表别名。只能包含数字、英文字母、中文字符、下划线以及中划线。长度为0~32。

        :return: The table_alias of this CreateTableRequestBody.
        :rtype: str
        """
        return self._table_alias

    @table_alias.setter
    def table_alias(self, table_alias):
        """Sets the table_alias of this CreateTableRequestBody.

        新增表别名。只能包含数字、英文字母、中文字符、下划线以及中划线。长度为0~32。

        :param table_alias: The table_alias of this CreateTableRequestBody.
        :type table_alias: str
        """
        self._table_alias = table_alias

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

        新增表的描述信息。

        :return: The columns of this CreateTableRequestBody.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.Column`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this CreateTableRequestBody.

        新增表的描述信息。

        :param columns: The columns of this CreateTableRequestBody.
        :type columns: list[:class:`huaweicloudsdkiotanalytics.v1.Column`]
        """
        self._columns = columns

    @property
    def data_type(self):
        """Gets the data_type of this CreateTableRequestBody.

        新增表的数据类型，目前支持：Parquet、CSV格式。

        :return: The data_type of this CreateTableRequestBody.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this CreateTableRequestBody.

        新增表的数据类型，目前支持：Parquet、CSV格式。

        :param data_type: The data_type of this CreateTableRequestBody.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def data_source(self):
        """Gets the data_source of this CreateTableRequestBody.

        数据来源。来源类型有：pipeline, default. 默认为default.

        :return: The data_source of this CreateTableRequestBody.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source):
        """Sets the data_source of this CreateTableRequestBody.

        数据来源。来源类型有：pipeline, default. 默认为default.

        :param data_source: The data_source of this CreateTableRequestBody.
        :type data_source: str
        """
        self._data_source = data_source

    @property
    def data_store_id(self):
        """Gets the data_store_id of this CreateTableRequestBody.

        仅当数据来源为pipeline时使用。数据的Data Store ID.

        :return: The data_store_id of this CreateTableRequestBody.
        :rtype: str
        """
        return self._data_store_id

    @data_store_id.setter
    def data_store_id(self, data_store_id):
        """Sets the data_store_id of this CreateTableRequestBody.

        仅当数据来源为pipeline时使用。数据的Data Store ID.

        :param data_store_id: The data_store_id of this CreateTableRequestBody.
        :type data_store_id: str
        """
        self._data_store_id = data_store_id

    @property
    def with_column_header(self):
        """Gets the with_column_header of this CreateTableRequestBody.

        表数据是否包含表头。只有CSV类型数据具有该属性。

        :return: The with_column_header of this CreateTableRequestBody.
        :rtype: bool
        """
        return self._with_column_header

    @with_column_header.setter
    def with_column_header(self, with_column_header):
        """Sets the with_column_header of this CreateTableRequestBody.

        表数据是否包含表头。只有CSV类型数据具有该属性。

        :param with_column_header: The with_column_header of this CreateTableRequestBody.
        :type with_column_header: bool
        """
        self._with_column_header = with_column_header

    @property
    def delimiter(self):
        """Gets the delimiter of this CreateTableRequestBody.

        用户自定义数据分隔符。只有CSV类型数据具有该属性。

        :return: The delimiter of this CreateTableRequestBody.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this CreateTableRequestBody.

        用户自定义数据分隔符。只有CSV类型数据具有该属性。

        :param delimiter: The delimiter of this CreateTableRequestBody.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def quote_char(self):
        """Gets the quote_char of this CreateTableRequestBody.

        用户自定义引用字符，默认为双引号（即“\"”）。只有CSV类型数据具有该属性。

        :return: The quote_char of this CreateTableRequestBody.
        :rtype: str
        """
        return self._quote_char

    @quote_char.setter
    def quote_char(self, quote_char):
        """Sets the quote_char of this CreateTableRequestBody.

        用户自定义引用字符，默认为双引号（即“\"”）。只有CSV类型数据具有该属性。

        :param quote_char: The quote_char of this CreateTableRequestBody.
        :type quote_char: str
        """
        self._quote_char = quote_char

    @property
    def escape_char(self):
        """Gets the escape_char of this CreateTableRequestBody.

        用户自定义转义字符，默认为反斜杠（即\\）。只有CSV类型数据具有该属性。

        :return: The escape_char of this CreateTableRequestBody.
        :rtype: str
        """
        return self._escape_char

    @escape_char.setter
    def escape_char(self, escape_char):
        """Sets the escape_char of this CreateTableRequestBody.

        用户自定义转义字符，默认为反斜杠（即\\）。只有CSV类型数据具有该属性。

        :param escape_char: The escape_char of this CreateTableRequestBody.
        :type escape_char: str
        """
        self._escape_char = escape_char

    @property
    def date_format(self):
        """Gets the date_format of this CreateTableRequestBody.

        用户自定义日期类型，默认格式为“yyyy-MM-dd”。日期格式字符定义详见表3。只有CSV和JSON类型数据具有该属性。

        :return: The date_format of this CreateTableRequestBody.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this CreateTableRequestBody.

        用户自定义日期类型，默认格式为“yyyy-MM-dd”。日期格式字符定义详见表3。只有CSV和JSON类型数据具有该属性。

        :param date_format: The date_format of this CreateTableRequestBody.
        :type date_format: str
        """
        self._date_format = date_format

    @property
    def timestamp_format(self):
        """Gets the timestamp_format of this CreateTableRequestBody.

        用户自定义时间类型。默认格式为“yyyy-MM-dd HH:mm:ss”。时间戳格式字符定义详见表3。只有CSV和JSON类型数据具有该属性。

        :return: The timestamp_format of this CreateTableRequestBody.
        :rtype: str
        """
        return self._timestamp_format

    @timestamp_format.setter
    def timestamp_format(self, timestamp_format):
        """Sets the timestamp_format of this CreateTableRequestBody.

        用户自定义时间类型。默认格式为“yyyy-MM-dd HH:mm:ss”。时间戳格式字符定义详见表3。只有CSV和JSON类型数据具有该属性。

        :param timestamp_format: The timestamp_format of this CreateTableRequestBody.
        :type timestamp_format: str
        """
        self._timestamp_format = timestamp_format

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
