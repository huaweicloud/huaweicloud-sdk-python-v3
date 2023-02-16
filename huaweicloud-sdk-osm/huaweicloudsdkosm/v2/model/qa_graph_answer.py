# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QaGraphAnswer:

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
        'score': 'float',
        'type': 'int',
        'options': 'list[str]'
    }

    attribute_map = {
        'answer': 'answer',
        'score': 'score',
        'type': 'type',
        'options': 'options'
    }

    def __init__(self, answer=None, score=None, type=None, options=None):
        """QaGraphAnswer

        The model defined in huaweicloud sdk

        :param answer: 答案
        :type answer: str
        :param score: 评分
        :type score: float
        :param type: 类型
        :type type: int
        :param options: 列表
        :type options: list[str]
        """
        
        

        self._answer = None
        self._score = None
        self._type = None
        self._options = None
        self.discriminator = None

        if answer is not None:
            self.answer = answer
        if score is not None:
            self.score = score
        if type is not None:
            self.type = type
        if options is not None:
            self.options = options

    @property
    def answer(self):
        """Gets the answer of this QaGraphAnswer.

        答案

        :return: The answer of this QaGraphAnswer.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this QaGraphAnswer.

        答案

        :param answer: The answer of this QaGraphAnswer.
        :type answer: str
        """
        self._answer = answer

    @property
    def score(self):
        """Gets the score of this QaGraphAnswer.

        评分

        :return: The score of this QaGraphAnswer.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this QaGraphAnswer.

        评分

        :param score: The score of this QaGraphAnswer.
        :type score: float
        """
        self._score = score

    @property
    def type(self):
        """Gets the type of this QaGraphAnswer.

        类型

        :return: The type of this QaGraphAnswer.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QaGraphAnswer.

        类型

        :param type: The type of this QaGraphAnswer.
        :type type: int
        """
        self._type = type

    @property
    def options(self):
        """Gets the options of this QaGraphAnswer.

        列表

        :return: The options of this QaGraphAnswer.
        :rtype: list[str]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this QaGraphAnswer.

        列表

        :param options: The options of this QaGraphAnswer.
        :type options: list[str]
        """
        self._options = options

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
        if not isinstance(other, QaGraphAnswer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
