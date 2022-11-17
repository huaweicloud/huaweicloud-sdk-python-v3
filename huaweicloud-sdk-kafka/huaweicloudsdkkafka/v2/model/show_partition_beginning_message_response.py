# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPartitionBeginningMessageResponse(SdkResponse):

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
        'partition': 'int',
        'offset': 'int',
        'timestamp': 'int'
    }

    attribute_map = {
        'topic': 'topic',
        'partition': 'partition',
        'offset': 'offset',
        'timestamp': 'timestamp'
    }

    def __init__(self, topic=None, partition=None, offset=None, timestamp=None):
        """ShowPartitionBeginningMessageResponse

        The model defined in huaweicloud sdk

        :param topic: Topic名称。
        :type topic: str
        :param partition: 分区编号。
        :type partition: int
        :param offset: 最新消息位置。
        :type offset: int
        :param timestamp: 生产消息的时间。 格式为Unix时间戳。单位为毫秒。
        :type timestamp: int
        """
        
        super(ShowPartitionBeginningMessageResponse, self).__init__()

        self._topic = None
        self._partition = None
        self._offset = None
        self._timestamp = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if partition is not None:
            self.partition = partition
        if offset is not None:
            self.offset = offset
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def topic(self):
        """Gets the topic of this ShowPartitionBeginningMessageResponse.

        Topic名称。

        :return: The topic of this ShowPartitionBeginningMessageResponse.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowPartitionBeginningMessageResponse.

        Topic名称。

        :param topic: The topic of this ShowPartitionBeginningMessageResponse.
        :type topic: str
        """
        self._topic = topic

    @property
    def partition(self):
        """Gets the partition of this ShowPartitionBeginningMessageResponse.

        分区编号。

        :return: The partition of this ShowPartitionBeginningMessageResponse.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this ShowPartitionBeginningMessageResponse.

        分区编号。

        :param partition: The partition of this ShowPartitionBeginningMessageResponse.
        :type partition: int
        """
        self._partition = partition

    @property
    def offset(self):
        """Gets the offset of this ShowPartitionBeginningMessageResponse.

        最新消息位置。

        :return: The offset of this ShowPartitionBeginningMessageResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowPartitionBeginningMessageResponse.

        最新消息位置。

        :param offset: The offset of this ShowPartitionBeginningMessageResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def timestamp(self):
        """Gets the timestamp of this ShowPartitionBeginningMessageResponse.

        生产消息的时间。 格式为Unix时间戳。单位为毫秒。

        :return: The timestamp of this ShowPartitionBeginningMessageResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ShowPartitionBeginningMessageResponse.

        生产消息的时间。 格式为Unix时间戳。单位为毫秒。

        :param timestamp: The timestamp of this ShowPartitionBeginningMessageResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, ShowPartitionBeginningMessageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
