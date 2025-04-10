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
        'events': 'list[ListEventModel]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'events': 'events',
        'page_info': 'page_info'
    }

    def __init__(self, events=None, page_info=None):
        r"""ListEventsResponse

        The model defined in huaweicloud sdk

        :param events: 事件或者告警详情。
        :type events: list[:class:`huaweicloudsdkaom.v2.ListEventModel`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkaom.v2.PageInfo`
        """
        
        super(ListEventsResponse, self).__init__()

        self._events = None
        self._page_info = None
        self.discriminator = None

        if events is not None:
            self.events = events
        if page_info is not None:
            self.page_info = page_info

    @property
    def events(self):
        r"""Gets the events of this ListEventsResponse.

        事件或者告警详情。

        :return: The events of this ListEventsResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.ListEventModel`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this ListEventsResponse.

        事件或者告警详情。

        :param events: The events of this ListEventsResponse.
        :type events: list[:class:`huaweicloudsdkaom.v2.ListEventModel`]
        """
        self._events = events

    @property
    def page_info(self):
        r"""Gets the page_info of this ListEventsResponse.

        :return: The page_info of this ListEventsResponse.
        :rtype: :class:`huaweicloudsdkaom.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListEventsResponse.

        :param page_info: The page_info of this ListEventsResponse.
        :type page_info: :class:`huaweicloudsdkaom.v2.PageInfo`
        """
        self._page_info = page_info

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
