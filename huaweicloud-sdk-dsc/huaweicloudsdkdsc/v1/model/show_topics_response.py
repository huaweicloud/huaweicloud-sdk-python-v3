# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopicsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default_topic_urn': 'str',
        'topic_count': 'int',
        'topics': 'list[TopicBean]'
    }

    attribute_map = {
        'default_topic_urn': 'default_topic_urn',
        'topic_count': 'topic_count',
        'topics': 'topics'
    }

    def __init__(self, default_topic_urn=None, topic_count=None, topics=None):
        """ShowTopicsResponse

        The model defined in huaweicloud sdk

        :param default_topic_urn: 默认消息通知主题的唯一资源标识符
        :type default_topic_urn: str
        :param topic_count: 已确认的消息通知主题数量
        :type topic_count: int
        :param topics: 已确认的消息通知主题列表
        :type topics: list[:class:`huaweicloudsdkdsc.v1.TopicBean`]
        """
        
        super(ShowTopicsResponse, self).__init__()

        self._default_topic_urn = None
        self._topic_count = None
        self._topics = None
        self.discriminator = None

        if default_topic_urn is not None:
            self.default_topic_urn = default_topic_urn
        if topic_count is not None:
            self.topic_count = topic_count
        if topics is not None:
            self.topics = topics

    @property
    def default_topic_urn(self):
        """Gets the default_topic_urn of this ShowTopicsResponse.

        默认消息通知主题的唯一资源标识符

        :return: The default_topic_urn of this ShowTopicsResponse.
        :rtype: str
        """
        return self._default_topic_urn

    @default_topic_urn.setter
    def default_topic_urn(self, default_topic_urn):
        """Sets the default_topic_urn of this ShowTopicsResponse.

        默认消息通知主题的唯一资源标识符

        :param default_topic_urn: The default_topic_urn of this ShowTopicsResponse.
        :type default_topic_urn: str
        """
        self._default_topic_urn = default_topic_urn

    @property
    def topic_count(self):
        """Gets the topic_count of this ShowTopicsResponse.

        已确认的消息通知主题数量

        :return: The topic_count of this ShowTopicsResponse.
        :rtype: int
        """
        return self._topic_count

    @topic_count.setter
    def topic_count(self, topic_count):
        """Sets the topic_count of this ShowTopicsResponse.

        已确认的消息通知主题数量

        :param topic_count: The topic_count of this ShowTopicsResponse.
        :type topic_count: int
        """
        self._topic_count = topic_count

    @property
    def topics(self):
        """Gets the topics of this ShowTopicsResponse.

        已确认的消息通知主题列表

        :return: The topics of this ShowTopicsResponse.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.TopicBean`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ShowTopicsResponse.

        已确认的消息通知主题列表

        :param topics: The topics of this ShowTopicsResponse.
        :type topics: list[:class:`huaweicloudsdkdsc.v1.TopicBean`]
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
        if not isinstance(other, ShowTopicsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
