# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateModelProxyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway_id': 'str',
        'name': 'str',
        'description': 'str',
        'endpoint_url': 'str',
        'inbound_authorizer_type': 'str',
        'tags': 'list[CoreGatewayTag]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'custom_model_provider_id': 'str'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'name': 'name',
        'description': 'description',
        'endpoint_url': 'endpoint_url',
        'inbound_authorizer_type': 'inbound_authorizer_type',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'custom_model_provider_id': 'custom_model_provider_id'
    }

    def __init__(self, gateway_id=None, name=None, description=None, endpoint_url=None, inbound_authorizer_type=None, tags=None, created_at=None, updated_at=None, custom_model_provider_id=None):
        r"""CreateModelProxyResponse

        The model defined in huaweicloud sdk

        :param gateway_id: **参数解释：** 模型代理的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **约束限制：** 不涉及。 **默认取值：** 不涉及。 
        :type gateway_id: str
        :param name: **参数解释：** 网关名称。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 
        :type name: str
        :param description: **参数解释：** 网关的详细描述。 **取值范围：** 长度为 0-1000 个字符。 
        :type description: str
        :param endpoint_url: **参数解释：** 访问模型代理的 URL 端点。 **取值范围：** 长度为 1-512 个字符。 - 示例：https://gateway-fo2ao8pg-beta1-gw-gu2geoldgz.cn-southwest-301.huaweicloud-agentarts.com 
        :type endpoint_url: str
        :param inbound_authorizer_type: **参数解释：** 入站认证类型。 **取值范围：** - &#x60;iam&#x60;: 使用 IAM 认证 - &#x60;api_key&#x60;: 使用 API 密钥认证 
        :type inbound_authorizer_type: str
        :param tags: **参数解释：** 资源标签列表。 **取值范围：** 数组长度为0-20。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        :param created_at: **参数解释：** 模型代理创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 模型代理最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 
        :type updated_at: datetime
        :param custom_model_provider_id: **参数解释：** 模型提供商ID。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type custom_model_provider_id: str
        """
        
        super().__init__()

        self._gateway_id = None
        self._name = None
        self._description = None
        self._endpoint_url = None
        self._inbound_authorizer_type = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self._custom_model_provider_id = None
        self.discriminator = None

        if gateway_id is not None:
            self.gateway_id = gateway_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if endpoint_url is not None:
            self.endpoint_url = endpoint_url
        if inbound_authorizer_type is not None:
            self.inbound_authorizer_type = inbound_authorizer_type
        if tags is not None:
            self.tags = tags
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if custom_model_provider_id is not None:
            self.custom_model_provider_id = custom_model_provider_id

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this CreateModelProxyResponse.

        **参数解释：** 模型代理的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **约束限制：** 不涉及。 **默认取值：** 不涉及。 

        :return: The gateway_id of this CreateModelProxyResponse.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this CreateModelProxyResponse.

        **参数解释：** 模型代理的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **约束限制：** 不涉及。 **默认取值：** 不涉及。 

        :param gateway_id: The gateway_id of this CreateModelProxyResponse.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def name(self):
        r"""Gets the name of this CreateModelProxyResponse.

        **参数解释：** 网关名称。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 

        :return: The name of this CreateModelProxyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateModelProxyResponse.

        **参数解释：** 网关名称。 **取值范围：** 长度为 2-40 个字符，匹配以小写字母开头、以小写字母或数字结尾、中间可包含0到38个小写字母、数字或连字符的字符串，符合正则条件^[a-z][a-z0-9-]{0,38}[a-z0-9]$。 

        :param name: The name of this CreateModelProxyResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateModelProxyResponse.

        **参数解释：** 网关的详细描述。 **取值范围：** 长度为 0-1000 个字符。 

        :return: The description of this CreateModelProxyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateModelProxyResponse.

        **参数解释：** 网关的详细描述。 **取值范围：** 长度为 0-1000 个字符。 

        :param description: The description of this CreateModelProxyResponse.
        :type description: str
        """
        self._description = description

    @property
    def endpoint_url(self):
        r"""Gets the endpoint_url of this CreateModelProxyResponse.

        **参数解释：** 访问模型代理的 URL 端点。 **取值范围：** 长度为 1-512 个字符。 - 示例：https://gateway-fo2ao8pg-beta1-gw-gu2geoldgz.cn-southwest-301.huaweicloud-agentarts.com 

        :return: The endpoint_url of this CreateModelProxyResponse.
        :rtype: str
        """
        return self._endpoint_url

    @endpoint_url.setter
    def endpoint_url(self, endpoint_url):
        r"""Sets the endpoint_url of this CreateModelProxyResponse.

        **参数解释：** 访问模型代理的 URL 端点。 **取值范围：** 长度为 1-512 个字符。 - 示例：https://gateway-fo2ao8pg-beta1-gw-gu2geoldgz.cn-southwest-301.huaweicloud-agentarts.com 

        :param endpoint_url: The endpoint_url of this CreateModelProxyResponse.
        :type endpoint_url: str
        """
        self._endpoint_url = endpoint_url

    @property
    def inbound_authorizer_type(self):
        r"""Gets the inbound_authorizer_type of this CreateModelProxyResponse.

        **参数解释：** 入站认证类型。 **取值范围：** - `iam`: 使用 IAM 认证 - `api_key`: 使用 API 密钥认证 

        :return: The inbound_authorizer_type of this CreateModelProxyResponse.
        :rtype: str
        """
        return self._inbound_authorizer_type

    @inbound_authorizer_type.setter
    def inbound_authorizer_type(self, inbound_authorizer_type):
        r"""Sets the inbound_authorizer_type of this CreateModelProxyResponse.

        **参数解释：** 入站认证类型。 **取值范围：** - `iam`: 使用 IAM 认证 - `api_key`: 使用 API 密钥认证 

        :param inbound_authorizer_type: The inbound_authorizer_type of this CreateModelProxyResponse.
        :type inbound_authorizer_type: str
        """
        self._inbound_authorizer_type = inbound_authorizer_type

    @property
    def tags(self):
        r"""Gets the tags of this CreateModelProxyResponse.

        **参数解释：** 资源标签列表。 **取值范围：** 数组长度为0-20。 

        :return: The tags of this CreateModelProxyResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateModelProxyResponse.

        **参数解释：** 资源标签列表。 **取值范围：** 数组长度为0-20。 

        :param tags: The tags of this CreateModelProxyResponse.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateModelProxyResponse.

        **参数解释：** 模型代理创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :return: The created_at of this CreateModelProxyResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateModelProxyResponse.

        **参数解释：** 模型代理创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :param created_at: The created_at of this CreateModelProxyResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateModelProxyResponse.

        **参数解释：** 模型代理最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :return: The updated_at of this CreateModelProxyResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateModelProxyResponse.

        **参数解释：** 模型代理最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :param updated_at: The updated_at of this CreateModelProxyResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def custom_model_provider_id(self):
        r"""Gets the custom_model_provider_id of this CreateModelProxyResponse.

        **参数解释：** 模型提供商ID。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The custom_model_provider_id of this CreateModelProxyResponse.
        :rtype: str
        """
        return self._custom_model_provider_id

    @custom_model_provider_id.setter
    def custom_model_provider_id(self, custom_model_provider_id):
        r"""Sets the custom_model_provider_id of this CreateModelProxyResponse.

        **参数解释：** 模型提供商ID。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param custom_model_provider_id: The custom_model_provider_id of this CreateModelProxyResponse.
        :type custom_model_provider_id: str
        """
        self._custom_model_provider_id = custom_model_provider_id

    def to_dict(self):
        import warnings
        warnings.warn("CreateModelProxyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateModelProxyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
