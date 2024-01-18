# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSmartChatRoomResponse(SdkResponse):

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
        'robot_id': 'str',
        'concurrency': 'int',
        'background_config': 'BackgroundConfigInfo',
        'layer_config': 'list[LayerConfig]',
        'review_config': 'ReviewConfig',
        'chat_subtitle_config': 'ChatSubtitleConfig',
        'room_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'cover_url': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'room_name': 'room_name',
        'room_description': 'room_description',
        'video_config': 'video_config',
        'model_asset_id': 'model_asset_id',
        'voice_config': 'voice_config',
        'robot_id': 'robot_id',
        'concurrency': 'concurrency',
        'background_config': 'background_config',
        'layer_config': 'layer_config',
        'review_config': 'review_config',
        'chat_subtitle_config': 'chat_subtitle_config',
        'room_id': 'room_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'cover_url': 'cover_url',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, room_name=None, room_description=None, video_config=None, model_asset_id=None, voice_config=None, robot_id=None, concurrency=None, background_config=None, layer_config=None, review_config=None, chat_subtitle_config=None, room_id=None, create_time=None, update_time=None, cover_url=None, x_request_id=None):
        """UpdateSmartChatRoomResponse

        The model defined in huaweicloud sdk

        :param room_name: 直播间名称
        :type room_name: str
        :param room_description: 直播间描述。
        :type room_description: str
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param model_asset_id: 数字人模型资产ID。
        :type model_asset_id: str
        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param robot_id: 机器人ID。
        :type robot_id: str
        :param concurrency: 并发路数。
        :type concurrency: int
        :param background_config: 
        :type background_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`
        :param layer_config: 图层配置。
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        :param chat_subtitle_config: 
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        :param room_id: 直播间ID
        :type room_id: str
        :param create_time: 智能交互对话直播间创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 智能交互对话直播间更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param cover_url: 直播间封面图URL
        :type cover_url: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(UpdateSmartChatRoomResponse, self).__init__()

        self._room_name = None
        self._room_description = None
        self._video_config = None
        self._model_asset_id = None
        self._voice_config = None
        self._robot_id = None
        self._concurrency = None
        self._background_config = None
        self._layer_config = None
        self._review_config = None
        self._chat_subtitle_config = None
        self._room_id = None
        self._create_time = None
        self._update_time = None
        self._cover_url = None
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
        self.robot_id = robot_id
        if concurrency is not None:
            self.concurrency = concurrency
        if background_config is not None:
            self.background_config = background_config
        if layer_config is not None:
            self.layer_config = layer_config
        if review_config is not None:
            self.review_config = review_config
        if chat_subtitle_config is not None:
            self.chat_subtitle_config = chat_subtitle_config
        if room_id is not None:
            self.room_id = room_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if cover_url is not None:
            self.cover_url = cover_url
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def room_name(self):
        """Gets the room_name of this UpdateSmartChatRoomResponse.

        直播间名称

        :return: The room_name of this UpdateSmartChatRoomResponse.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        """Sets the room_name of this UpdateSmartChatRoomResponse.

        直播间名称

        :param room_name: The room_name of this UpdateSmartChatRoomResponse.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_description(self):
        """Gets the room_description of this UpdateSmartChatRoomResponse.

        直播间描述。

        :return: The room_description of this UpdateSmartChatRoomResponse.
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        """Sets the room_description of this UpdateSmartChatRoomResponse.

        直播间描述。

        :param room_description: The room_description of this UpdateSmartChatRoomResponse.
        :type room_description: str
        """
        self._room_description = room_description

    @property
    def video_config(self):
        """Gets the video_config of this UpdateSmartChatRoomResponse.

        :return: The video_config of this UpdateSmartChatRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this UpdateSmartChatRoomResponse.

        :param video_config: The video_config of this UpdateSmartChatRoomResponse.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def model_asset_id(self):
        """Gets the model_asset_id of this UpdateSmartChatRoomResponse.

        数字人模型资产ID。

        :return: The model_asset_id of this UpdateSmartChatRoomResponse.
        :rtype: str
        """
        return self._model_asset_id

    @model_asset_id.setter
    def model_asset_id(self, model_asset_id):
        """Sets the model_asset_id of this UpdateSmartChatRoomResponse.

        数字人模型资产ID。

        :param model_asset_id: The model_asset_id of this UpdateSmartChatRoomResponse.
        :type model_asset_id: str
        """
        self._model_asset_id = model_asset_id

    @property
    def voice_config(self):
        """Gets the voice_config of this UpdateSmartChatRoomResponse.

        :return: The voice_config of this UpdateSmartChatRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        """Sets the voice_config of this UpdateSmartChatRoomResponse.

        :param voice_config: The voice_config of this UpdateSmartChatRoomResponse.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def robot_id(self):
        """Gets the robot_id of this UpdateSmartChatRoomResponse.

        机器人ID。

        :return: The robot_id of this UpdateSmartChatRoomResponse.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this UpdateSmartChatRoomResponse.

        机器人ID。

        :param robot_id: The robot_id of this UpdateSmartChatRoomResponse.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def concurrency(self):
        """Gets the concurrency of this UpdateSmartChatRoomResponse.

        并发路数。

        :return: The concurrency of this UpdateSmartChatRoomResponse.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this UpdateSmartChatRoomResponse.

        并发路数。

        :param concurrency: The concurrency of this UpdateSmartChatRoomResponse.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def background_config(self):
        """Gets the background_config of this UpdateSmartChatRoomResponse.

        :return: The background_config of this UpdateSmartChatRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`
        """
        return self._background_config

    @background_config.setter
    def background_config(self, background_config):
        """Sets the background_config of this UpdateSmartChatRoomResponse.

        :param background_config: The background_config of this UpdateSmartChatRoomResponse.
        :type background_config: :class:`huaweicloudsdkmetastudio.v1.BackgroundConfigInfo`
        """
        self._background_config = background_config

    @property
    def layer_config(self):
        """Gets the layer_config of this UpdateSmartChatRoomResponse.

        图层配置。

        :return: The layer_config of this UpdateSmartChatRoomResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        return self._layer_config

    @layer_config.setter
    def layer_config(self, layer_config):
        """Sets the layer_config of this UpdateSmartChatRoomResponse.

        图层配置。

        :param layer_config: The layer_config of this UpdateSmartChatRoomResponse.
        :type layer_config: list[:class:`huaweicloudsdkmetastudio.v1.LayerConfig`]
        """
        self._layer_config = layer_config

    @property
    def review_config(self):
        """Gets the review_config of this UpdateSmartChatRoomResponse.

        :return: The review_config of this UpdateSmartChatRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        """Sets the review_config of this UpdateSmartChatRoomResponse.

        :param review_config: The review_config of this UpdateSmartChatRoomResponse.
        :type review_config: :class:`huaweicloudsdkmetastudio.v1.ReviewConfig`
        """
        self._review_config = review_config

    @property
    def chat_subtitle_config(self):
        """Gets the chat_subtitle_config of this UpdateSmartChatRoomResponse.

        :return: The chat_subtitle_config of this UpdateSmartChatRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        """
        return self._chat_subtitle_config

    @chat_subtitle_config.setter
    def chat_subtitle_config(self, chat_subtitle_config):
        """Sets the chat_subtitle_config of this UpdateSmartChatRoomResponse.

        :param chat_subtitle_config: The chat_subtitle_config of this UpdateSmartChatRoomResponse.
        :type chat_subtitle_config: :class:`huaweicloudsdkmetastudio.v1.ChatSubtitleConfig`
        """
        self._chat_subtitle_config = chat_subtitle_config

    @property
    def room_id(self):
        """Gets the room_id of this UpdateSmartChatRoomResponse.

        直播间ID

        :return: The room_id of this UpdateSmartChatRoomResponse.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this UpdateSmartChatRoomResponse.

        直播间ID

        :param room_id: The room_id of this UpdateSmartChatRoomResponse.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def create_time(self):
        """Gets the create_time of this UpdateSmartChatRoomResponse.

        智能交互对话直播间创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this UpdateSmartChatRoomResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateSmartChatRoomResponse.

        智能交互对话直播间创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this UpdateSmartChatRoomResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this UpdateSmartChatRoomResponse.

        智能交互对话直播间更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this UpdateSmartChatRoomResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UpdateSmartChatRoomResponse.

        智能交互对话直播间更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this UpdateSmartChatRoomResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def cover_url(self):
        """Gets the cover_url of this UpdateSmartChatRoomResponse.

        直播间封面图URL

        :return: The cover_url of this UpdateSmartChatRoomResponse.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        """Sets the cover_url of this UpdateSmartChatRoomResponse.

        直播间封面图URL

        :param cover_url: The cover_url of this UpdateSmartChatRoomResponse.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateSmartChatRoomResponse.

        :return: The x_request_id of this UpdateSmartChatRoomResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateSmartChatRoomResponse.

        :param x_request_id: The x_request_id of this UpdateSmartChatRoomResponse.
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
        if not isinstance(other, UpdateSmartChatRoomResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
