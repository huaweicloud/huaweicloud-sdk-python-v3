# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSmartLiveRoomResponse(SdkResponse):

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
        'interaction_config': 'LiveRoomInteractionConfig',
        'interaction_rules': 'list[LiveRoomInteractionRuleInfo]',
        'play_policy': 'PlayPolicy',
        'video_config': 'VideoConfig',
        'output_urls': 'list[str]',
        'stream_keys': 'list[str]',
        'backup_model_asset_ids': 'list[str]',
        'live_event_callback_config': 'LiveRoomEventCallBackConfig',
        'rtc_callback_config': 'RTCLiveEventCallBackConfig',
        'review_config': 'ReviewConfig',
        'shared_config': 'SharedConfig',
        'view_mode': 'str',
        'co_streamer_config': 'CoStreamerConfig',
        'priv_data': 'str',
        'room_id': 'str',
        'relation_live_platform_info': 'PlatformLiveDetailInfo',
        'create_time': 'str',
        'update_time': 'str',
        'cover_url': 'str',
        'thumbnail': 'str',
        'room_state': 'str',
        'confirm_state': 'str',
        'script_version': 'str',
        'error_info': 'ErrorResponse',
        'x_request_id': 'str'
    }

    attribute_map = {
        'room_name': 'room_name',
        'room_description': 'room_description',
        'room_type': 'room_type',
        'scene_scripts': 'scene_scripts',
        'interaction_config': 'interaction_config',
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
        'priv_data': 'priv_data',
        'room_id': 'room_id',
        'relation_live_platform_info': 'relation_live_platform_info',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'cover_url': 'cover_url',
        'thumbnail': 'thumbnail',
        'room_state': 'room_state',
        'confirm_state': 'confirm_state',
        'script_version': 'script_version',
        'error_info': 'error_info',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, room_name=None, room_description=None, room_type=None, scene_scripts=None, interaction_config=None, interaction_rules=None, play_policy=None, video_config=None, output_urls=None, stream_keys=None, backup_model_asset_ids=None, live_event_callback_config=None, rtc_callback_config=None, review_config=None, shared_config=None, view_mode=None, co_streamer_config=None, priv_data=None, room_id=None, relation_live_platform_info=None, create_time=None, update_time=None, cover_url=None, thumbnail=None, room_state=None, confirm_state=None, script_version=None, error_info=None, x_request_id=None):
        r"""ShowSmartLiveRoomResponse

        The model defined in huaweicloud sdk

        :param room_name: **参数解释**： 直播间名称。 **约束限制**： 不涉及。 **取值范围**： 字符长度1-256位。 **默认取值**： 不涉及。
        :type room_name: str
        :param room_description: **参数解释**： 直播间描述。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-1024位。 **默认取值**： 不涉及。
        :type room_description: str
        :param room_type: **参数解释**： 直播间类型。 **约束限制**： 不涉及。 **取值范围**： * NORMAL：普通直播间，直播间一直存在，可以反复开播 * TEMP：临时直播间，直播任务结束后自动清理直播间。 * TEMPLATE：直播间模板。
        :type room_type: str
        :param scene_scripts: 默认直播剧本列表。
        :type scene_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LiveVideoScriptInfo`]
        :param interaction_config: 
        :type interaction_config: :class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionConfig`
        :param interaction_rules: 互动规则列表
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionRuleInfo`]
        :param play_policy: 
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param output_urls: **参数解释**： RTMP视频推流第三方直播平台地址。 &gt; 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。
        :type output_urls: list[str]
        :param stream_keys: **参数解释**： RTMP视频推流第三方直播平台流密钥，与推流地址对应。 &gt; 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。
        :type stream_keys: list[str]
        :param backup_model_asset_ids: **参数解释**： 主播轮换时备选主播数字人资产ID（仅形象资产，不包含声音）。  **约束限制**： 不涉及 **取值范围**： 当前最大支持5个备选主播。 数字人资产ID，字符长度0-64位。 **默认取值**： 不涉及
        :type backup_model_asset_ids: list[str]
        :param live_event_callback_config: 
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveRoomEventCallBackConfig`
        :param rtc_callback_config: 
        :type rtc_callback_config: :class:`huaweicloudsdkmetastudio.v1.RTCLiveEventCallBackConfig`
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param shared_config: 
        :type shared_config: :class:`huaweicloudsdkmetastudio.v1.SharedConfig`
        :param view_mode: **参数解释**： 横竖屏类型。 **约束限制**： 用户无需填写，通过video_config中分辨率判断 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL： 竖屏。
        :type view_mode: str
        :param co_streamer_config: 
        :type co_streamer_config: :class:`huaweicloudsdkmetastudio.v1.CoStreamerConfig`
        :param priv_data: **参数解释**： 匹配值私有数据，用户填写，原样带回。 **约束限制**： 不涉及 **取值范围**： 字符长度0-8192 **默认取值**： 不涉及。
        :type priv_data: str
        :param room_id: 直播间ID
        :type room_id: str
        :param relation_live_platform_info: 
        :type relation_live_platform_info: :class:`huaweicloudsdkmetastudio.v1.PlatformLiveDetailInfo`
        :param create_time: 直播间创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type create_time: str
        :param update_time: 直播间更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type update_time: str
        :param cover_url: 直播间封面图URL
        :type cover_url: str
        :param thumbnail: 直播间封面图新URL
        :type thumbnail: str
        :param room_state: 直播间配置状态。 - ENABLE: 直播间正常可用。 - DISABLE： 直播间不可用。不可用原因在error_info中说明。 - BLOCKED：直播间被冻结。冻结原因在error_info中说明。
        :type room_state: str
        :param confirm_state: 直播间确认状态。此状态仅用于特定用户需要人工确认场景。 - UNCONFIRM: 未确认 - CONFIRMED：已确认 - REJECT： 拒绝
        :type confirm_state: str
        :param script_version: 直播间剧本版本。调用update接口即更新版本。使用时间戳。
        :type script_version: str
        :param error_info: 
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowSmartLiveRoomResponse, self).__init__()

        self._room_name = None
        self._room_description = None
        self._room_type = None
        self._scene_scripts = None
        self._interaction_config = None
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
        self._room_id = None
        self._relation_live_platform_info = None
        self._create_time = None
        self._update_time = None
        self._cover_url = None
        self._thumbnail = None
        self._room_state = None
        self._confirm_state = None
        self._script_version = None
        self._error_info = None
        self._x_request_id = None
        self.discriminator = None

        self.room_name = room_name
        if room_description is not None:
            self.room_description = room_description
        if room_type is not None:
            self.room_type = room_type
        if scene_scripts is not None:
            self.scene_scripts = scene_scripts
        if interaction_config is not None:
            self.interaction_config = interaction_config
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
        if room_id is not None:
            self.room_id = room_id
        if relation_live_platform_info is not None:
            self.relation_live_platform_info = relation_live_platform_info
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if cover_url is not None:
            self.cover_url = cover_url
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if room_state is not None:
            self.room_state = room_state
        if confirm_state is not None:
            self.confirm_state = confirm_state
        if script_version is not None:
            self.script_version = script_version
        if error_info is not None:
            self.error_info = error_info
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def room_name(self):
        r"""Gets the room_name of this ShowSmartLiveRoomResponse.

        **参数解释**： 直播间名称。 **约束限制**： 不涉及。 **取值范围**： 字符长度1-256位。 **默认取值**： 不涉及。

        :return: The room_name of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        r"""Sets the room_name of this ShowSmartLiveRoomResponse.

        **参数解释**： 直播间名称。 **约束限制**： 不涉及。 **取值范围**： 字符长度1-256位。 **默认取值**： 不涉及。

        :param room_name: The room_name of this ShowSmartLiveRoomResponse.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_description(self):
        r"""Gets the room_description of this ShowSmartLiveRoomResponse.

        **参数解释**： 直播间描述。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-1024位。 **默认取值**： 不涉及。

        :return: The room_description of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        r"""Sets the room_description of this ShowSmartLiveRoomResponse.

        **参数解释**： 直播间描述。 **约束限制**： 不涉及。 **取值范围**： 字符长度0-1024位。 **默认取值**： 不涉及。

        :param room_description: The room_description of this ShowSmartLiveRoomResponse.
        :type room_description: str
        """
        self._room_description = room_description

    @property
    def room_type(self):
        r"""Gets the room_type of this ShowSmartLiveRoomResponse.

        **参数解释**： 直播间类型。 **约束限制**： 不涉及。 **取值范围**： * NORMAL：普通直播间，直播间一直存在，可以反复开播 * TEMP：临时直播间，直播任务结束后自动清理直播间。 * TEMPLATE：直播间模板。

        :return: The room_type of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._room_type

    @room_type.setter
    def room_type(self, room_type):
        r"""Sets the room_type of this ShowSmartLiveRoomResponse.

        **参数解释**： 直播间类型。 **约束限制**： 不涉及。 **取值范围**： * NORMAL：普通直播间，直播间一直存在，可以反复开播 * TEMP：临时直播间，直播任务结束后自动清理直播间。 * TEMPLATE：直播间模板。

        :param room_type: The room_type of this ShowSmartLiveRoomResponse.
        :type room_type: str
        """
        self._room_type = room_type

    @property
    def scene_scripts(self):
        r"""Gets the scene_scripts of this ShowSmartLiveRoomResponse.

        默认直播剧本列表。

        :return: The scene_scripts of this ShowSmartLiveRoomResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveVideoScriptInfo`]
        """
        return self._scene_scripts

    @scene_scripts.setter
    def scene_scripts(self, scene_scripts):
        r"""Sets the scene_scripts of this ShowSmartLiveRoomResponse.

        默认直播剧本列表。

        :param scene_scripts: The scene_scripts of this ShowSmartLiveRoomResponse.
        :type scene_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LiveVideoScriptInfo`]
        """
        self._scene_scripts = scene_scripts

    @property
    def interaction_config(self):
        r"""Gets the interaction_config of this ShowSmartLiveRoomResponse.

        :return: The interaction_config of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionConfig`
        """
        return self._interaction_config

    @interaction_config.setter
    def interaction_config(self, interaction_config):
        r"""Sets the interaction_config of this ShowSmartLiveRoomResponse.

        :param interaction_config: The interaction_config of this ShowSmartLiveRoomResponse.
        :type interaction_config: :class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionConfig`
        """
        self._interaction_config = interaction_config

    @property
    def interaction_rules(self):
        r"""Gets the interaction_rules of this ShowSmartLiveRoomResponse.

        互动规则列表

        :return: The interaction_rules of this ShowSmartLiveRoomResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionRuleInfo`]
        """
        return self._interaction_rules

    @interaction_rules.setter
    def interaction_rules(self, interaction_rules):
        r"""Sets the interaction_rules of this ShowSmartLiveRoomResponse.

        互动规则列表

        :param interaction_rules: The interaction_rules of this ShowSmartLiveRoomResponse.
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.LiveRoomInteractionRuleInfo`]
        """
        self._interaction_rules = interaction_rules

    @property
    def play_policy(self):
        r"""Gets the play_policy of this ShowSmartLiveRoomResponse.

        :return: The play_policy of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        return self._play_policy

    @play_policy.setter
    def play_policy(self, play_policy):
        r"""Sets the play_policy of this ShowSmartLiveRoomResponse.

        :param play_policy: The play_policy of this ShowSmartLiveRoomResponse.
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        self._play_policy = play_policy

    @property
    def video_config(self):
        r"""Gets the video_config of this ShowSmartLiveRoomResponse.

        :return: The video_config of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        r"""Sets the video_config of this ShowSmartLiveRoomResponse.

        :param video_config: The video_config of this ShowSmartLiveRoomResponse.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def output_urls(self):
        r"""Gets the output_urls of this ShowSmartLiveRoomResponse.

        **参数解释**： RTMP视频推流第三方直播平台地址。 > 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。

        :return: The output_urls of this ShowSmartLiveRoomResponse.
        :rtype: list[str]
        """
        return self._output_urls

    @output_urls.setter
    def output_urls(self, output_urls):
        r"""Sets the output_urls of this ShowSmartLiveRoomResponse.

        **参数解释**： RTMP视频推流第三方直播平台地址。 > 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。

        :param output_urls: The output_urls of this ShowSmartLiveRoomResponse.
        :type output_urls: list[str]
        """
        self._output_urls = output_urls

    @property
    def stream_keys(self):
        r"""Gets the stream_keys of this ShowSmartLiveRoomResponse.

        **参数解释**： RTMP视频推流第三方直播平台流密钥，与推流地址对应。 > 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。

        :return: The stream_keys of this ShowSmartLiveRoomResponse.
        :rtype: list[str]
        """
        return self._stream_keys

    @stream_keys.setter
    def stream_keys(self, stream_keys):
        r"""Sets the stream_keys of this ShowSmartLiveRoomResponse.

        **参数解释**： RTMP视频推流第三方直播平台流密钥，与推流地址对应。 > 直播过程中刷新地址，需要调用COMMAND命令REFRESH_OUTPUT_URL。  **约束限制**： 不涉及 **取值范围**： 当前仅支持一条RTMP出流地址。 **默认取值**： 不涉及。

        :param stream_keys: The stream_keys of this ShowSmartLiveRoomResponse.
        :type stream_keys: list[str]
        """
        self._stream_keys = stream_keys

    @property
    def backup_model_asset_ids(self):
        r"""Gets the backup_model_asset_ids of this ShowSmartLiveRoomResponse.

        **参数解释**： 主播轮换时备选主播数字人资产ID（仅形象资产，不包含声音）。  **约束限制**： 不涉及 **取值范围**： 当前最大支持5个备选主播。 数字人资产ID，字符长度0-64位。 **默认取值**： 不涉及

        :return: The backup_model_asset_ids of this ShowSmartLiveRoomResponse.
        :rtype: list[str]
        """
        return self._backup_model_asset_ids

    @backup_model_asset_ids.setter
    def backup_model_asset_ids(self, backup_model_asset_ids):
        r"""Sets the backup_model_asset_ids of this ShowSmartLiveRoomResponse.

        **参数解释**： 主播轮换时备选主播数字人资产ID（仅形象资产，不包含声音）。  **约束限制**： 不涉及 **取值范围**： 当前最大支持5个备选主播。 数字人资产ID，字符长度0-64位。 **默认取值**： 不涉及

        :param backup_model_asset_ids: The backup_model_asset_ids of this ShowSmartLiveRoomResponse.
        :type backup_model_asset_ids: list[str]
        """
        self._backup_model_asset_ids = backup_model_asset_ids

    @property
    def live_event_callback_config(self):
        r"""Gets the live_event_callback_config of this ShowSmartLiveRoomResponse.

        :return: The live_event_callback_config of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveRoomEventCallBackConfig`
        """
        return self._live_event_callback_config

    @live_event_callback_config.setter
    def live_event_callback_config(self, live_event_callback_config):
        r"""Sets the live_event_callback_config of this ShowSmartLiveRoomResponse.

        :param live_event_callback_config: The live_event_callback_config of this ShowSmartLiveRoomResponse.
        :type live_event_callback_config: :class:`huaweicloudsdkmetastudio.v1.LiveRoomEventCallBackConfig`
        """
        self._live_event_callback_config = live_event_callback_config

    @property
    def rtc_callback_config(self):
        r"""Gets the rtc_callback_config of this ShowSmartLiveRoomResponse.

        :return: The rtc_callback_config of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RTCLiveEventCallBackConfig`
        """
        return self._rtc_callback_config

    @rtc_callback_config.setter
    def rtc_callback_config(self, rtc_callback_config):
        r"""Sets the rtc_callback_config of this ShowSmartLiveRoomResponse.

        :param rtc_callback_config: The rtc_callback_config of this ShowSmartLiveRoomResponse.
        :type rtc_callback_config: :class:`huaweicloudsdkmetastudio.v1.RTCLiveEventCallBackConfig`
        """
        self._rtc_callback_config = rtc_callback_config

    @property
    def review_config(self):
        r"""Gets the review_config of this ShowSmartLiveRoomResponse.

        :return: The review_config of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        r"""Sets the review_config of this ShowSmartLiveRoomResponse.

        :param review_config: The review_config of this ShowSmartLiveRoomResponse.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def shared_config(self):
        r"""Gets the shared_config of this ShowSmartLiveRoomResponse.

        :return: The shared_config of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SharedConfig`
        """
        return self._shared_config

    @shared_config.setter
    def shared_config(self, shared_config):
        r"""Sets the shared_config of this ShowSmartLiveRoomResponse.

        :param shared_config: The shared_config of this ShowSmartLiveRoomResponse.
        :type shared_config: :class:`huaweicloudsdkmetastudio.v1.SharedConfig`
        """
        self._shared_config = shared_config

    @property
    def view_mode(self):
        r"""Gets the view_mode of this ShowSmartLiveRoomResponse.

        **参数解释**： 横竖屏类型。 **约束限制**： 用户无需填写，通过video_config中分辨率判断 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL： 竖屏。

        :return: The view_mode of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._view_mode

    @view_mode.setter
    def view_mode(self, view_mode):
        r"""Sets the view_mode of this ShowSmartLiveRoomResponse.

        **参数解释**： 横竖屏类型。 **约束限制**： 用户无需填写，通过video_config中分辨率判断 **取值范围**： * LANDSCAPE：横屏。 * VERTICAL： 竖屏。

        :param view_mode: The view_mode of this ShowSmartLiveRoomResponse.
        :type view_mode: str
        """
        self._view_mode = view_mode

    @property
    def co_streamer_config(self):
        r"""Gets the co_streamer_config of this ShowSmartLiveRoomResponse.

        :return: The co_streamer_config of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.CoStreamerConfig`
        """
        return self._co_streamer_config

    @co_streamer_config.setter
    def co_streamer_config(self, co_streamer_config):
        r"""Sets the co_streamer_config of this ShowSmartLiveRoomResponse.

        :param co_streamer_config: The co_streamer_config of this ShowSmartLiveRoomResponse.
        :type co_streamer_config: :class:`huaweicloudsdkmetastudio.v1.CoStreamerConfig`
        """
        self._co_streamer_config = co_streamer_config

    @property
    def priv_data(self):
        r"""Gets the priv_data of this ShowSmartLiveRoomResponse.

        **参数解释**： 匹配值私有数据，用户填写，原样带回。 **约束限制**： 不涉及 **取值范围**： 字符长度0-8192 **默认取值**： 不涉及。

        :return: The priv_data of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._priv_data

    @priv_data.setter
    def priv_data(self, priv_data):
        r"""Sets the priv_data of this ShowSmartLiveRoomResponse.

        **参数解释**： 匹配值私有数据，用户填写，原样带回。 **约束限制**： 不涉及 **取值范围**： 字符长度0-8192 **默认取值**： 不涉及。

        :param priv_data: The priv_data of this ShowSmartLiveRoomResponse.
        :type priv_data: str
        """
        self._priv_data = priv_data

    @property
    def room_id(self):
        r"""Gets the room_id of this ShowSmartLiveRoomResponse.

        直播间ID

        :return: The room_id of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this ShowSmartLiveRoomResponse.

        直播间ID

        :param room_id: The room_id of this ShowSmartLiveRoomResponse.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def relation_live_platform_info(self):
        r"""Gets the relation_live_platform_info of this ShowSmartLiveRoomResponse.

        :return: The relation_live_platform_info of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PlatformLiveDetailInfo`
        """
        return self._relation_live_platform_info

    @relation_live_platform_info.setter
    def relation_live_platform_info(self, relation_live_platform_info):
        r"""Sets the relation_live_platform_info of this ShowSmartLiveRoomResponse.

        :param relation_live_platform_info: The relation_live_platform_info of this ShowSmartLiveRoomResponse.
        :type relation_live_platform_info: :class:`huaweicloudsdkmetastudio.v1.PlatformLiveDetailInfo`
        """
        self._relation_live_platform_info = relation_live_platform_info

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSmartLiveRoomResponse.

        直播间创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The create_time of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSmartLiveRoomResponse.

        直播间创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param create_time: The create_time of this ShowSmartLiveRoomResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowSmartLiveRoomResponse.

        直播间更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The update_time of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowSmartLiveRoomResponse.

        直播间更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param update_time: The update_time of this ShowSmartLiveRoomResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def cover_url(self):
        r"""Gets the cover_url of this ShowSmartLiveRoomResponse.

        直播间封面图URL

        :return: The cover_url of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        r"""Sets the cover_url of this ShowSmartLiveRoomResponse.

        直播间封面图URL

        :param cover_url: The cover_url of this ShowSmartLiveRoomResponse.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def thumbnail(self):
        r"""Gets the thumbnail of this ShowSmartLiveRoomResponse.

        直播间封面图新URL

        :return: The thumbnail of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        r"""Sets the thumbnail of this ShowSmartLiveRoomResponse.

        直播间封面图新URL

        :param thumbnail: The thumbnail of this ShowSmartLiveRoomResponse.
        :type thumbnail: str
        """
        self._thumbnail = thumbnail

    @property
    def room_state(self):
        r"""Gets the room_state of this ShowSmartLiveRoomResponse.

        直播间配置状态。 - ENABLE: 直播间正常可用。 - DISABLE： 直播间不可用。不可用原因在error_info中说明。 - BLOCKED：直播间被冻结。冻结原因在error_info中说明。

        :return: The room_state of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._room_state

    @room_state.setter
    def room_state(self, room_state):
        r"""Sets the room_state of this ShowSmartLiveRoomResponse.

        直播间配置状态。 - ENABLE: 直播间正常可用。 - DISABLE： 直播间不可用。不可用原因在error_info中说明。 - BLOCKED：直播间被冻结。冻结原因在error_info中说明。

        :param room_state: The room_state of this ShowSmartLiveRoomResponse.
        :type room_state: str
        """
        self._room_state = room_state

    @property
    def confirm_state(self):
        r"""Gets the confirm_state of this ShowSmartLiveRoomResponse.

        直播间确认状态。此状态仅用于特定用户需要人工确认场景。 - UNCONFIRM: 未确认 - CONFIRMED：已确认 - REJECT： 拒绝

        :return: The confirm_state of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._confirm_state

    @confirm_state.setter
    def confirm_state(self, confirm_state):
        r"""Sets the confirm_state of this ShowSmartLiveRoomResponse.

        直播间确认状态。此状态仅用于特定用户需要人工确认场景。 - UNCONFIRM: 未确认 - CONFIRMED：已确认 - REJECT： 拒绝

        :param confirm_state: The confirm_state of this ShowSmartLiveRoomResponse.
        :type confirm_state: str
        """
        self._confirm_state = confirm_state

    @property
    def script_version(self):
        r"""Gets the script_version of this ShowSmartLiveRoomResponse.

        直播间剧本版本。调用update接口即更新版本。使用时间戳。

        :return: The script_version of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._script_version

    @script_version.setter
    def script_version(self, script_version):
        r"""Sets the script_version of this ShowSmartLiveRoomResponse.

        直播间剧本版本。调用update接口即更新版本。使用时间戳。

        :param script_version: The script_version of this ShowSmartLiveRoomResponse.
        :type script_version: str
        """
        self._script_version = script_version

    @property
    def error_info(self):
        r"""Gets the error_info of this ShowSmartLiveRoomResponse.

        :return: The error_info of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        r"""Sets the error_info of this ShowSmartLiveRoomResponse.

        :param error_info: The error_info of this ShowSmartLiveRoomResponse.
        :type error_info: :class:`huaweicloudsdkmetastudio.v1.ErrorResponse`
        """
        self._error_info = error_info

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowSmartLiveRoomResponse.

        :return: The x_request_id of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowSmartLiveRoomResponse.

        :param x_request_id: The x_request_id of this ShowSmartLiveRoomResponse.
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
        if not isinstance(other, ShowSmartLiveRoomResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
