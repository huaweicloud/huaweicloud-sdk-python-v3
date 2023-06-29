# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAppReq:

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
        'version': 'str',
        'execute_path': 'str',
        'work_path': 'str',
        'description': 'str',
        'command_param': 'str',
        'state': 'AppStateEnum',
        'sandbox_enable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'execute_path': 'execute_path',
        'work_path': 'work_path',
        'description': 'description',
        'command_param': 'command_param',
        'state': 'state',
        'sandbox_enable': 'sandbox_enable'
    }

    def __init__(self, name=None, version=None, execute_path=None, work_path=None, description=None, command_param=None, state=None, sandbox_enable=None):
        """UpdateAppReq

        The model defined in huaweicloud sdk

        :param name: 应用名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格 2. 长度1~64个字符
        :type name: str
        :param version: 应用版本号
        :type version: str
        :param execute_path: 执行路径
        :type execute_path: str
        :param work_path: 应用工作目录
        :type work_path: str
        :param description: 应用描述
        :type description: str
        :param command_param: 启动命令行参数
        :type command_param: str
        :param state: 
        :type state: :class:`huaweicloudsdkworkspaceapp.v1.AppStateEnum`
        :param sandbox_enable: 是否使用沙箱模式运行，取值为： - false: 表示不以沙箱模式运行 - true: 表示以沙箱模式运行
        :type sandbox_enable: bool
        """
        
        

        self._name = None
        self._version = None
        self._execute_path = None
        self._work_path = None
        self._description = None
        self._command_param = None
        self._state = None
        self._sandbox_enable = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if execute_path is not None:
            self.execute_path = execute_path
        if work_path is not None:
            self.work_path = work_path
        if description is not None:
            self.description = description
        if command_param is not None:
            self.command_param = command_param
        if state is not None:
            self.state = state
        if sandbox_enable is not None:
            self.sandbox_enable = sandbox_enable

    @property
    def name(self):
        """Gets the name of this UpdateAppReq.

        应用名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格 2. 长度1~64个字符

        :return: The name of this UpdateAppReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAppReq.

        应用名称,名称需满足如下规则: 1. 名称允许可见字符或空格，不可为全空格 2. 长度1~64个字符

        :param name: The name of this UpdateAppReq.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this UpdateAppReq.

        应用版本号

        :return: The version of this UpdateAppReq.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateAppReq.

        应用版本号

        :param version: The version of this UpdateAppReq.
        :type version: str
        """
        self._version = version

    @property
    def execute_path(self):
        """Gets the execute_path of this UpdateAppReq.

        执行路径

        :return: The execute_path of this UpdateAppReq.
        :rtype: str
        """
        return self._execute_path

    @execute_path.setter
    def execute_path(self, execute_path):
        """Sets the execute_path of this UpdateAppReq.

        执行路径

        :param execute_path: The execute_path of this UpdateAppReq.
        :type execute_path: str
        """
        self._execute_path = execute_path

    @property
    def work_path(self):
        """Gets the work_path of this UpdateAppReq.

        应用工作目录

        :return: The work_path of this UpdateAppReq.
        :rtype: str
        """
        return self._work_path

    @work_path.setter
    def work_path(self, work_path):
        """Sets the work_path of this UpdateAppReq.

        应用工作目录

        :param work_path: The work_path of this UpdateAppReq.
        :type work_path: str
        """
        self._work_path = work_path

    @property
    def description(self):
        """Gets the description of this UpdateAppReq.

        应用描述

        :return: The description of this UpdateAppReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAppReq.

        应用描述

        :param description: The description of this UpdateAppReq.
        :type description: str
        """
        self._description = description

    @property
    def command_param(self):
        """Gets the command_param of this UpdateAppReq.

        启动命令行参数

        :return: The command_param of this UpdateAppReq.
        :rtype: str
        """
        return self._command_param

    @command_param.setter
    def command_param(self, command_param):
        """Sets the command_param of this UpdateAppReq.

        启动命令行参数

        :param command_param: The command_param of this UpdateAppReq.
        :type command_param: str
        """
        self._command_param = command_param

    @property
    def state(self):
        """Gets the state of this UpdateAppReq.

        :return: The state of this UpdateAppReq.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppStateEnum`
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdateAppReq.

        :param state: The state of this UpdateAppReq.
        :type state: :class:`huaweicloudsdkworkspaceapp.v1.AppStateEnum`
        """
        self._state = state

    @property
    def sandbox_enable(self):
        """Gets the sandbox_enable of this UpdateAppReq.

        是否使用沙箱模式运行，取值为： - false: 表示不以沙箱模式运行 - true: 表示以沙箱模式运行

        :return: The sandbox_enable of this UpdateAppReq.
        :rtype: bool
        """
        return self._sandbox_enable

    @sandbox_enable.setter
    def sandbox_enable(self, sandbox_enable):
        """Sets the sandbox_enable of this UpdateAppReq.

        是否使用沙箱模式运行，取值为： - false: 表示不以沙箱模式运行 - true: 表示以沙箱模式运行

        :param sandbox_enable: The sandbox_enable of this UpdateAppReq.
        :type sandbox_enable: bool
        """
        self._sandbox_enable = sandbox_enable

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
        if not isinstance(other, UpdateAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
