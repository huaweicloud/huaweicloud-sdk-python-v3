# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeywordExtractReq:

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
        'limit': 'int',
        'lang': 'str'
    }

    attribute_map = {
        'text': 'text',
        'limit': 'limit',
        'lang': 'lang'
    }

    def __init__(self, text=None, limit=None, lang=None):
        r"""KeywordExtractReq

        The model defined in huaweicloud sdk

        :param text: 待分析文本，长度为1~512，文本编码为UTF-8。
        :type text: str
        :param limit: 返回关键词的最大数量，默认为5。
        :type limit: int
        :param lang: 支持的文本语言类型，目前只支持中文，默认为zh。
        :type lang: str
        """
        
        

        self._text = None
        self._limit = None
        self._lang = None
        self.discriminator = None

        self.text = text
        if limit is not None:
            self.limit = limit
        if lang is not None:
            self.lang = lang

    @property
    def text(self):
        r"""Gets the text of this KeywordExtractReq.

        待分析文本，长度为1~512，文本编码为UTF-8。

        :return: The text of this KeywordExtractReq.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this KeywordExtractReq.

        待分析文本，长度为1~512，文本编码为UTF-8。

        :param text: The text of this KeywordExtractReq.
        :type text: str
        """
        self._text = text

    @property
    def limit(self):
        r"""Gets the limit of this KeywordExtractReq.

        返回关键词的最大数量，默认为5。

        :return: The limit of this KeywordExtractReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this KeywordExtractReq.

        返回关键词的最大数量，默认为5。

        :param limit: The limit of this KeywordExtractReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def lang(self):
        r"""Gets the lang of this KeywordExtractReq.

        支持的文本语言类型，目前只支持中文，默认为zh。

        :return: The lang of this KeywordExtractReq.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        r"""Sets the lang of this KeywordExtractReq.

        支持的文本语言类型，目前只支持中文，默认为zh。

        :param lang: The lang of this KeywordExtractReq.
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
        if not isinstance(other, KeywordExtractReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
