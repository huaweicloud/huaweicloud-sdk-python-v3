# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSmartLiveRoomReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'room_name': 'str',
        'room_description': 'str',
        'room_type': 'str',
        'scene_scripts': 'list[LiveVideoScriptInfo]',
        'interaction_rules': 'list[LiveRoomInteractionRuleInfo]',
        'play_policy': 'PlayPolicy',
        'video_config': 'VideoConfig',
        'output_urls': 'list[str]',
        'stream_keys': 'list[str]',
        'backup_model_asset_ids': 'list[str]',
        'live_event_callback_config': 'LiveEventCallBackConfig',
        'rtc_callback_config': 'RTCLiveEventCallBackConfig',
        'review_config': 'ReviewConfig',
        'shared_config': 'SharedConfig',
        'view_mode': 'str',
        'co_streamer_config': 'CoStreamerConfig',
        'priv_data': 'str'
    }

    attribute_map = {
        'room_name': 'room_name',
        'room_description': 'room_description',
        'room_type': 'room_type',
        'scene_scripts': 'scene_scripts',
        'interaction_rules': 'interaction_rules',
        'play_policy': 'play_policy',
        'video_config': 'video_config',
        'output_urls': 'output_urls',
        'stream_keys': 'stream_keys',
        'backup_model_asset_ids': 'backup_model_asset_ids',
        'live_event_callback_config': 'live_event_callback_config',
        'rtc_callback_config': 'rtc_callback_config',
        'review_config': 'review_config',
        'shared_config': 'shared_config',
        'view_mode': 'view_mode',
        'co_streamer_config': 'co_streamer_config',
        'priv_data': 'priv_data'
    }

    def __init__(self, room_name=None, room_description=None, room_type=None, scene_scripts=None, interaction_rules=None, play_policy=None, video_config=None, output_urls=None, stream_keys=None, backup_model_asset_ids=None, live_event_callback_config=None, rtc_callback_config=None, review_config=None, shared_config=None, view_mode=None, co_streamer_config=None, priv_data=None):
        """CreateSmartLiveRoomReq

        The model defined in huaweicloud sdk

        :param room_name: 直播间名称
        :type room_name: str
        :param room_description: 直播间描述。
        :type room_description: str
        :param room_type: 直播间类型。 * NORMAL: 普通直播间，直播间一直存在，可以反复开播 * TEMP: 临时直播间,直播任务结束后自动清理直播间。 * TEMPLATE: 直播间模板。
        :type room_type: str
        :param scene_scripts: 默认直播剧本列表。
        :type scene_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LiveVideoScriptInfo`]
        :param interaction_rules: 互动规则列表
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionRuleInfo`]
        :param play_policy: 
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param output_urls: RTMP视频推流第三方直播平台地址。
        :type output_urls: list[str]
        :param stream_keys: RTMP视频推流第三方直播平台流秘钥，与推流地址对应。
        :type stream_keys: list[str]
        :param backup_model_asset_ids: 主播轮换时备选主播数字人资产ID（仅形象资产，不包含音色），可以从资产库中查询。
        :type backup_model_asset_ids: list[str]
        :param live_event_callback_config: 
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        :param rtc_callback_config: 
        :type rtc_callback_config: :class:`huaweicloudsdkmetastudio.v1.RTCLiveEventCallBackConfig`
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param shared_config: 
        :type shared_config: :class:`huaweicloudsdkmetastudio.v1.SharedConfig`
        :param view_mode: 横竖屏类型。默认值为：VERTICAL。 * LANDSCAPE：横屏。 * VERTICAL： 竖屏。
        :type view_mode: str
        :param co_streamer_config: 
        :type co_streamer_config: :class:`huaweicloudsdkmetastudio.v1.CoStreamerConfig`
        :param priv_data: 私有数据，用户填写，原样带回。
        :type priv_data: str
        """
        
        

        self._room_name = None
        self._room_description = None
        self._room_type = None
        self._scene_scripts = None
        self._interaction_rules = None
        self._play_policy = None
        self._video_config = None
        self._output_urls = None
        self._stream_keys = None
        self._backup_model_asset_ids = None
        self._live_event_callback_config = None
        self._rtc_callback_config = None
        self._review_config = None
        self._shared_config = None
        self._view_mode = None
        self._co_streamer_config = None
        self._priv_data = None
        self.discriminator = None

        self.room_name = room_name
        if room_description is not None:
            self.room_description = room_description
        if room_type is not None:
            self.room_type = room_type
        if scene_scripts is not None:
            self.scene_scripts = scene_scripts
        if interaction_rules is not None:
            self.interaction_rules = interaction_rules
        if play_policy is not None:
            self.play_policy = play_policy
        if video_config is not None:
            self.video_config = video_config
        if output_urls is not None:
            self.output_urls = output_urls
        if stream_keys is not None:
            self.stream_keys = stream_keys
        if backup_model_asset_ids is not None:
            self.backup_model_asset_ids = backup_model_asset_ids
        if live_event_callback_config is not None:
            self.live_event_callback_config = live_event_callback_config
        if rtc_callback_config is not None:
            self.rtc_callback_config = rtc_callback_config
        if review_config is not None:
            self.review_config = review_config
        if shared_config is not None:
            self.shared_config = shared_config
        if view_mode is not None:
            self.view_mode = view_mode
        if co_streamer_config is not None:
            self.co_streamer_config = co_streamer_config
        if priv_data is not None:
            self.priv_data = priv_data

    @property
    def room_name(self):
        """Gets the room_name of this CreateSmartLiveRoomReq.

        直播间名称

        :return: The room_name of this CreateSmartLiveRoomReq.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        """Sets the room_name of this CreateSmartLiveRoomReq.

        直播间名称

        :param room_name: The room_name of this CreateSmartLiveRoomReq.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_description(self):
        """Gets the room_description of this CreateSmartLiveRoomReq.

        直播间描述。

        :return: The room_description of this CreateSmartLiveRoomReq.
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        """Sets the room_description of this CreateSmartLiveRoomReq.

        直播间描述。

        :param room_description: The room_description of this CreateSmartLiveRoomReq.
        :type room_description: str
        """
        self._room_description = room_description

    @property
    def room_type(self):
        """Gets the room_type of this CreateSmartLiveRoomReq.

        直播间类型。 * NORMAL: 普通直播间，直播间一直存在，可以反复开播 * TEMP: 临时直播间,直播任务结束后自动清理直播间。 * TEMPLATE: 直播间模板。

        :return: The room_type of this CreateSmartLiveRoomReq.
        :rtype: str
        """
        return self._room_type

    @room_type.setter
    def room_type(self, room_type):
        """Sets the room_type of this CreateSmartLiveRoomReq.

        直播间类型。 * NORMAL: 普通直播间，直播间一直存在，可以反复开播 * TEMP: 临时直播间,直播任务结束后自动清理直播间。 * TEMPLATE: 直播间模板。

        :param room_type: The room_type of this CreateSmartLiveRoomReq.
        :type room_type: str
        """
        self._room_type = room_type

    @property
    def scene_scripts(self):
        """Gets the scene_scripts of this CreateSmartLiveRoomReq.

        默认直播剧本列表。

        :return: The scene_scripts of this CreateSmartLiveRoomReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveVideoScriptInfo`]
        """
        return self._scene_scripts

    @scene_scripts.setter
    def scene_scripts(self, scene_scripts):
        """Sets the scene_scripts of this CreateSmartLiveRoomReq.

        默认直播剧本列表。

        :param scene_scripts: The scene_scripts of this CreateSmartLiveRoomReq.
        :type scene_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LiveVideoScriptInfo`]
        """
        self._scene_scripts = scene_scripts

    @property
    def interaction_rules(self):
        """Gets the interaction_rules of this CreateSmartLiveRoomReq.

        互动规则列表

        :return: The interaction_rules of this CreateSmartLiveRoomReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionRuleInfo`]
        """
        return self._interaction_rules

    @interaction_rules.setter
    def interaction_rules(self, interaction_rules):
        """Sets the interaction_rules of this CreateSmartLiveRoomReq.

        互动规则列表

        :param interaction_rules: The interaction_rules of this CreateSmartLiveRoomReq.
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionRuleInfo`]
        """
        self._interaction_rules = interaction_rules

    @property
    def play_policy(self):
        """Gets the play_policy of this CreateSmartLiveRoomReq.

        :return: The play_policy of this CreateSmartLiveRoomReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        return self._play_policy

    @play_policy.setter
    def play_policy(self, play_policy):
        """Sets the play_policy of this CreateSmartLiveRoomReq.

        :param play_policy: The play_policy of this CreateSmartLiveRoomReq.
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        self._play_policy = play_policy

    @property
    def video_config(self):
        """Gets the video_config of this CreateSmartLiveRoomReq.

        :return: The video_config of this CreateSmartLiveRoomReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this CreateSmartLiveRoomReq.

        :param video_config: The video_config of this CreateSmartLiveRoomReq.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def output_urls(self):
        """Gets the output_urls of this CreateSmartLiveRoomReq.

        RTMP视频推流第三方直播平台地址。

        :return: The output_urls of this CreateSmartLiveRoomReq.
        :rtype: list[str]
        """
        return self._output_urls

    @output_urls.setter
    def output_urls(self, output_urls):
        """Sets the output_urls of this CreateSmartLiveRoomReq.

        RTMP视频推流第三方直播平台地址。

        :param output_urls: The output_urls of this CreateSmartLiveRoomReq.
        :type output_urls: list[str]
        """
        self._output_urls = output_urls

    @property
    def stream_keys(self):
        """Gets the stream_keys of this CreateSmartLiveRoomReq.

        RTMP视频推流第三方直播平台流秘钥，与推流地址对应。

        :return: The stream_keys of this CreateSmartLiveRoomReq.
        :rtype: list[str]
        """
        return self._stream_keys

    @stream_keys.setter
    def stream_keys(self, stream_keys):
        """Sets the stream_keys of this CreateSmartLiveRoomReq.

        RTMP视频推流第三方直播平台流秘钥，与推流地址对应。

        :param stream_keys: The stream_keys of this CreateSmartLiveRoomReq.
        :type stream_keys: list[str]
        """
        self._stream_keys = stream_keys

    @property
    def backup_model_asset_ids(self):
        """Gets the backup_model_asset_ids of this CreateSmartLiveRoomReq.

        主播轮换时备选主播数字人资产ID（仅形象资产，不包含音色），可以从资产库中查询。

        :return: The backup_model_asset_ids of this CreateSmartLiveRoomReq.
        :rtype: list[str]
        """
        return self._backup_model_asset_ids

    @backup_model_asset_ids.setter
    def backup_model_asset_ids(self, backup_model_asset_ids):
        """Sets the backup_model_asset_ids of this CreateSmartLiveRoomReq.

        主播轮换时备选主播数字人资产ID（仅形象资产，不包含音色），可以从资产库中查询。

        :param backup_model_asset_ids: The backup_model_asset_ids of this CreateSmartLiveRoomReq.
        :type backup_model_asset_ids: list[str]
        """
        self._backup_model_asset_ids = backup_model_asset_ids

    @property
    def live_event_callback_config(self):
        """Gets the live_event_callback_config of this CreateSmartLiveRoomReq.

        :return: The live_event_callback_config of this CreateSmartLiveRoomReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        return self._live_event_callback_config

    @live_event_callback_config.setter
    def live_event_callback_config(self, live_event_callback_config):
        """Sets the live_event_callback_config of this CreateSmartLiveRoomReq.

        :param live_event_callback_config: The live_event_callback_config of this CreateSmartLiveRoomReq.
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveEventCallBackConfig`
        """
        self._live_event_callback_config = live_event_callback_config

    @property
    def rtc_callback_config(self):
        """Gets the rtc_callback_config of this CreateSmartLiveRoomReq.

        :return: The rtc_callback_config of this CreateSmartLiveRoomReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RTCLiveEventCallBackConfig`
        """
        return self._rtc_callback_config

    @rtc_callback_config.setter
    def rtc_callback_config(self, rtc_callback_config):
        """Sets the rtc_callback_config of this CreateSmartLiveRoomReq.

        :param rtc_callback_config: The rtc_callback_config of this CreateSmartLiveRoomReq.
        :type rtc_callback_config: :class:`huaweicloudsdkmetastudio.v1.RTCLiveEventCallBackConfig`
        """
        self._rtc_callback_config = rtc_callback_config

    @property
    def review_config(self):
        """Gets the review_config of this CreateSmartLiveRoomReq.

        :return: The review_config of this CreateSmartLiveRoomReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        """Sets the review_config of this CreateSmartLiveRoomReq.

        :param review_config: The review_config of this CreateSmartLiveRoomReq.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def shared_config(self):
        """Gets the shared_config of this CreateSmartLiveRoomReq.

        :return: The shared_config of this CreateSmartLiveRoomReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SharedConfig`
        """
        return self._shared_config

    @shared_config.setter
    def shared_config(self, shared_config):
        """Sets the shared_config of this CreateSmartLiveRoomReq.

        :param shared_config: The shared_config of this CreateSmartLiveRoomReq.
        :type shared_config: :class:`huaweicloudsdkmetastudio.v1.SharedConfig`
        """
        self._shared_config = shared_config

    @property
    def view_mode(self):
        """Gets the view_mode of this CreateSmartLiveRoomReq.

        横竖屏类型。默认值为：VERTICAL。 * LANDSCAPE：横屏。 * VERTICAL： 竖屏。

        :return: The view_mode of this CreateSmartLiveRoomReq.
        :rtype: str
        """
        return self._view_mode

    @view_mode.setter
    def view_mode(self, view_mode):
        """Sets the view_mode of this CreateSmartLiveRoomReq.

        横竖屏类型。默认值为：VERTICAL。 * LANDSCAPE：横屏。 * VERTICAL： 竖屏。

        :param view_mode: The view_mode of this CreateSmartLiveRoomReq.
        :type view_mode: str
        """
        self._view_mode = view_mode

    @property
    def co_streamer_config(self):
        """Gets the co_streamer_config of this CreateSmartLiveRoomReq.

        :return: The co_streamer_config of this CreateSmartLiveRoomReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CoStreamerConfig`
        """
        return self._co_streamer_config

    @co_streamer_config.setter
    def co_streamer_config(self, co_streamer_config):
        """Sets the co_streamer_config of this CreateSmartLiveRoomReq.

        :param co_streamer_config: The co_streamer_config of this CreateSmartLiveRoomReq.
        :type co_streamer_config: :class:`huaweicloudsdkmetastudio.v1.CoStreamerConfig`
        """
        self._co_streamer_config = co_streamer_config

    @property
    def priv_data(self):
        """Gets the priv_data of this CreateSmartLiveRoomReq.

        私有数据，用户填写，原样带回。

        :return: The priv_data of this CreateSmartLiveRoomReq.
        :rtype: str
        """
        return self._priv_data

    @priv_data.setter
    def priv_data(self, priv_data):
        """Sets the priv_data of this CreateSmartLiveRoomReq.

        私有数据，用户填写，原样带回。

        :param priv_data: The priv_data of this CreateSmartLiveRoomReq.
        :type priv_data: str
        """
        self._priv_data = priv_data

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
        if not isinstance(other, CreateSmartLiveRoomReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
