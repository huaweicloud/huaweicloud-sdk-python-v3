# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryBasicDO:

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
        'repo_type': 'str',
        'policy': 'str',
        'tab_id': 'str',
        'repository_name': 'str',
        'display_name': 'str',
        'description': 'str',
        'project_id': 'str',
        'includes_pattern': 'str',
        'deployment_policy': 'str',
        'share_right': 'str',
        'url': 'str',
        'package_type': 'str',
        'storage_summary_info': 'DownloadFolderInfo'
    }

    attribute_map = {
        'id': 'id',
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
        'repo_type': 'repoType',
        'policy': 'policy',
        'tab_id': 'tabId',
        'repository_name': 'repositoryName',
        'display_name': 'displayName',
        'description': 'description',
        'project_id': 'projectId',
        'includes_pattern': 'includesPattern',
        'deployment_policy': 'deploymentPolicy',
        'share_right': 'shareRight',
        'url': 'url',
        'package_type': 'packageType',
        'storage_summary_info': 'storageSummaryInfo'
    }

    def __init__(self, id=None, status=None, domain_id=None, region=None, created_time=None, modified_time=None, created_user_id=None, created_user_name=None, modified_user_id=None, modified_user_name=None, name=None, disable=None, format=None, repo_type=None, policy=None, tab_id=None, repository_name=None, display_name=None, description=None, project_id=None, includes_pattern=None, deployment_policy=None, share_right=None, url=None, package_type=None, storage_summary_info=None):
        r"""RepositoryBasicDO

        The model defined in huaweicloud sdk

        :param id: **参数解释**： ID。 **取值范围**： 不涉及。
        :type id: str
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
        :param repo_type: **参数解释**： 仓库类型。 **取值范围**： - hosted：本地仓库。 - remote：代理仓库。 - virtual：虚拟仓库。
        :type repo_type: str
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
        :param project_id: **参数解释**： 项目id。 **取值范围**： 不涉及。
        :type project_id: str
        :param includes_pattern: **参数解释**： 路径包含规则。 **取值范围**： 不涉及。
        :type includes_pattern: str
        :param deployment_policy: **参数解释**： 覆盖策略。 **取值范围**： 不涉及。
        :type deployment_policy: str
        :param share_right: **参数解释**： 共享权限级别。 **取值范围**： PROJECT
        :type share_right: str
        :param url: **参数解释**： 仓库地址。 **取值范围**： 不涉及。
        :type url: str
        :param package_type: **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml
        :type package_type: str
        :param storage_summary_info: 
        :type storage_summary_info: :class:`huaweicloudsdkcodeartsartifact.v2.DownloadFolderInfo`
        """
        
        

        self._id = None
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
        self._repo_type = None
        self._policy = None
        self._tab_id = None
        self._repository_name = None
        self._display_name = None
        self._description = None
        self._project_id = None
        self._includes_pattern = None
        self._deployment_policy = None
        self._share_right = None
        self._url = None
        self._package_type = None
        self._storage_summary_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        if repo_type is not None:
            self.repo_type = repo_type
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
        if project_id is not None:
            self.project_id = project_id
        if includes_pattern is not None:
            self.includes_pattern = includes_pattern
        if deployment_policy is not None:
            self.deployment_policy = deployment_policy
        if share_right is not None:
            self.share_right = share_right
        if url is not None:
            self.url = url
        if package_type is not None:
            self.package_type = package_type
        if storage_summary_info is not None:
            self.storage_summary_info = storage_summary_info

    @property
    def id(self):
        r"""Gets the id of this RepositoryBasicDO.

        **参数解释**： ID。 **取值范围**： 不涉及。

        :return: The id of this RepositoryBasicDO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RepositoryBasicDO.

        **参数解释**： ID。 **取值范围**： 不涉及。

        :param id: The id of this RepositoryBasicDO.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this RepositoryBasicDO.

        **参数解释**： 仓库状态。 **取值范围**： - active：正常。 - delete：删除。 - disabled：无效。 - view：可浏览。 - trash：废弃。

        :return: The status of this RepositoryBasicDO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RepositoryBasicDO.

        **参数解释**： 仓库状态。 **取值范围**： - active：正常。 - delete：删除。 - disabled：无效。 - view：可浏览。 - trash：废弃。

        :param status: The status of this RepositoryBasicDO.
        :type status: str
        """
        self._status = status

    @property
    def domain_id(self):
        r"""Gets the domain_id of this RepositoryBasicDO.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :return: The domain_id of this RepositoryBasicDO.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this RepositoryBasicDO.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :param domain_id: The domain_id of this RepositoryBasicDO.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region(self):
        r"""Gets the region of this RepositoryBasicDO.

        **参数解释**： 区域。 **取值范围**： 不涉及。

        :return: The region of this RepositoryBasicDO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this RepositoryBasicDO.

        **参数解释**： 区域。 **取值范围**： 不涉及。

        :param region: The region of this RepositoryBasicDO.
        :type region: str
        """
        self._region = region

    @property
    def created_time(self):
        r"""Gets the created_time of this RepositoryBasicDO.

        **参数解释**： 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。

        :return: The created_time of this RepositoryBasicDO.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this RepositoryBasicDO.

        **参数解释**： 创建时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。

        :param created_time: The created_time of this RepositoryBasicDO.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this RepositoryBasicDO.

        **参数解释**： 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。

        :return: The modified_time of this RepositoryBasicDO.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this RepositoryBasicDO.

        **参数解释**： 修改时间，时间格式：yyyy-MM-dd HH:mm:ss。 **取值范围**： 不涉及。

        :param modified_time: The modified_time of this RepositoryBasicDO.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def created_user_id(self):
        r"""Gets the created_user_id of this RepositoryBasicDO.

        **参数解释**： 创建人ID。 **取值范围**： 不涉及。

        :return: The created_user_id of this RepositoryBasicDO.
        :rtype: str
        """
        return self._created_user_id

    @created_user_id.setter
    def created_user_id(self, created_user_id):
        r"""Sets the created_user_id of this RepositoryBasicDO.

        **参数解释**： 创建人ID。 **取值范围**： 不涉及。

        :param created_user_id: The created_user_id of this RepositoryBasicDO.
        :type created_user_id: str
        """
        self._created_user_id = created_user_id

    @property
    def created_user_name(self):
        r"""Gets the created_user_name of this RepositoryBasicDO.

        **参数解释**： 创建人名称。 **取值范围**： 不涉及。

        :return: The created_user_name of this RepositoryBasicDO.
        :rtype: str
        """
        return self._created_user_name

    @created_user_name.setter
    def created_user_name(self, created_user_name):
        r"""Sets the created_user_name of this RepositoryBasicDO.

        **参数解释**： 创建人名称。 **取值范围**： 不涉及。

        :param created_user_name: The created_user_name of this RepositoryBasicDO.
        :type created_user_name: str
        """
        self._created_user_name = created_user_name

    @property
    def modified_user_id(self):
        r"""Gets the modified_user_id of this RepositoryBasicDO.

        **参数解释**： 修改人ID。 **取值范围**： 不涉及。

        :return: The modified_user_id of this RepositoryBasicDO.
        :rtype: str
        """
        return self._modified_user_id

    @modified_user_id.setter
    def modified_user_id(self, modified_user_id):
        r"""Sets the modified_user_id of this RepositoryBasicDO.

        **参数解释**： 修改人ID。 **取值范围**： 不涉及。

        :param modified_user_id: The modified_user_id of this RepositoryBasicDO.
        :type modified_user_id: str
        """
        self._modified_user_id = modified_user_id

    @property
    def modified_user_name(self):
        r"""Gets the modified_user_name of this RepositoryBasicDO.

        **参数解释**： 修改人名称。 **取值范围**： 不涉及。

        :return: The modified_user_name of this RepositoryBasicDO.
        :rtype: str
        """
        return self._modified_user_name

    @modified_user_name.setter
    def modified_user_name(self, modified_user_name):
        r"""Sets the modified_user_name of this RepositoryBasicDO.

        **参数解释**： 修改人名称。 **取值范围**： 不涉及。

        :param modified_user_name: The modified_user_name of this RepositoryBasicDO.
        :type modified_user_name: str
        """
        self._modified_user_name = modified_user_name

    @property
    def name(self):
        r"""Gets the name of this RepositoryBasicDO.

        **参数解释**： 仓库ID。 **取值范围**： 不涉及。

        :return: The name of this RepositoryBasicDO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RepositoryBasicDO.

        **参数解释**： 仓库ID。 **取值范围**： 不涉及。

        :param name: The name of this RepositoryBasicDO.
        :type name: str
        """
        self._name = name

    @property
    def disable(self):
        r"""Gets the disable of this RepositoryBasicDO.

        **参数解释**： 是否禁用。 **取值范围**： 不涉及。

        :return: The disable of this RepositoryBasicDO.
        :rtype: bool
        """
        return self._disable

    @disable.setter
    def disable(self, disable):
        r"""Sets the disable of this RepositoryBasicDO.

        **参数解释**： 是否禁用。 **取值范围**： 不涉及。

        :param disable: The disable of this RepositoryBasicDO.
        :type disable: bool
        """
        self._disable = disable

    @property
    def format(self):
        r"""Gets the format of this RepositoryBasicDO.

        **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml

        :return: The format of this RepositoryBasicDO.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this RepositoryBasicDO.

        **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml

        :param format: The format of this RepositoryBasicDO.
        :type format: str
        """
        self._format = format

    @property
    def repo_type(self):
        r"""Gets the repo_type of this RepositoryBasicDO.

        **参数解释**： 仓库类型。 **取值范围**： - hosted：本地仓库。 - remote：代理仓库。 - virtual：虚拟仓库。

        :return: The repo_type of this RepositoryBasicDO.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        r"""Sets the repo_type of this RepositoryBasicDO.

        **参数解释**： 仓库类型。 **取值范围**： - hosted：本地仓库。 - remote：代理仓库。 - virtual：虚拟仓库。

        :param repo_type: The repo_type of this RepositoryBasicDO.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def policy(self):
        r"""Gets the policy of this RepositoryBasicDO.

        **参数解释**： 仓库策略。 **取值范围**： - release：正式仓库。 - snapshot：快照仓库。

        :return: The policy of this RepositoryBasicDO.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this RepositoryBasicDO.

        **参数解释**： 仓库策略。 **取值范围**： - release：正式仓库。 - snapshot：快照仓库。

        :param policy: The policy of this RepositoryBasicDO.
        :type policy: str
        """
        self._policy = policy

    @property
    def tab_id(self):
        r"""Gets the tab_id of this RepositoryBasicDO.

        **参数解释**： 用于标记一对Maven仓库(release、snapshot)，相同的tab_id即为一对Maven仓库。 **取值范围**： 不涉及。

        :return: The tab_id of this RepositoryBasicDO.
        :rtype: str
        """
        return self._tab_id

    @tab_id.setter
    def tab_id(self, tab_id):
        r"""Sets the tab_id of this RepositoryBasicDO.

        **参数解释**： 用于标记一对Maven仓库(release、snapshot)，相同的tab_id即为一对Maven仓库。 **取值范围**： 不涉及。

        :param tab_id: The tab_id of this RepositoryBasicDO.
        :type tab_id: str
        """
        self._tab_id = tab_id

    @property
    def repository_name(self):
        r"""Gets the repository_name of this RepositoryBasicDO.

        **参数解释**： 仓库名称。 **取值范围**： 不涉及。

        :return: The repository_name of this RepositoryBasicDO.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        r"""Sets the repository_name of this RepositoryBasicDO.

        **参数解释**： 仓库名称。 **取值范围**： 不涉及。

        :param repository_name: The repository_name of this RepositoryBasicDO.
        :type repository_name: str
        """
        self._repository_name = repository_name

    @property
    def display_name(self):
        r"""Gets the display_name of this RepositoryBasicDO.

        **参数解释**： 展示的仓库名称。 **取值范围**： 不涉及。

        :return: The display_name of this RepositoryBasicDO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this RepositoryBasicDO.

        **参数解释**： 展示的仓库名称。 **取值范围**： 不涉及。

        :param display_name: The display_name of this RepositoryBasicDO.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this RepositoryBasicDO.

        **参数解释**： 仓库描述。 **取值范围**： 不涉及。

        :return: The description of this RepositoryBasicDO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RepositoryBasicDO.

        **参数解释**： 仓库描述。 **取值范围**： 不涉及。

        :param description: The description of this RepositoryBasicDO.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this RepositoryBasicDO.

        **参数解释**： 项目id。 **取值范围**： 不涉及。

        :return: The project_id of this RepositoryBasicDO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RepositoryBasicDO.

        **参数解释**： 项目id。 **取值范围**： 不涉及。

        :param project_id: The project_id of this RepositoryBasicDO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def includes_pattern(self):
        r"""Gets the includes_pattern of this RepositoryBasicDO.

        **参数解释**： 路径包含规则。 **取值范围**： 不涉及。

        :return: The includes_pattern of this RepositoryBasicDO.
        :rtype: str
        """
        return self._includes_pattern

    @includes_pattern.setter
    def includes_pattern(self, includes_pattern):
        r"""Sets the includes_pattern of this RepositoryBasicDO.

        **参数解释**： 路径包含规则。 **取值范围**： 不涉及。

        :param includes_pattern: The includes_pattern of this RepositoryBasicDO.
        :type includes_pattern: str
        """
        self._includes_pattern = includes_pattern

    @property
    def deployment_policy(self):
        r"""Gets the deployment_policy of this RepositoryBasicDO.

        **参数解释**： 覆盖策略。 **取值范围**： 不涉及。

        :return: The deployment_policy of this RepositoryBasicDO.
        :rtype: str
        """
        return self._deployment_policy

    @deployment_policy.setter
    def deployment_policy(self, deployment_policy):
        r"""Sets the deployment_policy of this RepositoryBasicDO.

        **参数解释**： 覆盖策略。 **取值范围**： 不涉及。

        :param deployment_policy: The deployment_policy of this RepositoryBasicDO.
        :type deployment_policy: str
        """
        self._deployment_policy = deployment_policy

    @property
    def share_right(self):
        r"""Gets the share_right of this RepositoryBasicDO.

        **参数解释**： 共享权限级别。 **取值范围**： PROJECT

        :return: The share_right of this RepositoryBasicDO.
        :rtype: str
        """
        return self._share_right

    @share_right.setter
    def share_right(self, share_right):
        r"""Sets the share_right of this RepositoryBasicDO.

        **参数解释**： 共享权限级别。 **取值范围**： PROJECT

        :param share_right: The share_right of this RepositoryBasicDO.
        :type share_right: str
        """
        self._share_right = share_right

    @property
    def url(self):
        r"""Gets the url of this RepositoryBasicDO.

        **参数解释**： 仓库地址。 **取值范围**： 不涉及。

        :return: The url of this RepositoryBasicDO.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this RepositoryBasicDO.

        **参数解释**： 仓库地址。 **取值范围**： 不涉及。

        :param url: The url of this RepositoryBasicDO.
        :type url: str
        """
        self._url = url

    @property
    def package_type(self):
        r"""Gets the package_type of this RepositoryBasicDO.

        **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml

        :return: The package_type of this RepositoryBasicDO.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this RepositoryBasicDO.

        **参数解释**： 制品类型。 **取值范围**： - maven - maven2 - npm - go - pypi - rpm - composer - debian - conan - nuget - docker2 - cocoapods - ohpm - generic - helm - conda - huggingfaceml

        :param package_type: The package_type of this RepositoryBasicDO.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def storage_summary_info(self):
        r"""Gets the storage_summary_info of this RepositoryBasicDO.

        :return: The storage_summary_info of this RepositoryBasicDO.
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.DownloadFolderInfo`
        """
        return self._storage_summary_info

    @storage_summary_info.setter
    def storage_summary_info(self, storage_summary_info):
        r"""Sets the storage_summary_info of this RepositoryBasicDO.

        :param storage_summary_info: The storage_summary_info of this RepositoryBasicDO.
        :type storage_summary_info: :class:`huaweicloudsdkcodeartsartifact.v2.DownloadFolderInfo`
        """
        self._storage_summary_info = storage_summary_info

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
        if not isinstance(other, RepositoryBasicDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
