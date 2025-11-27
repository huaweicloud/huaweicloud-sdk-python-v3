# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_certificate_data': 'str',
        'client_key_data': 'str',
        'token': 'str'
    }

    attribute_map = {
        'client_certificate_data': 'client-certificate-data',
        'client_key_data': 'client-key-data',
        'token': 'token'
    }

    def __init__(self, client_certificate_data=None, client_key_data=None, token=None):
        r"""AuthInfo

        The model defined in huaweicloud sdk

        :param client_certificate_data: 客户端证书
        :type client_certificate_data: str
        :param client_key_data: 包含来自TLS客户端密钥文件的PEM编码数据
        :type client_key_data: str
        :param token: 身份验证令牌
        :type token: str
        """
        
        

        self._client_certificate_data = None
        self._client_key_data = None
        self._token = None
        self.discriminator = None

        if client_certificate_data is not None:
            self.client_certificate_data = client_certificate_data
        if client_key_data is not None:
            self.client_key_data = client_key_data
        if token is not None:
            self.token = token

    @property
    def client_certificate_data(self):
        r"""Gets the client_certificate_data of this AuthInfo.

        客户端证书

        :return: The client_certificate_data of this AuthInfo.
        :rtype: str
        """
        return self._client_certificate_data

    @client_certificate_data.setter
    def client_certificate_data(self, client_certificate_data):
        r"""Sets the client_certificate_data of this AuthInfo.

        客户端证书

        :param client_certificate_data: The client_certificate_data of this AuthInfo.
        :type client_certificate_data: str
        """
        self._client_certificate_data = client_certificate_data

    @property
    def client_key_data(self):
        r"""Gets the client_key_data of this AuthInfo.

        包含来自TLS客户端密钥文件的PEM编码数据

        :return: The client_key_data of this AuthInfo.
        :rtype: str
        """
        return self._client_key_data

    @client_key_data.setter
    def client_key_data(self, client_key_data):
        r"""Sets the client_key_data of this AuthInfo.

        包含来自TLS客户端密钥文件的PEM编码数据

        :param client_key_data: The client_key_data of this AuthInfo.
        :type client_key_data: str
        """
        self._client_key_data = client_key_data

    @property
    def token(self):
        r"""Gets the token of this AuthInfo.

        身份验证令牌

        :return: The token of this AuthInfo.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this AuthInfo.

        身份验证令牌

        :param token: The token of this AuthInfo.
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
        if not isinstance(other, AuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
