# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        r"""ShowInstanceTopicDetailRespReplicas

        The model defined in huaweicloud sdk

        :param broker: **参数解释**： 副本所在的节点ID。 **取值范围**： 不涉及
        :type broker: int
        :param leader: **参数解释**： 该副本是否为leader。 **取值范围**： - true：该副本是leader。 - false：该副本不是leader。
        :type leader: bool
        :param in_sync: **参数解释**： 该副本是否在ISR副本中。 **取值范围**： - true：在ISR副本中。 - false：不在ISR副本中。
        :type in_sync: bool
        :param size: **参数解释**： 该副本当前日志大小。单位：Byte。 **取值范围**： 不涉及
        :type size: int
        :param lag: **参数解释**： 该副本当前落后hw的消息数。 **取值范围**： 不涉及
        :type lag: int
        """
        
        

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
        r"""Gets the broker of this ShowInstanceTopicDetailRespReplicas.

        **参数解释**： 副本所在的节点ID。 **取值范围**： 不涉及

        :return: The broker of this ShowInstanceTopicDetailRespReplicas.
        :rtype: int
        """
        return self._broker

    @broker.setter
    def broker(self, broker):
        r"""Sets the broker of this ShowInstanceTopicDetailRespReplicas.

        **参数解释**： 副本所在的节点ID。 **取值范围**： 不涉及

        :param broker: The broker of this ShowInstanceTopicDetailRespReplicas.
        :type broker: int
        """
        self._broker = broker

    @property
    def leader(self):
        r"""Gets the leader of this ShowInstanceTopicDetailRespReplicas.

        **参数解释**： 该副本是否为leader。 **取值范围**： - true：该副本是leader。 - false：该副本不是leader。

        :return: The leader of this ShowInstanceTopicDetailRespReplicas.
        :rtype: bool
        """
        return self._leader

    @leader.setter
    def leader(self, leader):
        r"""Sets the leader of this ShowInstanceTopicDetailRespReplicas.

        **参数解释**： 该副本是否为leader。 **取值范围**： - true：该副本是leader。 - false：该副本不是leader。

        :param leader: The leader of this ShowInstanceTopicDetailRespReplicas.
        :type leader: bool
        """
        self._leader = leader

    @property
    def in_sync(self):
        r"""Gets the in_sync of this ShowInstanceTopicDetailRespReplicas.

        **参数解释**： 该副本是否在ISR副本中。 **取值范围**： - true：在ISR副本中。 - false：不在ISR副本中。

        :return: The in_sync of this ShowInstanceTopicDetailRespReplicas.
        :rtype: bool
        """
        return self._in_sync

    @in_sync.setter
    def in_sync(self, in_sync):
        r"""Sets the in_sync of this ShowInstanceTopicDetailRespReplicas.

        **参数解释**： 该副本是否在ISR副本中。 **取值范围**： - true：在ISR副本中。 - false：不在ISR副本中。

        :param in_sync: The in_sync of this ShowInstanceTopicDetailRespReplicas.
        :type in_sync: bool
        """
        self._in_sync = in_sync

    @property
    def size(self):
        r"""Gets the size of this ShowInstanceTopicDetailRespReplicas.

        **参数解释**： 该副本当前日志大小。单位：Byte。 **取值范围**： 不涉及

        :return: The size of this ShowInstanceTopicDetailRespReplicas.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowInstanceTopicDetailRespReplicas.

        **参数解释**： 该副本当前日志大小。单位：Byte。 **取值范围**： 不涉及

        :param size: The size of this ShowInstanceTopicDetailRespReplicas.
        :type size: int
        """
        self._size = size

    @property
    def lag(self):
        r"""Gets the lag of this ShowInstanceTopicDetailRespReplicas.

        **参数解释**： 该副本当前落后hw的消息数。 **取值范围**： 不涉及

        :return: The lag of this ShowInstanceTopicDetailRespReplicas.
        :rtype: int
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        r"""Sets the lag of this ShowInstanceTopicDetailRespReplicas.

        **参数解释**： 该副本当前落后hw的消息数。 **取值范围**： 不涉及

        :param lag: The lag of this ShowInstanceTopicDetailRespReplicas.
        :type lag: int
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
        if not isinstance(other, ShowInstanceTopicDetailRespReplicas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
