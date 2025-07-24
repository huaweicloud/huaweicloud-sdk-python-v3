# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'message_id': 'str',
        'event_message': 'str',
        'event_level': 'str',
        'status': 'str',
        'resource_id': 'str',
        'time': 'int',
        'origin_event': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'message_id': 'message_id',
        'event_message': 'event_message',
        'event_level': 'event_level',
        'status': 'status',
        'resource_id': 'resource_id',
        'time': 'time',
        'origin_event': 'origin_event'
    }

    def __init__(self, event_id=None, message_id=None, event_message=None, event_level=None, status=None, resource_id=None, time=None, origin_event=None):
        r"""EventInfo

        The model defined in huaweicloud sdk

        :param event_id: 事件ID
        :type event_id: str
        :param message_id: 描述ID
        :type message_id: str
        :param event_message: 事件描述
        :type event_message: str
        :param event_level: 事件级别，枚举类型：critical, major, minor, info
        :type event_level: str
        :param status: 事件状态
        :type status: str
        :param resource_id: 资源ID，最大长度128
        :type resource_id: str
        :param time: 事件发生时间，UNIX时间戳，单位毫秒
        :type time: int
        :param origin_event: 原始事件，最大长度4096
        :type origin_event: str
        """
        
        

        self._event_id = None
        self._message_id = None
        self._event_message = None
        self._event_level = None
        self._status = None
        self._resource_id = None
        self._time = None
        self._origin_event = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if message_id is not None:
            self.message_id = message_id
        if event_message is not None:
            self.event_message = event_message
        if event_level is not None:
            self.event_level = event_level
        if status is not None:
            self.status = status
        if resource_id is not None:
            self.resource_id = resource_id
        if time is not None:
            self.time = time
        if origin_event is not None:
            self.origin_event = origin_event

    @property
    def event_id(self):
        r"""Gets the event_id of this EventInfo.

        事件ID

        :return: The event_id of this EventInfo.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this EventInfo.

        事件ID

        :param event_id: The event_id of this EventInfo.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def message_id(self):
        r"""Gets the message_id of this EventInfo.

        描述ID

        :return: The message_id of this EventInfo.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        r"""Sets the message_id of this EventInfo.

        描述ID

        :param message_id: The message_id of this EventInfo.
        :type message_id: str
        """
        self._message_id = message_id

    @property
    def event_message(self):
        r"""Gets the event_message of this EventInfo.

        事件描述

        :return: The event_message of this EventInfo.
        :rtype: str
        """
        return self._event_message

    @event_message.setter
    def event_message(self, event_message):
        r"""Sets the event_message of this EventInfo.

        事件描述

        :param event_message: The event_message of this EventInfo.
        :type event_message: str
        """
        self._event_message = event_message

    @property
    def event_level(self):
        r"""Gets the event_level of this EventInfo.

        事件级别，枚举类型：critical, major, minor, info

        :return: The event_level of this EventInfo.
        :rtype: str
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        r"""Sets the event_level of this EventInfo.

        事件级别，枚举类型：critical, major, minor, info

        :param event_level: The event_level of this EventInfo.
        :type event_level: str
        """
        self._event_level = event_level

    @property
    def status(self):
        r"""Gets the status of this EventInfo.

        事件状态

        :return: The status of this EventInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EventInfo.

        事件状态

        :param status: The status of this EventInfo.
        :type status: str
        """
        self._status = status

    @property
    def resource_id(self):
        r"""Gets the resource_id of this EventInfo.

        资源ID，最大长度128

        :return: The resource_id of this EventInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this EventInfo.

        资源ID，最大长度128

        :param resource_id: The resource_id of this EventInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def time(self):
        r"""Gets the time of this EventInfo.

        事件发生时间，UNIX时间戳，单位毫秒

        :return: The time of this EventInfo.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this EventInfo.

        事件发生时间，UNIX时间戳，单位毫秒

        :param time: The time of this EventInfo.
        :type time: int
        """
        self._time = time

    @property
    def origin_event(self):
        r"""Gets the origin_event of this EventInfo.

        原始事件，最大长度4096

        :return: The origin_event of this EventInfo.
        :rtype: str
        """
        return self._origin_event

    @origin_event.setter
    def origin_event(self, origin_event):
        r"""Sets the origin_event of this EventInfo.

        原始事件，最大长度4096

        :param origin_event: The origin_event of this EventInfo.
        :type origin_event: str
        """
        self._origin_event = origin_event

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
        if not isinstance(other, EventInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
