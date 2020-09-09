# coding: utf-8

import pprint
import re

import six





class ShowMessagesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'topic': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int',
        'partition': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'topic': 'topic',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset',
        'partition': 'partition'
    }

    def __init__(self, instance_id=None, topic=None, start_time=None, end_time=None, limit=None, offset=None, partition=None):
        """ShowMessagesRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._topic = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self._partition = None
        self.discriminator = None

        self.instance_id = instance_id
        self.topic = topic
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if partition is not None:
            self.partition = partition

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowMessagesRequest.


        :return: The instance_id of this ShowMessagesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowMessagesRequest.


        :param instance_id: The instance_id of this ShowMessagesRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def topic(self):
        """Gets the topic of this ShowMessagesRequest.


        :return: The topic of this ShowMessagesRequest.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowMessagesRequest.


        :param topic: The topic of this ShowMessagesRequest.
        :type: str
        """
        self._topic = topic

    @property
    def start_time(self):
        """Gets the start_time of this ShowMessagesRequest.


        :return: The start_time of this ShowMessagesRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowMessagesRequest.


        :param start_time: The start_time of this ShowMessagesRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowMessagesRequest.


        :return: The end_time of this ShowMessagesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowMessagesRequest.


        :param end_time: The end_time of this ShowMessagesRequest.
        :type: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ShowMessagesRequest.


        :return: The limit of this ShowMessagesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowMessagesRequest.


        :param limit: The limit of this ShowMessagesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowMessagesRequest.


        :return: The offset of this ShowMessagesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowMessagesRequest.


        :param offset: The offset of this ShowMessagesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def partition(self):
        """Gets the partition of this ShowMessagesRequest.


        :return: The partition of this ShowMessagesRequest.
        :rtype: str
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this ShowMessagesRequest.


        :param partition: The partition of this ShowMessagesRequest.
        :type: str
        """
        self._partition = partition

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
        if not isinstance(other, ShowMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
