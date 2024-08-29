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
        'need_independent_capture_client': 'bool'
    }

    attribute_map = {
        'repeat_count': 'repeat_count',
        'auto_play_script': 'auto_play_script',
        'play_mode': 'play_mode',
        'random_play_mode': 'random_play_mode',
        'need_independent_capture_client': 'need_independent_capture_client'
    }

    def __init__(self, repeat_count=None, auto_play_script=None, play_mode=None, random_play_mode=None, need_independent_capture_client=None):
        """PlayPolicy

        The model defined in huaweicloud sdk

        :param repeat_count: 剧本重复播放次数。 -1表示持续重复，直至人工停止 0 表示不重复，仅执行一次 其他值n，实际运行次数为n+1次
        :type repeat_count: int
        :param auto_play_script: 是否启动推理，自动播放剧本。 如果不启动推理，数字人为静默状态。 true: 服务完成任务初始化后，自动播放剧本 false: 服务完成任务初始化后，等待信号后再开始播放剧本
        :type auto_play_script: bool
        :param play_mode: 驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动 * NO_PRESET: 无预置剧本。人工控制模式。
        :type play_mode: str
        :param random_play_mode: 随机播报模式。 * NONE: 不启动随机播报。 * SCENE: 按场景随机播报。场景内段落按顺序播报。 * SCRIPT_ITEM：按段落随机播报。场景按顺序播报。 * SCENE_AND_SCRIPT_ITEM： 场景和段落都随机播报。
        :type random_play_mode: str
        :param need_independent_capture_client: 是否需要独立采集端
        :type need_independent_capture_client: bool
        """
        
        

        self._repeat_count = None
        self._auto_play_script = None
        self._play_mode = None
        self._random_play_mode = None
        self._need_independent_capture_client = None
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

    @property
    def repeat_count(self):
        """Gets the repeat_count of this PlayPolicy.

        剧本重复播放次数。 -1表示持续重复，直至人工停止 0 表示不重复，仅执行一次 其他值n，实际运行次数为n+1次

        :return: The repeat_count of this PlayPolicy.
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this PlayPolicy.

        剧本重复播放次数。 -1表示持续重复，直至人工停止 0 表示不重复，仅执行一次 其他值n，实际运行次数为n+1次

        :param repeat_count: The repeat_count of this PlayPolicy.
        :type repeat_count: int
        """
        self._repeat_count = repeat_count

    @property
    def auto_play_script(self):
        """Gets the auto_play_script of this PlayPolicy.

        是否启动推理，自动播放剧本。 如果不启动推理，数字人为静默状态。 true: 服务完成任务初始化后，自动播放剧本 false: 服务完成任务初始化后，等待信号后再开始播放剧本

        :return: The auto_play_script of this PlayPolicy.
        :rtype: bool
        """
        return self._auto_play_script

    @auto_play_script.setter
    def auto_play_script(self, auto_play_script):
        """Sets the auto_play_script of this PlayPolicy.

        是否启动推理，自动播放剧本。 如果不启动推理，数字人为静默状态。 true: 服务完成任务初始化后，自动播放剧本 false: 服务完成任务初始化后，等待信号后再开始播放剧本

        :param auto_play_script: The auto_play_script of this PlayPolicy.
        :type auto_play_script: bool
        """
        self._auto_play_script = auto_play_script

    @property
    def play_mode(self):
        """Gets the play_mode of this PlayPolicy.

        驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动 * NO_PRESET: 无预置剧本。人工控制模式。

        :return: The play_mode of this PlayPolicy.
        :rtype: str
        """
        return self._play_mode

    @play_mode.setter
    def play_mode(self, play_mode):
        """Sets the play_mode of this PlayPolicy.

        驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动 * NO_PRESET: 无预置剧本。人工控制模式。

        :param play_mode: The play_mode of this PlayPolicy.
        :type play_mode: str
        """
        self._play_mode = play_mode

    @property
    def random_play_mode(self):
        """Gets the random_play_mode of this PlayPolicy.

        随机播报模式。 * NONE: 不启动随机播报。 * SCENE: 按场景随机播报。场景内段落按顺序播报。 * SCRIPT_ITEM：按段落随机播报。场景按顺序播报。 * SCENE_AND_SCRIPT_ITEM： 场景和段落都随机播报。

        :return: The random_play_mode of this PlayPolicy.
        :rtype: str
        """
        return self._random_play_mode

    @random_play_mode.setter
    def random_play_mode(self, random_play_mode):
        """Sets the random_play_mode of this PlayPolicy.

        随机播报模式。 * NONE: 不启动随机播报。 * SCENE: 按场景随机播报。场景内段落按顺序播报。 * SCRIPT_ITEM：按段落随机播报。场景按顺序播报。 * SCENE_AND_SCRIPT_ITEM： 场景和段落都随机播报。

        :param random_play_mode: The random_play_mode of this PlayPolicy.
        :type random_play_mode: str
        """
        self._random_play_mode = random_play_mode

    @property
    def need_independent_capture_client(self):
        """Gets the need_independent_capture_client of this PlayPolicy.

        是否需要独立采集端

        :return: The need_independent_capture_client of this PlayPolicy.
        :rtype: bool
        """
        return self._need_independent_capture_client

    @need_independent_capture_client.setter
    def need_independent_capture_client(self, need_independent_capture_client):
        """Sets the need_independent_capture_client of this PlayPolicy.

        是否需要独立采集端

        :param need_independent_capture_client: The need_independent_capture_client of this PlayPolicy.
        :type need_independent_capture_client: bool
        """
        self._need_independent_capture_client = need_independent_capture_client

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
