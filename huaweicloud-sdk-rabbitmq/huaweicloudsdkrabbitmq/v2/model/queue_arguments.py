# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueueArguments:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_message_ttl': 'int',
        'x_dead_letter_exchange': 'str',
        'x_dead_letter_routing_key': 'str',
        'x_queue_mode': 'str'
    }

    attribute_map = {
        'x_message_ttl': 'x-message-ttl',
        'x_dead_letter_exchange': 'x-dead-letter-exchange',
        'x_dead_letter_routing_key': 'x-dead-letter-routing-key',
        'x_queue_mode': 'x-queue-mode'
    }

    def __init__(self, x_message_ttl=None, x_dead_letter_exchange=None, x_dead_letter_routing_key=None, x_queue_mode=None):
        r"""QueueArguments

        The model defined in huaweicloud sdk

        :param x_message_ttl: 消息过期时间，发布到Queue的消息在被丢弃之前可以存活多长时间。
        :type x_message_ttl: int
        :param x_dead_letter_exchange: 死信Exchange名称，消息被拒绝或过期时将重新发布到该Exchange。
        :type x_dead_letter_exchange: str
        :param x_dead_letter_routing_key: 死信的RoutingKey，死信Exchange会发送死信消息到绑定对应RoutingKey的Queue上。
        :type x_dead_letter_routing_key: str
        :param x_queue_mode: 惰性队列[（AMQP版本默认持久化所有消息，不涉及此参数）](tag:hws,hws_hk)
        :type x_queue_mode: str
        """
        
        

        self._x_message_ttl = None
        self._x_dead_letter_exchange = None
        self._x_dead_letter_routing_key = None
        self._x_queue_mode = None
        self.discriminator = None

        if x_message_ttl is not None:
            self.x_message_ttl = x_message_ttl
        if x_dead_letter_exchange is not None:
            self.x_dead_letter_exchange = x_dead_letter_exchange
        if x_dead_letter_routing_key is not None:
            self.x_dead_letter_routing_key = x_dead_letter_routing_key
        if x_queue_mode is not None:
            self.x_queue_mode = x_queue_mode

    @property
    def x_message_ttl(self):
        r"""Gets the x_message_ttl of this QueueArguments.

        消息过期时间，发布到Queue的消息在被丢弃之前可以存活多长时间。

        :return: The x_message_ttl of this QueueArguments.
        :rtype: int
        """
        return self._x_message_ttl

    @x_message_ttl.setter
    def x_message_ttl(self, x_message_ttl):
        r"""Sets the x_message_ttl of this QueueArguments.

        消息过期时间，发布到Queue的消息在被丢弃之前可以存活多长时间。

        :param x_message_ttl: The x_message_ttl of this QueueArguments.
        :type x_message_ttl: int
        """
        self._x_message_ttl = x_message_ttl

    @property
    def x_dead_letter_exchange(self):
        r"""Gets the x_dead_letter_exchange of this QueueArguments.

        死信Exchange名称，消息被拒绝或过期时将重新发布到该Exchange。

        :return: The x_dead_letter_exchange of this QueueArguments.
        :rtype: str
        """
        return self._x_dead_letter_exchange

    @x_dead_letter_exchange.setter
    def x_dead_letter_exchange(self, x_dead_letter_exchange):
        r"""Sets the x_dead_letter_exchange of this QueueArguments.

        死信Exchange名称，消息被拒绝或过期时将重新发布到该Exchange。

        :param x_dead_letter_exchange: The x_dead_letter_exchange of this QueueArguments.
        :type x_dead_letter_exchange: str
        """
        self._x_dead_letter_exchange = x_dead_letter_exchange

    @property
    def x_dead_letter_routing_key(self):
        r"""Gets the x_dead_letter_routing_key of this QueueArguments.

        死信的RoutingKey，死信Exchange会发送死信消息到绑定对应RoutingKey的Queue上。

        :return: The x_dead_letter_routing_key of this QueueArguments.
        :rtype: str
        """
        return self._x_dead_letter_routing_key

    @x_dead_letter_routing_key.setter
    def x_dead_letter_routing_key(self, x_dead_letter_routing_key):
        r"""Sets the x_dead_letter_routing_key of this QueueArguments.

        死信的RoutingKey，死信Exchange会发送死信消息到绑定对应RoutingKey的Queue上。

        :param x_dead_letter_routing_key: The x_dead_letter_routing_key of this QueueArguments.
        :type x_dead_letter_routing_key: str
        """
        self._x_dead_letter_routing_key = x_dead_letter_routing_key

    @property
    def x_queue_mode(self):
        r"""Gets the x_queue_mode of this QueueArguments.

        惰性队列[（AMQP版本默认持久化所有消息，不涉及此参数）](tag:hws,hws_hk)

        :return: The x_queue_mode of this QueueArguments.
        :rtype: str
        """
        return self._x_queue_mode

    @x_queue_mode.setter
    def x_queue_mode(self, x_queue_mode):
        r"""Sets the x_queue_mode of this QueueArguments.

        惰性队列[（AMQP版本默认持久化所有消息，不涉及此参数）](tag:hws,hws_hk)

        :param x_queue_mode: The x_queue_mode of this QueueArguments.
        :type x_queue_mode: str
        """
        self._x_queue_mode = x_queue_mode

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
        if not isinstance(other, QueueArguments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
