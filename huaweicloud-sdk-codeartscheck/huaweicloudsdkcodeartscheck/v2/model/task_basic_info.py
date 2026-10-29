# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskBasicInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branch_name': 'str',
        'can_delete': 'bool',
        'can_edit': 'bool',
        'can_execute': 'bool',
        'can_read': 'bool',
        'config_template': 'ConfigTemplateBasicInfo',
        'config_template_id': 'str',
        'create_time': 'str',
        'id': 'str',
        'is_followed': 'bool',
        'job_result': 'JobResultInfo',
        'last_job': 'JobBasicInfo',
        'last_update_time': 'str',
        'name': 'str',
        'owner': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'region': 'str',
        'repo_url': 'str',
        'rule_sets': 'list[ConfigTemplateRuleSetInfo]',
        'rule_type': 'str',
        'task_group_id': 'str'
    }

    attribute_map = {
        'branch_name': 'branchName',
        'can_delete': 'canDelete',
        'can_edit': 'canEdit',
        'can_execute': 'canExecute',
        'can_read': 'canRead',
        'config_template': 'configTemplate',
        'config_template_id': 'configTemplateId',
        'create_time': 'createTime',
        'id': 'id',
        'is_followed': 'isFollowed',
        'job_result': 'jobResult',
        'last_job': 'lastJob',
        'last_update_time': 'lastUpdateTime',
        'name': 'name',
        'owner': 'owner',
        'project_id': 'projectId',
        'project_name': 'projectName',
        'region': 'region',
        'repo_url': 'repoUrl',
        'rule_sets': 'ruleSets',
        'rule_type': 'ruleType',
        'task_group_id': 'taskGroupId'
    }

    def __init__(self, branch_name=None, can_delete=None, can_edit=None, can_execute=None, can_read=None, config_template=None, config_template_id=None, create_time=None, id=None, is_followed=None, job_result=None, last_job=None, last_update_time=None, name=None, owner=None, project_id=None, project_name=None, region=None, repo_url=None, rule_sets=None, rule_type=None, task_group_id=None):
        r"""TaskBasicInfo

        The model defined in huaweicloud sdk

        :param branch_name: **参数解释：** 分支名称。 **取值范围：** 不涉及。
        :type branch_name: str
        :param can_delete: **参数解释：** 是否有删除任务的权限。 **取值范围：** - true：有删除的权限。 - false：没有删除的权限。
        :type can_delete: bool
        :param can_edit: **参数解释：** 是否有编辑的权限。 **取值范围：** - true：有编辑的权限。 - false：没有编辑的权限。
        :type can_edit: bool
        :param can_execute: **参数解释：** 是否有执行的权限。 **取值范围：** - true：有执行的权限。 - false：没有执行的权限。
        :type can_execute: bool
        :param can_read: **参数解释：** 是否有读的权限。 **取值范围：** - true：有读的权限。 - false：没有读的权限。
        :type can_read: bool
        :param config_template: 
        :type config_template: :class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateBasicInfo`
        :param config_template_id: **参数解释：** 任务的配置模板的ID。 **取值范围：** 长度为[1~128]个字符。
        :type config_template_id: str
        :param create_time: **参数解释：** 任务的创建时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\&quot;2025-11-28T06:55:41Z\&quot;。 **取值范围：** 不涉及。
        :type create_time: str
        :param id: **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~128]个字符。
        :type id: str
        :param is_followed: **参数解释：** 任务是否被关注。 **取值范围：** - true：任务被关注。 - false：任务未被关注。
        :type is_followed: bool
        :param job_result: 
        :type job_result: :class:`huaweicloudsdkcodeartscheck.v2.JobResultInfo`
        :param last_job: 
        :type last_job: :class:`huaweicloudsdkcodeartscheck.v2.JobBasicInfo`
        :param last_update_time: **参数解释：** 任务的上一次更新时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\&quot;2025-11-28T06:55:41Z\&quot;。 **取值范围：** 不涉及。
        :type last_update_time: str
        :param name: **参数解释：** 代码检查任务名。 **取值范围：** 不涉及。
        :type name: str
        :param owner: **参数解释：** 代码检查任务所有者。 **取值范围：** 不涉及。
        :type owner: str
        :param project_id: **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **取值范围：** 长度为[1~32]个字符。
        :type project_id: str
        :param project_name: **参数解释：** 项目名。 **取值范围：** 不涉及。
        :type project_name: str
        :param region: **参数解释：** 华为云地域。 **取值范围：** 不涉及。
        :type region: str
        :param repo_url: **参数解释：** 代码仓地址。 **取值范围：** 不涉及。
        :type repo_url: str
        :param rule_sets: **参数解释：** 规则集配置列表。
        :type rule_sets: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        :param rule_type: **参数解释：** 任务类型。 **取值范围：** - basic：普通任务。 - security：安全增强包任务。
        :type rule_type: str
        :param task_group_id: **参数解释：** 任务分组的ID。 **取值范围：** 长度为[1~128]个字符。
        :type task_group_id: str
        """
        
        

        self._branch_name = None
        self._can_delete = None
        self._can_edit = None
        self._can_execute = None
        self._can_read = None
        self._config_template = None
        self._config_template_id = None
        self._create_time = None
        self._id = None
        self._is_followed = None
        self._job_result = None
        self._last_job = None
        self._last_update_time = None
        self._name = None
        self._owner = None
        self._project_id = None
        self._project_name = None
        self._region = None
        self._repo_url = None
        self._rule_sets = None
        self._rule_type = None
        self._task_group_id = None
        self.discriminator = None

        if branch_name is not None:
            self.branch_name = branch_name
        if can_delete is not None:
            self.can_delete = can_delete
        if can_edit is not None:
            self.can_edit = can_edit
        if can_execute is not None:
            self.can_execute = can_execute
        if can_read is not None:
            self.can_read = can_read
        if config_template is not None:
            self.config_template = config_template
        if config_template_id is not None:
            self.config_template_id = config_template_id
        if create_time is not None:
            self.create_time = create_time
        if id is not None:
            self.id = id
        if is_followed is not None:
            self.is_followed = is_followed
        if job_result is not None:
            self.job_result = job_result
        if last_job is not None:
            self.last_job = last_job
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if region is not None:
            self.region = region
        if repo_url is not None:
            self.repo_url = repo_url
        if rule_sets is not None:
            self.rule_sets = rule_sets
        if rule_type is not None:
            self.rule_type = rule_type
        if task_group_id is not None:
            self.task_group_id = task_group_id

    @property
    def branch_name(self):
        r"""Gets the branch_name of this TaskBasicInfo.

        **参数解释：** 分支名称。 **取值范围：** 不涉及。

        :return: The branch_name of this TaskBasicInfo.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this TaskBasicInfo.

        **参数解释：** 分支名称。 **取值范围：** 不涉及。

        :param branch_name: The branch_name of this TaskBasicInfo.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def can_delete(self):
        r"""Gets the can_delete of this TaskBasicInfo.

        **参数解释：** 是否有删除任务的权限。 **取值范围：** - true：有删除的权限。 - false：没有删除的权限。

        :return: The can_delete of this TaskBasicInfo.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this TaskBasicInfo.

        **参数解释：** 是否有删除任务的权限。 **取值范围：** - true：有删除的权限。 - false：没有删除的权限。

        :param can_delete: The can_delete of this TaskBasicInfo.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_edit(self):
        r"""Gets the can_edit of this TaskBasicInfo.

        **参数解释：** 是否有编辑的权限。 **取值范围：** - true：有编辑的权限。 - false：没有编辑的权限。

        :return: The can_edit of this TaskBasicInfo.
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        r"""Sets the can_edit of this TaskBasicInfo.

        **参数解释：** 是否有编辑的权限。 **取值范围：** - true：有编辑的权限。 - false：没有编辑的权限。

        :param can_edit: The can_edit of this TaskBasicInfo.
        :type can_edit: bool
        """
        self._can_edit = can_edit

    @property
    def can_execute(self):
        r"""Gets the can_execute of this TaskBasicInfo.

        **参数解释：** 是否有执行的权限。 **取值范围：** - true：有执行的权限。 - false：没有执行的权限。

        :return: The can_execute of this TaskBasicInfo.
        :rtype: bool
        """
        return self._can_execute

    @can_execute.setter
    def can_execute(self, can_execute):
        r"""Sets the can_execute of this TaskBasicInfo.

        **参数解释：** 是否有执行的权限。 **取值范围：** - true：有执行的权限。 - false：没有执行的权限。

        :param can_execute: The can_execute of this TaskBasicInfo.
        :type can_execute: bool
        """
        self._can_execute = can_execute

    @property
    def can_read(self):
        r"""Gets the can_read of this TaskBasicInfo.

        **参数解释：** 是否有读的权限。 **取值范围：** - true：有读的权限。 - false：没有读的权限。

        :return: The can_read of this TaskBasicInfo.
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        r"""Sets the can_read of this TaskBasicInfo.

        **参数解释：** 是否有读的权限。 **取值范围：** - true：有读的权限。 - false：没有读的权限。

        :param can_read: The can_read of this TaskBasicInfo.
        :type can_read: bool
        """
        self._can_read = can_read

    @property
    def config_template(self):
        r"""Gets the config_template of this TaskBasicInfo.

        :return: The config_template of this TaskBasicInfo.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateBasicInfo`
        """
        return self._config_template

    @config_template.setter
    def config_template(self, config_template):
        r"""Sets the config_template of this TaskBasicInfo.

        :param config_template: The config_template of this TaskBasicInfo.
        :type config_template: :class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateBasicInfo`
        """
        self._config_template = config_template

    @property
    def config_template_id(self):
        r"""Gets the config_template_id of this TaskBasicInfo.

        **参数解释：** 任务的配置模板的ID。 **取值范围：** 长度为[1~128]个字符。

        :return: The config_template_id of this TaskBasicInfo.
        :rtype: str
        """
        return self._config_template_id

    @config_template_id.setter
    def config_template_id(self, config_template_id):
        r"""Sets the config_template_id of this TaskBasicInfo.

        **参数解释：** 任务的配置模板的ID。 **取值范围：** 长度为[1~128]个字符。

        :param config_template_id: The config_template_id of this TaskBasicInfo.
        :type config_template_id: str
        """
        self._config_template_id = config_template_id

    @property
    def create_time(self):
        r"""Gets the create_time of this TaskBasicInfo.

        **参数解释：** 任务的创建时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :return: The create_time of this TaskBasicInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TaskBasicInfo.

        **参数解释：** 任务的创建时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :param create_time: The create_time of this TaskBasicInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this TaskBasicInfo.

        **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~128]个字符。

        :return: The id of this TaskBasicInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskBasicInfo.

        **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~128]个字符。

        :param id: The id of this TaskBasicInfo.
        :type id: str
        """
        self._id = id

    @property
    def is_followed(self):
        r"""Gets the is_followed of this TaskBasicInfo.

        **参数解释：** 任务是否被关注。 **取值范围：** - true：任务被关注。 - false：任务未被关注。

        :return: The is_followed of this TaskBasicInfo.
        :rtype: bool
        """
        return self._is_followed

    @is_followed.setter
    def is_followed(self, is_followed):
        r"""Sets the is_followed of this TaskBasicInfo.

        **参数解释：** 任务是否被关注。 **取值范围：** - true：任务被关注。 - false：任务未被关注。

        :param is_followed: The is_followed of this TaskBasicInfo.
        :type is_followed: bool
        """
        self._is_followed = is_followed

    @property
    def job_result(self):
        r"""Gets the job_result of this TaskBasicInfo.

        :return: The job_result of this TaskBasicInfo.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.JobResultInfo`
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        r"""Sets the job_result of this TaskBasicInfo.

        :param job_result: The job_result of this TaskBasicInfo.
        :type job_result: :class:`huaweicloudsdkcodeartscheck.v2.JobResultInfo`
        """
        self._job_result = job_result

    @property
    def last_job(self):
        r"""Gets the last_job of this TaskBasicInfo.

        :return: The last_job of this TaskBasicInfo.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.JobBasicInfo`
        """
        return self._last_job

    @last_job.setter
    def last_job(self, last_job):
        r"""Sets the last_job of this TaskBasicInfo.

        :param last_job: The last_job of this TaskBasicInfo.
        :type last_job: :class:`huaweicloudsdkcodeartscheck.v2.JobBasicInfo`
        """
        self._last_job = last_job

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this TaskBasicInfo.

        **参数解释：** 任务的上一次更新时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :return: The last_update_time of this TaskBasicInfo.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this TaskBasicInfo.

        **参数解释：** 任务的上一次更新时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :param last_update_time: The last_update_time of this TaskBasicInfo.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def name(self):
        r"""Gets the name of this TaskBasicInfo.

        **参数解释：** 代码检查任务名。 **取值范围：** 不涉及。

        :return: The name of this TaskBasicInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskBasicInfo.

        **参数解释：** 代码检查任务名。 **取值范围：** 不涉及。

        :param name: The name of this TaskBasicInfo.
        :type name: str
        """
        self._name = name

    @property
    def owner(self):
        r"""Gets the owner of this TaskBasicInfo.

        **参数解释：** 代码检查任务所有者。 **取值范围：** 不涉及。

        :return: The owner of this TaskBasicInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TaskBasicInfo.

        **参数解释：** 代码检查任务所有者。 **取值范围：** 不涉及。

        :param owner: The owner of this TaskBasicInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def project_id(self):
        r"""Gets the project_id of this TaskBasicInfo.

        **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **取值范围：** 长度为[1~32]个字符。

        :return: The project_id of this TaskBasicInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TaskBasicInfo.

        **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **取值范围：** 长度为[1~32]个字符。

        :param project_id: The project_id of this TaskBasicInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this TaskBasicInfo.

        **参数解释：** 项目名。 **取值范围：** 不涉及。

        :return: The project_name of this TaskBasicInfo.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this TaskBasicInfo.

        **参数解释：** 项目名。 **取值范围：** 不涉及。

        :param project_name: The project_name of this TaskBasicInfo.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def region(self):
        r"""Gets the region of this TaskBasicInfo.

        **参数解释：** 华为云地域。 **取值范围：** 不涉及。

        :return: The region of this TaskBasicInfo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this TaskBasicInfo.

        **参数解释：** 华为云地域。 **取值范围：** 不涉及。

        :param region: The region of this TaskBasicInfo.
        :type region: str
        """
        self._region = region

    @property
    def repo_url(self):
        r"""Gets the repo_url of this TaskBasicInfo.

        **参数解释：** 代码仓地址。 **取值范围：** 不涉及。

        :return: The repo_url of this TaskBasicInfo.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        r"""Sets the repo_url of this TaskBasicInfo.

        **参数解释：** 代码仓地址。 **取值范围：** 不涉及。

        :param repo_url: The repo_url of this TaskBasicInfo.
        :type repo_url: str
        """
        self._repo_url = repo_url

    @property
    def rule_sets(self):
        r"""Gets the rule_sets of this TaskBasicInfo.

        **参数解释：** 规则集配置列表。

        :return: The rule_sets of this TaskBasicInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets):
        r"""Sets the rule_sets of this TaskBasicInfo.

        **参数解释：** 规则集配置列表。

        :param rule_sets: The rule_sets of this TaskBasicInfo.
        :type rule_sets: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        """
        self._rule_sets = rule_sets

    @property
    def rule_type(self):
        r"""Gets the rule_type of this TaskBasicInfo.

        **参数解释：** 任务类型。 **取值范围：** - basic：普通任务。 - security：安全增强包任务。

        :return: The rule_type of this TaskBasicInfo.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this TaskBasicInfo.

        **参数解释：** 任务类型。 **取值范围：** - basic：普通任务。 - security：安全增强包任务。

        :param rule_type: The rule_type of this TaskBasicInfo.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def task_group_id(self):
        r"""Gets the task_group_id of this TaskBasicInfo.

        **参数解释：** 任务分组的ID。 **取值范围：** 长度为[1~128]个字符。

        :return: The task_group_id of this TaskBasicInfo.
        :rtype: str
        """
        return self._task_group_id

    @task_group_id.setter
    def task_group_id(self, task_group_id):
        r"""Sets the task_group_id of this TaskBasicInfo.

        **参数解释：** 任务分组的ID。 **取值范围：** 长度为[1~128]个字符。

        :param task_group_id: The task_group_id of this TaskBasicInfo.
        :type task_group_id: str
        """
        self._task_group_id = task_group_id

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
        if not isinstance(other, TaskBasicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
