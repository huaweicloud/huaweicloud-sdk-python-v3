# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOauth2TokenResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_token': 'str',
        'refresh_token': 'str',
        'scope': 'str',
        'token_type': 'str',
        'expires_in': 'int'
    }

    attribute_map = {
        'access_token': 'access_token',
        'refresh_token': 'refresh_token',
        'scope': 'scope',
        'token_type': 'token_type',
        'expires_in': 'expires_in'
    }

    def __init__(self, access_token=None, refresh_token=None, scope=None, token_type=None, expires_in=None):
        r"""ShowOauth2TokenResponse

        The model defined in huaweicloud sdk

        :param access_token: 用户级接入token
        :type access_token: str
        :param refresh_token: 用户级刷新token，离线模式适用，用于服务端主动刷新用户token
        :type refresh_token: str
        :param scope: 授权信息范围
        :type scope: str
        :param token_type: token类型，固定值“Bearer”，消息头传入token时前缀填入方式
        :type token_type: str
        :param expires_in: token失效时长
        :type expires_in: int
        """
        
        super(ShowOauth2TokenResponse, self).__init__()

        self._access_token = None
        self._refresh_token = None
        self._scope = None
        self._token_type = None
        self._expires_in = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if scope is not None:
            self.scope = scope
        if token_type is not None:
            self.token_type = token_type
        if expires_in is not None:
            self.expires_in = expires_in

    @property
    def access_token(self):
        r"""Gets the access_token of this ShowOauth2TokenResponse.

        用户级接入token

        :return: The access_token of this ShowOauth2TokenResponse.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        r"""Sets the access_token of this ShowOauth2TokenResponse.

        用户级接入token

        :param access_token: The access_token of this ShowOauth2TokenResponse.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def refresh_token(self):
        r"""Gets the refresh_token of this ShowOauth2TokenResponse.

        用户级刷新token，离线模式适用，用于服务端主动刷新用户token

        :return: The refresh_token of this ShowOauth2TokenResponse.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        r"""Sets the refresh_token of this ShowOauth2TokenResponse.

        用户级刷新token，离线模式适用，用于服务端主动刷新用户token

        :param refresh_token: The refresh_token of this ShowOauth2TokenResponse.
        :type refresh_token: str
        """
        self._refresh_token = refresh_token

    @property
    def scope(self):
        r"""Gets the scope of this ShowOauth2TokenResponse.

        授权信息范围

        :return: The scope of this ShowOauth2TokenResponse.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ShowOauth2TokenResponse.

        授权信息范围

        :param scope: The scope of this ShowOauth2TokenResponse.
        :type scope: str
        """
        self._scope = scope

    @property
    def token_type(self):
        r"""Gets the token_type of this ShowOauth2TokenResponse.

        token类型，固定值“Bearer”，消息头传入token时前缀填入方式

        :return: The token_type of this ShowOauth2TokenResponse.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        r"""Sets the token_type of this ShowOauth2TokenResponse.

        token类型，固定值“Bearer”，消息头传入token时前缀填入方式

        :param token_type: The token_type of this ShowOauth2TokenResponse.
        :type token_type: str
        """
        self._token_type = token_type

    @property
    def expires_in(self):
        r"""Gets the expires_in of this ShowOauth2TokenResponse.

        token失效时长

        :return: The expires_in of this ShowOauth2TokenResponse.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        r"""Sets the expires_in of this ShowOauth2TokenResponse.

        token失效时长

        :param expires_in: The expires_in of this ShowOauth2TokenResponse.
        :type expires_in: int
        """
        self._expires_in = expires_in

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
        if not isinstance(other, ShowOauth2TokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
