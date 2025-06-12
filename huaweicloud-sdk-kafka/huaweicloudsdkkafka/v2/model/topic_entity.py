# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopicEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policies_only': 'bool',
        'name': 'str',
        'replication': 'int',
        'partition': 'int',
        'retention_time': 'int',
        'sync_replication': 'bool',
        'sync_message_flush': 'bool',
        'external_configs': 'object',
        'topic_type': 'int',
        'topic_other_configs': 'list[TopicEntityTopicOtherConfigs]',
        'topic_desc': 'str',
        'created_at': 'int'
    }

    attribute_map = {
        'policies_only': 'policiesOnly',
        'name': 'name',
        'replication': 'replication',
        'partition': 'partition',
        'retention_time': 'retention_time',
        'sync_replication': 'sync_replication',
        'sync_message_flush': 'sync_message_flush',
        'external_configs': 'external_configs',
        'topic_type': 'topic_type',
        'topic_other_configs': 'topic_other_configs',
        'topic_desc': 'topic_desc',
        'created_at': 'created_at'
    }

    def __init__(self, policies_only=None, name=None, replication=None, partition=None, retention_time=None, sync_replication=None, sync_message_flush=None, external_configs=None, topic_type=None, topic_other_configs=None, topic_desc=None, created_at=None):
        r"""TopicEntity

        The model defined in huaweicloud sdk

        :param policies_only: **参数解释**： 是否为默认策略。 **取值范围**： - true：默认策略。 - false：不是默认策略。
        :type policies_only: bool
        :param name: **参数解释**： Topic名称。 **取值范围**： 不涉及
        :type name: str
        :param replication: **参数解释**： 副本数，配置数据的可靠性。 **取值范围**： 不涉及
        :type replication: int
        :param partition: **参数解释**： Topic分区数，设置消费的并发数。 **取值范围**： 不涉及
        :type partition: int
        :param retention_time: **参数解释**： 消息老化时间。 **取值范围**： 0-720
        :type retention_time: int
        :param sync_replication: **参数解释**： 是否开启同步复制，默认关闭。 **取值范围**： - true：开启，客户端生产消息时相应的也要设置acks&#x3D;-1，否则不生效。 - false：关闭。
        :type sync_replication: bool
        :param sync_message_flush: **参数解释**： 是否使用同步落盘。默认值为false。同步落盘会导致性能降低。 **取值范围**： - true：同步落盘。 - false：不同步落盘。
        :type sync_message_flush: bool
        :param external_configs: **参数解释**： 扩展配置。
        :type external_configs: object
        :param topic_type: **参数解释**： Topic类型。 **取值范围**： - 0：普通Topic。 - 1：系统(内部)Topic。
        :type topic_type: int
        :param topic_other_configs: **参数解释**： Topic其他配置。
        :type topic_other_configs: list[:class:`huaweicloudsdkkafka.v2.TopicEntityTopicOtherConfigs`]
        :param topic_desc: **参数解释**： Topic描述。 **取值范围**： 不涉及
        :type topic_desc: str
        :param created_at: **参数解释**： Topic创建时间。 **取值范围**： 不涉及
        :type created_at: int
        """
        
        

        self._policies_only = None
        self._name = None
        self._replication = None
        self._partition = None
        self._retention_time = None
        self._sync_replication = None
        self._sync_message_flush = None
        self._external_configs = None
        self._topic_type = None
        self._topic_other_configs = None
        self._topic_desc = None
        self._created_at = None
        self.discriminator = None

        if policies_only is not None:
            self.policies_only = policies_only
        if name is not None:
            self.name = name
        if replication is not None:
            self.replication = replication
        if partition is not None:
            self.partition = partition
        if retention_time is not None:
            self.retention_time = retention_time
        if sync_replication is not None:
            self.sync_replication = sync_replication
        if sync_message_flush is not None:
            self.sync_message_flush = sync_message_flush
        if external_configs is not None:
            self.external_configs = external_configs
        if topic_type is not None:
            self.topic_type = topic_type
        if topic_other_configs is not None:
            self.topic_other_configs = topic_other_configs
        if topic_desc is not None:
            self.topic_desc = topic_desc
        if created_at is not None:
            self.created_at = created_at

    @property
    def policies_only(self):
        r"""Gets the policies_only of this TopicEntity.

        **参数解释**： 是否为默认策略。 **取值范围**： - true：默认策略。 - false：不是默认策略。

        :return: The policies_only of this TopicEntity.
        :rtype: bool
        """
        return self._policies_only

    @policies_only.setter
    def policies_only(self, policies_only):
        r"""Sets the policies_only of this TopicEntity.

        **参数解释**： 是否为默认策略。 **取值范围**： - true：默认策略。 - false：不是默认策略。

        :param policies_only: The policies_only of this TopicEntity.
        :type policies_only: bool
        """
        self._policies_only = policies_only

    @property
    def name(self):
        r"""Gets the name of this TopicEntity.

        **参数解释**： Topic名称。 **取值范围**： 不涉及

        :return: The name of this TopicEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TopicEntity.

        **参数解释**： Topic名称。 **取值范围**： 不涉及

        :param name: The name of this TopicEntity.
        :type name: str
        """
        self._name = name

    @property
    def replication(self):
        r"""Gets the replication of this TopicEntity.

        **参数解释**： 副本数，配置数据的可靠性。 **取值范围**： 不涉及

        :return: The replication of this TopicEntity.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        r"""Sets the replication of this TopicEntity.

        **参数解释**： 副本数，配置数据的可靠性。 **取值范围**： 不涉及

        :param replication: The replication of this TopicEntity.
        :type replication: int
        """
        self._replication = replication

    @property
    def partition(self):
        r"""Gets the partition of this TopicEntity.

        **参数解释**： Topic分区数，设置消费的并发数。 **取值范围**： 不涉及

        :return: The partition of this TopicEntity.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        r"""Sets the partition of this TopicEntity.

        **参数解释**： Topic分区数，设置消费的并发数。 **取值范围**： 不涉及

        :param partition: The partition of this TopicEntity.
        :type partition: int
        """
        self._partition = partition

    @property
    def retention_time(self):
        r"""Gets the retention_time of this TopicEntity.

        **参数解释**： 消息老化时间。 **取值范围**： 0-720

        :return: The retention_time of this TopicEntity.
        :rtype: int
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        r"""Sets the retention_time of this TopicEntity.

        **参数解释**： 消息老化时间。 **取值范围**： 0-720

        :param retention_time: The retention_time of this TopicEntity.
        :type retention_time: int
        """
        self._retention_time = retention_time

    @property
    def sync_replication(self):
        r"""Gets the sync_replication of this TopicEntity.

        **参数解释**： 是否开启同步复制，默认关闭。 **取值范围**： - true：开启，客户端生产消息时相应的也要设置acks=-1，否则不生效。 - false：关闭。

        :return: The sync_replication of this TopicEntity.
        :rtype: bool
        """
        return self._sync_replication

    @sync_replication.setter
    def sync_replication(self, sync_replication):
        r"""Sets the sync_replication of this TopicEntity.

        **参数解释**： 是否开启同步复制，默认关闭。 **取值范围**： - true：开启，客户端生产消息时相应的也要设置acks=-1，否则不生效。 - false：关闭。

        :param sync_replication: The sync_replication of this TopicEntity.
        :type sync_replication: bool
        """
        self._sync_replication = sync_replication

    @property
    def sync_message_flush(self):
        r"""Gets the sync_message_flush of this TopicEntity.

        **参数解释**： 是否使用同步落盘。默认值为false。同步落盘会导致性能降低。 **取值范围**： - true：同步落盘。 - false：不同步落盘。

        :return: The sync_message_flush of this TopicEntity.
        :rtype: bool
        """
        return self._sync_message_flush

    @sync_message_flush.setter
    def sync_message_flush(self, sync_message_flush):
        r"""Sets the sync_message_flush of this TopicEntity.

        **参数解释**： 是否使用同步落盘。默认值为false。同步落盘会导致性能降低。 **取值范围**： - true：同步落盘。 - false：不同步落盘。

        :param sync_message_flush: The sync_message_flush of this TopicEntity.
        :type sync_message_flush: bool
        """
        self._sync_message_flush = sync_message_flush

    @property
    def external_configs(self):
        r"""Gets the external_configs of this TopicEntity.

        **参数解释**： 扩展配置。

        :return: The external_configs of this TopicEntity.
        :rtype: object
        """
        return self._external_configs

    @external_configs.setter
    def external_configs(self, external_configs):
        r"""Sets the external_configs of this TopicEntity.

        **参数解释**： 扩展配置。

        :param external_configs: The external_configs of this TopicEntity.
        :type external_configs: object
        """
        self._external_configs = external_configs

    @property
    def topic_type(self):
        r"""Gets the topic_type of this TopicEntity.

        **参数解释**： Topic类型。 **取值范围**： - 0：普通Topic。 - 1：系统(内部)Topic。

        :return: The topic_type of this TopicEntity.
        :rtype: int
        """
        return self._topic_type

    @topic_type.setter
    def topic_type(self, topic_type):
        r"""Sets the topic_type of this TopicEntity.

        **参数解释**： Topic类型。 **取值范围**： - 0：普通Topic。 - 1：系统(内部)Topic。

        :param topic_type: The topic_type of this TopicEntity.
        :type topic_type: int
        """
        self._topic_type = topic_type

    @property
    def topic_other_configs(self):
        r"""Gets the topic_other_configs of this TopicEntity.

        **参数解释**： Topic其他配置。

        :return: The topic_other_configs of this TopicEntity.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.TopicEntityTopicOtherConfigs`]
        """
        return self._topic_other_configs

    @topic_other_configs.setter
    def topic_other_configs(self, topic_other_configs):
        r"""Sets the topic_other_configs of this TopicEntity.

        **参数解释**： Topic其他配置。

        :param topic_other_configs: The topic_other_configs of this TopicEntity.
        :type topic_other_configs: list[:class:`huaweicloudsdkkafka.v2.TopicEntityTopicOtherConfigs`]
        """
        self._topic_other_configs = topic_other_configs

    @property
    def topic_desc(self):
        r"""Gets the topic_desc of this TopicEntity.

        **参数解释**： Topic描述。 **取值范围**： 不涉及

        :return: The topic_desc of this TopicEntity.
        :rtype: str
        """
        return self._topic_desc

    @topic_desc.setter
    def topic_desc(self, topic_desc):
        r"""Sets the topic_desc of this TopicEntity.

        **参数解释**： Topic描述。 **取值范围**： 不涉及

        :param topic_desc: The topic_desc of this TopicEntity.
        :type topic_desc: str
        """
        self._topic_desc = topic_desc

    @property
    def created_at(self):
        r"""Gets the created_at of this TopicEntity.

        **参数解释**： Topic创建时间。 **取值范围**： 不涉及

        :return: The created_at of this TopicEntity.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this TopicEntity.

        **参数解释**： Topic创建时间。 **取值范围**： 不涉及

        :param created_at: The created_at of this TopicEntity.
        :type created_at: int
        """
        self._created_at = created_at

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
        if not isinstance(other, TopicEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
