# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TextSimilarityAdvanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text1': 'str',
        'text2': 'str',
        'lang': 'str'
    }

    attribute_map = {
        'text1': 'text1',
        'text2': 'text2',
        'lang': 'lang'
    }

    def __init__(self, text1=None, text2=None, lang=None):
        """TextSimilarityAdvanceRequest

        The model defined in huaweicloud sdk

        :param text1: 待计算文本1，长度1~512，文本编码为UTF-8。
        :type text1: str
        :param text2: 待计算文本1，长度1~512，文本编码为UTF-8。
        :type text2: str
        :param lang: 支持的文本语言类型，目前只支持中文（zh），默认为中文。
        :type lang: str
        """
        
        

        self._text1 = None
        self._text2 = None
        self._lang = None
        self.discriminator = None

        self.text1 = text1
        self.text2 = text2
        if lang is not None:
            self.lang = lang

    @property
    def text1(self):
        """Gets the text1 of this TextSimilarityAdvanceRequest.

        待计算文本1，长度1~512，文本编码为UTF-8。

        :return: The text1 of this TextSimilarityAdvanceRequest.
        :rtype: str
        """
        return self._text1

    @text1.setter
    def text1(self, text1):
        """Sets the text1 of this TextSimilarityAdvanceRequest.

        待计算文本1，长度1~512，文本编码为UTF-8。

        :param text1: The text1 of this TextSimilarityAdvanceRequest.
        :type text1: str
        """
        self._text1 = text1

    @property
    def text2(self):
        """Gets the text2 of this TextSimilarityAdvanceRequest.

        待计算文本1，长度1~512，文本编码为UTF-8。

        :return: The text2 of this TextSimilarityAdvanceRequest.
        :rtype: str
        """
        return self._text2

    @text2.setter
    def text2(self, text2):
        """Sets the text2 of this TextSimilarityAdvanceRequest.

        待计算文本1，长度1~512，文本编码为UTF-8。

        :param text2: The text2 of this TextSimilarityAdvanceRequest.
        :type text2: str
        """
        self._text2 = text2

    @property
    def lang(self):
        """Gets the lang of this TextSimilarityAdvanceRequest.

        支持的文本语言类型，目前只支持中文（zh），默认为中文。

        :return: The lang of this TextSimilarityAdvanceRequest.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this TextSimilarityAdvanceRequest.

        支持的文本语言类型，目前只支持中文（zh），默认为中文。

        :param lang: The lang of this TextSimilarityAdvanceRequest.
        :type lang: str
        """
        self._lang = lang

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
        if not isinstance(other, TextSimilarityAdvanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
