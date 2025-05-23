# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VocabInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vocabulary_id': 'str',
        'name': 'str',
        'language': 'str',
        'description': 'str'
    }

    attribute_map = {
        'vocabulary_id': 'vocabulary_id',
        'name': 'name',
        'language': 'language',
        'description': 'description'
    }

    def __init__(self, vocabulary_id=None, name=None, language=None, description=None):
        r"""VocabInfo

        The model defined in huaweicloud sdk

        :param vocabulary_id: 热词表ID。
        :type vocabulary_id: str
        :param name: 热词表名。
        :type name: str
        :param language: 热词表语言类型。
        :type language: str
        :param description: 热词表描述。
        :type description: str
        """
        
        

        self._vocabulary_id = None
        self._name = None
        self._language = None
        self._description = None
        self.discriminator = None

        self.vocabulary_id = vocabulary_id
        self.name = name
        self.language = language
        self.description = description

    @property
    def vocabulary_id(self):
        r"""Gets the vocabulary_id of this VocabInfo.

        热词表ID。

        :return: The vocabulary_id of this VocabInfo.
        :rtype: str
        """
        return self._vocabulary_id

    @vocabulary_id.setter
    def vocabulary_id(self, vocabulary_id):
        r"""Sets the vocabulary_id of this VocabInfo.

        热词表ID。

        :param vocabulary_id: The vocabulary_id of this VocabInfo.
        :type vocabulary_id: str
        """
        self._vocabulary_id = vocabulary_id

    @property
    def name(self):
        r"""Gets the name of this VocabInfo.

        热词表名。

        :return: The name of this VocabInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VocabInfo.

        热词表名。

        :param name: The name of this VocabInfo.
        :type name: str
        """
        self._name = name

    @property
    def language(self):
        r"""Gets the language of this VocabInfo.

        热词表语言类型。

        :return: The language of this VocabInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this VocabInfo.

        热词表语言类型。

        :param language: The language of this VocabInfo.
        :type language: str
        """
        self._language = language

    @property
    def description(self):
        r"""Gets the description of this VocabInfo.

        热词表描述。

        :return: The description of this VocabInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VocabInfo.

        热词表描述。

        :param description: The description of this VocabInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, VocabInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
