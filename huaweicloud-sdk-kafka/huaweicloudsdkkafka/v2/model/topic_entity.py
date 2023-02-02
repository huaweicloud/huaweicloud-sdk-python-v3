# coding: utf-8

import re
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
        'topic_type': 'int'
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
        'topic_type': 'topic_type'
    }

    def __init__(self, policies_only=None, name=None, replication=None, partition=None, retention_time=None, sync_replication=None, sync_message_flush=None, external_configs=None, topic_type=None):
        """TopicEntity

        The model defined in huaweicloud sdk

        :param policies_only: 是否为默认策略。
        :type policies_only: bool
        :param name: topic名称。
        :type name: str
        :param replication: 副本数，配置数据的可靠性。
        :type replication: int
        :param partition: topic分区数，设置消费的并发数。
        :type partition: int
        :param retention_time: 消息老化时间。
        :type retention_time: int
        :param sync_replication: 是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks&#x3D;-1，否则不生效，默认关闭。
        :type sync_replication: bool
        :param sync_message_flush: 是否使用同步落盘。默认值为false。同步落盘会导致性能降低。
        :type sync_message_flush: bool
        :param external_configs: 扩展配置。
        :type external_configs: object
        :param topic_type: topic类型(0:普通Topic 1:系统(内部)Topic)。
        :type topic_type: int
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

    @property
    def policies_only(self):
        """Gets the policies_only of this TopicEntity.

        是否为默认策略。

        :return: The policies_only of this TopicEntity.
        :rtype: bool
        """
        return self._policies_only

    @policies_only.setter
    def policies_only(self, policies_only):
        """Sets the policies_only of this TopicEntity.

        是否为默认策略。

        :param policies_only: The policies_only of this TopicEntity.
        :type policies_only: bool
        """
        self._policies_only = policies_only

    @property
    def name(self):
        """Gets the name of this TopicEntity.

        topic名称。

        :return: The name of this TopicEntity.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TopicEntity.

        topic名称。

        :param name: The name of this TopicEntity.
        :type name: str
        """
        self._name = name

    @property
    def replication(self):
        """Gets the replication of this TopicEntity.

        副本数，配置数据的可靠性。

        :return: The replication of this TopicEntity.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        """Sets the replication of this TopicEntity.

        副本数，配置数据的可靠性。

        :param replication: The replication of this TopicEntity.
        :type replication: int
        """
        self._replication = replication

    @property
    def partition(self):
        """Gets the partition of this TopicEntity.

        topic分区数，设置消费的并发数。

        :return: The partition of this TopicEntity.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this TopicEntity.

        topic分区数，设置消费的并发数。

        :param partition: The partition of this TopicEntity.
        :type partition: int
        """
        self._partition = partition

    @property
    def retention_time(self):
        """Gets the retention_time of this TopicEntity.

        消息老化时间。

        :return: The retention_time of this TopicEntity.
        :rtype: int
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        """Sets the retention_time of this TopicEntity.

        消息老化时间。

        :param retention_time: The retention_time of this TopicEntity.
        :type retention_time: int
        """
        self._retention_time = retention_time

    @property
    def sync_replication(self):
        """Gets the sync_replication of this TopicEntity.

        是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks=-1，否则不生效，默认关闭。

        :return: The sync_replication of this TopicEntity.
        :rtype: bool
        """
        return self._sync_replication

    @sync_replication.setter
    def sync_replication(self, sync_replication):
        """Sets the sync_replication of this TopicEntity.

        是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks=-1，否则不生效，默认关闭。

        :param sync_replication: The sync_replication of this TopicEntity.
        :type sync_replication: bool
        """
        self._sync_replication = sync_replication

    @property
    def sync_message_flush(self):
        """Gets the sync_message_flush of this TopicEntity.

        是否使用同步落盘。默认值为false。同步落盘会导致性能降低。

        :return: The sync_message_flush of this TopicEntity.
        :rtype: bool
        """
        return self._sync_message_flush

    @sync_message_flush.setter
    def sync_message_flush(self, sync_message_flush):
        """Sets the sync_message_flush of this TopicEntity.

        是否使用同步落盘。默认值为false。同步落盘会导致性能降低。

        :param sync_message_flush: The sync_message_flush of this TopicEntity.
        :type sync_message_flush: bool
        """
        self._sync_message_flush = sync_message_flush

    @property
    def external_configs(self):
        """Gets the external_configs of this TopicEntity.

        扩展配置。

        :return: The external_configs of this TopicEntity.
        :rtype: object
        """
        return self._external_configs

    @external_configs.setter
    def external_configs(self, external_configs):
        """Sets the external_configs of this TopicEntity.

        扩展配置。

        :param external_configs: The external_configs of this TopicEntity.
        :type external_configs: object
        """
        self._external_configs = external_configs

    @property
    def topic_type(self):
        """Gets the topic_type of this TopicEntity.

        topic类型(0:普通Topic 1:系统(内部)Topic)。

        :return: The topic_type of this TopicEntity.
        :rtype: int
        """
        return self._topic_type

    @topic_type.setter
    def topic_type(self, topic_type):
        """Sets the topic_type of this TopicEntity.

        topic类型(0:普通Topic 1:系统(内部)Topic)。

        :param topic_type: The topic_type of this TopicEntity.
        :type topic_type: int
        """
        self._topic_type = topic_type

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
