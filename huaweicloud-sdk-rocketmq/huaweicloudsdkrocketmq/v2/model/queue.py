# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Queue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'lag': 'int',
        'broker_offset': 'int',
        'consumer_offset': 'int',
        'last_message_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'lag': 'lag',
        'broker_offset': 'broker_offset',
        'consumer_offset': 'consumer_offset',
        'last_message_time': 'last_message_time'
    }

    def __init__(self, id=None, lag=None, broker_offset=None, consumer_offset=None, last_message_time=None):
        r"""Queue

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 队列ID。 **取值范围**： 不涉及。
        :type id: int
        :param lag: **参数解释**： 队列消费堆积总数。 **取值范围**： 不涉及。
        :type lag: int
        :param broker_offset: **参数解释**： 队列消息总数。 **取值范围**： 不涉及。
        :type broker_offset: int
        :param consumer_offset: **参数解释**： 已消费消息数。 **取值范围**： 不涉及。
        :type consumer_offset: int
        :param last_message_time: **参数解释**： 最新消费消息的存储时间，Unix毫秒时间戳格式。 **取值范围**： 不涉及。
        :type last_message_time: int
        """
        
        

        self._id = None
        self._lag = None
        self._broker_offset = None
        self._consumer_offset = None
        self._last_message_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if lag is not None:
            self.lag = lag
        if broker_offset is not None:
            self.broker_offset = broker_offset
        if consumer_offset is not None:
            self.consumer_offset = consumer_offset
        if last_message_time is not None:
            self.last_message_time = last_message_time

    @property
    def id(self):
        r"""Gets the id of this Queue.

        **参数解释**： 队列ID。 **取值范围**： 不涉及。

        :return: The id of this Queue.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Queue.

        **参数解释**： 队列ID。 **取值范围**： 不涉及。

        :param id: The id of this Queue.
        :type id: int
        """
        self._id = id

    @property
    def lag(self):
        r"""Gets the lag of this Queue.

        **参数解释**： 队列消费堆积总数。 **取值范围**： 不涉及。

        :return: The lag of this Queue.
        :rtype: int
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        r"""Sets the lag of this Queue.

        **参数解释**： 队列消费堆积总数。 **取值范围**： 不涉及。

        :param lag: The lag of this Queue.
        :type lag: int
        """
        self._lag = lag

    @property
    def broker_offset(self):
        r"""Gets the broker_offset of this Queue.

        **参数解释**： 队列消息总数。 **取值范围**： 不涉及。

        :return: The broker_offset of this Queue.
        :rtype: int
        """
        return self._broker_offset

    @broker_offset.setter
    def broker_offset(self, broker_offset):
        r"""Sets the broker_offset of this Queue.

        **参数解释**： 队列消息总数。 **取值范围**： 不涉及。

        :param broker_offset: The broker_offset of this Queue.
        :type broker_offset: int
        """
        self._broker_offset = broker_offset

    @property
    def consumer_offset(self):
        r"""Gets the consumer_offset of this Queue.

        **参数解释**： 已消费消息数。 **取值范围**： 不涉及。

        :return: The consumer_offset of this Queue.
        :rtype: int
        """
        return self._consumer_offset

    @consumer_offset.setter
    def consumer_offset(self, consumer_offset):
        r"""Sets the consumer_offset of this Queue.

        **参数解释**： 已消费消息数。 **取值范围**： 不涉及。

        :param consumer_offset: The consumer_offset of this Queue.
        :type consumer_offset: int
        """
        self._consumer_offset = consumer_offset

    @property
    def last_message_time(self):
        r"""Gets the last_message_time of this Queue.

        **参数解释**： 最新消费消息的存储时间，Unix毫秒时间戳格式。 **取值范围**： 不涉及。

        :return: The last_message_time of this Queue.
        :rtype: int
        """
        return self._last_message_time

    @last_message_time.setter
    def last_message_time(self, last_message_time):
        r"""Sets the last_message_time of this Queue.

        **参数解释**： 最新消费消息的存储时间，Unix毫秒时间戳格式。 **取值范围**： 不涉及。

        :param last_message_time: The last_message_time of this Queue.
        :type last_message_time: int
        """
        self._last_message_time = last_message_time

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
        if not isinstance(other, Queue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
