# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocBotAnswers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'answer': 'str',
        'score': 'float',
        'question': 'str',
        'answer_detail': 'DocQueryAnswerDetail',
        'details': 'list[DocQueryAnswerDetail]'
    }

    attribute_map = {
        'answer': 'answer',
        'score': 'score',
        'question': 'question',
        'answer_detail': 'answer_detail',
        'details': 'details'
    }

    def __init__(self, answer=None, score=None, question=None, answer_detail=None, details=None):
        """DocBotAnswers

        The model defined in huaweicloud sdk

        :param answer: 答案。
        :type answer: str
        :param score: 置信度。
        :type score: float
        :param question: 问题。
        :type question: str
        :param answer_detail: 
        :type answer_detail: :class:`huaweicloudsdkcbs.v1.DocQueryAnswerDetail`
        :param details: 候选答案列表
        :type details: list[:class:`huaweicloudsdkcbs.v1.DocQueryAnswerDetail`]
        """
        
        

        self._answer = None
        self._score = None
        self._question = None
        self._answer_detail = None
        self._details = None
        self.discriminator = None

        self.answer = answer
        self.score = score
        self.question = question
        if answer_detail is not None:
            self.answer_detail = answer_detail
        if details is not None:
            self.details = details

    @property
    def answer(self):
        """Gets the answer of this DocBotAnswers.

        答案。

        :return: The answer of this DocBotAnswers.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this DocBotAnswers.

        答案。

        :param answer: The answer of this DocBotAnswers.
        :type answer: str
        """
        self._answer = answer

    @property
    def score(self):
        """Gets the score of this DocBotAnswers.

        置信度。

        :return: The score of this DocBotAnswers.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this DocBotAnswers.

        置信度。

        :param score: The score of this DocBotAnswers.
        :type score: float
        """
        self._score = score

    @property
    def question(self):
        """Gets the question of this DocBotAnswers.

        问题。

        :return: The question of this DocBotAnswers.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this DocBotAnswers.

        问题。

        :param question: The question of this DocBotAnswers.
        :type question: str
        """
        self._question = question

    @property
    def answer_detail(self):
        """Gets the answer_detail of this DocBotAnswers.

        :return: The answer_detail of this DocBotAnswers.
        :rtype: :class:`huaweicloudsdkcbs.v1.DocQueryAnswerDetail`
        """
        return self._answer_detail

    @answer_detail.setter
    def answer_detail(self, answer_detail):
        """Sets the answer_detail of this DocBotAnswers.

        :param answer_detail: The answer_detail of this DocBotAnswers.
        :type answer_detail: :class:`huaweicloudsdkcbs.v1.DocQueryAnswerDetail`
        """
        self._answer_detail = answer_detail

    @property
    def details(self):
        """Gets the details of this DocBotAnswers.

        候选答案列表

        :return: The details of this DocBotAnswers.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.DocQueryAnswerDetail`]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this DocBotAnswers.

        候选答案列表

        :param details: The details of this DocBotAnswers.
        :type details: list[:class:`huaweicloudsdkcbs.v1.DocQueryAnswerDetail`]
        """
        self._details = details

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
        if not isinstance(other, DocBotAnswers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
