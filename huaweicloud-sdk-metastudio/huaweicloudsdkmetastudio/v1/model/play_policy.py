# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlayPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repeat_count': 'int',
        'auto_play_script': 'bool',
        'play_mode': 'str',
        'random_play_mode': 'str',
        'need_independent_capture_client': 'bool',
        'live_exit_config': 'LiveExitConfig',
        'is_rewrite_delay': 'bool'
    }

    attribute_map = {
        'repeat_count': 'repeat_count',
        'auto_play_script': 'auto_play_script',
        'play_mode': 'play_mode',
        'random_play_mode': 'random_play_mode',
        'need_independent_capture_client': 'need_independent_capture_client',
        'live_exit_config': 'live_exit_config',
        'is_rewrite_delay': 'is_rewrite_delay'
    }

    def __init__(self, repeat_count=None, auto_play_script=None, play_mode=None, random_play_mode=None, need_independent_capture_client=None, live_exit_config=None, is_rewrite_delay=None):
        r"""PlayPolicy

        The model defined in huaweicloud sdk

        :param repeat_count: **参数解释**： 剧本重复播放次数。 * -1：表示持续重复，直至人工停止。 * 0：表示不重复，仅执行一次。 * 其他值n：实际运行次数为n+1次。  **约束限制**： 不涉及。
        :type repeat_count: int
        :param auto_play_script: **参数解释**： 是否自动播放剧本。 **约束限制**： 不涉及。 **取值范围**： * true：服务完成任务初始化后，自动播放剧本。 * false：服务完成任务初始化后，等待信号后再开始播放剧本。
        :type auto_play_script: bool
        :param play_mode: **参数解释**： 驱动方式。 **约束限制**： 不涉及。 **取值范围**： * TEXT：文本驱动，即通过TTS合成语音。 * AUDIO：语音驱动。 * NO_PRESET：无预置剧本，人工控制模式。
        :type play_mode: str
        :param random_play_mode: **参数解释**： 随机播报模式。 **约束限制**： 从第二轮播报开始随机。 **取值范围**： * NONE：不启动随机播报。 * SCENE：按场景随机播报。场景内段落按顺序播报。 * SCRIPT_ITEM：按段落随机播报。场景按顺序播报。 * SCENE_AND_SCRIPT_ITEM：场景和段落都随机播报。
        :type random_play_mode: str
        :param need_independent_capture_client: **参数解释**： 是否需要独立采集端。用于客户端播放与命令分离场景。 **约束限制**： 不涉及。 **取值范围**： * true：分配CAPTURE、PLAYER两个RTC用户。 * false：仅分配PLAYER一个RTC用户。
        :type need_independent_capture_client: bool
        :param live_exit_config: 
        :type live_exit_config: :class:`huaweicloudsdkmetastudio.v1.LiveExitConfig`
        :param is_rewrite_delay: **参数解释**： 动态编辑未播放剧本是否需要下一轮生效。 **约束限制**： 不涉及。 **取值范围**： * true：下一轮生效。 * false：马上生效。 **默认取值**： false
        :type is_rewrite_delay: bool
        """
        
        

        self._repeat_count = None
        self._auto_play_script = None
        self._play_mode = None
        self._random_play_mode = None
        self._need_independent_capture_client = None
        self._live_exit_config = None
        self._is_rewrite_delay = None
        self.discriminator = None

        if repeat_count is not None:
            self.repeat_count = repeat_count
        if auto_play_script is not None:
            self.auto_play_script = auto_play_script
        if play_mode is not None:
            self.play_mode = play_mode
        if random_play_mode is not None:
            self.random_play_mode = random_play_mode
        if need_independent_capture_client is not None:
            self.need_independent_capture_client = need_independent_capture_client
        if live_exit_config is not None:
            self.live_exit_config = live_exit_config
        if is_rewrite_delay is not None:
            self.is_rewrite_delay = is_rewrite_delay

    @property
    def repeat_count(self):
        r"""Gets the repeat_count of this PlayPolicy.

        **参数解释**： 剧本重复播放次数。 * -1：表示持续重复，直至人工停止。 * 0：表示不重复，仅执行一次。 * 其他值n：实际运行次数为n+1次。  **约束限制**： 不涉及。

        :return: The repeat_count of this PlayPolicy.
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        r"""Sets the repeat_count of this PlayPolicy.

        **参数解释**： 剧本重复播放次数。 * -1：表示持续重复，直至人工停止。 * 0：表示不重复，仅执行一次。 * 其他值n：实际运行次数为n+1次。  **约束限制**： 不涉及。

        :param repeat_count: The repeat_count of this PlayPolicy.
        :type repeat_count: int
        """
        self._repeat_count = repeat_count

    @property
    def auto_play_script(self):
        r"""Gets the auto_play_script of this PlayPolicy.

        **参数解释**： 是否自动播放剧本。 **约束限制**： 不涉及。 **取值范围**： * true：服务完成任务初始化后，自动播放剧本。 * false：服务完成任务初始化后，等待信号后再开始播放剧本。

        :return: The auto_play_script of this PlayPolicy.
        :rtype: bool
        """
        return self._auto_play_script

    @auto_play_script.setter
    def auto_play_script(self, auto_play_script):
        r"""Sets the auto_play_script of this PlayPolicy.

        **参数解释**： 是否自动播放剧本。 **约束限制**： 不涉及。 **取值范围**： * true：服务完成任务初始化后，自动播放剧本。 * false：服务完成任务初始化后，等待信号后再开始播放剧本。

        :param auto_play_script: The auto_play_script of this PlayPolicy.
        :type auto_play_script: bool
        """
        self._auto_play_script = auto_play_script

    @property
    def play_mode(self):
        r"""Gets the play_mode of this PlayPolicy.

        **参数解释**： 驱动方式。 **约束限制**： 不涉及。 **取值范围**： * TEXT：文本驱动，即通过TTS合成语音。 * AUDIO：语音驱动。 * NO_PRESET：无预置剧本，人工控制模式。

        :return: The play_mode of this PlayPolicy.
        :rtype: str
        """
        return self._play_mode

    @play_mode.setter
    def play_mode(self, play_mode):
        r"""Sets the play_mode of this PlayPolicy.

        **参数解释**： 驱动方式。 **约束限制**： 不涉及。 **取值范围**： * TEXT：文本驱动，即通过TTS合成语音。 * AUDIO：语音驱动。 * NO_PRESET：无预置剧本，人工控制模式。

        :param play_mode: The play_mode of this PlayPolicy.
        :type play_mode: str
        """
        self._play_mode = play_mode

    @property
    def random_play_mode(self):
        r"""Gets the random_play_mode of this PlayPolicy.

        **参数解释**： 随机播报模式。 **约束限制**： 从第二轮播报开始随机。 **取值范围**： * NONE：不启动随机播报。 * SCENE：按场景随机播报。场景内段落按顺序播报。 * SCRIPT_ITEM：按段落随机播报。场景按顺序播报。 * SCENE_AND_SCRIPT_ITEM：场景和段落都随机播报。

        :return: The random_play_mode of this PlayPolicy.
        :rtype: str
        """
        return self._random_play_mode

    @random_play_mode.setter
    def random_play_mode(self, random_play_mode):
        r"""Sets the random_play_mode of this PlayPolicy.

        **参数解释**： 随机播报模式。 **约束限制**： 从第二轮播报开始随机。 **取值范围**： * NONE：不启动随机播报。 * SCENE：按场景随机播报。场景内段落按顺序播报。 * SCRIPT_ITEM：按段落随机播报。场景按顺序播报。 * SCENE_AND_SCRIPT_ITEM：场景和段落都随机播报。

        :param random_play_mode: The random_play_mode of this PlayPolicy.
        :type random_play_mode: str
        """
        self._random_play_mode = random_play_mode

    @property
    def need_independent_capture_client(self):
        r"""Gets the need_independent_capture_client of this PlayPolicy.

        **参数解释**： 是否需要独立采集端。用于客户端播放与命令分离场景。 **约束限制**： 不涉及。 **取值范围**： * true：分配CAPTURE、PLAYER两个RTC用户。 * false：仅分配PLAYER一个RTC用户。

        :return: The need_independent_capture_client of this PlayPolicy.
        :rtype: bool
        """
        return self._need_independent_capture_client

    @need_independent_capture_client.setter
    def need_independent_capture_client(self, need_independent_capture_client):
        r"""Sets the need_independent_capture_client of this PlayPolicy.

        **参数解释**： 是否需要独立采集端。用于客户端播放与命令分离场景。 **约束限制**： 不涉及。 **取值范围**： * true：分配CAPTURE、PLAYER两个RTC用户。 * false：仅分配PLAYER一个RTC用户。

        :param need_independent_capture_client: The need_independent_capture_client of this PlayPolicy.
        :type need_independent_capture_client: bool
        """
        self._need_independent_capture_client = need_independent_capture_client

    @property
    def live_exit_config(self):
        r"""Gets the live_exit_config of this PlayPolicy.

        :return: The live_exit_config of this PlayPolicy.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LiveExitConfig`
        """
        return self._live_exit_config

    @live_exit_config.setter
    def live_exit_config(self, live_exit_config):
        r"""Sets the live_exit_config of this PlayPolicy.

        :param live_exit_config: The live_exit_config of this PlayPolicy.
        :type live_exit_config: :class:`huaweicloudsdkmetastudio.v1.LiveExitConfig`
        """
        self._live_exit_config = live_exit_config

    @property
    def is_rewrite_delay(self):
        r"""Gets the is_rewrite_delay of this PlayPolicy.

        **参数解释**： 动态编辑未播放剧本是否需要下一轮生效。 **约束限制**： 不涉及。 **取值范围**： * true：下一轮生效。 * false：马上生效。 **默认取值**： false

        :return: The is_rewrite_delay of this PlayPolicy.
        :rtype: bool
        """
        return self._is_rewrite_delay

    @is_rewrite_delay.setter
    def is_rewrite_delay(self, is_rewrite_delay):
        r"""Sets the is_rewrite_delay of this PlayPolicy.

        **参数解释**： 动态编辑未播放剧本是否需要下一轮生效。 **约束限制**： 不涉及。 **取值范围**： * true：下一轮生效。 * false：马上生效。 **默认取值**： false

        :param is_rewrite_delay: The is_rewrite_delay of this PlayPolicy.
        :type is_rewrite_delay: bool
        """
        self._is_rewrite_delay = is_rewrite_delay

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
        if not isinstance(other, PlayPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
