# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowTodo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'duration': 'int',
        'workflow_id': 'str',
        'workflow_name': 'str',
        'execution_id': 'str',
        'step_name': 'str',
        'step_title': 'str',
        'status': 'str'
    }

    attribute_map = {
        'time': 'time',
        'duration': 'duration',
        'workflow_id': 'workflow_id',
        'workflow_name': 'workflow_name',
        'execution_id': 'execution_id',
        'step_name': 'step_name',
        'step_title': 'step_title',
        'status': 'status'
    }

    def __init__(self, time=None, duration=None, workflow_id=None, workflow_name=None, execution_id=None, step_name=None, step_title=None, status=None):
        r"""WorkflowTodo

        The model defined in huaweicloud sdk

        :param time: 时间。
        :type time: str
        :param duration: 运行时长。
        :type duration: int
        :param workflow_id: Workflow工作流ID。
        :type workflow_id: str
        :param workflow_name: 工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。
        :type workflow_name: str
        :param execution_id: 工作流执行ID。
        :type execution_id: str
        :param step_name: 节点名称。
        :type step_name: str
        :param step_title: 节点的Title。
        :type step_title: str
        :param status: 状态。
        :type status: str
        """
        
        

        self._time = None
        self._duration = None
        self._workflow_id = None
        self._workflow_name = None
        self._execution_id = None
        self._step_name = None
        self._step_title = None
        self._status = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if duration is not None:
            self.duration = duration
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if workflow_name is not None:
            self.workflow_name = workflow_name
        if execution_id is not None:
            self.execution_id = execution_id
        if step_name is not None:
            self.step_name = step_name
        if step_title is not None:
            self.step_title = step_title
        if status is not None:
            self.status = status

    @property
    def time(self):
        r"""Gets the time of this WorkflowTodo.

        时间。

        :return: The time of this WorkflowTodo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this WorkflowTodo.

        时间。

        :param time: The time of this WorkflowTodo.
        :type time: str
        """
        self._time = time

    @property
    def duration(self):
        r"""Gets the duration of this WorkflowTodo.

        运行时长。

        :return: The duration of this WorkflowTodo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this WorkflowTodo.

        运行时长。

        :param duration: The duration of this WorkflowTodo.
        :type duration: int
        """
        self._duration = duration

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this WorkflowTodo.

        Workflow工作流ID。

        :return: The workflow_id of this WorkflowTodo.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this WorkflowTodo.

        Workflow工作流ID。

        :param workflow_id: The workflow_id of this WorkflowTodo.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def workflow_name(self):
        r"""Gets the workflow_name of this WorkflowTodo.

        工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :return: The workflow_name of this WorkflowTodo.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        r"""Sets the workflow_name of this WorkflowTodo.

        工作流名称。填写1-64位，仅包含英文、数字、下划线（_）和中划线（-），并且以英文开头的名称。

        :param workflow_name: The workflow_name of this WorkflowTodo.
        :type workflow_name: str
        """
        self._workflow_name = workflow_name

    @property
    def execution_id(self):
        r"""Gets the execution_id of this WorkflowTodo.

        工作流执行ID。

        :return: The execution_id of this WorkflowTodo.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this WorkflowTodo.

        工作流执行ID。

        :param execution_id: The execution_id of this WorkflowTodo.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def step_name(self):
        r"""Gets the step_name of this WorkflowTodo.

        节点名称。

        :return: The step_name of this WorkflowTodo.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        r"""Sets the step_name of this WorkflowTodo.

        节点名称。

        :param step_name: The step_name of this WorkflowTodo.
        :type step_name: str
        """
        self._step_name = step_name

    @property
    def step_title(self):
        r"""Gets the step_title of this WorkflowTodo.

        节点的Title。

        :return: The step_title of this WorkflowTodo.
        :rtype: str
        """
        return self._step_title

    @step_title.setter
    def step_title(self, step_title):
        r"""Sets the step_title of this WorkflowTodo.

        节点的Title。

        :param step_title: The step_title of this WorkflowTodo.
        :type step_title: str
        """
        self._step_title = step_title

    @property
    def status(self):
        r"""Gets the status of this WorkflowTodo.

        状态。

        :return: The status of this WorkflowTodo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WorkflowTodo.

        状态。

        :param status: The status of this WorkflowTodo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, WorkflowTodo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
