# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMessagesRespMessages:

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
        'partition': 'int',
        'message_offset': 'int',
        'size': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'topic': 'topic',
        'partition': 'partition',
        'message_offset': 'message_offset',
        'size': 'size',
        'timestamp': 'timestamp'
    }

    def __init__(self, topic=None, partition=None, message_offset=None, size=None, timestamp=None):
        r"""ShowMessagesRespMessages

        The model defined in huaweicloud sdk

        :param topic: **参数解释**： Topic名称。 **取值范围**： 不涉及。
        :type topic: str
        :param partition: **参数解释**： 分区编号。 **取值范围**： 不涉及。
        :type partition: int
        :param message_offset: **参数解释**： 消息编号。 **取值范围**： 不涉及。
        :type message_offset: int
        :param size: **参数解释**： 消息大小，单位字节。 **取值范围**： 不涉及。
        :type size: int
        :param timestamp: **参数解释**： 生产消息的时间。 格式为Unix时间戳。单位为毫秒。 **取值范围**： 不涉及。
        :type timestamp: int
        """
        
        

        self._topic = None
        self._partition = None
        self._message_offset = None
        self._size = None
        self._timestamp = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if partition is not None:
            self.partition = partition
        if message_offset is not None:
            self.message_offset = message_offset
        if size is not None:
            self.size = size
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def topic(self):
        r"""Gets the topic of this ShowMessagesRespMessages.

        **参数解释**： Topic名称。 **取值范围**： 不涉及。

        :return: The topic of this ShowMessagesRespMessages.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this ShowMessagesRespMessages.

        **参数解释**： Topic名称。 **取值范围**： 不涉及。

        :param topic: The topic of this ShowMessagesRespMessages.
        :type topic: str
        """
        self._topic = topic

    @property
    def partition(self):
        r"""Gets the partition of this ShowMessagesRespMessages.

        **参数解释**： 分区编号。 **取值范围**： 不涉及。

        :return: The partition of this ShowMessagesRespMessages.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this ShowMessagesRespMessages.

        **参数解释**： 分区编号。 **取值范围**： 不涉及。

        :param partition: The partition of this ShowMessagesRespMessages.
        :type partition: int
        """
        self._partition = partition

    @property
    def message_offset(self):
        r"""Gets the message_offset of this ShowMessagesRespMessages.

        **参数解释**： 消息编号。 **取值范围**： 不涉及。

        :return: The message_offset of this ShowMessagesRespMessages.
        :rtype: int
        """
        return self._message_offset

    @message_offset.setter
    def message_offset(self, message_offset):
        r"""Sets the message_offset of this ShowMessagesRespMessages.

        **参数解释**： 消息编号。 **取值范围**： 不涉及。

        :param message_offset: The message_offset of this ShowMessagesRespMessages.
        :type message_offset: int
        """
        self._message_offset = message_offset

    @property
    def size(self):
        r"""Gets the size of this ShowMessagesRespMessages.

        **参数解释**： 消息大小，单位字节。 **取值范围**： 不涉及。

        :return: The size of this ShowMessagesRespMessages.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowMessagesRespMessages.

        **参数解释**： 消息大小，单位字节。 **取值范围**： 不涉及。

        :param size: The size of this ShowMessagesRespMessages.
        :type size: int
        """
        self._size = size

    @property
    def timestamp(self):
        r"""Gets the timestamp of this ShowMessagesRespMessages.

        **参数解释**： 生产消息的时间。 格式为Unix时间戳。单位为毫秒。 **取值范围**： 不涉及。

        :return: The timestamp of this ShowMessagesRespMessages.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this ShowMessagesRespMessages.

        **参数解释**： 生产消息的时间。 格式为Unix时间戳。单位为毫秒。 **取值范围**： 不涉及。

        :param timestamp: The timestamp of this ShowMessagesRespMessages.
        :type timestamp: int
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
        if not isinstance(other, ShowMessagesRespMessages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
