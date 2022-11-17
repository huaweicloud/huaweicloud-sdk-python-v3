# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocQueryAnswerDetail:

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
        'doc_id': 'str',
        'end_index': 'int',
        'paragraph_score': 'float',
        'paragraph_text': 'str',
        'phrase_score': 'float',
        'start_index': 'int',
        'total_score': 'float',
        'paragraph_number': 'int'
    }

    attribute_map = {
        'answer': 'answer',
        'doc_id': 'doc_id',
        'end_index': 'end_index',
        'paragraph_score': 'paragraph_score',
        'paragraph_text': 'paragraph_text',
        'phrase_score': 'phrase_score',
        'start_index': 'start_index',
        'total_score': 'total_score',
        'paragraph_number': 'paragraph_number'
    }

    def __init__(self, answer=None, doc_id=None, end_index=None, paragraph_score=None, paragraph_text=None, phrase_score=None, start_index=None, total_score=None, paragraph_number=None):
        """DocQueryAnswerDetail

        The model defined in huaweicloud sdk

        :param answer: 答案。
        :type answer: str
        :param doc_id: 文档ID。
        :type doc_id: str
        :param end_index: 答案结束下标。
        :type end_index: int
        :param paragraph_score: 段落评分。
        :type paragraph_score: float
        :param paragraph_text: 段落文字。
        :type paragraph_text: str
        :param phrase_score: 文档问答阅读理解评分。
        :type phrase_score: float
        :param start_index: 答案开始下标。
        :type start_index: int
        :param total_score: 文档问答总评分。
        :type total_score: float
        :param paragraph_number: 段落在文档中的编号。
        :type paragraph_number: int
        """
        
        

        self._answer = None
        self._doc_id = None
        self._end_index = None
        self._paragraph_score = None
        self._paragraph_text = None
        self._phrase_score = None
        self._start_index = None
        self._total_score = None
        self._paragraph_number = None
        self.discriminator = None

        self.answer = answer
        self.doc_id = doc_id
        self.end_index = end_index
        self.paragraph_score = paragraph_score
        self.paragraph_text = paragraph_text
        self.phrase_score = phrase_score
        self.start_index = start_index
        self.total_score = total_score
        self.paragraph_number = paragraph_number

    @property
    def answer(self):
        """Gets the answer of this DocQueryAnswerDetail.

        答案。

        :return: The answer of this DocQueryAnswerDetail.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this DocQueryAnswerDetail.

        答案。

        :param answer: The answer of this DocQueryAnswerDetail.
        :type answer: str
        """
        self._answer = answer

    @property
    def doc_id(self):
        """Gets the doc_id of this DocQueryAnswerDetail.

        文档ID。

        :return: The doc_id of this DocQueryAnswerDetail.
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """Sets the doc_id of this DocQueryAnswerDetail.

        文档ID。

        :param doc_id: The doc_id of this DocQueryAnswerDetail.
        :type doc_id: str
        """
        self._doc_id = doc_id

    @property
    def end_index(self):
        """Gets the end_index of this DocQueryAnswerDetail.

        答案结束下标。

        :return: The end_index of this DocQueryAnswerDetail.
        :rtype: int
        """
        return self._end_index

    @end_index.setter
    def end_index(self, end_index):
        """Sets the end_index of this DocQueryAnswerDetail.

        答案结束下标。

        :param end_index: The end_index of this DocQueryAnswerDetail.
        :type end_index: int
        """
        self._end_index = end_index

    @property
    def paragraph_score(self):
        """Gets the paragraph_score of this DocQueryAnswerDetail.

        段落评分。

        :return: The paragraph_score of this DocQueryAnswerDetail.
        :rtype: float
        """
        return self._paragraph_score

    @paragraph_score.setter
    def paragraph_score(self, paragraph_score):
        """Sets the paragraph_score of this DocQueryAnswerDetail.

        段落评分。

        :param paragraph_score: The paragraph_score of this DocQueryAnswerDetail.
        :type paragraph_score: float
        """
        self._paragraph_score = paragraph_score

    @property
    def paragraph_text(self):
        """Gets the paragraph_text of this DocQueryAnswerDetail.

        段落文字。

        :return: The paragraph_text of this DocQueryAnswerDetail.
        :rtype: str
        """
        return self._paragraph_text

    @paragraph_text.setter
    def paragraph_text(self, paragraph_text):
        """Sets the paragraph_text of this DocQueryAnswerDetail.

        段落文字。

        :param paragraph_text: The paragraph_text of this DocQueryAnswerDetail.
        :type paragraph_text: str
        """
        self._paragraph_text = paragraph_text

    @property
    def phrase_score(self):
        """Gets the phrase_score of this DocQueryAnswerDetail.

        文档问答阅读理解评分。

        :return: The phrase_score of this DocQueryAnswerDetail.
        :rtype: float
        """
        return self._phrase_score

    @phrase_score.setter
    def phrase_score(self, phrase_score):
        """Sets the phrase_score of this DocQueryAnswerDetail.

        文档问答阅读理解评分。

        :param phrase_score: The phrase_score of this DocQueryAnswerDetail.
        :type phrase_score: float
        """
        self._phrase_score = phrase_score

    @property
    def start_index(self):
        """Gets the start_index of this DocQueryAnswerDetail.

        答案开始下标。

        :return: The start_index of this DocQueryAnswerDetail.
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this DocQueryAnswerDetail.

        答案开始下标。

        :param start_index: The start_index of this DocQueryAnswerDetail.
        :type start_index: int
        """
        self._start_index = start_index

    @property
    def total_score(self):
        """Gets the total_score of this DocQueryAnswerDetail.

        文档问答总评分。

        :return: The total_score of this DocQueryAnswerDetail.
        :rtype: float
        """
        return self._total_score

    @total_score.setter
    def total_score(self, total_score):
        """Sets the total_score of this DocQueryAnswerDetail.

        文档问答总评分。

        :param total_score: The total_score of this DocQueryAnswerDetail.
        :type total_score: float
        """
        self._total_score = total_score

    @property
    def paragraph_number(self):
        """Gets the paragraph_number of this DocQueryAnswerDetail.

        段落在文档中的编号。

        :return: The paragraph_number of this DocQueryAnswerDetail.
        :rtype: int
        """
        return self._paragraph_number

    @paragraph_number.setter
    def paragraph_number(self, paragraph_number):
        """Sets the paragraph_number of this DocQueryAnswerDetail.

        段落在文档中的编号。

        :param paragraph_number: The paragraph_number of this DocQueryAnswerDetail.
        :type paragraph_number: int
        """
        self._paragraph_number = paragraph_number

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
        if not isinstance(other, DocQueryAnswerDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
