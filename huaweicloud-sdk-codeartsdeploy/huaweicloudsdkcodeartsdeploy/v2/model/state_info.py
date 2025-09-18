# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'nick_name': 'str',
        'record_id': 'str',
        'task_id': 'str',
        'step': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'executor': 'str',
        'task_name': 'str',
        'step_state': 'list[StepInfo]'
    }

    attribute_map = {
        'status': 'status',
        'nick_name': 'nick_name',
        'record_id': 'record_id',
        'task_id': 'task_id',
        'step': 'step',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'executor': 'executor',
        'task_name': 'task_name',
        'step_state': 'step_state'
    }

    def __init__(self, status=None, nick_name=None, record_id=None, task_id=None, step=None, start_time=None, end_time=None, executor=None, task_name=None, step_state=None):
        r"""StateInfo

        The model defined in huaweicloud sdk

        :param status: 任务执行状态
        :type status: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param record_id: 执行记录id
        :type record_id: str
        :param task_id: 任务id
        :type task_id: str
        :param step: 步骤状态
        :type step: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        :param executor: 执行人
        :type executor: str
        :param task_name: 任务名称
        :type task_name: str
        :param step_state: 子步骤信息
        :type step_state: list[:class:`huaweicloudsdkcodeartsdeploy.v2.StepInfo`]
        """
        
        

        self._status = None
        self._nick_name = None
        self._record_id = None
        self._task_id = None
        self._step = None
        self._start_time = None
        self._end_time = None
        self._executor = None
        self._task_name = None
        self._step_state = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if nick_name is not None:
            self.nick_name = nick_name
        if record_id is not None:
            self.record_id = record_id
        if task_id is not None:
            self.task_id = task_id
        if step is not None:
            self.step = step
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if executor is not None:
            self.executor = executor
        if task_name is not None:
            self.task_name = task_name
        if step_state is not None:
            self.step_state = step_state

    @property
    def status(self):
        r"""Gets the status of this StateInfo.

        任务执行状态

        :return: The status of this StateInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this StateInfo.

        任务执行状态

        :param status: The status of this StateInfo.
        :type status: str
        """
        self._status = status

    @property
    def nick_name(self):
        r"""Gets the nick_name of this StateInfo.

        用户昵称

        :return: The nick_name of this StateInfo.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this StateInfo.

        用户昵称

        :param nick_name: The nick_name of this StateInfo.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def record_id(self):
        r"""Gets the record_id of this StateInfo.

        执行记录id

        :return: The record_id of this StateInfo.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        r"""Sets the record_id of this StateInfo.

        执行记录id

        :param record_id: The record_id of this StateInfo.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def task_id(self):
        r"""Gets the task_id of this StateInfo.

        任务id

        :return: The task_id of this StateInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this StateInfo.

        任务id

        :param task_id: The task_id of this StateInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def step(self):
        r"""Gets the step of this StateInfo.

        步骤状态

        :return: The step of this StateInfo.
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this StateInfo.

        步骤状态

        :param step: The step of this StateInfo.
        :type step: str
        """
        self._step = step

    @property
    def start_time(self):
        r"""Gets the start_time of this StateInfo.

        开始时间

        :return: The start_time of this StateInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this StateInfo.

        开始时间

        :param start_time: The start_time of this StateInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this StateInfo.

        结束时间

        :return: The end_time of this StateInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this StateInfo.

        结束时间

        :param end_time: The end_time of this StateInfo.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def executor(self):
        r"""Gets the executor of this StateInfo.

        执行人

        :return: The executor of this StateInfo.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        r"""Sets the executor of this StateInfo.

        执行人

        :param executor: The executor of this StateInfo.
        :type executor: str
        """
        self._executor = executor

    @property
    def task_name(self):
        r"""Gets the task_name of this StateInfo.

        任务名称

        :return: The task_name of this StateInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this StateInfo.

        任务名称

        :param task_name: The task_name of this StateInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def step_state(self):
        r"""Gets the step_state of this StateInfo.

        子步骤信息

        :return: The step_state of this StateInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.StepInfo`]
        """
        return self._step_state

    @step_state.setter
    def step_state(self, step_state):
        r"""Sets the step_state of this StateInfo.

        子步骤信息

        :param step_state: The step_state of this StateInfo.
        :type step_state: list[:class:`huaweicloudsdkcodeartsdeploy.v2.StepInfo`]
        """
        self._step_state = step_state

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
        if not isinstance(other, StateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
