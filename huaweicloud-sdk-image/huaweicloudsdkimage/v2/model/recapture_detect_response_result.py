# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecaptureDetectResponseResult:

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
        'category': 'str',
        'score': 'str',
        'detail': 'list[RecaptureDetectResponseResultDetail]'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'category': 'category',
        'score': 'score',
        'detail': 'detail'
    }

    def __init__(self, suggestion=None, category=None, score=None, detail=None):
        """RecaptureDetectResponseResult

        The model defined in huaweicloud sdk

        :param suggestion: 总体的结论： true：真实 false：虚假 uncertainty：不确定 
        :type suggestion: str
        :param category: 标签（如果suggestion为真时，则该值为空字符串，否则不为空）。recapture：翻拍图
        :type category: str
        :param score: 总体置信度，取值范围（0~1）。
        :type score: str
        :param detail: 识别结果详情。
        :type detail: list[:class:`huaweicloudsdkimage.v2.RecaptureDetectResponseResultDetail`]
        """
        
        

        self._suggestion = None
        self._category = None
        self._score = None
        self._detail = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if category is not None:
            self.category = category
        if score is not None:
            self.score = score
        if detail is not None:
            self.detail = detail

    @property
    def suggestion(self):
        """Gets the suggestion of this RecaptureDetectResponseResult.

        总体的结论： true：真实 false：虚假 uncertainty：不确定 

        :return: The suggestion of this RecaptureDetectResponseResult.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this RecaptureDetectResponseResult.

        总体的结论： true：真实 false：虚假 uncertainty：不确定 

        :param suggestion: The suggestion of this RecaptureDetectResponseResult.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def category(self):
        """Gets the category of this RecaptureDetectResponseResult.

        标签（如果suggestion为真时，则该值为空字符串，否则不为空）。recapture：翻拍图

        :return: The category of this RecaptureDetectResponseResult.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this RecaptureDetectResponseResult.

        标签（如果suggestion为真时，则该值为空字符串，否则不为空）。recapture：翻拍图

        :param category: The category of this RecaptureDetectResponseResult.
        :type category: str
        """
        self._category = category

    @property
    def score(self):
        """Gets the score of this RecaptureDetectResponseResult.

        总体置信度，取值范围（0~1）。

        :return: The score of this RecaptureDetectResponseResult.
        :rtype: str
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this RecaptureDetectResponseResult.

        总体置信度，取值范围（0~1）。

        :param score: The score of this RecaptureDetectResponseResult.
        :type score: str
        """
        self._score = score

    @property
    def detail(self):
        """Gets the detail of this RecaptureDetectResponseResult.

        识别结果详情。

        :return: The detail of this RecaptureDetectResponseResult.
        :rtype: list[:class:`huaweicloudsdkimage.v2.RecaptureDetectResponseResultDetail`]
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this RecaptureDetectResponseResult.

        识别结果详情。

        :param detail: The detail of this RecaptureDetectResponseResult.
        :type detail: list[:class:`huaweicloudsdkimage.v2.RecaptureDetectResponseResultDetail`]
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
        if not isinstance(other, RecaptureDetectResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
