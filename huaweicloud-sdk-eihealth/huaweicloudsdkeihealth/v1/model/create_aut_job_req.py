# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAutJobReq:

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
        'database_id': 'str',
        'database_column': 'str',
        'database_column_type': 'str',
        'clean_database_column': 'bool',
        'database_trigger': 'list[DatabaseTriggerDto]',
        'tool_id': 'str',
        'tool_type': 'str',
        'job_name': 'str',
        'job_name_type': 'JobNameType',
        'job_description': 'str',
        'labels': 'list[str]',
        'priority': 'int',
        'timeout': 'int',
        'output_dir': 'str',
        'output_dir_type': 'str',
        'node_labels': 'list[str]',
        'io_acc_id': 'str',
        'tasks': 'list[JobTaskDto]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'database_id': 'database_id',
        'database_column': 'database_column',
        'database_column_type': 'database_column_type',
        'clean_database_column': 'clean_database_column',
        'database_trigger': 'database_trigger',
        'tool_id': 'tool_id',
        'tool_type': 'tool_type',
        'job_name': 'job_name',
        'job_name_type': 'job_name_type',
        'job_description': 'job_description',
        'labels': 'labels',
        'priority': 'priority',
        'timeout': 'timeout',
        'output_dir': 'output_dir',
        'output_dir_type': 'output_dir_type',
        'node_labels': 'node_labels',
        'io_acc_id': 'io_acc_id',
        'tasks': 'tasks'
    }

    def __init__(self, name=None, description=None, database_id=None, database_column=None, database_column_type=None, clean_database_column=None, database_trigger=None, tool_id=None, tool_type=None, job_name=None, job_name_type=None, job_description=None, labels=None, priority=None, timeout=None, output_dir=None, output_dir_type=None, node_labels=None, io_acc_id=None, tasks=None):
        """CreateAutJobReq

        The model defined in huaweicloud sdk

        :param name: 自动作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)
        :type name: str
        :param description: 自动作业的描述,取值范围：输入字符最大长度为255
        :type description: str
        :param database_id: 自动作业依赖的数据库ID
        :type database_id: str
        :param database_column: 自动作业状态更新列
        :type database_column: str
        :param database_column_type: 自动作业状态更新列的类型，不填默认为EXISTED
        :type database_column_type: str
        :param clean_database_column: 是否清空作业状态更新列
        :type clean_database_column: bool
        :param database_trigger: 自动作业触发器
        :type database_trigger: list[:class:`huaweicloudsdkeihealth.v1.DatabaseTriggerDto`]
        :param tool_id: 作业依赖的组件id，组件当前仅支持流程，取值范围[1,135]，支持大小写字母和数字。目前支持两种格式，特殊id：{流程名称}::{流程版本}::{源项目名称}；正常id：流程id
        :type tool_id: str
        :param tool_type: 作业依赖的组件类型，仅支持填写workflow
        :type tool_type: str
        :param job_name: 作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)
        :type job_name: str
        :param job_name_type: 
        :type job_name_type: :class:`huaweicloudsdkeihealth.v1.JobNameType`
        :param job_description: 作业的描述,取值范围：输入字符最大长度为255
        :type job_description: str
        :param labels: 作业标签，取值范围[0,5]，单个标签最大长度32字符，仅仅包含小写字母或数字或大写字母
        :type labels: list[str]
        :param priority: 作业的优先级,取值范围[0,9]，0最低，默认数值0
        :type priority: int
        :param timeout: 作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440
        :type timeout: int
        :param output_dir: job结果存储目录，不指定则在workflow的工作目录下生产job同名子目录，指定则已指定路径为准;不能包含以下特殊字符\\:*?&lt;\&quot;&gt;|。
        :type output_dir: str
        :param output_dir_type: 输出路径的类型
        :type output_dir_type: str
        :param node_labels: 节点标签 取值范围[0,1]，单个标签最大长度63字符
        :type node_labels: list[str]
        :param io_acc_id: 自动作业使用的SFS-Turbo实例id，不填表示不使用
        :type io_acc_id: str
        :param tasks: 自动作业依赖的流程信息
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.JobTaskDto`]
        """
        
        

        self._name = None
        self._description = None
        self._database_id = None
        self._database_column = None
        self._database_column_type = None
        self._clean_database_column = None
        self._database_trigger = None
        self._tool_id = None
        self._tool_type = None
        self._job_name = None
        self._job_name_type = None
        self._job_description = None
        self._labels = None
        self._priority = None
        self._timeout = None
        self._output_dir = None
        self._output_dir_type = None
        self._node_labels = None
        self._io_acc_id = None
        self._tasks = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.database_id = database_id
        self.database_column = database_column
        if database_column_type is not None:
            self.database_column_type = database_column_type
        if clean_database_column is not None:
            self.clean_database_column = clean_database_column
        if database_trigger is not None:
            self.database_trigger = database_trigger
        self.tool_id = tool_id
        self.tool_type = tool_type
        self.job_name = job_name
        self.job_name_type = job_name_type
        if job_description is not None:
            self.job_description = job_description
        if labels is not None:
            self.labels = labels
        if priority is not None:
            self.priority = priority
        if timeout is not None:
            self.timeout = timeout
        if output_dir is not None:
            self.output_dir = output_dir
        if output_dir_type is not None:
            self.output_dir_type = output_dir_type
        if node_labels is not None:
            self.node_labels = node_labels
        if io_acc_id is not None:
            self.io_acc_id = io_acc_id
        if tasks is not None:
            self.tasks = tasks

    @property
    def name(self):
        """Gets the name of this CreateAutJobReq.

        自动作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :return: The name of this CreateAutJobReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAutJobReq.

        自动作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :param name: The name of this CreateAutJobReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateAutJobReq.

        自动作业的描述,取值范围：输入字符最大长度为255

        :return: The description of this CreateAutJobReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAutJobReq.

        自动作业的描述,取值范围：输入字符最大长度为255

        :param description: The description of this CreateAutJobReq.
        :type description: str
        """
        self._description = description

    @property
    def database_id(self):
        """Gets the database_id of this CreateAutJobReq.

        自动作业依赖的数据库ID

        :return: The database_id of this CreateAutJobReq.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """Sets the database_id of this CreateAutJobReq.

        自动作业依赖的数据库ID

        :param database_id: The database_id of this CreateAutJobReq.
        :type database_id: str
        """
        self._database_id = database_id

    @property
    def database_column(self):
        """Gets the database_column of this CreateAutJobReq.

        自动作业状态更新列

        :return: The database_column of this CreateAutJobReq.
        :rtype: str
        """
        return self._database_column

    @database_column.setter
    def database_column(self, database_column):
        """Sets the database_column of this CreateAutJobReq.

        自动作业状态更新列

        :param database_column: The database_column of this CreateAutJobReq.
        :type database_column: str
        """
        self._database_column = database_column

    @property
    def database_column_type(self):
        """Gets the database_column_type of this CreateAutJobReq.

        自动作业状态更新列的类型，不填默认为EXISTED

        :return: The database_column_type of this CreateAutJobReq.
        :rtype: str
        """
        return self._database_column_type

    @database_column_type.setter
    def database_column_type(self, database_column_type):
        """Sets the database_column_type of this CreateAutJobReq.

        自动作业状态更新列的类型，不填默认为EXISTED

        :param database_column_type: The database_column_type of this CreateAutJobReq.
        :type database_column_type: str
        """
        self._database_column_type = database_column_type

    @property
    def clean_database_column(self):
        """Gets the clean_database_column of this CreateAutJobReq.

        是否清空作业状态更新列

        :return: The clean_database_column of this CreateAutJobReq.
        :rtype: bool
        """
        return self._clean_database_column

    @clean_database_column.setter
    def clean_database_column(self, clean_database_column):
        """Sets the clean_database_column of this CreateAutJobReq.

        是否清空作业状态更新列

        :param clean_database_column: The clean_database_column of this CreateAutJobReq.
        :type clean_database_column: bool
        """
        self._clean_database_column = clean_database_column

    @property
    def database_trigger(self):
        """Gets the database_trigger of this CreateAutJobReq.

        自动作业触发器

        :return: The database_trigger of this CreateAutJobReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.DatabaseTriggerDto`]
        """
        return self._database_trigger

    @database_trigger.setter
    def database_trigger(self, database_trigger):
        """Sets the database_trigger of this CreateAutJobReq.

        自动作业触发器

        :param database_trigger: The database_trigger of this CreateAutJobReq.
        :type database_trigger: list[:class:`huaweicloudsdkeihealth.v1.DatabaseTriggerDto`]
        """
        self._database_trigger = database_trigger

    @property
    def tool_id(self):
        """Gets the tool_id of this CreateAutJobReq.

        作业依赖的组件id，组件当前仅支持流程，取值范围[1,135]，支持大小写字母和数字。目前支持两种格式，特殊id：{流程名称}::{流程版本}::{源项目名称}；正常id：流程id

        :return: The tool_id of this CreateAutJobReq.
        :rtype: str
        """
        return self._tool_id

    @tool_id.setter
    def tool_id(self, tool_id):
        """Sets the tool_id of this CreateAutJobReq.

        作业依赖的组件id，组件当前仅支持流程，取值范围[1,135]，支持大小写字母和数字。目前支持两种格式，特殊id：{流程名称}::{流程版本}::{源项目名称}；正常id：流程id

        :param tool_id: The tool_id of this CreateAutJobReq.
        :type tool_id: str
        """
        self._tool_id = tool_id

    @property
    def tool_type(self):
        """Gets the tool_type of this CreateAutJobReq.

        作业依赖的组件类型，仅支持填写workflow

        :return: The tool_type of this CreateAutJobReq.
        :rtype: str
        """
        return self._tool_type

    @tool_type.setter
    def tool_type(self, tool_type):
        """Sets the tool_type of this CreateAutJobReq.

        作业依赖的组件类型，仅支持填写workflow

        :param tool_type: The tool_type of this CreateAutJobReq.
        :type tool_type: str
        """
        self._tool_type = tool_type

    @property
    def job_name(self):
        """Gets the job_name of this CreateAutJobReq.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :return: The job_name of this CreateAutJobReq.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this CreateAutJobReq.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :param job_name: The job_name of this CreateAutJobReq.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_name_type(self):
        """Gets the job_name_type of this CreateAutJobReq.


        :return: The job_name_type of this CreateAutJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.JobNameType`
        """
        return self._job_name_type

    @job_name_type.setter
    def job_name_type(self, job_name_type):
        """Sets the job_name_type of this CreateAutJobReq.


        :param job_name_type: The job_name_type of this CreateAutJobReq.
        :type job_name_type: :class:`huaweicloudsdkeihealth.v1.JobNameType`
        """
        self._job_name_type = job_name_type

    @property
    def job_description(self):
        """Gets the job_description of this CreateAutJobReq.

        作业的描述,取值范围：输入字符最大长度为255

        :return: The job_description of this CreateAutJobReq.
        :rtype: str
        """
        return self._job_description

    @job_description.setter
    def job_description(self, job_description):
        """Sets the job_description of this CreateAutJobReq.

        作业的描述,取值范围：输入字符最大长度为255

        :param job_description: The job_description of this CreateAutJobReq.
        :type job_description: str
        """
        self._job_description = job_description

    @property
    def labels(self):
        """Gets the labels of this CreateAutJobReq.

        作业标签，取值范围[0,5]，单个标签最大长度32字符，仅仅包含小写字母或数字或大写字母

        :return: The labels of this CreateAutJobReq.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreateAutJobReq.

        作业标签，取值范围[0,5]，单个标签最大长度32字符，仅仅包含小写字母或数字或大写字母

        :param labels: The labels of this CreateAutJobReq.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def priority(self):
        """Gets the priority of this CreateAutJobReq.

        作业的优先级,取值范围[0,9]，0最低，默认数值0

        :return: The priority of this CreateAutJobReq.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateAutJobReq.

        作业的优先级,取值范围[0,9]，0最低，默认数值0

        :param priority: The priority of this CreateAutJobReq.
        :type priority: int
        """
        self._priority = priority

    @property
    def timeout(self):
        """Gets the timeout of this CreateAutJobReq.

        作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440

        :return: The timeout of this CreateAutJobReq.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CreateAutJobReq.

        作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440

        :param timeout: The timeout of this CreateAutJobReq.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def output_dir(self):
        """Gets the output_dir of this CreateAutJobReq.

        job结果存储目录，不指定则在workflow的工作目录下生产job同名子目录，指定则已指定路径为准;不能包含以下特殊字符\\:*?<\">|。

        :return: The output_dir of this CreateAutJobReq.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        """Sets the output_dir of this CreateAutJobReq.

        job结果存储目录，不指定则在workflow的工作目录下生产job同名子目录，指定则已指定路径为准;不能包含以下特殊字符\\:*?<\">|。

        :param output_dir: The output_dir of this CreateAutJobReq.
        :type output_dir: str
        """
        self._output_dir = output_dir

    @property
    def output_dir_type(self):
        """Gets the output_dir_type of this CreateAutJobReq.

        输出路径的类型

        :return: The output_dir_type of this CreateAutJobReq.
        :rtype: str
        """
        return self._output_dir_type

    @output_dir_type.setter
    def output_dir_type(self, output_dir_type):
        """Sets the output_dir_type of this CreateAutJobReq.

        输出路径的类型

        :param output_dir_type: The output_dir_type of this CreateAutJobReq.
        :type output_dir_type: str
        """
        self._output_dir_type = output_dir_type

    @property
    def node_labels(self):
        """Gets the node_labels of this CreateAutJobReq.

        节点标签 取值范围[0,1]，单个标签最大长度63字符

        :return: The node_labels of this CreateAutJobReq.
        :rtype: list[str]
        """
        return self._node_labels

    @node_labels.setter
    def node_labels(self, node_labels):
        """Sets the node_labels of this CreateAutJobReq.

        节点标签 取值范围[0,1]，单个标签最大长度63字符

        :param node_labels: The node_labels of this CreateAutJobReq.
        :type node_labels: list[str]
        """
        self._node_labels = node_labels

    @property
    def io_acc_id(self):
        """Gets the io_acc_id of this CreateAutJobReq.

        自动作业使用的SFS-Turbo实例id，不填表示不使用

        :return: The io_acc_id of this CreateAutJobReq.
        :rtype: str
        """
        return self._io_acc_id

    @io_acc_id.setter
    def io_acc_id(self, io_acc_id):
        """Sets the io_acc_id of this CreateAutJobReq.

        自动作业使用的SFS-Turbo实例id，不填表示不使用

        :param io_acc_id: The io_acc_id of this CreateAutJobReq.
        :type io_acc_id: str
        """
        self._io_acc_id = io_acc_id

    @property
    def tasks(self):
        """Gets the tasks of this CreateAutJobReq.

        自动作业依赖的流程信息

        :return: The tasks of this CreateAutJobReq.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.JobTaskDto`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this CreateAutJobReq.

        自动作业依赖的流程信息

        :param tasks: The tasks of this CreateAutJobReq.
        :type tasks: list[:class:`huaweicloudsdkeihealth.v1.JobTaskDto`]
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
        if not isinstance(other, CreateAutJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
