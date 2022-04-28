# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskSteps:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'task_names': 'list[str]',
        'status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'task_executor_brief': 'TaskExecutorBrief',
        'tasks': 'list[Task]'
    }

    attribute_map = {
        'task_name': 'task_name',
        'task_names': 'task_names',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'task_executor_brief': 'task_executor_brief',
        'tasks': 'tasks'
    }

    def __init__(self, task_name=None, task_names=None, status=None, start_time=None, end_time=None, task_executor_brief=None, tasks=None):
        """TaskSteps

        The model defined in huaweicloud sdk

        :param task_name: 处理阶段名称
        :type task_name: str
        :param task_names: 当前处理阶段包含的处理步骤名称列表
        :type task_names: list[str]
        :param status: 处理阶段状态
        :type status: str
        :param start_time: 处理阶段开始时间
        :type start_time: int
        :param end_time: 处理阶段结束时间
        :type end_time: int
        :param task_executor_brief: 
        :type task_executor_brief: :class:`huaweicloudsdkcse.v1.TaskExecutorBrief`
        :param tasks: 处理步骤
        :type tasks: list[:class:`huaweicloudsdkcse.v1.Task`]
        """
        
        

        self._task_name = None
        self._task_names = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._task_executor_brief = None
        self._tasks = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if task_names is not None:
            self.task_names = task_names
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if task_executor_brief is not None:
            self.task_executor_brief = task_executor_brief
        if tasks is not None:
            self.tasks = tasks

    @property
    def task_name(self):
        """Gets the task_name of this TaskSteps.

        处理阶段名称

        :return: The task_name of this TaskSteps.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskSteps.

        处理阶段名称

        :param task_name: The task_name of this TaskSteps.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_names(self):
        """Gets the task_names of this TaskSteps.

        当前处理阶段包含的处理步骤名称列表

        :return: The task_names of this TaskSteps.
        :rtype: list[str]
        """
        return self._task_names

    @task_names.setter
    def task_names(self, task_names):
        """Sets the task_names of this TaskSteps.

        当前处理阶段包含的处理步骤名称列表

        :param task_names: The task_names of this TaskSteps.
        :type task_names: list[str]
        """
        self._task_names = task_names

    @property
    def status(self):
        """Gets the status of this TaskSteps.

        处理阶段状态

        :return: The status of this TaskSteps.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskSteps.

        处理阶段状态

        :param status: The status of this TaskSteps.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this TaskSteps.

        处理阶段开始时间

        :return: The start_time of this TaskSteps.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TaskSteps.

        处理阶段开始时间

        :param start_time: The start_time of this TaskSteps.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TaskSteps.

        处理阶段结束时间

        :return: The end_time of this TaskSteps.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TaskSteps.

        处理阶段结束时间

        :param end_time: The end_time of this TaskSteps.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def task_executor_brief(self):
        """Gets the task_executor_brief of this TaskSteps.


        :return: The task_executor_brief of this TaskSteps.
        :rtype: :class:`huaweicloudsdkcse.v1.TaskExecutorBrief`
        """
        return self._task_executor_brief

    @task_executor_brief.setter
    def task_executor_brief(self, task_executor_brief):
        """Sets the task_executor_brief of this TaskSteps.


        :param task_executor_brief: The task_executor_brief of this TaskSteps.
        :type task_executor_brief: :class:`huaweicloudsdkcse.v1.TaskExecutorBrief`
        """
        self._task_executor_brief = task_executor_brief

    @property
    def tasks(self):
        """Gets the tasks of this TaskSteps.

        处理步骤

        :return: The tasks of this TaskSteps.
        :rtype: list[:class:`huaweicloudsdkcse.v1.Task`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this TaskSteps.

        处理步骤

        :param tasks: The tasks of this TaskSteps.
        :type tasks: list[:class:`huaweicloudsdkcse.v1.Task`]
        """
        self._tasks = tasks

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
        if not isinstance(other, TaskSteps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
