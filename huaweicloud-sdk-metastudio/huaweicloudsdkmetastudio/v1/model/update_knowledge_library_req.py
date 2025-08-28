# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKnowledgeLibraryReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'topk': 'int',
        'score': 'float'
    }

    attribute_map = {
        'name': 'name',
        'topk': 'topk',
        'score': 'score'
    }

    def __init__(self, name=None, topk=None, score=None):
        r"""UpdateKnowledgeLibraryReq

        The model defined in huaweicloud sdk

        :param name: 知识库名称。
        :type name: str
        :param topk: 知识库召回数
        :type topk: int
        :param score: 知识库召回得分
        :type score: float
        """
        
        

        self._name = None
        self._topk = None
        self._score = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if topk is not None:
            self.topk = topk
        if score is not None:
            self.score = score

    @property
    def name(self):
        r"""Gets the name of this UpdateKnowledgeLibraryReq.

        知识库名称。

        :return: The name of this UpdateKnowledgeLibraryReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateKnowledgeLibraryReq.

        知识库名称。

        :param name: The name of this UpdateKnowledgeLibraryReq.
        :type name: str
        """
        self._name = name

    @property
    def topk(self):
        r"""Gets the topk of this UpdateKnowledgeLibraryReq.

        知识库召回数

        :return: The topk of this UpdateKnowledgeLibraryReq.
        :rtype: int
        """
        return self._topk

    @topk.setter
    def topk(self, topk):
        r"""Sets the topk of this UpdateKnowledgeLibraryReq.

        知识库召回数

        :param topk: The topk of this UpdateKnowledgeLibraryReq.
        :type topk: int
        """
        self._topk = topk

    @property
    def score(self):
        r"""Gets the score of this UpdateKnowledgeLibraryReq.

        知识库召回得分

        :return: The score of this UpdateKnowledgeLibraryReq.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this UpdateKnowledgeLibraryReq.

        知识库召回得分

        :param score: The score of this UpdateKnowledgeLibraryReq.
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
        if not isinstance(other, UpdateKnowledgeLibraryReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
