# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunLanguageDetectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'detected_language': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'detected_language': 'detected_language',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, detected_language=None, error_code=None, error_msg=None):
        """RunLanguageDetectionResponse

        The model defined in huaweicloud sdk

        :param detected_language: 调用成功时表示调用结果，语种缩写对应名称如下： zh    中文 en    英文 ru    俄语 ja    日文 de    德文 fr    法文 es    西班牙文 pt    葡萄牙文 it    意大利文 tr    土耳其文 ar    阿拉伯文 ko    韩语 th    泰国语 ms    马来语 vi    越南语 当输入文本过短或不明确时，识别结果可能不准确； 当输入文本包含多种语言时，会返回占比最高的语种。 调用失败时无此字段。
        :type detected_language: str
        :param error_code: 调用失败时的错误码，具体请参见错误码。调用成功时无此字段。
        :type error_code: str
        :param error_msg: 调用失败时的错误信息。调用成功时无此字段。
        :type error_msg: str
        """
        
        super(RunLanguageDetectionResponse, self).__init__()

        self._detected_language = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if detected_language is not None:
            self.detected_language = detected_language
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def detected_language(self):
        """Gets the detected_language of this RunLanguageDetectionResponse.

        调用成功时表示调用结果，语种缩写对应名称如下： zh    中文 en    英文 ru    俄语 ja    日文 de    德文 fr    法文 es    西班牙文 pt    葡萄牙文 it    意大利文 tr    土耳其文 ar    阿拉伯文 ko    韩语 th    泰国语 ms    马来语 vi    越南语 当输入文本过短或不明确时，识别结果可能不准确； 当输入文本包含多种语言时，会返回占比最高的语种。 调用失败时无此字段。

        :return: The detected_language of this RunLanguageDetectionResponse.
        :rtype: str
        """
        return self._detected_language

    @detected_language.setter
    def detected_language(self, detected_language):
        """Sets the detected_language of this RunLanguageDetectionResponse.

        调用成功时表示调用结果，语种缩写对应名称如下： zh    中文 en    英文 ru    俄语 ja    日文 de    德文 fr    法文 es    西班牙文 pt    葡萄牙文 it    意大利文 tr    土耳其文 ar    阿拉伯文 ko    韩语 th    泰国语 ms    马来语 vi    越南语 当输入文本过短或不明确时，识别结果可能不准确； 当输入文本包含多种语言时，会返回占比最高的语种。 调用失败时无此字段。

        :param detected_language: The detected_language of this RunLanguageDetectionResponse.
        :type detected_language: str
        """
        self._detected_language = detected_language

    @property
    def error_code(self):
        """Gets the error_code of this RunLanguageDetectionResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :return: The error_code of this RunLanguageDetectionResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this RunLanguageDetectionResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :param error_code: The error_code of this RunLanguageDetectionResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this RunLanguageDetectionResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :return: The error_msg of this RunLanguageDetectionResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this RunLanguageDetectionResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :param error_msg: The error_msg of this RunLanguageDetectionResponse.
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
        if not isinstance(other, RunLanguageDetectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
