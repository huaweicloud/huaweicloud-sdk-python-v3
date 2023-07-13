# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRtcAbnormalEventsResponse(SdkResponse):

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
        'events': 'list[AbnormalEvent]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'events': 'events',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, total=None, events=None, x_request_id=None):
        """ListRtcAbnormalEventsResponse

        The model defined in huaweicloud sdk

        :param total: 异常总数
        :type total: int
        :param events: 异常体验列表
        :type events: list[:class:`huaweicloudsdkcloudrtc.v1.AbnormalEvent`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListRtcAbnormalEventsResponse, self).__init__()

        self._total = None
        self._events = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if events is not None:
            self.events = events
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        """Gets the total of this ListRtcAbnormalEventsResponse.

        异常总数

        :return: The total of this ListRtcAbnormalEventsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListRtcAbnormalEventsResponse.

        异常总数

        :param total: The total of this ListRtcAbnormalEventsResponse.
        :type total: int
        """
        self._total = total

    @property
    def events(self):
        """Gets the events of this ListRtcAbnormalEventsResponse.

        异常体验列表

        :return: The events of this ListRtcAbnormalEventsResponse.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v1.AbnormalEvent`]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ListRtcAbnormalEventsResponse.

        异常体验列表

        :param events: The events of this ListRtcAbnormalEventsResponse.
        :type events: list[:class:`huaweicloudsdkcloudrtc.v1.AbnormalEvent`]
        """
        self._events = events

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListRtcAbnormalEventsResponse.

        :return: The x_request_id of this ListRtcAbnormalEventsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListRtcAbnormalEventsResponse.

        :param x_request_id: The x_request_id of this ListRtcAbnormalEventsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListRtcAbnormalEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
