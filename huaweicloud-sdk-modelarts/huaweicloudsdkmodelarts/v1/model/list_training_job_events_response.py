# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrainingJobEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'limit': 'int',
        'offset': 'int',
        'order': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'events': 'list[Event]'
    }

    attribute_map = {
        'total': 'total',
        'limit': 'limit',
        'offset': 'offset',
        'order': 'order',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'events': 'events'
    }

    def __init__(self, total=None, limit=None, offset=None, order=None, start_time=None, end_time=None, events=None):
        r"""ListTrainingJobEventsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：总条数。 **取值范围**：不涉及。
        :type total: int
        :param limit: **参数解释**：最大显示条数。 **取值范围**：不涉及。
        :type limit: int
        :param offset: **参数解释**：开始的条数。 **取值范围**：不涉及。
        :type offset: int
        :param order: **参数解释**：排序方式。 **取值范围**：不涉及。
        :type order: str
        :param start_time: **参数解释**：事件的开始时间。 **取值范围**：不涉及。
        :type start_time: str
        :param end_time: **参数解释**：事件的结束时间。 **取值范围**：不涉及。
        :type end_time: str
        :param events: **参数解释**：事件列表。
        :type events: list[:class:`huaweicloudsdkmodelarts.v1.Event`]
        """
        
        super().__init__()

        self._total = None
        self._limit = None
        self._offset = None
        self._order = None
        self._start_time = None
        self._end_time = None
        self._events = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order is not None:
            self.order = order
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if events is not None:
            self.events = events

    @property
    def total(self):
        r"""Gets the total of this ListTrainingJobEventsResponse.

        **参数解释**：总条数。 **取值范围**：不涉及。

        :return: The total of this ListTrainingJobEventsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListTrainingJobEventsResponse.

        **参数解释**：总条数。 **取值范围**：不涉及。

        :param total: The total of this ListTrainingJobEventsResponse.
        :type total: int
        """
        self._total = total

    @property
    def limit(self):
        r"""Gets the limit of this ListTrainingJobEventsResponse.

        **参数解释**：最大显示条数。 **取值范围**：不涉及。

        :return: The limit of this ListTrainingJobEventsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTrainingJobEventsResponse.

        **参数解释**：最大显示条数。 **取值范围**：不涉及。

        :param limit: The limit of this ListTrainingJobEventsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTrainingJobEventsResponse.

        **参数解释**：开始的条数。 **取值范围**：不涉及。

        :return: The offset of this ListTrainingJobEventsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTrainingJobEventsResponse.

        **参数解释**：开始的条数。 **取值范围**：不涉及。

        :param offset: The offset of this ListTrainingJobEventsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def order(self):
        r"""Gets the order of this ListTrainingJobEventsResponse.

        **参数解释**：排序方式。 **取值范围**：不涉及。

        :return: The order of this ListTrainingJobEventsResponse.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListTrainingJobEventsResponse.

        **参数解释**：排序方式。 **取值范围**：不涉及。

        :param order: The order of this ListTrainingJobEventsResponse.
        :type order: str
        """
        self._order = order

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTrainingJobEventsResponse.

        **参数解释**：事件的开始时间。 **取值范围**：不涉及。

        :return: The start_time of this ListTrainingJobEventsResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTrainingJobEventsResponse.

        **参数解释**：事件的开始时间。 **取值范围**：不涉及。

        :param start_time: The start_time of this ListTrainingJobEventsResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTrainingJobEventsResponse.

        **参数解释**：事件的结束时间。 **取值范围**：不涉及。

        :return: The end_time of this ListTrainingJobEventsResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTrainingJobEventsResponse.

        **参数解释**：事件的结束时间。 **取值范围**：不涉及。

        :param end_time: The end_time of this ListTrainingJobEventsResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def events(self):
        r"""Gets the events of this ListTrainingJobEventsResponse.

        **参数解释**：事件列表。

        :return: The events of this ListTrainingJobEventsResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Event`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this ListTrainingJobEventsResponse.

        **参数解释**：事件列表。

        :param events: The events of this ListTrainingJobEventsResponse.
        :type events: list[:class:`huaweicloudsdkmodelarts.v1.Event`]
        """
        self._events = events

    def to_dict(self):
        import warnings
        warnings.warn("ListTrainingJobEventsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTrainingJobEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
