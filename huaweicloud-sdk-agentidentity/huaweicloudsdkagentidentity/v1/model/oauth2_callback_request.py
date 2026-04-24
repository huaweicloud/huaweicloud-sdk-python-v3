# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Oauth2CallbackRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'credential_provider_id': 'str',
        'code': 'str',
        'state': 'str',
        'error': 'str',
        'error_description': 'str'
    }

    attribute_map = {
        'credential_provider_id': 'credential_provider_id',
        'code': 'code',
        'state': 'state',
        'error': 'error',
        'error_description': 'error_description'
    }

    def __init__(self, credential_provider_id=None, code=None, state=None, error=None, error_description=None):
        r"""Oauth2CallbackRequest

        The model defined in huaweicloud sdk

        :param credential_provider_id: Unique identifier of the credential provider
        :type credential_provider_id: str
        :param code: OAuth2.0 Standard Authorization Code - one-time use, short-lived token for access token exchange. Present ONLY on successful authorization.
        :type code: str
        :param state: OAuth2.0 Standard CSRF Protection State - opaque string, echo of original request state. PRESENT FOR BOTH SUCCESS AND ERROR.
        :type state: str
        :param error: OAuth2.0 Standard Error Code - present ONLY on authorization failure (denial/expiry/invalid). e.g. access_denied, invalid_scope, server_error
        :type error: str
        :param error_description: OAuth2.0 Standard Error Description - human-readable error message, paired with error param, URL-encoded for safe transmission
        :type error_description: str
        """
        
        

        self._credential_provider_id = None
        self._code = None
        self._state = None
        self._error = None
        self._error_description = None
        self.discriminator = None

        self.credential_provider_id = credential_provider_id
        if code is not None:
            self.code = code
        self.state = state
        if error is not None:
            self.error = error
        if error_description is not None:
            self.error_description = error_description

    @property
    def credential_provider_id(self):
        r"""Gets the credential_provider_id of this Oauth2CallbackRequest.

        Unique identifier of the credential provider

        :return: The credential_provider_id of this Oauth2CallbackRequest.
        :rtype: str
        """
        return self._credential_provider_id

    @credential_provider_id.setter
    def credential_provider_id(self, credential_provider_id):
        r"""Sets the credential_provider_id of this Oauth2CallbackRequest.

        Unique identifier of the credential provider

        :param credential_provider_id: The credential_provider_id of this Oauth2CallbackRequest.
        :type credential_provider_id: str
        """
        self._credential_provider_id = credential_provider_id

    @property
    def code(self):
        r"""Gets the code of this Oauth2CallbackRequest.

        OAuth2.0 Standard Authorization Code - one-time use, short-lived token for access token exchange. Present ONLY on successful authorization.

        :return: The code of this Oauth2CallbackRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this Oauth2CallbackRequest.

        OAuth2.0 Standard Authorization Code - one-time use, short-lived token for access token exchange. Present ONLY on successful authorization.

        :param code: The code of this Oauth2CallbackRequest.
        :type code: str
        """
        self._code = code

    @property
    def state(self):
        r"""Gets the state of this Oauth2CallbackRequest.

        OAuth2.0 Standard CSRF Protection State - opaque string, echo of original request state. PRESENT FOR BOTH SUCCESS AND ERROR.

        :return: The state of this Oauth2CallbackRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this Oauth2CallbackRequest.

        OAuth2.0 Standard CSRF Protection State - opaque string, echo of original request state. PRESENT FOR BOTH SUCCESS AND ERROR.

        :param state: The state of this Oauth2CallbackRequest.
        :type state: str
        """
        self._state = state

    @property
    def error(self):
        r"""Gets the error of this Oauth2CallbackRequest.

        OAuth2.0 Standard Error Code - present ONLY on authorization failure (denial/expiry/invalid). e.g. access_denied, invalid_scope, server_error

        :return: The error of this Oauth2CallbackRequest.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this Oauth2CallbackRequest.

        OAuth2.0 Standard Error Code - present ONLY on authorization failure (denial/expiry/invalid). e.g. access_denied, invalid_scope, server_error

        :param error: The error of this Oauth2CallbackRequest.
        :type error: str
        """
        self._error = error

    @property
    def error_description(self):
        r"""Gets the error_description of this Oauth2CallbackRequest.

        OAuth2.0 Standard Error Description - human-readable error message, paired with error param, URL-encoded for safe transmission

        :return: The error_description of this Oauth2CallbackRequest.
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        r"""Sets the error_description of this Oauth2CallbackRequest.

        OAuth2.0 Standard Error Description - human-readable error message, paired with error param, URL-encoded for safe transmission

        :param error_description: The error_description of this Oauth2CallbackRequest.
        :type error_description: str
        """
        self._error_description = error_description

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
        if not isinstance(other, Oauth2CallbackRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
