# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstructionReplyWordsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'LanguageEnum',
        'reply_words': 'str'
    }

    attribute_map = {
        'language': 'language',
        'reply_words': 'reply_words'
    }

    def __init__(self, language=None, reply_words=None):
        r"""InstructionReplyWordsInfo

        The model defined in huaweicloud sdk

        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param reply_words: 回复话术，多个回复话术间用换行符\\n分隔。
        :type reply_words: str
        """
        
        

        self._language = None
        self._reply_words = None
        self.discriminator = None

        self.language = language
        self.reply_words = reply_words

    @property
    def language(self):
        r"""Gets the language of this InstructionReplyWordsInfo.

        :return: The language of this InstructionReplyWordsInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this InstructionReplyWordsInfo.

        :param language: The language of this InstructionReplyWordsInfo.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def reply_words(self):
        r"""Gets the reply_words of this InstructionReplyWordsInfo.

        回复话术，多个回复话术间用换行符\\n分隔。

        :return: The reply_words of this InstructionReplyWordsInfo.
        :rtype: str
        """
        return self._reply_words

    @reply_words.setter
    def reply_words(self, reply_words):
        r"""Sets the reply_words of this InstructionReplyWordsInfo.

        回复话术，多个回复话术间用换行符\\n分隔。

        :param reply_words: The reply_words of this InstructionReplyWordsInfo.
        :type reply_words: str
        """
        self._reply_words = reply_words

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
        if not isinstance(other, InstructionReplyWordsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
