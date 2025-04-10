# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportTableSpaceInfo:

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
        'table': 'str',
        'db_engine': 'str',
        'table_size': 'int',
        'data_size': 'int',
        'index_size': 'int',
        'rows': 'int'
    }

    attribute_map = {
        'database': 'database',
        'table': 'table',
        'db_engine': 'db_engine',
        'table_size': 'table_size',
        'data_size': 'data_size',
        'index_size': 'index_size',
        'rows': 'rows'
    }

    def __init__(self, database=None, table=None, db_engine=None, table_size=None, data_size=None, index_size=None, rows=None):
        r"""HealthReportTableSpaceInfo

        The model defined in huaweicloud sdk

        :param database: 数据库名。
        :type database: str
        :param table: 表名。
        :type table: str
        :param db_engine: 数据库引擎。
        :type db_engine: str
        :param table_size: 表大小。
        :type table_size: int
        :param data_size: 数据大小。
        :type data_size: int
        :param index_size: 索引大小。
        :type index_size: int
        :param rows: 行数量。
        :type rows: int
        """
        
        

        self._database = None
        self._table = None
        self._db_engine = None
        self._table_size = None
        self._data_size = None
        self._index_size = None
        self._rows = None
        self.discriminator = None

        self.database = database
        self.table = table
        self.db_engine = db_engine
        self.table_size = table_size
        self.data_size = data_size
        self.index_size = index_size
        self.rows = rows

    @property
    def database(self):
        r"""Gets the database of this HealthReportTableSpaceInfo.

        数据库名。

        :return: The database of this HealthReportTableSpaceInfo.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this HealthReportTableSpaceInfo.

        数据库名。

        :param database: The database of this HealthReportTableSpaceInfo.
        :type database: str
        """
        self._database = database

    @property
    def table(self):
        r"""Gets the table of this HealthReportTableSpaceInfo.

        表名。

        :return: The table of this HealthReportTableSpaceInfo.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this HealthReportTableSpaceInfo.

        表名。

        :param table: The table of this HealthReportTableSpaceInfo.
        :type table: str
        """
        self._table = table

    @property
    def db_engine(self):
        r"""Gets the db_engine of this HealthReportTableSpaceInfo.

        数据库引擎。

        :return: The db_engine of this HealthReportTableSpaceInfo.
        :rtype: str
        """
        return self._db_engine

    @db_engine.setter
    def db_engine(self, db_engine):
        r"""Sets the db_engine of this HealthReportTableSpaceInfo.

        数据库引擎。

        :param db_engine: The db_engine of this HealthReportTableSpaceInfo.
        :type db_engine: str
        """
        self._db_engine = db_engine

    @property
    def table_size(self):
        r"""Gets the table_size of this HealthReportTableSpaceInfo.

        表大小。

        :return: The table_size of this HealthReportTableSpaceInfo.
        :rtype: int
        """
        return self._table_size

    @table_size.setter
    def table_size(self, table_size):
        r"""Sets the table_size of this HealthReportTableSpaceInfo.

        表大小。

        :param table_size: The table_size of this HealthReportTableSpaceInfo.
        :type table_size: int
        """
        self._table_size = table_size

    @property
    def data_size(self):
        r"""Gets the data_size of this HealthReportTableSpaceInfo.

        数据大小。

        :return: The data_size of this HealthReportTableSpaceInfo.
        :rtype: int
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        r"""Sets the data_size of this HealthReportTableSpaceInfo.

        数据大小。

        :param data_size: The data_size of this HealthReportTableSpaceInfo.
        :type data_size: int
        """
        self._data_size = data_size

    @property
    def index_size(self):
        r"""Gets the index_size of this HealthReportTableSpaceInfo.

        索引大小。

        :return: The index_size of this HealthReportTableSpaceInfo.
        :rtype: int
        """
        return self._index_size

    @index_size.setter
    def index_size(self, index_size):
        r"""Sets the index_size of this HealthReportTableSpaceInfo.

        索引大小。

        :param index_size: The index_size of this HealthReportTableSpaceInfo.
        :type index_size: int
        """
        self._index_size = index_size

    @property
    def rows(self):
        r"""Gets the rows of this HealthReportTableSpaceInfo.

        行数量。

        :return: The rows of this HealthReportTableSpaceInfo.
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this HealthReportTableSpaceInfo.

        行数量。

        :param rows: The rows of this HealthReportTableSpaceInfo.
        :type rows: int
        """
        self._rows = rows

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
        if not isinstance(other, HealthReportTableSpaceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
