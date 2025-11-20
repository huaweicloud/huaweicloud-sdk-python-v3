# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginStatusInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'host_type': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'host_status': 'str',
        'agent_status': 'str',
        'agent_version': 'str',
        'asset_value': 'str',
        'os_type': 'str',
        'os_arch': 'str',
        'os_name': 'str',
        'os_version': 'str',
        'plugin_status': 'str',
        'plugin_version': 'str',
        'status_detail': 'str',
        'install_progress': 'str',
        'remaining_time': 'str',
        'protect_status': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_type': 'host_type',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'agent_version': 'agent_version',
        'asset_value': 'asset_value',
        'os_type': 'os_type',
        'os_arch': 'os_arch',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'plugin_status': 'plugin_status',
        'plugin_version': 'plugin_version',
        'status_detail': 'status_detail',
        'install_progress': 'install_progress',
        'remaining_time': 'remaining_time',
        'protect_status': 'protect_status'
    }

    def __init__(self, host_id=None, host_name=None, host_type=None, private_ip=None, public_ip=None, host_status=None, agent_status=None, agent_version=None, asset_value=None, os_type=None, os_arch=None, os_name=None, os_version=None, plugin_status=None, plugin_version=None, status_detail=None, install_progress=None, remaining_time=None, protect_status=None):
        r"""PluginStatusInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 服务器ID **取值范围**: 字符长度1-128 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param host_type: **参数解释**: 服务器类型 **取值范围**: - host：非容器主机 - container：容器主机 
        :type host_type: str
        :param private_ip: **参数解释**: 服务器私网IP地址 **取值范围**: 字符长度0-128 
        :type private_ip: str
        :param public_ip: **参数解释**: 服务器公网IP地址 **取值范围**: 字符长度0-128 
        :type public_ip: str
        :param host_status: **参数解释**: 服务器状态 **取值范围**: - ACTIVE：正在运行 - BUILDING：创建中 - ERROR：故障 - SHUTOFF：关机 
        :type host_status: str
        :param agent_status: **参数解释**: Agent状态 **取值范围**: - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中
        :type agent_status: str
        :param agent_version: **参数解释**： agent版本 **取值范围**： 字符长度0-32位
        :type agent_version: str
        :param asset_value: **参数解释**: 服务器的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 
        :type asset_value: str
        :param os_type: **参数解释**: 操作系统类型 **取值范围**: - linux：Linux操作系统 - windows：windows操作系统 
        :type os_type: str
        :param os_arch: **参数解释**: 系统架构 **取值范围**: - x86_64：X86架构 - arm：ARM架构 
        :type os_arch: str
        :param os_name: **参数解释**: 系统名称 **取值范围**: 不涉及 
        :type os_name: str
        :param os_version: **参数解释**: 操作系统类型 **取值范围**: - linux：Linux操作系统 - windows：windows操作系统 系统版本 
        :type os_version: str
        :param plugin_status: **参数解释**: 插件状态 **取值范围**: - not_installed：未安装 - installing：安装中 - install_fail：安装失败 - starting：启动中 - running：运行中 - start_fail：启动失败 - offline：离线 - stopping：停止中 - stopped：已停止 - updating：更新中 - update_fail：更新失败 - uninstalling：卸载中 - uninstall_fail：卸载失败 
        :type plugin_status: str
        :param plugin_version: **参数解释**: 插件版本 **取值范围**: 不涉及 
        :type plugin_version: str
        :param status_detail: **参数解释**: 插件操作失败原因，包括安装失败、启动失败、离线、停止失败、更新失败以及卸载失败 **取值范围**: 不涉及 
        :type status_detail: str
        :param install_progress: **参数解释**: 插件安装进度，百分比 **取值范围**: 0-99 
        :type install_progress: str
        :param remaining_time: **参数解释**: 插件剩余安装时间，单位分钟 **取值范围**: 不涉及 
        :type remaining_time: str
        :param protect_status: **参数解释**: 主机防护状态 **取值范围**: - closed：未开启 - opened：防护中 
        :type protect_status: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._host_type = None
        self._private_ip = None
        self._public_ip = None
        self._host_status = None
        self._agent_status = None
        self._agent_version = None
        self._asset_value = None
        self._os_type = None
        self._os_arch = None
        self._os_name = None
        self._os_version = None
        self._plugin_status = None
        self._plugin_version = None
        self._status_detail = None
        self._install_progress = None
        self._remaining_time = None
        self._protect_status = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_type is not None:
            self.host_type = host_type
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status
        if agent_version is not None:
            self.agent_version = agent_version
        if asset_value is not None:
            self.asset_value = asset_value
        if os_type is not None:
            self.os_type = os_type
        if os_arch is not None:
            self.os_arch = os_arch
        if os_name is not None:
            self.os_name = os_name
        if os_version is not None:
            self.os_version = os_version
        if plugin_status is not None:
            self.plugin_status = plugin_status
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if status_detail is not None:
            self.status_detail = status_detail
        if install_progress is not None:
            self.install_progress = install_progress
        if remaining_time is not None:
            self.remaining_time = remaining_time
        if protect_status is not None:
            self.protect_status = protect_status

    @property
    def host_id(self):
        r"""Gets the host_id of this PluginStatusInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度1-128 

        :return: The host_id of this PluginStatusInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this PluginStatusInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度1-128 

        :param host_id: The host_id of this PluginStatusInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this PluginStatusInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this PluginStatusInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this PluginStatusInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this PluginStatusInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_type(self):
        r"""Gets the host_type of this PluginStatusInfo.

        **参数解释**: 服务器类型 **取值范围**: - host：非容器主机 - container：容器主机 

        :return: The host_type of this PluginStatusInfo.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this PluginStatusInfo.

        **参数解释**: 服务器类型 **取值范围**: - host：非容器主机 - container：容器主机 

        :param host_type: The host_type of this PluginStatusInfo.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def private_ip(self):
        r"""Gets the private_ip of this PluginStatusInfo.

        **参数解释**: 服务器私网IP地址 **取值范围**: 字符长度0-128 

        :return: The private_ip of this PluginStatusInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this PluginStatusInfo.

        **参数解释**: 服务器私网IP地址 **取值范围**: 字符长度0-128 

        :param private_ip: The private_ip of this PluginStatusInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this PluginStatusInfo.

        **参数解释**: 服务器公网IP地址 **取值范围**: 字符长度0-128 

        :return: The public_ip of this PluginStatusInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this PluginStatusInfo.

        **参数解释**: 服务器公网IP地址 **取值范围**: 字符长度0-128 

        :param public_ip: The public_ip of this PluginStatusInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def host_status(self):
        r"""Gets the host_status of this PluginStatusInfo.

        **参数解释**: 服务器状态 **取值范围**: - ACTIVE：正在运行 - BUILDING：创建中 - ERROR：故障 - SHUTOFF：关机 

        :return: The host_status of this PluginStatusInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this PluginStatusInfo.

        **参数解释**: 服务器状态 **取值范围**: - ACTIVE：正在运行 - BUILDING：创建中 - ERROR：故障 - SHUTOFF：关机 

        :param host_status: The host_status of this PluginStatusInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this PluginStatusInfo.

        **参数解释**: Agent状态 **取值范围**: - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中

        :return: The agent_status of this PluginStatusInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this PluginStatusInfo.

        **参数解释**: Agent状态 **取值范围**: - not_installed：未安装 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中

        :param agent_status: The agent_status of this PluginStatusInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def agent_version(self):
        r"""Gets the agent_version of this PluginStatusInfo.

        **参数解释**： agent版本 **取值范围**： 字符长度0-32位

        :return: The agent_version of this PluginStatusInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this PluginStatusInfo.

        **参数解释**： agent版本 **取值范围**： 字符长度0-32位

        :param agent_version: The agent_version of this PluginStatusInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def asset_value(self):
        r"""Gets the asset_value of this PluginStatusInfo.

        **参数解释**: 服务器的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 

        :return: The asset_value of this PluginStatusInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this PluginStatusInfo.

        **参数解释**: 服务器的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 

        :param asset_value: The asset_value of this PluginStatusInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def os_type(self):
        r"""Gets the os_type of this PluginStatusInfo.

        **参数解释**: 操作系统类型 **取值范围**: - linux：Linux操作系统 - windows：windows操作系统 

        :return: The os_type of this PluginStatusInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this PluginStatusInfo.

        **参数解释**: 操作系统类型 **取值范围**: - linux：Linux操作系统 - windows：windows操作系统 

        :param os_type: The os_type of this PluginStatusInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_arch(self):
        r"""Gets the os_arch of this PluginStatusInfo.

        **参数解释**: 系统架构 **取值范围**: - x86_64：X86架构 - arm：ARM架构 

        :return: The os_arch of this PluginStatusInfo.
        :rtype: str
        """
        return self._os_arch

    @os_arch.setter
    def os_arch(self, os_arch):
        r"""Sets the os_arch of this PluginStatusInfo.

        **参数解释**: 系统架构 **取值范围**: - x86_64：X86架构 - arm：ARM架构 

        :param os_arch: The os_arch of this PluginStatusInfo.
        :type os_arch: str
        """
        self._os_arch = os_arch

    @property
    def os_name(self):
        r"""Gets the os_name of this PluginStatusInfo.

        **参数解释**: 系统名称 **取值范围**: 不涉及 

        :return: The os_name of this PluginStatusInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this PluginStatusInfo.

        **参数解释**: 系统名称 **取值范围**: 不涉及 

        :param os_name: The os_name of this PluginStatusInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this PluginStatusInfo.

        **参数解释**: 操作系统类型 **取值范围**: - linux：Linux操作系统 - windows：windows操作系统 系统版本 

        :return: The os_version of this PluginStatusInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this PluginStatusInfo.

        **参数解释**: 操作系统类型 **取值范围**: - linux：Linux操作系统 - windows：windows操作系统 系统版本 

        :param os_version: The os_version of this PluginStatusInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def plugin_status(self):
        r"""Gets the plugin_status of this PluginStatusInfo.

        **参数解释**: 插件状态 **取值范围**: - not_installed：未安装 - installing：安装中 - install_fail：安装失败 - starting：启动中 - running：运行中 - start_fail：启动失败 - offline：离线 - stopping：停止中 - stopped：已停止 - updating：更新中 - update_fail：更新失败 - uninstalling：卸载中 - uninstall_fail：卸载失败 

        :return: The plugin_status of this PluginStatusInfo.
        :rtype: str
        """
        return self._plugin_status

    @plugin_status.setter
    def plugin_status(self, plugin_status):
        r"""Sets the plugin_status of this PluginStatusInfo.

        **参数解释**: 插件状态 **取值范围**: - not_installed：未安装 - installing：安装中 - install_fail：安装失败 - starting：启动中 - running：运行中 - start_fail：启动失败 - offline：离线 - stopping：停止中 - stopped：已停止 - updating：更新中 - update_fail：更新失败 - uninstalling：卸载中 - uninstall_fail：卸载失败 

        :param plugin_status: The plugin_status of this PluginStatusInfo.
        :type plugin_status: str
        """
        self._plugin_status = plugin_status

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this PluginStatusInfo.

        **参数解释**: 插件版本 **取值范围**: 不涉及 

        :return: The plugin_version of this PluginStatusInfo.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this PluginStatusInfo.

        **参数解释**: 插件版本 **取值范围**: 不涉及 

        :param plugin_version: The plugin_version of this PluginStatusInfo.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def status_detail(self):
        r"""Gets the status_detail of this PluginStatusInfo.

        **参数解释**: 插件操作失败原因，包括安装失败、启动失败、离线、停止失败、更新失败以及卸载失败 **取值范围**: 不涉及 

        :return: The status_detail of this PluginStatusInfo.
        :rtype: str
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        r"""Sets the status_detail of this PluginStatusInfo.

        **参数解释**: 插件操作失败原因，包括安装失败、启动失败、离线、停止失败、更新失败以及卸载失败 **取值范围**: 不涉及 

        :param status_detail: The status_detail of this PluginStatusInfo.
        :type status_detail: str
        """
        self._status_detail = status_detail

    @property
    def install_progress(self):
        r"""Gets the install_progress of this PluginStatusInfo.

        **参数解释**: 插件安装进度，百分比 **取值范围**: 0-99 

        :return: The install_progress of this PluginStatusInfo.
        :rtype: str
        """
        return self._install_progress

    @install_progress.setter
    def install_progress(self, install_progress):
        r"""Sets the install_progress of this PluginStatusInfo.

        **参数解释**: 插件安装进度，百分比 **取值范围**: 0-99 

        :param install_progress: The install_progress of this PluginStatusInfo.
        :type install_progress: str
        """
        self._install_progress = install_progress

    @property
    def remaining_time(self):
        r"""Gets the remaining_time of this PluginStatusInfo.

        **参数解释**: 插件剩余安装时间，单位分钟 **取值范围**: 不涉及 

        :return: The remaining_time of this PluginStatusInfo.
        :rtype: str
        """
        return self._remaining_time

    @remaining_time.setter
    def remaining_time(self, remaining_time):
        r"""Sets the remaining_time of this PluginStatusInfo.

        **参数解释**: 插件剩余安装时间，单位分钟 **取值范围**: 不涉及 

        :param remaining_time: The remaining_time of this PluginStatusInfo.
        :type remaining_time: str
        """
        self._remaining_time = remaining_time

    @property
    def protect_status(self):
        r"""Gets the protect_status of this PluginStatusInfo.

        **参数解释**: 主机防护状态 **取值范围**: - closed：未开启 - opened：防护中 

        :return: The protect_status of this PluginStatusInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this PluginStatusInfo.

        **参数解释**: 主机防护状态 **取值范围**: - closed：未开启 - opened：防护中 

        :param protect_status: The protect_status of this PluginStatusInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    def to_dict(self):
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
        if not isinstance(other, PluginStatusInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
