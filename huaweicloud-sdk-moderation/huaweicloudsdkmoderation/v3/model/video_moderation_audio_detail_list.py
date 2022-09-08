# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoModerationAudioDetailList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'confidence': 'float',
        'label': 'str',
        'suggestion': 'str',
        'segments': 'list[VideoModerationDetailSegment]'
    }

    attribute_map = {
        'confidence': 'confidence',
        'label': 'label',
        'suggestion': 'suggestion',
        'segments': 'segments'
    }

    def __init__(self, confidence=None, label=None, suggestion=None, segments=None):
        """VideoModerationAudioDetailList

        The model defined in huaweicloud sdk

        :param confidence: 风险置信度
        :type confidence: float
        :param label: 风险标签
        :type label: str
        :param suggestion: 审核处理建议： block：包含敏感信息，不通过 review：需要人工复检
        :type suggestion: str
        :param segments: 命中的风险片段信息列表，如果命中语义算法模型，则该字段不会存在
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationDetailSegment`]
        """
        
        

        self._confidence = None
        self._label = None
        self._suggestion = None
        self._segments = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if label is not None:
            self.label = label
        if suggestion is not None:
            self.suggestion = suggestion
        if segments is not None:
            self.segments = segments

    @property
    def confidence(self):
        """Gets the confidence of this VideoModerationAudioDetailList.

        风险置信度

        :return: The confidence of this VideoModerationAudioDetailList.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this VideoModerationAudioDetailList.

        风险置信度

        :param confidence: The confidence of this VideoModerationAudioDetailList.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def label(self):
        """Gets the label of this VideoModerationAudioDetailList.

        风险标签

        :return: The label of this VideoModerationAudioDetailList.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this VideoModerationAudioDetailList.

        风险标签

        :param label: The label of this VideoModerationAudioDetailList.
        :type label: str
        """
        self._label = label

    @property
    def suggestion(self):
        """Gets the suggestion of this VideoModerationAudioDetailList.

        审核处理建议： block：包含敏感信息，不通过 review：需要人工复检

        :return: The suggestion of this VideoModerationAudioDetailList.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this VideoModerationAudioDetailList.

        审核处理建议： block：包含敏感信息，不通过 review：需要人工复检

        :param suggestion: The suggestion of this VideoModerationAudioDetailList.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def segments(self):
        """Gets the segments of this VideoModerationAudioDetailList.

        命中的风险片段信息列表，如果命中语义算法模型，则该字段不会存在

        :return: The segments of this VideoModerationAudioDetailList.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationDetailSegment`]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this VideoModerationAudioDetailList.

        命中的风险片段信息列表，如果命中语义算法模型，则该字段不会存在

        :param segments: The segments of this VideoModerationAudioDetailList.
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
        if not isinstance(other, VideoModerationAudioDetailList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
