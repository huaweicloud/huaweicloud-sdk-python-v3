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
        'interaction_rules': 'list[InteractionRuleInfo]',
        'play_policy': 'PlayPolicy',
        'video_config': 'VideoConfig',
        'output_urls': 'list[str]',
        'room_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'cover_url': 'str',
        'x_request_id': 'str'
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
        'room_id': 'room_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'cover_url': 'cover_url',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, room_name=None, room_description=None, room_type=None, scene_scripts=None, interaction_rules=None, play_policy=None, video_config=None, output_urls=None, room_id=None, create_time=None, update_time=None, cover_url=None, x_request_id=None):
        """ShowSmartLiveRoomResponse

        The model defined in huaweicloud sdk

        :param room_name: 直播间名称
        :type room_name: str
        :param room_description: 直播间描述。
        :type room_description: str
        :param room_type: 直播间类型。 * NORMAL: 普通直播间，直播间一直存在，可以反复开播 * TEMP: 临时直播间,直播任务结束后自动清理直播间。
        :type room_type: str
        :param scene_scripts: 默认直播剧本列表。
        :type scene_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LiveVideoScriptInfo`]
        :param interaction_rules: 互动规则列表
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleInfo`]
        :param play_policy: 
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        :param video_config: 
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        :param output_urls: 视频推流第三方直播平台地址。
        :type output_urls: list[str]
        :param room_id: 直播间ID
        :type room_id: str
        :param create_time: 直播间创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 直播间更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param cover_url: 直播间封面图URL
        :type cover_url: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowSmartLiveRoomResponse, self).__init__()

        self._room_name = None
        self._room_description = None
        self._room_type = None
        self._scene_scripts = None
        self._interaction_rules = None
        self._play_policy = None
        self._video_config = None
        self._output_urls = None
        self._room_id = None
        self._create_time = None
        self._update_time = None
        self._cover_url = None
        self._x_request_id = None
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
        """Gets the room_name of this ShowSmartLiveRoomResponse.

        直播间名称

        :return: The room_name of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        """Sets the room_name of this ShowSmartLiveRoomResponse.

        直播间名称

        :param room_name: The room_name of this ShowSmartLiveRoomResponse.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_description(self):
        """Gets the room_description of this ShowSmartLiveRoomResponse.

        直播间描述。

        :return: The room_description of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        """Sets the room_description of this ShowSmartLiveRoomResponse.

        直播间描述。

        :param room_description: The room_description of this ShowSmartLiveRoomResponse.
        :type room_description: str
        """
        self._room_description = room_description

    @property
    def room_type(self):
        """Gets the room_type of this ShowSmartLiveRoomResponse.

        直播间类型。 * NORMAL: 普通直播间，直播间一直存在，可以反复开播 * TEMP: 临时直播间,直播任务结束后自动清理直播间。

        :return: The room_type of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._room_type

    @room_type.setter
    def room_type(self, room_type):
        """Sets the room_type of this ShowSmartLiveRoomResponse.

        直播间类型。 * NORMAL: 普通直播间，直播间一直存在，可以反复开播 * TEMP: 临时直播间,直播任务结束后自动清理直播间。

        :param room_type: The room_type of this ShowSmartLiveRoomResponse.
        :type room_type: str
        """
        self._room_type = room_type

    @property
    def scene_scripts(self):
        """Gets the scene_scripts of this ShowSmartLiveRoomResponse.

        默认直播剧本列表。

        :return: The scene_scripts of this ShowSmartLiveRoomResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveVideoScriptInfo`]
        """
        return self._scene_scripts

    @scene_scripts.setter
    def scene_scripts(self, scene_scripts):
        """Sets the scene_scripts of this ShowSmartLiveRoomResponse.

        默认直播剧本列表。

        :param scene_scripts: The scene_scripts of this ShowSmartLiveRoomResponse.
        :type scene_scripts: list[:class:`huaweicloudsdkmetastudio.v1.LiveVideoScriptInfo`]
        """
        self._scene_scripts = scene_scripts

    @property
    def interaction_rules(self):
        """Gets the interaction_rules of this ShowSmartLiveRoomResponse.

        互动规则列表

        :return: The interaction_rules of this ShowSmartLiveRoomResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleInfo`]
        """
        return self._interaction_rules

    @interaction_rules.setter
    def interaction_rules(self, interaction_rules):
        """Sets the interaction_rules of this ShowSmartLiveRoomResponse.

        互动规则列表

        :param interaction_rules: The interaction_rules of this ShowSmartLiveRoomResponse.
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleInfo`]
        """
        self._interaction_rules = interaction_rules

    @property
    def play_policy(self):
        """Gets the play_policy of this ShowSmartLiveRoomResponse.

        :return: The play_policy of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        return self._play_policy

    @play_policy.setter
    def play_policy(self, play_policy):
        """Sets the play_policy of this ShowSmartLiveRoomResponse.

        :param play_policy: The play_policy of this ShowSmartLiveRoomResponse.
        :type play_policy: :class:`huaweicloudsdkmetastudio.v1.PlayPolicy`
        """
        self._play_policy = play_policy

    @property
    def video_config(self):
        """Gets the video_config of this ShowSmartLiveRoomResponse.

        :return: The video_config of this ShowSmartLiveRoomResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        return self._video_config

    @video_config.setter
    def video_config(self, video_config):
        """Sets the video_config of this ShowSmartLiveRoomResponse.

        :param video_config: The video_config of this ShowSmartLiveRoomResponse.
        :type video_config: :class:`huaweicloudsdkmetastudio.v1.VideoConfig`
        """
        self._video_config = video_config

    @property
    def output_urls(self):
        """Gets the output_urls of this ShowSmartLiveRoomResponse.

        视频推流第三方直播平台地址。

        :return: The output_urls of this ShowSmartLiveRoomResponse.
        :rtype: list[str]
        """
        return self._output_urls

    @output_urls.setter
    def output_urls(self, output_urls):
        """Sets the output_urls of this ShowSmartLiveRoomResponse.

        视频推流第三方直播平台地址。

        :param output_urls: The output_urls of this ShowSmartLiveRoomResponse.
        :type output_urls: list[str]
        """
        self._output_urls = output_urls

    @property
    def room_id(self):
        """Gets the room_id of this ShowSmartLiveRoomResponse.

        直播间ID

        :return: The room_id of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this ShowSmartLiveRoomResponse.

        直播间ID

        :param room_id: The room_id of this ShowSmartLiveRoomResponse.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def create_time(self):
        """Gets the create_time of this ShowSmartLiveRoomResponse.

        直播间创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowSmartLiveRoomResponse.

        直播间创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowSmartLiveRoomResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowSmartLiveRoomResponse.

        直播间更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowSmartLiveRoomResponse.

        直播间更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowSmartLiveRoomResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def cover_url(self):
        """Gets the cover_url of this ShowSmartLiveRoomResponse.

        直播间封面图URL

        :return: The cover_url of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        """Sets the cover_url of this ShowSmartLiveRoomResponse.

        直播间封面图URL

        :param cover_url: The cover_url of this ShowSmartLiveRoomResponse.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowSmartLiveRoomResponse.

        :return: The x_request_id of this ShowSmartLiveRoomResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowSmartLiveRoomResponse.

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
