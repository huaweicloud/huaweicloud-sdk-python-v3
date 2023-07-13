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
        'events': 'list[EventModel]'
    }

    attribute_map = {
        'events': 'events'
    }

    def __init__(self, events=None):
        """ListEventsResponse

        The model defined in huaweicloud sdk

        :param events: 事件或者告警详情。
        :type events: list[:class:`huaweicloudsdkaom.v2.EventModel`]
        """
        
        super(ListEventsResponse, self).__init__()

        self._events = None
        self.discriminator = None

        if events is not None:
            self.events = events

    @property
    def events(self):
        """Gets the events of this ListEventsResponse.

        事件或者告警详情。

        :return: The events of this ListEventsResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.EventModel`]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ListEventsResponse.

        事件或者告警详情。

        :param events: The events of this ListEventsResponse.
        :type events: list[:class:`huaweicloudsdkaom.v2.EventModel`]
        """
        self._events = events

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
