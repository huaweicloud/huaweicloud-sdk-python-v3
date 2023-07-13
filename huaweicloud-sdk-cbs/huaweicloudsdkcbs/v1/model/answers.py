# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Answers:

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
        'score': 'float',
        'domain': 'str',
        'answer': 'str',
        'ex_questions': 'list[ExQuestions]'
    }

    attribute_map = {
        'qa_pair_id': 'qa_pair_id',
        'st_question': 'st_question',
        'score': 'score',
        'domain': 'domain',
        'answer': 'answer',
        'ex_questions': 'ex_questions'
    }

    def __init__(self, qa_pair_id=None, st_question=None, score=None, domain=None, answer=None, ex_questions=None):
        """Answers

        The model defined in huaweicloud sdk

        :param qa_pair_id: Answers.
        :type qa_pair_id: str
        :param st_question: 标准问题。
        :type st_question: str
        :param score: 相似度得分，精确到小数点后3位。
        :type score: float
        :param domain: Domain.
        :type domain: str
        :param answer: 答案。
        :type answer: str
        :param ex_questions: 扩展问。
        :type ex_questions: list[:class:`huaweicloudsdkcbs.v1.ExQuestions`]
        """
        
        

        self._qa_pair_id = None
        self._st_question = None
        self._score = None
        self._domain = None
        self._answer = None
        self._ex_questions = None
        self.discriminator = None

        if qa_pair_id is not None:
            self.qa_pair_id = qa_pair_id
        if st_question is not None:
            self.st_question = st_question
        if score is not None:
            self.score = score
        if domain is not None:
            self.domain = domain
        if answer is not None:
            self.answer = answer
        if ex_questions is not None:
            self.ex_questions = ex_questions

    @property
    def qa_pair_id(self):
        """Gets the qa_pair_id of this Answers.

        Answers.

        :return: The qa_pair_id of this Answers.
        :rtype: str
        """
        return self._qa_pair_id

    @qa_pair_id.setter
    def qa_pair_id(self, qa_pair_id):
        """Sets the qa_pair_id of this Answers.

        Answers.

        :param qa_pair_id: The qa_pair_id of this Answers.
        :type qa_pair_id: str
        """
        self._qa_pair_id = qa_pair_id

    @property
    def st_question(self):
        """Gets the st_question of this Answers.

        标准问题。

        :return: The st_question of this Answers.
        :rtype: str
        """
        return self._st_question

    @st_question.setter
    def st_question(self, st_question):
        """Sets the st_question of this Answers.

        标准问题。

        :param st_question: The st_question of this Answers.
        :type st_question: str
        """
        self._st_question = st_question

    @property
    def score(self):
        """Gets the score of this Answers.

        相似度得分，精确到小数点后3位。

        :return: The score of this Answers.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this Answers.

        相似度得分，精确到小数点后3位。

        :param score: The score of this Answers.
        :type score: float
        """
        self._score = score

    @property
    def domain(self):
        """Gets the domain of this Answers.

        Domain.

        :return: The domain of this Answers.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Answers.

        Domain.

        :param domain: The domain of this Answers.
        :type domain: str
        """
        self._domain = domain

    @property
    def answer(self):
        """Gets the answer of this Answers.

        答案。

        :return: The answer of this Answers.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this Answers.

        答案。

        :param answer: The answer of this Answers.
        :type answer: str
        """
        self._answer = answer

    @property
    def ex_questions(self):
        """Gets the ex_questions of this Answers.

        扩展问。

        :return: The ex_questions of this Answers.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.ExQuestions`]
        """
        return self._ex_questions

    @ex_questions.setter
    def ex_questions(self, ex_questions):
        """Sets the ex_questions of this Answers.

        扩展问。

        :param ex_questions: The ex_questions of this Answers.
        :type ex_questions: list[:class:`huaweicloudsdkcbs.v1.ExQuestions`]
        """
        self._ex_questions = ex_questions

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
        if not isinstance(other, Answers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
