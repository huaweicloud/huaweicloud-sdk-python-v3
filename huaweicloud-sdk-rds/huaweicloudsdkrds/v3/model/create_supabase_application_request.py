# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSupabaseApplicationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_client_token')

    openapi_types = {
        'x_language': 'str',
        'x_client_token': 'str',
        'body': 'CreateSupabaseApplicationRequestBody'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'x_client_token': 'X-Client-Token',
        'body': 'body'
    }

    def __init__(self, x_language=None, x_client_token=None, body=None):
        r"""CreateSupabaseApplicationRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param x_client_token: 保证客户端请求幂等性的标识。32位UUID格式，72小时内唯一。
        :type x_client_token: str
        :param body: Body of the CreateSupabaseApplicationRequest
        :type body: :class:`huaweicloudsdkrds.v3.CreateSupabaseApplicationRequestBody`
        """
        
        

        self._x_language = None
        self._x_client_token = None
        self._body = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if x_client_token is not None:
            self.x_client_token = x_client_token
        if body is not None:
            self.body = body

    @property
    def x_language(self):
        r"""Gets the x_language of this CreateSupabaseApplicationRequest.

        语言

        :return: The x_language of this CreateSupabaseApplicationRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this CreateSupabaseApplicationRequest.

        语言

        :param x_language: The x_language of this CreateSupabaseApplicationRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_client_token(self):
        r"""Gets the x_client_token of this CreateSupabaseApplicationRequest.

        保证客户端请求幂等性的标识。32位UUID格式，72小时内唯一。

        :return: The x_client_token of this CreateSupabaseApplicationRequest.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        r"""Sets the x_client_token of this CreateSupabaseApplicationRequest.

        保证客户端请求幂等性的标识。32位UUID格式，72小时内唯一。

        :param x_client_token: The x_client_token of this CreateSupabaseApplicationRequest.
        :type x_client_token: str
        """
        self._x_client_token = x_client_token

    @property
    def body(self):
        r"""Gets the body of this CreateSupabaseApplicationRequest.

        :return: The body of this CreateSupabaseApplicationRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.CreateSupabaseApplicationRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateSupabaseApplicationRequest.

        :param body: The body of this CreateSupabaseApplicationRequest.
        :type body: :class:`huaweicloudsdkrds.v3.CreateSupabaseApplicationRequestBody`
        """
        self._body = body

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
        if not isinstance(other, CreateSupabaseApplicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
