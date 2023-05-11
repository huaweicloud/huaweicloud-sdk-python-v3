# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReadWriteRatioList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema': 'str',
        'table': 'str',
        'read_count': 'str',
        'write_count': 'str',
        'relation_tables': 'str',
        'last_updated': 'str'
    }

    attribute_map = {
        'schema': 'schema',
        'table': 'table',
        'read_count': 'readCount',
        'write_count': 'writeCount',
        'relation_tables': 'relationTables',
        'last_updated': 'lastUpdated'
    }

    def __init__(self, schema=None, table=None, read_count=None, write_count=None, relation_tables=None, last_updated=None):
        """ReadWriteRatioList

        The model defined in huaweicloud sdk

        :param schema: 逻辑库名称。
        :type schema: str
        :param table: 逻辑表名称。
        :type table: str
        :param read_count: 读次数。
        :type read_count: str
        :param write_count: 写次数。
        :type write_count: str
        :param relation_tables: 关联表。
        :type relation_tables: str
        :param last_updated: 最后执行时间。
        :type last_updated: str
        """
        
        

        self._schema = None
        self._table = None
        self._read_count = None
        self._write_count = None
        self._relation_tables = None
        self._last_updated = None
        self.discriminator = None

        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table
        if read_count is not None:
            self.read_count = read_count
        if write_count is not None:
            self.write_count = write_count
        if relation_tables is not None:
            self.relation_tables = relation_tables
        if last_updated is not None:
            self.last_updated = last_updated

    @property
    def schema(self):
        """Gets the schema of this ReadWriteRatioList.

        逻辑库名称。

        :return: The schema of this ReadWriteRatioList.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ReadWriteRatioList.

        逻辑库名称。

        :param schema: The schema of this ReadWriteRatioList.
        :type schema: str
        """
        self._schema = schema

    @property
    def table(self):
        """Gets the table of this ReadWriteRatioList.

        逻辑表名称。

        :return: The table of this ReadWriteRatioList.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this ReadWriteRatioList.

        逻辑表名称。

        :param table: The table of this ReadWriteRatioList.
        :type table: str
        """
        self._table = table

    @property
    def read_count(self):
        """Gets the read_count of this ReadWriteRatioList.

        读次数。

        :return: The read_count of this ReadWriteRatioList.
        :rtype: str
        """
        return self._read_count

    @read_count.setter
    def read_count(self, read_count):
        """Sets the read_count of this ReadWriteRatioList.

        读次数。

        :param read_count: The read_count of this ReadWriteRatioList.
        :type read_count: str
        """
        self._read_count = read_count

    @property
    def write_count(self):
        """Gets the write_count of this ReadWriteRatioList.

        写次数。

        :return: The write_count of this ReadWriteRatioList.
        :rtype: str
        """
        return self._write_count

    @write_count.setter
    def write_count(self, write_count):
        """Sets the write_count of this ReadWriteRatioList.

        写次数。

        :param write_count: The write_count of this ReadWriteRatioList.
        :type write_count: str
        """
        self._write_count = write_count

    @property
    def relation_tables(self):
        """Gets the relation_tables of this ReadWriteRatioList.

        关联表。

        :return: The relation_tables of this ReadWriteRatioList.
        :rtype: str
        """
        return self._relation_tables

    @relation_tables.setter
    def relation_tables(self, relation_tables):
        """Sets the relation_tables of this ReadWriteRatioList.

        关联表。

        :param relation_tables: The relation_tables of this ReadWriteRatioList.
        :type relation_tables: str
        """
        self._relation_tables = relation_tables

    @property
    def last_updated(self):
        """Gets the last_updated of this ReadWriteRatioList.

        最后执行时间。

        :return: The last_updated of this ReadWriteRatioList.
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ReadWriteRatioList.

        最后执行时间。

        :param last_updated: The last_updated of this ReadWriteRatioList.
        :type last_updated: str
        """
        self._last_updated = last_updated

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
        if not isinstance(other, ReadWriteRatioList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
