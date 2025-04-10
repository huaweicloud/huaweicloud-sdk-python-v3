# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableQaAnswers:

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
        'table_id': 'str'
    }

    attribute_map = {
        'answer': 'answer',
        'score': 'score',
        'table_id': 'table_id'
    }

    def __init__(self, answer=None, score=None, table_id=None):
        r"""TableQaAnswers

        The model defined in huaweicloud sdk

        :param answer: 表格问答答案。
        :type answer: str
        :param score: 评分。
        :type score: float
        :param table_id: 表格ID。
        :type table_id: str
        """
        
        

        self._answer = None
        self._score = None
        self._table_id = None
        self.discriminator = None

        self.answer = answer
        self.score = score
        self.table_id = table_id

    @property
    def answer(self):
        r"""Gets the answer of this TableQaAnswers.

        表格问答答案。

        :return: The answer of this TableQaAnswers.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        r"""Sets the answer of this TableQaAnswers.

        表格问答答案。

        :param answer: The answer of this TableQaAnswers.
        :type answer: str
        """
        self._answer = answer

    @property
    def score(self):
        r"""Gets the score of this TableQaAnswers.

        评分。

        :return: The score of this TableQaAnswers.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this TableQaAnswers.

        评分。

        :param score: The score of this TableQaAnswers.
        :type score: float
        """
        self._score = score

    @property
    def table_id(self):
        r"""Gets the table_id of this TableQaAnswers.

        表格ID。

        :return: The table_id of this TableQaAnswers.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        r"""Sets the table_id of this TableQaAnswers.

        表格ID。

        :param table_id: The table_id of this TableQaAnswers.
        :type table_id: str
        """
        self._table_id = table_id

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
        if not isinstance(other, TableQaAnswers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
