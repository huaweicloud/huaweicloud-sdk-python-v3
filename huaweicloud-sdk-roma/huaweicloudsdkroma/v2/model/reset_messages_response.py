# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetMessagesResponse(SdkResponse):

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
        'consumer_key': 'str'
    }

    attribute_map = {
        'topic': 'topic',
        'partition': 'partition',
        'message_offset': 'message_offset',
        'consumer_key': 'consumer_key'
    }

    def __init__(self, topic=None, partition=None, message_offset=None, consumer_key=None):
        """ResetMessagesResponse

        The model defined in huaweicloud sdk

        :param topic: topic名称。
        :type topic: str
        :param partition: 分区。
        :type partition: int
        :param message_offset: 消息偏移量。
        :type message_offset: int
        :param consumer_key: 应用key。在该消息头中添加一个consumer_key的消息头。
        :type consumer_key: str
        """
        
        super(ResetMessagesResponse, self).__init__()

        self._topic = None
        self._partition = None
        self._message_offset = None
        self._consumer_key = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if partition is not None:
            self.partition = partition
        if message_offset is not None:
            self.message_offset = message_offset
        if consumer_key is not None:
            self.consumer_key = consumer_key

    @property
    def topic(self):
        """Gets the topic of this ResetMessagesResponse.

        topic名称。

        :return: The topic of this ResetMessagesResponse.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ResetMessagesResponse.

        topic名称。

        :param topic: The topic of this ResetMessagesResponse.
        :type topic: str
        """
        self._topic = topic

    @property
    def partition(self):
        """Gets the partition of this ResetMessagesResponse.

        分区。

        :return: The partition of this ResetMessagesResponse.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this ResetMessagesResponse.

        分区。

        :param partition: The partition of this ResetMessagesResponse.
        :type partition: int
        """
        self._partition = partition

    @property
    def message_offset(self):
        """Gets the message_offset of this ResetMessagesResponse.

        消息偏移量。

        :return: The message_offset of this ResetMessagesResponse.
        :rtype: int
        """
        return self._message_offset

    @message_offset.setter
    def message_offset(self, message_offset):
        """Sets the message_offset of this ResetMessagesResponse.

        消息偏移量。

        :param message_offset: The message_offset of this ResetMessagesResponse.
        :type message_offset: int
        """
        self._message_offset = message_offset

    @property
    def consumer_key(self):
        """Gets the consumer_key of this ResetMessagesResponse.

        应用key。在该消息头中添加一个consumer_key的消息头。

        :return: The consumer_key of this ResetMessagesResponse.
        :rtype: str
        """
        return self._consumer_key

    @consumer_key.setter
    def consumer_key(self, consumer_key):
        """Sets the consumer_key of this ResetMessagesResponse.

        应用key。在该消息头中添加一个consumer_key的消息头。

        :param consumer_key: The consumer_key of this ResetMessagesResponse.
        :type consumer_key: str
        """
        self._consumer_key = consumer_key

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
        if not isinstance(other, ResetMessagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
