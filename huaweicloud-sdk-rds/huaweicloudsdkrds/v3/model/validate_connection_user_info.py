# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateConnectionUserInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_ip': 'str',
        'server_port': 'int',
        'login_user_name': 'str',
        'login_user_password': 'str'
    }

    attribute_map = {
        'server_ip': 'server_ip',
        'server_port': 'server_port',
        'login_user_name': 'login_user_name',
        'login_user_password': 'login_user_password'
    }

    def __init__(self, server_ip=None, server_port=None, login_user_name=None, login_user_password=None):
        r"""ValidateConnectionUserInfo

        The model defined in huaweicloud sdk

        :param server_ip: 服务器ip。
        :type server_ip: str
        :param server_port: 端口号。
        :type server_port: int
        :param login_user_name: 登录名。
        :type login_user_name: str
        :param login_user_password: 登录密码。要求密码长度在5~64位之间。
        :type login_user_password: str
        """
        
        

        self._server_ip = None
        self._server_port = None
        self._login_user_name = None
        self._login_user_password = None
        self.discriminator = None

        if server_ip is not None:
            self.server_ip = server_ip
        if server_port is not None:
            self.server_port = server_port
        if login_user_name is not None:
            self.login_user_name = login_user_name
        if login_user_password is not None:
            self.login_user_password = login_user_password

    @property
    def server_ip(self):
        r"""Gets the server_ip of this ValidateConnectionUserInfo.

        服务器ip。

        :return: The server_ip of this ValidateConnectionUserInfo.
        :rtype: str
        """
        return self._server_ip

    @server_ip.setter
    def server_ip(self, server_ip):
        r"""Sets the server_ip of this ValidateConnectionUserInfo.

        服务器ip。

        :param server_ip: The server_ip of this ValidateConnectionUserInfo.
        :type server_ip: str
        """
        self._server_ip = server_ip

    @property
    def server_port(self):
        r"""Gets the server_port of this ValidateConnectionUserInfo.

        端口号。

        :return: The server_port of this ValidateConnectionUserInfo.
        :rtype: int
        """
        return self._server_port

    @server_port.setter
    def server_port(self, server_port):
        r"""Sets the server_port of this ValidateConnectionUserInfo.

        端口号。

        :param server_port: The server_port of this ValidateConnectionUserInfo.
        :type server_port: int
        """
        self._server_port = server_port

    @property
    def login_user_name(self):
        r"""Gets the login_user_name of this ValidateConnectionUserInfo.

        登录名。

        :return: The login_user_name of this ValidateConnectionUserInfo.
        :rtype: str
        """
        return self._login_user_name

    @login_user_name.setter
    def login_user_name(self, login_user_name):
        r"""Sets the login_user_name of this ValidateConnectionUserInfo.

        登录名。

        :param login_user_name: The login_user_name of this ValidateConnectionUserInfo.
        :type login_user_name: str
        """
        self._login_user_name = login_user_name

    @property
    def login_user_password(self):
        r"""Gets the login_user_password of this ValidateConnectionUserInfo.

        登录密码。要求密码长度在5~64位之间。

        :return: The login_user_password of this ValidateConnectionUserInfo.
        :rtype: str
        """
        return self._login_user_password

    @login_user_password.setter
    def login_user_password(self, login_user_password):
        r"""Sets the login_user_password of this ValidateConnectionUserInfo.

        登录密码。要求密码长度在5~64位之间。

        :param login_user_password: The login_user_password of this ValidateConnectionUserInfo.
        :type login_user_password: str
        """
        self._login_user_password = login_user_password

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
        if not isinstance(other, ValidateConnectionUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
