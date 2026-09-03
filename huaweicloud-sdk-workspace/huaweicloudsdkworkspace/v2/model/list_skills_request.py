# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSkillsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'category': 'str',
        'status': 'str',
        'skill_name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'offset': 'offset',
        'limit': 'limit',
        'category': 'category',
        'status': 'status',
        'skill_name': 'skill_name'
    }

    def __init__(self, x_language=None, offset=None, limit=None, category=None, status=None, skill_name=None):
        r"""ListSkillsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言，用于国际化。 - en-us：英文 - zh-cn：中文
        :type x_language: str
        :param offset: 偏移量，默认0。
        :type offset: int
        :param limit: 分页大小，默认20。
        :type limit: int
        :param category: 技能分类。
        :type category: str
        :param status: 技能状态。
        :type status: str
        :param skill_name: 技能名称（模糊匹配slug、display_name和alias_name）。
        :type skill_name: str
        """
        
        

        self._x_language = None
        self._offset = None
        self._limit = None
        self._category = None
        self._status = None
        self._skill_name = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if category is not None:
            self.category = category
        if status is not None:
            self.status = status
        if skill_name is not None:
            self.skill_name = skill_name

    @property
    def x_language(self):
        r"""Gets the x_language of this ListSkillsRequest.

        语言，用于国际化。 - en-us：英文 - zh-cn：中文

        :return: The x_language of this ListSkillsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListSkillsRequest.

        语言，用于国际化。 - en-us：英文 - zh-cn：中文

        :param x_language: The x_language of this ListSkillsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        r"""Gets the offset of this ListSkillsRequest.

        偏移量，默认0。

        :return: The offset of this ListSkillsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSkillsRequest.

        偏移量，默认0。

        :param offset: The offset of this ListSkillsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSkillsRequest.

        分页大小，默认20。

        :return: The limit of this ListSkillsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSkillsRequest.

        分页大小，默认20。

        :param limit: The limit of this ListSkillsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def category(self):
        r"""Gets the category of this ListSkillsRequest.

        技能分类。

        :return: The category of this ListSkillsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListSkillsRequest.

        技能分类。

        :param category: The category of this ListSkillsRequest.
        :type category: str
        """
        self._category = category

    @property
    def status(self):
        r"""Gets the status of this ListSkillsRequest.

        技能状态。

        :return: The status of this ListSkillsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSkillsRequest.

        技能状态。

        :param status: The status of this ListSkillsRequest.
        :type status: str
        """
        self._status = status

    @property
    def skill_name(self):
        r"""Gets the skill_name of this ListSkillsRequest.

        技能名称（模糊匹配slug、display_name和alias_name）。

        :return: The skill_name of this ListSkillsRequest.
        :rtype: str
        """
        return self._skill_name

    @skill_name.setter
    def skill_name(self, skill_name):
        r"""Sets the skill_name of this ListSkillsRequest.

        技能名称（模糊匹配slug、display_name和alias_name）。

        :param skill_name: The skill_name of this ListSkillsRequest.
        :type skill_name: str
        """
        self._skill_name = skill_name

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
        if not isinstance(other, ListSkillsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
