# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupBaseDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'project_name': 'str',
        'ancestor_ids': 'list[int]',
        'ancestor_names': 'list[str]',
        'develop_mode': 'str',
        'id': 'int',
        'name': 'str',
        'path': 'str',
        'group_level': 'int',
        'description': 'str',
        'subgroup_count': 'int',
        'project_count': 'int',
        'group_role': 'int',
        'group_members_count': 'int',
        'descendant_type': 'str',
        'visibility_level': 'int',
        'visibility': 'str',
        'is_project_admin': 'int',
        'is_group_creator': 'int',
        'is_repo_creator': 'int',
        'lfs_enabled': 'bool',
        'full_name': 'str',
        'full_path': 'str',
        'item_type': 'str',
        'parent_id': 'int',
        'my_role': 'GroupMyRoleDtoV4',
        'members': 'int',
        'web_url': 'str',
        'created_at': 'str',
        'sub_group_count': 'int',
        'last_owner': 'bool',
        'starred': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'project_name': 'project_name',
        'ancestor_ids': 'ancestor_ids',
        'ancestor_names': 'ancestor_names',
        'develop_mode': 'develop_mode',
        'id': 'id',
        'name': 'name',
        'path': 'path',
        'group_level': 'group_level',
        'description': 'description',
        'subgroup_count': 'subgroup_count',
        'project_count': 'project_count',
        'group_role': 'group_role',
        'group_members_count': 'group_members_count',
        'descendant_type': 'descendant_type',
        'visibility_level': 'visibility_level',
        'visibility': 'visibility',
        'is_project_admin': 'is_project_admin',
        'is_group_creator': 'is_group_creator',
        'is_repo_creator': 'is_repo_creator',
        'lfs_enabled': 'lfs_enabled',
        'full_name': 'full_name',
        'full_path': 'full_path',
        'item_type': 'item_type',
        'parent_id': 'parent_id',
        'my_role': 'my_role',
        'members': 'members',
        'web_url': 'web_url',
        'created_at': 'created_at',
        'sub_group_count': 'sub_group_count',
        'last_owner': 'last_owner',
        'starred': 'starred'
    }

    def __init__(self, project_id=None, project_name=None, ancestor_ids=None, ancestor_names=None, develop_mode=None, id=None, name=None, path=None, group_level=None, description=None, subgroup_count=None, project_count=None, group_role=None, group_members_count=None, descendant_type=None, visibility_level=None, visibility=None, is_project_admin=None, is_group_creator=None, is_repo_creator=None, lfs_enabled=None, full_name=None, full_path=None, item_type=None, parent_id=None, my_role=None, members=None, web_url=None, created_at=None, sub_group_count=None, last_owner=None, starred=None):
        r"""GroupBaseDto

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type project_id: str
        :param project_name: **参数解释：** 项目名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type project_name: str
        :param ancestor_ids: **参数解释：** 代码组id。
        :type ancestor_ids: list[int]
        :param ancestor_names: **参数解释：** 代码组名称。
        :type ancestor_names: list[str]
        :param develop_mode: **参数解释：** 开发模式，normal，cr。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type develop_mode: str
        :param id: **参数解释：** 记录id。
        :type id: int
        :param name: **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name: str
        :param path: **参数解释：** 路径。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type path: str
        :param group_level: **参数解释：** 代码组层级。
        :type group_level: int
        :param description: **参数解释：** 描述。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type description: str
        :param subgroup_count: **参数解释：** 子代码组数量。
        :type subgroup_count: int
        :param project_count: **参数解释：** 仓库数量。
        :type project_count: int
        :param group_role: **参数解释：** 代码组角色。
        :type group_role: int
        :param group_members_count: **参数解释：** 代码组成员数量。
        :type group_members_count: int
        :param descendant_type: **参数解释：** 类型。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type descendant_type: str
        :param visibility_level: **参数解释：** 可见性 0 20。
        :type visibility_level: int
        :param visibility: **参数解释：** 可见性 private public。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type visibility: str
        :param is_project_admin: **参数解释：** 是否为项目创建者。
        :type is_project_admin: int
        :param is_group_creator: **参数解释：** 是否为代码组创建者。
        :type is_group_creator: int
        :param is_repo_creator: **参数解释：** 是否为仓库创建者。
        :type is_repo_creator: int
        :param lfs_enabled: **参数解释：** lfs是否开启。
        :type lfs_enabled: bool
        :param full_name: **参数解释：** 全名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type full_name: str
        :param full_path: **参数解释：** 全路径。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type full_path: str
        :param item_type: **参数解释：** item类型。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type item_type: str
        :param parent_id: **参数解释：** 父代码组id。
        :type parent_id: int
        :param my_role: 
        :type my_role: :class:`huaweicloudsdkcodehub.v4.GroupMyRoleDtoV4`
        :param members: **参数解释：** 成员。
        :type members: int
        :param web_url: **参数解释：** url地址。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type web_url: str
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type created_at: str
        :param sub_group_count: **参数解释：** 子代码组数量。
        :type sub_group_count: int
        :param last_owner: **参数解释：** 是否为最后所有者。
        :type last_owner: bool
        :param starred: **参数解释：** 是否关注。
        :type starred: bool
        """
        
        

        self._project_id = None
        self._project_name = None
        self._ancestor_ids = None
        self._ancestor_names = None
        self._develop_mode = None
        self._id = None
        self._name = None
        self._path = None
        self._group_level = None
        self._description = None
        self._subgroup_count = None
        self._project_count = None
        self._group_role = None
        self._group_members_count = None
        self._descendant_type = None
        self._visibility_level = None
        self._visibility = None
        self._is_project_admin = None
        self._is_group_creator = None
        self._is_repo_creator = None
        self._lfs_enabled = None
        self._full_name = None
        self._full_path = None
        self._item_type = None
        self._parent_id = None
        self._my_role = None
        self._members = None
        self._web_url = None
        self._created_at = None
        self._sub_group_count = None
        self._last_owner = None
        self._starred = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if ancestor_ids is not None:
            self.ancestor_ids = ancestor_ids
        if ancestor_names is not None:
            self.ancestor_names = ancestor_names
        if develop_mode is not None:
            self.develop_mode = develop_mode
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if group_level is not None:
            self.group_level = group_level
        if description is not None:
            self.description = description
        if subgroup_count is not None:
            self.subgroup_count = subgroup_count
        if project_count is not None:
            self.project_count = project_count
        if group_role is not None:
            self.group_role = group_role
        if group_members_count is not None:
            self.group_members_count = group_members_count
        if descendant_type is not None:
            self.descendant_type = descendant_type
        if visibility_level is not None:
            self.visibility_level = visibility_level
        if visibility is not None:
            self.visibility = visibility
        if is_project_admin is not None:
            self.is_project_admin = is_project_admin
        if is_group_creator is not None:
            self.is_group_creator = is_group_creator
        if is_repo_creator is not None:
            self.is_repo_creator = is_repo_creator
        if lfs_enabled is not None:
            self.lfs_enabled = lfs_enabled
        if full_name is not None:
            self.full_name = full_name
        if full_path is not None:
            self.full_path = full_path
        if item_type is not None:
            self.item_type = item_type
        if parent_id is not None:
            self.parent_id = parent_id
        if my_role is not None:
            self.my_role = my_role
        if members is not None:
            self.members = members
        if web_url is not None:
            self.web_url = web_url
        if created_at is not None:
            self.created_at = created_at
        if sub_group_count is not None:
            self.sub_group_count = sub_group_count
        if last_owner is not None:
            self.last_owner = last_owner
        if starred is not None:
            self.starred = starred

    @property
    def project_id(self):
        r"""Gets the project_id of this GroupBaseDto.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The project_id of this GroupBaseDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this GroupBaseDto.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param project_id: The project_id of this GroupBaseDto.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this GroupBaseDto.

        **参数解释：** 项目名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The project_name of this GroupBaseDto.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this GroupBaseDto.

        **参数解释：** 项目名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param project_name: The project_name of this GroupBaseDto.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def ancestor_ids(self):
        r"""Gets the ancestor_ids of this GroupBaseDto.

        **参数解释：** 代码组id。

        :return: The ancestor_ids of this GroupBaseDto.
        :rtype: list[int]
        """
        return self._ancestor_ids

    @ancestor_ids.setter
    def ancestor_ids(self, ancestor_ids):
        r"""Sets the ancestor_ids of this GroupBaseDto.

        **参数解释：** 代码组id。

        :param ancestor_ids: The ancestor_ids of this GroupBaseDto.
        :type ancestor_ids: list[int]
        """
        self._ancestor_ids = ancestor_ids

    @property
    def ancestor_names(self):
        r"""Gets the ancestor_names of this GroupBaseDto.

        **参数解释：** 代码组名称。

        :return: The ancestor_names of this GroupBaseDto.
        :rtype: list[str]
        """
        return self._ancestor_names

    @ancestor_names.setter
    def ancestor_names(self, ancestor_names):
        r"""Sets the ancestor_names of this GroupBaseDto.

        **参数解释：** 代码组名称。

        :param ancestor_names: The ancestor_names of this GroupBaseDto.
        :type ancestor_names: list[str]
        """
        self._ancestor_names = ancestor_names

    @property
    def develop_mode(self):
        r"""Gets the develop_mode of this GroupBaseDto.

        **参数解释：** 开发模式，normal，cr。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The develop_mode of this GroupBaseDto.
        :rtype: str
        """
        return self._develop_mode

    @develop_mode.setter
    def develop_mode(self, develop_mode):
        r"""Sets the develop_mode of this GroupBaseDto.

        **参数解释：** 开发模式，normal，cr。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param develop_mode: The develop_mode of this GroupBaseDto.
        :type develop_mode: str
        """
        self._develop_mode = develop_mode

    @property
    def id(self):
        r"""Gets the id of this GroupBaseDto.

        **参数解释：** 记录id。

        :return: The id of this GroupBaseDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GroupBaseDto.

        **参数解释：** 记录id。

        :param id: The id of this GroupBaseDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this GroupBaseDto.

        **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name of this GroupBaseDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GroupBaseDto.

        **参数解释：** 名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name: The name of this GroupBaseDto.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        r"""Gets the path of this GroupBaseDto.

        **参数解释：** 路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The path of this GroupBaseDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this GroupBaseDto.

        **参数解释：** 路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param path: The path of this GroupBaseDto.
        :type path: str
        """
        self._path = path

    @property
    def group_level(self):
        r"""Gets the group_level of this GroupBaseDto.

        **参数解释：** 代码组层级。

        :return: The group_level of this GroupBaseDto.
        :rtype: int
        """
        return self._group_level

    @group_level.setter
    def group_level(self, group_level):
        r"""Sets the group_level of this GroupBaseDto.

        **参数解释：** 代码组层级。

        :param group_level: The group_level of this GroupBaseDto.
        :type group_level: int
        """
        self._group_level = group_level

    @property
    def description(self):
        r"""Gets the description of this GroupBaseDto.

        **参数解释：** 描述。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The description of this GroupBaseDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this GroupBaseDto.

        **参数解释：** 描述。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param description: The description of this GroupBaseDto.
        :type description: str
        """
        self._description = description

    @property
    def subgroup_count(self):
        r"""Gets the subgroup_count of this GroupBaseDto.

        **参数解释：** 子代码组数量。

        :return: The subgroup_count of this GroupBaseDto.
        :rtype: int
        """
        return self._subgroup_count

    @subgroup_count.setter
    def subgroup_count(self, subgroup_count):
        r"""Sets the subgroup_count of this GroupBaseDto.

        **参数解释：** 子代码组数量。

        :param subgroup_count: The subgroup_count of this GroupBaseDto.
        :type subgroup_count: int
        """
        self._subgroup_count = subgroup_count

    @property
    def project_count(self):
        r"""Gets the project_count of this GroupBaseDto.

        **参数解释：** 仓库数量。

        :return: The project_count of this GroupBaseDto.
        :rtype: int
        """
        return self._project_count

    @project_count.setter
    def project_count(self, project_count):
        r"""Sets the project_count of this GroupBaseDto.

        **参数解释：** 仓库数量。

        :param project_count: The project_count of this GroupBaseDto.
        :type project_count: int
        """
        self._project_count = project_count

    @property
    def group_role(self):
        r"""Gets the group_role of this GroupBaseDto.

        **参数解释：** 代码组角色。

        :return: The group_role of this GroupBaseDto.
        :rtype: int
        """
        return self._group_role

    @group_role.setter
    def group_role(self, group_role):
        r"""Sets the group_role of this GroupBaseDto.

        **参数解释：** 代码组角色。

        :param group_role: The group_role of this GroupBaseDto.
        :type group_role: int
        """
        self._group_role = group_role

    @property
    def group_members_count(self):
        r"""Gets the group_members_count of this GroupBaseDto.

        **参数解释：** 代码组成员数量。

        :return: The group_members_count of this GroupBaseDto.
        :rtype: int
        """
        return self._group_members_count

    @group_members_count.setter
    def group_members_count(self, group_members_count):
        r"""Sets the group_members_count of this GroupBaseDto.

        **参数解释：** 代码组成员数量。

        :param group_members_count: The group_members_count of this GroupBaseDto.
        :type group_members_count: int
        """
        self._group_members_count = group_members_count

    @property
    def descendant_type(self):
        r"""Gets the descendant_type of this GroupBaseDto.

        **参数解释：** 类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The descendant_type of this GroupBaseDto.
        :rtype: str
        """
        return self._descendant_type

    @descendant_type.setter
    def descendant_type(self, descendant_type):
        r"""Sets the descendant_type of this GroupBaseDto.

        **参数解释：** 类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param descendant_type: The descendant_type of this GroupBaseDto.
        :type descendant_type: str
        """
        self._descendant_type = descendant_type

    @property
    def visibility_level(self):
        r"""Gets the visibility_level of this GroupBaseDto.

        **参数解释：** 可见性 0 20。

        :return: The visibility_level of this GroupBaseDto.
        :rtype: int
        """
        return self._visibility_level

    @visibility_level.setter
    def visibility_level(self, visibility_level):
        r"""Sets the visibility_level of this GroupBaseDto.

        **参数解释：** 可见性 0 20。

        :param visibility_level: The visibility_level of this GroupBaseDto.
        :type visibility_level: int
        """
        self._visibility_level = visibility_level

    @property
    def visibility(self):
        r"""Gets the visibility of this GroupBaseDto.

        **参数解释：** 可见性 private public。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The visibility of this GroupBaseDto.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this GroupBaseDto.

        **参数解释：** 可见性 private public。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param visibility: The visibility of this GroupBaseDto.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def is_project_admin(self):
        r"""Gets the is_project_admin of this GroupBaseDto.

        **参数解释：** 是否为项目创建者。

        :return: The is_project_admin of this GroupBaseDto.
        :rtype: int
        """
        return self._is_project_admin

    @is_project_admin.setter
    def is_project_admin(self, is_project_admin):
        r"""Sets the is_project_admin of this GroupBaseDto.

        **参数解释：** 是否为项目创建者。

        :param is_project_admin: The is_project_admin of this GroupBaseDto.
        :type is_project_admin: int
        """
        self._is_project_admin = is_project_admin

    @property
    def is_group_creator(self):
        r"""Gets the is_group_creator of this GroupBaseDto.

        **参数解释：** 是否为代码组创建者。

        :return: The is_group_creator of this GroupBaseDto.
        :rtype: int
        """
        return self._is_group_creator

    @is_group_creator.setter
    def is_group_creator(self, is_group_creator):
        r"""Sets the is_group_creator of this GroupBaseDto.

        **参数解释：** 是否为代码组创建者。

        :param is_group_creator: The is_group_creator of this GroupBaseDto.
        :type is_group_creator: int
        """
        self._is_group_creator = is_group_creator

    @property
    def is_repo_creator(self):
        r"""Gets the is_repo_creator of this GroupBaseDto.

        **参数解释：** 是否为仓库创建者。

        :return: The is_repo_creator of this GroupBaseDto.
        :rtype: int
        """
        return self._is_repo_creator

    @is_repo_creator.setter
    def is_repo_creator(self, is_repo_creator):
        r"""Sets the is_repo_creator of this GroupBaseDto.

        **参数解释：** 是否为仓库创建者。

        :param is_repo_creator: The is_repo_creator of this GroupBaseDto.
        :type is_repo_creator: int
        """
        self._is_repo_creator = is_repo_creator

    @property
    def lfs_enabled(self):
        r"""Gets the lfs_enabled of this GroupBaseDto.

        **参数解释：** lfs是否开启。

        :return: The lfs_enabled of this GroupBaseDto.
        :rtype: bool
        """
        return self._lfs_enabled

    @lfs_enabled.setter
    def lfs_enabled(self, lfs_enabled):
        r"""Sets the lfs_enabled of this GroupBaseDto.

        **参数解释：** lfs是否开启。

        :param lfs_enabled: The lfs_enabled of this GroupBaseDto.
        :type lfs_enabled: bool
        """
        self._lfs_enabled = lfs_enabled

    @property
    def full_name(self):
        r"""Gets the full_name of this GroupBaseDto.

        **参数解释：** 全名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The full_name of this GroupBaseDto.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        r"""Sets the full_name of this GroupBaseDto.

        **参数解释：** 全名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param full_name: The full_name of this GroupBaseDto.
        :type full_name: str
        """
        self._full_name = full_name

    @property
    def full_path(self):
        r"""Gets the full_path of this GroupBaseDto.

        **参数解释：** 全路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The full_path of this GroupBaseDto.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        r"""Sets the full_path of this GroupBaseDto.

        **参数解释：** 全路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param full_path: The full_path of this GroupBaseDto.
        :type full_path: str
        """
        self._full_path = full_path

    @property
    def item_type(self):
        r"""Gets the item_type of this GroupBaseDto.

        **参数解释：** item类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The item_type of this GroupBaseDto.
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        r"""Sets the item_type of this GroupBaseDto.

        **参数解释：** item类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param item_type: The item_type of this GroupBaseDto.
        :type item_type: str
        """
        self._item_type = item_type

    @property
    def parent_id(self):
        r"""Gets the parent_id of this GroupBaseDto.

        **参数解释：** 父代码组id。

        :return: The parent_id of this GroupBaseDto.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this GroupBaseDto.

        **参数解释：** 父代码组id。

        :param parent_id: The parent_id of this GroupBaseDto.
        :type parent_id: int
        """
        self._parent_id = parent_id

    @property
    def my_role(self):
        r"""Gets the my_role of this GroupBaseDto.

        :return: The my_role of this GroupBaseDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.GroupMyRoleDtoV4`
        """
        return self._my_role

    @my_role.setter
    def my_role(self, my_role):
        r"""Sets the my_role of this GroupBaseDto.

        :param my_role: The my_role of this GroupBaseDto.
        :type my_role: :class:`huaweicloudsdkcodehub.v4.GroupMyRoleDtoV4`
        """
        self._my_role = my_role

    @property
    def members(self):
        r"""Gets the members of this GroupBaseDto.

        **参数解释：** 成员。

        :return: The members of this GroupBaseDto.
        :rtype: int
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this GroupBaseDto.

        **参数解释：** 成员。

        :param members: The members of this GroupBaseDto.
        :type members: int
        """
        self._members = members

    @property
    def web_url(self):
        r"""Gets the web_url of this GroupBaseDto.

        **参数解释：** url地址。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The web_url of this GroupBaseDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this GroupBaseDto.

        **参数解释：** url地址。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param web_url: The web_url of this GroupBaseDto.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def created_at(self):
        r"""Gets the created_at of this GroupBaseDto.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The created_at of this GroupBaseDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this GroupBaseDto.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param created_at: The created_at of this GroupBaseDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def sub_group_count(self):
        r"""Gets the sub_group_count of this GroupBaseDto.

        **参数解释：** 子代码组数量。

        :return: The sub_group_count of this GroupBaseDto.
        :rtype: int
        """
        return self._sub_group_count

    @sub_group_count.setter
    def sub_group_count(self, sub_group_count):
        r"""Sets the sub_group_count of this GroupBaseDto.

        **参数解释：** 子代码组数量。

        :param sub_group_count: The sub_group_count of this GroupBaseDto.
        :type sub_group_count: int
        """
        self._sub_group_count = sub_group_count

    @property
    def last_owner(self):
        r"""Gets the last_owner of this GroupBaseDto.

        **参数解释：** 是否为最后所有者。

        :return: The last_owner of this GroupBaseDto.
        :rtype: bool
        """
        return self._last_owner

    @last_owner.setter
    def last_owner(self, last_owner):
        r"""Sets the last_owner of this GroupBaseDto.

        **参数解释：** 是否为最后所有者。

        :param last_owner: The last_owner of this GroupBaseDto.
        :type last_owner: bool
        """
        self._last_owner = last_owner

    @property
    def starred(self):
        r"""Gets the starred of this GroupBaseDto.

        **参数解释：** 是否关注。

        :return: The starred of this GroupBaseDto.
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        r"""Sets the starred of this GroupBaseDto.

        **参数解释：** 是否关注。

        :param starred: The starred of this GroupBaseDto.
        :type starred: bool
        """
        self._starred = starred

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
        if not isinstance(other, GroupBaseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
