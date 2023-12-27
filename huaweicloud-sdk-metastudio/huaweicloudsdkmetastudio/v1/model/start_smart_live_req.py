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
        'live_event_callback_config': 'LiveEventCallBackConfig'
    }

    attribute_map = {
        'video_config': 'video_config',
        'play_policy': 'play_policy',
        'output_urls': 'output_urls',
        'stream_keys': 'stream_keys',
        'interaction_callback_url': 'interaction_callback_url',
        'live_event_callback_config': 'live_event_callback_config'
    }

    def __init__(self, video_config=None, play_policy=None, output_urls=None, stream_keys=None, interaction_callback_url=None, live_event_callback_config=None):
        """StartSmartLiveReq

        The model defined in huaweicloud sdk

        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param play_policy: 
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        :param output_urls: RTMP视频推流第三方直播平台地址。
        :type output_urls: list[str]
        :param stream_keys: RTMP视频推流第三方直播平台流秘钥，与推流地址对应。
        :type stream_keys: list[str]
        :param interaction_callback_url: 互动回调URL，含鉴权信息。
        :type interaction_callback_url: str
        :param live_event_callback_config: 
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        
        

        self._video_config = None
        self._play_policy = None
        self._output_urls = None
        self._stream_keys = None
        self._interaction_callback_url = None
        self._live_event_callback_config = None
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

    @property
    def video_config(self):
        """Gets the video_config of this StartSmartLiveReq.

        :return: The video_config of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this StartSmartLiveReq.

        :param video_config: The video_config of this StartSmartLiveReq.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def play_policy(self):
        """Gets the play_policy of this StartSmartLiveReq.

        :return: The play_policy of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        return self._play_policy

    @play_policy.setter
    def play_policy(self, play_policy):
        """Sets the play_policy of this StartSmartLiveReq.

        :param play_policy: The play_policy of this StartSmartLiveReq.
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        self._play_policy = play_policy

    @property
    def output_urls(self):
        """Gets the output_urls of this StartSmartLiveReq.

        RTMP视频推流第三方直播平台地址。

        :return: The output_urls of this StartSmartLiveReq.
        :rtype: list[str]
        """
        return self._output_urls

    @output_urls.setter
    def output_urls(self, output_urls):
        """Sets the output_urls of this StartSmartLiveReq.

        RTMP视频推流第三方直播平台地址。

        :param output_urls: The output_urls of this StartSmartLiveReq.
        :type output_urls: list[str]
        """
        self._output_urls = output_urls

    @property
    def stream_keys(self):
        """Gets the stream_keys of this StartSmartLiveReq.

        RTMP视频推流第三方直播平台流秘钥，与推流地址对应。

        :return: The stream_keys of this StartSmartLiveReq.
        :rtype: list[str]
        """
        return self._stream_keys

    @stream_keys.setter
    def stream_keys(self, stream_keys):
        """Sets the stream_keys of this StartSmartLiveReq.

        RTMP视频推流第三方直播平台流秘钥，与推流地址对应。

        :param stream_keys: The stream_keys of this StartSmartLiveReq.
        :type stream_keys: list[str]
        """
        self._stream_keys = stream_keys

    @property
    def interaction_callback_url(self):
        """Gets the interaction_callback_url of this StartSmartLiveReq.

        互动回调URL，含鉴权信息。

        :return: The interaction_callback_url of this StartSmartLiveReq.
        :rtype: str
        """
        return self._interaction_callback_url

    @interaction_callback_url.setter
    def interaction_callback_url(self, interaction_callback_url):
        """Sets the interaction_callback_url of this StartSmartLiveReq.

        互动回调URL，含鉴权信息。

        :param interaction_callback_url: The interaction_callback_url of this StartSmartLiveReq.
        :type interaction_callback_url: str
        """
        self._interaction_callback_url = interaction_callback_url

    @property
    def live_event_callback_config(self):
        """Gets the live_event_callback_config of this StartSmartLiveReq.

        :return: The live_event_callback_config of this StartSmartLiveReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        return self._live_event_callback_config

    @live_event_callback_config.setter
    def live_event_callback_config(self, live_event_callback_config):
        """Sets the live_event_callback_config of this StartSmartLiveReq.

        :param live_event_callback_config: The live_event_callback_config of this StartSmartLiveReq.
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        self._live_event_callback_config = live_event_callback_config

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
