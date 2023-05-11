# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostDomainNerRequest:

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
        'lang': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'text': 'text',
        'lang': 'lang',
        'domain': 'domain'
    }

    def __init__(self, text=None, lang=None, domain=None):
        """PostDomainNerRequest

        The model defined in huaweicloud sdk

        :param text: 待分析文本，长度为1~512，文本编码为UTF-8。
        :type text: str
        :param lang: 支持的文本语言类型，目前只支持中文，默认为zh。
        :type lang: str
        :param domain: 支持的领域类型，目前支持通用（general）领域、商务（business）领域、娱乐（entertainment）领域，默认为general。
        :type domain: str
        """
        
        

        self._text = None
        self._lang = None
        self._domain = None
        self.discriminator = None

        self.text = text
        if lang is not None:
            self.lang = lang
        if domain is not None:
            self.domain = domain

    @property
    def text(self):
        """Gets the text of this PostDomainNerRequest.

        待分析文本，长度为1~512，文本编码为UTF-8。

        :return: The text of this PostDomainNerRequest.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PostDomainNerRequest.

        待分析文本，长度为1~512，文本编码为UTF-8。

        :param text: The text of this PostDomainNerRequest.
        :type text: str
        """
        self._text = text

    @property
    def lang(self):
        """Gets the lang of this PostDomainNerRequest.

        支持的文本语言类型，目前只支持中文，默认为zh。

        :return: The lang of this PostDomainNerRequest.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this PostDomainNerRequest.

        支持的文本语言类型，目前只支持中文，默认为zh。

        :param lang: The lang of this PostDomainNerRequest.
        :type lang: str
        """
        self._lang = lang

    @property
    def domain(self):
        """Gets the domain of this PostDomainNerRequest.

        支持的领域类型，目前支持通用（general）领域、商务（business）领域、娱乐（entertainment）领域，默认为general。

        :return: The domain of this PostDomainNerRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this PostDomainNerRequest.

        支持的领域类型，目前支持通用（general）领域、商务（business）领域、娱乐（entertainment）领域，默认为general。

        :param domain: The domain of this PostDomainNerRequest.
        :type domain: str
        """
        self._domain = domain

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
        if not isinstance(other, PostDomainNerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
