# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Notification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'status': 'str',
        'topic': 'str',
        'msg_type': 'int'
    }

    attribute_map = {
        'event_name': 'event_name',
        'status': 'status',
        'topic': 'topic',
        'msg_type': 'msg_type'
    }

    def __init__(self, event_name=None, status=None, topic=None, msg_type=None):
        r"""Notification

        The model defined in huaweicloud sdk

        :param event_name: 消息事件的名称. 
        :type event_name: str
        :param status: 事件通知模板选中状态 
        :type status: str
        :param topic: 事件通知主题的URN. 
        :type topic: str
        :param msg_type: 订阅消息类型. 
        :type msg_type: int
        """
        
        

        self._event_name = None
        self._status = None
        self._topic = None
        self._msg_type = None
        self.discriminator = None

        if event_name is not None:
            self.event_name = event_name
        if status is not None:
            self.status = status
        if topic is not None:
            self.topic = topic
        if msg_type is not None:
            self.msg_type = msg_type

    @property
    def event_name(self):
        r"""Gets the event_name of this Notification.

        消息事件的名称. 

        :return: The event_name of this Notification.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this Notification.

        消息事件的名称. 

        :param event_name: The event_name of this Notification.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def status(self):
        r"""Gets the status of this Notification.

        事件通知模板选中状态 

        :return: The status of this Notification.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Notification.

        事件通知模板选中状态 

        :param status: The status of this Notification.
        :type status: str
        """
        self._status = status

    @property
    def topic(self):
        r"""Gets the topic of this Notification.

        事件通知主题的URN. 

        :return: The topic of this Notification.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this Notification.

        事件通知主题的URN. 

        :param topic: The topic of this Notification.
        :type topic: str
        """
        self._topic = topic

    @property
    def msg_type(self):
        r"""Gets the msg_type of this Notification.

        订阅消息类型. 

        :return: The msg_type of this Notification.
        :rtype: int
        """
        return self._msg_type

    @msg_type.setter
    def msg_type(self, msg_type):
        r"""Sets the msg_type of this Notification.

        订阅消息类型. 

        :param msg_type: The msg_type of this Notification.
        :type msg_type: int
        """
        self._msg_type = msg_type

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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
