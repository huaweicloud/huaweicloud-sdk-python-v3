# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOauth2TokenRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'grant_type': 'str',
        'code': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'redirect_uri': 'str',
        'access_type': 'str'
    }

    attribute_map = {
        'grant_type': 'grant_type',
        'code': 'code',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'redirect_uri': 'redirect_uri',
        'access_type': 'access_type'
    }

    def __init__(self, grant_type=None, code=None, client_id=None, client_secret=None, redirect_uri=None, access_type=None):
        r"""ShowOauth2TokenRequestBody

        The model defined in huaweicloud sdk

        :param grant_type: 固定值authorization_code
        :type grant_type: str
        :param code: 授权码
        :type code: str
        :param client_id: 客户端应用注册ID
        :type client_id: str
        :param client_secret: 客户端应用注册密钥
        :type client_secret: str
        :param redirect_uri: 重定向地址，与授权码重定向地址一直，与应用注册是配置的回调地址校验需要一致
        :type redirect_uri: str
        :param access_type: 接入模式，默认在线模式，可不填，值为离线模式时，设置为offline会返回refresh_token
        :type access_type: str
        """
        
        

        self._grant_type = None
        self._code = None
        self._client_id = None
        self._client_secret = None
        self._redirect_uri = None
        self._access_type = None
        self.discriminator = None

        self.grant_type = grant_type
        self.code = code
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        if access_type is not None:
            self.access_type = access_type

    @property
    def grant_type(self):
        r"""Gets the grant_type of this ShowOauth2TokenRequestBody.

        固定值authorization_code

        :return: The grant_type of this ShowOauth2TokenRequestBody.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        r"""Sets the grant_type of this ShowOauth2TokenRequestBody.

        固定值authorization_code

        :param grant_type: The grant_type of this ShowOauth2TokenRequestBody.
        :type grant_type: str
        """
        self._grant_type = grant_type

    @property
    def code(self):
        r"""Gets the code of this ShowOauth2TokenRequestBody.

        授权码

        :return: The code of this ShowOauth2TokenRequestBody.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowOauth2TokenRequestBody.

        授权码

        :param code: The code of this ShowOauth2TokenRequestBody.
        :type code: str
        """
        self._code = code

    @property
    def client_id(self):
        r"""Gets the client_id of this ShowOauth2TokenRequestBody.

        客户端应用注册ID

        :return: The client_id of this ShowOauth2TokenRequestBody.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this ShowOauth2TokenRequestBody.

        客户端应用注册ID

        :param client_id: The client_id of this ShowOauth2TokenRequestBody.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        r"""Gets the client_secret of this ShowOauth2TokenRequestBody.

        客户端应用注册密钥

        :return: The client_secret of this ShowOauth2TokenRequestBody.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        r"""Sets the client_secret of this ShowOauth2TokenRequestBody.

        客户端应用注册密钥

        :param client_secret: The client_secret of this ShowOauth2TokenRequestBody.
        :type client_secret: str
        """
        self._client_secret = client_secret

    @property
    def redirect_uri(self):
        r"""Gets the redirect_uri of this ShowOauth2TokenRequestBody.

        重定向地址，与授权码重定向地址一直，与应用注册是配置的回调地址校验需要一致

        :return: The redirect_uri of this ShowOauth2TokenRequestBody.
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        r"""Sets the redirect_uri of this ShowOauth2TokenRequestBody.

        重定向地址，与授权码重定向地址一直，与应用注册是配置的回调地址校验需要一致

        :param redirect_uri: The redirect_uri of this ShowOauth2TokenRequestBody.
        :type redirect_uri: str
        """
        self._redirect_uri = redirect_uri

    @property
    def access_type(self):
        r"""Gets the access_type of this ShowOauth2TokenRequestBody.

        接入模式，默认在线模式，可不填，值为离线模式时，设置为offline会返回refresh_token

        :return: The access_type of this ShowOauth2TokenRequestBody.
        :rtype: str
        """
        return self._access_type

    @access_type.setter
    def access_type(self, access_type):
        r"""Sets the access_type of this ShowOauth2TokenRequestBody.

        接入模式，默认在线模式，可不填，值为离线模式时，设置为offline会返回refresh_token

        :param access_type: The access_type of this ShowOauth2TokenRequestBody.
        :type access_type: str
        """
        self._access_type = access_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowOauth2TokenRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
