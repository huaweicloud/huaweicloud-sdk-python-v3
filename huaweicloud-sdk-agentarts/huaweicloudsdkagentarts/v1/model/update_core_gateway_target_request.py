# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreGatewayTargetRequest:

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
        'target_id': 'str',
        'body': 'UpdateCoreGatewayTargetRequestBody'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'target_id': 'target_id',
        'body': 'body'
    }

    def __init__(self, gateway_id=None, target_id=None, body=None):
        r"""UpdateCoreGatewayTargetRequest

        The model defined in huaweicloud sdk

        :param gateway_id: **参数解释：** 网关的唯一标识符。 网关ID获取方式： 1. 进入AgentArts平台，在左侧导航栏选择“开发中心 &gt; 组件库 ”，选择“网关”页签。 2. 在网关列表中“网关名称/ID”处复制网关ID即可。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type gateway_id: str
        :param target_id: **参数解释：** 目标服务的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type target_id: str
        :param body: Body of the UpdateCoreGatewayTargetRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateCoreGatewayTargetRequestBody`
        """
        
        

        self._gateway_id = None
        self._target_id = None
        self._body = None
        self.discriminator = None

        self.gateway_id = gateway_id
        self.target_id = target_id
        if body is not None:
            self.body = body

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this UpdateCoreGatewayTargetRequest.

        **参数解释：** 网关的唯一标识符。 网关ID获取方式： 1. 进入AgentArts平台，在左侧导航栏选择“开发中心 > 组件库 ”，选择“网关”页签。 2. 在网关列表中“网关名称/ID”处复制网关ID即可。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The gateway_id of this UpdateCoreGatewayTargetRequest.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this UpdateCoreGatewayTargetRequest.

        **参数解释：** 网关的唯一标识符。 网关ID获取方式： 1. 进入AgentArts平台，在左侧导航栏选择“开发中心 > 组件库 ”，选择“网关”页签。 2. 在网关列表中“网关名称/ID”处复制网关ID即可。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param gateway_id: The gateway_id of this UpdateCoreGatewayTargetRequest.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def target_id(self):
        r"""Gets the target_id of this UpdateCoreGatewayTargetRequest.

        **参数解释：** 目标服务的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The target_id of this UpdateCoreGatewayTargetRequest.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this UpdateCoreGatewayTargetRequest.

        **参数解释：** 目标服务的唯一标识符。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param target_id: The target_id of this UpdateCoreGatewayTargetRequest.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCoreGatewayTargetRequest.

        :return: The body of this UpdateCoreGatewayTargetRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCoreGatewayTargetRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCoreGatewayTargetRequest.

        :param body: The body of this UpdateCoreGatewayTargetRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateCoreGatewayTargetRequestBody`
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
        if not isinstance(other, UpdateCoreGatewayTargetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
