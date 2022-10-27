# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoModerationVideoDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'suggestion': 'str',
        'label': 'str',
        'audio_text': 'str',
        'end_time': 'float',
        'start_time': 'float',
        'detail': 'list[VideoModerationAudioDetailList]'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'label': 'label',
        'audio_text': 'audio_text',
        'end_time': 'end_time',
        'start_time': 'start_time',
        'detail': 'detail'
    }

    def __init__(self, suggestion=None, label=None, audio_text=None, end_time=None, start_time=None, detail=None):
        """VideoModerationVideoDetail

        The model defined in huaweicloud sdk

        :param suggestion: 音频片段审核结果是否通过。 block：包含敏感信息，不通过  review：需要人工复检
        :type suggestion: str
        :param label: 音频片段检测标签，选取detail中置信度最大的标签，可取值如下： politics: 涉政  terrorism: 暴恐  porn: 色情  ad: 广告 ad_law: 广告法 abuse: 辱骂 ban: 违禁 meaningless: 无意义 moan: 娇喘
        :type label: str
        :param audio_text: 音频片段文本内容
        :type audio_text: str
        :param end_time: 音频片段结束时间
        :type end_time: float
        :param start_time: 音频片段开始时间
        :type start_time: float
        :param detail: 音频片段审核详情
        :type detail: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationAudioDetailList`]
        """
        
        

        self._suggestion = None
        self._label = None
        self._audio_text = None
        self._end_time = None
        self._start_time = None
        self._detail = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if label is not None:
            self.label = label
        if audio_text is not None:
            self.audio_text = audio_text
        if end_time is not None:
            self.end_time = end_time
        if start_time is not None:
            self.start_time = start_time
        if detail is not None:
            self.detail = detail

    @property
    def suggestion(self):
        """Gets the suggestion of this VideoModerationVideoDetail.

        音频片段审核结果是否通过。 block：包含敏感信息，不通过  review：需要人工复检

        :return: The suggestion of this VideoModerationVideoDetail.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this VideoModerationVideoDetail.

        音频片段审核结果是否通过。 block：包含敏感信息，不通过  review：需要人工复检

        :param suggestion: The suggestion of this VideoModerationVideoDetail.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def label(self):
        """Gets the label of this VideoModerationVideoDetail.

        音频片段检测标签，选取detail中置信度最大的标签，可取值如下： politics: 涉政  terrorism: 暴恐  porn: 色情  ad: 广告 ad_law: 广告法 abuse: 辱骂 ban: 违禁 meaningless: 无意义 moan: 娇喘

        :return: The label of this VideoModerationVideoDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VideoModerationVideoDetail.

        音频片段检测标签，选取detail中置信度最大的标签，可取值如下： politics: 涉政  terrorism: 暴恐  porn: 色情  ad: 广告 ad_law: 广告法 abuse: 辱骂 ban: 违禁 meaningless: 无意义 moan: 娇喘

        :param label: The label of this VideoModerationVideoDetail.
        :type label: str
        """
        self._label = label

    @property
    def audio_text(self):
        """Gets the audio_text of this VideoModerationVideoDetail.

        音频片段文本内容

        :return: The audio_text of this VideoModerationVideoDetail.
        :rtype: str
        """
        return self._audio_text

    @audio_text.setter
    def audio_text(self, audio_text):
        """Sets the audio_text of this VideoModerationVideoDetail.

        音频片段文本内容

        :param audio_text: The audio_text of this VideoModerationVideoDetail.
        :type audio_text: str
        """
        self._audio_text = audio_text

    @property
    def end_time(self):
        """Gets the end_time of this VideoModerationVideoDetail.

        音频片段结束时间

        :return: The end_time of this VideoModerationVideoDetail.
        :rtype: float
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this VideoModerationVideoDetail.

        音频片段结束时间

        :param end_time: The end_time of this VideoModerationVideoDetail.
        :type end_time: float
        """
        self._end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this VideoModerationVideoDetail.

        音频片段开始时间

        :return: The start_time of this VideoModerationVideoDetail.
        :rtype: float
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this VideoModerationVideoDetail.

        音频片段开始时间

        :param start_time: The start_time of this VideoModerationVideoDetail.
        :type start_time: float
        """
        self._start_time = start_time

    @property
    def detail(self):
        """Gets the detail of this VideoModerationVideoDetail.

        音频片段审核详情

        :return: The detail of this VideoModerationVideoDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationAudioDetailList`]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this VideoModerationVideoDetail.

        音频片段审核详情

        :param detail: The detail of this VideoModerationVideoDetail.
        :type detail: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationAudioDetailList`]
        """
        self._detail = detail

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
        if not isinstance(other, VideoModerationVideoDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
