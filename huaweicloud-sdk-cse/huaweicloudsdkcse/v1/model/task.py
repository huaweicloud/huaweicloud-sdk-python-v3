# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Task:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'int',
        'id': 'int',
        'type': 'str',
        'assigned': 'str',
        'task_name': 'str',
        'engine_name': 'str',
        'task_order': 'int',
        'status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'create_time': 'int',
        'update_time': 'int',
        'timeout': 'int',
        'log': 'str',
        'output': 'str',
        'task_executor_brief': 'TaskExecutorBrief'
    }

    attribute_map = {
        'job_id': 'jobId',
        'id': 'id',
        'type': 'type',
        'assigned': 'assigned',
        'task_name': 'taskName',
        'engine_name': 'engineName',
        'task_order': 'taskOrder',
        'status': 'status',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'create_time': 'createTime',
        'update_time': 'updateTime',
        'timeout': 'timeout',
        'log': 'log',
        'output': 'output',
        'task_executor_brief': 'taskExecutorBrief'
    }

    def __init__(self, job_id=None, id=None, type=None, assigned=None, task_name=None, engine_name=None, task_order=None, status=None, start_time=None, end_time=None, create_time=None, update_time=None, timeout=None, log=None, output=None, task_executor_brief=None):
        """Task

        The model defined in huaweicloud sdk

        :param job_id: 子任务所属任务ID
        :type job_id: int
        :param id: 子任务ID，使用uuid
        :type id: int
        :param type: 子任务的类型
        :type type: str
        :param assigned: 子任务的执行者
        :type assigned: str
        :param task_name: 子任务名称
        :type task_name: str
        :param engine_name: 子任务所属引擎名称
        :type engine_name: str
        :param task_order: 子任务执行的顺序, 从小到大
        :type task_order: int
        :param status: 子任务状态
        :type status: str
        :param start_time: 子任务开始时间
        :type start_time: int
        :param end_time: 子任务结束时间
        :type end_time: int
        :param create_time: 子任务创建时间
        :type create_time: int
        :param update_time: 子任务更新时间
        :type update_time: int
        :param timeout: 子任务是否超时
        :type timeout: int
        :param log: 子任务详细信息，执行过程中产生的辅助信息
        :type log: str
        :param output: 子任务输出信息
        :type output: str
        :param task_executor_brief: 
        :type task_executor_brief: :class:`huaweicloudsdkcse.v1.TaskExecutorBrief`
        """
        
        

        self._job_id = None
        self._id = None
        self._type = None
        self._assigned = None
        self._task_name = None
        self._engine_name = None
        self._task_order = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._create_time = None
        self._update_time = None
        self._timeout = None
        self._log = None
        self._output = None
        self._task_executor_brief = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if assigned is not None:
            self.assigned = assigned
        if task_name is not None:
            self.task_name = task_name
        if engine_name is not None:
            self.engine_name = engine_name
        if task_order is not None:
            self.task_order = task_order
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if timeout is not None:
            self.timeout = timeout
        if log is not None:
            self.log = log
        if output is not None:
            self.output = output
        if task_executor_brief is not None:
            self.task_executor_brief = task_executor_brief

    @property
    def job_id(self):
        """Gets the job_id of this Task.

        子任务所属任务ID

        :return: The job_id of this Task.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this Task.

        子任务所属任务ID

        :param job_id: The job_id of this Task.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def id(self):
        """Gets the id of this Task.

        子任务ID，使用uuid

        :return: The id of this Task.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Task.

        子任务ID，使用uuid

        :param id: The id of this Task.
        :type id: int
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this Task.

        子任务的类型

        :return: The type of this Task.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Task.

        子任务的类型

        :param type: The type of this Task.
        :type type: str
        """
        self._type = type

    @property
    def assigned(self):
        """Gets the assigned of this Task.

        子任务的执行者

        :return: The assigned of this Task.
        :rtype: str
        """
        return self._assigned

    @assigned.setter
    def assigned(self, assigned):
        """Sets the assigned of this Task.

        子任务的执行者

        :param assigned: The assigned of this Task.
        :type assigned: str
        """
        self._assigned = assigned

    @property
    def task_name(self):
        """Gets the task_name of this Task.

        子任务名称

        :return: The task_name of this Task.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this Task.

        子任务名称

        :param task_name: The task_name of this Task.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def engine_name(self):
        """Gets the engine_name of this Task.

        子任务所属引擎名称

        :return: The engine_name of this Task.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this Task.

        子任务所属引擎名称

        :param engine_name: The engine_name of this Task.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def task_order(self):
        """Gets the task_order of this Task.

        子任务执行的顺序, 从小到大

        :return: The task_order of this Task.
        :rtype: int
        """
        return self._task_order

    @task_order.setter
    def task_order(self, task_order):
        """Sets the task_order of this Task.

        子任务执行的顺序, 从小到大

        :param task_order: The task_order of this Task.
        :type task_order: int
        """
        self._task_order = task_order

    @property
    def status(self):
        """Gets the status of this Task.

        子任务状态

        :return: The status of this Task.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.

        子任务状态

        :param status: The status of this Task.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this Task.

        子任务开始时间

        :return: The start_time of this Task.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this Task.

        子任务开始时间

        :param start_time: The start_time of this Task.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this Task.

        子任务结束时间

        :return: The end_time of this Task.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Task.

        子任务结束时间

        :param end_time: The end_time of this Task.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def create_time(self):
        """Gets the create_time of this Task.

        子任务创建时间

        :return: The create_time of this Task.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Task.

        子任务创建时间

        :param create_time: The create_time of this Task.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Task.

        子任务更新时间

        :return: The update_time of this Task.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Task.

        子任务更新时间

        :param update_time: The update_time of this Task.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def timeout(self):
        """Gets the timeout of this Task.

        子任务是否超时

        :return: The timeout of this Task.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Task.

        子任务是否超时

        :param timeout: The timeout of this Task.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def log(self):
        """Gets the log of this Task.

        子任务详细信息，执行过程中产生的辅助信息

        :return: The log of this Task.
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this Task.

        子任务详细信息，执行过程中产生的辅助信息

        :param log: The log of this Task.
        :type log: str
        """
        self._log = log

    @property
    def output(self):
        """Gets the output of this Task.

        子任务输出信息

        :return: The output of this Task.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this Task.

        子任务输出信息

        :param output: The output of this Task.
        :type output: str
        """
        self._output = output

    @property
    def task_executor_brief(self):
        """Gets the task_executor_brief of this Task.

        :return: The task_executor_brief of this Task.
        :rtype: :class:`huaweicloudsdkcse.v1.TaskExecutorBrief`
        """
        return self._task_executor_brief

    @task_executor_brief.setter
    def task_executor_brief(self, task_executor_brief):
        """Sets the task_executor_brief of this Task.

        :param task_executor_brief: The task_executor_brief of this Task.
        :type task_executor_brief: :class:`huaweicloudsdkcse.v1.TaskExecutorBrief`
        """
        self._task_executor_brief = task_executor_brief

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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
