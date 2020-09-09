# coding: utf-8

import pprint
import re

import six





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
        """ShowClusterRespCluster - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the controller of this ShowClusterRespCluster.

        控制器ID。

        :return: The controller of this ShowClusterRespCluster.
        :rtype: str
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this ShowClusterRespCluster.

        控制器ID。

        :param controller: The controller of this ShowClusterRespCluster.
        :type: str
        """
        self._controller = controller

    @property
    def brokers(self):
        """Gets the brokers of this ShowClusterRespCluster.

        节点列表。

        :return: The brokers of this ShowClusterRespCluster.
        :rtype: list[ShowClusterRespClusterBrokers]
        """
        return self._brokers

    @brokers.setter
    def brokers(self, brokers):
        """Sets the brokers of this ShowClusterRespCluster.

        节点列表。

        :param brokers: The brokers of this ShowClusterRespCluster.
        :type: list[ShowClusterRespClusterBrokers]
        """
        self._brokers = brokers

    @property
    def topics_count(self):
        """Gets the topics_count of this ShowClusterRespCluster.

        主题数量。

        :return: The topics_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._topics_count

    @topics_count.setter
    def topics_count(self, topics_count):
        """Sets the topics_count of this ShowClusterRespCluster.

        主题数量。

        :param topics_count: The topics_count of this ShowClusterRespCluster.
        :type: int
        """
        self._topics_count = topics_count

    @property
    def partitions_count(self):
        """Gets the partitions_count of this ShowClusterRespCluster.

        分区数量。

        :return: The partitions_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._partitions_count

    @partitions_count.setter
    def partitions_count(self, partitions_count):
        """Sets the partitions_count of this ShowClusterRespCluster.

        分区数量。

        :param partitions_count: The partitions_count of this ShowClusterRespCluster.
        :type: int
        """
        self._partitions_count = partitions_count

    @property
    def online_partitions_count(self):
        """Gets the online_partitions_count of this ShowClusterRespCluster.

        在线分区数量。

        :return: The online_partitions_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._online_partitions_count

    @online_partitions_count.setter
    def online_partitions_count(self, online_partitions_count):
        """Sets the online_partitions_count of this ShowClusterRespCluster.

        在线分区数量。

        :param online_partitions_count: The online_partitions_count of this ShowClusterRespCluster.
        :type: int
        """
        self._online_partitions_count = online_partitions_count

    @property
    def replicas_count(self):
        """Gets the replicas_count of this ShowClusterRespCluster.

        副本数量。

        :return: The replicas_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._replicas_count

    @replicas_count.setter
    def replicas_count(self, replicas_count):
        """Sets the replicas_count of this ShowClusterRespCluster.

        副本数量。

        :param replicas_count: The replicas_count of this ShowClusterRespCluster.
        :type: int
        """
        self._replicas_count = replicas_count

    @property
    def isr_replicas_count(self):
        """Gets the isr_replicas_count of this ShowClusterRespCluster.

        ISR（In-Sync Replicas） 副本总数。

        :return: The isr_replicas_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._isr_replicas_count

    @isr_replicas_count.setter
    def isr_replicas_count(self, isr_replicas_count):
        """Sets the isr_replicas_count of this ShowClusterRespCluster.

        ISR（In-Sync Replicas） 副本总数。

        :param isr_replicas_count: The isr_replicas_count of this ShowClusterRespCluster.
        :type: int
        """
        self._isr_replicas_count = isr_replicas_count

    @property
    def consumers_count(self):
        """Gets the consumers_count of this ShowClusterRespCluster.

        消费组数量。

        :return: The consumers_count of this ShowClusterRespCluster.
        :rtype: int
        """
        return self._consumers_count

    @consumers_count.setter
    def consumers_count(self, consumers_count):
        """Sets the consumers_count of this ShowClusterRespCluster.

        消费组数量。

        :param consumers_count: The consumers_count of this ShowClusterRespCluster.
        :type: int
        """
        self._consumers_count = consumers_count

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
        if not isinstance(other, ShowClusterRespCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
