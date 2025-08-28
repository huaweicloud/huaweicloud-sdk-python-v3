# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuestionAnswerResponse(SdkResponse):

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
        'update_time': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'question_answer_id': 'question_answer_id',
        'question': 'question',
        'answer': 'answer',
        'similar_questions': 'similar_questions',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, question_answer_id=None, question=None, answer=None, similar_questions=None, create_time=None, update_time=None, x_request_id=None):
        r"""ShowQuestionAnswerResponse

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
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowQuestionAnswerResponse, self).__init__()

        self._question_answer_id = None
        self._question = None
        self._answer = None
        self._similar_questions = None
        self._create_time = None
        self._update_time = None
        self._x_request_id = None
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
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def question_answer_id(self):
        r"""Gets the question_answer_id of this ShowQuestionAnswerResponse.

        问答对ID。

        :return: The question_answer_id of this ShowQuestionAnswerResponse.
        :rtype: str
        """
        return self._question_answer_id

    @question_answer_id.setter
    def question_answer_id(self, question_answer_id):
        r"""Sets the question_answer_id of this ShowQuestionAnswerResponse.

        问答对ID。

        :param question_answer_id: The question_answer_id of this ShowQuestionAnswerResponse.
        :type question_answer_id: str
        """
        self._question_answer_id = question_answer_id

    @property
    def question(self):
        r"""Gets the question of this ShowQuestionAnswerResponse.

        标准问题。

        :return: The question of this ShowQuestionAnswerResponse.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        r"""Sets the question of this ShowQuestionAnswerResponse.

        标准问题。

        :param question: The question of this ShowQuestionAnswerResponse.
        :type question: str
        """
        self._question = question

    @property
    def answer(self):
        r"""Gets the answer of this ShowQuestionAnswerResponse.

        问题答案。

        :return: The answer of this ShowQuestionAnswerResponse.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        r"""Sets the answer of this ShowQuestionAnswerResponse.

        问题答案。

        :param answer: The answer of this ShowQuestionAnswerResponse.
        :type answer: str
        """
        self._answer = answer

    @property
    def similar_questions(self):
        r"""Gets the similar_questions of this ShowQuestionAnswerResponse.

        所有相似问题，多个相似问题间用换行符\\n分隔。

        :return: The similar_questions of this ShowQuestionAnswerResponse.
        :rtype: str
        """
        return self._similar_questions

    @similar_questions.setter
    def similar_questions(self, similar_questions):
        r"""Sets the similar_questions of this ShowQuestionAnswerResponse.

        所有相似问题，多个相似问题间用换行符\\n分隔。

        :param similar_questions: The similar_questions of this ShowQuestionAnswerResponse.
        :type similar_questions: str
        """
        self._similar_questions = similar_questions

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowQuestionAnswerResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowQuestionAnswerResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowQuestionAnswerResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowQuestionAnswerResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowQuestionAnswerResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowQuestionAnswerResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowQuestionAnswerResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowQuestionAnswerResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowQuestionAnswerResponse.

        :return: The x_request_id of this ShowQuestionAnswerResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowQuestionAnswerResponse.

        :param x_request_id: The x_request_id of this ShowQuestionAnswerResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowQuestionAnswerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
