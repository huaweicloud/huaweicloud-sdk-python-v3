# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKnowledgeLibraryReq:

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
        'language': 'str',
        'knowledge_type': 'str',
        'topk': 'int',
        'score': 'float'
    }

    attribute_map = {
        'name': 'name',
        'language': 'language',
        'knowledge_type': 'knowledge_type',
        'topk': 'topk',
        'score': 'score'
    }

    def __init__(self, name=None, language=None, knowledge_type=None, topk=None, score=None):
        r"""CreateKnowledgeLibraryReq

        The model defined in huaweicloud sdk

        :param name: 知识库名称。
        :type name: str
        :param language: 智能交互语言 * CN：中文 * EN：英文
        :type language: str
        :param knowledge_type: 知识库类型 * QUESTION_ANSWER：问答 * DOCUMENT：文档
        :type knowledge_type: str
        :param topk: 知识库召回数
        :type topk: int
        :param score: 知识库召回得分
        :type score: float
        """
        
        

        self._name = None
        self._language = None
        self._knowledge_type = None
        self._topk = None
        self._score = None
        self.discriminator = None

        self.name = name
        self.language = language
        self.knowledge_type = knowledge_type
        if topk is not None:
            self.topk = topk
        if score is not None:
            self.score = score

    @property
    def name(self):
        r"""Gets the name of this CreateKnowledgeLibraryReq.

        知识库名称。

        :return: The name of this CreateKnowledgeLibraryReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateKnowledgeLibraryReq.

        知识库名称。

        :param name: The name of this CreateKnowledgeLibraryReq.
        :type name: str
        """
        self._name = name

    @property
    def language(self):
        r"""Gets the language of this CreateKnowledgeLibraryReq.

        智能交互语言 * CN：中文 * EN：英文

        :return: The language of this CreateKnowledgeLibraryReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this CreateKnowledgeLibraryReq.

        智能交互语言 * CN：中文 * EN：英文

        :param language: The language of this CreateKnowledgeLibraryReq.
        :type language: str
        """
        self._language = language

    @property
    def knowledge_type(self):
        r"""Gets the knowledge_type of this CreateKnowledgeLibraryReq.

        知识库类型 * QUESTION_ANSWER：问答 * DOCUMENT：文档

        :return: The knowledge_type of this CreateKnowledgeLibraryReq.
        :rtype: str
        """
        return self._knowledge_type

    @knowledge_type.setter
    def knowledge_type(self, knowledge_type):
        r"""Sets the knowledge_type of this CreateKnowledgeLibraryReq.

        知识库类型 * QUESTION_ANSWER：问答 * DOCUMENT：文档

        :param knowledge_type: The knowledge_type of this CreateKnowledgeLibraryReq.
        :type knowledge_type: str
        """
        self._knowledge_type = knowledge_type

    @property
    def topk(self):
        r"""Gets the topk of this CreateKnowledgeLibraryReq.

        知识库召回数

        :return: The topk of this CreateKnowledgeLibraryReq.
        :rtype: int
        """
        return self._topk

    @topk.setter
    def topk(self, topk):
        r"""Sets the topk of this CreateKnowledgeLibraryReq.

        知识库召回数

        :param topk: The topk of this CreateKnowledgeLibraryReq.
        :type topk: int
        """
        self._topk = topk

    @property
    def score(self):
        r"""Gets the score of this CreateKnowledgeLibraryReq.

        知识库召回得分

        :return: The score of this CreateKnowledgeLibraryReq.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this CreateKnowledgeLibraryReq.

        知识库召回得分

        :param score: The score of this CreateKnowledgeLibraryReq.
        :type score: float
        """
        self._score = score

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateKnowledgeLibraryReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
