# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskBasicInfoV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'avastar_type': 'str',
        'branch_name': 'str',
        'can_change_ignore_mode': 'bool',
        'can_delete': 'bool',
        'can_edit': 'bool',
        'can_edit_template_switch': 'bool',
        'can_execute': 'bool',
        'can_read': 'bool',
        'check_param_list': 'list[CustomParameter]',
        'check_param_map': 'TaskBasicInfoV3CheckParamMap',
        'config_template_id': 'str',
        'create_time': 'str',
        'criterion_sets': 'list[ConfigTemplateRuleSetInfo]',
        'custom_params': 'list[CustomParameter]',
        'default_branch_name': 'str',
        'file_encoding': 'str',
        'hw_cloud_region': 'str',
        'id': 'str',
        'include_paths': 'str',
        'is_set_mr_webhook': 'bool',
        'is_set_push_webhook': 'bool',
        'is_set_webhook': 'bool',
        'is_template_task': 'bool',
        'job_id': 'str',
        'job_timeout': 'str',
        'last_finished_full_job_id': 'str',
        'last_job': 'JobBasicInfoV3',
        'last_reviser': 'str',
        'last_update_time': 'str',
        'model_sets': 'list[str]',
        'mr_check_branch_strategy': 'int',
        'name': 'str',
        'notification_config': 'str',
        'owner': 'str',
        'owner_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'region': 'str',
        'repo_id': 'str',
        'repo_url': 'str',
        'review_data': 'list[str]',
        'rule_sets': 'list[str]',
        'source': 'str',
        'task_group_id': 'str',
        'task_ids': 'list[str]',
        'tenant_id': 'str',
        'use_cache': 'bool',
        'use_workspace_notification_config': 'int',
        'version_update_delay_days': 'list[str]',
        'webhook_check_mode': 'int',
        'zone': 'str'
    }

    attribute_map = {
        'avastar_type': 'avastarType',
        'branch_name': 'branchName',
        'can_change_ignore_mode': 'canChangeIgnoreMode',
        'can_delete': 'canDelete',
        'can_edit': 'canEdit',
        'can_edit_template_switch': 'canEditTemplateSwitch',
        'can_execute': 'canExecute',
        'can_read': 'canRead',
        'check_param_list': 'checkParamList',
        'check_param_map': 'checkParamMap',
        'config_template_id': 'configTemplateId',
        'create_time': 'createTime',
        'criterion_sets': 'criterionSets',
        'custom_params': 'customParams',
        'default_branch_name': 'defaultBranchName',
        'file_encoding': 'fileEncoding',
        'hw_cloud_region': 'hwCloudRegion',
        'id': 'id',
        'include_paths': 'includePaths',
        'is_set_mr_webhook': 'isSetMrWebhook',
        'is_set_push_webhook': 'isSetPushWebhook',
        'is_set_webhook': 'isSetWebhook',
        'is_template_task': 'isTemplateTask',
        'job_id': 'jobId',
        'job_timeout': 'jobTimeout',
        'last_finished_full_job_id': 'lastFinishedFullJobId',
        'last_job': 'lastJob',
        'last_reviser': 'lastReviser',
        'last_update_time': 'lastUpdateTime',
        'model_sets': 'modelSets',
        'mr_check_branch_strategy': 'mrCheckBranchStrategy',
        'name': 'name',
        'notification_config': 'notificationConfig',
        'owner': 'owner',
        'owner_id': 'ownerId',
        'project_id': 'projectId',
        'project_name': 'projectName',
        'region': 'region',
        'repo_id': 'repoId',
        'repo_url': 'repoUrl',
        'review_data': 'reviewData',
        'rule_sets': 'ruleSets',
        'source': 'source',
        'task_group_id': 'taskGroupId',
        'task_ids': 'taskIds',
        'tenant_id': 'tenantId',
        'use_cache': 'useCache',
        'use_workspace_notification_config': 'useWorkspaceNotificationConfig',
        'version_update_delay_days': 'versionUpdateDelayDays',
        'webhook_check_mode': 'webhookCheckMode',
        'zone': 'zone'
    }

    def __init__(self, avastar_type=None, branch_name=None, can_change_ignore_mode=None, can_delete=None, can_edit=None, can_edit_template_switch=None, can_execute=None, can_read=None, check_param_list=None, check_param_map=None, config_template_id=None, create_time=None, criterion_sets=None, custom_params=None, default_branch_name=None, file_encoding=None, hw_cloud_region=None, id=None, include_paths=None, is_set_mr_webhook=None, is_set_push_webhook=None, is_set_webhook=None, is_template_task=None, job_id=None, job_timeout=None, last_finished_full_job_id=None, last_job=None, last_reviser=None, last_update_time=None, model_sets=None, mr_check_branch_strategy=None, name=None, notification_config=None, owner=None, owner_id=None, project_id=None, project_name=None, region=None, repo_id=None, repo_url=None, review_data=None, rule_sets=None, source=None, task_group_id=None, task_ids=None, tenant_id=None, use_cache=None, use_workspace_notification_config=None, version_update_delay_days=None, webhook_check_mode=None, zone=None):
        r"""TaskBasicInfoV3

        The model defined in huaweicloud sdk

        :param avastar_type: **参数解释：** 头像颜色。 **取值范围：** - pure-blue：蓝色。 - pure-purple：紫色。 - pure-tomato：红色。 - pure-green：绿色。 - pure-orange：橙色。 - pure-pink：粉色。
        :type avastar_type: str
        :param branch_name: **参数解释：** 分支名称。 **取值范围：** 长度为[1~200]个字符。
        :type branch_name: str
        :param can_change_ignore_mode: **参数解释：** 是否可以更新忽略文件模式。 **取值范围：** - true：能更新忽略文件模式。 - false：不能更新忽略文件模式。
        :type can_change_ignore_mode: bool
        :param can_delete: **参数解释：** 是否有删除任务的权限。 **取值范围：** - true：有删除的权限。 - false：没有删除的权限。
        :type can_delete: bool
        :param can_edit: **参数解释：** 是否有编辑的权限。 **取值范围：** - true：有编辑的权限。 - false：没有编辑的权限。
        :type can_edit: bool
        :param can_edit_template_switch: **参数解释：** 是否有切换任务模板的权限。 **取值范围：** - true：有切换任务模板的权限。 - false：没有切换任务模板的权限。
        :type can_edit_template_switch: bool
        :param can_execute: **参数解释：** 是否有执行的权限。 **取值范围：** - true：有执行的权限。 - false：没有执行的权限。
        :type can_execute: bool
        :param can_read: **参数解释：** 是否有读的权限。 **取值范围：** - true：有读的权限。 - false：没有读的权限。
        :type can_read: bool
        :param check_param_list: **参数解释：** 自定义参数列表。
        :type check_param_list: list[:class:`huaweicloudsdkcodeartscheck.v2.CustomParameter`]
        :param check_param_map: 
        :type check_param_map: :class:`huaweicloudsdkcodeartscheck.v2.TaskBasicInfoV3CheckParamMap`
        :param config_template_id: **参数解释：** 任务的配置模板的ID。 **取值范围：** 长度为[1~128]个字符。
        :type config_template_id: str
        :param create_time: **参数解释：** 任务的创建时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\&quot;2025-11-28T06:55:41Z\&quot;。 **取值范围：** 不涉及。
        :type create_time: str
        :param criterion_sets: **参数解释：** 规则集列表，该字段一般返回空数组[]。
        :type criterion_sets: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        :param custom_params: **参数解释：** 自定义参数列表，该字段一般返回空数组[]。
        :type custom_params: list[:class:`huaweicloudsdkcodeartscheck.v2.CustomParameter`]
        :param default_branch_name: **参数解释：** 默认分支的分支名。 **取值范围：** 长度为[1~200]个字符。
        :type default_branch_name: str
        :param file_encoding: **参数解释：** 文件编码。 **取值范围：** - UTF-8：UTF-8格式。 - GBK：GBK格式。
        :type file_encoding: str
        :param hw_cloud_region: **参数解释：** 华为云地域。 **取值范围：** 长度为[1~32]个字符。
        :type hw_cloud_region: str
        :param id: **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~128]个字符。
        :type id: str
        :param include_paths: **参数解释：** 检查目录。 不配置检查目录时，检查代码仓中所有目录下的代码文件； 配置检查目录时，只检查配置目录中的代码文件。 **取值范围：** 长度为[1~200]个字符。
        :type include_paths: str
        :param is_set_mr_webhook: **参数解释：** 是否打开合并请求时触发。 **取值范围：** - true：打开。 - false：关闭。
        :type is_set_mr_webhook: bool
        :param is_set_push_webhook: **参数解释：** 是否打开代码提交时触发。 **取值范围：** - true：打开。 - false：关闭。
        :type is_set_push_webhook: bool
        :param is_set_webhook: **参数解释：** 是否打开合并请求时触发。 **取值范围：** - true：打开。 - false：关闭。
        :type is_set_webhook: bool
        :param is_template_task: **参数解释：** 是否是任务模板。 **取值范围：** - true：是任务模板。 - false：不是任务模板。
        :type is_template_task: bool
        :param job_id: **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 长度为[1~128]个字符。
        :type job_id: str
        :param job_timeout: **参数解释:** 超时时间，以分钟为单位，格式固定为\&quot;xxx min\&quot;，其中xxx为整数，0 ＜ xxx ≤ 1200。 **取值范围：** 不涉及。
        :type job_timeout: str
        :param last_finished_full_job_id: **参数解释：** 最后一次检查完成的任务的执行ID。 **取值范围：** 长度为[1~128]个字符。
        :type last_finished_full_job_id: str
        :param last_job: 
        :type last_job: :class:`huaweicloudsdkcodeartscheck.v2.JobBasicInfoV3`
        :param last_reviser: **参数解释：** 任务的最后修改人。 **取值范围：** 不涉及。
        :type last_reviser: str
        :param last_update_time: **参数解释：** 任务的上一次更新时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\&quot;2025-11-28T06:55:41Z\&quot;。 **取值范围：** 不涉及。
        :type last_update_time: str
        :param model_sets: **参数解释：** 模型集列表，该字段一般返回空数组[]。
        :type model_sets: list[str]
        :param mr_check_branch_strategy: **参数解释：** mr检查分支门禁策略。 **取值范围：** - 0：白名单。
        :type mr_check_branch_strategy: int
        :param name: **参数解释：** 代码检查任务名。 **取值范围：** 长度为[1~128]个字符。
        :type name: str
        :param notification_config: **参数解释：** 消息通知是否使用项目通知设置的配置项，格式为x,x,x,x,x,x，其中x的取值为0或者1。 x为0时代表使用任务的通知设置，x为1时代表使用项目通知设置。 从左到右依次为站内消息通知、邮件通知、企业微信、钉钉、飞书、通用webhook的消息通知配置。 **取值范围：** 格式为x,x,x,x,x,x，其中x的取值为0或者1。
        :type notification_config: str
        :param owner: **参数解释：** 代码检查任务所有者。 **取值范围：** 长度为[1~255]个字符。
        :type owner: str
        :param owner_id: **参数解释：** 代码检查任务所有者的用户ID。 **取值范围：** 长度为[1~64]个字符。
        :type owner_id: str
        :param project_id: **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **取值范围：** 长度为[1~32]个字符。
        :type project_id: str
        :param project_name: **参数解释：** 项目名。 **取值范围：** 长度为[1~128]个字符。
        :type project_name: str
        :param region: **参数解释：** 地域，此字段固定为\&quot;suzhou\&quot;。 **取值范围：** suzhou。
        :type region: str
        :param repo_id: **参数解释：** 代码仓地址对应的CodeartsRepo仓的RepoId。 **取值范围：** 长度为[1~128]个字符。
        :type repo_id: str
        :param repo_url: **参数解释：** 代码仓地址。 **取值范围：** 长度为[1~1024]个字符。
        :type repo_url: str
        :param review_data: **参数解释：** 门禁配置，该字段一般返回空数组[]。
        :type review_data: list[str]
        :param rule_sets: **参数解释：** 规则集配置，该字段一般返回空数组[]。
        :type rule_sets: list[str]
        :param source: **参数解释：** 任务来源，一般为\&quot;customer\&quot;。 **取值范围：** customer。
        :type source: str
        :param task_group_id: **参数解释：** 任务分组的ID。 **取值范围：** 长度为[1~128]个字符。
        :type task_group_id: str
        :param task_ids: **参数解释：** 任务ID列表，该字段一般返回空数组[]。
        :type task_ids: list[str]
        :param tenant_id: **参数解释：** 任务所属的租户的租户ID，租户ID的值来源于IAM的租户ID。 **取值范围：** 长度为[1~32]个字符。
        :type tenant_id: str
        :param use_cache: **参数解释：** 查询任务信息是否使用缓存。 **取值范围：** - true：使用缓存。 - false：不使用缓存。
        :type use_cache: bool
        :param use_workspace_notification_config: **参数解释：** 消息通知是否使用项目通知设置的配置项，来自notificationConfig的对应的二进制的取反转化成十进制。 例如，notificationConfig配置为1,1,0,1,0,0，则二进制为110100，取反为001011，转化为10进制时该值为11，最终useWorkspaceNotificationConfig的值为11。 **取值范围：** 0-31
        :type use_workspace_notification_config: int
        :param version_update_delay_days: **参数解释：** 版本升级缓冲期，该字段一般返回空数组[]。
        :type version_update_delay_days: list[str]
        :param webhook_check_mode: **参数解释：** webhook检查模式，一般为0，代表禁止来自其它代码仓的MR。 **取值范围：** 0
        :type webhook_check_mode: int
        :param zone: **参数解释：** 区域，一般为green。 **取值范围：** green。
        :type zone: str
        """
        
        

        self._avastar_type = None
        self._branch_name = None
        self._can_change_ignore_mode = None
        self._can_delete = None
        self._can_edit = None
        self._can_edit_template_switch = None
        self._can_execute = None
        self._can_read = None
        self._check_param_list = None
        self._check_param_map = None
        self._config_template_id = None
        self._create_time = None
        self._criterion_sets = None
        self._custom_params = None
        self._default_branch_name = None
        self._file_encoding = None
        self._hw_cloud_region = None
        self._id = None
        self._include_paths = None
        self._is_set_mr_webhook = None
        self._is_set_push_webhook = None
        self._is_set_webhook = None
        self._is_template_task = None
        self._job_id = None
        self._job_timeout = None
        self._last_finished_full_job_id = None
        self._last_job = None
        self._last_reviser = None
        self._last_update_time = None
        self._model_sets = None
        self._mr_check_branch_strategy = None
        self._name = None
        self._notification_config = None
        self._owner = None
        self._owner_id = None
        self._project_id = None
        self._project_name = None
        self._region = None
        self._repo_id = None
        self._repo_url = None
        self._review_data = None
        self._rule_sets = None
        self._source = None
        self._task_group_id = None
        self._task_ids = None
        self._tenant_id = None
        self._use_cache = None
        self._use_workspace_notification_config = None
        self._version_update_delay_days = None
        self._webhook_check_mode = None
        self._zone = None
        self.discriminator = None

        if avastar_type is not None:
            self.avastar_type = avastar_type
        if branch_name is not None:
            self.branch_name = branch_name
        if can_change_ignore_mode is not None:
            self.can_change_ignore_mode = can_change_ignore_mode
        if can_delete is not None:
            self.can_delete = can_delete
        if can_edit is not None:
            self.can_edit = can_edit
        if can_edit_template_switch is not None:
            self.can_edit_template_switch = can_edit_template_switch
        if can_execute is not None:
            self.can_execute = can_execute
        if can_read is not None:
            self.can_read = can_read
        if check_param_list is not None:
            self.check_param_list = check_param_list
        if check_param_map is not None:
            self.check_param_map = check_param_map
        if config_template_id is not None:
            self.config_template_id = config_template_id
        if create_time is not None:
            self.create_time = create_time
        if criterion_sets is not None:
            self.criterion_sets = criterion_sets
        if custom_params is not None:
            self.custom_params = custom_params
        if default_branch_name is not None:
            self.default_branch_name = default_branch_name
        if file_encoding is not None:
            self.file_encoding = file_encoding
        if hw_cloud_region is not None:
            self.hw_cloud_region = hw_cloud_region
        if id is not None:
            self.id = id
        if include_paths is not None:
            self.include_paths = include_paths
        if is_set_mr_webhook is not None:
            self.is_set_mr_webhook = is_set_mr_webhook
        if is_set_push_webhook is not None:
            self.is_set_push_webhook = is_set_push_webhook
        if is_set_webhook is not None:
            self.is_set_webhook = is_set_webhook
        if is_template_task is not None:
            self.is_template_task = is_template_task
        if job_id is not None:
            self.job_id = job_id
        if job_timeout is not None:
            self.job_timeout = job_timeout
        if last_finished_full_job_id is not None:
            self.last_finished_full_job_id = last_finished_full_job_id
        if last_job is not None:
            self.last_job = last_job
        if last_reviser is not None:
            self.last_reviser = last_reviser
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if model_sets is not None:
            self.model_sets = model_sets
        if mr_check_branch_strategy is not None:
            self.mr_check_branch_strategy = mr_check_branch_strategy
        if name is not None:
            self.name = name
        if notification_config is not None:
            self.notification_config = notification_config
        if owner is not None:
            self.owner = owner
        if owner_id is not None:
            self.owner_id = owner_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if region is not None:
            self.region = region
        if repo_id is not None:
            self.repo_id = repo_id
        if repo_url is not None:
            self.repo_url = repo_url
        if review_data is not None:
            self.review_data = review_data
        if rule_sets is not None:
            self.rule_sets = rule_sets
        if source is not None:
            self.source = source
        if task_group_id is not None:
            self.task_group_id = task_group_id
        if task_ids is not None:
            self.task_ids = task_ids
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if use_cache is not None:
            self.use_cache = use_cache
        if use_workspace_notification_config is not None:
            self.use_workspace_notification_config = use_workspace_notification_config
        if version_update_delay_days is not None:
            self.version_update_delay_days = version_update_delay_days
        if webhook_check_mode is not None:
            self.webhook_check_mode = webhook_check_mode
        if zone is not None:
            self.zone = zone

    @property
    def avastar_type(self):
        r"""Gets the avastar_type of this TaskBasicInfoV3.

        **参数解释：** 头像颜色。 **取值范围：** - pure-blue：蓝色。 - pure-purple：紫色。 - pure-tomato：红色。 - pure-green：绿色。 - pure-orange：橙色。 - pure-pink：粉色。

        :return: The avastar_type of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._avastar_type

    @avastar_type.setter
    def avastar_type(self, avastar_type):
        r"""Sets the avastar_type of this TaskBasicInfoV3.

        **参数解释：** 头像颜色。 **取值范围：** - pure-blue：蓝色。 - pure-purple：紫色。 - pure-tomato：红色。 - pure-green：绿色。 - pure-orange：橙色。 - pure-pink：粉色。

        :param avastar_type: The avastar_type of this TaskBasicInfoV3.
        :type avastar_type: str
        """
        self._avastar_type = avastar_type

    @property
    def branch_name(self):
        r"""Gets the branch_name of this TaskBasicInfoV3.

        **参数解释：** 分支名称。 **取值范围：** 长度为[1~200]个字符。

        :return: The branch_name of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this TaskBasicInfoV3.

        **参数解释：** 分支名称。 **取值范围：** 长度为[1~200]个字符。

        :param branch_name: The branch_name of this TaskBasicInfoV3.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def can_change_ignore_mode(self):
        r"""Gets the can_change_ignore_mode of this TaskBasicInfoV3.

        **参数解释：** 是否可以更新忽略文件模式。 **取值范围：** - true：能更新忽略文件模式。 - false：不能更新忽略文件模式。

        :return: The can_change_ignore_mode of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._can_change_ignore_mode

    @can_change_ignore_mode.setter
    def can_change_ignore_mode(self, can_change_ignore_mode):
        r"""Sets the can_change_ignore_mode of this TaskBasicInfoV3.

        **参数解释：** 是否可以更新忽略文件模式。 **取值范围：** - true：能更新忽略文件模式。 - false：不能更新忽略文件模式。

        :param can_change_ignore_mode: The can_change_ignore_mode of this TaskBasicInfoV3.
        :type can_change_ignore_mode: bool
        """
        self._can_change_ignore_mode = can_change_ignore_mode

    @property
    def can_delete(self):
        r"""Gets the can_delete of this TaskBasicInfoV3.

        **参数解释：** 是否有删除任务的权限。 **取值范围：** - true：有删除的权限。 - false：没有删除的权限。

        :return: The can_delete of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this TaskBasicInfoV3.

        **参数解释：** 是否有删除任务的权限。 **取值范围：** - true：有删除的权限。 - false：没有删除的权限。

        :param can_delete: The can_delete of this TaskBasicInfoV3.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_edit(self):
        r"""Gets the can_edit of this TaskBasicInfoV3.

        **参数解释：** 是否有编辑的权限。 **取值范围：** - true：有编辑的权限。 - false：没有编辑的权限。

        :return: The can_edit of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._can_edit

    @can_edit.setter
    def can_edit(self, can_edit):
        r"""Sets the can_edit of this TaskBasicInfoV3.

        **参数解释：** 是否有编辑的权限。 **取值范围：** - true：有编辑的权限。 - false：没有编辑的权限。

        :param can_edit: The can_edit of this TaskBasicInfoV3.
        :type can_edit: bool
        """
        self._can_edit = can_edit

    @property
    def can_edit_template_switch(self):
        r"""Gets the can_edit_template_switch of this TaskBasicInfoV3.

        **参数解释：** 是否有切换任务模板的权限。 **取值范围：** - true：有切换任务模板的权限。 - false：没有切换任务模板的权限。

        :return: The can_edit_template_switch of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._can_edit_template_switch

    @can_edit_template_switch.setter
    def can_edit_template_switch(self, can_edit_template_switch):
        r"""Sets the can_edit_template_switch of this TaskBasicInfoV3.

        **参数解释：** 是否有切换任务模板的权限。 **取值范围：** - true：有切换任务模板的权限。 - false：没有切换任务模板的权限。

        :param can_edit_template_switch: The can_edit_template_switch of this TaskBasicInfoV3.
        :type can_edit_template_switch: bool
        """
        self._can_edit_template_switch = can_edit_template_switch

    @property
    def can_execute(self):
        r"""Gets the can_execute of this TaskBasicInfoV3.

        **参数解释：** 是否有执行的权限。 **取值范围：** - true：有执行的权限。 - false：没有执行的权限。

        :return: The can_execute of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._can_execute

    @can_execute.setter
    def can_execute(self, can_execute):
        r"""Sets the can_execute of this TaskBasicInfoV3.

        **参数解释：** 是否有执行的权限。 **取值范围：** - true：有执行的权限。 - false：没有执行的权限。

        :param can_execute: The can_execute of this TaskBasicInfoV3.
        :type can_execute: bool
        """
        self._can_execute = can_execute

    @property
    def can_read(self):
        r"""Gets the can_read of this TaskBasicInfoV3.

        **参数解释：** 是否有读的权限。 **取值范围：** - true：有读的权限。 - false：没有读的权限。

        :return: The can_read of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        r"""Sets the can_read of this TaskBasicInfoV3.

        **参数解释：** 是否有读的权限。 **取值范围：** - true：有读的权限。 - false：没有读的权限。

        :param can_read: The can_read of this TaskBasicInfoV3.
        :type can_read: bool
        """
        self._can_read = can_read

    @property
    def check_param_list(self):
        r"""Gets the check_param_list of this TaskBasicInfoV3.

        **参数解释：** 自定义参数列表。

        :return: The check_param_list of this TaskBasicInfoV3.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.CustomParameter`]
        """
        return self._check_param_list

    @check_param_list.setter
    def check_param_list(self, check_param_list):
        r"""Sets the check_param_list of this TaskBasicInfoV3.

        **参数解释：** 自定义参数列表。

        :param check_param_list: The check_param_list of this TaskBasicInfoV3.
        :type check_param_list: list[:class:`huaweicloudsdkcodeartscheck.v2.CustomParameter`]
        """
        self._check_param_list = check_param_list

    @property
    def check_param_map(self):
        r"""Gets the check_param_map of this TaskBasicInfoV3.

        :return: The check_param_map of this TaskBasicInfoV3.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.TaskBasicInfoV3CheckParamMap`
        """
        return self._check_param_map

    @check_param_map.setter
    def check_param_map(self, check_param_map):
        r"""Sets the check_param_map of this TaskBasicInfoV3.

        :param check_param_map: The check_param_map of this TaskBasicInfoV3.
        :type check_param_map: :class:`huaweicloudsdkcodeartscheck.v2.TaskBasicInfoV3CheckParamMap`
        """
        self._check_param_map = check_param_map

    @property
    def config_template_id(self):
        r"""Gets the config_template_id of this TaskBasicInfoV3.

        **参数解释：** 任务的配置模板的ID。 **取值范围：** 长度为[1~128]个字符。

        :return: The config_template_id of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._config_template_id

    @config_template_id.setter
    def config_template_id(self, config_template_id):
        r"""Sets the config_template_id of this TaskBasicInfoV3.

        **参数解释：** 任务的配置模板的ID。 **取值范围：** 长度为[1~128]个字符。

        :param config_template_id: The config_template_id of this TaskBasicInfoV3.
        :type config_template_id: str
        """
        self._config_template_id = config_template_id

    @property
    def create_time(self):
        r"""Gets the create_time of this TaskBasicInfoV3.

        **参数解释：** 任务的创建时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :return: The create_time of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TaskBasicInfoV3.

        **参数解释：** 任务的创建时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :param create_time: The create_time of this TaskBasicInfoV3.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def criterion_sets(self):
        r"""Gets the criterion_sets of this TaskBasicInfoV3.

        **参数解释：** 规则集列表，该字段一般返回空数组[]。

        :return: The criterion_sets of this TaskBasicInfoV3.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        """
        return self._criterion_sets

    @criterion_sets.setter
    def criterion_sets(self, criterion_sets):
        r"""Sets the criterion_sets of this TaskBasicInfoV3.

        **参数解释：** 规则集列表，该字段一般返回空数组[]。

        :param criterion_sets: The criterion_sets of this TaskBasicInfoV3.
        :type criterion_sets: list[:class:`huaweicloudsdkcodeartscheck.v2.ConfigTemplateRuleSetInfo`]
        """
        self._criterion_sets = criterion_sets

    @property
    def custom_params(self):
        r"""Gets the custom_params of this TaskBasicInfoV3.

        **参数解释：** 自定义参数列表，该字段一般返回空数组[]。

        :return: The custom_params of this TaskBasicInfoV3.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.CustomParameter`]
        """
        return self._custom_params

    @custom_params.setter
    def custom_params(self, custom_params):
        r"""Sets the custom_params of this TaskBasicInfoV3.

        **参数解释：** 自定义参数列表，该字段一般返回空数组[]。

        :param custom_params: The custom_params of this TaskBasicInfoV3.
        :type custom_params: list[:class:`huaweicloudsdkcodeartscheck.v2.CustomParameter`]
        """
        self._custom_params = custom_params

    @property
    def default_branch_name(self):
        r"""Gets the default_branch_name of this TaskBasicInfoV3.

        **参数解释：** 默认分支的分支名。 **取值范围：** 长度为[1~200]个字符。

        :return: The default_branch_name of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._default_branch_name

    @default_branch_name.setter
    def default_branch_name(self, default_branch_name):
        r"""Sets the default_branch_name of this TaskBasicInfoV3.

        **参数解释：** 默认分支的分支名。 **取值范围：** 长度为[1~200]个字符。

        :param default_branch_name: The default_branch_name of this TaskBasicInfoV3.
        :type default_branch_name: str
        """
        self._default_branch_name = default_branch_name

    @property
    def file_encoding(self):
        r"""Gets the file_encoding of this TaskBasicInfoV3.

        **参数解释：** 文件编码。 **取值范围：** - UTF-8：UTF-8格式。 - GBK：GBK格式。

        :return: The file_encoding of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._file_encoding

    @file_encoding.setter
    def file_encoding(self, file_encoding):
        r"""Sets the file_encoding of this TaskBasicInfoV3.

        **参数解释：** 文件编码。 **取值范围：** - UTF-8：UTF-8格式。 - GBK：GBK格式。

        :param file_encoding: The file_encoding of this TaskBasicInfoV3.
        :type file_encoding: str
        """
        self._file_encoding = file_encoding

    @property
    def hw_cloud_region(self):
        r"""Gets the hw_cloud_region of this TaskBasicInfoV3.

        **参数解释：** 华为云地域。 **取值范围：** 长度为[1~32]个字符。

        :return: The hw_cloud_region of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._hw_cloud_region

    @hw_cloud_region.setter
    def hw_cloud_region(self, hw_cloud_region):
        r"""Sets the hw_cloud_region of this TaskBasicInfoV3.

        **参数解释：** 华为云地域。 **取值范围：** 长度为[1~32]个字符。

        :param hw_cloud_region: The hw_cloud_region of this TaskBasicInfoV3.
        :type hw_cloud_region: str
        """
        self._hw_cloud_region = hw_cloud_region

    @property
    def id(self):
        r"""Gets the id of this TaskBasicInfoV3.

        **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~128]个字符。

        :return: The id of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TaskBasicInfoV3.

        **参数解释：** 任务ID，即新建检查任务接口的返回值，每个代码检查任务及其下的分支任务、通过API创建的增量任务都有唯一的任务ID。即[[查询任务列表](https://support.huaweicloud.com/api-codecheck/ShowTasksList.html)](tag:hws)[[查询任务列表](https://support.huaweicloud.com/intl/zh-cn/api-codecheck/ShowTasksList.html)](tag:hws_hk)[查询任务列表](tag:hcs,hcs_sm)接口响应中的id字段。 **取值范围：** 长度为[1~128]个字符。

        :param id: The id of this TaskBasicInfoV3.
        :type id: str
        """
        self._id = id

    @property
    def include_paths(self):
        r"""Gets the include_paths of this TaskBasicInfoV3.

        **参数解释：** 检查目录。 不配置检查目录时，检查代码仓中所有目录下的代码文件； 配置检查目录时，只检查配置目录中的代码文件。 **取值范围：** 长度为[1~200]个字符。

        :return: The include_paths of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._include_paths

    @include_paths.setter
    def include_paths(self, include_paths):
        r"""Sets the include_paths of this TaskBasicInfoV3.

        **参数解释：** 检查目录。 不配置检查目录时，检查代码仓中所有目录下的代码文件； 配置检查目录时，只检查配置目录中的代码文件。 **取值范围：** 长度为[1~200]个字符。

        :param include_paths: The include_paths of this TaskBasicInfoV3.
        :type include_paths: str
        """
        self._include_paths = include_paths

    @property
    def is_set_mr_webhook(self):
        r"""Gets the is_set_mr_webhook of this TaskBasicInfoV3.

        **参数解释：** 是否打开合并请求时触发。 **取值范围：** - true：打开。 - false：关闭。

        :return: The is_set_mr_webhook of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._is_set_mr_webhook

    @is_set_mr_webhook.setter
    def is_set_mr_webhook(self, is_set_mr_webhook):
        r"""Sets the is_set_mr_webhook of this TaskBasicInfoV3.

        **参数解释：** 是否打开合并请求时触发。 **取值范围：** - true：打开。 - false：关闭。

        :param is_set_mr_webhook: The is_set_mr_webhook of this TaskBasicInfoV3.
        :type is_set_mr_webhook: bool
        """
        self._is_set_mr_webhook = is_set_mr_webhook

    @property
    def is_set_push_webhook(self):
        r"""Gets the is_set_push_webhook of this TaskBasicInfoV3.

        **参数解释：** 是否打开代码提交时触发。 **取值范围：** - true：打开。 - false：关闭。

        :return: The is_set_push_webhook of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._is_set_push_webhook

    @is_set_push_webhook.setter
    def is_set_push_webhook(self, is_set_push_webhook):
        r"""Sets the is_set_push_webhook of this TaskBasicInfoV3.

        **参数解释：** 是否打开代码提交时触发。 **取值范围：** - true：打开。 - false：关闭。

        :param is_set_push_webhook: The is_set_push_webhook of this TaskBasicInfoV3.
        :type is_set_push_webhook: bool
        """
        self._is_set_push_webhook = is_set_push_webhook

    @property
    def is_set_webhook(self):
        r"""Gets the is_set_webhook of this TaskBasicInfoV3.

        **参数解释：** 是否打开合并请求时触发。 **取值范围：** - true：打开。 - false：关闭。

        :return: The is_set_webhook of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._is_set_webhook

    @is_set_webhook.setter
    def is_set_webhook(self, is_set_webhook):
        r"""Sets the is_set_webhook of this TaskBasicInfoV3.

        **参数解释：** 是否打开合并请求时触发。 **取值范围：** - true：打开。 - false：关闭。

        :param is_set_webhook: The is_set_webhook of this TaskBasicInfoV3.
        :type is_set_webhook: bool
        """
        self._is_set_webhook = is_set_webhook

    @property
    def is_template_task(self):
        r"""Gets the is_template_task of this TaskBasicInfoV3.

        **参数解释：** 是否是任务模板。 **取值范围：** - true：是任务模板。 - false：不是任务模板。

        :return: The is_template_task of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._is_template_task

    @is_template_task.setter
    def is_template_task(self, is_template_task):
        r"""Sets the is_template_task of this TaskBasicInfoV3.

        **参数解释：** 是否是任务模板。 **取值范围：** - true：是任务模板。 - false：不是任务模板。

        :param is_template_task: The is_template_task of this TaskBasicInfoV3.
        :type is_template_task: bool
        """
        self._is_template_task = is_template_task

    @property
    def job_id(self):
        r"""Gets the job_id of this TaskBasicInfoV3.

        **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 长度为[1~128]个字符。

        :return: The job_id of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this TaskBasicInfoV3.

        **参数解释：** 执行ID，来自代码检查执行任务接口的返回值，每次执行代码检查任务都有唯一的执行ID。 **取值范围：** 长度为[1~128]个字符。

        :param job_id: The job_id of this TaskBasicInfoV3.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_timeout(self):
        r"""Gets the job_timeout of this TaskBasicInfoV3.

        **参数解释:** 超时时间，以分钟为单位，格式固定为\"xxx min\"，其中xxx为整数，0 ＜ xxx ≤ 1200。 **取值范围：** 不涉及。

        :return: The job_timeout of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._job_timeout

    @job_timeout.setter
    def job_timeout(self, job_timeout):
        r"""Sets the job_timeout of this TaskBasicInfoV3.

        **参数解释:** 超时时间，以分钟为单位，格式固定为\"xxx min\"，其中xxx为整数，0 ＜ xxx ≤ 1200。 **取值范围：** 不涉及。

        :param job_timeout: The job_timeout of this TaskBasicInfoV3.
        :type job_timeout: str
        """
        self._job_timeout = job_timeout

    @property
    def last_finished_full_job_id(self):
        r"""Gets the last_finished_full_job_id of this TaskBasicInfoV3.

        **参数解释：** 最后一次检查完成的任务的执行ID。 **取值范围：** 长度为[1~128]个字符。

        :return: The last_finished_full_job_id of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._last_finished_full_job_id

    @last_finished_full_job_id.setter
    def last_finished_full_job_id(self, last_finished_full_job_id):
        r"""Sets the last_finished_full_job_id of this TaskBasicInfoV3.

        **参数解释：** 最后一次检查完成的任务的执行ID。 **取值范围：** 长度为[1~128]个字符。

        :param last_finished_full_job_id: The last_finished_full_job_id of this TaskBasicInfoV3.
        :type last_finished_full_job_id: str
        """
        self._last_finished_full_job_id = last_finished_full_job_id

    @property
    def last_job(self):
        r"""Gets the last_job of this TaskBasicInfoV3.

        :return: The last_job of this TaskBasicInfoV3.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.JobBasicInfoV3`
        """
        return self._last_job

    @last_job.setter
    def last_job(self, last_job):
        r"""Sets the last_job of this TaskBasicInfoV3.

        :param last_job: The last_job of this TaskBasicInfoV3.
        :type last_job: :class:`huaweicloudsdkcodeartscheck.v2.JobBasicInfoV3`
        """
        self._last_job = last_job

    @property
    def last_reviser(self):
        r"""Gets the last_reviser of this TaskBasicInfoV3.

        **参数解释：** 任务的最后修改人。 **取值范围：** 不涉及。

        :return: The last_reviser of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._last_reviser

    @last_reviser.setter
    def last_reviser(self, last_reviser):
        r"""Sets the last_reviser of this TaskBasicInfoV3.

        **参数解释：** 任务的最后修改人。 **取值范围：** 不涉及。

        :param last_reviser: The last_reviser of this TaskBasicInfoV3.
        :type last_reviser: str
        """
        self._last_reviser = last_reviser

    @property
    def last_update_time(self):
        r"""Gets the last_update_time of this TaskBasicInfoV3.

        **参数解释：** 任务的上一次更新时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :return: The last_update_time of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        r"""Sets the last_update_time of this TaskBasicInfoV3.

        **参数解释：** 任务的上一次更新时间，使用UTC时间，格式为yyyy-MM-ddTHH:mm:ssZ，例如\"2025-11-28T06:55:41Z\"。 **取值范围：** 不涉及。

        :param last_update_time: The last_update_time of this TaskBasicInfoV3.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def model_sets(self):
        r"""Gets the model_sets of this TaskBasicInfoV3.

        **参数解释：** 模型集列表，该字段一般返回空数组[]。

        :return: The model_sets of this TaskBasicInfoV3.
        :rtype: list[str]
        """
        return self._model_sets

    @model_sets.setter
    def model_sets(self, model_sets):
        r"""Sets the model_sets of this TaskBasicInfoV3.

        **参数解释：** 模型集列表，该字段一般返回空数组[]。

        :param model_sets: The model_sets of this TaskBasicInfoV3.
        :type model_sets: list[str]
        """
        self._model_sets = model_sets

    @property
    def mr_check_branch_strategy(self):
        r"""Gets the mr_check_branch_strategy of this TaskBasicInfoV3.

        **参数解释：** mr检查分支门禁策略。 **取值范围：** - 0：白名单。

        :return: The mr_check_branch_strategy of this TaskBasicInfoV3.
        :rtype: int
        """
        return self._mr_check_branch_strategy

    @mr_check_branch_strategy.setter
    def mr_check_branch_strategy(self, mr_check_branch_strategy):
        r"""Sets the mr_check_branch_strategy of this TaskBasicInfoV3.

        **参数解释：** mr检查分支门禁策略。 **取值范围：** - 0：白名单。

        :param mr_check_branch_strategy: The mr_check_branch_strategy of this TaskBasicInfoV3.
        :type mr_check_branch_strategy: int
        """
        self._mr_check_branch_strategy = mr_check_branch_strategy

    @property
    def name(self):
        r"""Gets the name of this TaskBasicInfoV3.

        **参数解释：** 代码检查任务名。 **取值范围：** 长度为[1~128]个字符。

        :return: The name of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskBasicInfoV3.

        **参数解释：** 代码检查任务名。 **取值范围：** 长度为[1~128]个字符。

        :param name: The name of this TaskBasicInfoV3.
        :type name: str
        """
        self._name = name

    @property
    def notification_config(self):
        r"""Gets the notification_config of this TaskBasicInfoV3.

        **参数解释：** 消息通知是否使用项目通知设置的配置项，格式为x,x,x,x,x,x，其中x的取值为0或者1。 x为0时代表使用任务的通知设置，x为1时代表使用项目通知设置。 从左到右依次为站内消息通知、邮件通知、企业微信、钉钉、飞书、通用webhook的消息通知配置。 **取值范围：** 格式为x,x,x,x,x,x，其中x的取值为0或者1。

        :return: The notification_config of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._notification_config

    @notification_config.setter
    def notification_config(self, notification_config):
        r"""Sets the notification_config of this TaskBasicInfoV3.

        **参数解释：** 消息通知是否使用项目通知设置的配置项，格式为x,x,x,x,x,x，其中x的取值为0或者1。 x为0时代表使用任务的通知设置，x为1时代表使用项目通知设置。 从左到右依次为站内消息通知、邮件通知、企业微信、钉钉、飞书、通用webhook的消息通知配置。 **取值范围：** 格式为x,x,x,x,x,x，其中x的取值为0或者1。

        :param notification_config: The notification_config of this TaskBasicInfoV3.
        :type notification_config: str
        """
        self._notification_config = notification_config

    @property
    def owner(self):
        r"""Gets the owner of this TaskBasicInfoV3.

        **参数解释：** 代码检查任务所有者。 **取值范围：** 长度为[1~255]个字符。

        :return: The owner of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this TaskBasicInfoV3.

        **参数解释：** 代码检查任务所有者。 **取值范围：** 长度为[1~255]个字符。

        :param owner: The owner of this TaskBasicInfoV3.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_id(self):
        r"""Gets the owner_id of this TaskBasicInfoV3.

        **参数解释：** 代码检查任务所有者的用户ID。 **取值范围：** 长度为[1~64]个字符。

        :return: The owner_id of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this TaskBasicInfoV3.

        **参数解释：** 代码检查任务所有者的用户ID。 **取值范围：** 长度为[1~64]个字符。

        :param owner_id: The owner_id of this TaskBasicInfoV3.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def project_id(self):
        r"""Gets the project_id of this TaskBasicInfoV3.

        **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **取值范围：** 长度为[1~32]个字符。

        :return: The project_id of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this TaskBasicInfoV3.

        **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **取值范围：** 长度为[1~32]个字符。

        :param project_id: The project_id of this TaskBasicInfoV3.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        r"""Gets the project_name of this TaskBasicInfoV3.

        **参数解释：** 项目名。 **取值范围：** 长度为[1~128]个字符。

        :return: The project_name of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this TaskBasicInfoV3.

        **参数解释：** 项目名。 **取值范围：** 长度为[1~128]个字符。

        :param project_name: The project_name of this TaskBasicInfoV3.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def region(self):
        r"""Gets the region of this TaskBasicInfoV3.

        **参数解释：** 地域，此字段固定为\"suzhou\"。 **取值范围：** suzhou。

        :return: The region of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this TaskBasicInfoV3.

        **参数解释：** 地域，此字段固定为\"suzhou\"。 **取值范围：** suzhou。

        :param region: The region of this TaskBasicInfoV3.
        :type region: str
        """
        self._region = region

    @property
    def repo_id(self):
        r"""Gets the repo_id of this TaskBasicInfoV3.

        **参数解释：** 代码仓地址对应的CodeartsRepo仓的RepoId。 **取值范围：** 长度为[1~128]个字符。

        :return: The repo_id of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._repo_id

    @repo_id.setter
    def repo_id(self, repo_id):
        r"""Sets the repo_id of this TaskBasicInfoV3.

        **参数解释：** 代码仓地址对应的CodeartsRepo仓的RepoId。 **取值范围：** 长度为[1~128]个字符。

        :param repo_id: The repo_id of this TaskBasicInfoV3.
        :type repo_id: str
        """
        self._repo_id = repo_id

    @property
    def repo_url(self):
        r"""Gets the repo_url of this TaskBasicInfoV3.

        **参数解释：** 代码仓地址。 **取值范围：** 长度为[1~1024]个字符。

        :return: The repo_url of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        r"""Sets the repo_url of this TaskBasicInfoV3.

        **参数解释：** 代码仓地址。 **取值范围：** 长度为[1~1024]个字符。

        :param repo_url: The repo_url of this TaskBasicInfoV3.
        :type repo_url: str
        """
        self._repo_url = repo_url

    @property
    def review_data(self):
        r"""Gets the review_data of this TaskBasicInfoV3.

        **参数解释：** 门禁配置，该字段一般返回空数组[]。

        :return: The review_data of this TaskBasicInfoV3.
        :rtype: list[str]
        """
        return self._review_data

    @review_data.setter
    def review_data(self, review_data):
        r"""Sets the review_data of this TaskBasicInfoV3.

        **参数解释：** 门禁配置，该字段一般返回空数组[]。

        :param review_data: The review_data of this TaskBasicInfoV3.
        :type review_data: list[str]
        """
        self._review_data = review_data

    @property
    def rule_sets(self):
        r"""Gets the rule_sets of this TaskBasicInfoV3.

        **参数解释：** 规则集配置，该字段一般返回空数组[]。

        :return: The rule_sets of this TaskBasicInfoV3.
        :rtype: list[str]
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets):
        r"""Sets the rule_sets of this TaskBasicInfoV3.

        **参数解释：** 规则集配置，该字段一般返回空数组[]。

        :param rule_sets: The rule_sets of this TaskBasicInfoV3.
        :type rule_sets: list[str]
        """
        self._rule_sets = rule_sets

    @property
    def source(self):
        r"""Gets the source of this TaskBasicInfoV3.

        **参数解释：** 任务来源，一般为\"customer\"。 **取值范围：** customer。

        :return: The source of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this TaskBasicInfoV3.

        **参数解释：** 任务来源，一般为\"customer\"。 **取值范围：** customer。

        :param source: The source of this TaskBasicInfoV3.
        :type source: str
        """
        self._source = source

    @property
    def task_group_id(self):
        r"""Gets the task_group_id of this TaskBasicInfoV3.

        **参数解释：** 任务分组的ID。 **取值范围：** 长度为[1~128]个字符。

        :return: The task_group_id of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._task_group_id

    @task_group_id.setter
    def task_group_id(self, task_group_id):
        r"""Sets the task_group_id of this TaskBasicInfoV3.

        **参数解释：** 任务分组的ID。 **取值范围：** 长度为[1~128]个字符。

        :param task_group_id: The task_group_id of this TaskBasicInfoV3.
        :type task_group_id: str
        """
        self._task_group_id = task_group_id

    @property
    def task_ids(self):
        r"""Gets the task_ids of this TaskBasicInfoV3.

        **参数解释：** 任务ID列表，该字段一般返回空数组[]。

        :return: The task_ids of this TaskBasicInfoV3.
        :rtype: list[str]
        """
        return self._task_ids

    @task_ids.setter
    def task_ids(self, task_ids):
        r"""Sets the task_ids of this TaskBasicInfoV3.

        **参数解释：** 任务ID列表，该字段一般返回空数组[]。

        :param task_ids: The task_ids of this TaskBasicInfoV3.
        :type task_ids: list[str]
        """
        self._task_ids = task_ids

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this TaskBasicInfoV3.

        **参数解释：** 任务所属的租户的租户ID，租户ID的值来源于IAM的租户ID。 **取值范围：** 长度为[1~32]个字符。

        :return: The tenant_id of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this TaskBasicInfoV3.

        **参数解释：** 任务所属的租户的租户ID，租户ID的值来源于IAM的租户ID。 **取值范围：** 长度为[1~32]个字符。

        :param tenant_id: The tenant_id of this TaskBasicInfoV3.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def use_cache(self):
        r"""Gets the use_cache of this TaskBasicInfoV3.

        **参数解释：** 查询任务信息是否使用缓存。 **取值范围：** - true：使用缓存。 - false：不使用缓存。

        :return: The use_cache of this TaskBasicInfoV3.
        :rtype: bool
        """
        return self._use_cache

    @use_cache.setter
    def use_cache(self, use_cache):
        r"""Sets the use_cache of this TaskBasicInfoV3.

        **参数解释：** 查询任务信息是否使用缓存。 **取值范围：** - true：使用缓存。 - false：不使用缓存。

        :param use_cache: The use_cache of this TaskBasicInfoV3.
        :type use_cache: bool
        """
        self._use_cache = use_cache

    @property
    def use_workspace_notification_config(self):
        r"""Gets the use_workspace_notification_config of this TaskBasicInfoV3.

        **参数解释：** 消息通知是否使用项目通知设置的配置项，来自notificationConfig的对应的二进制的取反转化成十进制。 例如，notificationConfig配置为1,1,0,1,0,0，则二进制为110100，取反为001011，转化为10进制时该值为11，最终useWorkspaceNotificationConfig的值为11。 **取值范围：** 0-31

        :return: The use_workspace_notification_config of this TaskBasicInfoV3.
        :rtype: int
        """
        return self._use_workspace_notification_config

    @use_workspace_notification_config.setter
    def use_workspace_notification_config(self, use_workspace_notification_config):
        r"""Sets the use_workspace_notification_config of this TaskBasicInfoV3.

        **参数解释：** 消息通知是否使用项目通知设置的配置项，来自notificationConfig的对应的二进制的取反转化成十进制。 例如，notificationConfig配置为1,1,0,1,0,0，则二进制为110100，取反为001011，转化为10进制时该值为11，最终useWorkspaceNotificationConfig的值为11。 **取值范围：** 0-31

        :param use_workspace_notification_config: The use_workspace_notification_config of this TaskBasicInfoV3.
        :type use_workspace_notification_config: int
        """
        self._use_workspace_notification_config = use_workspace_notification_config

    @property
    def version_update_delay_days(self):
        r"""Gets the version_update_delay_days of this TaskBasicInfoV3.

        **参数解释：** 版本升级缓冲期，该字段一般返回空数组[]。

        :return: The version_update_delay_days of this TaskBasicInfoV3.
        :rtype: list[str]
        """
        return self._version_update_delay_days

    @version_update_delay_days.setter
    def version_update_delay_days(self, version_update_delay_days):
        r"""Sets the version_update_delay_days of this TaskBasicInfoV3.

        **参数解释：** 版本升级缓冲期，该字段一般返回空数组[]。

        :param version_update_delay_days: The version_update_delay_days of this TaskBasicInfoV3.
        :type version_update_delay_days: list[str]
        """
        self._version_update_delay_days = version_update_delay_days

    @property
    def webhook_check_mode(self):
        r"""Gets the webhook_check_mode of this TaskBasicInfoV3.

        **参数解释：** webhook检查模式，一般为0，代表禁止来自其它代码仓的MR。 **取值范围：** 0

        :return: The webhook_check_mode of this TaskBasicInfoV3.
        :rtype: int
        """
        return self._webhook_check_mode

    @webhook_check_mode.setter
    def webhook_check_mode(self, webhook_check_mode):
        r"""Sets the webhook_check_mode of this TaskBasicInfoV3.

        **参数解释：** webhook检查模式，一般为0，代表禁止来自其它代码仓的MR。 **取值范围：** 0

        :param webhook_check_mode: The webhook_check_mode of this TaskBasicInfoV3.
        :type webhook_check_mode: int
        """
        self._webhook_check_mode = webhook_check_mode

    @property
    def zone(self):
        r"""Gets the zone of this TaskBasicInfoV3.

        **参数解释：** 区域，一般为green。 **取值范围：** green。

        :return: The zone of this TaskBasicInfoV3.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        r"""Sets the zone of this TaskBasicInfoV3.

        **参数解释：** 区域，一般为green。 **取值范围：** green。

        :param zone: The zone of this TaskBasicInfoV3.
        :type zone: str
        """
        self._zone = zone

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
        if not isinstance(other, TaskBasicInfoV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
