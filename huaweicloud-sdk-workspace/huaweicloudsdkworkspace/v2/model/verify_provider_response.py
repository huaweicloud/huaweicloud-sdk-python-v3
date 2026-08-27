# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyProviderResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_id': 'str',
        'success': 'bool',
        'message': 'str'
    }

    attribute_map = {
        'provider_id': 'provider_id',
        'success': 'success',
        'message': 'message'
    }

    def __init__(self, provider_id=None, success=None, message=None):
        r"""VerifyProviderResponse

        The model defined in huaweicloud sdk

        :param provider_id: 供应商id。
        :type provider_id: str
        :param success: 是否验证成功。
        :type success: bool
        :param message: 验证结果信息。
        :type message: str
        """
        
        super().__init__()

        self._provider_id = None
        self._success = None
        self._message = None
        self.discriminator = None

        if provider_id is not None:
            self.provider_id = provider_id
        if success is not None:
            self.success = success
        if message is not None:
            self.message = message

    @property
    def provider_id(self):
        r"""Gets the provider_id of this VerifyProviderResponse.

        供应商id。

        :return: The provider_id of this VerifyProviderResponse.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this VerifyProviderResponse.

        供应商id。

        :param provider_id: The provider_id of this VerifyProviderResponse.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def success(self):
        r"""Gets the success of this VerifyProviderResponse.

        是否验证成功。

        :return: The success of this VerifyProviderResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this VerifyProviderResponse.

        是否验证成功。

        :param success: The success of this VerifyProviderResponse.
        :type success: bool
        """
        self._success = success

    @property
    def message(self):
        r"""Gets the message of this VerifyProviderResponse.

        验证结果信息。

        :return: The message of this VerifyProviderResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this VerifyProviderResponse.

        验证结果信息。

        :param message: The message of this VerifyProviderResponse.
        :type message: str
        """
        self._message = message

    def to_dict(self):
        import warnings
        warnings.warn("VerifyProviderResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, VerifyProviderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
