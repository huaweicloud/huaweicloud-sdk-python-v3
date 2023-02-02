# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopicAssignment:

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
        'partition_brokers': 'list[int]'
    }

    attribute_map = {
        'partition': 'partition',
        'partition_brokers': 'partition_brokers'
    }

    def __init__(self, partition=None, partition_brokers=None):
        """TopicAssignment

        The model defined in huaweicloud sdk

        :param partition: 手动指定分配方案时的分区号。
        :type partition: int
        :param partition_brokers: 手动指定某个分区将要分配的broker列表
        :type partition_brokers: list[int]
        """
        
        

        self._partition = None
        self._partition_brokers = None
        self.discriminator = None

        if partition is not None:
            self.partition = partition
        if partition_brokers is not None:
            self.partition_brokers = partition_brokers

    @property
    def partition(self):
        """Gets the partition of this TopicAssignment.

        手动指定分配方案时的分区号。

        :return: The partition of this TopicAssignment.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this TopicAssignment.

        手动指定分配方案时的分区号。

        :param partition: The partition of this TopicAssignment.
        :type partition: int
        """
        self._partition = partition

    @property
    def partition_brokers(self):
        """Gets the partition_brokers of this TopicAssignment.

        手动指定某个分区将要分配的broker列表

        :return: The partition_brokers of this TopicAssignment.
        :rtype: list[int]
        """
        return self._partition_brokers

    @partition_brokers.setter
    def partition_brokers(self, partition_brokers):
        """Sets the partition_brokers of this TopicAssignment.

        手动指定某个分区将要分配的broker列表

        :param partition_brokers: The partition_brokers of this TopicAssignment.
        :type partition_brokers: list[int]
        """
        self._partition_brokers = partition_brokers

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
        if not isinstance(other, TopicAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
