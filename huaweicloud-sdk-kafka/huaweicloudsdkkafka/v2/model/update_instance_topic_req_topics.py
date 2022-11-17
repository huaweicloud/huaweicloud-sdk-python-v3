# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceTopicReqTopics:

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
        'retention_time': 'int',
        'sync_replication': 'bool',
        'sync_message_flush': 'bool',
        'new_partition_numbers': 'int'
    }

    attribute_map = {
        'id': 'id',
        'retention_time': 'retention_time',
        'sync_replication': 'sync_replication',
        'sync_message_flush': 'sync_message_flush',
        'new_partition_numbers': 'new_partition_numbers'
    }

    def __init__(self, id=None, retention_time=None, sync_replication=None, sync_message_flush=None, new_partition_numbers=None):
        """UpdateInstanceTopicReqTopics

        The model defined in huaweicloud sdk

        :param id: topic名称，不支持修改。
        :type id: str
        :param retention_time: 老化时间，单位小时。
        :type retention_time: int
        :param sync_replication: 是否同步复制。
        :type sync_replication: bool
        :param sync_message_flush: 是否同步落盘。
        :type sync_message_flush: bool
        :param new_partition_numbers: 分区数。
        :type new_partition_numbers: int
        """
        
        

        self._id = None
        self._retention_time = None
        self._sync_replication = None
        self._sync_message_flush = None
        self._new_partition_numbers = None
        self.discriminator = None

        self.id = id
        if retention_time is not None:
            self.retention_time = retention_time
        if sync_replication is not None:
            self.sync_replication = sync_replication
        if sync_message_flush is not None:
            self.sync_message_flush = sync_message_flush
        if new_partition_numbers is not None:
            self.new_partition_numbers = new_partition_numbers

    @property
    def id(self):
        """Gets the id of this UpdateInstanceTopicReqTopics.

        topic名称，不支持修改。

        :return: The id of this UpdateInstanceTopicReqTopics.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateInstanceTopicReqTopics.

        topic名称，不支持修改。

        :param id: The id of this UpdateInstanceTopicReqTopics.
        :type id: str
        """
        self._id = id

    @property
    def retention_time(self):
        """Gets the retention_time of this UpdateInstanceTopicReqTopics.

        老化时间，单位小时。

        :return: The retention_time of this UpdateInstanceTopicReqTopics.
        :rtype: int
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        """Sets the retention_time of this UpdateInstanceTopicReqTopics.

        老化时间，单位小时。

        :param retention_time: The retention_time of this UpdateInstanceTopicReqTopics.
        :type retention_time: int
        """
        self._retention_time = retention_time

    @property
    def sync_replication(self):
        """Gets the sync_replication of this UpdateInstanceTopicReqTopics.

        是否同步复制。

        :return: The sync_replication of this UpdateInstanceTopicReqTopics.
        :rtype: bool
        """
        return self._sync_replication

    @sync_replication.setter
    def sync_replication(self, sync_replication):
        """Sets the sync_replication of this UpdateInstanceTopicReqTopics.

        是否同步复制。

        :param sync_replication: The sync_replication of this UpdateInstanceTopicReqTopics.
        :type sync_replication: bool
        """
        self._sync_replication = sync_replication

    @property
    def sync_message_flush(self):
        """Gets the sync_message_flush of this UpdateInstanceTopicReqTopics.

        是否同步落盘。

        :return: The sync_message_flush of this UpdateInstanceTopicReqTopics.
        :rtype: bool
        """
        return self._sync_message_flush

    @sync_message_flush.setter
    def sync_message_flush(self, sync_message_flush):
        """Sets the sync_message_flush of this UpdateInstanceTopicReqTopics.

        是否同步落盘。

        :param sync_message_flush: The sync_message_flush of this UpdateInstanceTopicReqTopics.
        :type sync_message_flush: bool
        """
        self._sync_message_flush = sync_message_flush

    @property
    def new_partition_numbers(self):
        """Gets the new_partition_numbers of this UpdateInstanceTopicReqTopics.

        分区数。

        :return: The new_partition_numbers of this UpdateInstanceTopicReqTopics.
        :rtype: int
        """
        return self._new_partition_numbers

    @new_partition_numbers.setter
    def new_partition_numbers(self, new_partition_numbers):
        """Sets the new_partition_numbers of this UpdateInstanceTopicReqTopics.

        分区数。

        :param new_partition_numbers: The new_partition_numbers of this UpdateInstanceTopicReqTopics.
        :type new_partition_numbers: int
        """
        self._new_partition_numbers = new_partition_numbers

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
        if not isinstance(other, UpdateInstanceTopicReqTopics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
