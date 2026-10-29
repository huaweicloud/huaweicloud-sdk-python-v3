# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigTemplateBasicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'branch': 'str',
        'create_time': 'str',
        'creator': 'str',
        'exclude': 'str',
        'id': 'str',
        'include_paths': 'str',
        'last_reviser': 'str',
        'last_update_time': 'str',
        'name': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'region': 'str',
        'repo_type': 'str',
        'repo_url': 'str',
        'resource_pool_id': 'str',
        'resource_pool_name': 'str',
        'resource_pool_type': 'str',
        'review_data': 'list[ReviewDataInfoResponse]',
        'review_data_json': 'str',
        'rule_sets': 'list[ConfigTemplateRuleSetInfo]'
    }

    attribute_map = {
        'arch': 'arch',
        'branch': 'branch',
        'create_time': 'createTime',
        'creator': 'creator',
        'exclude': 'exclude',
        'id': 'id',
        'include_paths': 'includePaths',
        'last_reviser': 'lastReviser',
        'last_update_time': 'lastUpdateTime',
        'name': 'name',
        'project_id': 'projectId',
        'project_name': 'projectName',
        'region': 'region',
        'repo_type': 'repoType',
        'repo_url': 'repoUrl',
        'resource_pool_id': 'resourcePoolId',
        'resource_pool_name': 'resourcePoolName',
        'resource_pool_type': 'resource_pool_type',
        'review_data': 'reviewData',
        'review_data_json': 'reviewDataJson',
        'rule_sets': 'ruleSets'
    }

    def __init__(self, arch=None, branch=None, create_time=None, creator=None, exclude=None, id=None, include_paths=None, last_reviser=None, last_update_time=None, name=None, project_id=None, project_name=None, region=None, repo_type=None, repo_url=None, resource_pool_id=None, resource_pool_name=None, resource_pool_type=None, review_data=None, review_data_json=None, rule_sets=None):
        r"""ConfigTemplateBasicInfo

        The model defined in huaweicloud sdk

        :param arch: **参数解释：** 执行机类型。 **取值范围：** X86/ARM。
        :type arch: str
        :param branch: **参数解释：** 分支名。 **取值范围：** 不涉及。
        :type branch: str
        :param create_time: **参数解释：** 配置模板创建时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\&quot;2025-11-28T06:55:41Z\&quot;。 **取值范围：** 不涉及。
        :type create_time: str
        :param creator: **参数解释：** 配置模板创建者。 **取值范围：** 不涉及。
        :type creator: str
        :param exclude: **参数解释：** 任务配置的排除目录信息。 **取值范围:** 不涉及。
        :type exclude: str
        :param id: **参数解释：** 配置模板ID，修改配置信息需要用到配置模板ID，每个代码检查任务及其下的分支任务都有相同的且唯一的配置模板ID。 **取值范围:** 不涉及。
        :type id: str
        :param include_paths: **参数解释：** 检查目录。不配置检查目录时，检查代码仓中所有目录下的代码文件；配置检查目录时，只检查配置目录中的文件。 **取值范围：** 不涉及。
        :type include_paths: str
        :param last_reviser: **参数解释：** 最后修改人的用户名。 **取值范围：** 不涉及。
        :type last_reviser: str
        :param last_update_time: **参数解释：** 配置模板上一次修改时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\&quot;2025-11-28T06:55:41Z\&quot;。 **取值范围：** 不涉及。
        :type last_update_time: str
        :param name: **参数解释：** 配置模板的名称。 **取值范围：** 不涉及。
        :type name: str
        :param project_id: **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **取值范围：** 长度为[1~32]个字符。
        :type project_id: str
        :param project_name: **参数解释：** 项目名。 **取值范围：** 不涉及。
        :type project_name: str
        :param region: **参数解释：** 华为云地域。 **取值范围：** 不涉及。
        :type region: str
        :param repo_type: **参数解释：** 代码仓类型。 **取值范围：** - DevCloud：CodeArtsRepo仓。 - Gitee：Gitee仓。 - GitHub：GitHub仓。 - GitPub：通用Git仓。 - gitcode：GitCode仓。 - gitlab：GitLab仓。 - self_gitlab：自建GitLab仓。 - tfs_git：TFS仓。 - bitbucket：Bitbucket仓。
        :type repo_type: str
        :param repo_url: **参数解释：** 代码仓地址。 **取值范围：** 不涉及。
        :type repo_url: str
        :param resource_pool_id: **参数解释：** 启用的资源池ID，使用内置执行机的情况下为\&quot;\&quot;。 **取值范围：** 不涉及。
        :type resource_pool_id: str
        :param resource_pool_name: **参数解释：** 启用的资源池名称，使用内置执行机的情况下为空。 **取值范围：** 不涉及。
        :type resource_pool_name: str
        :param resource_pool_type: **参数解释：** 启用的资源池类型。 **取值范围：** - default：使用内置资源池。 - exclusive：使用专属资源池。 - self-hosted：使用自定义资源池。
        :type resource_pool_type: str
        :param review_data: **参数解释：** 任务门禁配置列表。
        :type review_data: list[:class:`huaweicloudsdkcodeartscheck.v2.ReviewDataInfoResponse`]
        :param review_data_json: **参数解释：** 任务门禁配置列表的json字符串。 **取值范围：** 不涉及。
        :type review_data_json: str
        :param rule_sets: **参数解释：** 规则集配置列表。
        :type rule_sets: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        """
        
        

        self._arch = None
        self._branch = None
        self._create_time = None
        self._creator = None
        self._exclude = None
        self._id = None
        self._include_paths = None
        self._last_reviser = None
        self._last_update_time = None
        self._name = None
        self._project_id = None
        self._project_name = None
        self._region = None
        self._repo_type = None
        self._repo_url = None
        self._resource_pool_id = None
        self._resource_pool_name = None
        self._resource_pool_type = None
        self._review_data = None
        self._review_data_json = None
        self._rule_sets = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        if branch is not None:
            self.branch = branch
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if exclude is not None:
            self.exclude = exclude
        if id is not None:
            self.id = id
        if include_paths is not None:
            self.include_paths = include_paths
        if last_reviser is not None:
            self.last_reviser = last_reviser
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if region is not None:
            self.region = region
        if repo_type is not None:
            self.repo_type = repo_type
        if repo_url is not None:
            self.repo_url = repo_url
        if resource_pool_id is not None:
            self.resource_pool_id = resource_pool_id
        if resource_pool_name is not None:
            self.resource_pool_name = resource_pool_name
        if resource_pool_type is not None:
            self.resource_pool_type = resource_pool_type
        if review_data is not None:
            self.review_data = review_data
        if review_data_json is not None:
            self.review_data_json = review_data_json
        if rule_sets is not None:
            self.rule_sets = rule_sets

    @property
    def arch(self):
        r"""Gets the arch of this ConfigTemplateBasicInfo.

        **参数解释：** 执行机类型。 **取值范围：** X86/ARM。

        :return: The arch of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ConfigTemplateBasicInfo.

        **参数解释：** 执行机类型。 **取值范围：** X86/ARM。

        :param arch: The arch of this ConfigTemplateBasicInfo.
        :type arch: str
        """
        self._arch = arch

    @property
    def branch(self):
        r"""Gets the branch of this ConfigTemplateBasicInfo.

        **参数解释：** 分支名。 **取值范围：** 不涉及。

        :return: The branch of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this ConfigTemplateBasicInfo.

        **参数解释：** 分支名。 **取值范围：** 不涉及。

        :param branch: The branch of this ConfigTemplateBasicInfo.
        :type branch: str
        """
        self._branch = branch

    @property
    def create_time(self):
        r"""Gets the create_time of this ConfigTemplateBasicInfo.

        **参数解释：** 配置模板创建时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :return: The create_time of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ConfigTemplateBasicInfo.

        **参数解释：** 配置模板创建时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :param create_time: The create_time of this ConfigTemplateBasicInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this ConfigTemplateBasicInfo.

        **参数解释：** 配置模板创建者。 **取值范围：** 不涉及。

        :return: The creator of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ConfigTemplateBasicInfo.

        **参数解释：** 配置模板创建者。 **取值范围：** 不涉及。

        :param creator: The creator of this ConfigTemplateBasicInfo.
        :type creator: str
        """
        self._creator = creator

    @property
    def exclude(self):
        r"""Gets the exclude of this ConfigTemplateBasicInfo.

        **参数解释：** 任务配置的排除目录信息。 **取值范围:** 不涉及。

        :return: The exclude of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        r"""Sets the exclude of this ConfigTemplateBasicInfo.

        **参数解释：** 任务配置的排除目录信息。 **取值范围:** 不涉及。

        :param exclude: The exclude of this ConfigTemplateBasicInfo.
        :type exclude: str
        """
        self._exclude = exclude

    @property
    def id(self):
        r"""Gets the id of this ConfigTemplateBasicInfo.

        **参数解释：** 配置模板ID，修改配置信息需要用到配置模板ID，每个代码检查任务及其下的分支任务都有相同的且唯一的配置模板ID。 **取值范围:** 不涉及。

        :return: The id of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConfigTemplateBasicInfo.

        **参数解释：** 配置模板ID，修改配置信息需要用到配置模板ID，每个代码检查任务及其下的分支任务都有相同的且唯一的配置模板ID。 **取值范围:** 不涉及。

        :param id: The id of this ConfigTemplateBasicInfo.
        :type id: str
        """
        self._id = id

    @property
    def include_paths(self):
        r"""Gets the include_paths of this ConfigTemplateBasicInfo.

        **参数解释：** 检查目录。不配置检查目录时，检查代码仓中所有目录下的代码文件；配置检查目录时，只检查配置目录中的文件。 **取值范围：** 不涉及。

        :return: The include_paths of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._include_paths

    @include_paths.setter
    def include_paths(self, include_paths):
        r"""Sets the include_paths of this ConfigTemplateBasicInfo.

        **参数解释：** 检查目录。不配置检查目录时，检查代码仓中所有目录下的代码文件；配置检查目录时，只检查配置目录中的文件。 **取值范围：** 不涉及。

        :param include_paths: The include_paths of this ConfigTemplateBasicInfo.
        :type include_paths: str
        """
        self._include_paths = include_paths

    @property
    def last_reviser(self):
        r"""Gets the last_reviser of this ConfigTemplateBasicInfo.

        **参数解释：** 最后修改人的用户名。 **取值范围：** 不涉及。

        :return: The last_reviser of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._last_reviser

    @last_reviser.setter
    def last_reviser(self, last_reviser):
        r"""Sets the last_reviser of this ConfigTemplateBasicInfo.

        **参数解释：** 最后修改人的用户名。 **取值范围：** 不涉及。

        :param last_reviser: The last_reviser of this ConfigTemplateBasicInfo.
        :type last_reviser: str
        """
        self._last_reviser = last_reviser

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this ConfigTemplateBasicInfo.

        **参数解释：** 配置模板上一次修改时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :return: The last_update_time of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this ConfigTemplateBasicInfo.

        **参数解释：** 配置模板上一次修改时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :param last_update_time: The last_update_time of this ConfigTemplateBasicInfo.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def name(self):
        r"""Gets the name of this ConfigTemplateBasicInfo.

        **参数解释：** 配置模板的名称。 **取值范围：** 不涉及。

        :return: The name of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConfigTemplateBasicInfo.

        **参数解释：** 配置模板的名称。 **取值范围：** 不涉及。

        :param name: The name of this ConfigTemplateBasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ConfigTemplateBasicInfo.

        **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **取值范围：** 长度为[1~32]个字符。

        :return: The project_id of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ConfigTemplateBasicInfo.

        **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **取值范围：** 长度为[1~32]个字符。

        :param project_id: The project_id of this ConfigTemplateBasicInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this ConfigTemplateBasicInfo.

        **参数解释：** 项目名。 **取值范围：** 不涉及。

        :return: The project_name of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ConfigTemplateBasicInfo.

        **参数解释：** 项目名。 **取值范围：** 不涉及。

        :param project_name: The project_name of this ConfigTemplateBasicInfo.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def region(self):
        r"""Gets the region of this ConfigTemplateBasicInfo.

        **参数解释：** 华为云地域。 **取值范围：** 不涉及。

        :return: The region of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ConfigTemplateBasicInfo.

        **参数解释：** 华为云地域。 **取值范围：** 不涉及。

        :param region: The region of this ConfigTemplateBasicInfo.
        :type region: str
        """
        self._region = region

    @property
    def repo_type(self):
        r"""Gets the repo_type of this ConfigTemplateBasicInfo.

        **参数解释：** 代码仓类型。 **取值范围：** - DevCloud：CodeArtsRepo仓。 - Gitee：Gitee仓。 - GitHub：GitHub仓。 - GitPub：通用Git仓。 - gitcode：GitCode仓。 - gitlab：GitLab仓。 - self_gitlab：自建GitLab仓。 - tfs_git：TFS仓。 - bitbucket：Bitbucket仓。

        :return: The repo_type of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        r"""Sets the repo_type of this ConfigTemplateBasicInfo.

        **参数解释：** 代码仓类型。 **取值范围：** - DevCloud：CodeArtsRepo仓。 - Gitee：Gitee仓。 - GitHub：GitHub仓。 - GitPub：通用Git仓。 - gitcode：GitCode仓。 - gitlab：GitLab仓。 - self_gitlab：自建GitLab仓。 - tfs_git：TFS仓。 - bitbucket：Bitbucket仓。

        :param repo_type: The repo_type of this ConfigTemplateBasicInfo.
        :type repo_type: str
        """
        self._repo_type = repo_type

    @property
    def repo_url(self):
        r"""Gets the repo_url of this ConfigTemplateBasicInfo.

        **参数解释：** 代码仓地址。 **取值范围：** 不涉及。

        :return: The repo_url of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        r"""Sets the repo_url of this ConfigTemplateBasicInfo.

        **参数解释：** 代码仓地址。 **取值范围：** 不涉及。

        :param repo_url: The repo_url of this ConfigTemplateBasicInfo.
        :type repo_url: str
        """
        self._repo_url = repo_url

    @property
    def resource_pool_id(self):
        r"""Gets the resource_pool_id of this ConfigTemplateBasicInfo.

        **参数解释：** 启用的资源池ID，使用内置执行机的情况下为\"\"。 **取值范围：** 不涉及。

        :return: The resource_pool_id of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._resource_pool_id

    @resource_pool_id.setter
    def resource_pool_id(self, resource_pool_id):
        r"""Sets the resource_pool_id of this ConfigTemplateBasicInfo.

        **参数解释：** 启用的资源池ID，使用内置执行机的情况下为\"\"。 **取值范围：** 不涉及。

        :param resource_pool_id: The resource_pool_id of this ConfigTemplateBasicInfo.
        :type resource_pool_id: str
        """
        self._resource_pool_id = resource_pool_id

    @property
    def resource_pool_name(self):
        r"""Gets the resource_pool_name of this ConfigTemplateBasicInfo.

        **参数解释：** 启用的资源池名称，使用内置执行机的情况下为空。 **取值范围：** 不涉及。

        :return: The resource_pool_name of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._resource_pool_name

    @resource_pool_name.setter
    def resource_pool_name(self, resource_pool_name):
        r"""Sets the resource_pool_name of this ConfigTemplateBasicInfo.

        **参数解释：** 启用的资源池名称，使用内置执行机的情况下为空。 **取值范围：** 不涉及。

        :param resource_pool_name: The resource_pool_name of this ConfigTemplateBasicInfo.
        :type resource_pool_name: str
        """
        self._resource_pool_name = resource_pool_name

    @property
    def resource_pool_type(self):
        r"""Gets the resource_pool_type of this ConfigTemplateBasicInfo.

        **参数解释：** 启用的资源池类型。 **取值范围：** - default：使用内置资源池。 - exclusive：使用专属资源池。 - self-hosted：使用自定义资源池。

        :return: The resource_pool_type of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._resource_pool_type

    @resource_pool_type.setter
    def resource_pool_type(self, resource_pool_type):
        r"""Sets the resource_pool_type of this ConfigTemplateBasicInfo.

        **参数解释：** 启用的资源池类型。 **取值范围：** - default：使用内置资源池。 - exclusive：使用专属资源池。 - self-hosted：使用自定义资源池。

        :param resource_pool_type: The resource_pool_type of this ConfigTemplateBasicInfo.
        :type resource_pool_type: str
        """
        self._resource_pool_type = resource_pool_type

    @property
    def review_data(self):
        r"""Gets the review_data of this ConfigTemplateBasicInfo.

        **参数解释：** 任务门禁配置列表。

        :return: The review_data of this ConfigTemplateBasicInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.ReviewDataInfoResponse`]
        """
        return self._review_data

    @review_data.setter
    def review_data(self, review_data):
        r"""Sets the review_data of this ConfigTemplateBasicInfo.

        **参数解释：** 任务门禁配置列表。

        :param review_data: The review_data of this ConfigTemplateBasicInfo.
        :type review_data: list[:class:`huaweicloudsdkcodeartscheck.v2.ReviewDataInfoResponse`]
        """
        self._review_data = review_data

    @property
    def review_data_json(self):
        r"""Gets the review_data_json of this ConfigTemplateBasicInfo.

        **参数解释：** 任务门禁配置列表的json字符串。 **取值范围：** 不涉及。

        :return: The review_data_json of this ConfigTemplateBasicInfo.
        :rtype: str
        """
        return self._review_data_json

    @review_data_json.setter
    def review_data_json(self, review_data_json):
        r"""Sets the review_data_json of this ConfigTemplateBasicInfo.

        **参数解释：** 任务门禁配置列表的json字符串。 **取值范围：** 不涉及。

        :param review_data_json: The review_data_json of this ConfigTemplateBasicInfo.
        :type review_data_json: str
        """
        self._review_data_json = review_data_json

    @property
    def rule_sets(self):
        r"""Gets the rule_sets of this ConfigTemplateBasicInfo.

        **参数解释：** 规则集配置列表。

        :return: The rule_sets of this ConfigTemplateBasicInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets):
        r"""Sets the rule_sets of this ConfigTemplateBasicInfo.

        **参数解释：** 规则集配置列表。

        :param rule_sets: The rule_sets of this ConfigTemplateBasicInfo.
        :type rule_sets: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        """
        self._rule_sets = rule_sets

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
        if not isinstance(other, ConfigTemplateBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
