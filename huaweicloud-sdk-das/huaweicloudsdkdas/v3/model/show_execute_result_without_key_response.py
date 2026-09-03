# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExecuteResultWithoutKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'column_values': 'list[object]',
        'metadata': 'list[Column]',
        'result_type': 'str',
        'rows': 'int',
        'time_delay': 'int',
        'can_edit': 'bool',
        'can_export': 'bool',
        'edit_db_name': 'str',
        'edit_table': 'str',
        'edit_primary_keys': 'list[str]',
        'cannot_edit_reason': 'int',
        'extend_datas': 'list[object]',
        'data_sum': 'int',
        'big_table': 'bool',
        'warning': 'list[str]',
        'sql': 'str',
        'explain_sql': 'bool',
        'page_state': 'str',
        'exceed_data': 'bool',
        'execute_status': 'str'
    }

    attribute_map = {
        'column_values': 'column_values',
        'metadata': 'metadata',
        'result_type': 'result_type',
        'rows': 'rows',
        'time_delay': 'time_delay',
        'can_edit': 'can_edit',
        'can_export': 'can_export',
        'edit_db_name': 'edit_db_name',
        'edit_table': 'edit_table',
        'edit_primary_keys': 'edit_primary_keys',
        'cannot_edit_reason': 'cannot_edit_reason',
        'extend_datas': 'extend_datas',
        'data_sum': 'data_sum',
        'big_table': 'big_table',
        'warning': 'warning',
        'sql': 'sql',
        'explain_sql': 'explain_sql',
        'page_state': 'page_state',
        'exceed_data': 'exceed_data',
        'execute_status': 'execute_status'
    }

    def __init__(self, column_values=None, metadata=None, result_type=None, rows=None, time_delay=None, can_edit=None, can_export=None, edit_db_name=None, edit_table=None, edit_primary_keys=None, cannot_edit_reason=None, extend_datas=None, data_sum=None, big_table=None, warning=None, sql=None, explain_sql=None, page_state=None, exceed_data=None, execute_status=None):
        r"""ShowExecuteResultWithoutKeyResponse

        The model defined in huaweicloud sdk

        :param column_values: 字段值
        :type column_values: list[object]
        :param metadata: 字段属性，字段名等
        :type metadata: list[:class:`huaweicloudsdkdas.v3.Column`]
        :param result_type: 结果集类型
        :type result_type: str
        :param rows: 行数
        :type rows: int
        :param time_delay: 执行耗时
        :type time_delay: int
        :param can_edit: 结果集是否可编辑
        :type can_edit: bool
        :param can_export: 结果集是否可导出
        :type can_export: bool
        :param edit_db_name: 编辑库名
        :type edit_db_name: str
        :param edit_table: 编辑表名
        :type edit_table: str
        :param edit_primary_keys: 主键信息
        :type edit_primary_keys: list[str]
        :param cannot_edit_reason: 不能编辑的原因
        :type cannot_edit_reason: int
        :param extend_datas: 额外信息
        :type extend_datas: list[object]
        :param data_sum: 数据总量
        :type data_sum: int
        :param big_table: 是否为大表
        :type big_table: bool
        :param warning: 执行命令告警信息
        :type warning: list[str]
        :param sql: 要执行的SQL语句
        :type sql: str
        :param explain_sql: 是否为执行计划语句
        :type explain_sql: bool
        :param page_state: 页面状态
        :type page_state: str
        :param exceed_data: 查询结果是否超过规定大小
        :type exceed_data: bool
        :param execute_status: 执行状态（finished：执行完毕，pending：执行中）
        :type execute_status: str
        """
        
        super().__init__()

        self._column_values = None
        self._metadata = None
        self._result_type = None
        self._rows = None
        self._time_delay = None
        self._can_edit = None
        self._can_export = None
        self._edit_db_name = None
        self._edit_table = None
        self._edit_primary_keys = None
        self._cannot_edit_reason = None
        self._extend_datas = None
        self._data_sum = None
        self._big_table = None
        self._warning = None
        self._sql = None
        self._explain_sql = None
        self._page_state = None
        self._exceed_data = None
        self._execute_status = None
        self.discriminator = None

        if column_values is not None:
            self.column_values = column_values
        if metadata is not None:
            self.metadata = metadata
        if result_type is not None:
            self.result_type = result_type
        if rows is not None:
            self.rows = rows
        if time_delay is not None:
            self.time_delay = time_delay
        if can_edit is not None:
            self.can_edit = can_edit
        if can_export is not None:
            self.can_export = can_export
        if edit_db_name is not None:
            self.edit_db_name = edit_db_name
        if edit_table is not None:
            self.edit_table = edit_table
        if edit_primary_keys is not None:
            self.edit_primary_keys = edit_primary_keys
        if cannot_edit_reason is not None:
            self.cannot_edit_reason = cannot_edit_reason
        if extend_datas is not None:
            self.extend_datas = extend_datas
        if data_sum is not None:
            self.data_sum = data_sum
        if big_table is not None:
            self.big_table = big_table
        if warning is not None:
            self.warning = warning
        if sql is not None:
            self.sql = sql
        if explain_sql is not None:
            self.explain_sql = explain_sql
        if page_state is not None:
            self.page_state = page_state
        if exceed_data is not None:
            self.exceed_data = exceed_data
        if execute_status is not None:
            self.execute_status = execute_status

    @property
    def column_values(self):
        r"""Gets the column_values of this ShowExecuteResultWithoutKeyResponse.

        字段值

        :return: The column_values of this ShowExecuteResultWithoutKeyResponse.
        :rtype: list[object]
        """
        return self._column_values

    @column_values.setter
    def column_values(self, column_values):
        r"""Sets the column_values of this ShowExecuteResultWithoutKeyResponse.

        字段值

        :param column_values: The column_values of this ShowExecuteResultWithoutKeyResponse.
        :type column_values: list[object]
        """
        self._column_values = column_values

    @property
    def metadata(self):
        r"""Gets the metadata of this ShowExecuteResultWithoutKeyResponse.

        字段属性，字段名等

        :return: The metadata of this ShowExecuteResultWithoutKeyResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.Column`]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ShowExecuteResultWithoutKeyResponse.

        字段属性，字段名等

        :param metadata: The metadata of this ShowExecuteResultWithoutKeyResponse.
        :type metadata: list[:class:`huaweicloudsdkdas.v3.Column`]
        """
        self._metadata = metadata

    @property
    def result_type(self):
        r"""Gets the result_type of this ShowExecuteResultWithoutKeyResponse.

        结果集类型

        :return: The result_type of this ShowExecuteResultWithoutKeyResponse.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        r"""Sets the result_type of this ShowExecuteResultWithoutKeyResponse.

        结果集类型

        :param result_type: The result_type of this ShowExecuteResultWithoutKeyResponse.
        :type result_type: str
        """
        self._result_type = result_type

    @property
    def rows(self):
        r"""Gets the rows of this ShowExecuteResultWithoutKeyResponse.

        行数

        :return: The rows of this ShowExecuteResultWithoutKeyResponse.
        :rtype: int
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        r"""Sets the rows of this ShowExecuteResultWithoutKeyResponse.

        行数

        :param rows: The rows of this ShowExecuteResultWithoutKeyResponse.
        :type rows: int
        """
        self._rows = rows

    @property
    def time_delay(self):
        r"""Gets the time_delay of this ShowExecuteResultWithoutKeyResponse.

        执行耗时

        :return: The time_delay of this ShowExecuteResultWithoutKeyResponse.
        :rtype: int
        """
        return self._time_delay

    @time_delay.setter
    def time_delay(self, time_delay):
        r"""Sets the time_delay of this ShowExecuteResultWithoutKeyResponse.

        执行耗时

        :param time_delay: The time_delay of this ShowExecuteResultWithoutKeyResponse.
        :type time_delay: int
        """
        self._time_delay = time_delay

    @property
    def can_edit(self):
        r"""Gets the can_edit of this ShowExecuteResultWithoutKeyResponse.

        结果集是否可编辑

        :return: The can_edit of this ShowExecuteResultWithoutKeyResponse.
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        r"""Sets the can_edit of this ShowExecuteResultWithoutKeyResponse.

        结果集是否可编辑

        :param can_edit: The can_edit of this ShowExecuteResultWithoutKeyResponse.
        :type can_edit: bool
        """
        self._can_edit = can_edit

    @property
    def can_export(self):
        r"""Gets the can_export of this ShowExecuteResultWithoutKeyResponse.

        结果集是否可导出

        :return: The can_export of this ShowExecuteResultWithoutKeyResponse.
        :rtype: bool
        """
        return self._can_export

    @can_export.setter
    def can_export(self, can_export):
        r"""Sets the can_export of this ShowExecuteResultWithoutKeyResponse.

        结果集是否可导出

        :param can_export: The can_export of this ShowExecuteResultWithoutKeyResponse.
        :type can_export: bool
        """
        self._can_export = can_export

    @property
    def edit_db_name(self):
        r"""Gets the edit_db_name of this ShowExecuteResultWithoutKeyResponse.

        编辑库名

        :return: The edit_db_name of this ShowExecuteResultWithoutKeyResponse.
        :rtype: str
        """
        return self._edit_db_name

    @edit_db_name.setter
    def edit_db_name(self, edit_db_name):
        r"""Sets the edit_db_name of this ShowExecuteResultWithoutKeyResponse.

        编辑库名

        :param edit_db_name: The edit_db_name of this ShowExecuteResultWithoutKeyResponse.
        :type edit_db_name: str
        """
        self._edit_db_name = edit_db_name

    @property
    def edit_table(self):
        r"""Gets the edit_table of this ShowExecuteResultWithoutKeyResponse.

        编辑表名

        :return: The edit_table of this ShowExecuteResultWithoutKeyResponse.
        :rtype: str
        """
        return self._edit_table

    @edit_table.setter
    def edit_table(self, edit_table):
        r"""Sets the edit_table of this ShowExecuteResultWithoutKeyResponse.

        编辑表名

        :param edit_table: The edit_table of this ShowExecuteResultWithoutKeyResponse.
        :type edit_table: str
        """
        self._edit_table = edit_table

    @property
    def edit_primary_keys(self):
        r"""Gets the edit_primary_keys of this ShowExecuteResultWithoutKeyResponse.

        主键信息

        :return: The edit_primary_keys of this ShowExecuteResultWithoutKeyResponse.
        :rtype: list[str]
        """
        return self._edit_primary_keys

    @edit_primary_keys.setter
    def edit_primary_keys(self, edit_primary_keys):
        r"""Sets the edit_primary_keys of this ShowExecuteResultWithoutKeyResponse.

        主键信息

        :param edit_primary_keys: The edit_primary_keys of this ShowExecuteResultWithoutKeyResponse.
        :type edit_primary_keys: list[str]
        """
        self._edit_primary_keys = edit_primary_keys

    @property
    def cannot_edit_reason(self):
        r"""Gets the cannot_edit_reason of this ShowExecuteResultWithoutKeyResponse.

        不能编辑的原因

        :return: The cannot_edit_reason of this ShowExecuteResultWithoutKeyResponse.
        :rtype: int
        """
        return self._cannot_edit_reason

    @cannot_edit_reason.setter
    def cannot_edit_reason(self, cannot_edit_reason):
        r"""Sets the cannot_edit_reason of this ShowExecuteResultWithoutKeyResponse.

        不能编辑的原因

        :param cannot_edit_reason: The cannot_edit_reason of this ShowExecuteResultWithoutKeyResponse.
        :type cannot_edit_reason: int
        """
        self._cannot_edit_reason = cannot_edit_reason

    @property
    def extend_datas(self):
        r"""Gets the extend_datas of this ShowExecuteResultWithoutKeyResponse.

        额外信息

        :return: The extend_datas of this ShowExecuteResultWithoutKeyResponse.
        :rtype: list[object]
        """
        return self._extend_datas

    @extend_datas.setter
    def extend_datas(self, extend_datas):
        r"""Sets the extend_datas of this ShowExecuteResultWithoutKeyResponse.

        额外信息

        :param extend_datas: The extend_datas of this ShowExecuteResultWithoutKeyResponse.
        :type extend_datas: list[object]
        """
        self._extend_datas = extend_datas

    @property
    def data_sum(self):
        r"""Gets the data_sum of this ShowExecuteResultWithoutKeyResponse.

        数据总量

        :return: The data_sum of this ShowExecuteResultWithoutKeyResponse.
        :rtype: int
        """
        return self._data_sum

    @data_sum.setter
    def data_sum(self, data_sum):
        r"""Sets the data_sum of this ShowExecuteResultWithoutKeyResponse.

        数据总量

        :param data_sum: The data_sum of this ShowExecuteResultWithoutKeyResponse.
        :type data_sum: int
        """
        self._data_sum = data_sum

    @property
    def big_table(self):
        r"""Gets the big_table of this ShowExecuteResultWithoutKeyResponse.

        是否为大表

        :return: The big_table of this ShowExecuteResultWithoutKeyResponse.
        :rtype: bool
        """
        return self._big_table

    @big_table.setter
    def big_table(self, big_table):
        r"""Sets the big_table of this ShowExecuteResultWithoutKeyResponse.

        是否为大表

        :param big_table: The big_table of this ShowExecuteResultWithoutKeyResponse.
        :type big_table: bool
        """
        self._big_table = big_table

    @property
    def warning(self):
        r"""Gets the warning of this ShowExecuteResultWithoutKeyResponse.

        执行命令告警信息

        :return: The warning of this ShowExecuteResultWithoutKeyResponse.
        :rtype: list[str]
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        r"""Sets the warning of this ShowExecuteResultWithoutKeyResponse.

        执行命令告警信息

        :param warning: The warning of this ShowExecuteResultWithoutKeyResponse.
        :type warning: list[str]
        """
        self._warning = warning

    @property
    def sql(self):
        r"""Gets the sql of this ShowExecuteResultWithoutKeyResponse.

        要执行的SQL语句

        :return: The sql of this ShowExecuteResultWithoutKeyResponse.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        r"""Sets the sql of this ShowExecuteResultWithoutKeyResponse.

        要执行的SQL语句

        :param sql: The sql of this ShowExecuteResultWithoutKeyResponse.
        :type sql: str
        """
        self._sql = sql

    @property
    def explain_sql(self):
        r"""Gets the explain_sql of this ShowExecuteResultWithoutKeyResponse.

        是否为执行计划语句

        :return: The explain_sql of this ShowExecuteResultWithoutKeyResponse.
        :rtype: bool
        """
        return self._explain_sql

    @explain_sql.setter
    def explain_sql(self, explain_sql):
        r"""Sets the explain_sql of this ShowExecuteResultWithoutKeyResponse.

        是否为执行计划语句

        :param explain_sql: The explain_sql of this ShowExecuteResultWithoutKeyResponse.
        :type explain_sql: bool
        """
        self._explain_sql = explain_sql

    @property
    def page_state(self):
        r"""Gets the page_state of this ShowExecuteResultWithoutKeyResponse.

        页面状态

        :return: The page_state of this ShowExecuteResultWithoutKeyResponse.
        :rtype: str
        """
        return self._page_state

    @page_state.setter
    def page_state(self, page_state):
        r"""Sets the page_state of this ShowExecuteResultWithoutKeyResponse.

        页面状态

        :param page_state: The page_state of this ShowExecuteResultWithoutKeyResponse.
        :type page_state: str
        """
        self._page_state = page_state

    @property
    def exceed_data(self):
        r"""Gets the exceed_data of this ShowExecuteResultWithoutKeyResponse.

        查询结果是否超过规定大小

        :return: The exceed_data of this ShowExecuteResultWithoutKeyResponse.
        :rtype: bool
        """
        return self._exceed_data

    @exceed_data.setter
    def exceed_data(self, exceed_data):
        r"""Sets the exceed_data of this ShowExecuteResultWithoutKeyResponse.

        查询结果是否超过规定大小

        :param exceed_data: The exceed_data of this ShowExecuteResultWithoutKeyResponse.
        :type exceed_data: bool
        """
        self._exceed_data = exceed_data

    @property
    def execute_status(self):
        r"""Gets the execute_status of this ShowExecuteResultWithoutKeyResponse.

        执行状态（finished：执行完毕，pending：执行中）

        :return: The execute_status of this ShowExecuteResultWithoutKeyResponse.
        :rtype: str
        """
        return self._execute_status

    @execute_status.setter
    def execute_status(self, execute_status):
        r"""Sets the execute_status of this ShowExecuteResultWithoutKeyResponse.

        执行状态（finished：执行完毕，pending：执行中）

        :param execute_status: The execute_status of this ShowExecuteResultWithoutKeyResponse.
        :type execute_status: str
        """
        self._execute_status = execute_status

    def to_dict(self):
        import warnings
        warnings.warn("ShowExecuteResultWithoutKeyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowExecuteResultWithoutKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
