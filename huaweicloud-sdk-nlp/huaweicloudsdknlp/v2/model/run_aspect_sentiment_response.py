# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunAspectSentimentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'text': 'str',
        'label': 'int',
        'confidence': 'float',
        'aspect_opinions': 'list[AspectOpinion]',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'text': 'text',
        'label': 'label',
        'confidence': 'confidence',
        'aspect_opinions': 'aspect_opinions',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, text=None, label=None, confidence=None, aspect_opinions=None, error_code=None, error_msg=None):
        """RunAspectSentimentResponse

        The model defined in huaweicloud sdk

        :param text: 待分析文本
        :type text: str
        :param label: 该文本的整体情感标签，取值如下： 0  负向 1  正向
        :type label: int
        :param confidence: 该文本整体情感label的置信度,小数点精确到3位。
        :type confidence: float
        :param aspect_opinions: 属性级情感挖掘列表
        :type aspect_opinions: list[:class:`huaweicloudsdknlp.v2.AspectOpinion`]
        :param error_code: 调用失败时的错误码，具体请参见错误码。调用成功时无此字段。
        :type error_code: str
        :param error_msg: 调用失败时的错误信息。调用成功时无此字段。
        :type error_msg: str
        """
        
        super(RunAspectSentimentResponse, self).__init__()

        self._text = None
        self._label = None
        self._confidence = None
        self._aspect_opinions = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if label is not None:
            self.label = label
        if confidence is not None:
            self.confidence = confidence
        if aspect_opinions is not None:
            self.aspect_opinions = aspect_opinions
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def text(self):
        """Gets the text of this RunAspectSentimentResponse.

        待分析文本

        :return: The text of this RunAspectSentimentResponse.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this RunAspectSentimentResponse.

        待分析文本

        :param text: The text of this RunAspectSentimentResponse.
        :type text: str
        """
        self._text = text

    @property
    def label(self):
        """Gets the label of this RunAspectSentimentResponse.

        该文本的整体情感标签，取值如下： 0  负向 1  正向

        :return: The label of this RunAspectSentimentResponse.
        :rtype: int
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this RunAspectSentimentResponse.

        该文本的整体情感标签，取值如下： 0  负向 1  正向

        :param label: The label of this RunAspectSentimentResponse.
        :type label: int
        """
        self._label = label

    @property
    def confidence(self):
        """Gets the confidence of this RunAspectSentimentResponse.

        该文本整体情感label的置信度,小数点精确到3位。

        :return: The confidence of this RunAspectSentimentResponse.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this RunAspectSentimentResponse.

        该文本整体情感label的置信度,小数点精确到3位。

        :param confidence: The confidence of this RunAspectSentimentResponse.
        :type confidence: float
        """
        self._confidence = confidence

    @property
    def aspect_opinions(self):
        """Gets the aspect_opinions of this RunAspectSentimentResponse.

        属性级情感挖掘列表

        :return: The aspect_opinions of this RunAspectSentimentResponse.
        :rtype: list[:class:`huaweicloudsdknlp.v2.AspectOpinion`]
        """
        return self._aspect_opinions

    @aspect_opinions.setter
    def aspect_opinions(self, aspect_opinions):
        """Sets the aspect_opinions of this RunAspectSentimentResponse.

        属性级情感挖掘列表

        :param aspect_opinions: The aspect_opinions of this RunAspectSentimentResponse.
        :type aspect_opinions: list[:class:`huaweicloudsdknlp.v2.AspectOpinion`]
        """
        self._aspect_opinions = aspect_opinions

    @property
    def error_code(self):
        """Gets the error_code of this RunAspectSentimentResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :return: The error_code of this RunAspectSentimentResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this RunAspectSentimentResponse.

        调用失败时的错误码，具体请参见错误码。调用成功时无此字段。

        :param error_code: The error_code of this RunAspectSentimentResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this RunAspectSentimentResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :return: The error_msg of this RunAspectSentimentResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this RunAspectSentimentResponse.

        调用失败时的错误信息。调用成功时无此字段。

        :param error_msg: The error_msg of this RunAspectSentimentResponse.
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
        if not isinstance(other, RunAspectSentimentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
