# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIntentAndQuestionReq:

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
        'answer': 'str',
        'skill_id': 'str',
        'question_list': 'list[KnowledgeQuestionCreateInfo]'
    }

    attribute_map = {
        'name': 'name',
        'answer': 'answer',
        'skill_id': 'skill_id',
        'question_list': 'question_list'
    }

    def __init__(self, name=None, answer=None, skill_id=None, question_list=None):
        r"""CreateIntentAndQuestionReq

        The model defined in huaweicloud sdk

        :param name: 主题。
        :type name: str
        :param answer: 问题答案。
        :type answer: str
        :param skill_id: 技能ID。
        :type skill_id: str
        :param question_list: 问法列表
        :type question_list: list[:class:`huaweicloudsdkmetastudio.v1.KnowledgeQuestionCreateInfo`]
        """
        
        

        self._name = None
        self._answer = None
        self._skill_id = None
        self._question_list = None
        self.discriminator = None

        self.name = name
        self.answer = answer
        self.skill_id = skill_id
        if question_list is not None:
            self.question_list = question_list

    @property
    def name(self):
        r"""Gets the name of this CreateIntentAndQuestionReq.

        主题。

        :return: The name of this CreateIntentAndQuestionReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateIntentAndQuestionReq.

        主题。

        :param name: The name of this CreateIntentAndQuestionReq.
        :type name: str
        """
        self._name = name

    @property
    def answer(self):
        r"""Gets the answer of this CreateIntentAndQuestionReq.

        问题答案。

        :return: The answer of this CreateIntentAndQuestionReq.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        r"""Sets the answer of this CreateIntentAndQuestionReq.

        问题答案。

        :param answer: The answer of this CreateIntentAndQuestionReq.
        :type answer: str
        """
        self._answer = answer

    @property
    def skill_id(self):
        r"""Gets the skill_id of this CreateIntentAndQuestionReq.

        技能ID。

        :return: The skill_id of this CreateIntentAndQuestionReq.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        r"""Sets the skill_id of this CreateIntentAndQuestionReq.

        技能ID。

        :param skill_id: The skill_id of this CreateIntentAndQuestionReq.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def question_list(self):
        r"""Gets the question_list of this CreateIntentAndQuestionReq.

        问法列表

        :return: The question_list of this CreateIntentAndQuestionReq.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.KnowledgeQuestionCreateInfo`]
        """
        return self._question_list

    @question_list.setter
    def question_list(self, question_list):
        r"""Sets the question_list of this CreateIntentAndQuestionReq.

        问法列表

        :param question_list: The question_list of this CreateIntentAndQuestionReq.
        :type question_list: list[:class:`huaweicloudsdkmetastudio.v1.KnowledgeQuestionCreateInfo`]
        """
        self._question_list = question_list

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
        if not isinstance(other, CreateIntentAndQuestionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
