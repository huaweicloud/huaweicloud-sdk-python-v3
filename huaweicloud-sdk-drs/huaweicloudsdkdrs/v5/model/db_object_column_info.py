# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbObjectColumnInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'column_infos': 'list[QueryColumnInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'column_infos': 'column_infos',
        'total_count': 'total_count'
    }

    def __init__(self, db_name=None, schema_name=None, table_name=None, column_infos=None, total_count=None):
        """DbObjectColumnInfo

        The model defined in huaweicloud sdk

        :param db_name: 数据库库名称。
        :type db_name: str
        :param schema_name: 数据库schema名称。
        :type schema_name: str
        :param table_name: 数据库表名称。
        :type table_name: str
        :param column_infos: 数据库列信息。
        :type column_infos: list[:class:`huaweicloudsdkdrs.v5.QueryColumnInfo`]
        :param total_count: 数据库列信息总数，与分页无关，仅作为返回体参数
        :type total_count: int
        """
        
        

        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self._column_infos = None
        self._total_count = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if column_infos is not None:
            self.column_infos = column_infos
        if total_count is not None:
            self.total_count = total_count

    @property
    def db_name(self):
        """Gets the db_name of this DbObjectColumnInfo.

        数据库库名称。

        :return: The db_name of this DbObjectColumnInfo.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this DbObjectColumnInfo.

        数据库库名称。

        :param db_name: The db_name of this DbObjectColumnInfo.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        """Gets the schema_name of this DbObjectColumnInfo.

        数据库schema名称。

        :return: The schema_name of this DbObjectColumnInfo.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this DbObjectColumnInfo.

        数据库schema名称。

        :param schema_name: The schema_name of this DbObjectColumnInfo.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this DbObjectColumnInfo.

        数据库表名称。

        :return: The table_name of this DbObjectColumnInfo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this DbObjectColumnInfo.

        数据库表名称。

        :param table_name: The table_name of this DbObjectColumnInfo.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def column_infos(self):
        """Gets the column_infos of this DbObjectColumnInfo.

        数据库列信息。

        :return: The column_infos of this DbObjectColumnInfo.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.QueryColumnInfo`]
        """
        return self._column_infos

    @column_infos.setter
    def column_infos(self, column_infos):
        """Sets the column_infos of this DbObjectColumnInfo.

        数据库列信息。

        :param column_infos: The column_infos of this DbObjectColumnInfo.
        :type column_infos: list[:class:`huaweicloudsdkdrs.v5.QueryColumnInfo`]
        """
        self._column_infos = column_infos

    @property
    def total_count(self):
        """Gets the total_count of this DbObjectColumnInfo.

        数据库列信息总数，与分页无关，仅作为返回体参数

        :return: The total_count of this DbObjectColumnInfo.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this DbObjectColumnInfo.

        数据库列信息总数，与分页无关，仅作为返回体参数

        :param total_count: The total_count of this DbObjectColumnInfo.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, DbObjectColumnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
