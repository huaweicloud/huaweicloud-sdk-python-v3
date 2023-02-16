# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnswerDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'qabot_answers': 'list[QabotAnswer]',
        'qa_flow_answers': 'QaFlowHitResult',
        'chat_answer': 'str',
        'graph_answer': 'QaGraphAnswer'
    }

    attribute_map = {
        'qabot_answers': 'qabot_answers',
        'qa_flow_answers': 'qa_flow_answers',
        'chat_answer': 'chat_answer',
        'graph_answer': 'graph_answer'
    }

    def __init__(self, qabot_answers=None, qa_flow_answers=None, chat_answer=None, graph_answer=None):
        """AnswerDetail

        The model defined in huaweicloud sdk

        :param qabot_answers: 答案列表
        :type qabot_answers: list[:class:`huaweicloudsdkosm.v2.QabotAnswer`]
        :param qa_flow_answers: 
        :type qa_flow_answers: :class:`huaweicloudsdkosm.v2.QaFlowHitResult`
        :param chat_answer: 问题
        :type chat_answer: str
        :param graph_answer: 
        :type graph_answer: :class:`huaweicloudsdkosm.v2.QaGraphAnswer`
        """
        
        

        self._qabot_answers = None
        self._qa_flow_answers = None
        self._chat_answer = None
        self._graph_answer = None
        self.discriminator = None

        if qabot_answers is not None:
            self.qabot_answers = qabot_answers
        if qa_flow_answers is not None:
            self.qa_flow_answers = qa_flow_answers
        if chat_answer is not None:
            self.chat_answer = chat_answer
        if graph_answer is not None:
            self.graph_answer = graph_answer

    @property
    def qabot_answers(self):
        """Gets the qabot_answers of this AnswerDetail.

        答案列表

        :return: The qabot_answers of this AnswerDetail.
        :rtype: list[:class:`huaweicloudsdkosm.v2.QabotAnswer`]
        """
        return self._qabot_answers

    @qabot_answers.setter
    def qabot_answers(self, qabot_answers):
        """Sets the qabot_answers of this AnswerDetail.

        答案列表

        :param qabot_answers: The qabot_answers of this AnswerDetail.
        :type qabot_answers: list[:class:`huaweicloudsdkosm.v2.QabotAnswer`]
        """
        self._qabot_answers = qabot_answers

    @property
    def qa_flow_answers(self):
        """Gets the qa_flow_answers of this AnswerDetail.

        :return: The qa_flow_answers of this AnswerDetail.
        :rtype: :class:`huaweicloudsdkosm.v2.QaFlowHitResult`
        """
        return self._qa_flow_answers

    @qa_flow_answers.setter
    def qa_flow_answers(self, qa_flow_answers):
        """Sets the qa_flow_answers of this AnswerDetail.

        :param qa_flow_answers: The qa_flow_answers of this AnswerDetail.
        :type qa_flow_answers: :class:`huaweicloudsdkosm.v2.QaFlowHitResult`
        """
        self._qa_flow_answers = qa_flow_answers

    @property
    def chat_answer(self):
        """Gets the chat_answer of this AnswerDetail.

        问题

        :return: The chat_answer of this AnswerDetail.
        :rtype: str
        """
        return self._chat_answer

    @chat_answer.setter
    def chat_answer(self, chat_answer):
        """Sets the chat_answer of this AnswerDetail.

        问题

        :param chat_answer: The chat_answer of this AnswerDetail.
        :type chat_answer: str
        """
        self._chat_answer = chat_answer

    @property
    def graph_answer(self):
        """Gets the graph_answer of this AnswerDetail.

        :return: The graph_answer of this AnswerDetail.
        :rtype: :class:`huaweicloudsdkosm.v2.QaGraphAnswer`
        """
        return self._graph_answer

    @graph_answer.setter
    def graph_answer(self, graph_answer):
        """Sets the graph_answer of this AnswerDetail.

        :param graph_answer: The graph_answer of this AnswerDetail.
        :type graph_answer: :class:`huaweicloudsdkosm.v2.QaGraphAnswer`
        """
        self._graph_answer = graph_answer

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
        if not isinstance(other, AnswerDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
