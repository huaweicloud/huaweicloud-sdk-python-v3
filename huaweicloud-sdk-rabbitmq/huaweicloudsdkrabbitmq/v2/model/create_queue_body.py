# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateQueueBody:

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
        'auto_delete': 'bool',
        'durable': 'bool',
        'dead_letter_exchange': 'str',
        'dead_letter_routing_key': 'str',
        'message_ttl': 'int',
        'lazy_mode': 'str'
    }

    attribute_map = {
        'name': 'name',
        'auto_delete': 'auto_delete',
        'durable': 'durable',
        'dead_letter_exchange': 'dead_letter_exchange',
        'dead_letter_routing_key': 'dead_letter_routing_key',
        'message_ttl': 'message_ttl',
        'lazy_mode': 'lazy_mode'
    }

    def __init__(self, name=None, auto_delete=None, durable=None, dead_letter_exchange=None, dead_letter_routing_key=None, message_ttl=None, lazy_mode=None):
        r"""CreateQueueBody

        The model defined in huaweicloud sdk

        :param name: Queue名称
        :type name: str
        :param auto_delete: 是否自动删除
        :type auto_delete: bool
        :param durable: 是否持久化[（AMQP版本默认持久化，不涉及此字段）](tag:hws,hws_hk)
        :type durable: bool
        :param dead_letter_exchange: 死信Exchange名称，消息被拒绝或过期时将重新发布到该Exchange。
        :type dead_letter_exchange: str
        :param dead_letter_routing_key: 死信Exchange的RoutingKey，死信Exchange会发送死信消息到绑定对应RoutingKey的Queue上。
        :type dead_letter_routing_key: str
        :param message_ttl: 发布到Queue的消息在被丢弃之前可以存活多长时间
        :type message_ttl: int
        :param lazy_mode: 若设置惰性队列，请输入lazy。惰性队列模式会在磁盘上存储尽可能多的消息以减少内存使用；若不设置，队列将消息存储在内存缓存以尽可能快地传递消息。[（AMQP版本默认将消息存储到磁盘，不涉及此字段）](tag:hws,hws_hk)
        :type lazy_mode: str
        """
        
        

        self._name = None
        self._auto_delete = None
        self._durable = None
        self._dead_letter_exchange = None
        self._dead_letter_routing_key = None
        self._message_ttl = None
        self._lazy_mode = None
        self.discriminator = None

        self.name = name
        self.auto_delete = auto_delete
        if durable is not None:
            self.durable = durable
        if dead_letter_exchange is not None:
            self.dead_letter_exchange = dead_letter_exchange
        if dead_letter_routing_key is not None:
            self.dead_letter_routing_key = dead_letter_routing_key
        if message_ttl is not None:
            self.message_ttl = message_ttl
        if lazy_mode is not None:
            self.lazy_mode = lazy_mode

    @property
    def name(self):
        r"""Gets the name of this CreateQueueBody.

        Queue名称

        :return: The name of this CreateQueueBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateQueueBody.

        Queue名称

        :param name: The name of this CreateQueueBody.
        :type name: str
        """
        self._name = name

    @property
    def auto_delete(self):
        r"""Gets the auto_delete of this CreateQueueBody.

        是否自动删除

        :return: The auto_delete of this CreateQueueBody.
        :rtype: bool
        """
        return self._auto_delete

    @auto_delete.setter
    def auto_delete(self, auto_delete):
        r"""Sets the auto_delete of this CreateQueueBody.

        是否自动删除

        :param auto_delete: The auto_delete of this CreateQueueBody.
        :type auto_delete: bool
        """
        self._auto_delete = auto_delete

    @property
    def durable(self):
        r"""Gets the durable of this CreateQueueBody.

        是否持久化[（AMQP版本默认持久化，不涉及此字段）](tag:hws,hws_hk)

        :return: The durable of this CreateQueueBody.
        :rtype: bool
        """
        return self._durable

    @durable.setter
    def durable(self, durable):
        r"""Sets the durable of this CreateQueueBody.

        是否持久化[（AMQP版本默认持久化，不涉及此字段）](tag:hws,hws_hk)

        :param durable: The durable of this CreateQueueBody.
        :type durable: bool
        """
        self._durable = durable

    @property
    def dead_letter_exchange(self):
        r"""Gets the dead_letter_exchange of this CreateQueueBody.

        死信Exchange名称，消息被拒绝或过期时将重新发布到该Exchange。

        :return: The dead_letter_exchange of this CreateQueueBody.
        :rtype: str
        """
        return self._dead_letter_exchange

    @dead_letter_exchange.setter
    def dead_letter_exchange(self, dead_letter_exchange):
        r"""Sets the dead_letter_exchange of this CreateQueueBody.

        死信Exchange名称，消息被拒绝或过期时将重新发布到该Exchange。

        :param dead_letter_exchange: The dead_letter_exchange of this CreateQueueBody.
        :type dead_letter_exchange: str
        """
        self._dead_letter_exchange = dead_letter_exchange

    @property
    def dead_letter_routing_key(self):
        r"""Gets the dead_letter_routing_key of this CreateQueueBody.

        死信Exchange的RoutingKey，死信Exchange会发送死信消息到绑定对应RoutingKey的Queue上。

        :return: The dead_letter_routing_key of this CreateQueueBody.
        :rtype: str
        """
        return self._dead_letter_routing_key

    @dead_letter_routing_key.setter
    def dead_letter_routing_key(self, dead_letter_routing_key):
        r"""Sets the dead_letter_routing_key of this CreateQueueBody.

        死信Exchange的RoutingKey，死信Exchange会发送死信消息到绑定对应RoutingKey的Queue上。

        :param dead_letter_routing_key: The dead_letter_routing_key of this CreateQueueBody.
        :type dead_letter_routing_key: str
        """
        self._dead_letter_routing_key = dead_letter_routing_key

    @property
    def message_ttl(self):
        r"""Gets the message_ttl of this CreateQueueBody.

        发布到Queue的消息在被丢弃之前可以存活多长时间

        :return: The message_ttl of this CreateQueueBody.
        :rtype: int
        """
        return self._message_ttl

    @message_ttl.setter
    def message_ttl(self, message_ttl):
        r"""Sets the message_ttl of this CreateQueueBody.

        发布到Queue的消息在被丢弃之前可以存活多长时间

        :param message_ttl: The message_ttl of this CreateQueueBody.
        :type message_ttl: int
        """
        self._message_ttl = message_ttl

    @property
    def lazy_mode(self):
        r"""Gets the lazy_mode of this CreateQueueBody.

        若设置惰性队列，请输入lazy。惰性队列模式会在磁盘上存储尽可能多的消息以减少内存使用；若不设置，队列将消息存储在内存缓存以尽可能快地传递消息。[（AMQP版本默认将消息存储到磁盘，不涉及此字段）](tag:hws,hws_hk)

        :return: The lazy_mode of this CreateQueueBody.
        :rtype: str
        """
        return self._lazy_mode

    @lazy_mode.setter
    def lazy_mode(self, lazy_mode):
        r"""Sets the lazy_mode of this CreateQueueBody.

        若设置惰性队列，请输入lazy。惰性队列模式会在磁盘上存储尽可能多的消息以减少内存使用；若不设置，队列将消息存储在内存缓存以尽可能快地传递消息。[（AMQP版本默认将消息存储到磁盘，不涉及此字段）](tag:hws,hws_hk)

        :param lazy_mode: The lazy_mode of this CreateQueueBody.
        :type lazy_mode: str
        """
        self._lazy_mode = lazy_mode

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
        if not isinstance(other, CreateQueueBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
