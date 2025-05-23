# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChatAnswers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'answer': 'str',
        'score': 'float'
    }

    attribute_map = {
        'answer': 'answer',
        'score': 'score'
    }

    def __init__(self, answer=None, score=None):
        r"""ChatAnswers

        The model defined in huaweicloud sdk

        :param answer: 答案。
        :type answer: str
        :param score: 闲聊的置信度，范围:0.0~1.0  0.0表示兜底回复
        :type score: float
        """
        
        

        self._answer = None
        self._score = None
        self.discriminator = None

        self.answer = answer
        if score is not None:
            self.score = score

    @property
    def answer(self):
        r"""Gets the answer of this ChatAnswers.

        答案。

        :return: The answer of this ChatAnswers.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        r"""Sets the answer of this ChatAnswers.

        答案。

        :param answer: The answer of this ChatAnswers.
        :type answer: str
        """
        self._answer = answer

    @property
    def score(self):
        r"""Gets the score of this ChatAnswers.

        闲聊的置信度，范围:0.0~1.0  0.0表示兜底回复

        :return: The score of this ChatAnswers.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this ChatAnswers.

        闲聊的置信度，范围:0.0~1.0  0.0表示兜底回复

        :param score: The score of this ChatAnswers.
        :type score: float
        """
        self._score = score

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
        if not isinstance(other, ChatAnswers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
