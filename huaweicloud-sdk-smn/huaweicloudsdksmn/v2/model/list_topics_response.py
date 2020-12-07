# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListTopicsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'topic_count': 'int',
        'topics': 'list[ListTopicsItem]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'topic_count': 'topic_count',
        'topics': 'topics'
    }

    def __init__(self, request_id=None, topic_count=None, topics=None):
        """ListTopicsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._topic_count = None
        self._topics = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if topic_count is not None:
            self.topic_count = topic_count
        if topics is not None:
            self.topics = topics

    @property
    def request_id(self):
        """Gets the request_id of this ListTopicsResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListTopicsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListTopicsResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListTopicsResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def topic_count(self):
        """Gets the topic_count of this ListTopicsResponse.

        返回的Topic个数。该参数不受offset和limit影响，即返回的是您账户下所有的Topic个数。

        :return: The topic_count of this ListTopicsResponse.
        :rtype: int
        """
        return self._topic_count

    @topic_count.setter
    def topic_count(self, topic_count):
        """Sets the topic_count of this ListTopicsResponse.

        返回的Topic个数。该参数不受offset和limit影响，即返回的是您账户下所有的Topic个数。

        :param topic_count: The topic_count of this ListTopicsResponse.
        :type: int
        """
        self._topic_count = topic_count

    @property
    def topics(self):
        """Gets the topics of this ListTopicsResponse.

        Topic结构体数组。

        :return: The topics of this ListTopicsResponse.
        :rtype: list[ListTopicsItem]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ListTopicsResponse.

        Topic结构体数组。

        :param topics: The topics of this ListTopicsResponse.
        :type: list[ListTopicsItem]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListTopicsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
