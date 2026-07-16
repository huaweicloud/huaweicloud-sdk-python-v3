# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Status:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phase': 'str',
        'secondary_phase': 'str',
        'duration': 'int',
        'node_count_metrics': 'list[list[int]]',
        'tasks': 'list[str]',
        'start_time': 'int',
        'task_statuses': 'list[TaskStatuses]',
        'running_records': 'list[RunningRecord]'
    }

    attribute_map = {
        'phase': 'phase',
        'secondary_phase': 'secondary_phase',
        'duration': 'duration',
        'node_count_metrics': 'node_count_metrics',
        'tasks': 'tasks',
        'start_time': 'start_time',
        'task_statuses': 'task_statuses',
        'running_records': 'running_records'
    }

    def __init__(self, phase=None, secondary_phase=None, duration=None, node_count_metrics=None, tasks=None, start_time=None, task_statuses=None, running_records=None):
        r"""Status

        The model defined in huaweicloud sdk

        :param phase: 训练作业一级状态。可选值如下： - Creating：创建中 - Pending：等待中 - Running：运行中 - Failed：运行失败 - Completed：已完成 - Terminating：停止中 - Terminated：已停止 - Abnormal：异常
        :type phase: str
        :param secondary_phase: 训练作业二级状态为内部详细状态，可能会增加、修改、删除，不建议依赖。可选值如下： - Creating：创建中 - Queuing：排队中 - Running：运行中 - Failed：运行失败 - Completed：已完成 - Terminating：停止中 - Terminated：已停止 - CreateFailed：创建失败 - TerminatedFailed：停止失败 - Unknown：未知状态 - Lost：异常
        :type secondary_phase: str
        :param duration: 训练作业运行时长，单位为毫秒。
        :type duration: int
        :param node_count_metrics: 训练作业运行时节点数变化指标。
        :type node_count_metrics: list[list[int]]
        :param tasks: 训练作业子任务名称。
        :type tasks: list[str]
        :param start_time: 训练作业开始时间，格式为时间戳。
        :type start_time: int
        :param task_statuses: 训练在子任务状态信息。
        :type task_statuses: list[:class:`huaweicloudsdkmodelarts.v1.TaskStatuses`]
        :param running_records: 训练作业运行及故障恢复记录。
        :type running_records: list[:class:`huaweicloudsdkmodelarts.v1.RunningRecord`]
        """
        
        

        self._phase = None
        self._secondary_phase = None
        self._duration = None
        self._node_count_metrics = None
        self._tasks = None
        self._start_time = None
        self._task_statuses = None
        self._running_records = None
        self.discriminator = None

        if phase is not None:
            self.phase = phase
        if secondary_phase is not None:
            self.secondary_phase = secondary_phase
        if duration is not None:
            self.duration = duration
        if node_count_metrics is not None:
            self.node_count_metrics = node_count_metrics
        if tasks is not None:
            self.tasks = tasks
        if start_time is not None:
            self.start_time = start_time
        if task_statuses is not None:
            self.task_statuses = task_statuses
        if running_records is not None:
            self.running_records = running_records

    @property
    def phase(self):
        r"""Gets the phase of this Status.

        训练作业一级状态。可选值如下： - Creating：创建中 - Pending：等待中 - Running：运行中 - Failed：运行失败 - Completed：已完成 - Terminating：停止中 - Terminated：已停止 - Abnormal：异常

        :return: The phase of this Status.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        r"""Sets the phase of this Status.

        训练作业一级状态。可选值如下： - Creating：创建中 - Pending：等待中 - Running：运行中 - Failed：运行失败 - Completed：已完成 - Terminating：停止中 - Terminated：已停止 - Abnormal：异常

        :param phase: The phase of this Status.
        :type phase: str
        """
        self._phase = phase

    @property
    def secondary_phase(self):
        r"""Gets the secondary_phase of this Status.

        训练作业二级状态为内部详细状态，可能会增加、修改、删除，不建议依赖。可选值如下： - Creating：创建中 - Queuing：排队中 - Running：运行中 - Failed：运行失败 - Completed：已完成 - Terminating：停止中 - Terminated：已停止 - CreateFailed：创建失败 - TerminatedFailed：停止失败 - Unknown：未知状态 - Lost：异常

        :return: The secondary_phase of this Status.
        :rtype: str
        """
        return self._secondary_phase

    @secondary_phase.setter
    def secondary_phase(self, secondary_phase):
        r"""Sets the secondary_phase of this Status.

        训练作业二级状态为内部详细状态，可能会增加、修改、删除，不建议依赖。可选值如下： - Creating：创建中 - Queuing：排队中 - Running：运行中 - Failed：运行失败 - Completed：已完成 - Terminating：停止中 - Terminated：已停止 - CreateFailed：创建失败 - TerminatedFailed：停止失败 - Unknown：未知状态 - Lost：异常

        :param secondary_phase: The secondary_phase of this Status.
        :type secondary_phase: str
        """
        self._secondary_phase = secondary_phase

    @property
    def duration(self):
        r"""Gets the duration of this Status.

        训练作业运行时长，单位为毫秒。

        :return: The duration of this Status.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this Status.

        训练作业运行时长，单位为毫秒。

        :param duration: The duration of this Status.
        :type duration: int
        """
        self._duration = duration

    @property
    def node_count_metrics(self):
        r"""Gets the node_count_metrics of this Status.

        训练作业运行时节点数变化指标。

        :return: The node_count_metrics of this Status.
        :rtype: list[list[int]]
        """
        return self._node_count_metrics

    @node_count_metrics.setter
    def node_count_metrics(self, node_count_metrics):
        r"""Sets the node_count_metrics of this Status.

        训练作业运行时节点数变化指标。

        :param node_count_metrics: The node_count_metrics of this Status.
        :type node_count_metrics: list[list[int]]
        """
        self._node_count_metrics = node_count_metrics

    @property
    def tasks(self):
        r"""Gets the tasks of this Status.

        训练作业子任务名称。

        :return: The tasks of this Status.
        :rtype: list[str]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this Status.

        训练作业子任务名称。

        :param tasks: The tasks of this Status.
        :type tasks: list[str]
        """
        self._tasks = tasks

    @property
    def start_time(self):
        r"""Gets the start_time of this Status.

        训练作业开始时间，格式为时间戳。

        :return: The start_time of this Status.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this Status.

        训练作业开始时间，格式为时间戳。

        :param start_time: The start_time of this Status.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def task_statuses(self):
        r"""Gets the task_statuses of this Status.

        训练在子任务状态信息。

        :return: The task_statuses of this Status.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.TaskStatuses`]
        """
        return self._task_statuses

    @task_statuses.setter
    def task_statuses(self, task_statuses):
        r"""Sets the task_statuses of this Status.

        训练在子任务状态信息。

        :param task_statuses: The task_statuses of this Status.
        :type task_statuses: list[:class:`huaweicloudsdkmodelarts.v1.TaskStatuses`]
        """
        self._task_statuses = task_statuses

    @property
    def running_records(self):
        r"""Gets the running_records of this Status.

        训练作业运行及故障恢复记录。

        :return: The running_records of this Status.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.RunningRecord`]
        """
        return self._running_records

    @running_records.setter
    def running_records(self, running_records):
        r"""Sets the running_records of this Status.

        训练作业运行及故障恢复记录。

        :param running_records: The running_records of this Status.
        :type running_records: list[:class:`huaweicloudsdkmodelarts.v1.RunningRecord`]
        """
        self._running_records = running_records

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
        if not isinstance(other, Status):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
