# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreGatewayOpenApiTargetConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'payload': 'str',
        'obs': 'CoreGatewayObsConfiguration'
    }

    attribute_map = {
        'payload': 'payload',
        'obs': 'obs'
    }

    def __init__(self, payload=None, obs=None):
        r"""CoreGatewayOpenApiTargetConfiguration

        The model defined in huaweicloud sdk

        :param payload: **参数解释：** OpenAPI 规范文档内容（JSON 或 YAML 格式的内联内容）。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-1048576 个字符。 **默认取值：** 不涉及。 
        :type payload: str
        :param obs: 
        :type obs: :class:`huaweicloudsdkagentarts.v1.CoreGatewayObsConfiguration`
        """
        
        

        self._payload = None
        self._obs = None
        self.discriminator = None

        if payload is not None:
            self.payload = payload
        if obs is not None:
            self.obs = obs

    @property
    def payload(self):
        r"""Gets the payload of this CoreGatewayOpenApiTargetConfiguration.

        **参数解释：** OpenAPI 规范文档内容（JSON 或 YAML 格式的内联内容）。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-1048576 个字符。 **默认取值：** 不涉及。 

        :return: The payload of this CoreGatewayOpenApiTargetConfiguration.
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        r"""Sets the payload of this CoreGatewayOpenApiTargetConfiguration.

        **参数解释：** OpenAPI 规范文档内容（JSON 或 YAML 格式的内联内容）。 **约束限制：** 不涉及。 **取值范围：** 长度为 1-1048576 个字符。 **默认取值：** 不涉及。 

        :param payload: The payload of this CoreGatewayOpenApiTargetConfiguration.
        :type payload: str
        """
        self._payload = payload

    @property
    def obs(self):
        r"""Gets the obs of this CoreGatewayOpenApiTargetConfiguration.

        :return: The obs of this CoreGatewayOpenApiTargetConfiguration.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayObsConfiguration`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this CoreGatewayOpenApiTargetConfiguration.

        :param obs: The obs of this CoreGatewayOpenApiTargetConfiguration.
        :type obs: :class:`huaweicloudsdkagentarts.v1.CoreGatewayObsConfiguration`
        """
        self._obs = obs

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
        if not isinstance(other, CoreGatewayOpenApiTargetConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
