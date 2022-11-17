# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SummaryReq:

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
        'lang': 'str',
        'length_limit': 'float',
        'title': 'str'
    }

    attribute_map = {
        'content': 'content',
        'lang': 'lang',
        'length_limit': 'length_limit',
        'title': 'title'
    }

    def __init__(self, content=None, lang=None, length_limit=None, title=None):
        """SummaryReq

        The model defined in huaweicloud sdk

        :param content: 文本正文（目前仅支持UTF-8编码），长度不超过10000字。
        :type content: str
        :param lang: 支持的文本语言类型，目前支持中文（zh）和英文（en），默认为中文。
        :type lang: str
        :param length_limit: 生成摘要的长度限制。length_limit &gt; 1，则返回结果为字数不小于该值且最接近该值的摘要。 0 &lt;&#x3D; length_limit &lt;&#x3D; 1，则返回结果为长度百分比不小于该值且最接近该值的摘要。 默认数值为0.3。
        :type length_limit: float
        :param title: 文本标题（目前仅支持UTF-8编码），长度不超过1000字。
        :type title: str
        """
        
        

        self._content = None
        self._lang = None
        self._length_limit = None
        self._title = None
        self.discriminator = None

        self.content = content
        if lang is not None:
            self.lang = lang
        if length_limit is not None:
            self.length_limit = length_limit
        if title is not None:
            self.title = title

    @property
    def content(self):
        """Gets the content of this SummaryReq.

        文本正文（目前仅支持UTF-8编码），长度不超过10000字。

        :return: The content of this SummaryReq.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this SummaryReq.

        文本正文（目前仅支持UTF-8编码），长度不超过10000字。

        :param content: The content of this SummaryReq.
        :type content: str
        """
        self._content = content

    @property
    def lang(self):
        """Gets the lang of this SummaryReq.

        支持的文本语言类型，目前支持中文（zh）和英文（en），默认为中文。

        :return: The lang of this SummaryReq.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this SummaryReq.

        支持的文本语言类型，目前支持中文（zh）和英文（en），默认为中文。

        :param lang: The lang of this SummaryReq.
        :type lang: str
        """
        self._lang = lang

    @property
    def length_limit(self):
        """Gets the length_limit of this SummaryReq.

        生成摘要的长度限制。length_limit > 1，则返回结果为字数不小于该值且最接近该值的摘要。 0 <= length_limit <= 1，则返回结果为长度百分比不小于该值且最接近该值的摘要。 默认数值为0.3。

        :return: The length_limit of this SummaryReq.
        :rtype: float
        """
        return self._length_limit

    @length_limit.setter
    def length_limit(self, length_limit):
        """Sets the length_limit of this SummaryReq.

        生成摘要的长度限制。length_limit > 1，则返回结果为字数不小于该值且最接近该值的摘要。 0 <= length_limit <= 1，则返回结果为长度百分比不小于该值且最接近该值的摘要。 默认数值为0.3。

        :param length_limit: The length_limit of this SummaryReq.
        :type length_limit: float
        """
        self._length_limit = length_limit

    @property
    def title(self):
        """Gets the title of this SummaryReq.

        文本标题（目前仅支持UTF-8编码），长度不超过1000字。

        :return: The title of this SummaryReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this SummaryReq.

        文本标题（目前仅支持UTF-8编码），长度不超过1000字。

        :param title: The title of this SummaryReq.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, SummaryReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
