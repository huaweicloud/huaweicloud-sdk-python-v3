# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryDOV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'domain_id': 'str',
        'region': 'str',
        'created_time': 'str',
        'modified_time': 'str',
        'created_user_id': 'str',
        'created_user_name': 'str',
        'modified_user_id': 'str',
        'modified_user_name': 'str',
        'repository_name': 'str',
        'format': 'str',
        'type': 'str',
        'description': 'str',
        'release': 'str',
        'snapshot': 'str',
        'includes_pattern': 'str',
        'excludes_pattern': 'str',
        'share_right': 'str',
        'project_id': 'str',
        'name': 'str',
        'disable': 'bool',
        'policy': 'str',
        'npm': 'str',
        'uri': 'str',
        'repositories': 'str',
        'user_name': 'str',
        'password': 'str',
        'proxy': 'str',
        'scope': 'int',
        'url': 'str',
        'tab_id': 'str',
        'display_name': 'str',
        'snapshot_status': 'str',
        'release_status': 'str',
        'repository_ids': 'str',
        'deployment_policy': 'str',
        'parent_repo_name': 'str',
        'remote_url': 'str',
        'remote_auth': 'str',
        'pypi_registry_url': 'str',
        'default_deploy_repository': 'str',
        'package_type': 'str',
        'nexu_repo': 'bool',
        'migrate_flag': 'int'
    }

    attribute_map = {
        'status': 'status',
        'domain_id': 'domain_id',
        'region': 'region',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'created_user_id': 'created_user_id',
        'created_user_name': 'created_user_name',
        'modified_user_id': 'modified_user_id',
        'modified_user_name': 'modified_user_name',
        'repository_name': 'repository_name',
        'format': 'format',
        'type': 'type',
        'description': 'description',
        'release': 'release',
        'snapshot': 'snapshot',
        'includes_pattern': 'includes_pattern',
        'excludes_pattern': 'excludes_pattern',
        'share_right': 'share_right',
        'project_id': 'project_id',
        'name': 'name',
        'disable': 'disable',
        'policy': 'policy',
        'npm': 'npm',
        'uri': 'uri',
        'repositories': 'repositories',
        'user_name': 'user_name',
        'password': 'password',
        'proxy': 'proxy',
        'scope': 'scope',
        'url': 'url',
        'tab_id': 'tab_id',
        'display_name': 'display_name',
        'snapshot_status': 'snapshot_status',
        'release_status': 'release_status',
        'repository_ids': 'repository_ids',
        'deployment_policy': 'deployment_policy',
        'parent_repo_name': 'parent_repo_name',
        'remote_url': 'remote_url',
        'remote_auth': 'remote_auth',
        'pypi_registry_url': 'pypi_registry_url',
        'default_deploy_repository': 'default_deploy_repository',
        'package_type': 'package_type',
        'nexu_repo': 'nexu_repo',
        'migrate_flag': 'migrate_flag'
    }

    def __init__(self, status=None, domain_id=None, region=None, created_time=None, modified_time=None, created_user_id=None, created_user_name=None, modified_user_id=None, modified_user_name=None, repository_name=None, format=None, type=None, description=None, release=None, snapshot=None, includes_pattern=None, excludes_pattern=None, share_right=None, project_id=None, name=None, disable=None, policy=None, npm=None, uri=None, repositories=None, user_name=None, password=None, proxy=None, scope=None, url=None, tab_id=None, display_name=None, snapshot_status=None, release_status=None, repository_ids=None, deployment_policy=None, parent_repo_name=None, remote_url=None, remote_auth=None, pypi_registry_url=None, default_deploy_repository=None, package_type=None, nexu_repo=None, migrate_flag=None):
        r"""RepositoryDOV5

        The model defined in huaweicloud sdk

        :param status: **参数解释**: 仓库状态。 **取值范围**: active：正常。 delete：删除。 disabled：无效。 view：私有库浏览者。 trash：废弃。 
        :type status: str
        :param domain_id: **参数解释**: 租户id。 **取值范围**: 不涉及。
        :type domain_id: str
        :param region: **参数解释**: 区域。 **取值范围**: 不涉及。
        :type region: str
        :param created_time: **参数解释**: 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。
        :type created_time: str
        :param modified_time: **参数解释**: 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。
        :type modified_time: str
        :param created_user_id: **参数解释**: 创建人id。 **取值范围**: 不涉及。
        :type created_user_id: str
        :param created_user_name: **参数解释**: 创建人。 **取值范围**: 不涉及。
        :type created_user_name: str
        :param modified_user_id: **参数解释**: 修改人id。 **取值范围**: 不涉及。
        :type modified_user_id: str
        :param modified_user_name: **参数解释**: 修改人。 **取值范围**: 不涉及。
        :type modified_user_name: str
        :param repository_name: **参数解释**: 仓库名称。 **取值范围**: 不涉及。
        :type repository_name: str
        :param format: **参数解释**: 制品类型。 **取值范围**: - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda
        :type format: str
        :param type: **参数解释**: 仓库类型。 **取值范围**: hosted：本地仓库。 remote：代理仓库。 virtual：聚合仓库。 
        :type type: str
        :param description: **参数解释**: 仓库描述。 **取值范围**: 不涉及。
        :type description: str
        :param release: **参数解释**: release仓库名称,release和snapshot至少二选一。 **取值范围**: 不涉及。
        :type release: str
        :param snapshot: **参数解释**: snapshot仓库名称,release和snapshot至少二选一。 **取值范围**: 不涉及。
        :type snapshot: str
        :param includes_pattern: **参数解释**: 路径包含规则。 **取值范围**: 不涉及。
        :type includes_pattern: str
        :param excludes_pattern: **参数解释**: 路径排除规则。 **取值范围**: 不涉及。
        :type excludes_pattern: str
        :param share_right: **参数解释**: 共享权限级别。 **取值范围**: PROJECT。
        :type share_right: str
        :param project_id: **参数解释**: 项目ID。 **取值范围**: 不涉及。
        :type project_id: str
        :param name: **参数解释**: 仓库id。 **取值范围**: 不涉及。
        :type name: str
        :param disable: **参数解释**: 是否禁用。 **取值范围**: 不涉及。
        :type disable: bool
        :param policy: **参数解释**: 仓库策略。 **取值范围**: release或snapshot。
        :type policy: str
        :param npm: **参数解释**: npm。 **取值范围**: 不涉及。
        :type npm: str
        :param uri: **参数解释**: uri。 **取值范围**: 不涉及。
        :type uri: str
        :param repositories: **参数解释**: repositories。 **取值范围**: 不涉及。
        :type repositories: str
        :param user_name: **参数解释**: 账号。 **取值范围**: 不涉及。
        :type user_name: str
        :param password: **参数解释**: 密码。 **取值范围**: 不涉及。
        :type password: str
        :param proxy: **参数解释**: 代理。 **取值范围**: 不涉及。
        :type proxy: str
        :param scope: **参数解释**: 范围。 **取值范围**: 不涉及。
        :type scope: int
        :param url: **参数解释**: 地址。 **取值范围**: 不涉及。
        :type url: str
        :param tab_id: **参数解释**: 用于标记一对maven仓库(release、snapshot)，相同的tab_id即为一对maven仓库。 **取值范围**: 不涉及。 
        :type tab_id: str
        :param display_name: **参数解释**: 展示的仓库名称。 **取值范围**: 不涉及。
        :type display_name: str
        :param snapshot_status: **参数解释**: 快照仓状态。 **取值范围**: 不涉及。
        :type snapshot_status: str
        :param release_status: **参数解释**: 发布仓状态。 **取值范围**: 不涉及。
        :type release_status: str
        :param repository_ids: **参数解释**: 仓库id列表。 **取值范围**: 不涉及。
        :type repository_ids: str
        :param deployment_policy: **参数解释**: 覆盖策略。 **取值范围**: 不涉及。 
        :type deployment_policy: str
        :param parent_repo_name: **参数解释**: 父仓库名。 **取值范围**: 不涉及。
        :type parent_repo_name: str
        :param remote_url: **参数解释**: 代理仓地址。 **取值范围**: 不涉及。
        :type remote_url: str
        :param remote_auth: **参数解释**: 代理仓认证。 **取值范围**: 不涉及。
        :type remote_auth: str
        :param pypi_registry_url: **参数解释**: pypi索引代理地址。 **取值范围**: 不涉及。
        :type pypi_registry_url: str
        :param default_deploy_repository: **参数解释**: 虚仓的默认仓库。 **取值范围**: 不涉及。
        :type default_deploy_repository: str
        :param package_type: **参数解释**: 制品类型。 **取值范围**: 不涉及。
        :type package_type: str
        :param nexu_repo: **参数解释**: 是否nexu仓库。 **取值范围**: 不涉及。
        :type nexu_repo: bool
        :param migrate_flag: **参数解释**: 迁移标识。 **取值范围**: 不涉及。
        :type migrate_flag: int
        """
        
        

        self._status = None
        self._domain_id = None
        self._region = None
        self._created_time = None
        self._modified_time = None
        self._created_user_id = None
        self._created_user_name = None
        self._modified_user_id = None
        self._modified_user_name = None
        self._repository_name = None
        self._format = None
        self._type = None
        self._description = None
        self._release = None
        self._snapshot = None
        self._includes_pattern = None
        self._excludes_pattern = None
        self._share_right = None
        self._project_id = None
        self._name = None
        self._disable = None
        self._policy = None
        self._npm = None
        self._uri = None
        self._repositories = None
        self._user_name = None
        self._password = None
        self._proxy = None
        self._scope = None
        self._url = None
        self._tab_id = None
        self._display_name = None
        self._snapshot_status = None
        self._release_status = None
        self._repository_ids = None
        self._deployment_policy = None
        self._parent_repo_name = None
        self._remote_url = None
        self._remote_auth = None
        self._pypi_registry_url = None
        self._default_deploy_repository = None
        self._package_type = None
        self._nexu_repo = None
        self._migrate_flag = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if domain_id is not None:
            self.domain_id = domain_id
        if region is not None:
            self.region = region
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if created_user_id is not None:
            self.created_user_id = created_user_id
        if created_user_name is not None:
            self.created_user_name = created_user_name
        if modified_user_id is not None:
            self.modified_user_id = modified_user_id
        if modified_user_name is not None:
            self.modified_user_name = modified_user_name
        if repository_name is not None:
            self.repository_name = repository_name
        if format is not None:
            self.format = format
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if release is not None:
            self.release = release
        if snapshot is not None:
            self.snapshot = snapshot
        if includes_pattern is not None:
            self.includes_pattern = includes_pattern
        if excludes_pattern is not None:
            self.excludes_pattern = excludes_pattern
        if share_right is not None:
            self.share_right = share_right
        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if disable is not None:
            self.disable = disable
        if policy is not None:
            self.policy = policy
        if npm is not None:
            self.npm = npm
        if uri is not None:
            self.uri = uri
        if repositories is not None:
            self.repositories = repositories
        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password
        if proxy is not None:
            self.proxy = proxy
        if scope is not None:
            self.scope = scope
        if url is not None:
            self.url = url
        if tab_id is not None:
            self.tab_id = tab_id
        if display_name is not None:
            self.display_name = display_name
        if snapshot_status is not None:
            self.snapshot_status = snapshot_status
        if release_status is not None:
            self.release_status = release_status
        if repository_ids is not None:
            self.repository_ids = repository_ids
        if deployment_policy is not None:
            self.deployment_policy = deployment_policy
        if parent_repo_name is not None:
            self.parent_repo_name = parent_repo_name
        if remote_url is not None:
            self.remote_url = remote_url
        if remote_auth is not None:
            self.remote_auth = remote_auth
        if pypi_registry_url is not None:
            self.pypi_registry_url = pypi_registry_url
        if default_deploy_repository is not None:
            self.default_deploy_repository = default_deploy_repository
        if package_type is not None:
            self.package_type = package_type
        if nexu_repo is not None:
            self.nexu_repo = nexu_repo
        if migrate_flag is not None:
            self.migrate_flag = migrate_flag

    @property
    def status(self):
        r"""Gets the status of this RepositoryDOV5.

        **参数解释**: 仓库状态。 **取值范围**: active：正常。 delete：删除。 disabled：无效。 view：私有库浏览者。 trash：废弃。 

        :return: The status of this RepositoryDOV5.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RepositoryDOV5.

        **参数解释**: 仓库状态。 **取值范围**: active：正常。 delete：删除。 disabled：无效。 view：私有库浏览者。 trash：废弃。 

        :param status: The status of this RepositoryDOV5.
        :type status: str
        """
        self._status = status

    @property
    def domain_id(self):
        r"""Gets the domain_id of this RepositoryDOV5.

        **参数解释**: 租户id。 **取值范围**: 不涉及。

        :return: The domain_id of this RepositoryDOV5.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this RepositoryDOV5.

        **参数解释**: 租户id。 **取值范围**: 不涉及。

        :param domain_id: The domain_id of this RepositoryDOV5.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region(self):
        r"""Gets the region of this RepositoryDOV5.

        **参数解释**: 区域。 **取值范围**: 不涉及。

        :return: The region of this RepositoryDOV5.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this RepositoryDOV5.

        **参数解释**: 区域。 **取值范围**: 不涉及。

        :param region: The region of this RepositoryDOV5.
        :type region: str
        """
        self._region = region

    @property
    def created_time(self):
        r"""Gets the created_time of this RepositoryDOV5.

        **参数解释**: 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :return: The created_time of this RepositoryDOV5.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this RepositoryDOV5.

        **参数解释**: 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :param created_time: The created_time of this RepositoryDOV5.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this RepositoryDOV5.

        **参数解释**: 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :return: The modified_time of this RepositoryDOV5.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this RepositoryDOV5.

        **参数解释**: 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**: 不涉及。

        :param modified_time: The modified_time of this RepositoryDOV5.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def created_user_id(self):
        r"""Gets the created_user_id of this RepositoryDOV5.

        **参数解释**: 创建人id。 **取值范围**: 不涉及。

        :return: The created_user_id of this RepositoryDOV5.
        :rtype: str
        """
        return self._created_user_id

    @created_user_id.setter
    def created_user_id(self, created_user_id):
        r"""Sets the created_user_id of this RepositoryDOV5.

        **参数解释**: 创建人id。 **取值范围**: 不涉及。

        :param created_user_id: The created_user_id of this RepositoryDOV5.
        :type created_user_id: str
        """
        self._created_user_id = created_user_id

    @property
    def created_user_name(self):
        r"""Gets the created_user_name of this RepositoryDOV5.

        **参数解释**: 创建人。 **取值范围**: 不涉及。

        :return: The created_user_name of this RepositoryDOV5.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        r"""Sets the created_user_name of this RepositoryDOV5.

        **参数解释**: 创建人。 **取值范围**: 不涉及。

        :param created_user_name: The created_user_name of this RepositoryDOV5.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def modified_user_id(self):
        r"""Gets the modified_user_id of this RepositoryDOV5.

        **参数解释**: 修改人id。 **取值范围**: 不涉及。

        :return: The modified_user_id of this RepositoryDOV5.
        :rtype: str
        """
        return self._modified_user_id

    @modified_user_id.setter
    def modified_user_id(self, modified_user_id):
        r"""Sets the modified_user_id of this RepositoryDOV5.

        **参数解释**: 修改人id。 **取值范围**: 不涉及。

        :param modified_user_id: The modified_user_id of this RepositoryDOV5.
        :type modified_user_id: str
        """
        self._modified_user_id = modified_user_id

    @property
    def modified_user_name(self):
        r"""Gets the modified_user_name of this RepositoryDOV5.

        **参数解释**: 修改人。 **取值范围**: 不涉及。

        :return: The modified_user_name of this RepositoryDOV5.
        :rtype: str
        """
        return self._modified_user_name

    @modified_user_name.setter
    def modified_user_name(self, modified_user_name):
        r"""Sets the modified_user_name of this RepositoryDOV5.

        **参数解释**: 修改人。 **取值范围**: 不涉及。

        :param modified_user_name: The modified_user_name of this RepositoryDOV5.
        :type modified_user_name: str
        """
        self._modified_user_name = modified_user_name

    @property
    def repository_name(self):
        r"""Gets the repository_name of this RepositoryDOV5.

        **参数解释**: 仓库名称。 **取值范围**: 不涉及。

        :return: The repository_name of this RepositoryDOV5.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this RepositoryDOV5.

        **参数解释**: 仓库名称。 **取值范围**: 不涉及。

        :param repository_name: The repository_name of this RepositoryDOV5.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def format(self):
        r"""Gets the format of this RepositoryDOV5.

        **参数解释**: 制品类型。 **取值范围**: - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda

        :return: The format of this RepositoryDOV5.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this RepositoryDOV5.

        **参数解释**: 制品类型。 **取值范围**: - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda

        :param format: The format of this RepositoryDOV5.
        :type format: str
        """
        self._format = format

    @property
    def type(self):
        r"""Gets the type of this RepositoryDOV5.

        **参数解释**: 仓库类型。 **取值范围**: hosted：本地仓库。 remote：代理仓库。 virtual：聚合仓库。 

        :return: The type of this RepositoryDOV5.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RepositoryDOV5.

        **参数解释**: 仓库类型。 **取值范围**: hosted：本地仓库。 remote：代理仓库。 virtual：聚合仓库。 

        :param type: The type of this RepositoryDOV5.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this RepositoryDOV5.

        **参数解释**: 仓库描述。 **取值范围**: 不涉及。

        :return: The description of this RepositoryDOV5.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RepositoryDOV5.

        **参数解释**: 仓库描述。 **取值范围**: 不涉及。

        :param description: The description of this RepositoryDOV5.
        :type description: str
        """
        self._description = description

    @property
    def release(self):
        r"""Gets the release of this RepositoryDOV5.

        **参数解释**: release仓库名称,release和snapshot至少二选一。 **取值范围**: 不涉及。

        :return: The release of this RepositoryDOV5.
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        r"""Sets the release of this RepositoryDOV5.

        **参数解释**: release仓库名称,release和snapshot至少二选一。 **取值范围**: 不涉及。

        :param release: The release of this RepositoryDOV5.
        :type release: str
        """
        self._release = release

    @property
    def snapshot(self):
        r"""Gets the snapshot of this RepositoryDOV5.

        **参数解释**: snapshot仓库名称,release和snapshot至少二选一。 **取值范围**: 不涉及。

        :return: The snapshot of this RepositoryDOV5.
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        r"""Sets the snapshot of this RepositoryDOV5.

        **参数解释**: snapshot仓库名称,release和snapshot至少二选一。 **取值范围**: 不涉及。

        :param snapshot: The snapshot of this RepositoryDOV5.
        :type snapshot: str
        """
        self._snapshot = snapshot

    @property
    def includes_pattern(self):
        r"""Gets the includes_pattern of this RepositoryDOV5.

        **参数解释**: 路径包含规则。 **取值范围**: 不涉及。

        :return: The includes_pattern of this RepositoryDOV5.
        :rtype: str
        """
        return self._includes_pattern

    @includes_pattern.setter
    def includes_pattern(self, includes_pattern):
        r"""Sets the includes_pattern of this RepositoryDOV5.

        **参数解释**: 路径包含规则。 **取值范围**: 不涉及。

        :param includes_pattern: The includes_pattern of this RepositoryDOV5.
        :type includes_pattern: str
        """
        self._includes_pattern = includes_pattern

    @property
    def excludes_pattern(self):
        r"""Gets the excludes_pattern of this RepositoryDOV5.

        **参数解释**: 路径排除规则。 **取值范围**: 不涉及。

        :return: The excludes_pattern of this RepositoryDOV5.
        :rtype: str
        """
        return self._excludes_pattern

    @excludes_pattern.setter
    def excludes_pattern(self, excludes_pattern):
        r"""Sets the excludes_pattern of this RepositoryDOV5.

        **参数解释**: 路径排除规则。 **取值范围**: 不涉及。

        :param excludes_pattern: The excludes_pattern of this RepositoryDOV5.
        :type excludes_pattern: str
        """
        self._excludes_pattern = excludes_pattern

    @property
    def share_right(self):
        r"""Gets the share_right of this RepositoryDOV5.

        **参数解释**: 共享权限级别。 **取值范围**: PROJECT。

        :return: The share_right of this RepositoryDOV5.
        :rtype: str
        """
        return self._share_right

    @share_right.setter
    def share_right(self, share_right):
        r"""Sets the share_right of this RepositoryDOV5.

        **参数解释**: 共享权限级别。 **取值范围**: PROJECT。

        :param share_right: The share_right of this RepositoryDOV5.
        :type share_right: str
        """
        self._share_right = share_right

    @property
    def project_id(self):
        r"""Gets the project_id of this RepositoryDOV5.

        **参数解释**: 项目ID。 **取值范围**: 不涉及。

        :return: The project_id of this RepositoryDOV5.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RepositoryDOV5.

        **参数解释**: 项目ID。 **取值范围**: 不涉及。

        :param project_id: The project_id of this RepositoryDOV5.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this RepositoryDOV5.

        **参数解释**: 仓库id。 **取值范围**: 不涉及。

        :return: The name of this RepositoryDOV5.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepositoryDOV5.

        **参数解释**: 仓库id。 **取值范围**: 不涉及。

        :param name: The name of this RepositoryDOV5.
        :type name: str
        """
        self._name = name

    @property
    def disable(self):
        r"""Gets the disable of this RepositoryDOV5.

        **参数解释**: 是否禁用。 **取值范围**: 不涉及。

        :return: The disable of this RepositoryDOV5.
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        r"""Sets the disable of this RepositoryDOV5.

        **参数解释**: 是否禁用。 **取值范围**: 不涉及。

        :param disable: The disable of this RepositoryDOV5.
        :type disable: bool
        """
        self._disable = disable

    @property
    def policy(self):
        r"""Gets the policy of this RepositoryDOV5.

        **参数解释**: 仓库策略。 **取值范围**: release或snapshot。

        :return: The policy of this RepositoryDOV5.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this RepositoryDOV5.

        **参数解释**: 仓库策略。 **取值范围**: release或snapshot。

        :param policy: The policy of this RepositoryDOV5.
        :type policy: str
        """
        self._policy = policy

    @property
    def npm(self):
        r"""Gets the npm of this RepositoryDOV5.

        **参数解释**: npm。 **取值范围**: 不涉及。

        :return: The npm of this RepositoryDOV5.
        :rtype: str
        """
        return self._npm

    @npm.setter
    def npm(self, npm):
        r"""Sets the npm of this RepositoryDOV5.

        **参数解释**: npm。 **取值范围**: 不涉及。

        :param npm: The npm of this RepositoryDOV5.
        :type npm: str
        """
        self._npm = npm

    @property
    def uri(self):
        r"""Gets the uri of this RepositoryDOV5.

        **参数解释**: uri。 **取值范围**: 不涉及。

        :return: The uri of this RepositoryDOV5.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this RepositoryDOV5.

        **参数解释**: uri。 **取值范围**: 不涉及。

        :param uri: The uri of this RepositoryDOV5.
        :type uri: str
        """
        self._uri = uri

    @property
    def repositories(self):
        r"""Gets the repositories of this RepositoryDOV5.

        **参数解释**: repositories。 **取值范围**: 不涉及。

        :return: The repositories of this RepositoryDOV5.
        :rtype: str
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        r"""Sets the repositories of this RepositoryDOV5.

        **参数解释**: repositories。 **取值范围**: 不涉及。

        :param repositories: The repositories of this RepositoryDOV5.
        :type repositories: str
        """
        self._repositories = repositories

    @property
    def user_name(self):
        r"""Gets the user_name of this RepositoryDOV5.

        **参数解释**: 账号。 **取值范围**: 不涉及。

        :return: The user_name of this RepositoryDOV5.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this RepositoryDOV5.

        **参数解释**: 账号。 **取值范围**: 不涉及。

        :param user_name: The user_name of this RepositoryDOV5.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        r"""Gets the password of this RepositoryDOV5.

        **参数解释**: 密码。 **取值范围**: 不涉及。

        :return: The password of this RepositoryDOV5.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this RepositoryDOV5.

        **参数解释**: 密码。 **取值范围**: 不涉及。

        :param password: The password of this RepositoryDOV5.
        :type password: str
        """
        self._password = password

    @property
    def proxy(self):
        r"""Gets the proxy of this RepositoryDOV5.

        **参数解释**: 代理。 **取值范围**: 不涉及。

        :return: The proxy of this RepositoryDOV5.
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        r"""Sets the proxy of this RepositoryDOV5.

        **参数解释**: 代理。 **取值范围**: 不涉及。

        :param proxy: The proxy of this RepositoryDOV5.
        :type proxy: str
        """
        self._proxy = proxy

    @property
    def scope(self):
        r"""Gets the scope of this RepositoryDOV5.

        **参数解释**: 范围。 **取值范围**: 不涉及。

        :return: The scope of this RepositoryDOV5.
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this RepositoryDOV5.

        **参数解释**: 范围。 **取值范围**: 不涉及。

        :param scope: The scope of this RepositoryDOV5.
        :type scope: int
        """
        self._scope = scope

    @property
    def url(self):
        r"""Gets the url of this RepositoryDOV5.

        **参数解释**: 地址。 **取值范围**: 不涉及。

        :return: The url of this RepositoryDOV5.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this RepositoryDOV5.

        **参数解释**: 地址。 **取值范围**: 不涉及。

        :param url: The url of this RepositoryDOV5.
        :type url: str
        """
        self._url = url

    @property
    def tab_id(self):
        r"""Gets the tab_id of this RepositoryDOV5.

        **参数解释**: 用于标记一对maven仓库(release、snapshot)，相同的tab_id即为一对maven仓库。 **取值范围**: 不涉及。 

        :return: The tab_id of this RepositoryDOV5.
        :rtype: str
        """
        return self._tab_id

    @tab_id.setter
    def tab_id(self, tab_id):
        r"""Sets the tab_id of this RepositoryDOV5.

        **参数解释**: 用于标记一对maven仓库(release、snapshot)，相同的tab_id即为一对maven仓库。 **取值范围**: 不涉及。 

        :param tab_id: The tab_id of this RepositoryDOV5.
        :type tab_id: str
        """
        self._tab_id = tab_id

    @property
    def display_name(self):
        r"""Gets the display_name of this RepositoryDOV5.

        **参数解释**: 展示的仓库名称。 **取值范围**: 不涉及。

        :return: The display_name of this RepositoryDOV5.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this RepositoryDOV5.

        **参数解释**: 展示的仓库名称。 **取值范围**: 不涉及。

        :param display_name: The display_name of this RepositoryDOV5.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def snapshot_status(self):
        r"""Gets the snapshot_status of this RepositoryDOV5.

        **参数解释**: 快照仓状态。 **取值范围**: 不涉及。

        :return: The snapshot_status of this RepositoryDOV5.
        :rtype: str
        """
        return self._snapshot_status

    @snapshot_status.setter
    def snapshot_status(self, snapshot_status):
        r"""Sets the snapshot_status of this RepositoryDOV5.

        **参数解释**: 快照仓状态。 **取值范围**: 不涉及。

        :param snapshot_status: The snapshot_status of this RepositoryDOV5.
        :type snapshot_status: str
        """
        self._snapshot_status = snapshot_status

    @property
    def release_status(self):
        r"""Gets the release_status of this RepositoryDOV5.

        **参数解释**: 发布仓状态。 **取值范围**: 不涉及。

        :return: The release_status of this RepositoryDOV5.
        :rtype: str
        """
        return self._release_status

    @release_status.setter
    def release_status(self, release_status):
        r"""Sets the release_status of this RepositoryDOV5.

        **参数解释**: 发布仓状态。 **取值范围**: 不涉及。

        :param release_status: The release_status of this RepositoryDOV5.
        :type release_status: str
        """
        self._release_status = release_status

    @property
    def repository_ids(self):
        r"""Gets the repository_ids of this RepositoryDOV5.

        **参数解释**: 仓库id列表。 **取值范围**: 不涉及。

        :return: The repository_ids of this RepositoryDOV5.
        :rtype: str
        """
        return self._repository_ids

    @repository_ids.setter
    def repository_ids(self, repository_ids):
        r"""Sets the repository_ids of this RepositoryDOV5.

        **参数解释**: 仓库id列表。 **取值范围**: 不涉及。

        :param repository_ids: The repository_ids of this RepositoryDOV5.
        :type repository_ids: str
        """
        self._repository_ids = repository_ids

    @property
    def deployment_policy(self):
        r"""Gets the deployment_policy of this RepositoryDOV5.

        **参数解释**: 覆盖策略。 **取值范围**: 不涉及。 

        :return: The deployment_policy of this RepositoryDOV5.
        :rtype: str
        """
        return self._deployment_policy

    @deployment_policy.setter
    def deployment_policy(self, deployment_policy):
        r"""Sets the deployment_policy of this RepositoryDOV5.

        **参数解释**: 覆盖策略。 **取值范围**: 不涉及。 

        :param deployment_policy: The deployment_policy of this RepositoryDOV5.
        :type deployment_policy: str
        """
        self._deployment_policy = deployment_policy

    @property
    def parent_repo_name(self):
        r"""Gets the parent_repo_name of this RepositoryDOV5.

        **参数解释**: 父仓库名。 **取值范围**: 不涉及。

        :return: The parent_repo_name of this RepositoryDOV5.
        :rtype: str
        """
        return self._parent_repo_name

    @parent_repo_name.setter
    def parent_repo_name(self, parent_repo_name):
        r"""Sets the parent_repo_name of this RepositoryDOV5.

        **参数解释**: 父仓库名。 **取值范围**: 不涉及。

        :param parent_repo_name: The parent_repo_name of this RepositoryDOV5.
        :type parent_repo_name: str
        """
        self._parent_repo_name = parent_repo_name

    @property
    def remote_url(self):
        r"""Gets the remote_url of this RepositoryDOV5.

        **参数解释**: 代理仓地址。 **取值范围**: 不涉及。

        :return: The remote_url of this RepositoryDOV5.
        :rtype: str
        """
        return self._remote_url

    @remote_url.setter
    def remote_url(self, remote_url):
        r"""Sets the remote_url of this RepositoryDOV5.

        **参数解释**: 代理仓地址。 **取值范围**: 不涉及。

        :param remote_url: The remote_url of this RepositoryDOV5.
        :type remote_url: str
        """
        self._remote_url = remote_url

    @property
    def remote_auth(self):
        r"""Gets the remote_auth of this RepositoryDOV5.

        **参数解释**: 代理仓认证。 **取值范围**: 不涉及。

        :return: The remote_auth of this RepositoryDOV5.
        :rtype: str
        """
        return self._remote_auth

    @remote_auth.setter
    def remote_auth(self, remote_auth):
        r"""Sets the remote_auth of this RepositoryDOV5.

        **参数解释**: 代理仓认证。 **取值范围**: 不涉及。

        :param remote_auth: The remote_auth of this RepositoryDOV5.
        :type remote_auth: str
        """
        self._remote_auth = remote_auth

    @property
    def pypi_registry_url(self):
        r"""Gets the pypi_registry_url of this RepositoryDOV5.

        **参数解释**: pypi索引代理地址。 **取值范围**: 不涉及。

        :return: The pypi_registry_url of this RepositoryDOV5.
        :rtype: str
        """
        return self._pypi_registry_url

    @pypi_registry_url.setter
    def pypi_registry_url(self, pypi_registry_url):
        r"""Sets the pypi_registry_url of this RepositoryDOV5.

        **参数解释**: pypi索引代理地址。 **取值范围**: 不涉及。

        :param pypi_registry_url: The pypi_registry_url of this RepositoryDOV5.
        :type pypi_registry_url: str
        """
        self._pypi_registry_url = pypi_registry_url

    @property
    def default_deploy_repository(self):
        r"""Gets the default_deploy_repository of this RepositoryDOV5.

        **参数解释**: 虚仓的默认仓库。 **取值范围**: 不涉及。

        :return: The default_deploy_repository of this RepositoryDOV5.
        :rtype: str
        """
        return self._default_deploy_repository

    @default_deploy_repository.setter
    def default_deploy_repository(self, default_deploy_repository):
        r"""Sets the default_deploy_repository of this RepositoryDOV5.

        **参数解释**: 虚仓的默认仓库。 **取值范围**: 不涉及。

        :param default_deploy_repository: The default_deploy_repository of this RepositoryDOV5.
        :type default_deploy_repository: str
        """
        self._default_deploy_repository = default_deploy_repository

    @property
    def package_type(self):
        r"""Gets the package_type of this RepositoryDOV5.

        **参数解释**: 制品类型。 **取值范围**: 不涉及。

        :return: The package_type of this RepositoryDOV5.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this RepositoryDOV5.

        **参数解释**: 制品类型。 **取值范围**: 不涉及。

        :param package_type: The package_type of this RepositoryDOV5.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def nexu_repo(self):
        r"""Gets the nexu_repo of this RepositoryDOV5.

        **参数解释**: 是否nexu仓库。 **取值范围**: 不涉及。

        :return: The nexu_repo of this RepositoryDOV5.
        :rtype: bool
        """
        return self._nexu_repo

    @nexu_repo.setter
    def nexu_repo(self, nexu_repo):
        r"""Sets the nexu_repo of this RepositoryDOV5.

        **参数解释**: 是否nexu仓库。 **取值范围**: 不涉及。

        :param nexu_repo: The nexu_repo of this RepositoryDOV5.
        :type nexu_repo: bool
        """
        self._nexu_repo = nexu_repo

    @property
    def migrate_flag(self):
        r"""Gets the migrate_flag of this RepositoryDOV5.

        **参数解释**: 迁移标识。 **取值范围**: 不涉及。

        :return: The migrate_flag of this RepositoryDOV5.
        :rtype: int
        """
        return self._migrate_flag

    @migrate_flag.setter
    def migrate_flag(self, migrate_flag):
        r"""Sets the migrate_flag of this RepositoryDOV5.

        **参数解释**: 迁移标识。 **取值范围**: 不涉及。

        :param migrate_flag: The migrate_flag of this RepositoryDOV5.
        :type migrate_flag: int
        """
        self._migrate_flag = migrate_flag

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
        if not isinstance(other, RepositoryDOV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
