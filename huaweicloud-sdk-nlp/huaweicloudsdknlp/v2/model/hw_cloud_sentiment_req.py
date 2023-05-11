# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HWCloudSentimentReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'lang': 'str'
    }

    attribute_map = {
        'content': 'content',
        'lang': 'lang'
    }

    def __init__(self, content=None, lang=None):
        """HWCloudSentimentReq

        The model defined in huaweicloud sdk

        :param content: 待分析文本。文本编码要求为utf-8。仅支持中文和英文情感分析。 限定180个字符以内，超过180个字符，只截取前180个字符。 
        :type content: str
        :param lang: 支持的文本语言类型，目前支持中文（zh）和英文（en），默认为中文。
        :type lang: str
        """
        
        

        self._content = None
        self._lang = None
        self.discriminator = None

        self.content = content
        if lang is not None:
            self.lang = lang

    @property
    def content(self):
        """Gets the content of this HWCloudSentimentReq.

        待分析文本。文本编码要求为utf-8。仅支持中文和英文情感分析。 限定180个字符以内，超过180个字符，只截取前180个字符。 

        :return: The content of this HWCloudSentimentReq.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this HWCloudSentimentReq.

        待分析文本。文本编码要求为utf-8。仅支持中文和英文情感分析。 限定180个字符以内，超过180个字符，只截取前180个字符。 

        :param content: The content of this HWCloudSentimentReq.
        :type content: str
        """
        self._content = content

    @property
    def lang(self):
        """Gets the lang of this HWCloudSentimentReq.

        支持的文本语言类型，目前支持中文（zh）和英文（en），默认为中文。

        :return: The lang of this HWCloudSentimentReq.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this HWCloudSentimentReq.

        支持的文本语言类型，目前支持中文（zh）和英文（en），默认为中文。

        :param lang: The lang of this HWCloudSentimentReq.
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
        if not isinstance(other, HWCloudSentimentReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
