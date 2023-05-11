# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInputVcn:

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
        'port': 'int',
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
        """TaskInputVcn

        The model defined in huaweicloud sdk

        :param ip: VCN服务器的IP地址
        :type ip: str
        :param port: VCN服务器的端口号
        :type port: int
        :param username: VCN服务器的账号名
        :type username: str
        :param password: VCN服务器的与账号对应的密码
        :type password: str
        """
        
        

        self._ip = None
        self._port = None
        self._username = None
        self._password = None
        self.discriminator = None

        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    @property
    def ip(self):
        """Gets the ip of this TaskInputVcn.

        VCN服务器的IP地址

        :return: The ip of this TaskInputVcn.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this TaskInputVcn.

        VCN服务器的IP地址

        :param ip: The ip of this TaskInputVcn.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this TaskInputVcn.

        VCN服务器的端口号

        :return: The port of this TaskInputVcn.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TaskInputVcn.

        VCN服务器的端口号

        :param port: The port of this TaskInputVcn.
        :type port: int
        """
        self._port = port

    @property
    def username(self):
        """Gets the username of this TaskInputVcn.

        VCN服务器的账号名

        :return: The username of this TaskInputVcn.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this TaskInputVcn.

        VCN服务器的账号名

        :param username: The username of this TaskInputVcn.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        """Gets the password of this TaskInputVcn.

        VCN服务器的与账号对应的密码

        :return: The password of this TaskInputVcn.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TaskInputVcn.

        VCN服务器的与账号对应的密码

        :param password: The password of this TaskInputVcn.
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
        if not isinstance(other, TaskInputVcn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
