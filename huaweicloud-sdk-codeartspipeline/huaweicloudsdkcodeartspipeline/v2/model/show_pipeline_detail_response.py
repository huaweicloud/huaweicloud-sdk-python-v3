# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPipelineDetailResponse(SdkResponse):

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
        'name': 'str',
        'description': 'str',
        'manifest_version': 'str',
        'region': 'str',
        'domain_id': 'str',
        'project_id': 'str',
        'component_id': 'str',
        'is_publish': 'bool',
        'creator_id': 'str',
        'creator_name': 'str',
        'updater_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'is_collect': 'bool',
        'sources': 'list[PipelineSource]',
        'variables': 'list[PipelineVariable]',
        'schedules': 'list[PipelineSchedule]',
        'triggers': 'list[PipelineTrigger]',
        'group_id': 'str',
        'definition': 'str',
        'security_level': 'int',
        'origin_id': 'str',
        'disable_release_branch_management': 'bool',
        'deleted': 'bool',
        'banned': 'bool',
        'from_git_code': 'bool',
        'from_git_code_repo': 'bool',
        'git_code_repo_id': 'str',
        'yaml_definition': 'str',
        'pac_repo_relation': 'object',
        'yaml_content': 'str',
        'agency_name': 'str',
        'execution_plans': 'list[object]',
        'from_source': 'int',
        'project_name': 'str',
        'group_name': 'str',
        'concurrency_control': 'PipelineConcurrencyMgmt',
        'cancel_strategy': 'object',
        'tag_ids': 'list[str]',
        'variable_groups': 'list[str]',
        'security_level_code': 'str',
        'permissions': 'object',
        'subject_id': 'str',
        'detail_url': 'str',
        'modify_url': 'str',
        'tags': 'list[object]',
        'is_cr_model': 'bool',
        'archive_source': 'object',
        'yaml_repo_properties': 'object',
        'variable_group_ids': 'list[str]',
        'pac_source_alias': 'str',
        'pac_source_repo_https_endpoint': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'manifest_version': 'manifest_version',
        'region': 'region',
        'domain_id': 'domain_id',
        'project_id': 'project_id',
        'component_id': 'component_id',
        'is_publish': 'is_publish',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'updater_id': 'updater_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'is_collect': 'is_collect',
        'sources': 'sources',
        'variables': 'variables',
        'schedules': 'schedules',
        'triggers': 'triggers',
        'group_id': 'group_id',
        'definition': 'definition',
        'security_level': 'security_level',
        'origin_id': 'origin_id',
        'disable_release_branch_management': 'disable_release_branch_management',
        'deleted': 'deleted',
        'banned': 'banned',
        'from_git_code': 'from_git_code',
        'from_git_code_repo': 'from_git_code_repo',
        'git_code_repo_id': 'git_code_repo_id',
        'yaml_definition': 'yaml_definition',
        'pac_repo_relation': 'pac_repo_relation',
        'yaml_content': 'yaml_content',
        'agency_name': 'agency_name',
        'execution_plans': 'execution_plans',
        'from_source': 'from_source',
        'project_name': 'project_name',
        'group_name': 'group_name',
        'concurrency_control': 'concurrency_control',
        'cancel_strategy': 'cancel_strategy',
        'tag_ids': 'tag_ids',
        'variable_groups': 'variable_groups',
        'security_level_code': 'security_level_code',
        'permissions': 'permissions',
        'subject_id': 'subject_id',
        'detail_url': 'detail_url',
        'modify_url': 'modify_url',
        'tags': 'tags',
        'is_cr_model': 'is_cr_model',
        'archive_source': 'archive_source',
        'yaml_repo_properties': 'yaml_repo_properties',
        'variable_group_ids': 'variable_group_ids',
        'pac_source_alias': 'pac_source_alias',
        'pac_source_repo_https_endpoint': 'pac_source_repo_https_endpoint'
    }

    def __init__(self, id=None, name=None, description=None, manifest_version=None, region=None, domain_id=None, project_id=None, component_id=None, is_publish=None, creator_id=None, creator_name=None, updater_id=None, create_time=None, update_time=None, is_collect=None, sources=None, variables=None, schedules=None, triggers=None, group_id=None, definition=None, security_level=None, origin_id=None, disable_release_branch_management=None, deleted=None, banned=None, from_git_code=None, from_git_code_repo=None, git_code_repo_id=None, yaml_definition=None, pac_repo_relation=None, yaml_content=None, agency_name=None, execution_plans=None, from_source=None, project_name=None, group_name=None, concurrency_control=None, cancel_strategy=None, tag_ids=None, variable_groups=None, security_level_code=None, permissions=None, subject_id=None, detail_url=None, modify_url=None, tags=None, is_cr_model=None, archive_source=None, yaml_repo_properties=None, variable_group_ids=None, pac_source_alias=None, pac_source_repo_https_endpoint=None):
        r"""ShowPipelineDetailResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 流水线ID，可以通过[查询流水线列表](ListPipelines.xml)接口，其中pipelines.pipelineId即为流水线ID。 **取值范围**： 32位字符，仅由数字和字母组成。 
        :type id: str
        :param name: **参数解释**： 流水线名称。 **取值范围**： 仅包含中文、大小写英文字母、数字、&#39;-&#39;和&#39;_&#39;，且长度为[1,128]个字符。 
        :type name: str
        :param description: **参数解释**： 对流水线的补充描述。 **取值范围**： 不超过1024字符。 
        :type description: str
        :param manifest_version: **参数解释**： 流水线版本，默认为3.0。 **取值范围**： 不涉及。 
        :type manifest_version: str
        :param region: **参数解释**： 当前环境所属局点。 **取值范围**： 不涉及。 
        :type region: str
        :param domain_id: **参数解释**： 所属租户ID。 **取值范围**： 32位字符，仅由数字和字母组成。 
        :type domain_id: str
        :param project_id: **参数解释**： 项目ID。 **取值范围**： 32位字符，仅由数字和字母组成。 
        :type project_id: str
        :param component_id: **参数解释**： 所属微服务ID。可以通过[查询微服务列表](ListMicroservice.xml)接口获取，其中data.id即为微服务ID。 **取值范围**： 不涉及。 
        :type component_id: str
        :param is_publish: **参数解释**： 是否为变更流水线。 **取值范围**： - true：是变更流水线。 - false：不是变更流水线。 
        :type is_publish: bool
        :param creator_id: **参数解释**： 流水线创建人ID。 **取值范围**： 32位字符，仅由数字和字母组成。 
        :type creator_id: str
        :param creator_name: **参数解释**： 流水线创建人名称。 **取值范围**： 不涉及。 
        :type creator_name: str
        :param updater_id: **参数解释**： 流水线上次更新人ID。 **取值范围**： 32位字符，仅由数字和字母组成。 
        :type updater_id: str
        :param create_time: **参数解释**： 流水线创建时间。 **取值范围**： 不涉及。 
        :type create_time: int
        :param update_time: **参数解释**： 流水线更新时间。 **取值范围**： 不涉及。 
        :type update_time: int
        :param is_collect: **参数解释**： 流水线是否被当前用户收藏。 **取值范围**： - true：流水线已被收藏。 - false：流水线未被收藏。 
        :type is_collect: bool
        :param sources: **参数解释**： 流水线源列表。 **取值范围**： 不涉及。 
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSource`]
        :param variables: **参数解释**： 流水线自定义参数。 **取值范围**： 不涉及。 
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineVariable`]
        :param schedules: **参数解释**： 流水线定时任务设置。 **取值范围**： 不涉及。 
        :type schedules: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        :param triggers: **参数解释**： 流水线事件触发设置。 **取值范围**： 不涉及。 
        :type triggers: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        :param group_id: **参数解释**： 流水线所属分组ID。 **取值范围**： 不涉及。 
        :type group_id: str
        :param definition: **参数解释**： 流水线定义JSON。 **取值范围**： 不涉及。 
        :type definition: str
        :param security_level: **参数解释**： 流水线涉密等级。 **取值范围**： 不涉及。 
        :type security_level: int
        :param origin_id: **参数解释**： 复制流水线场景下，原流水线ID。 **取值范围**： 32位字符，仅由数字和字母组成。 
        :type origin_id: str
        :param disable_release_branch_management: **参数解释**： 是否禁用发布分支管理。 **取值范围**： - true：禁用发布分支管理。 - false：不禁用发布分支管理。 
        :type disable_release_branch_management: bool
        :param deleted: **参数解释**： 流水线是否已被删除。 **取值范围**： - true：已删除。 - false：未删除。 
        :type deleted: bool
        :param banned: **参数解释**： 流水线是否被禁用。 **取值范围**： - true：已禁用。 - false：未禁用。 
        :type banned: bool
        :param from_git_code: **参数解释**： 是否来自CodeHub代码仓。 **取值范围**： - true：来自CodeHub代码仓。 - false：非来自CodeHub代码仓。 
        :type from_git_code: bool
        :param from_git_code_repo: **参数解释**： 是否来自CodeHub代码仓库。 **取值范围**： - true：来自CodeHub代码仓库。 - false：非来自CodeHub代码仓库。 
        :type from_git_code_repo: bool
        :param git_code_repo_id: **参数解释**： CodeHub代码仓库ID。 **取值范围**： 不涉及。 
        :type git_code_repo_id: str
        :param yaml_definition: **参数解释**： YAML格式流水线定义。 **取值范围**： 不涉及。 
        :type yaml_definition: str
        :param pac_repo_relation: **参数解释**： PAC代码仓关联信息。 **取值范围**： 不涉及。 
        :type pac_repo_relation: object
        :param yaml_content: **参数解释**： YAML流水线文件内容。 **取值范围**： 不涉及。 
        :type yaml_content: str
        :param agency_name: **参数解释**： 委托名称。 **取值范围**： 不涉及。 
        :type agency_name: str
        :param execution_plans: **参数解释**： 执行计划列表。 **取值范围**： 不涉及。 
        :type execution_plans: list[object]
        :param from_source: **参数解释**： 流水线来源。 **取值范围**： - 0：默认。 - 1：普通模板创建。 - 2：老数据转换。 - 3：CloudInit凤凰商城触发模板创建。 - 4：CloudInit其他触发模板创建。 - 5：创建模板。 
        :type from_source: int
        :param project_name: **参数解释**： 项目名称。 **取值范围**： 不涉及。 
        :type project_name: str
        :param group_name: **参数解释**： 流水线所属分组名称。 **取值范围**： 不涉及。 
        :type group_name: str
        :param concurrency_control: 
        :type concurrency_control: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineConcurrencyMgmt`
        :param cancel_strategy: **参数解释**： 流水线取消运行策略。 **取值范围**： 不涉及。 
        :type cancel_strategy: object
        :param tag_ids: **参数解释**： 流水线标签ID列表。 **取值范围**： 不涉及。 
        :type tag_ids: list[str]
        :param variable_groups: **参数解释**： 流水线变量组列表。 **取值范围**： 不涉及。 
        :type variable_groups: list[str]
        :param security_level_code: **参数解释**： 流水线密级代码。 **取值范围**： 不涉及。 
        :type security_level_code: str
        :param permissions: **参数解释**： 流水线权限信息。 **取值范围**： 不涉及。 
        :type permissions: object
        :param subject_id: **参数解释**： 主体ID，即流水线ID。 **取值范围**： 32位字符，仅由数字和字母组成。 
        :type subject_id: str
        :param detail_url: **参数解释**： 流水线详情页URL。 **取值范围**： 不涉及。 
        :type detail_url: str
        :param modify_url: **参数解释**： 流水线编辑页URL。 **取值范围**： 不涉及。 
        :type modify_url: str
        :param tags: **参数解释**： 流水线标签列表。 **取值范围**： 不涉及。 
        :type tags: list[object]
        :param is_cr_model: **参数解释**： 是否为CR（变更）模型流水线。 **取值范围**： - true：是CR模型流水线。 - false：非CR模型流水线。 
        :type is_cr_model: bool
        :param archive_source: **参数解释**： PAC归档源信息。 **取值范围**： 不涉及。 
        :type archive_source: object
        :param yaml_repo_properties: **参数解释**： V2 YAML流水线的代码仓相关信息。 **取值范围**： 不涉及。 
        :type yaml_repo_properties: object
        :param variable_group_ids: **参数解释**： 关联的通用参数组ID列表。 **取值范围**： 不涉及。 
        :type variable_group_ids: list[str]
        :param pac_source_alias: **参数解释**： PAC代码源别名。 **取值范围**： 不涉及。 
        :type pac_source_alias: str
        :param pac_source_repo_https_endpoint: **参数解释**： PAC代码源CodeHub仓库的HTTPS端点ID。 **取值范围**： 不涉及。 
        :type pac_source_repo_https_endpoint: str
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._manifest_version = None
        self._region = None
        self._domain_id = None
        self._project_id = None
        self._component_id = None
        self._is_publish = None
        self._creator_id = None
        self._creator_name = None
        self._updater_id = None
        self._create_time = None
        self._update_time = None
        self._is_collect = None
        self._sources = None
        self._variables = None
        self._schedules = None
        self._triggers = None
        self._group_id = None
        self._definition = None
        self._security_level = None
        self._origin_id = None
        self._disable_release_branch_management = None
        self._deleted = None
        self._banned = None
        self._from_git_code = None
        self._from_git_code_repo = None
        self._git_code_repo_id = None
        self._yaml_definition = None
        self._pac_repo_relation = None
        self._yaml_content = None
        self._agency_name = None
        self._execution_plans = None
        self._from_source = None
        self._project_name = None
        self._group_name = None
        self._concurrency_control = None
        self._cancel_strategy = None
        self._tag_ids = None
        self._variable_groups = None
        self._security_level_code = None
        self._permissions = None
        self._subject_id = None
        self._detail_url = None
        self._modify_url = None
        self._tags = None
        self._is_cr_model = None
        self._archive_source = None
        self._yaml_repo_properties = None
        self._variable_group_ids = None
        self._pac_source_alias = None
        self._pac_source_repo_https_endpoint = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if manifest_version is not None:
            self.manifest_version = manifest_version
        if region is not None:
            self.region = region
        if domain_id is not None:
            self.domain_id = domain_id
        if project_id is not None:
            self.project_id = project_id
        if component_id is not None:
            self.component_id = component_id
        if is_publish is not None:
            self.is_publish = is_publish
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if updater_id is not None:
            self.updater_id = updater_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if is_collect is not None:
            self.is_collect = is_collect
        if sources is not None:
            self.sources = sources
        if variables is not None:
            self.variables = variables
        if schedules is not None:
            self.schedules = schedules
        if triggers is not None:
            self.triggers = triggers
        if group_id is not None:
            self.group_id = group_id
        if definition is not None:
            self.definition = definition
        if security_level is not None:
            self.security_level = security_level
        if origin_id is not None:
            self.origin_id = origin_id
        if disable_release_branch_management is not None:
            self.disable_release_branch_management = disable_release_branch_management
        if deleted is not None:
            self.deleted = deleted
        if banned is not None:
            self.banned = banned
        if from_git_code is not None:
            self.from_git_code = from_git_code
        if from_git_code_repo is not None:
            self.from_git_code_repo = from_git_code_repo
        if git_code_repo_id is not None:
            self.git_code_repo_id = git_code_repo_id
        if yaml_definition is not None:
            self.yaml_definition = yaml_definition
        if pac_repo_relation is not None:
            self.pac_repo_relation = pac_repo_relation
        if yaml_content is not None:
            self.yaml_content = yaml_content
        if agency_name is not None:
            self.agency_name = agency_name
        if execution_plans is not None:
            self.execution_plans = execution_plans
        if from_source is not None:
            self.from_source = from_source
        if project_name is not None:
            self.project_name = project_name
        if group_name is not None:
            self.group_name = group_name
        if concurrency_control is not None:
            self.concurrency_control = concurrency_control
        if cancel_strategy is not None:
            self.cancel_strategy = cancel_strategy
        if tag_ids is not None:
            self.tag_ids = tag_ids
        if variable_groups is not None:
            self.variable_groups = variable_groups
        if security_level_code is not None:
            self.security_level_code = security_level_code
        if permissions is not None:
            self.permissions = permissions
        if subject_id is not None:
            self.subject_id = subject_id
        if detail_url is not None:
            self.detail_url = detail_url
        if modify_url is not None:
            self.modify_url = modify_url
        if tags is not None:
            self.tags = tags
        if is_cr_model is not None:
            self.is_cr_model = is_cr_model
        if archive_source is not None:
            self.archive_source = archive_source
        if yaml_repo_properties is not None:
            self.yaml_repo_properties = yaml_repo_properties
        if variable_group_ids is not None:
            self.variable_group_ids = variable_group_ids
        if pac_source_alias is not None:
            self.pac_source_alias = pac_source_alias
        if pac_source_repo_https_endpoint is not None:
            self.pac_source_repo_https_endpoint = pac_source_repo_https_endpoint

    @property
    def id(self):
        r"""Gets the id of this ShowPipelineDetailResponse.

        **参数解释**： 流水线ID，可以通过[查询流水线列表](ListPipelines.xml)接口，其中pipelines.pipelineId即为流水线ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :return: The id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowPipelineDetailResponse.

        **参数解释**： 流水线ID，可以通过[查询流水线列表](ListPipelines.xml)接口，其中pipelines.pipelineId即为流水线ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :param id: The id of this ShowPipelineDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowPipelineDetailResponse.

        **参数解释**： 流水线名称。 **取值范围**： 仅包含中文、大小写英文字母、数字、'-'和'_'，且长度为[1,128]个字符。 

        :return: The name of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowPipelineDetailResponse.

        **参数解释**： 流水线名称。 **取值范围**： 仅包含中文、大小写英文字母、数字、'-'和'_'，且长度为[1,128]个字符。 

        :param name: The name of this ShowPipelineDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowPipelineDetailResponse.

        **参数解释**： 对流水线的补充描述。 **取值范围**： 不超过1024字符。 

        :return: The description of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowPipelineDetailResponse.

        **参数解释**： 对流水线的补充描述。 **取值范围**： 不超过1024字符。 

        :param description: The description of this ShowPipelineDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def manifest_version(self):
        r"""Gets the manifest_version of this ShowPipelineDetailResponse.

        **参数解释**： 流水线版本，默认为3.0。 **取值范围**： 不涉及。 

        :return: The manifest_version of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        r"""Sets the manifest_version of this ShowPipelineDetailResponse.

        **参数解释**： 流水线版本，默认为3.0。 **取值范围**： 不涉及。 

        :param manifest_version: The manifest_version of this ShowPipelineDetailResponse.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

    @property
    def region(self):
        r"""Gets the region of this ShowPipelineDetailResponse.

        **参数解释**： 当前环境所属局点。 **取值范围**： 不涉及。 

        :return: The region of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowPipelineDetailResponse.

        **参数解释**： 当前环境所属局点。 **取值范围**： 不涉及。 

        :param region: The region of this ShowPipelineDetailResponse.
        :type region: str
        """
        self._region = region

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowPipelineDetailResponse.

        **参数解释**： 所属租户ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :return: The domain_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowPipelineDetailResponse.

        **参数解释**： 所属租户ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :param domain_id: The domain_id of this ShowPipelineDetailResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowPipelineDetailResponse.

        **参数解释**： 项目ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :return: The project_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowPipelineDetailResponse.

        **参数解释**： 项目ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :param project_id: The project_id of this ShowPipelineDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def component_id(self):
        r"""Gets the component_id of this ShowPipelineDetailResponse.

        **参数解释**： 所属微服务ID。可以通过[查询微服务列表](ListMicroservice.xml)接口获取，其中data.id即为微服务ID。 **取值范围**： 不涉及。 

        :return: The component_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ShowPipelineDetailResponse.

        **参数解释**： 所属微服务ID。可以通过[查询微服务列表](ListMicroservice.xml)接口获取，其中data.id即为微服务ID。 **取值范围**： 不涉及。 

        :param component_id: The component_id of this ShowPipelineDetailResponse.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def is_publish(self):
        r"""Gets the is_publish of this ShowPipelineDetailResponse.

        **参数解释**： 是否为变更流水线。 **取值范围**： - true：是变更流水线。 - false：不是变更流水线。 

        :return: The is_publish of this ShowPipelineDetailResponse.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        r"""Sets the is_publish of this ShowPipelineDetailResponse.

        **参数解释**： 是否为变更流水线。 **取值范围**： - true：是变更流水线。 - false：不是变更流水线。 

        :param is_publish: The is_publish of this ShowPipelineDetailResponse.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ShowPipelineDetailResponse.

        **参数解释**： 流水线创建人ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :return: The creator_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ShowPipelineDetailResponse.

        **参数解释**： 流水线创建人ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :param creator_id: The creator_id of this ShowPipelineDetailResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this ShowPipelineDetailResponse.

        **参数解释**： 流水线创建人名称。 **取值范围**： 不涉及。 

        :return: The creator_name of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this ShowPipelineDetailResponse.

        **参数解释**： 流水线创建人名称。 **取值范围**： 不涉及。 

        :param creator_name: The creator_name of this ShowPipelineDetailResponse.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def updater_id(self):
        r"""Gets the updater_id of this ShowPipelineDetailResponse.

        **参数解释**： 流水线上次更新人ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :return: The updater_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        r"""Sets the updater_id of this ShowPipelineDetailResponse.

        **参数解释**： 流水线上次更新人ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :param updater_id: The updater_id of this ShowPipelineDetailResponse.
        :type updater_id: str
        """
        self._updater_id = updater_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowPipelineDetailResponse.

        **参数解释**： 流水线创建时间。 **取值范围**： 不涉及。 

        :return: The create_time of this ShowPipelineDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowPipelineDetailResponse.

        **参数解释**： 流水线创建时间。 **取值范围**： 不涉及。 

        :param create_time: The create_time of this ShowPipelineDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowPipelineDetailResponse.

        **参数解释**： 流水线更新时间。 **取值范围**： 不涉及。 

        :return: The update_time of this ShowPipelineDetailResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowPipelineDetailResponse.

        **参数解释**： 流水线更新时间。 **取值范围**： 不涉及。 

        :param update_time: The update_time of this ShowPipelineDetailResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def is_collect(self):
        r"""Gets the is_collect of this ShowPipelineDetailResponse.

        **参数解释**： 流水线是否被当前用户收藏。 **取值范围**： - true：流水线已被收藏。 - false：流水线未被收藏。 

        :return: The is_collect of this ShowPipelineDetailResponse.
        :rtype: bool
        """
        return self._is_collect

    @is_collect.setter
    def is_collect(self, is_collect):
        r"""Sets the is_collect of this ShowPipelineDetailResponse.

        **参数解释**： 流水线是否被当前用户收藏。 **取值范围**： - true：流水线已被收藏。 - false：流水线未被收藏。 

        :param is_collect: The is_collect of this ShowPipelineDetailResponse.
        :type is_collect: bool
        """
        self._is_collect = is_collect

    @property
    def sources(self):
        r"""Gets the sources of this ShowPipelineDetailResponse.

        **参数解释**： 流水线源列表。 **取值范围**： 不涉及。 

        :return: The sources of this ShowPipelineDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSource`]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        r"""Sets the sources of this ShowPipelineDetailResponse.

        **参数解释**： 流水线源列表。 **取值范围**： 不涉及。 

        :param sources: The sources of this ShowPipelineDetailResponse.
        :type sources: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSource`]
        """
        self._sources = sources

    @property
    def variables(self):
        r"""Gets the variables of this ShowPipelineDetailResponse.

        **参数解释**： 流水线自定义参数。 **取值范围**： 不涉及。 

        :return: The variables of this ShowPipelineDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineVariable`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this ShowPipelineDetailResponse.

        **参数解释**： 流水线自定义参数。 **取值范围**： 不涉及。 

        :param variables: The variables of this ShowPipelineDetailResponse.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineVariable`]
        """
        self._variables = variables

    @property
    def schedules(self):
        r"""Gets the schedules of this ShowPipelineDetailResponse.

        **参数解释**： 流水线定时任务设置。 **取值范围**： 不涉及。 

        :return: The schedules of this ShowPipelineDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        """
        return self._schedules

    @schedules.setter
    def schedules(self, schedules):
        r"""Sets the schedules of this ShowPipelineDetailResponse.

        **参数解释**： 流水线定时任务设置。 **取值范围**： 不涉及。 

        :param schedules: The schedules of this ShowPipelineDetailResponse.
        :type schedules: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineSchedule`]
        """
        self._schedules = schedules

    @property
    def triggers(self):
        r"""Gets the triggers of this ShowPipelineDetailResponse.

        **参数解释**： 流水线事件触发设置。 **取值范围**： 不涉及。 

        :return: The triggers of this ShowPipelineDetailResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        r"""Sets the triggers of this ShowPipelineDetailResponse.

        **参数解释**： 流水线事件触发设置。 **取值范围**： 不涉及。 

        :param triggers: The triggers of this ShowPipelineDetailResponse.
        :type triggers: list[:class:`huaweicloudsdkcodeartspipeline.v2.PipelineTrigger`]
        """
        self._triggers = triggers

    @property
    def group_id(self):
        r"""Gets the group_id of this ShowPipelineDetailResponse.

        **参数解释**： 流水线所属分组ID。 **取值范围**： 不涉及。 

        :return: The group_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ShowPipelineDetailResponse.

        **参数解释**： 流水线所属分组ID。 **取值范围**： 不涉及。 

        :param group_id: The group_id of this ShowPipelineDetailResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def definition(self):
        r"""Gets the definition of this ShowPipelineDetailResponse.

        **参数解释**： 流水线定义JSON。 **取值范围**： 不涉及。 

        :return: The definition of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        r"""Sets the definition of this ShowPipelineDetailResponse.

        **参数解释**： 流水线定义JSON。 **取值范围**： 不涉及。 

        :param definition: The definition of this ShowPipelineDetailResponse.
        :type definition: str
        """
        self._definition = definition

    @property
    def security_level(self):
        r"""Gets the security_level of this ShowPipelineDetailResponse.

        **参数解释**： 流水线涉密等级。 **取值范围**： 不涉及。 

        :return: The security_level of this ShowPipelineDetailResponse.
        :rtype: int
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this ShowPipelineDetailResponse.

        **参数解释**： 流水线涉密等级。 **取值范围**： 不涉及。 

        :param security_level: The security_level of this ShowPipelineDetailResponse.
        :type security_level: int
        """
        self._security_level = security_level

    @property
    def origin_id(self):
        r"""Gets the origin_id of this ShowPipelineDetailResponse.

        **参数解释**： 复制流水线场景下，原流水线ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :return: The origin_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._origin_id

    @origin_id.setter
    def origin_id(self, origin_id):
        r"""Sets the origin_id of this ShowPipelineDetailResponse.

        **参数解释**： 复制流水线场景下，原流水线ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :param origin_id: The origin_id of this ShowPipelineDetailResponse.
        :type origin_id: str
        """
        self._origin_id = origin_id

    @property
    def disable_release_branch_management(self):
        r"""Gets the disable_release_branch_management of this ShowPipelineDetailResponse.

        **参数解释**： 是否禁用发布分支管理。 **取值范围**： - true：禁用发布分支管理。 - false：不禁用发布分支管理。 

        :return: The disable_release_branch_management of this ShowPipelineDetailResponse.
        :rtype: bool
        """
        return self._disable_release_branch_management

    @disable_release_branch_management.setter
    def disable_release_branch_management(self, disable_release_branch_management):
        r"""Sets the disable_release_branch_management of this ShowPipelineDetailResponse.

        **参数解释**： 是否禁用发布分支管理。 **取值范围**： - true：禁用发布分支管理。 - false：不禁用发布分支管理。 

        :param disable_release_branch_management: The disable_release_branch_management of this ShowPipelineDetailResponse.
        :type disable_release_branch_management: bool
        """
        self._disable_release_branch_management = disable_release_branch_management

    @property
    def deleted(self):
        r"""Gets the deleted of this ShowPipelineDetailResponse.

        **参数解释**： 流水线是否已被删除。 **取值范围**： - true：已删除。 - false：未删除。 

        :return: The deleted of this ShowPipelineDetailResponse.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this ShowPipelineDetailResponse.

        **参数解释**： 流水线是否已被删除。 **取值范围**： - true：已删除。 - false：未删除。 

        :param deleted: The deleted of this ShowPipelineDetailResponse.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def banned(self):
        r"""Gets the banned of this ShowPipelineDetailResponse.

        **参数解释**： 流水线是否被禁用。 **取值范围**： - true：已禁用。 - false：未禁用。 

        :return: The banned of this ShowPipelineDetailResponse.
        :rtype: bool
        """
        return self._banned

    @banned.setter
    def banned(self, banned):
        r"""Sets the banned of this ShowPipelineDetailResponse.

        **参数解释**： 流水线是否被禁用。 **取值范围**： - true：已禁用。 - false：未禁用。 

        :param banned: The banned of this ShowPipelineDetailResponse.
        :type banned: bool
        """
        self._banned = banned

    @property
    def from_git_code(self):
        r"""Gets the from_git_code of this ShowPipelineDetailResponse.

        **参数解释**： 是否来自CodeHub代码仓。 **取值范围**： - true：来自CodeHub代码仓。 - false：非来自CodeHub代码仓。 

        :return: The from_git_code of this ShowPipelineDetailResponse.
        :rtype: bool
        """
        return self._from_git_code

    @from_git_code.setter
    def from_git_code(self, from_git_code):
        r"""Sets the from_git_code of this ShowPipelineDetailResponse.

        **参数解释**： 是否来自CodeHub代码仓。 **取值范围**： - true：来自CodeHub代码仓。 - false：非来自CodeHub代码仓。 

        :param from_git_code: The from_git_code of this ShowPipelineDetailResponse.
        :type from_git_code: bool
        """
        self._from_git_code = from_git_code

    @property
    def from_git_code_repo(self):
        r"""Gets the from_git_code_repo of this ShowPipelineDetailResponse.

        **参数解释**： 是否来自CodeHub代码仓库。 **取值范围**： - true：来自CodeHub代码仓库。 - false：非来自CodeHub代码仓库。 

        :return: The from_git_code_repo of this ShowPipelineDetailResponse.
        :rtype: bool
        """
        return self._from_git_code_repo

    @from_git_code_repo.setter
    def from_git_code_repo(self, from_git_code_repo):
        r"""Sets the from_git_code_repo of this ShowPipelineDetailResponse.

        **参数解释**： 是否来自CodeHub代码仓库。 **取值范围**： - true：来自CodeHub代码仓库。 - false：非来自CodeHub代码仓库。 

        :param from_git_code_repo: The from_git_code_repo of this ShowPipelineDetailResponse.
        :type from_git_code_repo: bool
        """
        self._from_git_code_repo = from_git_code_repo

    @property
    def git_code_repo_id(self):
        r"""Gets the git_code_repo_id of this ShowPipelineDetailResponse.

        **参数解释**： CodeHub代码仓库ID。 **取值范围**： 不涉及。 

        :return: The git_code_repo_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._git_code_repo_id

    @git_code_repo_id.setter
    def git_code_repo_id(self, git_code_repo_id):
        r"""Sets the git_code_repo_id of this ShowPipelineDetailResponse.

        **参数解释**： CodeHub代码仓库ID。 **取值范围**： 不涉及。 

        :param git_code_repo_id: The git_code_repo_id of this ShowPipelineDetailResponse.
        :type git_code_repo_id: str
        """
        self._git_code_repo_id = git_code_repo_id

    @property
    def yaml_definition(self):
        r"""Gets the yaml_definition of this ShowPipelineDetailResponse.

        **参数解释**： YAML格式流水线定义。 **取值范围**： 不涉及。 

        :return: The yaml_definition of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._yaml_definition

    @yaml_definition.setter
    def yaml_definition(self, yaml_definition):
        r"""Sets the yaml_definition of this ShowPipelineDetailResponse.

        **参数解释**： YAML格式流水线定义。 **取值范围**： 不涉及。 

        :param yaml_definition: The yaml_definition of this ShowPipelineDetailResponse.
        :type yaml_definition: str
        """
        self._yaml_definition = yaml_definition

    @property
    def pac_repo_relation(self):
        r"""Gets the pac_repo_relation of this ShowPipelineDetailResponse.

        **参数解释**： PAC代码仓关联信息。 **取值范围**： 不涉及。 

        :return: The pac_repo_relation of this ShowPipelineDetailResponse.
        :rtype: object
        """
        return self._pac_repo_relation

    @pac_repo_relation.setter
    def pac_repo_relation(self, pac_repo_relation):
        r"""Sets the pac_repo_relation of this ShowPipelineDetailResponse.

        **参数解释**： PAC代码仓关联信息。 **取值范围**： 不涉及。 

        :param pac_repo_relation: The pac_repo_relation of this ShowPipelineDetailResponse.
        :type pac_repo_relation: object
        """
        self._pac_repo_relation = pac_repo_relation

    @property
    def yaml_content(self):
        r"""Gets the yaml_content of this ShowPipelineDetailResponse.

        **参数解释**： YAML流水线文件内容。 **取值范围**： 不涉及。 

        :return: The yaml_content of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._yaml_content

    @yaml_content.setter
    def yaml_content(self, yaml_content):
        r"""Sets the yaml_content of this ShowPipelineDetailResponse.

        **参数解释**： YAML流水线文件内容。 **取值范围**： 不涉及。 

        :param yaml_content: The yaml_content of this ShowPipelineDetailResponse.
        :type yaml_content: str
        """
        self._yaml_content = yaml_content

    @property
    def agency_name(self):
        r"""Gets the agency_name of this ShowPipelineDetailResponse.

        **参数解释**： 委托名称。 **取值范围**： 不涉及。 

        :return: The agency_name of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this ShowPipelineDetailResponse.

        **参数解释**： 委托名称。 **取值范围**： 不涉及。 

        :param agency_name: The agency_name of this ShowPipelineDetailResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def execution_plans(self):
        r"""Gets the execution_plans of this ShowPipelineDetailResponse.

        **参数解释**： 执行计划列表。 **取值范围**： 不涉及。 

        :return: The execution_plans of this ShowPipelineDetailResponse.
        :rtype: list[object]
        """
        return self._execution_plans

    @execution_plans.setter
    def execution_plans(self, execution_plans):
        r"""Sets the execution_plans of this ShowPipelineDetailResponse.

        **参数解释**： 执行计划列表。 **取值范围**： 不涉及。 

        :param execution_plans: The execution_plans of this ShowPipelineDetailResponse.
        :type execution_plans: list[object]
        """
        self._execution_plans = execution_plans

    @property
    def from_source(self):
        r"""Gets the from_source of this ShowPipelineDetailResponse.

        **参数解释**： 流水线来源。 **取值范围**： - 0：默认。 - 1：普通模板创建。 - 2：老数据转换。 - 3：CloudInit凤凰商城触发模板创建。 - 4：CloudInit其他触发模板创建。 - 5：创建模板。 

        :return: The from_source of this ShowPipelineDetailResponse.
        :rtype: int
        """
        return self._from_source

    @from_source.setter
    def from_source(self, from_source):
        r"""Sets the from_source of this ShowPipelineDetailResponse.

        **参数解释**： 流水线来源。 **取值范围**： - 0：默认。 - 1：普通模板创建。 - 2：老数据转换。 - 3：CloudInit凤凰商城触发模板创建。 - 4：CloudInit其他触发模板创建。 - 5：创建模板。 

        :param from_source: The from_source of this ShowPipelineDetailResponse.
        :type from_source: int
        """
        self._from_source = from_source

    @property
    def project_name(self):
        r"""Gets the project_name of this ShowPipelineDetailResponse.

        **参数解释**： 项目名称。 **取值范围**： 不涉及。 

        :return: The project_name of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        r"""Sets the project_name of this ShowPipelineDetailResponse.

        **参数解释**： 项目名称。 **取值范围**： 不涉及。 

        :param project_name: The project_name of this ShowPipelineDetailResponse.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def group_name(self):
        r"""Gets the group_name of this ShowPipelineDetailResponse.

        **参数解释**： 流水线所属分组名称。 **取值范围**： 不涉及。 

        :return: The group_name of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ShowPipelineDetailResponse.

        **参数解释**： 流水线所属分组名称。 **取值范围**： 不涉及。 

        :param group_name: The group_name of this ShowPipelineDetailResponse.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def concurrency_control(self):
        r"""Gets the concurrency_control of this ShowPipelineDetailResponse.

        :return: The concurrency_control of this ShowPipelineDetailResponse.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineConcurrencyMgmt`
        """
        return self._concurrency_control

    @concurrency_control.setter
    def concurrency_control(self, concurrency_control):
        r"""Sets the concurrency_control of this ShowPipelineDetailResponse.

        :param concurrency_control: The concurrency_control of this ShowPipelineDetailResponse.
        :type concurrency_control: :class:`huaweicloudsdkcodeartspipeline.v2.PipelineConcurrencyMgmt`
        """
        self._concurrency_control = concurrency_control

    @property
    def cancel_strategy(self):
        r"""Gets the cancel_strategy of this ShowPipelineDetailResponse.

        **参数解释**： 流水线取消运行策略。 **取值范围**： 不涉及。 

        :return: The cancel_strategy of this ShowPipelineDetailResponse.
        :rtype: object
        """
        return self._cancel_strategy

    @cancel_strategy.setter
    def cancel_strategy(self, cancel_strategy):
        r"""Sets the cancel_strategy of this ShowPipelineDetailResponse.

        **参数解释**： 流水线取消运行策略。 **取值范围**： 不涉及。 

        :param cancel_strategy: The cancel_strategy of this ShowPipelineDetailResponse.
        :type cancel_strategy: object
        """
        self._cancel_strategy = cancel_strategy

    @property
    def tag_ids(self):
        r"""Gets the tag_ids of this ShowPipelineDetailResponse.

        **参数解释**： 流水线标签ID列表。 **取值范围**： 不涉及。 

        :return: The tag_ids of this ShowPipelineDetailResponse.
        :rtype: list[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        r"""Sets the tag_ids of this ShowPipelineDetailResponse.

        **参数解释**： 流水线标签ID列表。 **取值范围**： 不涉及。 

        :param tag_ids: The tag_ids of this ShowPipelineDetailResponse.
        :type tag_ids: list[str]
        """
        self._tag_ids = tag_ids

    @property
    def variable_groups(self):
        r"""Gets the variable_groups of this ShowPipelineDetailResponse.

        **参数解释**： 流水线变量组列表。 **取值范围**： 不涉及。 

        :return: The variable_groups of this ShowPipelineDetailResponse.
        :rtype: list[str]
        """
        return self._variable_groups

    @variable_groups.setter
    def variable_groups(self, variable_groups):
        r"""Sets the variable_groups of this ShowPipelineDetailResponse.

        **参数解释**： 流水线变量组列表。 **取值范围**： 不涉及。 

        :param variable_groups: The variable_groups of this ShowPipelineDetailResponse.
        :type variable_groups: list[str]
        """
        self._variable_groups = variable_groups

    @property
    def security_level_code(self):
        r"""Gets the security_level_code of this ShowPipelineDetailResponse.

        **参数解释**： 流水线密级代码。 **取值范围**： 不涉及。 

        :return: The security_level_code of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._security_level_code

    @security_level_code.setter
    def security_level_code(self, security_level_code):
        r"""Sets the security_level_code of this ShowPipelineDetailResponse.

        **参数解释**： 流水线密级代码。 **取值范围**： 不涉及。 

        :param security_level_code: The security_level_code of this ShowPipelineDetailResponse.
        :type security_level_code: str
        """
        self._security_level_code = security_level_code

    @property
    def permissions(self):
        r"""Gets the permissions of this ShowPipelineDetailResponse.

        **参数解释**： 流水线权限信息。 **取值范围**： 不涉及。 

        :return: The permissions of this ShowPipelineDetailResponse.
        :rtype: object
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this ShowPipelineDetailResponse.

        **参数解释**： 流水线权限信息。 **取值范围**： 不涉及。 

        :param permissions: The permissions of this ShowPipelineDetailResponse.
        :type permissions: object
        """
        self._permissions = permissions

    @property
    def subject_id(self):
        r"""Gets the subject_id of this ShowPipelineDetailResponse.

        **参数解释**： 主体ID，即流水线ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :return: The subject_id of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        r"""Sets the subject_id of this ShowPipelineDetailResponse.

        **参数解释**： 主体ID，即流水线ID。 **取值范围**： 32位字符，仅由数字和字母组成。 

        :param subject_id: The subject_id of this ShowPipelineDetailResponse.
        :type subject_id: str
        """
        self._subject_id = subject_id

    @property
    def detail_url(self):
        r"""Gets the detail_url of this ShowPipelineDetailResponse.

        **参数解释**： 流水线详情页URL。 **取值范围**： 不涉及。 

        :return: The detail_url of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        r"""Sets the detail_url of this ShowPipelineDetailResponse.

        **参数解释**： 流水线详情页URL。 **取值范围**： 不涉及。 

        :param detail_url: The detail_url of this ShowPipelineDetailResponse.
        :type detail_url: str
        """
        self._detail_url = detail_url

    @property
    def modify_url(self):
        r"""Gets the modify_url of this ShowPipelineDetailResponse.

        **参数解释**： 流水线编辑页URL。 **取值范围**： 不涉及。 

        :return: The modify_url of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._modify_url

    @modify_url.setter
    def modify_url(self, modify_url):
        r"""Sets the modify_url of this ShowPipelineDetailResponse.

        **参数解释**： 流水线编辑页URL。 **取值范围**： 不涉及。 

        :param modify_url: The modify_url of this ShowPipelineDetailResponse.
        :type modify_url: str
        """
        self._modify_url = modify_url

    @property
    def tags(self):
        r"""Gets the tags of this ShowPipelineDetailResponse.

        **参数解释**： 流水线标签列表。 **取值范围**： 不涉及。 

        :return: The tags of this ShowPipelineDetailResponse.
        :rtype: list[object]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowPipelineDetailResponse.

        **参数解释**： 流水线标签列表。 **取值范围**： 不涉及。 

        :param tags: The tags of this ShowPipelineDetailResponse.
        :type tags: list[object]
        """
        self._tags = tags

    @property
    def is_cr_model(self):
        r"""Gets the is_cr_model of this ShowPipelineDetailResponse.

        **参数解释**： 是否为CR（变更）模型流水线。 **取值范围**： - true：是CR模型流水线。 - false：非CR模型流水线。 

        :return: The is_cr_model of this ShowPipelineDetailResponse.
        :rtype: bool
        """
        return self._is_cr_model

    @is_cr_model.setter
    def is_cr_model(self, is_cr_model):
        r"""Sets the is_cr_model of this ShowPipelineDetailResponse.

        **参数解释**： 是否为CR（变更）模型流水线。 **取值范围**： - true：是CR模型流水线。 - false：非CR模型流水线。 

        :param is_cr_model: The is_cr_model of this ShowPipelineDetailResponse.
        :type is_cr_model: bool
        """
        self._is_cr_model = is_cr_model

    @property
    def archive_source(self):
        r"""Gets the archive_source of this ShowPipelineDetailResponse.

        **参数解释**： PAC归档源信息。 **取值范围**： 不涉及。 

        :return: The archive_source of this ShowPipelineDetailResponse.
        :rtype: object
        """
        return self._archive_source

    @archive_source.setter
    def archive_source(self, archive_source):
        r"""Sets the archive_source of this ShowPipelineDetailResponse.

        **参数解释**： PAC归档源信息。 **取值范围**： 不涉及。 

        :param archive_source: The archive_source of this ShowPipelineDetailResponse.
        :type archive_source: object
        """
        self._archive_source = archive_source

    @property
    def yaml_repo_properties(self):
        r"""Gets the yaml_repo_properties of this ShowPipelineDetailResponse.

        **参数解释**： V2 YAML流水线的代码仓相关信息。 **取值范围**： 不涉及。 

        :return: The yaml_repo_properties of this ShowPipelineDetailResponse.
        :rtype: object
        """
        return self._yaml_repo_properties

    @yaml_repo_properties.setter
    def yaml_repo_properties(self, yaml_repo_properties):
        r"""Sets the yaml_repo_properties of this ShowPipelineDetailResponse.

        **参数解释**： V2 YAML流水线的代码仓相关信息。 **取值范围**： 不涉及。 

        :param yaml_repo_properties: The yaml_repo_properties of this ShowPipelineDetailResponse.
        :type yaml_repo_properties: object
        """
        self._yaml_repo_properties = yaml_repo_properties

    @property
    def variable_group_ids(self):
        r"""Gets the variable_group_ids of this ShowPipelineDetailResponse.

        **参数解释**： 关联的通用参数组ID列表。 **取值范围**： 不涉及。 

        :return: The variable_group_ids of this ShowPipelineDetailResponse.
        :rtype: list[str]
        """
        return self._variable_group_ids

    @variable_group_ids.setter
    def variable_group_ids(self, variable_group_ids):
        r"""Sets the variable_group_ids of this ShowPipelineDetailResponse.

        **参数解释**： 关联的通用参数组ID列表。 **取值范围**： 不涉及。 

        :param variable_group_ids: The variable_group_ids of this ShowPipelineDetailResponse.
        :type variable_group_ids: list[str]
        """
        self._variable_group_ids = variable_group_ids

    @property
    def pac_source_alias(self):
        r"""Gets the pac_source_alias of this ShowPipelineDetailResponse.

        **参数解释**： PAC代码源别名。 **取值范围**： 不涉及。 

        :return: The pac_source_alias of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._pac_source_alias

    @pac_source_alias.setter
    def pac_source_alias(self, pac_source_alias):
        r"""Sets the pac_source_alias of this ShowPipelineDetailResponse.

        **参数解释**： PAC代码源别名。 **取值范围**： 不涉及。 

        :param pac_source_alias: The pac_source_alias of this ShowPipelineDetailResponse.
        :type pac_source_alias: str
        """
        self._pac_source_alias = pac_source_alias

    @property
    def pac_source_repo_https_endpoint(self):
        r"""Gets the pac_source_repo_https_endpoint of this ShowPipelineDetailResponse.

        **参数解释**： PAC代码源CodeHub仓库的HTTPS端点ID。 **取值范围**： 不涉及。 

        :return: The pac_source_repo_https_endpoint of this ShowPipelineDetailResponse.
        :rtype: str
        """
        return self._pac_source_repo_https_endpoint

    @pac_source_repo_https_endpoint.setter
    def pac_source_repo_https_endpoint(self, pac_source_repo_https_endpoint):
        r"""Sets the pac_source_repo_https_endpoint of this ShowPipelineDetailResponse.

        **参数解释**： PAC代码源CodeHub仓库的HTTPS端点ID。 **取值范围**： 不涉及。 

        :param pac_source_repo_https_endpoint: The pac_source_repo_https_endpoint of this ShowPipelineDetailResponse.
        :type pac_source_repo_https_endpoint: str
        """
        self._pac_source_repo_https_endpoint = pac_source_repo_https_endpoint

    def to_dict(self):
        import warnings
        warnings.warn("ShowPipelineDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowPipelineDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
