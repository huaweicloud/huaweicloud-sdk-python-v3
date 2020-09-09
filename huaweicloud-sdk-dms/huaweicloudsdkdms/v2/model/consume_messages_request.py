# coding: utf-8

import pprint
import re

import six





class ConsumeMessagesRequest:


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
        'ack_wait': 'int',
        'tag': 'str',
        'tag_type': 'str'
    }

    attribute_map = {
        'queue_id': 'queue_id',
        'consumer_group_id': 'consumer_group_id',
        'max_msgs': 'max_msgs',
        'time_wait': 'time_wait',
        'ack_wait': 'ack_wait',
        'tag': 'tag',
        'tag_type': 'tag_type'
    }

    def __init__(self, queue_id=None, consumer_group_id=None, max_msgs=None, time_wait=None, ack_wait=None, tag=None, tag_type=None):
        """ConsumeMessagesRequest - a model defined in huaweicloud sdk"""
        
        

        self._queue_id = None
        self._consumer_group_id = None
        self._max_msgs = None
        self._time_wait = None
        self._ack_wait = None
        self._tag = None
        self._tag_type = None
        self.discriminator = None

        self.queue_id = queue_id
        self.consumer_group_id = consumer_group_id
        if max_msgs is not None:
            self.max_msgs = max_msgs
        if time_wait is not None:
            self.time_wait = time_wait
        if ack_wait is not None:
            self.ack_wait = ack_wait
        if tag is not None:
            self.tag = tag
        if tag_type is not None:
            self.tag_type = tag_type

    @property
    def queue_id(self):
        """Gets the queue_id of this ConsumeMessagesRequest.


        :return: The queue_id of this ConsumeMessagesRequest.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this ConsumeMessagesRequest.


        :param queue_id: The queue_id of this ConsumeMessagesRequest.
        :type: str
        """
        self._queue_id = queue_id

    @property
    def consumer_group_id(self):
        """Gets the consumer_group_id of this ConsumeMessagesRequest.


        :return: The consumer_group_id of this ConsumeMessagesRequest.
        :rtype: str
        """
        return self._consumer_group_id

    @consumer_group_id.setter
    def consumer_group_id(self, consumer_group_id):
        """Sets the consumer_group_id of this ConsumeMessagesRequest.


        :param consumer_group_id: The consumer_group_id of this ConsumeMessagesRequest.
        :type: str
        """
        self._consumer_group_id = consumer_group_id

    @property
    def max_msgs(self):
        """Gets the max_msgs of this ConsumeMessagesRequest.


        :return: The max_msgs of this ConsumeMessagesRequest.
        :rtype: int
        """
        return self._max_msgs

    @max_msgs.setter
    def max_msgs(self, max_msgs):
        """Sets the max_msgs of this ConsumeMessagesRequest.


        :param max_msgs: The max_msgs of this ConsumeMessagesRequest.
        :type: int
        """
        self._max_msgs = max_msgs

    @property
    def time_wait(self):
        """Gets the time_wait of this ConsumeMessagesRequest.


        :return: The time_wait of this ConsumeMessagesRequest.
        :rtype: int
        """
        return self._time_wait

    @time_wait.setter
    def time_wait(self, time_wait):
        """Sets the time_wait of this ConsumeMessagesRequest.


        :param time_wait: The time_wait of this ConsumeMessagesRequest.
        :type: int
        """
        self._time_wait = time_wait

    @property
    def ack_wait(self):
        """Gets the ack_wait of this ConsumeMessagesRequest.


        :return: The ack_wait of this ConsumeMessagesRequest.
        :rtype: int
        """
        return self._ack_wait

    @ack_wait.setter
    def ack_wait(self, ack_wait):
        """Sets the ack_wait of this ConsumeMessagesRequest.


        :param ack_wait: The ack_wait of this ConsumeMessagesRequest.
        :type: int
        """
        self._ack_wait = ack_wait

    @property
    def tag(self):
        """Gets the tag of this ConsumeMessagesRequest.


        :return: The tag of this ConsumeMessagesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ConsumeMessagesRequest.


        :param tag: The tag of this ConsumeMessagesRequest.
        :type: str
        """
        self._tag = tag

    @property
    def tag_type(self):
        """Gets the tag_type of this ConsumeMessagesRequest.


        :return: The tag_type of this ConsumeMessagesRequest.
        :rtype: str
        """
        return self._tag_type

    @tag_type.setter
    def tag_type(self, tag_type):
        """Sets the tag_type of this ConsumeMessagesRequest.


        :param tag_type: The tag_type of this ConsumeMessagesRequest.
        :type: str
        """
        self._tag_type = tag_type

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
        if not isinstance(other, ConsumeMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
