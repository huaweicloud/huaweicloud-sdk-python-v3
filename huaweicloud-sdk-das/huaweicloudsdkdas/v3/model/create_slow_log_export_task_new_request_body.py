# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSlowLogExportTaskNewRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int',
        'bucket_name': 'str',
        'file_path': 'str',
        'export_type': 'str',
        'sort_field': 'str',
        'sort_asc': 'bool',
        'client': 'str',
        'user': 'str',
        'killed': 'str',
        'execute_time_min': 'int',
        'execute_time_max': 'int',
        'min_avg_execute_time': 'float',
        'max_avg_execute_time': 'float',
        'rows_max_examined': 'int',
        'rows_min_examined': 'int',
        'fuzzy_sql': 'str',
        'operation': 'str',
        'time_zone': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'bucket_name': 'bucket_name',
        'file_path': 'file_path',
        'export_type': 'export_type',
        'sort_field': 'sort_field',
        'sort_asc': 'sort_asc',
        'client': 'client',
        'user': 'user',
        'killed': 'killed',
        'execute_time_min': 'execute_time_min',
        'execute_time_max': 'execute_time_max',
        'min_avg_execute_time': 'min_avg_execute_time',
        'max_avg_execute_time': 'max_avg_execute_time',
        'rows_max_examined': 'rows_max_examined',
        'rows_min_examined': 'rows_min_examined',
        'fuzzy_sql': 'fuzzy_sql',
        'operation': 'operation',
        'time_zone': 'time_zone'
    }

    def __init__(self, start_time=None, end_time=None, bucket_name=None, file_path=None, export_type=None, sort_field=None, sort_asc=None, client=None, user=None, killed=None, execute_time_min=None, execute_time_max=None, min_avg_execute_time=None, max_avg_execute_time=None, rows_max_examined=None, rows_min_examined=None, fuzzy_sql=None, operation=None, time_zone=None):
        r"""CreateSlowLogExportTaskNewRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间（Unix timestamp），单位：毫秒
        :type start_time: int
        :param end_time: 结束时间（Unix timestamp），单位：毫秒
        :type end_time: int
        :param bucket_name: OBS桶名
        :type bucket_name: str
        :param file_path: 文件目录
        :type file_path: str
        :param export_type: 导出类型
        :type export_type: str
        :param sort_field: 排序字段
        :type sort_field: str
        :param sort_asc: 排序顺序（true：正序，false：逆序）
        :type sort_asc: bool
        :param client: 客户端
        :type client: str
        :param user: 用户
        :type user: str
        :param killed: 执行状态
        :type killed: str
        :param execute_time_min: 最小执行时间（Unix timestamp），单位：毫秒
        :type execute_time_min: int
        :param execute_time_max: 最大执行时间（Unix timestamp），单位：毫秒
        :type execute_time_max: int
        :param min_avg_execute_time: 最小平均执行时间
        :type min_avg_execute_time: float
        :param max_avg_execute_time: 最大平均执行时间
        :type max_avg_execute_time: float
        :param rows_max_examined: 最大扫描行数
        :type rows_max_examined: int
        :param rows_min_examined: 最小扫描行数
        :type rows_min_examined: int
        :param fuzzy_sql: 模糊SQL
        :type fuzzy_sql: str
        :param operation: 操作（可组合，用逗号分隔）
        :type operation: str
        :param time_zone: 时区
        :type time_zone: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._bucket_name = None
        self._file_path = None
        self._export_type = None
        self._sort_field = None
        self._sort_asc = None
        self._client = None
        self._user = None
        self._killed = None
        self._execute_time_min = None
        self._execute_time_max = None
        self._min_avg_execute_time = None
        self._max_avg_execute_time = None
        self._rows_max_examined = None
        self._rows_min_examined = None
        self._fuzzy_sql = None
        self._operation = None
        self._time_zone = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.bucket_name = bucket_name
        if file_path is not None:
            self.file_path = file_path
        if export_type is not None:
            self.export_type = export_type
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_asc is not None:
            self.sort_asc = sort_asc
        if client is not None:
            self.client = client
        if user is not None:
            self.user = user
        if killed is not None:
            self.killed = killed
        if execute_time_min is not None:
            self.execute_time_min = execute_time_min
        if execute_time_max is not None:
            self.execute_time_max = execute_time_max
        if min_avg_execute_time is not None:
            self.min_avg_execute_time = min_avg_execute_time
        if max_avg_execute_time is not None:
            self.max_avg_execute_time = max_avg_execute_time
        if rows_max_examined is not None:
            self.rows_max_examined = rows_max_examined
        if rows_min_examined is not None:
            self.rows_min_examined = rows_min_examined
        if fuzzy_sql is not None:
            self.fuzzy_sql = fuzzy_sql
        if operation is not None:
            self.operation = operation
        if time_zone is not None:
            self.time_zone = time_zone

    @property
    def start_time(self):
        r"""Gets the start_time of this CreateSlowLogExportTaskNewRequestBody.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_time of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CreateSlowLogExportTaskNewRequestBody.

        开始时间（Unix timestamp），单位：毫秒

        :param start_time: The start_time of this CreateSlowLogExportTaskNewRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this CreateSlowLogExportTaskNewRequestBody.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_time of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CreateSlowLogExportTaskNewRequestBody.

        结束时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this CreateSlowLogExportTaskNewRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this CreateSlowLogExportTaskNewRequestBody.

        OBS桶名

        :return: The bucket_name of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this CreateSlowLogExportTaskNewRequestBody.

        OBS桶名

        :param bucket_name: The bucket_name of this CreateSlowLogExportTaskNewRequestBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def file_path(self):
        r"""Gets the file_path of this CreateSlowLogExportTaskNewRequestBody.

        文件目录

        :return: The file_path of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this CreateSlowLogExportTaskNewRequestBody.

        文件目录

        :param file_path: The file_path of this CreateSlowLogExportTaskNewRequestBody.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def export_type(self):
        r"""Gets the export_type of this CreateSlowLogExportTaskNewRequestBody.

        导出类型

        :return: The export_type of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        r"""Sets the export_type of this CreateSlowLogExportTaskNewRequestBody.

        导出类型

        :param export_type: The export_type of this CreateSlowLogExportTaskNewRequestBody.
        :type export_type: str
        """
        self._export_type = export_type

    @property
    def sort_field(self):
        r"""Gets the sort_field of this CreateSlowLogExportTaskNewRequestBody.

        排序字段

        :return: The sort_field of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this CreateSlowLogExportTaskNewRequestBody.

        排序字段

        :param sort_field: The sort_field of this CreateSlowLogExportTaskNewRequestBody.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_asc(self):
        r"""Gets the sort_asc of this CreateSlowLogExportTaskNewRequestBody.

        排序顺序（true：正序，false：逆序）

        :return: The sort_asc of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: bool
        """
        return self._sort_asc

    @sort_asc.setter
    def sort_asc(self, sort_asc):
        r"""Sets the sort_asc of this CreateSlowLogExportTaskNewRequestBody.

        排序顺序（true：正序，false：逆序）

        :param sort_asc: The sort_asc of this CreateSlowLogExportTaskNewRequestBody.
        :type sort_asc: bool
        """
        self._sort_asc = sort_asc

    @property
    def client(self):
        r"""Gets the client of this CreateSlowLogExportTaskNewRequestBody.

        客户端

        :return: The client of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: str
        """
        return self._client

    @client.setter
    def client(self, client):
        r"""Sets the client of this CreateSlowLogExportTaskNewRequestBody.

        客户端

        :param client: The client of this CreateSlowLogExportTaskNewRequestBody.
        :type client: str
        """
        self._client = client

    @property
    def user(self):
        r"""Gets the user of this CreateSlowLogExportTaskNewRequestBody.

        用户

        :return: The user of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this CreateSlowLogExportTaskNewRequestBody.

        用户

        :param user: The user of this CreateSlowLogExportTaskNewRequestBody.
        :type user: str
        """
        self._user = user

    @property
    def killed(self):
        r"""Gets the killed of this CreateSlowLogExportTaskNewRequestBody.

        执行状态

        :return: The killed of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: str
        """
        return self._killed

    @killed.setter
    def killed(self, killed):
        r"""Sets the killed of this CreateSlowLogExportTaskNewRequestBody.

        执行状态

        :param killed: The killed of this CreateSlowLogExportTaskNewRequestBody.
        :type killed: str
        """
        self._killed = killed

    @property
    def execute_time_min(self):
        r"""Gets the execute_time_min of this CreateSlowLogExportTaskNewRequestBody.

        最小执行时间（Unix timestamp），单位：毫秒

        :return: The execute_time_min of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: int
        """
        return self._execute_time_min

    @execute_time_min.setter
    def execute_time_min(self, execute_time_min):
        r"""Sets the execute_time_min of this CreateSlowLogExportTaskNewRequestBody.

        最小执行时间（Unix timestamp），单位：毫秒

        :param execute_time_min: The execute_time_min of this CreateSlowLogExportTaskNewRequestBody.
        :type execute_time_min: int
        """
        self._execute_time_min = execute_time_min

    @property
    def execute_time_max(self):
        r"""Gets the execute_time_max of this CreateSlowLogExportTaskNewRequestBody.

        最大执行时间（Unix timestamp），单位：毫秒

        :return: The execute_time_max of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: int
        """
        return self._execute_time_max

    @execute_time_max.setter
    def execute_time_max(self, execute_time_max):
        r"""Sets the execute_time_max of this CreateSlowLogExportTaskNewRequestBody.

        最大执行时间（Unix timestamp），单位：毫秒

        :param execute_time_max: The execute_time_max of this CreateSlowLogExportTaskNewRequestBody.
        :type execute_time_max: int
        """
        self._execute_time_max = execute_time_max

    @property
    def min_avg_execute_time(self):
        r"""Gets the min_avg_execute_time of this CreateSlowLogExportTaskNewRequestBody.

        最小平均执行时间

        :return: The min_avg_execute_time of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: float
        """
        return self._min_avg_execute_time

    @min_avg_execute_time.setter
    def min_avg_execute_time(self, min_avg_execute_time):
        r"""Sets the min_avg_execute_time of this CreateSlowLogExportTaskNewRequestBody.

        最小平均执行时间

        :param min_avg_execute_time: The min_avg_execute_time of this CreateSlowLogExportTaskNewRequestBody.
        :type min_avg_execute_time: float
        """
        self._min_avg_execute_time = min_avg_execute_time

    @property
    def max_avg_execute_time(self):
        r"""Gets the max_avg_execute_time of this CreateSlowLogExportTaskNewRequestBody.

        最大平均执行时间

        :return: The max_avg_execute_time of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: float
        """
        return self._max_avg_execute_time

    @max_avg_execute_time.setter
    def max_avg_execute_time(self, max_avg_execute_time):
        r"""Sets the max_avg_execute_time of this CreateSlowLogExportTaskNewRequestBody.

        最大平均执行时间

        :param max_avg_execute_time: The max_avg_execute_time of this CreateSlowLogExportTaskNewRequestBody.
        :type max_avg_execute_time: float
        """
        self._max_avg_execute_time = max_avg_execute_time

    @property
    def rows_max_examined(self):
        r"""Gets the rows_max_examined of this CreateSlowLogExportTaskNewRequestBody.

        最大扫描行数

        :return: The rows_max_examined of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: int
        """
        return self._rows_max_examined

    @rows_max_examined.setter
    def rows_max_examined(self, rows_max_examined):
        r"""Sets the rows_max_examined of this CreateSlowLogExportTaskNewRequestBody.

        最大扫描行数

        :param rows_max_examined: The rows_max_examined of this CreateSlowLogExportTaskNewRequestBody.
        :type rows_max_examined: int
        """
        self._rows_max_examined = rows_max_examined

    @property
    def rows_min_examined(self):
        r"""Gets the rows_min_examined of this CreateSlowLogExportTaskNewRequestBody.

        最小扫描行数

        :return: The rows_min_examined of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: int
        """
        return self._rows_min_examined

    @rows_min_examined.setter
    def rows_min_examined(self, rows_min_examined):
        r"""Sets the rows_min_examined of this CreateSlowLogExportTaskNewRequestBody.

        最小扫描行数

        :param rows_min_examined: The rows_min_examined of this CreateSlowLogExportTaskNewRequestBody.
        :type rows_min_examined: int
        """
        self._rows_min_examined = rows_min_examined

    @property
    def fuzzy_sql(self):
        r"""Gets the fuzzy_sql of this CreateSlowLogExportTaskNewRequestBody.

        模糊SQL

        :return: The fuzzy_sql of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: str
        """
        return self._fuzzy_sql

    @fuzzy_sql.setter
    def fuzzy_sql(self, fuzzy_sql):
        r"""Sets the fuzzy_sql of this CreateSlowLogExportTaskNewRequestBody.

        模糊SQL

        :param fuzzy_sql: The fuzzy_sql of this CreateSlowLogExportTaskNewRequestBody.
        :type fuzzy_sql: str
        """
        self._fuzzy_sql = fuzzy_sql

    @property
    def operation(self):
        r"""Gets the operation of this CreateSlowLogExportTaskNewRequestBody.

        操作（可组合，用逗号分隔）

        :return: The operation of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this CreateSlowLogExportTaskNewRequestBody.

        操作（可组合，用逗号分隔）

        :param operation: The operation of this CreateSlowLogExportTaskNewRequestBody.
        :type operation: str
        """
        self._operation = operation

    @property
    def time_zone(self):
        r"""Gets the time_zone of this CreateSlowLogExportTaskNewRequestBody.

        时区

        :return: The time_zone of this CreateSlowLogExportTaskNewRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this CreateSlowLogExportTaskNewRequestBody.

        时区

        :param time_zone: The time_zone of this CreateSlowLogExportTaskNewRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

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
        if not isinstance(other, CreateSlowLogExportTaskNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
