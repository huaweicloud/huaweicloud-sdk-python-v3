# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteScriptOrCommandReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gray_count': 'int',
        'resource_type': 'str',
        'gray_resource_ids': 'list[str]',
        'gray_fail_threshold': 'int',
        'resource_ids': 'list[str]',
        'script_ids': 'list[str]',
        'command': 'str',
        'command_type': 'str',
        'execution_timeout': 'int',
        'pre_start': 'str',
        'post_finish': 'str',
        'resource_group_type': 'str',
        'resource_group_id': 'str'
    }

    attribute_map = {
        'gray_count': 'gray_count',
        'resource_type': 'resource_type',
        'gray_resource_ids': 'gray_resource_ids',
        'gray_fail_threshold': 'gray_fail_threshold',
        'resource_ids': 'resource_ids',
        'script_ids': 'script_ids',
        'command': 'command',
        'command_type': 'command_type',
        'execution_timeout': 'execution_timeout',
        'pre_start': 'pre_start',
        'post_finish': 'post_finish',
        'resource_group_type': 'resource_group_type',
        'resource_group_id': 'resource_group_id'
    }

    def __init__(self, gray_count=None, resource_type=None, gray_resource_ids=None, gray_fail_threshold=None, resource_ids=None, script_ids=None, command=None, command_type=None, execution_timeout=None, pre_start=None, post_finish=None, resource_group_type=None, resource_group_id=None):
        """ExecuteScriptOrCommandReq

        The model defined in huaweicloud sdk

        :param gray_count: 灰度资源数量。
        :type gray_count: int
        :param resource_type: 资源类型，如桌面(DESKTOP)。
        :type resource_type: str
        :param gray_resource_ids: 灰度执行脚本的资源列表。
        :type gray_resource_ids: list[str]
        :param gray_fail_threshold: 灰度失败阈值，达到阈值后停止进行下一批资源执行脚本，小于gray_count。
        :type gray_fail_threshold: int
        :param resource_ids: 执行脚本的资源列表。
        :type resource_ids: list[str]
        :param script_ids: 执行的脚本列表。
        :type script_ids: list[str]
        :param command: 执行的命令行，与scripts二选一。
        :type command: str
        :param command_type: 命令行的类型（POWERSHELL，BAT，SHELL）。
        :type command_type: str
        :param execution_timeout: 执行脚本的超时时间，单位分钟。
        :type execution_timeout: int
        :param pre_start: 执行脚本前置步骤。
        :type pre_start: str
        :param post_finish: 执行脚本后置步骤(STOP,REBOOT)。
        :type post_finish: str
        :param resource_group_type: 资源组类型，如桌面池(DESKTOP_POOL)。
        :type resource_group_type: str
        :param resource_group_id: 资源组ID。
        :type resource_group_id: str
        """
        
        

        self._gray_count = None
        self._resource_type = None
        self._gray_resource_ids = None
        self._gray_fail_threshold = None
        self._resource_ids = None
        self._script_ids = None
        self._command = None
        self._command_type = None
        self._execution_timeout = None
        self._pre_start = None
        self._post_finish = None
        self._resource_group_type = None
        self._resource_group_id = None
        self.discriminator = None

        if gray_count is not None:
            self.gray_count = gray_count
        if resource_type is not None:
            self.resource_type = resource_type
        if gray_resource_ids is not None:
            self.gray_resource_ids = gray_resource_ids
        if gray_fail_threshold is not None:
            self.gray_fail_threshold = gray_fail_threshold
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if script_ids is not None:
            self.script_ids = script_ids
        if command is not None:
            self.command = command
        if command_type is not None:
            self.command_type = command_type
        if execution_timeout is not None:
            self.execution_timeout = execution_timeout
        if pre_start is not None:
            self.pre_start = pre_start
        if post_finish is not None:
            self.post_finish = post_finish
        if resource_group_type is not None:
            self.resource_group_type = resource_group_type
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id

    @property
    def gray_count(self):
        """Gets the gray_count of this ExecuteScriptOrCommandReq.

        灰度资源数量。

        :return: The gray_count of this ExecuteScriptOrCommandReq.
        :rtype: int
        """
        return self._gray_count

    @gray_count.setter
    def gray_count(self, gray_count):
        """Sets the gray_count of this ExecuteScriptOrCommandReq.

        灰度资源数量。

        :param gray_count: The gray_count of this ExecuteScriptOrCommandReq.
        :type gray_count: int
        """
        self._gray_count = gray_count

    @property
    def resource_type(self):
        """Gets the resource_type of this ExecuteScriptOrCommandReq.

        资源类型，如桌面(DESKTOP)。

        :return: The resource_type of this ExecuteScriptOrCommandReq.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ExecuteScriptOrCommandReq.

        资源类型，如桌面(DESKTOP)。

        :param resource_type: The resource_type of this ExecuteScriptOrCommandReq.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def gray_resource_ids(self):
        """Gets the gray_resource_ids of this ExecuteScriptOrCommandReq.

        灰度执行脚本的资源列表。

        :return: The gray_resource_ids of this ExecuteScriptOrCommandReq.
        :rtype: list[str]
        """
        return self._gray_resource_ids

    @gray_resource_ids.setter
    def gray_resource_ids(self, gray_resource_ids):
        """Sets the gray_resource_ids of this ExecuteScriptOrCommandReq.

        灰度执行脚本的资源列表。

        :param gray_resource_ids: The gray_resource_ids of this ExecuteScriptOrCommandReq.
        :type gray_resource_ids: list[str]
        """
        self._gray_resource_ids = gray_resource_ids

    @property
    def gray_fail_threshold(self):
        """Gets the gray_fail_threshold of this ExecuteScriptOrCommandReq.

        灰度失败阈值，达到阈值后停止进行下一批资源执行脚本，小于gray_count。

        :return: The gray_fail_threshold of this ExecuteScriptOrCommandReq.
        :rtype: int
        """
        return self._gray_fail_threshold

    @gray_fail_threshold.setter
    def gray_fail_threshold(self, gray_fail_threshold):
        """Sets the gray_fail_threshold of this ExecuteScriptOrCommandReq.

        灰度失败阈值，达到阈值后停止进行下一批资源执行脚本，小于gray_count。

        :param gray_fail_threshold: The gray_fail_threshold of this ExecuteScriptOrCommandReq.
        :type gray_fail_threshold: int
        """
        self._gray_fail_threshold = gray_fail_threshold

    @property
    def resource_ids(self):
        """Gets the resource_ids of this ExecuteScriptOrCommandReq.

        执行脚本的资源列表。

        :return: The resource_ids of this ExecuteScriptOrCommandReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this ExecuteScriptOrCommandReq.

        执行脚本的资源列表。

        :param resource_ids: The resource_ids of this ExecuteScriptOrCommandReq.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def script_ids(self):
        """Gets the script_ids of this ExecuteScriptOrCommandReq.

        执行的脚本列表。

        :return: The script_ids of this ExecuteScriptOrCommandReq.
        :rtype: list[str]
        """
        return self._script_ids

    @script_ids.setter
    def script_ids(self, script_ids):
        """Sets the script_ids of this ExecuteScriptOrCommandReq.

        执行的脚本列表。

        :param script_ids: The script_ids of this ExecuteScriptOrCommandReq.
        :type script_ids: list[str]
        """
        self._script_ids = script_ids

    @property
    def command(self):
        """Gets the command of this ExecuteScriptOrCommandReq.

        执行的命令行，与scripts二选一。

        :return: The command of this ExecuteScriptOrCommandReq.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ExecuteScriptOrCommandReq.

        执行的命令行，与scripts二选一。

        :param command: The command of this ExecuteScriptOrCommandReq.
        :type command: str
        """
        self._command = command

    @property
    def command_type(self):
        """Gets the command_type of this ExecuteScriptOrCommandReq.

        命令行的类型（POWERSHELL，BAT，SHELL）。

        :return: The command_type of this ExecuteScriptOrCommandReq.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """Sets the command_type of this ExecuteScriptOrCommandReq.

        命令行的类型（POWERSHELL，BAT，SHELL）。

        :param command_type: The command_type of this ExecuteScriptOrCommandReq.
        :type command_type: str
        """
        self._command_type = command_type

    @property
    def execution_timeout(self):
        """Gets the execution_timeout of this ExecuteScriptOrCommandReq.

        执行脚本的超时时间，单位分钟。

        :return: The execution_timeout of this ExecuteScriptOrCommandReq.
        :rtype: int
        """
        return self._execution_timeout

    @execution_timeout.setter
    def execution_timeout(self, execution_timeout):
        """Sets the execution_timeout of this ExecuteScriptOrCommandReq.

        执行脚本的超时时间，单位分钟。

        :param execution_timeout: The execution_timeout of this ExecuteScriptOrCommandReq.
        :type execution_timeout: int
        """
        self._execution_timeout = execution_timeout

    @property
    def pre_start(self):
        """Gets the pre_start of this ExecuteScriptOrCommandReq.

        执行脚本前置步骤。

        :return: The pre_start of this ExecuteScriptOrCommandReq.
        :rtype: str
        """
        return self._pre_start

    @pre_start.setter
    def pre_start(self, pre_start):
        """Sets the pre_start of this ExecuteScriptOrCommandReq.

        执行脚本前置步骤。

        :param pre_start: The pre_start of this ExecuteScriptOrCommandReq.
        :type pre_start: str
        """
        self._pre_start = pre_start

    @property
    def post_finish(self):
        """Gets the post_finish of this ExecuteScriptOrCommandReq.

        执行脚本后置步骤(STOP,REBOOT)。

        :return: The post_finish of this ExecuteScriptOrCommandReq.
        :rtype: str
        """
        return self._post_finish

    @post_finish.setter
    def post_finish(self, post_finish):
        """Sets the post_finish of this ExecuteScriptOrCommandReq.

        执行脚本后置步骤(STOP,REBOOT)。

        :param post_finish: The post_finish of this ExecuteScriptOrCommandReq.
        :type post_finish: str
        """
        self._post_finish = post_finish

    @property
    def resource_group_type(self):
        """Gets the resource_group_type of this ExecuteScriptOrCommandReq.

        资源组类型，如桌面池(DESKTOP_POOL)。

        :return: The resource_group_type of this ExecuteScriptOrCommandReq.
        :rtype: str
        """
        return self._resource_group_type

    @resource_group_type.setter
    def resource_group_type(self, resource_group_type):
        """Sets the resource_group_type of this ExecuteScriptOrCommandReq.

        资源组类型，如桌面池(DESKTOP_POOL)。

        :param resource_group_type: The resource_group_type of this ExecuteScriptOrCommandReq.
        :type resource_group_type: str
        """
        self._resource_group_type = resource_group_type

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this ExecuteScriptOrCommandReq.

        资源组ID。

        :return: The resource_group_id of this ExecuteScriptOrCommandReq.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this ExecuteScriptOrCommandReq.

        资源组ID。

        :param resource_group_id: The resource_group_id of this ExecuteScriptOrCommandReq.
        :type resource_group_id: str
        """
        self._resource_group_id = resource_group_id

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
        if not isinstance(other, ExecuteScriptOrCommandReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
