# coding: utf-8

import pprint
import re

import six





class ShowInstanceMessagesRespMessages:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'topic': 'str',
        'partition': 'int',
        'key': 'str',
        'value': 'str',
        'size': 'int',
        'timestamp': 'int',
        'huge_message': 'bool',
        'message_offset': 'int',
        'message_id': 'str',
        'app_id': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'topic': 'topic',
        'partition': 'partition',
        'key': 'key',
        'value': 'value',
        'size': 'size',
        'timestamp': 'timestamp',
        'huge_message': 'huge_message',
        'message_offset': 'message_offset',
        'message_id': 'message_id',
        'app_id': 'app_id',
        'tag': 'tag'
    }

    def __init__(self, topic=None, partition=None, key=None, value=None, size=None, timestamp=None, huge_message=None, message_offset=None, message_id=None, app_id=None, tag=None):
        """ShowInstanceMessagesRespMessages - a model defined in huaweicloud sdk"""
        
        

        self._topic = None
        self._partition = None
        self._key = None
        self._value = None
        self._size = None
        self._timestamp = None
        self._huge_message = None
        self._message_offset = None
        self._message_id = None
        self._app_id = None
        self._tag = None
        self.discriminator = None

        if topic is not None:
            self.topic = topic
        if partition is not None:
            self.partition = partition
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if size is not None:
            self.size = size
        if timestamp is not None:
            self.timestamp = timestamp
        if huge_message is not None:
            self.huge_message = huge_message
        if message_offset is not None:
            self.message_offset = message_offset
        if message_id is not None:
            self.message_id = message_id
        if app_id is not None:
            self.app_id = app_id
        if tag is not None:
            self.tag = tag

    @property
    def topic(self):
        """Gets the topic of this ShowInstanceMessagesRespMessages.

        topic名称。

        :return: The topic of this ShowInstanceMessagesRespMessages.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this ShowInstanceMessagesRespMessages.

        topic名称。

        :param topic: The topic of this ShowInstanceMessagesRespMessages.
        :type: str
        """
        self._topic = topic

    @property
    def partition(self):
        """Gets the partition of this ShowInstanceMessagesRespMessages.

        消息所在的分区。

        :return: The partition of this ShowInstanceMessagesRespMessages.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """Sets the partition of this ShowInstanceMessagesRespMessages.

        消息所在的分区。

        :param partition: The partition of this ShowInstanceMessagesRespMessages.
        :type: int
        """
        self._partition = partition

    @property
    def key(self):
        """Gets the key of this ShowInstanceMessagesRespMessages.

        消息key。

        :return: The key of this ShowInstanceMessagesRespMessages.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ShowInstanceMessagesRespMessages.

        消息key。

        :param key: The key of this ShowInstanceMessagesRespMessages.
        :type: str
        """
        self._key = key

    @property
    def value(self):
        """Gets the value of this ShowInstanceMessagesRespMessages.

        消息内容。

        :return: The value of this ShowInstanceMessagesRespMessages.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ShowInstanceMessagesRespMessages.

        消息内容。

        :param value: The value of this ShowInstanceMessagesRespMessages.
        :type: str
        """
        self._value = value

    @property
    def size(self):
        """Gets the size of this ShowInstanceMessagesRespMessages.

        消息大小。

        :return: The size of this ShowInstanceMessagesRespMessages.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowInstanceMessagesRespMessages.

        消息大小。

        :param size: The size of this ShowInstanceMessagesRespMessages.
        :type: int
        """
        self._size = size

    @property
    def timestamp(self):
        """Gets the timestamp of this ShowInstanceMessagesRespMessages.

        topic名称。

        :return: The timestamp of this ShowInstanceMessagesRespMessages.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ShowInstanceMessagesRespMessages.

        topic名称。

        :param timestamp: The timestamp of this ShowInstanceMessagesRespMessages.
        :type: int
        """
        self._timestamp = timestamp

    @property
    def huge_message(self):
        """Gets the huge_message of this ShowInstanceMessagesRespMessages.

        大数据标识。

        :return: The huge_message of this ShowInstanceMessagesRespMessages.
        :rtype: bool
        """
        return self._huge_message

    @huge_message.setter
    def huge_message(self, huge_message):
        """Sets the huge_message of this ShowInstanceMessagesRespMessages.

        大数据标识。

        :param huge_message: The huge_message of this ShowInstanceMessagesRespMessages.
        :type: bool
        """
        self._huge_message = huge_message

    @property
    def message_offset(self):
        """Gets the message_offset of this ShowInstanceMessagesRespMessages.

        消息偏移量。

        :return: The message_offset of this ShowInstanceMessagesRespMessages.
        :rtype: int
        """
        return self._message_offset

    @message_offset.setter
    def message_offset(self, message_offset):
        """Sets the message_offset of this ShowInstanceMessagesRespMessages.

        消息偏移量。

        :param message_offset: The message_offset of this ShowInstanceMessagesRespMessages.
        :type: int
        """
        self._message_offset = message_offset

    @property
    def message_id(self):
        """Gets the message_id of this ShowInstanceMessagesRespMessages.

        消息ID。

        :return: The message_id of this ShowInstanceMessagesRespMessages.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this ShowInstanceMessagesRespMessages.

        消息ID。

        :param message_id: The message_id of this ShowInstanceMessagesRespMessages.
        :type: str
        """
        self._message_id = message_id

    @property
    def app_id(self):
        """Gets the app_id of this ShowInstanceMessagesRespMessages.

        应用ID。

        :return: The app_id of this ShowInstanceMessagesRespMessages.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowInstanceMessagesRespMessages.

        应用ID。

        :param app_id: The app_id of this ShowInstanceMessagesRespMessages.
        :type: str
        """
        self._app_id = app_id

    @property
    def tag(self):
        """Gets the tag of this ShowInstanceMessagesRespMessages.

        消息标签。

        :return: The tag of this ShowInstanceMessagesRespMessages.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ShowInstanceMessagesRespMessages.

        消息标签。

        :param tag: The tag of this ShowInstanceMessagesRespMessages.
        :type: str
        """
        self._tag = tag

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
        if not isinstance(other, ShowInstanceMessagesRespMessages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
