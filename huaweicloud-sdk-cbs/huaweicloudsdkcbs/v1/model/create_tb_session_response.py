# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTbSessionResponse(SdkResponse):


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
        'action': 'int',
        'session_id': 'str',
        'question_id': 'str',
        'audio_file_path': 'str'
    }

    attribute_map = {
        'question': 'question',
        'action': 'action',
        'session_id': 'session_id',
        'question_id': 'question_id',
        'audio_file_path': 'audio_file_path'
    }

    def __init__(self, question=None, action=None, session_id=None, question_id=None, audio_file_path=None):
        """CreateTbSessionResponse - a model defined in huaweicloud sdk"""
        
        super(CreateTbSessionResponse, self).__init__()

        self._question = None
        self._action = None
        self._session_id = None
        self._question_id = None
        self._audio_file_path = None
        self.discriminator = None

        if question is not None:
            self.question = question
        if action is not None:
            self.action = action
        if session_id is not None:
            self.session_id = session_id
        if question_id is not None:
            self.question_id = question_id
        if audio_file_path is not None:
            self.audio_file_path = audio_file_path

    @property
    def question(self):
        """Gets the question of this CreateTbSessionResponse.

        问题。

        :return: The question of this CreateTbSessionResponse.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this CreateTbSessionResponse.

        问题。

        :param question: The question of this CreateTbSessionResponse.
        :type: str
        """
        self._question = question

    @property
    def action(self):
        """Gets the action of this CreateTbSessionResponse.

        0表示继续， 1表示直接中断， 2表示播放结束音后中断。

        :return: The action of this CreateTbSessionResponse.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this CreateTbSessionResponse.

        0表示继续， 1表示直接中断， 2表示播放结束音后中断。

        :param action: The action of this CreateTbSessionResponse.
        :type: int
        """
        self._action = action

    @property
    def session_id(self):
        """Gets the session_id of this CreateTbSessionResponse.

        会话ID。

        :return: The session_id of this CreateTbSessionResponse.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this CreateTbSessionResponse.

        会话ID。

        :param session_id: The session_id of this CreateTbSessionResponse.
        :type: str
        """
        self._session_id = session_id

    @property
    def question_id(self):
        """Gets the question_id of this CreateTbSessionResponse.

        问题ID。

        :return: The question_id of this CreateTbSessionResponse.
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        """Sets the question_id of this CreateTbSessionResponse.

        问题ID。

        :param question_id: The question_id of this CreateTbSessionResponse.
        :type: str
        """
        self._question_id = question_id

    @property
    def audio_file_path(self):
        """Gets the audio_file_path of this CreateTbSessionResponse.

        语音文件地址。

        :return: The audio_file_path of this CreateTbSessionResponse.
        :rtype: str
        """
        return self._audio_file_path

    @audio_file_path.setter
    def audio_file_path(self, audio_file_path):
        """Sets the audio_file_path of this CreateTbSessionResponse.

        语音文件地址。

        :param audio_file_path: The audio_file_path of this CreateTbSessionResponse.
        :type: str
        """
        self._audio_file_path = audio_file_path

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
        if not isinstance(other, CreateTbSessionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
