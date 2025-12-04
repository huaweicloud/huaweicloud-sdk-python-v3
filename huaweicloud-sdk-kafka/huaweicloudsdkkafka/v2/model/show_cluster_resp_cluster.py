# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterRespCluster:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'controller': 'str',
        'brokers': 'list[ShowClusterRespClusterBrokers]',
        'topics_count': 'int',
        'partitions_count': 'int',
        'online_partitions_count': 'int',
        'replicas_count': 'int',
        'isr_replicas_count': 'int',
        'consumers_count': 'int'
    }

    attribute_map = {
        'controller': 'controller',
        'brokers': 'brokers',
        'topics_count': 'topics_count',
        'partitions_count': 'partitions_count',
        'online_partitions_count': 'online_partitions_count',
        'replicas_count': 'replicas_count',
        'isr_replicas_count': 'isr_replicas_count',
        'consumers_count': 'consumers_count'
    }

    def __init__(self, controller=None, brokers=None, topics_count=None, partitions_count=None, online_partitions_count=None, replicas_count=None, isr_replicas_count=None, consumers_count=None):
        r"""ShowClusterRespCluster

        The model defined in huaweicloud sdk

        :param controller: **参数解释**： 控制器ID。 **取值范围**： 不涉及。
        :type controller: str
        :param brokers: **参数解释**： 节点列表。
        :type brokers: list[:class:`huaweicloudsdkkafka.v2.ShowClusterRespClusterBrokers`]
        :param topics_count: **参数解释**： 主题数量。 **取值范围**： 不涉及。
        :type topics_count: int
        :param partitions_count: **参数解释**： 分区数量。 **取值范围**： 不涉及。
        :type partitions_count: int
        :param online_partitions_count: **参数解释**： 在线分区数量。 **取值范围**： 不涉及。
        :type online_partitions_count: int
        :param replicas_count: **参数解释**： 副本数量。 **取值范围**： 不涉及。
        :type replicas_count: int
        :param isr_replicas_count: **参数解释**： ISR（In-Sync Replicas） 副本总数。 **取值范围**： 不涉及。
        :type isr_replicas_count: int
        :param consumers_count: **参数解释**： 消费组数量。 **取值范围**： 不涉及。
        :type consumers_count: int
        """
        
        

        self._controller = None
        self._brokers = None
        self._topics_count = None
        self._partitions_count = None
        self._online_partitions_count = None
        self._replicas_count = None
        self._isr_replicas_count = None
        self._consumers_count = None
        self.discriminator = None

        if controller is not None:
            self.controller = controller
        if brokers is not None:
            self.brokers = brokers
        if topics_count is not None:
            self.topics_count = topics_count
        if partitions_count is not None:
            self.partitions_count = partitions_count
        if online_partitions_count is not None:
            self.online_partitions_count = online_partitions_count
        if replicas_count is not None:
            self.replicas_count = replicas_count
        if isr_replicas_count is not None:
            self.isr_replicas_count = isr_replicas_count
        if consumers_count is not None:
            self.consumers_count = consumers_count

    @property
    def controller(self):
        r"""Gets the controller of this ShowClusterRespCluster.

        **参数解释**： 控制器ID。 **取值范围**： 不涉及。

        :return: The controller of this ShowClusterRespCluster.
        :rtype: str
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        r"""Sets the controller of this ShowClusterRespCluster.

        **参数解释**： 控制器ID。 **取值范围**： 不涉及。

        :param controller: The controller of this ShowClusterRespCluster.
        :type controller: str
        """
        self._controller = controller

    @property
    def brokers(self):
        r"""Gets the brokers of this ShowClusterRespCluster.

        **参数解释**： 节点列表。

        :return: The brokers of this ShowClusterRespCluster.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowClusterRespClusterBrokers`]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        r"""Sets the brokers of this ShowClusterRespCluster.

        **参数解释**： 节点列表。

        :param brokers: The brokers of this ShowClusterRespCluster.
        :type brokers: list[:class:`huaweicloudsdkkafka.v2.ShowClusterRespClusterBrokers`]
        """
        self._brokers = brokers

    @property
    def topics_count(self):
        r"""Gets the topics_count of this ShowClusterRespCluster.

        **参数解释**： 主题数量。 **取值范围**： 不涉及。

        :return: The topics_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._topics_count

    @topics_count.setter
    def topics_count(self, topics_count):
        r"""Sets the topics_count of this ShowClusterRespCluster.

        **参数解释**： 主题数量。 **取值范围**： 不涉及。

        :param topics_count: The topics_count of this ShowClusterRespCluster.
        :type topics_count: int
        """
        self._topics_count = topics_count

    @property
    def partitions_count(self):
        r"""Gets the partitions_count of this ShowClusterRespCluster.

        **参数解释**： 分区数量。 **取值范围**： 不涉及。

        :return: The partitions_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._partitions_count

    @partitions_count.setter
    def partitions_count(self, partitions_count):
        r"""Sets the partitions_count of this ShowClusterRespCluster.

        **参数解释**： 分区数量。 **取值范围**： 不涉及。

        :param partitions_count: The partitions_count of this ShowClusterRespCluster.
        :type partitions_count: int
        """
        self._partitions_count = partitions_count

    @property
    def online_partitions_count(self):
        r"""Gets the online_partitions_count of this ShowClusterRespCluster.

        **参数解释**： 在线分区数量。 **取值范围**： 不涉及。

        :return: The online_partitions_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._online_partitions_count

    @online_partitions_count.setter
    def online_partitions_count(self, online_partitions_count):
        r"""Sets the online_partitions_count of this ShowClusterRespCluster.

        **参数解释**： 在线分区数量。 **取值范围**： 不涉及。

        :param online_partitions_count: The online_partitions_count of this ShowClusterRespCluster.
        :type online_partitions_count: int
        """
        self._online_partitions_count = online_partitions_count

    @property
    def replicas_count(self):
        r"""Gets the replicas_count of this ShowClusterRespCluster.

        **参数解释**： 副本数量。 **取值范围**： 不涉及。

        :return: The replicas_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._replicas_count

    @replicas_count.setter
    def replicas_count(self, replicas_count):
        r"""Sets the replicas_count of this ShowClusterRespCluster.

        **参数解释**： 副本数量。 **取值范围**： 不涉及。

        :param replicas_count: The replicas_count of this ShowClusterRespCluster.
        :type replicas_count: int
        """
        self._replicas_count = replicas_count

    @property
    def isr_replicas_count(self):
        r"""Gets the isr_replicas_count of this ShowClusterRespCluster.

        **参数解释**： ISR（In-Sync Replicas） 副本总数。 **取值范围**： 不涉及。

        :return: The isr_replicas_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._isr_replicas_count

    @isr_replicas_count.setter
    def isr_replicas_count(self, isr_replicas_count):
        r"""Sets the isr_replicas_count of this ShowClusterRespCluster.

        **参数解释**： ISR（In-Sync Replicas） 副本总数。 **取值范围**： 不涉及。

        :param isr_replicas_count: The isr_replicas_count of this ShowClusterRespCluster.
        :type isr_replicas_count: int
        """
        self._isr_replicas_count = isr_replicas_count

    @property
    def consumers_count(self):
        r"""Gets the consumers_count of this ShowClusterRespCluster.

        **参数解释**： 消费组数量。 **取值范围**： 不涉及。

        :return: The consumers_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._consumers_count

    @consumers_count.setter
    def consumers_count(self, consumers_count):
        r"""Sets the consumers_count of this ShowClusterRespCluster.

        **参数解释**： 消费组数量。 **取值范围**： 不涉及。

        :param consumers_count: The consumers_count of this ShowClusterRespCluster.
        :type consumers_count: int
        """
        self._consumers_count = consumers_count

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
        if not isinstance(other, ShowClusterRespCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
