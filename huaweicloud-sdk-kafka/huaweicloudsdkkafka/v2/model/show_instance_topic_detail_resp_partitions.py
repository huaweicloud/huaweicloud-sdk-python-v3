# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceTopicDetailRespPartitions:

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
        'leo': 'int',
        'hw': 'int',
        'lso': 'int',
        'last_update_timestamp': 'int',
        'replicas': 'list[ShowInstanceTopicDetailRespReplicas]'
    }

    attribute_map = {
        'partition': 'partition',
        'leader': 'leader',
        'leo': 'leo',
        'hw': 'hw',
        'lso': 'lso',
        'last_update_timestamp': 'last_update_timestamp',
        'replicas': 'replicas'
    }

    def __init__(self, partition=None, leader=None, leo=None, hw=None, lso=None, last_update_timestamp=None, replicas=None):
        """ShowInstanceTopicDetailRespPartitions

        The model defined in huaweicloud sdk

        :param partition: 分区ID。
        :type partition: int
        :param leader: leader副本所在节点的id。
        :type leader: int
        :param leo: 分区leader副本的LEO（Log End Offset）。
        :type leo: int
        :param hw: 分区高水位（HW，High Watermark）。
        :type hw: int
        :param lso: 分区leader副本的LSO（Log Start Offset）。
        :type lso: int
        :param last_update_timestamp: 分区上次写入消息的时间。  格式为Unix时间戳。  单位：毫秒。
        :type last_update_timestamp: int
        :param replicas: 副本列表。
        :type replicas: list[:class:`huaweicloudsdkkafka.v2.ShowInstanceTopicDetailRespReplicas`]
        """
        
        

        self._partition = None
        self._leader = None
        self._leo = None
        self._hw = None
        self._lso = None
        self._last_update_timestamp = None
        self._replicas = None
        self.discriminator = None

        if partition is not None:
            self.partition = partition
        if leader is not None:
            self.leader = leader
        if leo is not None:
            self.leo = leo
        if hw is not None:
            self.hw = hw
        if lso is not None:
            self.lso = lso
        if last_update_timestamp is not None:
            self.last_update_timestamp = last_update_timestamp
        if replicas is not None:
            self.replicas = replicas

    @property
    def partition(self):
        """Gets the partition of this ShowInstanceTopicDetailRespPartitions.

        分区ID。

        :return: The partition of this ShowInstanceTopicDetailRespPartitions.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this ShowInstanceTopicDetailRespPartitions.

        分区ID。

        :param partition: The partition of this ShowInstanceTopicDetailRespPartitions.
        :type partition: int
        """
        self._partition = partition

    @property
    def leader(self):
        """Gets the leader of this ShowInstanceTopicDetailRespPartitions.

        leader副本所在节点的id。

        :return: The leader of this ShowInstanceTopicDetailRespPartitions.
        :rtype: int
        """
        return self._leader

    @leader.setter
    def leader(self, leader):
        """Sets the leader of this ShowInstanceTopicDetailRespPartitions.

        leader副本所在节点的id。

        :param leader: The leader of this ShowInstanceTopicDetailRespPartitions.
        :type leader: int
        """
        self._leader = leader

    @property
    def leo(self):
        """Gets the leo of this ShowInstanceTopicDetailRespPartitions.

        分区leader副本的LEO（Log End Offset）。

        :return: The leo of this ShowInstanceTopicDetailRespPartitions.
        :rtype: int
        """
        return self._leo

    @leo.setter
    def leo(self, leo):
        """Sets the leo of this ShowInstanceTopicDetailRespPartitions.

        分区leader副本的LEO（Log End Offset）。

        :param leo: The leo of this ShowInstanceTopicDetailRespPartitions.
        :type leo: int
        """
        self._leo = leo

    @property
    def hw(self):
        """Gets the hw of this ShowInstanceTopicDetailRespPartitions.

        分区高水位（HW，High Watermark）。

        :return: The hw of this ShowInstanceTopicDetailRespPartitions.
        :rtype: int
        """
        return self._hw

    @hw.setter
    def hw(self, hw):
        """Sets the hw of this ShowInstanceTopicDetailRespPartitions.

        分区高水位（HW，High Watermark）。

        :param hw: The hw of this ShowInstanceTopicDetailRespPartitions.
        :type hw: int
        """
        self._hw = hw

    @property
    def lso(self):
        """Gets the lso of this ShowInstanceTopicDetailRespPartitions.

        分区leader副本的LSO（Log Start Offset）。

        :return: The lso of this ShowInstanceTopicDetailRespPartitions.
        :rtype: int
        """
        return self._lso

    @lso.setter
    def lso(self, lso):
        """Sets the lso of this ShowInstanceTopicDetailRespPartitions.

        分区leader副本的LSO（Log Start Offset）。

        :param lso: The lso of this ShowInstanceTopicDetailRespPartitions.
        :type lso: int
        """
        self._lso = lso

    @property
    def last_update_timestamp(self):
        """Gets the last_update_timestamp of this ShowInstanceTopicDetailRespPartitions.

        分区上次写入消息的时间。  格式为Unix时间戳。  单位：毫秒。

        :return: The last_update_timestamp of this ShowInstanceTopicDetailRespPartitions.
        :rtype: int
        """
        return self._last_update_timestamp

    @last_update_timestamp.setter
    def last_update_timestamp(self, last_update_timestamp):
        """Sets the last_update_timestamp of this ShowInstanceTopicDetailRespPartitions.

        分区上次写入消息的时间。  格式为Unix时间戳。  单位：毫秒。

        :param last_update_timestamp: The last_update_timestamp of this ShowInstanceTopicDetailRespPartitions.
        :type last_update_timestamp: int
        """
        self._last_update_timestamp = last_update_timestamp

    @property
    def replicas(self):
        """Gets the replicas of this ShowInstanceTopicDetailRespPartitions.

        副本列表。

        :return: The replicas of this ShowInstanceTopicDetailRespPartitions.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowInstanceTopicDetailRespReplicas`]
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this ShowInstanceTopicDetailRespPartitions.

        副本列表。

        :param replicas: The replicas of this ShowInstanceTopicDetailRespPartitions.
        :type replicas: list[:class:`huaweicloudsdkkafka.v2.ShowInstanceTopicDetailRespReplicas`]
        """
        self._replicas = replicas

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
        if not isinstance(other, ShowInstanceTopicDetailRespPartitions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
