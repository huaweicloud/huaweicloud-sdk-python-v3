# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceTopicReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'replication': 'int',
        'sync_message_flush': 'bool',
        'partition': 'int',
        'sync_replication': 'bool',
        'retention_time': 'int',
        'topic_other_configs': 'list[CreateInstanceTopicReqTopicOtherConfigs]',
        'topic_desc': 'str'
    }

    attribute_map = {
        'id': 'id',
        'replication': 'replication',
        'sync_message_flush': 'sync_message_flush',
        'partition': 'partition',
        'sync_replication': 'sync_replication',
        'retention_time': 'retention_time',
        'topic_other_configs': 'topic_other_configs',
        'topic_desc': 'topic_desc'
    }

    def __init__(self, id=None, replication=None, sync_message_flush=None, partition=None, sync_replication=None, retention_time=None, topic_other_configs=None, topic_desc=None):
        r"""CreateInstanceTopicReq

        The model defined in huaweicloud sdk

        :param id: **参数解释**： Topic名称。 **约束限制**： 长度为3-200，以字母开头且只支持大小写字母、中横线、下划线、点以及数字。 **取值范围**： 不涉及 **默认取值**： 不涉及。 
        :type id: str
        :param replication: **参数解释**： 副本数，配置数据的可靠性。副本数和代理数有关，如果有3个代理，最大副本数是3。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。 
        :type replication: int
        :param sync_message_flush: **参数解释**： 是否使用同步落盘，同步落盘会导致性能降低。 **约束限制**： 不涉及。 **取值范围**： - true：同步落盘。 - false：不使用同步落盘。 **默认取值**： false
        :type sync_message_flush: bool
        :param partition: **参数解释**： Topic分区数，设置消费的并发数。 **约束限制**： 不涉及。 **取值范围**： 1-200。 **默认取值**： 不涉及。 
        :type partition: int
        :param sync_replication: **参数解释**： 是否开启同步复制。 **约束限制**： 不涉及。 **取值范围**： - true：开启。开启后，客户端生产消息时相应的也要设置acks&#x3D;-1，否则不生效。 - false：不开启。 **默认取值**： false。 
        :type sync_replication: bool
        :param retention_time: **参数解释**： 消息老化时间。 **约束限制**： 不涉及。 **取值范围**： 1-720 **默认取值**： 72
        :type retention_time: int
        :param topic_other_configs: **参数解释**： Topic配置
        :type topic_other_configs: list[:class:`huaweicloudsdkkafka.v2.CreateInstanceTopicReqTopicOtherConfigs`]
        :param topic_desc: **参数解释**： Topic描述。 **约束限制**： 不涉及。 **取值范围**： 0-200个字符。 **默认取值**： 不涉及。  
        :type topic_desc: str
        """
        
        

        self._id = None
        self._replication = None
        self._sync_message_flush = None
        self._partition = None
        self._sync_replication = None
        self._retention_time = None
        self._topic_other_configs = None
        self._topic_desc = None
        self.discriminator = None

        self.id = id
        if replication is not None:
            self.replication = replication
        if sync_message_flush is not None:
            self.sync_message_flush = sync_message_flush
        if partition is not None:
            self.partition = partition
        if sync_replication is not None:
            self.sync_replication = sync_replication
        if retention_time is not None:
            self.retention_time = retention_time
        if topic_other_configs is not None:
            self.topic_other_configs = topic_other_configs
        if topic_desc is not None:
            self.topic_desc = topic_desc

    @property
    def id(self):
        r"""Gets the id of this CreateInstanceTopicReq.

        **参数解释**： Topic名称。 **约束限制**： 长度为3-200，以字母开头且只支持大小写字母、中横线、下划线、点以及数字。 **取值范围**： 不涉及 **默认取值**： 不涉及。 

        :return: The id of this CreateInstanceTopicReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateInstanceTopicReq.

        **参数解释**： Topic名称。 **约束限制**： 长度为3-200，以字母开头且只支持大小写字母、中横线、下划线、点以及数字。 **取值范围**： 不涉及 **默认取值**： 不涉及。 

        :param id: The id of this CreateInstanceTopicReq.
        :type id: str
        """
        self._id = id

    @property
    def replication(self):
        r"""Gets the replication of this CreateInstanceTopicReq.

        **参数解释**： 副本数，配置数据的可靠性。副本数和代理数有关，如果有3个代理，最大副本数是3。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。 

        :return: The replication of this CreateInstanceTopicReq.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        r"""Sets the replication of this CreateInstanceTopicReq.

        **参数解释**： 副本数，配置数据的可靠性。副本数和代理数有关，如果有3个代理，最大副本数是3。 **约束限制**： 不涉及。 **取值范围**： 不涉及 **默认取值**： 不涉及。 

        :param replication: The replication of this CreateInstanceTopicReq.
        :type replication: int
        """
        self._replication = replication

    @property
    def sync_message_flush(self):
        r"""Gets the sync_message_flush of this CreateInstanceTopicReq.

        **参数解释**： 是否使用同步落盘，同步落盘会导致性能降低。 **约束限制**： 不涉及。 **取值范围**： - true：同步落盘。 - false：不使用同步落盘。 **默认取值**： false

        :return: The sync_message_flush of this CreateInstanceTopicReq.
        :rtype: bool
        """
        return self._sync_message_flush

    @sync_message_flush.setter
    def sync_message_flush(self, sync_message_flush):
        r"""Sets the sync_message_flush of this CreateInstanceTopicReq.

        **参数解释**： 是否使用同步落盘，同步落盘会导致性能降低。 **约束限制**： 不涉及。 **取值范围**： - true：同步落盘。 - false：不使用同步落盘。 **默认取值**： false

        :param sync_message_flush: The sync_message_flush of this CreateInstanceTopicReq.
        :type sync_message_flush: bool
        """
        self._sync_message_flush = sync_message_flush

    @property
    def partition(self):
        r"""Gets the partition of this CreateInstanceTopicReq.

        **参数解释**： Topic分区数，设置消费的并发数。 **约束限制**： 不涉及。 **取值范围**： 1-200。 **默认取值**： 不涉及。 

        :return: The partition of this CreateInstanceTopicReq.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this CreateInstanceTopicReq.

        **参数解释**： Topic分区数，设置消费的并发数。 **约束限制**： 不涉及。 **取值范围**： 1-200。 **默认取值**： 不涉及。 

        :param partition: The partition of this CreateInstanceTopicReq.
        :type partition: int
        """
        self._partition = partition

    @property
    def sync_replication(self):
        r"""Gets the sync_replication of this CreateInstanceTopicReq.

        **参数解释**： 是否开启同步复制。 **约束限制**： 不涉及。 **取值范围**： - true：开启。开启后，客户端生产消息时相应的也要设置acks=-1，否则不生效。 - false：不开启。 **默认取值**： false。 

        :return: The sync_replication of this CreateInstanceTopicReq.
        :rtype: bool
        """
        return self._sync_replication

    @sync_replication.setter
    def sync_replication(self, sync_replication):
        r"""Sets the sync_replication of this CreateInstanceTopicReq.

        **参数解释**： 是否开启同步复制。 **约束限制**： 不涉及。 **取值范围**： - true：开启。开启后，客户端生产消息时相应的也要设置acks=-1，否则不生效。 - false：不开启。 **默认取值**： false。 

        :param sync_replication: The sync_replication of this CreateInstanceTopicReq.
        :type sync_replication: bool
        """
        self._sync_replication = sync_replication

    @property
    def retention_time(self):
        r"""Gets the retention_time of this CreateInstanceTopicReq.

        **参数解释**： 消息老化时间。 **约束限制**： 不涉及。 **取值范围**： 1-720 **默认取值**： 72

        :return: The retention_time of this CreateInstanceTopicReq.
        :rtype: int
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        r"""Sets the retention_time of this CreateInstanceTopicReq.

        **参数解释**： 消息老化时间。 **约束限制**： 不涉及。 **取值范围**： 1-720 **默认取值**： 72

        :param retention_time: The retention_time of this CreateInstanceTopicReq.
        :type retention_time: int
        """
        self._retention_time = retention_time

    @property
    def topic_other_configs(self):
        r"""Gets the topic_other_configs of this CreateInstanceTopicReq.

        **参数解释**： Topic配置

        :return: The topic_other_configs of this CreateInstanceTopicReq.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.CreateInstanceTopicReqTopicOtherConfigs`]
        """
        return self._topic_other_configs

    @topic_other_configs.setter
    def topic_other_configs(self, topic_other_configs):
        r"""Sets the topic_other_configs of this CreateInstanceTopicReq.

        **参数解释**： Topic配置

        :param topic_other_configs: The topic_other_configs of this CreateInstanceTopicReq.
        :type topic_other_configs: list[:class:`huaweicloudsdkkafka.v2.CreateInstanceTopicReqTopicOtherConfigs`]
        """
        self._topic_other_configs = topic_other_configs

    @property
    def topic_desc(self):
        r"""Gets the topic_desc of this CreateInstanceTopicReq.

        **参数解释**： Topic描述。 **约束限制**： 不涉及。 **取值范围**： 0-200个字符。 **默认取值**： 不涉及。  

        :return: The topic_desc of this CreateInstanceTopicReq.
        :rtype: str
        """
        return self._topic_desc

    @topic_desc.setter
    def topic_desc(self, topic_desc):
        r"""Sets the topic_desc of this CreateInstanceTopicReq.

        **参数解释**： Topic描述。 **约束限制**： 不涉及。 **取值范围**： 0-200个字符。 **默认取值**： 不涉及。  

        :param topic_desc: The topic_desc of this CreateInstanceTopicReq.
        :type topic_desc: str
        """
        self._topic_desc = topic_desc

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
        if not isinstance(other, CreateInstanceTopicReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
