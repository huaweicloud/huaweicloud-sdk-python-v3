# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HWCloudSentimentResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label': 'int',
        'confidence': 'float',
        'content': 'str'
    }

    attribute_map = {
        'label': 'label',
        'confidence': 'confidence',
        'content': 'content'
    }

    def __init__(self, label=None, confidence=None, content=None):
        r"""HWCloudSentimentResp

        The model defined in huaweicloud sdk

        :param label: 该文本的分析结果标签，取值如下： 0 负向 1 正向
        :type label: int
        :param confidence: 标签label的置信度。小数点精确到（6）位。
        :type confidence: float
        :param content: 待分析文本
        :type content: str
        """
        
        

        self._label = None
        self._confidence = None
        self._content = None
        self.discriminator = None

        self.label = label
        self.confidence = confidence
        self.content = content

    @property
    def label(self):
        r"""Gets the label of this HWCloudSentimentResp.

        该文本的分析结果标签，取值如下： 0 负向 1 正向

        :return: The label of this HWCloudSentimentResp.
        :rtype: int
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this HWCloudSentimentResp.

        该文本的分析结果标签，取值如下： 0 负向 1 正向

        :param label: The label of this HWCloudSentimentResp.
        :type label: int
        """
        self._label = label

    @property
    def confidence(self):
        r"""Gets the confidence of this HWCloudSentimentResp.

        标签label的置信度。小数点精确到（6）位。

        :return: The confidence of this HWCloudSentimentResp.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        r"""Sets the confidence of this HWCloudSentimentResp.

        标签label的置信度。小数点精确到（6）位。

        :param confidence: The confidence of this HWCloudSentimentResp.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def content(self):
        r"""Gets the content of this HWCloudSentimentResp.

        待分析文本

        :return: The content of this HWCloudSentimentResp.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this HWCloudSentimentResp.

        待分析文本

        :param content: The content of this HWCloudSentimentResp.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, HWCloudSentimentResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
