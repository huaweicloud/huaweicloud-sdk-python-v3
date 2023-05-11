# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTraceEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'span_event_list': 'list[SpanEventInfo]'
    }

    attribute_map = {
        'span_event_list': 'span_event_list'
    }

    def __init__(self, span_event_list=None):
        """ShowTraceEventsResponse

        The model defined in huaweicloud sdk

        :param span_event_list: span event信息列表。
        :type span_event_list: list[:class:`huaweicloudsdkapm.v1.SpanEventInfo`]
        """
        
        super(ShowTraceEventsResponse, self).__init__()

        self._span_event_list = None
        self.discriminator = None

        if span_event_list is not None:
            self.span_event_list = span_event_list

    @property
    def span_event_list(self):
        """Gets the span_event_list of this ShowTraceEventsResponse.

        span event信息列表。

        :return: The span_event_list of this ShowTraceEventsResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.SpanEventInfo`]
        """
        return self._span_event_list

    @span_event_list.setter
    def span_event_list(self, span_event_list):
        """Sets the span_event_list of this ShowTraceEventsResponse.

        span event信息列表。

        :param span_event_list: The span_event_list of this ShowTraceEventsResponse.
        :type span_event_list: list[:class:`huaweicloudsdkapm.v1.SpanEventInfo`]
        """
        self._span_event_list = span_event_list

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
        if not isinstance(other, ShowTraceEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
