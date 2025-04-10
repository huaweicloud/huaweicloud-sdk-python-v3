# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChannelDetails:

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
        'number': 'int',
        'user': 'str',
        'connection_name': 'str',
        'peer_host': 'str',
        'peer_port': 'int'
    }

    attribute_map = {
        'name': 'name',
        'number': 'number',
        'user': 'user',
        'connection_name': 'connection_name',
        'peer_host': 'peer_host',
        'peer_port': 'peer_port'
    }

    def __init__(self, name=None, number=None, user=None, connection_name=None, peer_host=None, peer_port=None):
        r"""ChannelDetails

        The model defined in huaweicloud sdk

        :param name: channel信息，包括客户端IP:Port到服务端IP:Port(channel_id)。
        :type name: str
        :param number: channel数量
        :type number: int
        :param user: 消费者用户名，在开启ACL访问控制后返回真实用户名，未开启ACL时返回null。
        :type user: str
        :param connection_name: connection信息，包括客户端IP:Port到服务端IP:Port。
        :type connection_name: str
        :param peer_host: 连接的消费者IP
        :type peer_host: str
        :param peer_port: 连接的消费者进程端口号
        :type peer_port: int
        """
        
        

        self._name = None
        self._number = None
        self._user = None
        self._connection_name = None
        self._peer_host = None
        self._peer_port = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if user is not None:
            self.user = user
        if connection_name is not None:
            self.connection_name = connection_name
        if peer_host is not None:
            self.peer_host = peer_host
        if peer_port is not None:
            self.peer_port = peer_port

    @property
    def name(self):
        r"""Gets the name of this ChannelDetails.

        channel信息，包括客户端IP:Port到服务端IP:Port(channel_id)。

        :return: The name of this ChannelDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ChannelDetails.

        channel信息，包括客户端IP:Port到服务端IP:Port(channel_id)。

        :param name: The name of this ChannelDetails.
        :type name: str
        """
        self._name = name

    @property
    def number(self):
        r"""Gets the number of this ChannelDetails.

        channel数量

        :return: The number of this ChannelDetails.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ChannelDetails.

        channel数量

        :param number: The number of this ChannelDetails.
        :type number: int
        """
        self._number = number

    @property
    def user(self):
        r"""Gets the user of this ChannelDetails.

        消费者用户名，在开启ACL访问控制后返回真实用户名，未开启ACL时返回null。

        :return: The user of this ChannelDetails.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ChannelDetails.

        消费者用户名，在开启ACL访问控制后返回真实用户名，未开启ACL时返回null。

        :param user: The user of this ChannelDetails.
        :type user: str
        """
        self._user = user

    @property
    def connection_name(self):
        r"""Gets the connection_name of this ChannelDetails.

        connection信息，包括客户端IP:Port到服务端IP:Port。

        :return: The connection_name of this ChannelDetails.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        r"""Sets the connection_name of this ChannelDetails.

        connection信息，包括客户端IP:Port到服务端IP:Port。

        :param connection_name: The connection_name of this ChannelDetails.
        :type connection_name: str
        """
        self._connection_name = connection_name

    @property
    def peer_host(self):
        r"""Gets the peer_host of this ChannelDetails.

        连接的消费者IP

        :return: The peer_host of this ChannelDetails.
        :rtype: str
        """
        return self._peer_host

    @peer_host.setter
    def peer_host(self, peer_host):
        r"""Sets the peer_host of this ChannelDetails.

        连接的消费者IP

        :param peer_host: The peer_host of this ChannelDetails.
        :type peer_host: str
        """
        self._peer_host = peer_host

    @property
    def peer_port(self):
        r"""Gets the peer_port of this ChannelDetails.

        连接的消费者进程端口号

        :return: The peer_port of this ChannelDetails.
        :rtype: int
        """
        return self._peer_port

    @peer_port.setter
    def peer_port(self, peer_port):
        r"""Sets the peer_port of this ChannelDetails.

        连接的消费者进程端口号

        :param peer_port: The peer_port of this ChannelDetails.
        :type peer_port: int
        """
        self._peer_port = peer_port

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
        if not isinstance(other, ChannelDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
