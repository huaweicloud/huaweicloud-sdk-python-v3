# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyWordsStat:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keyword': 'str',
        'freq': 'int'
    }

    attribute_map = {
        'keyword': 'keyword',
        'freq': 'freq'
    }

    def __init__(self, keyword=None, freq=None):
        """KeyWordsStat

        The model defined in huaweicloud sdk

        :param keyword: 关键词。
        :type keyword: str
        :param freq: 关键词频次。
        :type freq: int
        """
        
        

        self._keyword = None
        self._freq = None
        self.discriminator = None

        self.keyword = keyword
        self.freq = freq

    @property
    def keyword(self):
        """Gets the keyword of this KeyWordsStat.

        关键词。

        :return: The keyword of this KeyWordsStat.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this KeyWordsStat.

        关键词。

        :param keyword: The keyword of this KeyWordsStat.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def freq(self):
        """Gets the freq of this KeyWordsStat.

        关键词频次。

        :return: The freq of this KeyWordsStat.
        :rtype: int
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """Sets the freq of this KeyWordsStat.

        关键词频次。

        :param freq: The freq of this KeyWordsStat.
        :type freq: int
        """
        self._freq = freq

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
        if not isinstance(other, KeyWordsStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
