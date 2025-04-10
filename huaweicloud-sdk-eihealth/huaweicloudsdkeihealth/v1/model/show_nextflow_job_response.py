# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNextflowJobResponse(SdkResponse):

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
        'priority': 'int',
        'description': 'str',
        'labels': 'list[str]',
        'status': 'str',
        'has_ignore_failed_tasks': 'bool',
        'create_time': 'str',
        'finish_time': 'str',
        'failed_message': 'str',
        'failed_reason': 'str',
        'workflow_name': 'str',
        'workflow_id': 'str',
        'command_line': 'str',
        'params': 'list[NextflowParamsDto]',
        'nextflow_parameters': 'dict(str, object)',
        'config_files': 'list[str]',
        'config_context': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'priority': 'priority',
        'description': 'description',
        'labels': 'labels',
        'status': 'status',
        'has_ignore_failed_tasks': 'has_ignore_failed_tasks',
        'create_time': 'create_time',
        'finish_time': 'finish_time',
        'failed_message': 'failed_message',
        'failed_reason': 'failed_reason',
        'workflow_name': 'workflow_name',
        'workflow_id': 'workflow_id',
        'command_line': 'command_line',
        'params': 'params',
        'nextflow_parameters': 'nextflow_parameters',
        'config_files': 'config_files',
        'config_context': 'config_context'
    }

    def __init__(self, id=None, name=None, priority=None, description=None, labels=None, status=None, has_ignore_failed_tasks=None, create_time=None, finish_time=None, failed_message=None, failed_reason=None, workflow_name=None, workflow_id=None, command_line=None, params=None, nextflow_parameters=None, config_files=None, config_context=None):
        r"""ShowNextflowJobResponse

        The model defined in huaweicloud sdk

        :param id: 作业id
        :type id: str
        :param name: 作业的名称
        :type name: str
        :param priority: 作业的优先级,取值范围[0,9]，0最低，默认数值0
        :type priority: int
        :param description: 作业的描述
        :type description: str
        :param labels: 作业标签
        :type labels: list[str]
        :param status: 作业运行状态
        :type status: str
        :param has_ignore_failed_tasks: 是否包含已被忽略的失败tasks
        :type has_ignore_failed_tasks: bool
        :param create_time: 作业创建时间
        :type create_time: str
        :param finish_time: 作业完成时间
        :type finish_time: str
        :param failed_message: 作业运行失败描述信息，当作业执行失败时会返回
        :type failed_message: str
        :param failed_reason: 作业运行失败原因，当作业执行失败时会返回
        :type failed_reason: str
        :param workflow_name: 流程名称
        :type workflow_name: str
        :param workflow_id: 流程id
        :type workflow_id: str
        :param command_line: nextflow执行命令
        :type command_line: str
        :param params: 作业参数列表
        :type params: list[:class:`huaweicloudsdkeihealth.v1.NextflowParamsDto`]
        :param nextflow_parameters: nextflow流程返回的全量参数列表
        :type nextflow_parameters: dict(str, object)
        :param config_files: 作业标签
        :type config_files: list[str]
        :param config_context: nextflow config文件内容
        :type config_context: str
        """
        
        super(ShowNextflowJobResponse, self).__init__()

        self._id = None
        self._name = None
        self._priority = None
        self._description = None
        self._labels = None
        self._status = None
        self._has_ignore_failed_tasks = None
        self._create_time = None
        self._finish_time = None
        self._failed_message = None
        self._failed_reason = None
        self._workflow_name = None
        self._workflow_id = None
        self._command_line = None
        self._params = None
        self._nextflow_parameters = None
        self._config_files = None
        self._config_context = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if priority is not None:
            self.priority = priority
        if description is not None:
            self.description = description
        if labels is not None:
            self.labels = labels
        if status is not None:
            self.status = status
        if has_ignore_failed_tasks is not None:
            self.has_ignore_failed_tasks = has_ignore_failed_tasks
        if create_time is not None:
            self.create_time = create_time
        if finish_time is not None:
            self.finish_time = finish_time
        if failed_message is not None:
            self.failed_message = failed_message
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if workflow_name is not None:
            self.workflow_name = workflow_name
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if command_line is not None:
            self.command_line = command_line
        if params is not None:
            self.params = params
        if nextflow_parameters is not None:
            self.nextflow_parameters = nextflow_parameters
        if config_files is not None:
            self.config_files = config_files
        if config_context is not None:
            self.config_context = config_context

    @property
    def id(self):
        r"""Gets the id of this ShowNextflowJobResponse.

        作业id

        :return: The id of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowNextflowJobResponse.

        作业id

        :param id: The id of this ShowNextflowJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowNextflowJobResponse.

        作业的名称

        :return: The name of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowNextflowJobResponse.

        作业的名称

        :param name: The name of this ShowNextflowJobResponse.
        :type name: str
        """
        self._name = name

    @property
    def priority(self):
        r"""Gets the priority of this ShowNextflowJobResponse.

        作业的优先级,取值范围[0,9]，0最低，默认数值0

        :return: The priority of this ShowNextflowJobResponse.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ShowNextflowJobResponse.

        作业的优先级,取值范围[0,9]，0最低，默认数值0

        :param priority: The priority of this ShowNextflowJobResponse.
        :type priority: int
        """
        self._priority = priority

    @property
    def description(self):
        r"""Gets the description of this ShowNextflowJobResponse.

        作业的描述

        :return: The description of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowNextflowJobResponse.

        作业的描述

        :param description: The description of this ShowNextflowJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        r"""Gets the labels of this ShowNextflowJobResponse.

        作业标签

        :return: The labels of this ShowNextflowJobResponse.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ShowNextflowJobResponse.

        作业标签

        :param labels: The labels of this ShowNextflowJobResponse.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def status(self):
        r"""Gets the status of this ShowNextflowJobResponse.

        作业运行状态

        :return: The status of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowNextflowJobResponse.

        作业运行状态

        :param status: The status of this ShowNextflowJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def has_ignore_failed_tasks(self):
        r"""Gets the has_ignore_failed_tasks of this ShowNextflowJobResponse.

        是否包含已被忽略的失败tasks

        :return: The has_ignore_failed_tasks of this ShowNextflowJobResponse.
        :rtype: bool
        """
        return self._has_ignore_failed_tasks

    @has_ignore_failed_tasks.setter
    def has_ignore_failed_tasks(self, has_ignore_failed_tasks):
        r"""Sets the has_ignore_failed_tasks of this ShowNextflowJobResponse.

        是否包含已被忽略的失败tasks

        :param has_ignore_failed_tasks: The has_ignore_failed_tasks of this ShowNextflowJobResponse.
        :type has_ignore_failed_tasks: bool
        """
        self._has_ignore_failed_tasks = has_ignore_failed_tasks

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowNextflowJobResponse.

        作业创建时间

        :return: The create_time of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowNextflowJobResponse.

        作业创建时间

        :param create_time: The create_time of this ShowNextflowJobResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        r"""Gets the finish_time of this ShowNextflowJobResponse.

        作业完成时间

        :return: The finish_time of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        r"""Sets the finish_time of this ShowNextflowJobResponse.

        作业完成时间

        :param finish_time: The finish_time of this ShowNextflowJobResponse.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def failed_message(self):
        r"""Gets the failed_message of this ShowNextflowJobResponse.

        作业运行失败描述信息，当作业执行失败时会返回

        :return: The failed_message of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        r"""Sets the failed_message of this ShowNextflowJobResponse.

        作业运行失败描述信息，当作业执行失败时会返回

        :param failed_message: The failed_message of this ShowNextflowJobResponse.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ShowNextflowJobResponse.

        作业运行失败原因，当作业执行失败时会返回

        :return: The failed_reason of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ShowNextflowJobResponse.

        作业运行失败原因，当作业执行失败时会返回

        :param failed_reason: The failed_reason of this ShowNextflowJobResponse.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def workflow_name(self):
        r"""Gets the workflow_name of this ShowNextflowJobResponse.

        流程名称

        :return: The workflow_name of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        r"""Sets the workflow_name of this ShowNextflowJobResponse.

        流程名称

        :param workflow_name: The workflow_name of this ShowNextflowJobResponse.
        :type workflow_name: str
        """
        self._workflow_name = workflow_name

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this ShowNextflowJobResponse.

        流程id

        :return: The workflow_id of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this ShowNextflowJobResponse.

        流程id

        :param workflow_id: The workflow_id of this ShowNextflowJobResponse.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def command_line(self):
        r"""Gets the command_line of this ShowNextflowJobResponse.

        nextflow执行命令

        :return: The command_line of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._command_line

    @command_line.setter
    def command_line(self, command_line):
        r"""Sets the command_line of this ShowNextflowJobResponse.

        nextflow执行命令

        :param command_line: The command_line of this ShowNextflowJobResponse.
        :type command_line: str
        """
        self._command_line = command_line

    @property
    def params(self):
        r"""Gets the params of this ShowNextflowJobResponse.

        作业参数列表

        :return: The params of this ShowNextflowJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.NextflowParamsDto`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this ShowNextflowJobResponse.

        作业参数列表

        :param params: The params of this ShowNextflowJobResponse.
        :type params: list[:class:`huaweicloudsdkeihealth.v1.NextflowParamsDto`]
        """
        self._params = params

    @property
    def nextflow_parameters(self):
        r"""Gets the nextflow_parameters of this ShowNextflowJobResponse.

        nextflow流程返回的全量参数列表

        :return: The nextflow_parameters of this ShowNextflowJobResponse.
        :rtype: dict(str, object)
        """
        return self._nextflow_parameters

    @nextflow_parameters.setter
    def nextflow_parameters(self, nextflow_parameters):
        r"""Sets the nextflow_parameters of this ShowNextflowJobResponse.

        nextflow流程返回的全量参数列表

        :param nextflow_parameters: The nextflow_parameters of this ShowNextflowJobResponse.
        :type nextflow_parameters: dict(str, object)
        """
        self._nextflow_parameters = nextflow_parameters

    @property
    def config_files(self):
        r"""Gets the config_files of this ShowNextflowJobResponse.

        作业标签

        :return: The config_files of this ShowNextflowJobResponse.
        :rtype: list[str]
        """
        return self._config_files

    @config_files.setter
    def config_files(self, config_files):
        r"""Sets the config_files of this ShowNextflowJobResponse.

        作业标签

        :param config_files: The config_files of this ShowNextflowJobResponse.
        :type config_files: list[str]
        """
        self._config_files = config_files

    @property
    def config_context(self):
        r"""Gets the config_context of this ShowNextflowJobResponse.

        nextflow config文件内容

        :return: The config_context of this ShowNextflowJobResponse.
        :rtype: str
        """
        return self._config_context

    @config_context.setter
    def config_context(self, config_context):
        r"""Sets the config_context of this ShowNextflowJobResponse.

        nextflow config文件内容

        :param config_context: The config_context of this ShowNextflowJobResponse.
        :type config_context: str
        """
        self._config_context = config_context

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
        if not isinstance(other, ShowNextflowJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
