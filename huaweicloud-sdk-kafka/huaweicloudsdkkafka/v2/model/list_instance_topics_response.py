# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceTopicsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'size': 'int',
        'remain_partitions': 'int',
        'max_partitions': 'int',
        'topic_max_partitions': 'int',
        'topics': 'list[TopicEntity]'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'remain_partitions': 'remain_partitions',
        'max_partitions': 'max_partitions',
        'topic_max_partitions': 'topic_max_partitions',
        'topics': 'topics'
    }

    def __init__(self, total=None, size=None, remain_partitions=None, max_partitions=None, topic_max_partitions=None, topics=None):
        r"""ListInstanceTopicsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**： Topic总数。 **取值范围**： 不涉及。
        :type total: int
        :param size: **参数解释**： 分页查询的大小。 **取值范围**： 不涉及。
        :type size: int
        :param remain_partitions: **参数解释**： 剩余分区数。 **取值范围**： 不涉及。
        :type remain_partitions: int
        :param max_partitions: **参数解释**： 分区总数。 **取值范围**： 不涉及。
        :type max_partitions: int
        :param topic_max_partitions: **参数解释**： 单个Topic最大占用分区数。 **取值范围**： 不涉及。
        :type topic_max_partitions: int
        :param topics: **参数解释**： Topic列表。
        :type topics: list[:class:`huaweicloudsdkkafka.v2.TopicEntity`]
        """
        
        super(ListInstanceTopicsResponse, self).__init__()

        self._total = None
        self._size = None
        self._remain_partitions = None
        self._max_partitions = None
        self._topic_max_partitions = None
        self._topics = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if remain_partitions is not None:
            self.remain_partitions = remain_partitions
        if max_partitions is not None:
            self.max_partitions = max_partitions
        if topic_max_partitions is not None:
            self.topic_max_partitions = topic_max_partitions
        if topics is not None:
            self.topics = topics

    @property
    def total(self):
        r"""Gets the total of this ListInstanceTopicsResponse.

        **参数解释**： Topic总数。 **取值范围**： 不涉及。

        :return: The total of this ListInstanceTopicsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceTopicsResponse.

        **参数解释**： Topic总数。 **取值范围**： 不涉及。

        :param total: The total of this ListInstanceTopicsResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        r"""Gets the size of this ListInstanceTopicsResponse.

        **参数解释**： 分页查询的大小。 **取值范围**： 不涉及。

        :return: The size of this ListInstanceTopicsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListInstanceTopicsResponse.

        **参数解释**： 分页查询的大小。 **取值范围**： 不涉及。

        :param size: The size of this ListInstanceTopicsResponse.
        :type size: int
        """
        self._size = size

    @property
    def remain_partitions(self):
        r"""Gets the remain_partitions of this ListInstanceTopicsResponse.

        **参数解释**： 剩余分区数。 **取值范围**： 不涉及。

        :return: The remain_partitions of this ListInstanceTopicsResponse.
        :rtype: int
        """
        return self._remain_partitions

    @remain_partitions.setter
    def remain_partitions(self, remain_partitions):
        r"""Sets the remain_partitions of this ListInstanceTopicsResponse.

        **参数解释**： 剩余分区数。 **取值范围**： 不涉及。

        :param remain_partitions: The remain_partitions of this ListInstanceTopicsResponse.
        :type remain_partitions: int
        """
        self._remain_partitions = remain_partitions

    @property
    def max_partitions(self):
        r"""Gets the max_partitions of this ListInstanceTopicsResponse.

        **参数解释**： 分区总数。 **取值范围**： 不涉及。

        :return: The max_partitions of this ListInstanceTopicsResponse.
        :rtype: int
        """
        return self._max_partitions

    @max_partitions.setter
    def max_partitions(self, max_partitions):
        r"""Sets the max_partitions of this ListInstanceTopicsResponse.

        **参数解释**： 分区总数。 **取值范围**： 不涉及。

        :param max_partitions: The max_partitions of this ListInstanceTopicsResponse.
        :type max_partitions: int
        """
        self._max_partitions = max_partitions

    @property
    def topic_max_partitions(self):
        r"""Gets the topic_max_partitions of this ListInstanceTopicsResponse.

        **参数解释**： 单个Topic最大占用分区数。 **取值范围**： 不涉及。

        :return: The topic_max_partitions of this ListInstanceTopicsResponse.
        :rtype: int
        """
        return self._topic_max_partitions

    @topic_max_partitions.setter
    def topic_max_partitions(self, topic_max_partitions):
        r"""Sets the topic_max_partitions of this ListInstanceTopicsResponse.

        **参数解释**： 单个Topic最大占用分区数。 **取值范围**： 不涉及。

        :param topic_max_partitions: The topic_max_partitions of this ListInstanceTopicsResponse.
        :type topic_max_partitions: int
        """
        self._topic_max_partitions = topic_max_partitions

    @property
    def topics(self):
        r"""Gets the topics of this ListInstanceTopicsResponse.

        **参数解释**： Topic列表。

        :return: The topics of this ListInstanceTopicsResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.TopicEntity`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this ListInstanceTopicsResponse.

        **参数解释**： Topic列表。

        :param topics: The topics of this ListInstanceTopicsResponse.
        :type topics: list[:class:`huaweicloudsdkkafka.v2.TopicEntity`]
        """
        self._topics = topics

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
        if not isinstance(other, ListInstanceTopicsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
