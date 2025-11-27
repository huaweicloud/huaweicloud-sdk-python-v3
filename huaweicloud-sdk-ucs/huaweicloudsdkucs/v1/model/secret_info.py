# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecretInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_mode': 'str',
        'secret': 'object'
    }

    attribute_map = {
        'auth_mode': 'authMode',
        'secret': 'secret'
    }

    def __init__(self, auth_mode=None, secret=None):
        r"""SecretInfo

        The model defined in huaweicloud sdk

        :param auth_mode: 使用的认证模式
        :type auth_mode: str
        :param secret: 存储了实际认证凭据的Secret
        :type secret: object
        """
        
        

        self._auth_mode = None
        self._secret = None
        self.discriminator = None

        if auth_mode is not None:
            self.auth_mode = auth_mode
        if secret is not None:
            self.secret = secret

    @property
    def auth_mode(self):
        r"""Gets the auth_mode of this SecretInfo.

        使用的认证模式

        :return: The auth_mode of this SecretInfo.
        :rtype: str
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        r"""Sets the auth_mode of this SecretInfo.

        使用的认证模式

        :param auth_mode: The auth_mode of this SecretInfo.
        :type auth_mode: str
        """
        self._auth_mode = auth_mode

    @property
    def secret(self):
        r"""Gets the secret of this SecretInfo.

        存储了实际认证凭据的Secret

        :return: The secret of this SecretInfo.
        :rtype: object
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        r"""Sets the secret of this SecretInfo.

        存储了实际认证凭据的Secret

        :param secret: The secret of this SecretInfo.
        :type secret: object
        """
        self._secret = secret

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
        if not isinstance(other, SecretInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
