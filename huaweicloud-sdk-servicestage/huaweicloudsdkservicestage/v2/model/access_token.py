# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessToken:

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
        'token': 'str',
        'host': 'str'
    }

    attribute_map = {
        'name': 'name',
        'token': 'token',
        'host': 'host'
    }

    def __init__(self, name=None, token=None, host=None):
        """AccessToken

        The model defined in huaweicloud sdk

        :param name: 授权名称。
        :type name: str
        :param token: git仓库设置中创建的私有token。
        :type token: str
        :param host: git仓库的主机地址，如https://192.168.1.1:8080/gitlab，默认为官方主机。
        :type host: str
        """
        
        

        self._name = None
        self._token = None
        self._host = None
        self.discriminator = None

        self.name = name
        self.token = token
        if host is not None:
            self.host = host

    @property
    def name(self):
        """Gets the name of this AccessToken.

        授权名称。

        :return: The name of this AccessToken.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessToken.

        授权名称。

        :param name: The name of this AccessToken.
        :type name: str
        """
        self._name = name

    @property
    def token(self):
        """Gets the token of this AccessToken.

        git仓库设置中创建的私有token。

        :return: The token of this AccessToken.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AccessToken.

        git仓库设置中创建的私有token。

        :param token: The token of this AccessToken.
        :type token: str
        """
        self._token = token

    @property
    def host(self):
        """Gets the host of this AccessToken.

        git仓库的主机地址，如https://192.168.1.1:8080/gitlab，默认为官方主机。

        :return: The host of this AccessToken.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this AccessToken.

        git仓库的主机地址，如https://192.168.1.1:8080/gitlab，默认为官方主机。

        :param host: The host of this AccessToken.
        :type host: str
        """
        self._host = host

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
        if not isinstance(other, AccessToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
