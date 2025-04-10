# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event:

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
        'event_id': 'str',
        'event_types': 'list[str]',
        'state': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'notification': 'Notification'
    }

    attribute_map = {
        'name': 'name',
        'event_id': 'event_id',
        'event_types': 'event_types',
        'state': 'state',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'notification': 'notification'
    }

    def __init__(self, name=None, event_id=None, event_types=None, state=None, create_time=None, update_time=None, notification=None):
        r"""Event

        The model defined in huaweicloud sdk

        :param name: 事件通知名称。
        :type name: str
        :param event_id: 事件通知的资源标识符。
        :type event_id: str
        :param event_types: 设置事件的基础事件类型列表,。  约束：数组大小：最小1，最大12。
        :type event_types: list[str]
        :param state: 事件通知状态，取值如下。  ENABLED：表示启用状态 DISABLED：表示禁用状态
        :type state: str
        :param create_time: 事件通知创建时间，时间戳，即从1970年1月1日至该时间的总秒数。
        :type create_time: int
        :param update_time: 事件通知上次更新时间，时间戳，即从1970年1月1日至该时间的总秒数。
        :type update_time: int
        :param notification: 
        :type notification: :class:`huaweicloudsdkcsms.v1.Notification`
        """
        
        

        self._name = None
        self._event_id = None
        self._event_types = None
        self._state = None
        self._create_time = None
        self._update_time = None
        self._notification = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if event_id is not None:
            self.event_id = event_id
        if event_types is not None:
            self.event_types = event_types
        if state is not None:
            self.state = state
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if notification is not None:
            self.notification = notification

    @property
    def name(self):
        r"""Gets the name of this Event.

        事件通知名称。

        :return: The name of this Event.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Event.

        事件通知名称。

        :param name: The name of this Event.
        :type name: str
        """
        self._name = name

    @property
    def event_id(self):
        r"""Gets the event_id of this Event.

        事件通知的资源标识符。

        :return: The event_id of this Event.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this Event.

        事件通知的资源标识符。

        :param event_id: The event_id of this Event.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_types(self):
        r"""Gets the event_types of this Event.

        设置事件的基础事件类型列表,。  约束：数组大小：最小1，最大12。

        :return: The event_types of this Event.
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        r"""Sets the event_types of this Event.

        设置事件的基础事件类型列表,。  约束：数组大小：最小1，最大12。

        :param event_types: The event_types of this Event.
        :type event_types: list[str]
        """
        self._event_types = event_types

    @property
    def state(self):
        r"""Gets the state of this Event.

        事件通知状态，取值如下。  ENABLED：表示启用状态 DISABLED：表示禁用状态

        :return: The state of this Event.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this Event.

        事件通知状态，取值如下。  ENABLED：表示启用状态 DISABLED：表示禁用状态

        :param state: The state of this Event.
        :type state: str
        """
        self._state = state

    @property
    def create_time(self):
        r"""Gets the create_time of this Event.

        事件通知创建时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The create_time of this Event.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this Event.

        事件通知创建时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :param create_time: The create_time of this Event.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this Event.

        事件通知上次更新时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The update_time of this Event.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this Event.

        事件通知上次更新时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :param update_time: The update_time of this Event.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def notification(self):
        r"""Gets the notification of this Event.

        :return: The notification of this Event.
        :rtype: :class:`huaweicloudsdkcsms.v1.Notification`
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        r"""Sets the notification of this Event.

        :param notification: The notification of this Event.
        :type notification: :class:`huaweicloudsdkcsms.v1.Notification`
        """
        self._notification = notification

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
