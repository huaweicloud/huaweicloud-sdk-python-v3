# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NerRequest:

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
        'lang': 'str'
    }

    attribute_map = {
        'text': 'text',
        'lang': 'lang'
    }

    def __init__(self, text=None, lang=None):
        """NerRequest

        The model defined in huaweicloud sdk

        :param text: 待分析文本，中文长度为1~512，英文和西班牙文长度为1~2000，文本编码为UTF-8。
        :type text: str
        :param lang: 支持的文本语言类型，目前支持中文（zh）,英文（en）,和西班牙文（es），默认为中文。
        :type lang: str
        """
        
        

        self._text = None
        self._lang = None
        self.discriminator = None

        self.text = text
        if lang is not None:
            self.lang = lang

    @property
    def text(self):
        """Gets the text of this NerRequest.

        待分析文本，中文长度为1~512，英文和西班牙文长度为1~2000，文本编码为UTF-8。

        :return: The text of this NerRequest.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this NerRequest.

        待分析文本，中文长度为1~512，英文和西班牙文长度为1~2000，文本编码为UTF-8。

        :param text: The text of this NerRequest.
        :type text: str
        """
        self._text = text

    @property
    def lang(self):
        """Gets the lang of this NerRequest.

        支持的文本语言类型，目前支持中文（zh）,英文（en）,和西班牙文（es），默认为中文。

        :return: The lang of this NerRequest.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this NerRequest.

        支持的文本语言类型，目前支持中文（zh）,英文（en）,和西班牙文（es），默认为中文。

        :param lang: The lang of this NerRequest.
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
        if not isinstance(other, NerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
