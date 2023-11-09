# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentAudioDetail:

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
        'end_time': 'float',
        'suggestion': 'str',
        'audio_text': 'str',
        'label': 'str',
        'segments': 'list[DocumentVideoImageDetailSegments]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'suggestion': 'suggestion',
        'audio_text': 'audio_text',
        'label': 'label',
        'segments': 'segments'
    }

    def __init__(self, start_time=None, end_time=None, suggestion=None, audio_text=None, label=None, segments=None):
        """DocumentAudioDetail

        The model defined in huaweicloud sdk

        :param start_time: 音频片段开始时间
        :type start_time: float
        :param end_time: 音频片段结束时间
        :type end_time: float
        :param suggestion: 音频片段审核处理建议： block：包含敏感信息，不通过 review：需要人工复检
        :type suggestion: str
        :param audio_text: 音频片段文本内容
        :type audio_text: str
        :param label: 音频片段标签
        :type label: str
        :param segments: 命中的风险片段信息列表
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.DocumentVideoImageDetailSegments`]
        """
        
        

        self._start_time = None
        self._end_time = None
        self._suggestion = None
        self._audio_text = None
        self._label = None
        self._segments = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if suggestion is not None:
            self.suggestion = suggestion
        if audio_text is not None:
            self.audio_text = audio_text
        if label is not None:
            self.label = label
        if segments is not None:
            self.segments = segments

    @property
    def start_time(self):
        """Gets the start_time of this DocumentAudioDetail.

        音频片段开始时间

        :return: The start_time of this DocumentAudioDetail.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DocumentAudioDetail.

        音频片段开始时间

        :param start_time: The start_time of this DocumentAudioDetail.
        :type start_time: float
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this DocumentAudioDetail.

        音频片段结束时间

        :return: The end_time of this DocumentAudioDetail.
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DocumentAudioDetail.

        音频片段结束时间

        :param end_time: The end_time of this DocumentAudioDetail.
        :type end_time: float
        """
        self._end_time = end_time

    @property
    def suggestion(self):
        """Gets the suggestion of this DocumentAudioDetail.

        音频片段审核处理建议： block：包含敏感信息，不通过 review：需要人工复检

        :return: The suggestion of this DocumentAudioDetail.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this DocumentAudioDetail.

        音频片段审核处理建议： block：包含敏感信息，不通过 review：需要人工复检

        :param suggestion: The suggestion of this DocumentAudioDetail.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def audio_text(self):
        """Gets the audio_text of this DocumentAudioDetail.

        音频片段文本内容

        :return: The audio_text of this DocumentAudioDetail.
        :rtype: str
        """
        return self._audio_text

    @audio_text.setter
    def audio_text(self, audio_text):
        """Sets the audio_text of this DocumentAudioDetail.

        音频片段文本内容

        :param audio_text: The audio_text of this DocumentAudioDetail.
        :type audio_text: str
        """
        self._audio_text = audio_text

    @property
    def label(self):
        """Gets the label of this DocumentAudioDetail.

        音频片段标签

        :return: The label of this DocumentAudioDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DocumentAudioDetail.

        音频片段标签

        :param label: The label of this DocumentAudioDetail.
        :type label: str
        """
        self._label = label

    @property
    def segments(self):
        """Gets the segments of this DocumentAudioDetail.

        命中的风险片段信息列表

        :return: The segments of this DocumentAudioDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.DocumentVideoImageDetailSegments`]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this DocumentAudioDetail.

        命中的风险片段信息列表

        :param segments: The segments of this DocumentAudioDetail.
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.DocumentVideoImageDetailSegments`]
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
        if not isinstance(other, DocumentAudioDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
