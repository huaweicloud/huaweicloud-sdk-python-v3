# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryBuildVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'password': 'str',
        'status': 'str',
        'domain_id': 'str',
        'region': 'str',
        'created_time': 'str',
        'modified_time': 'str',
        'created_user_id': 'str',
        'created_user_name': 'str',
        'modified_user_id': 'str',
        'modified_user_name': 'str',
        'name': 'str',
        'disable': 'bool',
        'format': 'str',
        'type': 'str',
        'policy': 'str',
        'tab_id': 'str',
        'repository_name': 'str',
        'display_name': 'str',
        'description': 'str',
        'snapshot': 'str',
        'release': 'str',
        'npm': 'str',
        'snapshot_status': 'str',
        'release_status': 'str',
        'project_id': 'str',
        'includes_pattern': 'str',
        'repository_ids': 'list[str]',
        'uri': 'str',
        'deployment_policy': 'str',
        'repositories': 'list[str]',
        'parent_repo_name': 'str',
        'user_name': 'str',
        'remote_url': 'str',
        'default_deploy_repository': 'str',
        'remote_type': 'str',
        'proxy': 'str',
        'allow_anonymous': 'bool',
        'auto_clean_snapshot': 'bool',
        'snapshot_alive_days': 'str',
        'max_unique_snapshots': 'str',
        'share_right': 'str',
        'nexu_repo': 'bool',
        'url': 'str',
        'package_type': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'status': 'status',
        'domain_id': 'domainId',
        'region': 'region',
        'created_time': 'createdTime',
        'modified_time': 'modifiedTime',
        'created_user_id': 'createdUserId',
        'created_user_name': 'createdUserName',
        'modified_user_id': 'modifiedUserId',
        'modified_user_name': 'modifiedUserName',
        'name': 'name',
        'disable': 'disable',
        'format': 'format',
        'type': 'type',
        'policy': 'policy',
        'tab_id': 'tabId',
        'repository_name': 'repositoryName',
        'display_name': 'displayName',
        'description': 'description',
        'snapshot': 'snapshot',
        'release': 'release',
        'npm': 'npm',
        'snapshot_status': 'snapshotStatus',
        'release_status': 'releaseStatus',
        'project_id': 'projectId',
        'includes_pattern': 'includesPattern',
        'repository_ids': 'repositoryIds',
        'uri': 'uri',
        'deployment_policy': 'deploymentPolicy',
        'repositories': 'repositories',
        'parent_repo_name': 'parentRepoName',
        'user_name': 'userName',
        'remote_url': 'remoteUrl',
        'default_deploy_repository': 'defaultDeployRepository',
        'remote_type': 'remoteType',
        'proxy': 'proxy',
        'allow_anonymous': 'allowAnonymous',
        'auto_clean_snapshot': 'autoCleanSnapshot',
        'snapshot_alive_days': 'snapshotAliveDays',
        'max_unique_snapshots': 'maxUniqueSnapshots',
        'share_right': 'shareRight',
        'nexu_repo': 'nexuRepo',
        'url': 'url',
        'package_type': 'packageType'
    }

    def __init__(self, username=None, password=None, status=None, domain_id=None, region=None, created_time=None, modified_time=None, created_user_id=None, created_user_name=None, modified_user_id=None, modified_user_name=None, name=None, disable=None, format=None, type=None, policy=None, tab_id=None, repository_name=None, display_name=None, description=None, snapshot=None, release=None, npm=None, snapshot_status=None, release_status=None, project_id=None, includes_pattern=None, repository_ids=None, uri=None, deployment_policy=None, repositories=None, parent_repo_name=None, user_name=None, remote_url=None, default_deploy_repository=None, remote_type=None, proxy=None, allow_anonymous=None, auto_clean_snapshot=None, snapshot_alive_days=None, max_unique_snapshots=None, share_right=None, nexu_repo=None, url=None, package_type=None):
        r"""RepositoryBuildVO

        The model defined in huaweicloud sdk

        :param username: **参数解释**： 账号。 **取值范围**： 不涉及。
        :type username: str
        :param password: **参数解释**： 密码。 **取值范围**： 不涉及。
        :type password: str
        :param status: **参数解释**： 仓库状态。 **取值范围**： - active：正常。 - delete：删除。 - disabled：无效。 - view：可浏览。 - trash：废弃。
        :type status: str
        :param domain_id: **参数解释**： 租户ID。 **取值范围**： 不涉及。
        :type domain_id: str
        :param region: **参数解释**： 区域。 **取值范围**： 不涉及。
        :type region: str
        :param created_time: **参数解释**： 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。
        :type created_time: str
        :param modified_time: **参数解释**： 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。
        :type modified_time: str
        :param created_user_id: **参数解释**： 创建人ID。 **取值范围**： 不涉及。
        :type created_user_id: str
        :param created_user_name: **参数解释**： 创建人名称。 **取值范围**： 不涉及。
        :type created_user_name: str
        :param modified_user_id: **参数解释**： 修改人ID。 **取值范围**： 不涉及。
        :type modified_user_id: str
        :param modified_user_name: **参数解释**： 修改人名称。 **取值范围**： 不涉及。
        :type modified_user_name: str
        :param name: **参数解释**： 仓库ID。 **取值范围**： 不涉及。
        :type name: str
        :param disable: **参数解释**： 是否禁用。 **取值范围**： 不涉及。
        :type disable: bool
        :param format: **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml
        :type format: str
        :param type: **参数解释**： 仓库类型。 **取值范围**： - hosted：本地仓库。 - remote：代理仓库。 - virtual：虚拟仓库。
        :type type: str
        :param policy: **参数解释**： 仓库策略。 **取值范围**： - release：正式仓库。 - snapshot：快照仓库。
        :type policy: str
        :param tab_id: **参数解释**： 用于标记一对Maven仓库(release、snapshot)，相同的tab_id即为一对Maven仓库。 **取值范围**： 不涉及。
        :type tab_id: str
        :param repository_name: **参数解释**： 仓库名称。 **取值范围**： 不涉及。
        :type repository_name: str
        :param display_name: **参数解释**： 展示的仓库名称。 **取值范围**： 不涉及。
        :type display_name: str
        :param description: **参数解释**： 仓库描述。 **取值范围**： 不涉及。
        :type description: str
        :param snapshot: **参数解释**： snapshot仓库名称,release和snapshot至少二选一。 **取值范围**： 不涉及。
        :type snapshot: str
        :param release: **参数解释**： release仓库名称,release和snapshot至少二选一。 **取值范围**： 不涉及。
        :type release: str
        :param npm: **参数解释**： npm。 **取值范围**： 不涉及。
        :type npm: str
        :param snapshot_status: **参数解释**： 快照仓库状态。 **取值范围**： 不涉及。
        :type snapshot_status: str
        :param release_status: **参数解释**： 正式仓库状态。 **取值范围**： 不涉及。
        :type release_status: str
        :param project_id: **参数解释**： 项目id。 **取值范围**： 不涉及。
        :type project_id: str
        :param includes_pattern: **参数解释**： 路径包含规则。 **取值范围**： 不涉及。
        :type includes_pattern: str
        :param repository_ids: **参数解释**： 仓库ID列表。 **取值范围**： 不涉及。
        :type repository_ids: list[str]
        :param uri: **参数解释**： uri。 **取值范围**： 不涉及。
        :type uri: str
        :param deployment_policy: **参数解释**： 覆盖策略。 **取值范围**： 不涉及。
        :type deployment_policy: str
        :param repositories: **参数解释**： 仓库列表。 **取值范围**： 不涉及。
        :type repositories: list[str]
        :param parent_repo_name: **参数解释**： 父仓库名。 **取值范围**： 不涉及。
        :type parent_repo_name: str
        :param user_name: **参数解释**: 用户名。 **取值范围**: 不涉及。
        :type user_name: str
        :param remote_url: **参数解释**： 代理仓地址。 **取值范围**： 不涉及。
        :type remote_url: str
        :param default_deploy_repository: **参数解释**： 默认仓库。 **取值范围**： 不涉及。
        :type default_deploy_repository: str
        :param remote_type: **参数解释**： 代理仓类型。 **取值范围**： - public：公共代理仓； - customize：用户自定义代理仓。
        :type remote_type: str
        :param proxy: **参数解释**： 代理。 **取值范围**： 不涉及。
        :type proxy: str
        :param allow_anonymous: **参数解释**： 是否允许匿名下载。 **取值范围**： 不涉及。
        :type allow_anonymous: bool
        :param auto_clean_snapshot: **参数解释**： 是否自动清理快照版本。 **取值范围**： 不涉及。
        :type auto_clean_snapshot: bool
        :param snapshot_alive_days: **参数解释**： 快照版本有效期，单位：天。 **取值范围**： 不涉及。
        :type snapshot_alive_days: str
        :param max_unique_snapshots: **参数解释**： 最大快照数。 **取值范围**： 不涉及。
        :type max_unique_snapshots: str
        :param share_right: **参数解释**： 共享权限级别。 **取值范围**： PROJECT
        :type share_right: str
        :param nexu_repo: **参数解释**： 是否nexus仓库。 **取值范围**： 不涉及。
        :type nexu_repo: bool
        :param url: **参数解释**： 仓库地址。 **取值范围**： 不涉及。
        :type url: str
        :param package_type: **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml
        :type package_type: str
        """
        
        

        self._username = None
        self._password = None
        self._status = None
        self._domain_id = None
        self._region = None
        self._created_time = None
        self._modified_time = None
        self._created_user_id = None
        self._created_user_name = None
        self._modified_user_id = None
        self._modified_user_name = None
        self._name = None
        self._disable = None
        self._format = None
        self._type = None
        self._policy = None
        self._tab_id = None
        self._repository_name = None
        self._display_name = None
        self._description = None
        self._snapshot = None
        self._release = None
        self._npm = None
        self._snapshot_status = None
        self._release_status = None
        self._project_id = None
        self._includes_pattern = None
        self._repository_ids = None
        self._uri = None
        self._deployment_policy = None
        self._repositories = None
        self._parent_repo_name = None
        self._user_name = None
        self._remote_url = None
        self._default_deploy_repository = None
        self._remote_type = None
        self._proxy = None
        self._allow_anonymous = None
        self._auto_clean_snapshot = None
        self._snapshot_alive_days = None
        self._max_unique_snapshots = None
        self._share_right = None
        self._nexu_repo = None
        self._url = None
        self._package_type = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
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
        if name is not None:
            self.name = name
        if disable is not None:
            self.disable = disable
        if format is not None:
            self.format = format
        if type is not None:
            self.type = type
        if policy is not None:
            self.policy = policy
        if tab_id is not None:
            self.tab_id = tab_id
        if repository_name is not None:
            self.repository_name = repository_name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if snapshot is not None:
            self.snapshot = snapshot
        if release is not None:
            self.release = release
        if npm is not None:
            self.npm = npm
        if snapshot_status is not None:
            self.snapshot_status = snapshot_status
        if release_status is not None:
            self.release_status = release_status
        if project_id is not None:
            self.project_id = project_id
        if includes_pattern is not None:
            self.includes_pattern = includes_pattern
        if repository_ids is not None:
            self.repository_ids = repository_ids
        if uri is not None:
            self.uri = uri
        if deployment_policy is not None:
            self.deployment_policy = deployment_policy
        if repositories is not None:
            self.repositories = repositories
        if parent_repo_name is not None:
            self.parent_repo_name = parent_repo_name
        if user_name is not None:
            self.user_name = user_name
        if remote_url is not None:
            self.remote_url = remote_url
        if default_deploy_repository is not None:
            self.default_deploy_repository = default_deploy_repository
        if remote_type is not None:
            self.remote_type = remote_type
        if proxy is not None:
            self.proxy = proxy
        if allow_anonymous is not None:
            self.allow_anonymous = allow_anonymous
        if auto_clean_snapshot is not None:
            self.auto_clean_snapshot = auto_clean_snapshot
        if snapshot_alive_days is not None:
            self.snapshot_alive_days = snapshot_alive_days
        if max_unique_snapshots is not None:
            self.max_unique_snapshots = max_unique_snapshots
        if share_right is not None:
            self.share_right = share_right
        if nexu_repo is not None:
            self.nexu_repo = nexu_repo
        if url is not None:
            self.url = url
        if package_type is not None:
            self.package_type = package_type

    @property
    def username(self):
        r"""Gets the username of this RepositoryBuildVO.

        **参数解释**： 账号。 **取值范围**： 不涉及。

        :return: The username of this RepositoryBuildVO.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this RepositoryBuildVO.

        **参数解释**： 账号。 **取值范围**： 不涉及。

        :param username: The username of this RepositoryBuildVO.
        :type username: str
        """
        self._username = username

    @property
    def password(self):
        r"""Gets the password of this RepositoryBuildVO.

        **参数解释**： 密码。 **取值范围**： 不涉及。

        :return: The password of this RepositoryBuildVO.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this RepositoryBuildVO.

        **参数解释**： 密码。 **取值范围**： 不涉及。

        :param password: The password of this RepositoryBuildVO.
        :type password: str
        """
        self._password = password

    @property
    def status(self):
        r"""Gets the status of this RepositoryBuildVO.

        **参数解释**： 仓库状态。 **取值范围**： - active：正常。 - delete：删除。 - disabled：无效。 - view：可浏览。 - trash：废弃。

        :return: The status of this RepositoryBuildVO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RepositoryBuildVO.

        **参数解释**： 仓库状态。 **取值范围**： - active：正常。 - delete：删除。 - disabled：无效。 - view：可浏览。 - trash：废弃。

        :param status: The status of this RepositoryBuildVO.
        :type status: str
        """
        self._status = status

    @property
    def domain_id(self):
        r"""Gets the domain_id of this RepositoryBuildVO.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :return: The domain_id of this RepositoryBuildVO.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this RepositoryBuildVO.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :param domain_id: The domain_id of this RepositoryBuildVO.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region(self):
        r"""Gets the region of this RepositoryBuildVO.

        **参数解释**： 区域。 **取值范围**： 不涉及。

        :return: The region of this RepositoryBuildVO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this RepositoryBuildVO.

        **参数解释**： 区域。 **取值范围**： 不涉及。

        :param region: The region of this RepositoryBuildVO.
        :type region: str
        """
        self._region = region

    @property
    def created_time(self):
        r"""Gets the created_time of this RepositoryBuildVO.

        **参数解释**： 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。

        :return: The created_time of this RepositoryBuildVO.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this RepositoryBuildVO.

        **参数解释**： 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。

        :param created_time: The created_time of this RepositoryBuildVO.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this RepositoryBuildVO.

        **参数解释**： 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。

        :return: The modified_time of this RepositoryBuildVO.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this RepositoryBuildVO.

        **参数解释**： 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。

        :param modified_time: The modified_time of this RepositoryBuildVO.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def created_user_id(self):
        r"""Gets the created_user_id of this RepositoryBuildVO.

        **参数解释**： 创建人ID。 **取值范围**： 不涉及。

        :return: The created_user_id of this RepositoryBuildVO.
        :rtype: str
        """
        return self._created_user_id

    @created_user_id.setter
    def created_user_id(self, created_user_id):
        r"""Sets the created_user_id of this RepositoryBuildVO.

        **参数解释**： 创建人ID。 **取值范围**： 不涉及。

        :param created_user_id: The created_user_id of this RepositoryBuildVO.
        :type created_user_id: str
        """
        self._created_user_id = created_user_id

    @property
    def created_user_name(self):
        r"""Gets the created_user_name of this RepositoryBuildVO.

        **参数解释**： 创建人名称。 **取值范围**： 不涉及。

        :return: The created_user_name of this RepositoryBuildVO.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        r"""Sets the created_user_name of this RepositoryBuildVO.

        **参数解释**： 创建人名称。 **取值范围**： 不涉及。

        :param created_user_name: The created_user_name of this RepositoryBuildVO.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def modified_user_id(self):
        r"""Gets the modified_user_id of this RepositoryBuildVO.

        **参数解释**： 修改人ID。 **取值范围**： 不涉及。

        :return: The modified_user_id of this RepositoryBuildVO.
        :rtype: str
        """
        return self._modified_user_id

    @modified_user_id.setter
    def modified_user_id(self, modified_user_id):
        r"""Sets the modified_user_id of this RepositoryBuildVO.

        **参数解释**： 修改人ID。 **取值范围**： 不涉及。

        :param modified_user_id: The modified_user_id of this RepositoryBuildVO.
        :type modified_user_id: str
        """
        self._modified_user_id = modified_user_id

    @property
    def modified_user_name(self):
        r"""Gets the modified_user_name of this RepositoryBuildVO.

        **参数解释**： 修改人名称。 **取值范围**： 不涉及。

        :return: The modified_user_name of this RepositoryBuildVO.
        :rtype: str
        """
        return self._modified_user_name

    @modified_user_name.setter
    def modified_user_name(self, modified_user_name):
        r"""Sets the modified_user_name of this RepositoryBuildVO.

        **参数解释**： 修改人名称。 **取值范围**： 不涉及。

        :param modified_user_name: The modified_user_name of this RepositoryBuildVO.
        :type modified_user_name: str
        """
        self._modified_user_name = modified_user_name

    @property
    def name(self):
        r"""Gets the name of this RepositoryBuildVO.

        **参数解释**： 仓库ID。 **取值范围**： 不涉及。

        :return: The name of this RepositoryBuildVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepositoryBuildVO.

        **参数解释**： 仓库ID。 **取值范围**： 不涉及。

        :param name: The name of this RepositoryBuildVO.
        :type name: str
        """
        self._name = name

    @property
    def disable(self):
        r"""Gets the disable of this RepositoryBuildVO.

        **参数解释**： 是否禁用。 **取值范围**： 不涉及。

        :return: The disable of this RepositoryBuildVO.
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        r"""Sets the disable of this RepositoryBuildVO.

        **参数解释**： 是否禁用。 **取值范围**： 不涉及。

        :param disable: The disable of this RepositoryBuildVO.
        :type disable: bool
        """
        self._disable = disable

    @property
    def format(self):
        r"""Gets the format of this RepositoryBuildVO.

        **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml

        :return: The format of this RepositoryBuildVO.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this RepositoryBuildVO.

        **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml

        :param format: The format of this RepositoryBuildVO.
        :type format: str
        """
        self._format = format

    @property
    def type(self):
        r"""Gets the type of this RepositoryBuildVO.

        **参数解释**： 仓库类型。 **取值范围**： - hosted：本地仓库。 - remote：代理仓库。 - virtual：虚拟仓库。

        :return: The type of this RepositoryBuildVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RepositoryBuildVO.

        **参数解释**： 仓库类型。 **取值范围**： - hosted：本地仓库。 - remote：代理仓库。 - virtual：虚拟仓库。

        :param type: The type of this RepositoryBuildVO.
        :type type: str
        """
        self._type = type

    @property
    def policy(self):
        r"""Gets the policy of this RepositoryBuildVO.

        **参数解释**： 仓库策略。 **取值范围**： - release：正式仓库。 - snapshot：快照仓库。

        :return: The policy of this RepositoryBuildVO.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this RepositoryBuildVO.

        **参数解释**： 仓库策略。 **取值范围**： - release：正式仓库。 - snapshot：快照仓库。

        :param policy: The policy of this RepositoryBuildVO.
        :type policy: str
        """
        self._policy = policy

    @property
    def tab_id(self):
        r"""Gets the tab_id of this RepositoryBuildVO.

        **参数解释**： 用于标记一对Maven仓库(release、snapshot)，相同的tab_id即为一对Maven仓库。 **取值范围**： 不涉及。

        :return: The tab_id of this RepositoryBuildVO.
        :rtype: str
        """
        return self._tab_id

    @tab_id.setter
    def tab_id(self, tab_id):
        r"""Sets the tab_id of this RepositoryBuildVO.

        **参数解释**： 用于标记一对Maven仓库(release、snapshot)，相同的tab_id即为一对Maven仓库。 **取值范围**： 不涉及。

        :param tab_id: The tab_id of this RepositoryBuildVO.
        :type tab_id: str
        """
        self._tab_id = tab_id

    @property
    def repository_name(self):
        r"""Gets the repository_name of this RepositoryBuildVO.

        **参数解释**： 仓库名称。 **取值范围**： 不涉及。

        :return: The repository_name of this RepositoryBuildVO.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this RepositoryBuildVO.

        **参数解释**： 仓库名称。 **取值范围**： 不涉及。

        :param repository_name: The repository_name of this RepositoryBuildVO.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def display_name(self):
        r"""Gets the display_name of this RepositoryBuildVO.

        **参数解释**： 展示的仓库名称。 **取值范围**： 不涉及。

        :return: The display_name of this RepositoryBuildVO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this RepositoryBuildVO.

        **参数解释**： 展示的仓库名称。 **取值范围**： 不涉及。

        :param display_name: The display_name of this RepositoryBuildVO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this RepositoryBuildVO.

        **参数解释**： 仓库描述。 **取值范围**： 不涉及。

        :return: The description of this RepositoryBuildVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RepositoryBuildVO.

        **参数解释**： 仓库描述。 **取值范围**： 不涉及。

        :param description: The description of this RepositoryBuildVO.
        :type description: str
        """
        self._description = description

    @property
    def snapshot(self):
        r"""Gets the snapshot of this RepositoryBuildVO.

        **参数解释**： snapshot仓库名称,release和snapshot至少二选一。 **取值范围**： 不涉及。

        :return: The snapshot of this RepositoryBuildVO.
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        r"""Sets the snapshot of this RepositoryBuildVO.

        **参数解释**： snapshot仓库名称,release和snapshot至少二选一。 **取值范围**： 不涉及。

        :param snapshot: The snapshot of this RepositoryBuildVO.
        :type snapshot: str
        """
        self._snapshot = snapshot

    @property
    def release(self):
        r"""Gets the release of this RepositoryBuildVO.

        **参数解释**： release仓库名称,release和snapshot至少二选一。 **取值范围**： 不涉及。

        :return: The release of this RepositoryBuildVO.
        :rtype: str
        """
        return self._release

    @release.setter
    def release(self, release):
        r"""Sets the release of this RepositoryBuildVO.

        **参数解释**： release仓库名称,release和snapshot至少二选一。 **取值范围**： 不涉及。

        :param release: The release of this RepositoryBuildVO.
        :type release: str
        """
        self._release = release

    @property
    def npm(self):
        r"""Gets the npm of this RepositoryBuildVO.

        **参数解释**： npm。 **取值范围**： 不涉及。

        :return: The npm of this RepositoryBuildVO.
        :rtype: str
        """
        return self._npm

    @npm.setter
    def npm(self, npm):
        r"""Sets the npm of this RepositoryBuildVO.

        **参数解释**： npm。 **取值范围**： 不涉及。

        :param npm: The npm of this RepositoryBuildVO.
        :type npm: str
        """
        self._npm = npm

    @property
    def snapshot_status(self):
        r"""Gets the snapshot_status of this RepositoryBuildVO.

        **参数解释**： 快照仓库状态。 **取值范围**： 不涉及。

        :return: The snapshot_status of this RepositoryBuildVO.
        :rtype: str
        """
        return self._snapshot_status

    @snapshot_status.setter
    def snapshot_status(self, snapshot_status):
        r"""Sets the snapshot_status of this RepositoryBuildVO.

        **参数解释**： 快照仓库状态。 **取值范围**： 不涉及。

        :param snapshot_status: The snapshot_status of this RepositoryBuildVO.
        :type snapshot_status: str
        """
        self._snapshot_status = snapshot_status

    @property
    def release_status(self):
        r"""Gets the release_status of this RepositoryBuildVO.

        **参数解释**： 正式仓库状态。 **取值范围**： 不涉及。

        :return: The release_status of this RepositoryBuildVO.
        :rtype: str
        """
        return self._release_status

    @release_status.setter
    def release_status(self, release_status):
        r"""Sets the release_status of this RepositoryBuildVO.

        **参数解释**： 正式仓库状态。 **取值范围**： 不涉及。

        :param release_status: The release_status of this RepositoryBuildVO.
        :type release_status: str
        """
        self._release_status = release_status

    @property
    def project_id(self):
        r"""Gets the project_id of this RepositoryBuildVO.

        **参数解释**： 项目id。 **取值范围**： 不涉及。

        :return: The project_id of this RepositoryBuildVO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RepositoryBuildVO.

        **参数解释**： 项目id。 **取值范围**： 不涉及。

        :param project_id: The project_id of this RepositoryBuildVO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def includes_pattern(self):
        r"""Gets the includes_pattern of this RepositoryBuildVO.

        **参数解释**： 路径包含规则。 **取值范围**： 不涉及。

        :return: The includes_pattern of this RepositoryBuildVO.
        :rtype: str
        """
        return self._includes_pattern

    @includes_pattern.setter
    def includes_pattern(self, includes_pattern):
        r"""Sets the includes_pattern of this RepositoryBuildVO.

        **参数解释**： 路径包含规则。 **取值范围**： 不涉及。

        :param includes_pattern: The includes_pattern of this RepositoryBuildVO.
        :type includes_pattern: str
        """
        self._includes_pattern = includes_pattern

    @property
    def repository_ids(self):
        r"""Gets the repository_ids of this RepositoryBuildVO.

        **参数解释**： 仓库ID列表。 **取值范围**： 不涉及。

        :return: The repository_ids of this RepositoryBuildVO.
        :rtype: list[str]
        """
        return self._repository_ids

    @repository_ids.setter
    def repository_ids(self, repository_ids):
        r"""Sets the repository_ids of this RepositoryBuildVO.

        **参数解释**： 仓库ID列表。 **取值范围**： 不涉及。

        :param repository_ids: The repository_ids of this RepositoryBuildVO.
        :type repository_ids: list[str]
        """
        self._repository_ids = repository_ids

    @property
    def uri(self):
        r"""Gets the uri of this RepositoryBuildVO.

        **参数解释**： uri。 **取值范围**： 不涉及。

        :return: The uri of this RepositoryBuildVO.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this RepositoryBuildVO.

        **参数解释**： uri。 **取值范围**： 不涉及。

        :param uri: The uri of this RepositoryBuildVO.
        :type uri: str
        """
        self._uri = uri

    @property
    def deployment_policy(self):
        r"""Gets the deployment_policy of this RepositoryBuildVO.

        **参数解释**： 覆盖策略。 **取值范围**： 不涉及。

        :return: The deployment_policy of this RepositoryBuildVO.
        :rtype: str
        """
        return self._deployment_policy

    @deployment_policy.setter
    def deployment_policy(self, deployment_policy):
        r"""Sets the deployment_policy of this RepositoryBuildVO.

        **参数解释**： 覆盖策略。 **取值范围**： 不涉及。

        :param deployment_policy: The deployment_policy of this RepositoryBuildVO.
        :type deployment_policy: str
        """
        self._deployment_policy = deployment_policy

    @property
    def repositories(self):
        r"""Gets the repositories of this RepositoryBuildVO.

        **参数解释**： 仓库列表。 **取值范围**： 不涉及。

        :return: The repositories of this RepositoryBuildVO.
        :rtype: list[str]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        r"""Sets the repositories of this RepositoryBuildVO.

        **参数解释**： 仓库列表。 **取值范围**： 不涉及。

        :param repositories: The repositories of this RepositoryBuildVO.
        :type repositories: list[str]
        """
        self._repositories = repositories

    @property
    def parent_repo_name(self):
        r"""Gets the parent_repo_name of this RepositoryBuildVO.

        **参数解释**： 父仓库名。 **取值范围**： 不涉及。

        :return: The parent_repo_name of this RepositoryBuildVO.
        :rtype: str
        """
        return self._parent_repo_name

    @parent_repo_name.setter
    def parent_repo_name(self, parent_repo_name):
        r"""Sets the parent_repo_name of this RepositoryBuildVO.

        **参数解释**： 父仓库名。 **取值范围**： 不涉及。

        :param parent_repo_name: The parent_repo_name of this RepositoryBuildVO.
        :type parent_repo_name: str
        """
        self._parent_repo_name = parent_repo_name

    @property
    def user_name(self):
        r"""Gets the user_name of this RepositoryBuildVO.

        **参数解释**: 用户名。 **取值范围**: 不涉及。

        :return: The user_name of this RepositoryBuildVO.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this RepositoryBuildVO.

        **参数解释**: 用户名。 **取值范围**: 不涉及。

        :param user_name: The user_name of this RepositoryBuildVO.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def remote_url(self):
        r"""Gets the remote_url of this RepositoryBuildVO.

        **参数解释**： 代理仓地址。 **取值范围**： 不涉及。

        :return: The remote_url of this RepositoryBuildVO.
        :rtype: str
        """
        return self._remote_url

    @remote_url.setter
    def remote_url(self, remote_url):
        r"""Sets the remote_url of this RepositoryBuildVO.

        **参数解释**： 代理仓地址。 **取值范围**： 不涉及。

        :param remote_url: The remote_url of this RepositoryBuildVO.
        :type remote_url: str
        """
        self._remote_url = remote_url

    @property
    def default_deploy_repository(self):
        r"""Gets the default_deploy_repository of this RepositoryBuildVO.

        **参数解释**： 默认仓库。 **取值范围**： 不涉及。

        :return: The default_deploy_repository of this RepositoryBuildVO.
        :rtype: str
        """
        return self._default_deploy_repository

    @default_deploy_repository.setter
    def default_deploy_repository(self, default_deploy_repository):
        r"""Sets the default_deploy_repository of this RepositoryBuildVO.

        **参数解释**： 默认仓库。 **取值范围**： 不涉及。

        :param default_deploy_repository: The default_deploy_repository of this RepositoryBuildVO.
        :type default_deploy_repository: str
        """
        self._default_deploy_repository = default_deploy_repository

    @property
    def remote_type(self):
        r"""Gets the remote_type of this RepositoryBuildVO.

        **参数解释**： 代理仓类型。 **取值范围**： - public：公共代理仓； - customize：用户自定义代理仓。

        :return: The remote_type of this RepositoryBuildVO.
        :rtype: str
        """
        return self._remote_type

    @remote_type.setter
    def remote_type(self, remote_type):
        r"""Sets the remote_type of this RepositoryBuildVO.

        **参数解释**： 代理仓类型。 **取值范围**： - public：公共代理仓； - customize：用户自定义代理仓。

        :param remote_type: The remote_type of this RepositoryBuildVO.
        :type remote_type: str
        """
        self._remote_type = remote_type

    @property
    def proxy(self):
        r"""Gets the proxy of this RepositoryBuildVO.

        **参数解释**： 代理。 **取值范围**： 不涉及。

        :return: The proxy of this RepositoryBuildVO.
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        r"""Sets the proxy of this RepositoryBuildVO.

        **参数解释**： 代理。 **取值范围**： 不涉及。

        :param proxy: The proxy of this RepositoryBuildVO.
        :type proxy: str
        """
        self._proxy = proxy

    @property
    def allow_anonymous(self):
        r"""Gets the allow_anonymous of this RepositoryBuildVO.

        **参数解释**： 是否允许匿名下载。 **取值范围**： 不涉及。

        :return: The allow_anonymous of this RepositoryBuildVO.
        :rtype: bool
        """
        return self._allow_anonymous

    @allow_anonymous.setter
    def allow_anonymous(self, allow_anonymous):
        r"""Sets the allow_anonymous of this RepositoryBuildVO.

        **参数解释**： 是否允许匿名下载。 **取值范围**： 不涉及。

        :param allow_anonymous: The allow_anonymous of this RepositoryBuildVO.
        :type allow_anonymous: bool
        """
        self._allow_anonymous = allow_anonymous

    @property
    def auto_clean_snapshot(self):
        r"""Gets the auto_clean_snapshot of this RepositoryBuildVO.

        **参数解释**： 是否自动清理快照版本。 **取值范围**： 不涉及。

        :return: The auto_clean_snapshot of this RepositoryBuildVO.
        :rtype: bool
        """
        return self._auto_clean_snapshot

    @auto_clean_snapshot.setter
    def auto_clean_snapshot(self, auto_clean_snapshot):
        r"""Sets the auto_clean_snapshot of this RepositoryBuildVO.

        **参数解释**： 是否自动清理快照版本。 **取值范围**： 不涉及。

        :param auto_clean_snapshot: The auto_clean_snapshot of this RepositoryBuildVO.
        :type auto_clean_snapshot: bool
        """
        self._auto_clean_snapshot = auto_clean_snapshot

    @property
    def snapshot_alive_days(self):
        r"""Gets the snapshot_alive_days of this RepositoryBuildVO.

        **参数解释**： 快照版本有效期，单位：天。 **取值范围**： 不涉及。

        :return: The snapshot_alive_days of this RepositoryBuildVO.
        :rtype: str
        """
        return self._snapshot_alive_days

    @snapshot_alive_days.setter
    def snapshot_alive_days(self, snapshot_alive_days):
        r"""Sets the snapshot_alive_days of this RepositoryBuildVO.

        **参数解释**： 快照版本有效期，单位：天。 **取值范围**： 不涉及。

        :param snapshot_alive_days: The snapshot_alive_days of this RepositoryBuildVO.
        :type snapshot_alive_days: str
        """
        self._snapshot_alive_days = snapshot_alive_days

    @property
    def max_unique_snapshots(self):
        r"""Gets the max_unique_snapshots of this RepositoryBuildVO.

        **参数解释**： 最大快照数。 **取值范围**： 不涉及。

        :return: The max_unique_snapshots of this RepositoryBuildVO.
        :rtype: str
        """
        return self._max_unique_snapshots

    @max_unique_snapshots.setter
    def max_unique_snapshots(self, max_unique_snapshots):
        r"""Sets the max_unique_snapshots of this RepositoryBuildVO.

        **参数解释**： 最大快照数。 **取值范围**： 不涉及。

        :param max_unique_snapshots: The max_unique_snapshots of this RepositoryBuildVO.
        :type max_unique_snapshots: str
        """
        self._max_unique_snapshots = max_unique_snapshots

    @property
    def share_right(self):
        r"""Gets the share_right of this RepositoryBuildVO.

        **参数解释**： 共享权限级别。 **取值范围**： PROJECT

        :return: The share_right of this RepositoryBuildVO.
        :rtype: str
        """
        return self._share_right

    @share_right.setter
    def share_right(self, share_right):
        r"""Sets the share_right of this RepositoryBuildVO.

        **参数解释**： 共享权限级别。 **取值范围**： PROJECT

        :param share_right: The share_right of this RepositoryBuildVO.
        :type share_right: str
        """
        self._share_right = share_right

    @property
    def nexu_repo(self):
        r"""Gets the nexu_repo of this RepositoryBuildVO.

        **参数解释**： 是否nexus仓库。 **取值范围**： 不涉及。

        :return: The nexu_repo of this RepositoryBuildVO.
        :rtype: bool
        """
        return self._nexu_repo

    @nexu_repo.setter
    def nexu_repo(self, nexu_repo):
        r"""Sets the nexu_repo of this RepositoryBuildVO.

        **参数解释**： 是否nexus仓库。 **取值范围**： 不涉及。

        :param nexu_repo: The nexu_repo of this RepositoryBuildVO.
        :type nexu_repo: bool
        """
        self._nexu_repo = nexu_repo

    @property
    def url(self):
        r"""Gets the url of this RepositoryBuildVO.

        **参数解释**： 仓库地址。 **取值范围**： 不涉及。

        :return: The url of this RepositoryBuildVO.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this RepositoryBuildVO.

        **参数解释**： 仓库地址。 **取值范围**： 不涉及。

        :param url: The url of this RepositoryBuildVO.
        :type url: str
        """
        self._url = url

    @property
    def package_type(self):
        r"""Gets the package_type of this RepositoryBuildVO.

        **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml

        :return: The package_type of this RepositoryBuildVO.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this RepositoryBuildVO.

        **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml

        :param package_type: The package_type of this RepositoryBuildVO.
        :type package_type: str
        """
        self._package_type = package_type

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
        if not isinstance(other, RepositoryBuildVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
