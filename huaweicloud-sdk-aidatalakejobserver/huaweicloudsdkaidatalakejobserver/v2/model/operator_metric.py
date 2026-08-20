# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperatorMetric:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query_id': 'int',
        'plan_node_id': 'int',
        'plan_node_name': 'str',
        'start_time': 'datetime',
        'duration': 'int',
        'status': 'str',
        'query_dop': 'int',
        'estimated_rows': 'int',
        'tuple_processed': 'int',
        'min_peak_memory': 'int',
        'max_peak_memory': 'int',
        'average_peak_memory': 'int',
        'memory_skew_percent': 'int',
        'min_spill_size': 'int',
        'max_spill_size': 'int',
        'average_spill_size': 'int',
        'spill_skew_percent': 'str',
        'loops': 'int',
        'progress': 'str',
        'total_read_size': 'int',
        'total_write_size': 'int',
        'sub_operator_metrics': 'list[OperatorMetric]'
    }

    attribute_map = {
        'query_id': 'query_id',
        'plan_node_id': 'plan_node_id',
        'plan_node_name': 'plan_node_name',
        'start_time': 'start_time',
        'duration': 'duration',
        'status': 'status',
        'query_dop': 'query_dop',
        'estimated_rows': 'estimated_rows',
        'tuple_processed': 'tuple_processed',
        'min_peak_memory': 'min_peak_memory',
        'max_peak_memory': 'max_peak_memory',
        'average_peak_memory': 'average_peak_memory',
        'memory_skew_percent': 'memory_skew_percent',
        'min_spill_size': 'min_spill_size',
        'max_spill_size': 'max_spill_size',
        'average_spill_size': 'average_spill_size',
        'spill_skew_percent': 'spill_skew_percent',
        'loops': 'loops',
        'progress': 'progress',
        'total_read_size': 'total_read_size',
        'total_write_size': 'total_write_size',
        'sub_operator_metrics': 'sub_operator_metrics'
    }

    def __init__(self, query_id=None, plan_node_id=None, plan_node_name=None, start_time=None, duration=None, status=None, query_dop=None, estimated_rows=None, tuple_processed=None, min_peak_memory=None, max_peak_memory=None, average_peak_memory=None, memory_skew_percent=None, min_spill_size=None, max_spill_size=None, average_spill_size=None, spill_skew_percent=None, loops=None, progress=None, total_read_size=None, total_write_size=None, sub_operator_metrics=None):
        r"""OperatorMetric

        The model defined in huaweicloud sdk

        :param query_id: **参数解释**：查询ID。 **取值范围**：1~9223372036854775807。
        :type query_id: int
        :param plan_node_id: **参数解释**：节点ID。 **取值范围**：1~2147483647。
        :type plan_node_id: int
        :param plan_node_name: **参数解释**：节点名称。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。
        :type plan_node_name: str
        :param start_time: **参数解释**：开始时间，格式为：YYYY-MM-DD HH:MM:SS。 **取值范围**：时间范围：1000-01-01 00:00:00/9999-12-31 23:59:59。
        :type start_time: datetime
        :param duration: **参数解释**：执行时长。 **取值范围**：1~9223372036854775807。
        :type duration: int
        :param status: **参数解释**：算子当前执行状态。 **取值范围**：   - init：初始化。   - waiting：等待中。   - finished：已结束。   - running：运行中。
        :type status: str
        :param query_dop: **参数解释**：查询的并行度。 **取值范围**：1~2147483647。
        :type query_dop: int
        :param estimated_rows: **参数解释**：预估的行数。 **取值范围**：1~9223372036854775807。
        :type estimated_rows: int
        :param tuple_processed: **参数解释**：当前已经处理完成的行数。 **取值范围**：1~9223372036854775807。
        :type tuple_processed: int
        :param min_peak_memory: **参数解释**：内存使用的最小峰值。 **取值范围**：1~2147483647。
        :type min_peak_memory: int
        :param max_peak_memory: **参数解释**：内存使用的最大峰值。 **取值范围**：1~2147483647。
        :type max_peak_memory: int
        :param average_peak_memory: **参数解释**：内存使用的平均峰值。 **取值范围**：1~2147483647。
        :type average_peak_memory: int
        :param memory_skew_percent: **参数解释**：内存使用倾斜百分比。 **取值范围**：1~2147483647。
        :type memory_skew_percent: int
        :param min_spill_size: **参数解释**：下盘的最小数据量。 **取值范围**：1~2147483647。
        :type min_spill_size: int
        :param max_spill_size: **参数解释**：下盘的最大数据量。 **取值范围**：1~2147483647。
        :type max_spill_size: int
        :param average_spill_size: **参数解释**：下盘的平均数据量。 **取值范围**：1~2147483647。
        :type average_spill_size: int
        :param spill_skew_percent: **参数解释**：下盘数据的倾斜百分比。 **取值范围**：不涉及。
        :type spill_skew_percent: str
        :param loops: **参数解释**：算子执行迭代次数。 **取值范围**：1~2147483647。
        :type loops: int
        :param progress: **参数解释**：执行进度百分比。 **取值范围**：不涉及。
        :type progress: str
        :param total_read_size: **参数解释**：所有节点读取的总数据量。 **取值范围**：1~9223372036854775807。
        :type total_read_size: int
        :param total_write_size: **参数解释**：所有节点写入的总数据量。 **取值范围**：1~9223372036854775807。
        :type total_write_size: int
        :param sub_operator_metrics: **参数解释**：子节点。 **取值范围**：不涉及。
        :type sub_operator_metrics: list[:class:`huaweicloudsdkaidatalakejobserver.v2.OperatorMetric`]
        """
        
        

        self._query_id = None
        self._plan_node_id = None
        self._plan_node_name = None
        self._start_time = None
        self._duration = None
        self._status = None
        self._query_dop = None
        self._estimated_rows = None
        self._tuple_processed = None
        self._min_peak_memory = None
        self._max_peak_memory = None
        self._average_peak_memory = None
        self._memory_skew_percent = None
        self._min_spill_size = None
        self._max_spill_size = None
        self._average_spill_size = None
        self._spill_skew_percent = None
        self._loops = None
        self._progress = None
        self._total_read_size = None
        self._total_write_size = None
        self._sub_operator_metrics = None
        self.discriminator = None

        if query_id is not None:
            self.query_id = query_id
        if plan_node_id is not None:
            self.plan_node_id = plan_node_id
        if plan_node_name is not None:
            self.plan_node_name = plan_node_name
        if start_time is not None:
            self.start_time = start_time
        if duration is not None:
            self.duration = duration
        if status is not None:
            self.status = status
        if query_dop is not None:
            self.query_dop = query_dop
        if estimated_rows is not None:
            self.estimated_rows = estimated_rows
        if tuple_processed is not None:
            self.tuple_processed = tuple_processed
        if min_peak_memory is not None:
            self.min_peak_memory = min_peak_memory
        if max_peak_memory is not None:
            self.max_peak_memory = max_peak_memory
        if average_peak_memory is not None:
            self.average_peak_memory = average_peak_memory
        if memory_skew_percent is not None:
            self.memory_skew_percent = memory_skew_percent
        if min_spill_size is not None:
            self.min_spill_size = min_spill_size
        if max_spill_size is not None:
            self.max_spill_size = max_spill_size
        if average_spill_size is not None:
            self.average_spill_size = average_spill_size
        if spill_skew_percent is not None:
            self.spill_skew_percent = spill_skew_percent
        if loops is not None:
            self.loops = loops
        if progress is not None:
            self.progress = progress
        if total_read_size is not None:
            self.total_read_size = total_read_size
        if total_write_size is not None:
            self.total_write_size = total_write_size
        if sub_operator_metrics is not None:
            self.sub_operator_metrics = sub_operator_metrics

    @property
    def query_id(self):
        r"""Gets the query_id of this OperatorMetric.

        **参数解释**：查询ID。 **取值范围**：1~9223372036854775807。

        :return: The query_id of this OperatorMetric.
        :rtype: int
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        r"""Sets the query_id of this OperatorMetric.

        **参数解释**：查询ID。 **取值范围**：1~9223372036854775807。

        :param query_id: The query_id of this OperatorMetric.
        :type query_id: int
        """
        self._query_id = query_id

    @property
    def plan_node_id(self):
        r"""Gets the plan_node_id of this OperatorMetric.

        **参数解释**：节点ID。 **取值范围**：1~2147483647。

        :return: The plan_node_id of this OperatorMetric.
        :rtype: int
        """
        return self._plan_node_id

    @plan_node_id.setter
    def plan_node_id(self, plan_node_id):
        r"""Sets the plan_node_id of this OperatorMetric.

        **参数解释**：节点ID。 **取值范围**：1~2147483647。

        :param plan_node_id: The plan_node_id of this OperatorMetric.
        :type plan_node_id: int
        """
        self._plan_node_id = plan_node_id

    @property
    def plan_node_name(self):
        r"""Gets the plan_node_name of this OperatorMetric.

        **参数解释**：节点名称。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。

        :return: The plan_node_name of this OperatorMetric.
        :rtype: str
        """
        return self._plan_node_name

    @plan_node_name.setter
    def plan_node_name(self, plan_node_name):
        r"""Sets the plan_node_name of this OperatorMetric.

        **参数解释**：节点名称。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。

        :param plan_node_name: The plan_node_name of this OperatorMetric.
        :type plan_node_name: str
        """
        self._plan_node_name = plan_node_name

    @property
    def start_time(self):
        r"""Gets the start_time of this OperatorMetric.

        **参数解释**：开始时间，格式为：YYYY-MM-DD HH:MM:SS。 **取值范围**：时间范围：1000-01-01 00:00:00/9999-12-31 23:59:59。

        :return: The start_time of this OperatorMetric.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this OperatorMetric.

        **参数解释**：开始时间，格式为：YYYY-MM-DD HH:MM:SS。 **取值范围**：时间范围：1000-01-01 00:00:00/9999-12-31 23:59:59。

        :param start_time: The start_time of this OperatorMetric.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def duration(self):
        r"""Gets the duration of this OperatorMetric.

        **参数解释**：执行时长。 **取值范围**：1~9223372036854775807。

        :return: The duration of this OperatorMetric.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this OperatorMetric.

        **参数解释**：执行时长。 **取值范围**：1~9223372036854775807。

        :param duration: The duration of this OperatorMetric.
        :type duration: int
        """
        self._duration = duration

    @property
    def status(self):
        r"""Gets the status of this OperatorMetric.

        **参数解释**：算子当前执行状态。 **取值范围**：   - init：初始化。   - waiting：等待中。   - finished：已结束。   - running：运行中。

        :return: The status of this OperatorMetric.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OperatorMetric.

        **参数解释**：算子当前执行状态。 **取值范围**：   - init：初始化。   - waiting：等待中。   - finished：已结束。   - running：运行中。

        :param status: The status of this OperatorMetric.
        :type status: str
        """
        self._status = status

    @property
    def query_dop(self):
        r"""Gets the query_dop of this OperatorMetric.

        **参数解释**：查询的并行度。 **取值范围**：1~2147483647。

        :return: The query_dop of this OperatorMetric.
        :rtype: int
        """
        return self._query_dop

    @query_dop.setter
    def query_dop(self, query_dop):
        r"""Sets the query_dop of this OperatorMetric.

        **参数解释**：查询的并行度。 **取值范围**：1~2147483647。

        :param query_dop: The query_dop of this OperatorMetric.
        :type query_dop: int
        """
        self._query_dop = query_dop

    @property
    def estimated_rows(self):
        r"""Gets the estimated_rows of this OperatorMetric.

        **参数解释**：预估的行数。 **取值范围**：1~9223372036854775807。

        :return: The estimated_rows of this OperatorMetric.
        :rtype: int
        """
        return self._estimated_rows

    @estimated_rows.setter
    def estimated_rows(self, estimated_rows):
        r"""Sets the estimated_rows of this OperatorMetric.

        **参数解释**：预估的行数。 **取值范围**：1~9223372036854775807。

        :param estimated_rows: The estimated_rows of this OperatorMetric.
        :type estimated_rows: int
        """
        self._estimated_rows = estimated_rows

    @property
    def tuple_processed(self):
        r"""Gets the tuple_processed of this OperatorMetric.

        **参数解释**：当前已经处理完成的行数。 **取值范围**：1~9223372036854775807。

        :return: The tuple_processed of this OperatorMetric.
        :rtype: int
        """
        return self._tuple_processed

    @tuple_processed.setter
    def tuple_processed(self, tuple_processed):
        r"""Sets the tuple_processed of this OperatorMetric.

        **参数解释**：当前已经处理完成的行数。 **取值范围**：1~9223372036854775807。

        :param tuple_processed: The tuple_processed of this OperatorMetric.
        :type tuple_processed: int
        """
        self._tuple_processed = tuple_processed

    @property
    def min_peak_memory(self):
        r"""Gets the min_peak_memory of this OperatorMetric.

        **参数解释**：内存使用的最小峰值。 **取值范围**：1~2147483647。

        :return: The min_peak_memory of this OperatorMetric.
        :rtype: int
        """
        return self._min_peak_memory

    @min_peak_memory.setter
    def min_peak_memory(self, min_peak_memory):
        r"""Sets the min_peak_memory of this OperatorMetric.

        **参数解释**：内存使用的最小峰值。 **取值范围**：1~2147483647。

        :param min_peak_memory: The min_peak_memory of this OperatorMetric.
        :type min_peak_memory: int
        """
        self._min_peak_memory = min_peak_memory

    @property
    def max_peak_memory(self):
        r"""Gets the max_peak_memory of this OperatorMetric.

        **参数解释**：内存使用的最大峰值。 **取值范围**：1~2147483647。

        :return: The max_peak_memory of this OperatorMetric.
        :rtype: int
        """
        return self._max_peak_memory

    @max_peak_memory.setter
    def max_peak_memory(self, max_peak_memory):
        r"""Sets the max_peak_memory of this OperatorMetric.

        **参数解释**：内存使用的最大峰值。 **取值范围**：1~2147483647。

        :param max_peak_memory: The max_peak_memory of this OperatorMetric.
        :type max_peak_memory: int
        """
        self._max_peak_memory = max_peak_memory

    @property
    def average_peak_memory(self):
        r"""Gets the average_peak_memory of this OperatorMetric.

        **参数解释**：内存使用的平均峰值。 **取值范围**：1~2147483647。

        :return: The average_peak_memory of this OperatorMetric.
        :rtype: int
        """
        return self._average_peak_memory

    @average_peak_memory.setter
    def average_peak_memory(self, average_peak_memory):
        r"""Sets the average_peak_memory of this OperatorMetric.

        **参数解释**：内存使用的平均峰值。 **取值范围**：1~2147483647。

        :param average_peak_memory: The average_peak_memory of this OperatorMetric.
        :type average_peak_memory: int
        """
        self._average_peak_memory = average_peak_memory

    @property
    def memory_skew_percent(self):
        r"""Gets the memory_skew_percent of this OperatorMetric.

        **参数解释**：内存使用倾斜百分比。 **取值范围**：1~2147483647。

        :return: The memory_skew_percent of this OperatorMetric.
        :rtype: int
        """
        return self._memory_skew_percent

    @memory_skew_percent.setter
    def memory_skew_percent(self, memory_skew_percent):
        r"""Sets the memory_skew_percent of this OperatorMetric.

        **参数解释**：内存使用倾斜百分比。 **取值范围**：1~2147483647。

        :param memory_skew_percent: The memory_skew_percent of this OperatorMetric.
        :type memory_skew_percent: int
        """
        self._memory_skew_percent = memory_skew_percent

    @property
    def min_spill_size(self):
        r"""Gets the min_spill_size of this OperatorMetric.

        **参数解释**：下盘的最小数据量。 **取值范围**：1~2147483647。

        :return: The min_spill_size of this OperatorMetric.
        :rtype: int
        """
        return self._min_spill_size

    @min_spill_size.setter
    def min_spill_size(self, min_spill_size):
        r"""Sets the min_spill_size of this OperatorMetric.

        **参数解释**：下盘的最小数据量。 **取值范围**：1~2147483647。

        :param min_spill_size: The min_spill_size of this OperatorMetric.
        :type min_spill_size: int
        """
        self._min_spill_size = min_spill_size

    @property
    def max_spill_size(self):
        r"""Gets the max_spill_size of this OperatorMetric.

        **参数解释**：下盘的最大数据量。 **取值范围**：1~2147483647。

        :return: The max_spill_size of this OperatorMetric.
        :rtype: int
        """
        return self._max_spill_size

    @max_spill_size.setter
    def max_spill_size(self, max_spill_size):
        r"""Sets the max_spill_size of this OperatorMetric.

        **参数解释**：下盘的最大数据量。 **取值范围**：1~2147483647。

        :param max_spill_size: The max_spill_size of this OperatorMetric.
        :type max_spill_size: int
        """
        self._max_spill_size = max_spill_size

    @property
    def average_spill_size(self):
        r"""Gets the average_spill_size of this OperatorMetric.

        **参数解释**：下盘的平均数据量。 **取值范围**：1~2147483647。

        :return: The average_spill_size of this OperatorMetric.
        :rtype: int
        """
        return self._average_spill_size

    @average_spill_size.setter
    def average_spill_size(self, average_spill_size):
        r"""Sets the average_spill_size of this OperatorMetric.

        **参数解释**：下盘的平均数据量。 **取值范围**：1~2147483647。

        :param average_spill_size: The average_spill_size of this OperatorMetric.
        :type average_spill_size: int
        """
        self._average_spill_size = average_spill_size

    @property
    def spill_skew_percent(self):
        r"""Gets the spill_skew_percent of this OperatorMetric.

        **参数解释**：下盘数据的倾斜百分比。 **取值范围**：不涉及。

        :return: The spill_skew_percent of this OperatorMetric.
        :rtype: str
        """
        return self._spill_skew_percent

    @spill_skew_percent.setter
    def spill_skew_percent(self, spill_skew_percent):
        r"""Sets the spill_skew_percent of this OperatorMetric.

        **参数解释**：下盘数据的倾斜百分比。 **取值范围**：不涉及。

        :param spill_skew_percent: The spill_skew_percent of this OperatorMetric.
        :type spill_skew_percent: str
        """
        self._spill_skew_percent = spill_skew_percent

    @property
    def loops(self):
        r"""Gets the loops of this OperatorMetric.

        **参数解释**：算子执行迭代次数。 **取值范围**：1~2147483647。

        :return: The loops of this OperatorMetric.
        :rtype: int
        """
        return self._loops

    @loops.setter
    def loops(self, loops):
        r"""Sets the loops of this OperatorMetric.

        **参数解释**：算子执行迭代次数。 **取值范围**：1~2147483647。

        :param loops: The loops of this OperatorMetric.
        :type loops: int
        """
        self._loops = loops

    @property
    def progress(self):
        r"""Gets the progress of this OperatorMetric.

        **参数解释**：执行进度百分比。 **取值范围**：不涉及。

        :return: The progress of this OperatorMetric.
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this OperatorMetric.

        **参数解释**：执行进度百分比。 **取值范围**：不涉及。

        :param progress: The progress of this OperatorMetric.
        :type progress: str
        """
        self._progress = progress

    @property
    def total_read_size(self):
        r"""Gets the total_read_size of this OperatorMetric.

        **参数解释**：所有节点读取的总数据量。 **取值范围**：1~9223372036854775807。

        :return: The total_read_size of this OperatorMetric.
        :rtype: int
        """
        return self._total_read_size

    @total_read_size.setter
    def total_read_size(self, total_read_size):
        r"""Sets the total_read_size of this OperatorMetric.

        **参数解释**：所有节点读取的总数据量。 **取值范围**：1~9223372036854775807。

        :param total_read_size: The total_read_size of this OperatorMetric.
        :type total_read_size: int
        """
        self._total_read_size = total_read_size

    @property
    def total_write_size(self):
        r"""Gets the total_write_size of this OperatorMetric.

        **参数解释**：所有节点写入的总数据量。 **取值范围**：1~9223372036854775807。

        :return: The total_write_size of this OperatorMetric.
        :rtype: int
        """
        return self._total_write_size

    @total_write_size.setter
    def total_write_size(self, total_write_size):
        r"""Sets the total_write_size of this OperatorMetric.

        **参数解释**：所有节点写入的总数据量。 **取值范围**：1~9223372036854775807。

        :param total_write_size: The total_write_size of this OperatorMetric.
        :type total_write_size: int
        """
        self._total_write_size = total_write_size

    @property
    def sub_operator_metrics(self):
        r"""Gets the sub_operator_metrics of this OperatorMetric.

        **参数解释**：子节点。 **取值范围**：不涉及。

        :return: The sub_operator_metrics of this OperatorMetric.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.OperatorMetric`]
        """
        return self._sub_operator_metrics

    @sub_operator_metrics.setter
    def sub_operator_metrics(self, sub_operator_metrics):
        r"""Sets the sub_operator_metrics of this OperatorMetric.

        **参数解释**：子节点。 **取值范围**：不涉及。

        :param sub_operator_metrics: The sub_operator_metrics of this OperatorMetric.
        :type sub_operator_metrics: list[:class:`huaweicloudsdkaidatalakejobserver.v2.OperatorMetric`]
        """
        self._sub_operator_metrics = sub_operator_metrics

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
        if not isinstance(other, OperatorMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
