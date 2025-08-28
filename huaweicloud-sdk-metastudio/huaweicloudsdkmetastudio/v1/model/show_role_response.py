# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRoleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_id': 'str',
        'name': 'str',
        'description': 'str',
        'role_business_list': 'list[RoleBusinessInfo]',
        'llm_source': 'LlmSourceEnum',
        'llm_config_id': 'str',
        'plugin_config_list': 'list[RolePluginConfigInfo]',
        'mcp_server_info_list': 'list[McpServerBaseInfo]',
        'instruction_library_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'role_id': 'role_id',
        'name': 'name',
        'description': 'description',
        'role_business_list': 'role_business_list',
        'llm_source': 'llm_source',
        'llm_config_id': 'llm_config_id',
        'plugin_config_list': 'plugin_config_list',
        'mcp_server_info_list': 'mcp_server_info_list',
        'instruction_library_id': 'instruction_library_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, role_id=None, name=None, description=None, role_business_list=None, llm_source=None, llm_config_id=None, plugin_config_list=None, mcp_server_info_list=None, instruction_library_id=None, create_time=None, update_time=None, x_request_id=None):
        r"""ShowRoleResponse

        The model defined in huaweicloud sdk

        :param role_id: 角色ID。
        :type role_id: str
        :param name: 角色名称。
        :type name: str
        :param description: 角色描述。
        :type description: str
        :param role_business_list: 角色业务配置列表。
        :type role_business_list: list[:class:`huaweicloudsdkmetastudio.v1.RoleBusinessInfo`]
        :param llm_source: 
        :type llm_source: :class:`huaweicloudsdkmetastudio.v1.LlmSourceEnum`
        :param llm_config_id: 大语言模型配置ID。
        :type llm_config_id: str
        :param plugin_config_list: 插件配置列表
        :type plugin_config_list: list[:class:`huaweicloudsdkmetastudio.v1.RolePluginConfigInfo`]
        :param mcp_server_info_list: MCP服务端对接配置信息列表
        :type mcp_server_info_list: list[:class:`huaweicloudsdkmetastudio.v1.McpServerBaseInfo`]
        :param instruction_library_id: 指令集ID。
        :type instruction_library_id: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowRoleResponse, self).__init__()

        self._role_id = None
        self._name = None
        self._description = None
        self._role_business_list = None
        self._llm_source = None
        self._llm_config_id = None
        self._plugin_config_list = None
        self._mcp_server_info_list = None
        self._instruction_library_id = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
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
        if mcp_server_info_list is not None:
            self.mcp_server_info_list = mcp_server_info_list
        if instruction_library_id is not None:
            self.instruction_library_id = instruction_library_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def role_id(self):
        r"""Gets the role_id of this ShowRoleResponse.

        角色ID。

        :return: The role_id of this ShowRoleResponse.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this ShowRoleResponse.

        角色ID。

        :param role_id: The role_id of this ShowRoleResponse.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def name(self):
        r"""Gets the name of this ShowRoleResponse.

        角色名称。

        :return: The name of this ShowRoleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowRoleResponse.

        角色名称。

        :param name: The name of this ShowRoleResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowRoleResponse.

        角色描述。

        :return: The description of this ShowRoleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowRoleResponse.

        角色描述。

        :param description: The description of this ShowRoleResponse.
        :type description: str
        """
        self._description = description

    @property
    def role_business_list(self):
        r"""Gets the role_business_list of this ShowRoleResponse.

        角色业务配置列表。

        :return: The role_business_list of this ShowRoleResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.RoleBusinessInfo`]
        """
        return self._role_business_list

    @role_business_list.setter
    def role_business_list(self, role_business_list):
        r"""Sets the role_business_list of this ShowRoleResponse.

        角色业务配置列表。

        :param role_business_list: The role_business_list of this ShowRoleResponse.
        :type role_business_list: list[:class:`huaweicloudsdkmetastudio.v1.RoleBusinessInfo`]
        """
        self._role_business_list = role_business_list

    @property
    def llm_source(self):
        r"""Gets the llm_source of this ShowRoleResponse.

        :return: The llm_source of this ShowRoleResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LlmSourceEnum`
        """
        return self._llm_source

    @llm_source.setter
    def llm_source(self, llm_source):
        r"""Sets the llm_source of this ShowRoleResponse.

        :param llm_source: The llm_source of this ShowRoleResponse.
        :type llm_source: :class:`huaweicloudsdkmetastudio.v1.LlmSourceEnum`
        """
        self._llm_source = llm_source

    @property
    def llm_config_id(self):
        r"""Gets the llm_config_id of this ShowRoleResponse.

        大语言模型配置ID。

        :return: The llm_config_id of this ShowRoleResponse.
        :rtype: str
        """
        return self._llm_config_id

    @llm_config_id.setter
    def llm_config_id(self, llm_config_id):
        r"""Sets the llm_config_id of this ShowRoleResponse.

        大语言模型配置ID。

        :param llm_config_id: The llm_config_id of this ShowRoleResponse.
        :type llm_config_id: str
        """
        self._llm_config_id = llm_config_id

    @property
    def plugin_config_list(self):
        r"""Gets the plugin_config_list of this ShowRoleResponse.

        插件配置列表

        :return: The plugin_config_list of this ShowRoleResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.RolePluginConfigInfo`]
        """
        return self._plugin_config_list

    @plugin_config_list.setter
    def plugin_config_list(self, plugin_config_list):
        r"""Sets the plugin_config_list of this ShowRoleResponse.

        插件配置列表

        :param plugin_config_list: The plugin_config_list of this ShowRoleResponse.
        :type plugin_config_list: list[:class:`huaweicloudsdkmetastudio.v1.RolePluginConfigInfo`]
        """
        self._plugin_config_list = plugin_config_list

    @property
    def mcp_server_info_list(self):
        r"""Gets the mcp_server_info_list of this ShowRoleResponse.

        MCP服务端对接配置信息列表

        :return: The mcp_server_info_list of this ShowRoleResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.McpServerBaseInfo`]
        """
        return self._mcp_server_info_list

    @mcp_server_info_list.setter
    def mcp_server_info_list(self, mcp_server_info_list):
        r"""Sets the mcp_server_info_list of this ShowRoleResponse.

        MCP服务端对接配置信息列表

        :param mcp_server_info_list: The mcp_server_info_list of this ShowRoleResponse.
        :type mcp_server_info_list: list[:class:`huaweicloudsdkmetastudio.v1.McpServerBaseInfo`]
        """
        self._mcp_server_info_list = mcp_server_info_list

    @property
    def instruction_library_id(self):
        r"""Gets the instruction_library_id of this ShowRoleResponse.

        指令集ID。

        :return: The instruction_library_id of this ShowRoleResponse.
        :rtype: str
        """
        return self._instruction_library_id

    @instruction_library_id.setter
    def instruction_library_id(self, instruction_library_id):
        r"""Sets the instruction_library_id of this ShowRoleResponse.

        指令集ID。

        :param instruction_library_id: The instruction_library_id of this ShowRoleResponse.
        :type instruction_library_id: str
        """
        self._instruction_library_id = instruction_library_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowRoleResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowRoleResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowRoleResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowRoleResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowRoleResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowRoleResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowRoleResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowRoleResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowRoleResponse.

        :return: The x_request_id of this ShowRoleResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowRoleResponse.

        :param x_request_id: The x_request_id of this ShowRoleResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowRoleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
