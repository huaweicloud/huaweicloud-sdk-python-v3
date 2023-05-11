# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceDB:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'connection_string': 'str',
        'source_db_type': 'str',
        'service_name': 'str',
        'ip': 'str',
        'port': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'connection_string': 'connection_string',
        'source_db_type': 'source_db_type',
        'service_name': 'service_name',
        'ip': 'ip',
        'port': 'port'
    }

    def __init__(self, user_name=None, connection_string=None, source_db_type=None, service_name=None, ip=None, port=None):
        """SourceDB

        The model defined in huaweicloud sdk

        :param user_name: 用户名。
        :type user_name: str
        :param connection_string: 连接字符串。
        :type connection_string: str
        :param source_db_type: 源数据库类型。
        :type source_db_type: str
        :param service_name: service名称。
        :type service_name: str
        :param ip: ip。
        :type ip: str
        :param port: port。
        :type port: str
        """
        
        

        self._user_name = None
        self._connection_string = None
        self._source_db_type = None
        self._service_name = None
        self._ip = None
        self._port = None
        self.discriminator = None

        self.user_name = user_name
        if connection_string is not None:
            self.connection_string = connection_string
        self.source_db_type = source_db_type
        self.service_name = service_name
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port

    @property
    def user_name(self):
        """Gets the user_name of this SourceDB.

        用户名。

        :return: The user_name of this SourceDB.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this SourceDB.

        用户名。

        :param user_name: The user_name of this SourceDB.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def connection_string(self):
        """Gets the connection_string of this SourceDB.

        连接字符串。

        :return: The connection_string of this SourceDB.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this SourceDB.

        连接字符串。

        :param connection_string: The connection_string of this SourceDB.
        :type connection_string: str
        """
        self._connection_string = connection_string

    @property
    def source_db_type(self):
        """Gets the source_db_type of this SourceDB.

        源数据库类型。

        :return: The source_db_type of this SourceDB.
        :rtype: str
        """
        return self._source_db_type

    @source_db_type.setter
    def source_db_type(self, source_db_type):
        """Sets the source_db_type of this SourceDB.

        源数据库类型。

        :param source_db_type: The source_db_type of this SourceDB.
        :type source_db_type: str
        """
        self._source_db_type = source_db_type

    @property
    def service_name(self):
        """Gets the service_name of this SourceDB.

        service名称。

        :return: The service_name of this SourceDB.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this SourceDB.

        service名称。

        :param service_name: The service_name of this SourceDB.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def ip(self):
        """Gets the ip of this SourceDB.

        ip。

        :return: The ip of this SourceDB.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this SourceDB.

        ip。

        :param ip: The ip of this SourceDB.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        """Gets the port of this SourceDB.

        port。

        :return: The port of this SourceDB.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SourceDB.

        port。

        :param port: The port of this SourceDB.
        :type port: str
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
        if not isinstance(other, SourceDB):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
