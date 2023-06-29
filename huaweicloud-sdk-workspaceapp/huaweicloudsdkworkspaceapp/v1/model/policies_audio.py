# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesAudio:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_redirection_enable': 'bool',
        'play_redirection_enable': 'bool',
        'play_classification': 'str',
        'record_redirection_enable': 'bool',
        'record_classification': 'str'
    }

    attribute_map = {
        'audio_redirection_enable': 'audio_redirection_enable',
        'play_redirection_enable': 'play_redirection_enable',
        'play_classification': 'play_classification',
        'record_redirection_enable': 'record_redirection_enable',
        'record_classification': 'record_classification'
    }

    def __init__(self, audio_redirection_enable=None, play_redirection_enable=None, play_classification=None, record_redirection_enable=None, record_classification=None):
        """PoliciesAudio

        The model defined in huaweicloud sdk

        :param audio_redirection_enable: 是否开启音频重定向。取值为： false：表示关闭。 true：表示开启。
        :type audio_redirection_enable: bool
        :param play_redirection_enable: 是否开启播音重定向。取值为： false：表示关闭。 true：表示开启。
        :type play_redirection_enable: bool
        :param play_classification: 播音场景。取值为： 无损播音：LossLess。 语音通话：Speech Call。 音乐播音：Music Play。 自动识别：Automatic Identification。
        :type play_classification: str
        :param record_redirection_enable: 是否开启录音重定向。取值为： false：表示关闭。 true：表示开启。
        :type record_redirection_enable: bool
        :param record_classification: 录音场景。取值为： 无损录音：LossLess。 语音通话：Speech Call。 音乐录音：Music Record。 自动识别：Automatic Identification。
        :type record_classification: str
        """
        
        

        self._audio_redirection_enable = None
        self._play_redirection_enable = None
        self._play_classification = None
        self._record_redirection_enable = None
        self._record_classification = None
        self.discriminator = None

        if audio_redirection_enable is not None:
            self.audio_redirection_enable = audio_redirection_enable
        if play_redirection_enable is not None:
            self.play_redirection_enable = play_redirection_enable
        if play_classification is not None:
            self.play_classification = play_classification
        if record_redirection_enable is not None:
            self.record_redirection_enable = record_redirection_enable
        if record_classification is not None:
            self.record_classification = record_classification

    @property
    def audio_redirection_enable(self):
        """Gets the audio_redirection_enable of this PoliciesAudio.

        是否开启音频重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The audio_redirection_enable of this PoliciesAudio.
        :rtype: bool
        """
        return self._audio_redirection_enable

    @audio_redirection_enable.setter
    def audio_redirection_enable(self, audio_redirection_enable):
        """Sets the audio_redirection_enable of this PoliciesAudio.

        是否开启音频重定向。取值为： false：表示关闭。 true：表示开启。

        :param audio_redirection_enable: The audio_redirection_enable of this PoliciesAudio.
        :type audio_redirection_enable: bool
        """
        self._audio_redirection_enable = audio_redirection_enable

    @property
    def play_redirection_enable(self):
        """Gets the play_redirection_enable of this PoliciesAudio.

        是否开启播音重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The play_redirection_enable of this PoliciesAudio.
        :rtype: bool
        """
        return self._play_redirection_enable

    @play_redirection_enable.setter
    def play_redirection_enable(self, play_redirection_enable):
        """Sets the play_redirection_enable of this PoliciesAudio.

        是否开启播音重定向。取值为： false：表示关闭。 true：表示开启。

        :param play_redirection_enable: The play_redirection_enable of this PoliciesAudio.
        :type play_redirection_enable: bool
        """
        self._play_redirection_enable = play_redirection_enable

    @property
    def play_classification(self):
        """Gets the play_classification of this PoliciesAudio.

        播音场景。取值为： 无损播音：LossLess。 语音通话：Speech Call。 音乐播音：Music Play。 自动识别：Automatic Identification。

        :return: The play_classification of this PoliciesAudio.
        :rtype: str
        """
        return self._play_classification

    @play_classification.setter
    def play_classification(self, play_classification):
        """Sets the play_classification of this PoliciesAudio.

        播音场景。取值为： 无损播音：LossLess。 语音通话：Speech Call。 音乐播音：Music Play。 自动识别：Automatic Identification。

        :param play_classification: The play_classification of this PoliciesAudio.
        :type play_classification: str
        """
        self._play_classification = play_classification

    @property
    def record_redirection_enable(self):
        """Gets the record_redirection_enable of this PoliciesAudio.

        是否开启录音重定向。取值为： false：表示关闭。 true：表示开启。

        :return: The record_redirection_enable of this PoliciesAudio.
        :rtype: bool
        """
        return self._record_redirection_enable

    @record_redirection_enable.setter
    def record_redirection_enable(self, record_redirection_enable):
        """Sets the record_redirection_enable of this PoliciesAudio.

        是否开启录音重定向。取值为： false：表示关闭。 true：表示开启。

        :param record_redirection_enable: The record_redirection_enable of this PoliciesAudio.
        :type record_redirection_enable: bool
        """
        self._record_redirection_enable = record_redirection_enable

    @property
    def record_classification(self):
        """Gets the record_classification of this PoliciesAudio.

        录音场景。取值为： 无损录音：LossLess。 语音通话：Speech Call。 音乐录音：Music Record。 自动识别：Automatic Identification。

        :return: The record_classification of this PoliciesAudio.
        :rtype: str
        """
        return self._record_classification

    @record_classification.setter
    def record_classification(self, record_classification):
        """Sets the record_classification of this PoliciesAudio.

        录音场景。取值为： 无损录音：LossLess。 语音通话：Speech Call。 音乐录音：Music Record。 自动识别：Automatic Identification。

        :param record_classification: The record_classification of this PoliciesAudio.
        :type record_classification: str
        """
        self._record_classification = record_classification

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
        if not isinstance(other, PoliciesAudio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
