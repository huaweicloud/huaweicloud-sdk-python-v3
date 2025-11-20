# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'plugin_code': 'str',
        'plugin_version': 'str',
        'plugin_status': 'str',
        'host_name': 'str',
        'host_ids': 'list[str]',
        'host_status': 'list[str]',
        'agent_status': 'str',
        'os_type': 'str',
        'os_arch': 'str',
        'host_type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'plugin_code': 'plugin_code',
        'plugin_version': 'plugin_version',
        'plugin_status': 'plugin_status',
        'host_name': 'host_name',
        'host_ids': 'host_ids',
        'host_status': 'host_status',
        'agent_status': 'agent_status',
        'os_type': 'os_type',
        'os_arch': 'os_arch',
        'host_type': 'host_type'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, plugin_code=None, plugin_version=None, plugin_status=None, host_name=None, host_ids=None, host_status=None, agent_status=None, os_type=None, os_arch=None, host_type=None):
        r"""ListPluginStatusRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param plugin_code: **参数解释**： 插件编码 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type plugin_code: str
        :param plugin_version: **参数解释**： 插件版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type plugin_version: str
        :param plugin_status: **参数解释**： 插件状态 **约束限制**: 不涉及 **取值范围**: - not_installed：未安装 - installing：安装中 - install_fail：安装失败 - starting：启动中 - running：运行中 - start_fail：启动失败 - offline：离线 - stopping：停止中 - stopped：已停止 - updating：更新中 - update_fail：更新失败 - uninstalling：卸载中 - uninstall_fail：卸载失败  **默认取值**: 不涉及 
        :type plugin_status: str
        :param host_name: **参数解释**： 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_name: str
        :param host_ids: **参数解释**： 服务器ID列表 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type host_ids: list[str]
        :param host_status: **参数解释**： 服务器状态 **约束限制**: 不涉及 **取值范围**: - ACTIVE：正在运行 - BUILDING：创建中 - ERROR：故障 - SHUTOFF：关机  **默认取值**: 不涉及 
        :type host_status: list[str]
        :param agent_status: **参数解释**： agent状态 **约束限制**: 不涉及 **取值范围**: -not_installed：未安装 -online：在线 -offline：离线 -install_failed：安装失败 -installing：安装中  **默认取值**: 不涉及 
        :type agent_status: str
        :param os_type: **参数解释**： 主机操作系统 **约束限制**: 不涉及 **取值范围**: - linux：Linux操作系统 - Windows：windows操作系统  **默认取值**: 不涉及 
        :type os_type: str
        :param os_arch: **参数解释**： 系统架构 **约束限制**: 不涉及 **取值范围**: - x86_64：X86架构 - arm：ARM架构  **默认取值**: 不涉及 
        :type os_arch: str
        :param host_type: **参数解释**： 服务器类型 **约束限制**: 不涉及 **取值范围**: - host：非容器主机 - container：容器主机  **默认取值**: 不涉及 
        :type host_type: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._plugin_code = None
        self._plugin_version = None
        self._plugin_status = None
        self._host_name = None
        self._host_ids = None
        self._host_status = None
        self._agent_status = None
        self._os_type = None
        self._os_arch = None
        self._host_type = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.plugin_code = plugin_code
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if plugin_status is not None:
            self.plugin_status = plugin_status
        if host_name is not None:
            self.host_name = host_name
        if host_ids is not None:
            self.host_ids = host_ids
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status
        if os_type is not None:
            self.os_type = os_type
        if os_arch is not None:
            self.os_arch = os_arch
        if host_type is not None:
            self.host_type = host_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPluginStatusRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListPluginStatusRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPluginStatusRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListPluginStatusRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListPluginStatusRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListPluginStatusRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPluginStatusRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListPluginStatusRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPluginStatusRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListPluginStatusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPluginStatusRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListPluginStatusRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def plugin_code(self):
        r"""Gets the plugin_code of this ListPluginStatusRequest.

        **参数解释**： 插件编码 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The plugin_code of this ListPluginStatusRequest.
        :rtype: str
        """
        return self._plugin_code

    @plugin_code.setter
    def plugin_code(self, plugin_code):
        r"""Sets the plugin_code of this ListPluginStatusRequest.

        **参数解释**： 插件编码 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param plugin_code: The plugin_code of this ListPluginStatusRequest.
        :type plugin_code: str
        """
        self._plugin_code = plugin_code

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this ListPluginStatusRequest.

        **参数解释**： 插件版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The plugin_version of this ListPluginStatusRequest.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this ListPluginStatusRequest.

        **参数解释**： 插件版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param plugin_version: The plugin_version of this ListPluginStatusRequest.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def plugin_status(self):
        r"""Gets the plugin_status of this ListPluginStatusRequest.

        **参数解释**： 插件状态 **约束限制**: 不涉及 **取值范围**: - not_installed：未安装 - installing：安装中 - install_fail：安装失败 - starting：启动中 - running：运行中 - start_fail：启动失败 - offline：离线 - stopping：停止中 - stopped：已停止 - updating：更新中 - update_fail：更新失败 - uninstalling：卸载中 - uninstall_fail：卸载失败  **默认取值**: 不涉及 

        :return: The plugin_status of this ListPluginStatusRequest.
        :rtype: str
        """
        return self._plugin_status

    @plugin_status.setter
    def plugin_status(self, plugin_status):
        r"""Sets the plugin_status of this ListPluginStatusRequest.

        **参数解释**： 插件状态 **约束限制**: 不涉及 **取值范围**: - not_installed：未安装 - installing：安装中 - install_fail：安装失败 - starting：启动中 - running：运行中 - start_fail：启动失败 - offline：离线 - stopping：停止中 - stopped：已停止 - updating：更新中 - update_fail：更新失败 - uninstalling：卸载中 - uninstall_fail：卸载失败  **默认取值**: 不涉及 

        :param plugin_status: The plugin_status of this ListPluginStatusRequest.
        :type plugin_status: str
        """
        self._plugin_status = plugin_status

    @property
    def host_name(self):
        r"""Gets the host_name of this ListPluginStatusRequest.

        **参数解释**： 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_name of this ListPluginStatusRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListPluginStatusRequest.

        **参数解释**： 服务器名称 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_name: The host_name of this ListPluginStatusRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ids(self):
        r"""Gets the host_ids of this ListPluginStatusRequest.

        **参数解释**： 服务器ID列表 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The host_ids of this ListPluginStatusRequest.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this ListPluginStatusRequest.

        **参数解释**： 服务器ID列表 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param host_ids: The host_ids of this ListPluginStatusRequest.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

    @property
    def host_status(self):
        r"""Gets the host_status of this ListPluginStatusRequest.

        **参数解释**： 服务器状态 **约束限制**: 不涉及 **取值范围**: - ACTIVE：正在运行 - BUILDING：创建中 - ERROR：故障 - SHUTOFF：关机  **默认取值**: 不涉及 

        :return: The host_status of this ListPluginStatusRequest.
        :rtype: list[str]
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ListPluginStatusRequest.

        **参数解释**： 服务器状态 **约束限制**: 不涉及 **取值范围**: - ACTIVE：正在运行 - BUILDING：创建中 - ERROR：故障 - SHUTOFF：关机  **默认取值**: 不涉及 

        :param host_status: The host_status of this ListPluginStatusRequest.
        :type host_status: list[str]
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListPluginStatusRequest.

        **参数解释**： agent状态 **约束限制**: 不涉及 **取值范围**: -not_installed：未安装 -online：在线 -offline：离线 -install_failed：安装失败 -installing：安装中  **默认取值**: 不涉及 

        :return: The agent_status of this ListPluginStatusRequest.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListPluginStatusRequest.

        **参数解释**： agent状态 **约束限制**: 不涉及 **取值范围**: -not_installed：未安装 -online：在线 -offline：离线 -install_failed：安装失败 -installing：安装中  **默认取值**: 不涉及 

        :param agent_status: The agent_status of this ListPluginStatusRequest.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def os_type(self):
        r"""Gets the os_type of this ListPluginStatusRequest.

        **参数解释**： 主机操作系统 **约束限制**: 不涉及 **取值范围**: - linux：Linux操作系统 - Windows：windows操作系统  **默认取值**: 不涉及 

        :return: The os_type of this ListPluginStatusRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListPluginStatusRequest.

        **参数解释**： 主机操作系统 **约束限制**: 不涉及 **取值范围**: - linux：Linux操作系统 - Windows：windows操作系统  **默认取值**: 不涉及 

        :param os_type: The os_type of this ListPluginStatusRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_arch(self):
        r"""Gets the os_arch of this ListPluginStatusRequest.

        **参数解释**： 系统架构 **约束限制**: 不涉及 **取值范围**: - x86_64：X86架构 - arm：ARM架构  **默认取值**: 不涉及 

        :return: The os_arch of this ListPluginStatusRequest.
        :rtype: str
        """
        return self._os_arch

    @os_arch.setter
    def os_arch(self, os_arch):
        r"""Sets the os_arch of this ListPluginStatusRequest.

        **参数解释**： 系统架构 **约束限制**: 不涉及 **取值范围**: - x86_64：X86架构 - arm：ARM架构  **默认取值**: 不涉及 

        :param os_arch: The os_arch of this ListPluginStatusRequest.
        :type os_arch: str
        """
        self._os_arch = os_arch

    @property
    def host_type(self):
        r"""Gets the host_type of this ListPluginStatusRequest.

        **参数解释**： 服务器类型 **约束限制**: 不涉及 **取值范围**: - host：非容器主机 - container：容器主机  **默认取值**: 不涉及 

        :return: The host_type of this ListPluginStatusRequest.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this ListPluginStatusRequest.

        **参数解释**： 服务器类型 **约束限制**: 不涉及 **取值范围**: - host：非容器主机 - container：容器主机  **默认取值**: 不涉及 

        :param host_type: The host_type of this ListPluginStatusRequest.
        :type host_type: str
        """
        self._host_type = host_type

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
        if not isinstance(other, ListPluginStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
