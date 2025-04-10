# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportFullSqlDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'task_ids': 'list[int]',
        'node_id': 'str',
        'keyword': 'str',
        'fuzzy': 'str',
        'user_list': 'str',
        'db_list': 'str',
        'operation_list': 'str',
        'client_ip_list': 'str',
        'thread_id_list': 'str',
        'trx_id_list': 'str',
        'session_id_list': 'str',
        'status_list': 'str',
        'sql_template_ids': 'str',
        'cost_min': 'float',
        'cost_max': 'float',
        'scan_min': 'int',
        'scan_max': 'int',
        'affect_min': 'int',
        'affect_max': 'int',
        'return_min': 'int',
        'return_max': 'int',
        'sort_field': 'str',
        'asc': 'bool',
        'page': 'int',
        'limit': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
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
        'sql_template_ids': 'sql_template_ids',
        'cost_min': 'cost_min',
        'cost_max': 'cost_max',
        'scan_min': 'scan_min',
        'scan_max': 'scan_max',
        'affect_min': 'affect_min',
        'affect_max': 'affect_max',
        'return_min': 'return_min',
        'return_max': 'return_max',
        'sort_field': 'sort_field',
        'asc': 'asc',
        'page': 'page',
        'limit': 'limit',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, start_at=None, end_at=None, task_ids=None, node_id=None, keyword=None, fuzzy=None, user_list=None, db_list=None, operation_list=None, client_ip_list=None, thread_id_list=None, trx_id_list=None, session_id_list=None, status_list=None, sql_template_ids=None, cost_min=None, cost_max=None, scan_min=None, scan_max=None, affect_min=None, affect_max=None, return_min=None, return_max=None, sort_field=None, asc=None, page=None, limit=None, x_language=None):
        r"""ExportFullSqlDetailsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param start_at: 开始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        :param task_ids: SQL洞察任务ID列表，时间范围大于1天的SQL洞察任务后台将拆分为多个任务解析，该场景支持多任务过滤导出。
        :type task_ids: list[int]
        :param node_id: 节点ID。
        :type node_id: str
        :param keyword: 关键字（可组合，用逗号分隔）。
        :type keyword: str
        :param fuzzy: 是否模糊匹配。
        :type fuzzy: str
        :param user_list: 用户名（可组合，用空格分隔）。
        :type user_list: str
        :param db_list: 数据库（可组合，用空格分隔）。
        :type db_list: str
        :param operation_list: 操作类型（可组合，用空格分隔）。
        :type operation_list: str
        :param client_ip_list: 客户端IP（可组合，用空格分隔）。
        :type client_ip_list: str
        :param thread_id_list: 线程ID（可组合，用空格分隔）。
        :type thread_id_list: str
        :param trx_id_list: 事务ID（可组合，用空格分隔）。
        :type trx_id_list: str
        :param session_id_list: 会话ID（可组合，用空格分隔）。
        :type session_id_list: str
        :param status_list: 执行状态（0:成功，1:失败，可组合，用空格分隔）。
        :type status_list: str
        :param sql_template_ids: SQL模板ID（可组合，用空格分隔）。
        :type sql_template_ids: str
        :param cost_min: 最小执行耗时（毫秒）。
        :type cost_min: float
        :param cost_max: 最大执行耗时（毫秒）。
        :type cost_max: float
        :param scan_min: 最小扫描行数。
        :type scan_min: int
        :param scan_max: 最大扫描行数。
        :type scan_max: int
        :param affect_min: 最小影响行数。
        :type affect_min: int
        :param affect_max: 最大影响行数。
        :type affect_max: int
        :param return_min: 最小返回行数。
        :type return_min: int
        :param return_max: 最大返回行数。
        :type return_max: int
        :param sort_field: 排序字段（execute_at:执行时间, execute_cost:执行耗时, lock_wait_time:锁等待时间, rows_examined:扫描行数, rows_returned:返回行数）。
        :type sort_field: str
        :param asc: 排序顺序（true:正序, false:逆序）。
        :type asc: bool
        :param page: 页码。
        :type page: int
        :param limit: 每页记录数。最大为100。
        :type limit: int
        :param x_language: 请求语言类型。
        :type x_language: str
        """
        
        

        self._instance_id = None
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
        self._sql_template_ids = None
        self._cost_min = None
        self._cost_max = None
        self._scan_min = None
        self._scan_max = None
        self._affect_min = None
        self._affect_max = None
        self._return_min = None
        self._return_max = None
        self._sort_field = None
        self._asc = None
        self._page = None
        self._limit = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
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
        if sql_template_ids is not None:
            self.sql_template_ids = sql_template_ids
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
        if sort_field is not None:
            self.sort_field = sort_field
        if asc is not None:
            self.asc = asc
        if page is not None:
            self.page = page
        if limit is not None:
            self.limit = limit
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ExportFullSqlDetailsRequest.

        实例ID。

        :return: The instance_id of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ExportFullSqlDetailsRequest.

        实例ID。

        :param instance_id: The instance_id of this ExportFullSqlDetailsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_at(self):
        r"""Gets the start_at of this ExportFullSqlDetailsRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this ExportFullSqlDetailsRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ExportFullSqlDetailsRequest.

        开始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this ExportFullSqlDetailsRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ExportFullSqlDetailsRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this ExportFullSqlDetailsRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ExportFullSqlDetailsRequest.

        结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this ExportFullSqlDetailsRequest.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def task_ids(self):
        r"""Gets the task_ids of this ExportFullSqlDetailsRequest.

        SQL洞察任务ID列表，时间范围大于1天的SQL洞察任务后台将拆分为多个任务解析，该场景支持多任务过滤导出。

        :return: The task_ids of this ExportFullSqlDetailsRequest.
        :rtype: list[int]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        r"""Sets the task_ids of this ExportFullSqlDetailsRequest.

        SQL洞察任务ID列表，时间范围大于1天的SQL洞察任务后台将拆分为多个任务解析，该场景支持多任务过滤导出。

        :param task_ids: The task_ids of this ExportFullSqlDetailsRequest.
        :type task_ids: list[int]
        """
        self._task_ids = task_ids

    @property
    def node_id(self):
        r"""Gets the node_id of this ExportFullSqlDetailsRequest.

        节点ID。

        :return: The node_id of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ExportFullSqlDetailsRequest.

        节点ID。

        :param node_id: The node_id of this ExportFullSqlDetailsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def keyword(self):
        r"""Gets the keyword of this ExportFullSqlDetailsRequest.

        关键字（可组合，用逗号分隔）。

        :return: The keyword of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ExportFullSqlDetailsRequest.

        关键字（可组合，用逗号分隔）。

        :param keyword: The keyword of this ExportFullSqlDetailsRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def fuzzy(self):
        r"""Gets the fuzzy of this ExportFullSqlDetailsRequest.

        是否模糊匹配。

        :return: The fuzzy of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._fuzzy

    @fuzzy.setter
    def fuzzy(self, fuzzy):
        r"""Sets the fuzzy of this ExportFullSqlDetailsRequest.

        是否模糊匹配。

        :param fuzzy: The fuzzy of this ExportFullSqlDetailsRequest.
        :type fuzzy: str
        """
        self._fuzzy = fuzzy

    @property
    def user_list(self):
        r"""Gets the user_list of this ExportFullSqlDetailsRequest.

        用户名（可组合，用空格分隔）。

        :return: The user_list of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        r"""Sets the user_list of this ExportFullSqlDetailsRequest.

        用户名（可组合，用空格分隔）。

        :param user_list: The user_list of this ExportFullSqlDetailsRequest.
        :type user_list: str
        """
        self._user_list = user_list

    @property
    def db_list(self):
        r"""Gets the db_list of this ExportFullSqlDetailsRequest.

        数据库（可组合，用空格分隔）。

        :return: The db_list of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._db_list

    @db_list.setter
    def db_list(self, db_list):
        r"""Sets the db_list of this ExportFullSqlDetailsRequest.

        数据库（可组合，用空格分隔）。

        :param db_list: The db_list of this ExportFullSqlDetailsRequest.
        :type db_list: str
        """
        self._db_list = db_list

    @property
    def operation_list(self):
        r"""Gets the operation_list of this ExportFullSqlDetailsRequest.

        操作类型（可组合，用空格分隔）。

        :return: The operation_list of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._operation_list

    @operation_list.setter
    def operation_list(self, operation_list):
        r"""Sets the operation_list of this ExportFullSqlDetailsRequest.

        操作类型（可组合，用空格分隔）。

        :param operation_list: The operation_list of this ExportFullSqlDetailsRequest.
        :type operation_list: str
        """
        self._operation_list = operation_list

    @property
    def client_ip_list(self):
        r"""Gets the client_ip_list of this ExportFullSqlDetailsRequest.

        客户端IP（可组合，用空格分隔）。

        :return: The client_ip_list of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._client_ip_list

    @client_ip_list.setter
    def client_ip_list(self, client_ip_list):
        r"""Sets the client_ip_list of this ExportFullSqlDetailsRequest.

        客户端IP（可组合，用空格分隔）。

        :param client_ip_list: The client_ip_list of this ExportFullSqlDetailsRequest.
        :type client_ip_list: str
        """
        self._client_ip_list = client_ip_list

    @property
    def thread_id_list(self):
        r"""Gets the thread_id_list of this ExportFullSqlDetailsRequest.

        线程ID（可组合，用空格分隔）。

        :return: The thread_id_list of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._thread_id_list

    @thread_id_list.setter
    def thread_id_list(self, thread_id_list):
        r"""Sets the thread_id_list of this ExportFullSqlDetailsRequest.

        线程ID（可组合，用空格分隔）。

        :param thread_id_list: The thread_id_list of this ExportFullSqlDetailsRequest.
        :type thread_id_list: str
        """
        self._thread_id_list = thread_id_list

    @property
    def trx_id_list(self):
        r"""Gets the trx_id_list of this ExportFullSqlDetailsRequest.

        事务ID（可组合，用空格分隔）。

        :return: The trx_id_list of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._trx_id_list

    @trx_id_list.setter
    def trx_id_list(self, trx_id_list):
        r"""Sets the trx_id_list of this ExportFullSqlDetailsRequest.

        事务ID（可组合，用空格分隔）。

        :param trx_id_list: The trx_id_list of this ExportFullSqlDetailsRequest.
        :type trx_id_list: str
        """
        self._trx_id_list = trx_id_list

    @property
    def session_id_list(self):
        r"""Gets the session_id_list of this ExportFullSqlDetailsRequest.

        会话ID（可组合，用空格分隔）。

        :return: The session_id_list of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._session_id_list

    @session_id_list.setter
    def session_id_list(self, session_id_list):
        r"""Sets the session_id_list of this ExportFullSqlDetailsRequest.

        会话ID（可组合，用空格分隔）。

        :param session_id_list: The session_id_list of this ExportFullSqlDetailsRequest.
        :type session_id_list: str
        """
        self._session_id_list = session_id_list

    @property
    def status_list(self):
        r"""Gets the status_list of this ExportFullSqlDetailsRequest.

        执行状态（0:成功，1:失败，可组合，用空格分隔）。

        :return: The status_list of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        r"""Sets the status_list of this ExportFullSqlDetailsRequest.

        执行状态（0:成功，1:失败，可组合，用空格分隔）。

        :param status_list: The status_list of this ExportFullSqlDetailsRequest.
        :type status_list: str
        """
        self._status_list = status_list

    @property
    def sql_template_ids(self):
        r"""Gets the sql_template_ids of this ExportFullSqlDetailsRequest.

        SQL模板ID（可组合，用空格分隔）。

        :return: The sql_template_ids of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._sql_template_ids

    @sql_template_ids.setter
    def sql_template_ids(self, sql_template_ids):
        r"""Sets the sql_template_ids of this ExportFullSqlDetailsRequest.

        SQL模板ID（可组合，用空格分隔）。

        :param sql_template_ids: The sql_template_ids of this ExportFullSqlDetailsRequest.
        :type sql_template_ids: str
        """
        self._sql_template_ids = sql_template_ids

    @property
    def cost_min(self):
        r"""Gets the cost_min of this ExportFullSqlDetailsRequest.

        最小执行耗时（毫秒）。

        :return: The cost_min of this ExportFullSqlDetailsRequest.
        :rtype: float
        """
        return self._cost_min

    @cost_min.setter
    def cost_min(self, cost_min):
        r"""Sets the cost_min of this ExportFullSqlDetailsRequest.

        最小执行耗时（毫秒）。

        :param cost_min: The cost_min of this ExportFullSqlDetailsRequest.
        :type cost_min: float
        """
        self._cost_min = cost_min

    @property
    def cost_max(self):
        r"""Gets the cost_max of this ExportFullSqlDetailsRequest.

        最大执行耗时（毫秒）。

        :return: The cost_max of this ExportFullSqlDetailsRequest.
        :rtype: float
        """
        return self._cost_max

    @cost_max.setter
    def cost_max(self, cost_max):
        r"""Sets the cost_max of this ExportFullSqlDetailsRequest.

        最大执行耗时（毫秒）。

        :param cost_max: The cost_max of this ExportFullSqlDetailsRequest.
        :type cost_max: float
        """
        self._cost_max = cost_max

    @property
    def scan_min(self):
        r"""Gets the scan_min of this ExportFullSqlDetailsRequest.

        最小扫描行数。

        :return: The scan_min of this ExportFullSqlDetailsRequest.
        :rtype: int
        """
        return self._scan_min

    @scan_min.setter
    def scan_min(self, scan_min):
        r"""Sets the scan_min of this ExportFullSqlDetailsRequest.

        最小扫描行数。

        :param scan_min: The scan_min of this ExportFullSqlDetailsRequest.
        :type scan_min: int
        """
        self._scan_min = scan_min

    @property
    def scan_max(self):
        r"""Gets the scan_max of this ExportFullSqlDetailsRequest.

        最大扫描行数。

        :return: The scan_max of this ExportFullSqlDetailsRequest.
        :rtype: int
        """
        return self._scan_max

    @scan_max.setter
    def scan_max(self, scan_max):
        r"""Sets the scan_max of this ExportFullSqlDetailsRequest.

        最大扫描行数。

        :param scan_max: The scan_max of this ExportFullSqlDetailsRequest.
        :type scan_max: int
        """
        self._scan_max = scan_max

    @property
    def affect_min(self):
        r"""Gets the affect_min of this ExportFullSqlDetailsRequest.

        最小影响行数。

        :return: The affect_min of this ExportFullSqlDetailsRequest.
        :rtype: int
        """
        return self._affect_min

    @affect_min.setter
    def affect_min(self, affect_min):
        r"""Sets the affect_min of this ExportFullSqlDetailsRequest.

        最小影响行数。

        :param affect_min: The affect_min of this ExportFullSqlDetailsRequest.
        :type affect_min: int
        """
        self._affect_min = affect_min

    @property
    def affect_max(self):
        r"""Gets the affect_max of this ExportFullSqlDetailsRequest.

        最大影响行数。

        :return: The affect_max of this ExportFullSqlDetailsRequest.
        :rtype: int
        """
        return self._affect_max

    @affect_max.setter
    def affect_max(self, affect_max):
        r"""Sets the affect_max of this ExportFullSqlDetailsRequest.

        最大影响行数。

        :param affect_max: The affect_max of this ExportFullSqlDetailsRequest.
        :type affect_max: int
        """
        self._affect_max = affect_max

    @property
    def return_min(self):
        r"""Gets the return_min of this ExportFullSqlDetailsRequest.

        最小返回行数。

        :return: The return_min of this ExportFullSqlDetailsRequest.
        :rtype: int
        """
        return self._return_min

    @return_min.setter
    def return_min(self, return_min):
        r"""Sets the return_min of this ExportFullSqlDetailsRequest.

        最小返回行数。

        :param return_min: The return_min of this ExportFullSqlDetailsRequest.
        :type return_min: int
        """
        self._return_min = return_min

    @property
    def return_max(self):
        r"""Gets the return_max of this ExportFullSqlDetailsRequest.

        最大返回行数。

        :return: The return_max of this ExportFullSqlDetailsRequest.
        :rtype: int
        """
        return self._return_max

    @return_max.setter
    def return_max(self, return_max):
        r"""Sets the return_max of this ExportFullSqlDetailsRequest.

        最大返回行数。

        :param return_max: The return_max of this ExportFullSqlDetailsRequest.
        :type return_max: int
        """
        self._return_max = return_max

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ExportFullSqlDetailsRequest.

        排序字段（execute_at:执行时间, execute_cost:执行耗时, lock_wait_time:锁等待时间, rows_examined:扫描行数, rows_returned:返回行数）。

        :return: The sort_field of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ExportFullSqlDetailsRequest.

        排序字段（execute_at:执行时间, execute_cost:执行耗时, lock_wait_time:锁等待时间, rows_examined:扫描行数, rows_returned:返回行数）。

        :param sort_field: The sort_field of this ExportFullSqlDetailsRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def asc(self):
        r"""Gets the asc of this ExportFullSqlDetailsRequest.

        排序顺序（true:正序, false:逆序）。

        :return: The asc of this ExportFullSqlDetailsRequest.
        :rtype: bool
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        r"""Sets the asc of this ExportFullSqlDetailsRequest.

        排序顺序（true:正序, false:逆序）。

        :param asc: The asc of this ExportFullSqlDetailsRequest.
        :type asc: bool
        """
        self._asc = asc

    @property
    def page(self):
        r"""Gets the page of this ExportFullSqlDetailsRequest.

        页码。

        :return: The page of this ExportFullSqlDetailsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ExportFullSqlDetailsRequest.

        页码。

        :param page: The page of this ExportFullSqlDetailsRequest.
        :type page: int
        """
        self._page = page

    @property
    def limit(self):
        r"""Gets the limit of this ExportFullSqlDetailsRequest.

        每页记录数。最大为100。

        :return: The limit of this ExportFullSqlDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ExportFullSqlDetailsRequest.

        每页记录数。最大为100。

        :param limit: The limit of this ExportFullSqlDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ExportFullSqlDetailsRequest.

        请求语言类型。

        :return: The x_language of this ExportFullSqlDetailsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ExportFullSqlDetailsRequest.

        请求语言类型。

        :param x_language: The x_language of this ExportFullSqlDetailsRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ExportFullSqlDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
