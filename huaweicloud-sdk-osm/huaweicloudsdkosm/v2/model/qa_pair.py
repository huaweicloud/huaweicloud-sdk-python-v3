# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QaPair:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'link': 'str',
        'question': 'str',
        'answers': 'list[Answer]',
        'qa_pair_id': 'str',
        'ex_questions': 'list[ExtendQuestion]',
        'related_question_ids': 'list[str]'
    }

    attribute_map = {
        'domain': 'domain',
        'link': 'link',
        'question': 'question',
        'answers': 'answers',
        'qa_pair_id': 'qa_pair_id',
        'ex_questions': 'ex_questions',
        'related_question_ids': 'related_question_ids'
    }

    def __init__(self, domain=None, link=None, question=None, answers=None, qa_pair_id=None, ex_questions=None, related_question_ids=None):
        """QaPair

        The model defined in huaweicloud sdk

        :param domain: 主题
        :type domain: str
        :param link: 链接
        :type link: str
        :param question: 问题
        :type question: str
        :param answers: 答案列表
        :type answers: list[:class:`huaweicloudsdkosm.v2.Answer`]
        :param qa_pair_id: 语料Id
        :type qa_pair_id: str
        :param ex_questions: 扩展问题列表
        :type ex_questions: list[:class:`huaweicloudsdkosm.v2.ExtendQuestion`]
        :param related_question_ids: 相关问题列表
        :type related_question_ids: list[str]
        """
        
        

        self._domain = None
        self._link = None
        self._question = None
        self._answers = None
        self._qa_pair_id = None
        self._ex_questions = None
        self._related_question_ids = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if link is not None:
            self.link = link
        if question is not None:
            self.question = question
        if answers is not None:
            self.answers = answers
        if qa_pair_id is not None:
            self.qa_pair_id = qa_pair_id
        if ex_questions is not None:
            self.ex_questions = ex_questions
        if related_question_ids is not None:
            self.related_question_ids = related_question_ids

    @property
    def domain(self):
        """Gets the domain of this QaPair.

        主题

        :return: The domain of this QaPair.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this QaPair.

        主题

        :param domain: The domain of this QaPair.
        :type domain: str
        """
        self._domain = domain

    @property
    def link(self):
        """Gets the link of this QaPair.

        链接

        :return: The link of this QaPair.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this QaPair.

        链接

        :param link: The link of this QaPair.
        :type link: str
        """
        self._link = link

    @property
    def question(self):
        """Gets the question of this QaPair.

        问题

        :return: The question of this QaPair.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this QaPair.

        问题

        :param question: The question of this QaPair.
        :type question: str
        """
        self._question = question

    @property
    def answers(self):
        """Gets the answers of this QaPair.

        答案列表

        :return: The answers of this QaPair.
        :rtype: list[:class:`huaweicloudsdkosm.v2.Answer`]
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """Sets the answers of this QaPair.

        答案列表

        :param answers: The answers of this QaPair.
        :type answers: list[:class:`huaweicloudsdkosm.v2.Answer`]
        """
        self._answers = answers

    @property
    def qa_pair_id(self):
        """Gets the qa_pair_id of this QaPair.

        语料Id

        :return: The qa_pair_id of this QaPair.
        :rtype: str
        """
        return self._qa_pair_id

    @qa_pair_id.setter
    def qa_pair_id(self, qa_pair_id):
        """Sets the qa_pair_id of this QaPair.

        语料Id

        :param qa_pair_id: The qa_pair_id of this QaPair.
        :type qa_pair_id: str
        """
        self._qa_pair_id = qa_pair_id

    @property
    def ex_questions(self):
        """Gets the ex_questions of this QaPair.

        扩展问题列表

        :return: The ex_questions of this QaPair.
        :rtype: list[:class:`huaweicloudsdkosm.v2.ExtendQuestion`]
        """
        return self._ex_questions

    @ex_questions.setter
    def ex_questions(self, ex_questions):
        """Sets the ex_questions of this QaPair.

        扩展问题列表

        :param ex_questions: The ex_questions of this QaPair.
        :type ex_questions: list[:class:`huaweicloudsdkosm.v2.ExtendQuestion`]
        """
        self._ex_questions = ex_questions

    @property
    def related_question_ids(self):
        """Gets the related_question_ids of this QaPair.

        相关问题列表

        :return: The related_question_ids of this QaPair.
        :rtype: list[str]
        """
        return self._related_question_ids

    @related_question_ids.setter
    def related_question_ids(self, related_question_ids):
        """Sets the related_question_ids of this QaPair.

        相关问题列表

        :param related_question_ids: The related_question_ids of this QaPair.
        :type related_question_ids: list[str]
        """
        self._related_question_ids = related_question_ids

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
        if not isinstance(other, QaPair):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
