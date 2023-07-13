# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceRequest:

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
        'body': 'InstanceRequest'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'x_client_token': 'X-Client-Token',
        'body': 'body'
    }

    def __init__(self, x_language=None, x_client_token=None, body=None):
        """CreateInstanceRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param x_client_token: 保证客户端请求幂等性的标识。 该标识为32位UUID格式，由客户端生成，且需确保72小时内不同请求之间该标识具有唯一性。
        :type x_client_token: str
        :param body: Body of the CreateInstanceRequest
        :type body: :class:`huaweicloudsdkrds.v3.InstanceRequest`
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
        """Gets the x_language of this CreateInstanceRequest.

        语言

        :return: The x_language of this CreateInstanceRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this CreateInstanceRequest.

        语言

        :param x_language: The x_language of this CreateInstanceRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def x_client_token(self):
        """Gets the x_client_token of this CreateInstanceRequest.

        保证客户端请求幂等性的标识。 该标识为32位UUID格式，由客户端生成，且需确保72小时内不同请求之间该标识具有唯一性。

        :return: The x_client_token of this CreateInstanceRequest.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        """Sets the x_client_token of this CreateInstanceRequest.

        保证客户端请求幂等性的标识。 该标识为32位UUID格式，由客户端生成，且需确保72小时内不同请求之间该标识具有唯一性。

        :param x_client_token: The x_client_token of this CreateInstanceRequest.
        :type x_client_token: str
        """
        self._x_client_token = x_client_token

    @property
    def body(self):
        """Gets the body of this CreateInstanceRequest.

        :return: The body of this CreateInstanceRequest.
        :rtype: :class:`huaweicloudsdkrds.v3.InstanceRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateInstanceRequest.

        :param body: The body of this CreateInstanceRequest.
        :type body: :class:`huaweicloudsdkrds.v3.InstanceRequest`
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
        if not isinstance(other, CreateInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
