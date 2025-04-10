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
        'events': 'list[LiveEvent]',
        'review_config': 'ReviewConfig'
    }

    attribute_map = {
        'total': 'total',
        'events': 'events',
        'review_config': 'review_config'
    }

    def __init__(self, total=None, events=None, review_config=None):
        r"""ReportLiveEventReq

        The model defined in huaweicloud sdk

        :param total: **参数解释**： 事件条目数。
        :type total: int
        :param events: 事件内容。
        :type events: list[:class:`huaweicloudsdkmetastudio.v1.LiveEvent`]
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        
        

        self._total = None
        self._events = None
        self._review_config = None
        self.discriminator = None

        self.total = total
        if events is not None:
            self.events = events
        if review_config is not None:
            self.review_config = review_config

    @property
    def total(self):
        r"""Gets the total of this ReportLiveEventReq.

        **参数解释**： 事件条目数。

        :return: The total of this ReportLiveEventReq.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ReportLiveEventReq.

        **参数解释**： 事件条目数。

        :param total: The total of this ReportLiveEventReq.
        :type total: int
        """
        self._total = total

    @property
    def events(self):
        r"""Gets the events of this ReportLiveEventReq.

        事件内容。

        :return: The events of this ReportLiveEventReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveEvent`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this ReportLiveEventReq.

        事件内容。

        :param events: The events of this ReportLiveEventReq.
        :type events: list[:class:`huaweicloudsdkmetastudio.v1.LiveEvent`]
        """
        self._events = events

    @property
    def review_config(self):
        r"""Gets the review_config of this ReportLiveEventReq.

        :return: The review_config of this ReportLiveEventReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        r"""Sets the review_config of this ReportLiveEventReq.

        :param review_config: The review_config of this ReportLiveEventReq.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

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
