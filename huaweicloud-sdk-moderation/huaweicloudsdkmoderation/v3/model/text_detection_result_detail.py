# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextDetectionResultDetail:

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
        'confidence': 'float',
        'segments': 'list[SegmentResult]'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'label': 'label',
        'confidence': 'confidence',
        'segments': 'segments'
    }

    def __init__(self, suggestion=None, label=None, confidence=None, segments=None):
        """TextDetectionResultDetail

        The model defined in huaweicloud sdk

        :param suggestion: 审核结果是否通过。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检
        :type suggestion: str
        :param label: 检测结果的标签。  支持label列表如下：  politics: 涉政  terrorism: 暴恐  porn: 色情  ban: 违禁  abuse: 辱骂  ad: 广告  ad_law: 广告法  meaningless: ⽆意义  customized：自定义（命中自定义词库中的关键词）
        :type label: str
        :param confidence: 置信度，取值范围 0-1，值越⼤，可信度越⾼。
        :type confidence: float
        :param segments: 命中的风险片段信息，如果命中了语义算法模型，则会返回一个空的列表。
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.SegmentResult`]
        """
        
        

        self._suggestion = None
        self._label = None
        self._confidence = None
        self._segments = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if label is not None:
            self.label = label
        if confidence is not None:
            self.confidence = confidence
        if segments is not None:
            self.segments = segments

    @property
    def suggestion(self):
        """Gets the suggestion of this TextDetectionResultDetail.

        审核结果是否通过。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检

        :return: The suggestion of this TextDetectionResultDetail.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this TextDetectionResultDetail.

        审核结果是否通过。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检

        :param suggestion: The suggestion of this TextDetectionResultDetail.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def label(self):
        """Gets the label of this TextDetectionResultDetail.

        检测结果的标签。  支持label列表如下：  politics: 涉政  terrorism: 暴恐  porn: 色情  ban: 违禁  abuse: 辱骂  ad: 广告  ad_law: 广告法  meaningless: ⽆意义  customized：自定义（命中自定义词库中的关键词）

        :return: The label of this TextDetectionResultDetail.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TextDetectionResultDetail.

        检测结果的标签。  支持label列表如下：  politics: 涉政  terrorism: 暴恐  porn: 色情  ban: 违禁  abuse: 辱骂  ad: 广告  ad_law: 广告法  meaningless: ⽆意义  customized：自定义（命中自定义词库中的关键词）

        :param label: The label of this TextDetectionResultDetail.
        :type label: str
        """
        self._label = label

    @property
    def confidence(self):
        """Gets the confidence of this TextDetectionResultDetail.

        置信度，取值范围 0-1，值越⼤，可信度越⾼。

        :return: The confidence of this TextDetectionResultDetail.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TextDetectionResultDetail.

        置信度，取值范围 0-1，值越⼤，可信度越⾼。

        :param confidence: The confidence of this TextDetectionResultDetail.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def segments(self):
        """Gets the segments of this TextDetectionResultDetail.

        命中的风险片段信息，如果命中了语义算法模型，则会返回一个空的列表。

        :return: The segments of this TextDetectionResultDetail.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.SegmentResult`]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this TextDetectionResultDetail.

        命中的风险片段信息，如果命中了语义算法模型，则会返回一个空的列表。

        :param segments: The segments of this TextDetectionResultDetail.
        :type segments: list[:class:`huaweicloudsdkmoderation.v3.SegmentResult`]
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
        if not isinstance(other, TextDetectionResultDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
