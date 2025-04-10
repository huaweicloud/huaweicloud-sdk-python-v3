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
        'live_event_callback_config': 'LiveEventCallBackConfig',
        'live_warning_info': 'list[LiveWarningItem]',
        'limit_duration': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'rtc_room_info': 'rtc_room_info',
        'live_event_report_url': 'live_event_report_url',
        'live_event_callback_config': 'live_event_callback_config',
        'live_warning_info': 'live_warning_info',
        'limit_duration': 'limit_duration',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_id=None, rtc_room_info=None, live_event_report_url=None, live_event_callback_config=None, live_warning_info=None, limit_duration=None, x_request_id=None):
        r"""StartSmartLiveResponse

        The model defined in huaweicloud sdk

        :param job_id: 直播任务ID。
        :type job_id: str
        :param rtc_room_info: 
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        :param live_event_report_url: 直播事件上报地址。用户将自行获取的直播间事件上报到此地址，用于触发智能互动，自动回复话术。
        :type live_event_report_url: str
        :param live_event_callback_config: 
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        :param live_warning_info: 开播风险告警列表。
        :type live_warning_info: list[:class:`huaweicloudsdkmetastudio.v1.LiveWarningItem`]
        :param limit_duration: **参数解释**： 配置的最大直播时长。单位小时。 0 为不限制。 **约束限制**： 停止直播逻辑配置为立即停止则直播停止误差在5分钟之内。其他逻辑则加上处理时长。 **默认取值**： 不设置则表示不限时。
        :type limit_duration: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(StartSmartLiveResponse, self).__init__()

        self._job_id = None
        self._rtc_room_info = None
        self._live_event_report_url = None
        self._live_event_callback_config = None
        self._live_warning_info = None
        self._limit_duration = None
        self._x_request_id = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if rtc_room_info is not None:
            self.rtc_room_info = rtc_room_info
        if live_event_report_url is not None:
            self.live_event_report_url = live_event_report_url
        if live_event_callback_config is not None:
            self.live_event_callback_config = live_event_callback_config
        if live_warning_info is not None:
            self.live_warning_info = live_warning_info
        if limit_duration is not None:
            self.limit_duration = limit_duration
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_id(self):
        r"""Gets the job_id of this StartSmartLiveResponse.

        直播任务ID。

        :return: The job_id of this StartSmartLiveResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this StartSmartLiveResponse.

        直播任务ID。

        :param job_id: The job_id of this StartSmartLiveResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def rtc_room_info(self):
        r"""Gets the rtc_room_info of this StartSmartLiveResponse.

        :return: The rtc_room_info of this StartSmartLiveResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        return self._rtc_room_info

    @rtc_room_info.setter
    def rtc_room_info(self, rtc_room_info):
        r"""Sets the rtc_room_info of this StartSmartLiveResponse.

        :param rtc_room_info: The rtc_room_info of this StartSmartLiveResponse.
        :type rtc_room_info: :class:`huaweicloudsdkmetastudio.v1.RTCRoomInfoList`
        """
        self._rtc_room_info = rtc_room_info

    @property
    def live_event_report_url(self):
        r"""Gets the live_event_report_url of this StartSmartLiveResponse.

        直播事件上报地址。用户将自行获取的直播间事件上报到此地址，用于触发智能互动，自动回复话术。

        :return: The live_event_report_url of this StartSmartLiveResponse.
        :rtype: str
        """
        return self._live_event_report_url

    @live_event_report_url.setter
    def live_event_report_url(self, live_event_report_url):
        r"""Sets the live_event_report_url of this StartSmartLiveResponse.

        直播事件上报地址。用户将自行获取的直播间事件上报到此地址，用于触发智能互动，自动回复话术。

        :param live_event_report_url: The live_event_report_url of this StartSmartLiveResponse.
        :type live_event_report_url: str
        """
        self._live_event_report_url = live_event_report_url

    @property
    def live_event_callback_config(self):
        r"""Gets the live_event_callback_config of this StartSmartLiveResponse.

        :return: The live_event_callback_config of this StartSmartLiveResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        return self._live_event_callback_config

    @live_event_callback_config.setter
    def live_event_callback_config(self, live_event_callback_config):
        r"""Sets the live_event_callback_config of this StartSmartLiveResponse.

        :param live_event_callback_config: The live_event_callback_config of this StartSmartLiveResponse.
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        self._live_event_callback_config = live_event_callback_config

    @property
    def live_warning_info(self):
        r"""Gets the live_warning_info of this StartSmartLiveResponse.

        开播风险告警列表。

        :return: The live_warning_info of this StartSmartLiveResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveWarningItem`]
        """
        return self._live_warning_info

    @live_warning_info.setter
    def live_warning_info(self, live_warning_info):
        r"""Sets the live_warning_info of this StartSmartLiveResponse.

        开播风险告警列表。

        :param live_warning_info: The live_warning_info of this StartSmartLiveResponse.
        :type live_warning_info: list[:class:`huaweicloudsdkmetastudio.v1.LiveWarningItem`]
        """
        self._live_warning_info = live_warning_info

    @property
    def limit_duration(self):
        r"""Gets the limit_duration of this StartSmartLiveResponse.

        **参数解释**： 配置的最大直播时长。单位小时。 0 为不限制。 **约束限制**： 停止直播逻辑配置为立即停止则直播停止误差在5分钟之内。其他逻辑则加上处理时长。 **默认取值**： 不设置则表示不限时。

        :return: The limit_duration of this StartSmartLiveResponse.
        :rtype: int
        """
        return self._limit_duration

    @limit_duration.setter
    def limit_duration(self, limit_duration):
        r"""Sets the limit_duration of this StartSmartLiveResponse.

        **参数解释**： 配置的最大直播时长。单位小时。 0 为不限制。 **约束限制**： 停止直播逻辑配置为立即停止则直播停止误差在5分钟之内。其他逻辑则加上处理时长。 **默认取值**： 不设置则表示不限时。

        :param limit_duration: The limit_duration of this StartSmartLiveResponse.
        :type limit_duration: int
        """
        self._limit_duration = limit_duration

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this StartSmartLiveResponse.

        :return: The x_request_id of this StartSmartLiveResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this StartSmartLiveResponse.

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
