# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConstituencyParserReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'lang': 'str',
        'text': 'str'
    }

    attribute_map = {
        'lang': 'lang',
        'text': 'text'
    }

    def __init__(self, lang=None, text=None):
        """ConstituencyParserReq

        The model defined in huaweicloud sdk

        :param lang: 支持的文本语言类型，目前支持中文（zh）。
        :type lang: str
        :param text: 待分析文本，长度为1~32。
        :type text: str
        """
        
        

        self._lang = None
        self._text = None
        self.discriminator = None

        if lang is not None:
            self.lang = lang
        self.text = text

    @property
    def lang(self):
        """Gets the lang of this ConstituencyParserReq.

        支持的文本语言类型，目前支持中文（zh）。

        :return: The lang of this ConstituencyParserReq.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this ConstituencyParserReq.

        支持的文本语言类型，目前支持中文（zh）。

        :param lang: The lang of this ConstituencyParserReq.
        :type lang: str
        """
        self._lang = lang

    @property
    def text(self):
        """Gets the text of this ConstituencyParserReq.

        待分析文本，长度为1~32。

        :return: The text of this ConstituencyParserReq.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ConstituencyParserReq.

        待分析文本，长度为1~32。

        :param text: The text of this ConstituencyParserReq.
        :type text: str
        """
        self._text = text

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
        if not isinstance(other, ConstituencyParserReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
