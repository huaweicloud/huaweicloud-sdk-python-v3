# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreGatewayTargetsRequest:

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
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, gateway_id=None, limit=None, offset=None):
        r"""ListCoreGatewayTargetsRequest

        The model defined in huaweicloud sdk

        :param gateway_id: **参数解释：** 网关的唯一标识符。 网关ID获取方式： 1. 进入AgentArts平台，在左侧导航栏选择“开发中心 &gt; 组件库 ”，选择“网关”页签。 2. 在网关列表中“网关名称/ID”处复制网关ID即可。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type gateway_id: str
        :param limit: **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100。 **默认取值：** 50 
        :type limit: int
        :param offset: **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100000。 **默认取值：** 0 
        :type offset: int
        """
        
        

        self._gateway_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.gateway_id = gateway_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this ListCoreGatewayTargetsRequest.

        **参数解释：** 网关的唯一标识符。 网关ID获取方式： 1. 进入AgentArts平台，在左侧导航栏选择“开发中心 > 组件库 ”，选择“网关”页签。 2. 在网关列表中“网关名称/ID”处复制网关ID即可。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The gateway_id of this ListCoreGatewayTargetsRequest.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this ListCoreGatewayTargetsRequest.

        **参数解释：** 网关的唯一标识符。 网关ID获取方式： 1. 进入AgentArts平台，在左侧导航栏选择“开发中心 > 组件库 ”，选择“网关”页签。 2. 在网关列表中“网关名称/ID”处复制网关ID即可。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param gateway_id: The gateway_id of this ListCoreGatewayTargetsRequest.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def limit(self):
        r"""Gets the limit of this ListCoreGatewayTargetsRequest.

        **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100。 **默认取值：** 50 

        :return: The limit of this ListCoreGatewayTargetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCoreGatewayTargetsRequest.

        **参数解释：** 返回的最大结果数。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100。 **默认取值：** 50 

        :param limit: The limit of this ListCoreGatewayTargetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCoreGatewayTargetsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100000。 **默认取值：** 0 

        :return: The offset of this ListCoreGatewayTargetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCoreGatewayTargetsRequest.

        **参数解释：** 返回结果偏移量。 **约束限制：** 不涉及。 **取值范围：** 整数类型，取值为1-100000。 **默认取值：** 0 

        :param offset: The offset of this ListCoreGatewayTargetsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListCoreGatewayTargetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
