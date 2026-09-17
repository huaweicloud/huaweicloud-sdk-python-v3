# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportFilterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_names': 'list[str]',
        'tb_names': 'list[str]',
        'file_names': 'list[str]',
        'start_time': 'int',
        'end_time': 'int',
        'type_list': 'list[str]',
        'column_list': 'list[ExportColumnInfo]',
        'parse_double_insert': 'bool'
    }

    attribute_map = {
        'db_names': 'db_names',
        'tb_names': 'tb_names',
        'file_names': 'file_names',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'type_list': 'type_list',
        'column_list': 'column_list',
        'parse_double_insert': 'parse_double_insert'
    }

    def __init__(self, db_names=None, tb_names=None, file_names=None, start_time=None, end_time=None, type_list=None, column_list=None, parse_double_insert=None):
        r"""ExportFilterInfo

        The model defined in huaweicloud sdk

        :param db_names: 数据库名称列表
        :type db_names: list[str]
        :param tb_names: 表名称列表
        :type tb_names: list[str]
        :param file_names: 文件名称列表
        :type file_names: list[str]
        :param start_time: 开始时间
        :type start_time: int
        :param end_time: 结束时间
        :type end_time: int
        :param type_list: SQL类型列表（insert、update、delete、ddl）
        :type type_list: list[str]
        :param column_list: 列列表
        :type column_list: list[:class:`huaweicloudsdkdas.v3.ExportColumnInfo`]
        :param parse_double_insert: 是否将UPDATE语句导出为两条INSERT语句
        :type parse_double_insert: bool
        """
        
        

        self._db_names = None
        self._tb_names = None
        self._file_names = None
        self._start_time = None
        self._end_time = None
        self._type_list = None
        self._column_list = None
        self._parse_double_insert = None
        self.discriminator = None

        if db_names is not None:
            self.db_names = db_names
        if tb_names is not None:
            self.tb_names = tb_names
        if file_names is not None:
            self.file_names = file_names
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if type_list is not None:
            self.type_list = type_list
        if column_list is not None:
            self.column_list = column_list
        if parse_double_insert is not None:
            self.parse_double_insert = parse_double_insert

    @property
    def db_names(self):
        r"""Gets the db_names of this ExportFilterInfo.

        数据库名称列表

        :return: The db_names of this ExportFilterInfo.
        :rtype: list[str]
        """
        return self._db_names

    @db_names.setter
    def db_names(self, db_names):
        r"""Sets the db_names of this ExportFilterInfo.

        数据库名称列表

        :param db_names: The db_names of this ExportFilterInfo.
        :type db_names: list[str]
        """
        self._db_names = db_names

    @property
    def tb_names(self):
        r"""Gets the tb_names of this ExportFilterInfo.

        表名称列表

        :return: The tb_names of this ExportFilterInfo.
        :rtype: list[str]
        """
        return self._tb_names

    @tb_names.setter
    def tb_names(self, tb_names):
        r"""Sets the tb_names of this ExportFilterInfo.

        表名称列表

        :param tb_names: The tb_names of this ExportFilterInfo.
        :type tb_names: list[str]
        """
        self._tb_names = tb_names

    @property
    def file_names(self):
        r"""Gets the file_names of this ExportFilterInfo.

        文件名称列表

        :return: The file_names of this ExportFilterInfo.
        :rtype: list[str]
        """
        return self._file_names

    @file_names.setter
    def file_names(self, file_names):
        r"""Sets the file_names of this ExportFilterInfo.

        文件名称列表

        :param file_names: The file_names of this ExportFilterInfo.
        :type file_names: list[str]
        """
        self._file_names = file_names

    @property
    def start_time(self):
        r"""Gets the start_time of this ExportFilterInfo.

        开始时间

        :return: The start_time of this ExportFilterInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ExportFilterInfo.

        开始时间

        :param start_time: The start_time of this ExportFilterInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ExportFilterInfo.

        结束时间

        :return: The end_time of this ExportFilterInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ExportFilterInfo.

        结束时间

        :param end_time: The end_time of this ExportFilterInfo.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def type_list(self):
        r"""Gets the type_list of this ExportFilterInfo.

        SQL类型列表（insert、update、delete、ddl）

        :return: The type_list of this ExportFilterInfo.
        :rtype: list[str]
        """
        return self._type_list

    @type_list.setter
    def type_list(self, type_list):
        r"""Sets the type_list of this ExportFilterInfo.

        SQL类型列表（insert、update、delete、ddl）

        :param type_list: The type_list of this ExportFilterInfo.
        :type type_list: list[str]
        """
        self._type_list = type_list

    @property
    def column_list(self):
        r"""Gets the column_list of this ExportFilterInfo.

        列列表

        :return: The column_list of this ExportFilterInfo.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ExportColumnInfo`]
        """
        return self._column_list

    @column_list.setter
    def column_list(self, column_list):
        r"""Sets the column_list of this ExportFilterInfo.

        列列表

        :param column_list: The column_list of this ExportFilterInfo.
        :type column_list: list[:class:`huaweicloudsdkdas.v3.ExportColumnInfo`]
        """
        self._column_list = column_list

    @property
    def parse_double_insert(self):
        r"""Gets the parse_double_insert of this ExportFilterInfo.

        是否将UPDATE语句导出为两条INSERT语句

        :return: The parse_double_insert of this ExportFilterInfo.
        :rtype: bool
        """
        return self._parse_double_insert

    @parse_double_insert.setter
    def parse_double_insert(self, parse_double_insert):
        r"""Sets the parse_double_insert of this ExportFilterInfo.

        是否将UPDATE语句导出为两条INSERT语句

        :param parse_double_insert: The parse_double_insert of this ExportFilterInfo.
        :type parse_double_insert: bool
        """
        self._parse_double_insert = parse_double_insert

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
        if not isinstance(other, ExportFilterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
