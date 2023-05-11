# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMqsInstanceTopicsResponse(SdkResponse):

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
        'permissions': 'list[str]',
        'topics': 'list[ListInstanceTopicsRespTopics]',
        'remain_partitions': 'int',
        'max_partitions': 'int'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'permissions': 'permissions',
        'topics': 'topics',
        'remain_partitions': 'remain_partitions',
        'max_partitions': 'max_partitions'
    }

    def __init__(self, total=None, size=None, permissions=None, topics=None, remain_partitions=None, max_partitions=None):
        """ListMqsInstanceTopicsResponse

        The model defined in huaweicloud sdk

        :param total: topic的总数。
        :type total: int
        :param size: 当前查询的topic数量。
        :type size: int
        :param permissions: 允许操作的权限。
        :type permissions: list[str]
        :param topics: Topic列表。
        :type topics: list[:class:`huaweicloudsdkroma.v2.ListInstanceTopicsRespTopics`]
        :param remain_partitions: 剩余分区数。
        :type remain_partitions: int
        :param max_partitions: 分区总数。
        :type max_partitions: int
        """
        
        super(ListMqsInstanceTopicsResponse, self).__init__()

        self._total = None
        self._size = None
        self._permissions = None
        self._topics = None
        self._remain_partitions = None
        self._max_partitions = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if permissions is not None:
            self.permissions = permissions
        if topics is not None:
            self.topics = topics
        if remain_partitions is not None:
            self.remain_partitions = remain_partitions
        if max_partitions is not None:
            self.max_partitions = max_partitions

    @property
    def total(self):
        """Gets the total of this ListMqsInstanceTopicsResponse.

        topic的总数。

        :return: The total of this ListMqsInstanceTopicsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListMqsInstanceTopicsResponse.

        topic的总数。

        :param total: The total of this ListMqsInstanceTopicsResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        """Gets the size of this ListMqsInstanceTopicsResponse.

        当前查询的topic数量。

        :return: The size of this ListMqsInstanceTopicsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListMqsInstanceTopicsResponse.

        当前查询的topic数量。

        :param size: The size of this ListMqsInstanceTopicsResponse.
        :type size: int
        """
        self._size = size

    @property
    def permissions(self):
        """Gets the permissions of this ListMqsInstanceTopicsResponse.

        允许操作的权限。

        :return: The permissions of this ListMqsInstanceTopicsResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ListMqsInstanceTopicsResponse.

        允许操作的权限。

        :param permissions: The permissions of this ListMqsInstanceTopicsResponse.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def topics(self):
        """Gets the topics of this ListMqsInstanceTopicsResponse.

        Topic列表。

        :return: The topics of this ListMqsInstanceTopicsResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.ListInstanceTopicsRespTopics`]
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ListMqsInstanceTopicsResponse.

        Topic列表。

        :param topics: The topics of this ListMqsInstanceTopicsResponse.
        :type topics: list[:class:`huaweicloudsdkroma.v2.ListInstanceTopicsRespTopics`]
        """
        self._topics = topics

    @property
    def remain_partitions(self):
        """Gets the remain_partitions of this ListMqsInstanceTopicsResponse.

        剩余分区数。

        :return: The remain_partitions of this ListMqsInstanceTopicsResponse.
        :rtype: int
        """
        return self._remain_partitions

    @remain_partitions.setter
    def remain_partitions(self, remain_partitions):
        """Sets the remain_partitions of this ListMqsInstanceTopicsResponse.

        剩余分区数。

        :param remain_partitions: The remain_partitions of this ListMqsInstanceTopicsResponse.
        :type remain_partitions: int
        """
        self._remain_partitions = remain_partitions

    @property
    def max_partitions(self):
        """Gets the max_partitions of this ListMqsInstanceTopicsResponse.

        分区总数。

        :return: The max_partitions of this ListMqsInstanceTopicsResponse.
        :rtype: int
        """
        return self._max_partitions

    @max_partitions.setter
    def max_partitions(self, max_partitions):
        """Sets the max_partitions of this ListMqsInstanceTopicsResponse.

        分区总数。

        :param max_partitions: The max_partitions of this ListMqsInstanceTopicsResponse.
        :type max_partitions: int
        """
        self._max_partitions = max_partitions

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
        if not isinstance(other, ListMqsInstanceTopicsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
