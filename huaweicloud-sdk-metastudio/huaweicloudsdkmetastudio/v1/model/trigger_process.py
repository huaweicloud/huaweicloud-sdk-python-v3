# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerProcess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_window': 'int',
        'reply_mode': 'str',
        'layer_config': 'SmartLayerConfig',
        'extra_layer_config': 'SmartLayerConfig',
        'reply_texts': 'list[str]',
        'reply_audios': 'list[ReplyAudioInfo]',
        'reply_order': 'str',
        'reply_role': 'str',
        'robot_id': 'str',
        'play_type': 'str'
    }

    attribute_map = {
        'time_window': 'time_window',
        'reply_mode': 'reply_mode',
        'layer_config': 'layer_config',
        'extra_layer_config': 'extra_layer_config',
        'reply_texts': 'reply_texts',
        'reply_audios': 'reply_audios',
        'reply_order': 'reply_order',
        'reply_role': 'reply_role',
        'robot_id': 'robot_id',
        'play_type': 'play_type'
    }

    def __init__(self, time_window=None, reply_mode=None, layer_config=None, extra_layer_config=None, reply_texts=None, reply_audios=None, reply_order=None, reply_role=None, robot_id=None, play_type=None):
        r"""TriggerProcess

        The model defined in huaweicloud sdk

        :param time_window: **参数解释**： 处理抑制时长。单位秒。 - -1：表示整场直播仅触发一次。 - 0：表示无抑制，每次都触发。 - 其他值n：表示n秒内仅触发一次。  **约束限制**： 不涉及 **默认取值**： 不涉及
        :type time_window: int
        :param reply_mode: **参数解释**： 回复类型。 **约束限制**： 不涉及 **取值范围**： * SYSTEM_REPLY：系统自动回复预先设置的话术。 * CALLBACK：回调给其他服务，携带设置的话术。 * SYSTEM_REPLY_AND_CALLBACK：系统自动回复预先设置的话术，同时回调给用户,携带设置的话术。 * SHOW_LAYER：仅显示叠加图层，不影响话术。 * INTELLIGENT_REPLY：使用配置的大模型生成回复话术。  **默认取值**： 不涉及
        :type reply_mode: str
        :param layer_config: 
        :type layer_config: :class:`huaweicloudsdkmetastudio.v1.SmartLayerConfig`
        :param extra_layer_config: 
        :type extra_layer_config: :class:`huaweicloudsdkmetastudio.v1.SmartLayerConfig`
        :param reply_texts: **参数解释**： 回复话术集。 **约束限制**： 不涉及 **取值范围**： 最大支持5条预置话术。 单条话术字符长度0-1024位。 **默认取值**： 不涉及
        :type reply_texts: list[str]
        :param reply_audios: **参数解释**： 回复音频集。填写audio_url。 **约束限制**： 不涉及 **取值范围**： 最大支持5条预置音频。 **默认取值**： 不涉及
        :type reply_audios: list[:class:`huaweicloudsdkmetastudio.v1.ReplyAudioInfo`]
        :param reply_order: **参数解释**： 回复话术选择次序。 **约束限制**： 不涉及 **取值范围**： * RANDOM：随机 * ORDER：顺序循环  **默认取值**： 不涉及
        :type reply_order: str
        :param reply_role: **参数解释**： 回复角色。 **约束限制**： 不涉及 **取值范围**： * STREAMER：主播 * CO_STREAMER：助播，仅声音。
        :type reply_role: str
        :param robot_id: **参数解释**： 机器人ID。 **约束限制**： reply_mode为INTELLIGENT_REPLY时必填，智能交互配置的大模型机器人ID。 获取方法请参考[创建应用](CreateRobot.xml)。 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及
        :type robot_id: str
        :param play_type: 回复播放类型。 - APPEND：追加，放置在场景播放队列尾部 - INSERT： 插入，在两个音频文件，或者文本句末添加。 - PLAY_NOW : 立即插入，收到指令后，立即播放，无需等待句末。
        :type play_type: str
        """
        
        

        self._time_window = None
        self._reply_mode = None
        self._layer_config = None
        self._extra_layer_config = None
        self._reply_texts = None
        self._reply_audios = None
        self._reply_order = None
        self._reply_role = None
        self._robot_id = None
        self._play_type = None
        self.discriminator = None

        if time_window is not None:
            self.time_window = time_window
        if reply_mode is not None:
            self.reply_mode = reply_mode
        if layer_config is not None:
            self.layer_config = layer_config
        if extra_layer_config is not None:
            self.extra_layer_config = extra_layer_config
        if reply_texts is not None:
            self.reply_texts = reply_texts
        if reply_audios is not None:
            self.reply_audios = reply_audios
        if reply_order is not None:
            self.reply_order = reply_order
        if reply_role is not None:
            self.reply_role = reply_role
        if robot_id is not None:
            self.robot_id = robot_id
        if play_type is not None:
            self.play_type = play_type

    @property
    def time_window(self):
        r"""Gets the time_window of this TriggerProcess.

        **参数解释**： 处理抑制时长。单位秒。 - -1：表示整场直播仅触发一次。 - 0：表示无抑制，每次都触发。 - 其他值n：表示n秒内仅触发一次。  **约束限制**： 不涉及 **默认取值**： 不涉及

        :return: The time_window of this TriggerProcess.
        :rtype: int
        """
        return self._time_window

    @time_window.setter
    def time_window(self, time_window):
        r"""Sets the time_window of this TriggerProcess.

        **参数解释**： 处理抑制时长。单位秒。 - -1：表示整场直播仅触发一次。 - 0：表示无抑制，每次都触发。 - 其他值n：表示n秒内仅触发一次。  **约束限制**： 不涉及 **默认取值**： 不涉及

        :param time_window: The time_window of this TriggerProcess.
        :type time_window: int
        """
        self._time_window = time_window

    @property
    def reply_mode(self):
        r"""Gets the reply_mode of this TriggerProcess.

        **参数解释**： 回复类型。 **约束限制**： 不涉及 **取值范围**： * SYSTEM_REPLY：系统自动回复预先设置的话术。 * CALLBACK：回调给其他服务，携带设置的话术。 * SYSTEM_REPLY_AND_CALLBACK：系统自动回复预先设置的话术，同时回调给用户,携带设置的话术。 * SHOW_LAYER：仅显示叠加图层，不影响话术。 * INTELLIGENT_REPLY：使用配置的大模型生成回复话术。  **默认取值**： 不涉及

        :return: The reply_mode of this TriggerProcess.
        :rtype: str
        """
        return self._reply_mode

    @reply_mode.setter
    def reply_mode(self, reply_mode):
        r"""Sets the reply_mode of this TriggerProcess.

        **参数解释**： 回复类型。 **约束限制**： 不涉及 **取值范围**： * SYSTEM_REPLY：系统自动回复预先设置的话术。 * CALLBACK：回调给其他服务，携带设置的话术。 * SYSTEM_REPLY_AND_CALLBACK：系统自动回复预先设置的话术，同时回调给用户,携带设置的话术。 * SHOW_LAYER：仅显示叠加图层，不影响话术。 * INTELLIGENT_REPLY：使用配置的大模型生成回复话术。  **默认取值**： 不涉及

        :param reply_mode: The reply_mode of this TriggerProcess.
        :type reply_mode: str
        """
        self._reply_mode = reply_mode

    @property
    def layer_config(self):
        r"""Gets the layer_config of this TriggerProcess.

        :return: The layer_config of this TriggerProcess.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SmartLayerConfig`
        """
        return self._layer_config

    @layer_config.setter
    def layer_config(self, layer_config):
        r"""Sets the layer_config of this TriggerProcess.

        :param layer_config: The layer_config of this TriggerProcess.
        :type layer_config: :class:`huaweicloudsdkmetastudio.v1.SmartLayerConfig`
        """
        self._layer_config = layer_config

    @property
    def extra_layer_config(self):
        r"""Gets the extra_layer_config of this TriggerProcess.

        :return: The extra_layer_config of this TriggerProcess.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SmartLayerConfig`
        """
        return self._extra_layer_config

    @extra_layer_config.setter
    def extra_layer_config(self, extra_layer_config):
        r"""Sets the extra_layer_config of this TriggerProcess.

        :param extra_layer_config: The extra_layer_config of this TriggerProcess.
        :type extra_layer_config: :class:`huaweicloudsdkmetastudio.v1.SmartLayerConfig`
        """
        self._extra_layer_config = extra_layer_config

    @property
    def reply_texts(self):
        r"""Gets the reply_texts of this TriggerProcess.

        **参数解释**： 回复话术集。 **约束限制**： 不涉及 **取值范围**： 最大支持5条预置话术。 单条话术字符长度0-1024位。 **默认取值**： 不涉及

        :return: The reply_texts of this TriggerProcess.
        :rtype: list[str]
        """
        return self._reply_texts

    @reply_texts.setter
    def reply_texts(self, reply_texts):
        r"""Sets the reply_texts of this TriggerProcess.

        **参数解释**： 回复话术集。 **约束限制**： 不涉及 **取值范围**： 最大支持5条预置话术。 单条话术字符长度0-1024位。 **默认取值**： 不涉及

        :param reply_texts: The reply_texts of this TriggerProcess.
        :type reply_texts: list[str]
        """
        self._reply_texts = reply_texts

    @property
    def reply_audios(self):
        r"""Gets the reply_audios of this TriggerProcess.

        **参数解释**： 回复音频集。填写audio_url。 **约束限制**： 不涉及 **取值范围**： 最大支持5条预置音频。 **默认取值**： 不涉及

        :return: The reply_audios of this TriggerProcess.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.ReplyAudioInfo`]
        """
        return self._reply_audios

    @reply_audios.setter
    def reply_audios(self, reply_audios):
        r"""Sets the reply_audios of this TriggerProcess.

        **参数解释**： 回复音频集。填写audio_url。 **约束限制**： 不涉及 **取值范围**： 最大支持5条预置音频。 **默认取值**： 不涉及

        :param reply_audios: The reply_audios of this TriggerProcess.
        :type reply_audios: list[:class:`huaweicloudsdkmetastudio.v1.ReplyAudioInfo`]
        """
        self._reply_audios = reply_audios

    @property
    def reply_order(self):
        r"""Gets the reply_order of this TriggerProcess.

        **参数解释**： 回复话术选择次序。 **约束限制**： 不涉及 **取值范围**： * RANDOM：随机 * ORDER：顺序循环  **默认取值**： 不涉及

        :return: The reply_order of this TriggerProcess.
        :rtype: str
        """
        return self._reply_order

    @reply_order.setter
    def reply_order(self, reply_order):
        r"""Sets the reply_order of this TriggerProcess.

        **参数解释**： 回复话术选择次序。 **约束限制**： 不涉及 **取值范围**： * RANDOM：随机 * ORDER：顺序循环  **默认取值**： 不涉及

        :param reply_order: The reply_order of this TriggerProcess.
        :type reply_order: str
        """
        self._reply_order = reply_order

    @property
    def reply_role(self):
        r"""Gets the reply_role of this TriggerProcess.

        **参数解释**： 回复角色。 **约束限制**： 不涉及 **取值范围**： * STREAMER：主播 * CO_STREAMER：助播，仅声音。

        :return: The reply_role of this TriggerProcess.
        :rtype: str
        """
        return self._reply_role

    @reply_role.setter
    def reply_role(self, reply_role):
        r"""Sets the reply_role of this TriggerProcess.

        **参数解释**： 回复角色。 **约束限制**： 不涉及 **取值范围**： * STREAMER：主播 * CO_STREAMER：助播，仅声音。

        :param reply_role: The reply_role of this TriggerProcess.
        :type reply_role: str
        """
        self._reply_role = reply_role

    @property
    def robot_id(self):
        r"""Gets the robot_id of this TriggerProcess.

        **参数解释**： 机器人ID。 **约束限制**： reply_mode为INTELLIGENT_REPLY时必填，智能交互配置的大模型机器人ID。 获取方法请参考[创建应用](CreateRobot.xml)。 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及

        :return: The robot_id of this TriggerProcess.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this TriggerProcess.

        **参数解释**： 机器人ID。 **约束限制**： reply_mode为INTELLIGENT_REPLY时必填，智能交互配置的大模型机器人ID。 获取方法请参考[创建应用](CreateRobot.xml)。 **取值范围**： 字符长度0-64位。 **默认取值**： 不涉及

        :param robot_id: The robot_id of this TriggerProcess.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def play_type(self):
        r"""Gets the play_type of this TriggerProcess.

        回复播放类型。 - APPEND：追加，放置在场景播放队列尾部 - INSERT： 插入，在两个音频文件，或者文本句末添加。 - PLAY_NOW : 立即插入，收到指令后，立即播放，无需等待句末。

        :return: The play_type of this TriggerProcess.
        :rtype: str
        """
        return self._play_type

    @play_type.setter
    def play_type(self, play_type):
        r"""Sets the play_type of this TriggerProcess.

        回复播放类型。 - APPEND：追加，放置在场景播放队列尾部 - INSERT： 插入，在两个音频文件，或者文本句末添加。 - PLAY_NOW : 立即插入，收到指令后，立即播放，无需等待句末。

        :param play_type: The play_type of this TriggerProcess.
        :type play_type: str
        """
        self._play_type = play_type

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
        if not isinstance(other, TriggerProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
