# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteDesktopPoolScriptsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'script_ids': 'list[str]',
        'gray_count': 'int',
        'gray_desktop_ids': 'list[str]',
        'gray_fail_threshold': 'int',
        'pre_start': 'str',
        'post_finish': 'str',
        'command_content': 'str',
        'command_type': 'str',
        'execution_timeout': 'int'
    }

    attribute_map = {
        'script_ids': 'script_ids',
        'gray_count': 'gray_count',
        'gray_desktop_ids': 'gray_desktop_ids',
        'gray_fail_threshold': 'gray_fail_threshold',
        'pre_start': 'pre_start',
        'post_finish': 'post_finish',
        'command_content': 'command_content',
        'command_type': 'command_type',
        'execution_timeout': 'execution_timeout'
    }

    def __init__(self, script_ids=None, gray_count=None, gray_desktop_ids=None, gray_fail_threshold=None, pre_start=None, post_finish=None, command_content=None, command_type=None, execution_timeout=None):
        r"""ExecuteDesktopPoolScriptsReq

        The model defined in huaweicloud sdk

        :param script_ids: 执行的脚本id列表，与command二选一。
        :type script_ids: list[str]
        :param gray_count: 首批执行的桌面数量，优先级高于gray_desktop_ids。
        :type gray_count: int
        :param gray_desktop_ids: 首批执行的桌面id列表，优先级低于gray_count。
        :type gray_desktop_ids: list[str]
        :param gray_fail_threshold: 灰度失败阈值，灰度执行失败次数达到该值时，不执行下一批任务。
        :type gray_fail_threshold: int
        :param pre_start: 执行脚本前置步骤。
        :type pre_start: str
        :param post_finish: 执行脚本完成后置步骤，当前支持关机（stop）、重启（reboot）。
        :type post_finish: str
        :param command_content: 执行的命令行，与script_ids二选一。
        :type command_content: str
        :param command_type: 命令行类型，执行命令行时必传。 - POWERSHELL：WINDOWS系统使用。 - BAT：WINDOWS系统使用。 - SHELL：LINUX系统使用。
        :type command_type: str
        :param execution_timeout: 执行脚本的超时时间，单位分钟，默认1分钟。
        :type execution_timeout: int
        """
        
        

        self._script_ids = None
        self._gray_count = None
        self._gray_desktop_ids = None
        self._gray_fail_threshold = None
        self._pre_start = None
        self._post_finish = None
        self._command_content = None
        self._command_type = None
        self._execution_timeout = None
        self.discriminator = None

        if script_ids is not None:
            self.script_ids = script_ids
        if gray_count is not None:
            self.gray_count = gray_count
        if gray_desktop_ids is not None:
            self.gray_desktop_ids = gray_desktop_ids
        if gray_fail_threshold is not None:
            self.gray_fail_threshold = gray_fail_threshold
        if pre_start is not None:
            self.pre_start = pre_start
        if post_finish is not None:
            self.post_finish = post_finish
        if command_content is not None:
            self.command_content = command_content
        if command_type is not None:
            self.command_type = command_type
        if execution_timeout is not None:
            self.execution_timeout = execution_timeout

    @property
    def script_ids(self):
        r"""Gets the script_ids of this ExecuteDesktopPoolScriptsReq.

        执行的脚本id列表，与command二选一。

        :return: The script_ids of this ExecuteDesktopPoolScriptsReq.
        :rtype: list[str]
        """
        return self._script_ids

    @script_ids.setter
    def script_ids(self, script_ids):
        r"""Sets the script_ids of this ExecuteDesktopPoolScriptsReq.

        执行的脚本id列表，与command二选一。

        :param script_ids: The script_ids of this ExecuteDesktopPoolScriptsReq.
        :type script_ids: list[str]
        """
        self._script_ids = script_ids

    @property
    def gray_count(self):
        r"""Gets the gray_count of this ExecuteDesktopPoolScriptsReq.

        首批执行的桌面数量，优先级高于gray_desktop_ids。

        :return: The gray_count of this ExecuteDesktopPoolScriptsReq.
        :rtype: int
        """
        return self._gray_count

    @gray_count.setter
    def gray_count(self, gray_count):
        r"""Sets the gray_count of this ExecuteDesktopPoolScriptsReq.

        首批执行的桌面数量，优先级高于gray_desktop_ids。

        :param gray_count: The gray_count of this ExecuteDesktopPoolScriptsReq.
        :type gray_count: int
        """
        self._gray_count = gray_count

    @property
    def gray_desktop_ids(self):
        r"""Gets the gray_desktop_ids of this ExecuteDesktopPoolScriptsReq.

        首批执行的桌面id列表，优先级低于gray_count。

        :return: The gray_desktop_ids of this ExecuteDesktopPoolScriptsReq.
        :rtype: list[str]
        """
        return self._gray_desktop_ids

    @gray_desktop_ids.setter
    def gray_desktop_ids(self, gray_desktop_ids):
        r"""Sets the gray_desktop_ids of this ExecuteDesktopPoolScriptsReq.

        首批执行的桌面id列表，优先级低于gray_count。

        :param gray_desktop_ids: The gray_desktop_ids of this ExecuteDesktopPoolScriptsReq.
        :type gray_desktop_ids: list[str]
        """
        self._gray_desktop_ids = gray_desktop_ids

    @property
    def gray_fail_threshold(self):
        r"""Gets the gray_fail_threshold of this ExecuteDesktopPoolScriptsReq.

        灰度失败阈值，灰度执行失败次数达到该值时，不执行下一批任务。

        :return: The gray_fail_threshold of this ExecuteDesktopPoolScriptsReq.
        :rtype: int
        """
        return self._gray_fail_threshold

    @gray_fail_threshold.setter
    def gray_fail_threshold(self, gray_fail_threshold):
        r"""Sets the gray_fail_threshold of this ExecuteDesktopPoolScriptsReq.

        灰度失败阈值，灰度执行失败次数达到该值时，不执行下一批任务。

        :param gray_fail_threshold: The gray_fail_threshold of this ExecuteDesktopPoolScriptsReq.
        :type gray_fail_threshold: int
        """
        self._gray_fail_threshold = gray_fail_threshold

    @property
    def pre_start(self):
        r"""Gets the pre_start of this ExecuteDesktopPoolScriptsReq.

        执行脚本前置步骤。

        :return: The pre_start of this ExecuteDesktopPoolScriptsReq.
        :rtype: str
        """
        return self._pre_start

    @pre_start.setter
    def pre_start(self, pre_start):
        r"""Sets the pre_start of this ExecuteDesktopPoolScriptsReq.

        执行脚本前置步骤。

        :param pre_start: The pre_start of this ExecuteDesktopPoolScriptsReq.
        :type pre_start: str
        """
        self._pre_start = pre_start

    @property
    def post_finish(self):
        r"""Gets the post_finish of this ExecuteDesktopPoolScriptsReq.

        执行脚本完成后置步骤，当前支持关机（stop）、重启（reboot）。

        :return: The post_finish of this ExecuteDesktopPoolScriptsReq.
        :rtype: str
        """
        return self._post_finish

    @post_finish.setter
    def post_finish(self, post_finish):
        r"""Sets the post_finish of this ExecuteDesktopPoolScriptsReq.

        执行脚本完成后置步骤，当前支持关机（stop）、重启（reboot）。

        :param post_finish: The post_finish of this ExecuteDesktopPoolScriptsReq.
        :type post_finish: str
        """
        self._post_finish = post_finish

    @property
    def command_content(self):
        r"""Gets the command_content of this ExecuteDesktopPoolScriptsReq.

        执行的命令行，与script_ids二选一。

        :return: The command_content of this ExecuteDesktopPoolScriptsReq.
        :rtype: str
        """
        return self._command_content

    @command_content.setter
    def command_content(self, command_content):
        r"""Sets the command_content of this ExecuteDesktopPoolScriptsReq.

        执行的命令行，与script_ids二选一。

        :param command_content: The command_content of this ExecuteDesktopPoolScriptsReq.
        :type command_content: str
        """
        self._command_content = command_content

    @property
    def command_type(self):
        r"""Gets the command_type of this ExecuteDesktopPoolScriptsReq.

        命令行类型，执行命令行时必传。 - POWERSHELL：WINDOWS系统使用。 - BAT：WINDOWS系统使用。 - SHELL：LINUX系统使用。

        :return: The command_type of this ExecuteDesktopPoolScriptsReq.
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        r"""Sets the command_type of this ExecuteDesktopPoolScriptsReq.

        命令行类型，执行命令行时必传。 - POWERSHELL：WINDOWS系统使用。 - BAT：WINDOWS系统使用。 - SHELL：LINUX系统使用。

        :param command_type: The command_type of this ExecuteDesktopPoolScriptsReq.
        :type command_type: str
        """
        self._command_type = command_type

    @property
    def execution_timeout(self):
        r"""Gets the execution_timeout of this ExecuteDesktopPoolScriptsReq.

        执行脚本的超时时间，单位分钟，默认1分钟。

        :return: The execution_timeout of this ExecuteDesktopPoolScriptsReq.
        :rtype: int
        """
        return self._execution_timeout

    @execution_timeout.setter
    def execution_timeout(self, execution_timeout):
        r"""Sets the execution_timeout of this ExecuteDesktopPoolScriptsReq.

        执行脚本的超时时间，单位分钟，默认1分钟。

        :param execution_timeout: The execution_timeout of this ExecuteDesktopPoolScriptsReq.
        :type execution_timeout: int
        """
        self._execution_timeout = execution_timeout

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
        if not isinstance(other, ExecuteDesktopPoolScriptsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
