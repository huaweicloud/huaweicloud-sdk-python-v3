# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartSmartLiveResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'rtc_room_info': 'RTCRoomInfoList',
        'live_event_report_url': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'rtc_room_info': 'rtc_room_info',
        'live_event_report_url': 'live_event_report_url',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, rtc_room_info=None, live_event_report_url=None, x_request_id=None):
        """StartSmartLiveResponse

        The model defined in huaweicloud sdk

        :param job_id: 直播任务ID。
        :type job_id: str
        :param rtc_room_info: 
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        :param live_event_report_url: 直播事件上报地址。用户将自行获取的直播间事件上报到此地址，用于触发智能互动，自动回复话术。
        :type live_event_report_url: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(StartSmartLiveResponse, self).__init__()

        self._job_id = None
        self._rtc_room_info = None
        self._live_event_report_url = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if rtc_room_info is not None:
            self.rtc_room_info = rtc_room_info
        if live_event_report_url is not None:
            self.live_event_report_url = live_event_report_url
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        """Gets the job_id of this StartSmartLiveResponse.

        直播任务ID。

        :return: The job_id of this StartSmartLiveResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this StartSmartLiveResponse.

        直播任务ID。

        :param job_id: The job_id of this StartSmartLiveResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def rtc_room_info(self):
        """Gets the rtc_room_info of this StartSmartLiveResponse.

        :return: The rtc_room_info of this StartSmartLiveResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        return self._rtc_room_info

    @rtc_room_info.setter
    def rtc_room_info(self, rtc_room_info):
        """Sets the rtc_room_info of this StartSmartLiveResponse.

        :param rtc_room_info: The rtc_room_info of this StartSmartLiveResponse.
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        self._rtc_room_info = rtc_room_info

    @property
    def live_event_report_url(self):
        """Gets the live_event_report_url of this StartSmartLiveResponse.

        直播事件上报地址。用户将自行获取的直播间事件上报到此地址，用于触发智能互动，自动回复话术。

        :return: The live_event_report_url of this StartSmartLiveResponse.
        :rtype: str
        """
        return self._live_event_report_url

    @live_event_report_url.setter
    def live_event_report_url(self, live_event_report_url):
        """Sets the live_event_report_url of this StartSmartLiveResponse.

        直播事件上报地址。用户将自行获取的直播间事件上报到此地址，用于触发智能互动，自动回复话术。

        :param live_event_report_url: The live_event_report_url of this StartSmartLiveResponse.
        :type live_event_report_url: str
        """
        self._live_event_report_url = live_event_report_url

    @property
    def x_request_id(self):
        """Gets the x_request_id of this StartSmartLiveResponse.

        :return: The x_request_id of this StartSmartLiveResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this StartSmartLiveResponse.

        :param x_request_id: The x_request_id of this StartSmartLiveResponse.
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
        if not isinstance(other, StartSmartLiveResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
