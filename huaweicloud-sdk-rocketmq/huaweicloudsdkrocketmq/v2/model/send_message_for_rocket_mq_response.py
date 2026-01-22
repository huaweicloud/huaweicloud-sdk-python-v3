# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendMessageForRocketMqResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic': 'str',
        'body': 'str',
        'property_list': 'list[SendMessageProperties]',
        'msg_id': 'str',
        'queue_id': 'float',
        'queue_offset': 'float',
        'broker_name': 'str'
    }

    attribute_map = {
        'topic': 'topic',
        'body': 'body',
        'property_list': 'property_list',
        'msg_id': 'msg_id',
        'queue_id': 'queue_id',
        'queue_offset': 'queue_offset',
        'broker_name': 'broker_name'
    }

    def __init__(self, topic=None, body=None, property_list=None, msg_id=None, queue_id=None, queue_offset=None, broker_name=None):
        r"""SendMessageForRocketMqResponse

        The model defined in huaweicloud sdk

        :param topic: **参数解释**： 主题名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。
        :type topic: str
        :param body: **参数解释**： 消息内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。
        :type body: str
        :param property_list: **参数解释**： 特性列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。
        :type property_list: list[:class:`huaweicloudsdkrocketmq.v2.SendMessageProperties`]
        :param msg_id: **参数解释**： 消息ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。
        :type msg_id: str
        :param queue_id: **参数解释**： 队列ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。
        :type queue_id: float
        :param queue_offset: **参数解释**： 队列offset。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。
        :type queue_offset: float
        :param broker_name: **参数解释**： Broker名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。
        :type broker_name: str
        """
        
        super().__init__()

        self._topic = None
        self._body = None
        self._property_list = None
        self._msg_id = None
        self._queue_id = None
        self._queue_offset = None
        self._broker_name = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if body is not None:
            self.body = body
        if property_list is not None:
            self.property_list = property_list
        if msg_id is not None:
            self.msg_id = msg_id
        if queue_id is not None:
            self.queue_id = queue_id
        if queue_offset is not None:
            self.queue_offset = queue_offset
        if broker_name is not None:
            self.broker_name = broker_name

    @property
    def topic(self):
        r"""Gets the topic of this SendMessageForRocketMqResponse.

        **参数解释**： 主题名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :return: The topic of this SendMessageForRocketMqResponse.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this SendMessageForRocketMqResponse.

        **参数解释**： 主题名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :param topic: The topic of this SendMessageForRocketMqResponse.
        :type topic: str
        """
        self._topic = topic

    @property
    def body(self):
        r"""Gets the body of this SendMessageForRocketMqResponse.

        **参数解释**： 消息内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :return: The body of this SendMessageForRocketMqResponse.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this SendMessageForRocketMqResponse.

        **参数解释**： 消息内容。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :param body: The body of this SendMessageForRocketMqResponse.
        :type body: str
        """
        self._body = body

    @property
    def property_list(self):
        r"""Gets the property_list of this SendMessageForRocketMqResponse.

        **参数解释**： 特性列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :return: The property_list of this SendMessageForRocketMqResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.SendMessageProperties`]
        """
        return self._property_list

    @property_list.setter
    def property_list(self, property_list):
        r"""Sets the property_list of this SendMessageForRocketMqResponse.

        **参数解释**： 特性列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :param property_list: The property_list of this SendMessageForRocketMqResponse.
        :type property_list: list[:class:`huaweicloudsdkrocketmq.v2.SendMessageProperties`]
        """
        self._property_list = property_list

    @property
    def msg_id(self):
        r"""Gets the msg_id of this SendMessageForRocketMqResponse.

        **参数解释**： 消息ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :return: The msg_id of this SendMessageForRocketMqResponse.
        :rtype: str
        """
        return self._msg_id

    @msg_id.setter
    def msg_id(self, msg_id):
        r"""Sets the msg_id of this SendMessageForRocketMqResponse.

        **参数解释**： 消息ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :param msg_id: The msg_id of this SendMessageForRocketMqResponse.
        :type msg_id: str
        """
        self._msg_id = msg_id

    @property
    def queue_id(self):
        r"""Gets the queue_id of this SendMessageForRocketMqResponse.

        **参数解释**： 队列ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :return: The queue_id of this SendMessageForRocketMqResponse.
        :rtype: float
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        r"""Sets the queue_id of this SendMessageForRocketMqResponse.

        **参数解释**： 队列ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :param queue_id: The queue_id of this SendMessageForRocketMqResponse.
        :type queue_id: float
        """
        self._queue_id = queue_id

    @property
    def queue_offset(self):
        r"""Gets the queue_offset of this SendMessageForRocketMqResponse.

        **参数解释**： 队列offset。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :return: The queue_offset of this SendMessageForRocketMqResponse.
        :rtype: float
        """
        return self._queue_offset

    @queue_offset.setter
    def queue_offset(self, queue_offset):
        r"""Sets the queue_offset of this SendMessageForRocketMqResponse.

        **参数解释**： 队列offset。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :param queue_offset: The queue_offset of this SendMessageForRocketMqResponse.
        :type queue_offset: float
        """
        self._queue_offset = queue_offset

    @property
    def broker_name(self):
        r"""Gets the broker_name of this SendMessageForRocketMqResponse.

        **参数解释**： Broker名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :return: The broker_name of this SendMessageForRocketMqResponse.
        :rtype: str
        """
        return self._broker_name

    @broker_name.setter
    def broker_name(self, broker_name):
        r"""Sets the broker_name of this SendMessageForRocketMqResponse.

        **参数解释**： Broker名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值** 不涉及。

        :param broker_name: The broker_name of this SendMessageForRocketMqResponse.
        :type broker_name: str
        """
        self._broker_name = broker_name

    def to_dict(self):
        import warnings
        warnings.warn("SendMessageForRocketMqResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendMessageForRocketMqResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
