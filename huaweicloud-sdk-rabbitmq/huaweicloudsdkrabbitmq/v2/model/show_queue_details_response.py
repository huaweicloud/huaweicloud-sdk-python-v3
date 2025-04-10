# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQueueDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vhost': 'str',
        'name': 'str',
        'durable': 'bool',
        'auto_delete': 'bool',
        'messages': 'int',
        'consumers': 'int',
        'policy': 'str',
        'arguments': 'QueueArguments',
        'consumer_details': 'list[ConsumerDetails]',
        'queue_bindings': 'list[BindingsDetails]'
    }

    attribute_map = {
        'vhost': 'vhost',
        'name': 'name',
        'durable': 'durable',
        'auto_delete': 'auto_delete',
        'messages': 'messages',
        'consumers': 'consumers',
        'policy': 'policy',
        'arguments': 'arguments',
        'consumer_details': 'consumer_details',
        'queue_bindings': 'queue_bindings'
    }

    def __init__(self, vhost=None, name=None, durable=None, auto_delete=None, messages=None, consumers=None, policy=None, arguments=None, consumer_details=None, queue_bindings=None):
        r"""ShowQueueDetailsResponse

        The model defined in huaweicloud sdk

        :param vhost: Queue所属Vhost名称
        :type vhost: str
        :param name: Queue名称
        :type name: str
        :param durable: 是否持久化
        :type durable: bool
        :param auto_delete: 是否自动删除
        :type auto_delete: bool
        :param messages: 待消费消息数
        :type messages: int
        :param consumers: 连接的消费者数
        :type consumers: int
        :param policy: 策略[（AMQP版本不支持policy，不涉及此参数）](tag:hws,hws_hk)
        :type policy: str
        :param arguments: 
        :type arguments: :class:`huaweicloudsdkrabbitmq.v2.QueueArguments`
        :param consumer_details: 订阅该Queue的消费者信息。
        :type consumer_details: list[:class:`huaweicloudsdkrabbitmq.v2.ConsumerDetails`]
        :param queue_bindings: 以此Queue为目标的绑定信息列表。
        :type queue_bindings: list[:class:`huaweicloudsdkrabbitmq.v2.BindingsDetails`]
        """
        
        super(ShowQueueDetailsResponse, self).__init__()

        self._vhost = None
        self._name = None
        self._durable = None
        self._auto_delete = None
        self._messages = None
        self._consumers = None
        self._policy = None
        self._arguments = None
        self._consumer_details = None
        self._queue_bindings = None
        self.discriminator = None

        if vhost is not None:
            self.vhost = vhost
        if name is not None:
            self.name = name
        if durable is not None:
            self.durable = durable
        if auto_delete is not None:
            self.auto_delete = auto_delete
        if messages is not None:
            self.messages = messages
        if consumers is not None:
            self.consumers = consumers
        if policy is not None:
            self.policy = policy
        if arguments is not None:
            self.arguments = arguments
        if consumer_details is not None:
            self.consumer_details = consumer_details
        if queue_bindings is not None:
            self.queue_bindings = queue_bindings

    @property
    def vhost(self):
        r"""Gets the vhost of this ShowQueueDetailsResponse.

        Queue所属Vhost名称

        :return: The vhost of this ShowQueueDetailsResponse.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        r"""Sets the vhost of this ShowQueueDetailsResponse.

        Queue所属Vhost名称

        :param vhost: The vhost of this ShowQueueDetailsResponse.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def name(self):
        r"""Gets the name of this ShowQueueDetailsResponse.

        Queue名称

        :return: The name of this ShowQueueDetailsResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowQueueDetailsResponse.

        Queue名称

        :param name: The name of this ShowQueueDetailsResponse.
        :type name: str
        """
        self._name = name

    @property
    def durable(self):
        r"""Gets the durable of this ShowQueueDetailsResponse.

        是否持久化

        :return: The durable of this ShowQueueDetailsResponse.
        :rtype: bool
        """
        return self._durable

    @durable.setter
    def durable(self, durable):
        r"""Sets the durable of this ShowQueueDetailsResponse.

        是否持久化

        :param durable: The durable of this ShowQueueDetailsResponse.
        :type durable: bool
        """
        self._durable = durable

    @property
    def auto_delete(self):
        r"""Gets the auto_delete of this ShowQueueDetailsResponse.

        是否自动删除

        :return: The auto_delete of this ShowQueueDetailsResponse.
        :rtype: bool
        """
        return self._auto_delete

    @auto_delete.setter
    def auto_delete(self, auto_delete):
        r"""Sets the auto_delete of this ShowQueueDetailsResponse.

        是否自动删除

        :param auto_delete: The auto_delete of this ShowQueueDetailsResponse.
        :type auto_delete: bool
        """
        self._auto_delete = auto_delete

    @property
    def messages(self):
        r"""Gets the messages of this ShowQueueDetailsResponse.

        待消费消息数

        :return: The messages of this ShowQueueDetailsResponse.
        :rtype: int
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        r"""Sets the messages of this ShowQueueDetailsResponse.

        待消费消息数

        :param messages: The messages of this ShowQueueDetailsResponse.
        :type messages: int
        """
        self._messages = messages

    @property
    def consumers(self):
        r"""Gets the consumers of this ShowQueueDetailsResponse.

        连接的消费者数

        :return: The consumers of this ShowQueueDetailsResponse.
        :rtype: int
        """
        return self._consumers

    @consumers.setter
    def consumers(self, consumers):
        r"""Sets the consumers of this ShowQueueDetailsResponse.

        连接的消费者数

        :param consumers: The consumers of this ShowQueueDetailsResponse.
        :type consumers: int
        """
        self._consumers = consumers

    @property
    def policy(self):
        r"""Gets the policy of this ShowQueueDetailsResponse.

        策略[（AMQP版本不支持policy，不涉及此参数）](tag:hws,hws_hk)

        :return: The policy of this ShowQueueDetailsResponse.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ShowQueueDetailsResponse.

        策略[（AMQP版本不支持policy，不涉及此参数）](tag:hws,hws_hk)

        :param policy: The policy of this ShowQueueDetailsResponse.
        :type policy: str
        """
        self._policy = policy

    @property
    def arguments(self):
        r"""Gets the arguments of this ShowQueueDetailsResponse.

        :return: The arguments of this ShowQueueDetailsResponse.
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.QueueArguments`
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        r"""Sets the arguments of this ShowQueueDetailsResponse.

        :param arguments: The arguments of this ShowQueueDetailsResponse.
        :type arguments: :class:`huaweicloudsdkrabbitmq.v2.QueueArguments`
        """
        self._arguments = arguments

    @property
    def consumer_details(self):
        r"""Gets the consumer_details of this ShowQueueDetailsResponse.

        订阅该Queue的消费者信息。

        :return: The consumer_details of this ShowQueueDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.ConsumerDetails`]
        """
        return self._consumer_details

    @consumer_details.setter
    def consumer_details(self, consumer_details):
        r"""Sets the consumer_details of this ShowQueueDetailsResponse.

        订阅该Queue的消费者信息。

        :param consumer_details: The consumer_details of this ShowQueueDetailsResponse.
        :type consumer_details: list[:class:`huaweicloudsdkrabbitmq.v2.ConsumerDetails`]
        """
        self._consumer_details = consumer_details

    @property
    def queue_bindings(self):
        r"""Gets the queue_bindings of this ShowQueueDetailsResponse.

        以此Queue为目标的绑定信息列表。

        :return: The queue_bindings of this ShowQueueDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkrabbitmq.v2.BindingsDetails`]
        """
        return self._queue_bindings

    @queue_bindings.setter
    def queue_bindings(self, queue_bindings):
        r"""Sets the queue_bindings of this ShowQueueDetailsResponse.

        以此Queue为目标的绑定信息列表。

        :param queue_bindings: The queue_bindings of this ShowQueueDetailsResponse.
        :type queue_bindings: list[:class:`huaweicloudsdkrabbitmq.v2.BindingsDetails`]
        """
        self._queue_bindings = queue_bindings

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
        if not isinstance(other, ShowQueueDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
