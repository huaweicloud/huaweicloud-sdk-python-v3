# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceConsumerGroupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'float',
        'groups': 'list[ConsumerGroup]',
        'max': 'float',
        'remaining': 'float',
        'next_offset': 'float',
        'previous_offset': 'float'
    }

    attribute_map = {
        'total': 'total',
        'groups': 'groups',
        'max': 'max',
        'remaining': 'remaining',
        'next_offset': 'next_offset',
        'previous_offset': 'previous_offset'
    }

    def __init__(self, total=None, groups=None, max=None, remaining=None, next_offset=None, previous_offset=None):
        """ListInstanceConsumerGroupsResponse

        The model defined in huaweicloud sdk

        :param total: 消费组总数。
        :type total: float
        :param groups: 消费组列表。
        :type groups: list[:class:`huaweicloudsdkrocketmq.v2.ConsumerGroup`]
        :param max: 最大可创建消费组数量。
        :type max: float
        :param remaining: 剩余可创建消费组数量。
        :type remaining: float
        :param next_offset: 下个分页的offset。
        :type next_offset: float
        :param previous_offset: 上个分页的offset。
        :type previous_offset: float
        """
        
        super(ListInstanceConsumerGroupsResponse, self).__init__()

        self._total = None
        self._groups = None
        self._max = None
        self._remaining = None
        self._next_offset = None
        self._previous_offset = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if groups is not None:
            self.groups = groups
        if max is not None:
            self.max = max
        if remaining is not None:
            self.remaining = remaining
        if next_offset is not None:
            self.next_offset = next_offset
        if previous_offset is not None:
            self.previous_offset = previous_offset

    @property
    def total(self):
        """Gets the total of this ListInstanceConsumerGroupsResponse.

        消费组总数。

        :return: The total of this ListInstanceConsumerGroupsResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListInstanceConsumerGroupsResponse.

        消费组总数。

        :param total: The total of this ListInstanceConsumerGroupsResponse.
        :type total: float
        """
        self._total = total

    @property
    def groups(self):
        """Gets the groups of this ListInstanceConsumerGroupsResponse.

        消费组列表。

        :return: The groups of this ListInstanceConsumerGroupsResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ConsumerGroup`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ListInstanceConsumerGroupsResponse.

        消费组列表。

        :param groups: The groups of this ListInstanceConsumerGroupsResponse.
        :type groups: list[:class:`huaweicloudsdkrocketmq.v2.ConsumerGroup`]
        """
        self._groups = groups

    @property
    def max(self):
        """Gets the max of this ListInstanceConsumerGroupsResponse.

        最大可创建消费组数量。

        :return: The max of this ListInstanceConsumerGroupsResponse.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ListInstanceConsumerGroupsResponse.

        最大可创建消费组数量。

        :param max: The max of this ListInstanceConsumerGroupsResponse.
        :type max: float
        """
        self._max = max

    @property
    def remaining(self):
        """Gets the remaining of this ListInstanceConsumerGroupsResponse.

        剩余可创建消费组数量。

        :return: The remaining of this ListInstanceConsumerGroupsResponse.
        :rtype: float
        """
        return self._remaining

    @remaining.setter
    def remaining(self, remaining):
        """Sets the remaining of this ListInstanceConsumerGroupsResponse.

        剩余可创建消费组数量。

        :param remaining: The remaining of this ListInstanceConsumerGroupsResponse.
        :type remaining: float
        """
        self._remaining = remaining

    @property
    def next_offset(self):
        """Gets the next_offset of this ListInstanceConsumerGroupsResponse.

        下个分页的offset。

        :return: The next_offset of this ListInstanceConsumerGroupsResponse.
        :rtype: float
        """
        return self._next_offset

    @next_offset.setter
    def next_offset(self, next_offset):
        """Sets the next_offset of this ListInstanceConsumerGroupsResponse.

        下个分页的offset。

        :param next_offset: The next_offset of this ListInstanceConsumerGroupsResponse.
        :type next_offset: float
        """
        self._next_offset = next_offset

    @property
    def previous_offset(self):
        """Gets the previous_offset of this ListInstanceConsumerGroupsResponse.

        上个分页的offset。

        :return: The previous_offset of this ListInstanceConsumerGroupsResponse.
        :rtype: float
        """
        return self._previous_offset

    @previous_offset.setter
    def previous_offset(self, previous_offset):
        """Sets the previous_offset of this ListInstanceConsumerGroupsResponse.

        上个分页的offset。

        :param previous_offset: The previous_offset of this ListInstanceConsumerGroupsResponse.
        :type previous_offset: float
        """
        self._previous_offset = previous_offset

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
        if not isinstance(other, ListInstanceConsumerGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
