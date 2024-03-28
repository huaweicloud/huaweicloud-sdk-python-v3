# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IefEvent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_type': 'str',
        'operation': 'str',
        'timestamp': 'int',
        'topic': 'str',
        'name': 'str',
        'attributes': 'str'
    }

    attribute_map = {
        'event_type': 'event_type',
        'operation': 'operation',
        'timestamp': 'timestamp',
        'topic': 'topic',
        'name': 'name',
        'attributes': 'attributes'
    }

    def __init__(self, event_type=None, operation=None, timestamp=None, topic=None, name=None, attributes=None):
        """IefEvent

        The model defined in huaweicloud sdk

        :param event_type: 资源类型
        :type event_type: str
        :param operation: 资源的操作类型
        :type operation: str
        :param timestamp: 事件产生的时间戳
        :type timestamp: int
        :param topic: 消息发送的Topic
        :type topic: str
        :param name: 资源名称
        :type name: str
        :param attributes: 资源的属性
        :type attributes: str
        """
        
        

        self._event_type = None
        self._operation = None
        self._timestamp = None
        self._topic = None
        self._name = None
        self._attributes = None
        self.discriminator = None

        self.event_type = event_type
        self.operation = operation
        self.timestamp = timestamp
        self.topic = topic
        self.name = name
        if attributes is not None:
            self.attributes = attributes

    @property
    def event_type(self):
        """Gets the event_type of this IefEvent.

        资源类型

        :return: The event_type of this IefEvent.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this IefEvent.

        资源类型

        :param event_type: The event_type of this IefEvent.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def operation(self):
        """Gets the operation of this IefEvent.

        资源的操作类型

        :return: The operation of this IefEvent.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this IefEvent.

        资源的操作类型

        :param operation: The operation of this IefEvent.
        :type operation: str
        """
        self._operation = operation

    @property
    def timestamp(self):
        """Gets the timestamp of this IefEvent.

        事件产生的时间戳

        :return: The timestamp of this IefEvent.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this IefEvent.

        事件产生的时间戳

        :param timestamp: The timestamp of this IefEvent.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def topic(self):
        """Gets the topic of this IefEvent.

        消息发送的Topic

        :return: The topic of this IefEvent.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this IefEvent.

        消息发送的Topic

        :param topic: The topic of this IefEvent.
        :type topic: str
        """
        self._topic = topic

    @property
    def name(self):
        """Gets the name of this IefEvent.

        资源名称

        :return: The name of this IefEvent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IefEvent.

        资源名称

        :param name: The name of this IefEvent.
        :type name: str
        """
        self._name = name

    @property
    def attributes(self):
        """Gets the attributes of this IefEvent.

        资源的属性

        :return: The attributes of this IefEvent.
        :rtype: str
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this IefEvent.

        资源的属性

        :param attributes: The attributes of this IefEvent.
        :type attributes: str
        """
        self._attributes = attributes

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
        if not isinstance(other, IefEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
