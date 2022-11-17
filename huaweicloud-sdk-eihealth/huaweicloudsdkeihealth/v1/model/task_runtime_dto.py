# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskRuntimeDto:

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
        'create_time': 'str',
        'finish_time': 'str',
        'actual_running_time': 'int',
        'status': 'str',
        'sub_tasks': 'list[SubTaskRuntimeDto]'
    }

    attribute_map = {
        'task_name': 'task_name',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'actual_running_time': 'actual_running_time',
        'status': 'status',
        'sub_tasks': 'sub_tasks'
    }

    def __init__(self, task_name=None, create_time=None, finish_time=None, actual_running_time=None, status=None, sub_tasks=None):
        """TaskRuntimeDto

        The model defined in huaweicloud sdk

        :param task_name: 作业子任务名称
        :type task_name: str
        :param create_time: 作业子任务运行创建时间
        :type create_time: str
        :param finish_time: 作业子任务运行结束时间
        :type finish_time: str
        :param actual_running_time: 作业子任务实际运行时间
        :type actual_running_time: int
        :param status: 作业子任务运行状态
        :type status: str
        :param sub_tasks: 作业子任务的并发实例列表
        :type sub_tasks: list[:class:`huaweicloudsdkeihealth.v1.SubTaskRuntimeDto`]
        """
        
        

        self._task_name = None
        self._create_time = None
        self._finish_time = None
        self._actual_running_time = None
        self._status = None
        self._sub_tasks = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if actual_running_time is not None:
            self.actual_running_time = actual_running_time
        if status is not None:
            self.status = status
        if sub_tasks is not None:
            self.sub_tasks = sub_tasks

    @property
    def task_name(self):
        """Gets the task_name of this TaskRuntimeDto.

        作业子任务名称

        :return: The task_name of this TaskRuntimeDto.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskRuntimeDto.

        作业子任务名称

        :param task_name: The task_name of this TaskRuntimeDto.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def create_time(self):
        """Gets the create_time of this TaskRuntimeDto.

        作业子任务运行创建时间

        :return: The create_time of this TaskRuntimeDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TaskRuntimeDto.

        作业子任务运行创建时间

        :param create_time: The create_time of this TaskRuntimeDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        """Gets the finish_time of this TaskRuntimeDto.

        作业子任务运行结束时间

        :return: The finish_time of this TaskRuntimeDto.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this TaskRuntimeDto.

        作业子任务运行结束时间

        :param finish_time: The finish_time of this TaskRuntimeDto.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def actual_running_time(self):
        """Gets the actual_running_time of this TaskRuntimeDto.

        作业子任务实际运行时间

        :return: The actual_running_time of this TaskRuntimeDto.
        :rtype: int
        """
        return self._actual_running_time

    @actual_running_time.setter
    def actual_running_time(self, actual_running_time):
        """Sets the actual_running_time of this TaskRuntimeDto.

        作业子任务实际运行时间

        :param actual_running_time: The actual_running_time of this TaskRuntimeDto.
        :type actual_running_time: int
        """
        self._actual_running_time = actual_running_time

    @property
    def status(self):
        """Gets the status of this TaskRuntimeDto.

        作业子任务运行状态

        :return: The status of this TaskRuntimeDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskRuntimeDto.

        作业子任务运行状态

        :param status: The status of this TaskRuntimeDto.
        :type status: str
        """
        self._status = status

    @property
    def sub_tasks(self):
        """Gets the sub_tasks of this TaskRuntimeDto.

        作业子任务的并发实例列表

        :return: The sub_tasks of this TaskRuntimeDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.SubTaskRuntimeDto`]
        """
        return self._sub_tasks

    @sub_tasks.setter
    def sub_tasks(self, sub_tasks):
        """Sets the sub_tasks of this TaskRuntimeDto.

        作业子任务的并发实例列表

        :param sub_tasks: The sub_tasks of this TaskRuntimeDto.
        :type sub_tasks: list[:class:`huaweicloudsdkeihealth.v1.SubTaskRuntimeDto`]
        """
        self._sub_tasks = sub_tasks

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
        if not isinstance(other, TaskRuntimeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
