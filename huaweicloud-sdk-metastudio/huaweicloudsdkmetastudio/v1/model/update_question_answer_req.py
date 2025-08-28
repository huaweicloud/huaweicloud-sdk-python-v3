# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateQuestionAnswerReq:

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
        'similar_questions': 'str'
    }

    attribute_map = {
        'question': 'question',
        'answer': 'answer',
        'similar_questions': 'similar_questions'
    }

    def __init__(self, question=None, answer=None, similar_questions=None):
        r"""UpdateQuestionAnswerReq

        The model defined in huaweicloud sdk

        :param question: 标准问题。
        :type question: str
        :param answer: 问题答案。
        :type answer: str
        :param similar_questions: 所有相似问题，多个相似问题间用换行符\\n分隔。
        :type similar_questions: str
        """
        
        

        self._question = None
        self._answer = None
        self._similar_questions = None
        self.discriminator = None

        if question is not None:
            self.question = question
        if answer is not None:
            self.answer = answer
        if similar_questions is not None:
            self.similar_questions = similar_questions

    @property
    def question(self):
        r"""Gets the question of this UpdateQuestionAnswerReq.

        标准问题。

        :return: The question of this UpdateQuestionAnswerReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        r"""Sets the question of this UpdateQuestionAnswerReq.

        标准问题。

        :param question: The question of this UpdateQuestionAnswerReq.
        :type question: str
        """
        self._question = question

    @property
    def answer(self):
        r"""Gets the answer of this UpdateQuestionAnswerReq.

        问题答案。

        :return: The answer of this UpdateQuestionAnswerReq.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        r"""Sets the answer of this UpdateQuestionAnswerReq.

        问题答案。

        :param answer: The answer of this UpdateQuestionAnswerReq.
        :type answer: str
        """
        self._answer = answer

    @property
    def similar_questions(self):
        r"""Gets the similar_questions of this UpdateQuestionAnswerReq.

        所有相似问题，多个相似问题间用换行符\\n分隔。

        :return: The similar_questions of this UpdateQuestionAnswerReq.
        :rtype: str
        """
        return self._similar_questions

    @similar_questions.setter
    def similar_questions(self, similar_questions):
        r"""Sets the similar_questions of this UpdateQuestionAnswerReq.

        所有相似问题，多个相似问题间用换行符\\n分隔。

        :param similar_questions: The similar_questions of this UpdateQuestionAnswerReq.
        :type similar_questions: str
        """
        self._similar_questions = similar_questions

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
        if not isinstance(other, UpdateQuestionAnswerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
