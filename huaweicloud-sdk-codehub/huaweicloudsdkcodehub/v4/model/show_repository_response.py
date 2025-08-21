# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryResponse(SdkResponse):

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
        'description': 'str',
        'name': 'str',
        'name_with_namespace': 'str',
        'path': 'str',
        'path_with_namespace': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'archived': 'bool',
        'ssh_url_to_repo': 'str',
        'http_url_to_repo': 'str',
        'web_url': 'str',
        'readme_url': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'develop_mode': 'str',
        'moderation_result': 'bool',
        'default_branch': 'str',
        'avatar_url': 'str',
        'star_count': 'int',
        'forks_count': 'int',
        'open_issues_count': 'int',
        'open_merge_requests_count': 'int',
        'last_activity_at': 'str',
        'namespace': 'NamespaceBasicDto',
        'empty_repo': 'bool',
        'starred': 'bool',
        'visibility': 'str',
        'security_tag': 'str',
        'security': 'str',
        'network_type': 'str',
        'owner': 'RepositoryUserBasicDto',
        'creator': 'RepositoryUserBasicDto',
        'creator_id': 'int',
        'forked_from_repository': 'RepositorySimpleDto',
        'uuid': 'str',
        'ancestor_ids': 'list[int]',
        'ancestor_names': 'list[str]',
        'import_status': 'str',
        'import_url': 'str',
        'import_error': 'str',
        'repo_type': 'str',
        'only_allow_merge_if_pipeline_succeeds': 'bool',
        'request_access_enabled': 'bool',
        'only_allow_merge_if_all_discussions_are_resolved': 'bool',
        'merge_method': 'str',
        'fork_network_repositories': 'list[RepositoryIdentityDto]',
        'permissions': 'PermissionsDto',
        'repository_type': 'str',
        'statistics': 'RepositoryStatisticsDto',
        'branch_count': 'int',
        'tag_count': 'int',
        'label_count': 'int',
        'member_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'name': 'name',
        'name_with_namespace': 'name_with_namespace',
        'path': 'path',
        'path_with_namespace': 'path_with_namespace',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'archived': 'archived',
        'ssh_url_to_repo': 'ssh_url_to_repo',
        'http_url_to_repo': 'http_url_to_repo',
        'web_url': 'web_url',
        'readme_url': 'readme_url',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'develop_mode': 'develop_mode',
        'moderation_result': 'moderation_result',
        'default_branch': 'default_branch',
        'avatar_url': 'avatar_url',
        'star_count': 'star_count',
        'forks_count': 'forks_count',
        'open_issues_count': 'open_issues_count',
        'open_merge_requests_count': 'open_merge_requests_count',
        'last_activity_at': 'last_activity_at',
        'namespace': 'namespace',
        'empty_repo': 'empty_repo',
        'starred': 'starred',
        'visibility': 'visibility',
        'security_tag': 'security_tag',
        'security': 'security',
        'network_type': 'network_type',
        'owner': 'owner',
        'creator': 'creator',
        'creator_id': 'creator_id',
        'forked_from_repository': 'forked_from_repository',
        'uuid': 'uuid',
        'ancestor_ids': 'ancestor_ids',
        'ancestor_names': 'ancestor_names',
        'import_status': 'import_status',
        'import_url': 'import_url',
        'import_error': 'import_error',
        'repo_type': 'repo_type',
        'only_allow_merge_if_pipeline_succeeds': 'only_allow_merge_if_pipeline_succeeds',
        'request_access_enabled': 'request_access_enabled',
        'only_allow_merge_if_all_discussions_are_resolved': 'only_allow_merge_if_all_discussions_are_resolved',
        'merge_method': 'merge_method',
        'fork_network_repositories': 'fork_network_repositories',
        'permissions': 'permissions',
        'repository_type': 'repository_type',
        'statistics': 'statistics',
        'branch_count': 'branch_count',
        'tag_count': 'tag_count',
        'label_count': 'label_count',
        'member_count': 'member_count'
    }

    def __init__(self, id=None, description=None, name=None, name_with_namespace=None, path=None, path_with_namespace=None, created_at=None, updated_at=None, archived=None, ssh_url_to_repo=None, http_url_to_repo=None, web_url=None, readme_url=None, project_id=None, project_name=None, develop_mode=None, moderation_result=None, default_branch=None, avatar_url=None, star_count=None, forks_count=None, open_issues_count=None, open_merge_requests_count=None, last_activity_at=None, namespace=None, empty_repo=None, starred=None, visibility=None, security_tag=None, security=None, network_type=None, owner=None, creator=None, creator_id=None, forked_from_repository=None, uuid=None, ancestor_ids=None, ancestor_names=None, import_status=None, import_url=None, import_error=None, repo_type=None, only_allow_merge_if_pipeline_succeeds=None, request_access_enabled=None, only_allow_merge_if_all_discussions_are_resolved=None, merge_method=None, fork_network_repositories=None, permissions=None, repository_type=None, statistics=None, branch_count=None, tag_count=None, label_count=None, member_count=None):
        r"""ShowRepositoryResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 仓库ID。
        :type id: int
        :param description: **参数解释：** 仓库描述信息。
        :type description: str
        :param name: **参数解释：** 仓库名称。
        :type name: str
        :param name_with_namespace: **参数解释：** 仓库完整名称。
        :type name_with_namespace: str
        :param path: **参数解释：** 仓库路径。
        :type path: str
        :param path_with_namespace: **参数解释：** 仓库完整路径。
        :type path_with_namespace: str
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。
        :type updated_at: str
        :param archived: **参数解释：** 是否归档。
        :type archived: bool
        :param ssh_url_to_repo: **参数解释：** 仓库ssh地址。
        :type ssh_url_to_repo: str
        :param http_url_to_repo: **参数解释：** 仓库http地址。
        :type http_url_to_repo: str
        :param web_url: **参数解释：** 仓库页面链接。
        :type web_url: str
        :param readme_url: **参数解释：** 仓库readme文件链接。
        :type readme_url: str
        :param project_id: **参数解释：** 仓库所属项目ID。
        :type project_id: str
        :param project_name: **参数解释：** 仓库所属项目名称。
        :type project_name: str
        :param develop_mode: **参数解释：** 仓库开发模式。 **取值范围：** - normal - CR
        :type develop_mode: str
        :param moderation_result: **参数解释：** 审核状态。
        :type moderation_result: bool
        :param default_branch: **参数解释：** 仓库默认分支 **约束限制：** 不涉及。
        :type default_branch: str
        :param avatar_url: **参数解释：** 仓库图标url **约束限制：** 不涉及。
        :type avatar_url: str
        :param star_count: **参数解释：** 关注数 **约束限制：** 不涉及。
        :type star_count: int
        :param forks_count: **参数解释：** fork数 **约束限制：** 不涉及。
        :type forks_count: int
        :param open_issues_count: **参数解释：** 开启issue数 **约束限制：** 不涉及。
        :type open_issues_count: int
        :param open_merge_requests_count: **参数解释：** 开启中的CR、MR数量 **约束限制：** 不涉及。
        :type open_merge_requests_count: int
        :param last_activity_at: **参数解释：** 最后活跃时间 **约束限制：** 不涉及。
        :type last_activity_at: str
        :param namespace: 
        :type namespace: :class:`huaweicloudsdkcodehub.v4.NamespaceBasicDto`
        :param empty_repo: **参数解释：** 空仓库 **约束限制：** 不涉及。
        :type empty_repo: bool
        :param starred: **参数解释：** 是否已关注 **约束限制：** 不涉及。
        :type starred: bool
        :param visibility: **参数解释：** 仓库可见等级 **约束限制：** 不涉及。
        :type visibility: str
        :param security_tag: **参数解释：** 仓库保密等级 **约束限制：** 不涉及。
        :type security_tag: str
        :param security: **参数解释：** 仓库保密等级 **约束限制：** 不涉及。
        :type security: str
        :param network_type: **参数解释：** 网络类型 **约束限制：** 不涉及。
        :type network_type: str
        :param owner: 
        :type owner: :class:`huaweicloudsdkcodehub.v4.RepositoryUserBasicDto`
        :param creator: 
        :type creator: :class:`huaweicloudsdkcodehub.v4.RepositoryUserBasicDto`
        :param creator_id: **参数解释：** 创建者ID **约束限制：** 不涉及。
        :type creator_id: int
        :param forked_from_repository: 
        :type forked_from_repository: :class:`huaweicloudsdkcodehub.v4.RepositorySimpleDto`
        :param uuid: **参数解释：** 仓库唯一标识符。 **约束限制：** 不涉及。
        :type uuid: str
        :param ancestor_ids: **参数解释：** 祖先仓库ID列表。 **约束限制：** 不涉及。
        :type ancestor_ids: list[int]
        :param ancestor_names: **参数解释：** 祖先仓库名称列表。 **约束限制：** 不涉及。
        :type ancestor_names: list[str]
        :param import_status: **参数解释：** 导入状态。 **约束限制：** 不涉及。
        :type import_status: str
        :param import_url: **参数解释：** 导入源地址。 **约束限制：** 不涉及。
        :type import_url: str
        :param import_error: **参数解释：** 导入错误信息。 **约束限制：** 不涉及。
        :type import_error: str
        :param repo_type: **参数解释：** 仓库类型。 **约束限制：** 不涉及。
        :type repo_type: str
        :param only_allow_merge_if_pipeline_succeeds: **参数解释：** 是否仅在流水线成功时允许合并。 **约束限制：** 不涉及。
        :type only_allow_merge_if_pipeline_succeeds: bool
        :param request_access_enabled: **参数解释：** 是否启用访问请求。 **约束限制：** 不涉及。
        :type request_access_enabled: bool
        :param only_allow_merge_if_all_discussions_are_resolved: **参数解释：** 是否仅在所有检视意见解决时允许合并。 **约束限制：** 不涉及。
        :type only_allow_merge_if_all_discussions_are_resolved: bool
        :param merge_method: **参数解释：** 合并方法。 **约束限制：** 不涉及。
        :type merge_method: str
        :param fork_network_repositories: **参数解释：** fork关联仓库列表。 **约束限制：** 不涉及。
        :type fork_network_repositories: list[:class:`huaweicloudsdkcodehub.v4.RepositoryIdentityDto`]
        :param permissions: 
        :type permissions: :class:`huaweicloudsdkcodehub.v4.PermissionsDto`
        :param repository_type: **参数解释：** 仓库类型。 **约束限制：** 不涉及。
        :type repository_type: str
        :param statistics: 
        :type statistics: :class:`huaweicloudsdkcodehub.v4.RepositoryStatisticsDto`
        :param branch_count: **参数解释：** 分支数量。 **约束限制：** 不涉及。
        :type branch_count: int
        :param tag_count: **参数解释：** Tag数量。 **约束限制：** 不涉及。
        :type tag_count: int
        :param label_count: **参数解释：** 标签数量。 **约束限制：** 不涉及。
        :type label_count: int
        :param member_count: **参数解释：** 成员数量。 **约束限制：** 不涉及。
        :type member_count: int
        """
        
        super(ShowRepositoryResponse, self).__init__()

        self._id = None
        self._description = None
        self._name = None
        self._name_with_namespace = None
        self._path = None
        self._path_with_namespace = None
        self._created_at = None
        self._updated_at = None
        self._archived = None
        self._ssh_url_to_repo = None
        self._http_url_to_repo = None
        self._web_url = None
        self._readme_url = None
        self._project_id = None
        self._project_name = None
        self._develop_mode = None
        self._moderation_result = None
        self._default_branch = None
        self._avatar_url = None
        self._star_count = None
        self._forks_count = None
        self._open_issues_count = None
        self._open_merge_requests_count = None
        self._last_activity_at = None
        self._namespace = None
        self._empty_repo = None
        self._starred = None
        self._visibility = None
        self._security_tag = None
        self._security = None
        self._network_type = None
        self._owner = None
        self._creator = None
        self._creator_id = None
        self._forked_from_repository = None
        self._uuid = None
        self._ancestor_ids = None
        self._ancestor_names = None
        self._import_status = None
        self._import_url = None
        self._import_error = None
        self._repo_type = None
        self._only_allow_merge_if_pipeline_succeeds = None
        self._request_access_enabled = None
        self._only_allow_merge_if_all_discussions_are_resolved = None
        self._merge_method = None
        self._fork_network_repositories = None
        self._permissions = None
        self._repository_type = None
        self._statistics = None
        self._branch_count = None
        self._tag_count = None
        self._label_count = None
        self._member_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if name_with_namespace is not None:
            self.name_with_namespace = name_with_namespace
        if path is not None:
            self.path = path
        if path_with_namespace is not None:
            self.path_with_namespace = path_with_namespace
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if archived is not None:
            self.archived = archived
        if ssh_url_to_repo is not None:
            self.ssh_url_to_repo = ssh_url_to_repo
        if http_url_to_repo is not None:
            self.http_url_to_repo = http_url_to_repo
        if web_url is not None:
            self.web_url = web_url
        if readme_url is not None:
            self.readme_url = readme_url
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if develop_mode is not None:
            self.develop_mode = develop_mode
        if moderation_result is not None:
            self.moderation_result = moderation_result
        if default_branch is not None:
            self.default_branch = default_branch
        if avatar_url is not None:
            self.avatar_url = avatar_url
        if star_count is not None:
            self.star_count = star_count
        if forks_count is not None:
            self.forks_count = forks_count
        if open_issues_count is not None:
            self.open_issues_count = open_issues_count
        if open_merge_requests_count is not None:
            self.open_merge_requests_count = open_merge_requests_count
        if last_activity_at is not None:
            self.last_activity_at = last_activity_at
        if namespace is not None:
            self.namespace = namespace
        if empty_repo is not None:
            self.empty_repo = empty_repo
        if starred is not None:
            self.starred = starred
        if visibility is not None:
            self.visibility = visibility
        if security_tag is not None:
            self.security_tag = security_tag
        if security is not None:
            self.security = security
        if network_type is not None:
            self.network_type = network_type
        if owner is not None:
            self.owner = owner
        if creator is not None:
            self.creator = creator
        if creator_id is not None:
            self.creator_id = creator_id
        if forked_from_repository is not None:
            self.forked_from_repository = forked_from_repository
        if uuid is not None:
            self.uuid = uuid
        if ancestor_ids is not None:
            self.ancestor_ids = ancestor_ids
        if ancestor_names is not None:
            self.ancestor_names = ancestor_names
        if import_status is not None:
            self.import_status = import_status
        if import_url is not None:
            self.import_url = import_url
        if import_error is not None:
            self.import_error = import_error
        if repo_type is not None:
            self.repo_type = repo_type
        if only_allow_merge_if_pipeline_succeeds is not None:
            self.only_allow_merge_if_pipeline_succeeds = only_allow_merge_if_pipeline_succeeds
        if request_access_enabled is not None:
            self.request_access_enabled = request_access_enabled
        if only_allow_merge_if_all_discussions_are_resolved is not None:
            self.only_allow_merge_if_all_discussions_are_resolved = only_allow_merge_if_all_discussions_are_resolved
        if merge_method is not None:
            self.merge_method = merge_method
        if fork_network_repositories is not None:
            self.fork_network_repositories = fork_network_repositories
        if permissions is not None:
            self.permissions = permissions
        if repository_type is not None:
            self.repository_type = repository_type
        if statistics is not None:
            self.statistics = statistics
        if branch_count is not None:
            self.branch_count = branch_count
        if tag_count is not None:
            self.tag_count = tag_count
        if label_count is not None:
            self.label_count = label_count
        if member_count is not None:
            self.member_count = member_count

    @property
    def id(self):
        r"""Gets the id of this ShowRepositoryResponse.

        **参数解释：** 仓库ID。

        :return: The id of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowRepositoryResponse.

        **参数解释：** 仓库ID。

        :param id: The id of this ShowRepositoryResponse.
        :type id: int
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this ShowRepositoryResponse.

        **参数解释：** 仓库描述信息。

        :return: The description of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowRepositoryResponse.

        **参数解释：** 仓库描述信息。

        :param description: The description of this ShowRepositoryResponse.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this ShowRepositoryResponse.

        **参数解释：** 仓库名称。

        :return: The name of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowRepositoryResponse.

        **参数解释：** 仓库名称。

        :param name: The name of this ShowRepositoryResponse.
        :type name: str
        """
        self._name = name

    @property
    def name_with_namespace(self):
        r"""Gets the name_with_namespace of this ShowRepositoryResponse.

        **参数解释：** 仓库完整名称。

        :return: The name_with_namespace of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._name_with_namespace

    @name_with_namespace.setter
    def name_with_namespace(self, name_with_namespace):
        r"""Sets the name_with_namespace of this ShowRepositoryResponse.

        **参数解释：** 仓库完整名称。

        :param name_with_namespace: The name_with_namespace of this ShowRepositoryResponse.
        :type name_with_namespace: str
        """
        self._name_with_namespace = name_with_namespace

    @property
    def path(self):
        r"""Gets the path of this ShowRepositoryResponse.

        **参数解释：** 仓库路径。

        :return: The path of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowRepositoryResponse.

        **参数解释：** 仓库路径。

        :param path: The path of this ShowRepositoryResponse.
        :type path: str
        """
        self._path = path

    @property
    def path_with_namespace(self):
        r"""Gets the path_with_namespace of this ShowRepositoryResponse.

        **参数解释：** 仓库完整路径。

        :return: The path_with_namespace of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._path_with_namespace

    @path_with_namespace.setter
    def path_with_namespace(self, path_with_namespace):
        r"""Sets the path_with_namespace of this ShowRepositoryResponse.

        **参数解释：** 仓库完整路径。

        :param path_with_namespace: The path_with_namespace of this ShowRepositoryResponse.
        :type path_with_namespace: str
        """
        self._path_with_namespace = path_with_namespace

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowRepositoryResponse.

        **参数解释：** 创建时间。

        :return: The created_at of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowRepositoryResponse.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this ShowRepositoryResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowRepositoryResponse.

        **参数解释：** 更新时间。

        :return: The updated_at of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowRepositoryResponse.

        **参数解释：** 更新时间。

        :param updated_at: The updated_at of this ShowRepositoryResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def archived(self):
        r"""Gets the archived of this ShowRepositoryResponse.

        **参数解释：** 是否归档。

        :return: The archived of this ShowRepositoryResponse.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this ShowRepositoryResponse.

        **参数解释：** 是否归档。

        :param archived: The archived of this ShowRepositoryResponse.
        :type archived: bool
        """
        self._archived = archived

    @property
    def ssh_url_to_repo(self):
        r"""Gets the ssh_url_to_repo of this ShowRepositoryResponse.

        **参数解释：** 仓库ssh地址。

        :return: The ssh_url_to_repo of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._ssh_url_to_repo

    @ssh_url_to_repo.setter
    def ssh_url_to_repo(self, ssh_url_to_repo):
        r"""Sets the ssh_url_to_repo of this ShowRepositoryResponse.

        **参数解释：** 仓库ssh地址。

        :param ssh_url_to_repo: The ssh_url_to_repo of this ShowRepositoryResponse.
        :type ssh_url_to_repo: str
        """
        self._ssh_url_to_repo = ssh_url_to_repo

    @property
    def http_url_to_repo(self):
        r"""Gets the http_url_to_repo of this ShowRepositoryResponse.

        **参数解释：** 仓库http地址。

        :return: The http_url_to_repo of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._http_url_to_repo

    @http_url_to_repo.setter
    def http_url_to_repo(self, http_url_to_repo):
        r"""Sets the http_url_to_repo of this ShowRepositoryResponse.

        **参数解释：** 仓库http地址。

        :param http_url_to_repo: The http_url_to_repo of this ShowRepositoryResponse.
        :type http_url_to_repo: str
        """
        self._http_url_to_repo = http_url_to_repo

    @property
    def web_url(self):
        r"""Gets the web_url of this ShowRepositoryResponse.

        **参数解释：** 仓库页面链接。

        :return: The web_url of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this ShowRepositoryResponse.

        **参数解释：** 仓库页面链接。

        :param web_url: The web_url of this ShowRepositoryResponse.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def readme_url(self):
        r"""Gets the readme_url of this ShowRepositoryResponse.

        **参数解释：** 仓库readme文件链接。

        :return: The readme_url of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._readme_url

    @readme_url.setter
    def readme_url(self, readme_url):
        r"""Sets the readme_url of this ShowRepositoryResponse.

        **参数解释：** 仓库readme文件链接。

        :param readme_url: The readme_url of this ShowRepositoryResponse.
        :type readme_url: str
        """
        self._readme_url = readme_url

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowRepositoryResponse.

        **参数解释：** 仓库所属项目ID。

        :return: The project_id of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowRepositoryResponse.

        **参数解释：** 仓库所属项目ID。

        :param project_id: The project_id of this ShowRepositoryResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this ShowRepositoryResponse.

        **参数解释：** 仓库所属项目名称。

        :return: The project_name of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ShowRepositoryResponse.

        **参数解释：** 仓库所属项目名称。

        :param project_name: The project_name of this ShowRepositoryResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def develop_mode(self):
        r"""Gets the develop_mode of this ShowRepositoryResponse.

        **参数解释：** 仓库开发模式。 **取值范围：** - normal - CR

        :return: The develop_mode of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._develop_mode

    @develop_mode.setter
    def develop_mode(self, develop_mode):
        r"""Sets the develop_mode of this ShowRepositoryResponse.

        **参数解释：** 仓库开发模式。 **取值范围：** - normal - CR

        :param develop_mode: The develop_mode of this ShowRepositoryResponse.
        :type develop_mode: str
        """
        self._develop_mode = develop_mode

    @property
    def moderation_result(self):
        r"""Gets the moderation_result of this ShowRepositoryResponse.

        **参数解释：** 审核状态。

        :return: The moderation_result of this ShowRepositoryResponse.
        :rtype: bool
        """
        return self._moderation_result

    @moderation_result.setter
    def moderation_result(self, moderation_result):
        r"""Sets the moderation_result of this ShowRepositoryResponse.

        **参数解释：** 审核状态。

        :param moderation_result: The moderation_result of this ShowRepositoryResponse.
        :type moderation_result: bool
        """
        self._moderation_result = moderation_result

    @property
    def default_branch(self):
        r"""Gets the default_branch of this ShowRepositoryResponse.

        **参数解释：** 仓库默认分支 **约束限制：** 不涉及。

        :return: The default_branch of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        r"""Sets the default_branch of this ShowRepositoryResponse.

        **参数解释：** 仓库默认分支 **约束限制：** 不涉及。

        :param default_branch: The default_branch of this ShowRepositoryResponse.
        :type default_branch: str
        """
        self._default_branch = default_branch

    @property
    def avatar_url(self):
        r"""Gets the avatar_url of this ShowRepositoryResponse.

        **参数解释：** 仓库图标url **约束限制：** 不涉及。

        :return: The avatar_url of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        r"""Sets the avatar_url of this ShowRepositoryResponse.

        **参数解释：** 仓库图标url **约束限制：** 不涉及。

        :param avatar_url: The avatar_url of this ShowRepositoryResponse.
        :type avatar_url: str
        """
        self._avatar_url = avatar_url

    @property
    def star_count(self):
        r"""Gets the star_count of this ShowRepositoryResponse.

        **参数解释：** 关注数 **约束限制：** 不涉及。

        :return: The star_count of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._star_count

    @star_count.setter
    def star_count(self, star_count):
        r"""Sets the star_count of this ShowRepositoryResponse.

        **参数解释：** 关注数 **约束限制：** 不涉及。

        :param star_count: The star_count of this ShowRepositoryResponse.
        :type star_count: int
        """
        self._star_count = star_count

    @property
    def forks_count(self):
        r"""Gets the forks_count of this ShowRepositoryResponse.

        **参数解释：** fork数 **约束限制：** 不涉及。

        :return: The forks_count of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._forks_count

    @forks_count.setter
    def forks_count(self, forks_count):
        r"""Sets the forks_count of this ShowRepositoryResponse.

        **参数解释：** fork数 **约束限制：** 不涉及。

        :param forks_count: The forks_count of this ShowRepositoryResponse.
        :type forks_count: int
        """
        self._forks_count = forks_count

    @property
    def open_issues_count(self):
        r"""Gets the open_issues_count of this ShowRepositoryResponse.

        **参数解释：** 开启issue数 **约束限制：** 不涉及。

        :return: The open_issues_count of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._open_issues_count

    @open_issues_count.setter
    def open_issues_count(self, open_issues_count):
        r"""Sets the open_issues_count of this ShowRepositoryResponse.

        **参数解释：** 开启issue数 **约束限制：** 不涉及。

        :param open_issues_count: The open_issues_count of this ShowRepositoryResponse.
        :type open_issues_count: int
        """
        self._open_issues_count = open_issues_count

    @property
    def open_merge_requests_count(self):
        r"""Gets the open_merge_requests_count of this ShowRepositoryResponse.

        **参数解释：** 开启中的CR、MR数量 **约束限制：** 不涉及。

        :return: The open_merge_requests_count of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._open_merge_requests_count

    @open_merge_requests_count.setter
    def open_merge_requests_count(self, open_merge_requests_count):
        r"""Sets the open_merge_requests_count of this ShowRepositoryResponse.

        **参数解释：** 开启中的CR、MR数量 **约束限制：** 不涉及。

        :param open_merge_requests_count: The open_merge_requests_count of this ShowRepositoryResponse.
        :type open_merge_requests_count: int
        """
        self._open_merge_requests_count = open_merge_requests_count

    @property
    def last_activity_at(self):
        r"""Gets the last_activity_at of this ShowRepositoryResponse.

        **参数解释：** 最后活跃时间 **约束限制：** 不涉及。

        :return: The last_activity_at of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._last_activity_at

    @last_activity_at.setter
    def last_activity_at(self, last_activity_at):
        r"""Sets the last_activity_at of this ShowRepositoryResponse.

        **参数解释：** 最后活跃时间 **约束限制：** 不涉及。

        :param last_activity_at: The last_activity_at of this ShowRepositoryResponse.
        :type last_activity_at: str
        """
        self._last_activity_at = last_activity_at

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowRepositoryResponse.

        :return: The namespace of this ShowRepositoryResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.NamespaceBasicDto`
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowRepositoryResponse.

        :param namespace: The namespace of this ShowRepositoryResponse.
        :type namespace: :class:`huaweicloudsdkcodehub.v4.NamespaceBasicDto`
        """
        self._namespace = namespace

    @property
    def empty_repo(self):
        r"""Gets the empty_repo of this ShowRepositoryResponse.

        **参数解释：** 空仓库 **约束限制：** 不涉及。

        :return: The empty_repo of this ShowRepositoryResponse.
        :rtype: bool
        """
        return self._empty_repo

    @empty_repo.setter
    def empty_repo(self, empty_repo):
        r"""Sets the empty_repo of this ShowRepositoryResponse.

        **参数解释：** 空仓库 **约束限制：** 不涉及。

        :param empty_repo: The empty_repo of this ShowRepositoryResponse.
        :type empty_repo: bool
        """
        self._empty_repo = empty_repo

    @property
    def starred(self):
        r"""Gets the starred of this ShowRepositoryResponse.

        **参数解释：** 是否已关注 **约束限制：** 不涉及。

        :return: The starred of this ShowRepositoryResponse.
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        r"""Sets the starred of this ShowRepositoryResponse.

        **参数解释：** 是否已关注 **约束限制：** 不涉及。

        :param starred: The starred of this ShowRepositoryResponse.
        :type starred: bool
        """
        self._starred = starred

    @property
    def visibility(self):
        r"""Gets the visibility of this ShowRepositoryResponse.

        **参数解释：** 仓库可见等级 **约束限制：** 不涉及。

        :return: The visibility of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ShowRepositoryResponse.

        **参数解释：** 仓库可见等级 **约束限制：** 不涉及。

        :param visibility: The visibility of this ShowRepositoryResponse.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def security_tag(self):
        r"""Gets the security_tag of this ShowRepositoryResponse.

        **参数解释：** 仓库保密等级 **约束限制：** 不涉及。

        :return: The security_tag of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._security_tag

    @security_tag.setter
    def security_tag(self, security_tag):
        r"""Sets the security_tag of this ShowRepositoryResponse.

        **参数解释：** 仓库保密等级 **约束限制：** 不涉及。

        :param security_tag: The security_tag of this ShowRepositoryResponse.
        :type security_tag: str
        """
        self._security_tag = security_tag

    @property
    def security(self):
        r"""Gets the security of this ShowRepositoryResponse.

        **参数解释：** 仓库保密等级 **约束限制：** 不涉及。

        :return: The security of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._security

    @security.setter
    def security(self, security):
        r"""Sets the security of this ShowRepositoryResponse.

        **参数解释：** 仓库保密等级 **约束限制：** 不涉及。

        :param security: The security of this ShowRepositoryResponse.
        :type security: str
        """
        self._security = security

    @property
    def network_type(self):
        r"""Gets the network_type of this ShowRepositoryResponse.

        **参数解释：** 网络类型 **约束限制：** 不涉及。

        :return: The network_type of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this ShowRepositoryResponse.

        **参数解释：** 网络类型 **约束限制：** 不涉及。

        :param network_type: The network_type of this ShowRepositoryResponse.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def owner(self):
        r"""Gets the owner of this ShowRepositoryResponse.

        :return: The owner of this ShowRepositoryResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepositoryUserBasicDto`
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ShowRepositoryResponse.

        :param owner: The owner of this ShowRepositoryResponse.
        :type owner: :class:`huaweicloudsdkcodehub.v4.RepositoryUserBasicDto`
        """
        self._owner = owner

    @property
    def creator(self):
        r"""Gets the creator of this ShowRepositoryResponse.

        :return: The creator of this ShowRepositoryResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepositoryUserBasicDto`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ShowRepositoryResponse.

        :param creator: The creator of this ShowRepositoryResponse.
        :type creator: :class:`huaweicloudsdkcodehub.v4.RepositoryUserBasicDto`
        """
        self._creator = creator

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ShowRepositoryResponse.

        **参数解释：** 创建者ID **约束限制：** 不涉及。

        :return: The creator_id of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ShowRepositoryResponse.

        **参数解释：** 创建者ID **约束限制：** 不涉及。

        :param creator_id: The creator_id of this ShowRepositoryResponse.
        :type creator_id: int
        """
        self._creator_id = creator_id

    @property
    def forked_from_repository(self):
        r"""Gets the forked_from_repository of this ShowRepositoryResponse.

        :return: The forked_from_repository of this ShowRepositoryResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepositorySimpleDto`
        """
        return self._forked_from_repository

    @forked_from_repository.setter
    def forked_from_repository(self, forked_from_repository):
        r"""Sets the forked_from_repository of this ShowRepositoryResponse.

        :param forked_from_repository: The forked_from_repository of this ShowRepositoryResponse.
        :type forked_from_repository: :class:`huaweicloudsdkcodehub.v4.RepositorySimpleDto`
        """
        self._forked_from_repository = forked_from_repository

    @property
    def uuid(self):
        r"""Gets the uuid of this ShowRepositoryResponse.

        **参数解释：** 仓库唯一标识符。 **约束限制：** 不涉及。

        :return: The uuid of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        r"""Sets the uuid of this ShowRepositoryResponse.

        **参数解释：** 仓库唯一标识符。 **约束限制：** 不涉及。

        :param uuid: The uuid of this ShowRepositoryResponse.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def ancestor_ids(self):
        r"""Gets the ancestor_ids of this ShowRepositoryResponse.

        **参数解释：** 祖先仓库ID列表。 **约束限制：** 不涉及。

        :return: The ancestor_ids of this ShowRepositoryResponse.
        :rtype: list[int]
        """
        return self._ancestor_ids

    @ancestor_ids.setter
    def ancestor_ids(self, ancestor_ids):
        r"""Sets the ancestor_ids of this ShowRepositoryResponse.

        **参数解释：** 祖先仓库ID列表。 **约束限制：** 不涉及。

        :param ancestor_ids: The ancestor_ids of this ShowRepositoryResponse.
        :type ancestor_ids: list[int]
        """
        self._ancestor_ids = ancestor_ids

    @property
    def ancestor_names(self):
        r"""Gets the ancestor_names of this ShowRepositoryResponse.

        **参数解释：** 祖先仓库名称列表。 **约束限制：** 不涉及。

        :return: The ancestor_names of this ShowRepositoryResponse.
        :rtype: list[str]
        """
        return self._ancestor_names

    @ancestor_names.setter
    def ancestor_names(self, ancestor_names):
        r"""Sets the ancestor_names of this ShowRepositoryResponse.

        **参数解释：** 祖先仓库名称列表。 **约束限制：** 不涉及。

        :param ancestor_names: The ancestor_names of this ShowRepositoryResponse.
        :type ancestor_names: list[str]
        """
        self._ancestor_names = ancestor_names

    @property
    def import_status(self):
        r"""Gets the import_status of this ShowRepositoryResponse.

        **参数解释：** 导入状态。 **约束限制：** 不涉及。

        :return: The import_status of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        r"""Sets the import_status of this ShowRepositoryResponse.

        **参数解释：** 导入状态。 **约束限制：** 不涉及。

        :param import_status: The import_status of this ShowRepositoryResponse.
        :type import_status: str
        """
        self._import_status = import_status

    @property
    def import_url(self):
        r"""Gets the import_url of this ShowRepositoryResponse.

        **参数解释：** 导入源地址。 **约束限制：** 不涉及。

        :return: The import_url of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._import_url

    @import_url.setter
    def import_url(self, import_url):
        r"""Sets the import_url of this ShowRepositoryResponse.

        **参数解释：** 导入源地址。 **约束限制：** 不涉及。

        :param import_url: The import_url of this ShowRepositoryResponse.
        :type import_url: str
        """
        self._import_url = import_url

    @property
    def import_error(self):
        r"""Gets the import_error of this ShowRepositoryResponse.

        **参数解释：** 导入错误信息。 **约束限制：** 不涉及。

        :return: The import_error of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._import_error

    @import_error.setter
    def import_error(self, import_error):
        r"""Sets the import_error of this ShowRepositoryResponse.

        **参数解释：** 导入错误信息。 **约束限制：** 不涉及。

        :param import_error: The import_error of this ShowRepositoryResponse.
        :type import_error: str
        """
        self._import_error = import_error

    @property
    def repo_type(self):
        r"""Gets the repo_type of this ShowRepositoryResponse.

        **参数解释：** 仓库类型。 **约束限制：** 不涉及。

        :return: The repo_type of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        r"""Sets the repo_type of this ShowRepositoryResponse.

        **参数解释：** 仓库类型。 **约束限制：** 不涉及。

        :param repo_type: The repo_type of this ShowRepositoryResponse.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def only_allow_merge_if_pipeline_succeeds(self):
        r"""Gets the only_allow_merge_if_pipeline_succeeds of this ShowRepositoryResponse.

        **参数解释：** 是否仅在流水线成功时允许合并。 **约束限制：** 不涉及。

        :return: The only_allow_merge_if_pipeline_succeeds of this ShowRepositoryResponse.
        :rtype: bool
        """
        return self._only_allow_merge_if_pipeline_succeeds

    @only_allow_merge_if_pipeline_succeeds.setter
    def only_allow_merge_if_pipeline_succeeds(self, only_allow_merge_if_pipeline_succeeds):
        r"""Sets the only_allow_merge_if_pipeline_succeeds of this ShowRepositoryResponse.

        **参数解释：** 是否仅在流水线成功时允许合并。 **约束限制：** 不涉及。

        :param only_allow_merge_if_pipeline_succeeds: The only_allow_merge_if_pipeline_succeeds of this ShowRepositoryResponse.
        :type only_allow_merge_if_pipeline_succeeds: bool
        """
        self._only_allow_merge_if_pipeline_succeeds = only_allow_merge_if_pipeline_succeeds

    @property
    def request_access_enabled(self):
        r"""Gets the request_access_enabled of this ShowRepositoryResponse.

        **参数解释：** 是否启用访问请求。 **约束限制：** 不涉及。

        :return: The request_access_enabled of this ShowRepositoryResponse.
        :rtype: bool
        """
        return self._request_access_enabled

    @request_access_enabled.setter
    def request_access_enabled(self, request_access_enabled):
        r"""Sets the request_access_enabled of this ShowRepositoryResponse.

        **参数解释：** 是否启用访问请求。 **约束限制：** 不涉及。

        :param request_access_enabled: The request_access_enabled of this ShowRepositoryResponse.
        :type request_access_enabled: bool
        """
        self._request_access_enabled = request_access_enabled

    @property
    def only_allow_merge_if_all_discussions_are_resolved(self):
        r"""Gets the only_allow_merge_if_all_discussions_are_resolved of this ShowRepositoryResponse.

        **参数解释：** 是否仅在所有检视意见解决时允许合并。 **约束限制：** 不涉及。

        :return: The only_allow_merge_if_all_discussions_are_resolved of this ShowRepositoryResponse.
        :rtype: bool
        """
        return self._only_allow_merge_if_all_discussions_are_resolved

    @only_allow_merge_if_all_discussions_are_resolved.setter
    def only_allow_merge_if_all_discussions_are_resolved(self, only_allow_merge_if_all_discussions_are_resolved):
        r"""Sets the only_allow_merge_if_all_discussions_are_resolved of this ShowRepositoryResponse.

        **参数解释：** 是否仅在所有检视意见解决时允许合并。 **约束限制：** 不涉及。

        :param only_allow_merge_if_all_discussions_are_resolved: The only_allow_merge_if_all_discussions_are_resolved of this ShowRepositoryResponse.
        :type only_allow_merge_if_all_discussions_are_resolved: bool
        """
        self._only_allow_merge_if_all_discussions_are_resolved = only_allow_merge_if_all_discussions_are_resolved

    @property
    def merge_method(self):
        r"""Gets the merge_method of this ShowRepositoryResponse.

        **参数解释：** 合并方法。 **约束限制：** 不涉及。

        :return: The merge_method of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._merge_method

    @merge_method.setter
    def merge_method(self, merge_method):
        r"""Sets the merge_method of this ShowRepositoryResponse.

        **参数解释：** 合并方法。 **约束限制：** 不涉及。

        :param merge_method: The merge_method of this ShowRepositoryResponse.
        :type merge_method: str
        """
        self._merge_method = merge_method

    @property
    def fork_network_repositories(self):
        r"""Gets the fork_network_repositories of this ShowRepositoryResponse.

        **参数解释：** fork关联仓库列表。 **约束限制：** 不涉及。

        :return: The fork_network_repositories of this ShowRepositoryResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.RepositoryIdentityDto`]
        """
        return self._fork_network_repositories

    @fork_network_repositories.setter
    def fork_network_repositories(self, fork_network_repositories):
        r"""Sets the fork_network_repositories of this ShowRepositoryResponse.

        **参数解释：** fork关联仓库列表。 **约束限制：** 不涉及。

        :param fork_network_repositories: The fork_network_repositories of this ShowRepositoryResponse.
        :type fork_network_repositories: list[:class:`huaweicloudsdkcodehub.v4.RepositoryIdentityDto`]
        """
        self._fork_network_repositories = fork_network_repositories

    @property
    def permissions(self):
        r"""Gets the permissions of this ShowRepositoryResponse.

        :return: The permissions of this ShowRepositoryResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.PermissionsDto`
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this ShowRepositoryResponse.

        :param permissions: The permissions of this ShowRepositoryResponse.
        :type permissions: :class:`huaweicloudsdkcodehub.v4.PermissionsDto`
        """
        self._permissions = permissions

    @property
    def repository_type(self):
        r"""Gets the repository_type of this ShowRepositoryResponse.

        **参数解释：** 仓库类型。 **约束限制：** 不涉及。

        :return: The repository_type of this ShowRepositoryResponse.
        :rtype: str
        """
        return self._repository_type

    @repository_type.setter
    def repository_type(self, repository_type):
        r"""Sets the repository_type of this ShowRepositoryResponse.

        **参数解释：** 仓库类型。 **约束限制：** 不涉及。

        :param repository_type: The repository_type of this ShowRepositoryResponse.
        :type repository_type: str
        """
        self._repository_type = repository_type

    @property
    def statistics(self):
        r"""Gets the statistics of this ShowRepositoryResponse.

        :return: The statistics of this ShowRepositoryResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.RepositoryStatisticsDto`
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        r"""Sets the statistics of this ShowRepositoryResponse.

        :param statistics: The statistics of this ShowRepositoryResponse.
        :type statistics: :class:`huaweicloudsdkcodehub.v4.RepositoryStatisticsDto`
        """
        self._statistics = statistics

    @property
    def branch_count(self):
        r"""Gets the branch_count of this ShowRepositoryResponse.

        **参数解释：** 分支数量。 **约束限制：** 不涉及。

        :return: The branch_count of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._branch_count

    @branch_count.setter
    def branch_count(self, branch_count):
        r"""Sets the branch_count of this ShowRepositoryResponse.

        **参数解释：** 分支数量。 **约束限制：** 不涉及。

        :param branch_count: The branch_count of this ShowRepositoryResponse.
        :type branch_count: int
        """
        self._branch_count = branch_count

    @property
    def tag_count(self):
        r"""Gets the tag_count of this ShowRepositoryResponse.

        **参数解释：** Tag数量。 **约束限制：** 不涉及。

        :return: The tag_count of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._tag_count

    @tag_count.setter
    def tag_count(self, tag_count):
        r"""Sets the tag_count of this ShowRepositoryResponse.

        **参数解释：** Tag数量。 **约束限制：** 不涉及。

        :param tag_count: The tag_count of this ShowRepositoryResponse.
        :type tag_count: int
        """
        self._tag_count = tag_count

    @property
    def label_count(self):
        r"""Gets the label_count of this ShowRepositoryResponse.

        **参数解释：** 标签数量。 **约束限制：** 不涉及。

        :return: The label_count of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._label_count

    @label_count.setter
    def label_count(self, label_count):
        r"""Sets the label_count of this ShowRepositoryResponse.

        **参数解释：** 标签数量。 **约束限制：** 不涉及。

        :param label_count: The label_count of this ShowRepositoryResponse.
        :type label_count: int
        """
        self._label_count = label_count

    @property
    def member_count(self):
        r"""Gets the member_count of this ShowRepositoryResponse.

        **参数解释：** 成员数量。 **约束限制：** 不涉及。

        :return: The member_count of this ShowRepositoryResponse.
        :rtype: int
        """
        return self._member_count

    @member_count.setter
    def member_count(self, member_count):
        r"""Sets the member_count of this ShowRepositoryResponse.

        **参数解释：** 成员数量。 **约束限制：** 不涉及。

        :param member_count: The member_count of this ShowRepositoryResponse.
        :type member_count: int
        """
        self._member_count = member_count

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
        if not isinstance(other, ShowRepositoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
