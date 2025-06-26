# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BgpPeer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'peer_ip_address': 'str',
        'peer_asn': 'int',
        'state': 'str',
        'state_duration': 'str',
        'num_received_routes': 'int',
        'num_message_received': 'int',
        'num_message_sent': 'int'
    }

    attribute_map = {
        'peer_ip_address': 'peer_ip_address',
        'peer_asn': 'peer_asn',
        'state': 'state',
        'state_duration': 'state_duration',
        'num_received_routes': 'num_received_routes',
        'num_message_received': 'num_message_received',
        'num_message_sent': 'num_message_sent'
    }

    def __init__(self, peer_ip_address=None, peer_asn=None, state=None, state_duration=None, num_received_routes=None, num_message_received=None, num_message_sent=None):
        r"""BgpPeer

        The model defined in huaweicloud sdk

        :param peer_ip_address: 对端IP地址
        :type peer_ip_address: str
        :param peer_asn: 对端AS号
        :type peer_asn: int
        :param state: 状态
        :type state: str
        :param state_duration: 状态周期
        :type state_duration: str
        :param num_received_routes: 接收到的路由数量
        :type num_received_routes: int
        :param num_message_received: 接收到的消息数量
        :type num_message_received: int
        :param num_message_sent: 已发送的消息数量
        :type num_message_sent: int
        """
        
        

        self._peer_ip_address = None
        self._peer_asn = None
        self._state = None
        self._state_duration = None
        self._num_received_routes = None
        self._num_message_received = None
        self._num_message_sent = None
        self.discriminator = None

        if peer_ip_address is not None:
            self.peer_ip_address = peer_ip_address
        if peer_asn is not None:
            self.peer_asn = peer_asn
        if state is not None:
            self.state = state
        if state_duration is not None:
            self.state_duration = state_duration
        if num_received_routes is not None:
            self.num_received_routes = num_received_routes
        if num_message_received is not None:
            self.num_message_received = num_message_received
        if num_message_sent is not None:
            self.num_message_sent = num_message_sent

    @property
    def peer_ip_address(self):
        r"""Gets the peer_ip_address of this BgpPeer.

        对端IP地址

        :return: The peer_ip_address of this BgpPeer.
        :rtype: str
        """
        return self._peer_ip_address

    @peer_ip_address.setter
    def peer_ip_address(self, peer_ip_address):
        r"""Sets the peer_ip_address of this BgpPeer.

        对端IP地址

        :param peer_ip_address: The peer_ip_address of this BgpPeer.
        :type peer_ip_address: str
        """
        self._peer_ip_address = peer_ip_address

    @property
    def peer_asn(self):
        r"""Gets the peer_asn of this BgpPeer.

        对端AS号

        :return: The peer_asn of this BgpPeer.
        :rtype: int
        """
        return self._peer_asn

    @peer_asn.setter
    def peer_asn(self, peer_asn):
        r"""Sets the peer_asn of this BgpPeer.

        对端AS号

        :param peer_asn: The peer_asn of this BgpPeer.
        :type peer_asn: int
        """
        self._peer_asn = peer_asn

    @property
    def state(self):
        r"""Gets the state of this BgpPeer.

        状态

        :return: The state of this BgpPeer.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this BgpPeer.

        状态

        :param state: The state of this BgpPeer.
        :type state: str
        """
        self._state = state

    @property
    def state_duration(self):
        r"""Gets the state_duration of this BgpPeer.

        状态周期

        :return: The state_duration of this BgpPeer.
        :rtype: str
        """
        return self._state_duration

    @state_duration.setter
    def state_duration(self, state_duration):
        r"""Sets the state_duration of this BgpPeer.

        状态周期

        :param state_duration: The state_duration of this BgpPeer.
        :type state_duration: str
        """
        self._state_duration = state_duration

    @property
    def num_received_routes(self):
        r"""Gets the num_received_routes of this BgpPeer.

        接收到的路由数量

        :return: The num_received_routes of this BgpPeer.
        :rtype: int
        """
        return self._num_received_routes

    @num_received_routes.setter
    def num_received_routes(self, num_received_routes):
        r"""Sets the num_received_routes of this BgpPeer.

        接收到的路由数量

        :param num_received_routes: The num_received_routes of this BgpPeer.
        :type num_received_routes: int
        """
        self._num_received_routes = num_received_routes

    @property
    def num_message_received(self):
        r"""Gets the num_message_received of this BgpPeer.

        接收到的消息数量

        :return: The num_message_received of this BgpPeer.
        :rtype: int
        """
        return self._num_message_received

    @num_message_received.setter
    def num_message_received(self, num_message_received):
        r"""Sets the num_message_received of this BgpPeer.

        接收到的消息数量

        :param num_message_received: The num_message_received of this BgpPeer.
        :type num_message_received: int
        """
        self._num_message_received = num_message_received

    @property
    def num_message_sent(self):
        r"""Gets the num_message_sent of this BgpPeer.

        已发送的消息数量

        :return: The num_message_sent of this BgpPeer.
        :rtype: int
        """
        return self._num_message_sent

    @num_message_sent.setter
    def num_message_sent(self, num_message_sent):
        r"""Sets the num_message_sent of this BgpPeer.

        已发送的消息数量

        :param num_message_sent: The num_message_sent of this BgpPeer.
        :type num_message_sent: int
        """
        self._num_message_sent = num_message_sent

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
        if not isinstance(other, BgpPeer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
