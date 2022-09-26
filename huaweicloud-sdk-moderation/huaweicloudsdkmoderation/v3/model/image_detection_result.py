# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageDetectionResult:

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
        'details': 'list[ImageDetectionResultDetail]',
        'ocr_text': 'str'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'category': 'category',
        'details': 'details',
        'ocr_text': 'ocr_text'
    }

    def __init__(self, suggestion=None, category=None, details=None, ocr_text=None):
        """ImageDetectionResult

        The model defined in huaweicloud sdk

        :param suggestion: 审核结果是否通过。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检
        :type suggestion: str
        :param category: 检测结果的一级标签。 支持category列表如下： politics: 涉政 terrorism: 暴恐 porn: 色情 image_text: 图文审核
        :type category: str
        :param details: 检测详情
        :type details: list[:class:`huaweicloudsdkmoderation.v3.ImageDetectionResultDetail`]
        :param ocr_text: 图文审核检测出的文本，只有在category参数配置image_text且检测出文本时展示该字段。
        :type ocr_text: str
        """
        
        

        self._suggestion = None
        self._category = None
        self._details = None
        self._ocr_text = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if category is not None:
            self.category = category
        if details is not None:
            self.details = details
        if ocr_text is not None:
            self.ocr_text = ocr_text

    @property
    def suggestion(self):
        """Gets the suggestion of this ImageDetectionResult.

        审核结果是否通过。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检

        :return: The suggestion of this ImageDetectionResult.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this ImageDetectionResult.

        审核结果是否通过。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检

        :param suggestion: The suggestion of this ImageDetectionResult.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def category(self):
        """Gets the category of this ImageDetectionResult.

        检测结果的一级标签。 支持category列表如下： politics: 涉政 terrorism: 暴恐 porn: 色情 image_text: 图文审核

        :return: The category of this ImageDetectionResult.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ImageDetectionResult.

        检测结果的一级标签。 支持category列表如下： politics: 涉政 terrorism: 暴恐 porn: 色情 image_text: 图文审核

        :param category: The category of this ImageDetectionResult.
        :type category: str
        """
        self._category = category

    @property
    def details(self):
        """Gets the details of this ImageDetectionResult.

        检测详情

        :return: The details of this ImageDetectionResult.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.ImageDetectionResultDetail`]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ImageDetectionResult.

        检测详情

        :param details: The details of this ImageDetectionResult.
        :type details: list[:class:`huaweicloudsdkmoderation.v3.ImageDetectionResultDetail`]
        """
        self._details = details

    @property
    def ocr_text(self):
        """Gets the ocr_text of this ImageDetectionResult.

        图文审核检测出的文本，只有在category参数配置image_text且检测出文本时展示该字段。

        :return: The ocr_text of this ImageDetectionResult.
        :rtype: str
        """
        return self._ocr_text

    @ocr_text.setter
    def ocr_text(self, ocr_text):
        """Sets the ocr_text of this ImageDetectionResult.

        图文审核检测出的文本，只有在category参数配置image_text且检测出文本时展示该字段。

        :param ocr_text: The ocr_text of this ImageDetectionResult.
        :type ocr_text: str
        """
        self._ocr_text = ocr_text

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
        if not isinstance(other, ImageDetectionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
