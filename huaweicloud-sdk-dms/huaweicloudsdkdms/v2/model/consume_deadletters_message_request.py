# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsumeDeadlettersMessageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queue_id': 'str',
        'consumer_group_id': 'str',
        'max_msgs': 'int',
        'time_wait': 'int',
        'ack_wait': 'int'
    }

    attribute_map = {
        'queue_id': 'queue_id',
        'consumer_group_id': 'consumer_group_id',
        'max_msgs': 'max_msgs',
        'time_wait': 'time_wait',
        'ack_wait': 'ack_wait'
    }

    def __init__(self, queue_id=None, consumer_group_id=None, max_msgs=None, time_wait=None, ack_wait=None):
        """ConsumeDeadlettersMessageRequest

        The model defined in huaweicloud sdk

        :param queue_id: 指定的队列ID。
        :type queue_id: str
        :param consumer_group_id: 消费组的ID。
        :type consumer_group_id: str
        :param max_msgs: 获取可消费的死信消息的条数。  &gt;单次消费返回的消息数量可能会少于指定条数，但多次消费最终可获取全部消息。  取值范围：1~10。  默认值：10
        :type max_msgs: int
        :param time_wait: 设定消费组中可消费的死信为0时的读取消息等待时间。  如果在等待时间内有新的死信消息，则立即返回消费结果，如果等待时间内没有新的死信消息，则到等待时间后返回消费结果。  取值范围：1~60s  默认值：3s  说明：不带该参数或者配置为空，都默认为3s。
        :type time_wait: int
        :param ack_wait: commit提交超时时间，在该时间内提交确认，确认有效，如果超过指定时间，系统会报消息确认超时，或handler无效。  取值范围：15~300s  默认值：30s  说明：不带该参数或者配置为空，都默认为30s。
        :type ack_wait: int
        """
        
        

        self._queue_id = None
        self._consumer_group_id = None
        self._max_msgs = None
        self._time_wait = None
        self._ack_wait = None
        self.discriminator = None

        self.queue_id = queue_id
        self.consumer_group_id = consumer_group_id
        if max_msgs is not None:
            self.max_msgs = max_msgs
        if time_wait is not None:
            self.time_wait = time_wait
        if ack_wait is not None:
            self.ack_wait = ack_wait

    @property
    def queue_id(self):
        """Gets the queue_id of this ConsumeDeadlettersMessageRequest.

        指定的队列ID。

        :return: The queue_id of this ConsumeDeadlettersMessageRequest.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this ConsumeDeadlettersMessageRequest.

        指定的队列ID。

        :param queue_id: The queue_id of this ConsumeDeadlettersMessageRequest.
        :type queue_id: str
        """
        self._queue_id = queue_id

    @property
    def consumer_group_id(self):
        """Gets the consumer_group_id of this ConsumeDeadlettersMessageRequest.

        消费组的ID。

        :return: The consumer_group_id of this ConsumeDeadlettersMessageRequest.
        :rtype: str
        """
        return self._consumer_group_id

    @consumer_group_id.setter
    def consumer_group_id(self, consumer_group_id):
        """Sets the consumer_group_id of this ConsumeDeadlettersMessageRequest.

        消费组的ID。

        :param consumer_group_id: The consumer_group_id of this ConsumeDeadlettersMessageRequest.
        :type consumer_group_id: str
        """
        self._consumer_group_id = consumer_group_id

    @property
    def max_msgs(self):
        """Gets the max_msgs of this ConsumeDeadlettersMessageRequest.

        获取可消费的死信消息的条数。  >单次消费返回的消息数量可能会少于指定条数，但多次消费最终可获取全部消息。  取值范围：1~10。  默认值：10

        :return: The max_msgs of this ConsumeDeadlettersMessageRequest.
        :rtype: int
        """
        return self._max_msgs

    @max_msgs.setter
    def max_msgs(self, max_msgs):
        """Sets the max_msgs of this ConsumeDeadlettersMessageRequest.

        获取可消费的死信消息的条数。  >单次消费返回的消息数量可能会少于指定条数，但多次消费最终可获取全部消息。  取值范围：1~10。  默认值：10

        :param max_msgs: The max_msgs of this ConsumeDeadlettersMessageRequest.
        :type max_msgs: int
        """
        self._max_msgs = max_msgs

    @property
    def time_wait(self):
        """Gets the time_wait of this ConsumeDeadlettersMessageRequest.

        设定消费组中可消费的死信为0时的读取消息等待时间。  如果在等待时间内有新的死信消息，则立即返回消费结果，如果等待时间内没有新的死信消息，则到等待时间后返回消费结果。  取值范围：1~60s  默认值：3s  说明：不带该参数或者配置为空，都默认为3s。

        :return: The time_wait of this ConsumeDeadlettersMessageRequest.
        :rtype: int
        """
        return self._time_wait

    @time_wait.setter
    def time_wait(self, time_wait):
        """Sets the time_wait of this ConsumeDeadlettersMessageRequest.

        设定消费组中可消费的死信为0时的读取消息等待时间。  如果在等待时间内有新的死信消息，则立即返回消费结果，如果等待时间内没有新的死信消息，则到等待时间后返回消费结果。  取值范围：1~60s  默认值：3s  说明：不带该参数或者配置为空，都默认为3s。

        :param time_wait: The time_wait of this ConsumeDeadlettersMessageRequest.
        :type time_wait: int
        """
        self._time_wait = time_wait

    @property
    def ack_wait(self):
        """Gets the ack_wait of this ConsumeDeadlettersMessageRequest.

        commit提交超时时间，在该时间内提交确认，确认有效，如果超过指定时间，系统会报消息确认超时，或handler无效。  取值范围：15~300s  默认值：30s  说明：不带该参数或者配置为空，都默认为30s。

        :return: The ack_wait of this ConsumeDeadlettersMessageRequest.
        :rtype: int
        """
        return self._ack_wait

    @ack_wait.setter
    def ack_wait(self, ack_wait):
        """Sets the ack_wait of this ConsumeDeadlettersMessageRequest.

        commit提交超时时间，在该时间内提交确认，确认有效，如果超过指定时间，系统会报消息确认超时，或handler无效。  取值范围：15~300s  默认值：30s  说明：不带该参数或者配置为空，都默认为30s。

        :param ack_wait: The ack_wait of this ConsumeDeadlettersMessageRequest.
        :type ack_wait: int
        """
        self._ack_wait = ack_wait

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
        if not isinstance(other, ConsumeDeadlettersMessageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
