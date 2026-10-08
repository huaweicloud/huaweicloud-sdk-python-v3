# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCustomModelProviderResponse(SdkResponse):

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
        'base_url': 'str',
        'credential_configuration': 'CoreModelProviderCredentialConfiguration',
        'network_configuration': 'CoreModelProviderOutboundNetworkConfiguration',
        'description': 'str',
        'tags': 'list[CoreModelProviderTag]',
        'id': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'gateways': 'list[ShowCustomModelProviderGatewayDetails]'
    }

    attribute_map = {
        'name': 'name',
        'base_url': 'base_url',
        'credential_configuration': 'credential_configuration',
        'network_configuration': 'network_configuration',
        'description': 'description',
        'tags': 'tags',
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'gateways': 'gateways'
    }

    def __init__(self, name=None, base_url=None, credential_configuration=None, network_configuration=None, description=None, tags=None, id=None, created_at=None, updated_at=None, gateways=None):
        r"""ShowCustomModelProviderResponse

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 模型提供商名称。 **约束限制：** 账户下模型提供商名称唯一（不区分大小写）。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 **默认取值：** 不涉及。 
        :type name: str
        :param base_url: **参数解释：** 模型提供商的默认API基础地址。 **约束限制：** 不涉及。 **取值范围：** 长度为1-2048个字符。以https://开头的完整URL。 **默认取值：** 不涉及。 
        :type base_url: str
        :param credential_configuration: 
        :type credential_configuration: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderCredentialConfiguration`
        :param network_configuration: 
        :type network_configuration: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderOutboundNetworkConfiguration`
        :param description: **参数解释：** 模型的详细描述。 **取值范围：** 长度为 0-1000 个字符。 
        :type description: str
        :param tags: **参数解释：** 资源标签列表。 **约束限制：** 不涉及。 **取值范围：** 数组长度为 0-20。 **默认取值：** 不涉及。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreModelProviderTag`]
        :param id: **参数解释：** 模型提供商ID。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 
        :type id: str
        :param created_at: **参数解释：** 模型提供商创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 模型提供商最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 
        :type updated_at: datetime
        :param gateways: **参数解释：** 模型提供商关联的网关列表。 **取值范围：** 数组长度为0-100个。 
        :type gateways: list[:class:`huaweicloudsdkagentarts.v1.ShowCustomModelProviderGatewayDetails`]
        """
        
        super().__init__()

        self._name = None
        self._base_url = None
        self._credential_configuration = None
        self._network_configuration = None
        self._description = None
        self._tags = None
        self._id = None
        self._created_at = None
        self._updated_at = None
        self._gateways = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if base_url is not None:
            self.base_url = base_url
        if credential_configuration is not None:
            self.credential_configuration = credential_configuration
        if network_configuration is not None:
            self.network_configuration = network_configuration
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if gateways is not None:
            self.gateways = gateways

    @property
    def name(self):
        r"""Gets the name of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商名称。 **约束限制：** 账户下模型提供商名称唯一（不区分大小写）。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 **默认取值：** 不涉及。 

        :return: The name of this ShowCustomModelProviderResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商名称。 **约束限制：** 账户下模型提供商名称唯一（不区分大小写）。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 **默认取值：** 不涉及。 

        :param name: The name of this ShowCustomModelProviderResponse.
        :type name: str
        """
        self._name = name

    @property
    def base_url(self):
        r"""Gets the base_url of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商的默认API基础地址。 **约束限制：** 不涉及。 **取值范围：** 长度为1-2048个字符。以https://开头的完整URL。 **默认取值：** 不涉及。 

        :return: The base_url of this ShowCustomModelProviderResponse.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        r"""Sets the base_url of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商的默认API基础地址。 **约束限制：** 不涉及。 **取值范围：** 长度为1-2048个字符。以https://开头的完整URL。 **默认取值：** 不涉及。 

        :param base_url: The base_url of this ShowCustomModelProviderResponse.
        :type base_url: str
        """
        self._base_url = base_url

    @property
    def credential_configuration(self):
        r"""Gets the credential_configuration of this ShowCustomModelProviderResponse.

        :return: The credential_configuration of this ShowCustomModelProviderResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderCredentialConfiguration`
        """
        return self._credential_configuration

    @credential_configuration.setter
    def credential_configuration(self, credential_configuration):
        r"""Sets the credential_configuration of this ShowCustomModelProviderResponse.

        :param credential_configuration: The credential_configuration of this ShowCustomModelProviderResponse.
        :type credential_configuration: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderCredentialConfiguration`
        """
        self._credential_configuration = credential_configuration

    @property
    def network_configuration(self):
        r"""Gets the network_configuration of this ShowCustomModelProviderResponse.

        :return: The network_configuration of this ShowCustomModelProviderResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderOutboundNetworkConfiguration`
        """
        return self._network_configuration

    @network_configuration.setter
    def network_configuration(self, network_configuration):
        r"""Sets the network_configuration of this ShowCustomModelProviderResponse.

        :param network_configuration: The network_configuration of this ShowCustomModelProviderResponse.
        :type network_configuration: :class:`huaweicloudsdkagentarts.v1.CoreModelProviderOutboundNetworkConfiguration`
        """
        self._network_configuration = network_configuration

    @property
    def description(self):
        r"""Gets the description of this ShowCustomModelProviderResponse.

        **参数解释：** 模型的详细描述。 **取值范围：** 长度为 0-1000 个字符。 

        :return: The description of this ShowCustomModelProviderResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowCustomModelProviderResponse.

        **参数解释：** 模型的详细描述。 **取值范围：** 长度为 0-1000 个字符。 

        :param description: The description of this ShowCustomModelProviderResponse.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this ShowCustomModelProviderResponse.

        **参数解释：** 资源标签列表。 **约束限制：** 不涉及。 **取值范围：** 数组长度为 0-20。 **默认取值：** 不涉及。 

        :return: The tags of this ShowCustomModelProviderResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreModelProviderTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowCustomModelProviderResponse.

        **参数解释：** 资源标签列表。 **约束限制：** 不涉及。 **取值范围：** 数组长度为 0-20。 **默认取值：** 不涉及。 

        :param tags: The tags of this ShowCustomModelProviderResponse.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreModelProviderTag`]
        """
        self._tags = tags

    @property
    def id(self):
        r"""Gets the id of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商ID。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :return: The id of this ShowCustomModelProviderResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商ID。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :param id: The id of this ShowCustomModelProviderResponse.
        :type id: str
        """
        self._id = id

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :return: The created_at of this ShowCustomModelProviderResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :param created_at: The created_at of this ShowCustomModelProviderResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :return: The updated_at of this ShowCustomModelProviderResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :param updated_at: The updated_at of this ShowCustomModelProviderResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def gateways(self):
        r"""Gets the gateways of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商关联的网关列表。 **取值范围：** 数组长度为0-100个。 

        :return: The gateways of this ShowCustomModelProviderResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ShowCustomModelProviderGatewayDetails`]
        """
        return self._gateways

    @gateways.setter
    def gateways(self, gateways):
        r"""Sets the gateways of this ShowCustomModelProviderResponse.

        **参数解释：** 模型提供商关联的网关列表。 **取值范围：** 数组长度为0-100个。 

        :param gateways: The gateways of this ShowCustomModelProviderResponse.
        :type gateways: list[:class:`huaweicloudsdkagentarts.v1.ShowCustomModelProviderGatewayDetails`]
        """
        self._gateways = gateways

    def to_dict(self):
        import warnings
        warnings.warn("ShowCustomModelProviderResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowCustomModelProviderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
