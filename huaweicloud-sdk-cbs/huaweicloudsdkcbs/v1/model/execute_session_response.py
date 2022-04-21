# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteSessionResponse(SdkResponse):

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
        'qabot_answers': 'QaBotAnswers',
        'chat_answers': 'ChatAnswers',
        'taskbot_answers': 'TaskBotAnswers',
        'request_id': 'str'
    }

    attribute_map = {
        'reply_type': 'reply_type',
        'qabot_answers': 'qabot_answers',
        'chat_answers': 'chat_answers',
        'taskbot_answers': 'taskbot_answers',
        'request_id': 'request_id'
    }

    def __init__(self, reply_type=None, qabot_answers=None, chat_answers=None, taskbot_answers=None, request_id=None):
        """ExecuteSessionResponse

        The model defined in huaweicloud sdk

        :param reply_type: 回复类型： 0   问答型机器人回复。 1   任务型机器人回复。 2   闲聊回复。
        :type reply_type: int
        :param qabot_answers: 
        :type qabot_answers: :class:`huaweicloudsdkcbs.v1.QaBotAnswers`
        :param chat_answers: 
        :type chat_answers: :class:`huaweicloudsdkcbs.v1.ChatAnswers`
        :param taskbot_answers: 
        :type taskbot_answers: :class:`huaweicloudsdkcbs.v1.TaskBotAnswers`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ExecuteSessionResponse, self).__init__()

        self._reply_type = None
        self._qabot_answers = None
        self._chat_answers = None
        self._taskbot_answers = None
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
        if request_id is not None:
            self.request_id = request_id

    @property
    def reply_type(self):
        """Gets the reply_type of this ExecuteSessionResponse.

        回复类型： 0   问答型机器人回复。 1   任务型机器人回复。 2   闲聊回复。

        :return: The reply_type of this ExecuteSessionResponse.
        :rtype: int
        """
        return self._reply_type

    @reply_type.setter
    def reply_type(self, reply_type):
        """Sets the reply_type of this ExecuteSessionResponse.

        回复类型： 0   问答型机器人回复。 1   任务型机器人回复。 2   闲聊回复。

        :param reply_type: The reply_type of this ExecuteSessionResponse.
        :type reply_type: int
        """
        self._reply_type = reply_type

    @property
    def qabot_answers(self):
        """Gets the qabot_answers of this ExecuteSessionResponse.


        :return: The qabot_answers of this ExecuteSessionResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.QaBotAnswers`
        """
        return self._qabot_answers

    @qabot_answers.setter
    def qabot_answers(self, qabot_answers):
        """Sets the qabot_answers of this ExecuteSessionResponse.


        :param qabot_answers: The qabot_answers of this ExecuteSessionResponse.
        :type qabot_answers: :class:`huaweicloudsdkcbs.v1.QaBotAnswers`
        """
        self._qabot_answers = qabot_answers

    @property
    def chat_answers(self):
        """Gets the chat_answers of this ExecuteSessionResponse.


        :return: The chat_answers of this ExecuteSessionResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.ChatAnswers`
        """
        return self._chat_answers

    @chat_answers.setter
    def chat_answers(self, chat_answers):
        """Sets the chat_answers of this ExecuteSessionResponse.


        :param chat_answers: The chat_answers of this ExecuteSessionResponse.
        :type chat_answers: :class:`huaweicloudsdkcbs.v1.ChatAnswers`
        """
        self._chat_answers = chat_answers

    @property
    def taskbot_answers(self):
        """Gets the taskbot_answers of this ExecuteSessionResponse.


        :return: The taskbot_answers of this ExecuteSessionResponse.
        :rtype: :class:`huaweicloudsdkcbs.v1.TaskBotAnswers`
        """
        return self._taskbot_answers

    @taskbot_answers.setter
    def taskbot_answers(self, taskbot_answers):
        """Sets the taskbot_answers of this ExecuteSessionResponse.


        :param taskbot_answers: The taskbot_answers of this ExecuteSessionResponse.
        :type taskbot_answers: :class:`huaweicloudsdkcbs.v1.TaskBotAnswers`
        """
        self._taskbot_answers = taskbot_answers

    @property
    def request_id(self):
        """Gets the request_id of this ExecuteSessionResponse.

        请求ID。

        :return: The request_id of this ExecuteSessionResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ExecuteSessionResponse.

        请求ID。

        :param request_id: The request_id of this ExecuteSessionResponse.
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
        if not isinstance(other, ExecuteSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
