# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SkillListItemVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'slug': 'str',
        'display_name': 'str',
        'alias_name': 'str',
        'category': 'SkillCategoryEnum',
        'description': 'str',
        'tags': 'list[str]',
        'status': 'SkillStatusEnum',
        'visibility_scope': 'VisibilityScopeEnum',
        'current_package_id': 'str',
        'current_version': 'str',
        'current_revision': 'int',
        'cover': 'str',
        'source': 'SkillSourceEnum',
        'support_os_types': 'list[str]',
        'create_time': 'str',
        'update_time': 'str',
        'attach_instance_number': 'int'
    }

    attribute_map = {
        'id': 'id',
        'slug': 'slug',
        'display_name': 'display_name',
        'alias_name': 'alias_name',
        'category': 'category',
        'description': 'description',
        'tags': 'tags',
        'status': 'status',
        'visibility_scope': 'visibility_scope',
        'current_package_id': 'current_package_id',
        'current_version': 'current_version',
        'current_revision': 'current_revision',
        'cover': 'cover',
        'source': 'source',
        'support_os_types': 'support_os_types',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'attach_instance_number': 'attach_instance_number'
    }

    def __init__(self, id=None, slug=None, display_name=None, alias_name=None, category=None, description=None, tags=None, status=None, visibility_scope=None, current_package_id=None, current_version=None, current_revision=None, cover=None, source=None, support_os_types=None, create_time=None, update_time=None, attach_instance_number=None):
        r"""SkillListItemVO

        The model defined in huaweicloud sdk

        :param id: 技能id。
        :type id: str
        :param slug: 技能slug。
        :type slug: str
        :param display_name: 技能名称。
        :type display_name: str
        :param alias_name: 别名。
        :type alias_name: str
        :param category: 
        :type category: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        :param description: 技能描述。
        :type description: str
        :param tags: 技能标签。
        :type tags: list[str]
        :param status: 
        :type status: :class:`huaweicloudsdkworkspace.v2.SkillStatusEnum`
        :param visibility_scope: 
        :type visibility_scope: :class:`huaweicloudsdkworkspace.v2.VisibilityScopeEnum`
        :param current_package_id: 当前生效的技能包id。
        :type current_package_id: str
        :param current_version: 当前生效版本号。
        :type current_version: str
        :param current_revision: 当前生效版本修订号。
        :type current_revision: int
        :param cover: 技能封面图 base64 编码。
        :type cover: str
        :param source: 
        :type source: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        :param support_os_types: 支持的操作系统类型列表。
        :type support_os_types: list[str]
        :param create_time: 创建时间（ISO8601格式，UTC时区）。
        :type create_time: str
        :param update_time: 更新时间（ISO8601格式，UTC时区）。
        :type update_time: str
        :param attach_instance_number: 已绑定实例数量。
        :type attach_instance_number: int
        """
        
        

        self._id = None
        self._slug = None
        self._display_name = None
        self._alias_name = None
        self._category = None
        self._description = None
        self._tags = None
        self._status = None
        self._visibility_scope = None
        self._current_package_id = None
        self._current_version = None
        self._current_revision = None
        self._cover = None
        self._source = None
        self._support_os_types = None
        self._create_time = None
        self._update_time = None
        self._attach_instance_number = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if slug is not None:
            self.slug = slug
        if display_name is not None:
            self.display_name = display_name
        if alias_name is not None:
            self.alias_name = alias_name
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if visibility_scope is not None:
            self.visibility_scope = visibility_scope
        if current_package_id is not None:
            self.current_package_id = current_package_id
        if current_version is not None:
            self.current_version = current_version
        if current_revision is not None:
            self.current_revision = current_revision
        if cover is not None:
            self.cover = cover
        if source is not None:
            self.source = source
        if support_os_types is not None:
            self.support_os_types = support_os_types
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if attach_instance_number is not None:
            self.attach_instance_number = attach_instance_number

    @property
    def id(self):
        r"""Gets the id of this SkillListItemVO.

        技能id。

        :return: The id of this SkillListItemVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SkillListItemVO.

        技能id。

        :param id: The id of this SkillListItemVO.
        :type id: str
        """
        self._id = id

    @property
    def slug(self):
        r"""Gets the slug of this SkillListItemVO.

        技能slug。

        :return: The slug of this SkillListItemVO.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        r"""Sets the slug of this SkillListItemVO.

        技能slug。

        :param slug: The slug of this SkillListItemVO.
        :type slug: str
        """
        self._slug = slug

    @property
    def display_name(self):
        r"""Gets the display_name of this SkillListItemVO.

        技能名称。

        :return: The display_name of this SkillListItemVO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this SkillListItemVO.

        技能名称。

        :param display_name: The display_name of this SkillListItemVO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def alias_name(self):
        r"""Gets the alias_name of this SkillListItemVO.

        别名。

        :return: The alias_name of this SkillListItemVO.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        r"""Sets the alias_name of this SkillListItemVO.

        别名。

        :param alias_name: The alias_name of this SkillListItemVO.
        :type alias_name: str
        """
        self._alias_name = alias_name

    @property
    def category(self):
        r"""Gets the category of this SkillListItemVO.

        :return: The category of this SkillListItemVO.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SkillListItemVO.

        :param category: The category of this SkillListItemVO.
        :type category: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this SkillListItemVO.

        技能描述。

        :return: The description of this SkillListItemVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SkillListItemVO.

        技能描述。

        :param description: The description of this SkillListItemVO.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this SkillListItemVO.

        技能标签。

        :return: The tags of this SkillListItemVO.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SkillListItemVO.

        技能标签。

        :param tags: The tags of this SkillListItemVO.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def status(self):
        r"""Gets the status of this SkillListItemVO.

        :return: The status of this SkillListItemVO.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SkillListItemVO.

        :param status: The status of this SkillListItemVO.
        :type status: :class:`huaweicloudsdkworkspace.v2.SkillStatusEnum`
        """
        self._status = status

    @property
    def visibility_scope(self):
        r"""Gets the visibility_scope of this SkillListItemVO.

        :return: The visibility_scope of this SkillListItemVO.
        :rtype: :class:`huaweicloudsdkworkspace.v2.VisibilityScopeEnum`
        """
        return self._visibility_scope

    @visibility_scope.setter
    def visibility_scope(self, visibility_scope):
        r"""Sets the visibility_scope of this SkillListItemVO.

        :param visibility_scope: The visibility_scope of this SkillListItemVO.
        :type visibility_scope: :class:`huaweicloudsdkworkspace.v2.VisibilityScopeEnum`
        """
        self._visibility_scope = visibility_scope

    @property
    def current_package_id(self):
        r"""Gets the current_package_id of this SkillListItemVO.

        当前生效的技能包id。

        :return: The current_package_id of this SkillListItemVO.
        :rtype: str
        """
        return self._current_package_id

    @current_package_id.setter
    def current_package_id(self, current_package_id):
        r"""Sets the current_package_id of this SkillListItemVO.

        当前生效的技能包id。

        :param current_package_id: The current_package_id of this SkillListItemVO.
        :type current_package_id: str
        """
        self._current_package_id = current_package_id

    @property
    def current_version(self):
        r"""Gets the current_version of this SkillListItemVO.

        当前生效版本号。

        :return: The current_version of this SkillListItemVO.
        :rtype: str
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this SkillListItemVO.

        当前生效版本号。

        :param current_version: The current_version of this SkillListItemVO.
        :type current_version: str
        """
        self._current_version = current_version

    @property
    def current_revision(self):
        r"""Gets the current_revision of this SkillListItemVO.

        当前生效版本修订号。

        :return: The current_revision of this SkillListItemVO.
        :rtype: int
        """
        return self._current_revision

    @current_revision.setter
    def current_revision(self, current_revision):
        r"""Sets the current_revision of this SkillListItemVO.

        当前生效版本修订号。

        :param current_revision: The current_revision of this SkillListItemVO.
        :type current_revision: int
        """
        self._current_revision = current_revision

    @property
    def cover(self):
        r"""Gets the cover of this SkillListItemVO.

        技能封面图 base64 编码。

        :return: The cover of this SkillListItemVO.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        r"""Sets the cover of this SkillListItemVO.

        技能封面图 base64 编码。

        :param cover: The cover of this SkillListItemVO.
        :type cover: str
        """
        self._cover = cover

    @property
    def source(self):
        r"""Gets the source of this SkillListItemVO.

        :return: The source of this SkillListItemVO.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this SkillListItemVO.

        :param source: The source of this SkillListItemVO.
        :type source: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        """
        self._source = source

    @property
    def support_os_types(self):
        r"""Gets the support_os_types of this SkillListItemVO.

        支持的操作系统类型列表。

        :return: The support_os_types of this SkillListItemVO.
        :rtype: list[str]
        """
        return self._support_os_types

    @support_os_types.setter
    def support_os_types(self, support_os_types):
        r"""Sets the support_os_types of this SkillListItemVO.

        支持的操作系统类型列表。

        :param support_os_types: The support_os_types of this SkillListItemVO.
        :type support_os_types: list[str]
        """
        self._support_os_types = support_os_types

    @property
    def create_time(self):
        r"""Gets the create_time of this SkillListItemVO.

        创建时间（ISO8601格式，UTC时区）。

        :return: The create_time of this SkillListItemVO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SkillListItemVO.

        创建时间（ISO8601格式，UTC时区）。

        :param create_time: The create_time of this SkillListItemVO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this SkillListItemVO.

        更新时间（ISO8601格式，UTC时区）。

        :return: The update_time of this SkillListItemVO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SkillListItemVO.

        更新时间（ISO8601格式，UTC时区）。

        :param update_time: The update_time of this SkillListItemVO.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def attach_instance_number(self):
        r"""Gets the attach_instance_number of this SkillListItemVO.

        已绑定实例数量。

        :return: The attach_instance_number of this SkillListItemVO.
        :rtype: int
        """
        return self._attach_instance_number

    @attach_instance_number.setter
    def attach_instance_number(self, attach_instance_number):
        r"""Sets the attach_instance_number of this SkillListItemVO.

        已绑定实例数量。

        :param attach_instance_number: The attach_instance_number of this SkillListItemVO.
        :type attach_instance_number: int
        """
        self._attach_instance_number = attach_instance_number

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
        if not isinstance(other, SkillListItemVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
