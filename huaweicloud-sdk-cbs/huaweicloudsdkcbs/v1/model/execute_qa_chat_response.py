# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteQaChatResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reply_type': 'int',
        'qabot_answers': 'QaBotAnswersNew',
        'chat_answers': 'ChatAnswers',
        'taskbot_answers': 'TaskBotAnswers',
        'docqa_answers': 'DocBotAnswers',
        'tableqa_answers': 'TableQaAnswers',
        'session_id': 'str',
        'kbqa_answers': 'KbqaAnswers',
        'request_id': 'str'
    }

    attribute_map = {
        'reply_type': 'reply_type',
        'qabot_answers': 'qabot_answers',
        'chat_answers': 'chat_answers',
        'taskbot_answers': 'taskbot_answers',
        'docqa_answers': 'docqa_answers',
        'tableqa_answers': 'tableqa_answers',
        'session_id': 'session_id',
        'kbqa_answers': 'kbqa_answers',
        'request_id': 'request_id'
    }

    def __init__(self, reply_type=None, qabot_answers=None, chat_answers=None, taskbot_answers=None, docqa_answers=None, tableqa_answers=None, session_id=None, kbqa_answers=None, request_id=None):
        """ExecuteQaChatResponse

        The model defined in huaweicloud sdk

        :param reply_type: 回复类型： 0   问答型机器人回复。 1   任务型机器人回复。 2   闲聊回复。 3   图谱问答回复。 4   文档问答回复。 5   表格问答回复。
        :type reply_type: int
        :param qabot_answers: 
        :type qabot_answers: :class:`huaweicloudsdkcbs.v1.QaBotAnswersNew`
        :param chat_answers: 
        :type chat_answers: :class:`huaweicloudsdkcbs.v1.ChatAnswers`
        :param taskbot_answers: 
        :type taskbot_answers: :class:`huaweicloudsdkcbs.v1.TaskBotAnswers`
        :param docqa_answers: 
        :type docqa_answers: :class:`huaweicloudsdkcbs.v1.DocBotAnswers`
        :param tableqa_answers: 
        :type tableqa_answers: :class:`huaweicloudsdkcbs.v1.TableQaAnswers`
        :param session_id: 会话ID，在下一次请求中传入改id表示继续会话。
        :type session_id: str
        :param kbqa_answers: 
        :type kbqa_answers: :class:`huaweicloudsdkcbs.v1.KbqaAnswers`
        :param request_id: 请求ID。用来标记调用失败时，用来标记本次问答。
        :type request_id: str
        """
        
        super(ExecuteQaChatResponse, self).__init__()

        self._reply_type = None
        self._qabot_answers = None
        self._chat_answers = None
        self._taskbot_answers = None
        self._docqa_answers = None
        self._tableqa_answers = None
        self._session_id = None
        self._kbqa_answers = None
        self._request_id = None
        self.discriminator = None

        if reply_type is not None:
            self.reply_type = reply_type
        if qabot_answers is not None:
            self.qabot_answers = qabot_answers
        if chat_answers is not None:
            self.chat_answers = chat_answers
        if taskbot_answers is not None:
            self.taskbot_answers = taskbot_answers
        if docqa_answers is not None:
            self.docqa_answers = docqa_answers
        if tableqa_answers is not None:
            self.tableqa_answers = tableqa_answers
        if session_id is not None:
            self.session_id = session_id
        if kbqa_answers is not None:
            self.kbqa_answers = kbqa_answers
        if request_id is not None:
            self.request_id = request_id

    @property
    def reply_type(self):
        """Gets the reply_type of this ExecuteQaChatResponse.

        回复类型： 0   问答型机器人回复。 1   任务型机器人回复。 2   闲聊回复。 3   图谱问答回复。 4   文档问答回复。 5   表格问答回复。

        :return: The reply_type of this ExecuteQaChatResponse.
        :rtype: int
        """
        return self._reply_type

    @reply_type.setter
    def reply_type(self, reply_type):
        """Sets the reply_type of this ExecuteQaChatResponse.

        回复类型： 0   问答型机器人回复。 1   任务型机器人回复。 2   闲聊回复。 3   图谱问答回复。 4   文档问答回复。 5   表格问答回复。

        :param reply_type: The reply_type of this ExecuteQaChatResponse.
        :type reply_type: int
        """
        self._reply_type = reply_type

    @property
    def qabot_answers(self):
        """Gets the qabot_answers of this ExecuteQaChatResponse.

        :return: The qabot_answers of this ExecuteQaChatResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.QaBotAnswersNew`
        """
        return self._qabot_answers

    @qabot_answers.setter
    def qabot_answers(self, qabot_answers):
        """Sets the qabot_answers of this ExecuteQaChatResponse.

        :param qabot_answers: The qabot_answers of this ExecuteQaChatResponse.
        :type qabot_answers: :class:`huaweicloudsdkcbs.v1.QaBotAnswersNew`
        """
        self._qabot_answers = qabot_answers

    @property
    def chat_answers(self):
        """Gets the chat_answers of this ExecuteQaChatResponse.

        :return: The chat_answers of this ExecuteQaChatResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.ChatAnswers`
        """
        return self._chat_answers

    @chat_answers.setter
    def chat_answers(self, chat_answers):
        """Sets the chat_answers of this ExecuteQaChatResponse.

        :param chat_answers: The chat_answers of this ExecuteQaChatResponse.
        :type chat_answers: :class:`huaweicloudsdkcbs.v1.ChatAnswers`
        """
        self._chat_answers = chat_answers

    @property
    def taskbot_answers(self):
        """Gets the taskbot_answers of this ExecuteQaChatResponse.

        :return: The taskbot_answers of this ExecuteQaChatResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.TaskBotAnswers`
        """
        return self._taskbot_answers

    @taskbot_answers.setter
    def taskbot_answers(self, taskbot_answers):
        """Sets the taskbot_answers of this ExecuteQaChatResponse.

        :param taskbot_answers: The taskbot_answers of this ExecuteQaChatResponse.
        :type taskbot_answers: :class:`huaweicloudsdkcbs.v1.TaskBotAnswers`
        """
        self._taskbot_answers = taskbot_answers

    @property
    def docqa_answers(self):
        """Gets the docqa_answers of this ExecuteQaChatResponse.

        :return: The docqa_answers of this ExecuteQaChatResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.DocBotAnswers`
        """
        return self._docqa_answers

    @docqa_answers.setter
    def docqa_answers(self, docqa_answers):
        """Sets the docqa_answers of this ExecuteQaChatResponse.

        :param docqa_answers: The docqa_answers of this ExecuteQaChatResponse.
        :type docqa_answers: :class:`huaweicloudsdkcbs.v1.DocBotAnswers`
        """
        self._docqa_answers = docqa_answers

    @property
    def tableqa_answers(self):
        """Gets the tableqa_answers of this ExecuteQaChatResponse.

        :return: The tableqa_answers of this ExecuteQaChatResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.TableQaAnswers`
        """
        return self._tableqa_answers

    @tableqa_answers.setter
    def tableqa_answers(self, tableqa_answers):
        """Sets the tableqa_answers of this ExecuteQaChatResponse.

        :param tableqa_answers: The tableqa_answers of this ExecuteQaChatResponse.
        :type tableqa_answers: :class:`huaweicloudsdkcbs.v1.TableQaAnswers`
        """
        self._tableqa_answers = tableqa_answers

    @property
    def session_id(self):
        """Gets the session_id of this ExecuteQaChatResponse.

        会话ID，在下一次请求中传入改id表示继续会话。

        :return: The session_id of this ExecuteQaChatResponse.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ExecuteQaChatResponse.

        会话ID，在下一次请求中传入改id表示继续会话。

        :param session_id: The session_id of this ExecuteQaChatResponse.
        :type session_id: str
        """
        self._session_id = session_id

    @property
    def kbqa_answers(self):
        """Gets the kbqa_answers of this ExecuteQaChatResponse.

        :return: The kbqa_answers of this ExecuteQaChatResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.KbqaAnswers`
        """
        return self._kbqa_answers

    @kbqa_answers.setter
    def kbqa_answers(self, kbqa_answers):
        """Sets the kbqa_answers of this ExecuteQaChatResponse.

        :param kbqa_answers: The kbqa_answers of this ExecuteQaChatResponse.
        :type kbqa_answers: :class:`huaweicloudsdkcbs.v1.KbqaAnswers`
        """
        self._kbqa_answers = kbqa_answers

    @property
    def request_id(self):
        """Gets the request_id of this ExecuteQaChatResponse.

        请求ID。用来标记调用失败时，用来标记本次问答。

        :return: The request_id of this ExecuteQaChatResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ExecuteQaChatResponse.

        请求ID。用来标记调用失败时，用来标记本次问答。

        :param request_id: The request_id of this ExecuteQaChatResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ExecuteQaChatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
