# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayTarget:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_id': 'str',
        'gateway_id': 'str',
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'inactive_reason': 'str',
        'target_type': 'str',
        'target_configuration': 'CoreGatewayTargetConfiguration',
        'credential_provider_configuration': 'CoreGatewayCredentialProviderConfiguration',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'target_id': 'target_id',
        'gateway_id': 'gateway_id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'inactive_reason': 'inactive_reason',
        'target_type': 'target_type',
        'target_configuration': 'target_configuration',
        'credential_provider_configuration': 'credential_provider_configuration',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, target_id=None, gateway_id=None, name=None, description=None, status=None, inactive_reason=None, target_type=None, target_configuration=None, credential_provider_configuration=None, created_at=None, updated_at=None):
        r"""CoreGatewayTarget

        The model defined in huaweicloud sdk

        :param target_id: **参数解释：** 目标服务的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 
        :type target_id: str
        :param gateway_id: **参数解释：** 所属网关的标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 
        :type gateway_id: str
        :param name: **参数解释：** 目标服务名称。 **取值范围：** 长度为 1-50 个字符，匹配以字母数字开头和结尾、中间可含0到48个字母数字或短横线的字符串，符合正则条件^[a-zA-Z0-9]\\([a-zA-Z0-9-]{0,48}[a-zA-Z0-9])?$。 
        :type name: str
        :param description: **参数解释：** 目标服务描述。 **取值范围：** 长度为 1-200 个字符。 
        :type description: str
        :param status: **参数解释：** 目标服务状态。 **取值范围：** - &#x60;creating&#x60;: 创建中 - &#x60;updating&#x60;: 更新中 - &#x60;ready&#x60;: 就绪可用 - &#x60;failed&#x60;: 失败 - &#x60;deleting&#x60;: 删除中 - &#x60;synchronize_pending&#x60;: 等待同步中 - &#x60;synchronizing&#x60;: 同步中 - &#x60;active&#x60;: 在线 - &#x60;inactive&#x60;: 离线 
        :type status: str
        :param inactive_reason: **参数解释：** 目标服务离线状态原因。 **取值范围：** 长度为 1-100 个字符。 
        :type inactive_reason: str
        :param target_type: **参数解释：** 目标服务类型。 **取值范围：** - &#x60;mcp_server&#x60;: MCP 服务器 - &#x60;openapi&#x60;: 基于 OpenAPI 规范的 REST API 
        :type target_type: str
        :param target_configuration: 
        :type target_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetConfiguration`
        :param credential_provider_configuration: 
        :type credential_provider_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCredentialProviderConfiguration`
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 不涉及。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 最后更新时间。 **取值范围：** 不涉及。 
        :type updated_at: datetime
        """
        
        

        self._target_id = None
        self._gateway_id = None
        self._name = None
        self._description = None
        self._status = None
        self._inactive_reason = None
        self._target_type = None
        self._target_configuration = None
        self._credential_provider_configuration = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.target_id = target_id
        self.gateway_id = gateway_id
        self.name = name
        if description is not None:
            self.description = description
        self.status = status
        if inactive_reason is not None:
            self.inactive_reason = inactive_reason
        self.target_type = target_type
        self.target_configuration = target_configuration
        if credential_provider_configuration is not None:
            self.credential_provider_configuration = credential_provider_configuration
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def target_id(self):
        r"""Gets the target_id of this CoreGatewayTarget.

        **参数解释：** 目标服务的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :return: The target_id of this CoreGatewayTarget.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this CoreGatewayTarget.

        **参数解释：** 目标服务的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :param target_id: The target_id of this CoreGatewayTarget.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this CoreGatewayTarget.

        **参数解释：** 所属网关的标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :return: The gateway_id of this CoreGatewayTarget.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this CoreGatewayTarget.

        **参数解释：** 所属网关的标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :param gateway_id: The gateway_id of this CoreGatewayTarget.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def name(self):
        r"""Gets the name of this CoreGatewayTarget.

        **参数解释：** 目标服务名称。 **取值范围：** 长度为 1-50 个字符，匹配以字母数字开头和结尾、中间可含0到48个字母数字或短横线的字符串，符合正则条件^[a-zA-Z0-9]\\([a-zA-Z0-9-]{0,48}[a-zA-Z0-9])?$。 

        :return: The name of this CoreGatewayTarget.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CoreGatewayTarget.

        **参数解释：** 目标服务名称。 **取值范围：** 长度为 1-50 个字符，匹配以字母数字开头和结尾、中间可含0到48个字母数字或短横线的字符串，符合正则条件^[a-zA-Z0-9]\\([a-zA-Z0-9-]{0,48}[a-zA-Z0-9])?$。 

        :param name: The name of this CoreGatewayTarget.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CoreGatewayTarget.

        **参数解释：** 目标服务描述。 **取值范围：** 长度为 1-200 个字符。 

        :return: The description of this CoreGatewayTarget.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CoreGatewayTarget.

        **参数解释：** 目标服务描述。 **取值范围：** 长度为 1-200 个字符。 

        :param description: The description of this CoreGatewayTarget.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this CoreGatewayTarget.

        **参数解释：** 目标服务状态。 **取值范围：** - `creating`: 创建中 - `updating`: 更新中 - `ready`: 就绪可用 - `failed`: 失败 - `deleting`: 删除中 - `synchronize_pending`: 等待同步中 - `synchronizing`: 同步中 - `active`: 在线 - `inactive`: 离线 

        :return: The status of this CoreGatewayTarget.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CoreGatewayTarget.

        **参数解释：** 目标服务状态。 **取值范围：** - `creating`: 创建中 - `updating`: 更新中 - `ready`: 就绪可用 - `failed`: 失败 - `deleting`: 删除中 - `synchronize_pending`: 等待同步中 - `synchronizing`: 同步中 - `active`: 在线 - `inactive`: 离线 

        :param status: The status of this CoreGatewayTarget.
        :type status: str
        """
        self._status = status

    @property
    def inactive_reason(self):
        r"""Gets the inactive_reason of this CoreGatewayTarget.

        **参数解释：** 目标服务离线状态原因。 **取值范围：** 长度为 1-100 个字符。 

        :return: The inactive_reason of this CoreGatewayTarget.
        :rtype: str
        """
        return self._inactive_reason

    @inactive_reason.setter
    def inactive_reason(self, inactive_reason):
        r"""Sets the inactive_reason of this CoreGatewayTarget.

        **参数解释：** 目标服务离线状态原因。 **取值范围：** 长度为 1-100 个字符。 

        :param inactive_reason: The inactive_reason of this CoreGatewayTarget.
        :type inactive_reason: str
        """
        self._inactive_reason = inactive_reason

    @property
    def target_type(self):
        r"""Gets the target_type of this CoreGatewayTarget.

        **参数解释：** 目标服务类型。 **取值范围：** - `mcp_server`: MCP 服务器 - `openapi`: 基于 OpenAPI 规范的 REST API 

        :return: The target_type of this CoreGatewayTarget.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this CoreGatewayTarget.

        **参数解释：** 目标服务类型。 **取值范围：** - `mcp_server`: MCP 服务器 - `openapi`: 基于 OpenAPI 规范的 REST API 

        :param target_type: The target_type of this CoreGatewayTarget.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_configuration(self):
        r"""Gets the target_configuration of this CoreGatewayTarget.

        :return: The target_configuration of this CoreGatewayTarget.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetConfiguration`
        """
        return self._target_configuration

    @target_configuration.setter
    def target_configuration(self, target_configuration):
        r"""Sets the target_configuration of this CoreGatewayTarget.

        :param target_configuration: The target_configuration of this CoreGatewayTarget.
        :type target_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetConfiguration`
        """
        self._target_configuration = target_configuration

    @property
    def credential_provider_configuration(self):
        r"""Gets the credential_provider_configuration of this CoreGatewayTarget.

        :return: The credential_provider_configuration of this CoreGatewayTarget.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCredentialProviderConfiguration`
        """
        return self._credential_provider_configuration

    @credential_provider_configuration.setter
    def credential_provider_configuration(self, credential_provider_configuration):
        r"""Sets the credential_provider_configuration of this CoreGatewayTarget.

        :param credential_provider_configuration: The credential_provider_configuration of this CoreGatewayTarget.
        :type credential_provider_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCredentialProviderConfiguration`
        """
        self._credential_provider_configuration = credential_provider_configuration

    @property
    def created_at(self):
        r"""Gets the created_at of this CoreGatewayTarget.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。 

        :return: The created_at of this CoreGatewayTarget.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CoreGatewayTarget.

        **参数解释：** 创建时间。 **取值范围：** 不涉及。 

        :param created_at: The created_at of this CoreGatewayTarget.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CoreGatewayTarget.

        **参数解释：** 最后更新时间。 **取值范围：** 不涉及。 

        :return: The updated_at of this CoreGatewayTarget.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CoreGatewayTarget.

        **参数解释：** 最后更新时间。 **取值范围：** 不涉及。 

        :param updated_at: The updated_at of this CoreGatewayTarget.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, CoreGatewayTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
