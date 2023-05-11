# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'str',
        'ip': 'str',
        'user_name': 'str',
        'service_name': 'str',
        'connection_string': 'str'
    }

    attribute_map = {
        'port': 'port',
        'ip': 'ip',
        'user_name': 'user_name',
        'service_name': 'service_name',
        'connection_string': 'connection_string'
    }

    def __init__(self, port=None, ip=None, user_name=None, service_name=None, connection_string=None):
        """DataBase

        The model defined in huaweicloud sdk

        :param port: 端口。
        :type port: str
        :param ip: 连接IP。
        :type ip: str
        :param user_name: 用户名。
        :type user_name: str
        :param service_name: 服务名。
        :type service_name: str
        :param connection_string: 连接字符串。
        :type connection_string: str
        """
        
        

        self._port = None
        self._ip = None
        self._user_name = None
        self._service_name = None
        self._connection_string = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if ip is not None:
            self.ip = ip
        self.user_name = user_name
        self.service_name = service_name
        if connection_string is not None:
            self.connection_string = connection_string

    @property
    def port(self):
        """Gets the port of this DataBase.

        端口。

        :return: The port of this DataBase.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DataBase.

        端口。

        :param port: The port of this DataBase.
        :type port: str
        """
        self._port = port

    @property
    def ip(self):
        """Gets the ip of this DataBase.

        连接IP。

        :return: The ip of this DataBase.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this DataBase.

        连接IP。

        :param ip: The ip of this DataBase.
        :type ip: str
        """
        self._ip = ip

    @property
    def user_name(self):
        """Gets the user_name of this DataBase.

        用户名。

        :return: The user_name of this DataBase.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this DataBase.

        用户名。

        :param user_name: The user_name of this DataBase.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def service_name(self):
        """Gets the service_name of this DataBase.

        服务名。

        :return: The service_name of this DataBase.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this DataBase.

        服务名。

        :param service_name: The service_name of this DataBase.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def connection_string(self):
        """Gets the connection_string of this DataBase.

        连接字符串。

        :return: The connection_string of this DataBase.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this DataBase.

        连接字符串。

        :param connection_string: The connection_string of this DataBase.
        :type connection_string: str
        """
        self._connection_string = connection_string

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
        if not isinstance(other, DataBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
