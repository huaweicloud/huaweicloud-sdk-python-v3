# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchBinlogParseRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'db_name': 'str',
        'table_name': 'str',
        'type_list': 'list[str]',
        'cur_page': 'int',
        'per_page': 'int',
        'column_list': 'list[FilterColumn]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'db_name': 'db_name',
        'table_name': 'table_name',
        'type_list': 'type_list',
        'cur_page': 'cur_page',
        'per_page': 'per_page',
        'column_list': 'column_list'
    }

    def __init__(self, task_id=None, start_time=None, end_time=None, db_name=None, table_name=None, type_list=None, cur_page=None, per_page=None, column_list=None):
        r"""SearchBinlogParseRequestBody

        The model defined in huaweicloud sdk

        :param task_id: 解析任务ID
        :type task_id: int
        :param start_time: 开始时间（Unix timestamp），单位：毫秒
        :type start_time: int
        :param end_time: 结束时间（Unix timestamp），单位：毫秒
        :type end_time: int
        :param db_name: 数据库名称
        :type db_name: str
        :param table_name: 表名称
        :type table_name: str
        :param type_list: SQL类型列表。取值范围：insert、update、delete、ddl
        :type type_list: list[str]
        :param cur_page: 页码
        :type cur_page: int
        :param per_page: 每页记录数
        :type per_page: int
        :param column_list: 筛选条件列表
        :type column_list: list[:class:`huaweicloudsdkdas.v3.FilterColumn`]
        """
        
        

        self._task_id = None
        self._start_time = None
        self._end_time = None
        self._db_name = None
        self._table_name = None
        self._type_list = None
        self._cur_page = None
        self._per_page = None
        self._column_list = None
        self.discriminator = None

        self.task_id = task_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if db_name is not None:
            self.db_name = db_name
        if table_name is not None:
            self.table_name = table_name
        if type_list is not None:
            self.type_list = type_list
        self.cur_page = cur_page
        self.per_page = per_page
        if column_list is not None:
            self.column_list = column_list

    @property
    def task_id(self):
        r"""Gets the task_id of this SearchBinlogParseRequestBody.

        解析任务ID

        :return: The task_id of this SearchBinlogParseRequestBody.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this SearchBinlogParseRequestBody.

        解析任务ID

        :param task_id: The task_id of this SearchBinlogParseRequestBody.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def start_time(self):
        r"""Gets the start_time of this SearchBinlogParseRequestBody.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_time of this SearchBinlogParseRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SearchBinlogParseRequestBody.

        开始时间（Unix timestamp），单位：毫秒

        :param start_time: The start_time of this SearchBinlogParseRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SearchBinlogParseRequestBody.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_time of this SearchBinlogParseRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SearchBinlogParseRequestBody.

        结束时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this SearchBinlogParseRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def db_name(self):
        r"""Gets the db_name of this SearchBinlogParseRequestBody.

        数据库名称

        :return: The db_name of this SearchBinlogParseRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this SearchBinlogParseRequestBody.

        数据库名称

        :param db_name: The db_name of this SearchBinlogParseRequestBody.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        r"""Gets the table_name of this SearchBinlogParseRequestBody.

        表名称

        :return: The table_name of this SearchBinlogParseRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this SearchBinlogParseRequestBody.

        表名称

        :param table_name: The table_name of this SearchBinlogParseRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def type_list(self):
        r"""Gets the type_list of this SearchBinlogParseRequestBody.

        SQL类型列表。取值范围：insert、update、delete、ddl

        :return: The type_list of this SearchBinlogParseRequestBody.
        :rtype: list[str]
        """
        return self._type_list

    @type_list.setter
    def type_list(self, type_list):
        r"""Sets the type_list of this SearchBinlogParseRequestBody.

        SQL类型列表。取值范围：insert、update、delete、ddl

        :param type_list: The type_list of this SearchBinlogParseRequestBody.
        :type type_list: list[str]
        """
        self._type_list = type_list

    @property
    def cur_page(self):
        r"""Gets the cur_page of this SearchBinlogParseRequestBody.

        页码

        :return: The cur_page of this SearchBinlogParseRequestBody.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this SearchBinlogParseRequestBody.

        页码

        :param cur_page: The cur_page of this SearchBinlogParseRequestBody.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this SearchBinlogParseRequestBody.

        每页记录数

        :return: The per_page of this SearchBinlogParseRequestBody.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this SearchBinlogParseRequestBody.

        每页记录数

        :param per_page: The per_page of this SearchBinlogParseRequestBody.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def column_list(self):
        r"""Gets the column_list of this SearchBinlogParseRequestBody.

        筛选条件列表

        :return: The column_list of this SearchBinlogParseRequestBody.
        :rtype: list[:class:`huaweicloudsdkdas.v3.FilterColumn`]
        """
        return self._column_list

    @column_list.setter
    def column_list(self, column_list):
        r"""Sets the column_list of this SearchBinlogParseRequestBody.

        筛选条件列表

        :param column_list: The column_list of this SearchBinlogParseRequestBody.
        :type column_list: list[:class:`huaweicloudsdkdas.v3.FilterColumn`]
        """
        self._column_list = column_list

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
        if not isinstance(other, SearchBinlogParseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
