# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRocketInstanceTopicsResponse(SdkResponse):

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
        'max': 'int',
        'remaining': 'int',
        'next_offset': 'int',
        'previous_offset': 'int',
        'topics': 'list[Topic]'
    }

    attribute_map = {
        'total': 'total',
        'max': 'max',
        'remaining': 'remaining',
        'next_offset': 'next_offset',
        'previous_offset': 'previous_offset',
        'topics': 'topics'
    }

    def __init__(self, total=None, max=None, remaining=None, next_offset=None, previous_offset=None, topics=None):
        """ListRocketInstanceTopicsResponse

        The model defined in huaweicloud sdk

        :param total: topic总数。
        :type total: int
        :param max: 最大可创建topic数量。
        :type max: int
        :param remaining: 剩余可创建topic数量。
        :type remaining: int
        :param next_offset: 下个分页的offset。
        :type next_offset: int
        :param previous_offset: 上个分页的offset。
        :type previous_offset: int
        :param topics: topic列表。
        :type topics: list[:class:`huaweicloudsdkrocketmq.v2.Topic`]
        """
        
        super(ListRocketInstanceTopicsResponse, self).__init__()

        self._total = None
        self._max = None
        self._remaining = None
        self._next_offset = None
        self._previous_offset = None
        self._topics = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if max is not None:
            self.max = max
        if remaining is not None:
            self.remaining = remaining
        if next_offset is not None:
            self.next_offset = next_offset
        if previous_offset is not None:
            self.previous_offset = previous_offset
        if topics is not None:
            self.topics = topics

    @property
    def total(self):
        """Gets the total of this ListRocketInstanceTopicsResponse.

        topic总数。

        :return: The total of this ListRocketInstanceTopicsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListRocketInstanceTopicsResponse.

        topic总数。

        :param total: The total of this ListRocketInstanceTopicsResponse.
        :type total: int
        """
        self._total = total

    @property
    def max(self):
        """Gets the max of this ListRocketInstanceTopicsResponse.

        最大可创建topic数量。

        :return: The max of this ListRocketInstanceTopicsResponse.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ListRocketInstanceTopicsResponse.

        最大可创建topic数量。

        :param max: The max of this ListRocketInstanceTopicsResponse.
        :type max: int
        """
        self._max = max

    @property
    def remaining(self):
        """Gets the remaining of this ListRocketInstanceTopicsResponse.

        剩余可创建topic数量。

        :return: The remaining of this ListRocketInstanceTopicsResponse.
        :rtype: int
        """
        return self._remaining

    @remaining.setter
    def remaining(self, remaining):
        """Sets the remaining of this ListRocketInstanceTopicsResponse.

        剩余可创建topic数量。

        :param remaining: The remaining of this ListRocketInstanceTopicsResponse.
        :type remaining: int
        """
        self._remaining = remaining

    @property
    def next_offset(self):
        """Gets the next_offset of this ListRocketInstanceTopicsResponse.

        下个分页的offset。

        :return: The next_offset of this ListRocketInstanceTopicsResponse.
        :rtype: int
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        """Sets the next_offset of this ListRocketInstanceTopicsResponse.

        下个分页的offset。

        :param next_offset: The next_offset of this ListRocketInstanceTopicsResponse.
        :type next_offset: int
        """
        self._next_offset = next_offset

    @property
    def previous_offset(self):
        """Gets the previous_offset of this ListRocketInstanceTopicsResponse.

        上个分页的offset。

        :return: The previous_offset of this ListRocketInstanceTopicsResponse.
        :rtype: int
        """
        return self._previous_offset

    @previous_offset.setter
    def previous_offset(self, previous_offset):
        """Sets the previous_offset of this ListRocketInstanceTopicsResponse.

        上个分页的offset。

        :param previous_offset: The previous_offset of this ListRocketInstanceTopicsResponse.
        :type previous_offset: int
        """
        self._previous_offset = previous_offset

    @property
    def topics(self):
        """Gets the topics of this ListRocketInstanceTopicsResponse.

        topic列表。

        :return: The topics of this ListRocketInstanceTopicsResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.Topic`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ListRocketInstanceTopicsResponse.

        topic列表。

        :param topics: The topics of this ListRocketInstanceTopicsResponse.
        :type topics: list[:class:`huaweicloudsdkrocketmq.v2.Topic`]
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
        if not isinstance(other, ListRocketInstanceTopicsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
