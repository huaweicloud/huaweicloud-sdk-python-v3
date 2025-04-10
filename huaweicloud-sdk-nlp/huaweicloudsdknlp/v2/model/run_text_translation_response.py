# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunTextTranslationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'src_text': 'str',
        'translated_text': 'str',
        '_from': 'str',
        'to': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'src_text': 'src_text',
        'translated_text': 'translated_text',
        '_from': 'from',
        'to': 'to',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, src_text=None, translated_text=None, _from=None, to=None, error_code=None, error_msg=None):
        r"""RunTextTranslationResponse

        The model defined in huaweicloud sdk

        :param src_text: 翻译原文，编码格式为UTF-8。调用失败时无此字段。
        :type src_text: str
        :param translated_text: 翻译译文，编码格式为UTF-8。调用失败时无此字段。
        :type translated_text: str
        :param _from: 调用成功时表示源语种（源语种输入为auto时，显示语种识别结果），编码格式为UTF-8。调用失败时无此字段。
        :type _from: str
        :param to: 调用成功时表示目标语种，编码格式为UTF-8。调用失败时无此字段。
        :type to: str
        :param error_code: 调用失败时的错误码，具体请参见错误码。调用成功时无此字段。
        :type error_code: str
        :param error_msg: 调用失败时的错误信息。调用成功时无此字段。
        :type error_msg: str
        """
        
        super(RunTextTranslationResponse, self).__init__()

        self._src_text = None
        self._translated_text = None
        self.__from = None
        self._to = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if src_text is not None:
            self.src_text = src_text
        if translated_text is not None:
            self.translated_text = translated_text
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def src_text(self):
        r"""Gets the src_text of this RunTextTranslationResponse.

        翻译原文，编码格式为UTF-8。调用失败时无此字段。

        :return: The src_text of this RunTextTranslationResponse.
        :rtype: str
        """
        return self._src_text

    @src_text.setter
    def src_text(self, src_text):
        r"""Sets the src_text of this RunTextTranslationResponse.

        翻译原文，编码格式为UTF-8。调用失败时无此字段。

        :param src_text: The src_text of this RunTextTranslationResponse.
        :type src_text: str
        """
        self._src_text = src_text

    @property
    def translated_text(self):
        r"""Gets the translated_text of this RunTextTranslationResponse.

        翻译译文，编码格式为UTF-8。调用失败时无此字段。

        :return: The translated_text of this RunTextTranslationResponse.
        :rtype: str
        """
        return self._translated_text

    @translated_text.setter
    def translated_text(self, translated_text):
        r"""Sets the translated_text of this RunTextTranslationResponse.

        翻译译文，编码格式为UTF-8。调用失败时无此字段。

        :param translated_text: The translated_text of this RunTextTranslationResponse.
        :type translated_text: str
        """
        self._translated_text = translated_text

    @property
    def _from(self):
        r"""Gets the _from of this RunTextTranslationResponse.

        调用成功时表示源语种（源语种输入为auto时，显示语种识别结果），编码格式为UTF-8。调用失败时无此字段。

        :return: The _from of this RunTextTranslationResponse.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this RunTextTranslationResponse.

        调用成功时表示源语种（源语种输入为auto时，显示语种识别结果），编码格式为UTF-8。调用失败时无此字段。

        :param _from: The _from of this RunTextTranslationResponse.
        :type _from: str
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this RunTextTranslationResponse.

        调用成功时表示目标语种，编码格式为UTF-8。调用失败时无此字段。

        :return: The to of this RunTextTranslationResponse.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this RunTextTranslationResponse.

        调用成功时表示目标语种，编码格式为UTF-8。调用失败时无此字段。

        :param to: The to of this RunTextTranslationResponse.
        :type to: str
        """
        self._to = to

    @property
    def error_code(self):
        r"""Gets the error_code of this RunTextTranslationResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :return: The error_code of this RunTextTranslationResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this RunTextTranslationResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :param error_code: The error_code of this RunTextTranslationResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this RunTextTranslationResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :return: The error_msg of this RunTextTranslationResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this RunTextTranslationResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :param error_msg: The error_msg of this RunTextTranslationResponse.
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
        if not isinstance(other, RunTextTranslationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
