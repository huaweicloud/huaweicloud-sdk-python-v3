# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConsumerListOrDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topics': 'list[str]',
        'total': 'int',
        'lag': 'int',
        'max_offset': 'int',
        'consumer_offset': 'int',
        'brokers': 'list[Brokers]'
    }

    attribute_map = {
        'topics': 'topics',
        'total': 'total',
        'lag': 'lag',
        'max_offset': 'max_offset',
        'consumer_offset': 'consumer_offset',
        'brokers': 'brokers'
    }

    def __init__(self, topics=None, total=None, lag=None, max_offset=None, consumer_offset=None, brokers=None):
        r"""ShowConsumerListOrDetailsResponse

        The model defined in huaweicloud sdk

        :param topics: **参数解释**： Topic列表（当查询Topic消费“列表”时才显示此参数）。
        :type topics: list[str]
        :param total: **参数解释**： Topic总数（当查询Topic消费“列表”时才显示此参数）。 **取值范围**： 不涉及。
        :type total: int
        :param lag: **参数解释**： 消费堆积总数。 **取值范围**： 不涉及。
        :type lag: int
        :param max_offset: **参数解释**： 消息总数。 **取值范围**： 不涉及。
        :type max_offset: int
        :param consumer_offset: **参数解释**： 已消费消息数。 **取值范围**： 不涉及。
        :type consumer_offset: int
        :param brokers: **参数解释**： Topic关联代理（当查询Topic消费“详情”才显示此参数）。
        :type brokers: list[:class:`huaweicloudsdkrocketmq.v2.Brokers`]
        """
        
        super(ShowConsumerListOrDetailsResponse, self).__init__()

        self._topics = None
        self._total = None
        self._lag = None
        self._max_offset = None
        self._consumer_offset = None
        self._brokers = None
        self.discriminator = None

        if topics is not None:
            self.topics = topics
        if total is not None:
            self.total = total
        if lag is not None:
            self.lag = lag
        if max_offset is not None:
            self.max_offset = max_offset
        if consumer_offset is not None:
            self.consumer_offset = consumer_offset
        if brokers is not None:
            self.brokers = brokers

    @property
    def topics(self):
        r"""Gets the topics of this ShowConsumerListOrDetailsResponse.

        **参数解释**： Topic列表（当查询Topic消费“列表”时才显示此参数）。

        :return: The topics of this ShowConsumerListOrDetailsResponse.
        :rtype: list[str]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this ShowConsumerListOrDetailsResponse.

        **参数解释**： Topic列表（当查询Topic消费“列表”时才显示此参数）。

        :param topics: The topics of this ShowConsumerListOrDetailsResponse.
        :type topics: list[str]
        """
        self._topics = topics

    @property
    def total(self):
        r"""Gets the total of this ShowConsumerListOrDetailsResponse.

        **参数解释**： Topic总数（当查询Topic消费“列表”时才显示此参数）。 **取值范围**： 不涉及。

        :return: The total of this ShowConsumerListOrDetailsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowConsumerListOrDetailsResponse.

        **参数解释**： Topic总数（当查询Topic消费“列表”时才显示此参数）。 **取值范围**： 不涉及。

        :param total: The total of this ShowConsumerListOrDetailsResponse.
        :type total: int
        """
        self._total = total

    @property
    def lag(self):
        r"""Gets the lag of this ShowConsumerListOrDetailsResponse.

        **参数解释**： 消费堆积总数。 **取值范围**： 不涉及。

        :return: The lag of this ShowConsumerListOrDetailsResponse.
        :rtype: int
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        r"""Sets the lag of this ShowConsumerListOrDetailsResponse.

        **参数解释**： 消费堆积总数。 **取值范围**： 不涉及。

        :param lag: The lag of this ShowConsumerListOrDetailsResponse.
        :type lag: int
        """
        self._lag = lag

    @property
    def max_offset(self):
        r"""Gets the max_offset of this ShowConsumerListOrDetailsResponse.

        **参数解释**： 消息总数。 **取值范围**： 不涉及。

        :return: The max_offset of this ShowConsumerListOrDetailsResponse.
        :rtype: int
        """
        return self._max_offset

    @max_offset.setter
    def max_offset(self, max_offset):
        r"""Sets the max_offset of this ShowConsumerListOrDetailsResponse.

        **参数解释**： 消息总数。 **取值范围**： 不涉及。

        :param max_offset: The max_offset of this ShowConsumerListOrDetailsResponse.
        :type max_offset: int
        """
        self._max_offset = max_offset

    @property
    def consumer_offset(self):
        r"""Gets the consumer_offset of this ShowConsumerListOrDetailsResponse.

        **参数解释**： 已消费消息数。 **取值范围**： 不涉及。

        :return: The consumer_offset of this ShowConsumerListOrDetailsResponse.
        :rtype: int
        """
        return self._consumer_offset

    @consumer_offset.setter
    def consumer_offset(self, consumer_offset):
        r"""Sets the consumer_offset of this ShowConsumerListOrDetailsResponse.

        **参数解释**： 已消费消息数。 **取值范围**： 不涉及。

        :param consumer_offset: The consumer_offset of this ShowConsumerListOrDetailsResponse.
        :type consumer_offset: int
        """
        self._consumer_offset = consumer_offset

    @property
    def brokers(self):
        r"""Gets the brokers of this ShowConsumerListOrDetailsResponse.

        **参数解释**： Topic关联代理（当查询Topic消费“详情”才显示此参数）。

        :return: The brokers of this ShowConsumerListOrDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.Brokers`]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        r"""Sets the brokers of this ShowConsumerListOrDetailsResponse.

        **参数解释**： Topic关联代理（当查询Topic消费“详情”才显示此参数）。

        :param brokers: The brokers of this ShowConsumerListOrDetailsResponse.
        :type brokers: list[:class:`huaweicloudsdkrocketmq.v2.Brokers`]
        """
        self._brokers = brokers

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
        if not isinstance(other, ShowConsumerListOrDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
