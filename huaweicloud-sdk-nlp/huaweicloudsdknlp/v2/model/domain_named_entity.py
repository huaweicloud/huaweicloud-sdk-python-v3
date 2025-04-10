# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainNamedEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'word': 'str',
        'tag': 'str',
        'offset': 'int',
        'len': 'int'
    }

    attribute_map = {
        'word': 'word',
        'tag': 'tag',
        'offset': 'offset',
        'len': 'len'
    }

    def __init__(self, word=None, tag=None, offset=None, len=None):
        r"""DomainNamedEntity

        The model defined in huaweicloud sdk

        :param word: 实体文本。
        :type word: str
        :param tag: 实体类型，枚举类型。 通用领域：支持人名nr，地名ns，机构名nt，时间点tpt，日期day，百分比pct，货币额度mny，序数词ord，计量规格词qtt，民族race，职业job，邮箱email，国家coun，节日fest。 商务领域：支持公司名com、品牌名bra、职业job、职位post、邮箱email、手机号码cell、电话号码tele、IP地址ip、身份证号id、网址web。 娱乐领域：支持电影名mov、动漫anime、书名book、互联网int、歌名song、产品名pro、电视剧名dra、电视节目名tv。
        :type tag: str
        :param offset: 实体文本在待分析文本中的起始位置。
        :type offset: int
        :param len: 实体文本长度。
        :type len: int
        """
        
        

        self._word = None
        self._tag = None
        self._offset = None
        self._len = None
        self.discriminator = None

        self.word = word
        self.tag = tag
        self.offset = offset
        self.len = len

    @property
    def word(self):
        r"""Gets the word of this DomainNamedEntity.

        实体文本。

        :return: The word of this DomainNamedEntity.
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        r"""Sets the word of this DomainNamedEntity.

        实体文本。

        :param word: The word of this DomainNamedEntity.
        :type word: str
        """
        self._word = word

    @property
    def tag(self):
        r"""Gets the tag of this DomainNamedEntity.

        实体类型，枚举类型。 通用领域：支持人名nr，地名ns，机构名nt，时间点tpt，日期day，百分比pct，货币额度mny，序数词ord，计量规格词qtt，民族race，职业job，邮箱email，国家coun，节日fest。 商务领域：支持公司名com、品牌名bra、职业job、职位post、邮箱email、手机号码cell、电话号码tele、IP地址ip、身份证号id、网址web。 娱乐领域：支持电影名mov、动漫anime、书名book、互联网int、歌名song、产品名pro、电视剧名dra、电视节目名tv。

        :return: The tag of this DomainNamedEntity.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this DomainNamedEntity.

        实体类型，枚举类型。 通用领域：支持人名nr，地名ns，机构名nt，时间点tpt，日期day，百分比pct，货币额度mny，序数词ord，计量规格词qtt，民族race，职业job，邮箱email，国家coun，节日fest。 商务领域：支持公司名com、品牌名bra、职业job、职位post、邮箱email、手机号码cell、电话号码tele、IP地址ip、身份证号id、网址web。 娱乐领域：支持电影名mov、动漫anime、书名book、互联网int、歌名song、产品名pro、电视剧名dra、电视节目名tv。

        :param tag: The tag of this DomainNamedEntity.
        :type tag: str
        """
        self._tag = tag

    @property
    def offset(self):
        r"""Gets the offset of this DomainNamedEntity.

        实体文本在待分析文本中的起始位置。

        :return: The offset of this DomainNamedEntity.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this DomainNamedEntity.

        实体文本在待分析文本中的起始位置。

        :param offset: The offset of this DomainNamedEntity.
        :type offset: int
        """
        self._offset = offset

    @property
    def len(self):
        r"""Gets the len of this DomainNamedEntity.

        实体文本长度。

        :return: The len of this DomainNamedEntity.
        :rtype: int
        """
        return self._len

    @len.setter
    def len(self, len):
        r"""Sets the len of this DomainNamedEntity.

        实体文本长度。

        :param len: The len of this DomainNamedEntity.
        :type len: int
        """
        self._len = len

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
        if not isinstance(other, DomainNamedEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
