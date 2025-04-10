# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioInputBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'language': 'str'
    }

    attribute_map = {
        'url': 'url',
        'language': 'language'
    }

    def __init__(self, url=None, language=None):
        r"""AudioInputBody

        The model defined in huaweicloud sdk

        :param url: 音频url地址。
        :type url: str
        :param language: 支持的语言，默认为zh，zh：中文
        :type language: str
        """
        
        

        self._url = None
        self._language = None
        self.discriminator = None

        self.url = url
        if language is not None:
            self.language = language

    @property
    def url(self):
        r"""Gets the url of this AudioInputBody.

        音频url地址。

        :return: The url of this AudioInputBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this AudioInputBody.

        音频url地址。

        :param url: The url of this AudioInputBody.
        :type url: str
        """
        self._url = url

    @property
    def language(self):
        r"""Gets the language of this AudioInputBody.

        支持的语言，默认为zh，zh：中文

        :return: The language of this AudioInputBody.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this AudioInputBody.

        支持的语言，默认为zh，zh：中文

        :param language: The language of this AudioInputBody.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, AudioInputBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
