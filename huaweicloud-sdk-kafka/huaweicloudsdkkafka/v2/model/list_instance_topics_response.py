# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


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
        'count': 'int',
        'size': 'int',
        'topics': 'list[ListInstanceTopicsRespTopics]'
    }

    attribute_map = {
        'count': 'count',
        'size': 'size',
        'topics': 'topics'
    }

    def __init__(self, count=None, size=None, topics=None):
        """ListInstanceTopicsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._count = None
        self._size = None
        self._topics = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if size is not None:
            self.size = size
        if topics is not None:
            self.topics = topics

    @property
    def count(self):
        """Gets the count of this ListInstanceTopicsResponse.

        topic总数。

        :return: The count of this ListInstanceTopicsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListInstanceTopicsResponse.

        topic总数。

        :param count: The count of this ListInstanceTopicsResponse.
        :type: int
        """
        self._count = count

    @property
    def size(self):
        """Gets the size of this ListInstanceTopicsResponse.

        分页查询的大小。

        :return: The size of this ListInstanceTopicsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListInstanceTopicsResponse.

        分页查询的大小。

        :param size: The size of this ListInstanceTopicsResponse.
        :type: int
        """
        self._size = size

    @property
    def topics(self):
        """Gets the topics of this ListInstanceTopicsResponse.

        Topic列表。

        :return: The topics of this ListInstanceTopicsResponse.
        :rtype: list[ListInstanceTopicsRespTopics]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ListInstanceTopicsResponse.

        Topic列表。

        :param topics: The topics of this ListInstanceTopicsResponse.
        :type: list[ListInstanceTopicsRespTopics]
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
        if not isinstance(other, ListInstanceTopicsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
