# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiskusageTopicEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'str',
        'topic_name': 'str',
        'topic_partition': 'str',
        'percentage': 'float'
    }

    attribute_map = {
        'size': 'size',
        'topic_name': 'topic_name',
        'topic_partition': 'topic_partition',
        'percentage': 'percentage'
    }

    def __init__(self, size=None, topic_name=None, topic_partition=None, percentage=None):
        """DiskusageTopicEntity

        The model defined in huaweicloud sdk

        :param size: 磁盘使用量。
        :type size: str
        :param topic_name: topic名称。
        :type topic_name: str
        :param topic_partition: 分区。
        :type topic_partition: str
        :param percentage: 磁盘使用量的占比。
        :type percentage: float
        """
        
        

        self._size = None
        self._topic_name = None
        self._topic_partition = None
        self._percentage = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if topic_name is not None:
            self.topic_name = topic_name
        if topic_partition is not None:
            self.topic_partition = topic_partition
        if percentage is not None:
            self.percentage = percentage

    @property
    def size(self):
        """Gets the size of this DiskusageTopicEntity.

        磁盘使用量。

        :return: The size of this DiskusageTopicEntity.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DiskusageTopicEntity.

        磁盘使用量。

        :param size: The size of this DiskusageTopicEntity.
        :type size: str
        """
        self._size = size

    @property
    def topic_name(self):
        """Gets the topic_name of this DiskusageTopicEntity.

        topic名称。

        :return: The topic_name of this DiskusageTopicEntity.
        :rtype: str
        """
        return self._topic_name

    @topic_name.setter
    def topic_name(self, topic_name):
        """Sets the topic_name of this DiskusageTopicEntity.

        topic名称。

        :param topic_name: The topic_name of this DiskusageTopicEntity.
        :type topic_name: str
        """
        self._topic_name = topic_name

    @property
    def topic_partition(self):
        """Gets the topic_partition of this DiskusageTopicEntity.

        分区。

        :return: The topic_partition of this DiskusageTopicEntity.
        :rtype: str
        """
        return self._topic_partition

    @topic_partition.setter
    def topic_partition(self, topic_partition):
        """Sets the topic_partition of this DiskusageTopicEntity.

        分区。

        :param topic_partition: The topic_partition of this DiskusageTopicEntity.
        :type topic_partition: str
        """
        self._topic_partition = topic_partition

    @property
    def percentage(self):
        """Gets the percentage of this DiskusageTopicEntity.

        磁盘使用量的占比。

        :return: The percentage of this DiskusageTopicEntity.
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this DiskusageTopicEntity.

        磁盘使用量的占比。

        :param percentage: The percentage of this DiskusageTopicEntity.
        :type percentage: float
        """
        self._percentage = percentage

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
        if not isinstance(other, DiskusageTopicEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
