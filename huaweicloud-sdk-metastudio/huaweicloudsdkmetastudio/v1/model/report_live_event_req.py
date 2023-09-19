# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReportLiveEventReq:

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
        'events': 'list[LiveEvent]'
    }

    attribute_map = {
        'total': 'total',
        'events': 'events'
    }

    def __init__(self, total=None, events=None):
        """ReportLiveEventReq

        The model defined in huaweicloud sdk

        :param total: 事件条目数。
        :type total: int
        :param events: 事件内容。
        :type events: list[:class:`huaweicloudsdkmetastudio.v1.LiveEvent`]
        """
        
        

        self._total = None
        self._events = None
        self.discriminator = None

        self.total = total
        if events is not None:
            self.events = events

    @property
    def total(self):
        """Gets the total of this ReportLiveEventReq.

        事件条目数。

        :return: The total of this ReportLiveEventReq.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ReportLiveEventReq.

        事件条目数。

        :param total: The total of this ReportLiveEventReq.
        :type total: int
        """
        self._total = total

    @property
    def events(self):
        """Gets the events of this ReportLiveEventReq.

        事件内容。

        :return: The events of this ReportLiveEventReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveEvent`]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ReportLiveEventReq.

        事件内容。

        :param events: The events of this ReportLiveEventReq.
        :type events: list[:class:`huaweicloudsdkmetastudio.v1.LiveEvent`]
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
        if not isinstance(other, ReportLiveEventReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
