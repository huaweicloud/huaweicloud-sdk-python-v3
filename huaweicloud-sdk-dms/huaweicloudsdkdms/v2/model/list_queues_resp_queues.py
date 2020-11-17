# coding: utf-8

import pprint
import re

import six





class ListQueuesRespQueues:


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
        'name': 'str',
        'description': 'str',
        'queue_mode': 'str',
        'reservation': 'int',
        'max_msg_size_byte': 'int',
        'produced_messages': 'int',
        'redrive_policy': 'str',
        'max_consume_count': 'int',
        'group_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'queue_mode': 'queue_mode',
        'reservation': 'reservation',
        'max_msg_size_byte': 'max_msg_size_byte',
        'produced_messages': 'produced_messages',
        'redrive_policy': 'redrive_policy',
        'max_consume_count': 'max_consume_count',
        'group_count': 'group_count'
    }

    def __init__(self, id=None, name=None, description=None, queue_mode=None, reservation=None, max_msg_size_byte=None, produced_messages=None, redrive_policy=None, max_consume_count=None, group_count=None):
        """ListQueuesRespQueues - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._description = None
        self._queue_mode = None
        self._reservation = None
        self._max_msg_size_byte = None
        self._produced_messages = None
        self._redrive_policy = None
        self._max_consume_count = None
        self._group_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if queue_mode is not None:
            self.queue_mode = queue_mode
        if reservation is not None:
            self.reservation = reservation
        if max_msg_size_byte is not None:
            self.max_msg_size_byte = max_msg_size_byte
        if produced_messages is not None:
            self.produced_messages = produced_messages
        if redrive_policy is not None:
            self.redrive_policy = redrive_policy
        if max_consume_count is not None:
            self.max_consume_count = max_consume_count
        if group_count is not None:
            self.group_count = group_count

    @property
    def id(self):
        """Gets the id of this ListQueuesRespQueues.

        队列ID。

        :return: The id of this ListQueuesRespQueues.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListQueuesRespQueues.

        队列ID。

        :param id: The id of this ListQueuesRespQueues.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListQueuesRespQueues.

        队列的名称。

        :return: The name of this ListQueuesRespQueues.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListQueuesRespQueues.

        队列的名称。

        :param name: The name of this ListQueuesRespQueues.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListQueuesRespQueues.

        队列的描述信息。

        :return: The description of this ListQueuesRespQueues.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListQueuesRespQueues.

        队列的描述信息。

        :param description: The description of this ListQueuesRespQueues.
        :type: str
        """
        self._description = description

    @property
    def queue_mode(self):
        """Gets the queue_mode of this ListQueuesRespQueues.

        队列类型。

        :return: The queue_mode of this ListQueuesRespQueues.
        :rtype: str
        """
        return self._queue_mode

    @queue_mode.setter
    def queue_mode(self, queue_mode):
        """Sets the queue_mode of this ListQueuesRespQueues.

        队列类型。

        :param queue_mode: The queue_mode of this ListQueuesRespQueues.
        :type: str
        """
        self._queue_mode = queue_mode

    @property
    def reservation(self):
        """Gets the reservation of this ListQueuesRespQueues.

        消息在队列中允许保留的时长（单位分钟）。

        :return: The reservation of this ListQueuesRespQueues.
        :rtype: int
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        """Sets the reservation of this ListQueuesRespQueues.

        消息在队列中允许保留的时长（单位分钟）。

        :param reservation: The reservation of this ListQueuesRespQueues.
        :type: int
        """
        self._reservation = reservation

    @property
    def max_msg_size_byte(self):
        """Gets the max_msg_size_byte of this ListQueuesRespQueues.

        队列中允许的最大消息大小（单位Byte）。

        :return: The max_msg_size_byte of this ListQueuesRespQueues.
        :rtype: int
        """
        return self._max_msg_size_byte

    @max_msg_size_byte.setter
    def max_msg_size_byte(self, max_msg_size_byte):
        """Sets the max_msg_size_byte of this ListQueuesRespQueues.

        队列中允许的最大消息大小（单位Byte）。

        :param max_msg_size_byte: The max_msg_size_byte of this ListQueuesRespQueues.
        :type: int
        """
        self._max_msg_size_byte = max_msg_size_byte

    @property
    def produced_messages(self):
        """Gets the produced_messages of this ListQueuesRespQueues.

        队列的消息总数。

        :return: The produced_messages of this ListQueuesRespQueues.
        :rtype: int
        """
        return self._produced_messages

    @produced_messages.setter
    def produced_messages(self, produced_messages):
        """Sets the produced_messages of this ListQueuesRespQueues.

        队列的消息总数。

        :param produced_messages: The produced_messages of this ListQueuesRespQueues.
        :type: int
        """
        self._produced_messages = produced_messages

    @property
    def redrive_policy(self):
        """Gets the redrive_policy of this ListQueuesRespQueues.

        该队列是否开启死信消息。仅当include_deadletter为true时，才有该响应参数。 - enable：表示开启。 - disable：表示不开启。

        :return: The redrive_policy of this ListQueuesRespQueues.
        :rtype: str
        """
        return self._redrive_policy

    @redrive_policy.setter
    def redrive_policy(self, redrive_policy):
        """Sets the redrive_policy of this ListQueuesRespQueues.

        该队列是否开启死信消息。仅当include_deadletter为true时，才有该响应参数。 - enable：表示开启。 - disable：表示不开启。

        :param redrive_policy: The redrive_policy of this ListQueuesRespQueues.
        :type: str
        """
        self._redrive_policy = redrive_policy

    @property
    def max_consume_count(self):
        """Gets the max_consume_count of this ListQueuesRespQueues.

        最大确认消费失败的次数，当达到最大确认失败次数后，DMS会将该条消息转存到死信队列中。  仅当include_deadletter为true时，才有该响应参数。

        :return: The max_consume_count of this ListQueuesRespQueues.
        :rtype: int
        """
        return self._max_consume_count

    @max_consume_count.setter
    def max_consume_count(self, max_consume_count):
        """Sets the max_consume_count of this ListQueuesRespQueues.

        最大确认消费失败的次数，当达到最大确认失败次数后，DMS会将该条消息转存到死信队列中。  仅当include_deadletter为true时，才有该响应参数。

        :param max_consume_count: The max_consume_count of this ListQueuesRespQueues.
        :type: int
        """
        self._max_consume_count = max_consume_count

    @property
    def group_count(self):
        """Gets the group_count of this ListQueuesRespQueues.

        该队列下的消费组数量。

        :return: The group_count of this ListQueuesRespQueues.
        :rtype: int
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        """Sets the group_count of this ListQueuesRespQueues.

        该队列下的消费组数量。

        :param group_count: The group_count of this ListQueuesRespQueues.
        :type: int
        """
        self._group_count = group_count

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
        if not isinstance(other, ListQueuesRespQueues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
