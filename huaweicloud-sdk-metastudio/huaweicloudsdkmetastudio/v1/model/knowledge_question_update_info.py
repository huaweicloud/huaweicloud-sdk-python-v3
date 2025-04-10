# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KnowledgeQuestionUpdateInfo:

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
        'question': 'str'
    }

    attribute_map = {
        'question_id': 'question_id',
        'question': 'question'
    }

    def __init__(self, question_id=None, question=None):
        r"""KnowledgeQuestionUpdateInfo

        The model defined in huaweicloud sdk

        :param question_id: 问法ID。
        :type question_id: str
        :param question: 问法。
        :type question: str
        """
        
        

        self._question_id = None
        self._question = None
        self.discriminator = None

        self.question_id = question_id
        self.question = question

    @property
    def question_id(self):
        r"""Gets the question_id of this KnowledgeQuestionUpdateInfo.

        问法ID。

        :return: The question_id of this KnowledgeQuestionUpdateInfo.
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        r"""Sets the question_id of this KnowledgeQuestionUpdateInfo.

        问法ID。

        :param question_id: The question_id of this KnowledgeQuestionUpdateInfo.
        :type question_id: str
        """
        self._question_id = question_id

    @property
    def question(self):
        r"""Gets the question of this KnowledgeQuestionUpdateInfo.

        问法。

        :return: The question of this KnowledgeQuestionUpdateInfo.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        r"""Sets the question of this KnowledgeQuestionUpdateInfo.

        问法。

        :param question: The question of this KnowledgeQuestionUpdateInfo.
        :type question: str
        """
        self._question = question

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
        if not isinstance(other, KnowledgeQuestionUpdateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
