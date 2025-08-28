# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecallKnowledgeLibraryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'document_id': 'str',
        'file_name': 'str',
        'file_type': 'str',
        'question_answer_id': 'str',
        'content': 'str',
        'score': 'float'
    }

    attribute_map = {
        'document_id': 'document_id',
        'file_name': 'file_name',
        'file_type': 'file_type',
        'question_answer_id': 'question_answer_id',
        'content': 'content',
        'score': 'score'
    }

    def __init__(self, document_id=None, file_name=None, file_type=None, question_answer_id=None, content=None, score=None):
        r"""RecallKnowledgeLibraryInfo

        The model defined in huaweicloud sdk

        :param document_id: 文档ID。
        :type document_id: str
        :param file_name: 文档名称。
        :type file_name: str
        :param file_type: 文档类型。
        :type file_type: str
        :param question_answer_id: 问答对ID。
        :type question_answer_id: str
        :param content: 召回文本
        :type content: str
        :param score: 知识库召回得分
        :type score: float
        """
        
        

        self._document_id = None
        self._file_name = None
        self._file_type = None
        self._question_answer_id = None
        self._content = None
        self._score = None
        self.discriminator = None

        if document_id is not None:
            self.document_id = document_id
        if file_name is not None:
            self.file_name = file_name
        if file_type is not None:
            self.file_type = file_type
        if question_answer_id is not None:
            self.question_answer_id = question_answer_id
        if content is not None:
            self.content = content
        if score is not None:
            self.score = score

    @property
    def document_id(self):
        r"""Gets the document_id of this RecallKnowledgeLibraryInfo.

        文档ID。

        :return: The document_id of this RecallKnowledgeLibraryInfo.
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        r"""Sets the document_id of this RecallKnowledgeLibraryInfo.

        文档ID。

        :param document_id: The document_id of this RecallKnowledgeLibraryInfo.
        :type document_id: str
        """
        self._document_id = document_id

    @property
    def file_name(self):
        r"""Gets the file_name of this RecallKnowledgeLibraryInfo.

        文档名称。

        :return: The file_name of this RecallKnowledgeLibraryInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this RecallKnowledgeLibraryInfo.

        文档名称。

        :param file_name: The file_name of this RecallKnowledgeLibraryInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def file_type(self):
        r"""Gets the file_type of this RecallKnowledgeLibraryInfo.

        文档类型。

        :return: The file_type of this RecallKnowledgeLibraryInfo.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        r"""Sets the file_type of this RecallKnowledgeLibraryInfo.

        文档类型。

        :param file_type: The file_type of this RecallKnowledgeLibraryInfo.
        :type file_type: str
        """
        self._file_type = file_type

    @property
    def question_answer_id(self):
        r"""Gets the question_answer_id of this RecallKnowledgeLibraryInfo.

        问答对ID。

        :return: The question_answer_id of this RecallKnowledgeLibraryInfo.
        :rtype: str
        """
        return self._question_answer_id

    @question_answer_id.setter
    def question_answer_id(self, question_answer_id):
        r"""Sets the question_answer_id of this RecallKnowledgeLibraryInfo.

        问答对ID。

        :param question_answer_id: The question_answer_id of this RecallKnowledgeLibraryInfo.
        :type question_answer_id: str
        """
        self._question_answer_id = question_answer_id

    @property
    def content(self):
        r"""Gets the content of this RecallKnowledgeLibraryInfo.

        召回文本

        :return: The content of this RecallKnowledgeLibraryInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this RecallKnowledgeLibraryInfo.

        召回文本

        :param content: The content of this RecallKnowledgeLibraryInfo.
        :type content: str
        """
        self._content = content

    @property
    def score(self):
        r"""Gets the score of this RecallKnowledgeLibraryInfo.

        知识库召回得分

        :return: The score of this RecallKnowledgeLibraryInfo.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this RecallKnowledgeLibraryInfo.

        知识库召回得分

        :param score: The score of this RecallKnowledgeLibraryInfo.
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
        if not isinstance(other, RecallKnowledgeLibraryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
