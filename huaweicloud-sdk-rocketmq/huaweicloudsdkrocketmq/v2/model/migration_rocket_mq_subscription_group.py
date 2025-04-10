# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrationRocketMqSubscriptionGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'consume_broadcast_enable': 'bool',
        'consume_enable': 'bool',
        'consume_from_min_enable': 'bool',
        'notify_consumer_ids_changed_enable': 'bool',
        'retry_max_times': 'int',
        'retry_queue_nums': 'int',
        'which_broker_when_consume_slow': 'int'
    }

    attribute_map = {
        'group_name': 'groupName',
        'consume_broadcast_enable': 'consumeBroadcastEnable',
        'consume_enable': 'consumeEnable',
        'consume_from_min_enable': 'consumeFromMinEnable',
        'notify_consumer_ids_changed_enable': 'notifyConsumerIdsChangedEnable',
        'retry_max_times': 'retryMaxTimes',
        'retry_queue_nums': 'retryQueueNums',
        'which_broker_when_consume_slow': 'whichBrokerWhenConsumeSlow'
    }

    def __init__(self, group_name=None, consume_broadcast_enable=None, consume_enable=None, consume_from_min_enable=None, notify_consumer_ids_changed_enable=None, retry_max_times=None, retry_queue_nums=None, which_broker_when_consume_slow=None):
        r"""MigrationRocketMqSubscriptionGroup

        The model defined in huaweicloud sdk

        :param group_name: 消费组名。
        :type group_name: str
        :param consume_broadcast_enable: 是否允许以广播模式消费。
        :type consume_broadcast_enable: bool
        :param consume_enable: 是否允许消费。
        :type consume_enable: bool
        :param consume_from_min_enable: 是否从最小偏移量开始消费。
        :type consume_from_min_enable: bool
        :param notify_consumer_ids_changed_enable: 消费者ID变化时是否通知。
        :type notify_consumer_ids_changed_enable: bool
        :param retry_max_times: 消费最大重试次数。
        :type retry_max_times: int
        :param retry_queue_nums: 重试队列个数。
        :type retry_queue_nums: int
        :param which_broker_when_consume_slow: 慢消费时选择的broker节点ID。
        :type which_broker_when_consume_slow: int
        """
        
        

        self._group_name = None
        self._consume_broadcast_enable = None
        self._consume_enable = None
        self._consume_from_min_enable = None
        self._notify_consumer_ids_changed_enable = None
        self._retry_max_times = None
        self._retry_queue_nums = None
        self._which_broker_when_consume_slow = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if consume_broadcast_enable is not None:
            self.consume_broadcast_enable = consume_broadcast_enable
        if consume_enable is not None:
            self.consume_enable = consume_enable
        if consume_from_min_enable is not None:
            self.consume_from_min_enable = consume_from_min_enable
        if notify_consumer_ids_changed_enable is not None:
            self.notify_consumer_ids_changed_enable = notify_consumer_ids_changed_enable
        if retry_max_times is not None:
            self.retry_max_times = retry_max_times
        if retry_queue_nums is not None:
            self.retry_queue_nums = retry_queue_nums
        if which_broker_when_consume_slow is not None:
            self.which_broker_when_consume_slow = which_broker_when_consume_slow

    @property
    def group_name(self):
        r"""Gets the group_name of this MigrationRocketMqSubscriptionGroup.

        消费组名。

        :return: The group_name of this MigrationRocketMqSubscriptionGroup.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this MigrationRocketMqSubscriptionGroup.

        消费组名。

        :param group_name: The group_name of this MigrationRocketMqSubscriptionGroup.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def consume_broadcast_enable(self):
        r"""Gets the consume_broadcast_enable of this MigrationRocketMqSubscriptionGroup.

        是否允许以广播模式消费。

        :return: The consume_broadcast_enable of this MigrationRocketMqSubscriptionGroup.
        :rtype: bool
        """
        return self._consume_broadcast_enable

    @consume_broadcast_enable.setter
    def consume_broadcast_enable(self, consume_broadcast_enable):
        r"""Sets the consume_broadcast_enable of this MigrationRocketMqSubscriptionGroup.

        是否允许以广播模式消费。

        :param consume_broadcast_enable: The consume_broadcast_enable of this MigrationRocketMqSubscriptionGroup.
        :type consume_broadcast_enable: bool
        """
        self._consume_broadcast_enable = consume_broadcast_enable

    @property
    def consume_enable(self):
        r"""Gets the consume_enable of this MigrationRocketMqSubscriptionGroup.

        是否允许消费。

        :return: The consume_enable of this MigrationRocketMqSubscriptionGroup.
        :rtype: bool
        """
        return self._consume_enable

    @consume_enable.setter
    def consume_enable(self, consume_enable):
        r"""Sets the consume_enable of this MigrationRocketMqSubscriptionGroup.

        是否允许消费。

        :param consume_enable: The consume_enable of this MigrationRocketMqSubscriptionGroup.
        :type consume_enable: bool
        """
        self._consume_enable = consume_enable

    @property
    def consume_from_min_enable(self):
        r"""Gets the consume_from_min_enable of this MigrationRocketMqSubscriptionGroup.

        是否从最小偏移量开始消费。

        :return: The consume_from_min_enable of this MigrationRocketMqSubscriptionGroup.
        :rtype: bool
        """
        return self._consume_from_min_enable

    @consume_from_min_enable.setter
    def consume_from_min_enable(self, consume_from_min_enable):
        r"""Sets the consume_from_min_enable of this MigrationRocketMqSubscriptionGroup.

        是否从最小偏移量开始消费。

        :param consume_from_min_enable: The consume_from_min_enable of this MigrationRocketMqSubscriptionGroup.
        :type consume_from_min_enable: bool
        """
        self._consume_from_min_enable = consume_from_min_enable

    @property
    def notify_consumer_ids_changed_enable(self):
        r"""Gets the notify_consumer_ids_changed_enable of this MigrationRocketMqSubscriptionGroup.

        消费者ID变化时是否通知。

        :return: The notify_consumer_ids_changed_enable of this MigrationRocketMqSubscriptionGroup.
        :rtype: bool
        """
        return self._notify_consumer_ids_changed_enable

    @notify_consumer_ids_changed_enable.setter
    def notify_consumer_ids_changed_enable(self, notify_consumer_ids_changed_enable):
        r"""Sets the notify_consumer_ids_changed_enable of this MigrationRocketMqSubscriptionGroup.

        消费者ID变化时是否通知。

        :param notify_consumer_ids_changed_enable: The notify_consumer_ids_changed_enable of this MigrationRocketMqSubscriptionGroup.
        :type notify_consumer_ids_changed_enable: bool
        """
        self._notify_consumer_ids_changed_enable = notify_consumer_ids_changed_enable

    @property
    def retry_max_times(self):
        r"""Gets the retry_max_times of this MigrationRocketMqSubscriptionGroup.

        消费最大重试次数。

        :return: The retry_max_times of this MigrationRocketMqSubscriptionGroup.
        :rtype: int
        """
        return self._retry_max_times

    @retry_max_times.setter
    def retry_max_times(self, retry_max_times):
        r"""Sets the retry_max_times of this MigrationRocketMqSubscriptionGroup.

        消费最大重试次数。

        :param retry_max_times: The retry_max_times of this MigrationRocketMqSubscriptionGroup.
        :type retry_max_times: int
        """
        self._retry_max_times = retry_max_times

    @property
    def retry_queue_nums(self):
        r"""Gets the retry_queue_nums of this MigrationRocketMqSubscriptionGroup.

        重试队列个数。

        :return: The retry_queue_nums of this MigrationRocketMqSubscriptionGroup.
        :rtype: int
        """
        return self._retry_queue_nums

    @retry_queue_nums.setter
    def retry_queue_nums(self, retry_queue_nums):
        r"""Sets the retry_queue_nums of this MigrationRocketMqSubscriptionGroup.

        重试队列个数。

        :param retry_queue_nums: The retry_queue_nums of this MigrationRocketMqSubscriptionGroup.
        :type retry_queue_nums: int
        """
        self._retry_queue_nums = retry_queue_nums

    @property
    def which_broker_when_consume_slow(self):
        r"""Gets the which_broker_when_consume_slow of this MigrationRocketMqSubscriptionGroup.

        慢消费时选择的broker节点ID。

        :return: The which_broker_when_consume_slow of this MigrationRocketMqSubscriptionGroup.
        :rtype: int
        """
        return self._which_broker_when_consume_slow

    @which_broker_when_consume_slow.setter
    def which_broker_when_consume_slow(self, which_broker_when_consume_slow):
        r"""Sets the which_broker_when_consume_slow of this MigrationRocketMqSubscriptionGroup.

        慢消费时选择的broker节点ID。

        :param which_broker_when_consume_slow: The which_broker_when_consume_slow of this MigrationRocketMqSubscriptionGroup.
        :type which_broker_when_consume_slow: int
        """
        self._which_broker_when_consume_slow = which_broker_when_consume_slow

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
        if not isinstance(other, MigrationRocketMqSubscriptionGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
