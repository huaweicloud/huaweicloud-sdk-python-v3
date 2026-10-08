# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreModelProxyDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_model_provider_id': 'str',
        'gateway_id': 'str'
    }

    attribute_map = {
        'custom_model_provider_id': 'custom_model_provider_id',
        'gateway_id': 'gateway_id'
    }

    def __init__(self, custom_model_provider_id=None, gateway_id=None):
        r"""CoreModelProxyDetails

        The model defined in huaweicloud sdk

        :param custom_model_provider_id: **参数解释：** 模型提供商ID。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type custom_model_provider_id: str
        :param gateway_id: **参数解释：** 模型代理的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **约束限制：** 不涉及。 **默认取值：** 不涉及。 
        :type gateway_id: str
        """
        
        

        self._custom_model_provider_id = None
        self._gateway_id = None
        self.discriminator = None

        self.custom_model_provider_id = custom_model_provider_id
        self.gateway_id = gateway_id

    @property
    def custom_model_provider_id(self):
        r"""Gets the custom_model_provider_id of this CoreModelProxyDetails.

        **参数解释：** 模型提供商ID。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The custom_model_provider_id of this CoreModelProxyDetails.
        :rtype: str
        """
        return self._custom_model_provider_id

    @custom_model_provider_id.setter
    def custom_model_provider_id(self, custom_model_provider_id):
        r"""Sets the custom_model_provider_id of this CoreModelProxyDetails.

        **参数解释：** 模型提供商ID。 **约束限制：** 不涉及。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param custom_model_provider_id: The custom_model_provider_id of this CoreModelProxyDetails.
        :type custom_model_provider_id: str
        """
        self._custom_model_provider_id = custom_model_provider_id

    @property
    def gateway_id(self):
        r"""Gets the gateway_id of this CoreModelProxyDetails.

        **参数解释：** 模型代理的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **约束限制：** 不涉及。 **默认取值：** 不涉及。 

        :return: The gateway_id of this CoreModelProxyDetails.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        r"""Sets the gateway_id of this CoreModelProxyDetails.

        **参数解释：** 模型代理的唯一标识符。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **约束限制：** 不涉及。 **默认取值：** 不涉及。 

        :param gateway_id: The gateway_id of this CoreModelProxyDetails.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

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
        if not isinstance(other, CoreModelProxyDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
