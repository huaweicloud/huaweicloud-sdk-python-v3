# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckResultItemsBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'suggestion': 'str',
        'detail': 'ImageDetectionResultDetail',
        'category_suggestions': 'dict(str, str)',
        'ocr_text': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'url': 'url',
        'suggestion': 'suggestion',
        'detail': 'detail',
        'category_suggestions': 'category_suggestions',
        'ocr_text': 'ocr_text',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, url=None, suggestion=None, detail=None, category_suggestions=None, ocr_text=None, error_code=None, error_msg=None):
        """CheckResultItemsBody

        The model defined in huaweicloud sdk

        :param url: 图片的URL路径。
        :type url: str
        :param suggestion: 检测结果是否通过。 - block：包含敏感信息，不通过 - pass：不包含敏感信息，通过 - review：需要人工复检 &gt; 当同时检测多个场景时，suggestion的值以最可能包含敏感信息的场景为准。即任一场景出现了block则总的suggestion为block，所有场景都pass时suggestion为pass，这两种情况之外则一定有场景需要review，此时suggestion为review。 
        :type suggestion: str
        :param detail: 
        :type detail: :class:`huaweicloudsdkmoderation.v2.ImageDetectionResultDetail`
        :param category_suggestions: 具体每个场景的检测结果。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检 
        :type category_suggestions: dict(str, str)
        :param ocr_text: ocr识别结果。
        :type ocr_text: str
        :param error_code: 图像审核失败时错误码
        :type error_code: str
        :param error_msg: 图像审核失败时错误信息
        :type error_msg: str
        """
        
        

        self._url = None
        self._suggestion = None
        self._detail = None
        self._category_suggestions = None
        self._ocr_text = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if suggestion is not None:
            self.suggestion = suggestion
        if detail is not None:
            self.detail = detail
        if category_suggestions is not None:
            self.category_suggestions = category_suggestions
        if ocr_text is not None:
            self.ocr_text = ocr_text
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def url(self):
        """Gets the url of this CheckResultItemsBody.

        图片的URL路径。

        :return: The url of this CheckResultItemsBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CheckResultItemsBody.

        图片的URL路径。

        :param url: The url of this CheckResultItemsBody.
        :type url: str
        """
        self._url = url

    @property
    def suggestion(self):
        """Gets the suggestion of this CheckResultItemsBody.

        检测结果是否通过。 - block：包含敏感信息，不通过 - pass：不包含敏感信息，通过 - review：需要人工复检 > 当同时检测多个场景时，suggestion的值以最可能包含敏感信息的场景为准。即任一场景出现了block则总的suggestion为block，所有场景都pass时suggestion为pass，这两种情况之外则一定有场景需要review，此时suggestion为review。 

        :return: The suggestion of this CheckResultItemsBody.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this CheckResultItemsBody.

        检测结果是否通过。 - block：包含敏感信息，不通过 - pass：不包含敏感信息，通过 - review：需要人工复检 > 当同时检测多个场景时，suggestion的值以最可能包含敏感信息的场景为准。即任一场景出现了block则总的suggestion为block，所有场景都pass时suggestion为pass，这两种情况之外则一定有场景需要review，此时suggestion为review。 

        :param suggestion: The suggestion of this CheckResultItemsBody.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def detail(self):
        """Gets the detail of this CheckResultItemsBody.

        :return: The detail of this CheckResultItemsBody.
        :rtype: :class:`huaweicloudsdkmoderation.v2.ImageDetectionResultDetail`
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this CheckResultItemsBody.

        :param detail: The detail of this CheckResultItemsBody.
        :type detail: :class:`huaweicloudsdkmoderation.v2.ImageDetectionResultDetail`
        """
        self._detail = detail

    @property
    def category_suggestions(self):
        """Gets the category_suggestions of this CheckResultItemsBody.

        具体每个场景的检测结果。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检 

        :return: The category_suggestions of this CheckResultItemsBody.
        :rtype: dict(str, str)
        """
        return self._category_suggestions

    @category_suggestions.setter
    def category_suggestions(self, category_suggestions):
        """Sets the category_suggestions of this CheckResultItemsBody.

        具体每个场景的检测结果。  block：包含敏感信息，不通过  pass：不包含敏感信息，通过  review：需要人工复检 

        :param category_suggestions: The category_suggestions of this CheckResultItemsBody.
        :type category_suggestions: dict(str, str)
        """
        self._category_suggestions = category_suggestions

    @property
    def ocr_text(self):
        """Gets the ocr_text of this CheckResultItemsBody.

        ocr识别结果。

        :return: The ocr_text of this CheckResultItemsBody.
        :rtype: str
        """
        return self._ocr_text

    @ocr_text.setter
    def ocr_text(self, ocr_text):
        """Sets the ocr_text of this CheckResultItemsBody.

        ocr识别结果。

        :param ocr_text: The ocr_text of this CheckResultItemsBody.
        :type ocr_text: str
        """
        self._ocr_text = ocr_text

    @property
    def error_code(self):
        """Gets the error_code of this CheckResultItemsBody.

        图像审核失败时错误码

        :return: The error_code of this CheckResultItemsBody.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this CheckResultItemsBody.

        图像审核失败时错误码

        :param error_code: The error_code of this CheckResultItemsBody.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this CheckResultItemsBody.

        图像审核失败时错误信息

        :return: The error_msg of this CheckResultItemsBody.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this CheckResultItemsBody.

        图像审核失败时错误信息

        :param error_msg: The error_msg of this CheckResultItemsBody.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, CheckResultItemsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
