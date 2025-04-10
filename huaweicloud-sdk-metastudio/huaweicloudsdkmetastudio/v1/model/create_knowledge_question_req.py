# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKnowledgeQuestionReq:

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
        'intent_id': 'str'
    }

    attribute_map = {
        'question': 'question',
        'intent_id': 'intent_id'
    }

    def __init__(self, question=None, intent_id=None):
        r"""CreateKnowledgeQuestionReq

        The model defined in huaweicloud sdk

        :param question: 问法。
        :type question: str
        :param intent_id: 意图ID。
        :type intent_id: str
        """
        
        

        self._question = None
        self._intent_id = None
        self.discriminator = None

        self.question = question
        if intent_id is not None:
            self.intent_id = intent_id

    @property
    def question(self):
        r"""Gets the question of this CreateKnowledgeQuestionReq.

        问法。

        :return: The question of this CreateKnowledgeQuestionReq.
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        r"""Sets the question of this CreateKnowledgeQuestionReq.

        问法。

        :param question: The question of this CreateKnowledgeQuestionReq.
        :type question: str
        """
        self._question = question

    @property
    def intent_id(self):
        r"""Gets the intent_id of this CreateKnowledgeQuestionReq.

        意图ID。

        :return: The intent_id of this CreateKnowledgeQuestionReq.
        :rtype: str
        """
        return self._intent_id

    @intent_id.setter
    def intent_id(self, intent_id):
        r"""Sets the intent_id of this CreateKnowledgeQuestionReq.

        意图ID。

        :param intent_id: The intent_id of this CreateKnowledgeQuestionReq.
        :type intent_id: str
        """
        self._intent_id = intent_id

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
        if not isinstance(other, CreateKnowledgeQuestionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
