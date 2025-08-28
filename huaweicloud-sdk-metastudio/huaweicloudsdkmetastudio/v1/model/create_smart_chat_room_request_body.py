# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSmartChatRoomRequestBody:

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
        'exit_mute_threshold': 'int'
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
        'exit_mute_threshold': 'exit_mute_threshold'
    }

    def __init__(self, room_name=None, room_description=None, video_config=None, model_asset_id=None, voice_config=None, voice_config_list=None, robot_id=None, billing_mode=None, reuse_resource=None, concurrency=None, client_nums=None, default_language=None, background_config=None, layer_config=None, review_config=None, chat_subtitle_config=None, chat_video_type=None, exit_mute_threshold=None):
        r"""CreateSmartChatRoomRequestBody

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
        """
        
        

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

    @property
    def room_name(self):
        r"""Gets the room_name of this CreateSmartChatRoomRequestBody.

        对话名称

        :return: The room_name of this CreateSmartChatRoomRequestBody.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        r"""Sets the room_name of this CreateSmartChatRoomRequestBody.

        对话名称

        :param room_name: The room_name of this CreateSmartChatRoomRequestBody.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_description(self):
        r"""Gets the room_description of this CreateSmartChatRoomRequestBody.

        对话描述。

        :return: The room_description of this CreateSmartChatRoomRequestBody.
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        r"""Sets the room_description of this CreateSmartChatRoomRequestBody.

        对话描述。

        :param room_description: The room_description of this CreateSmartChatRoomRequestBody.
        :type room_description: str
        """
        self._room_description = room_description

    @property
    def video_config(self):
        r"""Gets the video_config of this CreateSmartChatRoomRequestBody.

        :return: The video_config of this CreateSmartChatRoomRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        r"""Sets the video_config of this CreateSmartChatRoomRequestBody.

        :param video_config: The video_config of this CreateSmartChatRoomRequestBody.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def model_asset_id(self):
        r"""Gets the model_asset_id of this CreateSmartChatRoomRequestBody.

        数字人模型资产ID。

        :return: The model_asset_id of this CreateSmartChatRoomRequestBody.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        r"""Sets the model_asset_id of this CreateSmartChatRoomRequestBody.

        数字人模型资产ID。

        :param model_asset_id: The model_asset_id of this CreateSmartChatRoomRequestBody.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def voice_config(self):
        r"""Gets the voice_config of this CreateSmartChatRoomRequestBody.

        :return: The voice_config of this CreateSmartChatRoomRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        r"""Sets the voice_config of this CreateSmartChatRoomRequestBody.

        :param voice_config: The voice_config of this CreateSmartChatRoomRequestBody.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def voice_config_list(self):
        r"""Gets the voice_config_list of this CreateSmartChatRoomRequestBody.

        语音配置参数列表。

        :return: The voice_config_list of this CreateSmartChatRoomRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ChatVoiceConfig`]
        """
        return self._voice_config_list

    @voice_config_list.setter
    def voice_config_list(self, voice_config_list):
        r"""Sets the voice_config_list of this CreateSmartChatRoomRequestBody.

        语音配置参数列表。

        :param voice_config_list: The voice_config_list of this CreateSmartChatRoomRequestBody.
        :type voice_config_list: list[:class:`huaweicloudsdkmetastudio.v1.ChatVoiceConfig`]
        """
        self._voice_config_list = voice_config_list

    @property
    def robot_id(self):
        r"""Gets the robot_id of this CreateSmartChatRoomRequestBody.

        机器人ID。获取方法请参考[创建应用](CreateRobot.xml)。

        :return: The robot_id of this CreateSmartChatRoomRequestBody.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this CreateSmartChatRoomRequestBody.

        机器人ID。获取方法请参考[创建应用](CreateRobot.xml)。

        :param robot_id: The robot_id of this CreateSmartChatRoomRequestBody.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this CreateSmartChatRoomRequestBody.

        计费模式，默认值CONCURRENCY * CONCURRENCY：并发计费 * CLIENT：按接入端计费 * CLIENT_TOKENS: 按接入端计费（TOKENS）

        :return: The billing_mode of this CreateSmartChatRoomRequestBody.
        :rtype: str
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this CreateSmartChatRoomRequestBody.

        计费模式，默认值CONCURRENCY * CONCURRENCY：并发计费 * CLIENT：按接入端计费 * CLIENT_TOKENS: 按接入端计费（TOKENS）

        :param billing_mode: The billing_mode of this CreateSmartChatRoomRequestBody.
        :type billing_mode: str
        """
        self._billing_mode = billing_mode

    @property
    def reuse_resource(self):
        r"""Gets the reuse_resource of this CreateSmartChatRoomRequestBody.

        是否允许使用未分配的并发数（端模式下不能复用），默认不使用。

        :return: The reuse_resource of this CreateSmartChatRoomRequestBody.
        :rtype: bool
        """
        return self._reuse_resource

    @reuse_resource.setter
    def reuse_resource(self, reuse_resource):
        r"""Sets the reuse_resource of this CreateSmartChatRoomRequestBody.

        是否允许使用未分配的并发数（端模式下不能复用），默认不使用。

        :param reuse_resource: The reuse_resource of this CreateSmartChatRoomRequestBody.
        :type reuse_resource: bool
        """
        self._reuse_resource = reuse_resource

    @property
    def concurrency(self):
        r"""Gets the concurrency of this CreateSmartChatRoomRequestBody.

        **参数解释**： 并发路数。 **约束限制**： 默认没有并发路数，如果不配置并发数量，则无法启动智能交互对话任务。

        :return: The concurrency of this CreateSmartChatRoomRequestBody.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        r"""Sets the concurrency of this CreateSmartChatRoomRequestBody.

        **参数解释**： 并发路数。 **约束限制**： 默认没有并发路数，如果不配置并发数量，则无法启动智能交互对话任务。

        :param concurrency: The concurrency of this CreateSmartChatRoomRequestBody.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def client_nums(self):
        r"""Gets the client_nums of this CreateSmartChatRoomRequestBody.

        **参数解释**： 允许接入终端端数量。

        :return: The client_nums of this CreateSmartChatRoomRequestBody.
        :rtype: int
        """
        return self._client_nums

    @client_nums.setter
    def client_nums(self, client_nums):
        r"""Sets the client_nums of this CreateSmartChatRoomRequestBody.

        **参数解释**： 允许接入终端端数量。

        :param client_nums: The client_nums of this CreateSmartChatRoomRequestBody.
        :type client_nums: int
        """
        self._client_nums = client_nums

    @property
    def default_language(self):
        r"""Gets the default_language of this CreateSmartChatRoomRequestBody.

        默认语言，智能交互接口使用。默认值CN。 * CN：简体中文。 * EN：英语。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :return: The default_language of this CreateSmartChatRoomRequestBody.
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        r"""Sets the default_language of this CreateSmartChatRoomRequestBody.

        默认语言，智能交互接口使用。默认值CN。 * CN：简体中文。 * EN：英语。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :param default_language: The default_language of this CreateSmartChatRoomRequestBody.
        :type default_language: str
        """
        self._default_language = default_language

    @property
    def background_config(self):
        r"""Gets the background_config of this CreateSmartChatRoomRequestBody.

        :return: The background_config of this CreateSmartChatRoomRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`
        """
        return self._background_config

    @background_config.setter
    def background_config(self, background_config):
        r"""Sets the background_config of this CreateSmartChatRoomRequestBody.

        :param background_config: The background_config of this CreateSmartChatRoomRequestBody.
        :type background_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`
        """
        self._background_config = background_config

    @property
    def layer_config(self):
        r"""Gets the layer_config of this CreateSmartChatRoomRequestBody.

        图层配置。

        :return: The layer_config of this CreateSmartChatRoomRequestBody.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        return self._layer_config

    @layer_config.setter
    def layer_config(self, layer_config):
        r"""Sets the layer_config of this CreateSmartChatRoomRequestBody.

        图层配置。

        :param layer_config: The layer_config of this CreateSmartChatRoomRequestBody.
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        self._layer_config = layer_config

    @property
    def review_config(self):
        r"""Gets the review_config of this CreateSmartChatRoomRequestBody.

        :return: The review_config of this CreateSmartChatRoomRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        r"""Sets the review_config of this CreateSmartChatRoomRequestBody.

        :param review_config: The review_config of this CreateSmartChatRoomRequestBody.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def chat_subtitle_config(self):
        r"""Gets the chat_subtitle_config of this CreateSmartChatRoomRequestBody.

        :return: The chat_subtitle_config of this CreateSmartChatRoomRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        """
        return self._chat_subtitle_config

    @chat_subtitle_config.setter
    def chat_subtitle_config(self, chat_subtitle_config):
        r"""Sets the chat_subtitle_config of this CreateSmartChatRoomRequestBody.

        :param chat_subtitle_config: The chat_subtitle_config of this CreateSmartChatRoomRequestBody.
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        """
        self._chat_subtitle_config = chat_subtitle_config

    @property
    def chat_video_type(self):
        r"""Gets the chat_video_type of this CreateSmartChatRoomRequestBody.

        智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏

        :return: The chat_video_type of this CreateSmartChatRoomRequestBody.
        :rtype: str
        """
        return self._chat_video_type

    @chat_video_type.setter
    def chat_video_type(self, chat_video_type):
        r"""Sets the chat_video_type of this CreateSmartChatRoomRequestBody.

        智能交互对话端配置。 * COMPUTER: 电脑端 * MOBILE: 手机端 * HUB: 大屏

        :param chat_video_type: The chat_video_type of this CreateSmartChatRoomRequestBody.
        :type chat_video_type: str
        """
        self._chat_video_type = chat_video_type

    @property
    def exit_mute_threshold(self):
        r"""Gets the exit_mute_threshold of this CreateSmartChatRoomRequestBody.

        **参数解释**： 静默退出时长。

        :return: The exit_mute_threshold of this CreateSmartChatRoomRequestBody.
        :rtype: int
        """
        return self._exit_mute_threshold

    @exit_mute_threshold.setter
    def exit_mute_threshold(self, exit_mute_threshold):
        r"""Sets the exit_mute_threshold of this CreateSmartChatRoomRequestBody.

        **参数解释**： 静默退出时长。

        :param exit_mute_threshold: The exit_mute_threshold of this CreateSmartChatRoomRequestBody.
        :type exit_mute_threshold: int
        """
        self._exit_mute_threshold = exit_mute_threshold

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
        if not isinstance(other, CreateSmartChatRoomRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
