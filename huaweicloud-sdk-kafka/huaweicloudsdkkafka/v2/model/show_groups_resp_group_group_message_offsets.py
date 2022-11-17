# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupsRespGroupGroupMessageOffsets:

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
        'lag': 'int',
        'topic': 'str',
        'message_current_offset': 'int',
        'message_log_end_offset': 'int'
    }

    attribute_map = {
        'partition': 'partition',
        'lag': 'lag',
        'topic': 'topic',
        'message_current_offset': 'message_current_offset',
        'message_log_end_offset': 'message_log_end_offset'
    }

    def __init__(self, partition=None, lag=None, topic=None, message_current_offset=None, message_log_end_offset=None):
        """ShowGroupsRespGroupGroupMessageOffsets

        The model defined in huaweicloud sdk

        :param partition: 分区编号。
        :type partition: int
        :param lag: 剩余可消费消息数，即消息堆积数。
        :type lag: int
        :param topic: topic名称。
        :type topic: str
        :param message_current_offset: 当前消费进度。
        :type message_current_offset: int
        :param message_log_end_offset: 最大消息位置（LEO）。
        :type message_log_end_offset: int
        """
        
        

        self._partition = None
        self._lag = None
        self._topic = None
        self._message_current_offset = None
        self._message_log_end_offset = None
        self.discriminator = None

        if partition is not None:
            self.partition = partition
        if lag is not None:
            self.lag = lag
        if topic is not None:
            self.topic = topic
        if message_current_offset is not None:
            self.message_current_offset = message_current_offset
        if message_log_end_offset is not None:
            self.message_log_end_offset = message_log_end_offset

    @property
    def partition(self):
        """Gets the partition of this ShowGroupsRespGroupGroupMessageOffsets.

        分区编号。

        :return: The partition of this ShowGroupsRespGroupGroupMessageOffsets.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this ShowGroupsRespGroupGroupMessageOffsets.

        分区编号。

        :param partition: The partition of this ShowGroupsRespGroupGroupMessageOffsets.
        :type partition: int
        """
        self._partition = partition

    @property
    def lag(self):
        """Gets the lag of this ShowGroupsRespGroupGroupMessageOffsets.

        剩余可消费消息数，即消息堆积数。

        :return: The lag of this ShowGroupsRespGroupGroupMessageOffsets.
        :rtype: int
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        """Sets the lag of this ShowGroupsRespGroupGroupMessageOffsets.

        剩余可消费消息数，即消息堆积数。

        :param lag: The lag of this ShowGroupsRespGroupGroupMessageOffsets.
        :type lag: int
        """
        self._lag = lag

    @property
    def topic(self):
        """Gets the topic of this ShowGroupsRespGroupGroupMessageOffsets.

        topic名称。

        :return: The topic of this ShowGroupsRespGroupGroupMessageOffsets.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowGroupsRespGroupGroupMessageOffsets.

        topic名称。

        :param topic: The topic of this ShowGroupsRespGroupGroupMessageOffsets.
        :type topic: str
        """
        self._topic = topic

    @property
    def message_current_offset(self):
        """Gets the message_current_offset of this ShowGroupsRespGroupGroupMessageOffsets.

        当前消费进度。

        :return: The message_current_offset of this ShowGroupsRespGroupGroupMessageOffsets.
        :rtype: int
        """
        return self._message_current_offset

    @message_current_offset.setter
    def message_current_offset(self, message_current_offset):
        """Sets the message_current_offset of this ShowGroupsRespGroupGroupMessageOffsets.

        当前消费进度。

        :param message_current_offset: The message_current_offset of this ShowGroupsRespGroupGroupMessageOffsets.
        :type message_current_offset: int
        """
        self._message_current_offset = message_current_offset

    @property
    def message_log_end_offset(self):
        """Gets the message_log_end_offset of this ShowGroupsRespGroupGroupMessageOffsets.

        最大消息位置（LEO）。

        :return: The message_log_end_offset of this ShowGroupsRespGroupGroupMessageOffsets.
        :rtype: int
        """
        return self._message_log_end_offset

    @message_log_end_offset.setter
    def message_log_end_offset(self, message_log_end_offset):
        """Sets the message_log_end_offset of this ShowGroupsRespGroupGroupMessageOffsets.

        最大消息位置（LEO）。

        :param message_log_end_offset: The message_log_end_offset of this ShowGroupsRespGroupGroupMessageOffsets.
        :type message_log_end_offset: int
        """
        self._message_log_end_offset = message_log_end_offset

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
        if not isinstance(other, ShowGroupsRespGroupGroupMessageOffsets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
