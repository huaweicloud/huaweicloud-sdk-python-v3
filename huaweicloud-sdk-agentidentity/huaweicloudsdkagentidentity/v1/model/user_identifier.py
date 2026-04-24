# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserIdentifier:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_token': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'user_token': 'user_token',
        'user_id': 'user_id'
    }

    def __init__(self, user_token=None, user_id=None):
        r"""UserIdentifier

        The model defined in huaweicloud sdk

        :param user_token: OAuth2.0 token for user identification
        :type user_token: str
        :param user_id: User ID for identification
        :type user_id: str
        """
        
        

        self._user_token = None
        self._user_id = None
        self.discriminator = None

        if user_token is not None:
            self.user_token = user_token
        if user_id is not None:
            self.user_id = user_id

    @property
    def user_token(self):
        r"""Gets the user_token of this UserIdentifier.

        OAuth2.0 token for user identification

        :return: The user_token of this UserIdentifier.
        :rtype: str
        """
        return self._user_token

    @user_token.setter
    def user_token(self, user_token):
        r"""Sets the user_token of this UserIdentifier.

        OAuth2.0 token for user identification

        :param user_token: The user_token of this UserIdentifier.
        :type user_token: str
        """
        self._user_token = user_token

    @property
    def user_id(self):
        r"""Gets the user_id of this UserIdentifier.

        User ID for identification

        :return: The user_id of this UserIdentifier.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UserIdentifier.

        User ID for identification

        :param user_id: The user_id of this UserIdentifier.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, UserIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
