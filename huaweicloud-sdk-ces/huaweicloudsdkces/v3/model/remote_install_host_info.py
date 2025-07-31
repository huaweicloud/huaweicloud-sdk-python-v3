# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoteInstallHostInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'remote_ip': 'str',
        'user_name': 'str',
        'port': 'str',
        'password': 'str',
        'remote_use_pem': 'bool'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'remote_ip': 'remote_ip',
        'user_name': 'user_name',
        'port': 'port',
        'password': 'password',
        'remote_use_pem': 'remote_use_pem'
    }

    def __init__(self, instance_name=None, remote_ip=None, user_name=None, port=None, password=None, remote_use_pem=None):
        r"""RemoteInstallHostInfo

        The model defined in huaweicloud sdk

        :param instance_name: 被远程安装的主机名称
        :type instance_name: str
        :param remote_ip: 被远程安装的主机IP
        :type remote_ip: str
        :param user_name: 被远程安装的主机的登录用户名
        :type user_name: str
        :param port: 被远程安装的主机的登录端口
        :type port: str
        :param password: 被远程安装的主机的登录密码
        :type password: str
        :param remote_use_pem: 被远程安装的主机远程连接是否采用秘钥方式（false时为密码方式）
        :type remote_use_pem: bool
        """
        
        

        self._instance_name = None
        self._remote_ip = None
        self._user_name = None
        self._port = None
        self._password = None
        self._remote_use_pem = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if remote_ip is not None:
            self.remote_ip = remote_ip
        if user_name is not None:
            self.user_name = user_name
        if port is not None:
            self.port = port
        if password is not None:
            self.password = password
        if remote_use_pem is not None:
            self.remote_use_pem = remote_use_pem

    @property
    def instance_name(self):
        r"""Gets the instance_name of this RemoteInstallHostInfo.

        被远程安装的主机名称

        :return: The instance_name of this RemoteInstallHostInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this RemoteInstallHostInfo.

        被远程安装的主机名称

        :param instance_name: The instance_name of this RemoteInstallHostInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def remote_ip(self):
        r"""Gets the remote_ip of this RemoteInstallHostInfo.

        被远程安装的主机IP

        :return: The remote_ip of this RemoteInstallHostInfo.
        :rtype: str
        """
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, remote_ip):
        r"""Sets the remote_ip of this RemoteInstallHostInfo.

        被远程安装的主机IP

        :param remote_ip: The remote_ip of this RemoteInstallHostInfo.
        :type remote_ip: str
        """
        self._remote_ip = remote_ip

    @property
    def user_name(self):
        r"""Gets the user_name of this RemoteInstallHostInfo.

        被远程安装的主机的登录用户名

        :return: The user_name of this RemoteInstallHostInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this RemoteInstallHostInfo.

        被远程安装的主机的登录用户名

        :param user_name: The user_name of this RemoteInstallHostInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def port(self):
        r"""Gets the port of this RemoteInstallHostInfo.

        被远程安装的主机的登录端口

        :return: The port of this RemoteInstallHostInfo.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this RemoteInstallHostInfo.

        被远程安装的主机的登录端口

        :param port: The port of this RemoteInstallHostInfo.
        :type port: str
        """
        self._port = port

    @property
    def password(self):
        r"""Gets the password of this RemoteInstallHostInfo.

        被远程安装的主机的登录密码

        :return: The password of this RemoteInstallHostInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this RemoteInstallHostInfo.

        被远程安装的主机的登录密码

        :param password: The password of this RemoteInstallHostInfo.
        :type password: str
        """
        self._password = password

    @property
    def remote_use_pem(self):
        r"""Gets the remote_use_pem of this RemoteInstallHostInfo.

        被远程安装的主机远程连接是否采用秘钥方式（false时为密码方式）

        :return: The remote_use_pem of this RemoteInstallHostInfo.
        :rtype: bool
        """
        return self._remote_use_pem

    @remote_use_pem.setter
    def remote_use_pem(self, remote_use_pem):
        r"""Sets the remote_use_pem of this RemoteInstallHostInfo.

        被远程安装的主机远程连接是否采用秘钥方式（false时为密码方式）

        :param remote_use_pem: The remote_use_pem of this RemoteInstallHostInfo.
        :type remote_use_pem: bool
        """
        self._remote_use_pem = remote_use_pem

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
        if not isinstance(other, RemoteInstallHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
