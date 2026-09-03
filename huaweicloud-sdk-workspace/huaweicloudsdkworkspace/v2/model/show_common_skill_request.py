# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCommonSkillRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'skill_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'skill_id': 'skill_id'
    }

    def __init__(self, x_language=None, skill_id=None):
        r"""ShowCommonSkillRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言，用于国际化。 - en-us：英文 - zh-cn：中文
        :type x_language: str
        :param skill_id: 技能标识。
        :type skill_id: str
        """
        
        

        self._x_language = None
        self._skill_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.skill_id = skill_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowCommonSkillRequest.

        语言，用于国际化。 - en-us：英文 - zh-cn：中文

        :return: The x_language of this ShowCommonSkillRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowCommonSkillRequest.

        语言，用于国际化。 - en-us：英文 - zh-cn：中文

        :param x_language: The x_language of this ShowCommonSkillRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def skill_id(self):
        r"""Gets the skill_id of this ShowCommonSkillRequest.

        技能标识。

        :return: The skill_id of this ShowCommonSkillRequest.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        r"""Sets the skill_id of this ShowCommonSkillRequest.

        技能标识。

        :param skill_id: The skill_id of this ShowCommonSkillRequest.
        :type skill_id: str
        """
        self._skill_id = skill_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowCommonSkillRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
