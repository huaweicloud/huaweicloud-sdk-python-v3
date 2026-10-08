# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomModelProviderRequest:

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
        'body': 'UpdateCustomModelProviderRequestBody'
    }

    attribute_map = {
        'custom_model_provider_id': 'custom_model_provider_id',
        'body': 'body'
    }

    def __init__(self, custom_model_provider_id=None, body=None):
        r"""UpdateCustomModelProviderRequest

        The model defined in huaweicloud sdk

        :param custom_model_provider_id: **参数解释：** 模型提供商ID。 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type custom_model_provider_id: str
        :param body: Body of the UpdateCustomModelProviderRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateCustomModelProviderRequestBody`
        """
        
        

        self._custom_model_provider_id = None
        self._body = None
        self.discriminator = None

        self.custom_model_provider_id = custom_model_provider_id
        if body is not None:
            self.body = body

    @property
    def custom_model_provider_id(self):
        r"""Gets the custom_model_provider_id of this UpdateCustomModelProviderRequest.

        **参数解释：** 模型提供商ID。 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The custom_model_provider_id of this UpdateCustomModelProviderRequest.
        :rtype: str
        """
        return self._custom_model_provider_id

    @custom_model_provider_id.setter
    def custom_model_provider_id(self, custom_model_provider_id):
        r"""Sets the custom_model_provider_id of this UpdateCustomModelProviderRequest.

        **参数解释：** 模型提供商ID。 **约束限制：** 长度固定为36字符，必须为UUID格式。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param custom_model_provider_id: The custom_model_provider_id of this UpdateCustomModelProviderRequest.
        :type custom_model_provider_id: str
        """
        self._custom_model_provider_id = custom_model_provider_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCustomModelProviderRequest.

        :return: The body of this UpdateCustomModelProviderRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UpdateCustomModelProviderRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCustomModelProviderRequest.

        :param body: The body of this UpdateCustomModelProviderRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.UpdateCustomModelProviderRequestBody`
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
        if not isinstance(other, UpdateCustomModelProviderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
