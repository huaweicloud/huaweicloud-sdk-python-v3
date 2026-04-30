# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchCpcsTokenResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token': 'SwitchTokenResponseToken',
        'x_cpcs_token': 'str'
    }

    attribute_map = {
        'token': 'token',
        'x_cpcs_token': 'X-CPCS-Token'
    }

    def __init__(self, token=None, x_cpcs_token=None):
        r"""SwitchCpcsTokenResponse

        The model defined in huaweicloud sdk

        :param token: 
        :type token: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseToken`
        :param x_cpcs_token: 
        :type x_cpcs_token: str
        """
        
        super().__init__()

        self._token = None
        self._x_cpcs_token = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if x_cpcs_token is not None:
            self.x_cpcs_token = x_cpcs_token

    @property
    def token(self):
        r"""Gets the token of this SwitchCpcsTokenResponse.

        :return: The token of this SwitchCpcsTokenResponse.
        :rtype: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseToken`
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this SwitchCpcsTokenResponse.

        :param token: The token of this SwitchCpcsTokenResponse.
        :type token: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseToken`
        """
        self._token = token

    @property
    def x_cpcs_token(self):
        r"""Gets the x_cpcs_token of this SwitchCpcsTokenResponse.

        :return: The x_cpcs_token of this SwitchCpcsTokenResponse.
        :rtype: str
        """
        return self._x_cpcs_token

    @x_cpcs_token.setter
    def x_cpcs_token(self, x_cpcs_token):
        r"""Sets the x_cpcs_token of this SwitchCpcsTokenResponse.

        :param x_cpcs_token: The x_cpcs_token of this SwitchCpcsTokenResponse.
        :type x_cpcs_token: str
        """
        self._x_cpcs_token = x_cpcs_token

    def to_dict(self):
        import warnings
        warnings.warn("SwitchCpcsTokenResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SwitchCpcsTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
