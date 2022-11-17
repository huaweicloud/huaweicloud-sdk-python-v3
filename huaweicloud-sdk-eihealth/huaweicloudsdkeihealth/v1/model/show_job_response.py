# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobResponse(SdkResponse):

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
        'name': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'priority': 'int',
        'timeout': 'int',
        'output_dir': 'str',
        'status': 'str',
        'create_time': 'str',
        'finish_time': 'str',
        'failed_message': 'str',
        'failed_reason': 'str',
        'tool_info': 'ToolInfoDto',
        'tasks': 'list[TaskDefinitionDto]',
        'task_runtime_info': 'list[TaskRuntimeDto]',
        'dag': 'dict(str, dict(str, str))',
        'io_acc_expected_usage': 'int',
        'io_acc_info': 'IoAccInfoDto',
        'node_labels': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'labels': 'labels',
        'priority': 'priority',
        'timeout': 'timeout',
        'output_dir': 'output_dir',
        'status': 'status',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'failed_message': 'failed_message',
        'failed_reason': 'failed_reason',
        'tool_info': 'tool_info',
        'tasks': 'tasks',
        'task_runtime_info': 'task_runtime_info',
        'dag': 'dag',
        'io_acc_expected_usage': 'io_acc_expected_usage',
        'io_acc_info': 'io_acc_info',
        'node_labels': 'node_labels'
    }

    def __init__(self, id=None, name=None, description=None, labels=None, priority=None, timeout=None, output_dir=None, status=None, create_time=None, finish_time=None, failed_message=None, failed_reason=None, tool_info=None, tasks=None, task_runtime_info=None, dag=None, io_acc_expected_usage=None, io_acc_info=None, node_labels=None):
        """ShowJobResponse

        The model defined in huaweicloud sdk

        :param id: 作业id
        :type id: str
        :param name: 作业的名称
        :type name: str
        :param description: 作业的描述
        :type description: str
        :param labels: 作业标签
        :type labels: list[str]
        :param priority: 作业的优先级
        :type priority: int
        :param timeout: 作业执行超时时长
        :type timeout: int
        :param output_dir: 压扁后的效果，即job运行的实际配置
        :type output_dir: str
        :param status: 作业运行状态
        :type status: str
        :param create_time: 作业创建时间
        :type create_time: str
        :param finish_time: 作业完成时间
        :type finish_time: str
        :param failed_message: 作业运行失败描述信息，当作业执行失败时会返回
        :type failed_message: str
        :param failed_reason: 作业运行失败原因，当作业执行失败时会返回
        :type failed_reason: str
        :param tool_info: 
        :type tool_info: :class:`huaweicloudsdkeihealth.v1.ToolInfoDto`
        :param tasks: 基于替换规则压扁后的效果，即job运行的实际配置
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.TaskDefinitionDto`]
        :param task_runtime_info: 作业子步骤的运行信息
        :type task_runtime_info: list[:class:`huaweicloudsdkeihealth.v1.TaskRuntimeDto`]
        :param dag: 作业子步骤的依赖关系
        :type dag: dict(str, dict(str, str))
        :param io_acc_expected_usage: 作业使用的SFS-Turbo实例预期占用存储量，单位G，用于投递作业时评估当前加速实例余量是否充足
        :type io_acc_expected_usage: int
        :param io_acc_info: 
        :type io_acc_info: :class:`huaweicloudsdkeihealth.v1.IoAccInfoDto`
        :param node_labels: 计算节点标签
        :type node_labels: list[str]
        """
        
        super(ShowJobResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._labels = None
        self._priority = None
        self._timeout = None
        self._output_dir = None
        self._status = None
        self._create_time = None
        self._finish_time = None
        self._failed_message = None
        self._failed_reason = None
        self._tool_info = None
        self._tasks = None
        self._task_runtime_info = None
        self._dag = None
        self._io_acc_expected_usage = None
        self._io_acc_info = None
        self._node_labels = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if priority is not None:
            self.priority = priority
        if timeout is not None:
            self.timeout = timeout
        if output_dir is not None:
            self.output_dir = output_dir
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if failed_message is not None:
            self.failed_message = failed_message
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if tool_info is not None:
            self.tool_info = tool_info
        if tasks is not None:
            self.tasks = tasks
        if task_runtime_info is not None:
            self.task_runtime_info = task_runtime_info
        if dag is not None:
            self.dag = dag
        if io_acc_expected_usage is not None:
            self.io_acc_expected_usage = io_acc_expected_usage
        if io_acc_info is not None:
            self.io_acc_info = io_acc_info
        if node_labels is not None:
            self.node_labels = node_labels

    @property
    def id(self):
        """Gets the id of this ShowJobResponse.

        作业id

        :return: The id of this ShowJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowJobResponse.

        作业id

        :param id: The id of this ShowJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowJobResponse.

        作业的名称

        :return: The name of this ShowJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowJobResponse.

        作业的名称

        :param name: The name of this ShowJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowJobResponse.

        作业的描述

        :return: The description of this ShowJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowJobResponse.

        作业的描述

        :param description: The description of this ShowJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this ShowJobResponse.

        作业标签

        :return: The labels of this ShowJobResponse.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ShowJobResponse.

        作业标签

        :param labels: The labels of this ShowJobResponse.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def priority(self):
        """Gets the priority of this ShowJobResponse.

        作业的优先级

        :return: The priority of this ShowJobResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ShowJobResponse.

        作业的优先级

        :param priority: The priority of this ShowJobResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def timeout(self):
        """Gets the timeout of this ShowJobResponse.

        作业执行超时时长

        :return: The timeout of this ShowJobResponse.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ShowJobResponse.

        作业执行超时时长

        :param timeout: The timeout of this ShowJobResponse.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def output_dir(self):
        """Gets the output_dir of this ShowJobResponse.

        压扁后的效果，即job运行的实际配置

        :return: The output_dir of this ShowJobResponse.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        """Sets the output_dir of this ShowJobResponse.

        压扁后的效果，即job运行的实际配置

        :param output_dir: The output_dir of this ShowJobResponse.
        :type output_dir: str
        """
        self._output_dir = output_dir

    @property
    def status(self):
        """Gets the status of this ShowJobResponse.

        作业运行状态

        :return: The status of this ShowJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJobResponse.

        作业运行状态

        :param status: The status of this ShowJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this ShowJobResponse.

        作业创建时间

        :return: The create_time of this ShowJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowJobResponse.

        作业创建时间

        :param create_time: The create_time of this ShowJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        """Gets the finish_time of this ShowJobResponse.

        作业完成时间

        :return: The finish_time of this ShowJobResponse.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this ShowJobResponse.

        作业完成时间

        :param finish_time: The finish_time of this ShowJobResponse.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def failed_message(self):
        """Gets the failed_message of this ShowJobResponse.

        作业运行失败描述信息，当作业执行失败时会返回

        :return: The failed_message of this ShowJobResponse.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        """Sets the failed_message of this ShowJobResponse.

        作业运行失败描述信息，当作业执行失败时会返回

        :param failed_message: The failed_message of this ShowJobResponse.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def failed_reason(self):
        """Gets the failed_reason of this ShowJobResponse.

        作业运行失败原因，当作业执行失败时会返回

        :return: The failed_reason of this ShowJobResponse.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this ShowJobResponse.

        作业运行失败原因，当作业执行失败时会返回

        :param failed_reason: The failed_reason of this ShowJobResponse.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def tool_info(self):
        """Gets the tool_info of this ShowJobResponse.

        :return: The tool_info of this ShowJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ToolInfoDto`
        """
        return self._tool_info

    @tool_info.setter
    def tool_info(self, tool_info):
        """Sets the tool_info of this ShowJobResponse.

        :param tool_info: The tool_info of this ShowJobResponse.
        :type tool_info: :class:`huaweicloudsdkeihealth.v1.ToolInfoDto`
        """
        self._tool_info = tool_info

    @property
    def tasks(self):
        """Gets the tasks of this ShowJobResponse.

        基于替换规则压扁后的效果，即job运行的实际配置

        :return: The tasks of this ShowJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TaskDefinitionDto`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ShowJobResponse.

        基于替换规则压扁后的效果，即job运行的实际配置

        :param tasks: The tasks of this ShowJobResponse.
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.TaskDefinitionDto`]
        """
        self._tasks = tasks

    @property
    def task_runtime_info(self):
        """Gets the task_runtime_info of this ShowJobResponse.

        作业子步骤的运行信息

        :return: The task_runtime_info of this ShowJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.TaskRuntimeDto`]
        """
        return self._task_runtime_info

    @task_runtime_info.setter
    def task_runtime_info(self, task_runtime_info):
        """Sets the task_runtime_info of this ShowJobResponse.

        作业子步骤的运行信息

        :param task_runtime_info: The task_runtime_info of this ShowJobResponse.
        :type task_runtime_info: list[:class:`huaweicloudsdkeihealth.v1.TaskRuntimeDto`]
        """
        self._task_runtime_info = task_runtime_info

    @property
    def dag(self):
        """Gets the dag of this ShowJobResponse.

        作业子步骤的依赖关系

        :return: The dag of this ShowJobResponse.
        :rtype: dict(str, dict(str, str))
        """
        return self._dag

    @dag.setter
    def dag(self, dag):
        """Sets the dag of this ShowJobResponse.

        作业子步骤的依赖关系

        :param dag: The dag of this ShowJobResponse.
        :type dag: dict(str, dict(str, str))
        """
        self._dag = dag

    @property
    def io_acc_expected_usage(self):
        """Gets the io_acc_expected_usage of this ShowJobResponse.

        作业使用的SFS-Turbo实例预期占用存储量，单位G，用于投递作业时评估当前加速实例余量是否充足

        :return: The io_acc_expected_usage of this ShowJobResponse.
        :rtype: int
        """
        return self._io_acc_expected_usage

    @io_acc_expected_usage.setter
    def io_acc_expected_usage(self, io_acc_expected_usage):
        """Sets the io_acc_expected_usage of this ShowJobResponse.

        作业使用的SFS-Turbo实例预期占用存储量，单位G，用于投递作业时评估当前加速实例余量是否充足

        :param io_acc_expected_usage: The io_acc_expected_usage of this ShowJobResponse.
        :type io_acc_expected_usage: int
        """
        self._io_acc_expected_usage = io_acc_expected_usage

    @property
    def io_acc_info(self):
        """Gets the io_acc_info of this ShowJobResponse.

        :return: The io_acc_info of this ShowJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.IoAccInfoDto`
        """
        return self._io_acc_info

    @io_acc_info.setter
    def io_acc_info(self, io_acc_info):
        """Sets the io_acc_info of this ShowJobResponse.

        :param io_acc_info: The io_acc_info of this ShowJobResponse.
        :type io_acc_info: :class:`huaweicloudsdkeihealth.v1.IoAccInfoDto`
        """
        self._io_acc_info = io_acc_info

    @property
    def node_labels(self):
        """Gets the node_labels of this ShowJobResponse.

        计算节点标签

        :return: The node_labels of this ShowJobResponse.
        :rtype: list[str]
        """
        return self._node_labels

    @node_labels.setter
    def node_labels(self, node_labels):
        """Sets the node_labels of this ShowJobResponse.

        计算节点标签

        :param node_labels: The node_labels of this ShowJobResponse.
        :type node_labels: list[str]
        """
        self._node_labels = node_labels

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
        if not isinstance(other, ShowJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
