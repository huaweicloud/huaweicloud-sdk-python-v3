# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventRowsVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'int',
        'file_name': 'str',
        'position': 'int',
        'timestamp': 'int',
        'db_name': 'str',
        'table_name': 'str',
        'sql_type': 'str',
        'sql_statement': 'str',
        'column_names': 'list[str]',
        'primary_keys': 'list[str]',
        'affect_rows': 'int',
        'row_pairs': 'list[RowPairDto]'
    }

    attribute_map = {
        'event_id': 'event_id',
        'file_name': 'file_name',
        'position': 'position',
        'timestamp': 'timestamp',
        'db_name': 'db_name',
        'table_name': 'table_name',
        'sql_type': 'sql_type',
        'sql_statement': 'sql_statement',
        'column_names': 'column_names',
        'primary_keys': 'primary_keys',
        'affect_rows': 'affect_rows',
        'row_pairs': 'row_pairs'
    }

    def __init__(self, event_id=None, file_name=None, position=None, timestamp=None, db_name=None, table_name=None, sql_type=None, sql_statement=None, column_names=None, primary_keys=None, affect_rows=None, row_pairs=None):
        r"""EventRowsVo

        The model defined in huaweicloud sdk

        :param event_id: 事件ID
        :type event_id: int
        :param file_name: 文件名称
        :type file_name: str
        :param position: 解析位置
        :type position: int
        :param timestamp: 事件发生时间，单位毫秒
        :type timestamp: int
        :param db_name: 变更的数据库名称
        :type db_name: str
        :param table_name: 变更的表名称
        :type table_name: str
        :param sql_type: 变更的SQL类型。取值范围：insert、update、delete、ddl
        :type sql_type: str
        :param sql_statement: 变更的SQL语句
        :type sql_statement: str
        :param column_names: 变更的列名称列表
        :type column_names: list[str]
        :param primary_keys: 变更的主键列表
        :type primary_keys: list[str]
        :param affect_rows: 变更影响的行数
        :type affect_rows: int
        :param row_pairs: 变更数据详情
        :type row_pairs: list[:class:`huaweicloudsdkdas.v3.RowPairDto`]
        """
        
        

        self._event_id = None
        self._file_name = None
        self._position = None
        self._timestamp = None
        self._db_name = None
        self._table_name = None
        self._sql_type = None
        self._sql_statement = None
        self._column_names = None
        self._primary_keys = None
        self._affect_rows = None
        self._row_pairs = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if file_name is not None:
            self.file_name = file_name
        if position is not None:
            self.position = position
        if timestamp is not None:
            self.timestamp = timestamp
        if db_name is not None:
            self.db_name = db_name
        if table_name is not None:
            self.table_name = table_name
        if sql_type is not None:
            self.sql_type = sql_type
        if sql_statement is not None:
            self.sql_statement = sql_statement
        if column_names is not None:
            self.column_names = column_names
        if primary_keys is not None:
            self.primary_keys = primary_keys
        if affect_rows is not None:
            self.affect_rows = affect_rows
        if row_pairs is not None:
            self.row_pairs = row_pairs

    @property
    def event_id(self):
        r"""Gets the event_id of this EventRowsVo.

        事件ID

        :return: The event_id of this EventRowsVo.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this EventRowsVo.

        事件ID

        :param event_id: The event_id of this EventRowsVo.
        :type event_id: int
        """
        self._event_id = event_id

    @property
    def file_name(self):
        r"""Gets the file_name of this EventRowsVo.

        文件名称

        :return: The file_name of this EventRowsVo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this EventRowsVo.

        文件名称

        :param file_name: The file_name of this EventRowsVo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def position(self):
        r"""Gets the position of this EventRowsVo.

        解析位置

        :return: The position of this EventRowsVo.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this EventRowsVo.

        解析位置

        :param position: The position of this EventRowsVo.
        :type position: int
        """
        self._position = position

    @property
    def timestamp(self):
        r"""Gets the timestamp of this EventRowsVo.

        事件发生时间，单位毫秒

        :return: The timestamp of this EventRowsVo.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this EventRowsVo.

        事件发生时间，单位毫秒

        :param timestamp: The timestamp of this EventRowsVo.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def db_name(self):
        r"""Gets the db_name of this EventRowsVo.

        变更的数据库名称

        :return: The db_name of this EventRowsVo.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this EventRowsVo.

        变更的数据库名称

        :param db_name: The db_name of this EventRowsVo.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this EventRowsVo.

        变更的表名称

        :return: The table_name of this EventRowsVo.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this EventRowsVo.

        变更的表名称

        :param table_name: The table_name of this EventRowsVo.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def sql_type(self):
        r"""Gets the sql_type of this EventRowsVo.

        变更的SQL类型。取值范围：insert、update、delete、ddl

        :return: The sql_type of this EventRowsVo.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        r"""Sets the sql_type of this EventRowsVo.

        变更的SQL类型。取值范围：insert、update、delete、ddl

        :param sql_type: The sql_type of this EventRowsVo.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def sql_statement(self):
        r"""Gets the sql_statement of this EventRowsVo.

        变更的SQL语句

        :return: The sql_statement of this EventRowsVo.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        r"""Sets the sql_statement of this EventRowsVo.

        变更的SQL语句

        :param sql_statement: The sql_statement of this EventRowsVo.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

    @property
    def column_names(self):
        r"""Gets the column_names of this EventRowsVo.

        变更的列名称列表

        :return: The column_names of this EventRowsVo.
        :rtype: list[str]
        """
        return self._column_names

    @column_names.setter
    def column_names(self, column_names):
        r"""Sets the column_names of this EventRowsVo.

        变更的列名称列表

        :param column_names: The column_names of this EventRowsVo.
        :type column_names: list[str]
        """
        self._column_names = column_names

    @property
    def primary_keys(self):
        r"""Gets the primary_keys of this EventRowsVo.

        变更的主键列表

        :return: The primary_keys of this EventRowsVo.
        :rtype: list[str]
        """
        return self._primary_keys

    @primary_keys.setter
    def primary_keys(self, primary_keys):
        r"""Sets the primary_keys of this EventRowsVo.

        变更的主键列表

        :param primary_keys: The primary_keys of this EventRowsVo.
        :type primary_keys: list[str]
        """
        self._primary_keys = primary_keys

    @property
    def affect_rows(self):
        r"""Gets the affect_rows of this EventRowsVo.

        变更影响的行数

        :return: The affect_rows of this EventRowsVo.
        :rtype: int
        """
        return self._affect_rows

    @affect_rows.setter
    def affect_rows(self, affect_rows):
        r"""Sets the affect_rows of this EventRowsVo.

        变更影响的行数

        :param affect_rows: The affect_rows of this EventRowsVo.
        :type affect_rows: int
        """
        self._affect_rows = affect_rows

    @property
    def row_pairs(self):
        r"""Gets the row_pairs of this EventRowsVo.

        变更数据详情

        :return: The row_pairs of this EventRowsVo.
        :rtype: list[:class:`huaweicloudsdkdas.v3.RowPairDto`]
        """
        return self._row_pairs

    @row_pairs.setter
    def row_pairs(self, row_pairs):
        r"""Sets the row_pairs of this EventRowsVo.

        变更数据详情

        :param row_pairs: The row_pairs of this EventRowsVo.
        :type row_pairs: list[:class:`huaweicloudsdkdas.v3.RowPairDto`]
        """
        self._row_pairs = row_pairs

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EventRowsVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
