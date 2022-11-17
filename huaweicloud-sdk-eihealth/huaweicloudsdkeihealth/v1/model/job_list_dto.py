# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobListDto:

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
        'user_name': 'str',
        'tool_info': 'ToolInfoDto',
        'io_acc_id': 'str',
        'io_acc_expected_usage': 'int',
        'still_running_tasks': 'list[str]'
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
        'user_name': 'user_name',
        'tool_info': 'tool_info',
        'io_acc_id': 'io_acc_id',
        'io_acc_expected_usage': 'io_acc_expected_usage',
        'still_running_tasks': 'still_running_tasks'
    }

    def __init__(self, id=None, name=None, description=None, labels=None, priority=None, timeout=None, output_dir=None, status=None, create_time=None, finish_time=None, failed_message=None, failed_reason=None, user_name=None, tool_info=None, io_acc_id=None, io_acc_expected_usage=None, still_running_tasks=None):
        """JobListDto

        The model defined in huaweicloud sdk

        :param id: 作业id
        :type id: str
        :param name: 作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)
        :type name: str
        :param description: 作业的描述,取值范围：输入字符最大长度为255
        :type description: str
        :param labels: 作业标签
        :type labels: list[str]
        :param priority: 作业优先级，[0,9]，0表示最低，默认0
        :type priority: int
        :param timeout: 作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440
        :type timeout: int
        :param output_dir: job结果存储目录，不指定则在workflow的工作目录下生产job同名子目录，指定则已指定路径为准
        :type output_dir: str
        :param status: 作业状态
        :type status: str
        :param create_time: 作业创建时间
        :type create_time: str
        :param finish_time: 作业结束时间
        :type finish_time: str
        :param failed_message: 失败提示，当作业执行失败时会返回
        :type failed_message: str
        :param failed_reason: 失败原因，当作业执行失败时会返回
        :type failed_reason: str
        :param user_name: 创建任务的用户名称
        :type user_name: str
        :param tool_info: 
        :type tool_info: :class:`huaweicloudsdkeihealth.v1.ToolInfoDto`
        :param io_acc_id: IO加速实例ID
        :type io_acc_id: str
        :param io_acc_expected_usage: 作业使用的SFS-Turbo实例预期占用存储量，单位G，用于投递作业时评估当前加速实例余量是否充足
        :type io_acc_expected_usage: int
        :param still_running_tasks: 仍在运行中的子任务
        :type still_running_tasks: list[str]
        """
        
        

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
        self._user_name = None
        self._tool_info = None
        self._io_acc_id = None
        self._io_acc_expected_usage = None
        self._still_running_tasks = None
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
        if user_name is not None:
            self.user_name = user_name
        if tool_info is not None:
            self.tool_info = tool_info
        if io_acc_id is not None:
            self.io_acc_id = io_acc_id
        if io_acc_expected_usage is not None:
            self.io_acc_expected_usage = io_acc_expected_usage
        if still_running_tasks is not None:
            self.still_running_tasks = still_running_tasks

    @property
    def id(self):
        """Gets the id of this JobListDto.

        作业id

        :return: The id of this JobListDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobListDto.

        作业id

        :param id: The id of this JobListDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this JobListDto.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :return: The name of this JobListDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobListDto.

        作业的名称，取值范围：[1,63]，允许大小写字母、数字、以及特殊字符中划线(-)

        :param name: The name of this JobListDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this JobListDto.

        作业的描述,取值范围：输入字符最大长度为255

        :return: The description of this JobListDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobListDto.

        作业的描述,取值范围：输入字符最大长度为255

        :param description: The description of this JobListDto.
        :type description: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this JobListDto.

        作业标签

        :return: The labels of this JobListDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this JobListDto.

        作业标签

        :param labels: The labels of this JobListDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def priority(self):
        """Gets the priority of this JobListDto.

        作业优先级，[0,9]，0表示最低，默认0

        :return: The priority of this JobListDto.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this JobListDto.

        作业优先级，[0,9]，0表示最低，默认0

        :param priority: The priority of this JobListDto.
        :type priority: int
        """
        self._priority = priority

    @property
    def timeout(self):
        """Gets the timeout of this JobListDto.

        作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440

        :return: The timeout of this JobListDto.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this JobListDto.

        作业执行超时时长，取值范围: [1, 144000]，单位：分钟，默认数值1440

        :param timeout: The timeout of this JobListDto.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def output_dir(self):
        """Gets the output_dir of this JobListDto.

        job结果存储目录，不指定则在workflow的工作目录下生产job同名子目录，指定则已指定路径为准

        :return: The output_dir of this JobListDto.
        :rtype: str
        """
        return self._output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        """Sets the output_dir of this JobListDto.

        job结果存储目录，不指定则在workflow的工作目录下生产job同名子目录，指定则已指定路径为准

        :param output_dir: The output_dir of this JobListDto.
        :type output_dir: str
        """
        self._output_dir = output_dir

    @property
    def status(self):
        """Gets the status of this JobListDto.

        作业状态

        :return: The status of this JobListDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobListDto.

        作业状态

        :param status: The status of this JobListDto.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this JobListDto.

        作业创建时间

        :return: The create_time of this JobListDto.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this JobListDto.

        作业创建时间

        :param create_time: The create_time of this JobListDto.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def finish_time(self):
        """Gets the finish_time of this JobListDto.

        作业结束时间

        :return: The finish_time of this JobListDto.
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this JobListDto.

        作业结束时间

        :param finish_time: The finish_time of this JobListDto.
        :type finish_time: str
        """
        self._finish_time = finish_time

    @property
    def failed_message(self):
        """Gets the failed_message of this JobListDto.

        失败提示，当作业执行失败时会返回

        :return: The failed_message of this JobListDto.
        :rtype: str
        """
        return self._failed_message

    @failed_message.setter
    def failed_message(self, failed_message):
        """Sets the failed_message of this JobListDto.

        失败提示，当作业执行失败时会返回

        :param failed_message: The failed_message of this JobListDto.
        :type failed_message: str
        """
        self._failed_message = failed_message

    @property
    def failed_reason(self):
        """Gets the failed_reason of this JobListDto.

        失败原因，当作业执行失败时会返回

        :return: The failed_reason of this JobListDto.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this JobListDto.

        失败原因，当作业执行失败时会返回

        :param failed_reason: The failed_reason of this JobListDto.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def user_name(self):
        """Gets the user_name of this JobListDto.

        创建任务的用户名称

        :return: The user_name of this JobListDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this JobListDto.

        创建任务的用户名称

        :param user_name: The user_name of this JobListDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def tool_info(self):
        """Gets the tool_info of this JobListDto.

        :return: The tool_info of this JobListDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ToolInfoDto`
        """
        return self._tool_info

    @tool_info.setter
    def tool_info(self, tool_info):
        """Sets the tool_info of this JobListDto.

        :param tool_info: The tool_info of this JobListDto.
        :type tool_info: :class:`huaweicloudsdkeihealth.v1.ToolInfoDto`
        """
        self._tool_info = tool_info

    @property
    def io_acc_id(self):
        """Gets the io_acc_id of this JobListDto.

        IO加速实例ID

        :return: The io_acc_id of this JobListDto.
        :rtype: str
        """
        return self._io_acc_id

    @io_acc_id.setter
    def io_acc_id(self, io_acc_id):
        """Sets the io_acc_id of this JobListDto.

        IO加速实例ID

        :param io_acc_id: The io_acc_id of this JobListDto.
        :type io_acc_id: str
        """
        self._io_acc_id = io_acc_id

    @property
    def io_acc_expected_usage(self):
        """Gets the io_acc_expected_usage of this JobListDto.

        作业使用的SFS-Turbo实例预期占用存储量，单位G，用于投递作业时评估当前加速实例余量是否充足

        :return: The io_acc_expected_usage of this JobListDto.
        :rtype: int
        """
        return self._io_acc_expected_usage

    @io_acc_expected_usage.setter
    def io_acc_expected_usage(self, io_acc_expected_usage):
        """Sets the io_acc_expected_usage of this JobListDto.

        作业使用的SFS-Turbo实例预期占用存储量，单位G，用于投递作业时评估当前加速实例余量是否充足

        :param io_acc_expected_usage: The io_acc_expected_usage of this JobListDto.
        :type io_acc_expected_usage: int
        """
        self._io_acc_expected_usage = io_acc_expected_usage

    @property
    def still_running_tasks(self):
        """Gets the still_running_tasks of this JobListDto.

        仍在运行中的子任务

        :return: The still_running_tasks of this JobListDto.
        :rtype: list[str]
        """
        return self._still_running_tasks

    @still_running_tasks.setter
    def still_running_tasks(self, still_running_tasks):
        """Sets the still_running_tasks of this JobListDto.

        仍在运行中的子任务

        :param still_running_tasks: The still_running_tasks of this JobListDto.
        :type still_running_tasks: list[str]
        """
        self._still_running_tasks = still_running_tasks

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
        if not isinstance(other, JobListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
