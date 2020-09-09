# coding: utf-8

import pprint
import re

import six





class ShowInstanceTopicDetailRespReplicas:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'broker': 'int',
        'leader': 'bool',
        'in_sync': 'bool',
        'size': 'int',
        'lag': 'int'
    }

    attribute_map = {
        'broker': 'broker',
        'leader': 'leader',
        'in_sync': 'in_sync',
        'size': 'size',
        'lag': 'lag'
    }

    def __init__(self, broker=None, leader=None, in_sync=None, size=None, lag=None):
        """ShowInstanceTopicDetailRespReplicas - a model defined in huaweicloud sdk"""
        
        

        self._broker = None
        self._leader = None
        self._in_sync = None
        self._size = None
        self._lag = None
        self.discriminator = None

        if broker is not None:
            self.broker = broker
        if leader is not None:
            self.leader = leader
        if in_sync is not None:
            self.in_sync = in_sync
        if size is not None:
            self.size = size
        if lag is not None:
            self.lag = lag

    @property
    def broker(self):
        """Gets the broker of this ShowInstanceTopicDetailRespReplicas.

        副本所在的节点ID。

        :return: The broker of this ShowInstanceTopicDetailRespReplicas.
        :rtype: int
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        """Sets the broker of this ShowInstanceTopicDetailRespReplicas.

        副本所在的节点ID。

        :param broker: The broker of this ShowInstanceTopicDetailRespReplicas.
        :type: int
        """
        self._broker = broker

    @property
    def leader(self):
        """Gets the leader of this ShowInstanceTopicDetailRespReplicas.

        该副本是否为leader。

        :return: The leader of this ShowInstanceTopicDetailRespReplicas.
        :rtype: bool
        """
        return self._leader

    @leader.setter
    def leader(self, leader):
        """Sets the leader of this ShowInstanceTopicDetailRespReplicas.

        该副本是否为leader。

        :param leader: The leader of this ShowInstanceTopicDetailRespReplicas.
        :type: bool
        """
        self._leader = leader

    @property
    def in_sync(self):
        """Gets the in_sync of this ShowInstanceTopicDetailRespReplicas.

        该副本是否在ISR副本中。

        :return: The in_sync of this ShowInstanceTopicDetailRespReplicas.
        :rtype: bool
        """
        return self._in_sync

    @in_sync.setter
    def in_sync(self, in_sync):
        """Sets the in_sync of this ShowInstanceTopicDetailRespReplicas.

        该副本是否在ISR副本中。

        :param in_sync: The in_sync of this ShowInstanceTopicDetailRespReplicas.
        :type: bool
        """
        self._in_sync = in_sync

    @property
    def size(self):
        """Gets the size of this ShowInstanceTopicDetailRespReplicas.

        该副本当前日志大小。

        :return: The size of this ShowInstanceTopicDetailRespReplicas.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowInstanceTopicDetailRespReplicas.

        该副本当前日志大小。

        :param size: The size of this ShowInstanceTopicDetailRespReplicas.
        :type: int
        """
        self._size = size

    @property
    def lag(self):
        """Gets the lag of this ShowInstanceTopicDetailRespReplicas.

        该副本当前落后hw的消息数。

        :return: The lag of this ShowInstanceTopicDetailRespReplicas.
        :rtype: int
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        """Sets the lag of this ShowInstanceTopicDetailRespReplicas.

        该副本当前落后hw的消息数。

        :param lag: The lag of this ShowInstanceTopicDetailRespReplicas.
        :type: int
        """
        self._lag = lag

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
        if not isinstance(other, ShowInstanceTopicDetailRespReplicas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
