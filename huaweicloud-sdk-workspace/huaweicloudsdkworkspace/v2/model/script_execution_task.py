# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptExecutionTask:

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
        'desktop_pool_id': 'str',
        'desktop_pool_name': 'str',
        'scripts': 'list[Script]',
        'command_content': 'str',
        'command_type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'success_num': 'int',
        'failed_num': 'int',
        'skip_num': 'int'
    }

    attribute_map = {
        'id': 'id',
        'desktop_pool_id': 'desktop_pool_id',
        'desktop_pool_name': 'desktop_pool_name',
        'scripts': 'scripts',
        'command_content': 'command_content',
        'command_type': 'command_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'success_num': 'success_num',
        'failed_num': 'failed_num',
        'skip_num': 'skip_num'
    }

    def __init__(self, id=None, desktop_pool_id=None, desktop_pool_name=None, scripts=None, command_content=None, command_type=None, start_time=None, end_time=None, status=None, success_num=None, failed_num=None, skip_num=None):
        r"""ScriptExecutionTask

        The model defined in huaweicloud sdk

        :param id: 任务id。
        :type id: str
        :param desktop_pool_id: 桌面池id。
        :type desktop_pool_id: str
        :param desktop_pool_name: 桌面池名称。
        :type desktop_pool_name: str
        :param scripts: 脚本信息列表。
        :type scripts: list[:class:`huaweicloudsdkworkspace.v2.Script`]
        :param command_content: 执行的命令行。
        :type command_content: str
        :param command_type: 命令行类型。 - POWERSHELL：WINDOWS系统使用。 - BAT：WINDOWS系统使用。 - SHELL：LINUX系统使用。
        :type command_type: str
        :param start_time: 任务开始时间，格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type start_time: str
        :param end_time: 任务结束时间，格式为：yyyy-MM-ddTHH:mm:ssZ。
        :type end_time: str
        :param status: 任务状态，值含： - FINISH：已完成。 - FAILED：失败。 - RUNNING：运行中。 - INIT： 初始化。
        :type status: str
        :param success_num: 成功数量。
        :type success_num: int
        :param failed_num: 失败数量。
        :type failed_num: int
        :param skip_num: 跳过数量。
        :type skip_num: int
        """
        
        

        self._id = None
        self._desktop_pool_id = None
        self._desktop_pool_name = None
        self._scripts = None
        self._command_content = None
        self._command_type = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._success_num = None
        self._failed_num = None
        self._skip_num = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if desktop_pool_name is not None:
            self.desktop_pool_name = desktop_pool_name
        if scripts is not None:
            self.scripts = scripts
        if command_content is not None:
            self.command_content = command_content
        if command_type is not None:
            self.command_type = command_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if success_num is not None:
            self.success_num = success_num
        if failed_num is not None:
            self.failed_num = failed_num
        if skip_num is not None:
            self.skip_num = skip_num

    @property
    def id(self):
        r"""Gets the id of this ScriptExecutionTask.

        任务id。

        :return: The id of this ScriptExecutionTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScriptExecutionTask.

        任务id。

        :param id: The id of this ScriptExecutionTask.
        :type id: str
        """
        self._id = id

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this ScriptExecutionTask.

        桌面池id。

        :return: The desktop_pool_id of this ScriptExecutionTask.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this ScriptExecutionTask.

        桌面池id。

        :param desktop_pool_id: The desktop_pool_id of this ScriptExecutionTask.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def desktop_pool_name(self):
        r"""Gets the desktop_pool_name of this ScriptExecutionTask.

        桌面池名称。

        :return: The desktop_pool_name of this ScriptExecutionTask.
        :rtype: str
        """
        return self._desktop_pool_name

    @desktop_pool_name.setter
    def desktop_pool_name(self, desktop_pool_name):
        r"""Sets the desktop_pool_name of this ScriptExecutionTask.

        桌面池名称。

        :param desktop_pool_name: The desktop_pool_name of this ScriptExecutionTask.
        :type desktop_pool_name: str
        """
        self._desktop_pool_name = desktop_pool_name

    @property
    def scripts(self):
        r"""Gets the scripts of this ScriptExecutionTask.

        脚本信息列表。

        :return: The scripts of this ScriptExecutionTask.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Script`]
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        r"""Sets the scripts of this ScriptExecutionTask.

        脚本信息列表。

        :param scripts: The scripts of this ScriptExecutionTask.
        :type scripts: list[:class:`huaweicloudsdkworkspace.v2.Script`]
        """
        self._scripts = scripts

    @property
    def command_content(self):
        r"""Gets the command_content of this ScriptExecutionTask.

        执行的命令行。

        :return: The command_content of this ScriptExecutionTask.
        :rtype: str
        """
        return self._command_content

    @command_content.setter
    def command_content(self, command_content):
        r"""Sets the command_content of this ScriptExecutionTask.

        执行的命令行。

        :param command_content: The command_content of this ScriptExecutionTask.
        :type command_content: str
        """
        self._command_content = command_content

    @property
    def command_type(self):
        r"""Gets the command_type of this ScriptExecutionTask.

        命令行类型。 - POWERSHELL：WINDOWS系统使用。 - BAT：WINDOWS系统使用。 - SHELL：LINUX系统使用。

        :return: The command_type of this ScriptExecutionTask.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        r"""Sets the command_type of this ScriptExecutionTask.

        命令行类型。 - POWERSHELL：WINDOWS系统使用。 - BAT：WINDOWS系统使用。 - SHELL：LINUX系统使用。

        :param command_type: The command_type of this ScriptExecutionTask.
        :type command_type: str
        """
        self._command_type = command_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ScriptExecutionTask.

        任务开始时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The start_time of this ScriptExecutionTask.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ScriptExecutionTask.

        任务开始时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param start_time: The start_time of this ScriptExecutionTask.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ScriptExecutionTask.

        任务结束时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :return: The end_time of this ScriptExecutionTask.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ScriptExecutionTask.

        任务结束时间，格式为：yyyy-MM-ddTHH:mm:ssZ。

        :param end_time: The end_time of this ScriptExecutionTask.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ScriptExecutionTask.

        任务状态，值含： - FINISH：已完成。 - FAILED：失败。 - RUNNING：运行中。 - INIT： 初始化。

        :return: The status of this ScriptExecutionTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScriptExecutionTask.

        任务状态，值含： - FINISH：已完成。 - FAILED：失败。 - RUNNING：运行中。 - INIT： 初始化。

        :param status: The status of this ScriptExecutionTask.
        :type status: str
        """
        self._status = status

    @property
    def success_num(self):
        r"""Gets the success_num of this ScriptExecutionTask.

        成功数量。

        :return: The success_num of this ScriptExecutionTask.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this ScriptExecutionTask.

        成功数量。

        :param success_num: The success_num of this ScriptExecutionTask.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def failed_num(self):
        r"""Gets the failed_num of this ScriptExecutionTask.

        失败数量。

        :return: The failed_num of this ScriptExecutionTask.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this ScriptExecutionTask.

        失败数量。

        :param failed_num: The failed_num of this ScriptExecutionTask.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def skip_num(self):
        r"""Gets the skip_num of this ScriptExecutionTask.

        跳过数量。

        :return: The skip_num of this ScriptExecutionTask.
        :rtype: int
        """
        return self._skip_num

    @skip_num.setter
    def skip_num(self, skip_num):
        r"""Sets the skip_num of this ScriptExecutionTask.

        跳过数量。

        :param skip_num: The skip_num of this ScriptExecutionTask.
        :type skip_num: int
        """
        self._skip_num = skip_num

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
        if not isinstance(other, ScriptExecutionTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
