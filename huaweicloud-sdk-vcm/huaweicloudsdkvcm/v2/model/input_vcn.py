# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InputVcn:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'port': 'str',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, ip=None, port=None, username=None, password=None):
        r"""InputVcn

        The model defined in huaweicloud sdk

        :param ip: vcn服务器的IP地址。
        :type ip: str
        :param port: vcn服务器的端口号。
        :type port: str
        :param username: vcn服务器的账号名。
        :type username: str
        :param password: vcn服务器与上述账号对应的密码。
        :type password: str
        """
        
        

        self._ip = None
        self._port = None
        self._username = None
        self._password = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def ip(self):
        r"""Gets the ip of this InputVcn.

        vcn服务器的IP地址。

        :return: The ip of this InputVcn.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this InputVcn.

        vcn服务器的IP地址。

        :param ip: The ip of this InputVcn.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this InputVcn.

        vcn服务器的端口号。

        :return: The port of this InputVcn.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this InputVcn.

        vcn服务器的端口号。

        :param port: The port of this InputVcn.
        :type port: str
        """
        self._port = port

    @property
    def username(self):
        r"""Gets the username of this InputVcn.

        vcn服务器的账号名。

        :return: The username of this InputVcn.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this InputVcn.

        vcn服务器的账号名。

        :param username: The username of this InputVcn.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this InputVcn.

        vcn服务器与上述账号对应的密码。

        :return: The password of this InputVcn.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this InputVcn.

        vcn服务器与上述账号对应的密码。

        :param password: The password of this InputVcn.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, InputVcn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
