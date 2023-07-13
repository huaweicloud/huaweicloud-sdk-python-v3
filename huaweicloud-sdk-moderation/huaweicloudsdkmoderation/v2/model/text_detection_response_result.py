# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextDetectionResponseResult:

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
        'detail': 'object'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'detail': 'detail'
    }

    def __init__(self, suggestion=None, detail=None):
        """TextDetectionResponseResult

        The model defined in huaweicloud sdk

        :param suggestion: 检测结果是否通过。  block：包含敏感信息，不通过。  pass：不包含敏感信息，通过。  review：需要人工复查。
        :type suggestion: str
        :param detail: 返回的相关检测结果详细信息：  - politics：涉政敏感词列表。  - porn：涉黄敏感词列表。  - ad：广告敏感词列表。  - abuse：辱骂敏感词列表。  - contraband：违禁品敏感词列表。  - flood：灌水文本。  &gt; - 灌水文本最多显示200个字符。 &gt; - 每个场景的返回结果的详细信息是指命中词，不是返回全部文本。
        :type detail: object
        """
        
        

        self._suggestion = None
        self._detail = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if detail is not None:
            self.detail = detail

    @property
    def suggestion(self):
        """Gets the suggestion of this TextDetectionResponseResult.

        检测结果是否通过。  block：包含敏感信息，不通过。  pass：不包含敏感信息，通过。  review：需要人工复查。

        :return: The suggestion of this TextDetectionResponseResult.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this TextDetectionResponseResult.

        检测结果是否通过。  block：包含敏感信息，不通过。  pass：不包含敏感信息，通过。  review：需要人工复查。

        :param suggestion: The suggestion of this TextDetectionResponseResult.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def detail(self):
        """Gets the detail of this TextDetectionResponseResult.

        返回的相关检测结果详细信息：  - politics：涉政敏感词列表。  - porn：涉黄敏感词列表。  - ad：广告敏感词列表。  - abuse：辱骂敏感词列表。  - contraband：违禁品敏感词列表。  - flood：灌水文本。  > - 灌水文本最多显示200个字符。 > - 每个场景的返回结果的详细信息是指命中词，不是返回全部文本。

        :return: The detail of this TextDetectionResponseResult.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this TextDetectionResponseResult.

        返回的相关检测结果详细信息：  - politics：涉政敏感词列表。  - porn：涉黄敏感词列表。  - ad：广告敏感词列表。  - abuse：辱骂敏感词列表。  - contraband：违禁品敏感词列表。  - flood：灌水文本。  > - 灌水文本最多显示200个字符。 > - 每个场景的返回结果的详细信息是指命中词，不是返回全部文本。

        :param detail: The detail of this TextDetectionResponseResult.
        :type detail: object
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
        if not isinstance(other, TextDetectionResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
