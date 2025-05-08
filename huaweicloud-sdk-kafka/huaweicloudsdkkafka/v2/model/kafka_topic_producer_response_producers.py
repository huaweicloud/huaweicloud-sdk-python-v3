# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaTopicProducerResponseProducers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'producer_address': 'str',
        'broker_address': 'str',
        'join_time': 'int'
    }

    attribute_map = {
        'producer_address': 'producer_address',
        'broker_address': 'broker_address',
        'join_time': 'join_time'
    }

    def __init__(self, producer_address=None, broker_address=None, join_time=None):
        r"""KafkaTopicProducerResponseProducers

        The model defined in huaweicloud sdk

        :param producer_address: **参数解释**： 生产者地址。 **取值范围**： 不涉及
        :type producer_address: str
        :param broker_address: **参数解释**： broker地址。 **取值范围**： 不涉及
        :type broker_address: str
        :param join_time: **参数解释**： 加入时间，以Unix时间戳显示。 **取值范围**： 不涉及
        :type join_time: int
        """
        
        

        self._producer_address = None
        self._broker_address = None
        self._join_time = None
        self.discriminator = None

        if producer_address is not None:
            self.producer_address = producer_address
        if broker_address is not None:
            self.broker_address = broker_address
        if join_time is not None:
            self.join_time = join_time

    @property
    def producer_address(self):
        r"""Gets the producer_address of this KafkaTopicProducerResponseProducers.

        **参数解释**： 生产者地址。 **取值范围**： 不涉及

        :return: The producer_address of this KafkaTopicProducerResponseProducers.
        :rtype: str
        """
        return self._producer_address

    @producer_address.setter
    def producer_address(self, producer_address):
        r"""Sets the producer_address of this KafkaTopicProducerResponseProducers.

        **参数解释**： 生产者地址。 **取值范围**： 不涉及

        :param producer_address: The producer_address of this KafkaTopicProducerResponseProducers.
        :type producer_address: str
        """
        self._producer_address = producer_address

    @property
    def broker_address(self):
        r"""Gets the broker_address of this KafkaTopicProducerResponseProducers.

        **参数解释**： broker地址。 **取值范围**： 不涉及

        :return: The broker_address of this KafkaTopicProducerResponseProducers.
        :rtype: str
        """
        return self._broker_address

    @broker_address.setter
    def broker_address(self, broker_address):
        r"""Sets the broker_address of this KafkaTopicProducerResponseProducers.

        **参数解释**： broker地址。 **取值范围**： 不涉及

        :param broker_address: The broker_address of this KafkaTopicProducerResponseProducers.
        :type broker_address: str
        """
        self._broker_address = broker_address

    @property
    def join_time(self):
        r"""Gets the join_time of this KafkaTopicProducerResponseProducers.

        **参数解释**： 加入时间，以Unix时间戳显示。 **取值范围**： 不涉及

        :return: The join_time of this KafkaTopicProducerResponseProducers.
        :rtype: int
        """
        return self._join_time

    @join_time.setter
    def join_time(self, join_time):
        r"""Sets the join_time of this KafkaTopicProducerResponseProducers.

        **参数解释**： 加入时间，以Unix时间戳显示。 **取值范围**： 不涉及

        :param join_time: The join_time of this KafkaTopicProducerResponseProducers.
        :type join_time: int
        """
        self._join_time = join_time

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
        if not isinstance(other, KafkaTopicProducerResponseProducers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
