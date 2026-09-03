# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSkillReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'slug': 'str',
        'display_name': 'str',
        'alias_name': 'str',
        'description': 'str',
        'category': 'SkillCategoryEnum',
        'tags': 'list[str]',
        'cover': 'str',
        'source': 'SkillSourceEnum',
        'support_os_types': 'list[str]',
        'packages': 'list[CreateSkillPackage]'
    }

    attribute_map = {
        'slug': 'slug',
        'display_name': 'display_name',
        'alias_name': 'alias_name',
        'description': 'description',
        'category': 'category',
        'tags': 'tags',
        'cover': 'cover',
        'source': 'source',
        'support_os_types': 'support_os_types',
        'packages': 'packages'
    }

    def __init__(self, slug=None, display_name=None, alias_name=None, description=None, category=None, tags=None, cover=None, source=None, support_os_types=None, packages=None):
        r"""CreateSkillReq

        The model defined in huaweicloud sdk

        :param slug: 技能slug，创建后不可修改。
        :type slug: str
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
        :param source: 
        :type source: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        :param support_os_types: 支持的操作系统类型列表。
        :type support_os_types: list[str]
        :param packages: 技能包信息列表。
        :type packages: list[:class:`huaweicloudsdkworkspace.v2.CreateSkillPackage`]
        """
        
        

        self._slug = None
        self._display_name = None
        self._alias_name = None
        self._description = None
        self._category = None
        self._tags = None
        self._cover = None
        self._source = None
        self._support_os_types = None
        self._packages = None
        self.discriminator = None

        self.slug = slug
        self.display_name = display_name
        if alias_name is not None:
            self.alias_name = alias_name
        if description is not None:
            self.description = description
        self.category = category
        if tags is not None:
            self.tags = tags
        if cover is not None:
            self.cover = cover
        if source is not None:
            self.source = source
        if support_os_types is not None:
            self.support_os_types = support_os_types
        if packages is not None:
            self.packages = packages

    @property
    def slug(self):
        r"""Gets the slug of this CreateSkillReq.

        技能slug，创建后不可修改。

        :return: The slug of this CreateSkillReq.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        r"""Sets the slug of this CreateSkillReq.

        技能slug，创建后不可修改。

        :param slug: The slug of this CreateSkillReq.
        :type slug: str
        """
        self._slug = slug

    @property
    def display_name(self):
        r"""Gets the display_name of this CreateSkillReq.

        技能名称。

        :return: The display_name of this CreateSkillReq.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CreateSkillReq.

        技能名称。

        :param display_name: The display_name of this CreateSkillReq.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def alias_name(self):
        r"""Gets the alias_name of this CreateSkillReq.

        别名（业务界面可修改的名称）。

        :return: The alias_name of this CreateSkillReq.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        r"""Sets the alias_name of this CreateSkillReq.

        别名（业务界面可修改的名称）。

        :param alias_name: The alias_name of this CreateSkillReq.
        :type alias_name: str
        """
        self._alias_name = alias_name

    @property
    def description(self):
        r"""Gets the description of this CreateSkillReq.

        技能描述。

        :return: The description of this CreateSkillReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateSkillReq.

        技能描述。

        :param description: The description of this CreateSkillReq.
        :type description: str
        """
        self._description = description

    @property
    def category(self):
        r"""Gets the category of this CreateSkillReq.

        :return: The category of this CreateSkillReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateSkillReq.

        :param category: The category of this CreateSkillReq.
        :type category: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        """
        self._category = category

    @property
    def tags(self):
        r"""Gets the tags of this CreateSkillReq.

        技能标签。

        :return: The tags of this CreateSkillReq.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateSkillReq.

        技能标签。

        :param tags: The tags of this CreateSkillReq.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def cover(self):
        r"""Gets the cover of this CreateSkillReq.

        封面图 base64 编码。

        :return: The cover of this CreateSkillReq.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        r"""Sets the cover of this CreateSkillReq.

        封面图 base64 编码。

        :param cover: The cover of this CreateSkillReq.
        :type cover: str
        """
        self._cover = cover

    @property
    def source(self):
        r"""Gets the source of this CreateSkillReq.

        :return: The source of this CreateSkillReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateSkillReq.

        :param source: The source of this CreateSkillReq.
        :type source: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        """
        self._source = source

    @property
    def support_os_types(self):
        r"""Gets the support_os_types of this CreateSkillReq.

        支持的操作系统类型列表。

        :return: The support_os_types of this CreateSkillReq.
        :rtype: list[str]
        """
        return self._support_os_types

    @support_os_types.setter
    def support_os_types(self, support_os_types):
        r"""Sets the support_os_types of this CreateSkillReq.

        支持的操作系统类型列表。

        :param support_os_types: The support_os_types of this CreateSkillReq.
        :type support_os_types: list[str]
        """
        self._support_os_types = support_os_types

    @property
    def packages(self):
        r"""Gets the packages of this CreateSkillReq.

        技能包信息列表。

        :return: The packages of this CreateSkillReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.CreateSkillPackage`]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        r"""Sets the packages of this CreateSkillReq.

        技能包信息列表。

        :param packages: The packages of this CreateSkillReq.
        :type packages: list[:class:`huaweicloudsdkworkspace.v2.CreateSkillPackage`]
        """
        self._packages = packages

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
        if not isinstance(other, CreateSkillReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
