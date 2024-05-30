# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectInfoAccessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_ip': 'str',
        'intranet_ip': 'str',
        'access_ipv6': 'str',
        'access_port': 'int',
        'session_id': 'str',
        'timestamp': 'str',
        'ticket': 'str'
    }

    attribute_map = {
        'access_ip': 'access_ip',
        'intranet_ip': 'intranet_ip',
        'access_ipv6': 'access_ipv6',
        'access_port': 'access_port',
        'session_id': 'session_id',
        'timestamp': 'timestamp',
        'ticket': 'ticket'
    }

    def __init__(self, access_ip=None, intranet_ip=None, access_ipv6=None, access_port=None, session_id=None, timestamp=None, ticket=None):
        """ConnectInfoAccessInfo

        The model defined in huaweicloud sdk

        :param access_ip: 云手机实例的访问IP
        :type access_ip: str
        :param intranet_ip: 云手机实例的内网访问IP
        :type intranet_ip: str
        :param access_ipv6: 云手机服务器IPv6 IP
        :type access_ipv6: str
        :param access_port: 云手机实例的访问端口
        :type access_port: int
        :param session_id: 本次接入的会话ID
        :type session_id: str
        :param timestamp: 时间戳
        :type timestamp: str
        :param ticket: 签名令牌
        :type ticket: str
        """
        
        

        self._access_ip = None
        self._intranet_ip = None
        self._access_ipv6 = None
        self._access_port = None
        self._session_id = None
        self._timestamp = None
        self._ticket = None
        self.discriminator = None

        if access_ip is not None:
            self.access_ip = access_ip
        if intranet_ip is not None:
            self.intranet_ip = intranet_ip
        if access_ipv6 is not None:
            self.access_ipv6 = access_ipv6
        if access_port is not None:
            self.access_port = access_port
        if session_id is not None:
            self.session_id = session_id
        if timestamp is not None:
            self.timestamp = timestamp
        if ticket is not None:
            self.ticket = ticket

    @property
    def access_ip(self):
        """Gets the access_ip of this ConnectInfoAccessInfo.

        云手机实例的访问IP

        :return: The access_ip of this ConnectInfoAccessInfo.
        :rtype: str
        """
        return self._access_ip

    @access_ip.setter
    def access_ip(self, access_ip):
        """Sets the access_ip of this ConnectInfoAccessInfo.

        云手机实例的访问IP

        :param access_ip: The access_ip of this ConnectInfoAccessInfo.
        :type access_ip: str
        """
        self._access_ip = access_ip

    @property
    def intranet_ip(self):
        """Gets the intranet_ip of this ConnectInfoAccessInfo.

        云手机实例的内网访问IP

        :return: The intranet_ip of this ConnectInfoAccessInfo.
        :rtype: str
        """
        return self._intranet_ip

    @intranet_ip.setter
    def intranet_ip(self, intranet_ip):
        """Sets the intranet_ip of this ConnectInfoAccessInfo.

        云手机实例的内网访问IP

        :param intranet_ip: The intranet_ip of this ConnectInfoAccessInfo.
        :type intranet_ip: str
        """
        self._intranet_ip = intranet_ip

    @property
    def access_ipv6(self):
        """Gets the access_ipv6 of this ConnectInfoAccessInfo.

        云手机服务器IPv6 IP

        :return: The access_ipv6 of this ConnectInfoAccessInfo.
        :rtype: str
        """
        return self._access_ipv6

    @access_ipv6.setter
    def access_ipv6(self, access_ipv6):
        """Sets the access_ipv6 of this ConnectInfoAccessInfo.

        云手机服务器IPv6 IP

        :param access_ipv6: The access_ipv6 of this ConnectInfoAccessInfo.
        :type access_ipv6: str
        """
        self._access_ipv6 = access_ipv6

    @property
    def access_port(self):
        """Gets the access_port of this ConnectInfoAccessInfo.

        云手机实例的访问端口

        :return: The access_port of this ConnectInfoAccessInfo.
        :rtype: int
        """
        return self._access_port

    @access_port.setter
    def access_port(self, access_port):
        """Sets the access_port of this ConnectInfoAccessInfo.

        云手机实例的访问端口

        :param access_port: The access_port of this ConnectInfoAccessInfo.
        :type access_port: int
        """
        self._access_port = access_port

    @property
    def session_id(self):
        """Gets the session_id of this ConnectInfoAccessInfo.

        本次接入的会话ID

        :return: The session_id of this ConnectInfoAccessInfo.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ConnectInfoAccessInfo.

        本次接入的会话ID

        :param session_id: The session_id of this ConnectInfoAccessInfo.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def timestamp(self):
        """Gets the timestamp of this ConnectInfoAccessInfo.

        时间戳

        :return: The timestamp of this ConnectInfoAccessInfo.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ConnectInfoAccessInfo.

        时间戳

        :param timestamp: The timestamp of this ConnectInfoAccessInfo.
        :type timestamp: str
        """
        self._timestamp = timestamp

    @property
    def ticket(self):
        """Gets the ticket of this ConnectInfoAccessInfo.

        签名令牌

        :return: The ticket of this ConnectInfoAccessInfo.
        :rtype: str
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        """Sets the ticket of this ConnectInfoAccessInfo.

        签名令牌

        :param ticket: The ticket of this ConnectInfoAccessInfo.
        :type ticket: str
        """
        self._ticket = ticket

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
        if not isinstance(other, ConnectInfoAccessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
