# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuestionAnswerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'question_answer_id': 'str',
        'question': 'str',
        'answer': 'str',
        'similar_questions': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'question_answer_id': 'question_answer_id',
        'question': 'question',
        'answer': 'answer',
        'similar_questions': 'similar_questions',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, question_answer_id=None, question=None, answer=None, similar_questions=None, create_time=None, update_time=None):
        r"""QuestionAnswerInfo

        The model defined in huaweicloud sdk

        :param question_answer_id: 问答对ID。
        :type question_answer_id: str
        :param question: 标准问题。
        :type question: str
        :param answer: 问题答案。
        :type answer: str
        :param similar_questions: 所有相似问题，多个相似问题间用换行符\\n分隔。
        :type similar_questions: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._question_answer_id = None
        self._question = None
        self._answer = None
        self._similar_questions = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if question_answer_id is not None:
            self.question_answer_id = question_answer_id
        if question is not None:
            self.question = question
        if answer is not None:
            self.answer = answer
        if similar_questions is not None:
            self.similar_questions = similar_questions
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def question_answer_id(self):
        r"""Gets the question_answer_id of this QuestionAnswerInfo.

        问答对ID。

        :return: The question_answer_id of this QuestionAnswerInfo.
        :rtype: str
        """
        return self._question_answer_id

    @question_answer_id.setter
    def question_answer_id(self, question_answer_id):
        r"""Sets the question_answer_id of this QuestionAnswerInfo.

        问答对ID。

        :param question_answer_id: The question_answer_id of this QuestionAnswerInfo.
        :type question_answer_id: str
        """
        self._question_answer_id = question_answer_id

    @property
    def question(self):
        r"""Gets the question of this QuestionAnswerInfo.

        标准问题。

        :return: The question of this QuestionAnswerInfo.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        r"""Sets the question of this QuestionAnswerInfo.

        标准问题。

        :param question: The question of this QuestionAnswerInfo.
        :type question: str
        """
        self._question = question

    @property
    def answer(self):
        r"""Gets the answer of this QuestionAnswerInfo.

        问题答案。

        :return: The answer of this QuestionAnswerInfo.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        r"""Sets the answer of this QuestionAnswerInfo.

        问题答案。

        :param answer: The answer of this QuestionAnswerInfo.
        :type answer: str
        """
        self._answer = answer

    @property
    def similar_questions(self):
        r"""Gets the similar_questions of this QuestionAnswerInfo.

        所有相似问题，多个相似问题间用换行符\\n分隔。

        :return: The similar_questions of this QuestionAnswerInfo.
        :rtype: str
        """
        return self._similar_questions

    @similar_questions.setter
    def similar_questions(self, similar_questions):
        r"""Sets the similar_questions of this QuestionAnswerInfo.

        所有相似问题，多个相似问题间用换行符\\n分隔。

        :param similar_questions: The similar_questions of this QuestionAnswerInfo.
        :type similar_questions: str
        """
        self._similar_questions = similar_questions

    @property
    def create_time(self):
        r"""Gets the create_time of this QuestionAnswerInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this QuestionAnswerInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this QuestionAnswerInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this QuestionAnswerInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this QuestionAnswerInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this QuestionAnswerInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this QuestionAnswerInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this QuestionAnswerInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, QuestionAnswerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
