# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionExtensionResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'verification_code_enabled': 'bool'
    }

    attribute_map = {
        'verification_code_enabled': 'verification_code_enabled'
    }

    def __init__(self, verification_code_enabled=None):
        r"""SubscriptionExtensionResponse

        The model defined in huaweicloud sdk

        :param verification_code_enabled: 是否启用验证码发送确认短信，默认为false。
        :type verification_code_enabled: bool
        """
        
        

        self._verification_code_enabled = None
        self.discriminator = None

        if verification_code_enabled is not None:
            self.verification_code_enabled = verification_code_enabled

    @property
    def verification_code_enabled(self):
        r"""Gets the verification_code_enabled of this SubscriptionExtensionResponse.

        是否启用验证码发送确认短信，默认为false。

        :return: The verification_code_enabled of this SubscriptionExtensionResponse.
        :rtype: bool
        """
        return self._verification_code_enabled

    @verification_code_enabled.setter
    def verification_code_enabled(self, verification_code_enabled):
        r"""Sets the verification_code_enabled of this SubscriptionExtensionResponse.

        是否启用验证码发送确认短信，默认为false。

        :param verification_code_enabled: The verification_code_enabled of this SubscriptionExtensionResponse.
        :type verification_code_enabled: bool
        """
        self._verification_code_enabled = verification_code_enabled

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
        if not isinstance(other, SubscriptionExtensionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
