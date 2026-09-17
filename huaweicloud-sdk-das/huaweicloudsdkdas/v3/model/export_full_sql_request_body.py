# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportFullSqlRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_at': 'int',
        'end_at': 'int',
        'task_ids': 'list[int]',
        'node_id': 'str',
        'keyword': 'str',
        'fuzzy': 'bool',
        'user_list': 'list[str]',
        'db_list': 'list[str]',
        'operation_list': 'list[str]',
        'client_ip_list': 'list[str]',
        'thread_id_list': 'list[int]',
        'trx_id_list': 'list[int]',
        'session_id_list': 'list[int]',
        'status_list': 'list[int]',
        'cost_min': 'float',
        'cost_max': 'float',
        'scan_min': 'int',
        'scan_max': 'int',
        'affect_min': 'int',
        'affect_max': 'int',
        'return_min': 'int',
        'return_max': 'int',
        'bucket_name': 'str',
        'export_column_list': 'list[str]',
        'time_zone': 'str',
        'instance_id': 'str',
        'task_id': 'int'
    }

    attribute_map = {
        'start_at': 'start_at',
        'end_at': 'end_at',
        'task_ids': 'task_ids',
        'node_id': 'node_id',
        'keyword': 'keyword',
        'fuzzy': 'fuzzy',
        'user_list': 'user_list',
        'db_list': 'db_list',
        'operation_list': 'operation_list',
        'client_ip_list': 'client_ip_list',
        'thread_id_list': 'thread_id_list',
        'trx_id_list': 'trx_id_list',
        'session_id_list': 'session_id_list',
        'status_list': 'status_list',
        'cost_min': 'cost_min',
        'cost_max': 'cost_max',
        'scan_min': 'scan_min',
        'scan_max': 'scan_max',
        'affect_min': 'affect_min',
        'affect_max': 'affect_max',
        'return_min': 'return_min',
        'return_max': 'return_max',
        'bucket_name': 'bucket_name',
        'export_column_list': 'export_column_list',
        'time_zone': 'time_zone',
        'instance_id': 'instance_id',
        'task_id': 'task_id'
    }

    def __init__(self, start_at=None, end_at=None, task_ids=None, node_id=None, keyword=None, fuzzy=None, user_list=None, db_list=None, operation_list=None, client_ip_list=None, thread_id_list=None, trx_id_list=None, session_id_list=None, status_list=None, cost_min=None, cost_max=None, scan_min=None, scan_max=None, affect_min=None, affect_max=None, return_min=None, return_max=None, bucket_name=None, export_column_list=None, time_zone=None, instance_id=None, task_id=None):
        r"""ExportFullSqlRequestBody

        The model defined in huaweicloud sdk

        :param start_at: 开始时间（Unix timestamp），单位：毫秒
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒
        :type end_at: int
        :param task_ids: SQL洞察任务ID列表
        :type task_ids: list[int]
        :param node_id: 节点ID
        :type node_id: str
        :param keyword: 关键字
        :type keyword: str
        :param fuzzy: 是否模糊匹配
        :type fuzzy: bool
        :param user_list: 用户名
        :type user_list: list[str]
        :param db_list: 数据库
        :type db_list: list[str]
        :param operation_list: 操作类型
        :type operation_list: list[str]
        :param client_ip_list: 客户端IP
        :type client_ip_list: list[str]
        :param thread_id_list: 线程ID
        :type thread_id_list: list[int]
        :param trx_id_list: 事务ID
        :type trx_id_list: list[int]
        :param session_id_list: 会话ID
        :type session_id_list: list[int]
        :param status_list: 执行状态（0：成功，1：失败）
        :type status_list: list[int]
        :param cost_min: 最小执行耗时（毫秒）
        :type cost_min: float
        :param cost_max: 最大执行耗时（毫秒）
        :type cost_max: float
        :param scan_min: 最小扫描行数
        :type scan_min: int
        :param scan_max: 最大扫描行数
        :type scan_max: int
        :param affect_min: 最小影响行数
        :type affect_min: int
        :param affect_max: 最大影响行数
        :type affect_max: int
        :param return_min: 最小返回行数
        :type return_min: int
        :param return_max: 最大返回行数
        :type return_max: int
        :param bucket_name: OBS桶名
        :type bucket_name: str
        :param export_column_list: 导出的列名
        :type export_column_list: list[str]
        :param time_zone: 时区
        :type time_zone: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param task_id: 任务ID
        :type task_id: int
        """
        
        

        self._start_at = None
        self._end_at = None
        self._task_ids = None
        self._node_id = None
        self._keyword = None
        self._fuzzy = None
        self._user_list = None
        self._db_list = None
        self._operation_list = None
        self._client_ip_list = None
        self._thread_id_list = None
        self._trx_id_list = None
        self._session_id_list = None
        self._status_list = None
        self._cost_min = None
        self._cost_max = None
        self._scan_min = None
        self._scan_max = None
        self._affect_min = None
        self._affect_max = None
        self._return_min = None
        self._return_max = None
        self._bucket_name = None
        self._export_column_list = None
        self._time_zone = None
        self._instance_id = None
        self._task_id = None
        self.discriminator = None

        self.start_at = start_at
        self.end_at = end_at
        if task_ids is not None:
            self.task_ids = task_ids
        if node_id is not None:
            self.node_id = node_id
        if keyword is not None:
            self.keyword = keyword
        if fuzzy is not None:
            self.fuzzy = fuzzy
        if user_list is not None:
            self.user_list = user_list
        if db_list is not None:
            self.db_list = db_list
        if operation_list is not None:
            self.operation_list = operation_list
        if client_ip_list is not None:
            self.client_ip_list = client_ip_list
        if thread_id_list is not None:
            self.thread_id_list = thread_id_list
        if trx_id_list is not None:
            self.trx_id_list = trx_id_list
        if session_id_list is not None:
            self.session_id_list = session_id_list
        if status_list is not None:
            self.status_list = status_list
        if cost_min is not None:
            self.cost_min = cost_min
        if cost_max is not None:
            self.cost_max = cost_max
        if scan_min is not None:
            self.scan_min = scan_min
        if scan_max is not None:
            self.scan_max = scan_max
        if affect_min is not None:
            self.affect_min = affect_min
        if affect_max is not None:
            self.affect_max = affect_max
        if return_min is not None:
            self.return_min = return_min
        if return_max is not None:
            self.return_max = return_max
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if export_column_list is not None:
            self.export_column_list = export_column_list
        if time_zone is not None:
            self.time_zone = time_zone
        if instance_id is not None:
            self.instance_id = instance_id
        if task_id is not None:
            self.task_id = task_id

    @property
    def start_at(self):
        r"""Gets the start_at of this ExportFullSqlRequestBody.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_at of this ExportFullSqlRequestBody.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ExportFullSqlRequestBody.

        开始时间（Unix timestamp），单位：毫秒

        :param start_at: The start_at of this ExportFullSqlRequestBody.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ExportFullSqlRequestBody.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_at of this ExportFullSqlRequestBody.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ExportFullSqlRequestBody.

        结束时间（Unix timestamp），单位：毫秒

        :param end_at: The end_at of this ExportFullSqlRequestBody.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def task_ids(self):
        r"""Gets the task_ids of this ExportFullSqlRequestBody.

        SQL洞察任务ID列表

        :return: The task_ids of this ExportFullSqlRequestBody.
        :rtype: list[int]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        r"""Sets the task_ids of this ExportFullSqlRequestBody.

        SQL洞察任务ID列表

        :param task_ids: The task_ids of this ExportFullSqlRequestBody.
        :type task_ids: list[int]
        """
        self._task_ids = task_ids

    @property
    def node_id(self):
        r"""Gets the node_id of this ExportFullSqlRequestBody.

        节点ID

        :return: The node_id of this ExportFullSqlRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ExportFullSqlRequestBody.

        节点ID

        :param node_id: The node_id of this ExportFullSqlRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def keyword(self):
        r"""Gets the keyword of this ExportFullSqlRequestBody.

        关键字

        :return: The keyword of this ExportFullSqlRequestBody.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ExportFullSqlRequestBody.

        关键字

        :param keyword: The keyword of this ExportFullSqlRequestBody.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def fuzzy(self):
        r"""Gets the fuzzy of this ExportFullSqlRequestBody.

        是否模糊匹配

        :return: The fuzzy of this ExportFullSqlRequestBody.
        :rtype: bool
        """
        return self._fuzzy

    @fuzzy.setter
    def fuzzy(self, fuzzy):
        r"""Sets the fuzzy of this ExportFullSqlRequestBody.

        是否模糊匹配

        :param fuzzy: The fuzzy of this ExportFullSqlRequestBody.
        :type fuzzy: bool
        """
        self._fuzzy = fuzzy

    @property
    def user_list(self):
        r"""Gets the user_list of this ExportFullSqlRequestBody.

        用户名

        :return: The user_list of this ExportFullSqlRequestBody.
        :rtype: list[str]
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        r"""Sets the user_list of this ExportFullSqlRequestBody.

        用户名

        :param user_list: The user_list of this ExportFullSqlRequestBody.
        :type user_list: list[str]
        """
        self._user_list = user_list

    @property
    def db_list(self):
        r"""Gets the db_list of this ExportFullSqlRequestBody.

        数据库

        :return: The db_list of this ExportFullSqlRequestBody.
        :rtype: list[str]
        """
        return self._db_list

    @db_list.setter
    def db_list(self, db_list):
        r"""Sets the db_list of this ExportFullSqlRequestBody.

        数据库

        :param db_list: The db_list of this ExportFullSqlRequestBody.
        :type db_list: list[str]
        """
        self._db_list = db_list

    @property
    def operation_list(self):
        r"""Gets the operation_list of this ExportFullSqlRequestBody.

        操作类型

        :return: The operation_list of this ExportFullSqlRequestBody.
        :rtype: list[str]
        """
        return self._operation_list

    @operation_list.setter
    def operation_list(self, operation_list):
        r"""Sets the operation_list of this ExportFullSqlRequestBody.

        操作类型

        :param operation_list: The operation_list of this ExportFullSqlRequestBody.
        :type operation_list: list[str]
        """
        self._operation_list = operation_list

    @property
    def client_ip_list(self):
        r"""Gets the client_ip_list of this ExportFullSqlRequestBody.

        客户端IP

        :return: The client_ip_list of this ExportFullSqlRequestBody.
        :rtype: list[str]
        """
        return self._client_ip_list

    @client_ip_list.setter
    def client_ip_list(self, client_ip_list):
        r"""Sets the client_ip_list of this ExportFullSqlRequestBody.

        客户端IP

        :param client_ip_list: The client_ip_list of this ExportFullSqlRequestBody.
        :type client_ip_list: list[str]
        """
        self._client_ip_list = client_ip_list

    @property
    def thread_id_list(self):
        r"""Gets the thread_id_list of this ExportFullSqlRequestBody.

        线程ID

        :return: The thread_id_list of this ExportFullSqlRequestBody.
        :rtype: list[int]
        """
        return self._thread_id_list

    @thread_id_list.setter
    def thread_id_list(self, thread_id_list):
        r"""Sets the thread_id_list of this ExportFullSqlRequestBody.

        线程ID

        :param thread_id_list: The thread_id_list of this ExportFullSqlRequestBody.
        :type thread_id_list: list[int]
        """
        self._thread_id_list = thread_id_list

    @property
    def trx_id_list(self):
        r"""Gets the trx_id_list of this ExportFullSqlRequestBody.

        事务ID

        :return: The trx_id_list of this ExportFullSqlRequestBody.
        :rtype: list[int]
        """
        return self._trx_id_list

    @trx_id_list.setter
    def trx_id_list(self, trx_id_list):
        r"""Sets the trx_id_list of this ExportFullSqlRequestBody.

        事务ID

        :param trx_id_list: The trx_id_list of this ExportFullSqlRequestBody.
        :type trx_id_list: list[int]
        """
        self._trx_id_list = trx_id_list

    @property
    def session_id_list(self):
        r"""Gets the session_id_list of this ExportFullSqlRequestBody.

        会话ID

        :return: The session_id_list of this ExportFullSqlRequestBody.
        :rtype: list[int]
        """
        return self._session_id_list

    @session_id_list.setter
    def session_id_list(self, session_id_list):
        r"""Sets the session_id_list of this ExportFullSqlRequestBody.

        会话ID

        :param session_id_list: The session_id_list of this ExportFullSqlRequestBody.
        :type session_id_list: list[int]
        """
        self._session_id_list = session_id_list

    @property
    def status_list(self):
        r"""Gets the status_list of this ExportFullSqlRequestBody.

        执行状态（0：成功，1：失败）

        :return: The status_list of this ExportFullSqlRequestBody.
        :rtype: list[int]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this ExportFullSqlRequestBody.

        执行状态（0：成功，1：失败）

        :param status_list: The status_list of this ExportFullSqlRequestBody.
        :type status_list: list[int]
        """
        self._status_list = status_list

    @property
    def cost_min(self):
        r"""Gets the cost_min of this ExportFullSqlRequestBody.

        最小执行耗时（毫秒）

        :return: The cost_min of this ExportFullSqlRequestBody.
        :rtype: float
        """
        return self._cost_min

    @cost_min.setter
    def cost_min(self, cost_min):
        r"""Sets the cost_min of this ExportFullSqlRequestBody.

        最小执行耗时（毫秒）

        :param cost_min: The cost_min of this ExportFullSqlRequestBody.
        :type cost_min: float
        """
        self._cost_min = cost_min

    @property
    def cost_max(self):
        r"""Gets the cost_max of this ExportFullSqlRequestBody.

        最大执行耗时（毫秒）

        :return: The cost_max of this ExportFullSqlRequestBody.
        :rtype: float
        """
        return self._cost_max

    @cost_max.setter
    def cost_max(self, cost_max):
        r"""Sets the cost_max of this ExportFullSqlRequestBody.

        最大执行耗时（毫秒）

        :param cost_max: The cost_max of this ExportFullSqlRequestBody.
        :type cost_max: float
        """
        self._cost_max = cost_max

    @property
    def scan_min(self):
        r"""Gets the scan_min of this ExportFullSqlRequestBody.

        最小扫描行数

        :return: The scan_min of this ExportFullSqlRequestBody.
        :rtype: int
        """
        return self._scan_min

    @scan_min.setter
    def scan_min(self, scan_min):
        r"""Sets the scan_min of this ExportFullSqlRequestBody.

        最小扫描行数

        :param scan_min: The scan_min of this ExportFullSqlRequestBody.
        :type scan_min: int
        """
        self._scan_min = scan_min

    @property
    def scan_max(self):
        r"""Gets the scan_max of this ExportFullSqlRequestBody.

        最大扫描行数

        :return: The scan_max of this ExportFullSqlRequestBody.
        :rtype: int
        """
        return self._scan_max

    @scan_max.setter
    def scan_max(self, scan_max):
        r"""Sets the scan_max of this ExportFullSqlRequestBody.

        最大扫描行数

        :param scan_max: The scan_max of this ExportFullSqlRequestBody.
        :type scan_max: int
        """
        self._scan_max = scan_max

    @property
    def affect_min(self):
        r"""Gets the affect_min of this ExportFullSqlRequestBody.

        最小影响行数

        :return: The affect_min of this ExportFullSqlRequestBody.
        :rtype: int
        """
        return self._affect_min

    @affect_min.setter
    def affect_min(self, affect_min):
        r"""Sets the affect_min of this ExportFullSqlRequestBody.

        最小影响行数

        :param affect_min: The affect_min of this ExportFullSqlRequestBody.
        :type affect_min: int
        """
        self._affect_min = affect_min

    @property
    def affect_max(self):
        r"""Gets the affect_max of this ExportFullSqlRequestBody.

        最大影响行数

        :return: The affect_max of this ExportFullSqlRequestBody.
        :rtype: int
        """
        return self._affect_max

    @affect_max.setter
    def affect_max(self, affect_max):
        r"""Sets the affect_max of this ExportFullSqlRequestBody.

        最大影响行数

        :param affect_max: The affect_max of this ExportFullSqlRequestBody.
        :type affect_max: int
        """
        self._affect_max = affect_max

    @property
    def return_min(self):
        r"""Gets the return_min of this ExportFullSqlRequestBody.

        最小返回行数

        :return: The return_min of this ExportFullSqlRequestBody.
        :rtype: int
        """
        return self._return_min

    @return_min.setter
    def return_min(self, return_min):
        r"""Sets the return_min of this ExportFullSqlRequestBody.

        最小返回行数

        :param return_min: The return_min of this ExportFullSqlRequestBody.
        :type return_min: int
        """
        self._return_min = return_min

    @property
    def return_max(self):
        r"""Gets the return_max of this ExportFullSqlRequestBody.

        最大返回行数

        :return: The return_max of this ExportFullSqlRequestBody.
        :rtype: int
        """
        return self._return_max

    @return_max.setter
    def return_max(self, return_max):
        r"""Sets the return_max of this ExportFullSqlRequestBody.

        最大返回行数

        :param return_max: The return_max of this ExportFullSqlRequestBody.
        :type return_max: int
        """
        self._return_max = return_max

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ExportFullSqlRequestBody.

        OBS桶名

        :return: The bucket_name of this ExportFullSqlRequestBody.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ExportFullSqlRequestBody.

        OBS桶名

        :param bucket_name: The bucket_name of this ExportFullSqlRequestBody.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def export_column_list(self):
        r"""Gets the export_column_list of this ExportFullSqlRequestBody.

        导出的列名

        :return: The export_column_list of this ExportFullSqlRequestBody.
        :rtype: list[str]
        """
        return self._export_column_list

    @export_column_list.setter
    def export_column_list(self, export_column_list):
        r"""Sets the export_column_list of this ExportFullSqlRequestBody.

        导出的列名

        :param export_column_list: The export_column_list of this ExportFullSqlRequestBody.
        :type export_column_list: list[str]
        """
        self._export_column_list = export_column_list

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ExportFullSqlRequestBody.

        时区

        :return: The time_zone of this ExportFullSqlRequestBody.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ExportFullSqlRequestBody.

        时区

        :param time_zone: The time_zone of this ExportFullSqlRequestBody.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ExportFullSqlRequestBody.

        实例ID

        :return: The instance_id of this ExportFullSqlRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ExportFullSqlRequestBody.

        实例ID

        :param instance_id: The instance_id of this ExportFullSqlRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ExportFullSqlRequestBody.

        任务ID

        :return: The task_id of this ExportFullSqlRequestBody.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ExportFullSqlRequestBody.

        任务ID

        :param task_id: The task_id of this ExportFullSqlRequestBody.
        :type task_id: int
        """
        self._task_id = task_id

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
        if not isinstance(other, ExportFullSqlRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
