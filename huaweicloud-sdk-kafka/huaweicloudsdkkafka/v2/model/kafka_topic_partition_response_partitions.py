# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaTopicPartitionResponsePartitions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition': 'int',
        'start_offset': 'int',
        'last_offset': 'int',
        'message_count': 'int',
        'last_update_time': 'int'
    }

    attribute_map = {
        'partition': 'partition',
        'start_offset': 'start_offset',
        'last_offset': 'last_offset',
        'message_count': 'message_count',
        'last_update_time': 'last_update_time'
    }

    def __init__(self, partition=None, start_offset=None, last_offset=None, message_count=None, last_update_time=None):
        """KafkaTopicPartitionResponsePartitions

        The model defined in huaweicloud sdk

        :param partition: 分区ID
        :type partition: int
        :param start_offset: 起始偏移量
        :type start_offset: int
        :param last_offset: 最后偏移量
        :type last_offset: int
        :param message_count: 分区消息数
        :type message_count: int
        :param last_update_time: 最近更新时间
        :type last_update_time: int
        """
        
        

        self._partition = None
        self._start_offset = None
        self._last_offset = None
        self._message_count = None
        self._last_update_time = None
        self.discriminator = None

        if partition is not None:
            self.partition = partition
        if start_offset is not None:
            self.start_offset = start_offset
        if last_offset is not None:
            self.last_offset = last_offset
        if message_count is not None:
            self.message_count = message_count
        if last_update_time is not None:
            self.last_update_time = last_update_time

    @property
    def partition(self):
        """Gets the partition of this KafkaTopicPartitionResponsePartitions.

        分区ID

        :return: The partition of this KafkaTopicPartitionResponsePartitions.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this KafkaTopicPartitionResponsePartitions.

        分区ID

        :param partition: The partition of this KafkaTopicPartitionResponsePartitions.
        :type partition: int
        """
        self._partition = partition

    @property
    def start_offset(self):
        """Gets the start_offset of this KafkaTopicPartitionResponsePartitions.

        起始偏移量

        :return: The start_offset of this KafkaTopicPartitionResponsePartitions.
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        """Sets the start_offset of this KafkaTopicPartitionResponsePartitions.

        起始偏移量

        :param start_offset: The start_offset of this KafkaTopicPartitionResponsePartitions.
        :type start_offset: int
        """
        self._start_offset = start_offset

    @property
    def last_offset(self):
        """Gets the last_offset of this KafkaTopicPartitionResponsePartitions.

        最后偏移量

        :return: The last_offset of this KafkaTopicPartitionResponsePartitions.
        :rtype: int
        """
        return self._last_offset

    @last_offset.setter
    def last_offset(self, last_offset):
        """Sets the last_offset of this KafkaTopicPartitionResponsePartitions.

        最后偏移量

        :param last_offset: The last_offset of this KafkaTopicPartitionResponsePartitions.
        :type last_offset: int
        """
        self._last_offset = last_offset

    @property
    def message_count(self):
        """Gets the message_count of this KafkaTopicPartitionResponsePartitions.

        分区消息数

        :return: The message_count of this KafkaTopicPartitionResponsePartitions.
        :rtype: int
        """
        return self._message_count

    @message_count.setter
    def message_count(self, message_count):
        """Sets the message_count of this KafkaTopicPartitionResponsePartitions.

        分区消息数

        :param message_count: The message_count of this KafkaTopicPartitionResponsePartitions.
        :type message_count: int
        """
        self._message_count = message_count

    @property
    def last_update_time(self):
        """Gets the last_update_time of this KafkaTopicPartitionResponsePartitions.

        最近更新时间

        :return: The last_update_time of this KafkaTopicPartitionResponsePartitions.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this KafkaTopicPartitionResponsePartitions.

        最近更新时间

        :param last_update_time: The last_update_time of this KafkaTopicPartitionResponsePartitions.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

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
        if not isinstance(other, KafkaTopicPartitionResponsePartitions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
