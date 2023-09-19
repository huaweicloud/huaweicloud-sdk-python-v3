# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSmartLiveResponse(SdkResponse):

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
        'state': 'str',
        'duration': 'float',
        'start_time': 'str',
        'end_time': 'str',
        'error_info': 'ErrorResponse',
        'create_time': 'str',
        'lastupdate_time': 'str',
        'rtc_room_info': 'RTCRoomInfoList',
        'live_event_report_url': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'state': 'state',
        'duration': 'duration',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'error_info': 'error_info',
        'create_time': 'create_time',
        'lastupdate_time': 'lastupdate_time',
        'rtc_room_info': 'rtc_room_info',
        'live_event_report_url': 'live_event_report_url',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, state=None, duration=None, start_time=None, end_time=None, error_info=None, create_time=None, lastupdate_time=None, rtc_room_info=None, live_event_report_url=None, x_request_id=None):
        """ShowSmartLiveResponse

        The model defined in huaweicloud sdk

        :param job_id: 数字人直播任务ID。
        :type job_id: str
        :param state: 数字人直播任务的状态。 * WAITING: 等待 * PROCESSING: 处理中 * SUCCEED: 成功 * FAILED: 失败
        :type state: str
        :param duration: 数字人直播时长，单位秒。
        :type duration: float
        :param start_time: 数字人直播任务开始时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type start_time: str
        :param end_time: 数字人直播任务结束时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type end_time: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        :param create_time: 数字人直播任务创建时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param lastupdate_time: 数字人直播任务最后更新时间。格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type lastupdate_time: str
        :param rtc_room_info: 
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        :param live_event_report_url: 直播事件上报地址。用户将自行获取的直播间事件上报到此地址，用于触发智能互动，自动回复话术。
        :type live_event_report_url: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowSmartLiveResponse, self).__init__()

        self._job_id = None
        self._state = None
        self._duration = None
        self._start_time = None
        self._end_time = None
        self._error_info = None
        self._create_time = None
        self._lastupdate_time = None
        self._rtc_room_info = None
        self._live_event_report_url = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if state is not None:
            self.state = state
        if duration is not None:
            self.duration = duration
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if error_info is not None:
            self.error_info = error_info
        if create_time is not None:
            self.create_time = create_time
        if lastupdate_time is not None:
            self.lastupdate_time = lastupdate_time
        if rtc_room_info is not None:
            self.rtc_room_info = rtc_room_info
        if live_event_report_url is not None:
            self.live_event_report_url = live_event_report_url
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        """Gets the job_id of this ShowSmartLiveResponse.

        数字人直播任务ID。

        :return: The job_id of this ShowSmartLiveResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowSmartLiveResponse.

        数字人直播任务ID。

        :param job_id: The job_id of this ShowSmartLiveResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def state(self):
        """Gets the state of this ShowSmartLiveResponse.

        数字人直播任务的状态。 * WAITING: 等待 * PROCESSING: 处理中 * SUCCEED: 成功 * FAILED: 失败

        :return: The state of this ShowSmartLiveResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShowSmartLiveResponse.

        数字人直播任务的状态。 * WAITING: 等待 * PROCESSING: 处理中 * SUCCEED: 成功 * FAILED: 失败

        :param state: The state of this ShowSmartLiveResponse.
        :type state: str
        """
        self._state = state

    @property
    def duration(self):
        """Gets the duration of this ShowSmartLiveResponse.

        数字人直播时长，单位秒。

        :return: The duration of this ShowSmartLiveResponse.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ShowSmartLiveResponse.

        数字人直播时长，单位秒。

        :param duration: The duration of this ShowSmartLiveResponse.
        :type duration: float
        """
        self._duration = duration

    @property
    def start_time(self):
        """Gets the start_time of this ShowSmartLiveResponse.

        数字人直播任务开始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The start_time of this ShowSmartLiveResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowSmartLiveResponse.

        数字人直播任务开始时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param start_time: The start_time of this ShowSmartLiveResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowSmartLiveResponse.

        数字人直播任务结束时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The end_time of this ShowSmartLiveResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowSmartLiveResponse.

        数字人直播任务结束时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param end_time: The end_time of this ShowSmartLiveResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def error_info(self):
        """Gets the error_info of this ShowSmartLiveResponse.

        :return: The error_info of this ShowSmartLiveResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """Sets the error_info of this ShowSmartLiveResponse.

        :param error_info: The error_info of this ShowSmartLiveResponse.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

    @property
    def create_time(self):
        """Gets the create_time of this ShowSmartLiveResponse.

        数字人直播任务创建时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowSmartLiveResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowSmartLiveResponse.

        数字人直播任务创建时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowSmartLiveResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def lastupdate_time(self):
        """Gets the lastupdate_time of this ShowSmartLiveResponse.

        数字人直播任务最后更新时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The lastupdate_time of this ShowSmartLiveResponse.
        :rtype: str
        """
        return self._lastupdate_time

    @lastupdate_time.setter
    def lastupdate_time(self, lastupdate_time):
        """Sets the lastupdate_time of this ShowSmartLiveResponse.

        数字人直播任务最后更新时间。格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param lastupdate_time: The lastupdate_time of this ShowSmartLiveResponse.
        :type lastupdate_time: str
        """
        self._lastupdate_time = lastupdate_time

    @property
    def rtc_room_info(self):
        """Gets the rtc_room_info of this ShowSmartLiveResponse.

        :return: The rtc_room_info of this ShowSmartLiveResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        return self._rtc_room_info

    @rtc_room_info.setter
    def rtc_room_info(self, rtc_room_info):
        """Sets the rtc_room_info of this ShowSmartLiveResponse.

        :param rtc_room_info: The rtc_room_info of this ShowSmartLiveResponse.
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        self._rtc_room_info = rtc_room_info

    @property
    def live_event_report_url(self):
        """Gets the live_event_report_url of this ShowSmartLiveResponse.

        直播事件上报地址。用户将自行获取的直播间事件上报到此地址，用于触发智能互动，自动回复话术。

        :return: The live_event_report_url of this ShowSmartLiveResponse.
        :rtype: str
        """
        return self._live_event_report_url

    @live_event_report_url.setter
    def live_event_report_url(self, live_event_report_url):
        """Sets the live_event_report_url of this ShowSmartLiveResponse.

        直播事件上报地址。用户将自行获取的直播间事件上报到此地址，用于触发智能互动，自动回复话术。

        :param live_event_report_url: The live_event_report_url of this ShowSmartLiveResponse.
        :type live_event_report_url: str
        """
        self._live_event_report_url = live_event_report_url

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowSmartLiveResponse.

        :return: The x_request_id of this ShowSmartLiveResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowSmartLiveResponse.

        :param x_request_id: The x_request_id of this ShowSmartLiveResponse.
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
        if not isinstance(other, ShowSmartLiveResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
