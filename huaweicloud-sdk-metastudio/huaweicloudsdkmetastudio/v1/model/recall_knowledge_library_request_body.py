# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecallKnowledgeLibraryRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'knowledge_library_id': 'str',
        'knowledge_type': 'KnowledgeTypeEnum',
        'query': 'str',
        'topk': 'int',
        'score': 'float'
    }

    attribute_map = {
        'knowledge_library_id': 'knowledge_library_id',
        'knowledge_type': 'knowledge_type',
        'query': 'query',
        'topk': 'topk',
        'score': 'score'
    }

    def __init__(self, knowledge_library_id=None, knowledge_type=None, query=None, topk=None, score=None):
        r"""RecallKnowledgeLibraryRequestBody

        The model defined in huaweicloud sdk

        :param knowledge_library_id: 知识库名称。
        :type knowledge_library_id: str
        :param knowledge_type: 
        :type knowledge_type: :class:`huaweicloudsdkmetastudio.v1.KnowledgeTypeEnum`
        :param query: 知识库召回请求文本
        :type query: str
        :param topk: 文档库召回topk
        :type topk: int
        :param score: 知识库召回得分
        :type score: float
        """
        
        

        self._knowledge_library_id = None
        self._knowledge_type = None
        self._query = None
        self._topk = None
        self._score = None
        self.discriminator = None

        self.knowledge_library_id = knowledge_library_id
        self.knowledge_type = knowledge_type
        self.query = query
        if topk is not None:
            self.topk = topk
        if score is not None:
            self.score = score

    @property
    def knowledge_library_id(self):
        r"""Gets the knowledge_library_id of this RecallKnowledgeLibraryRequestBody.

        知识库名称。

        :return: The knowledge_library_id of this RecallKnowledgeLibraryRequestBody.
        :rtype: str
        """
        return self._knowledge_library_id

    @knowledge_library_id.setter
    def knowledge_library_id(self, knowledge_library_id):
        r"""Sets the knowledge_library_id of this RecallKnowledgeLibraryRequestBody.

        知识库名称。

        :param knowledge_library_id: The knowledge_library_id of this RecallKnowledgeLibraryRequestBody.
        :type knowledge_library_id: str
        """
        self._knowledge_library_id = knowledge_library_id

    @property
    def knowledge_type(self):
        r"""Gets the knowledge_type of this RecallKnowledgeLibraryRequestBody.

        :return: The knowledge_type of this RecallKnowledgeLibraryRequestBody.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.KnowledgeTypeEnum`
        """
        return self._knowledge_type

    @knowledge_type.setter
    def knowledge_type(self, knowledge_type):
        r"""Sets the knowledge_type of this RecallKnowledgeLibraryRequestBody.

        :param knowledge_type: The knowledge_type of this RecallKnowledgeLibraryRequestBody.
        :type knowledge_type: :class:`huaweicloudsdkmetastudio.v1.KnowledgeTypeEnum`
        """
        self._knowledge_type = knowledge_type

    @property
    def query(self):
        r"""Gets the query of this RecallKnowledgeLibraryRequestBody.

        知识库召回请求文本

        :return: The query of this RecallKnowledgeLibraryRequestBody.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this RecallKnowledgeLibraryRequestBody.

        知识库召回请求文本

        :param query: The query of this RecallKnowledgeLibraryRequestBody.
        :type query: str
        """
        self._query = query

    @property
    def topk(self):
        r"""Gets the topk of this RecallKnowledgeLibraryRequestBody.

        文档库召回topk

        :return: The topk of this RecallKnowledgeLibraryRequestBody.
        :rtype: int
        """
        return self._topk

    @topk.setter
    def topk(self, topk):
        r"""Sets the topk of this RecallKnowledgeLibraryRequestBody.

        文档库召回topk

        :param topk: The topk of this RecallKnowledgeLibraryRequestBody.
        :type topk: int
        """
        self._topk = topk

    @property
    def score(self):
        r"""Gets the score of this RecallKnowledgeLibraryRequestBody.

        知识库召回得分

        :return: The score of this RecallKnowledgeLibraryRequestBody.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this RecallKnowledgeLibraryRequestBody.

        知识库召回得分

        :param score: The score of this RecallKnowledgeLibraryRequestBody.
        :type score: float
        """
        self._score = score

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
        if not isinstance(other, RecallKnowledgeLibraryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
