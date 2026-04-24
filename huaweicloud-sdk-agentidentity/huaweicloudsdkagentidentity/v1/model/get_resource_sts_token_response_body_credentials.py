# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetResourceStsTokenResponseBodyCredentials:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('secret_access_key')
    sensitive_list.append('security_token')

    openapi_types = {
        'access_key_id': 'str',
        'expiration': 'datetime',
        'secret_access_key': 'str',
        'security_token': 'str'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'expiration': 'expiration',
        'secret_access_key': 'secret_access_key',
        'security_token': 'security_token'
    }

    def __init__(self, access_key_id=None, expiration=None, secret_access_key=None, security_token=None):
        r"""GetResourceStsTokenResponseBodyCredentials

        The model defined in huaweicloud sdk

        :param access_key_id: The access key ID that identifies the temporary security credentials
        :type access_key_id: str
        :param expiration: The date and time on which the current credentials expire
        :type expiration: datetime
        :param secret_access_key: The secret access key that can be used to sign requests
        :type secret_access_key: str
        :param security_token: The token that users must pass to the service API to use the temporary credentials
        :type security_token: str
        """
        
        

        self._access_key_id = None
        self._expiration = None
        self._secret_access_key = None
        self._security_token = None
        self.discriminator = None

        self.access_key_id = access_key_id
        self.expiration = expiration
        self.secret_access_key = secret_access_key
        self.security_token = security_token

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this GetResourceStsTokenResponseBodyCredentials.

        The access key ID that identifies the temporary security credentials

        :return: The access_key_id of this GetResourceStsTokenResponseBodyCredentials.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this GetResourceStsTokenResponseBodyCredentials.

        The access key ID that identifies the temporary security credentials

        :param access_key_id: The access_key_id of this GetResourceStsTokenResponseBodyCredentials.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def expiration(self):
        r"""Gets the expiration of this GetResourceStsTokenResponseBodyCredentials.

        The date and time on which the current credentials expire

        :return: The expiration of this GetResourceStsTokenResponseBodyCredentials.
        :rtype: datetime
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        r"""Sets the expiration of this GetResourceStsTokenResponseBodyCredentials.

        The date and time on which the current credentials expire

        :param expiration: The expiration of this GetResourceStsTokenResponseBodyCredentials.
        :type expiration: datetime
        """
        self._expiration = expiration

    @property
    def secret_access_key(self):
        r"""Gets the secret_access_key of this GetResourceStsTokenResponseBodyCredentials.

        The secret access key that can be used to sign requests

        :return: The secret_access_key of this GetResourceStsTokenResponseBodyCredentials.
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        r"""Sets the secret_access_key of this GetResourceStsTokenResponseBodyCredentials.

        The secret access key that can be used to sign requests

        :param secret_access_key: The secret_access_key of this GetResourceStsTokenResponseBodyCredentials.
        :type secret_access_key: str
        """
        self._secret_access_key = secret_access_key

    @property
    def security_token(self):
        r"""Gets the security_token of this GetResourceStsTokenResponseBodyCredentials.

        The token that users must pass to the service API to use the temporary credentials

        :return: The security_token of this GetResourceStsTokenResponseBodyCredentials.
        :rtype: str
        """
        return self._security_token

    @security_token.setter
    def security_token(self, security_token):
        r"""Sets the security_token of this GetResourceStsTokenResponseBodyCredentials.

        The token that users must pass to the service API to use the temporary credentials

        :param security_token: The security_token of this GetResourceStsTokenResponseBodyCredentials.
        :type security_token: str
        """
        self._security_token = security_token

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
        if not isinstance(other, GetResourceStsTokenResponseBodyCredentials):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
