# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateQueueReq:

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
        'queue_mode': 'str',
        'description': 'str',
        'redrive_policy': 'str',
        'max_consume_count': 'int',
        'retention_hours': 'int'
    }

    attribute_map = {
        'name': 'name',
        'queue_mode': 'queue_mode',
        'description': 'description',
        'redrive_policy': 'redrive_policy',
        'max_consume_count': 'max_consume_count',
        'retention_hours': 'retention_hours'
    }

    def __init__(self, name=None, queue_mode=None, description=None, redrive_policy=None, max_consume_count=None, retention_hours=None):
        """CreateQueueReq

        The model defined in huaweicloud sdk

        :param name: 队列的名称，必须唯一。  长度不超过64位的字符串，包含a~z，A~Z，0~9、中划线（-）和下划线（_）。  创建队列后无法修改名称。
        :type name: str
        :param queue_mode: 队列类型。  取值范围： - NORMAL：普通队列，更高的并发性能，不保证先入先出（FIFO）的严格顺序。 - FIFO：有序队列，保证消息先入先出（FIFO）的严格顺序。 - KAFKA_HA：高可靠模式的kafka队列。消息多副本同步落盘，保证消息的可靠性。 - KAFKA_HT：高吞吐模式的kafka队列。消息副本异步落盘，具有较高的性能。  默认值：NORMAL
        :type queue_mode: str
        :param description: 队列的描述信息。  长度不超过160位的字符串，不能包含尖括号&lt;&gt;。
        :type description: str
        :param redrive_policy: 仅当queue_mode为“NORMAL”或者“FIFO”时，该参数有效。  是否开启死信消息，死信消息是指无法被正常消费的消息。  当达到最大消费次数仍然失败后，DMS会将该条消息转存到死信队列中，有效期为72小时，用户可以根据需要对死信消息进行重新消费。  消费死信消息时，只能消费该消费组产生的死信消息。  有序队列的死信消息依然按照先入先出（FIFO）的顺序存储在死信队列中。  取值范围： - enable：开启 - disable：不开启  默认值：disable
        :type redrive_policy: str
        :param max_consume_count: 仅当redrive_policy为enable时，该参数必选。  最大确认消费失败的次数，当达到最大确认失败次数后，DMS会将该条消息转存到死信队列中。  取值范围：1~100
        :type max_consume_count: int
        :param retention_hours: 指定kafka队列的消息保存时间，单位为小时。  仅当queue_mode为KAFKA_HA或者KAFKA_HT才有效。  取值范围: 1-72（小时）
        :type retention_hours: int
        """
        
        

        self._name = None
        self._queue_mode = None
        self._description = None
        self._redrive_policy = None
        self._max_consume_count = None
        self._retention_hours = None
        self.discriminator = None

        self.name = name
        if queue_mode is not None:
            self.queue_mode = queue_mode
        if description is not None:
            self.description = description
        if redrive_policy is not None:
            self.redrive_policy = redrive_policy
        if max_consume_count is not None:
            self.max_consume_count = max_consume_count
        if retention_hours is not None:
            self.retention_hours = retention_hours

    @property
    def name(self):
        """Gets the name of this CreateQueueReq.

        队列的名称，必须唯一。  长度不超过64位的字符串，包含a~z，A~Z，0~9、中划线（-）和下划线（_）。  创建队列后无法修改名称。

        :return: The name of this CreateQueueReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateQueueReq.

        队列的名称，必须唯一。  长度不超过64位的字符串，包含a~z，A~Z，0~9、中划线（-）和下划线（_）。  创建队列后无法修改名称。

        :param name: The name of this CreateQueueReq.
        :type name: str
        """
        self._name = name

    @property
    def queue_mode(self):
        """Gets the queue_mode of this CreateQueueReq.

        队列类型。  取值范围： - NORMAL：普通队列，更高的并发性能，不保证先入先出（FIFO）的严格顺序。 - FIFO：有序队列，保证消息先入先出（FIFO）的严格顺序。 - KAFKA_HA：高可靠模式的kafka队列。消息多副本同步落盘，保证消息的可靠性。 - KAFKA_HT：高吞吐模式的kafka队列。消息副本异步落盘，具有较高的性能。  默认值：NORMAL

        :return: The queue_mode of this CreateQueueReq.
        :rtype: str
        """
        return self._queue_mode

    @queue_mode.setter
    def queue_mode(self, queue_mode):
        """Sets the queue_mode of this CreateQueueReq.

        队列类型。  取值范围： - NORMAL：普通队列，更高的并发性能，不保证先入先出（FIFO）的严格顺序。 - FIFO：有序队列，保证消息先入先出（FIFO）的严格顺序。 - KAFKA_HA：高可靠模式的kafka队列。消息多副本同步落盘，保证消息的可靠性。 - KAFKA_HT：高吞吐模式的kafka队列。消息副本异步落盘，具有较高的性能。  默认值：NORMAL

        :param queue_mode: The queue_mode of this CreateQueueReq.
        :type queue_mode: str
        """
        self._queue_mode = queue_mode

    @property
    def description(self):
        """Gets the description of this CreateQueueReq.

        队列的描述信息。  长度不超过160位的字符串，不能包含尖括号<>。

        :return: The description of this CreateQueueReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateQueueReq.

        队列的描述信息。  长度不超过160位的字符串，不能包含尖括号<>。

        :param description: The description of this CreateQueueReq.
        :type description: str
        """
        self._description = description

    @property
    def redrive_policy(self):
        """Gets the redrive_policy of this CreateQueueReq.

        仅当queue_mode为“NORMAL”或者“FIFO”时，该参数有效。  是否开启死信消息，死信消息是指无法被正常消费的消息。  当达到最大消费次数仍然失败后，DMS会将该条消息转存到死信队列中，有效期为72小时，用户可以根据需要对死信消息进行重新消费。  消费死信消息时，只能消费该消费组产生的死信消息。  有序队列的死信消息依然按照先入先出（FIFO）的顺序存储在死信队列中。  取值范围： - enable：开启 - disable：不开启  默认值：disable

        :return: The redrive_policy of this CreateQueueReq.
        :rtype: str
        """
        return self._redrive_policy

    @redrive_policy.setter
    def redrive_policy(self, redrive_policy):
        """Sets the redrive_policy of this CreateQueueReq.

        仅当queue_mode为“NORMAL”或者“FIFO”时，该参数有效。  是否开启死信消息，死信消息是指无法被正常消费的消息。  当达到最大消费次数仍然失败后，DMS会将该条消息转存到死信队列中，有效期为72小时，用户可以根据需要对死信消息进行重新消费。  消费死信消息时，只能消费该消费组产生的死信消息。  有序队列的死信消息依然按照先入先出（FIFO）的顺序存储在死信队列中。  取值范围： - enable：开启 - disable：不开启  默认值：disable

        :param redrive_policy: The redrive_policy of this CreateQueueReq.
        :type redrive_policy: str
        """
        self._redrive_policy = redrive_policy

    @property
    def max_consume_count(self):
        """Gets the max_consume_count of this CreateQueueReq.

        仅当redrive_policy为enable时，该参数必选。  最大确认消费失败的次数，当达到最大确认失败次数后，DMS会将该条消息转存到死信队列中。  取值范围：1~100

        :return: The max_consume_count of this CreateQueueReq.
        :rtype: int
        """
        return self._max_consume_count

    @max_consume_count.setter
    def max_consume_count(self, max_consume_count):
        """Sets the max_consume_count of this CreateQueueReq.

        仅当redrive_policy为enable时，该参数必选。  最大确认消费失败的次数，当达到最大确认失败次数后，DMS会将该条消息转存到死信队列中。  取值范围：1~100

        :param max_consume_count: The max_consume_count of this CreateQueueReq.
        :type max_consume_count: int
        """
        self._max_consume_count = max_consume_count

    @property
    def retention_hours(self):
        """Gets the retention_hours of this CreateQueueReq.

        指定kafka队列的消息保存时间，单位为小时。  仅当queue_mode为KAFKA_HA或者KAFKA_HT才有效。  取值范围: 1-72（小时）

        :return: The retention_hours of this CreateQueueReq.
        :rtype: int
        """
        return self._retention_hours

    @retention_hours.setter
    def retention_hours(self, retention_hours):
        """Sets the retention_hours of this CreateQueueReq.

        指定kafka队列的消息保存时间，单位为小时。  仅当queue_mode为KAFKA_HA或者KAFKA_HT才有效。  取值范围: 1-72（小时）

        :param retention_hours: The retention_hours of this CreateQueueReq.
        :type retention_hours: int
        """
        self._retention_hours = retention_hours

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
        if not isinstance(other, CreateQueueReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
