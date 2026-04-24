# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompleteResourceTokenAuthRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'session_uri': 'str',
        'user_identifier': 'UserIdentifier'
    }

    attribute_map = {
        'session_uri': 'session_uri',
        'user_identifier': 'user_identifier'
    }

    def __init__(self, session_uri=None, user_identifier=None):
        r"""CompleteResourceTokenAuthRequestBody

        The model defined in huaweicloud sdk

        :param session_uri: Unique identifier for the user&#39;s authentication session (tracks OAuth2 flow state)
        :type session_uri: str
        :param user_identifier: 
        :type user_identifier: :class:`huaweicloudsdkagentidentity.v1.UserIdentifier`
        """
        
        

        self._session_uri = None
        self._user_identifier = None
        self.discriminator = None

        self.session_uri = session_uri
        self.user_identifier = user_identifier

    @property
    def session_uri(self):
        r"""Gets the session_uri of this CompleteResourceTokenAuthRequestBody.

        Unique identifier for the user's authentication session (tracks OAuth2 flow state)

        :return: The session_uri of this CompleteResourceTokenAuthRequestBody.
        :rtype: str
        """
        return self._session_uri

    @session_uri.setter
    def session_uri(self, session_uri):
        r"""Sets the session_uri of this CompleteResourceTokenAuthRequestBody.

        Unique identifier for the user's authentication session (tracks OAuth2 flow state)

        :param session_uri: The session_uri of this CompleteResourceTokenAuthRequestBody.
        :type session_uri: str
        """
        self._session_uri = session_uri

    @property
    def user_identifier(self):
        r"""Gets the user_identifier of this CompleteResourceTokenAuthRequestBody.

        :return: The user_identifier of this CompleteResourceTokenAuthRequestBody.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.UserIdentifier`
        """
        return self._user_identifier

    @user_identifier.setter
    def user_identifier(self, user_identifier):
        r"""Sets the user_identifier of this CompleteResourceTokenAuthRequestBody.

        :param user_identifier: The user_identifier of this CompleteResourceTokenAuthRequestBody.
        :type user_identifier: :class:`huaweicloudsdkagentidentity.v1.UserIdentifier`
        """
        self._user_identifier = user_identifier

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
        if not isinstance(other, CompleteResourceTokenAuthRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
