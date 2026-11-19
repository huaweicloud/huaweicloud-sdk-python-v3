# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDefenderPluginManualCommandResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'opt': 'str',
        'claw_plugin_command': 'str',
        'script_url': 'str',
        'install_key': 'str',
        'plugin_pkg_url': 'str',
        'endpoint': 'str',
        'expire_time': 'int',
        'query_result_cmd': 'str'
    }

    attribute_map = {
        'opt': 'opt',
        'claw_plugin_command': 'claw_plugin_command',
        'script_url': 'script_url',
        'install_key': 'install_key',
        'plugin_pkg_url': 'plugin_pkg_url',
        'endpoint': 'endpoint',
        'expire_time': 'expire_time',
        'query_result_cmd': 'query_result_cmd'
    }

    def __init__(self, opt=None, claw_plugin_command=None, script_url=None, install_key=None, plugin_pkg_url=None, endpoint=None, expire_time=None, query_result_cmd=None):
        r"""ShowDefenderPluginManualCommandResponse

        The model defined in huaweicloud sdk

        :param opt: **参数解释**： 操作类型，回显请求的opt值 **取值范围**： - install：安装 - uninstall：卸载 
        :type opt: str
        :param claw_plugin_command: **参数解释**： 完整的手动操作命令，可直接复制到终端执行 **取值范围**： 字符长度为1-4096位 
        :type claw_plugin_command: str
        :param script_url: **参数解释**： 脚本下载地址 **取值范围**： 字符长度为1-512位 
        :type script_url: str
        :param install_key: **参数解释**： 安装凭证 **取值范围**： 字符长度为1-256位 
        :type install_key: str
        :param plugin_pkg_url: **参数解释**： 插件包下载地址 **取值范围**： 字符长度为1-512位 
        :type plugin_pkg_url: str
        :param endpoint: **参数解释**： AI Defender服务端地址 **取值范围**： 字符长度为1-512位 
        :type endpoint: str
        :param expire_time: **参数解释**： 安装凭证过期时间，毫秒时间戳，过期后需重新获取 **取值范围**： 最小值0，最大值9223372036854775807 
        :type expire_time: int
        :param query_result_cmd: **参数解释**： 查询安装结果命令 **取值范围**： \&quot;openclaw plugins info AgentDR_OpenClaw\&quot; 
        :type query_result_cmd: str
        """
        
        super().__init__()

        self._opt = None
        self._claw_plugin_command = None
        self._script_url = None
        self._install_key = None
        self._plugin_pkg_url = None
        self._endpoint = None
        self._expire_time = None
        self._query_result_cmd = None
        self.discriminator = None

        if opt is not None:
            self.opt = opt
        if claw_plugin_command is not None:
            self.claw_plugin_command = claw_plugin_command
        if script_url is not None:
            self.script_url = script_url
        if install_key is not None:
            self.install_key = install_key
        if plugin_pkg_url is not None:
            self.plugin_pkg_url = plugin_pkg_url
        if endpoint is not None:
            self.endpoint = endpoint
        if expire_time is not None:
            self.expire_time = expire_time
        if query_result_cmd is not None:
            self.query_result_cmd = query_result_cmd

    @property
    def opt(self):
        r"""Gets the opt of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 操作类型，回显请求的opt值 **取值范围**： - install：安装 - uninstall：卸载 

        :return: The opt of this ShowDefenderPluginManualCommandResponse.
        :rtype: str
        """
        return self._opt

    @opt.setter
    def opt(self, opt):
        r"""Sets the opt of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 操作类型，回显请求的opt值 **取值范围**： - install：安装 - uninstall：卸载 

        :param opt: The opt of this ShowDefenderPluginManualCommandResponse.
        :type opt: str
        """
        self._opt = opt

    @property
    def claw_plugin_command(self):
        r"""Gets the claw_plugin_command of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 完整的手动操作命令，可直接复制到终端执行 **取值范围**： 字符长度为1-4096位 

        :return: The claw_plugin_command of this ShowDefenderPluginManualCommandResponse.
        :rtype: str
        """
        return self._claw_plugin_command

    @claw_plugin_command.setter
    def claw_plugin_command(self, claw_plugin_command):
        r"""Sets the claw_plugin_command of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 完整的手动操作命令，可直接复制到终端执行 **取值范围**： 字符长度为1-4096位 

        :param claw_plugin_command: The claw_plugin_command of this ShowDefenderPluginManualCommandResponse.
        :type claw_plugin_command: str
        """
        self._claw_plugin_command = claw_plugin_command

    @property
    def script_url(self):
        r"""Gets the script_url of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 脚本下载地址 **取值范围**： 字符长度为1-512位 

        :return: The script_url of this ShowDefenderPluginManualCommandResponse.
        :rtype: str
        """
        return self._script_url

    @script_url.setter
    def script_url(self, script_url):
        r"""Sets the script_url of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 脚本下载地址 **取值范围**： 字符长度为1-512位 

        :param script_url: The script_url of this ShowDefenderPluginManualCommandResponse.
        :type script_url: str
        """
        self._script_url = script_url

    @property
    def install_key(self):
        r"""Gets the install_key of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 安装凭证 **取值范围**： 字符长度为1-256位 

        :return: The install_key of this ShowDefenderPluginManualCommandResponse.
        :rtype: str
        """
        return self._install_key

    @install_key.setter
    def install_key(self, install_key):
        r"""Sets the install_key of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 安装凭证 **取值范围**： 字符长度为1-256位 

        :param install_key: The install_key of this ShowDefenderPluginManualCommandResponse.
        :type install_key: str
        """
        self._install_key = install_key

    @property
    def plugin_pkg_url(self):
        r"""Gets the plugin_pkg_url of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 插件包下载地址 **取值范围**： 字符长度为1-512位 

        :return: The plugin_pkg_url of this ShowDefenderPluginManualCommandResponse.
        :rtype: str
        """
        return self._plugin_pkg_url

    @plugin_pkg_url.setter
    def plugin_pkg_url(self, plugin_pkg_url):
        r"""Sets the plugin_pkg_url of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 插件包下载地址 **取值范围**： 字符长度为1-512位 

        :param plugin_pkg_url: The plugin_pkg_url of this ShowDefenderPluginManualCommandResponse.
        :type plugin_pkg_url: str
        """
        self._plugin_pkg_url = plugin_pkg_url

    @property
    def endpoint(self):
        r"""Gets the endpoint of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： AI Defender服务端地址 **取值范围**： 字符长度为1-512位 

        :return: The endpoint of this ShowDefenderPluginManualCommandResponse.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        r"""Sets the endpoint of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： AI Defender服务端地址 **取值范围**： 字符长度为1-512位 

        :param endpoint: The endpoint of this ShowDefenderPluginManualCommandResponse.
        :type endpoint: str
        """
        self._endpoint = endpoint

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 安装凭证过期时间，毫秒时间戳，过期后需重新获取 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The expire_time of this ShowDefenderPluginManualCommandResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 安装凭证过期时间，毫秒时间戳，过期后需重新获取 **取值范围**： 最小值0，最大值9223372036854775807 

        :param expire_time: The expire_time of this ShowDefenderPluginManualCommandResponse.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def query_result_cmd(self):
        r"""Gets the query_result_cmd of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 查询安装结果命令 **取值范围**： \"openclaw plugins info AgentDR_OpenClaw\" 

        :return: The query_result_cmd of this ShowDefenderPluginManualCommandResponse.
        :rtype: str
        """
        return self._query_result_cmd

    @query_result_cmd.setter
    def query_result_cmd(self, query_result_cmd):
        r"""Sets the query_result_cmd of this ShowDefenderPluginManualCommandResponse.

        **参数解释**： 查询安装结果命令 **取值范围**： \"openclaw plugins info AgentDR_OpenClaw\" 

        :param query_result_cmd: The query_result_cmd of this ShowDefenderPluginManualCommandResponse.
        :type query_result_cmd: str
        """
        self._query_result_cmd = query_result_cmd

    def to_dict(self):
        import warnings
        warnings.warn("ShowDefenderPluginManualCommandResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowDefenderPluginManualCommandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
