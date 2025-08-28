# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRoleReq:

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
        'description': 'str',
        'role_business_list': 'list[RoleBusinessReq]',
        'llm_source': 'LlmSourceEnum',
        'llm_config_id': 'str',
        'plugin_config_list': 'list[RolePluginConfigInfo]',
        'mcp_server_id_list': 'list[str]',
        'instruction_library_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'role_business_list': 'role_business_list',
        'llm_source': 'llm_source',
        'llm_config_id': 'llm_config_id',
        'plugin_config_list': 'plugin_config_list',
        'mcp_server_id_list': 'mcp_server_id_list',
        'instruction_library_id': 'instruction_library_id'
    }

    def __init__(self, name=None, description=None, role_business_list=None, llm_source=None, llm_config_id=None, plugin_config_list=None, mcp_server_id_list=None, instruction_library_id=None):
        r"""UpdateRoleReq

        The model defined in huaweicloud sdk

        :param name: 角色名称。
        :type name: str
        :param description: 角色描述。
        :type description: str
        :param role_business_list: 角色业务配置列表
        :type role_business_list: list[:class:`huaweicloudsdkmetastudio.v1.RoleBusinessReq`]
        :param llm_source: 
        :type llm_source: :class:`huaweicloudsdkmetastudio.v1.LlmSourceEnum`
        :param llm_config_id: 大语言模型配置ID。
        :type llm_config_id: str
        :param plugin_config_list: 插件配置列表
        :type plugin_config_list: list[:class:`huaweicloudsdkmetastudio.v1.RolePluginConfigInfo`]
        :param mcp_server_id_list: MCP服务端对接配置ID列表
        :type mcp_server_id_list: list[str]
        :param instruction_library_id: 指令集ID。
        :type instruction_library_id: str
        """
        
        

        self._name = None
        self._description = None
        self._role_business_list = None
        self._llm_source = None
        self._llm_config_id = None
        self._plugin_config_list = None
        self._mcp_server_id_list = None
        self._instruction_library_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if role_business_list is not None:
            self.role_business_list = role_business_list
        if llm_source is not None:
            self.llm_source = llm_source
        if llm_config_id is not None:
            self.llm_config_id = llm_config_id
        if plugin_config_list is not None:
            self.plugin_config_list = plugin_config_list
        if mcp_server_id_list is not None:
            self.mcp_server_id_list = mcp_server_id_list
        if instruction_library_id is not None:
            self.instruction_library_id = instruction_library_id

    @property
    def name(self):
        r"""Gets the name of this UpdateRoleReq.

        角色名称。

        :return: The name of this UpdateRoleReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateRoleReq.

        角色名称。

        :param name: The name of this UpdateRoleReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateRoleReq.

        角色描述。

        :return: The description of this UpdateRoleReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateRoleReq.

        角色描述。

        :param description: The description of this UpdateRoleReq.
        :type description: str
        """
        self._description = description

    @property
    def role_business_list(self):
        r"""Gets the role_business_list of this UpdateRoleReq.

        角色业务配置列表

        :return: The role_business_list of this UpdateRoleReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.RoleBusinessReq`]
        """
        return self._role_business_list

    @role_business_list.setter
    def role_business_list(self, role_business_list):
        r"""Sets the role_business_list of this UpdateRoleReq.

        角色业务配置列表

        :param role_business_list: The role_business_list of this UpdateRoleReq.
        :type role_business_list: list[:class:`huaweicloudsdkmetastudio.v1.RoleBusinessReq`]
        """
        self._role_business_list = role_business_list

    @property
    def llm_source(self):
        r"""Gets the llm_source of this UpdateRoleReq.

        :return: The llm_source of this UpdateRoleReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LlmSourceEnum`
        """
        return self._llm_source

    @llm_source.setter
    def llm_source(self, llm_source):
        r"""Sets the llm_source of this UpdateRoleReq.

        :param llm_source: The llm_source of this UpdateRoleReq.
        :type llm_source: :class:`huaweicloudsdkmetastudio.v1.LlmSourceEnum`
        """
        self._llm_source = llm_source

    @property
    def llm_config_id(self):
        r"""Gets the llm_config_id of this UpdateRoleReq.

        大语言模型配置ID。

        :return: The llm_config_id of this UpdateRoleReq.
        :rtype: str
        """
        return self._llm_config_id

    @llm_config_id.setter
    def llm_config_id(self, llm_config_id):
        r"""Sets the llm_config_id of this UpdateRoleReq.

        大语言模型配置ID。

        :param llm_config_id: The llm_config_id of this UpdateRoleReq.
        :type llm_config_id: str
        """
        self._llm_config_id = llm_config_id

    @property
    def plugin_config_list(self):
        r"""Gets the plugin_config_list of this UpdateRoleReq.

        插件配置列表

        :return: The plugin_config_list of this UpdateRoleReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.RolePluginConfigInfo`]
        """
        return self._plugin_config_list

    @plugin_config_list.setter
    def plugin_config_list(self, plugin_config_list):
        r"""Sets the plugin_config_list of this UpdateRoleReq.

        插件配置列表

        :param plugin_config_list: The plugin_config_list of this UpdateRoleReq.
        :type plugin_config_list: list[:class:`huaweicloudsdkmetastudio.v1.RolePluginConfigInfo`]
        """
        self._plugin_config_list = plugin_config_list

    @property
    def mcp_server_id_list(self):
        r"""Gets the mcp_server_id_list of this UpdateRoleReq.

        MCP服务端对接配置ID列表

        :return: The mcp_server_id_list of this UpdateRoleReq.
        :rtype: list[str]
        """
        return self._mcp_server_id_list

    @mcp_server_id_list.setter
    def mcp_server_id_list(self, mcp_server_id_list):
        r"""Sets the mcp_server_id_list of this UpdateRoleReq.

        MCP服务端对接配置ID列表

        :param mcp_server_id_list: The mcp_server_id_list of this UpdateRoleReq.
        :type mcp_server_id_list: list[str]
        """
        self._mcp_server_id_list = mcp_server_id_list

    @property
    def instruction_library_id(self):
        r"""Gets the instruction_library_id of this UpdateRoleReq.

        指令集ID。

        :return: The instruction_library_id of this UpdateRoleReq.
        :rtype: str
        """
        return self._instruction_library_id

    @instruction_library_id.setter
    def instruction_library_id(self, instruction_library_id):
        r"""Sets the instruction_library_id of this UpdateRoleReq.

        指令集ID。

        :param instruction_library_id: The instruction_library_id of this UpdateRoleReq.
        :type instruction_library_id: str
        """
        self._instruction_library_id = instruction_library_id

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
        if not isinstance(other, UpdateRoleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
