# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'labels': 'list[str]',
        'priority': 'int',
        'timeout': 'int',
        'output_dir': 'str',
        'tool_id': 'str',
        'tool_type': 'str',
        'tasks': 'list[JobTaskDto]',
        'io_acc_id': 'str',
        'io_acc_expected_usage': 'int',
        'node_labels': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'labels': 'labels',
        'priority': 'priority',
        'timeout': 'timeout',
        'output_dir': 'output_dir',
        'tool_id': 'tool_id',
        'tool_type': 'tool_type',
        'tasks': 'tasks',
        'io_acc_id': 'io_acc_id',
        'io_acc_expected_usage': 'io_acc_expected_usage',
        'node_labels': 'node_labels'
    }

    def __init__(self, name=None, description=None, labels=None, priority=None, timeout=None, output_dir=None, tool_id=None, tool_type=None, tasks=None, io_acc_id=None, io_acc_expected_usage=None, node_labels=None):
        """JobDto

        The model defined in huaweicloud sdk

        :param name: 作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)
        :type name: str
        :param description: 作业的描述,取值范围：输入字符最大长度为255
        :type description: str
        :param labels: 作业标签，取值范围[0,5]，单个标签最大长度32字符，仅仅包含小写字母或数字或大写字母
        :type labels: list[str]
        :param priority: 作业的优先级,取值范围[0,9]，0最低，默认数值0
        :type priority: int
        :param timeout: 作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440
        :type timeout: int
        :param output_dir: job结果存储目录，不指定则在workflow的工作目录下生产job同名子目录，指定则已指定路径为准;必须以/开头，结尾不能有/.;不能包含以下特殊字符\\:*?&lt;\&quot;&gt;|。
        :type output_dir: str
        :param tool_id: 作业依赖的组件id，组件当前仅支持流程，取值范围[1,135]，支持大小写字母和数字。目前支持两种格式，特殊id：{流程名称}::{流程版本}::{源项目名称}；正常id：流程id
        :type tool_id: str
        :param tool_type: 作业依赖的组件类型，仅支持填写workflow
        :type tool_type: str
        :param tasks: 基于替换规则压扁后，job实际的运行信息
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.JobTaskDto`]
        :param io_acc_id: 作业使用的SFS-Turbo实例id，不填表示不使用
        :type io_acc_id: str
        :param io_acc_expected_usage: 作业使用的SFS-Turbo实例预期占用存储量，单位G，用于投递作业时评估当前加速实例余量是否充足
        :type io_acc_expected_usage: int
        :param node_labels: 节点标签 取值范围[0,1]，单个标签最大长度63字符
        :type node_labels: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._labels = None
        self._priority = None
        self._timeout = None
        self._output_dir = None
        self._tool_id = None
        self._tool_type = None
        self._tasks = None
        self._io_acc_id = None
        self._io_acc_expected_usage = None
        self._node_labels = None
        self.discriminator = None

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
        self.tool_id = tool_id
        self.tool_type = tool_type
        if tasks is not None:
            self.tasks = tasks
        if io_acc_id is not None:
            self.io_acc_id = io_acc_id
        if io_acc_expected_usage is not None:
            self.io_acc_expected_usage = io_acc_expected_usage
        if node_labels is not None:
            self.node_labels = node_labels

    @property
    def name(self):
        """Gets the name of this JobDto.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :return: The name of this JobDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobDto.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :param name: The name of this JobDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this JobDto.

        作业的描述,取值范围：输入字符最大长度为255

        :return: The description of this JobDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobDto.

        作业的描述,取值范围：输入字符最大长度为255

        :param description: The description of this JobDto.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this JobDto.

        作业标签，取值范围[0,5]，单个标签最大长度32字符，仅仅包含小写字母或数字或大写字母

        :return: The labels of this JobDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this JobDto.

        作业标签，取值范围[0,5]，单个标签最大长度32字符，仅仅包含小写字母或数字或大写字母

        :param labels: The labels of this JobDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def priority(self):
        """Gets the priority of this JobDto.

        作业的优先级,取值范围[0,9]，0最低，默认数值0

        :return: The priority of this JobDto.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this JobDto.

        作业的优先级,取值范围[0,9]，0最低，默认数值0

        :param priority: The priority of this JobDto.
        :type priority: int
        """
        self._priority = priority

    @property
    def timeout(self):
        """Gets the timeout of this JobDto.

        作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440

        :return: The timeout of this JobDto.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this JobDto.

        作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440

        :param timeout: The timeout of this JobDto.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def output_dir(self):
        """Gets the output_dir of this JobDto.

        job结果存储目录，不指定则在workflow的工作目录下生产job同名子目录，指定则已指定路径为准;必须以/开头，结尾不能有/.;不能包含以下特殊字符\\:*?<\">|。

        :return: The output_dir of this JobDto.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        """Sets the output_dir of this JobDto.

        job结果存储目录，不指定则在workflow的工作目录下生产job同名子目录，指定则已指定路径为准;必须以/开头，结尾不能有/.;不能包含以下特殊字符\\:*?<\">|。

        :param output_dir: The output_dir of this JobDto.
        :type output_dir: str
        """
        self._output_dir = output_dir

    @property
    def tool_id(self):
        """Gets the tool_id of this JobDto.

        作业依赖的组件id，组件当前仅支持流程，取值范围[1,135]，支持大小写字母和数字。目前支持两种格式，特殊id：{流程名称}::{流程版本}::{源项目名称}；正常id：流程id

        :return: The tool_id of this JobDto.
        :rtype: str
        """
        return self._tool_id

    @tool_id.setter
    def tool_id(self, tool_id):
        """Sets the tool_id of this JobDto.

        作业依赖的组件id，组件当前仅支持流程，取值范围[1,135]，支持大小写字母和数字。目前支持两种格式，特殊id：{流程名称}::{流程版本}::{源项目名称}；正常id：流程id

        :param tool_id: The tool_id of this JobDto.
        :type tool_id: str
        """
        self._tool_id = tool_id

    @property
    def tool_type(self):
        """Gets the tool_type of this JobDto.

        作业依赖的组件类型，仅支持填写workflow

        :return: The tool_type of this JobDto.
        :rtype: str
        """
        return self._tool_type

    @tool_type.setter
    def tool_type(self, tool_type):
        """Sets the tool_type of this JobDto.

        作业依赖的组件类型，仅支持填写workflow

        :param tool_type: The tool_type of this JobDto.
        :type tool_type: str
        """
        self._tool_type = tool_type

    @property
    def tasks(self):
        """Gets the tasks of this JobDto.

        基于替换规则压扁后，job实际的运行信息

        :return: The tasks of this JobDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.JobTaskDto`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this JobDto.

        基于替换规则压扁后，job实际的运行信息

        :param tasks: The tasks of this JobDto.
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.JobTaskDto`]
        """
        self._tasks = tasks

    @property
    def io_acc_id(self):
        """Gets the io_acc_id of this JobDto.

        作业使用的SFS-Turbo实例id，不填表示不使用

        :return: The io_acc_id of this JobDto.
        :rtype: str
        """
        return self._io_acc_id

    @io_acc_id.setter
    def io_acc_id(self, io_acc_id):
        """Sets the io_acc_id of this JobDto.

        作业使用的SFS-Turbo实例id，不填表示不使用

        :param io_acc_id: The io_acc_id of this JobDto.
        :type io_acc_id: str
        """
        self._io_acc_id = io_acc_id

    @property
    def io_acc_expected_usage(self):
        """Gets the io_acc_expected_usage of this JobDto.

        作业使用的SFS-Turbo实例预期占用存储量，单位G，用于投递作业时评估当前加速实例余量是否充足

        :return: The io_acc_expected_usage of this JobDto.
        :rtype: int
        """
        return self._io_acc_expected_usage

    @io_acc_expected_usage.setter
    def io_acc_expected_usage(self, io_acc_expected_usage):
        """Sets the io_acc_expected_usage of this JobDto.

        作业使用的SFS-Turbo实例预期占用存储量，单位G，用于投递作业时评估当前加速实例余量是否充足

        :param io_acc_expected_usage: The io_acc_expected_usage of this JobDto.
        :type io_acc_expected_usage: int
        """
        self._io_acc_expected_usage = io_acc_expected_usage

    @property
    def node_labels(self):
        """Gets the node_labels of this JobDto.

        节点标签 取值范围[0,1]，单个标签最大长度63字符

        :return: The node_labels of this JobDto.
        :rtype: list[str]
        """
        return self._node_labels

    @node_labels.setter
    def node_labels(self, node_labels):
        """Sets the node_labels of this JobDto.

        节点标签 取值范围[0,1]，单个标签最大长度63字符

        :param node_labels: The node_labels of this JobDto.
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
        if not isinstance(other, JobDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
