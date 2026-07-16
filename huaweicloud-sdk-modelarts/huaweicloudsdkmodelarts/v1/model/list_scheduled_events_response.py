# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'events': 'list[ScheduledEvent]',
        'count': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'events': 'events',
        'count': 'count',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, events=None, count=None, x_request_id=None):
        r"""ListScheduledEventsResponse

        The model defined in huaweicloud sdk

        :param events: **参数解释**：计划事件列表
        :type events: list[:class:`huaweicloudsdkmodelarts.v1.ScheduledEvent`]
        :param count: **参数解释**：计划事件总数。 **取值范围**：不涉及。
        :type count: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._events = None
        self._count = None
        self._x_request_id = None
        self.discriminator = None

        if events is not None:
            self.events = events
        if count is not None:
            self.count = count
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def events(self):
        r"""Gets the events of this ListScheduledEventsResponse.

        **参数解释**：计划事件列表

        :return: The events of this ListScheduledEventsResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ScheduledEvent`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this ListScheduledEventsResponse.

        **参数解释**：计划事件列表

        :param events: The events of this ListScheduledEventsResponse.
        :type events: list[:class:`huaweicloudsdkmodelarts.v1.ScheduledEvent`]
        """
        self._events = events

    @property
    def count(self):
        r"""Gets the count of this ListScheduledEventsResponse.

        **参数解释**：计划事件总数。 **取值范围**：不涉及。

        :return: The count of this ListScheduledEventsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListScheduledEventsResponse.

        **参数解释**：计划事件总数。 **取值范围**：不涉及。

        :param count: The count of this ListScheduledEventsResponse.
        :type count: int
        """
        self._count = count

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListScheduledEventsResponse.

        :return: The x_request_id of this ListScheduledEventsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListScheduledEventsResponse.

        :param x_request_id: The x_request_id of this ListScheduledEventsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListScheduledEventsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListScheduledEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
