# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QaBotAnswer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'qa_pair_id': 'str',
        'st_question': 'str',
        'answer': 'str',
        'score': 'float',
        'domain': 'str',
        'top_score_question': 'str'
    }

    attribute_map = {
        'qa_pair_id': 'qa_pair_id',
        'st_question': 'st_question',
        'answer': 'answer',
        'score': 'score',
        'domain': 'domain',
        'top_score_question': 'top_score_question'
    }

    def __init__(self, qa_pair_id=None, st_question=None, answer=None, score=None, domain=None, top_score_question=None):
        r"""QaBotAnswer

        The model defined in huaweicloud sdk

        :param qa_pair_id: 问答对ID。
        :type qa_pair_id: str
        :param st_question: 标准问题。
        :type st_question: str
        :param answer: 知识库答案，包含该字段的回答为直接回答，未包含该字段的是推荐回答。
        :type answer: str
        :param score: 相似度得分，精确到小数点后3位。
        :type score: float
        :param domain: 所属领域。
        :type domain: str
        :param top_score_question: 最高评分的扩展问或标准问，当关闭内部阈值处理时返回。
        :type top_score_question: str
        """
        
        

        self._qa_pair_id = None
        self._st_question = None
        self._answer = None
        self._score = None
        self._domain = None
        self._top_score_question = None
        self.discriminator = None

        if qa_pair_id is not None:
            self.qa_pair_id = qa_pair_id
        if st_question is not None:
            self.st_question = st_question
        if answer is not None:
            self.answer = answer
        if score is not None:
            self.score = score
        if domain is not None:
            self.domain = domain
        if top_score_question is not None:
            self.top_score_question = top_score_question

    @property
    def qa_pair_id(self):
        r"""Gets the qa_pair_id of this QaBotAnswer.

        问答对ID。

        :return: The qa_pair_id of this QaBotAnswer.
        :rtype: str
        """
        return self._qa_pair_id

    @qa_pair_id.setter
    def qa_pair_id(self, qa_pair_id):
        r"""Sets the qa_pair_id of this QaBotAnswer.

        问答对ID。

        :param qa_pair_id: The qa_pair_id of this QaBotAnswer.
        :type qa_pair_id: str
        """
        self._qa_pair_id = qa_pair_id

    @property
    def st_question(self):
        r"""Gets the st_question of this QaBotAnswer.

        标准问题。

        :return: The st_question of this QaBotAnswer.
        :rtype: str
        """
        return self._st_question

    @st_question.setter
    def st_question(self, st_question):
        r"""Sets the st_question of this QaBotAnswer.

        标准问题。

        :param st_question: The st_question of this QaBotAnswer.
        :type st_question: str
        """
        self._st_question = st_question

    @property
    def answer(self):
        r"""Gets the answer of this QaBotAnswer.

        知识库答案，包含该字段的回答为直接回答，未包含该字段的是推荐回答。

        :return: The answer of this QaBotAnswer.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        r"""Sets the answer of this QaBotAnswer.

        知识库答案，包含该字段的回答为直接回答，未包含该字段的是推荐回答。

        :param answer: The answer of this QaBotAnswer.
        :type answer: str
        """
        self._answer = answer

    @property
    def score(self):
        r"""Gets the score of this QaBotAnswer.

        相似度得分，精确到小数点后3位。

        :return: The score of this QaBotAnswer.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this QaBotAnswer.

        相似度得分，精确到小数点后3位。

        :param score: The score of this QaBotAnswer.
        :type score: float
        """
        self._score = score

    @property
    def domain(self):
        r"""Gets the domain of this QaBotAnswer.

        所属领域。

        :return: The domain of this QaBotAnswer.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this QaBotAnswer.

        所属领域。

        :param domain: The domain of this QaBotAnswer.
        :type domain: str
        """
        self._domain = domain

    @property
    def top_score_question(self):
        r"""Gets the top_score_question of this QaBotAnswer.

        最高评分的扩展问或标准问，当关闭内部阈值处理时返回。

        :return: The top_score_question of this QaBotAnswer.
        :rtype: str
        """
        return self._top_score_question

    @top_score_question.setter
    def top_score_question(self, top_score_question):
        r"""Sets the top_score_question of this QaBotAnswer.

        最高评分的扩展问或标准问，当关闭内部阈值处理时返回。

        :param top_score_question: The top_score_question of this QaBotAnswer.
        :type top_score_question: str
        """
        self._top_score_question = top_score_question

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
        if not isinstance(other, QaBotAnswer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
