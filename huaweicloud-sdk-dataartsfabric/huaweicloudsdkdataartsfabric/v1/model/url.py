# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Url:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'address': 'str',
        'type': 'str',
        'token': 'str'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'type': 'type',
        'token': 'token'
    }

    def __init__(self, name=None, address=None, type=None, token=None):
        r"""Url

        The model defined in huaweicloud sdk

        :param name: Url名称，其中ApiInvoke表示endpoint相关功能restful接口，其他名称的意义可以从cap信息中获取
        :type name: str
        :param address: Url地址
        :type address: str
        :param type: 类型，PUBLIC为公网地址，PRIVATE为内网地址
        :type type: str
        :param token: Token
        :type token: str
        """
        
        

        self._name = None
        self._address = None
        self._type = None
        self._token = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if type is not None:
            self.type = type
        if token is not None:
            self.token = token

    @property
    def name(self):
        r"""Gets the name of this Url.

        Url名称，其中ApiInvoke表示endpoint相关功能restful接口，其他名称的意义可以从cap信息中获取

        :return: The name of this Url.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Url.

        Url名称，其中ApiInvoke表示endpoint相关功能restful接口，其他名称的意义可以从cap信息中获取

        :param name: The name of this Url.
        :type name: str
        """
        self._name = name

    @property
    def address(self):
        r"""Gets the address of this Url.

        Url地址

        :return: The address of this Url.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this Url.

        Url地址

        :param address: The address of this Url.
        :type address: str
        """
        self._address = address

    @property
    def type(self):
        r"""Gets the type of this Url.

        类型，PUBLIC为公网地址，PRIVATE为内网地址

        :return: The type of this Url.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Url.

        类型，PUBLIC为公网地址，PRIVATE为内网地址

        :param type: The type of this Url.
        :type type: str
        """
        self._type = type

    @property
    def token(self):
        r"""Gets the token of this Url.

        Token

        :return: The token of this Url.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this Url.

        Token

        :param token: The token of this Url.
        :type token: str
        """
        self._token = token

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
        if not isinstance(other, Url):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
