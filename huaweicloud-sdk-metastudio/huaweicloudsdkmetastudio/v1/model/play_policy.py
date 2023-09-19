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
        'play_mode': 'str'
    }

    attribute_map = {
        'repeat_count': 'repeat_count',
        'auto_play_script': 'auto_play_script',
        'play_mode': 'play_mode'
    }

    def __init__(self, repeat_count=None, auto_play_script=None, play_mode=None):
        """PlayPolicy

        The model defined in huaweicloud sdk

        :param repeat_count: 剧本重复播放次数。 -1表示持续重复，直至人工停止 0 表示不重复，仅执行一次 其他值n，实际运行次数为n+1次
        :type repeat_count: int
        :param auto_play_script: 是否自动播放剧本。 true: 服务完成任务初始化后，自动播放剧本 false: 服务完成任务初始化后，等待信号后再开始播放剧本
        :type auto_play_script: bool
        :param play_mode: 驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动
        :type play_mode: str
        """
        
        

        self._repeat_count = None
        self._auto_play_script = None
        self._play_mode = None
        self.discriminator = None

        if repeat_count is not None:
            self.repeat_count = repeat_count
        if auto_play_script is not None:
            self.auto_play_script = auto_play_script
        if play_mode is not None:
            self.play_mode = play_mode

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

        是否自动播放剧本。 true: 服务完成任务初始化后，自动播放剧本 false: 服务完成任务初始化后，等待信号后再开始播放剧本

        :return: The auto_play_script of this PlayPolicy.
        :rtype: bool
        """
        return self._auto_play_script

    @auto_play_script.setter
    def auto_play_script(self, auto_play_script):
        """Sets the auto_play_script of this PlayPolicy.

        是否自动播放剧本。 true: 服务完成任务初始化后，自动播放剧本 false: 服务完成任务初始化后，等待信号后再开始播放剧本

        :param auto_play_script: The auto_play_script of this PlayPolicy.
        :type auto_play_script: bool
        """
        self._auto_play_script = auto_play_script

    @property
    def play_mode(self):
        """Gets the play_mode of this PlayPolicy.

        驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :return: The play_mode of this PlayPolicy.
        :rtype: str
        """
        return self._play_mode

    @play_mode.setter
    def play_mode(self, play_mode):
        """Sets the play_mode of this PlayPolicy.

        驱动方式。默认TEXT * TEXT: 文本驱动，即通过TTS合成语音 * AUDIO: 语音驱动

        :param play_mode: The play_mode of this PlayPolicy.
        :type play_mode: str
        """
        self._play_mode = play_mode

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
