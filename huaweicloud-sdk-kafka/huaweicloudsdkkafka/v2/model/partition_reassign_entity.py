# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PartitionReassignEntity:

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
        'brokers': 'list[int]',
        'replication_factor': 'int',
        'assignment': 'list[TopicAssignment]'
    }

    attribute_map = {
        'topic': 'topic',
        'brokers': 'brokers',
        'replication_factor': 'replication_factor',
        'assignment': 'assignment'
    }

    def __init__(self, topic=None, brokers=None, replication_factor=None, assignment=None):
        """PartitionReassignEntity

        The model defined in huaweicloud sdk

        :param topic: topic名称
        :type topic: str
        :param brokers: 分区重平衡到的broker列表，自动生成分配方案时需指定该参数。
        :type brokers: list[int]
        :param replication_factor: 副本因子，自动生成分配方案时可指定。
        :type replication_factor: int
        :param assignment: 手动指定的分配方案。brokers参数与该参数不能同时为空。
        :type assignment: list[:class:`huaweicloudsdkkafka.v2.TopicAssignment`]
        """
        
        

        self._topic = None
        self._brokers = None
        self._replication_factor = None
        self._assignment = None
        self.discriminator = None

        self.topic = topic
        if brokers is not None:
            self.brokers = brokers
        if replication_factor is not None:
            self.replication_factor = replication_factor
        if assignment is not None:
            self.assignment = assignment

    @property
    def topic(self):
        """Gets the topic of this PartitionReassignEntity.

        topic名称

        :return: The topic of this PartitionReassignEntity.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this PartitionReassignEntity.

        topic名称

        :param topic: The topic of this PartitionReassignEntity.
        :type topic: str
        """
        self._topic = topic

    @property
    def brokers(self):
        """Gets the brokers of this PartitionReassignEntity.

        分区重平衡到的broker列表，自动生成分配方案时需指定该参数。

        :return: The brokers of this PartitionReassignEntity.
        :rtype: list[int]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this PartitionReassignEntity.

        分区重平衡到的broker列表，自动生成分配方案时需指定该参数。

        :param brokers: The brokers of this PartitionReassignEntity.
        :type brokers: list[int]
        """
        self._brokers = brokers

    @property
    def replication_factor(self):
        """Gets the replication_factor of this PartitionReassignEntity.

        副本因子，自动生成分配方案时可指定。

        :return: The replication_factor of this PartitionReassignEntity.
        :rtype: int
        """
        return self._replication_factor

    @replication_factor.setter
    def replication_factor(self, replication_factor):
        """Sets the replication_factor of this PartitionReassignEntity.

        副本因子，自动生成分配方案时可指定。

        :param replication_factor: The replication_factor of this PartitionReassignEntity.
        :type replication_factor: int
        """
        self._replication_factor = replication_factor

    @property
    def assignment(self):
        """Gets the assignment of this PartitionReassignEntity.

        手动指定的分配方案。brokers参数与该参数不能同时为空。

        :return: The assignment of this PartitionReassignEntity.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.TopicAssignment`]
        """
        return self._assignment

    @assignment.setter
    def assignment(self, assignment):
        """Sets the assignment of this PartitionReassignEntity.

        手动指定的分配方案。brokers参数与该参数不能同时为空。

        :param assignment: The assignment of this PartitionReassignEntity.
        :type assignment: list[:class:`huaweicloudsdkkafka.v2.TopicAssignment`]
        """
        self._assignment = assignment

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
        if not isinstance(other, PartitionReassignEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
