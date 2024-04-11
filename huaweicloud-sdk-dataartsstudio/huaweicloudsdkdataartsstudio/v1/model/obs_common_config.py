# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OBSCommonConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_map': 'object',
        'path': 'str',
        'delimiter': 'str',
        'quote': 'str',
        'escape': 'str',
        'header': 'bool',
        'data_type': 'str',
        'date_format': 'str',
        'timestamp_format': 'str',
        'null_value': 'str',
        'comment': 'str',
        'parse_mode': 'str',
        'join_table': 'str'
    }

    attribute_map = {
        'column_map': 'column_map',
        'path': 'path',
        'delimiter': 'delimiter',
        'quote': 'quote',
        'escape': 'escape',
        'header': 'header',
        'data_type': 'data_type',
        'date_format': 'date_format',
        'timestamp_format': 'timestamp_format',
        'null_value': 'null_value',
        'comment': 'comment',
        'parse_mode': 'parse_mode',
        'join_table': 'join_table'
    }

    def __init__(self, column_map=None, path=None, delimiter=None, quote=None, escape=None, header=None, data_type=None, date_format=None, timestamp_format=None, null_value=None, comment=None, parse_mode=None, join_table=None):
        """OBSCommonConfig

        The model defined in huaweicloud sdk

        :param column_map: Map&lt;String, String&gt;结构
        :type column_map: object
        :param path: 路径
        :type path: str
        :param delimiter: 分隔符
        :type delimiter: str
        :param quote: 引用
        :type quote: str
        :param escape: 规避
        :type escape: str
        :param header: 是否是标头
        :type header: bool
        :param data_type: 数据类型
        :type data_type: str
        :param date_format: 数据格式
        :type date_format: str
        :param timestamp_format: 时间格式
        :type timestamp_format: str
        :param null_value: 为空时默认值
        :type null_value: str
        :param comment: 注解
        :type comment: str
        :param parse_mode: 解析模式
        :type parse_mode: str
        :param join_table: 联表
        :type join_table: str
        """
        
        

        self._column_map = None
        self._path = None
        self._delimiter = None
        self._quote = None
        self._escape = None
        self._header = None
        self._data_type = None
        self._date_format = None
        self._timestamp_format = None
        self._null_value = None
        self._comment = None
        self._parse_mode = None
        self._join_table = None
        self.discriminator = None

        if column_map is not None:
            self.column_map = column_map
        if path is not None:
            self.path = path
        if delimiter is not None:
            self.delimiter = delimiter
        if quote is not None:
            self.quote = quote
        if escape is not None:
            self.escape = escape
        if header is not None:
            self.header = header
        if data_type is not None:
            self.data_type = data_type
        if date_format is not None:
            self.date_format = date_format
        if timestamp_format is not None:
            self.timestamp_format = timestamp_format
        if null_value is not None:
            self.null_value = null_value
        if comment is not None:
            self.comment = comment
        if parse_mode is not None:
            self.parse_mode = parse_mode
        if join_table is not None:
            self.join_table = join_table

    @property
    def column_map(self):
        """Gets the column_map of this OBSCommonConfig.

        Map<String, String>结构

        :return: The column_map of this OBSCommonConfig.
        :rtype: object
        """
        return self._column_map

    @column_map.setter
    def column_map(self, column_map):
        """Sets the column_map of this OBSCommonConfig.

        Map<String, String>结构

        :param column_map: The column_map of this OBSCommonConfig.
        :type column_map: object
        """
        self._column_map = column_map

    @property
    def path(self):
        """Gets the path of this OBSCommonConfig.

        路径

        :return: The path of this OBSCommonConfig.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this OBSCommonConfig.

        路径

        :param path: The path of this OBSCommonConfig.
        :type path: str
        """
        self._path = path

    @property
    def delimiter(self):
        """Gets the delimiter of this OBSCommonConfig.

        分隔符

        :return: The delimiter of this OBSCommonConfig.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """Sets the delimiter of this OBSCommonConfig.

        分隔符

        :param delimiter: The delimiter of this OBSCommonConfig.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def quote(self):
        """Gets the quote of this OBSCommonConfig.

        引用

        :return: The quote of this OBSCommonConfig.
        :rtype: str
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this OBSCommonConfig.

        引用

        :param quote: The quote of this OBSCommonConfig.
        :type quote: str
        """
        self._quote = quote

    @property
    def escape(self):
        """Gets the escape of this OBSCommonConfig.

        规避

        :return: The escape of this OBSCommonConfig.
        :rtype: str
        """
        return self._escape

    @escape.setter
    def escape(self, escape):
        """Sets the escape of this OBSCommonConfig.

        规避

        :param escape: The escape of this OBSCommonConfig.
        :type escape: str
        """
        self._escape = escape

    @property
    def header(self):
        """Gets the header of this OBSCommonConfig.

        是否是标头

        :return: The header of this OBSCommonConfig.
        :rtype: bool
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this OBSCommonConfig.

        是否是标头

        :param header: The header of this OBSCommonConfig.
        :type header: bool
        """
        self._header = header

    @property
    def data_type(self):
        """Gets the data_type of this OBSCommonConfig.

        数据类型

        :return: The data_type of this OBSCommonConfig.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this OBSCommonConfig.

        数据类型

        :param data_type: The data_type of this OBSCommonConfig.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def date_format(self):
        """Gets the date_format of this OBSCommonConfig.

        数据格式

        :return: The date_format of this OBSCommonConfig.
        :rtype: str
        """
        return self._date_format

    @date_format.setter
    def date_format(self, date_format):
        """Sets the date_format of this OBSCommonConfig.

        数据格式

        :param date_format: The date_format of this OBSCommonConfig.
        :type date_format: str
        """
        self._date_format = date_format

    @property
    def timestamp_format(self):
        """Gets the timestamp_format of this OBSCommonConfig.

        时间格式

        :return: The timestamp_format of this OBSCommonConfig.
        :rtype: str
        """
        return self._timestamp_format

    @timestamp_format.setter
    def timestamp_format(self, timestamp_format):
        """Sets the timestamp_format of this OBSCommonConfig.

        时间格式

        :param timestamp_format: The timestamp_format of this OBSCommonConfig.
        :type timestamp_format: str
        """
        self._timestamp_format = timestamp_format

    @property
    def null_value(self):
        """Gets the null_value of this OBSCommonConfig.

        为空时默认值

        :return: The null_value of this OBSCommonConfig.
        :rtype: str
        """
        return self._null_value

    @null_value.setter
    def null_value(self, null_value):
        """Sets the null_value of this OBSCommonConfig.

        为空时默认值

        :param null_value: The null_value of this OBSCommonConfig.
        :type null_value: str
        """
        self._null_value = null_value

    @property
    def comment(self):
        """Gets the comment of this OBSCommonConfig.

        注解

        :return: The comment of this OBSCommonConfig.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this OBSCommonConfig.

        注解

        :param comment: The comment of this OBSCommonConfig.
        :type comment: str
        """
        self._comment = comment

    @property
    def parse_mode(self):
        """Gets the parse_mode of this OBSCommonConfig.

        解析模式

        :return: The parse_mode of this OBSCommonConfig.
        :rtype: str
        """
        return self._parse_mode

    @parse_mode.setter
    def parse_mode(self, parse_mode):
        """Sets the parse_mode of this OBSCommonConfig.

        解析模式

        :param parse_mode: The parse_mode of this OBSCommonConfig.
        :type parse_mode: str
        """
        self._parse_mode = parse_mode

    @property
    def join_table(self):
        """Gets the join_table of this OBSCommonConfig.

        联表

        :return: The join_table of this OBSCommonConfig.
        :rtype: str
        """
        return self._join_table

    @join_table.setter
    def join_table(self, join_table):
        """Sets the join_table of this OBSCommonConfig.

        联表

        :param join_table: The join_table of this OBSCommonConfig.
        :type join_table: str
        """
        self._join_table = join_table

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
        if not isinstance(other, OBSCommonConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
