# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNextflowTaskDetailResponse(SdkResponse):

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
        'command': 'str',
        'status': 'str',
        'error_action': 'str',
        'exit': 'int',
        'work_dir': 'str',
        'environment': 'str',
        'module': 'list[str]',
        'container': 'str',
        'attempt': 'int',
        'scratch': 'str',
        'execution_time': 'NextflowTaskExecutionTime',
        'resource_requested': 'NextflowTaskResourceRequested',
        'resource_usage': 'NextflowTaskResourceUsage'
    }

    attribute_map = {
        'id': 'id',
        'command': 'command',
        'status': 'status',
        'error_action': 'error_action',
        'exit': 'exit',
        'work_dir': 'work_dir',
        'environment': 'environment',
        'module': 'module',
        'container': 'container',
        'attempt': 'attempt',
        'scratch': 'scratch',
        'execution_time': 'execution_time',
        'resource_requested': 'resource_requested',
        'resource_usage': 'resource_usage'
    }

    def __init__(self, id=None, command=None, status=None, error_action=None, exit=None, work_dir=None, environment=None, module=None, container=None, attempt=None, scratch=None, execution_time=None, resource_requested=None, resource_usage=None):
        """ShowNextflowTaskDetailResponse

        The model defined in huaweicloud sdk

        :param id: task id
        :type id: str
        :param command: task执行命令
        :type command: str
        :param status: task状态
        :type status: str
        :param error_action: task失败后的策略
        :type error_action: str
        :param exit: task退出状态码
        :type exit: int
        :param work_dir: task执行路径
        :type work_dir: str
        :param environment: task执行的环境变量值
        :type environment: str
        :param module: 子任务运行环境列表
        :type module: list[str]
        :param container: 容器名称
        :type container: str
        :param attempt: 执行次数
        :type attempt: int
        :param scratch: 临时工作目录
        :type scratch: str
        :param execution_time: 
        :type execution_time: :class:`huaweicloudsdkeihealth.v1.NextflowTaskExecutionTime`
        :param resource_requested: 
        :type resource_requested: :class:`huaweicloudsdkeihealth.v1.NextflowTaskResourceRequested`
        :param resource_usage: 
        :type resource_usage: :class:`huaweicloudsdkeihealth.v1.NextflowTaskResourceUsage`
        """
        
        super(ShowNextflowTaskDetailResponse, self).__init__()

        self._id = None
        self._command = None
        self._status = None
        self._error_action = None
        self._exit = None
        self._work_dir = None
        self._environment = None
        self._module = None
        self._container = None
        self._attempt = None
        self._scratch = None
        self._execution_time = None
        self._resource_requested = None
        self._resource_usage = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if command is not None:
            self.command = command
        if status is not None:
            self.status = status
        if error_action is not None:
            self.error_action = error_action
        if exit is not None:
            self.exit = exit
        if work_dir is not None:
            self.work_dir = work_dir
        if environment is not None:
            self.environment = environment
        if module is not None:
            self.module = module
        if container is not None:
            self.container = container
        if attempt is not None:
            self.attempt = attempt
        if scratch is not None:
            self.scratch = scratch
        if execution_time is not None:
            self.execution_time = execution_time
        if resource_requested is not None:
            self.resource_requested = resource_requested
        if resource_usage is not None:
            self.resource_usage = resource_usage

    @property
    def id(self):
        """Gets the id of this ShowNextflowTaskDetailResponse.

        task id

        :return: The id of this ShowNextflowTaskDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowNextflowTaskDetailResponse.

        task id

        :param id: The id of this ShowNextflowTaskDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def command(self):
        """Gets the command of this ShowNextflowTaskDetailResponse.

        task执行命令

        :return: The command of this ShowNextflowTaskDetailResponse.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ShowNextflowTaskDetailResponse.

        task执行命令

        :param command: The command of this ShowNextflowTaskDetailResponse.
        :type command: str
        """
        self._command = command

    @property
    def status(self):
        """Gets the status of this ShowNextflowTaskDetailResponse.

        task状态

        :return: The status of this ShowNextflowTaskDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowNextflowTaskDetailResponse.

        task状态

        :param status: The status of this ShowNextflowTaskDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def error_action(self):
        """Gets the error_action of this ShowNextflowTaskDetailResponse.

        task失败后的策略

        :return: The error_action of this ShowNextflowTaskDetailResponse.
        :rtype: str
        """
        return self._error_action

    @error_action.setter
    def error_action(self, error_action):
        """Sets the error_action of this ShowNextflowTaskDetailResponse.

        task失败后的策略

        :param error_action: The error_action of this ShowNextflowTaskDetailResponse.
        :type error_action: str
        """
        self._error_action = error_action

    @property
    def exit(self):
        """Gets the exit of this ShowNextflowTaskDetailResponse.

        task退出状态码

        :return: The exit of this ShowNextflowTaskDetailResponse.
        :rtype: int
        """
        return self._exit

    @exit.setter
    def exit(self, exit):
        """Sets the exit of this ShowNextflowTaskDetailResponse.

        task退出状态码

        :param exit: The exit of this ShowNextflowTaskDetailResponse.
        :type exit: int
        """
        self._exit = exit

    @property
    def work_dir(self):
        """Gets the work_dir of this ShowNextflowTaskDetailResponse.

        task执行路径

        :return: The work_dir of this ShowNextflowTaskDetailResponse.
        :rtype: str
        """
        return self._work_dir

    @work_dir.setter
    def work_dir(self, work_dir):
        """Sets the work_dir of this ShowNextflowTaskDetailResponse.

        task执行路径

        :param work_dir: The work_dir of this ShowNextflowTaskDetailResponse.
        :type work_dir: str
        """
        self._work_dir = work_dir

    @property
    def environment(self):
        """Gets the environment of this ShowNextflowTaskDetailResponse.

        task执行的环境变量值

        :return: The environment of this ShowNextflowTaskDetailResponse.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this ShowNextflowTaskDetailResponse.

        task执行的环境变量值

        :param environment: The environment of this ShowNextflowTaskDetailResponse.
        :type environment: str
        """
        self._environment = environment

    @property
    def module(self):
        """Gets the module of this ShowNextflowTaskDetailResponse.

        子任务运行环境列表

        :return: The module of this ShowNextflowTaskDetailResponse.
        :rtype: list[str]
        """
        return self._module

    @module.setter
    def module(self, module):
        """Sets the module of this ShowNextflowTaskDetailResponse.

        子任务运行环境列表

        :param module: The module of this ShowNextflowTaskDetailResponse.
        :type module: list[str]
        """
        self._module = module

    @property
    def container(self):
        """Gets the container of this ShowNextflowTaskDetailResponse.

        容器名称

        :return: The container of this ShowNextflowTaskDetailResponse.
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this ShowNextflowTaskDetailResponse.

        容器名称

        :param container: The container of this ShowNextflowTaskDetailResponse.
        :type container: str
        """
        self._container = container

    @property
    def attempt(self):
        """Gets the attempt of this ShowNextflowTaskDetailResponse.

        执行次数

        :return: The attempt of this ShowNextflowTaskDetailResponse.
        :rtype: int
        """
        return self._attempt

    @attempt.setter
    def attempt(self, attempt):
        """Sets the attempt of this ShowNextflowTaskDetailResponse.

        执行次数

        :param attempt: The attempt of this ShowNextflowTaskDetailResponse.
        :type attempt: int
        """
        self._attempt = attempt

    @property
    def scratch(self):
        """Gets the scratch of this ShowNextflowTaskDetailResponse.

        临时工作目录

        :return: The scratch of this ShowNextflowTaskDetailResponse.
        :rtype: str
        """
        return self._scratch

    @scratch.setter
    def scratch(self, scratch):
        """Sets the scratch of this ShowNextflowTaskDetailResponse.

        临时工作目录

        :param scratch: The scratch of this ShowNextflowTaskDetailResponse.
        :type scratch: str
        """
        self._scratch = scratch

    @property
    def execution_time(self):
        """Gets the execution_time of this ShowNextflowTaskDetailResponse.

        :return: The execution_time of this ShowNextflowTaskDetailResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.NextflowTaskExecutionTime`
        """
        return self._execution_time

    @execution_time.setter
    def execution_time(self, execution_time):
        """Sets the execution_time of this ShowNextflowTaskDetailResponse.

        :param execution_time: The execution_time of this ShowNextflowTaskDetailResponse.
        :type execution_time: :class:`huaweicloudsdkeihealth.v1.NextflowTaskExecutionTime`
        """
        self._execution_time = execution_time

    @property
    def resource_requested(self):
        """Gets the resource_requested of this ShowNextflowTaskDetailResponse.

        :return: The resource_requested of this ShowNextflowTaskDetailResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.NextflowTaskResourceRequested`
        """
        return self._resource_requested

    @resource_requested.setter
    def resource_requested(self, resource_requested):
        """Sets the resource_requested of this ShowNextflowTaskDetailResponse.

        :param resource_requested: The resource_requested of this ShowNextflowTaskDetailResponse.
        :type resource_requested: :class:`huaweicloudsdkeihealth.v1.NextflowTaskResourceRequested`
        """
        self._resource_requested = resource_requested

    @property
    def resource_usage(self):
        """Gets the resource_usage of this ShowNextflowTaskDetailResponse.

        :return: The resource_usage of this ShowNextflowTaskDetailResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.NextflowTaskResourceUsage`
        """
        return self._resource_usage

    @resource_usage.setter
    def resource_usage(self, resource_usage):
        """Sets the resource_usage of this ShowNextflowTaskDetailResponse.

        :param resource_usage: The resource_usage of this ShowNextflowTaskDetailResponse.
        :type resource_usage: :class:`huaweicloudsdkeihealth.v1.NextflowTaskResourceUsage`
        """
        self._resource_usage = resource_usage

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
        if not isinstance(other, ShowNextflowTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
