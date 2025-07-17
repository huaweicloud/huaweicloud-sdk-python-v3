# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAsrVocabularyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vocabulary_type': 'AsrVocabularyTypeEnum',
        'name': 'str',
        'language': 'LanguageEnum',
        'mobvoi_vocabulary': 'MobvoiVocabulary'
    }

    attribute_map = {
        'vocabulary_type': 'vocabulary_type',
        'name': 'name',
        'language': 'language',
        'mobvoi_vocabulary': 'mobvoi_vocabulary'
    }

    def __init__(self, vocabulary_type=None, name=None, language=None, mobvoi_vocabulary=None):
        r"""CreateAsrVocabularyReq

        The model defined in huaweicloud sdk

        :param vocabulary_type: 
        :type vocabulary_type: :class:`huaweicloudsdkmetastudio.v1.AsrVocabularyTypeEnum`
        :param name: 奇妙问热词表名
        :type name: str
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param mobvoi_vocabulary: 
        :type mobvoi_vocabulary: :class:`huaweicloudsdkmetastudio.v1.MobvoiVocabulary`
        """
        
        

        self._vocabulary_type = None
        self._name = None
        self._language = None
        self._mobvoi_vocabulary = None
        self.discriminator = None

        self.vocabulary_type = vocabulary_type
        self.name = name
        self.language = language
        if mobvoi_vocabulary is not None:
            self.mobvoi_vocabulary = mobvoi_vocabulary

    @property
    def vocabulary_type(self):
        r"""Gets the vocabulary_type of this CreateAsrVocabularyReq.

        :return: The vocabulary_type of this CreateAsrVocabularyReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AsrVocabularyTypeEnum`
        """
        return self._vocabulary_type

    @vocabulary_type.setter
    def vocabulary_type(self, vocabulary_type):
        r"""Sets the vocabulary_type of this CreateAsrVocabularyReq.

        :param vocabulary_type: The vocabulary_type of this CreateAsrVocabularyReq.
        :type vocabulary_type: :class:`huaweicloudsdkmetastudio.v1.AsrVocabularyTypeEnum`
        """
        self._vocabulary_type = vocabulary_type

    @property
    def name(self):
        r"""Gets the name of this CreateAsrVocabularyReq.

        奇妙问热词表名

        :return: The name of this CreateAsrVocabularyReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateAsrVocabularyReq.

        奇妙问热词表名

        :param name: The name of this CreateAsrVocabularyReq.
        :type name: str
        """
        self._name = name

    @property
    def language(self):
        r"""Gets the language of this CreateAsrVocabularyReq.

        :return: The language of this CreateAsrVocabularyReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this CreateAsrVocabularyReq.

        :param language: The language of this CreateAsrVocabularyReq.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def mobvoi_vocabulary(self):
        r"""Gets the mobvoi_vocabulary of this CreateAsrVocabularyReq.

        :return: The mobvoi_vocabulary of this CreateAsrVocabularyReq.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.MobvoiVocabulary`
        """
        return self._mobvoi_vocabulary

    @mobvoi_vocabulary.setter
    def mobvoi_vocabulary(self, mobvoi_vocabulary):
        r"""Sets the mobvoi_vocabulary of this CreateAsrVocabularyReq.

        :param mobvoi_vocabulary: The mobvoi_vocabulary of this CreateAsrVocabularyReq.
        :type mobvoi_vocabulary: :class:`huaweicloudsdkmetastudio.v1.MobvoiVocabulary`
        """
        self._mobvoi_vocabulary = mobvoi_vocabulary

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
        if not isinstance(other, CreateAsrVocabularyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
