# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LangResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'is_en': 'bool'
    }

    attribute_map = {
        'language': 'language',
        'is_en': 'is_en'
    }

    def __init__(self, language=None, is_en=None):
        """LangResult

        The model defined in huaweicloud sdk

        :param language: 语言
        :type language: str
        :param is_en: 是否英语
        :type is_en: bool
        """
        
        

        self._language = None
        self._is_en = None
        self.discriminator = None

        if language is not None:
            self.language = language
        if is_en is not None:
            self.is_en = is_en

    @property
    def language(self):
        """Gets the language of this LangResult.

        语言

        :return: The language of this LangResult.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this LangResult.

        语言

        :param language: The language of this LangResult.
        :type language: str
        """
        self._language = language

    @property
    def is_en(self):
        """Gets the is_en of this LangResult.

        是否英语

        :return: The is_en of this LangResult.
        :rtype: bool
        """
        return self._is_en

    @is_en.setter
    def is_en(self, is_en):
        """Sets the is_en of this LangResult.

        是否英语

        :param is_en: The is_en of this LangResult.
        :type is_en: bool
        """
        self._is_en = is_en

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
        if not isinstance(other, LangResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
