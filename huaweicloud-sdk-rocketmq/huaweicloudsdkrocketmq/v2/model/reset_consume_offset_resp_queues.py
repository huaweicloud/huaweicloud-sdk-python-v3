# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetConsumeOffsetRespQueues:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'broker_name': 'str',
        'queue_id': 'int',
        'timestamp_offset': 'int'
    }

    attribute_map = {
        'broker_name': 'broker_name',
        'queue_id': 'queue_id',
        'timestamp_offset': 'timestamp_offset'
    }

    def __init__(self, broker_name=None, queue_id=None, timestamp_offset=None):
        """ResetConsumeOffsetRespQueues

        The model defined in huaweicloud sdk

        :param broker_name: 队列所在的broker。
        :type broker_name: str
        :param queue_id: 队列ID。
        :type queue_id: int
        :param timestamp_offset: 重置消费进度。
        :type timestamp_offset: int
        """
        
        

        self._broker_name = None
        self._queue_id = None
        self._timestamp_offset = None
        self.discriminator = None

        if broker_name is not None:
            self.broker_name = broker_name
        if queue_id is not None:
            self.queue_id = queue_id
        if timestamp_offset is not None:
            self.timestamp_offset = timestamp_offset

    @property
    def broker_name(self):
        """Gets the broker_name of this ResetConsumeOffsetRespQueues.

        队列所在的broker。

        :return: The broker_name of this ResetConsumeOffsetRespQueues.
        :rtype: str
        """
        return self._broker_name

    @broker_name.setter
    def broker_name(self, broker_name):
        """Sets the broker_name of this ResetConsumeOffsetRespQueues.

        队列所在的broker。

        :param broker_name: The broker_name of this ResetConsumeOffsetRespQueues.
        :type broker_name: str
        """
        self._broker_name = broker_name

    @property
    def queue_id(self):
        """Gets the queue_id of this ResetConsumeOffsetRespQueues.

        队列ID。

        :return: The queue_id of this ResetConsumeOffsetRespQueues.
        :rtype: int
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this ResetConsumeOffsetRespQueues.

        队列ID。

        :param queue_id: The queue_id of this ResetConsumeOffsetRespQueues.
        :type queue_id: int
        """
        self._queue_id = queue_id

    @property
    def timestamp_offset(self):
        """Gets the timestamp_offset of this ResetConsumeOffsetRespQueues.

        重置消费进度。

        :return: The timestamp_offset of this ResetConsumeOffsetRespQueues.
        :rtype: int
        """
        return self._timestamp_offset

    @timestamp_offset.setter
    def timestamp_offset(self, timestamp_offset):
        """Sets the timestamp_offset of this ResetConsumeOffsetRespQueues.

        重置消费进度。

        :param timestamp_offset: The timestamp_offset of this ResetConsumeOffsetRespQueues.
        :type timestamp_offset: int
        """
        self._timestamp_offset = timestamp_offset

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
        if not isinstance(other, ResetConsumeOffsetRespQueues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
