# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AsrVocabularyAssociation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'hot_words_id': 'str',
        'vocabulary_id': 'str',
        'robot_id': 'str',
        'language': 'LanguageEnum'
    }

    attribute_map = {
        'hot_words_id': 'hot_words_id',
        'vocabulary_id': 'vocabulary_id',
        'robot_id': 'robot_id',
        'language': 'language'
    }

    def __init__(self, hot_words_id=None, vocabulary_id=None, robot_id=None, language=None):
        r"""AsrVocabularyAssociation

        The model defined in huaweicloud sdk

        :param hot_words_id: 热词记录ID
        :type hot_words_id: str
        :param vocabulary_id: 热词表ID
        :type vocabulary_id: str
        :param robot_id: 应用ID。
        :type robot_id: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        
        

        self._hot_words_id = None
        self._vocabulary_id = None
        self._robot_id = None
        self._language = None
        self.discriminator = None

        if hot_words_id is not None:
            self.hot_words_id = hot_words_id
        if vocabulary_id is not None:
            self.vocabulary_id = vocabulary_id
        if robot_id is not None:
            self.robot_id = robot_id
        if language is not None:
            self.language = language

    @property
    def hot_words_id(self):
        r"""Gets the hot_words_id of this AsrVocabularyAssociation.

        热词记录ID

        :return: The hot_words_id of this AsrVocabularyAssociation.
        :rtype: str
        """
        return self._hot_words_id

    @hot_words_id.setter
    def hot_words_id(self, hot_words_id):
        r"""Sets the hot_words_id of this AsrVocabularyAssociation.

        热词记录ID

        :param hot_words_id: The hot_words_id of this AsrVocabularyAssociation.
        :type hot_words_id: str
        """
        self._hot_words_id = hot_words_id

    @property
    def vocabulary_id(self):
        r"""Gets the vocabulary_id of this AsrVocabularyAssociation.

        热词表ID

        :return: The vocabulary_id of this AsrVocabularyAssociation.
        :rtype: str
        """
        return self._vocabulary_id

    @vocabulary_id.setter
    def vocabulary_id(self, vocabulary_id):
        r"""Sets the vocabulary_id of this AsrVocabularyAssociation.

        热词表ID

        :param vocabulary_id: The vocabulary_id of this AsrVocabularyAssociation.
        :type vocabulary_id: str
        """
        self._vocabulary_id = vocabulary_id

    @property
    def robot_id(self):
        r"""Gets the robot_id of this AsrVocabularyAssociation.

        应用ID。

        :return: The robot_id of this AsrVocabularyAssociation.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this AsrVocabularyAssociation.

        应用ID。

        :param robot_id: The robot_id of this AsrVocabularyAssociation.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def language(self):
        r"""Gets the language of this AsrVocabularyAssociation.

        :return: The language of this AsrVocabularyAssociation.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this AsrVocabularyAssociation.

        :param language: The language of this AsrVocabularyAssociation.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
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
        if not isinstance(other, AsrVocabularyAssociation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
