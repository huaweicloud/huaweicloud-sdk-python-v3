# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskBotAnswers:

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
        'skill_id': 'str',
        'skill_responses': 'list[SkillResponse]'
    }

    attribute_map = {
        'answer': 'answer',
        'skill_id': 'skill_id',
        'skill_responses': 'skill_responses'
    }

    def __init__(self, answer=None, skill_id=None, skill_responses=None):
        """TaskBotAnswers

        The model defined in huaweicloud sdk

        :param answer: 答案。
        :type answer: str
        :param skill_id: 技能ID。
        :type skill_id: str
        :param skill_responses: 技能回复信息。
        :type skill_responses: list[:class:`huaweicloudsdkcbs.v1.SkillResponse`]
        """
        
        

        self._answer = None
        self._skill_id = None
        self._skill_responses = None
        self.discriminator = None

        self.answer = answer
        self.skill_id = skill_id
        self.skill_responses = skill_responses

    @property
    def answer(self):
        """Gets the answer of this TaskBotAnswers.

        答案。

        :return: The answer of this TaskBotAnswers.
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this TaskBotAnswers.

        答案。

        :param answer: The answer of this TaskBotAnswers.
        :type answer: str
        """
        self._answer = answer

    @property
    def skill_id(self):
        """Gets the skill_id of this TaskBotAnswers.

        技能ID。

        :return: The skill_id of this TaskBotAnswers.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        """Sets the skill_id of this TaskBotAnswers.

        技能ID。

        :param skill_id: The skill_id of this TaskBotAnswers.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def skill_responses(self):
        """Gets the skill_responses of this TaskBotAnswers.

        技能回复信息。

        :return: The skill_responses of this TaskBotAnswers.
        :rtype: list[:class:`huaweicloudsdkcbs.v1.SkillResponse`]
        """
        return self._skill_responses

    @skill_responses.setter
    def skill_responses(self, skill_responses):
        """Sets the skill_responses of this TaskBotAnswers.

        技能回复信息。

        :param skill_responses: The skill_responses of this TaskBotAnswers.
        :type skill_responses: list[:class:`huaweicloudsdkcbs.v1.SkillResponse`]
        """
        self._skill_responses = skill_responses

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
        if not isinstance(other, TaskBotAnswers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
