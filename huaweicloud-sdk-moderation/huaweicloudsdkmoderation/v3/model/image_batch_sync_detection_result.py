# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageBatchSyncDetectionResult:

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
        'ocr_text': 'str',
        'data_id': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'category': 'category',
        'details': 'details',
        'ocr_text': 'ocr_text',
        'data_id': 'data_id',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, suggestion=None, category=None, details=None, ocr_text=None, data_id=None, error_code=None, error_msg=None):
        r"""ImageBatchSyncDetectionResult

        The model defined in huaweicloud sdk

        :param suggestion: 审核结果是否通过。 - block：包含敏感信息，不通过。 - pass：不包含敏感信息，通过 。 - review：需要人工复检。
        :type suggestion: str
        :param category: 检测结果的一级标签。支持category列表如下： - terrorism: 暴恐 - porn: 色情 - image_text: 图文审核
        :type category: str
        :param details: 检测详情。
        :type details: list[:class:`huaweicloudsdkmoderation.v3.ImageDetectionResultDetail`]
        :param ocr_text: 图文审核检测出的文本，只有在category参数配置image_text且检测出文本时展示该字段。
        :type ocr_text: str
        :param data_id: 图片唯一标识。同一次请求中不可重复，由大小写英文字母、数字、下划线（_）、中划线（-）组成，不超过30个字符。
        :type data_id: str
        :param error_code: 调用失败时的错误码，具体请参见错误码。 调用成功时无此字段。
        :type error_code: str
        :param error_msg: 调用失败时的错误信息。 调用成功时无此字段。
        :type error_msg: str
        """
        
        

        self._suggestion = None
        self._category = None
        self._details = None
        self._ocr_text = None
        self._data_id = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if category is not None:
            self.category = category
        if details is not None:
            self.details = details
        if ocr_text is not None:
            self.ocr_text = ocr_text
        self.data_id = data_id
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def suggestion(self):
        r"""Gets the suggestion of this ImageBatchSyncDetectionResult.

        审核结果是否通过。 - block：包含敏感信息，不通过。 - pass：不包含敏感信息，通过 。 - review：需要人工复检。

        :return: The suggestion of this ImageBatchSyncDetectionResult.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this ImageBatchSyncDetectionResult.

        审核结果是否通过。 - block：包含敏感信息，不通过。 - pass：不包含敏感信息，通过 。 - review：需要人工复检。

        :param suggestion: The suggestion of this ImageBatchSyncDetectionResult.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def category(self):
        r"""Gets the category of this ImageBatchSyncDetectionResult.

        检测结果的一级标签。支持category列表如下： - terrorism: 暴恐 - porn: 色情 - image_text: 图文审核

        :return: The category of this ImageBatchSyncDetectionResult.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ImageBatchSyncDetectionResult.

        检测结果的一级标签。支持category列表如下： - terrorism: 暴恐 - porn: 色情 - image_text: 图文审核

        :param category: The category of this ImageBatchSyncDetectionResult.
        :type category: str
        """
        self._category = category

    @property
    def details(self):
        r"""Gets the details of this ImageBatchSyncDetectionResult.

        检测详情。

        :return: The details of this ImageBatchSyncDetectionResult.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.ImageDetectionResultDetail`]
        """
        return self._details

    @details.setter
    def details(self, details):
        r"""Sets the details of this ImageBatchSyncDetectionResult.

        检测详情。

        :param details: The details of this ImageBatchSyncDetectionResult.
        :type details: list[:class:`huaweicloudsdkmoderation.v3.ImageDetectionResultDetail`]
        """
        self._details = details

    @property
    def ocr_text(self):
        r"""Gets the ocr_text of this ImageBatchSyncDetectionResult.

        图文审核检测出的文本，只有在category参数配置image_text且检测出文本时展示该字段。

        :return: The ocr_text of this ImageBatchSyncDetectionResult.
        :rtype: str
        """
        return self._ocr_text

    @ocr_text.setter
    def ocr_text(self, ocr_text):
        r"""Sets the ocr_text of this ImageBatchSyncDetectionResult.

        图文审核检测出的文本，只有在category参数配置image_text且检测出文本时展示该字段。

        :param ocr_text: The ocr_text of this ImageBatchSyncDetectionResult.
        :type ocr_text: str
        """
        self._ocr_text = ocr_text

    @property
    def data_id(self):
        r"""Gets the data_id of this ImageBatchSyncDetectionResult.

        图片唯一标识。同一次请求中不可重复，由大小写英文字母、数字、下划线（_）、中划线（-）组成，不超过30个字符。

        :return: The data_id of this ImageBatchSyncDetectionResult.
        :rtype: str
        """
        return self._data_id

    @data_id.setter
    def data_id(self, data_id):
        r"""Sets the data_id of this ImageBatchSyncDetectionResult.

        图片唯一标识。同一次请求中不可重复，由大小写英文字母、数字、下划线（_）、中划线（-）组成，不超过30个字符。

        :param data_id: The data_id of this ImageBatchSyncDetectionResult.
        :type data_id: str
        """
        self._data_id = data_id

    @property
    def error_code(self):
        r"""Gets the error_code of this ImageBatchSyncDetectionResult.

        调用失败时的错误码，具体请参见错误码。 调用成功时无此字段。

        :return: The error_code of this ImageBatchSyncDetectionResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ImageBatchSyncDetectionResult.

        调用失败时的错误码，具体请参见错误码。 调用成功时无此字段。

        :param error_code: The error_code of this ImageBatchSyncDetectionResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ImageBatchSyncDetectionResult.

        调用失败时的错误信息。 调用成功时无此字段。

        :return: The error_msg of this ImageBatchSyncDetectionResult.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ImageBatchSyncDetectionResult.

        调用失败时的错误信息。 调用成功时无此字段。

        :param error_msg: The error_msg of this ImageBatchSyncDetectionResult.
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
        if not isinstance(other, ImageBatchSyncDetectionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
