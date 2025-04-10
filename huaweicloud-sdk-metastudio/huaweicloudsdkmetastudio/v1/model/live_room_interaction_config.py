# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveRoomInteractionConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'play_type': 'str',
        'ignore_current_sentence': 'bool'
    }

    attribute_map = {
        'play_type': 'play_type',
        'ignore_current_sentence': 'ignore_current_sentence'
    }

    def __init__(self, play_type=None, ignore_current_sentence=None):
        r"""LiveRoomInteractionConfig

        The model defined in huaweicloud sdk

        :param play_type: 播放类型。 - APPEND：追加，放置在场景播放队列尾部 - INSERT： 插入，在两个音频文件，或者文本句末添加。 - PLAY_NOW : 立即插入，收到指令后，立即播放，无需等待句末。
        :type play_type: str
        :param ignore_current_sentence: 忽略互动回复中断句子后半句不再播放。用于立即中断场景。默认不忽略。
        :type ignore_current_sentence: bool
        """
        
        

        self._play_type = None
        self._ignore_current_sentence = None
        self.discriminator = None

        if play_type is not None:
            self.play_type = play_type
        if ignore_current_sentence is not None:
            self.ignore_current_sentence = ignore_current_sentence

    @property
    def play_type(self):
        r"""Gets the play_type of this LiveRoomInteractionConfig.

        播放类型。 - APPEND：追加，放置在场景播放队列尾部 - INSERT： 插入，在两个音频文件，或者文本句末添加。 - PLAY_NOW : 立即插入，收到指令后，立即播放，无需等待句末。

        :return: The play_type of this LiveRoomInteractionConfig.
        :rtype: str
        """
        return self._play_type

    @play_type.setter
    def play_type(self, play_type):
        r"""Sets the play_type of this LiveRoomInteractionConfig.

        播放类型。 - APPEND：追加，放置在场景播放队列尾部 - INSERT： 插入，在两个音频文件，或者文本句末添加。 - PLAY_NOW : 立即插入，收到指令后，立即播放，无需等待句末。

        :param play_type: The play_type of this LiveRoomInteractionConfig.
        :type play_type: str
        """
        self._play_type = play_type

    @property
    def ignore_current_sentence(self):
        r"""Gets the ignore_current_sentence of this LiveRoomInteractionConfig.

        忽略互动回复中断句子后半句不再播放。用于立即中断场景。默认不忽略。

        :return: The ignore_current_sentence of this LiveRoomInteractionConfig.
        :rtype: bool
        """
        return self._ignore_current_sentence

    @ignore_current_sentence.setter
    def ignore_current_sentence(self, ignore_current_sentence):
        r"""Sets the ignore_current_sentence of this LiveRoomInteractionConfig.

        忽略互动回复中断句子后半句不再播放。用于立即中断场景。默认不忽略。

        :param ignore_current_sentence: The ignore_current_sentence of this LiveRoomInteractionConfig.
        :type ignore_current_sentence: bool
        """
        self._ignore_current_sentence = ignore_current_sentence

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
        if not isinstance(other, LiveRoomInteractionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
