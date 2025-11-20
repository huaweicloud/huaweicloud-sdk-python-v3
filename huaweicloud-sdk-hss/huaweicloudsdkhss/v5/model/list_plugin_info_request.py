# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginInfoRequest:

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
        'code': 'str',
        'plugin_version': 'str',
        'agent_version': 'str',
        'plugin_arch': 'str',
        'plugin_os_type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'code': 'code',
        'plugin_version': 'plugin_version',
        'agent_version': 'agent_version',
        'plugin_arch': 'plugin_arch',
        'plugin_os_type': 'plugin_os_type'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, code=None, plugin_version=None, agent_version=None, plugin_arch=None, plugin_os_type=None):
        r"""ListPluginInfoRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param code: **参数解释**： 插件编码 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type code: str
        :param plugin_version: **参数解释**： 插件版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type plugin_version: str
        :param agent_version: **参数解释**： agent版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_version: str
        :param plugin_arch: **参数解释**： 插件架构 **约束限制**: 不涉及 **取值范围**: - x86_64：X86架构 - arm：ARM架构  **默认取值**: 不涉及 
        :type plugin_arch: str
        :param plugin_os_type: **参数解释**： 插件支持的操作系统类型 **约束限制**: 不涉及 **取值范围**: - Linux：Linux操作系统 - Windows：Windows操作系统  **默认取值**: 不涉及  | 
        :type plugin_os_type: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._code = None
        self._plugin_version = None
        self._agent_version = None
        self._plugin_arch = None
        self._plugin_os_type = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.code = code
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if agent_version is not None:
            self.agent_version = agent_version
        if plugin_arch is not None:
            self.plugin_arch = plugin_arch
        if plugin_os_type is not None:
            self.plugin_os_type = plugin_os_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPluginInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListPluginInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPluginInfoRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListPluginInfoRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListPluginInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListPluginInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPluginInfoRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListPluginInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPluginInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListPluginInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPluginInfoRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListPluginInfoRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def code(self):
        r"""Gets the code of this ListPluginInfoRequest.

        **参数解释**： 插件编码 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The code of this ListPluginInfoRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListPluginInfoRequest.

        **参数解释**： 插件编码 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param code: The code of this ListPluginInfoRequest.
        :type code: str
        """
        self._code = code

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this ListPluginInfoRequest.

        **参数解释**： 插件版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The plugin_version of this ListPluginInfoRequest.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this ListPluginInfoRequest.

        **参数解释**： 插件版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param plugin_version: The plugin_version of this ListPluginInfoRequest.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def agent_version(self):
        r"""Gets the agent_version of this ListPluginInfoRequest.

        **参数解释**： agent版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_version of this ListPluginInfoRequest.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this ListPluginInfoRequest.

        **参数解释**： agent版本 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_version: The agent_version of this ListPluginInfoRequest.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def plugin_arch(self):
        r"""Gets the plugin_arch of this ListPluginInfoRequest.

        **参数解释**： 插件架构 **约束限制**: 不涉及 **取值范围**: - x86_64：X86架构 - arm：ARM架构  **默认取值**: 不涉及 

        :return: The plugin_arch of this ListPluginInfoRequest.
        :rtype: str
        """
        return self._plugin_arch

    @plugin_arch.setter
    def plugin_arch(self, plugin_arch):
        r"""Sets the plugin_arch of this ListPluginInfoRequest.

        **参数解释**： 插件架构 **约束限制**: 不涉及 **取值范围**: - x86_64：X86架构 - arm：ARM架构  **默认取值**: 不涉及 

        :param plugin_arch: The plugin_arch of this ListPluginInfoRequest.
        :type plugin_arch: str
        """
        self._plugin_arch = plugin_arch

    @property
    def plugin_os_type(self):
        r"""Gets the plugin_os_type of this ListPluginInfoRequest.

        **参数解释**： 插件支持的操作系统类型 **约束限制**: 不涉及 **取值范围**: - Linux：Linux操作系统 - Windows：Windows操作系统  **默认取值**: 不涉及  | 

        :return: The plugin_os_type of this ListPluginInfoRequest.
        :rtype: str
        """
        return self._plugin_os_type

    @plugin_os_type.setter
    def plugin_os_type(self, plugin_os_type):
        r"""Sets the plugin_os_type of this ListPluginInfoRequest.

        **参数解释**： 插件支持的操作系统类型 **约束限制**: 不涉及 **取值范围**: - Linux：Linux操作系统 - Windows：Windows操作系统  **默认取值**: 不涉及  | 

        :param plugin_os_type: The plugin_os_type of this ListPluginInfoRequest.
        :type plugin_os_type: str
        """
        self._plugin_os_type = plugin_os_type

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
        if not isinstance(other, ListPluginInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
