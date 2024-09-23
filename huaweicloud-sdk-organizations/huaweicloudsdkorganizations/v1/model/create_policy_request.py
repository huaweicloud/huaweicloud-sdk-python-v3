# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePolicyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_security_token')

    openapi_types = {
        'x_security_token': 'str',
        'x_language': 'str',
        'body': 'CreatePolicyReqBody'
    }

    attribute_map = {
        'x_security_token': 'X-Security-Token',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, x_security_token=None, x_language=None, body=None):
        """CreatePolicyRequest

        The model defined in huaweicloud sdk

        :param x_security_token: 如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。
        :type x_security_token: str
        :param x_language: 选择接口返回的信息的语言
        :type x_language: str
        :param body: Body of the CreatePolicyRequest
        :type body: :class:`huaweicloudsdkorganizations.v1.CreatePolicyReqBody`
        """
        
        

        self._x_security_token = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        if x_security_token is not None:
            self.x_security_token = x_security_token
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def x_security_token(self):
        """Gets the x_security_token of this CreatePolicyRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :return: The x_security_token of this CreatePolicyRequest.
        :rtype: str
        """
        return self._x_security_token

    @x_security_token.setter
    def x_security_token(self, x_security_token):
        """Sets the x_security_token of this CreatePolicyRequest.

        如果正在使用临时安全凭据，则此header是必需的，该值是临时安全凭据的安全令牌（会话令牌）。

        :param x_security_token: The x_security_token of this CreatePolicyRequest.
        :type x_security_token: str
        """
        self._x_security_token = x_security_token

    @property
    def x_language(self):
        """Gets the x_language of this CreatePolicyRequest.

        选择接口返回的信息的语言

        :return: The x_language of this CreatePolicyRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this CreatePolicyRequest.

        选择接口返回的信息的语言

        :param x_language: The x_language of this CreatePolicyRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        """Gets the body of this CreatePolicyRequest.

        :return: The body of this CreatePolicyRequest.
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreatePolicyReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreatePolicyRequest.

        :param body: The body of this CreatePolicyRequest.
        :type body: :class:`huaweicloudsdkorganizations.v1.CreatePolicyReqBody`
        """
        self._body = body

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
        if not isinstance(other, CreatePolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
