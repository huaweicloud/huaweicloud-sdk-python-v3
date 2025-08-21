# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubgroupAndProjectBaseDto:

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
        'role_namecn': 'str',
        'role_nameen': 'str',
        'full_name': 'str',
        'full_path': 'str',
        'created_at': 'str',
        'updated_at_timestamp': 'str',
        'star_time': 'str',
        'starred': 'bool',
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
        'role_show_flag': 'int',
        'uuid': 'str',
        'forks_count': 'int',
        'is_kia': 'bool',
        'is_owner': 'bool',
        'archived': 'bool',
        'last_repository_updated_at': 'str',
        'open_merge_requests_count': 'int',
        'all_merge_requests_count': 'int',
        'project_role': 'int',
        'project_members_count': 'int',
        'project_creator': 'ProjectCreatorDto',
        'star_count': 'int',
        'tag_list': 'list[str]',
        'http_url_to_repo': 'str',
        'ssh_url_to_repo': 'str',
        'status': 'int',
        'active_statistic': 'list[int]',
        'security_tag': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'project_name': 'project_name',
        'role_namecn': 'role_namecn',
        'role_nameen': 'role_nameen',
        'full_name': 'full_name',
        'full_path': 'full_path',
        'created_at': 'created_at',
        'updated_at_timestamp': 'updated_at_timestamp',
        'star_time': 'star_time',
        'starred': 'starred',
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
        'role_show_flag': 'role_show_flag',
        'uuid': 'uuid',
        'forks_count': 'forks_count',
        'is_kia': 'is_kia',
        'is_owner': 'is_owner',
        'archived': 'archived',
        'last_repository_updated_at': 'last_repository_updated_at',
        'open_merge_requests_count': 'open_merge_requests_count',
        'all_merge_requests_count': 'all_merge_requests_count',
        'project_role': 'project_role',
        'project_members_count': 'project_members_count',
        'project_creator': 'project_creator',
        'star_count': 'star_count',
        'tag_list': 'tag_list',
        'http_url_to_repo': 'http_url_to_repo',
        'ssh_url_to_repo': 'ssh_url_to_repo',
        'status': 'status',
        'active_statistic': 'active_statistic',
        'security_tag': 'security_tag'
    }

    def __init__(self, project_id=None, project_name=None, role_namecn=None, role_nameen=None, full_name=None, full_path=None, created_at=None, updated_at_timestamp=None, star_time=None, starred=None, develop_mode=None, id=None, name=None, path=None, group_level=None, description=None, subgroup_count=None, project_count=None, group_role=None, group_members_count=None, descendant_type=None, visibility_level=None, visibility=None, is_project_admin=None, is_group_creator=None, is_repo_creator=None, role_show_flag=None, uuid=None, forks_count=None, is_kia=None, is_owner=None, archived=None, last_repository_updated_at=None, open_merge_requests_count=None, all_merge_requests_count=None, project_role=None, project_members_count=None, project_creator=None, star_count=None, tag_list=None, http_url_to_repo=None, ssh_url_to_repo=None, status=None, active_statistic=None, security_tag=None):
        r"""SubgroupAndProjectBaseDto

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type project_id: str
        :param project_name: **参数解释：** 项目名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type project_name: str
        :param role_namecn: **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_namecn: str
        :param role_nameen: **参数解释：** 角色英文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_nameen: str
        :param full_name: **参数解释：** 全名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type full_name: str
        :param full_path: **参数解释：** 全路径。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type full_path: str
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type created_at: str
        :param updated_at_timestamp: **参数解释：** 更新时间戳。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type updated_at_timestamp: str
        :param star_time: **参数解释：** 开始时间戳。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type star_time: str
        :param starred: **参数解释：** 是否收藏。
        :type starred: bool
        :param develop_mode: **参数解释：** 开发模式，cr,\&quot;normal\&quot;。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type develop_mode: str
        :param id: **参数解释：** 仓库或者代码组id。
        :type id: int
        :param name: **参数解释：** 代码组或仓库名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type name: str
        :param path: **参数解释：** 路径。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type path: str
        :param group_level: **参数解释：** 代码组层级。
        :type group_level: int
        :param description: **参数解释：** 代码组或仓库描述。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type description: str
        :param subgroup_count: **参数解释：** 子代码组数量。
        :type subgroup_count: int
        :param project_count: **参数解释：** 仓库数量。
        :type project_count: int
        :param group_role: **参数解释：** 代码组角色。
        :type group_role: int
        :param group_members_count: **参数解释：** 代码组成员数量。
        :type group_members_count: int
        :param descendant_type: **参数解释：** 资源类型 group,project。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type descendant_type: str
        :param visibility_level: **参数解释：** 可见性level 0(私有),20(公开)
        :type visibility_level: int
        :param visibility: **参数解释：** 可见性 private public。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type visibility: str
        :param is_project_admin: **参数解释：** 当前用户是否为项目创建者。
        :type is_project_admin: int
        :param is_group_creator: **参数解释：** 当前用户是否为代码组创建者。
        :type is_group_creator: int
        :param is_repo_creator: **参数解释：** 当前用户是否为仓库创建者。
        :type is_repo_creator: int
        :param role_show_flag: **参数解释：** 角色展示标记。
        :type role_show_flag: int
        :param uuid: **参数解释：** 仓库的uuid。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type uuid: str
        :param forks_count: **参数解释：** fork数量。
        :type forks_count: int
        :param is_kia: **参数解释：** 是否为kia。
        :type is_kia: bool
        :param is_owner: **参数解释：** 是否为所有者。
        :type is_owner: bool
        :param archived: **参数解释：** 是否为存档。
        :type archived: bool
        :param last_repository_updated_at: **参数解释：** 仓库的最后更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type last_repository_updated_at: str
        :param open_merge_requests_count: **参数解释：** 开启的mr数量。
        :type open_merge_requests_count: int
        :param all_merge_requests_count: **参数解释：** 所有的mr数量。
        :type all_merge_requests_count: int
        :param project_role: **参数解释：** 仓库角色。
        :type project_role: int
        :param project_members_count: **参数解释：** fork数量。
        :type project_members_count: int
        :param project_creator: 
        :type project_creator: :class:`huaweicloudsdkcodehub.v4.ProjectCreatorDto`
        :param star_count: **参数解释：** fork数量。
        :type star_count: int
        :param tag_list: **参数解释：** tag列表。
        :type tag_list: list[str]
        :param http_url_to_repo: **参数解释：** 仓库的http url。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type http_url_to_repo: str
        :param ssh_url_to_repo: **参数解释：** 仓库的ssh url。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type ssh_url_to_repo: str
        :param status: **参数解释：** 状态。
        :type status: int
        :param active_statistic: **参数解释：** 活跃统计。
        :type active_statistic: list[int]
        :param security_tag: **参数解释：** 安全标签。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type security_tag: str
        """
        
        

        self._project_id = None
        self._project_name = None
        self._role_namecn = None
        self._role_nameen = None
        self._full_name = None
        self._full_path = None
        self._created_at = None
        self._updated_at_timestamp = None
        self._star_time = None
        self._starred = None
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
        self._role_show_flag = None
        self._uuid = None
        self._forks_count = None
        self._is_kia = None
        self._is_owner = None
        self._archived = None
        self._last_repository_updated_at = None
        self._open_merge_requests_count = None
        self._all_merge_requests_count = None
        self._project_role = None
        self._project_members_count = None
        self._project_creator = None
        self._star_count = None
        self._tag_list = None
        self._http_url_to_repo = None
        self._ssh_url_to_repo = None
        self._status = None
        self._active_statistic = None
        self._security_tag = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if role_namecn is not None:
            self.role_namecn = role_namecn
        if role_nameen is not None:
            self.role_nameen = role_nameen
        if full_name is not None:
            self.full_name = full_name
        if full_path is not None:
            self.full_path = full_path
        if created_at is not None:
            self.created_at = created_at
        if updated_at_timestamp is not None:
            self.updated_at_timestamp = updated_at_timestamp
        if star_time is not None:
            self.star_time = star_time
        if starred is not None:
            self.starred = starred
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
        if role_show_flag is not None:
            self.role_show_flag = role_show_flag
        if uuid is not None:
            self.uuid = uuid
        if forks_count is not None:
            self.forks_count = forks_count
        if is_kia is not None:
            self.is_kia = is_kia
        if is_owner is not None:
            self.is_owner = is_owner
        if archived is not None:
            self.archived = archived
        if last_repository_updated_at is not None:
            self.last_repository_updated_at = last_repository_updated_at
        if open_merge_requests_count is not None:
            self.open_merge_requests_count = open_merge_requests_count
        if all_merge_requests_count is not None:
            self.all_merge_requests_count = all_merge_requests_count
        if project_role is not None:
            self.project_role = project_role
        if project_members_count is not None:
            self.project_members_count = project_members_count
        if project_creator is not None:
            self.project_creator = project_creator
        if star_count is not None:
            self.star_count = star_count
        if tag_list is not None:
            self.tag_list = tag_list
        if http_url_to_repo is not None:
            self.http_url_to_repo = http_url_to_repo
        if ssh_url_to_repo is not None:
            self.ssh_url_to_repo = ssh_url_to_repo
        if status is not None:
            self.status = status
        if active_statistic is not None:
            self.active_statistic = active_statistic
        if security_tag is not None:
            self.security_tag = security_tag

    @property
    def project_id(self):
        r"""Gets the project_id of this SubgroupAndProjectBaseDto.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The project_id of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this SubgroupAndProjectBaseDto.

        **参数解释：** 项目id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param project_id: The project_id of this SubgroupAndProjectBaseDto.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this SubgroupAndProjectBaseDto.

        **参数解释：** 项目名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The project_name of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this SubgroupAndProjectBaseDto.

        **参数解释：** 项目名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param project_name: The project_name of this SubgroupAndProjectBaseDto.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def role_namecn(self):
        r"""Gets the role_namecn of this SubgroupAndProjectBaseDto.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_namecn of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._role_namecn

    @role_namecn.setter
    def role_namecn(self, role_namecn):
        r"""Sets the role_namecn of this SubgroupAndProjectBaseDto.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_namecn: The role_namecn of this SubgroupAndProjectBaseDto.
        :type role_namecn: str
        """
        self._role_namecn = role_namecn

    @property
    def role_nameen(self):
        r"""Gets the role_nameen of this SubgroupAndProjectBaseDto.

        **参数解释：** 角色英文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_nameen of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._role_nameen

    @role_nameen.setter
    def role_nameen(self, role_nameen):
        r"""Sets the role_nameen of this SubgroupAndProjectBaseDto.

        **参数解释：** 角色英文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_nameen: The role_nameen of this SubgroupAndProjectBaseDto.
        :type role_nameen: str
        """
        self._role_nameen = role_nameen

    @property
    def full_name(self):
        r"""Gets the full_name of this SubgroupAndProjectBaseDto.

        **参数解释：** 全名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The full_name of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        r"""Sets the full_name of this SubgroupAndProjectBaseDto.

        **参数解释：** 全名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param full_name: The full_name of this SubgroupAndProjectBaseDto.
        :type full_name: str
        """
        self._full_name = full_name

    @property
    def full_path(self):
        r"""Gets the full_path of this SubgroupAndProjectBaseDto.

        **参数解释：** 全路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The full_path of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._full_path

    @full_path.setter
    def full_path(self, full_path):
        r"""Sets the full_path of this SubgroupAndProjectBaseDto.

        **参数解释：** 全路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param full_path: The full_path of this SubgroupAndProjectBaseDto.
        :type full_path: str
        """
        self._full_path = full_path

    @property
    def created_at(self):
        r"""Gets the created_at of this SubgroupAndProjectBaseDto.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The created_at of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SubgroupAndProjectBaseDto.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param created_at: The created_at of this SubgroupAndProjectBaseDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at_timestamp(self):
        r"""Gets the updated_at_timestamp of this SubgroupAndProjectBaseDto.

        **参数解释：** 更新时间戳。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The updated_at_timestamp of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._updated_at_timestamp

    @updated_at_timestamp.setter
    def updated_at_timestamp(self, updated_at_timestamp):
        r"""Sets the updated_at_timestamp of this SubgroupAndProjectBaseDto.

        **参数解释：** 更新时间戳。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param updated_at_timestamp: The updated_at_timestamp of this SubgroupAndProjectBaseDto.
        :type updated_at_timestamp: str
        """
        self._updated_at_timestamp = updated_at_timestamp

    @property
    def star_time(self):
        r"""Gets the star_time of this SubgroupAndProjectBaseDto.

        **参数解释：** 开始时间戳。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The star_time of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._star_time

    @star_time.setter
    def star_time(self, star_time):
        r"""Sets the star_time of this SubgroupAndProjectBaseDto.

        **参数解释：** 开始时间戳。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param star_time: The star_time of this SubgroupAndProjectBaseDto.
        :type star_time: str
        """
        self._star_time = star_time

    @property
    def starred(self):
        r"""Gets the starred of this SubgroupAndProjectBaseDto.

        **参数解释：** 是否收藏。

        :return: The starred of this SubgroupAndProjectBaseDto.
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        r"""Sets the starred of this SubgroupAndProjectBaseDto.

        **参数解释：** 是否收藏。

        :param starred: The starred of this SubgroupAndProjectBaseDto.
        :type starred: bool
        """
        self._starred = starred

    @property
    def develop_mode(self):
        r"""Gets the develop_mode of this SubgroupAndProjectBaseDto.

        **参数解释：** 开发模式，cr,\"normal\"。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The develop_mode of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._develop_mode

    @develop_mode.setter
    def develop_mode(self, develop_mode):
        r"""Sets the develop_mode of this SubgroupAndProjectBaseDto.

        **参数解释：** 开发模式，cr,\"normal\"。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param develop_mode: The develop_mode of this SubgroupAndProjectBaseDto.
        :type develop_mode: str
        """
        self._develop_mode = develop_mode

    @property
    def id(self):
        r"""Gets the id of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库或者代码组id。

        :return: The id of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库或者代码组id。

        :param id: The id of this SubgroupAndProjectBaseDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SubgroupAndProjectBaseDto.

        **参数解释：** 代码组或仓库名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The name of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SubgroupAndProjectBaseDto.

        **参数解释：** 代码组或仓库名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param name: The name of this SubgroupAndProjectBaseDto.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        r"""Gets the path of this SubgroupAndProjectBaseDto.

        **参数解释：** 路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The path of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this SubgroupAndProjectBaseDto.

        **参数解释：** 路径。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param path: The path of this SubgroupAndProjectBaseDto.
        :type path: str
        """
        self._path = path

    @property
    def group_level(self):
        r"""Gets the group_level of this SubgroupAndProjectBaseDto.

        **参数解释：** 代码组层级。

        :return: The group_level of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._group_level

    @group_level.setter
    def group_level(self, group_level):
        r"""Sets the group_level of this SubgroupAndProjectBaseDto.

        **参数解释：** 代码组层级。

        :param group_level: The group_level of this SubgroupAndProjectBaseDto.
        :type group_level: int
        """
        self._group_level = group_level

    @property
    def description(self):
        r"""Gets the description of this SubgroupAndProjectBaseDto.

        **参数解释：** 代码组或仓库描述。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The description of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SubgroupAndProjectBaseDto.

        **参数解释：** 代码组或仓库描述。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param description: The description of this SubgroupAndProjectBaseDto.
        :type description: str
        """
        self._description = description

    @property
    def subgroup_count(self):
        r"""Gets the subgroup_count of this SubgroupAndProjectBaseDto.

        **参数解释：** 子代码组数量。

        :return: The subgroup_count of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._subgroup_count

    @subgroup_count.setter
    def subgroup_count(self, subgroup_count):
        r"""Sets the subgroup_count of this SubgroupAndProjectBaseDto.

        **参数解释：** 子代码组数量。

        :param subgroup_count: The subgroup_count of this SubgroupAndProjectBaseDto.
        :type subgroup_count: int
        """
        self._subgroup_count = subgroup_count

    @property
    def project_count(self):
        r"""Gets the project_count of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库数量。

        :return: The project_count of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._project_count

    @project_count.setter
    def project_count(self, project_count):
        r"""Sets the project_count of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库数量。

        :param project_count: The project_count of this SubgroupAndProjectBaseDto.
        :type project_count: int
        """
        self._project_count = project_count

    @property
    def group_role(self):
        r"""Gets the group_role of this SubgroupAndProjectBaseDto.

        **参数解释：** 代码组角色。

        :return: The group_role of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._group_role

    @group_role.setter
    def group_role(self, group_role):
        r"""Sets the group_role of this SubgroupAndProjectBaseDto.

        **参数解释：** 代码组角色。

        :param group_role: The group_role of this SubgroupAndProjectBaseDto.
        :type group_role: int
        """
        self._group_role = group_role

    @property
    def group_members_count(self):
        r"""Gets the group_members_count of this SubgroupAndProjectBaseDto.

        **参数解释：** 代码组成员数量。

        :return: The group_members_count of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._group_members_count

    @group_members_count.setter
    def group_members_count(self, group_members_count):
        r"""Sets the group_members_count of this SubgroupAndProjectBaseDto.

        **参数解释：** 代码组成员数量。

        :param group_members_count: The group_members_count of this SubgroupAndProjectBaseDto.
        :type group_members_count: int
        """
        self._group_members_count = group_members_count

    @property
    def descendant_type(self):
        r"""Gets the descendant_type of this SubgroupAndProjectBaseDto.

        **参数解释：** 资源类型 group,project。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The descendant_type of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._descendant_type

    @descendant_type.setter
    def descendant_type(self, descendant_type):
        r"""Sets the descendant_type of this SubgroupAndProjectBaseDto.

        **参数解释：** 资源类型 group,project。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param descendant_type: The descendant_type of this SubgroupAndProjectBaseDto.
        :type descendant_type: str
        """
        self._descendant_type = descendant_type

    @property
    def visibility_level(self):
        r"""Gets the visibility_level of this SubgroupAndProjectBaseDto.

        **参数解释：** 可见性level 0(私有),20(公开)

        :return: The visibility_level of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._visibility_level

    @visibility_level.setter
    def visibility_level(self, visibility_level):
        r"""Sets the visibility_level of this SubgroupAndProjectBaseDto.

        **参数解释：** 可见性level 0(私有),20(公开)

        :param visibility_level: The visibility_level of this SubgroupAndProjectBaseDto.
        :type visibility_level: int
        """
        self._visibility_level = visibility_level

    @property
    def visibility(self):
        r"""Gets the visibility of this SubgroupAndProjectBaseDto.

        **参数解释：** 可见性 private public。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The visibility of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this SubgroupAndProjectBaseDto.

        **参数解释：** 可见性 private public。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param visibility: The visibility of this SubgroupAndProjectBaseDto.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def is_project_admin(self):
        r"""Gets the is_project_admin of this SubgroupAndProjectBaseDto.

        **参数解释：** 当前用户是否为项目创建者。

        :return: The is_project_admin of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._is_project_admin

    @is_project_admin.setter
    def is_project_admin(self, is_project_admin):
        r"""Sets the is_project_admin of this SubgroupAndProjectBaseDto.

        **参数解释：** 当前用户是否为项目创建者。

        :param is_project_admin: The is_project_admin of this SubgroupAndProjectBaseDto.
        :type is_project_admin: int
        """
        self._is_project_admin = is_project_admin

    @property
    def is_group_creator(self):
        r"""Gets the is_group_creator of this SubgroupAndProjectBaseDto.

        **参数解释：** 当前用户是否为代码组创建者。

        :return: The is_group_creator of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._is_group_creator

    @is_group_creator.setter
    def is_group_creator(self, is_group_creator):
        r"""Sets the is_group_creator of this SubgroupAndProjectBaseDto.

        **参数解释：** 当前用户是否为代码组创建者。

        :param is_group_creator: The is_group_creator of this SubgroupAndProjectBaseDto.
        :type is_group_creator: int
        """
        self._is_group_creator = is_group_creator

    @property
    def is_repo_creator(self):
        r"""Gets the is_repo_creator of this SubgroupAndProjectBaseDto.

        **参数解释：** 当前用户是否为仓库创建者。

        :return: The is_repo_creator of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._is_repo_creator

    @is_repo_creator.setter
    def is_repo_creator(self, is_repo_creator):
        r"""Sets the is_repo_creator of this SubgroupAndProjectBaseDto.

        **参数解释：** 当前用户是否为仓库创建者。

        :param is_repo_creator: The is_repo_creator of this SubgroupAndProjectBaseDto.
        :type is_repo_creator: int
        """
        self._is_repo_creator = is_repo_creator

    @property
    def role_show_flag(self):
        r"""Gets the role_show_flag of this SubgroupAndProjectBaseDto.

        **参数解释：** 角色展示标记。

        :return: The role_show_flag of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._role_show_flag

    @role_show_flag.setter
    def role_show_flag(self, role_show_flag):
        r"""Sets the role_show_flag of this SubgroupAndProjectBaseDto.

        **参数解释：** 角色展示标记。

        :param role_show_flag: The role_show_flag of this SubgroupAndProjectBaseDto.
        :type role_show_flag: int
        """
        self._role_show_flag = role_show_flag

    @property
    def uuid(self):
        r"""Gets the uuid of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库的uuid。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The uuid of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库的uuid。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param uuid: The uuid of this SubgroupAndProjectBaseDto.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def forks_count(self):
        r"""Gets the forks_count of this SubgroupAndProjectBaseDto.

        **参数解释：** fork数量。

        :return: The forks_count of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._forks_count

    @forks_count.setter
    def forks_count(self, forks_count):
        r"""Sets the forks_count of this SubgroupAndProjectBaseDto.

        **参数解释：** fork数量。

        :param forks_count: The forks_count of this SubgroupAndProjectBaseDto.
        :type forks_count: int
        """
        self._forks_count = forks_count

    @property
    def is_kia(self):
        r"""Gets the is_kia of this SubgroupAndProjectBaseDto.

        **参数解释：** 是否为kia。

        :return: The is_kia of this SubgroupAndProjectBaseDto.
        :rtype: bool
        """
        return self._is_kia

    @is_kia.setter
    def is_kia(self, is_kia):
        r"""Sets the is_kia of this SubgroupAndProjectBaseDto.

        **参数解释：** 是否为kia。

        :param is_kia: The is_kia of this SubgroupAndProjectBaseDto.
        :type is_kia: bool
        """
        self._is_kia = is_kia

    @property
    def is_owner(self):
        r"""Gets the is_owner of this SubgroupAndProjectBaseDto.

        **参数解释：** 是否为所有者。

        :return: The is_owner of this SubgroupAndProjectBaseDto.
        :rtype: bool
        """
        return self._is_owner

    @is_owner.setter
    def is_owner(self, is_owner):
        r"""Sets the is_owner of this SubgroupAndProjectBaseDto.

        **参数解释：** 是否为所有者。

        :param is_owner: The is_owner of this SubgroupAndProjectBaseDto.
        :type is_owner: bool
        """
        self._is_owner = is_owner

    @property
    def archived(self):
        r"""Gets the archived of this SubgroupAndProjectBaseDto.

        **参数解释：** 是否为存档。

        :return: The archived of this SubgroupAndProjectBaseDto.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this SubgroupAndProjectBaseDto.

        **参数解释：** 是否为存档。

        :param archived: The archived of this SubgroupAndProjectBaseDto.
        :type archived: bool
        """
        self._archived = archived

    @property
    def last_repository_updated_at(self):
        r"""Gets the last_repository_updated_at of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库的最后更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The last_repository_updated_at of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._last_repository_updated_at

    @last_repository_updated_at.setter
    def last_repository_updated_at(self, last_repository_updated_at):
        r"""Sets the last_repository_updated_at of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库的最后更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param last_repository_updated_at: The last_repository_updated_at of this SubgroupAndProjectBaseDto.
        :type last_repository_updated_at: str
        """
        self._last_repository_updated_at = last_repository_updated_at

    @property
    def open_merge_requests_count(self):
        r"""Gets the open_merge_requests_count of this SubgroupAndProjectBaseDto.

        **参数解释：** 开启的mr数量。

        :return: The open_merge_requests_count of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._open_merge_requests_count

    @open_merge_requests_count.setter
    def open_merge_requests_count(self, open_merge_requests_count):
        r"""Sets the open_merge_requests_count of this SubgroupAndProjectBaseDto.

        **参数解释：** 开启的mr数量。

        :param open_merge_requests_count: The open_merge_requests_count of this SubgroupAndProjectBaseDto.
        :type open_merge_requests_count: int
        """
        self._open_merge_requests_count = open_merge_requests_count

    @property
    def all_merge_requests_count(self):
        r"""Gets the all_merge_requests_count of this SubgroupAndProjectBaseDto.

        **参数解释：** 所有的mr数量。

        :return: The all_merge_requests_count of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._all_merge_requests_count

    @all_merge_requests_count.setter
    def all_merge_requests_count(self, all_merge_requests_count):
        r"""Sets the all_merge_requests_count of this SubgroupAndProjectBaseDto.

        **参数解释：** 所有的mr数量。

        :param all_merge_requests_count: The all_merge_requests_count of this SubgroupAndProjectBaseDto.
        :type all_merge_requests_count: int
        """
        self._all_merge_requests_count = all_merge_requests_count

    @property
    def project_role(self):
        r"""Gets the project_role of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库角色。

        :return: The project_role of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._project_role

    @project_role.setter
    def project_role(self, project_role):
        r"""Sets the project_role of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库角色。

        :param project_role: The project_role of this SubgroupAndProjectBaseDto.
        :type project_role: int
        """
        self._project_role = project_role

    @property
    def project_members_count(self):
        r"""Gets the project_members_count of this SubgroupAndProjectBaseDto.

        **参数解释：** fork数量。

        :return: The project_members_count of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._project_members_count

    @project_members_count.setter
    def project_members_count(self, project_members_count):
        r"""Sets the project_members_count of this SubgroupAndProjectBaseDto.

        **参数解释：** fork数量。

        :param project_members_count: The project_members_count of this SubgroupAndProjectBaseDto.
        :type project_members_count: int
        """
        self._project_members_count = project_members_count

    @property
    def project_creator(self):
        r"""Gets the project_creator of this SubgroupAndProjectBaseDto.

        :return: The project_creator of this SubgroupAndProjectBaseDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ProjectCreatorDto`
        """
        return self._project_creator

    @project_creator.setter
    def project_creator(self, project_creator):
        r"""Sets the project_creator of this SubgroupAndProjectBaseDto.

        :param project_creator: The project_creator of this SubgroupAndProjectBaseDto.
        :type project_creator: :class:`huaweicloudsdkcodehub.v4.ProjectCreatorDto`
        """
        self._project_creator = project_creator

    @property
    def star_count(self):
        r"""Gets the star_count of this SubgroupAndProjectBaseDto.

        **参数解释：** fork数量。

        :return: The star_count of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._star_count

    @star_count.setter
    def star_count(self, star_count):
        r"""Sets the star_count of this SubgroupAndProjectBaseDto.

        **参数解释：** fork数量。

        :param star_count: The star_count of this SubgroupAndProjectBaseDto.
        :type star_count: int
        """
        self._star_count = star_count

    @property
    def tag_list(self):
        r"""Gets the tag_list of this SubgroupAndProjectBaseDto.

        **参数解释：** tag列表。

        :return: The tag_list of this SubgroupAndProjectBaseDto.
        :rtype: list[str]
        """
        return self._tag_list

    @tag_list.setter
    def tag_list(self, tag_list):
        r"""Sets the tag_list of this SubgroupAndProjectBaseDto.

        **参数解释：** tag列表。

        :param tag_list: The tag_list of this SubgroupAndProjectBaseDto.
        :type tag_list: list[str]
        """
        self._tag_list = tag_list

    @property
    def http_url_to_repo(self):
        r"""Gets the http_url_to_repo of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库的http url。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The http_url_to_repo of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._http_url_to_repo

    @http_url_to_repo.setter
    def http_url_to_repo(self, http_url_to_repo):
        r"""Sets the http_url_to_repo of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库的http url。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param http_url_to_repo: The http_url_to_repo of this SubgroupAndProjectBaseDto.
        :type http_url_to_repo: str
        """
        self._http_url_to_repo = http_url_to_repo

    @property
    def ssh_url_to_repo(self):
        r"""Gets the ssh_url_to_repo of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库的ssh url。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The ssh_url_to_repo of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._ssh_url_to_repo

    @ssh_url_to_repo.setter
    def ssh_url_to_repo(self, ssh_url_to_repo):
        r"""Sets the ssh_url_to_repo of this SubgroupAndProjectBaseDto.

        **参数解释：** 仓库的ssh url。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param ssh_url_to_repo: The ssh_url_to_repo of this SubgroupAndProjectBaseDto.
        :type ssh_url_to_repo: str
        """
        self._ssh_url_to_repo = ssh_url_to_repo

    @property
    def status(self):
        r"""Gets the status of this SubgroupAndProjectBaseDto.

        **参数解释：** 状态。

        :return: The status of this SubgroupAndProjectBaseDto.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SubgroupAndProjectBaseDto.

        **参数解释：** 状态。

        :param status: The status of this SubgroupAndProjectBaseDto.
        :type status: int
        """
        self._status = status

    @property
    def active_statistic(self):
        r"""Gets the active_statistic of this SubgroupAndProjectBaseDto.

        **参数解释：** 活跃统计。

        :return: The active_statistic of this SubgroupAndProjectBaseDto.
        :rtype: list[int]
        """
        return self._active_statistic

    @active_statistic.setter
    def active_statistic(self, active_statistic):
        r"""Sets the active_statistic of this SubgroupAndProjectBaseDto.

        **参数解释：** 活跃统计。

        :param active_statistic: The active_statistic of this SubgroupAndProjectBaseDto.
        :type active_statistic: list[int]
        """
        self._active_statistic = active_statistic

    @property
    def security_tag(self):
        r"""Gets the security_tag of this SubgroupAndProjectBaseDto.

        **参数解释：** 安全标签。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The security_tag of this SubgroupAndProjectBaseDto.
        :rtype: str
        """
        return self._security_tag

    @security_tag.setter
    def security_tag(self, security_tag):
        r"""Sets the security_tag of this SubgroupAndProjectBaseDto.

        **参数解释：** 安全标签。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param security_tag: The security_tag of this SubgroupAndProjectBaseDto.
        :type security_tag: str
        """
        self._security_tag = security_tag

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
        if not isinstance(other, SubgroupAndProjectBaseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
