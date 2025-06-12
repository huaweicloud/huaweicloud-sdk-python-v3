# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceConsumerGroupTopicsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topics': 'list[GroupTopicEntity]',
        'total': 'int'
    }

    attribute_map = {
        'topics': 'topics',
        'total': 'total'
    }

    def __init__(self, topics=None, total=None):
        r"""ListInstanceConsumerGroupTopicsResponse

        The model defined in huaweicloud sdk

        :param topics: 消费组Topic
        :type topics: list[:class:`huaweicloudsdkkafka.v2.GroupTopicEntity`]
        :param total: 统计数量
        :type total: int
        """
        
        super(ListInstanceConsumerGroupTopicsResponse, self).__init__()

        self._topics = None
        self._total = None
        self.discriminator = None

        if topics is not None:
            self.topics = topics
        if total is not None:
            self.total = total

    @property
    def topics(self):
        r"""Gets the topics of this ListInstanceConsumerGroupTopicsResponse.

        消费组Topic

        :return: The topics of this ListInstanceConsumerGroupTopicsResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.GroupTopicEntity`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        r"""Sets the topics of this ListInstanceConsumerGroupTopicsResponse.

        消费组Topic

        :param topics: The topics of this ListInstanceConsumerGroupTopicsResponse.
        :type topics: list[:class:`huaweicloudsdkkafka.v2.GroupTopicEntity`]
        """
        self._topics = topics

    @property
    def total(self):
        r"""Gets the total of this ListInstanceConsumerGroupTopicsResponse.

        统计数量

        :return: The total of this ListInstanceConsumerGroupTopicsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceConsumerGroupTopicsResponse.

        统计数量

        :param total: The total of this ListInstanceConsumerGroupTopicsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListInstanceConsumerGroupTopicsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
