# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartSmartLiveReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_config': 'VideoConfig',
        'play_policy': 'PlayPolicy',
        'output_urls': 'list[str]',
        'stream_keys': 'list[str]',
        'interaction_callback_url': 'str',
        'live_event_callback_config': 'LiveEventCallBackConfig',
        'rtc_callback_config': 'RTCLiveEventCallBackConfig',
        'view_mode': 'str',
        'co_streamer_config': 'CoStreamerConfig',
        'job_run_config': 'LiveJobRunConfig'
    }

    attribute_map = {
        'video_config': 'video_config',
        'play_policy': 'play_policy',
        'output_urls': 'output_urls',
        'stream_keys': 'stream_keys',
        'interaction_callback_url': 'interaction_callback_url',
        'live_event_callback_config': 'live_event_callback_config',
        'rtc_callback_config': 'rtc_callback_config',
        'view_mode': 'view_mode',
        'co_streamer_config': 'co_streamer_config',
        'job_run_config': 'job_run_config'
    }

    def __init__(self, video_config=None, play_policy=None, output_urls=None, stream_keys=None, interaction_callback_url=None, live_event_callback_config=None, rtc_callback_config=None, view_mode=None, co_streamer_config=None, job_run_config=None):
        r"""StartSmartLiveReq

        The model defined in huaweicloud sdk

        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param play_policy: 
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        :param output_urls: **参数解释**： RTMP视频推流第三方直播平台地址。 &gt; 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。
        :type output_urls: list[str]
        :param stream_keys: **参数解释**： RTMP视频推流第三方直播平台流密钥，与推流地址对应。 &gt; 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。
        :type stream_keys: list[str]
        :param interaction_callback_url: **参数解释**： 互动回调URL，含鉴权信息。 互动规则trigger.reply_mode配置为CALLBACK时填写 **约束限制**： 不涉及 **取值范围**： 字符长度0-2048位 **默认取值**： 不涉及。
        :type interaction_callback_url: str
        :param live_event_callback_config: 
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        :param rtc_callback_config: 
        :type rtc_callback_config: :class:`huaweicloudsdkmetastudio.v1.RTCLiveEventCallBackConfig`
        :param view_mode: **参数解释**： 横竖屏类型。 **约束限制**： 用户无需填写，通过video_config中分辨率判断 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL： 竖屏。
        :type view_mode: str
        :param co_streamer_config: 
        :type co_streamer_config: :class:`huaweicloudsdkmetastudio.v1.CoStreamerConfig`
        :param job_run_config: 
        :type job_run_config: :class:`huaweicloudsdkmetastudio.v1.LiveJobRunConfig`
        """
        
        

        self._video_config = None
        self._play_policy = None
        self._output_urls = None
        self._stream_keys = None
        self._interaction_callback_url = None
        self._live_event_callback_config = None
        self._rtc_callback_config = None
        self._view_mode = None
        self._co_streamer_config = None
        self._job_run_config = None
        self.discriminator = None

        if video_config is not None:
            self.video_config = video_config
        if play_policy is not None:
            self.play_policy = play_policy
        if output_urls is not None:
            self.output_urls = output_urls
        if stream_keys is not None:
            self.stream_keys = stream_keys
        if interaction_callback_url is not None:
            self.interaction_callback_url = interaction_callback_url
        if live_event_callback_config is not None:
            self.live_event_callback_config = live_event_callback_config
        if rtc_callback_config is not None:
            self.rtc_callback_config = rtc_callback_config
        if view_mode is not None:
            self.view_mode = view_mode
        if co_streamer_config is not None:
            self.co_streamer_config = co_streamer_config
        if job_run_config is not None:
            self.job_run_config = job_run_config

    @property
    def video_config(self):
        r"""Gets the video_config of this StartSmartLiveReq.

        :return: The video_config of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        r"""Sets the video_config of this StartSmartLiveReq.

        :param video_config: The video_config of this StartSmartLiveReq.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def play_policy(self):
        r"""Gets the play_policy of this StartSmartLiveReq.

        :return: The play_policy of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        return self._play_policy

    @play_policy.setter
    def play_policy(self, play_policy):
        r"""Sets the play_policy of this StartSmartLiveReq.

        :param play_policy: The play_policy of this StartSmartLiveReq.
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        self._play_policy = play_policy

    @property
    def output_urls(self):
        r"""Gets the output_urls of this StartSmartLiveReq.

        **参数解释**： RTMP视频推流第三方直播平台地址。 > 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。

        :return: The output_urls of this StartSmartLiveReq.
        :rtype: list[str]
        """
        return self._output_urls

    @output_urls.setter
    def output_urls(self, output_urls):
        r"""Sets the output_urls of this StartSmartLiveReq.

        **参数解释**： RTMP视频推流第三方直播平台地址。 > 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。

        :param output_urls: The output_urls of this StartSmartLiveReq.
        :type output_urls: list[str]
        """
        self._output_urls = output_urls

    @property
    def stream_keys(self):
        r"""Gets the stream_keys of this StartSmartLiveReq.

        **参数解释**： RTMP视频推流第三方直播平台流密钥，与推流地址对应。 > 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。

        :return: The stream_keys of this StartSmartLiveReq.
        :rtype: list[str]
        """
        return self._stream_keys

    @stream_keys.setter
    def stream_keys(self, stream_keys):
        r"""Sets the stream_keys of this StartSmartLiveReq.

        **参数解释**： RTMP视频推流第三方直播平台流密钥，与推流地址对应。 > 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。

        :param stream_keys: The stream_keys of this StartSmartLiveReq.
        :type stream_keys: list[str]
        """
        self._stream_keys = stream_keys

    @property
    def interaction_callback_url(self):
        r"""Gets the interaction_callback_url of this StartSmartLiveReq.

        **参数解释**： 互动回调URL，含鉴权信息。 互动规则trigger.reply_mode配置为CALLBACK时填写 **约束限制**： 不涉及 **取值范围**： 字符长度0-2048位 **默认取值**： 不涉及。

        :return: The interaction_callback_url of this StartSmartLiveReq.
        :rtype: str
        """
        return self._interaction_callback_url

    @interaction_callback_url.setter
    def interaction_callback_url(self, interaction_callback_url):
        r"""Sets the interaction_callback_url of this StartSmartLiveReq.

        **参数解释**： 互动回调URL，含鉴权信息。 互动规则trigger.reply_mode配置为CALLBACK时填写 **约束限制**： 不涉及 **取值范围**： 字符长度0-2048位 **默认取值**： 不涉及。

        :param interaction_callback_url: The interaction_callback_url of this StartSmartLiveReq.
        :type interaction_callback_url: str
        """
        self._interaction_callback_url = interaction_callback_url

    @property
    def live_event_callback_config(self):
        r"""Gets the live_event_callback_config of this StartSmartLiveReq.

        :return: The live_event_callback_config of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        return self._live_event_callback_config

    @live_event_callback_config.setter
    def live_event_callback_config(self, live_event_callback_config):
        r"""Sets the live_event_callback_config of this StartSmartLiveReq.

        :param live_event_callback_config: The live_event_callback_config of this StartSmartLiveReq.
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        self._live_event_callback_config = live_event_callback_config

    @property
    def rtc_callback_config(self):
        r"""Gets the rtc_callback_config of this StartSmartLiveReq.

        :return: The rtc_callback_config of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RTCLiveEventCallBackConfig`
        """
        return self._rtc_callback_config

    @rtc_callback_config.setter
    def rtc_callback_config(self, rtc_callback_config):
        r"""Sets the rtc_callback_config of this StartSmartLiveReq.

        :param rtc_callback_config: The rtc_callback_config of this StartSmartLiveReq.
        :type rtc_callback_config: :class:`huaweicloudsdkmetastudio.v1.RTCLiveEventCallBackConfig`
        """
        self._rtc_callback_config = rtc_callback_config

    @property
    def view_mode(self):
        r"""Gets the view_mode of this StartSmartLiveReq.

        **参数解释**： 横竖屏类型。 **约束限制**： 用户无需填写，通过video_config中分辨率判断 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL： 竖屏。

        :return: The view_mode of this StartSmartLiveReq.
        :rtype: str
        """
        return self._view_mode

    @view_mode.setter
    def view_mode(self, view_mode):
        r"""Sets the view_mode of this StartSmartLiveReq.

        **参数解释**： 横竖屏类型。 **约束限制**： 用户无需填写，通过video_config中分辨率判断 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL： 竖屏。

        :param view_mode: The view_mode of this StartSmartLiveReq.
        :type view_mode: str
        """
        self._view_mode = view_mode

    @property
    def co_streamer_config(self):
        r"""Gets the co_streamer_config of this StartSmartLiveReq.

        :return: The co_streamer_config of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CoStreamerConfig`
        """
        return self._co_streamer_config

    @co_streamer_config.setter
    def co_streamer_config(self, co_streamer_config):
        r"""Sets the co_streamer_config of this StartSmartLiveReq.

        :param co_streamer_config: The co_streamer_config of this StartSmartLiveReq.
        :type co_streamer_config: :class:`huaweicloudsdkmetastudio.v1.CoStreamerConfig`
        """
        self._co_streamer_config = co_streamer_config

    @property
    def job_run_config(self):
        r"""Gets the job_run_config of this StartSmartLiveReq.

        :return: The job_run_config of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveJobRunConfig`
        """
        return self._job_run_config

    @job_run_config.setter
    def job_run_config(self, job_run_config):
        r"""Sets the job_run_config of this StartSmartLiveReq.

        :param job_run_config: The job_run_config of this StartSmartLiveReq.
        :type job_run_config: :class:`huaweicloudsdkmetastudio.v1.LiveJobRunConfig`
        """
        self._job_run_config = job_run_config

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
        if not isinstance(other, StartSmartLiveReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
