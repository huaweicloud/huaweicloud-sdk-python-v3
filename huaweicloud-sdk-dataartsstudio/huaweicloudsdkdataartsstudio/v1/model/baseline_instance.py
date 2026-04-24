# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaselineInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'baseline': 'object',
        'baseline_id': 'str',
        'baseline_name': 'str',
        'baseline_version': 'int',
        'priority': 'int',
        'dag': 'str',
        'status': 'str',
        'buffer': 'int',
        'estimate_complete_time': 'int',
        'expect_time': 'int',
        'finish_status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'execute_time': 'int',
        'error_code': 'str',
        'error_message': 'str',
        'task_instances': 'object',
        'owner_id': 'str',
        'owner_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'project_id': 'str',
        'instance_id': 'str',
        'workspace_id': 'str',
        'first_alarm_time': 'int',
        'last_alarm_time': 'int',
        'sla_time': 'int',
        'process_time': 'int',
        'recover_time': 'int',
        'ignore_time': 'int',
        'process_buffer': 'int',
        'create_day': 'int',
        'instance_type': 'str',
        'process_user_id': 'str',
        'process_user_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'baseline': 'baseline',
        'baseline_id': 'baseline_id',
        'baseline_name': 'baseline_name',
        'baseline_version': 'baseline_version',
        'priority': 'priority',
        'dag': 'dag',
        'status': 'status',
        'buffer': 'buffer',
        'estimate_complete_time': 'estimate_complete_time',
        'expect_time': 'expect_time',
        'finish_status': 'finish_status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'execute_time': 'execute_time',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'task_instances': 'task_instances',
        'owner_id': 'owner_id',
        'owner_name': 'owner_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'project_id': 'project_id',
        'instance_id': 'instance_id',
        'workspace_id': 'workspace_id',
        'first_alarm_time': 'first_alarm_time',
        'last_alarm_time': 'last_alarm_time',
        'sla_time': 'sla_time',
        'process_time': 'process_time',
        'recover_time': 'recover_time',
        'ignore_time': 'ignore_time',
        'process_buffer': 'process_buffer',
        'create_day': 'create_day',
        'instance_type': 'instance_type',
        'process_user_id': 'process_user_id',
        'process_user_name': 'process_user_name'
    }

    def __init__(self, id=None, baseline=None, baseline_id=None, baseline_name=None, baseline_version=None, priority=None, dag=None, status=None, buffer=None, estimate_complete_time=None, expect_time=None, finish_status=None, start_time=None, end_time=None, execute_time=None, error_code=None, error_message=None, task_instances=None, owner_id=None, owner_name=None, domain_id=None, domain_name=None, project_id=None, instance_id=None, workspace_id=None, first_alarm_time=None, last_alarm_time=None, sla_time=None, process_time=None, recover_time=None, ignore_time=None, process_buffer=None, create_day=None, instance_type=None, process_user_id=None, process_user_name=None):
        r"""BaselineInstance

        The model defined in huaweicloud sdk

        :param id: 基线实例ID。
        :type id: str
        :param baseline: 基线明细。
        :type baseline: object
        :param baseline_id: 基线ID。
        :type baseline_id: str
        :param baseline_name: 基线任务名称。
        :type baseline_name: str
        :param baseline_version: 版本号。
        :type baseline_version: int
        :param priority: 优先级。
        :type priority: int
        :param dag: 基线任务实例作业依赖图（包含JOB_ID+JOB名称+版本号+是否为关键路径节点）。
        :type dag: str
        :param status: 基线实例状态。
        :type status: str
        :param buffer: 基线实例余量，单位为s。
        :type buffer: int
        :param estimate_complete_time: 预计完成时间戳，单位毫秒。
        :type estimate_complete_time: int
        :param expect_time: 实例预警时间戳，单位毫秒。
        :type expect_time: int
        :param finish_status: 基线实例是否完成。
        :type finish_status: str
        :param start_time: 基线实例开始时间戳，单位毫秒。
        :type start_time: int
        :param end_time: 基线实例结束时间戳，单位毫秒，finish_status（基线实例完成状态）为FINISH（已完成）时，返回基线实例的完成时间戳。
        :type end_time: int
        :param execute_time: 运行时间戳，单位毫秒。
        :type execute_time: int
        :param error_code: 错误编码。
        :type error_code: str
        :param error_message: 错误信息。
        :type error_message: str
        :param task_instances: 任务实例信息。
        :type task_instances: object
        :param owner_id: 责任人用户ID。
        :type owner_id: str
        :param owner_name: 责任人用户名称。
        :type owner_name: str
        :param domain_id: 责任人租户ID。
        :type domain_id: str
        :param domain_name: 责任人租户名称。
        :type domain_name: str
        :param project_id: 项目ID。
        :type project_id: str
        :param instance_id: DataArts Studio实例ID。
        :type instance_id: str
        :param workspace_id: 工作空间ID。
        :type workspace_id: str
        :param first_alarm_time: 首次告警时间戳，单位毫秒。
        :type first_alarm_time: int
        :param last_alarm_time: 最后告警时间戳，单位毫秒。
        :type last_alarm_time: int
        :param sla_time: 实例承诺时间戳，单位毫秒。
        :type sla_time: int
        :param process_time: 处理时间戳，单位毫秒。
        :type process_time: int
        :param recover_time: 恢复时间戳，单位毫秒。
        :type recover_time: int
        :param ignore_time: 忽略时间戳，单位毫秒。
        :type ignore_time: int
        :param process_buffer: 处理时长，设置处理时间所需要的时间，设置后在该时间段内将暂停事件报警，事件的处理操作记录会被记录。
        :type process_buffer: int
        :param create_day: 创建时间的天数，表示一年的第几天。
        :type create_day: int
        :param instance_type: 实例类型。
        :type instance_type: str
        :param process_user_id: 基线处理人用户ID。
        :type process_user_id: str
        :param process_user_name: 基线处理人用户名称。
        :type process_user_name: str
        """
        
        

        self._id = None
        self._baseline = None
        self._baseline_id = None
        self._baseline_name = None
        self._baseline_version = None
        self._priority = None
        self._dag = None
        self._status = None
        self._buffer = None
        self._estimate_complete_time = None
        self._expect_time = None
        self._finish_status = None
        self._start_time = None
        self._end_time = None
        self._execute_time = None
        self._error_code = None
        self._error_message = None
        self._task_instances = None
        self._owner_id = None
        self._owner_name = None
        self._domain_id = None
        self._domain_name = None
        self._project_id = None
        self._instance_id = None
        self._workspace_id = None
        self._first_alarm_time = None
        self._last_alarm_time = None
        self._sla_time = None
        self._process_time = None
        self._recover_time = None
        self._ignore_time = None
        self._process_buffer = None
        self._create_day = None
        self._instance_type = None
        self._process_user_id = None
        self._process_user_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if baseline is not None:
            self.baseline = baseline
        if baseline_id is not None:
            self.baseline_id = baseline_id
        if baseline_name is not None:
            self.baseline_name = baseline_name
        if baseline_version is not None:
            self.baseline_version = baseline_version
        if priority is not None:
            self.priority = priority
        if dag is not None:
            self.dag = dag
        if status is not None:
            self.status = status
        if buffer is not None:
            self.buffer = buffer
        if estimate_complete_time is not None:
            self.estimate_complete_time = estimate_complete_time
        if expect_time is not None:
            self.expect_time = expect_time
        if finish_status is not None:
            self.finish_status = finish_status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if execute_time is not None:
            self.execute_time = execute_time
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if task_instances is not None:
            self.task_instances = task_instances
        if owner_id is not None:
            self.owner_id = owner_id
        if owner_name is not None:
            self.owner_name = owner_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if project_id is not None:
            self.project_id = project_id
        if instance_id is not None:
            self.instance_id = instance_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if first_alarm_time is not None:
            self.first_alarm_time = first_alarm_time
        if last_alarm_time is not None:
            self.last_alarm_time = last_alarm_time
        if sla_time is not None:
            self.sla_time = sla_time
        if process_time is not None:
            self.process_time = process_time
        if recover_time is not None:
            self.recover_time = recover_time
        if ignore_time is not None:
            self.ignore_time = ignore_time
        if process_buffer is not None:
            self.process_buffer = process_buffer
        if create_day is not None:
            self.create_day = create_day
        if instance_type is not None:
            self.instance_type = instance_type
        if process_user_id is not None:
            self.process_user_id = process_user_id
        if process_user_name is not None:
            self.process_user_name = process_user_name

    @property
    def id(self):
        r"""Gets the id of this BaselineInstance.

        基线实例ID。

        :return: The id of this BaselineInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BaselineInstance.

        基线实例ID。

        :param id: The id of this BaselineInstance.
        :type id: str
        """
        self._id = id

    @property
    def baseline(self):
        r"""Gets the baseline of this BaselineInstance.

        基线明细。

        :return: The baseline of this BaselineInstance.
        :rtype: object
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this BaselineInstance.

        基线明细。

        :param baseline: The baseline of this BaselineInstance.
        :type baseline: object
        """
        self._baseline = baseline

    @property
    def baseline_id(self):
        r"""Gets the baseline_id of this BaselineInstance.

        基线ID。

        :return: The baseline_id of this BaselineInstance.
        :rtype: str
        """
        return self._baseline_id

    @baseline_id.setter
    def baseline_id(self, baseline_id):
        r"""Sets the baseline_id of this BaselineInstance.

        基线ID。

        :param baseline_id: The baseline_id of this BaselineInstance.
        :type baseline_id: str
        """
        self._baseline_id = baseline_id

    @property
    def baseline_name(self):
        r"""Gets the baseline_name of this BaselineInstance.

        基线任务名称。

        :return: The baseline_name of this BaselineInstance.
        :rtype: str
        """
        return self._baseline_name

    @baseline_name.setter
    def baseline_name(self, baseline_name):
        r"""Sets the baseline_name of this BaselineInstance.

        基线任务名称。

        :param baseline_name: The baseline_name of this BaselineInstance.
        :type baseline_name: str
        """
        self._baseline_name = baseline_name

    @property
    def baseline_version(self):
        r"""Gets the baseline_version of this BaselineInstance.

        版本号。

        :return: The baseline_version of this BaselineInstance.
        :rtype: int
        """
        return self._baseline_version

    @baseline_version.setter
    def baseline_version(self, baseline_version):
        r"""Sets the baseline_version of this BaselineInstance.

        版本号。

        :param baseline_version: The baseline_version of this BaselineInstance.
        :type baseline_version: int
        """
        self._baseline_version = baseline_version

    @property
    def priority(self):
        r"""Gets the priority of this BaselineInstance.

        优先级。

        :return: The priority of this BaselineInstance.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this BaselineInstance.

        优先级。

        :param priority: The priority of this BaselineInstance.
        :type priority: int
        """
        self._priority = priority

    @property
    def dag(self):
        r"""Gets the dag of this BaselineInstance.

        基线任务实例作业依赖图（包含JOB_ID+JOB名称+版本号+是否为关键路径节点）。

        :return: The dag of this BaselineInstance.
        :rtype: str
        """
        return self._dag

    @dag.setter
    def dag(self, dag):
        r"""Sets the dag of this BaselineInstance.

        基线任务实例作业依赖图（包含JOB_ID+JOB名称+版本号+是否为关键路径节点）。

        :param dag: The dag of this BaselineInstance.
        :type dag: str
        """
        self._dag = dag

    @property
    def status(self):
        r"""Gets the status of this BaselineInstance.

        基线实例状态。

        :return: The status of this BaselineInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BaselineInstance.

        基线实例状态。

        :param status: The status of this BaselineInstance.
        :type status: str
        """
        self._status = status

    @property
    def buffer(self):
        r"""Gets the buffer of this BaselineInstance.

        基线实例余量，单位为s。

        :return: The buffer of this BaselineInstance.
        :rtype: int
        """
        return self._buffer

    @buffer.setter
    def buffer(self, buffer):
        r"""Sets the buffer of this BaselineInstance.

        基线实例余量，单位为s。

        :param buffer: The buffer of this BaselineInstance.
        :type buffer: int
        """
        self._buffer = buffer

    @property
    def estimate_complete_time(self):
        r"""Gets the estimate_complete_time of this BaselineInstance.

        预计完成时间戳，单位毫秒。

        :return: The estimate_complete_time of this BaselineInstance.
        :rtype: int
        """
        return self._estimate_complete_time

    @estimate_complete_time.setter
    def estimate_complete_time(self, estimate_complete_time):
        r"""Sets the estimate_complete_time of this BaselineInstance.

        预计完成时间戳，单位毫秒。

        :param estimate_complete_time: The estimate_complete_time of this BaselineInstance.
        :type estimate_complete_time: int
        """
        self._estimate_complete_time = estimate_complete_time

    @property
    def expect_time(self):
        r"""Gets the expect_time of this BaselineInstance.

        实例预警时间戳，单位毫秒。

        :return: The expect_time of this BaselineInstance.
        :rtype: int
        """
        return self._expect_time

    @expect_time.setter
    def expect_time(self, expect_time):
        r"""Sets the expect_time of this BaselineInstance.

        实例预警时间戳，单位毫秒。

        :param expect_time: The expect_time of this BaselineInstance.
        :type expect_time: int
        """
        self._expect_time = expect_time

    @property
    def finish_status(self):
        r"""Gets the finish_status of this BaselineInstance.

        基线实例是否完成。

        :return: The finish_status of this BaselineInstance.
        :rtype: str
        """
        return self._finish_status

    @finish_status.setter
    def finish_status(self, finish_status):
        r"""Sets the finish_status of this BaselineInstance.

        基线实例是否完成。

        :param finish_status: The finish_status of this BaselineInstance.
        :type finish_status: str
        """
        self._finish_status = finish_status

    @property
    def start_time(self):
        r"""Gets the start_time of this BaselineInstance.

        基线实例开始时间戳，单位毫秒。

        :return: The start_time of this BaselineInstance.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this BaselineInstance.

        基线实例开始时间戳，单位毫秒。

        :param start_time: The start_time of this BaselineInstance.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this BaselineInstance.

        基线实例结束时间戳，单位毫秒，finish_status（基线实例完成状态）为FINISH（已完成）时，返回基线实例的完成时间戳。

        :return: The end_time of this BaselineInstance.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this BaselineInstance.

        基线实例结束时间戳，单位毫秒，finish_status（基线实例完成状态）为FINISH（已完成）时，返回基线实例的完成时间戳。

        :param end_time: The end_time of this BaselineInstance.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def execute_time(self):
        r"""Gets the execute_time of this BaselineInstance.

        运行时间戳，单位毫秒。

        :return: The execute_time of this BaselineInstance.
        :rtype: int
        """
        return self._execute_time

    @execute_time.setter
    def execute_time(self, execute_time):
        r"""Sets the execute_time of this BaselineInstance.

        运行时间戳，单位毫秒。

        :param execute_time: The execute_time of this BaselineInstance.
        :type execute_time: int
        """
        self._execute_time = execute_time

    @property
    def error_code(self):
        r"""Gets the error_code of this BaselineInstance.

        错误编码。

        :return: The error_code of this BaselineInstance.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this BaselineInstance.

        错误编码。

        :param error_code: The error_code of this BaselineInstance.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this BaselineInstance.

        错误信息。

        :return: The error_message of this BaselineInstance.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this BaselineInstance.

        错误信息。

        :param error_message: The error_message of this BaselineInstance.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def task_instances(self):
        r"""Gets the task_instances of this BaselineInstance.

        任务实例信息。

        :return: The task_instances of this BaselineInstance.
        :rtype: object
        """
        return self._task_instances

    @task_instances.setter
    def task_instances(self, task_instances):
        r"""Sets the task_instances of this BaselineInstance.

        任务实例信息。

        :param task_instances: The task_instances of this BaselineInstance.
        :type task_instances: object
        """
        self._task_instances = task_instances

    @property
    def owner_id(self):
        r"""Gets the owner_id of this BaselineInstance.

        责任人用户ID。

        :return: The owner_id of this BaselineInstance.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this BaselineInstance.

        责任人用户ID。

        :param owner_id: The owner_id of this BaselineInstance.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def owner_name(self):
        r"""Gets the owner_name of this BaselineInstance.

        责任人用户名称。

        :return: The owner_name of this BaselineInstance.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        r"""Sets the owner_name of this BaselineInstance.

        责任人用户名称。

        :param owner_name: The owner_name of this BaselineInstance.
        :type owner_name: str
        """
        self._owner_name = owner_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this BaselineInstance.

        责任人租户ID。

        :return: The domain_id of this BaselineInstance.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this BaselineInstance.

        责任人租户ID。

        :param domain_id: The domain_id of this BaselineInstance.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this BaselineInstance.

        责任人租户名称。

        :return: The domain_name of this BaselineInstance.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this BaselineInstance.

        责任人租户名称。

        :param domain_name: The domain_name of this BaselineInstance.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def project_id(self):
        r"""Gets the project_id of this BaselineInstance.

        项目ID。

        :return: The project_id of this BaselineInstance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this BaselineInstance.

        项目ID。

        :param project_id: The project_id of this BaselineInstance.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BaselineInstance.

        DataArts Studio实例ID。

        :return: The instance_id of this BaselineInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BaselineInstance.

        DataArts Studio实例ID。

        :param instance_id: The instance_id of this BaselineInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this BaselineInstance.

        工作空间ID。

        :return: The workspace_id of this BaselineInstance.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this BaselineInstance.

        工作空间ID。

        :param workspace_id: The workspace_id of this BaselineInstance.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def first_alarm_time(self):
        r"""Gets the first_alarm_time of this BaselineInstance.

        首次告警时间戳，单位毫秒。

        :return: The first_alarm_time of this BaselineInstance.
        :rtype: int
        """
        return self._first_alarm_time

    @first_alarm_time.setter
    def first_alarm_time(self, first_alarm_time):
        r"""Sets the first_alarm_time of this BaselineInstance.

        首次告警时间戳，单位毫秒。

        :param first_alarm_time: The first_alarm_time of this BaselineInstance.
        :type first_alarm_time: int
        """
        self._first_alarm_time = first_alarm_time

    @property
    def last_alarm_time(self):
        r"""Gets the last_alarm_time of this BaselineInstance.

        最后告警时间戳，单位毫秒。

        :return: The last_alarm_time of this BaselineInstance.
        :rtype: int
        """
        return self._last_alarm_time

    @last_alarm_time.setter
    def last_alarm_time(self, last_alarm_time):
        r"""Sets the last_alarm_time of this BaselineInstance.

        最后告警时间戳，单位毫秒。

        :param last_alarm_time: The last_alarm_time of this BaselineInstance.
        :type last_alarm_time: int
        """
        self._last_alarm_time = last_alarm_time

    @property
    def sla_time(self):
        r"""Gets the sla_time of this BaselineInstance.

        实例承诺时间戳，单位毫秒。

        :return: The sla_time of this BaselineInstance.
        :rtype: int
        """
        return self._sla_time

    @sla_time.setter
    def sla_time(self, sla_time):
        r"""Sets the sla_time of this BaselineInstance.

        实例承诺时间戳，单位毫秒。

        :param sla_time: The sla_time of this BaselineInstance.
        :type sla_time: int
        """
        self._sla_time = sla_time

    @property
    def process_time(self):
        r"""Gets the process_time of this BaselineInstance.

        处理时间戳，单位毫秒。

        :return: The process_time of this BaselineInstance.
        :rtype: int
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        r"""Sets the process_time of this BaselineInstance.

        处理时间戳，单位毫秒。

        :param process_time: The process_time of this BaselineInstance.
        :type process_time: int
        """
        self._process_time = process_time

    @property
    def recover_time(self):
        r"""Gets the recover_time of this BaselineInstance.

        恢复时间戳，单位毫秒。

        :return: The recover_time of this BaselineInstance.
        :rtype: int
        """
        return self._recover_time

    @recover_time.setter
    def recover_time(self, recover_time):
        r"""Sets the recover_time of this BaselineInstance.

        恢复时间戳，单位毫秒。

        :param recover_time: The recover_time of this BaselineInstance.
        :type recover_time: int
        """
        self._recover_time = recover_time

    @property
    def ignore_time(self):
        r"""Gets the ignore_time of this BaselineInstance.

        忽略时间戳，单位毫秒。

        :return: The ignore_time of this BaselineInstance.
        :rtype: int
        """
        return self._ignore_time

    @ignore_time.setter
    def ignore_time(self, ignore_time):
        r"""Sets the ignore_time of this BaselineInstance.

        忽略时间戳，单位毫秒。

        :param ignore_time: The ignore_time of this BaselineInstance.
        :type ignore_time: int
        """
        self._ignore_time = ignore_time

    @property
    def process_buffer(self):
        r"""Gets the process_buffer of this BaselineInstance.

        处理时长，设置处理时间所需要的时间，设置后在该时间段内将暂停事件报警，事件的处理操作记录会被记录。

        :return: The process_buffer of this BaselineInstance.
        :rtype: int
        """
        return self._process_buffer

    @process_buffer.setter
    def process_buffer(self, process_buffer):
        r"""Sets the process_buffer of this BaselineInstance.

        处理时长，设置处理时间所需要的时间，设置后在该时间段内将暂停事件报警，事件的处理操作记录会被记录。

        :param process_buffer: The process_buffer of this BaselineInstance.
        :type process_buffer: int
        """
        self._process_buffer = process_buffer

    @property
    def create_day(self):
        r"""Gets the create_day of this BaselineInstance.

        创建时间的天数，表示一年的第几天。

        :return: The create_day of this BaselineInstance.
        :rtype: int
        """
        return self._create_day

    @create_day.setter
    def create_day(self, create_day):
        r"""Sets the create_day of this BaselineInstance.

        创建时间的天数，表示一年的第几天。

        :param create_day: The create_day of this BaselineInstance.
        :type create_day: int
        """
        self._create_day = create_day

    @property
    def instance_type(self):
        r"""Gets the instance_type of this BaselineInstance.

        实例类型。

        :return: The instance_type of this BaselineInstance.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this BaselineInstance.

        实例类型。

        :param instance_type: The instance_type of this BaselineInstance.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def process_user_id(self):
        r"""Gets the process_user_id of this BaselineInstance.

        基线处理人用户ID。

        :return: The process_user_id of this BaselineInstance.
        :rtype: str
        """
        return self._process_user_id

    @process_user_id.setter
    def process_user_id(self, process_user_id):
        r"""Sets the process_user_id of this BaselineInstance.

        基线处理人用户ID。

        :param process_user_id: The process_user_id of this BaselineInstance.
        :type process_user_id: str
        """
        self._process_user_id = process_user_id

    @property
    def process_user_name(self):
        r"""Gets the process_user_name of this BaselineInstance.

        基线处理人用户名称。

        :return: The process_user_name of this BaselineInstance.
        :rtype: str
        """
        return self._process_user_name

    @process_user_name.setter
    def process_user_name(self, process_user_name):
        r"""Sets the process_user_name of this BaselineInstance.

        基线处理人用户名称。

        :param process_user_name: The process_user_name of this BaselineInstance.
        :type process_user_name: str
        """
        self._process_user_name = process_user_name

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
        if not isinstance(other, BaselineInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
