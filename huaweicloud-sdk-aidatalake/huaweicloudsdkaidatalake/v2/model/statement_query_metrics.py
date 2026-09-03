# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatementQueryMetrics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_id': 'str',
        'statement_id': 'str',
        'start_time': 'str',
        'duration': 'int',
        'schema_name': 'str',
        'query': 'str',
        'query_plan': 'str',
        'estimate_total_time': 'int',
        'estimate_left_time': 'int',
        'startup_coordinator_duration': 'int',
        'create_session_duration': 'int',
        'enqueue_statement_duration': 'int',
        'queue_duration': 'int',
        'write_resultset_duration': 'int',
        'parse_time': 'int',
        'estimate_memory': 'int',
        'status': 'str',
        'error_info': 'str',
        'dn_time_skew_percent': 'int',
        'dn_max_peak_memory': 'int',
        'dn_average_peak_memory': 'int',
        'dn_spill_skew_percent': 'int',
        'dn_write_disk_total_size': 'int',
        'dn_spill_obs_total_size': 'int',
        'cn_spill_obs_size': 'int',
        'disk_cache_hit_ratio': 'float',
        'obs_io_req_avg_latency': 'int',
        'obs_io_req_latency_gt_1s': 'int',
        'obs_io_req_latency_gt_10s': 'int'
    }

    attribute_map = {
        'session_id': 'session_id',
        'statement_id': 'statement_id',
        'start_time': 'start_time',
        'duration': 'duration',
        'schema_name': 'schema_name',
        'query': 'query',
        'query_plan': 'query_plan',
        'estimate_total_time': 'estimate_total_time',
        'estimate_left_time': 'estimate_left_time',
        'startup_coordinator_duration': 'startup_coordinator_duration',
        'create_session_duration': 'create_session_duration',
        'enqueue_statement_duration': 'enqueue_statement_duration',
        'queue_duration': 'queue_duration',
        'write_resultset_duration': 'write_resultset_duration',
        'parse_time': 'parse_time',
        'estimate_memory': 'estimate_memory',
        'status': 'status',
        'error_info': 'error_info',
        'dn_time_skew_percent': 'dn_time_skew_percent',
        'dn_max_peak_memory': 'dn_max_peak_memory',
        'dn_average_peak_memory': 'dn_average_peak_memory',
        'dn_spill_skew_percent': 'dn_spill_skew_percent',
        'dn_write_disk_total_size': 'dn_write_disk_total_size',
        'dn_spill_obs_total_size': 'dn_spill_obs_total_size',
        'cn_spill_obs_size': 'cn_spill_obs_size',
        'disk_cache_hit_ratio': 'disk_cache_hit_ratio',
        'obs_io_req_avg_latency': 'obs_io_req_avg_latency',
        'obs_io_req_latency_gt_1s': 'obs_io_req_latency_gt_1s',
        'obs_io_req_latency_gt_10s': 'obs_io_req_latency_gt_10s'
    }

    def __init__(self, session_id=None, statement_id=None, start_time=None, duration=None, schema_name=None, query=None, query_plan=None, estimate_total_time=None, estimate_left_time=None, startup_coordinator_duration=None, create_session_duration=None, enqueue_statement_duration=None, queue_duration=None, write_resultset_duration=None, parse_time=None, estimate_memory=None, status=None, error_info=None, dn_time_skew_percent=None, dn_max_peak_memory=None, dn_average_peak_memory=None, dn_spill_skew_percent=None, dn_write_disk_total_size=None, dn_spill_obs_total_size=None, cn_spill_obs_size=None, disk_cache_hit_ratio=None, obs_io_req_avg_latency=None, obs_io_req_latency_gt_1s=None, obs_io_req_latency_gt_10s=None):
        r"""StatementQueryMetrics

        The model defined in huaweicloud sdk

        :param session_id: **参数解释**：会话ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。
        :type session_id: str
        :param statement_id: **参数解释**：语句ID。 **取值范围**：不涉及。
        :type statement_id: str
        :param start_time: **参数解释**：语句开始时间。 **取值范围**：不涉及。
        :type start_time: str
        :param duration: **参数解释**：语句运行时长（单位：ms）。 **取值范围**：不涉及。
        :type duration: int
        :param schema_name: **参数解释**：语句执行时的Schema名称。 **取值范围**：不涉及。
        :type schema_name: str
        :param query: **参数解释**：查询语句。 **取值范围**：不涉及。
        :type query: str
        :param query_plan: **参数解释**：语句计划信息。 **取值范围**：不涉及。
        :type query_plan: str
        :param estimate_total_time: **参数解释**：预计语句运行时长（单位：ms）。 **取值范围**：不涉及。
        :type estimate_total_time: int
        :param estimate_left_time: **参数解释**：预计语句剩余时长（单位：ms）。 **取值范围**：不涉及。
        :type estimate_left_time: int
        :param startup_coordinator_duration: **参数解释**：cn启动时长（单位：ms）。 **取值范围**：不涉及。
        :type startup_coordinator_duration: int
        :param create_session_duration: **参数解释**：创建会话时长（单位：ms）。 **取值范围**：不涉及。
        :type create_session_duration: int
        :param enqueue_statement_duration: **参数解释**：语句加入任务队列时长（单位：ms）。 **取值范围**：不涉及。
        :type enqueue_statement_duration: int
        :param queue_duration: **参数解释**：语句排队时长（单位：ms）。 **取值范围**：不涉及。
        :type queue_duration: int
        :param write_resultset_duration: **参数解释**：语句写结果集时长（单位：ms）。 **取值范围**：不涉及。
        :type write_resultset_duration: int
        :param parse_time: **参数解释**：执行前解析时间（单位：ms）。 **取值范围**：不涉及。
        :type parse_time: int
        :param estimate_memory: **参数解释**：预计使用内存（单位：MB）。 **取值范围**：不涉及。
        :type estimate_memory: int
        :param status: **参数解释**：语句状态，WLM状态。 **取值范围**：不涉及。
        :type status: str
        :param error_info: **参数解释**：语句报错信息。 **取值范围**：不涉及。
        :type error_info: str
        :param dn_time_skew_percent: **参数解释**：DN时长偏斜百分比（单位：%）。 **取值范围**：不涉及。
        :type dn_time_skew_percent: int
        :param dn_max_peak_memory: **参数解释**：DN最大峰值内存（单位：MB）。 **取值范围**：不涉及。
        :type dn_max_peak_memory: int
        :param dn_average_peak_memory: **参数解释**：DN平均峰值内存（单位：MB）。 **取值范围**：不涉及。
        :type dn_average_peak_memory: int
        :param dn_spill_skew_percent: **参数解释**：dn下盘倾斜率（单位：%）。 **取值范围**：不涉及。
        :type dn_spill_skew_percent: int
        :param dn_write_disk_total_size: **参数解释**：dn落盘总大小（单位：MB）。 **取值范围**：不涉及。
        :type dn_write_disk_total_size: int
        :param dn_spill_obs_total_size: **参数解释**：dn溢写OBS总大小（单位：MB）。 **取值范围**：不涉及。
        :type dn_spill_obs_total_size: int
        :param cn_spill_obs_size: **参数解释**：cn溢写OBS大小（单位：MB）。 **取值范围**：不涉及。
        :type cn_spill_obs_size: int
        :param disk_cache_hit_ratio: **参数解释**：磁盘缓存命中率。 **取值范围**：不涉及。
        :type disk_cache_hit_ratio: float
        :param obs_io_req_avg_latency: **参数解释**：OBS IO请求平均延迟（单位：us）。 **取值范围**：不涉及。
        :type obs_io_req_avg_latency: int
        :param obs_io_req_latency_gt_1s: **参数解释**：OBS IO请求延迟大于1秒的次数。 **取值范围**：不涉及。
        :type obs_io_req_latency_gt_1s: int
        :param obs_io_req_latency_gt_10s: **参数解释**：OBS IO请求延迟大于10秒的次数。 **取值范围**：不涉及。
        :type obs_io_req_latency_gt_10s: int
        """
        
        

        self._session_id = None
        self._statement_id = None
        self._start_time = None
        self._duration = None
        self._schema_name = None
        self._query = None
        self._query_plan = None
        self._estimate_total_time = None
        self._estimate_left_time = None
        self._startup_coordinator_duration = None
        self._create_session_duration = None
        self._enqueue_statement_duration = None
        self._queue_duration = None
        self._write_resultset_duration = None
        self._parse_time = None
        self._estimate_memory = None
        self._status = None
        self._error_info = None
        self._dn_time_skew_percent = None
        self._dn_max_peak_memory = None
        self._dn_average_peak_memory = None
        self._dn_spill_skew_percent = None
        self._dn_write_disk_total_size = None
        self._dn_spill_obs_total_size = None
        self._cn_spill_obs_size = None
        self._disk_cache_hit_ratio = None
        self._obs_io_req_avg_latency = None
        self._obs_io_req_latency_gt_1s = None
        self._obs_io_req_latency_gt_10s = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if statement_id is not None:
            self.statement_id = statement_id
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if schema_name is not None:
            self.schema_name = schema_name
        if query is not None:
            self.query = query
        if query_plan is not None:
            self.query_plan = query_plan
        if estimate_total_time is not None:
            self.estimate_total_time = estimate_total_time
        if estimate_left_time is not None:
            self.estimate_left_time = estimate_left_time
        if startup_coordinator_duration is not None:
            self.startup_coordinator_duration = startup_coordinator_duration
        if create_session_duration is not None:
            self.create_session_duration = create_session_duration
        if enqueue_statement_duration is not None:
            self.enqueue_statement_duration = enqueue_statement_duration
        if queue_duration is not None:
            self.queue_duration = queue_duration
        if write_resultset_duration is not None:
            self.write_resultset_duration = write_resultset_duration
        if parse_time is not None:
            self.parse_time = parse_time
        if estimate_memory is not None:
            self.estimate_memory = estimate_memory
        if status is not None:
            self.status = status
        if error_info is not None:
            self.error_info = error_info
        if dn_time_skew_percent is not None:
            self.dn_time_skew_percent = dn_time_skew_percent
        if dn_max_peak_memory is not None:
            self.dn_max_peak_memory = dn_max_peak_memory
        if dn_average_peak_memory is not None:
            self.dn_average_peak_memory = dn_average_peak_memory
        if dn_spill_skew_percent is not None:
            self.dn_spill_skew_percent = dn_spill_skew_percent
        if dn_write_disk_total_size is not None:
            self.dn_write_disk_total_size = dn_write_disk_total_size
        if dn_spill_obs_total_size is not None:
            self.dn_spill_obs_total_size = dn_spill_obs_total_size
        if cn_spill_obs_size is not None:
            self.cn_spill_obs_size = cn_spill_obs_size
        if disk_cache_hit_ratio is not None:
            self.disk_cache_hit_ratio = disk_cache_hit_ratio
        if obs_io_req_avg_latency is not None:
            self.obs_io_req_avg_latency = obs_io_req_avg_latency
        if obs_io_req_latency_gt_1s is not None:
            self.obs_io_req_latency_gt_1s = obs_io_req_latency_gt_1s
        if obs_io_req_latency_gt_10s is not None:
            self.obs_io_req_latency_gt_10s = obs_io_req_latency_gt_10s

    @property
    def session_id(self):
        r"""Gets the session_id of this StatementQueryMetrics.

        **参数解释**：会话ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :return: The session_id of this StatementQueryMetrics.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        r"""Sets the session_id of this StatementQueryMetrics.

        **参数解释**：会话ID。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。

        :param session_id: The session_id of this StatementQueryMetrics.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def statement_id(self):
        r"""Gets the statement_id of this StatementQueryMetrics.

        **参数解释**：语句ID。 **取值范围**：不涉及。

        :return: The statement_id of this StatementQueryMetrics.
        :rtype: str
        """
        return self._statement_id

    @statement_id.setter
    def statement_id(self, statement_id):
        r"""Sets the statement_id of this StatementQueryMetrics.

        **参数解释**：语句ID。 **取值范围**：不涉及。

        :param statement_id: The statement_id of this StatementQueryMetrics.
        :type statement_id: str
        """
        self._statement_id = statement_id

    @property
    def start_time(self):
        r"""Gets the start_time of this StatementQueryMetrics.

        **参数解释**：语句开始时间。 **取值范围**：不涉及。

        :return: The start_time of this StatementQueryMetrics.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this StatementQueryMetrics.

        **参数解释**：语句开始时间。 **取值范围**：不涉及。

        :param start_time: The start_time of this StatementQueryMetrics.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def duration(self):
        r"""Gets the duration of this StatementQueryMetrics.

        **参数解释**：语句运行时长（单位：ms）。 **取值范围**：不涉及。

        :return: The duration of this StatementQueryMetrics.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this StatementQueryMetrics.

        **参数解释**：语句运行时长（单位：ms）。 **取值范围**：不涉及。

        :param duration: The duration of this StatementQueryMetrics.
        :type duration: int
        """
        self._duration = duration

    @property
    def schema_name(self):
        r"""Gets the schema_name of this StatementQueryMetrics.

        **参数解释**：语句执行时的Schema名称。 **取值范围**：不涉及。

        :return: The schema_name of this StatementQueryMetrics.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this StatementQueryMetrics.

        **参数解释**：语句执行时的Schema名称。 **取值范围**：不涉及。

        :param schema_name: The schema_name of this StatementQueryMetrics.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def query(self):
        r"""Gets the query of this StatementQueryMetrics.

        **参数解释**：查询语句。 **取值范围**：不涉及。

        :return: The query of this StatementQueryMetrics.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this StatementQueryMetrics.

        **参数解释**：查询语句。 **取值范围**：不涉及。

        :param query: The query of this StatementQueryMetrics.
        :type query: str
        """
        self._query = query

    @property
    def query_plan(self):
        r"""Gets the query_plan of this StatementQueryMetrics.

        **参数解释**：语句计划信息。 **取值范围**：不涉及。

        :return: The query_plan of this StatementQueryMetrics.
        :rtype: str
        """
        return self._query_plan

    @query_plan.setter
    def query_plan(self, query_plan):
        r"""Sets the query_plan of this StatementQueryMetrics.

        **参数解释**：语句计划信息。 **取值范围**：不涉及。

        :param query_plan: The query_plan of this StatementQueryMetrics.
        :type query_plan: str
        """
        self._query_plan = query_plan

    @property
    def estimate_total_time(self):
        r"""Gets the estimate_total_time of this StatementQueryMetrics.

        **参数解释**：预计语句运行时长（单位：ms）。 **取值范围**：不涉及。

        :return: The estimate_total_time of this StatementQueryMetrics.
        :rtype: int
        """
        return self._estimate_total_time

    @estimate_total_time.setter
    def estimate_total_time(self, estimate_total_time):
        r"""Sets the estimate_total_time of this StatementQueryMetrics.

        **参数解释**：预计语句运行时长（单位：ms）。 **取值范围**：不涉及。

        :param estimate_total_time: The estimate_total_time of this StatementQueryMetrics.
        :type estimate_total_time: int
        """
        self._estimate_total_time = estimate_total_time

    @property
    def estimate_left_time(self):
        r"""Gets the estimate_left_time of this StatementQueryMetrics.

        **参数解释**：预计语句剩余时长（单位：ms）。 **取值范围**：不涉及。

        :return: The estimate_left_time of this StatementQueryMetrics.
        :rtype: int
        """
        return self._estimate_left_time

    @estimate_left_time.setter
    def estimate_left_time(self, estimate_left_time):
        r"""Sets the estimate_left_time of this StatementQueryMetrics.

        **参数解释**：预计语句剩余时长（单位：ms）。 **取值范围**：不涉及。

        :param estimate_left_time: The estimate_left_time of this StatementQueryMetrics.
        :type estimate_left_time: int
        """
        self._estimate_left_time = estimate_left_time

    @property
    def startup_coordinator_duration(self):
        r"""Gets the startup_coordinator_duration of this StatementQueryMetrics.

        **参数解释**：cn启动时长（单位：ms）。 **取值范围**：不涉及。

        :return: The startup_coordinator_duration of this StatementQueryMetrics.
        :rtype: int
        """
        return self._startup_coordinator_duration

    @startup_coordinator_duration.setter
    def startup_coordinator_duration(self, startup_coordinator_duration):
        r"""Sets the startup_coordinator_duration of this StatementQueryMetrics.

        **参数解释**：cn启动时长（单位：ms）。 **取值范围**：不涉及。

        :param startup_coordinator_duration: The startup_coordinator_duration of this StatementQueryMetrics.
        :type startup_coordinator_duration: int
        """
        self._startup_coordinator_duration = startup_coordinator_duration

    @property
    def create_session_duration(self):
        r"""Gets the create_session_duration of this StatementQueryMetrics.

        **参数解释**：创建会话时长（单位：ms）。 **取值范围**：不涉及。

        :return: The create_session_duration of this StatementQueryMetrics.
        :rtype: int
        """
        return self._create_session_duration

    @create_session_duration.setter
    def create_session_duration(self, create_session_duration):
        r"""Sets the create_session_duration of this StatementQueryMetrics.

        **参数解释**：创建会话时长（单位：ms）。 **取值范围**：不涉及。

        :param create_session_duration: The create_session_duration of this StatementQueryMetrics.
        :type create_session_duration: int
        """
        self._create_session_duration = create_session_duration

    @property
    def enqueue_statement_duration(self):
        r"""Gets the enqueue_statement_duration of this StatementQueryMetrics.

        **参数解释**：语句加入任务队列时长（单位：ms）。 **取值范围**：不涉及。

        :return: The enqueue_statement_duration of this StatementQueryMetrics.
        :rtype: int
        """
        return self._enqueue_statement_duration

    @enqueue_statement_duration.setter
    def enqueue_statement_duration(self, enqueue_statement_duration):
        r"""Sets the enqueue_statement_duration of this StatementQueryMetrics.

        **参数解释**：语句加入任务队列时长（单位：ms）。 **取值范围**：不涉及。

        :param enqueue_statement_duration: The enqueue_statement_duration of this StatementQueryMetrics.
        :type enqueue_statement_duration: int
        """
        self._enqueue_statement_duration = enqueue_statement_duration

    @property
    def queue_duration(self):
        r"""Gets the queue_duration of this StatementQueryMetrics.

        **参数解释**：语句排队时长（单位：ms）。 **取值范围**：不涉及。

        :return: The queue_duration of this StatementQueryMetrics.
        :rtype: int
        """
        return self._queue_duration

    @queue_duration.setter
    def queue_duration(self, queue_duration):
        r"""Sets the queue_duration of this StatementQueryMetrics.

        **参数解释**：语句排队时长（单位：ms）。 **取值范围**：不涉及。

        :param queue_duration: The queue_duration of this StatementQueryMetrics.
        :type queue_duration: int
        """
        self._queue_duration = queue_duration

    @property
    def write_resultset_duration(self):
        r"""Gets the write_resultset_duration of this StatementQueryMetrics.

        **参数解释**：语句写结果集时长（单位：ms）。 **取值范围**：不涉及。

        :return: The write_resultset_duration of this StatementQueryMetrics.
        :rtype: int
        """
        return self._write_resultset_duration

    @write_resultset_duration.setter
    def write_resultset_duration(self, write_resultset_duration):
        r"""Sets the write_resultset_duration of this StatementQueryMetrics.

        **参数解释**：语句写结果集时长（单位：ms）。 **取值范围**：不涉及。

        :param write_resultset_duration: The write_resultset_duration of this StatementQueryMetrics.
        :type write_resultset_duration: int
        """
        self._write_resultset_duration = write_resultset_duration

    @property
    def parse_time(self):
        r"""Gets the parse_time of this StatementQueryMetrics.

        **参数解释**：执行前解析时间（单位：ms）。 **取值范围**：不涉及。

        :return: The parse_time of this StatementQueryMetrics.
        :rtype: int
        """
        return self._parse_time

    @parse_time.setter
    def parse_time(self, parse_time):
        r"""Sets the parse_time of this StatementQueryMetrics.

        **参数解释**：执行前解析时间（单位：ms）。 **取值范围**：不涉及。

        :param parse_time: The parse_time of this StatementQueryMetrics.
        :type parse_time: int
        """
        self._parse_time = parse_time

    @property
    def estimate_memory(self):
        r"""Gets the estimate_memory of this StatementQueryMetrics.

        **参数解释**：预计使用内存（单位：MB）。 **取值范围**：不涉及。

        :return: The estimate_memory of this StatementQueryMetrics.
        :rtype: int
        """
        return self._estimate_memory

    @estimate_memory.setter
    def estimate_memory(self, estimate_memory):
        r"""Sets the estimate_memory of this StatementQueryMetrics.

        **参数解释**：预计使用内存（单位：MB）。 **取值范围**：不涉及。

        :param estimate_memory: The estimate_memory of this StatementQueryMetrics.
        :type estimate_memory: int
        """
        self._estimate_memory = estimate_memory

    @property
    def status(self):
        r"""Gets the status of this StatementQueryMetrics.

        **参数解释**：语句状态，WLM状态。 **取值范围**：不涉及。

        :return: The status of this StatementQueryMetrics.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StatementQueryMetrics.

        **参数解释**：语句状态，WLM状态。 **取值范围**：不涉及。

        :param status: The status of this StatementQueryMetrics.
        :type status: str
        """
        self._status = status

    @property
    def error_info(self):
        r"""Gets the error_info of this StatementQueryMetrics.

        **参数解释**：语句报错信息。 **取值范围**：不涉及。

        :return: The error_info of this StatementQueryMetrics.
        :rtype: str
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this StatementQueryMetrics.

        **参数解释**：语句报错信息。 **取值范围**：不涉及。

        :param error_info: The error_info of this StatementQueryMetrics.
        :type error_info: str
        """
        self._error_info = error_info

    @property
    def dn_time_skew_percent(self):
        r"""Gets the dn_time_skew_percent of this StatementQueryMetrics.

        **参数解释**：DN时长偏斜百分比（单位：%）。 **取值范围**：不涉及。

        :return: The dn_time_skew_percent of this StatementQueryMetrics.
        :rtype: int
        """
        return self._dn_time_skew_percent

    @dn_time_skew_percent.setter
    def dn_time_skew_percent(self, dn_time_skew_percent):
        r"""Sets the dn_time_skew_percent of this StatementQueryMetrics.

        **参数解释**：DN时长偏斜百分比（单位：%）。 **取值范围**：不涉及。

        :param dn_time_skew_percent: The dn_time_skew_percent of this StatementQueryMetrics.
        :type dn_time_skew_percent: int
        """
        self._dn_time_skew_percent = dn_time_skew_percent

    @property
    def dn_max_peak_memory(self):
        r"""Gets the dn_max_peak_memory of this StatementQueryMetrics.

        **参数解释**：DN最大峰值内存（单位：MB）。 **取值范围**：不涉及。

        :return: The dn_max_peak_memory of this StatementQueryMetrics.
        :rtype: int
        """
        return self._dn_max_peak_memory

    @dn_max_peak_memory.setter
    def dn_max_peak_memory(self, dn_max_peak_memory):
        r"""Sets the dn_max_peak_memory of this StatementQueryMetrics.

        **参数解释**：DN最大峰值内存（单位：MB）。 **取值范围**：不涉及。

        :param dn_max_peak_memory: The dn_max_peak_memory of this StatementQueryMetrics.
        :type dn_max_peak_memory: int
        """
        self._dn_max_peak_memory = dn_max_peak_memory

    @property
    def dn_average_peak_memory(self):
        r"""Gets the dn_average_peak_memory of this StatementQueryMetrics.

        **参数解释**：DN平均峰值内存（单位：MB）。 **取值范围**：不涉及。

        :return: The dn_average_peak_memory of this StatementQueryMetrics.
        :rtype: int
        """
        return self._dn_average_peak_memory

    @dn_average_peak_memory.setter
    def dn_average_peak_memory(self, dn_average_peak_memory):
        r"""Sets the dn_average_peak_memory of this StatementQueryMetrics.

        **参数解释**：DN平均峰值内存（单位：MB）。 **取值范围**：不涉及。

        :param dn_average_peak_memory: The dn_average_peak_memory of this StatementQueryMetrics.
        :type dn_average_peak_memory: int
        """
        self._dn_average_peak_memory = dn_average_peak_memory

    @property
    def dn_spill_skew_percent(self):
        r"""Gets the dn_spill_skew_percent of this StatementQueryMetrics.

        **参数解释**：dn下盘倾斜率（单位：%）。 **取值范围**：不涉及。

        :return: The dn_spill_skew_percent of this StatementQueryMetrics.
        :rtype: int
        """
        return self._dn_spill_skew_percent

    @dn_spill_skew_percent.setter
    def dn_spill_skew_percent(self, dn_spill_skew_percent):
        r"""Sets the dn_spill_skew_percent of this StatementQueryMetrics.

        **参数解释**：dn下盘倾斜率（单位：%）。 **取值范围**：不涉及。

        :param dn_spill_skew_percent: The dn_spill_skew_percent of this StatementQueryMetrics.
        :type dn_spill_skew_percent: int
        """
        self._dn_spill_skew_percent = dn_spill_skew_percent

    @property
    def dn_write_disk_total_size(self):
        r"""Gets the dn_write_disk_total_size of this StatementQueryMetrics.

        **参数解释**：dn落盘总大小（单位：MB）。 **取值范围**：不涉及。

        :return: The dn_write_disk_total_size of this StatementQueryMetrics.
        :rtype: int
        """
        return self._dn_write_disk_total_size

    @dn_write_disk_total_size.setter
    def dn_write_disk_total_size(self, dn_write_disk_total_size):
        r"""Sets the dn_write_disk_total_size of this StatementQueryMetrics.

        **参数解释**：dn落盘总大小（单位：MB）。 **取值范围**：不涉及。

        :param dn_write_disk_total_size: The dn_write_disk_total_size of this StatementQueryMetrics.
        :type dn_write_disk_total_size: int
        """
        self._dn_write_disk_total_size = dn_write_disk_total_size

    @property
    def dn_spill_obs_total_size(self):
        r"""Gets the dn_spill_obs_total_size of this StatementQueryMetrics.

        **参数解释**：dn溢写OBS总大小（单位：MB）。 **取值范围**：不涉及。

        :return: The dn_spill_obs_total_size of this StatementQueryMetrics.
        :rtype: int
        """
        return self._dn_spill_obs_total_size

    @dn_spill_obs_total_size.setter
    def dn_spill_obs_total_size(self, dn_spill_obs_total_size):
        r"""Sets the dn_spill_obs_total_size of this StatementQueryMetrics.

        **参数解释**：dn溢写OBS总大小（单位：MB）。 **取值范围**：不涉及。

        :param dn_spill_obs_total_size: The dn_spill_obs_total_size of this StatementQueryMetrics.
        :type dn_spill_obs_total_size: int
        """
        self._dn_spill_obs_total_size = dn_spill_obs_total_size

    @property
    def cn_spill_obs_size(self):
        r"""Gets the cn_spill_obs_size of this StatementQueryMetrics.

        **参数解释**：cn溢写OBS大小（单位：MB）。 **取值范围**：不涉及。

        :return: The cn_spill_obs_size of this StatementQueryMetrics.
        :rtype: int
        """
        return self._cn_spill_obs_size

    @cn_spill_obs_size.setter
    def cn_spill_obs_size(self, cn_spill_obs_size):
        r"""Sets the cn_spill_obs_size of this StatementQueryMetrics.

        **参数解释**：cn溢写OBS大小（单位：MB）。 **取值范围**：不涉及。

        :param cn_spill_obs_size: The cn_spill_obs_size of this StatementQueryMetrics.
        :type cn_spill_obs_size: int
        """
        self._cn_spill_obs_size = cn_spill_obs_size

    @property
    def disk_cache_hit_ratio(self):
        r"""Gets the disk_cache_hit_ratio of this StatementQueryMetrics.

        **参数解释**：磁盘缓存命中率。 **取值范围**：不涉及。

        :return: The disk_cache_hit_ratio of this StatementQueryMetrics.
        :rtype: float
        """
        return self._disk_cache_hit_ratio

    @disk_cache_hit_ratio.setter
    def disk_cache_hit_ratio(self, disk_cache_hit_ratio):
        r"""Sets the disk_cache_hit_ratio of this StatementQueryMetrics.

        **参数解释**：磁盘缓存命中率。 **取值范围**：不涉及。

        :param disk_cache_hit_ratio: The disk_cache_hit_ratio of this StatementQueryMetrics.
        :type disk_cache_hit_ratio: float
        """
        self._disk_cache_hit_ratio = disk_cache_hit_ratio

    @property
    def obs_io_req_avg_latency(self):
        r"""Gets the obs_io_req_avg_latency of this StatementQueryMetrics.

        **参数解释**：OBS IO请求平均延迟（单位：us）。 **取值范围**：不涉及。

        :return: The obs_io_req_avg_latency of this StatementQueryMetrics.
        :rtype: int
        """
        return self._obs_io_req_avg_latency

    @obs_io_req_avg_latency.setter
    def obs_io_req_avg_latency(self, obs_io_req_avg_latency):
        r"""Sets the obs_io_req_avg_latency of this StatementQueryMetrics.

        **参数解释**：OBS IO请求平均延迟（单位：us）。 **取值范围**：不涉及。

        :param obs_io_req_avg_latency: The obs_io_req_avg_latency of this StatementQueryMetrics.
        :type obs_io_req_avg_latency: int
        """
        self._obs_io_req_avg_latency = obs_io_req_avg_latency

    @property
    def obs_io_req_latency_gt_1s(self):
        r"""Gets the obs_io_req_latency_gt_1s of this StatementQueryMetrics.

        **参数解释**：OBS IO请求延迟大于1秒的次数。 **取值范围**：不涉及。

        :return: The obs_io_req_latency_gt_1s of this StatementQueryMetrics.
        :rtype: int
        """
        return self._obs_io_req_latency_gt_1s

    @obs_io_req_latency_gt_1s.setter
    def obs_io_req_latency_gt_1s(self, obs_io_req_latency_gt_1s):
        r"""Sets the obs_io_req_latency_gt_1s of this StatementQueryMetrics.

        **参数解释**：OBS IO请求延迟大于1秒的次数。 **取值范围**：不涉及。

        :param obs_io_req_latency_gt_1s: The obs_io_req_latency_gt_1s of this StatementQueryMetrics.
        :type obs_io_req_latency_gt_1s: int
        """
        self._obs_io_req_latency_gt_1s = obs_io_req_latency_gt_1s

    @property
    def obs_io_req_latency_gt_10s(self):
        r"""Gets the obs_io_req_latency_gt_10s of this StatementQueryMetrics.

        **参数解释**：OBS IO请求延迟大于10秒的次数。 **取值范围**：不涉及。

        :return: The obs_io_req_latency_gt_10s of this StatementQueryMetrics.
        :rtype: int
        """
        return self._obs_io_req_latency_gt_10s

    @obs_io_req_latency_gt_10s.setter
    def obs_io_req_latency_gt_10s(self, obs_io_req_latency_gt_10s):
        r"""Sets the obs_io_req_latency_gt_10s of this StatementQueryMetrics.

        **参数解释**：OBS IO请求延迟大于10秒的次数。 **取值范围**：不涉及。

        :param obs_io_req_latency_gt_10s: The obs_io_req_latency_gt_10s of this StatementQueryMetrics.
        :type obs_io_req_latency_gt_10s: int
        """
        self._obs_io_req_latency_gt_10s = obs_io_req_latency_gt_10s

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
        if not isinstance(other, StatementQueryMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
