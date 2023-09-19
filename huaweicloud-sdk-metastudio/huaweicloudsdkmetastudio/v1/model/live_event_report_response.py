# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveEventReportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'live_event_report_url': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'live_event_report_url': 'live_event_report_url',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, live_event_report_url=None, x_request_id=None):
        """LiveEventReportResponse

        The model defined in huaweicloud sdk

        :param live_event_report_url: 刷新后的直播事件上传URL
        :type live_event_report_url: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(LiveEventReportResponse, self).__init__()

        self._live_event_report_url = None
        self._x_request_id = None
        self.discriminator = None

        if live_event_report_url is not None:
            self.live_event_report_url = live_event_report_url
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def live_event_report_url(self):
        """Gets the live_event_report_url of this LiveEventReportResponse.

        刷新后的直播事件上传URL

        :return: The live_event_report_url of this LiveEventReportResponse.
        :rtype: str
        """
        return self._live_event_report_url

    @live_event_report_url.setter
    def live_event_report_url(self, live_event_report_url):
        """Sets the live_event_report_url of this LiveEventReportResponse.

        刷新后的直播事件上传URL

        :param live_event_report_url: The live_event_report_url of this LiveEventReportResponse.
        :type live_event_report_url: str
        """
        self._live_event_report_url = live_event_report_url

    @property
    def x_request_id(self):
        """Gets the x_request_id of this LiveEventReportResponse.

        :return: The x_request_id of this LiveEventReportResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this LiveEventReportResponse.

        :param x_request_id: The x_request_id of this LiveEventReportResponse.
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
        if not isinstance(other, LiveEventReportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
