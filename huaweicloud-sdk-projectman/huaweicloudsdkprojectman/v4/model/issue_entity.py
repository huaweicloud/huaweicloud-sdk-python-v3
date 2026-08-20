# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueEntity:

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
        'title': 'str',
        'description': 'str',
        'type': 'str',
        'number': 'str',
        'category': 'str',
        'category_layer_id': 'str',
        'parent_id': 'str',
        'project_id': 'str',
        'status': 'str',
        'state': 'str',
        'assignee': 'UserEntity',
        'assigned_cc': 'list[UserEntity]',
        'created_by': 'UserEntity',
        'created_time': 'str',
        'modified_by': 'UserEntity',
        'modified_time': 'str',
        'plan_end_date': 'str',
        'close_time': 'str',
        'workload': 'str',
        'workload_sum': 'str',
        'tenant_id': 'str',
        'link': 'str',
        'suspended': 'bool',
        'status_modified_time': 'str',
        'labels': 'list[LabelEntity]',
        'custom_fields': 'list[FieldCodeValuePair]',
        'children': 'list[IssueEntity]',
        'path': 'str',
        'ir2feature': 'str',
        'need_break': 'str',
        'break_status': 'str',
        'baseline': 'str',
        'priority': 'str',
        'related_network_security': 'str',
        'collaboratives': 'str',
        'business_domain': 'str',
        'plan_pi': 'str',
        'plan_iteration': 'str',
        'change_status': 'str',
        'no_break_reason': 'str',
        'submitted_by': 'list[UserEntity]',
        'ir2rr': 'str',
        'feature_set': 'str',
        'expected_repair_date': 'str',
        'found_pi': 'str',
        'found_iteration': 'str',
        'reason_analysis': 'str',
        'repair_solution': 'str',
        'test_report': 'str',
        'sys_no_repair_reason': 'str',
        'sys_activation_reason': 'str',
        'sys_return_reason': 'str',
        'test_failures_times': 'int',
        'close_type': 'str',
        'plan_owner': 'UserEntity',
        'doing_owner': 'UserEntity',
        'delivered_owner': 'UserEntity',
        'checking_owner': 'UserEntity',
        'test_owner': 'UserEntity',
        'develop_owner': 'UserEntity',
        'processing_owner': 'UserEntity',
        'fixed_owner': 'UserEntity',
        'researchanddevelop_owner': 'UserEntity',
        'analyse_owner': 'UserEntity',
        'plan_start_date': 'str',
        'expect_delivery_time': 'str',
        'plan_test_end_date': 'str',
        'severity': 'str',
        'promised': 'str',
        'recipient': 'list[UserEntity]',
        'sys_no_develop_reason': 'str',
        'val_feature': 'str',
        'function_scene': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'type': 'type',
        'number': 'number',
        'category': 'category',
        'category_layer_id': 'category_layer_id',
        'parent_id': 'parent_id',
        'project_id': 'project_id',
        'status': 'status',
        'state': 'state',
        'assignee': 'assignee',
        'assigned_cc': 'assigned_cc',
        'created_by': 'created_by',
        'created_time': 'created_time',
        'modified_by': 'modified_by',
        'modified_time': 'modified_time',
        'plan_end_date': 'plan_end_date',
        'close_time': 'close_time',
        'workload': 'workload',
        'workload_sum': 'workload_sum',
        'tenant_id': 'tenant_id',
        'link': 'link',
        'suspended': 'suspended',
        'status_modified_time': 'status_modified_time',
        'labels': 'labels',
        'custom_fields': 'custom_fields',
        'children': 'children',
        'path': 'path',
        'ir2feature': 'ir2feature',
        'need_break': 'need_break',
        'break_status': 'break_status',
        'baseline': 'baseline',
        'priority': 'priority',
        'related_network_security': 'related_network_security',
        'collaboratives': 'collaboratives',
        'business_domain': 'business_domain',
        'plan_pi': 'plan_pi',
        'plan_iteration': 'plan_iteration',
        'change_status': 'change_status',
        'no_break_reason': 'no_break_reason',
        'submitted_by': 'submitted_by',
        'ir2rr': 'ir2rr',
        'feature_set': 'feature_set',
        'expected_repair_date': 'expected_repair_date',
        'found_pi': 'found_pi',
        'found_iteration': 'found_iteration',
        'reason_analysis': 'reason_analysis',
        'repair_solution': 'repair_solution',
        'test_report': 'test_report',
        'sys_no_repair_reason': 'sys_no_repair_reason',
        'sys_activation_reason': 'sys_activation_reason',
        'sys_return_reason': 'sys_return_reason',
        'test_failures_times': 'test_failures_times',
        'close_type': 'close_type',
        'plan_owner': 'plan_owner',
        'doing_owner': 'doing_owner',
        'delivered_owner': 'delivered_owner',
        'checking_owner': 'checking_owner',
        'test_owner': 'test_owner',
        'develop_owner': 'develop_owner',
        'processing_owner': 'processing_owner',
        'fixed_owner': 'fixed_owner',
        'researchanddevelop_owner': 'researchanddevelop_owner',
        'analyse_owner': 'analyse_owner',
        'plan_start_date': 'plan_start_date',
        'expect_delivery_time': 'expect_delivery_time',
        'plan_test_end_date': 'plan_test_end_date',
        'severity': 'severity',
        'promised': 'promised',
        'recipient': 'recipient',
        'sys_no_develop_reason': 'sys_no_develop_reason',
        'val_feature': 'val_feature',
        'function_scene': 'function_scene'
    }

    def __init__(self, id=None, title=None, description=None, type=None, number=None, category=None, category_layer_id=None, parent_id=None, project_id=None, status=None, state=None, assignee=None, assigned_cc=None, created_by=None, created_time=None, modified_by=None, modified_time=None, plan_end_date=None, close_time=None, workload=None, workload_sum=None, tenant_id=None, link=None, suspended=None, status_modified_time=None, labels=None, custom_fields=None, children=None, path=None, ir2feature=None, need_break=None, break_status=None, baseline=None, priority=None, related_network_security=None, collaboratives=None, business_domain=None, plan_pi=None, plan_iteration=None, change_status=None, no_break_reason=None, submitted_by=None, ir2rr=None, feature_set=None, expected_repair_date=None, found_pi=None, found_iteration=None, reason_analysis=None, repair_solution=None, test_report=None, sys_no_repair_reason=None, sys_activation_reason=None, sys_return_reason=None, test_failures_times=None, close_type=None, plan_owner=None, doing_owner=None, delivered_owner=None, checking_owner=None, test_owner=None, develop_owner=None, processing_owner=None, fixed_owner=None, researchanddevelop_owner=None, analyse_owner=None, plan_start_date=None, expect_delivery_time=None, plan_test_end_date=None, severity=None, promised=None, recipient=None, sys_no_develop_reason=None, val_feature=None, function_scene=None):
        r"""IssueEntity

        The model defined in huaweicloud sdk

        :param id: 需要更新的工作项ID，可通过查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。
        :type id: str
        :param title: 工作项标题，可通过查询树状工作项接口获取，响应消息体中的title字段的值就是工作项标题。
        :type title: str
        :param description: 工作项描述字段，可通过查询树状工作项接口获取，响应消息体中的description字段的值就是工作项描述字段。
        :type description: str
        :param type: 工作项大分类定义。工作项创建、编辑无此字段，仅作展示用，可通过查询树状工作项接口获取，响应消息体中的type字段的值就是工作项大分类定义。
        :type type: str
        :param number: 工作项编号，可通过查询树状工作项接口获取，响应消息体中的number字段的值就是工作项编号。
        :type number: str
        :param category: 工作项类型，可通过查询树状工作项接口获取，响应消息体中的category字段的值就是工作项类型。
        :type category: str
        :param category_layer_id: 工作项类型层级关系ID，此参数影响工作项的层级显示。通过获取模型树配置信息获取，根据参数中的category在响应消息体中category_layer_config中找到对应的category_code，和category_code同级的id就是工作项类型层级关系ID。
        :type category_layer_id: str
        :param parent_id: 父工作项ID，可通过查询树状工作项接口获取，响应消息体中的parent_id字段的值就是父工作项ID。
        :type parent_id: str
        :param project_id: 项目的32位uuid，项目唯一标识，通过查询IPD项目列表接口获取，响应消息体中的project_id字段的值就是项目ID。
        :type project_id: str
        :param status: 工作项状态code。可通过查询工作项状态接口获取，响应消息体中的code字段的值就是工作项工作项状态code。
        :type status: str
        :param state: 工作项的生命周期，可选值为“正在工作”，“作废”，可通过查询树状工作项接口获取，响应消息体中的state字段的值就是工作项的生命周期。
        :type state: str
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param assigned_cc: 工作项抄送人，支持多个抄送人。数组元素为UserEntity对象。
        :type assigned_cc: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param created_time: 工作项创建时间，unix时间戳，单位：毫秒。
        :type created_time: str
        :param modified_by: 
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param modified_time: 工作项最近更新时间，unix时间戳，单位：毫秒。
        :type modified_time: str
        :param plan_end_date: 工作项计划结束日期，unix时间戳，单位：毫秒。
        :type plan_end_date: str
        :param close_time: 工作项关闭时间，unix时间戳，单位：毫秒。
        :type close_time: str
        :param workload: 工作项计划工时。
        :type workload: str
        :param workload_sum: 工作项实际工时。
        :type workload_sum: str
        :param tenant_id: 工作项所属租户ID，可通过查询树状工作项接口获取，响应消息体中的tenant_id字段的值就是工作项所属租户ID。
        :type tenant_id: str
        :param link: 工作项关联项ID。
        :type link: str
        :param suspended: 工作项是否已挂起。
        :type suspended: bool
        :param status_modified_time: 工作项状态改变时间，可用于计算工作项在当前状态停留天数，unix时间戳，单位：毫秒。
        :type status_modified_time: str
        :param labels: 工作项标签。数组元素为LabelEntity对象。
        :type labels: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        :param custom_fields: 工作项自定义字段映射，用户添加的系统字段也在此列，格式为{\&quot;code\&quot;:\&quot;字段code\&quot;,\&quot;value\&quot;:\&quot;字段值\&quot;}。数组元素为FieldCodeValuePair对象。
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        :param children: 工作项的子工作项集合。数组元素为IssueEntity对象。
        :type children: list[:class:`huaweicloudsdkprojectman.v4.IssueEntity`]
        :param path: 子工作项的路径。
        :type path: str
        :param ir2feature: IR和SF的关联字段。
        :type ir2feature: str
        :param need_break: 工作项是否需要分解。
        :type need_break: str
        :param break_status: 分解状态。
        :type break_status: str
        :param baseline: 工作项基线状态。
        :type baseline: str
        :param priority: 工作项优先级，部分工作项有此字段。
        :type priority: str
        :param related_network_security: 是否涉及网络安全。
        :type related_network_security: str
        :param collaboratives: 研发需求协同信息，协同任务ID，可通过查询树状工作项接口获取，响应消息体中的collaboratives字段的值就是研发需求协同信息，协同任务ID。
        :type collaboratives: str
        :param business_domain: 领域字段。
        :type business_domain: str
        :param plan_pi: 工作项发布计划ID。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category&#x3D;PI的对象的id字段就是迭代计划的ID。
        :type plan_pi: str
        :param plan_iteration: 工作项完成的迭代计划ID，在Bug中为修复迭代计划ID。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category&#x3D;Iteration的对象的id字段就是迭代计划的ID。
        :type plan_iteration: str
        :param change_status: 工作项变更状态。
        :type change_status: str
        :param no_break_reason: 无需分解原因。
        :type no_break_reason: str
        :param submitted_by: 工作项提出人。数组元素为UserEntity对象。
        :type submitted_by: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        :param ir2rr: IR关联的RR ID，可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。
        :type ir2rr: str
        :param feature_set: 特性集ID，可以通过查询特性集接口获取，响应消息体中的id字段的值就是特性集ID。
        :type feature_set: str
        :param expected_repair_date: 期望修复时间。预设字段中，仅Bug有此字段，unix时间戳，单位：毫秒。
        :type expected_repair_date: str
        :param found_pi: 缺陷发现发布计划ID，预设字段中，仅Bug有此字段。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category&#x3D;PI的对象的id字段就是迭代计划的ID。
        :type found_pi: str
        :param found_iteration: 缺陷发现迭代计划ID，预设字段中，仅Bug有此字段。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category&#x3D;Iteration的对象的id字段就是迭代计划的ID。
        :type found_iteration: str
        :param reason_analysis: 分析原因。
        :type reason_analysis: str
        :param repair_solution: 修复方案。预设字段中，仅Bug有此字段。
        :type repair_solution: str
        :param test_report: 测试报告。预设字段中，仅Bug有此字段。
        :type test_report: str
        :param sys_no_repair_reason: 无需修复原因。预设字段中，仅Bug有此字段。
        :type sys_no_repair_reason: str
        :param sys_activation_reason: 激活原因。预设字段中，仅Bug有此字段。
        :type sys_activation_reason: str
        :param sys_return_reason: 退回原因。预设字段中，仅Bug有此字段。
        :type sys_return_reason: str
        :param test_failures_times: 回归不通过次数。预设字段中，仅Bug有此字段。
        :type test_failures_times: int
        :param close_type: 关闭类型。
        :type close_type: str
        :param plan_owner: 
        :type plan_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param doing_owner: 
        :type doing_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param delivered_owner: 
        :type delivered_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param checking_owner: 
        :type checking_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param test_owner: 
        :type test_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param develop_owner: 
        :type develop_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param processing_owner: 
        :type processing_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param fixed_owner: 
        :type fixed_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param researchanddevelop_owner: 
        :type researchanddevelop_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param analyse_owner: 
        :type analyse_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param plan_start_date: 计划开始时间。工作项的计划启动日期，用于项目进度管理和排期。
        :type plan_start_date: str
        :param expect_delivery_time: 期望完成时间。工作项的预期交付日期，用于跟踪工作项是否按期完成。
        :type expect_delivery_time: str
        :param plan_test_end_date: 计划测试结束时间。Bug类型工作项的计划测试完成日期，用于跟踪Bug修复后的测试进度。
        :type plan_test_end_date: str
        :param severity: 严重程度。Bug类型工作项的严重级别，用于评估Bug的影响范围和修复优先级。
        :type severity: str
        :param promised: 是否承诺。RR（原始需求）类型工作项的承诺状态标识，用于标记需求是否已承诺交付。
        :type promised: str
        :param recipient: 承接人。RR（原始需求）类型工作项的需求承接责任人，负责需求的分析和转化。
        :type recipient: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        :param sys_no_develop_reason: 无需研发原因。RR（原始需求）类型工作项不需要进行研发的原因说明。
        :type sys_no_develop_reason: str
        :param val_feature: 价值特性。SF/FE类型工作项对应的业务价值特性描述，用于关联业务价值和技术实现。
        :type val_feature: str
        :param function_scene: 功能场景。SF/FE类型工作项的功能应用场景描述，用于说明特性的使用场景和用户故事。
        :type function_scene: str
        """
        
        

        self._id = None
        self._title = None
        self._description = None
        self._type = None
        self._number = None
        self._category = None
        self._category_layer_id = None
        self._parent_id = None
        self._project_id = None
        self._status = None
        self._state = None
        self._assignee = None
        self._assigned_cc = None
        self._created_by = None
        self._created_time = None
        self._modified_by = None
        self._modified_time = None
        self._plan_end_date = None
        self._close_time = None
        self._workload = None
        self._workload_sum = None
        self._tenant_id = None
        self._link = None
        self._suspended = None
        self._status_modified_time = None
        self._labels = None
        self._custom_fields = None
        self._children = None
        self._path = None
        self._ir2feature = None
        self._need_break = None
        self._break_status = None
        self._baseline = None
        self._priority = None
        self._related_network_security = None
        self._collaboratives = None
        self._business_domain = None
        self._plan_pi = None
        self._plan_iteration = None
        self._change_status = None
        self._no_break_reason = None
        self._submitted_by = None
        self._ir2rr = None
        self._feature_set = None
        self._expected_repair_date = None
        self._found_pi = None
        self._found_iteration = None
        self._reason_analysis = None
        self._repair_solution = None
        self._test_report = None
        self._sys_no_repair_reason = None
        self._sys_activation_reason = None
        self._sys_return_reason = None
        self._test_failures_times = None
        self._close_type = None
        self._plan_owner = None
        self._doing_owner = None
        self._delivered_owner = None
        self._checking_owner = None
        self._test_owner = None
        self._develop_owner = None
        self._processing_owner = None
        self._fixed_owner = None
        self._researchanddevelop_owner = None
        self._analyse_owner = None
        self._plan_start_date = None
        self._expect_delivery_time = None
        self._plan_test_end_date = None
        self._severity = None
        self._promised = None
        self._recipient = None
        self._sys_no_develop_reason = None
        self._val_feature = None
        self._function_scene = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if number is not None:
            self.number = number
        self.category = category
        self.category_layer_id = category_layer_id
        if parent_id is not None:
            self.parent_id = parent_id
        if project_id is not None:
            self.project_id = project_id
        if status is not None:
            self.status = status
        if state is not None:
            self.state = state
        if assignee is not None:
            self.assignee = assignee
        if assigned_cc is not None:
            self.assigned_cc = assigned_cc
        if created_by is not None:
            self.created_by = created_by
        if created_time is not None:
            self.created_time = created_time
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_time is not None:
            self.modified_time = modified_time
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if close_time is not None:
            self.close_time = close_time
        if workload is not None:
            self.workload = workload
        if workload_sum is not None:
            self.workload_sum = workload_sum
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if link is not None:
            self.link = link
        if suspended is not None:
            self.suspended = suspended
        if status_modified_time is not None:
            self.status_modified_time = status_modified_time
        if labels is not None:
            self.labels = labels
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if children is not None:
            self.children = children
        if path is not None:
            self.path = path
        if ir2feature is not None:
            self.ir2feature = ir2feature
        if need_break is not None:
            self.need_break = need_break
        if break_status is not None:
            self.break_status = break_status
        if baseline is not None:
            self.baseline = baseline
        if priority is not None:
            self.priority = priority
        if related_network_security is not None:
            self.related_network_security = related_network_security
        if collaboratives is not None:
            self.collaboratives = collaboratives
        if business_domain is not None:
            self.business_domain = business_domain
        if plan_pi is not None:
            self.plan_pi = plan_pi
        if plan_iteration is not None:
            self.plan_iteration = plan_iteration
        if change_status is not None:
            self.change_status = change_status
        if no_break_reason is not None:
            self.no_break_reason = no_break_reason
        if submitted_by is not None:
            self.submitted_by = submitted_by
        if ir2rr is not None:
            self.ir2rr = ir2rr
        if feature_set is not None:
            self.feature_set = feature_set
        if expected_repair_date is not None:
            self.expected_repair_date = expected_repair_date
        if found_pi is not None:
            self.found_pi = found_pi
        if found_iteration is not None:
            self.found_iteration = found_iteration
        if reason_analysis is not None:
            self.reason_analysis = reason_analysis
        if repair_solution is not None:
            self.repair_solution = repair_solution
        if test_report is not None:
            self.test_report = test_report
        if sys_no_repair_reason is not None:
            self.sys_no_repair_reason = sys_no_repair_reason
        if sys_activation_reason is not None:
            self.sys_activation_reason = sys_activation_reason
        if sys_return_reason is not None:
            self.sys_return_reason = sys_return_reason
        if test_failures_times is not None:
            self.test_failures_times = test_failures_times
        if close_type is not None:
            self.close_type = close_type
        if plan_owner is not None:
            self.plan_owner = plan_owner
        if doing_owner is not None:
            self.doing_owner = doing_owner
        if delivered_owner is not None:
            self.delivered_owner = delivered_owner
        if checking_owner is not None:
            self.checking_owner = checking_owner
        if test_owner is not None:
            self.test_owner = test_owner
        if develop_owner is not None:
            self.develop_owner = develop_owner
        if processing_owner is not None:
            self.processing_owner = processing_owner
        if fixed_owner is not None:
            self.fixed_owner = fixed_owner
        if researchanddevelop_owner is not None:
            self.researchanddevelop_owner = researchanddevelop_owner
        if analyse_owner is not None:
            self.analyse_owner = analyse_owner
        if plan_start_date is not None:
            self.plan_start_date = plan_start_date
        if expect_delivery_time is not None:
            self.expect_delivery_time = expect_delivery_time
        if plan_test_end_date is not None:
            self.plan_test_end_date = plan_test_end_date
        if severity is not None:
            self.severity = severity
        if promised is not None:
            self.promised = promised
        if recipient is not None:
            self.recipient = recipient
        if sys_no_develop_reason is not None:
            self.sys_no_develop_reason = sys_no_develop_reason
        if val_feature is not None:
            self.val_feature = val_feature
        if function_scene is not None:
            self.function_scene = function_scene

    @property
    def id(self):
        r"""Gets the id of this IssueEntity.

        需要更新的工作项ID，可通过查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :return: The id of this IssueEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueEntity.

        需要更新的工作项ID，可通过查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :param id: The id of this IssueEntity.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this IssueEntity.

        工作项标题，可通过查询树状工作项接口获取，响应消息体中的title字段的值就是工作项标题。

        :return: The title of this IssueEntity.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this IssueEntity.

        工作项标题，可通过查询树状工作项接口获取，响应消息体中的title字段的值就是工作项标题。

        :param title: The title of this IssueEntity.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this IssueEntity.

        工作项描述字段，可通过查询树状工作项接口获取，响应消息体中的description字段的值就是工作项描述字段。

        :return: The description of this IssueEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IssueEntity.

        工作项描述字段，可通过查询树状工作项接口获取，响应消息体中的description字段的值就是工作项描述字段。

        :param description: The description of this IssueEntity.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this IssueEntity.

        工作项大分类定义。工作项创建、编辑无此字段，仅作展示用，可通过查询树状工作项接口获取，响应消息体中的type字段的值就是工作项大分类定义。

        :return: The type of this IssueEntity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IssueEntity.

        工作项大分类定义。工作项创建、编辑无此字段，仅作展示用，可通过查询树状工作项接口获取，响应消息体中的type字段的值就是工作项大分类定义。

        :param type: The type of this IssueEntity.
        :type type: str
        """
        self._type = type

    @property
    def number(self):
        r"""Gets the number of this IssueEntity.

        工作项编号，可通过查询树状工作项接口获取，响应消息体中的number字段的值就是工作项编号。

        :return: The number of this IssueEntity.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this IssueEntity.

        工作项编号，可通过查询树状工作项接口获取，响应消息体中的number字段的值就是工作项编号。

        :param number: The number of this IssueEntity.
        :type number: str
        """
        self._number = number

    @property
    def category(self):
        r"""Gets the category of this IssueEntity.

        工作项类型，可通过查询树状工作项接口获取，响应消息体中的category字段的值就是工作项类型。

        :return: The category of this IssueEntity.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this IssueEntity.

        工作项类型，可通过查询树状工作项接口获取，响应消息体中的category字段的值就是工作项类型。

        :param category: The category of this IssueEntity.
        :type category: str
        """
        self._category = category

    @property
    def category_layer_id(self):
        r"""Gets the category_layer_id of this IssueEntity.

        工作项类型层级关系ID，此参数影响工作项的层级显示。通过获取模型树配置信息获取，根据参数中的category在响应消息体中category_layer_config中找到对应的category_code，和category_code同级的id就是工作项类型层级关系ID。

        :return: The category_layer_id of this IssueEntity.
        :rtype: str
        """
        return self._category_layer_id

    @category_layer_id.setter
    def category_layer_id(self, category_layer_id):
        r"""Sets the category_layer_id of this IssueEntity.

        工作项类型层级关系ID，此参数影响工作项的层级显示。通过获取模型树配置信息获取，根据参数中的category在响应消息体中category_layer_config中找到对应的category_code，和category_code同级的id就是工作项类型层级关系ID。

        :param category_layer_id: The category_layer_id of this IssueEntity.
        :type category_layer_id: str
        """
        self._category_layer_id = category_layer_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this IssueEntity.

        父工作项ID，可通过查询树状工作项接口获取，响应消息体中的parent_id字段的值就是父工作项ID。

        :return: The parent_id of this IssueEntity.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this IssueEntity.

        父工作项ID，可通过查询树状工作项接口获取，响应消息体中的parent_id字段的值就是父工作项ID。

        :param parent_id: The parent_id of this IssueEntity.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def project_id(self):
        r"""Gets the project_id of this IssueEntity.

        项目的32位uuid，项目唯一标识，通过查询IPD项目列表接口获取，响应消息体中的project_id字段的值就是项目ID。

        :return: The project_id of this IssueEntity.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this IssueEntity.

        项目的32位uuid，项目唯一标识，通过查询IPD项目列表接口获取，响应消息体中的project_id字段的值就是项目ID。

        :param project_id: The project_id of this IssueEntity.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this IssueEntity.

        工作项状态code。可通过查询工作项状态接口获取，响应消息体中的code字段的值就是工作项工作项状态code。

        :return: The status of this IssueEntity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IssueEntity.

        工作项状态code。可通过查询工作项状态接口获取，响应消息体中的code字段的值就是工作项工作项状态code。

        :param status: The status of this IssueEntity.
        :type status: str
        """
        self._status = status

    @property
    def state(self):
        r"""Gets the state of this IssueEntity.

        工作项的生命周期，可选值为“正在工作”，“作废”，可通过查询树状工作项接口获取，响应消息体中的state字段的值就是工作项的生命周期。

        :return: The state of this IssueEntity.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this IssueEntity.

        工作项的生命周期，可选值为“正在工作”，“作废”，可通过查询树状工作项接口获取，响应消息体中的state字段的值就是工作项的生命周期。

        :param state: The state of this IssueEntity.
        :type state: str
        """
        self._state = state

    @property
    def assignee(self):
        r"""Gets the assignee of this IssueEntity.

        :return: The assignee of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this IssueEntity.

        :param assignee: The assignee of this IssueEntity.
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._assignee = assignee

    @property
    def assigned_cc(self):
        r"""Gets the assigned_cc of this IssueEntity.

        工作项抄送人，支持多个抄送人。数组元素为UserEntity对象。

        :return: The assigned_cc of this IssueEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        return self._assigned_cc

    @assigned_cc.setter
    def assigned_cc(self, assigned_cc):
        r"""Sets the assigned_cc of this IssueEntity.

        工作项抄送人，支持多个抄送人。数组元素为UserEntity对象。

        :param assigned_cc: The assigned_cc of this IssueEntity.
        :type assigned_cc: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        self._assigned_cc = assigned_cc

    @property
    def created_by(self):
        r"""Gets the created_by of this IssueEntity.

        :return: The created_by of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this IssueEntity.

        :param created_by: The created_by of this IssueEntity.
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._created_by = created_by

    @property
    def created_time(self):
        r"""Gets the created_time of this IssueEntity.

        工作项创建时间，unix时间戳，单位：毫秒。

        :return: The created_time of this IssueEntity.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this IssueEntity.

        工作项创建时间，unix时间戳，单位：毫秒。

        :param created_time: The created_time of this IssueEntity.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_by(self):
        r"""Gets the modified_by of this IssueEntity.

        :return: The modified_by of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this IssueEntity.

        :param modified_by: The modified_by of this IssueEntity.
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._modified_by = modified_by

    @property
    def modified_time(self):
        r"""Gets the modified_time of this IssueEntity.

        工作项最近更新时间，unix时间戳，单位：毫秒。

        :return: The modified_time of this IssueEntity.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this IssueEntity.

        工作项最近更新时间，unix时间戳，单位：毫秒。

        :param modified_time: The modified_time of this IssueEntity.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this IssueEntity.

        工作项计划结束日期，unix时间戳，单位：毫秒。

        :return: The plan_end_date of this IssueEntity.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this IssueEntity.

        工作项计划结束日期，unix时间戳，单位：毫秒。

        :param plan_end_date: The plan_end_date of this IssueEntity.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def close_time(self):
        r"""Gets the close_time of this IssueEntity.

        工作项关闭时间，unix时间戳，单位：毫秒。

        :return: The close_time of this IssueEntity.
        :rtype: str
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        r"""Sets the close_time of this IssueEntity.

        工作项关闭时间，unix时间戳，单位：毫秒。

        :param close_time: The close_time of this IssueEntity.
        :type close_time: str
        """
        self._close_time = close_time

    @property
    def workload(self):
        r"""Gets the workload of this IssueEntity.

        工作项计划工时。

        :return: The workload of this IssueEntity.
        :rtype: str
        """
        return self._workload

    @workload.setter
    def workload(self, workload):
        r"""Sets the workload of this IssueEntity.

        工作项计划工时。

        :param workload: The workload of this IssueEntity.
        :type workload: str
        """
        self._workload = workload

    @property
    def workload_sum(self):
        r"""Gets the workload_sum of this IssueEntity.

        工作项实际工时。

        :return: The workload_sum of this IssueEntity.
        :rtype: str
        """
        return self._workload_sum

    @workload_sum.setter
    def workload_sum(self, workload_sum):
        r"""Sets the workload_sum of this IssueEntity.

        工作项实际工时。

        :param workload_sum: The workload_sum of this IssueEntity.
        :type workload_sum: str
        """
        self._workload_sum = workload_sum

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this IssueEntity.

        工作项所属租户ID，可通过查询树状工作项接口获取，响应消息体中的tenant_id字段的值就是工作项所属租户ID。

        :return: The tenant_id of this IssueEntity.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this IssueEntity.

        工作项所属租户ID，可通过查询树状工作项接口获取，响应消息体中的tenant_id字段的值就是工作项所属租户ID。

        :param tenant_id: The tenant_id of this IssueEntity.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def link(self):
        r"""Gets the link of this IssueEntity.

        工作项关联项ID。

        :return: The link of this IssueEntity.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this IssueEntity.

        工作项关联项ID。

        :param link: The link of this IssueEntity.
        :type link: str
        """
        self._link = link

    @property
    def suspended(self):
        r"""Gets the suspended of this IssueEntity.

        工作项是否已挂起。

        :return: The suspended of this IssueEntity.
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        r"""Sets the suspended of this IssueEntity.

        工作项是否已挂起。

        :param suspended: The suspended of this IssueEntity.
        :type suspended: bool
        """
        self._suspended = suspended

    @property
    def status_modified_time(self):
        r"""Gets the status_modified_time of this IssueEntity.

        工作项状态改变时间，可用于计算工作项在当前状态停留天数，unix时间戳，单位：毫秒。

        :return: The status_modified_time of this IssueEntity.
        :rtype: str
        """
        return self._status_modified_time

    @status_modified_time.setter
    def status_modified_time(self, status_modified_time):
        r"""Sets the status_modified_time of this IssueEntity.

        工作项状态改变时间，可用于计算工作项在当前状态停留天数，unix时间戳，单位：毫秒。

        :param status_modified_time: The status_modified_time of this IssueEntity.
        :type status_modified_time: str
        """
        self._status_modified_time = status_modified_time

    @property
    def labels(self):
        r"""Gets the labels of this IssueEntity.

        工作项标签。数组元素为LabelEntity对象。

        :return: The labels of this IssueEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this IssueEntity.

        工作项标签。数组元素为LabelEntity对象。

        :param labels: The labels of this IssueEntity.
        :type labels: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        """
        self._labels = labels

    @property
    def custom_fields(self):
        r"""Gets the custom_fields of this IssueEntity.

        工作项自定义字段映射，用户添加的系统字段也在此列，格式为{\"code\":\"字段code\",\"value\":\"字段值\"}。数组元素为FieldCodeValuePair对象。

        :return: The custom_fields of this IssueEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        r"""Sets the custom_fields of this IssueEntity.

        工作项自定义字段映射，用户添加的系统字段也在此列，格式为{\"code\":\"字段code\",\"value\":\"字段值\"}。数组元素为FieldCodeValuePair对象。

        :param custom_fields: The custom_fields of this IssueEntity.
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        """
        self._custom_fields = custom_fields

    @property
    def children(self):
        r"""Gets the children of this IssueEntity.

        工作项的子工作项集合。数组元素为IssueEntity对象。

        :return: The children of this IssueEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueEntity`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this IssueEntity.

        工作项的子工作项集合。数组元素为IssueEntity对象。

        :param children: The children of this IssueEntity.
        :type children: list[:class:`huaweicloudsdkprojectman.v4.IssueEntity`]
        """
        self._children = children

    @property
    def path(self):
        r"""Gets the path of this IssueEntity.

        子工作项的路径。

        :return: The path of this IssueEntity.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this IssueEntity.

        子工作项的路径。

        :param path: The path of this IssueEntity.
        :type path: str
        """
        self._path = path

    @property
    def ir2feature(self):
        r"""Gets the ir2feature of this IssueEntity.

        IR和SF的关联字段。

        :return: The ir2feature of this IssueEntity.
        :rtype: str
        """
        return self._ir2feature

    @ir2feature.setter
    def ir2feature(self, ir2feature):
        r"""Sets the ir2feature of this IssueEntity.

        IR和SF的关联字段。

        :param ir2feature: The ir2feature of this IssueEntity.
        :type ir2feature: str
        """
        self._ir2feature = ir2feature

    @property
    def need_break(self):
        r"""Gets the need_break of this IssueEntity.

        工作项是否需要分解。

        :return: The need_break of this IssueEntity.
        :rtype: str
        """
        return self._need_break

    @need_break.setter
    def need_break(self, need_break):
        r"""Sets the need_break of this IssueEntity.

        工作项是否需要分解。

        :param need_break: The need_break of this IssueEntity.
        :type need_break: str
        """
        self._need_break = need_break

    @property
    def break_status(self):
        r"""Gets the break_status of this IssueEntity.

        分解状态。

        :return: The break_status of this IssueEntity.
        :rtype: str
        """
        return self._break_status

    @break_status.setter
    def break_status(self, break_status):
        r"""Sets the break_status of this IssueEntity.

        分解状态。

        :param break_status: The break_status of this IssueEntity.
        :type break_status: str
        """
        self._break_status = break_status

    @property
    def baseline(self):
        r"""Gets the baseline of this IssueEntity.

        工作项基线状态。

        :return: The baseline of this IssueEntity.
        :rtype: str
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this IssueEntity.

        工作项基线状态。

        :param baseline: The baseline of this IssueEntity.
        :type baseline: str
        """
        self._baseline = baseline

    @property
    def priority(self):
        r"""Gets the priority of this IssueEntity.

        工作项优先级，部分工作项有此字段。

        :return: The priority of this IssueEntity.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this IssueEntity.

        工作项优先级，部分工作项有此字段。

        :param priority: The priority of this IssueEntity.
        :type priority: str
        """
        self._priority = priority

    @property
    def related_network_security(self):
        r"""Gets the related_network_security of this IssueEntity.

        是否涉及网络安全。

        :return: The related_network_security of this IssueEntity.
        :rtype: str
        """
        return self._related_network_security

    @related_network_security.setter
    def related_network_security(self, related_network_security):
        r"""Sets the related_network_security of this IssueEntity.

        是否涉及网络安全。

        :param related_network_security: The related_network_security of this IssueEntity.
        :type related_network_security: str
        """
        self._related_network_security = related_network_security

    @property
    def collaboratives(self):
        r"""Gets the collaboratives of this IssueEntity.

        研发需求协同信息，协同任务ID，可通过查询树状工作项接口获取，响应消息体中的collaboratives字段的值就是研发需求协同信息，协同任务ID。

        :return: The collaboratives of this IssueEntity.
        :rtype: str
        """
        return self._collaboratives

    @collaboratives.setter
    def collaboratives(self, collaboratives):
        r"""Sets the collaboratives of this IssueEntity.

        研发需求协同信息，协同任务ID，可通过查询树状工作项接口获取，响应消息体中的collaboratives字段的值就是研发需求协同信息，协同任务ID。

        :param collaboratives: The collaboratives of this IssueEntity.
        :type collaboratives: str
        """
        self._collaboratives = collaboratives

    @property
    def business_domain(self):
        r"""Gets the business_domain of this IssueEntity.

        领域字段。

        :return: The business_domain of this IssueEntity.
        :rtype: str
        """
        return self._business_domain

    @business_domain.setter
    def business_domain(self, business_domain):
        r"""Sets the business_domain of this IssueEntity.

        领域字段。

        :param business_domain: The business_domain of this IssueEntity.
        :type business_domain: str
        """
        self._business_domain = business_domain

    @property
    def plan_pi(self):
        r"""Gets the plan_pi of this IssueEntity.

        工作项发布计划ID。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category=PI的对象的id字段就是迭代计划的ID。

        :return: The plan_pi of this IssueEntity.
        :rtype: str
        """
        return self._plan_pi

    @plan_pi.setter
    def plan_pi(self, plan_pi):
        r"""Sets the plan_pi of this IssueEntity.

        工作项发布计划ID。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category=PI的对象的id字段就是迭代计划的ID。

        :param plan_pi: The plan_pi of this IssueEntity.
        :type plan_pi: str
        """
        self._plan_pi = plan_pi

    @property
    def plan_iteration(self):
        r"""Gets the plan_iteration of this IssueEntity.

        工作项完成的迭代计划ID，在Bug中为修复迭代计划ID。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category=Iteration的对象的id字段就是迭代计划的ID。

        :return: The plan_iteration of this IssueEntity.
        :rtype: str
        """
        return self._plan_iteration

    @plan_iteration.setter
    def plan_iteration(self, plan_iteration):
        r"""Sets the plan_iteration of this IssueEntity.

        工作项完成的迭代计划ID，在Bug中为修复迭代计划ID。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category=Iteration的对象的id字段就是迭代计划的ID。

        :param plan_iteration: The plan_iteration of this IssueEntity.
        :type plan_iteration: str
        """
        self._plan_iteration = plan_iteration

    @property
    def change_status(self):
        r"""Gets the change_status of this IssueEntity.

        工作项变更状态。

        :return: The change_status of this IssueEntity.
        :rtype: str
        """
        return self._change_status

    @change_status.setter
    def change_status(self, change_status):
        r"""Sets the change_status of this IssueEntity.

        工作项变更状态。

        :param change_status: The change_status of this IssueEntity.
        :type change_status: str
        """
        self._change_status = change_status

    @property
    def no_break_reason(self):
        r"""Gets the no_break_reason of this IssueEntity.

        无需分解原因。

        :return: The no_break_reason of this IssueEntity.
        :rtype: str
        """
        return self._no_break_reason

    @no_break_reason.setter
    def no_break_reason(self, no_break_reason):
        r"""Sets the no_break_reason of this IssueEntity.

        无需分解原因。

        :param no_break_reason: The no_break_reason of this IssueEntity.
        :type no_break_reason: str
        """
        self._no_break_reason = no_break_reason

    @property
    def submitted_by(self):
        r"""Gets the submitted_by of this IssueEntity.

        工作项提出人。数组元素为UserEntity对象。

        :return: The submitted_by of this IssueEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        r"""Sets the submitted_by of this IssueEntity.

        工作项提出人。数组元素为UserEntity对象。

        :param submitted_by: The submitted_by of this IssueEntity.
        :type submitted_by: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        self._submitted_by = submitted_by

    @property
    def ir2rr(self):
        r"""Gets the ir2rr of this IssueEntity.

        IR关联的RR ID，可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :return: The ir2rr of this IssueEntity.
        :rtype: str
        """
        return self._ir2rr

    @ir2rr.setter
    def ir2rr(self, ir2rr):
        r"""Sets the ir2rr of this IssueEntity.

        IR关联的RR ID，可以通过查询工作项列表或者查询树状工作项接口获取，响应消息体中的id字段的值就是工作项ID。

        :param ir2rr: The ir2rr of this IssueEntity.
        :type ir2rr: str
        """
        self._ir2rr = ir2rr

    @property
    def feature_set(self):
        r"""Gets the feature_set of this IssueEntity.

        特性集ID，可以通过查询特性集接口获取，响应消息体中的id字段的值就是特性集ID。

        :return: The feature_set of this IssueEntity.
        :rtype: str
        """
        return self._feature_set

    @feature_set.setter
    def feature_set(self, feature_set):
        r"""Sets the feature_set of this IssueEntity.

        特性集ID，可以通过查询特性集接口获取，响应消息体中的id字段的值就是特性集ID。

        :param feature_set: The feature_set of this IssueEntity.
        :type feature_set: str
        """
        self._feature_set = feature_set

    @property
    def expected_repair_date(self):
        r"""Gets the expected_repair_date of this IssueEntity.

        期望修复时间。预设字段中，仅Bug有此字段，unix时间戳，单位：毫秒。

        :return: The expected_repair_date of this IssueEntity.
        :rtype: str
        """
        return self._expected_repair_date

    @expected_repair_date.setter
    def expected_repair_date(self, expected_repair_date):
        r"""Sets the expected_repair_date of this IssueEntity.

        期望修复时间。预设字段中，仅Bug有此字段，unix时间戳，单位：毫秒。

        :param expected_repair_date: The expected_repair_date of this IssueEntity.
        :type expected_repair_date: str
        """
        self._expected_repair_date = expected_repair_date

    @property
    def found_pi(self):
        r"""Gets the found_pi of this IssueEntity.

        缺陷发现发布计划ID，预设字段中，仅Bug有此字段。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category=PI的对象的id字段就是迭代计划的ID。

        :return: The found_pi of this IssueEntity.
        :rtype: str
        """
        return self._found_pi

    @found_pi.setter
    def found_pi(self, found_pi):
        r"""Sets the found_pi of this IssueEntity.

        缺陷发现发布计划ID，预设字段中，仅Bug有此字段。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category=PI的对象的id字段就是迭代计划的ID。

        :param found_pi: The found_pi of this IssueEntity.
        :type found_pi: str
        """
        self._found_pi = found_pi

    @property
    def found_iteration(self):
        r"""Gets the found_iteration of this IssueEntity.

        缺陷发现迭代计划ID，预设字段中，仅Bug有此字段。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category=Iteration的对象的id字段就是迭代计划的ID。

        :return: The found_iteration of this IssueEntity.
        :rtype: str
        """
        return self._found_iteration

    @found_iteration.setter
    def found_iteration(self, found_iteration):
        r"""Sets the found_iteration of this IssueEntity.

        缺陷发现迭代计划ID，预设字段中，仅Bug有此字段。通过发布/迭代计划列表查询接口查询计划列表，返回参数中PlanVO里面的category=Iteration的对象的id字段就是迭代计划的ID。

        :param found_iteration: The found_iteration of this IssueEntity.
        :type found_iteration: str
        """
        self._found_iteration = found_iteration

    @property
    def reason_analysis(self):
        r"""Gets the reason_analysis of this IssueEntity.

        分析原因。

        :return: The reason_analysis of this IssueEntity.
        :rtype: str
        """
        return self._reason_analysis

    @reason_analysis.setter
    def reason_analysis(self, reason_analysis):
        r"""Sets the reason_analysis of this IssueEntity.

        分析原因。

        :param reason_analysis: The reason_analysis of this IssueEntity.
        :type reason_analysis: str
        """
        self._reason_analysis = reason_analysis

    @property
    def repair_solution(self):
        r"""Gets the repair_solution of this IssueEntity.

        修复方案。预设字段中，仅Bug有此字段。

        :return: The repair_solution of this IssueEntity.
        :rtype: str
        """
        return self._repair_solution

    @repair_solution.setter
    def repair_solution(self, repair_solution):
        r"""Sets the repair_solution of this IssueEntity.

        修复方案。预设字段中，仅Bug有此字段。

        :param repair_solution: The repair_solution of this IssueEntity.
        :type repair_solution: str
        """
        self._repair_solution = repair_solution

    @property
    def test_report(self):
        r"""Gets the test_report of this IssueEntity.

        测试报告。预设字段中，仅Bug有此字段。

        :return: The test_report of this IssueEntity.
        :rtype: str
        """
        return self._test_report

    @test_report.setter
    def test_report(self, test_report):
        r"""Sets the test_report of this IssueEntity.

        测试报告。预设字段中，仅Bug有此字段。

        :param test_report: The test_report of this IssueEntity.
        :type test_report: str
        """
        self._test_report = test_report

    @property
    def sys_no_repair_reason(self):
        r"""Gets the sys_no_repair_reason of this IssueEntity.

        无需修复原因。预设字段中，仅Bug有此字段。

        :return: The sys_no_repair_reason of this IssueEntity.
        :rtype: str
        """
        return self._sys_no_repair_reason

    @sys_no_repair_reason.setter
    def sys_no_repair_reason(self, sys_no_repair_reason):
        r"""Sets the sys_no_repair_reason of this IssueEntity.

        无需修复原因。预设字段中，仅Bug有此字段。

        :param sys_no_repair_reason: The sys_no_repair_reason of this IssueEntity.
        :type sys_no_repair_reason: str
        """
        self._sys_no_repair_reason = sys_no_repair_reason

    @property
    def sys_activation_reason(self):
        r"""Gets the sys_activation_reason of this IssueEntity.

        激活原因。预设字段中，仅Bug有此字段。

        :return: The sys_activation_reason of this IssueEntity.
        :rtype: str
        """
        return self._sys_activation_reason

    @sys_activation_reason.setter
    def sys_activation_reason(self, sys_activation_reason):
        r"""Sets the sys_activation_reason of this IssueEntity.

        激活原因。预设字段中，仅Bug有此字段。

        :param sys_activation_reason: The sys_activation_reason of this IssueEntity.
        :type sys_activation_reason: str
        """
        self._sys_activation_reason = sys_activation_reason

    @property
    def sys_return_reason(self):
        r"""Gets the sys_return_reason of this IssueEntity.

        退回原因。预设字段中，仅Bug有此字段。

        :return: The sys_return_reason of this IssueEntity.
        :rtype: str
        """
        return self._sys_return_reason

    @sys_return_reason.setter
    def sys_return_reason(self, sys_return_reason):
        r"""Sets the sys_return_reason of this IssueEntity.

        退回原因。预设字段中，仅Bug有此字段。

        :param sys_return_reason: The sys_return_reason of this IssueEntity.
        :type sys_return_reason: str
        """
        self._sys_return_reason = sys_return_reason

    @property
    def test_failures_times(self):
        r"""Gets the test_failures_times of this IssueEntity.

        回归不通过次数。预设字段中，仅Bug有此字段。

        :return: The test_failures_times of this IssueEntity.
        :rtype: int
        """
        return self._test_failures_times

    @test_failures_times.setter
    def test_failures_times(self, test_failures_times):
        r"""Sets the test_failures_times of this IssueEntity.

        回归不通过次数。预设字段中，仅Bug有此字段。

        :param test_failures_times: The test_failures_times of this IssueEntity.
        :type test_failures_times: int
        """
        self._test_failures_times = test_failures_times

    @property
    def close_type(self):
        r"""Gets the close_type of this IssueEntity.

        关闭类型。

        :return: The close_type of this IssueEntity.
        :rtype: str
        """
        return self._close_type

    @close_type.setter
    def close_type(self, close_type):
        r"""Sets the close_type of this IssueEntity.

        关闭类型。

        :param close_type: The close_type of this IssueEntity.
        :type close_type: str
        """
        self._close_type = close_type

    @property
    def plan_owner(self):
        r"""Gets the plan_owner of this IssueEntity.

        :return: The plan_owner of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._plan_owner

    @plan_owner.setter
    def plan_owner(self, plan_owner):
        r"""Sets the plan_owner of this IssueEntity.

        :param plan_owner: The plan_owner of this IssueEntity.
        :type plan_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._plan_owner = plan_owner

    @property
    def doing_owner(self):
        r"""Gets the doing_owner of this IssueEntity.

        :return: The doing_owner of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._doing_owner

    @doing_owner.setter
    def doing_owner(self, doing_owner):
        r"""Sets the doing_owner of this IssueEntity.

        :param doing_owner: The doing_owner of this IssueEntity.
        :type doing_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._doing_owner = doing_owner

    @property
    def delivered_owner(self):
        r"""Gets the delivered_owner of this IssueEntity.

        :return: The delivered_owner of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._delivered_owner

    @delivered_owner.setter
    def delivered_owner(self, delivered_owner):
        r"""Sets the delivered_owner of this IssueEntity.

        :param delivered_owner: The delivered_owner of this IssueEntity.
        :type delivered_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._delivered_owner = delivered_owner

    @property
    def checking_owner(self):
        r"""Gets the checking_owner of this IssueEntity.

        :return: The checking_owner of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._checking_owner

    @checking_owner.setter
    def checking_owner(self, checking_owner):
        r"""Sets the checking_owner of this IssueEntity.

        :param checking_owner: The checking_owner of this IssueEntity.
        :type checking_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._checking_owner = checking_owner

    @property
    def test_owner(self):
        r"""Gets the test_owner of this IssueEntity.

        :return: The test_owner of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._test_owner

    @test_owner.setter
    def test_owner(self, test_owner):
        r"""Sets the test_owner of this IssueEntity.

        :param test_owner: The test_owner of this IssueEntity.
        :type test_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._test_owner = test_owner

    @property
    def develop_owner(self):
        r"""Gets the develop_owner of this IssueEntity.

        :return: The develop_owner of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._develop_owner

    @develop_owner.setter
    def develop_owner(self, develop_owner):
        r"""Sets the develop_owner of this IssueEntity.

        :param develop_owner: The develop_owner of this IssueEntity.
        :type develop_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._develop_owner = develop_owner

    @property
    def processing_owner(self):
        r"""Gets the processing_owner of this IssueEntity.

        :return: The processing_owner of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._processing_owner

    @processing_owner.setter
    def processing_owner(self, processing_owner):
        r"""Sets the processing_owner of this IssueEntity.

        :param processing_owner: The processing_owner of this IssueEntity.
        :type processing_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._processing_owner = processing_owner

    @property
    def fixed_owner(self):
        r"""Gets the fixed_owner of this IssueEntity.

        :return: The fixed_owner of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._fixed_owner

    @fixed_owner.setter
    def fixed_owner(self, fixed_owner):
        r"""Sets the fixed_owner of this IssueEntity.

        :param fixed_owner: The fixed_owner of this IssueEntity.
        :type fixed_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._fixed_owner = fixed_owner

    @property
    def researchanddevelop_owner(self):
        r"""Gets the researchanddevelop_owner of this IssueEntity.

        :return: The researchanddevelop_owner of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._researchanddevelop_owner

    @researchanddevelop_owner.setter
    def researchanddevelop_owner(self, researchanddevelop_owner):
        r"""Sets the researchanddevelop_owner of this IssueEntity.

        :param researchanddevelop_owner: The researchanddevelop_owner of this IssueEntity.
        :type researchanddevelop_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._researchanddevelop_owner = researchanddevelop_owner

    @property
    def analyse_owner(self):
        r"""Gets the analyse_owner of this IssueEntity.

        :return: The analyse_owner of this IssueEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._analyse_owner

    @analyse_owner.setter
    def analyse_owner(self, analyse_owner):
        r"""Sets the analyse_owner of this IssueEntity.

        :param analyse_owner: The analyse_owner of this IssueEntity.
        :type analyse_owner: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._analyse_owner = analyse_owner

    @property
    def plan_start_date(self):
        r"""Gets the plan_start_date of this IssueEntity.

        计划开始时间。工作项的计划启动日期，用于项目进度管理和排期。

        :return: The plan_start_date of this IssueEntity.
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        r"""Sets the plan_start_date of this IssueEntity.

        计划开始时间。工作项的计划启动日期，用于项目进度管理和排期。

        :param plan_start_date: The plan_start_date of this IssueEntity.
        :type plan_start_date: str
        """
        self._plan_start_date = plan_start_date

    @property
    def expect_delivery_time(self):
        r"""Gets the expect_delivery_time of this IssueEntity.

        期望完成时间。工作项的预期交付日期，用于跟踪工作项是否按期完成。

        :return: The expect_delivery_time of this IssueEntity.
        :rtype: str
        """
        return self._expect_delivery_time

    @expect_delivery_time.setter
    def expect_delivery_time(self, expect_delivery_time):
        r"""Sets the expect_delivery_time of this IssueEntity.

        期望完成时间。工作项的预期交付日期，用于跟踪工作项是否按期完成。

        :param expect_delivery_time: The expect_delivery_time of this IssueEntity.
        :type expect_delivery_time: str
        """
        self._expect_delivery_time = expect_delivery_time

    @property
    def plan_test_end_date(self):
        r"""Gets the plan_test_end_date of this IssueEntity.

        计划测试结束时间。Bug类型工作项的计划测试完成日期，用于跟踪Bug修复后的测试进度。

        :return: The plan_test_end_date of this IssueEntity.
        :rtype: str
        """
        return self._plan_test_end_date

    @plan_test_end_date.setter
    def plan_test_end_date(self, plan_test_end_date):
        r"""Sets the plan_test_end_date of this IssueEntity.

        计划测试结束时间。Bug类型工作项的计划测试完成日期，用于跟踪Bug修复后的测试进度。

        :param plan_test_end_date: The plan_test_end_date of this IssueEntity.
        :type plan_test_end_date: str
        """
        self._plan_test_end_date = plan_test_end_date

    @property
    def severity(self):
        r"""Gets the severity of this IssueEntity.

        严重程度。Bug类型工作项的严重级别，用于评估Bug的影响范围和修复优先级。

        :return: The severity of this IssueEntity.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this IssueEntity.

        严重程度。Bug类型工作项的严重级别，用于评估Bug的影响范围和修复优先级。

        :param severity: The severity of this IssueEntity.
        :type severity: str
        """
        self._severity = severity

    @property
    def promised(self):
        r"""Gets the promised of this IssueEntity.

        是否承诺。RR（原始需求）类型工作项的承诺状态标识，用于标记需求是否已承诺交付。

        :return: The promised of this IssueEntity.
        :rtype: str
        """
        return self._promised

    @promised.setter
    def promised(self, promised):
        r"""Sets the promised of this IssueEntity.

        是否承诺。RR（原始需求）类型工作项的承诺状态标识，用于标记需求是否已承诺交付。

        :param promised: The promised of this IssueEntity.
        :type promised: str
        """
        self._promised = promised

    @property
    def recipient(self):
        r"""Gets the recipient of this IssueEntity.

        承接人。RR（原始需求）类型工作项的需求承接责任人，负责需求的分析和转化。

        :return: The recipient of this IssueEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        r"""Sets the recipient of this IssueEntity.

        承接人。RR（原始需求）类型工作项的需求承接责任人，负责需求的分析和转化。

        :param recipient: The recipient of this IssueEntity.
        :type recipient: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        self._recipient = recipient

    @property
    def sys_no_develop_reason(self):
        r"""Gets the sys_no_develop_reason of this IssueEntity.

        无需研发原因。RR（原始需求）类型工作项不需要进行研发的原因说明。

        :return: The sys_no_develop_reason of this IssueEntity.
        :rtype: str
        """
        return self._sys_no_develop_reason

    @sys_no_develop_reason.setter
    def sys_no_develop_reason(self, sys_no_develop_reason):
        r"""Sets the sys_no_develop_reason of this IssueEntity.

        无需研发原因。RR（原始需求）类型工作项不需要进行研发的原因说明。

        :param sys_no_develop_reason: The sys_no_develop_reason of this IssueEntity.
        :type sys_no_develop_reason: str
        """
        self._sys_no_develop_reason = sys_no_develop_reason

    @property
    def val_feature(self):
        r"""Gets the val_feature of this IssueEntity.

        价值特性。SF/FE类型工作项对应的业务价值特性描述，用于关联业务价值和技术实现。

        :return: The val_feature of this IssueEntity.
        :rtype: str
        """
        return self._val_feature

    @val_feature.setter
    def val_feature(self, val_feature):
        r"""Sets the val_feature of this IssueEntity.

        价值特性。SF/FE类型工作项对应的业务价值特性描述，用于关联业务价值和技术实现。

        :param val_feature: The val_feature of this IssueEntity.
        :type val_feature: str
        """
        self._val_feature = val_feature

    @property
    def function_scene(self):
        r"""Gets the function_scene of this IssueEntity.

        功能场景。SF/FE类型工作项的功能应用场景描述，用于说明特性的使用场景和用户故事。

        :return: The function_scene of this IssueEntity.
        :rtype: str
        """
        return self._function_scene

    @function_scene.setter
    def function_scene(self, function_scene):
        r"""Sets the function_scene of this IssueEntity.

        功能场景。SF/FE类型工作项的功能应用场景描述，用于说明特性的使用场景和用户故事。

        :param function_scene: The function_scene of this IssueEntity.
        :type function_scene: str
        """
        self._function_scene = function_scene

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
        if not isinstance(other, IssueEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
