# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueriesDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virtual_cluster_id': 'int',
        'ctime': 'int',
        'pid': 'str',
        'inst_name': 'str',
        'waiting': 'bool',
        'enqueue': 'str',
        'warning': 'str',
        'query': 'str',
        'lane': 'str',
        'db_name': 'str',
        'priority': 'str',
        'query_id': 'str',
        'query_band': 'str',
        'job_name': 'str',
        'job_inst': 'str',
        'user_name': 'str',
        'application_name': 'str',
        'client_address': 'str',
        'client_hostname': 'str',
        'client_port': 'str',
        'start_time': 'int',
        'block_time': 'int',
        'duration': 'int',
        'estimate_total_time': 'int',
        'estimate_left_time': 'int',
        'resource_pool': 'str',
        'control_group': 'str',
        'min_peak_memory': 'int',
        'max_peak_memory': 'int',
        'average_peak_memory': 'int',
        'memory_skew_percent': 'int',
        'estimate_memory': 'int',
        'spill_info': 'str',
        'min_spill_size': 'int',
        'max_spill_size': 'int',
        'average_spill_size': 'int',
        'spill_skew_percent': 'int',
        'min_dn_time': 'int',
        'max_dn_time': 'int',
        'average_dn_time': 'int',
        'dntime_skew_percent': 'int',
        'min_cpu_time': 'int',
        'max_cpu_time': 'int',
        'total_cpu_time': 'int',
        'cpu_skew_percent': 'int',
        'average_peak_iops': 'int',
        'iops_skew_percent': 'int',
        'max_peak_iops': 'int',
        'min_peak_iops': 'int',
        'query_plan': 'str',
        'query_status': 'str',
        'wlm_status': 'str',
        'wlm_attrib': 'str',
        'system_query': 'bool',
        'backend_start': 'int',
        'elapsed_time': 'int',
        'curr_xact_start': 'int',
        'state_change': 'int',
        'query_start': 'int',
        'query_elapsed_time': 'int'
    }

    attribute_map = {
        'virtual_cluster_id': 'virtual_cluster_id',
        'ctime': 'ctime',
        'pid': 'pid',
        'inst_name': 'inst_name',
        'waiting': 'waiting',
        'enqueue': 'enqueue',
        'warning': 'warning',
        'query': 'query',
        'lane': 'lane',
        'db_name': 'db_name',
        'priority': 'priority',
        'query_id': 'query_id',
        'query_band': 'query_band',
        'job_name': 'job_name',
        'job_inst': 'job_inst',
        'user_name': 'user_name',
        'application_name': 'application_name',
        'client_address': 'client_address',
        'client_hostname': 'client_hostname',
        'client_port': 'client_port',
        'start_time': 'start_time',
        'block_time': 'block_time',
        'duration': 'duration',
        'estimate_total_time': 'estimate_total_time',
        'estimate_left_time': 'estimate_left_time',
        'resource_pool': 'resource_pool',
        'control_group': 'control_group',
        'min_peak_memory': 'min_peak_memory',
        'max_peak_memory': 'max_peak_memory',
        'average_peak_memory': 'average_peak_memory',
        'memory_skew_percent': 'memory_skew_percent',
        'estimate_memory': 'estimate_memory',
        'spill_info': 'spill_info',
        'min_spill_size': 'min_spill_size',
        'max_spill_size': 'max_spill_size',
        'average_spill_size': 'average_spill_size',
        'spill_skew_percent': 'spill_skew_percent',
        'min_dn_time': 'min_dn_time',
        'max_dn_time': 'max_dn_time',
        'average_dn_time': 'average_dn_time',
        'dntime_skew_percent': 'dntime_skew_percent',
        'min_cpu_time': 'min_cpu_time',
        'max_cpu_time': 'max_cpu_time',
        'total_cpu_time': 'total_cpu_time',
        'cpu_skew_percent': 'cpu_skew_percent',
        'average_peak_iops': 'average_peak_iops',
        'iops_skew_percent': 'iops_skew_percent',
        'max_peak_iops': 'max_peak_iops',
        'min_peak_iops': 'min_peak_iops',
        'query_plan': 'query_plan',
        'query_status': 'query_status',
        'wlm_status': 'wlm_status',
        'wlm_attrib': 'wlm_attrib',
        'system_query': 'system_query',
        'backend_start': 'backend_start',
        'elapsed_time': 'elapsed_time',
        'curr_xact_start': 'curr_xact_start',
        'state_change': 'state_change',
        'query_start': 'query_start',
        'query_elapsed_time': 'query_elapsed_time'
    }

    def __init__(self, virtual_cluster_id=None, ctime=None, pid=None, inst_name=None, waiting=None, enqueue=None, warning=None, query=None, lane=None, db_name=None, priority=None, query_id=None, query_band=None, job_name=None, job_inst=None, user_name=None, application_name=None, client_address=None, client_hostname=None, client_port=None, start_time=None, block_time=None, duration=None, estimate_total_time=None, estimate_left_time=None, resource_pool=None, control_group=None, min_peak_memory=None, max_peak_memory=None, average_peak_memory=None, memory_skew_percent=None, estimate_memory=None, spill_info=None, min_spill_size=None, max_spill_size=None, average_spill_size=None, spill_skew_percent=None, min_dn_time=None, max_dn_time=None, average_dn_time=None, dntime_skew_percent=None, min_cpu_time=None, max_cpu_time=None, total_cpu_time=None, cpu_skew_percent=None, average_peak_iops=None, iops_skew_percent=None, max_peak_iops=None, min_peak_iops=None, query_plan=None, query_status=None, wlm_status=None, wlm_attrib=None, system_query=None, backend_start=None, elapsed_time=None, curr_xact_start=None, state_change=None, query_start=None, query_elapsed_time=None):
        r"""ListQueriesDto

        The model defined in huaweicloud sdk

        :param virtual_cluster_id: **参数解释**： 虚拟集群ID。 **取值范围**： 不涉及。
        :type virtual_cluster_id: int
        :param ctime: **参数解释**： 采集时间。 **取值范围**： 不涉及。
        :type ctime: int
        :param pid: **参数解释**： 会话ID。 **取值范围**： 不涉及。
        :type pid: str
        :param inst_name: **参数解释**： 实例名称。 **取值范围**： 不涉及。
        :type inst_name: str
        :param waiting: **参数解释**： 如果后台当前正等待锁则为true。 **取值范围**： 不涉及。
        :type waiting: bool
        :param enqueue: **参数解释**： 资源状态。 **取值范围**： 不涉及。
        :type enqueue: str
        :param warning: **参数解释**： 主要显示如下几类告警信息以及sql自诊断调优相关告警。 **取值范围**： 不涉及。
        :type warning: str
        :param query: **参数解释**： 查询语句。 **取值范围**： 不涉及。
        :type query: str
        :param lane: **参数解释**： 快慢车道。 **取值范围**： fast：快车道。 slow：慢车道。
        :type lane: str
        :param db_name: **参数解释**： 数据库名称。 **取值范围**： 不涉及。
        :type db_name: str
        :param priority: **参数解释**： 任务在资源池中的优先级。 **取值范围**： 1：最高。 2：高。 4：中。 8：低。
        :type priority: str
        :param query_id: **参数解释**： 语句执行使用的内部查询ID。 **取值范围**： 不涉及。
        :type query_id: str
        :param query_band: **参数解释**： 用于标示作业类型，可通过guc参数query_band进行设置，默认为空字符串。 **取值范围**： 不涉及。
        :type query_band: str
        :param job_name: **参数解释**： 该值是从query_band的字段中取出来的，位置0。 **取值范围**： 不涉及。
        :type job_name: str
        :param job_inst: **参数解释**： 该值是从query_band的字段中取出来的，位置1。 **取值范围**： 不涉及。
        :type job_inst: str
        :param user_name: **参数解释**： 连接到后端的用户名。 **取值范围**： 不涉及。
        :type user_name: str
        :param application_name: **参数解释**： 连接到后端的应用名。 **取值范围**： 不涉及。
        :type application_name: str
        :param client_address: **参数解释**： 连接到后端的客户端的IP地址。 **取值范围**： 不涉及。
        :type client_address: str
        :param client_hostname: **参数解释**： 客户端的主机名。 **取值范围**： 不涉及。
        :type client_hostname: str
        :param client_port: **参数解释**： 客户端用于与后端通讯的tcp端口号。 **取值范围**： 不涉及。
        :type client_port: str
        :param start_time: **参数解释**： 语句执行的开始时间。 **取值范围**： 不涉及。
        :type start_time: int
        :param block_time: **参数解释**： 语句执行前的阻塞时间，单位ms。 **取值范围**： 不涉及。
        :type block_time: int
        :param duration: **参数解释**： 语句已经执行的时间，单位ms。 **取值范围**： 不涉及。
        :type duration: int
        :param estimate_total_time: **参数解释**： 语句执行预估总时间，单位ms。 **取值范围**： 不涉及。
        :type estimate_total_time: int
        :param estimate_left_time: **参数解释**： 语句执行预估剩余时间，单位ms。 **取值范围**： 不涉及。
        :type estimate_left_time: int
        :param resource_pool: **参数解释**： 用户使用的资源池。 **取值范围**： 不涉及。
        :type resource_pool: str
        :param control_group: **参数解释**： 语句所使用的cgroup。 **取值范围**： 不涉及。
        :type control_group: str
        :param min_peak_memory: **参数解释**： 语句在所有dn上的最小内存峰值，单位mb。 **取值范围**： 不涉及。
        :type min_peak_memory: int
        :param max_peak_memory: **参数解释**： 语句在所有dn上的最大内存峰值，单位mb。 **取值范围**： 不涉及。
        :type max_peak_memory: int
        :param average_peak_memory: **参数解释**： 语句执行过程中的内存使用平均值，单位mb。 **取值范围**： 不涉及。
        :type average_peak_memory: int
        :param memory_skew_percent: **参数解释**： 语句在各dn间的内存使用倾斜率。 **取值范围**： 不涉及。
        :type memory_skew_percent: int
        :param estimate_memory: **参数解释**： 语句预估使用内存，单位mb。 **取值范围**： 不涉及。
        :type estimate_memory: int
        :param spill_info: **参数解释**： 语句在所有dn上的下盘信息。 **取值范围**： 不涉及。
        :type spill_info: str
        :param min_spill_size: **参数解释**： 若发生下盘，所有dn上下盘的最小数据量 (单位mb) 默认为0。 **取值范围**： 不涉及。
        :type min_spill_size: int
        :param max_spill_size: **参数解释**： 若发生下盘，所有dn上下盘的最大数据量 (单位mb) 默认为0。 **取值范围**： 不涉及。
        :type max_spill_size: int
        :param average_spill_size: **参数解释**： 若发生下盘，所有dn上下盘的平均数据量 (单位mb) 默认为0。 **取值范围**： 不涉及。
        :type average_spill_size: int
        :param spill_skew_percent: **参数解释**： 若发生下盘，dn间下盘倾斜率。 **取值范围**： 不涉及。
        :type spill_skew_percent: int
        :param min_dn_time: **参数解释**： 语句在所有dn上的最小执行时间，单位ms。 **取值范围**： 不涉及。
        :type min_dn_time: int
        :param max_dn_time: **参数解释**： 语句在所有dn上的最大执行时间，单位ms。 **取值范围**： 不涉及。
        :type max_dn_time: int
        :param average_dn_time: **参数解释**： 语句在所有dn上的平均执行时间，单位ms。 **取值范围**： 不涉及。
        :type average_dn_time: int
        :param dntime_skew_percent: **参数解释**： 语句在各dn间的执行时间倾斜率。 **取值范围**： 不涉及。
        :type dntime_skew_percent: int
        :param min_cpu_time: **参数解释**： 语句在所有dn上的最小cpu时间，单位ms。 **取值范围**： 不涉及。
        :type min_cpu_time: int
        :param max_cpu_time: **参数解释**： 语句在所有dn上的最大cpu时间，单位ms。 **取值范围**： 不涉及。
        :type max_cpu_time: int
        :param total_cpu_time: **参数解释**： 语句在所有dn上的cpu总时间，单位ms。 **取值范围**： 不涉及。
        :type total_cpu_time: int
        :param cpu_skew_percent: **参数解释**： 语句在各dn间的cpu时间倾斜率。 **取值范围**： 不涉及。
        :type cpu_skew_percent: int
        :param average_peak_iops: **参数解释**： 语句在所有dn上的每秒平均io峰值（列存单位是次/s，行存单位是万次/s）。 **取值范围**： 不涉及。
        :type average_peak_iops: int
        :param iops_skew_percent: **参数解释**： 语句在dn间的io倾斜率。 **取值范围**： 不涉及。
        :type iops_skew_percent: int
        :param max_peak_iops: **参数解释**： 语句在所有dn上的每秒最大io峰值（列存单位是次/s，行存单位是万次/s）。 **取值范围**： 不涉及。
        :type max_peak_iops: int
        :param min_peak_iops: **参数解释**： 语句在所有dn上的每秒最小io峰值（列存单位是次/s，行存单位是万次/s）。 **取值范围**： 不涉及。
        :type min_peak_iops: int
        :param query_plan: **参数解释**： 查询计划。 **取值范围**： 不涉及。
        :type query_plan: str
        :param query_status: **参数解释**： 当前查询语句的实时运行状态。 **取值范围**： active、idle、idle in transaction、idle in transaction(aborted)、fastpath function call、disabled。
        :type query_status: str
        :param wlm_status: **参数解释**： 当前查询语句在资源池上的运行状态。 **取值范围**： pending：待生效。 running：运行中。 finished：结束。 aborted：终止。 active：正常。 unknown：未知。
        :type wlm_status: str
        :param wlm_attrib: **参数解释**： 语句的属性。 **取值范围**： ordinary：普通。 simple：简单。 complicated：复杂。 internal：内部。
        :type wlm_attrib: str
        :param system_query: **参数解释**： 是否系统查询。 **取值范围**： 不涉及。
        :type system_query: bool
        :param backend_start: **参数解释**： 该过程开始的时间，即当客户端连接服务器时。 **取值范围**： 不涉及。
        :type backend_start: int
        :param elapsed_time: **参数解释**： 到目前为止的执行时间。 **取值范围**： 不涉及。
        :type elapsed_time: int
        :param curr_xact_start: **参数解释**： 启动当前事务的时间，如果没有事务是活跃的，则为null。如果当前查询是首个事务，则这列等同于query_start列。 **取值范围**： 不涉及。
        :type curr_xact_start: int
        :param state_change: **参数解释**： 上次状态改变的时间。 **取值范围**： 不涉及。
        :type state_change: int
        :param query_start: **参数解释**： 语句执行的开始时间。 **取值范围**： 不涉及。
        :type query_start: int
        :param query_elapsed_time: **参数解释**： 语句当前为止的实际执行时间。单位：秒。 **取值范围**： 不涉及。
        :type query_elapsed_time: int
        """
        
        

        self._virtual_cluster_id = None
        self._ctime = None
        self._pid = None
        self._inst_name = None
        self._waiting = None
        self._enqueue = None
        self._warning = None
        self._query = None
        self._lane = None
        self._db_name = None
        self._priority = None
        self._query_id = None
        self._query_band = None
        self._job_name = None
        self._job_inst = None
        self._user_name = None
        self._application_name = None
        self._client_address = None
        self._client_hostname = None
        self._client_port = None
        self._start_time = None
        self._block_time = None
        self._duration = None
        self._estimate_total_time = None
        self._estimate_left_time = None
        self._resource_pool = None
        self._control_group = None
        self._min_peak_memory = None
        self._max_peak_memory = None
        self._average_peak_memory = None
        self._memory_skew_percent = None
        self._estimate_memory = None
        self._spill_info = None
        self._min_spill_size = None
        self._max_spill_size = None
        self._average_spill_size = None
        self._spill_skew_percent = None
        self._min_dn_time = None
        self._max_dn_time = None
        self._average_dn_time = None
        self._dntime_skew_percent = None
        self._min_cpu_time = None
        self._max_cpu_time = None
        self._total_cpu_time = None
        self._cpu_skew_percent = None
        self._average_peak_iops = None
        self._iops_skew_percent = None
        self._max_peak_iops = None
        self._min_peak_iops = None
        self._query_plan = None
        self._query_status = None
        self._wlm_status = None
        self._wlm_attrib = None
        self._system_query = None
        self._backend_start = None
        self._elapsed_time = None
        self._curr_xact_start = None
        self._state_change = None
        self._query_start = None
        self._query_elapsed_time = None
        self.discriminator = None

        if virtual_cluster_id is not None:
            self.virtual_cluster_id = virtual_cluster_id
        if ctime is not None:
            self.ctime = ctime
        if pid is not None:
            self.pid = pid
        if inst_name is not None:
            self.inst_name = inst_name
        if waiting is not None:
            self.waiting = waiting
        if enqueue is not None:
            self.enqueue = enqueue
        if warning is not None:
            self.warning = warning
        if query is not None:
            self.query = query
        if lane is not None:
            self.lane = lane
        if db_name is not None:
            self.db_name = db_name
        if priority is not None:
            self.priority = priority
        if query_id is not None:
            self.query_id = query_id
        if query_band is not None:
            self.query_band = query_band
        if job_name is not None:
            self.job_name = job_name
        if job_inst is not None:
            self.job_inst = job_inst
        if user_name is not None:
            self.user_name = user_name
        if application_name is not None:
            self.application_name = application_name
        if client_address is not None:
            self.client_address = client_address
        if client_hostname is not None:
            self.client_hostname = client_hostname
        if client_port is not None:
            self.client_port = client_port
        if start_time is not None:
            self.start_time = start_time
        if block_time is not None:
            self.block_time = block_time
        if duration is not None:
            self.duration = duration
        if estimate_total_time is not None:
            self.estimate_total_time = estimate_total_time
        if estimate_left_time is not None:
            self.estimate_left_time = estimate_left_time
        if resource_pool is not None:
            self.resource_pool = resource_pool
        if control_group is not None:
            self.control_group = control_group
        if min_peak_memory is not None:
            self.min_peak_memory = min_peak_memory
        if max_peak_memory is not None:
            self.max_peak_memory = max_peak_memory
        if average_peak_memory is not None:
            self.average_peak_memory = average_peak_memory
        if memory_skew_percent is not None:
            self.memory_skew_percent = memory_skew_percent
        if estimate_memory is not None:
            self.estimate_memory = estimate_memory
        if spill_info is not None:
            self.spill_info = spill_info
        if min_spill_size is not None:
            self.min_spill_size = min_spill_size
        if max_spill_size is not None:
            self.max_spill_size = max_spill_size
        if average_spill_size is not None:
            self.average_spill_size = average_spill_size
        if spill_skew_percent is not None:
            self.spill_skew_percent = spill_skew_percent
        if min_dn_time is not None:
            self.min_dn_time = min_dn_time
        if max_dn_time is not None:
            self.max_dn_time = max_dn_time
        if average_dn_time is not None:
            self.average_dn_time = average_dn_time
        if dntime_skew_percent is not None:
            self.dntime_skew_percent = dntime_skew_percent
        if min_cpu_time is not None:
            self.min_cpu_time = min_cpu_time
        if max_cpu_time is not None:
            self.max_cpu_time = max_cpu_time
        if total_cpu_time is not None:
            self.total_cpu_time = total_cpu_time
        if cpu_skew_percent is not None:
            self.cpu_skew_percent = cpu_skew_percent
        if average_peak_iops is not None:
            self.average_peak_iops = average_peak_iops
        if iops_skew_percent is not None:
            self.iops_skew_percent = iops_skew_percent
        if max_peak_iops is not None:
            self.max_peak_iops = max_peak_iops
        if min_peak_iops is not None:
            self.min_peak_iops = min_peak_iops
        if query_plan is not None:
            self.query_plan = query_plan
        if query_status is not None:
            self.query_status = query_status
        if wlm_status is not None:
            self.wlm_status = wlm_status
        if wlm_attrib is not None:
            self.wlm_attrib = wlm_attrib
        if system_query is not None:
            self.system_query = system_query
        if backend_start is not None:
            self.backend_start = backend_start
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if curr_xact_start is not None:
            self.curr_xact_start = curr_xact_start
        if state_change is not None:
            self.state_change = state_change
        if query_start is not None:
            self.query_start = query_start
        if query_elapsed_time is not None:
            self.query_elapsed_time = query_elapsed_time

    @property
    def virtual_cluster_id(self):
        r"""Gets the virtual_cluster_id of this ListQueriesDto.

        **参数解释**： 虚拟集群ID。 **取值范围**： 不涉及。

        :return: The virtual_cluster_id of this ListQueriesDto.
        :rtype: int
        """
        return self._virtual_cluster_id

    @virtual_cluster_id.setter
    def virtual_cluster_id(self, virtual_cluster_id):
        r"""Sets the virtual_cluster_id of this ListQueriesDto.

        **参数解释**： 虚拟集群ID。 **取值范围**： 不涉及。

        :param virtual_cluster_id: The virtual_cluster_id of this ListQueriesDto.
        :type virtual_cluster_id: int
        """
        self._virtual_cluster_id = virtual_cluster_id

    @property
    def ctime(self):
        r"""Gets the ctime of this ListQueriesDto.

        **参数解释**： 采集时间。 **取值范围**： 不涉及。

        :return: The ctime of this ListQueriesDto.
        :rtype: int
        """
        return self._ctime

    @ctime.setter
    def ctime(self, ctime):
        r"""Sets the ctime of this ListQueriesDto.

        **参数解释**： 采集时间。 **取值范围**： 不涉及。

        :param ctime: The ctime of this ListQueriesDto.
        :type ctime: int
        """
        self._ctime = ctime

    @property
    def pid(self):
        r"""Gets the pid of this ListQueriesDto.

        **参数解释**： 会话ID。 **取值范围**： 不涉及。

        :return: The pid of this ListQueriesDto.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this ListQueriesDto.

        **参数解释**： 会话ID。 **取值范围**： 不涉及。

        :param pid: The pid of this ListQueriesDto.
        :type pid: str
        """
        self._pid = pid

    @property
    def inst_name(self):
        r"""Gets the inst_name of this ListQueriesDto.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :return: The inst_name of this ListQueriesDto.
        :rtype: str
        """
        return self._inst_name

    @inst_name.setter
    def inst_name(self, inst_name):
        r"""Sets the inst_name of this ListQueriesDto.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :param inst_name: The inst_name of this ListQueriesDto.
        :type inst_name: str
        """
        self._inst_name = inst_name

    @property
    def waiting(self):
        r"""Gets the waiting of this ListQueriesDto.

        **参数解释**： 如果后台当前正等待锁则为true。 **取值范围**： 不涉及。

        :return: The waiting of this ListQueriesDto.
        :rtype: bool
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        r"""Sets the waiting of this ListQueriesDto.

        **参数解释**： 如果后台当前正等待锁则为true。 **取值范围**： 不涉及。

        :param waiting: The waiting of this ListQueriesDto.
        :type waiting: bool
        """
        self._waiting = waiting

    @property
    def enqueue(self):
        r"""Gets the enqueue of this ListQueriesDto.

        **参数解释**： 资源状态。 **取值范围**： 不涉及。

        :return: The enqueue of this ListQueriesDto.
        :rtype: str
        """
        return self._enqueue

    @enqueue.setter
    def enqueue(self, enqueue):
        r"""Sets the enqueue of this ListQueriesDto.

        **参数解释**： 资源状态。 **取值范围**： 不涉及。

        :param enqueue: The enqueue of this ListQueriesDto.
        :type enqueue: str
        """
        self._enqueue = enqueue

    @property
    def warning(self):
        r"""Gets the warning of this ListQueriesDto.

        **参数解释**： 主要显示如下几类告警信息以及sql自诊断调优相关告警。 **取值范围**： 不涉及。

        :return: The warning of this ListQueriesDto.
        :rtype: str
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        r"""Sets the warning of this ListQueriesDto.

        **参数解释**： 主要显示如下几类告警信息以及sql自诊断调优相关告警。 **取值范围**： 不涉及。

        :param warning: The warning of this ListQueriesDto.
        :type warning: str
        """
        self._warning = warning

    @property
    def query(self):
        r"""Gets the query of this ListQueriesDto.

        **参数解释**： 查询语句。 **取值范围**： 不涉及。

        :return: The query of this ListQueriesDto.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ListQueriesDto.

        **参数解释**： 查询语句。 **取值范围**： 不涉及。

        :param query: The query of this ListQueriesDto.
        :type query: str
        """
        self._query = query

    @property
    def lane(self):
        r"""Gets the lane of this ListQueriesDto.

        **参数解释**： 快慢车道。 **取值范围**： fast：快车道。 slow：慢车道。

        :return: The lane of this ListQueriesDto.
        :rtype: str
        """
        return self._lane

    @lane.setter
    def lane(self, lane):
        r"""Sets the lane of this ListQueriesDto.

        **参数解释**： 快慢车道。 **取值范围**： fast：快车道。 slow：慢车道。

        :param lane: The lane of this ListQueriesDto.
        :type lane: str
        """
        self._lane = lane

    @property
    def db_name(self):
        r"""Gets the db_name of this ListQueriesDto.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :return: The db_name of this ListQueriesDto.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListQueriesDto.

        **参数解释**： 数据库名称。 **取值范围**： 不涉及。

        :param db_name: The db_name of this ListQueriesDto.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def priority(self):
        r"""Gets the priority of this ListQueriesDto.

        **参数解释**： 任务在资源池中的优先级。 **取值范围**： 1：最高。 2：高。 4：中。 8：低。

        :return: The priority of this ListQueriesDto.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ListQueriesDto.

        **参数解释**： 任务在资源池中的优先级。 **取值范围**： 1：最高。 2：高。 4：中。 8：低。

        :param priority: The priority of this ListQueriesDto.
        :type priority: str
        """
        self._priority = priority

    @property
    def query_id(self):
        r"""Gets the query_id of this ListQueriesDto.

        **参数解释**： 语句执行使用的内部查询ID。 **取值范围**： 不涉及。

        :return: The query_id of this ListQueriesDto.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this ListQueriesDto.

        **参数解释**： 语句执行使用的内部查询ID。 **取值范围**： 不涉及。

        :param query_id: The query_id of this ListQueriesDto.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def query_band(self):
        r"""Gets the query_band of this ListQueriesDto.

        **参数解释**： 用于标示作业类型，可通过guc参数query_band进行设置，默认为空字符串。 **取值范围**： 不涉及。

        :return: The query_band of this ListQueriesDto.
        :rtype: str
        """
        return self._query_band

    @query_band.setter
    def query_band(self, query_band):
        r"""Sets the query_band of this ListQueriesDto.

        **参数解释**： 用于标示作业类型，可通过guc参数query_band进行设置，默认为空字符串。 **取值范围**： 不涉及。

        :param query_band: The query_band of this ListQueriesDto.
        :type query_band: str
        """
        self._query_band = query_band

    @property
    def job_name(self):
        r"""Gets the job_name of this ListQueriesDto.

        **参数解释**： 该值是从query_band的字段中取出来的，位置0。 **取值范围**： 不涉及。

        :return: The job_name of this ListQueriesDto.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListQueriesDto.

        **参数解释**： 该值是从query_band的字段中取出来的，位置0。 **取值范围**： 不涉及。

        :param job_name: The job_name of this ListQueriesDto.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_inst(self):
        r"""Gets the job_inst of this ListQueriesDto.

        **参数解释**： 该值是从query_band的字段中取出来的，位置1。 **取值范围**： 不涉及。

        :return: The job_inst of this ListQueriesDto.
        :rtype: str
        """
        return self._job_inst

    @job_inst.setter
    def job_inst(self, job_inst):
        r"""Sets the job_inst of this ListQueriesDto.

        **参数解释**： 该值是从query_band的字段中取出来的，位置1。 **取值范围**： 不涉及。

        :param job_inst: The job_inst of this ListQueriesDto.
        :type job_inst: str
        """
        self._job_inst = job_inst

    @property
    def user_name(self):
        r"""Gets the user_name of this ListQueriesDto.

        **参数解释**： 连接到后端的用户名。 **取值范围**： 不涉及。

        :return: The user_name of this ListQueriesDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListQueriesDto.

        **参数解释**： 连接到后端的用户名。 **取值范围**： 不涉及。

        :param user_name: The user_name of this ListQueriesDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def application_name(self):
        r"""Gets the application_name of this ListQueriesDto.

        **参数解释**： 连接到后端的应用名。 **取值范围**： 不涉及。

        :return: The application_name of this ListQueriesDto.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        r"""Sets the application_name of this ListQueriesDto.

        **参数解释**： 连接到后端的应用名。 **取值范围**： 不涉及。

        :param application_name: The application_name of this ListQueriesDto.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def client_address(self):
        r"""Gets the client_address of this ListQueriesDto.

        **参数解释**： 连接到后端的客户端的IP地址。 **取值范围**： 不涉及。

        :return: The client_address of this ListQueriesDto.
        :rtype: str
        """
        return self._client_address

    @client_address.setter
    def client_address(self, client_address):
        r"""Sets the client_address of this ListQueriesDto.

        **参数解释**： 连接到后端的客户端的IP地址。 **取值范围**： 不涉及。

        :param client_address: The client_address of this ListQueriesDto.
        :type client_address: str
        """
        self._client_address = client_address

    @property
    def client_hostname(self):
        r"""Gets the client_hostname of this ListQueriesDto.

        **参数解释**： 客户端的主机名。 **取值范围**： 不涉及。

        :return: The client_hostname of this ListQueriesDto.
        :rtype: str
        """
        return self._client_hostname

    @client_hostname.setter
    def client_hostname(self, client_hostname):
        r"""Sets the client_hostname of this ListQueriesDto.

        **参数解释**： 客户端的主机名。 **取值范围**： 不涉及。

        :param client_hostname: The client_hostname of this ListQueriesDto.
        :type client_hostname: str
        """
        self._client_hostname = client_hostname

    @property
    def client_port(self):
        r"""Gets the client_port of this ListQueriesDto.

        **参数解释**： 客户端用于与后端通讯的tcp端口号。 **取值范围**： 不涉及。

        :return: The client_port of this ListQueriesDto.
        :rtype: str
        """
        return self._client_port

    @client_port.setter
    def client_port(self, client_port):
        r"""Sets the client_port of this ListQueriesDto.

        **参数解释**： 客户端用于与后端通讯的tcp端口号。 **取值范围**： 不涉及。

        :param client_port: The client_port of this ListQueriesDto.
        :type client_port: str
        """
        self._client_port = client_port

    @property
    def start_time(self):
        r"""Gets the start_time of this ListQueriesDto.

        **参数解释**： 语句执行的开始时间。 **取值范围**： 不涉及。

        :return: The start_time of this ListQueriesDto.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListQueriesDto.

        **参数解释**： 语句执行的开始时间。 **取值范围**： 不涉及。

        :param start_time: The start_time of this ListQueriesDto.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def block_time(self):
        r"""Gets the block_time of this ListQueriesDto.

        **参数解释**： 语句执行前的阻塞时间，单位ms。 **取值范围**： 不涉及。

        :return: The block_time of this ListQueriesDto.
        :rtype: int
        """
        return self._block_time

    @block_time.setter
    def block_time(self, block_time):
        r"""Sets the block_time of this ListQueriesDto.

        **参数解释**： 语句执行前的阻塞时间，单位ms。 **取值范围**： 不涉及。

        :param block_time: The block_time of this ListQueriesDto.
        :type block_time: int
        """
        self._block_time = block_time

    @property
    def duration(self):
        r"""Gets the duration of this ListQueriesDto.

        **参数解释**： 语句已经执行的时间，单位ms。 **取值范围**： 不涉及。

        :return: The duration of this ListQueriesDto.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ListQueriesDto.

        **参数解释**： 语句已经执行的时间，单位ms。 **取值范围**： 不涉及。

        :param duration: The duration of this ListQueriesDto.
        :type duration: int
        """
        self._duration = duration

    @property
    def estimate_total_time(self):
        r"""Gets the estimate_total_time of this ListQueriesDto.

        **参数解释**： 语句执行预估总时间，单位ms。 **取值范围**： 不涉及。

        :return: The estimate_total_time of this ListQueriesDto.
        :rtype: int
        """
        return self._estimate_total_time

    @estimate_total_time.setter
    def estimate_total_time(self, estimate_total_time):
        r"""Sets the estimate_total_time of this ListQueriesDto.

        **参数解释**： 语句执行预估总时间，单位ms。 **取值范围**： 不涉及。

        :param estimate_total_time: The estimate_total_time of this ListQueriesDto.
        :type estimate_total_time: int
        """
        self._estimate_total_time = estimate_total_time

    @property
    def estimate_left_time(self):
        r"""Gets the estimate_left_time of this ListQueriesDto.

        **参数解释**： 语句执行预估剩余时间，单位ms。 **取值范围**： 不涉及。

        :return: The estimate_left_time of this ListQueriesDto.
        :rtype: int
        """
        return self._estimate_left_time

    @estimate_left_time.setter
    def estimate_left_time(self, estimate_left_time):
        r"""Sets the estimate_left_time of this ListQueriesDto.

        **参数解释**： 语句执行预估剩余时间，单位ms。 **取值范围**： 不涉及。

        :param estimate_left_time: The estimate_left_time of this ListQueriesDto.
        :type estimate_left_time: int
        """
        self._estimate_left_time = estimate_left_time

    @property
    def resource_pool(self):
        r"""Gets the resource_pool of this ListQueriesDto.

        **参数解释**： 用户使用的资源池。 **取值范围**： 不涉及。

        :return: The resource_pool of this ListQueriesDto.
        :rtype: str
        """
        return self._resource_pool

    @resource_pool.setter
    def resource_pool(self, resource_pool):
        r"""Sets the resource_pool of this ListQueriesDto.

        **参数解释**： 用户使用的资源池。 **取值范围**： 不涉及。

        :param resource_pool: The resource_pool of this ListQueriesDto.
        :type resource_pool: str
        """
        self._resource_pool = resource_pool

    @property
    def control_group(self):
        r"""Gets the control_group of this ListQueriesDto.

        **参数解释**： 语句所使用的cgroup。 **取值范围**： 不涉及。

        :return: The control_group of this ListQueriesDto.
        :rtype: str
        """
        return self._control_group

    @control_group.setter
    def control_group(self, control_group):
        r"""Sets the control_group of this ListQueriesDto.

        **参数解释**： 语句所使用的cgroup。 **取值范围**： 不涉及。

        :param control_group: The control_group of this ListQueriesDto.
        :type control_group: str
        """
        self._control_group = control_group

    @property
    def min_peak_memory(self):
        r"""Gets the min_peak_memory of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最小内存峰值，单位mb。 **取值范围**： 不涉及。

        :return: The min_peak_memory of this ListQueriesDto.
        :rtype: int
        """
        return self._min_peak_memory

    @min_peak_memory.setter
    def min_peak_memory(self, min_peak_memory):
        r"""Sets the min_peak_memory of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最小内存峰值，单位mb。 **取值范围**： 不涉及。

        :param min_peak_memory: The min_peak_memory of this ListQueriesDto.
        :type min_peak_memory: int
        """
        self._min_peak_memory = min_peak_memory

    @property
    def max_peak_memory(self):
        r"""Gets the max_peak_memory of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最大内存峰值，单位mb。 **取值范围**： 不涉及。

        :return: The max_peak_memory of this ListQueriesDto.
        :rtype: int
        """
        return self._max_peak_memory

    @max_peak_memory.setter
    def max_peak_memory(self, max_peak_memory):
        r"""Sets the max_peak_memory of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最大内存峰值，单位mb。 **取值范围**： 不涉及。

        :param max_peak_memory: The max_peak_memory of this ListQueriesDto.
        :type max_peak_memory: int
        """
        self._max_peak_memory = max_peak_memory

    @property
    def average_peak_memory(self):
        r"""Gets the average_peak_memory of this ListQueriesDto.

        **参数解释**： 语句执行过程中的内存使用平均值，单位mb。 **取值范围**： 不涉及。

        :return: The average_peak_memory of this ListQueriesDto.
        :rtype: int
        """
        return self._average_peak_memory

    @average_peak_memory.setter
    def average_peak_memory(self, average_peak_memory):
        r"""Sets the average_peak_memory of this ListQueriesDto.

        **参数解释**： 语句执行过程中的内存使用平均值，单位mb。 **取值范围**： 不涉及。

        :param average_peak_memory: The average_peak_memory of this ListQueriesDto.
        :type average_peak_memory: int
        """
        self._average_peak_memory = average_peak_memory

    @property
    def memory_skew_percent(self):
        r"""Gets the memory_skew_percent of this ListQueriesDto.

        **参数解释**： 语句在各dn间的内存使用倾斜率。 **取值范围**： 不涉及。

        :return: The memory_skew_percent of this ListQueriesDto.
        :rtype: int
        """
        return self._memory_skew_percent

    @memory_skew_percent.setter
    def memory_skew_percent(self, memory_skew_percent):
        r"""Sets the memory_skew_percent of this ListQueriesDto.

        **参数解释**： 语句在各dn间的内存使用倾斜率。 **取值范围**： 不涉及。

        :param memory_skew_percent: The memory_skew_percent of this ListQueriesDto.
        :type memory_skew_percent: int
        """
        self._memory_skew_percent = memory_skew_percent

    @property
    def estimate_memory(self):
        r"""Gets the estimate_memory of this ListQueriesDto.

        **参数解释**： 语句预估使用内存，单位mb。 **取值范围**： 不涉及。

        :return: The estimate_memory of this ListQueriesDto.
        :rtype: int
        """
        return self._estimate_memory

    @estimate_memory.setter
    def estimate_memory(self, estimate_memory):
        r"""Sets the estimate_memory of this ListQueriesDto.

        **参数解释**： 语句预估使用内存，单位mb。 **取值范围**： 不涉及。

        :param estimate_memory: The estimate_memory of this ListQueriesDto.
        :type estimate_memory: int
        """
        self._estimate_memory = estimate_memory

    @property
    def spill_info(self):
        r"""Gets the spill_info of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的下盘信息。 **取值范围**： 不涉及。

        :return: The spill_info of this ListQueriesDto.
        :rtype: str
        """
        return self._spill_info

    @spill_info.setter
    def spill_info(self, spill_info):
        r"""Sets the spill_info of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的下盘信息。 **取值范围**： 不涉及。

        :param spill_info: The spill_info of this ListQueriesDto.
        :type spill_info: str
        """
        self._spill_info = spill_info

    @property
    def min_spill_size(self):
        r"""Gets the min_spill_size of this ListQueriesDto.

        **参数解释**： 若发生下盘，所有dn上下盘的最小数据量 (单位mb) 默认为0。 **取值范围**： 不涉及。

        :return: The min_spill_size of this ListQueriesDto.
        :rtype: int
        """
        return self._min_spill_size

    @min_spill_size.setter
    def min_spill_size(self, min_spill_size):
        r"""Sets the min_spill_size of this ListQueriesDto.

        **参数解释**： 若发生下盘，所有dn上下盘的最小数据量 (单位mb) 默认为0。 **取值范围**： 不涉及。

        :param min_spill_size: The min_spill_size of this ListQueriesDto.
        :type min_spill_size: int
        """
        self._min_spill_size = min_spill_size

    @property
    def max_spill_size(self):
        r"""Gets the max_spill_size of this ListQueriesDto.

        **参数解释**： 若发生下盘，所有dn上下盘的最大数据量 (单位mb) 默认为0。 **取值范围**： 不涉及。

        :return: The max_spill_size of this ListQueriesDto.
        :rtype: int
        """
        return self._max_spill_size

    @max_spill_size.setter
    def max_spill_size(self, max_spill_size):
        r"""Sets the max_spill_size of this ListQueriesDto.

        **参数解释**： 若发生下盘，所有dn上下盘的最大数据量 (单位mb) 默认为0。 **取值范围**： 不涉及。

        :param max_spill_size: The max_spill_size of this ListQueriesDto.
        :type max_spill_size: int
        """
        self._max_spill_size = max_spill_size

    @property
    def average_spill_size(self):
        r"""Gets the average_spill_size of this ListQueriesDto.

        **参数解释**： 若发生下盘，所有dn上下盘的平均数据量 (单位mb) 默认为0。 **取值范围**： 不涉及。

        :return: The average_spill_size of this ListQueriesDto.
        :rtype: int
        """
        return self._average_spill_size

    @average_spill_size.setter
    def average_spill_size(self, average_spill_size):
        r"""Sets the average_spill_size of this ListQueriesDto.

        **参数解释**： 若发生下盘，所有dn上下盘的平均数据量 (单位mb) 默认为0。 **取值范围**： 不涉及。

        :param average_spill_size: The average_spill_size of this ListQueriesDto.
        :type average_spill_size: int
        """
        self._average_spill_size = average_spill_size

    @property
    def spill_skew_percent(self):
        r"""Gets the spill_skew_percent of this ListQueriesDto.

        **参数解释**： 若发生下盘，dn间下盘倾斜率。 **取值范围**： 不涉及。

        :return: The spill_skew_percent of this ListQueriesDto.
        :rtype: int
        """
        return self._spill_skew_percent

    @spill_skew_percent.setter
    def spill_skew_percent(self, spill_skew_percent):
        r"""Sets the spill_skew_percent of this ListQueriesDto.

        **参数解释**： 若发生下盘，dn间下盘倾斜率。 **取值范围**： 不涉及。

        :param spill_skew_percent: The spill_skew_percent of this ListQueriesDto.
        :type spill_skew_percent: int
        """
        self._spill_skew_percent = spill_skew_percent

    @property
    def min_dn_time(self):
        r"""Gets the min_dn_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最小执行时间，单位ms。 **取值范围**： 不涉及。

        :return: The min_dn_time of this ListQueriesDto.
        :rtype: int
        """
        return self._min_dn_time

    @min_dn_time.setter
    def min_dn_time(self, min_dn_time):
        r"""Sets the min_dn_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最小执行时间，单位ms。 **取值范围**： 不涉及。

        :param min_dn_time: The min_dn_time of this ListQueriesDto.
        :type min_dn_time: int
        """
        self._min_dn_time = min_dn_time

    @property
    def max_dn_time(self):
        r"""Gets the max_dn_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最大执行时间，单位ms。 **取值范围**： 不涉及。

        :return: The max_dn_time of this ListQueriesDto.
        :rtype: int
        """
        return self._max_dn_time

    @max_dn_time.setter
    def max_dn_time(self, max_dn_time):
        r"""Sets the max_dn_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最大执行时间，单位ms。 **取值范围**： 不涉及。

        :param max_dn_time: The max_dn_time of this ListQueriesDto.
        :type max_dn_time: int
        """
        self._max_dn_time = max_dn_time

    @property
    def average_dn_time(self):
        r"""Gets the average_dn_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的平均执行时间，单位ms。 **取值范围**： 不涉及。

        :return: The average_dn_time of this ListQueriesDto.
        :rtype: int
        """
        return self._average_dn_time

    @average_dn_time.setter
    def average_dn_time(self, average_dn_time):
        r"""Sets the average_dn_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的平均执行时间，单位ms。 **取值范围**： 不涉及。

        :param average_dn_time: The average_dn_time of this ListQueriesDto.
        :type average_dn_time: int
        """
        self._average_dn_time = average_dn_time

    @property
    def dntime_skew_percent(self):
        r"""Gets the dntime_skew_percent of this ListQueriesDto.

        **参数解释**： 语句在各dn间的执行时间倾斜率。 **取值范围**： 不涉及。

        :return: The dntime_skew_percent of this ListQueriesDto.
        :rtype: int
        """
        return self._dntime_skew_percent

    @dntime_skew_percent.setter
    def dntime_skew_percent(self, dntime_skew_percent):
        r"""Sets the dntime_skew_percent of this ListQueriesDto.

        **参数解释**： 语句在各dn间的执行时间倾斜率。 **取值范围**： 不涉及。

        :param dntime_skew_percent: The dntime_skew_percent of this ListQueriesDto.
        :type dntime_skew_percent: int
        """
        self._dntime_skew_percent = dntime_skew_percent

    @property
    def min_cpu_time(self):
        r"""Gets the min_cpu_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最小cpu时间，单位ms。 **取值范围**： 不涉及。

        :return: The min_cpu_time of this ListQueriesDto.
        :rtype: int
        """
        return self._min_cpu_time

    @min_cpu_time.setter
    def min_cpu_time(self, min_cpu_time):
        r"""Sets the min_cpu_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最小cpu时间，单位ms。 **取值范围**： 不涉及。

        :param min_cpu_time: The min_cpu_time of this ListQueriesDto.
        :type min_cpu_time: int
        """
        self._min_cpu_time = min_cpu_time

    @property
    def max_cpu_time(self):
        r"""Gets the max_cpu_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最大cpu时间，单位ms。 **取值范围**： 不涉及。

        :return: The max_cpu_time of this ListQueriesDto.
        :rtype: int
        """
        return self._max_cpu_time

    @max_cpu_time.setter
    def max_cpu_time(self, max_cpu_time):
        r"""Sets the max_cpu_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的最大cpu时间，单位ms。 **取值范围**： 不涉及。

        :param max_cpu_time: The max_cpu_time of this ListQueriesDto.
        :type max_cpu_time: int
        """
        self._max_cpu_time = max_cpu_time

    @property
    def total_cpu_time(self):
        r"""Gets the total_cpu_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的cpu总时间，单位ms。 **取值范围**： 不涉及。

        :return: The total_cpu_time of this ListQueriesDto.
        :rtype: int
        """
        return self._total_cpu_time

    @total_cpu_time.setter
    def total_cpu_time(self, total_cpu_time):
        r"""Sets the total_cpu_time of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的cpu总时间，单位ms。 **取值范围**： 不涉及。

        :param total_cpu_time: The total_cpu_time of this ListQueriesDto.
        :type total_cpu_time: int
        """
        self._total_cpu_time = total_cpu_time

    @property
    def cpu_skew_percent(self):
        r"""Gets the cpu_skew_percent of this ListQueriesDto.

        **参数解释**： 语句在各dn间的cpu时间倾斜率。 **取值范围**： 不涉及。

        :return: The cpu_skew_percent of this ListQueriesDto.
        :rtype: int
        """
        return self._cpu_skew_percent

    @cpu_skew_percent.setter
    def cpu_skew_percent(self, cpu_skew_percent):
        r"""Sets the cpu_skew_percent of this ListQueriesDto.

        **参数解释**： 语句在各dn间的cpu时间倾斜率。 **取值范围**： 不涉及。

        :param cpu_skew_percent: The cpu_skew_percent of this ListQueriesDto.
        :type cpu_skew_percent: int
        """
        self._cpu_skew_percent = cpu_skew_percent

    @property
    def average_peak_iops(self):
        r"""Gets the average_peak_iops of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的每秒平均io峰值（列存单位是次/s，行存单位是万次/s）。 **取值范围**： 不涉及。

        :return: The average_peak_iops of this ListQueriesDto.
        :rtype: int
        """
        return self._average_peak_iops

    @average_peak_iops.setter
    def average_peak_iops(self, average_peak_iops):
        r"""Sets the average_peak_iops of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的每秒平均io峰值（列存单位是次/s，行存单位是万次/s）。 **取值范围**： 不涉及。

        :param average_peak_iops: The average_peak_iops of this ListQueriesDto.
        :type average_peak_iops: int
        """
        self._average_peak_iops = average_peak_iops

    @property
    def iops_skew_percent(self):
        r"""Gets the iops_skew_percent of this ListQueriesDto.

        **参数解释**： 语句在dn间的io倾斜率。 **取值范围**： 不涉及。

        :return: The iops_skew_percent of this ListQueriesDto.
        :rtype: int
        """
        return self._iops_skew_percent

    @iops_skew_percent.setter
    def iops_skew_percent(self, iops_skew_percent):
        r"""Sets the iops_skew_percent of this ListQueriesDto.

        **参数解释**： 语句在dn间的io倾斜率。 **取值范围**： 不涉及。

        :param iops_skew_percent: The iops_skew_percent of this ListQueriesDto.
        :type iops_skew_percent: int
        """
        self._iops_skew_percent = iops_skew_percent

    @property
    def max_peak_iops(self):
        r"""Gets the max_peak_iops of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的每秒最大io峰值（列存单位是次/s，行存单位是万次/s）。 **取值范围**： 不涉及。

        :return: The max_peak_iops of this ListQueriesDto.
        :rtype: int
        """
        return self._max_peak_iops

    @max_peak_iops.setter
    def max_peak_iops(self, max_peak_iops):
        r"""Sets the max_peak_iops of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的每秒最大io峰值（列存单位是次/s，行存单位是万次/s）。 **取值范围**： 不涉及。

        :param max_peak_iops: The max_peak_iops of this ListQueriesDto.
        :type max_peak_iops: int
        """
        self._max_peak_iops = max_peak_iops

    @property
    def min_peak_iops(self):
        r"""Gets the min_peak_iops of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的每秒最小io峰值（列存单位是次/s，行存单位是万次/s）。 **取值范围**： 不涉及。

        :return: The min_peak_iops of this ListQueriesDto.
        :rtype: int
        """
        return self._min_peak_iops

    @min_peak_iops.setter
    def min_peak_iops(self, min_peak_iops):
        r"""Sets the min_peak_iops of this ListQueriesDto.

        **参数解释**： 语句在所有dn上的每秒最小io峰值（列存单位是次/s，行存单位是万次/s）。 **取值范围**： 不涉及。

        :param min_peak_iops: The min_peak_iops of this ListQueriesDto.
        :type min_peak_iops: int
        """
        self._min_peak_iops = min_peak_iops

    @property
    def query_plan(self):
        r"""Gets the query_plan of this ListQueriesDto.

        **参数解释**： 查询计划。 **取值范围**： 不涉及。

        :return: The query_plan of this ListQueriesDto.
        :rtype: str
        """
        return self._query_plan

    @query_plan.setter
    def query_plan(self, query_plan):
        r"""Sets the query_plan of this ListQueriesDto.

        **参数解释**： 查询计划。 **取值范围**： 不涉及。

        :param query_plan: The query_plan of this ListQueriesDto.
        :type query_plan: str
        """
        self._query_plan = query_plan

    @property
    def query_status(self):
        r"""Gets the query_status of this ListQueriesDto.

        **参数解释**： 当前查询语句的实时运行状态。 **取值范围**： active、idle、idle in transaction、idle in transaction(aborted)、fastpath function call、disabled。

        :return: The query_status of this ListQueriesDto.
        :rtype: str
        """
        return self._query_status

    @query_status.setter
    def query_status(self, query_status):
        r"""Sets the query_status of this ListQueriesDto.

        **参数解释**： 当前查询语句的实时运行状态。 **取值范围**： active、idle、idle in transaction、idle in transaction(aborted)、fastpath function call、disabled。

        :param query_status: The query_status of this ListQueriesDto.
        :type query_status: str
        """
        self._query_status = query_status

    @property
    def wlm_status(self):
        r"""Gets the wlm_status of this ListQueriesDto.

        **参数解释**： 当前查询语句在资源池上的运行状态。 **取值范围**： pending：待生效。 running：运行中。 finished：结束。 aborted：终止。 active：正常。 unknown：未知。

        :return: The wlm_status of this ListQueriesDto.
        :rtype: str
        """
        return self._wlm_status

    @wlm_status.setter
    def wlm_status(self, wlm_status):
        r"""Sets the wlm_status of this ListQueriesDto.

        **参数解释**： 当前查询语句在资源池上的运行状态。 **取值范围**： pending：待生效。 running：运行中。 finished：结束。 aborted：终止。 active：正常。 unknown：未知。

        :param wlm_status: The wlm_status of this ListQueriesDto.
        :type wlm_status: str
        """
        self._wlm_status = wlm_status

    @property
    def wlm_attrib(self):
        r"""Gets the wlm_attrib of this ListQueriesDto.

        **参数解释**： 语句的属性。 **取值范围**： ordinary：普通。 simple：简单。 complicated：复杂。 internal：内部。

        :return: The wlm_attrib of this ListQueriesDto.
        :rtype: str
        """
        return self._wlm_attrib

    @wlm_attrib.setter
    def wlm_attrib(self, wlm_attrib):
        r"""Sets the wlm_attrib of this ListQueriesDto.

        **参数解释**： 语句的属性。 **取值范围**： ordinary：普通。 simple：简单。 complicated：复杂。 internal：内部。

        :param wlm_attrib: The wlm_attrib of this ListQueriesDto.
        :type wlm_attrib: str
        """
        self._wlm_attrib = wlm_attrib

    @property
    def system_query(self):
        r"""Gets the system_query of this ListQueriesDto.

        **参数解释**： 是否系统查询。 **取值范围**： 不涉及。

        :return: The system_query of this ListQueriesDto.
        :rtype: bool
        """
        return self._system_query

    @system_query.setter
    def system_query(self, system_query):
        r"""Sets the system_query of this ListQueriesDto.

        **参数解释**： 是否系统查询。 **取值范围**： 不涉及。

        :param system_query: The system_query of this ListQueriesDto.
        :type system_query: bool
        """
        self._system_query = system_query

    @property
    def backend_start(self):
        r"""Gets the backend_start of this ListQueriesDto.

        **参数解释**： 该过程开始的时间，即当客户端连接服务器时。 **取值范围**： 不涉及。

        :return: The backend_start of this ListQueriesDto.
        :rtype: int
        """
        return self._backend_start

    @backend_start.setter
    def backend_start(self, backend_start):
        r"""Sets the backend_start of this ListQueriesDto.

        **参数解释**： 该过程开始的时间，即当客户端连接服务器时。 **取值范围**： 不涉及。

        :param backend_start: The backend_start of this ListQueriesDto.
        :type backend_start: int
        """
        self._backend_start = backend_start

    @property
    def elapsed_time(self):
        r"""Gets the elapsed_time of this ListQueriesDto.

        **参数解释**： 到目前为止的执行时间。 **取值范围**： 不涉及。

        :return: The elapsed_time of this ListQueriesDto.
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        r"""Sets the elapsed_time of this ListQueriesDto.

        **参数解释**： 到目前为止的执行时间。 **取值范围**： 不涉及。

        :param elapsed_time: The elapsed_time of this ListQueriesDto.
        :type elapsed_time: int
        """
        self._elapsed_time = elapsed_time

    @property
    def curr_xact_start(self):
        r"""Gets the curr_xact_start of this ListQueriesDto.

        **参数解释**： 启动当前事务的时间，如果没有事务是活跃的，则为null。如果当前查询是首个事务，则这列等同于query_start列。 **取值范围**： 不涉及。

        :return: The curr_xact_start of this ListQueriesDto.
        :rtype: int
        """
        return self._curr_xact_start

    @curr_xact_start.setter
    def curr_xact_start(self, curr_xact_start):
        r"""Sets the curr_xact_start of this ListQueriesDto.

        **参数解释**： 启动当前事务的时间，如果没有事务是活跃的，则为null。如果当前查询是首个事务，则这列等同于query_start列。 **取值范围**： 不涉及。

        :param curr_xact_start: The curr_xact_start of this ListQueriesDto.
        :type curr_xact_start: int
        """
        self._curr_xact_start = curr_xact_start

    @property
    def state_change(self):
        r"""Gets the state_change of this ListQueriesDto.

        **参数解释**： 上次状态改变的时间。 **取值范围**： 不涉及。

        :return: The state_change of this ListQueriesDto.
        :rtype: int
        """
        return self._state_change

    @state_change.setter
    def state_change(self, state_change):
        r"""Sets the state_change of this ListQueriesDto.

        **参数解释**： 上次状态改变的时间。 **取值范围**： 不涉及。

        :param state_change: The state_change of this ListQueriesDto.
        :type state_change: int
        """
        self._state_change = state_change

    @property
    def query_start(self):
        r"""Gets the query_start of this ListQueriesDto.

        **参数解释**： 语句执行的开始时间。 **取值范围**： 不涉及。

        :return: The query_start of this ListQueriesDto.
        :rtype: int
        """
        return self._query_start

    @query_start.setter
    def query_start(self, query_start):
        r"""Sets the query_start of this ListQueriesDto.

        **参数解释**： 语句执行的开始时间。 **取值范围**： 不涉及。

        :param query_start: The query_start of this ListQueriesDto.
        :type query_start: int
        """
        self._query_start = query_start

    @property
    def query_elapsed_time(self):
        r"""Gets the query_elapsed_time of this ListQueriesDto.

        **参数解释**： 语句当前为止的实际执行时间。单位：秒。 **取值范围**： 不涉及。

        :return: The query_elapsed_time of this ListQueriesDto.
        :rtype: int
        """
        return self._query_elapsed_time

    @query_elapsed_time.setter
    def query_elapsed_time(self, query_elapsed_time):
        r"""Sets the query_elapsed_time of this ListQueriesDto.

        **参数解释**： 语句当前为止的实际执行时间。单位：秒。 **取值范围**： 不涉及。

        :param query_elapsed_time: The query_elapsed_time of this ListQueriesDto.
        :type query_elapsed_time: int
        """
        self._query_elapsed_time = query_elapsed_time

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
        if not isinstance(other, ListQueriesDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
