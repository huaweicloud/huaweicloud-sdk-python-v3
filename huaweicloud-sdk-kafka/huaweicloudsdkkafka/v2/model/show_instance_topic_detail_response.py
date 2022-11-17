# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceTopicDetailResponse(SdkResponse):

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
        'partitions': 'list[ShowInstanceTopicDetailRespPartitions]',
        'group_subscribed': 'list[str]'
    }

    attribute_map = {
        'topic': 'topic',
        'partitions': 'partitions',
        'group_subscribed': 'group_subscribed'
    }

    def __init__(self, topic=None, partitions=None, group_subscribed=None):
        """ShowInstanceTopicDetailResponse

        The model defined in huaweicloud sdk

        :param topic: topic名称。
        :type topic: str
        :param partitions: 分区列表。
        :type partitions: list[:class:`huaweicloudsdkkafka.v2.ShowInstanceTopicDetailRespPartitions`]
        :param group_subscribed: 订阅该topic的消费组名称列表。
        :type group_subscribed: list[str]
        """
        
        super(ShowInstanceTopicDetailResponse, self).__init__()

        self._topic = None
        self._partitions = None
        self._group_subscribed = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if partitions is not None:
            self.partitions = partitions
        if group_subscribed is not None:
            self.group_subscribed = group_subscribed

    @property
    def topic(self):
        """Gets the topic of this ShowInstanceTopicDetailResponse.

        topic名称。

        :return: The topic of this ShowInstanceTopicDetailResponse.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowInstanceTopicDetailResponse.

        topic名称。

        :param topic: The topic of this ShowInstanceTopicDetailResponse.
        :type topic: str
        """
        self._topic = topic

    @property
    def partitions(self):
        """Gets the partitions of this ShowInstanceTopicDetailResponse.

        分区列表。

        :return: The partitions of this ShowInstanceTopicDetailResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowInstanceTopicDetailRespPartitions`]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this ShowInstanceTopicDetailResponse.

        分区列表。

        :param partitions: The partitions of this ShowInstanceTopicDetailResponse.
        :type partitions: list[:class:`huaweicloudsdkkafka.v2.ShowInstanceTopicDetailRespPartitions`]
        """
        self._partitions = partitions

    @property
    def group_subscribed(self):
        """Gets the group_subscribed of this ShowInstanceTopicDetailResponse.

        订阅该topic的消费组名称列表。

        :return: The group_subscribed of this ShowInstanceTopicDetailResponse.
        :rtype: list[str]
        """
        return self._group_subscribed

    @group_subscribed.setter
    def group_subscribed(self, group_subscribed):
        """Sets the group_subscribed of this ShowInstanceTopicDetailResponse.

        订阅该topic的消费组名称列表。

        :param group_subscribed: The group_subscribed of this ShowInstanceTopicDetailResponse.
        :type group_subscribed: list[str]
        """
        self._group_subscribed = group_subscribed

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
        if not isinstance(other, ShowInstanceTopicDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
