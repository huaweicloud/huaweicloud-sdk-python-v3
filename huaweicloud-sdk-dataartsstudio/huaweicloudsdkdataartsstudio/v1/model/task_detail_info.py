# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'monitor_report_id': 'str',
        'task_type': 'str',
        'running_status': 'str',
        'external_job_id': 'str',
        'source_type': 'str',
        'target_type': 'str',
        'tracking_url': 'str',
        'state': 'str',
        'error_msg': 'str',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'monitor_report_id': 'monitor_report_id',
        'task_type': 'task_type',
        'running_status': 'running_status',
        'external_job_id': 'external_job_id',
        'source_type': 'source_type',
        'target_type': 'target_type',
        'tracking_url': 'tracking_url',
        'state': 'state',
        'error_msg': 'error_msg',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, task_id=None, task_name=None, monitor_report_id=None, task_type=None, running_status=None, external_job_id=None, source_type=None, target_type=None, tracking_url=None, state=None, error_msg=None, create_time=None, update_time=None):
        r"""TaskDetailInfo

        The model defined in huaweicloud sdk

        :param task_id: 集成任务ID。
        :type task_id: str
        :param task_name: 任务名称，长度限制0-57个字符。
        :type task_name: str
        :param monitor_report_id: DLF作业ID。
        :type monitor_report_id: str
        :param task_type: 任务类型。 - FLINK：Flink类型 - SPARK：Spark类型 - DRS：DRS类型
        :type task_type: str
        :param running_status: 作业运行状态。 - INITIALIZING：初始化中 - SNAPSHOT：全量阶段 - BINLOG：增量阶段
        :type running_status: str
        :param external_job_id: 计算作业ID，DLI/CCE/DRS执行的作业ID。
        :type external_job_id: str
        :param source_type: 源端类型。
        :type source_type: str
        :param target_type: 目的端类型。
        :type target_type: str
        :param tracking_url: MRS Flink作业trackingUrl。
        :type tracking_url: str
        :param state: 任务状态。 - EXCEPTION：异常 - STOPPING：停止中 - SUBMITTING：提交中 - RUNNING：运行中 - STOPPED：已停止 - SUCCESS：成功
        :type state: str
        :param error_msg: 错误信息。
        :type error_msg: str
        :param create_time: 任务创建时间，毫秒时间戳。
        :type create_time: int
        :param update_time: 任务更新时间，毫秒时间戳。
        :type update_time: int
        """
        
        

        self._task_id = None
        self._task_name = None
        self._monitor_report_id = None
        self._task_type = None
        self._running_status = None
        self._external_job_id = None
        self._source_type = None
        self._target_type = None
        self._tracking_url = None
        self._state = None
        self._error_msg = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if monitor_report_id is not None:
            self.monitor_report_id = monitor_report_id
        if task_type is not None:
            self.task_type = task_type
        if running_status is not None:
            self.running_status = running_status
        if external_job_id is not None:
            self.external_job_id = external_job_id
        if source_type is not None:
            self.source_type = source_type
        if target_type is not None:
            self.target_type = target_type
        if tracking_url is not None:
            self.tracking_url = tracking_url
        if state is not None:
            self.state = state
        if error_msg is not None:
            self.error_msg = error_msg
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def task_id(self):
        r"""Gets the task_id of this TaskDetailInfo.

        集成任务ID。

        :return: The task_id of this TaskDetailInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this TaskDetailInfo.

        集成任务ID。

        :param task_id: The task_id of this TaskDetailInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this TaskDetailInfo.

        任务名称，长度限制0-57个字符。

        :return: The task_name of this TaskDetailInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this TaskDetailInfo.

        任务名称，长度限制0-57个字符。

        :param task_name: The task_name of this TaskDetailInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def monitor_report_id(self):
        r"""Gets the monitor_report_id of this TaskDetailInfo.

        DLF作业ID。

        :return: The monitor_report_id of this TaskDetailInfo.
        :rtype: str
        """
        return self._monitor_report_id

    @monitor_report_id.setter
    def monitor_report_id(self, monitor_report_id):
        r"""Sets the monitor_report_id of this TaskDetailInfo.

        DLF作业ID。

        :param monitor_report_id: The monitor_report_id of this TaskDetailInfo.
        :type monitor_report_id: str
        """
        self._monitor_report_id = monitor_report_id

    @property
    def task_type(self):
        r"""Gets the task_type of this TaskDetailInfo.

        任务类型。 - FLINK：Flink类型 - SPARK：Spark类型 - DRS：DRS类型

        :return: The task_type of this TaskDetailInfo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this TaskDetailInfo.

        任务类型。 - FLINK：Flink类型 - SPARK：Spark类型 - DRS：DRS类型

        :param task_type: The task_type of this TaskDetailInfo.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def running_status(self):
        r"""Gets the running_status of this TaskDetailInfo.

        作业运行状态。 - INITIALIZING：初始化中 - SNAPSHOT：全量阶段 - BINLOG：增量阶段

        :return: The running_status of this TaskDetailInfo.
        :rtype: str
        """
        return self._running_status

    @running_status.setter
    def running_status(self, running_status):
        r"""Sets the running_status of this TaskDetailInfo.

        作业运行状态。 - INITIALIZING：初始化中 - SNAPSHOT：全量阶段 - BINLOG：增量阶段

        :param running_status: The running_status of this TaskDetailInfo.
        :type running_status: str
        """
        self._running_status = running_status

    @property
    def external_job_id(self):
        r"""Gets the external_job_id of this TaskDetailInfo.

        计算作业ID，DLI/CCE/DRS执行的作业ID。

        :return: The external_job_id of this TaskDetailInfo.
        :rtype: str
        """
        return self._external_job_id

    @external_job_id.setter
    def external_job_id(self, external_job_id):
        r"""Sets the external_job_id of this TaskDetailInfo.

        计算作业ID，DLI/CCE/DRS执行的作业ID。

        :param external_job_id: The external_job_id of this TaskDetailInfo.
        :type external_job_id: str
        """
        self._external_job_id = external_job_id

    @property
    def source_type(self):
        r"""Gets the source_type of this TaskDetailInfo.

        源端类型。

        :return: The source_type of this TaskDetailInfo.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this TaskDetailInfo.

        源端类型。

        :param source_type: The source_type of this TaskDetailInfo.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def target_type(self):
        r"""Gets the target_type of this TaskDetailInfo.

        目的端类型。

        :return: The target_type of this TaskDetailInfo.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this TaskDetailInfo.

        目的端类型。

        :param target_type: The target_type of this TaskDetailInfo.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def tracking_url(self):
        r"""Gets the tracking_url of this TaskDetailInfo.

        MRS Flink作业trackingUrl。

        :return: The tracking_url of this TaskDetailInfo.
        :rtype: str
        """
        return self._tracking_url

    @tracking_url.setter
    def tracking_url(self, tracking_url):
        r"""Sets the tracking_url of this TaskDetailInfo.

        MRS Flink作业trackingUrl。

        :param tracking_url: The tracking_url of this TaskDetailInfo.
        :type tracking_url: str
        """
        self._tracking_url = tracking_url

    @property
    def state(self):
        r"""Gets the state of this TaskDetailInfo.

        任务状态。 - EXCEPTION：异常 - STOPPING：停止中 - SUBMITTING：提交中 - RUNNING：运行中 - STOPPED：已停止 - SUCCESS：成功

        :return: The state of this TaskDetailInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this TaskDetailInfo.

        任务状态。 - EXCEPTION：异常 - STOPPING：停止中 - SUBMITTING：提交中 - RUNNING：运行中 - STOPPED：已停止 - SUCCESS：成功

        :param state: The state of this TaskDetailInfo.
        :type state: str
        """
        self._state = state

    @property
    def error_msg(self):
        r"""Gets the error_msg of this TaskDetailInfo.

        错误信息。

        :return: The error_msg of this TaskDetailInfo.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this TaskDetailInfo.

        错误信息。

        :param error_msg: The error_msg of this TaskDetailInfo.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def create_time(self):
        r"""Gets the create_time of this TaskDetailInfo.

        任务创建时间，毫秒时间戳。

        :return: The create_time of this TaskDetailInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TaskDetailInfo.

        任务创建时间，毫秒时间戳。

        :param create_time: The create_time of this TaskDetailInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TaskDetailInfo.

        任务更新时间，毫秒时间戳。

        :return: The update_time of this TaskDetailInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TaskDetailInfo.

        任务更新时间，毫秒时间戳。

        :param update_time: The update_time of this TaskDetailInfo.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, TaskDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
