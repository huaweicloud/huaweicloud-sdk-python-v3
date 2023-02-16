# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QabotAnswer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'question': 'str',
        'answer': 'str',
        'score': 'float',
        'domain': 'str',
        'link': 'str',
        'qa_pair_id': 'str',
        'domain_id': 'str',
        'top_score_question': 'str',
        'relevance_details': 'list[RelevanceQapair]'
    }

    attribute_map = {
        'question': 'question',
        'answer': 'answer',
        'score': 'score',
        'domain': 'domain',
        'link': 'link',
        'qa_pair_id': 'qa_pair_id',
        'domain_id': 'domain_id',
        'top_score_question': 'top_score_question',
        'relevance_details': 'relevance_details'
    }

    def __init__(self, question=None, answer=None, score=None, domain=None, link=None, qa_pair_id=None, domain_id=None, top_score_question=None, relevance_details=None):
        """QabotAnswer

        The model defined in huaweicloud sdk

        :param question: 问题
        :type question: str
        :param answer: 答案
        :type answer: str
        :param score: 评分
        :type score: float
        :param domain: 主题
        :type domain: str
        :param link: 链接地址
        :type link: str
        :param qa_pair_id: 语料id
        :type qa_pair_id: str
        :param domain_id: 主题id
        :type domain_id: str
        :param top_score_question: 推荐答案
        :type top_score_question: str
        :param relevance_details: 相关问题列表
        :type relevance_details: list[:class:`huaweicloudsdkosm.v2.RelevanceQapair`]
        """
        
        

        self._question = None
        self._answer = None
        self._score = None
        self._domain = None
        self._link = None
        self._qa_pair_id = None
        self._domain_id = None
        self._top_score_question = None
        self._relevance_details = None
        self.discriminator = None

        if question is not None:
            self.question = question
        if answer is not None:
            self.answer = answer
        if score is not None:
            self.score = score
        if domain is not None:
            self.domain = domain
        if link is not None:
            self.link = link
        if qa_pair_id is not None:
            self.qa_pair_id = qa_pair_id
        if domain_id is not None:
            self.domain_id = domain_id
        if top_score_question is not None:
            self.top_score_question = top_score_question
        if relevance_details is not None:
            self.relevance_details = relevance_details

    @property
    def question(self):
        """Gets the question of this QabotAnswer.

        问题

        :return: The question of this QabotAnswer.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this QabotAnswer.

        问题

        :param question: The question of this QabotAnswer.
        :type question: str
        """
        self._question = question

    @property
    def answer(self):
        """Gets the answer of this QabotAnswer.

        答案

        :return: The answer of this QabotAnswer.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this QabotAnswer.

        答案

        :param answer: The answer of this QabotAnswer.
        :type answer: str
        """
        self._answer = answer

    @property
    def score(self):
        """Gets the score of this QabotAnswer.

        评分

        :return: The score of this QabotAnswer.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this QabotAnswer.

        评分

        :param score: The score of this QabotAnswer.
        :type score: float
        """
        self._score = score

    @property
    def domain(self):
        """Gets the domain of this QabotAnswer.

        主题

        :return: The domain of this QabotAnswer.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this QabotAnswer.

        主题

        :param domain: The domain of this QabotAnswer.
        :type domain: str
        """
        self._domain = domain

    @property
    def link(self):
        """Gets the link of this QabotAnswer.

        链接地址

        :return: The link of this QabotAnswer.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this QabotAnswer.

        链接地址

        :param link: The link of this QabotAnswer.
        :type link: str
        """
        self._link = link

    @property
    def qa_pair_id(self):
        """Gets the qa_pair_id of this QabotAnswer.

        语料id

        :return: The qa_pair_id of this QabotAnswer.
        :rtype: str
        """
        return self._qa_pair_id

    @qa_pair_id.setter
    def qa_pair_id(self, qa_pair_id):
        """Sets the qa_pair_id of this QabotAnswer.

        语料id

        :param qa_pair_id: The qa_pair_id of this QabotAnswer.
        :type qa_pair_id: str
        """
        self._qa_pair_id = qa_pair_id

    @property
    def domain_id(self):
        """Gets the domain_id of this QabotAnswer.

        主题id

        :return: The domain_id of this QabotAnswer.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this QabotAnswer.

        主题id

        :param domain_id: The domain_id of this QabotAnswer.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def top_score_question(self):
        """Gets the top_score_question of this QabotAnswer.

        推荐答案

        :return: The top_score_question of this QabotAnswer.
        :rtype: str
        """
        return self._top_score_question

    @top_score_question.setter
    def top_score_question(self, top_score_question):
        """Sets the top_score_question of this QabotAnswer.

        推荐答案

        :param top_score_question: The top_score_question of this QabotAnswer.
        :type top_score_question: str
        """
        self._top_score_question = top_score_question

    @property
    def relevance_details(self):
        """Gets the relevance_details of this QabotAnswer.

        相关问题列表

        :return: The relevance_details of this QabotAnswer.
        :rtype: list[:class:`huaweicloudsdkosm.v2.RelevanceQapair`]
        """
        return self._relevance_details

    @relevance_details.setter
    def relevance_details(self, relevance_details):
        """Sets the relevance_details of this QabotAnswer.

        相关问题列表

        :param relevance_details: The relevance_details of this QabotAnswer.
        :type relevance_details: list[:class:`huaweicloudsdkosm.v2.RelevanceQapair`]
        """
        self._relevance_details = relevance_details

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
        if not isinstance(other, QabotAnswer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
