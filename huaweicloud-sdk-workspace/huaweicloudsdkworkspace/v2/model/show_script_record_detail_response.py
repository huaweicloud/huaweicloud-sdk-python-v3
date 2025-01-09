# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScriptRecordDetailResponse(SdkResponse):

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
        'script_id': 'str',
        'script_name': 'str',
        'script_task_id': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_type': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'status': 'str',
        'execute_order': 'int',
        'command_content': 'str',
        'command_type': 'str',
        'result_code': 'str',
        'reason': 'str',
        'output': 'str'
    }

    attribute_map = {
        'id': 'id',
        'script_id': 'script_id',
        'script_name': 'script_name',
        'script_task_id': 'script_task_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_type': 'resource_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'execute_order': 'execute_order',
        'command_content': 'command_content',
        'command_type': 'command_type',
        'result_code': 'result_code',
        'reason': 'reason',
        'output': 'output'
    }

    def __init__(self, id=None, script_id=None, script_name=None, script_task_id=None, resource_id=None, resource_name=None, resource_type=None, start_time=None, end_time=None, status=None, execute_order=None, command_content=None, command_type=None, result_code=None, reason=None, output=None):
        """ShowScriptRecordDetailResponse

        The model defined in huaweicloud sdk

        :param id: 脚本执行记录ID。
        :type id: str
        :param script_id: 脚本ID。
        :type script_id: str
        :param script_name: 脚本名称。
        :type script_name: str
        :param script_task_id: 脚本执行的任务ID。
        :type script_task_id: str
        :param resource_id: 执行脚本的资源ID，如桌面ID。
        :type resource_id: str
        :param resource_name: 执行脚本的资源名称，如桌面名称。
        :type resource_name: str
        :param resource_type: 资源类型，如桌面(DESKTOP)。
        :type resource_type: str
        :param start_time: 脚本执行开始时间。
        :type start_time: datetime
        :param end_time: 脚本执行结束时间。
        :type end_time: datetime
        :param status: 脚本执行状态。
        :type status: str
        :param execute_order: 执行批次（默认：0，灰度：1，非灰度：2）。
        :type execute_order: int
        :param command_content: 命令行内容。
        :type command_content: str
        :param command_type: 命令行类型(POWERSHELL/BAT/SHELL)。
        :type command_type: str
        :param result_code: 错误码。
        :type result_code: str
        :param reason: 原因。
        :type reason: str
        :param output: 脚本执行的输出。
        :type output: str
        """
        
        super(ShowScriptRecordDetailResponse, self).__init__()

        self._id = None
        self._script_id = None
        self._script_name = None
        self._script_task_id = None
        self._resource_id = None
        self._resource_name = None
        self._resource_type = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._execute_order = None
        self._command_content = None
        self._command_type = None
        self._result_code = None
        self._reason = None
        self._output = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if script_id is not None:
            self.script_id = script_id
        if script_name is not None:
            self.script_name = script_name
        if script_task_id is not None:
            self.script_task_id = script_task_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_type is not None:
            self.resource_type = resource_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if execute_order is not None:
            self.execute_order = execute_order
        if command_content is not None:
            self.command_content = command_content
        if command_type is not None:
            self.command_type = command_type
        if result_code is not None:
            self.result_code = result_code
        if reason is not None:
            self.reason = reason
        if output is not None:
            self.output = output

    @property
    def id(self):
        """Gets the id of this ShowScriptRecordDetailResponse.

        脚本执行记录ID。

        :return: The id of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowScriptRecordDetailResponse.

        脚本执行记录ID。

        :param id: The id of this ShowScriptRecordDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def script_id(self):
        """Gets the script_id of this ShowScriptRecordDetailResponse.

        脚本ID。

        :return: The script_id of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        """Sets the script_id of this ShowScriptRecordDetailResponse.

        脚本ID。

        :param script_id: The script_id of this ShowScriptRecordDetailResponse.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def script_name(self):
        """Gets the script_name of this ShowScriptRecordDetailResponse.

        脚本名称。

        :return: The script_name of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """Sets the script_name of this ShowScriptRecordDetailResponse.

        脚本名称。

        :param script_name: The script_name of this ShowScriptRecordDetailResponse.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def script_task_id(self):
        """Gets the script_task_id of this ShowScriptRecordDetailResponse.

        脚本执行的任务ID。

        :return: The script_task_id of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._script_task_id

    @script_task_id.setter
    def script_task_id(self, script_task_id):
        """Sets the script_task_id of this ShowScriptRecordDetailResponse.

        脚本执行的任务ID。

        :param script_task_id: The script_task_id of this ShowScriptRecordDetailResponse.
        :type script_task_id: str
        """
        self._script_task_id = script_task_id

    @property
    def resource_id(self):
        """Gets the resource_id of this ShowScriptRecordDetailResponse.

        执行脚本的资源ID，如桌面ID。

        :return: The resource_id of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ShowScriptRecordDetailResponse.

        执行脚本的资源ID，如桌面ID。

        :param resource_id: The resource_id of this ShowScriptRecordDetailResponse.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this ShowScriptRecordDetailResponse.

        执行脚本的资源名称，如桌面名称。

        :return: The resource_name of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this ShowScriptRecordDetailResponse.

        执行脚本的资源名称，如桌面名称。

        :param resource_name: The resource_name of this ShowScriptRecordDetailResponse.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_type(self):
        """Gets the resource_type of this ShowScriptRecordDetailResponse.

        资源类型，如桌面(DESKTOP)。

        :return: The resource_type of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ShowScriptRecordDetailResponse.

        资源类型，如桌面(DESKTOP)。

        :param resource_type: The resource_type of this ShowScriptRecordDetailResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def start_time(self):
        """Gets the start_time of this ShowScriptRecordDetailResponse.

        脚本执行开始时间。

        :return: The start_time of this ShowScriptRecordDetailResponse.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowScriptRecordDetailResponse.

        脚本执行开始时间。

        :param start_time: The start_time of this ShowScriptRecordDetailResponse.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowScriptRecordDetailResponse.

        脚本执行结束时间。

        :return: The end_time of this ShowScriptRecordDetailResponse.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowScriptRecordDetailResponse.

        脚本执行结束时间。

        :param end_time: The end_time of this ShowScriptRecordDetailResponse.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ShowScriptRecordDetailResponse.

        脚本执行状态。

        :return: The status of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowScriptRecordDetailResponse.

        脚本执行状态。

        :param status: The status of this ShowScriptRecordDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def execute_order(self):
        """Gets the execute_order of this ShowScriptRecordDetailResponse.

        执行批次（默认：0，灰度：1，非灰度：2）。

        :return: The execute_order of this ShowScriptRecordDetailResponse.
        :rtype: int
        """
        return self._execute_order

    @execute_order.setter
    def execute_order(self, execute_order):
        """Sets the execute_order of this ShowScriptRecordDetailResponse.

        执行批次（默认：0，灰度：1，非灰度：2）。

        :param execute_order: The execute_order of this ShowScriptRecordDetailResponse.
        :type execute_order: int
        """
        self._execute_order = execute_order

    @property
    def command_content(self):
        """Gets the command_content of this ShowScriptRecordDetailResponse.

        命令行内容。

        :return: The command_content of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._command_content

    @command_content.setter
    def command_content(self, command_content):
        """Sets the command_content of this ShowScriptRecordDetailResponse.

        命令行内容。

        :param command_content: The command_content of this ShowScriptRecordDetailResponse.
        :type command_content: str
        """
        self._command_content = command_content

    @property
    def command_type(self):
        """Gets the command_type of this ShowScriptRecordDetailResponse.

        命令行类型(POWERSHELL/BAT/SHELL)。

        :return: The command_type of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """Sets the command_type of this ShowScriptRecordDetailResponse.

        命令行类型(POWERSHELL/BAT/SHELL)。

        :param command_type: The command_type of this ShowScriptRecordDetailResponse.
        :type command_type: str
        """
        self._command_type = command_type

    @property
    def result_code(self):
        """Gets the result_code of this ShowScriptRecordDetailResponse.

        错误码。

        :return: The result_code of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        """Sets the result_code of this ShowScriptRecordDetailResponse.

        错误码。

        :param result_code: The result_code of this ShowScriptRecordDetailResponse.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def reason(self):
        """Gets the reason of this ShowScriptRecordDetailResponse.

        原因。

        :return: The reason of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ShowScriptRecordDetailResponse.

        原因。

        :param reason: The reason of this ShowScriptRecordDetailResponse.
        :type reason: str
        """
        self._reason = reason

    @property
    def output(self):
        """Gets the output of this ShowScriptRecordDetailResponse.

        脚本执行的输出。

        :return: The output of this ShowScriptRecordDetailResponse.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this ShowScriptRecordDetailResponse.

        脚本执行的输出。

        :param output: The output of this ShowScriptRecordDetailResponse.
        :type output: str
        """
        self._output = output

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
        if not isinstance(other, ShowScriptRecordDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
