# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaTopicQuota:

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
        'producer_byte_rate': 'int',
        'consumer_byte_rate': 'int'
    }

    attribute_map = {
        'topic': 'topic',
        'producer_byte_rate': 'producer-byte-rate',
        'consumer_byte_rate': 'consumer-byte-rate'
    }

    def __init__(self, topic=None, producer_byte_rate=None, consumer_byte_rate=None):
        r"""KafkaTopicQuota

        The model defined in huaweicloud sdk

        :param topic: Topic名称
        :type topic: str
        :param producer_byte_rate: 生产者速率
        :type producer_byte_rate: int
        :param consumer_byte_rate: 消费者速率
        :type consumer_byte_rate: int
        """
        
        

        self._topic = None
        self._producer_byte_rate = None
        self._consumer_byte_rate = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if producer_byte_rate is not None:
            self.producer_byte_rate = producer_byte_rate
        if consumer_byte_rate is not None:
            self.consumer_byte_rate = consumer_byte_rate

    @property
    def topic(self):
        r"""Gets the topic of this KafkaTopicQuota.

        Topic名称

        :return: The topic of this KafkaTopicQuota.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this KafkaTopicQuota.

        Topic名称

        :param topic: The topic of this KafkaTopicQuota.
        :type topic: str
        """
        self._topic = topic

    @property
    def producer_byte_rate(self):
        r"""Gets the producer_byte_rate of this KafkaTopicQuota.

        生产者速率

        :return: The producer_byte_rate of this KafkaTopicQuota.
        :rtype: int
        """
        return self._producer_byte_rate

    @producer_byte_rate.setter
    def producer_byte_rate(self, producer_byte_rate):
        r"""Sets the producer_byte_rate of this KafkaTopicQuota.

        生产者速率

        :param producer_byte_rate: The producer_byte_rate of this KafkaTopicQuota.
        :type producer_byte_rate: int
        """
        self._producer_byte_rate = producer_byte_rate

    @property
    def consumer_byte_rate(self):
        r"""Gets the consumer_byte_rate of this KafkaTopicQuota.

        消费者速率

        :return: The consumer_byte_rate of this KafkaTopicQuota.
        :rtype: int
        """
        return self._consumer_byte_rate

    @consumer_byte_rate.setter
    def consumer_byte_rate(self, consumer_byte_rate):
        r"""Sets the consumer_byte_rate of this KafkaTopicQuota.

        消费者速率

        :param consumer_byte_rate: The consumer_byte_rate of this KafkaTopicQuota.
        :type consumer_byte_rate: int
        """
        self._consumer_byte_rate = consumer_byte_rate

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
        if not isinstance(other, KafkaTopicQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
