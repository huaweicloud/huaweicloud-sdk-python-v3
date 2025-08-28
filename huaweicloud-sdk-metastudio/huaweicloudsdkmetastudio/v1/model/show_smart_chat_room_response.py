# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSmartChatRoomResponse(SdkResponse):

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
        'video_config': 'VideoConfig',
        'model_asset_id': 'str',
        'voice_config': 'VoiceConfig',
        'voice_config_list': 'list[ChatVoiceConfig]',
        'robot_id': 'str',
        'billing_mode': 'str',
        'reuse_resource': 'bool',
        'concurrency': 'int',
        'client_nums': 'int',
        'default_language': 'str',
        'background_config': 'BackgroundConfigInfo',
        'layer_config': 'list[LayerConfig]',
        'review_config': 'ReviewConfig',
        'chat_subtitle_config': 'ChatSubtitleConfig',
        'chat_video_type': 'str',
        'exit_mute_threshold': 'int',
        'room_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'cover_url': 'str',
        'is_pool_mode': 'bool',
        'chat_resource_config': 'list[ChatResourceConfigInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'room_name': 'room_name',
        'room_description': 'room_description',
        'video_config': 'video_config',
        'model_asset_id': 'model_asset_id',
        'voice_config': 'voice_config',
        'voice_config_list': 'voice_config_list',
        'robot_id': 'robot_id',
        'billing_mode': 'billing_mode',
        'reuse_resource': 'reuse_resource',
        'concurrency': 'concurrency',
        'client_nums': 'client_nums',
        'default_language': 'default_language',
        'background_config': 'background_config',
        'layer_config': 'layer_config',
        'review_config': 'review_config',
        'chat_subtitle_config': 'chat_subtitle_config',
        'chat_video_type': 'chat_video_type',
        'exit_mute_threshold': 'exit_mute_threshold',
        'room_id': 'room_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'cover_url': 'cover_url',
        'is_pool_mode': 'is_pool_mode',
        'chat_resource_config': 'chat_resource_config',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, room_name=None, room_description=None, video_config=None, model_asset_id=None, voice_config=None, voice_config_list=None, robot_id=None, billing_mode=None, reuse_resource=None, concurrency=None, client_nums=None, default_language=None, background_config=None, layer_config=None, review_config=None, chat_subtitle_config=None, chat_video_type=None, exit_mute_threshold=None, room_id=None, create_time=None, update_time=None, cover_url=None, is_pool_mode=None, chat_resource_config=None, x_request_id=None):
        r"""ShowSmartChatRoomResponse

        The model defined in huaweicloud sdk

        :param room_name: 对话名称
        :type room_name: str
        :param room_description: 对话描述。
        :type room_description: str
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param model_asset_id: 数字人模型资产ID。
        :type model_asset_id: str
        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param voice_config_list: 语音配置参数列表。
        :type voice_config_list: list[:class:`huaweicloudsdkmetastudio.v1.ChatVoiceConfig`]
        :param robot_id: 机器人ID。获取方法请参考[创建应用](CreateRobot.xml)。
        :type robot_id: str
        :param billing_mode: 计费模式，默认值CONCURRENCY * CONCURRENCY：并发计费 * CLIENT：按接入端计费 * CLIENT_TOKENS: 按接入端计费（TOKENS）
        :type billing_mode: str
        :param reuse_resource: 是否允许使用未分配的并发数（端模式下不能复用），默认不使用。
        :type reuse_resource: bool
        :param concurrency: **参数解释**： 并发路数。 **约束限制**： 默认没有并发路数，如果不配置并发数量，则无法启动智能交互对话任务。
        :type concurrency: int
        :param client_nums: **参数解释**： 允许接入终端端数量。
        :type client_nums: int
        :param default_language: 默认语言，智能交互接口使用。默认值CN。 * CN：简体中文。 * EN：英语。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）
        :type default_language: str
        :param background_config: 
        :type background_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`
        :param layer_config: 图层配置。
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param chat_subtitle_config: 
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        :param chat_video_type: 智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏
        :type chat_video_type: str
        :param exit_mute_threshold: **参数解释**： 静默退出时长。
        :type exit_mute_threshold: int
        :param room_id: 对话ID。
        :type room_id: str
        :param create_time: 智能交互对话创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type create_time: str
        :param update_time: 智能交互对话更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type update_time: str
        :param cover_url: 对话封面图URL
        :type cover_url: str
        :param is_pool_mode: 是否是资源池模式
        :type is_pool_mode: bool
        :param chat_resource_config: 资源配置。
        :type chat_resource_config: list[:class:`huaweicloudsdkmetastudio.v1.ChatResourceConfigInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowSmartChatRoomResponse, self).__init__()

        self._room_name = None
        self._room_description = None
        self._video_config = None
        self._model_asset_id = None
        self._voice_config = None
        self._voice_config_list = None
        self._robot_id = None
        self._billing_mode = None
        self._reuse_resource = None
        self._concurrency = None
        self._client_nums = None
        self._default_language = None
        self._background_config = None
        self._layer_config = None
        self._review_config = None
        self._chat_subtitle_config = None
        self._chat_video_type = None
        self._exit_mute_threshold = None
        self._room_id = None
        self._create_time = None
        self._update_time = None
        self._cover_url = None
        self._is_pool_mode = None
        self._chat_resource_config = None
        self._x_request_id = None
        self.discriminator = None

        self.room_name = room_name
        if room_description is not None:
            self.room_description = room_description
        if video_config is not None:
            self.video_config = video_config
        if model_asset_id is not None:
            self.model_asset_id = model_asset_id
        if voice_config is not None:
            self.voice_config = voice_config
        if voice_config_list is not None:
            self.voice_config_list = voice_config_list
        if robot_id is not None:
            self.robot_id = robot_id
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if reuse_resource is not None:
            self.reuse_resource = reuse_resource
        if concurrency is not None:
            self.concurrency = concurrency
        if client_nums is not None:
            self.client_nums = client_nums
        if default_language is not None:
            self.default_language = default_language
        if background_config is not None:
            self.background_config = background_config
        if layer_config is not None:
            self.layer_config = layer_config
        if review_config is not None:
            self.review_config = review_config
        if chat_subtitle_config is not None:
            self.chat_subtitle_config = chat_subtitle_config
        if chat_video_type is not None:
            self.chat_video_type = chat_video_type
        if exit_mute_threshold is not None:
            self.exit_mute_threshold = exit_mute_threshold
        if room_id is not None:
            self.room_id = room_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if cover_url is not None:
            self.cover_url = cover_url
        if is_pool_mode is not None:
            self.is_pool_mode = is_pool_mode
        if chat_resource_config is not None:
            self.chat_resource_config = chat_resource_config
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def room_name(self):
        r"""Gets the room_name of this ShowSmartChatRoomResponse.

        对话名称

        :return: The room_name of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        r"""Sets the room_name of this ShowSmartChatRoomResponse.

        对话名称

        :param room_name: The room_name of this ShowSmartChatRoomResponse.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_description(self):
        r"""Gets the room_description of this ShowSmartChatRoomResponse.

        对话描述。

        :return: The room_description of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        r"""Sets the room_description of this ShowSmartChatRoomResponse.

        对话描述。

        :param room_description: The room_description of this ShowSmartChatRoomResponse.
        :type room_description: str
        """
        self._room_description = room_description

    @property
    def video_config(self):
        r"""Gets the video_config of this ShowSmartChatRoomResponse.

        :return: The video_config of this ShowSmartChatRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        r"""Sets the video_config of this ShowSmartChatRoomResponse.

        :param video_config: The video_config of this ShowSmartChatRoomResponse.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def model_asset_id(self):
        r"""Gets the model_asset_id of this ShowSmartChatRoomResponse.

        数字人模型资产ID。

        :return: The model_asset_id of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        r"""Sets the model_asset_id of this ShowSmartChatRoomResponse.

        数字人模型资产ID。

        :param model_asset_id: The model_asset_id of this ShowSmartChatRoomResponse.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def voice_config(self):
        r"""Gets the voice_config of this ShowSmartChatRoomResponse.

        :return: The voice_config of this ShowSmartChatRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        r"""Sets the voice_config of this ShowSmartChatRoomResponse.

        :param voice_config: The voice_config of this ShowSmartChatRoomResponse.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def voice_config_list(self):
        r"""Gets the voice_config_list of this ShowSmartChatRoomResponse.

        语音配置参数列表。

        :return: The voice_config_list of this ShowSmartChatRoomResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ChatVoiceConfig`]
        """
        return self._voice_config_list

    @voice_config_list.setter
    def voice_config_list(self, voice_config_list):
        r"""Sets the voice_config_list of this ShowSmartChatRoomResponse.

        语音配置参数列表。

        :param voice_config_list: The voice_config_list of this ShowSmartChatRoomResponse.
        :type voice_config_list: list[:class:`huaweicloudsdkmetastudio.v1.ChatVoiceConfig`]
        """
        self._voice_config_list = voice_config_list

    @property
    def robot_id(self):
        r"""Gets the robot_id of this ShowSmartChatRoomResponse.

        机器人ID。获取方法请参考[创建应用](CreateRobot.xml)。

        :return: The robot_id of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this ShowSmartChatRoomResponse.

        机器人ID。获取方法请参考[创建应用](CreateRobot.xml)。

        :param robot_id: The robot_id of this ShowSmartChatRoomResponse.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this ShowSmartChatRoomResponse.

        计费模式，默认值CONCURRENCY * CONCURRENCY：并发计费 * CLIENT：按接入端计费 * CLIENT_TOKENS: 按接入端计费（TOKENS）

        :return: The billing_mode of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this ShowSmartChatRoomResponse.

        计费模式，默认值CONCURRENCY * CONCURRENCY：并发计费 * CLIENT：按接入端计费 * CLIENT_TOKENS: 按接入端计费（TOKENS）

        :param billing_mode: The billing_mode of this ShowSmartChatRoomResponse.
        :type billing_mode: str
        """
        self._billing_mode = billing_mode

    @property
    def reuse_resource(self):
        r"""Gets the reuse_resource of this ShowSmartChatRoomResponse.

        是否允许使用未分配的并发数（端模式下不能复用），默认不使用。

        :return: The reuse_resource of this ShowSmartChatRoomResponse.
        :rtype: bool
        """
        return self._reuse_resource

    @reuse_resource.setter
    def reuse_resource(self, reuse_resource):
        r"""Sets the reuse_resource of this ShowSmartChatRoomResponse.

        是否允许使用未分配的并发数（端模式下不能复用），默认不使用。

        :param reuse_resource: The reuse_resource of this ShowSmartChatRoomResponse.
        :type reuse_resource: bool
        """
        self._reuse_resource = reuse_resource

    @property
    def concurrency(self):
        r"""Gets the concurrency of this ShowSmartChatRoomResponse.

        **参数解释**： 并发路数。 **约束限制**： 默认没有并发路数，如果不配置并发数量，则无法启动智能交互对话任务。

        :return: The concurrency of this ShowSmartChatRoomResponse.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        r"""Sets the concurrency of this ShowSmartChatRoomResponse.

        **参数解释**： 并发路数。 **约束限制**： 默认没有并发路数，如果不配置并发数量，则无法启动智能交互对话任务。

        :param concurrency: The concurrency of this ShowSmartChatRoomResponse.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def client_nums(self):
        r"""Gets the client_nums of this ShowSmartChatRoomResponse.

        **参数解释**： 允许接入终端端数量。

        :return: The client_nums of this ShowSmartChatRoomResponse.
        :rtype: int
        """
        return self._client_nums

    @client_nums.setter
    def client_nums(self, client_nums):
        r"""Sets the client_nums of this ShowSmartChatRoomResponse.

        **参数解释**： 允许接入终端端数量。

        :param client_nums: The client_nums of this ShowSmartChatRoomResponse.
        :type client_nums: int
        """
        self._client_nums = client_nums

    @property
    def default_language(self):
        r"""Gets the default_language of this ShowSmartChatRoomResponse.

        默认语言，智能交互接口使用。默认值CN。 * CN：简体中文。 * EN：英语。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :return: The default_language of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        r"""Sets the default_language of this ShowSmartChatRoomResponse.

        默认语言，智能交互接口使用。默认值CN。 * CN：简体中文。 * EN：英语。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :param default_language: The default_language of this ShowSmartChatRoomResponse.
        :type default_language: str
        """
        self._default_language = default_language

    @property
    def background_config(self):
        r"""Gets the background_config of this ShowSmartChatRoomResponse.

        :return: The background_config of this ShowSmartChatRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`
        """
        return self._background_config

    @background_config.setter
    def background_config(self, background_config):
        r"""Sets the background_config of this ShowSmartChatRoomResponse.

        :param background_config: The background_config of this ShowSmartChatRoomResponse.
        :type background_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`
        """
        self._background_config = background_config

    @property
    def layer_config(self):
        r"""Gets the layer_config of this ShowSmartChatRoomResponse.

        图层配置。

        :return: The layer_config of this ShowSmartChatRoomResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        return self._layer_config

    @layer_config.setter
    def layer_config(self, layer_config):
        r"""Sets the layer_config of this ShowSmartChatRoomResponse.

        图层配置。

        :param layer_config: The layer_config of this ShowSmartChatRoomResponse.
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        self._layer_config = layer_config

    @property
    def review_config(self):
        r"""Gets the review_config of this ShowSmartChatRoomResponse.

        :return: The review_config of this ShowSmartChatRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        r"""Sets the review_config of this ShowSmartChatRoomResponse.

        :param review_config: The review_config of this ShowSmartChatRoomResponse.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def chat_subtitle_config(self):
        r"""Gets the chat_subtitle_config of this ShowSmartChatRoomResponse.

        :return: The chat_subtitle_config of this ShowSmartChatRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        """
        return self._chat_subtitle_config

    @chat_subtitle_config.setter
    def chat_subtitle_config(self, chat_subtitle_config):
        r"""Sets the chat_subtitle_config of this ShowSmartChatRoomResponse.

        :param chat_subtitle_config: The chat_subtitle_config of this ShowSmartChatRoomResponse.
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        """
        self._chat_subtitle_config = chat_subtitle_config

    @property
    def chat_video_type(self):
        r"""Gets the chat_video_type of this ShowSmartChatRoomResponse.

        智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏

        :return: The chat_video_type of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._chat_video_type

    @chat_video_type.setter
    def chat_video_type(self, chat_video_type):
        r"""Sets the chat_video_type of this ShowSmartChatRoomResponse.

        智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏

        :param chat_video_type: The chat_video_type of this ShowSmartChatRoomResponse.
        :type chat_video_type: str
        """
        self._chat_video_type = chat_video_type

    @property
    def exit_mute_threshold(self):
        r"""Gets the exit_mute_threshold of this ShowSmartChatRoomResponse.

        **参数解释**： 静默退出时长。

        :return: The exit_mute_threshold of this ShowSmartChatRoomResponse.
        :rtype: int
        """
        return self._exit_mute_threshold

    @exit_mute_threshold.setter
    def exit_mute_threshold(self, exit_mute_threshold):
        r"""Sets the exit_mute_threshold of this ShowSmartChatRoomResponse.

        **参数解释**： 静默退出时长。

        :param exit_mute_threshold: The exit_mute_threshold of this ShowSmartChatRoomResponse.
        :type exit_mute_threshold: int
        """
        self._exit_mute_threshold = exit_mute_threshold

    @property
    def room_id(self):
        r"""Gets the room_id of this ShowSmartChatRoomResponse.

        对话ID。

        :return: The room_id of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this ShowSmartChatRoomResponse.

        对话ID。

        :param room_id: The room_id of this ShowSmartChatRoomResponse.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowSmartChatRoomResponse.

        智能交互对话创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The create_time of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowSmartChatRoomResponse.

        智能交互对话创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param create_time: The create_time of this ShowSmartChatRoomResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowSmartChatRoomResponse.

        智能交互对话更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The update_time of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowSmartChatRoomResponse.

        智能交互对话更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param update_time: The update_time of this ShowSmartChatRoomResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def cover_url(self):
        r"""Gets the cover_url of this ShowSmartChatRoomResponse.

        对话封面图URL

        :return: The cover_url of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        r"""Sets the cover_url of this ShowSmartChatRoomResponse.

        对话封面图URL

        :param cover_url: The cover_url of this ShowSmartChatRoomResponse.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def is_pool_mode(self):
        r"""Gets the is_pool_mode of this ShowSmartChatRoomResponse.

        是否是资源池模式

        :return: The is_pool_mode of this ShowSmartChatRoomResponse.
        :rtype: bool
        """
        return self._is_pool_mode

    @is_pool_mode.setter
    def is_pool_mode(self, is_pool_mode):
        r"""Sets the is_pool_mode of this ShowSmartChatRoomResponse.

        是否是资源池模式

        :param is_pool_mode: The is_pool_mode of this ShowSmartChatRoomResponse.
        :type is_pool_mode: bool
        """
        self._is_pool_mode = is_pool_mode

    @property
    def chat_resource_config(self):
        r"""Gets the chat_resource_config of this ShowSmartChatRoomResponse.

        资源配置。

        :return: The chat_resource_config of this ShowSmartChatRoomResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ChatResourceConfigInfo`]
        """
        return self._chat_resource_config

    @chat_resource_config.setter
    def chat_resource_config(self, chat_resource_config):
        r"""Sets the chat_resource_config of this ShowSmartChatRoomResponse.

        资源配置。

        :param chat_resource_config: The chat_resource_config of this ShowSmartChatRoomResponse.
        :type chat_resource_config: list[:class:`huaweicloudsdkmetastudio.v1.ChatResourceConfigInfo`]
        """
        self._chat_resource_config = chat_resource_config

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowSmartChatRoomResponse.

        :return: The x_request_id of this ShowSmartChatRoomResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowSmartChatRoomResponse.

        :param x_request_id: The x_request_id of this ShowSmartChatRoomResponse.
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
        if not isinstance(other, ShowSmartChatRoomResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
