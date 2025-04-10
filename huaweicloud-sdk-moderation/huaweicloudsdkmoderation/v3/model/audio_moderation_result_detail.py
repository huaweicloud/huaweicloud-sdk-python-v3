# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioModerationResultDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'float',
        'suggestion': 'str',
        'end_time': 'float',
        'label': 'str',
        'audio_text': 'str',
        'segments': 'list[VideoModerationDetailSegment]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'suggestion': 'suggestion',
        'end_time': 'end_time',
        'label': 'label',
        'audio_text': 'audio_text',
        'segments': 'segments'
    }

    def __init__(self, start_time=None, suggestion=None, end_time=None, label=None, audio_text=None, segments=None):
        r"""AudioModerationResultDetail

        The model defined in huaweicloud sdk

        :param start_time: 音频片段开始时间
        :type start_time: float
        :param suggestion: 音频片段审核处理建议： block：包含敏感信息，不通过 review：需要人工复检
        :type suggestion: str
        :param end_time: 音频片段结束时间
        :type end_time: float
        :param label: 音频片段标签
        :type label: str
        :param audio_text: 音频片段文本内容
        :type audio_text: str
        :param segments: 命中的风险片段信息列表，如果命中语义算法模型，则该字段不会存在
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationDetailSegment`]
        """
        
        

        self._start_time = None
        self._suggestion = None
        self._end_time = None
        self._label = None
        self._audio_text = None
        self._segments = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if suggestion is not None:
            self.suggestion = suggestion
        if end_time is not None:
            self.end_time = end_time
        if label is not None:
            self.label = label
        if audio_text is not None:
            self.audio_text = audio_text
        if segments is not None:
            self.segments = segments

    @property
    def start_time(self):
        r"""Gets the start_time of this AudioModerationResultDetail.

        音频片段开始时间

        :return: The start_time of this AudioModerationResultDetail.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this AudioModerationResultDetail.

        音频片段开始时间

        :param start_time: The start_time of this AudioModerationResultDetail.
        :type start_time: float
        """
        self._start_time = start_time

    @property
    def suggestion(self):
        r"""Gets the suggestion of this AudioModerationResultDetail.

        音频片段审核处理建议： block：包含敏感信息，不通过 review：需要人工复检

        :return: The suggestion of this AudioModerationResultDetail.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this AudioModerationResultDetail.

        音频片段审核处理建议： block：包含敏感信息，不通过 review：需要人工复检

        :param suggestion: The suggestion of this AudioModerationResultDetail.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def end_time(self):
        r"""Gets the end_time of this AudioModerationResultDetail.

        音频片段结束时间

        :return: The end_time of this AudioModerationResultDetail.
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this AudioModerationResultDetail.

        音频片段结束时间

        :param end_time: The end_time of this AudioModerationResultDetail.
        :type end_time: float
        """
        self._end_time = end_time

    @property
    def label(self):
        r"""Gets the label of this AudioModerationResultDetail.

        音频片段标签

        :return: The label of this AudioModerationResultDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this AudioModerationResultDetail.

        音频片段标签

        :param label: The label of this AudioModerationResultDetail.
        :type label: str
        """
        self._label = label

    @property
    def audio_text(self):
        r"""Gets the audio_text of this AudioModerationResultDetail.

        音频片段文本内容

        :return: The audio_text of this AudioModerationResultDetail.
        :rtype: str
        """
        return self._audio_text

    @audio_text.setter
    def audio_text(self, audio_text):
        r"""Sets the audio_text of this AudioModerationResultDetail.

        音频片段文本内容

        :param audio_text: The audio_text of this AudioModerationResultDetail.
        :type audio_text: str
        """
        self._audio_text = audio_text

    @property
    def segments(self):
        r"""Gets the segments of this AudioModerationResultDetail.

        命中的风险片段信息列表，如果命中语义算法模型，则该字段不会存在

        :return: The segments of this AudioModerationResultDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationDetailSegment`]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        r"""Sets the segments of this AudioModerationResultDetail.

        命中的风险片段信息列表，如果命中语义算法模型，则该字段不会存在

        :param segments: The segments of this AudioModerationResultDetail.
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationDetailSegment`]
        """
        self._segments = segments

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
        if not isinstance(other, AudioModerationResultDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
