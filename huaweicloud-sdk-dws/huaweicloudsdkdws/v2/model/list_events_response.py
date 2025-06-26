# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'events': 'list[EventResponse]',
        'count': 'int'
    }

    attribute_map = {
        'events': 'events',
        'count': 'count'
    }

    def __init__(self, events=None, count=None):
        r"""ListEventsResponse

        The model defined in huaweicloud sdk

        :param events: **参数解释**： 事件详情列表。 **取值范围**： 不涉及。
        :type events: list[:class:`huaweicloudsdkdws.v2.EventResponse`]
        :param count: **参数解释**： 事件总数。 **取值范围**： 不涉及。
        :type count: int
        """
        
        super(ListEventsResponse, self).__init__()

        self._events = None
        self._count = None
        self.discriminator = None

        if events is not None:
            self.events = events
        if count is not None:
            self.count = count

    @property
    def events(self):
        r"""Gets the events of this ListEventsResponse.

        **参数解释**： 事件详情列表。 **取值范围**： 不涉及。

        :return: The events of this ListEventsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.EventResponse`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this ListEventsResponse.

        **参数解释**： 事件详情列表。 **取值范围**： 不涉及。

        :param events: The events of this ListEventsResponse.
        :type events: list[:class:`huaweicloudsdkdws.v2.EventResponse`]
        """
        self._events = events

    @property
    def count(self):
        r"""Gets the count of this ListEventsResponse.

        **参数解释**： 事件总数。 **取值范围**： 不涉及。

        :return: The count of this ListEventsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListEventsResponse.

        **参数解释**： 事件总数。 **取值范围**： 不涉及。

        :param count: The count of this ListEventsResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
