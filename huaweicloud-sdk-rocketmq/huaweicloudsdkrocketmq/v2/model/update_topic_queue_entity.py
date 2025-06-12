# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTopicQueueEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'broker': 'str',
        'read_queue_num': 'float',
        'write_queue_num': 'float'
    }

    attribute_map = {
        'broker': 'broker',
        'read_queue_num': 'read_queue_num',
        'write_queue_num': 'write_queue_num'
    }

    def __init__(self, broker=None, read_queue_num=None, write_queue_num=None):
        r"""UpdateTopicQueueEntity

        The model defined in huaweicloud sdk

        :param broker: **参数解释**： Broker名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type broker: str
        :param read_queue_num: **参数解释**： 读队列个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type read_queue_num: float
        :param write_queue_num: **参数解释**： 写队列个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type write_queue_num: float
        """
        
        

        self._broker = None
        self._read_queue_num = None
        self._write_queue_num = None
        self.discriminator = None

        if broker is not None:
            self.broker = broker
        if read_queue_num is not None:
            self.read_queue_num = read_queue_num
        if write_queue_num is not None:
            self.write_queue_num = write_queue_num

    @property
    def broker(self):
        r"""Gets the broker of this UpdateTopicQueueEntity.

        **参数解释**： Broker名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The broker of this UpdateTopicQueueEntity.
        :rtype: str
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        r"""Sets the broker of this UpdateTopicQueueEntity.

        **参数解释**： Broker名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param broker: The broker of this UpdateTopicQueueEntity.
        :type broker: str
        """
        self._broker = broker

    @property
    def read_queue_num(self):
        r"""Gets the read_queue_num of this UpdateTopicQueueEntity.

        **参数解释**： 读队列个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The read_queue_num of this UpdateTopicQueueEntity.
        :rtype: float
        """
        return self._read_queue_num

    @read_queue_num.setter
    def read_queue_num(self, read_queue_num):
        r"""Sets the read_queue_num of this UpdateTopicQueueEntity.

        **参数解释**： 读队列个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param read_queue_num: The read_queue_num of this UpdateTopicQueueEntity.
        :type read_queue_num: float
        """
        self._read_queue_num = read_queue_num

    @property
    def write_queue_num(self):
        r"""Gets the write_queue_num of this UpdateTopicQueueEntity.

        **参数解释**： 写队列个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The write_queue_num of this UpdateTopicQueueEntity.
        :rtype: float
        """
        return self._write_queue_num

    @write_queue_num.setter
    def write_queue_num(self, write_queue_num):
        r"""Sets the write_queue_num of this UpdateTopicQueueEntity.

        **参数解释**： 写队列个数。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param write_queue_num: The write_queue_num of this UpdateTopicQueueEntity.
        :type write_queue_num: float
        """
        self._write_queue_num = write_queue_num

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
        if not isinstance(other, UpdateTopicQueueEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
