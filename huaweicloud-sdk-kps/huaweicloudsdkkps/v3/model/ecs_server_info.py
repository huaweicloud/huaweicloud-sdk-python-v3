# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EcsServerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'auth': 'Auth',
        'disable_password': 'bool',
        'port': 'int'
    }

    attribute_map = {
        'id': 'id',
        'auth': 'auth',
        'disable_password': 'disable_password',
        'port': 'port'
    }

    def __init__(self, id=None, auth=None, disable_password=None, port=None):
        """EcsServerInfo

        The model defined in huaweicloud sdk

        :param id: 需要绑定(替换或重置)SSH密钥对的虚拟机id
        :type id: str
        :param auth: 
        :type auth: :class:`huaweicloudsdkkps.v3.Auth`
        :param disable_password: - true：禁用虚拟机的ssh登录。 - false：不禁用虚拟机的ssh登录。
        :type disable_password: bool
        :param port: SSH监听端口。
        :type port: int
        """
        
        

        self._id = None
        self._auth = None
        self._disable_password = None
        self._port = None
        self.discriminator = None

        self.id = id
        if auth is not None:
            self.auth = auth
        if disable_password is not None:
            self.disable_password = disable_password
        if port is not None:
            self.port = port

    @property
    def id(self):
        """Gets the id of this EcsServerInfo.

        需要绑定(替换或重置)SSH密钥对的虚拟机id

        :return: The id of this EcsServerInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcsServerInfo.

        需要绑定(替换或重置)SSH密钥对的虚拟机id

        :param id: The id of this EcsServerInfo.
        :type id: str
        """
        self._id = id

    @property
    def auth(self):
        """Gets the auth of this EcsServerInfo.

        :return: The auth of this EcsServerInfo.
        :rtype: :class:`huaweicloudsdkkps.v3.Auth`
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """Sets the auth of this EcsServerInfo.

        :param auth: The auth of this EcsServerInfo.
        :type auth: :class:`huaweicloudsdkkps.v3.Auth`
        """
        self._auth = auth

    @property
    def disable_password(self):
        """Gets the disable_password of this EcsServerInfo.

        - true：禁用虚拟机的ssh登录。 - false：不禁用虚拟机的ssh登录。

        :return: The disable_password of this EcsServerInfo.
        :rtype: bool
        """
        return self._disable_password

    @disable_password.setter
    def disable_password(self, disable_password):
        """Sets the disable_password of this EcsServerInfo.

        - true：禁用虚拟机的ssh登录。 - false：不禁用虚拟机的ssh登录。

        :param disable_password: The disable_password of this EcsServerInfo.
        :type disable_password: bool
        """
        self._disable_password = disable_password

    @property
    def port(self):
        """Gets the port of this EcsServerInfo.

        SSH监听端口。

        :return: The port of this EcsServerInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this EcsServerInfo.

        SSH监听端口。

        :param port: The port of this EcsServerInfo.
        :type port: int
        """
        self._port = port

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
        if not isinstance(other, EcsServerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
