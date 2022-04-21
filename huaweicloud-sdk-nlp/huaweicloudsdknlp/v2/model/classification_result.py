# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClassificationResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'label': 'int',
        'confidence': 'float'
    }

    attribute_map = {
        'content': 'content',
        'label': 'label',
        'confidence': 'confidence'
    }

    def __init__(self, content=None, label=None, confidence=None):
        """ClassificationResult

        The model defined in huaweicloud sdk

        :param content: 待分析文本。
        :type content: str
        :param label: 分类标签。 1：广告 0：非广告
        :type label: int
        :param confidence: 标签label的置信度。
        :type confidence: float
        """
        
        

        self._content = None
        self._label = None
        self._confidence = None
        self.discriminator = None

        self.content = content
        self.label = label
        self.confidence = confidence

    @property
    def content(self):
        """Gets the content of this ClassificationResult.

        待分析文本。

        :return: The content of this ClassificationResult.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ClassificationResult.

        待分析文本。

        :param content: The content of this ClassificationResult.
        :type content: str
        """
        self._content = content

    @property
    def label(self):
        """Gets the label of this ClassificationResult.

        分类标签。 1：广告 0：非广告

        :return: The label of this ClassificationResult.
        :rtype: int
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ClassificationResult.

        分类标签。 1：广告 0：非广告

        :param label: The label of this ClassificationResult.
        :type label: int
        """
        self._label = label

    @property
    def confidence(self):
        """Gets the confidence of this ClassificationResult.

        标签label的置信度。

        :return: The confidence of this ClassificationResult.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this ClassificationResult.

        标签label的置信度。

        :param confidence: The confidence of this ClassificationResult.
        :type confidence: float
        """
        self._confidence = confidence

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
        if not isinstance(other, ClassificationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
