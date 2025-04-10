# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueueDetails:

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
        'arguments': 'QueueArguments'
    }

    attribute_map = {
        'vhost': 'vhost',
        'name': 'name',
        'durable': 'durable',
        'auto_delete': 'auto_delete',
        'messages': 'messages',
        'consumers': 'consumers',
        'policy': 'policy',
        'arguments': 'arguments'
    }

    def __init__(self, vhost=None, name=None, durable=None, auto_delete=None, messages=None, consumers=None, policy=None, arguments=None):
        r"""QueueDetails

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
        """
        
        

        self._vhost = None
        self._name = None
        self._durable = None
        self._auto_delete = None
        self._messages = None
        self._consumers = None
        self._policy = None
        self._arguments = None
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

    @property
    def vhost(self):
        r"""Gets the vhost of this QueueDetails.

        Queue所属Vhost名称

        :return: The vhost of this QueueDetails.
        :rtype: str
        """
        return self._vhost

    @vhost.setter
    def vhost(self, vhost):
        r"""Sets the vhost of this QueueDetails.

        Queue所属Vhost名称

        :param vhost: The vhost of this QueueDetails.
        :type vhost: str
        """
        self._vhost = vhost

    @property
    def name(self):
        r"""Gets the name of this QueueDetails.

        Queue名称

        :return: The name of this QueueDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueueDetails.

        Queue名称

        :param name: The name of this QueueDetails.
        :type name: str
        """
        self._name = name

    @property
    def durable(self):
        r"""Gets the durable of this QueueDetails.

        是否持久化

        :return: The durable of this QueueDetails.
        :rtype: bool
        """
        return self._durable

    @durable.setter
    def durable(self, durable):
        r"""Sets the durable of this QueueDetails.

        是否持久化

        :param durable: The durable of this QueueDetails.
        :type durable: bool
        """
        self._durable = durable

    @property
    def auto_delete(self):
        r"""Gets the auto_delete of this QueueDetails.

        是否自动删除

        :return: The auto_delete of this QueueDetails.
        :rtype: bool
        """
        return self._auto_delete

    @auto_delete.setter
    def auto_delete(self, auto_delete):
        r"""Sets the auto_delete of this QueueDetails.

        是否自动删除

        :param auto_delete: The auto_delete of this QueueDetails.
        :type auto_delete: bool
        """
        self._auto_delete = auto_delete

    @property
    def messages(self):
        r"""Gets the messages of this QueueDetails.

        待消费消息数

        :return: The messages of this QueueDetails.
        :rtype: int
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        r"""Sets the messages of this QueueDetails.

        待消费消息数

        :param messages: The messages of this QueueDetails.
        :type messages: int
        """
        self._messages = messages

    @property
    def consumers(self):
        r"""Gets the consumers of this QueueDetails.

        连接的消费者数

        :return: The consumers of this QueueDetails.
        :rtype: int
        """
        return self._consumers

    @consumers.setter
    def consumers(self, consumers):
        r"""Sets the consumers of this QueueDetails.

        连接的消费者数

        :param consumers: The consumers of this QueueDetails.
        :type consumers: int
        """
        self._consumers = consumers

    @property
    def policy(self):
        r"""Gets the policy of this QueueDetails.

        策略[（AMQP版本不支持policy，不涉及此参数）](tag:hws,hws_hk)

        :return: The policy of this QueueDetails.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this QueueDetails.

        策略[（AMQP版本不支持policy，不涉及此参数）](tag:hws,hws_hk)

        :param policy: The policy of this QueueDetails.
        :type policy: str
        """
        self._policy = policy

    @property
    def arguments(self):
        r"""Gets the arguments of this QueueDetails.

        :return: The arguments of this QueueDetails.
        :rtype: :class:`huaweicloudsdkrabbitmq.v2.QueueArguments`
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        r"""Sets the arguments of this QueueDetails.

        :param arguments: The arguments of this QueueDetails.
        :type arguments: :class:`huaweicloudsdkrabbitmq.v2.QueueArguments`
        """
        self._arguments = arguments

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
        if not isinstance(other, QueueDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
