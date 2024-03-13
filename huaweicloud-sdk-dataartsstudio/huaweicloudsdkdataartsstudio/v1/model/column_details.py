# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ColumnDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database': 'str',
        'schema': 'str',
        'table': 'str',
        'column': 'str'
    }

    attribute_map = {
        'database': 'database',
        'schema': 'schema',
        'table': 'table',
        'column': 'column'
    }

    def __init__(self, database=None, schema=None, table=None, column=None):
        """ColumnDetails

        The model defined in huaweicloud sdk

        :param database: 数据库名称
        :type database: str
        :param schema: 逻辑库名称
        :type schema: str
        :param table: 表名称
        :type table: str
        :param column: 字段名称
        :type column: str
        """
        
        

        self._database = None
        self._schema = None
        self._table = None
        self._column = None
        self.discriminator = None

        if database is not None:
            self.database = database
        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table
        if column is not None:
            self.column = column

    @property
    def database(self):
        """Gets the database of this ColumnDetails.

        数据库名称

        :return: The database of this ColumnDetails.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ColumnDetails.

        数据库名称

        :param database: The database of this ColumnDetails.
        :type database: str
        """
        self._database = database

    @property
    def schema(self):
        """Gets the schema of this ColumnDetails.

        逻辑库名称

        :return: The schema of this ColumnDetails.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ColumnDetails.

        逻辑库名称

        :param schema: The schema of this ColumnDetails.
        :type schema: str
        """
        self._schema = schema

    @property
    def table(self):
        """Gets the table of this ColumnDetails.

        表名称

        :return: The table of this ColumnDetails.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this ColumnDetails.

        表名称

        :param table: The table of this ColumnDetails.
        :type table: str
        """
        self._table = table

    @property
    def column(self):
        """Gets the column of this ColumnDetails.

        字段名称

        :return: The column of this ColumnDetails.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this ColumnDetails.

        字段名称

        :param column: The column of this ColumnDetails.
        :type column: str
        """
        self._column = column

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
        if not isinstance(other, ColumnDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
