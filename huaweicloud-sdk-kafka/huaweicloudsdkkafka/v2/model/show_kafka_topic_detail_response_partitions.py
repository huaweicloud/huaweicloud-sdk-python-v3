# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaTopicDetailResponsePartitions:

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
        'leader': 'int',
        'replicas': 'list[int]'
    }

    attribute_map = {
        'partition': 'partition',
        'leader': 'leader',
        'replicas': 'replicas'
    }

    def __init__(self, partition=None, leader=None, replicas=None):
        r"""ShowKafkaTopicDetailResponsePartitions

        The model defined in huaweicloud sdk

        :param partition: **参数解释**： 分区编号。  **取值范围**： 不涉及。
        :type partition: int
        :param leader: **参数解释**： leader副本所在节点的ID。  **取值范围**： 不涉及。
        :type leader: int
        :param replicas: **参数解释**： 副本列表。
        :type replicas: list[int]
        """
        
        

        self._partition = None
        self._leader = None
        self._replicas = None
        self.discriminator = None

        if partition is not None:
            self.partition = partition
        if leader is not None:
            self.leader = leader
        if replicas is not None:
            self.replicas = replicas

    @property
    def partition(self):
        r"""Gets the partition of this ShowKafkaTopicDetailResponsePartitions.

        **参数解释**： 分区编号。  **取值范围**： 不涉及。

        :return: The partition of this ShowKafkaTopicDetailResponsePartitions.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this ShowKafkaTopicDetailResponsePartitions.

        **参数解释**： 分区编号。  **取值范围**： 不涉及。

        :param partition: The partition of this ShowKafkaTopicDetailResponsePartitions.
        :type partition: int
        """
        self._partition = partition

    @property
    def leader(self):
        r"""Gets the leader of this ShowKafkaTopicDetailResponsePartitions.

        **参数解释**： leader副本所在节点的ID。  **取值范围**： 不涉及。

        :return: The leader of this ShowKafkaTopicDetailResponsePartitions.
        :rtype: int
        """
        return self._leader

    @leader.setter
    def leader(self, leader):
        r"""Sets the leader of this ShowKafkaTopicDetailResponsePartitions.

        **参数解释**： leader副本所在节点的ID。  **取值范围**： 不涉及。

        :param leader: The leader of this ShowKafkaTopicDetailResponsePartitions.
        :type leader: int
        """
        self._leader = leader

    @property
    def replicas(self):
        r"""Gets the replicas of this ShowKafkaTopicDetailResponsePartitions.

        **参数解释**： 副本列表。

        :return: The replicas of this ShowKafkaTopicDetailResponsePartitions.
        :rtype: list[int]
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        r"""Sets the replicas of this ShowKafkaTopicDetailResponsePartitions.

        **参数解释**： 副本列表。

        :param replicas: The replicas of this ShowKafkaTopicDetailResponsePartitions.
        :type replicas: list[int]
        """
        self._replicas = replicas

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowKafkaTopicDetailResponsePartitions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
