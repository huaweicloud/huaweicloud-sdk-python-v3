# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteCoreGatewayTagsRequest:

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
        'body': 'BatchDeleteCoreGatewayTagsRequestBody'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'body': 'body'
    }

    def __init__(self, gateway_id=None, body=None):
        r"""BatchDeleteCoreGatewayTagsRequest

        The model defined in huaweicloud sdk

        :param gateway_id: **参数解释：** 网关ID，网关的唯一标识符。 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type gateway_id: str
        :param body: Body of the BatchDeleteCoreGatewayTagsRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.BatchDeleteCoreGatewayTagsRequestBody`
        """
        
        

        self._gateway_id = None
        self._body = None
        self.discriminator = None

        self.gateway_id = gateway_id
        if body is not None:
            self.body = body

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this BatchDeleteCoreGatewayTagsRequest.

        **参数解释：** 网关ID，网关的唯一标识符。 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The gateway_id of this BatchDeleteCoreGatewayTagsRequest.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this BatchDeleteCoreGatewayTagsRequest.

        **参数解释：** 网关ID，网关的唯一标识符。 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param gateway_id: The gateway_id of this BatchDeleteCoreGatewayTagsRequest.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def body(self):
        r"""Gets the body of this BatchDeleteCoreGatewayTagsRequest.

        :return: The body of this BatchDeleteCoreGatewayTagsRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchDeleteCoreGatewayTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchDeleteCoreGatewayTagsRequest.

        :param body: The body of this BatchDeleteCoreGatewayTagsRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.BatchDeleteCoreGatewayTagsRequestBody`
        """
        self._body = body

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
        if not isinstance(other, BatchDeleteCoreGatewayTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
