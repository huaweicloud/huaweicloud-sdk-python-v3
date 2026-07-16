# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssumeAgencyForPodIdentityRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token': 'str'
    }

    attribute_map = {
        'token': 'token'
    }

    def __init__(self, token=None):
        r"""AssumeAgencyForPodIdentityRequestBody

        The model defined in huaweicloud sdk

        :param token: **参数解释：** pod-identity关联所绑定的ServiceAccount token。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无
        :type token: str
        """
        
        

        self._token = None
        self.discriminator = None

        self.token = token

    @property
    def token(self):
        r"""Gets the token of this AssumeAgencyForPodIdentityRequestBody.

        **参数解释：** pod-identity关联所绑定的ServiceAccount token。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无

        :return: The token of this AssumeAgencyForPodIdentityRequestBody.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this AssumeAgencyForPodIdentityRequestBody.

        **参数解释：** pod-identity关联所绑定的ServiceAccount token。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 无

        :param token: The token of this AssumeAgencyForPodIdentityRequestBody.
        :type token: str
        """
        self._token = token

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
        if not isinstance(other, AssumeAgencyForPodIdentityRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
