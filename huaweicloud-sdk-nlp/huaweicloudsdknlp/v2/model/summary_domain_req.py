# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SummaryDomainReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'length_limit': 'float',
        'title': 'str',
        'lang': 'str',
        'content': 'str',
        'type': 'int'
    }

    attribute_map = {
        'length_limit': 'length_limit',
        'title': 'title',
        'lang': 'lang',
        'content': 'content',
        'type': 'type'
    }

    def __init__(self, length_limit=None, title=None, lang=None, content=None, type=None):
        r"""SummaryDomainReq

        The model defined in huaweicloud sdk

        :param length_limit: 生成摘要的长度限制。length_limit &gt; 1，则返回结果为字数不小于该值且最接近该值的摘要。 0 &lt;&#x3D; length_limit &lt;&#x3D; 1，则返回结果为长度百分比不小于该值且最接近该值的摘要。
        :type length_limit: float
        :param title: 文本标题（目前仅支持UTF-8编码），长度不超过1000字。
        :type title: str
        :param lang: 支持的文本语言类型，目前支持中文（zh）。
        :type lang: str
        :param content: 文本正文（目前仅支持UTF-8编码），长度不超过10000字。
        :type content: str
        :param type: 支持的领域类型，取值如下（目前只支持通用领域），默认为通用领域： 0：通用领域
        :type type: int
        """
        
        

        self._length_limit = None
        self._title = None
        self._lang = None
        self._content = None
        self._type = None
        self.discriminator = None

        if length_limit is not None:
            self.length_limit = length_limit
        if title is not None:
            self.title = title
        if lang is not None:
            self.lang = lang
        self.content = content
        if type is not None:
            self.type = type

    @property
    def length_limit(self):
        r"""Gets the length_limit of this SummaryDomainReq.

        生成摘要的长度限制。length_limit > 1，则返回结果为字数不小于该值且最接近该值的摘要。 0 <= length_limit <= 1，则返回结果为长度百分比不小于该值且最接近该值的摘要。

        :return: The length_limit of this SummaryDomainReq.
        :rtype: float
        """
        return self._length_limit

    @length_limit.setter
    def length_limit(self, length_limit):
        r"""Sets the length_limit of this SummaryDomainReq.

        生成摘要的长度限制。length_limit > 1，则返回结果为字数不小于该值且最接近该值的摘要。 0 <= length_limit <= 1，则返回结果为长度百分比不小于该值且最接近该值的摘要。

        :param length_limit: The length_limit of this SummaryDomainReq.
        :type length_limit: float
        """
        self._length_limit = length_limit

    @property
    def title(self):
        r"""Gets the title of this SummaryDomainReq.

        文本标题（目前仅支持UTF-8编码），长度不超过1000字。

        :return: The title of this SummaryDomainReq.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this SummaryDomainReq.

        文本标题（目前仅支持UTF-8编码），长度不超过1000字。

        :param title: The title of this SummaryDomainReq.
        :type title: str
        """
        self._title = title

    @property
    def lang(self):
        r"""Gets the lang of this SummaryDomainReq.

        支持的文本语言类型，目前支持中文（zh）。

        :return: The lang of this SummaryDomainReq.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        r"""Sets the lang of this SummaryDomainReq.

        支持的文本语言类型，目前支持中文（zh）。

        :param lang: The lang of this SummaryDomainReq.
        :type lang: str
        """
        self._lang = lang

    @property
    def content(self):
        r"""Gets the content of this SummaryDomainReq.

        文本正文（目前仅支持UTF-8编码），长度不超过10000字。

        :return: The content of this SummaryDomainReq.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this SummaryDomainReq.

        文本正文（目前仅支持UTF-8编码），长度不超过10000字。

        :param content: The content of this SummaryDomainReq.
        :type content: str
        """
        self._content = content

    @property
    def type(self):
        r"""Gets the type of this SummaryDomainReq.

        支持的领域类型，取值如下（目前只支持通用领域），默认为通用领域： 0：通用领域

        :return: The type of this SummaryDomainReq.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SummaryDomainReq.

        支持的领域类型，取值如下（目前只支持通用领域），默认为通用领域： 0：通用领域

        :param type: The type of this SummaryDomainReq.
        :type type: int
        """
        self._type = type

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
        if not isinstance(other, SummaryDomainReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
