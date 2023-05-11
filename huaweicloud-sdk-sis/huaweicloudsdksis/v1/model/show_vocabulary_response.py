# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVocabularyResponse(SdkResponse):

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
        'description': 'str',
        'language': 'str',
        'contents': 'list[str]'
    }

    attribute_map = {
        'vocabulary_id': 'vocabulary_id',
        'name': 'name',
        'description': 'description',
        'language': 'language',
        'contents': 'contents'
    }

    def __init__(self, vocabulary_id=None, name=None, description=None, language=None, contents=None):
        """ShowVocabularyResponse

        The model defined in huaweicloud sdk

        :param vocabulary_id: 调用成功返回热词表ID，调用失败时无此字段。
        :type vocabulary_id: str
        :param name: 调用成功返回热词表名，调用失败时无此字段。
        :type name: str
        :param description: 调用成功返回热词表描述，调用失败时无此字段。
        :type description: str
        :param language: 调用成功返回热词表语言类型，调用失败时无此字段。
        :type language: str
        :param contents: 调用成功返回热词列表，调用失败时无此字段。
        :type contents: list[str]
        """
        
        super(ShowVocabularyResponse, self).__init__()

        self._vocabulary_id = None
        self._name = None
        self._description = None
        self._language = None
        self._contents = None
        self.discriminator = None

        if vocabulary_id is not None:
            self.vocabulary_id = vocabulary_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if language is not None:
            self.language = language
        if contents is not None:
            self.contents = contents

    @property
    def vocabulary_id(self):
        """Gets the vocabulary_id of this ShowVocabularyResponse.

        调用成功返回热词表ID，调用失败时无此字段。

        :return: The vocabulary_id of this ShowVocabularyResponse.
        :rtype: str
        """
        return self._vocabulary_id

    @vocabulary_id.setter
    def vocabulary_id(self, vocabulary_id):
        """Sets the vocabulary_id of this ShowVocabularyResponse.

        调用成功返回热词表ID，调用失败时无此字段。

        :param vocabulary_id: The vocabulary_id of this ShowVocabularyResponse.
        :type vocabulary_id: str
        """
        self._vocabulary_id = vocabulary_id

    @property
    def name(self):
        """Gets the name of this ShowVocabularyResponse.

        调用成功返回热词表名，调用失败时无此字段。

        :return: The name of this ShowVocabularyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowVocabularyResponse.

        调用成功返回热词表名，调用失败时无此字段。

        :param name: The name of this ShowVocabularyResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowVocabularyResponse.

        调用成功返回热词表描述，调用失败时无此字段。

        :return: The description of this ShowVocabularyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowVocabularyResponse.

        调用成功返回热词表描述，调用失败时无此字段。

        :param description: The description of this ShowVocabularyResponse.
        :type description: str
        """
        self._description = description

    @property
    def language(self):
        """Gets the language of this ShowVocabularyResponse.

        调用成功返回热词表语言类型，调用失败时无此字段。

        :return: The language of this ShowVocabularyResponse.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ShowVocabularyResponse.

        调用成功返回热词表语言类型，调用失败时无此字段。

        :param language: The language of this ShowVocabularyResponse.
        :type language: str
        """
        self._language = language

    @property
    def contents(self):
        """Gets the contents of this ShowVocabularyResponse.

        调用成功返回热词列表，调用失败时无此字段。

        :return: The contents of this ShowVocabularyResponse.
        :rtype: list[str]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this ShowVocabularyResponse.

        调用成功返回热词列表，调用失败时无此字段。

        :param contents: The contents of this ShowVocabularyResponse.
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
        if not isinstance(other, ShowVocabularyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
