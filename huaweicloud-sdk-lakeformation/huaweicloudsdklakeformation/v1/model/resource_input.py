# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'catalog': 'str',
        'database': 'str',
        'function': 'str',
        'table': 'str',
        'column': 'str',
        'uri': 'str',
        'columns': 'list[str]'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'catalog': 'catalog',
        'database': 'database',
        'function': 'function',
        'table': 'table',
        'column': 'column',
        'uri': 'uri',
        'columns': 'columns'
    }

    def __init__(self, resource_type=None, catalog=None, database=None, function=None, table=None, column=None, uri=None, columns=None):
        """ResourceInput

        The model defined in huaweicloud sdk

        :param resource_type: 元数据资源类型,CATALOG,DATABASE,TABLE,FUNC,MODEL,COLUMN,URI
        :type resource_type: str
        :param catalog: catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。
        :type catalog: str
        :param database: 数据库名称。只能包含中文、字母、数字和下划线，且长度为1到128个字符。
        :type database: str
        :param function: 函数名称。只能包含字母、数字和下划线，且长度为1~256个字符。
        :type function: str
        :param table: 表名称。只能包含中文、字母、数字和下划线，且长度为1~256个字符。
        :type table: str
        :param column: 列名称。只能包含中文、字母、数字和_-+*\\(), 特殊字符，且长度为1~767个字符。
        :type column: str
        :param uri: URI
        :type uri: str
        :param columns: 列名称列表
        :type columns: list[str]
        """
        
        

        self._resource_type = None
        self._catalog = None
        self._database = None
        self._function = None
        self._table = None
        self._column = None
        self._uri = None
        self._columns = None
        self.discriminator = None

        self.resource_type = resource_type
        if catalog is not None:
            self.catalog = catalog
        if database is not None:
            self.database = database
        if function is not None:
            self.function = function
        if table is not None:
            self.table = table
        if column is not None:
            self.column = column
        if uri is not None:
            self.uri = uri
        if columns is not None:
            self.columns = columns

    @property
    def resource_type(self):
        """Gets the resource_type of this ResourceInput.

        元数据资源类型,CATALOG,DATABASE,TABLE,FUNC,MODEL,COLUMN,URI

        :return: The resource_type of this ResourceInput.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ResourceInput.

        元数据资源类型,CATALOG,DATABASE,TABLE,FUNC,MODEL,COLUMN,URI

        :param resource_type: The resource_type of this ResourceInput.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def catalog(self):
        """Gets the catalog of this ResourceInput.

        catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :return: The catalog of this ResourceInput.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this ResourceInput.

        catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :param catalog: The catalog of this ResourceInput.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def database(self):
        """Gets the database of this ResourceInput.

        数据库名称。只能包含中文、字母、数字和下划线，且长度为1到128个字符。

        :return: The database of this ResourceInput.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ResourceInput.

        数据库名称。只能包含中文、字母、数字和下划线，且长度为1到128个字符。

        :param database: The database of this ResourceInput.
        :type database: str
        """
        self._database = database

    @property
    def function(self):
        """Gets the function of this ResourceInput.

        函数名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :return: The function of this ResourceInput.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this ResourceInput.

        函数名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :param function: The function of this ResourceInput.
        :type function: str
        """
        self._function = function

    @property
    def table(self):
        """Gets the table of this ResourceInput.

        表名称。只能包含中文、字母、数字和下划线，且长度为1~256个字符。

        :return: The table of this ResourceInput.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this ResourceInput.

        表名称。只能包含中文、字母、数字和下划线，且长度为1~256个字符。

        :param table: The table of this ResourceInput.
        :type table: str
        """
        self._table = table

    @property
    def column(self):
        """Gets the column of this ResourceInput.

        列名称。只能包含中文、字母、数字和_-+*\\(), 特殊字符，且长度为1~767个字符。

        :return: The column of this ResourceInput.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this ResourceInput.

        列名称。只能包含中文、字母、数字和_-+*\\(), 特殊字符，且长度为1~767个字符。

        :param column: The column of this ResourceInput.
        :type column: str
        """
        self._column = column

    @property
    def uri(self):
        """Gets the uri of this ResourceInput.

        URI

        :return: The uri of this ResourceInput.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ResourceInput.

        URI

        :param uri: The uri of this ResourceInput.
        :type uri: str
        """
        self._uri = uri

    @property
    def columns(self):
        """Gets the columns of this ResourceInput.

        列名称列表

        :return: The columns of this ResourceInput.
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this ResourceInput.

        列名称列表

        :param columns: The columns of this ResourceInput.
        :type columns: list[str]
        """
        self._columns = columns

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
        if not isinstance(other, ResourceInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
