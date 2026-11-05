# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateModelProxyResponse(SdkResponse):

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
        'tags': 'list[CoreGatewayTag]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, gateway_id=None, tags=None, created_at=None, updated_at=None):
        r"""UpdateModelProxyResponse

        The model defined in huaweicloud sdk

        :param gateway_id: **参数解释：** 网关的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 
        :type gateway_id: str
        :param tags: **参数解释：** 资源标签列表。 **取值范围：** 数组长度为0-20。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        :param created_at: **参数解释：** 模型代理创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 
        :type created_at: datetime
        :param updated_at: **参数解释：** 模型代理最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 
        :type updated_at: datetime
        """
        
        super().__init__()

        self._gateway_id = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if gateway_id is not None:
            self.gateway_id = gateway_id
        if tags is not None:
            self.tags = tags
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this UpdateModelProxyResponse.

        **参数解释：** 网关的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :return: The gateway_id of this UpdateModelProxyResponse.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this UpdateModelProxyResponse.

        **参数解释：** 网关的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 

        :param gateway_id: The gateway_id of this UpdateModelProxyResponse.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def tags(self):
        r"""Gets the tags of this UpdateModelProxyResponse.

        **参数解释：** 资源标签列表。 **取值范围：** 数组长度为0-20。 

        :return: The tags of this UpdateModelProxyResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateModelProxyResponse.

        **参数解释：** 资源标签列表。 **取值范围：** 数组长度为0-20。 

        :param tags: The tags of this UpdateModelProxyResponse.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayTag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateModelProxyResponse.

        **参数解释：** 模型代理创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :return: The created_at of this UpdateModelProxyResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateModelProxyResponse.

        **参数解释：** 模型代理创建时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :param created_at: The created_at of this UpdateModelProxyResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateModelProxyResponse.

        **参数解释：** 模型代理最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :return: The updated_at of this UpdateModelProxyResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateModelProxyResponse.

        **参数解释：** 模型代理最后更新时间戳。 **取值范围：** 遵循ISO 8601标准格式，例如：2022-11-09 16:37:24。 

        :param updated_at: The updated_at of this UpdateModelProxyResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    def to_dict(self):
        import warnings
        warnings.warn("UpdateModelProxyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateModelProxyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
