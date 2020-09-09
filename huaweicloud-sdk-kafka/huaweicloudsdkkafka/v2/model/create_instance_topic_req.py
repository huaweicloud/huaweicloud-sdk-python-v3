# coding: utf-8

import pprint
import re

import six





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
        'name': 'str',
        'replication': 'int',
        'sync_message_flush': 'bool',
        'partition': 'int',
        'sync_replication': 'bool',
        'retention_time': 'int'
    }

    attribute_map = {
        'name': 'name',
        'replication': 'replication',
        'sync_message_flush': 'sync_message_flush',
        'partition': 'partition',
        'sync_replication': 'sync_replication',
        'retention_time': 'retention_time'
    }

    def __init__(self, name=None, replication=None, sync_message_flush=None, partition=None, sync_replication=None, retention_time=None):
        """CreateInstanceTopicReq - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._replication = None
        self._sync_message_flush = None
        self._partition = None
        self._sync_replication = None
        self._retention_time = None
        self.discriminator = None

        self.name = name
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

    @property
    def name(self):
        """Gets the name of this CreateInstanceTopicReq.

        topic名称，长度为4-64，以字母开头且只支持大小写字母、中横线、下划线以及数字。

        :return: The name of this CreateInstanceTopicReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInstanceTopicReq.

        topic名称，长度为4-64，以字母开头且只支持大小写字母、中横线、下划线以及数字。

        :param name: The name of this CreateInstanceTopicReq.
        :type: str
        """
        self._name = name

    @property
    def replication(self):
        """Gets the replication of this CreateInstanceTopicReq.

        副本数，配置数据的可靠性。 取值范围：1-3。

        :return: The replication of this CreateInstanceTopicReq.
        :rtype: int
        """
        return self._replication

    @replication.setter
    def replication(self, replication):
        """Sets the replication of this CreateInstanceTopicReq.

        副本数，配置数据的可靠性。 取值范围：1-3。

        :param replication: The replication of this CreateInstanceTopicReq.
        :type: int
        """
        self._replication = replication

    @property
    def sync_message_flush(self):
        """Gets the sync_message_flush of this CreateInstanceTopicReq.

        是否使用同步落盘。默认值为false。同步落盘会导致性能降低。

        :return: The sync_message_flush of this CreateInstanceTopicReq.
        :rtype: bool
        """
        return self._sync_message_flush

    @sync_message_flush.setter
    def sync_message_flush(self, sync_message_flush):
        """Sets the sync_message_flush of this CreateInstanceTopicReq.

        是否使用同步落盘。默认值为false。同步落盘会导致性能降低。

        :param sync_message_flush: The sync_message_flush of this CreateInstanceTopicReq.
        :type: bool
        """
        self._sync_message_flush = sync_message_flush

    @property
    def partition(self):
        """Gets the partition of this CreateInstanceTopicReq.

        topic分区数，设置消费的并发数。 取值范围：1-20。

        :return: The partition of this CreateInstanceTopicReq.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this CreateInstanceTopicReq.

        topic分区数，设置消费的并发数。 取值范围：1-20。

        :param partition: The partition of this CreateInstanceTopicReq.
        :type: int
        """
        self._partition = partition

    @property
    def sync_replication(self):
        """Gets the sync_replication of this CreateInstanceTopicReq.

        是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks=-1，否则不生效，默认关闭。

        :return: The sync_replication of this CreateInstanceTopicReq.
        :rtype: bool
        """
        return self._sync_replication

    @sync_replication.setter
    def sync_replication(self, sync_replication):
        """Sets the sync_replication of this CreateInstanceTopicReq.

        是否开启同步复制，开启后，客户端生产消息时相应的也要设置acks=-1，否则不生效，默认关闭。

        :param sync_replication: The sync_replication of this CreateInstanceTopicReq.
        :type: bool
        """
        self._sync_replication = sync_replication

    @property
    def retention_time(self):
        """Gets the retention_time of this CreateInstanceTopicReq.

        消息老化时间。默认值为72。取值范围1~168，单位小时。

        :return: The retention_time of this CreateInstanceTopicReq.
        :rtype: int
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        """Sets the retention_time of this CreateInstanceTopicReq.

        消息老化时间。默认值为72。取值范围1~168，单位小时。

        :param retention_time: The retention_time of this CreateInstanceTopicReq.
        :type: int
        """
        self._retention_time = retention_time

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
        if not isinstance(other, CreateInstanceTopicReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
