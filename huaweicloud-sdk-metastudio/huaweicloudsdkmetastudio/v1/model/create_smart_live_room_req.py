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
        'interaction_rules': 'list[InteractionRuleInfo]',
        'play_policy': 'PlayPolicy',
        'video_config': 'VideoConfig',
        'output_urls': 'list[str]'
    }

    attribute_map = {
        'room_name': 'room_name',
        'room_description': 'room_description',
        'room_type': 'room_type',
        'scene_scripts': 'scene_scripts',
        'interaction_rules': 'interaction_rules',
        'play_policy': 'play_policy',
        'video_config': 'video_config',
        'output_urls': 'output_urls'
    }

    def __init__(self, room_name=None, room_description=None, room_type=None, scene_scripts=None, interaction_rules=None, play_policy=None, video_config=None, output_urls=None):
        """CreateSmartLiveRoomReq

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
        """
        
        

        self._room_name = None
        self._room_description = None
        self._room_type = None
        self._scene_scripts = None
        self._interaction_rules = None
        self._play_policy = None
        self._video_config = None
        self._output_urls = None
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

        直播间类型。 * NORMAL: 普通直播间，直播间一直存在，可以反复开播 * TEMP: 临时直播间,直播任务结束后自动清理直播间。

        :return: The room_type of this CreateSmartLiveRoomReq.
        :rtype: str
        """
        return self._room_type

    @room_type.setter
    def room_type(self, room_type):
        """Sets the room_type of this CreateSmartLiveRoomReq.

        直播间类型。 * NORMAL: 普通直播间，直播间一直存在，可以反复开播 * TEMP: 临时直播间,直播任务结束后自动清理直播间。

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
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleInfo`]
        """
        return self._interaction_rules

    @interaction_rules.setter
    def interaction_rules(self, interaction_rules):
        """Sets the interaction_rules of this CreateSmartLiveRoomReq.

        互动规则列表

        :param interaction_rules: The interaction_rules of this CreateSmartLiveRoomReq.
        :type interaction_rules: list[:class:`huaweicloudsdkmetastudio.v1.InteractionRuleInfo`]
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

        视频推流第三方直播平台地址。

        :return: The output_urls of this CreateSmartLiveRoomReq.
        :rtype: list[str]
        """
        return self._output_urls

    @output_urls.setter
    def output_urls(self, output_urls):
        """Sets the output_urls of this CreateSmartLiveRoomReq.

        视频推流第三方直播平台地址。

        :param output_urls: The output_urls of this CreateSmartLiveRoomReq.
        :type output_urls: list[str]
        """
        self._output_urls = output_urls

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
