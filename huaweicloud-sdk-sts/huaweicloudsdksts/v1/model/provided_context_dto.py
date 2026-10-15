# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProvidedContextDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'context_provider_urn': 'str',
        'context_assertion': 'str'
    }

    attribute_map = {
        'context_provider_urn': 'context_provider_urn',
        'context_assertion': 'context_assertion'
    }

    def __init__(self, context_provider_urn=None, context_assertion=None):
        r"""ProvidedContextDto

        The model defined in huaweicloud sdk

        :param context_provider_urn: **参数解释**： 生成可信上下文断言的提供者的URN。  **约束限制**： 长度最多为1500个字符。格式为5段，用\&quot;:\&quot;分隔，各段允许大小写字母、数字、\&quot;+\&quot;、\&quot;/\&quot;、\&quot;&#x3D;\&quot;、\&quot;-\&quot;、\&quot;_\&quot;（第2段还额外允许 \&quot;*\&quot;），长度限制为：第1段至少1位，第2段0~255位，第3段1~64位，第4段1~64位，第5段至少1位（任意字符）。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 
        :type context_provider_urn: str
        :param context_assertion: **参数解释**： 经过签名和加密的可信上下文断言。  **约束限制**： 不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 
        :type context_assertion: str
        """
        
        

        self._context_provider_urn = None
        self._context_assertion = None
        self.discriminator = None

        self.context_provider_urn = context_provider_urn
        self.context_assertion = context_assertion

    @property
    def context_provider_urn(self):
        r"""Gets the context_provider_urn of this ProvidedContextDto.

        **参数解释**： 生成可信上下文断言的提供者的URN。  **约束限制**： 长度最多为1500个字符。格式为5段，用\":\"分隔，各段允许大小写字母、数字、\"+\"、\"/\"、\"=\"、\"-\"、\"_\"（第2段还额外允许 \"*\"），长度限制为：第1段至少1位，第2段0~255位，第3段1~64位，第4段1~64位，第5段至少1位（任意字符）。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :return: The context_provider_urn of this ProvidedContextDto.
        :rtype: str
        """
        return self._context_provider_urn

    @context_provider_urn.setter
    def context_provider_urn(self, context_provider_urn):
        r"""Sets the context_provider_urn of this ProvidedContextDto.

        **参数解释**： 生成可信上下文断言的提供者的URN。  **约束限制**： 长度最多为1500个字符。格式为5段，用\":\"分隔，各段允许大小写字母、数字、\"+\"、\"/\"、\"=\"、\"-\"、\"_\"（第2段还额外允许 \"*\"），长度限制为：第1段至少1位，第2段0~255位，第3段1~64位，第4段1~64位，第5段至少1位（任意字符）。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :param context_provider_urn: The context_provider_urn of this ProvidedContextDto.
        :type context_provider_urn: str
        """
        self._context_provider_urn = context_provider_urn

    @property
    def context_assertion(self):
        r"""Gets the context_assertion of this ProvidedContextDto.

        **参数解释**： 经过签名和加密的可信上下文断言。  **约束限制**： 不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :return: The context_assertion of this ProvidedContextDto.
        :rtype: str
        """
        return self._context_assertion

    @context_assertion.setter
    def context_assertion(self, context_assertion):
        r"""Sets the context_assertion of this ProvidedContextDto.

        **参数解释**： 经过签名和加密的可信上下文断言。  **约束限制**： 不涉及。  **取值范围**： 不涉及。  **默认取值**： 不涉及。 

        :param context_assertion: The context_assertion of this ProvidedContextDto.
        :type context_assertion: str
        """
        self._context_assertion = context_assertion

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
        if not isinstance(other, ProvidedContextDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
