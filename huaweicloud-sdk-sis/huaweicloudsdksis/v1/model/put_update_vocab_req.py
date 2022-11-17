# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutUpdateVocabReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'language': 'str',
        'contents': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'language': 'language',
        'contents': 'contents'
    }

    def __init__(self, name=None, description=None, language=None, contents=None):
        """PutUpdateVocabReq

        The model defined in huaweicloud sdk

        :param name: 热词表名，不可重复。内容限制为字母，数字，下中划线和井号，长度不超过32字节。
        :type name: str
        :param description: 热词表描述，长度不超过255字节。
        :type description: str
        :param language: 热词表语言类型。 language取值范围： chinese_mandarin  汉语普通话
        :type language: str
        :param contents: 支持中英混编热词，单个热词只能由英文字母和unicode编码的汉字组成，不能有其他符号，包括空格。  单词库支持热词数上限1024。 单个热词长度上限32字节。
        :type contents: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._language = None
        self._contents = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.language = language
        self.contents = contents

    @property
    def name(self):
        """Gets the name of this PutUpdateVocabReq.

        热词表名，不可重复。内容限制为字母，数字，下中划线和井号，长度不超过32字节。

        :return: The name of this PutUpdateVocabReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PutUpdateVocabReq.

        热词表名，不可重复。内容限制为字母，数字，下中划线和井号，长度不超过32字节。

        :param name: The name of this PutUpdateVocabReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PutUpdateVocabReq.

        热词表描述，长度不超过255字节。

        :return: The description of this PutUpdateVocabReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutUpdateVocabReq.

        热词表描述，长度不超过255字节。

        :param description: The description of this PutUpdateVocabReq.
        :type description: str
        """
        self._description = description

    @property
    def language(self):
        """Gets the language of this PutUpdateVocabReq.

        热词表语言类型。 language取值范围： chinese_mandarin  汉语普通话

        :return: The language of this PutUpdateVocabReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PutUpdateVocabReq.

        热词表语言类型。 language取值范围： chinese_mandarin  汉语普通话

        :param language: The language of this PutUpdateVocabReq.
        :type language: str
        """
        self._language = language

    @property
    def contents(self):
        """Gets the contents of this PutUpdateVocabReq.

        支持中英混编热词，单个热词只能由英文字母和unicode编码的汉字组成，不能有其他符号，包括空格。  单词库支持热词数上限1024。 单个热词长度上限32字节。

        :return: The contents of this PutUpdateVocabReq.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this PutUpdateVocabReq.

        支持中英混编热词，单个热词只能由英文字母和unicode编码的汉字组成，不能有其他符号，包括空格。  单词库支持热词数上限1024。 单个热词长度上限32字节。

        :param contents: The contents of this PutUpdateVocabReq.
        :type contents: list[str]
        """
        self._contents = contents

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
        if not isinstance(other, PutUpdateVocabReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
