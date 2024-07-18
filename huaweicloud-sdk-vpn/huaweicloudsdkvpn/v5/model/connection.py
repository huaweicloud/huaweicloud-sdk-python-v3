# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Connection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('client_ip')

    openapi_types = {
        'connection_id': 'str',
        'client_virtual_ip': 'str',
        'client_ip': 'str',
        'client_user_name': 'str',
        'inbound_packets': 'int',
        'outbound_packets': 'int',
        'inbound_bytes': 'int',
        'outbound_bytes': 'int',
        'connection_established_time': 'datetime',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'client_virtual_ip': 'client_virtual_ip',
        'client_ip': 'client_ip',
        'client_user_name': 'client_user_name',
        'inbound_packets': 'inbound_packets',
        'outbound_packets': 'outbound_packets',
        'inbound_bytes': 'inbound_bytes',
        'outbound_bytes': 'outbound_bytes',
        'connection_established_time': 'connection_established_time',
        'timestamp': 'timestamp'
    }

    def __init__(self, connection_id=None, client_virtual_ip=None, client_ip=None, client_user_name=None, inbound_packets=None, outbound_packets=None, inbound_bytes=None, outbound_bytes=None, connection_established_time=None, timestamp=None):
        """Connection

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param client_virtual_ip: 客户端虚拟IP
        :type client_virtual_ip: str
        :param client_ip: 客户端IP
        :type client_ip: str
        :param client_user_name: 客户端用户名称
        :type client_user_name: str
        :param inbound_packets: 入网包数
        :type inbound_packets: int
        :param outbound_packets: 出网包数
        :type outbound_packets: int
        :param inbound_bytes: 入网字节数
        :type inbound_bytes: int
        :param outbound_bytes: 出网字节数
        :type outbound_bytes: int
        :param connection_established_time: 连接建立时间
        :type connection_established_time: datetime
        :param timestamp: 时间戳
        :type timestamp: datetime
        """
        
        

        self._connection_id = None
        self._client_virtual_ip = None
        self._client_ip = None
        self._client_user_name = None
        self._inbound_packets = None
        self._outbound_packets = None
        self._inbound_bytes = None
        self._outbound_bytes = None
        self._connection_established_time = None
        self._timestamp = None
        self.discriminator = None

        if connection_id is not None:
            self.connection_id = connection_id
        if client_virtual_ip is not None:
            self.client_virtual_ip = client_virtual_ip
        if client_ip is not None:
            self.client_ip = client_ip
        if client_user_name is not None:
            self.client_user_name = client_user_name
        if inbound_packets is not None:
            self.inbound_packets = inbound_packets
        if outbound_packets is not None:
            self.outbound_packets = outbound_packets
        if inbound_bytes is not None:
            self.inbound_bytes = inbound_bytes
        if outbound_bytes is not None:
            self.outbound_bytes = outbound_bytes
        if connection_established_time is not None:
            self.connection_established_time = connection_established_time
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def connection_id(self):
        """Gets the connection_id of this Connection.

        连接ID

        :return: The connection_id of this Connection.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this Connection.

        连接ID

        :param connection_id: The connection_id of this Connection.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def client_virtual_ip(self):
        """Gets the client_virtual_ip of this Connection.

        客户端虚拟IP

        :return: The client_virtual_ip of this Connection.
        :rtype: str
        """
        return self._client_virtual_ip

    @client_virtual_ip.setter
    def client_virtual_ip(self, client_virtual_ip):
        """Sets the client_virtual_ip of this Connection.

        客户端虚拟IP

        :param client_virtual_ip: The client_virtual_ip of this Connection.
        :type client_virtual_ip: str
        """
        self._client_virtual_ip = client_virtual_ip

    @property
    def client_ip(self):
        """Gets the client_ip of this Connection.

        客户端IP

        :return: The client_ip of this Connection.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this Connection.

        客户端IP

        :param client_ip: The client_ip of this Connection.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def client_user_name(self):
        """Gets the client_user_name of this Connection.

        客户端用户名称

        :return: The client_user_name of this Connection.
        :rtype: str
        """
        return self._client_user_name

    @client_user_name.setter
    def client_user_name(self, client_user_name):
        """Sets the client_user_name of this Connection.

        客户端用户名称

        :param client_user_name: The client_user_name of this Connection.
        :type client_user_name: str
        """
        self._client_user_name = client_user_name

    @property
    def inbound_packets(self):
        """Gets the inbound_packets of this Connection.

        入网包数

        :return: The inbound_packets of this Connection.
        :rtype: int
        """
        return self._inbound_packets

    @inbound_packets.setter
    def inbound_packets(self, inbound_packets):
        """Sets the inbound_packets of this Connection.

        入网包数

        :param inbound_packets: The inbound_packets of this Connection.
        :type inbound_packets: int
        """
        self._inbound_packets = inbound_packets

    @property
    def outbound_packets(self):
        """Gets the outbound_packets of this Connection.

        出网包数

        :return: The outbound_packets of this Connection.
        :rtype: int
        """
        return self._outbound_packets

    @outbound_packets.setter
    def outbound_packets(self, outbound_packets):
        """Sets the outbound_packets of this Connection.

        出网包数

        :param outbound_packets: The outbound_packets of this Connection.
        :type outbound_packets: int
        """
        self._outbound_packets = outbound_packets

    @property
    def inbound_bytes(self):
        """Gets the inbound_bytes of this Connection.

        入网字节数

        :return: The inbound_bytes of this Connection.
        :rtype: int
        """
        return self._inbound_bytes

    @inbound_bytes.setter
    def inbound_bytes(self, inbound_bytes):
        """Sets the inbound_bytes of this Connection.

        入网字节数

        :param inbound_bytes: The inbound_bytes of this Connection.
        :type inbound_bytes: int
        """
        self._inbound_bytes = inbound_bytes

    @property
    def outbound_bytes(self):
        """Gets the outbound_bytes of this Connection.

        出网字节数

        :return: The outbound_bytes of this Connection.
        :rtype: int
        """
        return self._outbound_bytes

    @outbound_bytes.setter
    def outbound_bytes(self, outbound_bytes):
        """Sets the outbound_bytes of this Connection.

        出网字节数

        :param outbound_bytes: The outbound_bytes of this Connection.
        :type outbound_bytes: int
        """
        self._outbound_bytes = outbound_bytes

    @property
    def connection_established_time(self):
        """Gets the connection_established_time of this Connection.

        连接建立时间

        :return: The connection_established_time of this Connection.
        :rtype: datetime
        """
        return self._connection_established_time

    @connection_established_time.setter
    def connection_established_time(self, connection_established_time):
        """Sets the connection_established_time of this Connection.

        连接建立时间

        :param connection_established_time: The connection_established_time of this Connection.
        :type connection_established_time: datetime
        """
        self._connection_established_time = connection_established_time

    @property
    def timestamp(self):
        """Gets the timestamp of this Connection.

        时间戳

        :return: The timestamp of this Connection.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Connection.

        时间戳

        :param timestamp: The timestamp of this Connection.
        :type timestamp: datetime
        """
        self._timestamp = timestamp

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
        if not isinstance(other, Connection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
