# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptTaskInfo:

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
        'task_scripts': 'list[ScriptTaskInfoTaskScripts]',
        'command_content': 'str',
        'command_type': 'str',
        'resource_type': 'str',
        'resource_group_id': 'str',
        'resource_group_type': 'str',
        'resource_ids': 'list[str]',
        'gray_resource_ids': 'list[str]',
        'pre_start': 'str',
        'post_finish': 'str',
        'success_num': 'int',
        'failed_num': 'int',
        'skip_num': 'int',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_scripts': 'task_scripts',
        'command_content': 'command_content',
        'command_type': 'command_type',
        'resource_type': 'resource_type',
        'resource_group_id': 'resource_group_id',
        'resource_group_type': 'resource_group_type',
        'resource_ids': 'resource_ids',
        'gray_resource_ids': 'gray_resource_ids',
        'pre_start': 'pre_start',
        'post_finish': 'post_finish',
        'success_num': 'success_num',
        'failed_num': 'failed_num',
        'skip_num': 'skip_num',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status'
    }

    def __init__(self, id=None, task_scripts=None, command_content=None, command_type=None, resource_type=None, resource_group_id=None, resource_group_type=None, resource_ids=None, gray_resource_ids=None, pre_start=None, post_finish=None, success_num=None, failed_num=None, skip_num=None, start_time=None, end_time=None, status=None):
        """ScriptTaskInfo

        The model defined in huaweicloud sdk

        :param id: 脚本任务ID。
        :type id: str
        :param task_scripts: 脚本列表。
        :type task_scripts: list[:class:`huaweicloudsdkworkspace.v2.ScriptTaskInfoTaskScripts`]
        :param command_content: 执行命令时输入的命令。
        :type command_content: str
        :param command_type: 命令行类型(POWERSHELL/BAT/SHELL)。
        :type command_type: str
        :param resource_type: 资源类型，如DESKTOP。
        :type resource_type: str
        :param resource_group_id: 资源组ID，如桌面池ID。
        :type resource_group_id: str
        :param resource_group_type: 资源组类型，如DESKTOP_POOL。
        :type resource_group_type: str
        :param resource_ids: 执行脚本的资源ID列表。
        :type resource_ids: list[str]
        :param gray_resource_ids: 灰度批次执行资源ID列表。
        :type gray_resource_ids: list[str]
        :param pre_start: 执行脚本前置步骤。
        :type pre_start: str
        :param post_finish: 执行脚本后置步骤。
        :type post_finish: str
        :param success_num: task中成功的执行记录数量。
        :type success_num: int
        :param failed_num: task中失败的执行记录数量。
        :type failed_num: int
        :param skip_num: task中跳过的执行记录数量。
        :type skip_num: int
        :param start_time: 脚本执行开始时间。
        :type start_time: datetime
        :param end_time: 脚本执行结束时间。
        :type end_time: datetime
        :param status: 任务结果。
        :type status: str
        """
        
        

        self._id = None
        self._task_scripts = None
        self._command_content = None
        self._command_type = None
        self._resource_type = None
        self._resource_group_id = None
        self._resource_group_type = None
        self._resource_ids = None
        self._gray_resource_ids = None
        self._pre_start = None
        self._post_finish = None
        self._success_num = None
        self._failed_num = None
        self._skip_num = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_scripts is not None:
            self.task_scripts = task_scripts
        if command_content is not None:
            self.command_content = command_content
        if command_type is not None:
            self.command_type = command_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        if resource_group_type is not None:
            self.resource_group_type = resource_group_type
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if gray_resource_ids is not None:
            self.gray_resource_ids = gray_resource_ids
        if pre_start is not None:
            self.pre_start = pre_start
        if post_finish is not None:
            self.post_finish = post_finish
        if success_num is not None:
            self.success_num = success_num
        if failed_num is not None:
            self.failed_num = failed_num
        if skip_num is not None:
            self.skip_num = skip_num
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this ScriptTaskInfo.

        脚本任务ID。

        :return: The id of this ScriptTaskInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScriptTaskInfo.

        脚本任务ID。

        :param id: The id of this ScriptTaskInfo.
        :type id: str
        """
        self._id = id

    @property
    def task_scripts(self):
        """Gets the task_scripts of this ScriptTaskInfo.

        脚本列表。

        :return: The task_scripts of this ScriptTaskInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ScriptTaskInfoTaskScripts`]
        """
        return self._task_scripts

    @task_scripts.setter
    def task_scripts(self, task_scripts):
        """Sets the task_scripts of this ScriptTaskInfo.

        脚本列表。

        :param task_scripts: The task_scripts of this ScriptTaskInfo.
        :type task_scripts: list[:class:`huaweicloudsdkworkspace.v2.ScriptTaskInfoTaskScripts`]
        """
        self._task_scripts = task_scripts

    @property
    def command_content(self):
        """Gets the command_content of this ScriptTaskInfo.

        执行命令时输入的命令。

        :return: The command_content of this ScriptTaskInfo.
        :rtype: str
        """
        return self._command_content

    @command_content.setter
    def command_content(self, command_content):
        """Sets the command_content of this ScriptTaskInfo.

        执行命令时输入的命令。

        :param command_content: The command_content of this ScriptTaskInfo.
        :type command_content: str
        """
        self._command_content = command_content

    @property
    def command_type(self):
        """Gets the command_type of this ScriptTaskInfo.

        命令行类型(POWERSHELL/BAT/SHELL)。

        :return: The command_type of this ScriptTaskInfo.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """Sets the command_type of this ScriptTaskInfo.

        命令行类型(POWERSHELL/BAT/SHELL)。

        :param command_type: The command_type of this ScriptTaskInfo.
        :type command_type: str
        """
        self._command_type = command_type

    @property
    def resource_type(self):
        """Gets the resource_type of this ScriptTaskInfo.

        资源类型，如DESKTOP。

        :return: The resource_type of this ScriptTaskInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ScriptTaskInfo.

        资源类型，如DESKTOP。

        :param resource_type: The resource_type of this ScriptTaskInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this ScriptTaskInfo.

        资源组ID，如桌面池ID。

        :return: The resource_group_id of this ScriptTaskInfo.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this ScriptTaskInfo.

        资源组ID，如桌面池ID。

        :param resource_group_id: The resource_group_id of this ScriptTaskInfo.
        :type resource_group_id: str
        """
        self._resource_group_id = resource_group_id

    @property
    def resource_group_type(self):
        """Gets the resource_group_type of this ScriptTaskInfo.

        资源组类型，如DESKTOP_POOL。

        :return: The resource_group_type of this ScriptTaskInfo.
        :rtype: str
        """
        return self._resource_group_type

    @resource_group_type.setter
    def resource_group_type(self, resource_group_type):
        """Sets the resource_group_type of this ScriptTaskInfo.

        资源组类型，如DESKTOP_POOL。

        :param resource_group_type: The resource_group_type of this ScriptTaskInfo.
        :type resource_group_type: str
        """
        self._resource_group_type = resource_group_type

    @property
    def resource_ids(self):
        """Gets the resource_ids of this ScriptTaskInfo.

        执行脚本的资源ID列表。

        :return: The resource_ids of this ScriptTaskInfo.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this ScriptTaskInfo.

        执行脚本的资源ID列表。

        :param resource_ids: The resource_ids of this ScriptTaskInfo.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def gray_resource_ids(self):
        """Gets the gray_resource_ids of this ScriptTaskInfo.

        灰度批次执行资源ID列表。

        :return: The gray_resource_ids of this ScriptTaskInfo.
        :rtype: list[str]
        """
        return self._gray_resource_ids

    @gray_resource_ids.setter
    def gray_resource_ids(self, gray_resource_ids):
        """Sets the gray_resource_ids of this ScriptTaskInfo.

        灰度批次执行资源ID列表。

        :param gray_resource_ids: The gray_resource_ids of this ScriptTaskInfo.
        :type gray_resource_ids: list[str]
        """
        self._gray_resource_ids = gray_resource_ids

    @property
    def pre_start(self):
        """Gets the pre_start of this ScriptTaskInfo.

        执行脚本前置步骤。

        :return: The pre_start of this ScriptTaskInfo.
        :rtype: str
        """
        return self._pre_start

    @pre_start.setter
    def pre_start(self, pre_start):
        """Sets the pre_start of this ScriptTaskInfo.

        执行脚本前置步骤。

        :param pre_start: The pre_start of this ScriptTaskInfo.
        :type pre_start: str
        """
        self._pre_start = pre_start

    @property
    def post_finish(self):
        """Gets the post_finish of this ScriptTaskInfo.

        执行脚本后置步骤。

        :return: The post_finish of this ScriptTaskInfo.
        :rtype: str
        """
        return self._post_finish

    @post_finish.setter
    def post_finish(self, post_finish):
        """Sets the post_finish of this ScriptTaskInfo.

        执行脚本后置步骤。

        :param post_finish: The post_finish of this ScriptTaskInfo.
        :type post_finish: str
        """
        self._post_finish = post_finish

    @property
    def success_num(self):
        """Gets the success_num of this ScriptTaskInfo.

        task中成功的执行记录数量。

        :return: The success_num of this ScriptTaskInfo.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        """Sets the success_num of this ScriptTaskInfo.

        task中成功的执行记录数量。

        :param success_num: The success_num of this ScriptTaskInfo.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def failed_num(self):
        """Gets the failed_num of this ScriptTaskInfo.

        task中失败的执行记录数量。

        :return: The failed_num of this ScriptTaskInfo.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        """Sets the failed_num of this ScriptTaskInfo.

        task中失败的执行记录数量。

        :param failed_num: The failed_num of this ScriptTaskInfo.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def skip_num(self):
        """Gets the skip_num of this ScriptTaskInfo.

        task中跳过的执行记录数量。

        :return: The skip_num of this ScriptTaskInfo.
        :rtype: int
        """
        return self._skip_num

    @skip_num.setter
    def skip_num(self, skip_num):
        """Sets the skip_num of this ScriptTaskInfo.

        task中跳过的执行记录数量。

        :param skip_num: The skip_num of this ScriptTaskInfo.
        :type skip_num: int
        """
        self._skip_num = skip_num

    @property
    def start_time(self):
        """Gets the start_time of this ScriptTaskInfo.

        脚本执行开始时间。

        :return: The start_time of this ScriptTaskInfo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ScriptTaskInfo.

        脚本执行开始时间。

        :param start_time: The start_time of this ScriptTaskInfo.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ScriptTaskInfo.

        脚本执行结束时间。

        :return: The end_time of this ScriptTaskInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ScriptTaskInfo.

        脚本执行结束时间。

        :param end_time: The end_time of this ScriptTaskInfo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ScriptTaskInfo.

        任务结果。

        :return: The status of this ScriptTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScriptTaskInfo.

        任务结果。

        :param status: The status of this ScriptTaskInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ScriptTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
