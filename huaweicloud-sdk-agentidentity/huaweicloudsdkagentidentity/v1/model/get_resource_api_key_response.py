# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetResourceApiKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('api_key')

    openapi_types = {
        'api_key': 'str'
    }

    attribute_map = {
        'api_key': 'api_key'
    }

    def __init__(self, api_key=None):
        r"""GetResourceApiKeyResponse

        The model defined in huaweicloud sdk

        :param api_key: API key associated with the requested resource
        :type api_key: str
        """
        
        super().__init__()

        self._api_key = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key

    @property
    def api_key(self):
        r"""Gets the api_key of this GetResourceApiKeyResponse.

        API key associated with the requested resource

        :return: The api_key of this GetResourceApiKeyResponse.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this GetResourceApiKeyResponse.

        API key associated with the requested resource

        :param api_key: The api_key of this GetResourceApiKeyResponse.
        :type api_key: str
        """
        self._api_key = api_key

    def to_dict(self):
        import warnings
        warnings.warn("GetResourceApiKeyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetResourceApiKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
