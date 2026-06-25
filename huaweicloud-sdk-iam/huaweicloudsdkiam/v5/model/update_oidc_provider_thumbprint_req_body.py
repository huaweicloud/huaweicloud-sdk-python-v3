# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateOIDCProviderThumbprintReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'thumbprints': 'list[str]'
    }

    attribute_map = {
        'thumbprints': 'thumbprints'
    }

    def __init__(self, thumbprints=None):
        r"""UpdateOIDCProviderThumbprintReqBody

        The model defined in huaweicloud sdk

        :param thumbprints: **参数解释**： OIDC 身份提供商的服务器证书指纹列表。  **约束限制**： 列表元素数量取值范围为[1,5]个，每个元素字符串长度为64。  **取值范围**： 不涉及。  **默认取值**： 不涉及。
        :type thumbprints: list[str]
        """
        
        

        self._thumbprints = None
        self.discriminator = None

        self.thumbprints = thumbprints

    @property
    def thumbprints(self):
        r"""Gets the thumbprints of this UpdateOIDCProviderThumbprintReqBody.

        **参数解释**： OIDC 身份提供商的服务器证书指纹列表。  **约束限制**： 列表元素数量取值范围为[1,5]个，每个元素字符串长度为64。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :return: The thumbprints of this UpdateOIDCProviderThumbprintReqBody.
        :rtype: list[str]
        """
        return self._thumbprints

    @thumbprints.setter
    def thumbprints(self, thumbprints):
        r"""Sets the thumbprints of this UpdateOIDCProviderThumbprintReqBody.

        **参数解释**： OIDC 身份提供商的服务器证书指纹列表。  **约束限制**： 列表元素数量取值范围为[1,5]个，每个元素字符串长度为64。  **取值范围**： 不涉及。  **默认取值**： 不涉及。

        :param thumbprints: The thumbprints of this UpdateOIDCProviderThumbprintReqBody.
        :type thumbprints: list[str]
        """
        self._thumbprints = thumbprints

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
        if not isinstance(other, UpdateOIDCProviderThumbprintReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
