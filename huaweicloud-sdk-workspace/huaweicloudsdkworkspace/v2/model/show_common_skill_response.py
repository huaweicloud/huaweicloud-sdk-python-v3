# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCommonSkillResponse(SdkResponse):

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
        'description': 'str',
        'category': 'SkillCategoryEnum',
        'tags': 'list[str]',
        'owner_type': 'SkillOwnerTypeEnum',
        'visibility_scope': 'VisibilityScopeEnum',
        'visible_domain_ids': 'list[str]',
        'status': 'SkillStatusEnum',
        'current_package_id': 'str',
        'cover': 'str',
        'source': 'SkillSourceEnum',
        'support_os_types': 'list[str]',
        'packages': 'list[SkillPackageSummary]',
        'create_time': 'str',
        'update_time': 'str',
        'attach_instance_number': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'slug': 'slug',
        'display_name': 'display_name',
        'alias_name': 'alias_name',
        'description': 'description',
        'category': 'category',
        'tags': 'tags',
        'owner_type': 'owner_type',
        'visibility_scope': 'visibility_scope',
        'visible_domain_ids': 'visible_domain_ids',
        'status': 'status',
        'current_package_id': 'current_package_id',
        'cover': 'cover',
        'source': 'source',
        'support_os_types': 'support_os_types',
        'packages': 'packages',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'attach_instance_number': 'attach_instance_number',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, id=None, slug=None, display_name=None, alias_name=None, description=None, category=None, tags=None, owner_type=None, visibility_scope=None, visible_domain_ids=None, status=None, current_package_id=None, cover=None, source=None, support_os_types=None, packages=None, create_time=None, update_time=None, attach_instance_number=None, x_request_id=None):
        r"""ShowCommonSkillResponse

        The model defined in huaweicloud sdk

        :param id: 技能id。
        :type id: str
        :param slug: 技能slug。
        :type slug: str
        :param display_name: 技能名称。
        :type display_name: str
        :param alias_name: 别名。
        :type alias_name: str
        :param description: 技能描述。
        :type description: str
        :param category: 
        :type category: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        :param tags: 技能标签。
        :type tags: list[str]
        :param owner_type: 
        :type owner_type: :class:`huaweicloudsdkworkspace.v2.SkillOwnerTypeEnum`
        :param visibility_scope: 
        :type visibility_scope: :class:`huaweicloudsdkworkspace.v2.VisibilityScopeEnum`
        :param visible_domain_ids: 可见租户 ID 列表，仅 visibility_scope&#x3D;SPECIFIC_TENANTS 时返回。
        :type visible_domain_ids: list[str]
        :param status: 
        :type status: :class:`huaweicloudsdkworkspace.v2.SkillStatusEnum`
        :param current_package_id: 当前生效的技能包id。
        :type current_package_id: str
        :param cover: 技能封面图 base64 编码。
        :type cover: str
        :param source: 
        :type source: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        :param support_os_types: 支持的操作系统类型列表。
        :type support_os_types: list[str]
        :param packages: 技能包摘要列表。
        :type packages: list[:class:`huaweicloudsdkworkspace.v2.SkillPackageSummary`]
        :param create_time: 创建时间（ISO8601格式，UTC时区）。
        :type create_time: str
        :param update_time: 更新时间（ISO8601格式，UTC时区）。
        :type update_time: str
        :param attach_instance_number: 已绑定实例数量。
        :type attach_instance_number: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._id = None
        self._slug = None
        self._display_name = None
        self._alias_name = None
        self._description = None
        self._category = None
        self._tags = None
        self._owner_type = None
        self._visibility_scope = None
        self._visible_domain_ids = None
        self._status = None
        self._current_package_id = None
        self._cover = None
        self._source = None
        self._support_os_types = None
        self._packages = None
        self._create_time = None
        self._update_time = None
        self._attach_instance_number = None
        self._x_request_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if slug is not None:
            self.slug = slug
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
        if owner_type is not None:
            self.owner_type = owner_type
        if visibility_scope is not None:
            self.visibility_scope = visibility_scope
        if visible_domain_ids is not None:
            self.visible_domain_ids = visible_domain_ids
        if status is not None:
            self.status = status
        if current_package_id is not None:
            self.current_package_id = current_package_id
        if cover is not None:
            self.cover = cover
        if source is not None:
            self.source = source
        if support_os_types is not None:
            self.support_os_types = support_os_types
        if packages is not None:
            self.packages = packages
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if attach_instance_number is not None:
            self.attach_instance_number = attach_instance_number
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def id(self):
        r"""Gets the id of this ShowCommonSkillResponse.

        技能id。

        :return: The id of this ShowCommonSkillResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowCommonSkillResponse.

        技能id。

        :param id: The id of this ShowCommonSkillResponse.
        :type id: str
        """
        self._id = id

    @property
    def slug(self):
        r"""Gets the slug of this ShowCommonSkillResponse.

        技能slug。

        :return: The slug of this ShowCommonSkillResponse.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        r"""Sets the slug of this ShowCommonSkillResponse.

        技能slug。

        :param slug: The slug of this ShowCommonSkillResponse.
        :type slug: str
        """
        self._slug = slug

    @property
    def display_name(self):
        r"""Gets the display_name of this ShowCommonSkillResponse.

        技能名称。

        :return: The display_name of this ShowCommonSkillResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ShowCommonSkillResponse.

        技能名称。

        :param display_name: The display_name of this ShowCommonSkillResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def alias_name(self):
        r"""Gets the alias_name of this ShowCommonSkillResponse.

        别名。

        :return: The alias_name of this ShowCommonSkillResponse.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        r"""Sets the alias_name of this ShowCommonSkillResponse.

        别名。

        :param alias_name: The alias_name of this ShowCommonSkillResponse.
        :type alias_name: str
        """
        self._alias_name = alias_name

    @property
    def description(self):
        r"""Gets the description of this ShowCommonSkillResponse.

        技能描述。

        :return: The description of this ShowCommonSkillResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowCommonSkillResponse.

        技能描述。

        :param description: The description of this ShowCommonSkillResponse.
        :type description: str
        """
        self._description = description

    @property
    def category(self):
        r"""Gets the category of this ShowCommonSkillResponse.

        :return: The category of this ShowCommonSkillResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowCommonSkillResponse.

        :param category: The category of this ShowCommonSkillResponse.
        :type category: :class:`huaweicloudsdkworkspace.v2.SkillCategoryEnum`
        """
        self._category = category

    @property
    def tags(self):
        r"""Gets the tags of this ShowCommonSkillResponse.

        技能标签。

        :return: The tags of this ShowCommonSkillResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowCommonSkillResponse.

        技能标签。

        :param tags: The tags of this ShowCommonSkillResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def owner_type(self):
        r"""Gets the owner_type of this ShowCommonSkillResponse.

        :return: The owner_type of this ShowCommonSkillResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillOwnerTypeEnum`
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this ShowCommonSkillResponse.

        :param owner_type: The owner_type of this ShowCommonSkillResponse.
        :type owner_type: :class:`huaweicloudsdkworkspace.v2.SkillOwnerTypeEnum`
        """
        self._owner_type = owner_type

    @property
    def visibility_scope(self):
        r"""Gets the visibility_scope of this ShowCommonSkillResponse.

        :return: The visibility_scope of this ShowCommonSkillResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.VisibilityScopeEnum`
        """
        return self._visibility_scope

    @visibility_scope.setter
    def visibility_scope(self, visibility_scope):
        r"""Sets the visibility_scope of this ShowCommonSkillResponse.

        :param visibility_scope: The visibility_scope of this ShowCommonSkillResponse.
        :type visibility_scope: :class:`huaweicloudsdkworkspace.v2.VisibilityScopeEnum`
        """
        self._visibility_scope = visibility_scope

    @property
    def visible_domain_ids(self):
        r"""Gets the visible_domain_ids of this ShowCommonSkillResponse.

        可见租户 ID 列表，仅 visibility_scope=SPECIFIC_TENANTS 时返回。

        :return: The visible_domain_ids of this ShowCommonSkillResponse.
        :rtype: list[str]
        """
        return self._visible_domain_ids

    @visible_domain_ids.setter
    def visible_domain_ids(self, visible_domain_ids):
        r"""Sets the visible_domain_ids of this ShowCommonSkillResponse.

        可见租户 ID 列表，仅 visibility_scope=SPECIFIC_TENANTS 时返回。

        :param visible_domain_ids: The visible_domain_ids of this ShowCommonSkillResponse.
        :type visible_domain_ids: list[str]
        """
        self._visible_domain_ids = visible_domain_ids

    @property
    def status(self):
        r"""Gets the status of this ShowCommonSkillResponse.

        :return: The status of this ShowCommonSkillResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowCommonSkillResponse.

        :param status: The status of this ShowCommonSkillResponse.
        :type status: :class:`huaweicloudsdkworkspace.v2.SkillStatusEnum`
        """
        self._status = status

    @property
    def current_package_id(self):
        r"""Gets the current_package_id of this ShowCommonSkillResponse.

        当前生效的技能包id。

        :return: The current_package_id of this ShowCommonSkillResponse.
        :rtype: str
        """
        return self._current_package_id

    @current_package_id.setter
    def current_package_id(self, current_package_id):
        r"""Sets the current_package_id of this ShowCommonSkillResponse.

        当前生效的技能包id。

        :param current_package_id: The current_package_id of this ShowCommonSkillResponse.
        :type current_package_id: str
        """
        self._current_package_id = current_package_id

    @property
    def cover(self):
        r"""Gets the cover of this ShowCommonSkillResponse.

        技能封面图 base64 编码。

        :return: The cover of this ShowCommonSkillResponse.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        r"""Sets the cover of this ShowCommonSkillResponse.

        技能封面图 base64 编码。

        :param cover: The cover of this ShowCommonSkillResponse.
        :type cover: str
        """
        self._cover = cover

    @property
    def source(self):
        r"""Gets the source of this ShowCommonSkillResponse.

        :return: The source of this ShowCommonSkillResponse.
        :rtype: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ShowCommonSkillResponse.

        :param source: The source of this ShowCommonSkillResponse.
        :type source: :class:`huaweicloudsdkworkspace.v2.SkillSourceEnum`
        """
        self._source = source

    @property
    def support_os_types(self):
        r"""Gets the support_os_types of this ShowCommonSkillResponse.

        支持的操作系统类型列表。

        :return: The support_os_types of this ShowCommonSkillResponse.
        :rtype: list[str]
        """
        return self._support_os_types

    @support_os_types.setter
    def support_os_types(self, support_os_types):
        r"""Sets the support_os_types of this ShowCommonSkillResponse.

        支持的操作系统类型列表。

        :param support_os_types: The support_os_types of this ShowCommonSkillResponse.
        :type support_os_types: list[str]
        """
        self._support_os_types = support_os_types

    @property
    def packages(self):
        r"""Gets the packages of this ShowCommonSkillResponse.

        技能包摘要列表。

        :return: The packages of this ShowCommonSkillResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.SkillPackageSummary`]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        r"""Sets the packages of this ShowCommonSkillResponse.

        技能包摘要列表。

        :param packages: The packages of this ShowCommonSkillResponse.
        :type packages: list[:class:`huaweicloudsdkworkspace.v2.SkillPackageSummary`]
        """
        self._packages = packages

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowCommonSkillResponse.

        创建时间（ISO8601格式，UTC时区）。

        :return: The create_time of this ShowCommonSkillResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowCommonSkillResponse.

        创建时间（ISO8601格式，UTC时区）。

        :param create_time: The create_time of this ShowCommonSkillResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowCommonSkillResponse.

        更新时间（ISO8601格式，UTC时区）。

        :return: The update_time of this ShowCommonSkillResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowCommonSkillResponse.

        更新时间（ISO8601格式，UTC时区）。

        :param update_time: The update_time of this ShowCommonSkillResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def attach_instance_number(self):
        r"""Gets the attach_instance_number of this ShowCommonSkillResponse.

        已绑定实例数量。

        :return: The attach_instance_number of this ShowCommonSkillResponse.
        :rtype: int
        """
        return self._attach_instance_number

    @attach_instance_number.setter
    def attach_instance_number(self, attach_instance_number):
        r"""Sets the attach_instance_number of this ShowCommonSkillResponse.

        已绑定实例数量。

        :param attach_instance_number: The attach_instance_number of this ShowCommonSkillResponse.
        :type attach_instance_number: int
        """
        self._attach_instance_number = attach_instance_number

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowCommonSkillResponse.

        :return: The x_request_id of this ShowCommonSkillResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowCommonSkillResponse.

        :param x_request_id: The x_request_id of this ShowCommonSkillResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowCommonSkillResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowCommonSkillResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
