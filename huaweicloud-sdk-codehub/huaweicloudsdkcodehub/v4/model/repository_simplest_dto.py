# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositorySimplestDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'namespace': 'str',
        'path': 'str',
        'develop_mode': 'str',
        'visibility': 'str',
        'security': 'str',
        'star_count': 'int',
        'forks_count': 'int',
        'open_issues_count': 'int',
        'open_merge_requests_count': 'int',
        'starred': 'bool',
        'name_with_namespace': 'str',
        'last_activity_at': 'str',
        'forked_from_repository': 'ForkedFromRepositorySimplestDto',
        'permissions': 'int',
        'archived': 'bool',
        'member_count': 'int',
        'uuid': 'str',
        'description': 'str',
        'last_repository_updated_at': 'str',
        'ssh_url_to_repo': 'str',
        'http_url_to_repo': 'str',
        'status': 'str',
        'active_statistic': 'list[int]',
        'project_name': 'str',
        'project_id': 'str',
        'project_is_delete': 'bool',
        'creator_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'namespace': 'namespace',
        'path': 'path',
        'develop_mode': 'develop_mode',
        'visibility': 'visibility',
        'security': 'security',
        'star_count': 'star_count',
        'forks_count': 'forks_count',
        'open_issues_count': 'open_issues_count',
        'open_merge_requests_count': 'open_merge_requests_count',
        'starred': 'starred',
        'name_with_namespace': 'name_with_namespace',
        'last_activity_at': 'last_activity_at',
        'forked_from_repository': 'forked_from_repository',
        'permissions': 'permissions',
        'archived': 'archived',
        'member_count': 'member_count',
        'uuid': 'uuid',
        'description': 'description',
        'last_repository_updated_at': 'last_repository_updated_at',
        'ssh_url_to_repo': 'ssh_url_to_repo',
        'http_url_to_repo': 'http_url_to_repo',
        'status': 'status',
        'active_statistic': 'active_statistic',
        'project_name': 'project_name',
        'project_id': 'project_id',
        'project_is_delete': 'project_is_delete',
        'creator_id': 'creator_id'
    }

    def __init__(self, id=None, name=None, namespace=None, path=None, develop_mode=None, visibility=None, security=None, star_count=None, forks_count=None, open_issues_count=None, open_merge_requests_count=None, starred=None, name_with_namespace=None, last_activity_at=None, forked_from_repository=None, permissions=None, archived=None, member_count=None, uuid=None, description=None, last_repository_updated_at=None, ssh_url_to_repo=None, http_url_to_repo=None, status=None, active_statistic=None, project_name=None, project_id=None, project_is_delete=None, creator_id=None):
        r"""RepositorySimplestDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 仓库ID **约束限制：** 不涉及。
        :type id: int
        :param name: **参数解释：** 仓库名称。 **约束限制：** 不涉及。
        :type name: str
        :param namespace: **参数解释：** 命名空间。 **约束限制：** 不涉及。
        :type namespace: str
        :param path: **参数解释：** 仓库路径。 **约束限制：** 不涉及。
        :type path: str
        :param develop_mode: **参数解释：** 开发模式。 **约束限制：** 不涉及。
        :type develop_mode: str
        :param visibility: **参数解释：** 可见性。 **约束限制：** 不涉及。
        :type visibility: str
        :param security: **参数解释：** 安全级别。 **约束限制：** 不涉及。
        :type security: str
        :param star_count: **参数解释：** 关注数。 **约束限制：** 不涉及。
        :type star_count: int
        :param forks_count: **参数解释：** Fork数。 **约束限制：** 不涉及。
        :type forks_count: int
        :param open_issues_count: **参数解释：** 开放的问题数。 **约束限制：** 不涉及。
        :type open_issues_count: int
        :param open_merge_requests_count: **参数解释：** 开放的合并请求数。 **约束限制：** 不涉及。
        :type open_merge_requests_count: int
        :param starred: **参数解释：** 是否已关注。 **约束限制：** 不涉及。
        :type starred: bool
        :param name_with_namespace: **参数解释：** 包含命名空间的仓库名称。 **约束限制：** 不涉及。
        :type name_with_namespace: str
        :param last_activity_at: **参数解释：** 最后活跃时间。 **约束限制：** 不涉及。
        :type last_activity_at: str
        :param forked_from_repository: 
        :type forked_from_repository: :class:`huaweicloudsdkcodehub.v4.ForkedFromRepositorySimplestDto`
        :param permissions: **参数解释：** 权限。 **约束限制：** 不涉及。
        :type permissions: int
        :param archived: **参数解释：** 是否归档。 **约束限制：** 不涉及。
        :type archived: bool
        :param member_count: **参数解释：** 成员数。 **约束限制：** 不涉及。
        :type member_count: int
        :param uuid: **参数解释：** 仓库唯一标识符。 **约束限制：** 不涉及。
        :type uuid: str
        :param description: **参数解释：** 仓库描述。 **约束限制：** 不涉及。
        :type description: str
        :param last_repository_updated_at: **参数解释：** 最后更新时间。 **约束限制：** 不涉及。
        :type last_repository_updated_at: str
        :param ssh_url_to_repo: **参数解释：** SSH仓库URL。 **约束限制：** 不涉及。
        :type ssh_url_to_repo: str
        :param http_url_to_repo: **参数解释：** HTTP仓库URL。 **约束限制：** 不涉及。
        :type http_url_to_repo: str
        :param status: **参数解释：** 仓库状态。 **约束限制：** 不涉及。
        :type status: str
        :param active_statistic: **参数解释：** 活跃统计。 **约束限制：** 不涉及。
        :type active_statistic: list[int]
        :param project_name: **参数解释：** 项目名称。 **约束限制：** 不涉及。
        :type project_name: str
        :param project_id: **参数解释：** 项目ID。 **约束限制：** 不涉及。
        :type project_id: str
        :param project_is_delete: **参数解释：** 项目是否删除。 **约束限制：** 不涉及。
        :type project_is_delete: bool
        :param creator_id: **参数解释：** 创建者ID **约束限制：** 不涉及。
        :type creator_id: int
        """
        
        

        self._id = None
        self._name = None
        self._namespace = None
        self._path = None
        self._develop_mode = None
        self._visibility = None
        self._security = None
        self._star_count = None
        self._forks_count = None
        self._open_issues_count = None
        self._open_merge_requests_count = None
        self._starred = None
        self._name_with_namespace = None
        self._last_activity_at = None
        self._forked_from_repository = None
        self._permissions = None
        self._archived = None
        self._member_count = None
        self._uuid = None
        self._description = None
        self._last_repository_updated_at = None
        self._ssh_url_to_repo = None
        self._http_url_to_repo = None
        self._status = None
        self._active_statistic = None
        self._project_name = None
        self._project_id = None
        self._project_is_delete = None
        self._creator_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if path is not None:
            self.path = path
        if develop_mode is not None:
            self.develop_mode = develop_mode
        if visibility is not None:
            self.visibility = visibility
        if security is not None:
            self.security = security
        if star_count is not None:
            self.star_count = star_count
        if forks_count is not None:
            self.forks_count = forks_count
        if open_issues_count is not None:
            self.open_issues_count = open_issues_count
        if open_merge_requests_count is not None:
            self.open_merge_requests_count = open_merge_requests_count
        if starred is not None:
            self.starred = starred
        if name_with_namespace is not None:
            self.name_with_namespace = name_with_namespace
        if last_activity_at is not None:
            self.last_activity_at = last_activity_at
        if forked_from_repository is not None:
            self.forked_from_repository = forked_from_repository
        if permissions is not None:
            self.permissions = permissions
        if archived is not None:
            self.archived = archived
        if member_count is not None:
            self.member_count = member_count
        if uuid is not None:
            self.uuid = uuid
        if description is not None:
            self.description = description
        if last_repository_updated_at is not None:
            self.last_repository_updated_at = last_repository_updated_at
        if ssh_url_to_repo is not None:
            self.ssh_url_to_repo = ssh_url_to_repo
        if http_url_to_repo is not None:
            self.http_url_to_repo = http_url_to_repo
        if status is not None:
            self.status = status
        if active_statistic is not None:
            self.active_statistic = active_statistic
        if project_name is not None:
            self.project_name = project_name
        if project_id is not None:
            self.project_id = project_id
        if project_is_delete is not None:
            self.project_is_delete = project_is_delete
        if creator_id is not None:
            self.creator_id = creator_id

    @property
    def id(self):
        r"""Gets the id of this RepositorySimplestDto.

        **参数解释：** 仓库ID **约束限制：** 不涉及。

        :return: The id of this RepositorySimplestDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RepositorySimplestDto.

        **参数解释：** 仓库ID **约束限制：** 不涉及。

        :param id: The id of this RepositorySimplestDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RepositorySimplestDto.

        **参数解释：** 仓库名称。 **约束限制：** 不涉及。

        :return: The name of this RepositorySimplestDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepositorySimplestDto.

        **参数解释：** 仓库名称。 **约束限制：** 不涉及。

        :param name: The name of this RepositorySimplestDto.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this RepositorySimplestDto.

        **参数解释：** 命名空间。 **约束限制：** 不涉及。

        :return: The namespace of this RepositorySimplestDto.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this RepositorySimplestDto.

        **参数解释：** 命名空间。 **约束限制：** 不涉及。

        :param namespace: The namespace of this RepositorySimplestDto.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def path(self):
        r"""Gets the path of this RepositorySimplestDto.

        **参数解释：** 仓库路径。 **约束限制：** 不涉及。

        :return: The path of this RepositorySimplestDto.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this RepositorySimplestDto.

        **参数解释：** 仓库路径。 **约束限制：** 不涉及。

        :param path: The path of this RepositorySimplestDto.
        :type path: str
        """
        self._path = path

    @property
    def develop_mode(self):
        r"""Gets the develop_mode of this RepositorySimplestDto.

        **参数解释：** 开发模式。 **约束限制：** 不涉及。

        :return: The develop_mode of this RepositorySimplestDto.
        :rtype: str
        """
        return self._develop_mode

    @develop_mode.setter
    def develop_mode(self, develop_mode):
        r"""Sets the develop_mode of this RepositorySimplestDto.

        **参数解释：** 开发模式。 **约束限制：** 不涉及。

        :param develop_mode: The develop_mode of this RepositorySimplestDto.
        :type develop_mode: str
        """
        self._develop_mode = develop_mode

    @property
    def visibility(self):
        r"""Gets the visibility of this RepositorySimplestDto.

        **参数解释：** 可见性。 **约束限制：** 不涉及。

        :return: The visibility of this RepositorySimplestDto.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this RepositorySimplestDto.

        **参数解释：** 可见性。 **约束限制：** 不涉及。

        :param visibility: The visibility of this RepositorySimplestDto.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def security(self):
        r"""Gets the security of this RepositorySimplestDto.

        **参数解释：** 安全级别。 **约束限制：** 不涉及。

        :return: The security of this RepositorySimplestDto.
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        r"""Sets the security of this RepositorySimplestDto.

        **参数解释：** 安全级别。 **约束限制：** 不涉及。

        :param security: The security of this RepositorySimplestDto.
        :type security: str
        """
        self._security = security

    @property
    def star_count(self):
        r"""Gets the star_count of this RepositorySimplestDto.

        **参数解释：** 关注数。 **约束限制：** 不涉及。

        :return: The star_count of this RepositorySimplestDto.
        :rtype: int
        """
        return self._star_count

    @star_count.setter
    def star_count(self, star_count):
        r"""Sets the star_count of this RepositorySimplestDto.

        **参数解释：** 关注数。 **约束限制：** 不涉及。

        :param star_count: The star_count of this RepositorySimplestDto.
        :type star_count: int
        """
        self._star_count = star_count

    @property
    def forks_count(self):
        r"""Gets the forks_count of this RepositorySimplestDto.

        **参数解释：** Fork数。 **约束限制：** 不涉及。

        :return: The forks_count of this RepositorySimplestDto.
        :rtype: int
        """
        return self._forks_count

    @forks_count.setter
    def forks_count(self, forks_count):
        r"""Sets the forks_count of this RepositorySimplestDto.

        **参数解释：** Fork数。 **约束限制：** 不涉及。

        :param forks_count: The forks_count of this RepositorySimplestDto.
        :type forks_count: int
        """
        self._forks_count = forks_count

    @property
    def open_issues_count(self):
        r"""Gets the open_issues_count of this RepositorySimplestDto.

        **参数解释：** 开放的问题数。 **约束限制：** 不涉及。

        :return: The open_issues_count of this RepositorySimplestDto.
        :rtype: int
        """
        return self._open_issues_count

    @open_issues_count.setter
    def open_issues_count(self, open_issues_count):
        r"""Sets the open_issues_count of this RepositorySimplestDto.

        **参数解释：** 开放的问题数。 **约束限制：** 不涉及。

        :param open_issues_count: The open_issues_count of this RepositorySimplestDto.
        :type open_issues_count: int
        """
        self._open_issues_count = open_issues_count

    @property
    def open_merge_requests_count(self):
        r"""Gets the open_merge_requests_count of this RepositorySimplestDto.

        **参数解释：** 开放的合并请求数。 **约束限制：** 不涉及。

        :return: The open_merge_requests_count of this RepositorySimplestDto.
        :rtype: int
        """
        return self._open_merge_requests_count

    @open_merge_requests_count.setter
    def open_merge_requests_count(self, open_merge_requests_count):
        r"""Sets the open_merge_requests_count of this RepositorySimplestDto.

        **参数解释：** 开放的合并请求数。 **约束限制：** 不涉及。

        :param open_merge_requests_count: The open_merge_requests_count of this RepositorySimplestDto.
        :type open_merge_requests_count: int
        """
        self._open_merge_requests_count = open_merge_requests_count

    @property
    def starred(self):
        r"""Gets the starred of this RepositorySimplestDto.

        **参数解释：** 是否已关注。 **约束限制：** 不涉及。

        :return: The starred of this RepositorySimplestDto.
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        r"""Sets the starred of this RepositorySimplestDto.

        **参数解释：** 是否已关注。 **约束限制：** 不涉及。

        :param starred: The starred of this RepositorySimplestDto.
        :type starred: bool
        """
        self._starred = starred

    @property
    def name_with_namespace(self):
        r"""Gets the name_with_namespace of this RepositorySimplestDto.

        **参数解释：** 包含命名空间的仓库名称。 **约束限制：** 不涉及。

        :return: The name_with_namespace of this RepositorySimplestDto.
        :rtype: str
        """
        return self._name_with_namespace

    @name_with_namespace.setter
    def name_with_namespace(self, name_with_namespace):
        r"""Sets the name_with_namespace of this RepositorySimplestDto.

        **参数解释：** 包含命名空间的仓库名称。 **约束限制：** 不涉及。

        :param name_with_namespace: The name_with_namespace of this RepositorySimplestDto.
        :type name_with_namespace: str
        """
        self._name_with_namespace = name_with_namespace

    @property
    def last_activity_at(self):
        r"""Gets the last_activity_at of this RepositorySimplestDto.

        **参数解释：** 最后活跃时间。 **约束限制：** 不涉及。

        :return: The last_activity_at of this RepositorySimplestDto.
        :rtype: str
        """
        return self._last_activity_at

    @last_activity_at.setter
    def last_activity_at(self, last_activity_at):
        r"""Sets the last_activity_at of this RepositorySimplestDto.

        **参数解释：** 最后活跃时间。 **约束限制：** 不涉及。

        :param last_activity_at: The last_activity_at of this RepositorySimplestDto.
        :type last_activity_at: str
        """
        self._last_activity_at = last_activity_at

    @property
    def forked_from_repository(self):
        r"""Gets the forked_from_repository of this RepositorySimplestDto.

        :return: The forked_from_repository of this RepositorySimplestDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ForkedFromRepositorySimplestDto`
        """
        return self._forked_from_repository

    @forked_from_repository.setter
    def forked_from_repository(self, forked_from_repository):
        r"""Sets the forked_from_repository of this RepositorySimplestDto.

        :param forked_from_repository: The forked_from_repository of this RepositorySimplestDto.
        :type forked_from_repository: :class:`huaweicloudsdkcodehub.v4.ForkedFromRepositorySimplestDto`
        """
        self._forked_from_repository = forked_from_repository

    @property
    def permissions(self):
        r"""Gets the permissions of this RepositorySimplestDto.

        **参数解释：** 权限。 **约束限制：** 不涉及。

        :return: The permissions of this RepositorySimplestDto.
        :rtype: int
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this RepositorySimplestDto.

        **参数解释：** 权限。 **约束限制：** 不涉及。

        :param permissions: The permissions of this RepositorySimplestDto.
        :type permissions: int
        """
        self._permissions = permissions

    @property
    def archived(self):
        r"""Gets the archived of this RepositorySimplestDto.

        **参数解释：** 是否归档。 **约束限制：** 不涉及。

        :return: The archived of this RepositorySimplestDto.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this RepositorySimplestDto.

        **参数解释：** 是否归档。 **约束限制：** 不涉及。

        :param archived: The archived of this RepositorySimplestDto.
        :type archived: bool
        """
        self._archived = archived

    @property
    def member_count(self):
        r"""Gets the member_count of this RepositorySimplestDto.

        **参数解释：** 成员数。 **约束限制：** 不涉及。

        :return: The member_count of this RepositorySimplestDto.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        r"""Sets the member_count of this RepositorySimplestDto.

        **参数解释：** 成员数。 **约束限制：** 不涉及。

        :param member_count: The member_count of this RepositorySimplestDto.
        :type member_count: int
        """
        self._member_count = member_count

    @property
    def uuid(self):
        r"""Gets the uuid of this RepositorySimplestDto.

        **参数解释：** 仓库唯一标识符。 **约束限制：** 不涉及。

        :return: The uuid of this RepositorySimplestDto.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this RepositorySimplestDto.

        **参数解释：** 仓库唯一标识符。 **约束限制：** 不涉及。

        :param uuid: The uuid of this RepositorySimplestDto.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def description(self):
        r"""Gets the description of this RepositorySimplestDto.

        **参数解释：** 仓库描述。 **约束限制：** 不涉及。

        :return: The description of this RepositorySimplestDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RepositorySimplestDto.

        **参数解释：** 仓库描述。 **约束限制：** 不涉及。

        :param description: The description of this RepositorySimplestDto.
        :type description: str
        """
        self._description = description

    @property
    def last_repository_updated_at(self):
        r"""Gets the last_repository_updated_at of this RepositorySimplestDto.

        **参数解释：** 最后更新时间。 **约束限制：** 不涉及。

        :return: The last_repository_updated_at of this RepositorySimplestDto.
        :rtype: str
        """
        return self._last_repository_updated_at

    @last_repository_updated_at.setter
    def last_repository_updated_at(self, last_repository_updated_at):
        r"""Sets the last_repository_updated_at of this RepositorySimplestDto.

        **参数解释：** 最后更新时间。 **约束限制：** 不涉及。

        :param last_repository_updated_at: The last_repository_updated_at of this RepositorySimplestDto.
        :type last_repository_updated_at: str
        """
        self._last_repository_updated_at = last_repository_updated_at

    @property
    def ssh_url_to_repo(self):
        r"""Gets the ssh_url_to_repo of this RepositorySimplestDto.

        **参数解释：** SSH仓库URL。 **约束限制：** 不涉及。

        :return: The ssh_url_to_repo of this RepositorySimplestDto.
        :rtype: str
        """
        return self._ssh_url_to_repo

    @ssh_url_to_repo.setter
    def ssh_url_to_repo(self, ssh_url_to_repo):
        r"""Sets the ssh_url_to_repo of this RepositorySimplestDto.

        **参数解释：** SSH仓库URL。 **约束限制：** 不涉及。

        :param ssh_url_to_repo: The ssh_url_to_repo of this RepositorySimplestDto.
        :type ssh_url_to_repo: str
        """
        self._ssh_url_to_repo = ssh_url_to_repo

    @property
    def http_url_to_repo(self):
        r"""Gets the http_url_to_repo of this RepositorySimplestDto.

        **参数解释：** HTTP仓库URL。 **约束限制：** 不涉及。

        :return: The http_url_to_repo of this RepositorySimplestDto.
        :rtype: str
        """
        return self._http_url_to_repo

    @http_url_to_repo.setter
    def http_url_to_repo(self, http_url_to_repo):
        r"""Sets the http_url_to_repo of this RepositorySimplestDto.

        **参数解释：** HTTP仓库URL。 **约束限制：** 不涉及。

        :param http_url_to_repo: The http_url_to_repo of this RepositorySimplestDto.
        :type http_url_to_repo: str
        """
        self._http_url_to_repo = http_url_to_repo

    @property
    def status(self):
        r"""Gets the status of this RepositorySimplestDto.

        **参数解释：** 仓库状态。 **约束限制：** 不涉及。

        :return: The status of this RepositorySimplestDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RepositorySimplestDto.

        **参数解释：** 仓库状态。 **约束限制：** 不涉及。

        :param status: The status of this RepositorySimplestDto.
        :type status: str
        """
        self._status = status

    @property
    def active_statistic(self):
        r"""Gets the active_statistic of this RepositorySimplestDto.

        **参数解释：** 活跃统计。 **约束限制：** 不涉及。

        :return: The active_statistic of this RepositorySimplestDto.
        :rtype: list[int]
        """
        return self._active_statistic

    @active_statistic.setter
    def active_statistic(self, active_statistic):
        r"""Sets the active_statistic of this RepositorySimplestDto.

        **参数解释：** 活跃统计。 **约束限制：** 不涉及。

        :param active_statistic: The active_statistic of this RepositorySimplestDto.
        :type active_statistic: list[int]
        """
        self._active_statistic = active_statistic

    @property
    def project_name(self):
        r"""Gets the project_name of this RepositorySimplestDto.

        **参数解释：** 项目名称。 **约束限制：** 不涉及。

        :return: The project_name of this RepositorySimplestDto.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this RepositorySimplestDto.

        **参数解释：** 项目名称。 **约束限制：** 不涉及。

        :param project_name: The project_name of this RepositorySimplestDto.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def project_id(self):
        r"""Gets the project_id of this RepositorySimplestDto.

        **参数解释：** 项目ID。 **约束限制：** 不涉及。

        :return: The project_id of this RepositorySimplestDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RepositorySimplestDto.

        **参数解释：** 项目ID。 **约束限制：** 不涉及。

        :param project_id: The project_id of this RepositorySimplestDto.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_is_delete(self):
        r"""Gets the project_is_delete of this RepositorySimplestDto.

        **参数解释：** 项目是否删除。 **约束限制：** 不涉及。

        :return: The project_is_delete of this RepositorySimplestDto.
        :rtype: bool
        """
        return self._project_is_delete

    @project_is_delete.setter
    def project_is_delete(self, project_is_delete):
        r"""Sets the project_is_delete of this RepositorySimplestDto.

        **参数解释：** 项目是否删除。 **约束限制：** 不涉及。

        :param project_is_delete: The project_is_delete of this RepositorySimplestDto.
        :type project_is_delete: bool
        """
        self._project_is_delete = project_is_delete

    @property
    def creator_id(self):
        r"""Gets the creator_id of this RepositorySimplestDto.

        **参数解释：** 创建者ID **约束限制：** 不涉及。

        :return: The creator_id of this RepositorySimplestDto.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this RepositorySimplestDto.

        **参数解释：** 创建者ID **约束限制：** 不涉及。

        :param creator_id: The creator_id of this RepositorySimplestDto.
        :type creator_id: int
        """
        self._creator_id = creator_id

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
        if not isinstance(other, RepositorySimplestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
