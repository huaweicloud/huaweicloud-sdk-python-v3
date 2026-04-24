# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSearchFactoryEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'events': 'list[EventSearchResultV2Events]',
        'total': 'int'
    }

    attribute_map = {
        'events': 'events',
        'total': 'total'
    }

    def __init__(self, events=None, total=None):
        r"""ListSearchFactoryEventsResponse

        The model defined in huaweicloud sdk

        :param events: 事件。
        :type events: list[:class:`huaweicloudsdkdataartsstudio.v1.EventSearchResultV2Events`]
        :param total: 总数。
        :type total: int
        """
        
        super().__init__()

        self._events = None
        self._total = None
        self.discriminator = None

        if events is not None:
            self.events = events
        if total is not None:
            self.total = total

    @property
    def events(self):
        r"""Gets the events of this ListSearchFactoryEventsResponse.

        事件。

        :return: The events of this ListSearchFactoryEventsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.EventSearchResultV2Events`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this ListSearchFactoryEventsResponse.

        事件。

        :param events: The events of this ListSearchFactoryEventsResponse.
        :type events: list[:class:`huaweicloudsdkdataartsstudio.v1.EventSearchResultV2Events`]
        """
        self._events = events

    @property
    def total(self):
        r"""Gets the total of this ListSearchFactoryEventsResponse.

        总数。

        :return: The total of this ListSearchFactoryEventsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSearchFactoryEventsResponse.

        总数。

        :param total: The total of this ListSearchFactoryEventsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListSearchFactoryEventsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSearchFactoryEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
