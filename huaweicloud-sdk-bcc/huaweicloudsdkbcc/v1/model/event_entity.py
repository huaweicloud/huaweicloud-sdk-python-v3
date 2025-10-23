# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventEntity:

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
        'event_name': 'str',
        'event_type': 'str',
        'event_source': 'EventSourceEnum',
        'time': 'str',
        'detail': 'EventDetailEntity'
    }

    attribute_map = {
        'event_id': 'event_id',
        'event_name': 'event_name',
        'event_type': 'event_type',
        'event_source': 'event_source',
        'time': 'time',
        'detail': 'detail'
    }

    def __init__(self, event_id=None, event_name=None, event_type=None, event_source=None, time=None, detail=None):
        r"""EventEntity

        The model defined in huaweicloud sdk

        :param event_id: 事件ID
        :type event_id: str
        :param event_name: 事件名称
        :type event_name: str
        :param event_type: 事件类型
        :type event_type: str
        :param event_source: 
        :type event_source: :class:`huaweicloudsdkbcc.v1.EventSourceEnum`
        :param time: 事件产生时间
        :type time: str
        :param detail: 
        :type detail: :class:`huaweicloudsdkbcc.v1.EventDetailEntity`
        """
        
        

        self._event_id = None
        self._event_name = None
        self._event_type = None
        self._event_source = None
        self._time = None
        self._detail = None
        self.discriminator = None

        self.event_id = event_id
        if event_name is not None:
            self.event_name = event_name
        if event_type is not None:
            self.event_type = event_type
        if event_source is not None:
            self.event_source = event_source
        if time is not None:
            self.time = time
        if detail is not None:
            self.detail = detail

    @property
    def event_id(self):
        r"""Gets the event_id of this EventEntity.

        事件ID

        :return: The event_id of this EventEntity.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this EventEntity.

        事件ID

        :param event_id: The event_id of this EventEntity.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_name(self):
        r"""Gets the event_name of this EventEntity.

        事件名称

        :return: The event_name of this EventEntity.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this EventEntity.

        事件名称

        :param event_name: The event_name of this EventEntity.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_type(self):
        r"""Gets the event_type of this EventEntity.

        事件类型

        :return: The event_type of this EventEntity.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this EventEntity.

        事件类型

        :param event_type: The event_type of this EventEntity.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_source(self):
        r"""Gets the event_source of this EventEntity.

        :return: The event_source of this EventEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.EventSourceEnum`
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        r"""Sets the event_source of this EventEntity.

        :param event_source: The event_source of this EventEntity.
        :type event_source: :class:`huaweicloudsdkbcc.v1.EventSourceEnum`
        """
        self._event_source = event_source

    @property
    def time(self):
        r"""Gets the time of this EventEntity.

        事件产生时间

        :return: The time of this EventEntity.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this EventEntity.

        事件产生时间

        :param time: The time of this EventEntity.
        :type time: str
        """
        self._time = time

    @property
    def detail(self):
        r"""Gets the detail of this EventEntity.

        :return: The detail of this EventEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.EventDetailEntity`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this EventEntity.

        :param detail: The detail of this EventEntity.
        :type detail: :class:`huaweicloudsdkbcc.v1.EventDetailEntity`
        """
        self._detail = detail

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
        if not isinstance(other, EventEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
