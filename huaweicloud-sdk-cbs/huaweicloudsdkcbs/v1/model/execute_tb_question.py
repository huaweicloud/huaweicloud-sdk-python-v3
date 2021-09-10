# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteTbQuestion:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'question_id': 'str',
        'audio_file_path': 'str',
        'question': 'str',
        'action': 'int'
    }

    attribute_map = {
        'question_id': 'question_id',
        'audio_file_path': 'audio_file_path',
        'question': 'question',
        'action': 'action'
    }

    def __init__(self, question_id=None, audio_file_path=None, question=None, action=None):
        """ExecuteTbQuestion - a model defined in huaweicloud sdk"""
        
        

        self._question_id = None
        self._audio_file_path = None
        self._question = None
        self._action = None
        self.discriminator = None

        self.question_id = question_id
        if audio_file_path is not None:
            self.audio_file_path = audio_file_path
        self.question = question
        self.action = action

    @property
    def question_id(self):
        """Gets the question_id of this ExecuteTbQuestion.

        问题ID。

        :return: The question_id of this ExecuteTbQuestion.
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        """Sets the question_id of this ExecuteTbQuestion.

        问题ID。

        :param question_id: The question_id of this ExecuteTbQuestion.
        :type: str
        """
        self._question_id = question_id

    @property
    def audio_file_path(self):
        """Gets the audio_file_path of this ExecuteTbQuestion.

        语音文件路径。

        :return: The audio_file_path of this ExecuteTbQuestion.
        :rtype: str
        """
        return self._audio_file_path

    @audio_file_path.setter
    def audio_file_path(self, audio_file_path):
        """Sets the audio_file_path of this ExecuteTbQuestion.

        语音文件路径。

        :param audio_file_path: The audio_file_path of this ExecuteTbQuestion.
        :type: str
        """
        self._audio_file_path = audio_file_path

    @property
    def question(self):
        """Gets the question of this ExecuteTbQuestion.

        问题。

        :return: The question of this ExecuteTbQuestion.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this ExecuteTbQuestion.

        问题。

        :param question: The question of this ExecuteTbQuestion.
        :type: str
        """
        self._question = question

    @property
    def action(self):
        """Gets the action of this ExecuteTbQuestion.

        0 继续， 1 直接中断， 2 播放结束音后中断。

        :return: The action of this ExecuteTbQuestion.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ExecuteTbQuestion.

        0 继续， 1 直接中断， 2 播放结束音后中断。

        :param action: The action of this ExecuteTbQuestion.
        :type: int
        """
        self._action = action

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
        if not isinstance(other, ExecuteTbQuestion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
