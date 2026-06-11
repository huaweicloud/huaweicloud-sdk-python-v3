# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryWaitEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'events': 'list[Event]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'events': 'events'
    }

    def __init__(self, total_count=None, events=None):
        r"""ListHistoryWaitEventsResponse

        The model defined in huaweicloud sdk

        :param total_count: 总记录数
        :type total_count: int
        :param events: 事件列表
        :type events: list[:class:`huaweicloudsdkrds.v3.Event`]
        """
        
        super().__init__()

        self._total_count = None
        self._events = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if events is not None:
            self.events = events

    @property
    def total_count(self):
        r"""Gets the total_count of this ListHistoryWaitEventsResponse.

        总记录数

        :return: The total_count of this ListHistoryWaitEventsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListHistoryWaitEventsResponse.

        总记录数

        :param total_count: The total_count of this ListHistoryWaitEventsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def events(self):
        r"""Gets the events of this ListHistoryWaitEventsResponse.

        事件列表

        :return: The events of this ListHistoryWaitEventsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.Event`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this ListHistoryWaitEventsResponse.

        事件列表

        :param events: The events of this ListHistoryWaitEventsResponse.
        :type events: list[:class:`huaweicloudsdkrds.v3.Event`]
        """
        self._events = events

    def to_dict(self):
        import warnings
        warnings.warn("ListHistoryWaitEventsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListHistoryWaitEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
