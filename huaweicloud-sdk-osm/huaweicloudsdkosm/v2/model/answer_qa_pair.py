# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnswerQaPair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'score': 'float',
        'answer': 'str',
        'domain': 'str',
        'link': 'str',
        'question': 'str',
        'qa_pair_id': 'str',
        'relevance_details': 'list[RelevanceQapair]',
        'task_complete': 'bool'
    }

    attribute_map = {
        'score': 'score',
        'answer': 'answer',
        'domain': 'domain',
        'link': 'link',
        'question': 'question',
        'qa_pair_id': 'qa_pair_id',
        'relevance_details': 'relevance_details',
        'task_complete': 'task_complete'
    }

    def __init__(self, score=None, answer=None, domain=None, link=None, question=None, qa_pair_id=None, relevance_details=None, task_complete=None):
        """AnswerQaPair

        The model defined in huaweicloud sdk

        :param score: 相似度得分
        :type score: float
        :param answer: 答案
        :type answer: str
        :param domain: 主题
        :type domain: str
        :param link: 链接
        :type link: str
        :param question: 问题
        :type question: str
        :param qa_pair_id: 语料Id
        :type qa_pair_id: str
        :param relevance_details: 相关问题详情列表
        :type relevance_details: list[:class:`huaweicloudsdkosm.v2.RelevanceQapair`]
        :param task_complete: 技能意图识别是否结束
        :type task_complete: bool
        """
        
        

        self._score = None
        self._answer = None
        self._domain = None
        self._link = None
        self._question = None
        self._qa_pair_id = None
        self._relevance_details = None
        self._task_complete = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if answer is not None:
            self.answer = answer
        if domain is not None:
            self.domain = domain
        if link is not None:
            self.link = link
        if question is not None:
            self.question = question
        if qa_pair_id is not None:
            self.qa_pair_id = qa_pair_id
        if relevance_details is not None:
            self.relevance_details = relevance_details
        if task_complete is not None:
            self.task_complete = task_complete

    @property
    def score(self):
        """Gets the score of this AnswerQaPair.

        相似度得分

        :return: The score of this AnswerQaPair.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this AnswerQaPair.

        相似度得分

        :param score: The score of this AnswerQaPair.
        :type score: float
        """
        self._score = score

    @property
    def answer(self):
        """Gets the answer of this AnswerQaPair.

        答案

        :return: The answer of this AnswerQaPair.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this AnswerQaPair.

        答案

        :param answer: The answer of this AnswerQaPair.
        :type answer: str
        """
        self._answer = answer

    @property
    def domain(self):
        """Gets the domain of this AnswerQaPair.

        主题

        :return: The domain of this AnswerQaPair.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AnswerQaPair.

        主题

        :param domain: The domain of this AnswerQaPair.
        :type domain: str
        """
        self._domain = domain

    @property
    def link(self):
        """Gets the link of this AnswerQaPair.

        链接

        :return: The link of this AnswerQaPair.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this AnswerQaPair.

        链接

        :param link: The link of this AnswerQaPair.
        :type link: str
        """
        self._link = link

    @property
    def question(self):
        """Gets the question of this AnswerQaPair.

        问题

        :return: The question of this AnswerQaPair.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this AnswerQaPair.

        问题

        :param question: The question of this AnswerQaPair.
        :type question: str
        """
        self._question = question

    @property
    def qa_pair_id(self):
        """Gets the qa_pair_id of this AnswerQaPair.

        语料Id

        :return: The qa_pair_id of this AnswerQaPair.
        :rtype: str
        """
        return self._qa_pair_id

    @qa_pair_id.setter
    def qa_pair_id(self, qa_pair_id):
        """Sets the qa_pair_id of this AnswerQaPair.

        语料Id

        :param qa_pair_id: The qa_pair_id of this AnswerQaPair.
        :type qa_pair_id: str
        """
        self._qa_pair_id = qa_pair_id

    @property
    def relevance_details(self):
        """Gets the relevance_details of this AnswerQaPair.

        相关问题详情列表

        :return: The relevance_details of this AnswerQaPair.
        :rtype: list[:class:`huaweicloudsdkosm.v2.RelevanceQapair`]
        """
        return self._relevance_details

    @relevance_details.setter
    def relevance_details(self, relevance_details):
        """Sets the relevance_details of this AnswerQaPair.

        相关问题详情列表

        :param relevance_details: The relevance_details of this AnswerQaPair.
        :type relevance_details: list[:class:`huaweicloudsdkosm.v2.RelevanceQapair`]
        """
        self._relevance_details = relevance_details

    @property
    def task_complete(self):
        """Gets the task_complete of this AnswerQaPair.

        技能意图识别是否结束

        :return: The task_complete of this AnswerQaPair.
        :rtype: bool
        """
        return self._task_complete

    @task_complete.setter
    def task_complete(self, task_complete):
        """Sets the task_complete of this AnswerQaPair.

        技能意图识别是否结束

        :param task_complete: The task_complete of this AnswerQaPair.
        :type task_complete: bool
        """
        self._task_complete = task_complete

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
        if not isinstance(other, AnswerQaPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
