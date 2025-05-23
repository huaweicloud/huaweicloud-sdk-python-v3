# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextDetectionDataReq:

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
        'language': 'str'
    }

    attribute_map = {
        'text': 'text',
        'language': 'language'
    }

    def __init__(self, text=None, language=None):
        r"""TextDetectionDataReq

        The model defined in huaweicloud sdk

        :param text: 待检测文本，编码格式为“utf-8”，限定2000个字符以内，文本长度超过10000个字符时，只检测前10000个字符。
        :type text: str
        :param language: 支持检测的文本语言
        :type language: str
        """
        
        

        self._text = None
        self._language = None
        self.discriminator = None

        self.text = text
        if language is not None:
            self.language = language

    @property
    def text(self):
        r"""Gets the text of this TextDetectionDataReq.

        待检测文本，编码格式为“utf-8”，限定2000个字符以内，文本长度超过10000个字符时，只检测前10000个字符。

        :return: The text of this TextDetectionDataReq.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this TextDetectionDataReq.

        待检测文本，编码格式为“utf-8”，限定2000个字符以内，文本长度超过10000个字符时，只检测前10000个字符。

        :param text: The text of this TextDetectionDataReq.
        :type text: str
        """
        self._text = text

    @property
    def language(self):
        r"""Gets the language of this TextDetectionDataReq.

        支持检测的文本语言

        :return: The language of this TextDetectionDataReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this TextDetectionDataReq.

        支持检测的文本语言

        :param language: The language of this TextDetectionDataReq.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, TextDetectionDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
