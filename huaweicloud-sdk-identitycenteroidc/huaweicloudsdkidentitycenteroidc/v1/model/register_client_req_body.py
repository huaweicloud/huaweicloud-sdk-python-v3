# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterClientReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_name': 'str',
        'client_type': 'str',
        'token_endpoint_auth_method': 'str',
        'scopes': 'list[str]',
        'grant_types': 'list[str]',
        'response_types': 'list[str]'
    }

    attribute_map = {
        'client_name': 'client_name',
        'client_type': 'client_type',
        'token_endpoint_auth_method': 'token_endpoint_auth_method',
        'scopes': 'scopes',
        'grant_types': 'grant_types',
        'response_types': 'response_types'
    }

    def __init__(self, client_name=None, client_type=None, token_endpoint_auth_method=None, scopes=None, grant_types=None, response_types=None):
        r"""RegisterClientReqBody

        The model defined in huaweicloud sdk

        :param client_name: 客户端名称
        :type client_name: str
        :param client_type: 客户端的类型。该服务仅支持public作为客户端类型
        :type client_type: str
        :param token_endpoint_auth_method: 向令牌端点发送请求时所需的身份验证方法
        :type token_endpoint_auth_method: str
        :param scopes: 客户端定义的作用域列表。授权后，此列表用于在授予访问令牌时限制权限
        :type scopes: list[str]
        :param grant_types: 客户端可以在令牌端点使用的OAuth2.0授权类型数组
        :type grant_types: list[str]
        :param response_types: 客户端可以在授权端点使用的OAuth2.0授权类型数组
        :type response_types: list[str]
        """
        
        

        self._client_name = None
        self._client_type = None
        self._token_endpoint_auth_method = None
        self._scopes = None
        self._grant_types = None
        self._response_types = None
        self.discriminator = None

        self.client_name = client_name
        self.client_type = client_type
        self.token_endpoint_auth_method = token_endpoint_auth_method
        if scopes is not None:
            self.scopes = scopes
        self.grant_types = grant_types
        self.response_types = response_types

    @property
    def client_name(self):
        r"""Gets the client_name of this RegisterClientReqBody.

        客户端名称

        :return: The client_name of this RegisterClientReqBody.
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        r"""Sets the client_name of this RegisterClientReqBody.

        客户端名称

        :param client_name: The client_name of this RegisterClientReqBody.
        :type client_name: str
        """
        self._client_name = client_name

    @property
    def client_type(self):
        r"""Gets the client_type of this RegisterClientReqBody.

        客户端的类型。该服务仅支持public作为客户端类型

        :return: The client_type of this RegisterClientReqBody.
        :rtype: str
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        r"""Sets the client_type of this RegisterClientReqBody.

        客户端的类型。该服务仅支持public作为客户端类型

        :param client_type: The client_type of this RegisterClientReqBody.
        :type client_type: str
        """
        self._client_type = client_type

    @property
    def token_endpoint_auth_method(self):
        r"""Gets the token_endpoint_auth_method of this RegisterClientReqBody.

        向令牌端点发送请求时所需的身份验证方法

        :return: The token_endpoint_auth_method of this RegisterClientReqBody.
        :rtype: str
        """
        return self._token_endpoint_auth_method

    @token_endpoint_auth_method.setter
    def token_endpoint_auth_method(self, token_endpoint_auth_method):
        r"""Sets the token_endpoint_auth_method of this RegisterClientReqBody.

        向令牌端点发送请求时所需的身份验证方法

        :param token_endpoint_auth_method: The token_endpoint_auth_method of this RegisterClientReqBody.
        :type token_endpoint_auth_method: str
        """
        self._token_endpoint_auth_method = token_endpoint_auth_method

    @property
    def scopes(self):
        r"""Gets the scopes of this RegisterClientReqBody.

        客户端定义的作用域列表。授权后，此列表用于在授予访问令牌时限制权限

        :return: The scopes of this RegisterClientReqBody.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        r"""Sets the scopes of this RegisterClientReqBody.

        客户端定义的作用域列表。授权后，此列表用于在授予访问令牌时限制权限

        :param scopes: The scopes of this RegisterClientReqBody.
        :type scopes: list[str]
        """
        self._scopes = scopes

    @property
    def grant_types(self):
        r"""Gets the grant_types of this RegisterClientReqBody.

        客户端可以在令牌端点使用的OAuth2.0授权类型数组

        :return: The grant_types of this RegisterClientReqBody.
        :rtype: list[str]
        """
        return self._grant_types

    @grant_types.setter
    def grant_types(self, grant_types):
        r"""Sets the grant_types of this RegisterClientReqBody.

        客户端可以在令牌端点使用的OAuth2.0授权类型数组

        :param grant_types: The grant_types of this RegisterClientReqBody.
        :type grant_types: list[str]
        """
        self._grant_types = grant_types

    @property
    def response_types(self):
        r"""Gets the response_types of this RegisterClientReqBody.

        客户端可以在授权端点使用的OAuth2.0授权类型数组

        :return: The response_types of this RegisterClientReqBody.
        :rtype: list[str]
        """
        return self._response_types

    @response_types.setter
    def response_types(self, response_types):
        r"""Sets the response_types of this RegisterClientReqBody.

        客户端可以在授权端点使用的OAuth2.0授权类型数组

        :param response_types: The response_types of this RegisterClientReqBody.
        :type response_types: list[str]
        """
        self._response_types = response_types

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
        if not isinstance(other, RegisterClientReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
