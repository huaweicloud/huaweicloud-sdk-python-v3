# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerAppStatusResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'web_midware': 'str',
        'jdk_version': 'str',
        'port_list': 'list[int]',
        'pid': 'int',
        'cmd_line': 'str',
        'error_info': 'str',
        'start_time': 'str',
        'app_protect_status': 'int',
        'chk_feature_name': 'str'
    }

    attribute_map = {
        'web_midware': 'web_midware',
        'jdk_version': 'jdk_version',
        'port_list': 'port_list',
        'pid': 'pid',
        'cmd_line': 'cmd_line',
        'error_info': 'error_info',
        'start_time': 'start_time',
        'app_protect_status': 'app_protect_status',
        'chk_feature_name': 'chk_feature_name'
    }

    def __init__(self, web_midware=None, jdk_version=None, port_list=None, pid=None, cmd_line=None, error_info=None, start_time=None, app_protect_status=None, chk_feature_name=None):
        r"""ServerAppStatusResponseInfo

        The model defined in huaweicloud sdk

        :param web_midware: web中间件名称
        :type web_midware: str
        :param jdk_version: jdk版本
        :type jdk_version: str
        :param port_list: java应用监听的端口列表
        :type port_list: list[int]
        :param pid: process id
        :type pid: int
        :param cmd_line: 启动命令
        :type cmd_line: str
        :param error_info: 动态接入报错信息
        :type error_info: str
        :param start_time: 应用启动时间，毫秒级时间戳(ms)
        :type start_time: str
        :param app_protect_status: java应用防护状态，包含如下4种。 - 0 ：未防护。 - 1 ：防护失败。 - 2 ：手动防护成功。 - 3 ：自动防护成功
        :type app_protect_status: int
        :param chk_feature_name: 检测规则标识
        :type chk_feature_name: str
        """
        
        

        self._web_midware = None
        self._jdk_version = None
        self._port_list = None
        self._pid = None
        self._cmd_line = None
        self._error_info = None
        self._start_time = None
        self._app_protect_status = None
        self._chk_feature_name = None
        self.discriminator = None

        if web_midware is not None:
            self.web_midware = web_midware
        if jdk_version is not None:
            self.jdk_version = jdk_version
        if port_list is not None:
            self.port_list = port_list
        if pid is not None:
            self.pid = pid
        if cmd_line is not None:
            self.cmd_line = cmd_line
        if error_info is not None:
            self.error_info = error_info
        if start_time is not None:
            self.start_time = start_time
        if app_protect_status is not None:
            self.app_protect_status = app_protect_status
        if chk_feature_name is not None:
            self.chk_feature_name = chk_feature_name

    @property
    def web_midware(self):
        r"""Gets the web_midware of this ServerAppStatusResponseInfo.

        web中间件名称

        :return: The web_midware of this ServerAppStatusResponseInfo.
        :rtype: str
        """
        return self._web_midware

    @web_midware.setter
    def web_midware(self, web_midware):
        r"""Sets the web_midware of this ServerAppStatusResponseInfo.

        web中间件名称

        :param web_midware: The web_midware of this ServerAppStatusResponseInfo.
        :type web_midware: str
        """
        self._web_midware = web_midware

    @property
    def jdk_version(self):
        r"""Gets the jdk_version of this ServerAppStatusResponseInfo.

        jdk版本

        :return: The jdk_version of this ServerAppStatusResponseInfo.
        :rtype: str
        """
        return self._jdk_version

    @jdk_version.setter
    def jdk_version(self, jdk_version):
        r"""Sets the jdk_version of this ServerAppStatusResponseInfo.

        jdk版本

        :param jdk_version: The jdk_version of this ServerAppStatusResponseInfo.
        :type jdk_version: str
        """
        self._jdk_version = jdk_version

    @property
    def port_list(self):
        r"""Gets the port_list of this ServerAppStatusResponseInfo.

        java应用监听的端口列表

        :return: The port_list of this ServerAppStatusResponseInfo.
        :rtype: list[int]
        """
        return self._port_list

    @port_list.setter
    def port_list(self, port_list):
        r"""Sets the port_list of this ServerAppStatusResponseInfo.

        java应用监听的端口列表

        :param port_list: The port_list of this ServerAppStatusResponseInfo.
        :type port_list: list[int]
        """
        self._port_list = port_list

    @property
    def pid(self):
        r"""Gets the pid of this ServerAppStatusResponseInfo.

        process id

        :return: The pid of this ServerAppStatusResponseInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this ServerAppStatusResponseInfo.

        process id

        :param pid: The pid of this ServerAppStatusResponseInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def cmd_line(self):
        r"""Gets the cmd_line of this ServerAppStatusResponseInfo.

        启动命令

        :return: The cmd_line of this ServerAppStatusResponseInfo.
        :rtype: str
        """
        return self._cmd_line

    @cmd_line.setter
    def cmd_line(self, cmd_line):
        r"""Sets the cmd_line of this ServerAppStatusResponseInfo.

        启动命令

        :param cmd_line: The cmd_line of this ServerAppStatusResponseInfo.
        :type cmd_line: str
        """
        self._cmd_line = cmd_line

    @property
    def error_info(self):
        r"""Gets the error_info of this ServerAppStatusResponseInfo.

        动态接入报错信息

        :return: The error_info of this ServerAppStatusResponseInfo.
        :rtype: str
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this ServerAppStatusResponseInfo.

        动态接入报错信息

        :param error_info: The error_info of this ServerAppStatusResponseInfo.
        :type error_info: str
        """
        self._error_info = error_info

    @property
    def start_time(self):
        r"""Gets the start_time of this ServerAppStatusResponseInfo.

        应用启动时间，毫秒级时间戳(ms)

        :return: The start_time of this ServerAppStatusResponseInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ServerAppStatusResponseInfo.

        应用启动时间，毫秒级时间戳(ms)

        :param start_time: The start_time of this ServerAppStatusResponseInfo.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def app_protect_status(self):
        r"""Gets the app_protect_status of this ServerAppStatusResponseInfo.

        java应用防护状态，包含如下4种。 - 0 ：未防护。 - 1 ：防护失败。 - 2 ：手动防护成功。 - 3 ：自动防护成功

        :return: The app_protect_status of this ServerAppStatusResponseInfo.
        :rtype: int
        """
        return self._app_protect_status

    @app_protect_status.setter
    def app_protect_status(self, app_protect_status):
        r"""Sets the app_protect_status of this ServerAppStatusResponseInfo.

        java应用防护状态，包含如下4种。 - 0 ：未防护。 - 1 ：防护失败。 - 2 ：手动防护成功。 - 3 ：自动防护成功

        :param app_protect_status: The app_protect_status of this ServerAppStatusResponseInfo.
        :type app_protect_status: int
        """
        self._app_protect_status = app_protect_status

    @property
    def chk_feature_name(self):
        r"""Gets the chk_feature_name of this ServerAppStatusResponseInfo.

        检测规则标识

        :return: The chk_feature_name of this ServerAppStatusResponseInfo.
        :rtype: str
        """
        return self._chk_feature_name

    @chk_feature_name.setter
    def chk_feature_name(self, chk_feature_name):
        r"""Sets the chk_feature_name of this ServerAppStatusResponseInfo.

        检测规则标识

        :param chk_feature_name: The chk_feature_name of this ServerAppStatusResponseInfo.
        :type chk_feature_name: str
        """
        self._chk_feature_name = chk_feature_name

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
        if not isinstance(other, ServerAppStatusResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
