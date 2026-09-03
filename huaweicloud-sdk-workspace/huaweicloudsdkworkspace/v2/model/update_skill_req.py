# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSkillReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'alias_name': 'str',
        'description': 'str',
        'category': 'SkillCategoryEnum',
        'tags': 'list[str]',
        'cover': 'str',
        'status': 'SkillStatusEnum',
        'source': 'SkillSourceEnum',
        'support_os_types': 'list[str]'
    }

    attribute_map = {
        'display_name': 'display_name',
        'alias_name': 'alias_name',
        'description': 'description',
        'category': 'category',
        'tags': 'tags',
        'cover': 'cover',
        'status': 'status',
        'source': 'source',
        'support_os_types': 'support_os_types'
    }

    def __init__(self, display_name=None, alias_name=None, description=None, category=None, tags=None, cover=None, status=None, source=None, support_os_types=None):
        r"""UpdateSkillReq

        The model defined in huaweicloud sdk

        :param display_name: 技能名称。
        :type display_name: str
        :param alias_name: 别名（业务界面可修改的名称）。
        :type alias_name: str
        :param description: 技能描述。
        :type description: str
        :param category: 
        :type category: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        :param tags: 技能标签。
        :type tags: list[str]
        :param cover: 封面图 base64 编码。
        :type cover: str
        :param status: 
        :type status: :class:`huaweicloudsdkworkspace.v2.SkillStatusEnum`
        :param source: 
        :type source: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        :param support_os_types: 支持的操作系统类型列表。
        :type support_os_types: list[str]
        """
        
        

        self._display_name = None
        self._alias_name = None
        self._description = None
        self._category = None
        self._tags = None
        self._cover = None
        self._status = None
        self._source = None
        self._support_os_types = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if alias_name is not None:
            self.alias_name = alias_name
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if tags is not None:
            self.tags = tags
        if cover is not None:
            self.cover = cover
        if status is not None:
            self.status = status
        if source is not None:
            self.source = source
        if support_os_types is not None:
            self.support_os_types = support_os_types

    @property
    def display_name(self):
        r"""Gets the display_name of this UpdateSkillReq.

        技能名称。

        :return: The display_name of this UpdateSkillReq.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this UpdateSkillReq.

        技能名称。

        :param display_name: The display_name of this UpdateSkillReq.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def alias_name(self):
        r"""Gets the alias_name of this UpdateSkillReq.

        别名（业务界面可修改的名称）。

        :return: The alias_name of this UpdateSkillReq.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        r"""Sets the alias_name of this UpdateSkillReq.

        别名（业务界面可修改的名称）。

        :param alias_name: The alias_name of this UpdateSkillReq.
        :type alias_name: str
        """
        self._alias_name = alias_name

    @property
    def description(self):
        r"""Gets the description of this UpdateSkillReq.

        技能描述。

        :return: The description of this UpdateSkillReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateSkillReq.

        技能描述。

        :param description: The description of this UpdateSkillReq.
        :type description: str
        """
        self._description = description

    @property
    def category(self):
        r"""Gets the category of this UpdateSkillReq.

        :return: The category of this UpdateSkillReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this UpdateSkillReq.

        :param category: The category of this UpdateSkillReq.
        :type category: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        """
        self._category = category

    @property
    def tags(self):
        r"""Gets the tags of this UpdateSkillReq.

        技能标签。

        :return: The tags of this UpdateSkillReq.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateSkillReq.

        技能标签。

        :param tags: The tags of this UpdateSkillReq.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def cover(self):
        r"""Gets the cover of this UpdateSkillReq.

        封面图 base64 编码。

        :return: The cover of this UpdateSkillReq.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        r"""Sets the cover of this UpdateSkillReq.

        封面图 base64 编码。

        :param cover: The cover of this UpdateSkillReq.
        :type cover: str
        """
        self._cover = cover

    @property
    def status(self):
        r"""Gets the status of this UpdateSkillReq.

        :return: The status of this UpdateSkillReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateSkillReq.

        :param status: The status of this UpdateSkillReq.
        :type status: :class:`huaweicloudsdkworkspace.v2.SkillStatusEnum`
        """
        self._status = status

    @property
    def source(self):
        r"""Gets the source of this UpdateSkillReq.

        :return: The source of this UpdateSkillReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this UpdateSkillReq.

        :param source: The source of this UpdateSkillReq.
        :type source: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        """
        self._source = source

    @property
    def support_os_types(self):
        r"""Gets the support_os_types of this UpdateSkillReq.

        支持的操作系统类型列表。

        :return: The support_os_types of this UpdateSkillReq.
        :rtype: list[str]
        """
        return self._support_os_types

    @support_os_types.setter
    def support_os_types(self, support_os_types):
        r"""Sets the support_os_types of this UpdateSkillReq.

        支持的操作系统类型列表。

        :param support_os_types: The support_os_types of this UpdateSkillReq.
        :type support_os_types: list[str]
        """
        self._support_os_types = support_os_types

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
        if not isinstance(other, UpdateSkillReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
