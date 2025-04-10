# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TokenInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('access_token')
    sensitive_list.append('id_token')
    sensitive_list.append('refresh_token')

    openapi_types = {
        'access_token': 'str',
        'expires_in': 'int',
        'id_token': 'str',
        'refresh_token': 'str',
        'token_type': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'expires_in': 'expires_in',
        'id_token': 'id_token',
        'refresh_token': 'refresh_token',
        'token_type': 'token_type'
    }

    def __init__(self, access_token=None, expires_in=None, id_token=None, refresh_token=None, token_type=None):
        r"""TokenInfoDto

        The model defined in huaweicloud sdk

        :param access_token: 用于访问分配给用户的IAM身份中心资源的不透明令牌
        :type access_token: str
        :param expires_in: 访问令牌的过期时间（以秒为单位）
        :type expires_in: int
        :param id_token: 用于表明用户身份的不透明令牌
        :type id_token: str
        :param refresh_token: 刷新令牌，此令牌可在访问令牌过期后获取新的访问令牌
        :type refresh_token: str
        :param token_type: 用于通知客户端返回的令牌是访问令牌，目前为BearerToken
        :type token_type: str
        """
        
        

        self._access_token = None
        self._expires_in = None
        self._id_token = None
        self._refresh_token = None
        self._token_type = None
        self.discriminator = None

        if access_token is not None:
            self.access_token = access_token
        if expires_in is not None:
            self.expires_in = expires_in
        if id_token is not None:
            self.id_token = id_token
        if refresh_token is not None:
            self.refresh_token = refresh_token
        if token_type is not None:
            self.token_type = token_type

    @property
    def access_token(self):
        r"""Gets the access_token of this TokenInfoDto.

        用于访问分配给用户的IAM身份中心资源的不透明令牌

        :return: The access_token of this TokenInfoDto.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        r"""Sets the access_token of this TokenInfoDto.

        用于访问分配给用户的IAM身份中心资源的不透明令牌

        :param access_token: The access_token of this TokenInfoDto.
        :type access_token: str
        """
        self._access_token = access_token

    @property
    def expires_in(self):
        r"""Gets the expires_in of this TokenInfoDto.

        访问令牌的过期时间（以秒为单位）

        :return: The expires_in of this TokenInfoDto.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        r"""Sets the expires_in of this TokenInfoDto.

        访问令牌的过期时间（以秒为单位）

        :param expires_in: The expires_in of this TokenInfoDto.
        :type expires_in: int
        """
        self._expires_in = expires_in

    @property
    def id_token(self):
        r"""Gets the id_token of this TokenInfoDto.

        用于表明用户身份的不透明令牌

        :return: The id_token of this TokenInfoDto.
        :rtype: str
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        r"""Sets the id_token of this TokenInfoDto.

        用于表明用户身份的不透明令牌

        :param id_token: The id_token of this TokenInfoDto.
        :type id_token: str
        """
        self._id_token = id_token

    @property
    def refresh_token(self):
        r"""Gets the refresh_token of this TokenInfoDto.

        刷新令牌，此令牌可在访问令牌过期后获取新的访问令牌

        :return: The refresh_token of this TokenInfoDto.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        r"""Sets the refresh_token of this TokenInfoDto.

        刷新令牌，此令牌可在访问令牌过期后获取新的访问令牌

        :param refresh_token: The refresh_token of this TokenInfoDto.
        :type refresh_token: str
        """
        self._refresh_token = refresh_token

    @property
    def token_type(self):
        r"""Gets the token_type of this TokenInfoDto.

        用于通知客户端返回的令牌是访问令牌，目前为BearerToken

        :return: The token_type of this TokenInfoDto.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        r"""Sets the token_type of this TokenInfoDto.

        用于通知客户端返回的令牌是访问令牌，目前为BearerToken

        :param token_type: The token_type of this TokenInfoDto.
        :type token_type: str
        """
        self._token_type = token_type

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
        if not isinstance(other, TokenInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
