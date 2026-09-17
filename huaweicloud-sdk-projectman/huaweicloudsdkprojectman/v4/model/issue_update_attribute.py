# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueUpdateAttribute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'category': 'str',
        'description': 'str',
        'parent_id': 'str',
        'status': 'str',
        'assignee': 'UserUpdateAttribute',
        'assigned_cc': 'list[UserUpdateAttribute]',
        'plan_end_date': 'str',
        'workload': 'str',
        'link': 'str',
        'labels': 'list[LabelEntity]',
        'custom_fields': 'list[FieldCodeValuePair]',
        'ir2feature': 'str',
        'need_break': 'str',
        'baseline': 'str',
        'priority': 'str',
        'related_network_security': 'str',
        'business_domain': 'str',
        'plan_pi': 'str',
        'plan_iteration': 'str',
        'no_break_reason': 'str',
        'submitted_by': 'list[UserUpdateAttribute]',
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
        'security_level': 'str',
        'plan_owner': 'UserUpdateAttribute',
        'doing_owner': 'UserUpdateAttribute',
        'delivered_owner': 'UserUpdateAttribute',
        'checking_owner': 'UserUpdateAttribute',
        'test_owner': 'UserUpdateAttribute',
        'develop_owner': 'UserUpdateAttribute',
        'processing_owner': 'UserUpdateAttribute',
        'fixed_owner': 'UserUpdateAttribute',
        'researchanddevelop_owner': 'UserUpdateAttribute',
        'analyse_owner': 'UserUpdateAttribute',
        'plan_start_date': 'str',
        'expect_delivery_time': 'str',
        'plan_test_end_date': 'str',
        'severity': 'str',
        'promised': 'str',
        'recipient': 'list[UserUpdateAttribute]',
        'sys_no_develop_reason': 'str',
        'val_feature': 'str',
        'function_scene': 'str'
    }

    attribute_map = {
        'category': 'category',
        'description': 'description',
        'parent_id': 'parent_id',
        'status': 'status',
        'assignee': 'assignee',
        'assigned_cc': 'assigned_cc',
        'plan_end_date': 'plan_end_date',
        'workload': 'workload',
        'link': 'link',
        'labels': 'labels',
        'custom_fields': 'custom_fields',
        'ir2feature': 'ir2feature',
        'need_break': 'need_break',
        'baseline': 'baseline',
        'priority': 'priority',
        'related_network_security': 'related_network_security',
        'business_domain': 'business_domain',
        'plan_pi': 'plan_pi',
        'plan_iteration': 'plan_iteration',
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
        'security_level': 'security_level',
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

    def __init__(self, category=None, description=None, parent_id=None, status=None, assignee=None, assigned_cc=None, plan_end_date=None, workload=None, link=None, labels=None, custom_fields=None, ir2feature=None, need_break=None, baseline=None, priority=None, related_network_security=None, business_domain=None, plan_pi=None, plan_iteration=None, no_break_reason=None, submitted_by=None, ir2rr=None, feature_set=None, expected_repair_date=None, found_pi=None, found_iteration=None, reason_analysis=None, repair_solution=None, test_report=None, sys_no_repair_reason=None, sys_activation_reason=None, sys_return_reason=None, test_failures_times=None, close_type=None, security_level=None, plan_owner=None, doing_owner=None, delivered_owner=None, checking_owner=None, test_owner=None, develop_owner=None, processing_owner=None, fixed_owner=None, researchanddevelop_owner=None, analyse_owner=None, plan_start_date=None, expect_delivery_time=None, plan_test_end_date=None, severity=None, promised=None, recipient=None, sys_no_develop_reason=None, val_feature=None, function_scene=None):
        r"""IssueUpdateAttribute

        The model defined in huaweicloud sdk

        :param category: **参数解释**： 工作项类型编码。编辑工作项时，此字段必填、值为当前工作项正确的工作项类型，但不会更新此字段。 **约束限制**： 不涉及。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug **默认取值**： 不涉及。
        :type category: str
        :param description: **参数解释**： 工作项描述字段，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**description**字段的值就是工作项描述字段。 **约束限制**： 不涉及。 **取值范围**： 1~500000个字符。 **默认取值**： 不涉及。
        :type description: str
        :param parent_id: **参数解释**： 父工作项ID，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**parent_id**字段的值就是父工作项ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。
        :type parent_id: str
        :param status: **参数解释**： 工作项状态code。可通过[查询工作项状态](ListIssueStatues.xml)接口获取，响应消息体中的**code**字段的值就是工作项状态code。 **约束限制**： 不涉及。 **取值范围**： 2~32个字符。 **默认取值**： 不涉及。
        :type status: str
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param assigned_cc: **参数解释**： 工作项抄送人，支持多个抄送人。数组元素为UserUpdateAttribute对象。 **约束限制**： 同一工作项最多支持50个抄送人。
        :type assigned_cc: list[:class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`]
        :param plan_end_date: **参数解释**： 工作项计划结束日期，unix时间戳，单位：毫秒。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type plan_end_date: str
        :param workload: **参数解释**： 工作项计划工时。 **约束限制**： 保留一位小数。 **取值范围**： 0~999999999.9。 **默认取值**： 不涉及。
        :type workload: str
        :param link: **参数解释**： 工作项关联项ID。 **约束限制**： 多个关联项用英文逗号分隔，同一工作项最多支持50个关联项。 **取值范围**： 0~2048个字符。 **默认取值**： 不涉及。
        :type link: str
        :param labels: **参数解释**： 工作项标签。数组元素为LabelEntity对象。 **约束限制**： 不涉及。 **取值范围**： 0~50个元素，每个元素为LabelEntity对象。 **默认取值**： 不涉及。
        :type labels: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        :param custom_fields: **参数解释**： 工作项自定义字段映射，用户添加的系统字段也在此列，格式为{\&quot;code\&quot;:\&quot;字段code\&quot;,\&quot;value\&quot;:\&quot;字段值\&quot;}。数组元素为FieldCodeValuePair对象。 **约束限制**： 不涉及。 **取值范围**： 0~200个元素，每个元素为FieldCodeValuePair对象。 **默认取值**： 不涉及。
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        :param ir2feature: **参数解释**： IR和SF的关联字段。 **约束限制**： IR可以填写该字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type ir2feature: str
        :param need_break: **参数解释**： 工作项是否需要分解。 **约束限制**： 仅可以分解的工作项类型有此字段。 **取值范围**： - yes：需要分解 - no：不需要分解 **默认取值**： 不涉及。
        :type need_break: str
        :param baseline: **参数解释**： 工作项基线状态。 **约束限制**： 不涉及。 **取值范围**： - null：未基线 - baselined：已基线 - baseline-reviewing：基线评审中 **默认取值**： 不涉及。
        :type baseline: str
        :param priority: **参数解释**： 工作项优先级，部分工作项有此字段。 **约束限制**： 不涉及。 **取值范围**： - 低：低优先级。 - 中：中优先级。 - 高：高优先级。 **默认取值**： 不涉及。
        :type priority: str
        :param related_network_security: **参数解释**： 是否涉及网络安全。 **约束限制**： 预设字段中，仅研发需求类型的工作项有此字段。 **取值范围**： - yes：涉及网络安全。 - no：不涉及网络安全。 **默认取值**： 不涉及。
        :type related_network_security: str
        :param business_domain: **参数解释**： 领域字段。 **约束限制**： 不涉及。 **取值范围**： - software - soft-hardware - hardware - 性能 - 功能 - 运维 - 运营 - 用户体验 - 隐私保护 - 合规 - 韧性(可靠性/可用性) - 韧性(危险检测与相应恢复) - 透明 - 无害 - 安全 - API - 成本 - 可维护性 - 其他DFX - 可用性 - others **默认取值**： 不涉及。
        :type business_domain: str
        :param plan_pi: **参数解释**： 工作项发布计划ID。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category&#x3D;PI的对象的**id**字段就是迭代计划的ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。
        :type plan_pi: str
        :param plan_iteration: **参数解释**： 工作项完成的迭代计划ID，在Bug中为修复迭代计划ID。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category&#x3D;Iteration的对象的**id**字段就是迭代计划的ID。 **约束限制**： 18~19个字符的数字字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type plan_iteration: str
        :param no_break_reason: **参数解释**： 无需分解原因。 **约束限制**： need_break字段值为“no”时有此字段。 **取值范围**： 0~512个字符。 **默认取值**： 不涉及。
        :type no_break_reason: str
        :param submitted_by: **参数解释**： 工作项提出人。数组元素为UserUpdateAttribute对象。 **约束限制**： 不涉及。
        :type submitted_by: list[:class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`]
        :param ir2rr: **参数解释**： IR关联的RR ID，可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 多个关联项ID使用英文逗号分隔。 **取值范围**： 0~1024个字符。 **默认取值**： 不涉及。
        :type ir2rr: str
        :param feature_set: **参数解释**： 特性集ID，可以通过[查询特性集](ShowBaselineSnapshots.xml)接口获取，响应消息体中的**id**字段的值就是特性集ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。
        :type feature_set: str
        :param expected_repair_date: **参数解释**： 期望修复时间。预设字段中，仅Bug有此字段，unix时间戳，单位：毫秒。 **约束限制**： 不涉及。 **取值范围**： 11~19个字符。 **默认取值**： 不涉及。
        :type expected_repair_date: str
        :param found_pi: **参数解释**： 缺陷发现发布计划ID，预设字段中，仅Bug有此字段。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category&#x3D;PI的对象的**id**字段就是迭代计划的ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。
        :type found_pi: str
        :param found_iteration: **参数解释**： 缺陷发现迭代计划ID，预设字段中，仅Bug有此字段。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category&#x3D;Iteration的对象的**id**字段就是迭代计划的ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。
        :type found_iteration: str
        :param reason_analysis: **参数解释**： 分析原因。 **约束限制**： 预设字段中，仅Bug有此字段。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。
        :type reason_analysis: str
        :param repair_solution: **参数解释**： 修复方案。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。
        :type repair_solution: str
        :param test_report: **参数解释**： 测试报告。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。
        :type test_report: str
        :param sys_no_repair_reason: **参数解释**： 无需修复原因。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。
        :type sys_no_repair_reason: str
        :param sys_activation_reason: **参数解释**： 激活原因。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。
        :type sys_activation_reason: str
        :param sys_return_reason: **参数解释**： 退回原因。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。
        :type sys_return_reason: str
        :param test_failures_times: **参数解释**： 回归不通过次数。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~999999。 **默认取值**： 不涉及。
        :type test_failures_times: int
        :param close_type: **参数解释**： 关闭类型。 **约束限制**： 不涉及。 **取值范围**： - problem_solved：问题解决关闭 - problem_to_requirement：问题转需求关闭 - duplicate_problem：重复问题关闭 - not_a_problem：非问题关闭 **默认取值**： 不涉及。
        :type close_type: str
        :param security_level: **参数解释**： 密级。低密级权限者不能访问高密级的工作项。可以通过[查询字段列表](ListIpdProjectFields.xml)接口获取，响应消息体中密级的**option**字段的值就是密级字段的可选值。 **约束限制**： 仅在涉密环境（SM）下存在此字段，非涉密环境下无此字段。涉密环境下必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type security_level: str
        :param plan_owner: 
        :type plan_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param doing_owner: 
        :type doing_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param delivered_owner: 
        :type delivered_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param checking_owner: 
        :type checking_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param test_owner: 
        :type test_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param develop_owner: 
        :type develop_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param processing_owner: 
        :type processing_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param fixed_owner: 
        :type fixed_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param researchanddevelop_owner: 
        :type researchanddevelop_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param analyse_owner: 
        :type analyse_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        :param plan_start_date: **参数解释**： 计划开始时间。工作项的计划启动日期，用于项目进度管理和排期。 **约束限制**： 不涉及。 **取值范围**： 11~19个字符的时间戳字符串，单位为毫秒（ms）。 **默认取值**： 不涉及。
        :type plan_start_date: str
        :param expect_delivery_time: **参数解释**： 期望完成时间。工作项的预期交付日期，用于跟踪工作项是否按期完成。 **约束限制**： 不涉及。 **取值范围**： 11~19个字符的时间戳字符串，单位为毫秒（ms）。 **默认取值**： 不涉及。
        :type expect_delivery_time: str
        :param plan_test_end_date: **参数解释**： 计划测试结束时间。Bug类型工作项的计划测试完成日期，用于跟踪Bug修复后的测试进度。 **约束限制**： 仅对Bug类型工作项生效，非Bug类型忽略此字段。 **取值范围**： 11~19个字符的时间戳字符串，单位为毫秒（ms）。 **默认取值**： 不涉及。
        :type plan_test_end_date: str
        :param severity: **参数解释**： 严重程度。Bug类型工作项的严重级别，用于评估Bug的影响范围和修复优先级。 **约束限制**： 仅对Bug类型工作项生效，非Bug类型忽略此字段。 **取值范围**： - 致命：系统崩溃、数据丢失等严重影响 - 严重：主要功能无法使用 - 一般：次要功能异常，有替代方案 - 提示：界面优化、建议性问题 **默认取值**： 不涉及。
        :type severity: str
        :param promised: **参数解释**： 是否承诺。RR（原始需求）类型工作项的承诺状态标识，用于标记需求是否已承诺交付。 **约束限制**： 仅对RR类型工作项生效，非RR类型忽略此字段。 **取值范围**： - yes：已承诺 - no：未承诺 **默认取值**： 不涉及。
        :type promised: str
        :param recipient: **参数解释**： 承接人。RR（原始需求）类型工作项的需求承接责任人，负责需求的分析和转化。 **约束限制**： 仅对RR类型工作项生效，非RR类型忽略此字段。
        :type recipient: list[:class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`]
        :param sys_no_develop_reason: **参数解释**： 无需研发原因。RR（原始需求）类型工作项不需要进行研发的原因说明。 **约束限制**： 仅对RR类型工作项生效，非RR类型忽略此字段。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。
        :type sys_no_develop_reason: str
        :param val_feature: **参数解释**： 价值特性。SF/FE类型工作项对应的业务价值特性描述，用于关联业务价值和技术实现。 **约束限制**： 仅对SF/FE类型工作项生效，其他类型忽略此字段。 **取值范围**： - yes：是 - no：否 **默认取值**： 不涉及。
        :type val_feature: str
        :param function_scene: **参数解释**： 功能场景。SF/FE类型工作项的功能应用场景描述，用于说明特性的使用场景和用户故事。 **约束限制**： 仅对SF/FE类型工作项生效，其他类型忽略此字段。 **取值范围**： 0~512个字符。 **默认取值**： 不涉及。
        :type function_scene: str
        """
        
        

        self._category = None
        self._description = None
        self._parent_id = None
        self._status = None
        self._assignee = None
        self._assigned_cc = None
        self._plan_end_date = None
        self._workload = None
        self._link = None
        self._labels = None
        self._custom_fields = None
        self._ir2feature = None
        self._need_break = None
        self._baseline = None
        self._priority = None
        self._related_network_security = None
        self._business_domain = None
        self._plan_pi = None
        self._plan_iteration = None
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
        self._security_level = None
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

        if category is not None:
            self.category = category
        if description is not None:
            self.description = description
        if parent_id is not None:
            self.parent_id = parent_id
        if status is not None:
            self.status = status
        if assignee is not None:
            self.assignee = assignee
        if assigned_cc is not None:
            self.assigned_cc = assigned_cc
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if workload is not None:
            self.workload = workload
        if link is not None:
            self.link = link
        if labels is not None:
            self.labels = labels
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if ir2feature is not None:
            self.ir2feature = ir2feature
        if need_break is not None:
            self.need_break = need_break
        if baseline is not None:
            self.baseline = baseline
        if priority is not None:
            self.priority = priority
        if related_network_security is not None:
            self.related_network_security = related_network_security
        if business_domain is not None:
            self.business_domain = business_domain
        if plan_pi is not None:
            self.plan_pi = plan_pi
        if plan_iteration is not None:
            self.plan_iteration = plan_iteration
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
        if security_level is not None:
            self.security_level = security_level
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
    def category(self):
        r"""Gets the category of this IssueUpdateAttribute.

        **参数解释**： 工作项类型编码。编辑工作项时，此字段必填、值为当前工作项正确的工作项类型，但不会更新此字段。 **约束限制**： 不涉及。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug **默认取值**： 不涉及。

        :return: The category of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this IssueUpdateAttribute.

        **参数解释**： 工作项类型编码。编辑工作项时，此字段必填、值为当前工作项正确的工作项类型，但不会更新此字段。 **约束限制**： 不涉及。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug **默认取值**： 不涉及。

        :param category: The category of this IssueUpdateAttribute.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this IssueUpdateAttribute.

        **参数解释**： 工作项描述字段，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**description**字段的值就是工作项描述字段。 **约束限制**： 不涉及。 **取值范围**： 1~500000个字符。 **默认取值**： 不涉及。

        :return: The description of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IssueUpdateAttribute.

        **参数解释**： 工作项描述字段，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**description**字段的值就是工作项描述字段。 **约束限制**： 不涉及。 **取值范围**： 1~500000个字符。 **默认取值**： 不涉及。

        :param description: The description of this IssueUpdateAttribute.
        :type description: str
        """
        self._description = description

    @property
    def parent_id(self):
        r"""Gets the parent_id of this IssueUpdateAttribute.

        **参数解释**： 父工作项ID，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**parent_id**字段的值就是父工作项ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :return: The parent_id of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this IssueUpdateAttribute.

        **参数解释**： 父工作项ID，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**parent_id**字段的值就是父工作项ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :param parent_id: The parent_id of this IssueUpdateAttribute.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def status(self):
        r"""Gets the status of this IssueUpdateAttribute.

        **参数解释**： 工作项状态code。可通过[查询工作项状态](ListIssueStatues.xml)接口获取，响应消息体中的**code**字段的值就是工作项状态code。 **约束限制**： 不涉及。 **取值范围**： 2~32个字符。 **默认取值**： 不涉及。

        :return: The status of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IssueUpdateAttribute.

        **参数解释**： 工作项状态code。可通过[查询工作项状态](ListIssueStatues.xml)接口获取，响应消息体中的**code**字段的值就是工作项状态code。 **约束限制**： 不涉及。 **取值范围**： 2~32个字符。 **默认取值**： 不涉及。

        :param status: The status of this IssueUpdateAttribute.
        :type status: str
        """
        self._status = status

    @property
    def assignee(self):
        r"""Gets the assignee of this IssueUpdateAttribute.

        :return: The assignee of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this IssueUpdateAttribute.

        :param assignee: The assignee of this IssueUpdateAttribute.
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._assignee = assignee

    @property
    def assigned_cc(self):
        r"""Gets the assigned_cc of this IssueUpdateAttribute.

        **参数解释**： 工作项抄送人，支持多个抄送人。数组元素为UserUpdateAttribute对象。 **约束限制**： 同一工作项最多支持50个抄送人。

        :return: The assigned_cc of this IssueUpdateAttribute.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`]
        """
        return self._assigned_cc

    @assigned_cc.setter
    def assigned_cc(self, assigned_cc):
        r"""Sets the assigned_cc of this IssueUpdateAttribute.

        **参数解释**： 工作项抄送人，支持多个抄送人。数组元素为UserUpdateAttribute对象。 **约束限制**： 同一工作项最多支持50个抄送人。

        :param assigned_cc: The assigned_cc of this IssueUpdateAttribute.
        :type assigned_cc: list[:class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`]
        """
        self._assigned_cc = assigned_cc

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this IssueUpdateAttribute.

        **参数解释**： 工作项计划结束日期，unix时间戳，单位：毫秒。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The plan_end_date of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this IssueUpdateAttribute.

        **参数解释**： 工作项计划结束日期，unix时间戳，单位：毫秒。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param plan_end_date: The plan_end_date of this IssueUpdateAttribute.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def workload(self):
        r"""Gets the workload of this IssueUpdateAttribute.

        **参数解释**： 工作项计划工时。 **约束限制**： 保留一位小数。 **取值范围**： 0~999999999.9。 **默认取值**： 不涉及。

        :return: The workload of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._workload

    @workload.setter
    def workload(self, workload):
        r"""Sets the workload of this IssueUpdateAttribute.

        **参数解释**： 工作项计划工时。 **约束限制**： 保留一位小数。 **取值范围**： 0~999999999.9。 **默认取值**： 不涉及。

        :param workload: The workload of this IssueUpdateAttribute.
        :type workload: str
        """
        self._workload = workload

    @property
    def link(self):
        r"""Gets the link of this IssueUpdateAttribute.

        **参数解释**： 工作项关联项ID。 **约束限制**： 多个关联项用英文逗号分隔，同一工作项最多支持50个关联项。 **取值范围**： 0~2048个字符。 **默认取值**： 不涉及。

        :return: The link of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this IssueUpdateAttribute.

        **参数解释**： 工作项关联项ID。 **约束限制**： 多个关联项用英文逗号分隔，同一工作项最多支持50个关联项。 **取值范围**： 0~2048个字符。 **默认取值**： 不涉及。

        :param link: The link of this IssueUpdateAttribute.
        :type link: str
        """
        self._link = link

    @property
    def labels(self):
        r"""Gets the labels of this IssueUpdateAttribute.

        **参数解释**： 工作项标签。数组元素为LabelEntity对象。 **约束限制**： 不涉及。 **取值范围**： 0~50个元素，每个元素为LabelEntity对象。 **默认取值**： 不涉及。

        :return: The labels of this IssueUpdateAttribute.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this IssueUpdateAttribute.

        **参数解释**： 工作项标签。数组元素为LabelEntity对象。 **约束限制**： 不涉及。 **取值范围**： 0~50个元素，每个元素为LabelEntity对象。 **默认取值**： 不涉及。

        :param labels: The labels of this IssueUpdateAttribute.
        :type labels: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        """
        self._labels = labels

    @property
    def custom_fields(self):
        r"""Gets the custom_fields of this IssueUpdateAttribute.

        **参数解释**： 工作项自定义字段映射，用户添加的系统字段也在此列，格式为{\"code\":\"字段code\",\"value\":\"字段值\"}。数组元素为FieldCodeValuePair对象。 **约束限制**： 不涉及。 **取值范围**： 0~200个元素，每个元素为FieldCodeValuePair对象。 **默认取值**： 不涉及。

        :return: The custom_fields of this IssueUpdateAttribute.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        r"""Sets the custom_fields of this IssueUpdateAttribute.

        **参数解释**： 工作项自定义字段映射，用户添加的系统字段也在此列，格式为{\"code\":\"字段code\",\"value\":\"字段值\"}。数组元素为FieldCodeValuePair对象。 **约束限制**： 不涉及。 **取值范围**： 0~200个元素，每个元素为FieldCodeValuePair对象。 **默认取值**： 不涉及。

        :param custom_fields: The custom_fields of this IssueUpdateAttribute.
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        """
        self._custom_fields = custom_fields

    @property
    def ir2feature(self):
        r"""Gets the ir2feature of this IssueUpdateAttribute.

        **参数解释**： IR和SF的关联字段。 **约束限制**： IR可以填写该字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The ir2feature of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._ir2feature

    @ir2feature.setter
    def ir2feature(self, ir2feature):
        r"""Sets the ir2feature of this IssueUpdateAttribute.

        **参数解释**： IR和SF的关联字段。 **约束限制**： IR可以填写该字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param ir2feature: The ir2feature of this IssueUpdateAttribute.
        :type ir2feature: str
        """
        self._ir2feature = ir2feature

    @property
    def need_break(self):
        r"""Gets the need_break of this IssueUpdateAttribute.

        **参数解释**： 工作项是否需要分解。 **约束限制**： 仅可以分解的工作项类型有此字段。 **取值范围**： - yes：需要分解 - no：不需要分解 **默认取值**： 不涉及。

        :return: The need_break of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._need_break

    @need_break.setter
    def need_break(self, need_break):
        r"""Sets the need_break of this IssueUpdateAttribute.

        **参数解释**： 工作项是否需要分解。 **约束限制**： 仅可以分解的工作项类型有此字段。 **取值范围**： - yes：需要分解 - no：不需要分解 **默认取值**： 不涉及。

        :param need_break: The need_break of this IssueUpdateAttribute.
        :type need_break: str
        """
        self._need_break = need_break

    @property
    def baseline(self):
        r"""Gets the baseline of this IssueUpdateAttribute.

        **参数解释**： 工作项基线状态。 **约束限制**： 不涉及。 **取值范围**： - null：未基线 - baselined：已基线 - baseline-reviewing：基线评审中 **默认取值**： 不涉及。

        :return: The baseline of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this IssueUpdateAttribute.

        **参数解释**： 工作项基线状态。 **约束限制**： 不涉及。 **取值范围**： - null：未基线 - baselined：已基线 - baseline-reviewing：基线评审中 **默认取值**： 不涉及。

        :param baseline: The baseline of this IssueUpdateAttribute.
        :type baseline: str
        """
        self._baseline = baseline

    @property
    def priority(self):
        r"""Gets the priority of this IssueUpdateAttribute.

        **参数解释**： 工作项优先级，部分工作项有此字段。 **约束限制**： 不涉及。 **取值范围**： - 低：低优先级。 - 中：中优先级。 - 高：高优先级。 **默认取值**： 不涉及。

        :return: The priority of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this IssueUpdateAttribute.

        **参数解释**： 工作项优先级，部分工作项有此字段。 **约束限制**： 不涉及。 **取值范围**： - 低：低优先级。 - 中：中优先级。 - 高：高优先级。 **默认取值**： 不涉及。

        :param priority: The priority of this IssueUpdateAttribute.
        :type priority: str
        """
        self._priority = priority

    @property
    def related_network_security(self):
        r"""Gets the related_network_security of this IssueUpdateAttribute.

        **参数解释**： 是否涉及网络安全。 **约束限制**： 预设字段中，仅研发需求类型的工作项有此字段。 **取值范围**： - yes：涉及网络安全。 - no：不涉及网络安全。 **默认取值**： 不涉及。

        :return: The related_network_security of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._related_network_security

    @related_network_security.setter
    def related_network_security(self, related_network_security):
        r"""Sets the related_network_security of this IssueUpdateAttribute.

        **参数解释**： 是否涉及网络安全。 **约束限制**： 预设字段中，仅研发需求类型的工作项有此字段。 **取值范围**： - yes：涉及网络安全。 - no：不涉及网络安全。 **默认取值**： 不涉及。

        :param related_network_security: The related_network_security of this IssueUpdateAttribute.
        :type related_network_security: str
        """
        self._related_network_security = related_network_security

    @property
    def business_domain(self):
        r"""Gets the business_domain of this IssueUpdateAttribute.

        **参数解释**： 领域字段。 **约束限制**： 不涉及。 **取值范围**： - software - soft-hardware - hardware - 性能 - 功能 - 运维 - 运营 - 用户体验 - 隐私保护 - 合规 - 韧性(可靠性/可用性) - 韧性(危险检测与相应恢复) - 透明 - 无害 - 安全 - API - 成本 - 可维护性 - 其他DFX - 可用性 - others **默认取值**： 不涉及。

        :return: The business_domain of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._business_domain

    @business_domain.setter
    def business_domain(self, business_domain):
        r"""Sets the business_domain of this IssueUpdateAttribute.

        **参数解释**： 领域字段。 **约束限制**： 不涉及。 **取值范围**： - software - soft-hardware - hardware - 性能 - 功能 - 运维 - 运营 - 用户体验 - 隐私保护 - 合规 - 韧性(可靠性/可用性) - 韧性(危险检测与相应恢复) - 透明 - 无害 - 安全 - API - 成本 - 可维护性 - 其他DFX - 可用性 - others **默认取值**： 不涉及。

        :param business_domain: The business_domain of this IssueUpdateAttribute.
        :type business_domain: str
        """
        self._business_domain = business_domain

    @property
    def plan_pi(self):
        r"""Gets the plan_pi of this IssueUpdateAttribute.

        **参数解释**： 工作项发布计划ID。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category=PI的对象的**id**字段就是迭代计划的ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :return: The plan_pi of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._plan_pi

    @plan_pi.setter
    def plan_pi(self, plan_pi):
        r"""Sets the plan_pi of this IssueUpdateAttribute.

        **参数解释**： 工作项发布计划ID。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category=PI的对象的**id**字段就是迭代计划的ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :param plan_pi: The plan_pi of this IssueUpdateAttribute.
        :type plan_pi: str
        """
        self._plan_pi = plan_pi

    @property
    def plan_iteration(self):
        r"""Gets the plan_iteration of this IssueUpdateAttribute.

        **参数解释**： 工作项完成的迭代计划ID，在Bug中为修复迭代计划ID。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category=Iteration的对象的**id**字段就是迭代计划的ID。 **约束限制**： 18~19个字符的数字字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The plan_iteration of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._plan_iteration

    @plan_iteration.setter
    def plan_iteration(self, plan_iteration):
        r"""Sets the plan_iteration of this IssueUpdateAttribute.

        **参数解释**： 工作项完成的迭代计划ID，在Bug中为修复迭代计划ID。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category=Iteration的对象的**id**字段就是迭代计划的ID。 **约束限制**： 18~19个字符的数字字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param plan_iteration: The plan_iteration of this IssueUpdateAttribute.
        :type plan_iteration: str
        """
        self._plan_iteration = plan_iteration

    @property
    def no_break_reason(self):
        r"""Gets the no_break_reason of this IssueUpdateAttribute.

        **参数解释**： 无需分解原因。 **约束限制**： need_break字段值为“no”时有此字段。 **取值范围**： 0~512个字符。 **默认取值**： 不涉及。

        :return: The no_break_reason of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._no_break_reason

    @no_break_reason.setter
    def no_break_reason(self, no_break_reason):
        r"""Sets the no_break_reason of this IssueUpdateAttribute.

        **参数解释**： 无需分解原因。 **约束限制**： need_break字段值为“no”时有此字段。 **取值范围**： 0~512个字符。 **默认取值**： 不涉及。

        :param no_break_reason: The no_break_reason of this IssueUpdateAttribute.
        :type no_break_reason: str
        """
        self._no_break_reason = no_break_reason

    @property
    def submitted_by(self):
        r"""Gets the submitted_by of this IssueUpdateAttribute.

        **参数解释**： 工作项提出人。数组元素为UserUpdateAttribute对象。 **约束限制**： 不涉及。

        :return: The submitted_by of this IssueUpdateAttribute.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`]
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        r"""Sets the submitted_by of this IssueUpdateAttribute.

        **参数解释**： 工作项提出人。数组元素为UserUpdateAttribute对象。 **约束限制**： 不涉及。

        :param submitted_by: The submitted_by of this IssueUpdateAttribute.
        :type submitted_by: list[:class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`]
        """
        self._submitted_by = submitted_by

    @property
    def ir2rr(self):
        r"""Gets the ir2rr of this IssueUpdateAttribute.

        **参数解释**： IR关联的RR ID，可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 多个关联项ID使用英文逗号分隔。 **取值范围**： 0~1024个字符。 **默认取值**： 不涉及。

        :return: The ir2rr of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._ir2rr

    @ir2rr.setter
    def ir2rr(self, ir2rr):
        r"""Sets the ir2rr of this IssueUpdateAttribute.

        **参数解释**： IR关联的RR ID，可以通过[查询工作项列表](ListIpdProjectIssues.xml)或者[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**id**字段的值就是工作项ID。 **约束限制**： 多个关联项ID使用英文逗号分隔。 **取值范围**： 0~1024个字符。 **默认取值**： 不涉及。

        :param ir2rr: The ir2rr of this IssueUpdateAttribute.
        :type ir2rr: str
        """
        self._ir2rr = ir2rr

    @property
    def feature_set(self):
        r"""Gets the feature_set of this IssueUpdateAttribute.

        **参数解释**： 特性集ID，可以通过[查询特性集](ShowBaselineSnapshots.xml)接口获取，响应消息体中的**id**字段的值就是特性集ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :return: The feature_set of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._feature_set

    @feature_set.setter
    def feature_set(self, feature_set):
        r"""Sets the feature_set of this IssueUpdateAttribute.

        **参数解释**： 特性集ID，可以通过[查询特性集](ShowBaselineSnapshots.xml)接口获取，响应消息体中的**id**字段的值就是特性集ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :param feature_set: The feature_set of this IssueUpdateAttribute.
        :type feature_set: str
        """
        self._feature_set = feature_set

    @property
    def expected_repair_date(self):
        r"""Gets the expected_repair_date of this IssueUpdateAttribute.

        **参数解释**： 期望修复时间。预设字段中，仅Bug有此字段，unix时间戳，单位：毫秒。 **约束限制**： 不涉及。 **取值范围**： 11~19个字符。 **默认取值**： 不涉及。

        :return: The expected_repair_date of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._expected_repair_date

    @expected_repair_date.setter
    def expected_repair_date(self, expected_repair_date):
        r"""Sets the expected_repair_date of this IssueUpdateAttribute.

        **参数解释**： 期望修复时间。预设字段中，仅Bug有此字段，unix时间戳，单位：毫秒。 **约束限制**： 不涉及。 **取值范围**： 11~19个字符。 **默认取值**： 不涉及。

        :param expected_repair_date: The expected_repair_date of this IssueUpdateAttribute.
        :type expected_repair_date: str
        """
        self._expected_repair_date = expected_repair_date

    @property
    def found_pi(self):
        r"""Gets the found_pi of this IssueUpdateAttribute.

        **参数解释**： 缺陷发现发布计划ID，预设字段中，仅Bug有此字段。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category=PI的对象的**id**字段就是迭代计划的ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :return: The found_pi of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._found_pi

    @found_pi.setter
    def found_pi(self, found_pi):
        r"""Sets the found_pi of this IssueUpdateAttribute.

        **参数解释**： 缺陷发现发布计划ID，预设字段中，仅Bug有此字段。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category=PI的对象的**id**字段就是迭代计划的ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :param found_pi: The found_pi of this IssueUpdateAttribute.
        :type found_pi: str
        """
        self._found_pi = found_pi

    @property
    def found_iteration(self):
        r"""Gets the found_iteration of this IssueUpdateAttribute.

        **参数解释**： 缺陷发现迭代计划ID，预设字段中，仅Bug有此字段。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category=Iteration的对象的**id**字段就是迭代计划的ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :return: The found_iteration of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._found_iteration

    @found_iteration.setter
    def found_iteration(self, found_iteration):
        r"""Sets the found_iteration of this IssueUpdateAttribute.

        **参数解释**： 缺陷发现迭代计划ID，预设字段中，仅Bug有此字段。通过[发布/迭代计划列表查询](ListPlan.xml)接口查询计划列表，返回参数中PlanVO里面的category=Iteration的对象的**id**字段就是迭代计划的ID。 **约束限制**： 不涉及。 **取值范围**： 18~19个字符的数字字符串。 **默认取值**： 不涉及。

        :param found_iteration: The found_iteration of this IssueUpdateAttribute.
        :type found_iteration: str
        """
        self._found_iteration = found_iteration

    @property
    def reason_analysis(self):
        r"""Gets the reason_analysis of this IssueUpdateAttribute.

        **参数解释**： 分析原因。 **约束限制**： 预设字段中，仅Bug有此字段。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :return: The reason_analysis of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._reason_analysis

    @reason_analysis.setter
    def reason_analysis(self, reason_analysis):
        r"""Sets the reason_analysis of this IssueUpdateAttribute.

        **参数解释**： 分析原因。 **约束限制**： 预设字段中，仅Bug有此字段。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :param reason_analysis: The reason_analysis of this IssueUpdateAttribute.
        :type reason_analysis: str
        """
        self._reason_analysis = reason_analysis

    @property
    def repair_solution(self):
        r"""Gets the repair_solution of this IssueUpdateAttribute.

        **参数解释**： 修复方案。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :return: The repair_solution of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._repair_solution

    @repair_solution.setter
    def repair_solution(self, repair_solution):
        r"""Sets the repair_solution of this IssueUpdateAttribute.

        **参数解释**： 修复方案。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :param repair_solution: The repair_solution of this IssueUpdateAttribute.
        :type repair_solution: str
        """
        self._repair_solution = repair_solution

    @property
    def test_report(self):
        r"""Gets the test_report of this IssueUpdateAttribute.

        **参数解释**： 测试报告。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :return: The test_report of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._test_report

    @test_report.setter
    def test_report(self, test_report):
        r"""Sets the test_report of this IssueUpdateAttribute.

        **参数解释**： 测试报告。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :param test_report: The test_report of this IssueUpdateAttribute.
        :type test_report: str
        """
        self._test_report = test_report

    @property
    def sys_no_repair_reason(self):
        r"""Gets the sys_no_repair_reason of this IssueUpdateAttribute.

        **参数解释**： 无需修复原因。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :return: The sys_no_repair_reason of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._sys_no_repair_reason

    @sys_no_repair_reason.setter
    def sys_no_repair_reason(self, sys_no_repair_reason):
        r"""Sets the sys_no_repair_reason of this IssueUpdateAttribute.

        **参数解释**： 无需修复原因。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :param sys_no_repair_reason: The sys_no_repair_reason of this IssueUpdateAttribute.
        :type sys_no_repair_reason: str
        """
        self._sys_no_repair_reason = sys_no_repair_reason

    @property
    def sys_activation_reason(self):
        r"""Gets the sys_activation_reason of this IssueUpdateAttribute.

        **参数解释**： 激活原因。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :return: The sys_activation_reason of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._sys_activation_reason

    @sys_activation_reason.setter
    def sys_activation_reason(self, sys_activation_reason):
        r"""Sets the sys_activation_reason of this IssueUpdateAttribute.

        **参数解释**： 激活原因。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :param sys_activation_reason: The sys_activation_reason of this IssueUpdateAttribute.
        :type sys_activation_reason: str
        """
        self._sys_activation_reason = sys_activation_reason

    @property
    def sys_return_reason(self):
        r"""Gets the sys_return_reason of this IssueUpdateAttribute.

        **参数解释**： 退回原因。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :return: The sys_return_reason of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._sys_return_reason

    @sys_return_reason.setter
    def sys_return_reason(self, sys_return_reason):
        r"""Sets the sys_return_reason of this IssueUpdateAttribute.

        **参数解释**： 退回原因。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :param sys_return_reason: The sys_return_reason of this IssueUpdateAttribute.
        :type sys_return_reason: str
        """
        self._sys_return_reason = sys_return_reason

    @property
    def test_failures_times(self):
        r"""Gets the test_failures_times of this IssueUpdateAttribute.

        **参数解释**： 回归不通过次数。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~999999。 **默认取值**： 不涉及。

        :return: The test_failures_times of this IssueUpdateAttribute.
        :rtype: int
        """
        return self._test_failures_times

    @test_failures_times.setter
    def test_failures_times(self, test_failures_times):
        r"""Sets the test_failures_times of this IssueUpdateAttribute.

        **参数解释**： 回归不通过次数。预设字段中，仅Bug有此字段。 **约束限制**： 不涉及。 **取值范围**： 0~999999。 **默认取值**： 不涉及。

        :param test_failures_times: The test_failures_times of this IssueUpdateAttribute.
        :type test_failures_times: int
        """
        self._test_failures_times = test_failures_times

    @property
    def close_type(self):
        r"""Gets the close_type of this IssueUpdateAttribute.

        **参数解释**： 关闭类型。 **约束限制**： 不涉及。 **取值范围**： - problem_solved：问题解决关闭 - problem_to_requirement：问题转需求关闭 - duplicate_problem：重复问题关闭 - not_a_problem：非问题关闭 **默认取值**： 不涉及。

        :return: The close_type of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._close_type

    @close_type.setter
    def close_type(self, close_type):
        r"""Sets the close_type of this IssueUpdateAttribute.

        **参数解释**： 关闭类型。 **约束限制**： 不涉及。 **取值范围**： - problem_solved：问题解决关闭 - problem_to_requirement：问题转需求关闭 - duplicate_problem：重复问题关闭 - not_a_problem：非问题关闭 **默认取值**： 不涉及。

        :param close_type: The close_type of this IssueUpdateAttribute.
        :type close_type: str
        """
        self._close_type = close_type

    @property
    def security_level(self):
        r"""Gets the security_level of this IssueUpdateAttribute.

        **参数解释**： 密级。低密级权限者不能访问高密级的工作项。可以通过[查询字段列表](ListIpdProjectFields.xml)接口获取，响应消息体中密级的**option**字段的值就是密级字段的可选值。 **约束限制**： 仅在涉密环境（SM）下存在此字段，非涉密环境下无此字段。涉密环境下必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The security_level of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this IssueUpdateAttribute.

        **参数解释**： 密级。低密级权限者不能访问高密级的工作项。可以通过[查询字段列表](ListIpdProjectFields.xml)接口获取，响应消息体中密级的**option**字段的值就是密级字段的可选值。 **约束限制**： 仅在涉密环境（SM）下存在此字段，非涉密环境下无此字段。涉密环境下必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param security_level: The security_level of this IssueUpdateAttribute.
        :type security_level: str
        """
        self._security_level = security_level

    @property
    def plan_owner(self):
        r"""Gets the plan_owner of this IssueUpdateAttribute.

        :return: The plan_owner of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._plan_owner

    @plan_owner.setter
    def plan_owner(self, plan_owner):
        r"""Sets the plan_owner of this IssueUpdateAttribute.

        :param plan_owner: The plan_owner of this IssueUpdateAttribute.
        :type plan_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._plan_owner = plan_owner

    @property
    def doing_owner(self):
        r"""Gets the doing_owner of this IssueUpdateAttribute.

        :return: The doing_owner of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._doing_owner

    @doing_owner.setter
    def doing_owner(self, doing_owner):
        r"""Sets the doing_owner of this IssueUpdateAttribute.

        :param doing_owner: The doing_owner of this IssueUpdateAttribute.
        :type doing_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._doing_owner = doing_owner

    @property
    def delivered_owner(self):
        r"""Gets the delivered_owner of this IssueUpdateAttribute.

        :return: The delivered_owner of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._delivered_owner

    @delivered_owner.setter
    def delivered_owner(self, delivered_owner):
        r"""Sets the delivered_owner of this IssueUpdateAttribute.

        :param delivered_owner: The delivered_owner of this IssueUpdateAttribute.
        :type delivered_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._delivered_owner = delivered_owner

    @property
    def checking_owner(self):
        r"""Gets the checking_owner of this IssueUpdateAttribute.

        :return: The checking_owner of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._checking_owner

    @checking_owner.setter
    def checking_owner(self, checking_owner):
        r"""Sets the checking_owner of this IssueUpdateAttribute.

        :param checking_owner: The checking_owner of this IssueUpdateAttribute.
        :type checking_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._checking_owner = checking_owner

    @property
    def test_owner(self):
        r"""Gets the test_owner of this IssueUpdateAttribute.

        :return: The test_owner of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._test_owner

    @test_owner.setter
    def test_owner(self, test_owner):
        r"""Sets the test_owner of this IssueUpdateAttribute.

        :param test_owner: The test_owner of this IssueUpdateAttribute.
        :type test_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._test_owner = test_owner

    @property
    def develop_owner(self):
        r"""Gets the develop_owner of this IssueUpdateAttribute.

        :return: The develop_owner of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._develop_owner

    @develop_owner.setter
    def develop_owner(self, develop_owner):
        r"""Sets the develop_owner of this IssueUpdateAttribute.

        :param develop_owner: The develop_owner of this IssueUpdateAttribute.
        :type develop_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._develop_owner = develop_owner

    @property
    def processing_owner(self):
        r"""Gets the processing_owner of this IssueUpdateAttribute.

        :return: The processing_owner of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._processing_owner

    @processing_owner.setter
    def processing_owner(self, processing_owner):
        r"""Sets the processing_owner of this IssueUpdateAttribute.

        :param processing_owner: The processing_owner of this IssueUpdateAttribute.
        :type processing_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._processing_owner = processing_owner

    @property
    def fixed_owner(self):
        r"""Gets the fixed_owner of this IssueUpdateAttribute.

        :return: The fixed_owner of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._fixed_owner

    @fixed_owner.setter
    def fixed_owner(self, fixed_owner):
        r"""Sets the fixed_owner of this IssueUpdateAttribute.

        :param fixed_owner: The fixed_owner of this IssueUpdateAttribute.
        :type fixed_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._fixed_owner = fixed_owner

    @property
    def researchanddevelop_owner(self):
        r"""Gets the researchanddevelop_owner of this IssueUpdateAttribute.

        :return: The researchanddevelop_owner of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._researchanddevelop_owner

    @researchanddevelop_owner.setter
    def researchanddevelop_owner(self, researchanddevelop_owner):
        r"""Sets the researchanddevelop_owner of this IssueUpdateAttribute.

        :param researchanddevelop_owner: The researchanddevelop_owner of this IssueUpdateAttribute.
        :type researchanddevelop_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._researchanddevelop_owner = researchanddevelop_owner

    @property
    def analyse_owner(self):
        r"""Gets the analyse_owner of this IssueUpdateAttribute.

        :return: The analyse_owner of this IssueUpdateAttribute.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        return self._analyse_owner

    @analyse_owner.setter
    def analyse_owner(self, analyse_owner):
        r"""Sets the analyse_owner of this IssueUpdateAttribute.

        :param analyse_owner: The analyse_owner of this IssueUpdateAttribute.
        :type analyse_owner: :class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`
        """
        self._analyse_owner = analyse_owner

    @property
    def plan_start_date(self):
        r"""Gets the plan_start_date of this IssueUpdateAttribute.

        **参数解释**： 计划开始时间。工作项的计划启动日期，用于项目进度管理和排期。 **约束限制**： 不涉及。 **取值范围**： 11~19个字符的时间戳字符串，单位为毫秒（ms）。 **默认取值**： 不涉及。

        :return: The plan_start_date of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        r"""Sets the plan_start_date of this IssueUpdateAttribute.

        **参数解释**： 计划开始时间。工作项的计划启动日期，用于项目进度管理和排期。 **约束限制**： 不涉及。 **取值范围**： 11~19个字符的时间戳字符串，单位为毫秒（ms）。 **默认取值**： 不涉及。

        :param plan_start_date: The plan_start_date of this IssueUpdateAttribute.
        :type plan_start_date: str
        """
        self._plan_start_date = plan_start_date

    @property
    def expect_delivery_time(self):
        r"""Gets the expect_delivery_time of this IssueUpdateAttribute.

        **参数解释**： 期望完成时间。工作项的预期交付日期，用于跟踪工作项是否按期完成。 **约束限制**： 不涉及。 **取值范围**： 11~19个字符的时间戳字符串，单位为毫秒（ms）。 **默认取值**： 不涉及。

        :return: The expect_delivery_time of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._expect_delivery_time

    @expect_delivery_time.setter
    def expect_delivery_time(self, expect_delivery_time):
        r"""Sets the expect_delivery_time of this IssueUpdateAttribute.

        **参数解释**： 期望完成时间。工作项的预期交付日期，用于跟踪工作项是否按期完成。 **约束限制**： 不涉及。 **取值范围**： 11~19个字符的时间戳字符串，单位为毫秒（ms）。 **默认取值**： 不涉及。

        :param expect_delivery_time: The expect_delivery_time of this IssueUpdateAttribute.
        :type expect_delivery_time: str
        """
        self._expect_delivery_time = expect_delivery_time

    @property
    def plan_test_end_date(self):
        r"""Gets the plan_test_end_date of this IssueUpdateAttribute.

        **参数解释**： 计划测试结束时间。Bug类型工作项的计划测试完成日期，用于跟踪Bug修复后的测试进度。 **约束限制**： 仅对Bug类型工作项生效，非Bug类型忽略此字段。 **取值范围**： 11~19个字符的时间戳字符串，单位为毫秒（ms）。 **默认取值**： 不涉及。

        :return: The plan_test_end_date of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._plan_test_end_date

    @plan_test_end_date.setter
    def plan_test_end_date(self, plan_test_end_date):
        r"""Sets the plan_test_end_date of this IssueUpdateAttribute.

        **参数解释**： 计划测试结束时间。Bug类型工作项的计划测试完成日期，用于跟踪Bug修复后的测试进度。 **约束限制**： 仅对Bug类型工作项生效，非Bug类型忽略此字段。 **取值范围**： 11~19个字符的时间戳字符串，单位为毫秒（ms）。 **默认取值**： 不涉及。

        :param plan_test_end_date: The plan_test_end_date of this IssueUpdateAttribute.
        :type plan_test_end_date: str
        """
        self._plan_test_end_date = plan_test_end_date

    @property
    def severity(self):
        r"""Gets the severity of this IssueUpdateAttribute.

        **参数解释**： 严重程度。Bug类型工作项的严重级别，用于评估Bug的影响范围和修复优先级。 **约束限制**： 仅对Bug类型工作项生效，非Bug类型忽略此字段。 **取值范围**： - 致命：系统崩溃、数据丢失等严重影响 - 严重：主要功能无法使用 - 一般：次要功能异常，有替代方案 - 提示：界面优化、建议性问题 **默认取值**： 不涉及。

        :return: The severity of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this IssueUpdateAttribute.

        **参数解释**： 严重程度。Bug类型工作项的严重级别，用于评估Bug的影响范围和修复优先级。 **约束限制**： 仅对Bug类型工作项生效，非Bug类型忽略此字段。 **取值范围**： - 致命：系统崩溃、数据丢失等严重影响 - 严重：主要功能无法使用 - 一般：次要功能异常，有替代方案 - 提示：界面优化、建议性问题 **默认取值**： 不涉及。

        :param severity: The severity of this IssueUpdateAttribute.
        :type severity: str
        """
        self._severity = severity

    @property
    def promised(self):
        r"""Gets the promised of this IssueUpdateAttribute.

        **参数解释**： 是否承诺。RR（原始需求）类型工作项的承诺状态标识，用于标记需求是否已承诺交付。 **约束限制**： 仅对RR类型工作项生效，非RR类型忽略此字段。 **取值范围**： - yes：已承诺 - no：未承诺 **默认取值**： 不涉及。

        :return: The promised of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._promised

    @promised.setter
    def promised(self, promised):
        r"""Sets the promised of this IssueUpdateAttribute.

        **参数解释**： 是否承诺。RR（原始需求）类型工作项的承诺状态标识，用于标记需求是否已承诺交付。 **约束限制**： 仅对RR类型工作项生效，非RR类型忽略此字段。 **取值范围**： - yes：已承诺 - no：未承诺 **默认取值**： 不涉及。

        :param promised: The promised of this IssueUpdateAttribute.
        :type promised: str
        """
        self._promised = promised

    @property
    def recipient(self):
        r"""Gets the recipient of this IssueUpdateAttribute.

        **参数解释**： 承接人。RR（原始需求）类型工作项的需求承接责任人，负责需求的分析和转化。 **约束限制**： 仅对RR类型工作项生效，非RR类型忽略此字段。

        :return: The recipient of this IssueUpdateAttribute.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`]
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        r"""Sets the recipient of this IssueUpdateAttribute.

        **参数解释**： 承接人。RR（原始需求）类型工作项的需求承接责任人，负责需求的分析和转化。 **约束限制**： 仅对RR类型工作项生效，非RR类型忽略此字段。

        :param recipient: The recipient of this IssueUpdateAttribute.
        :type recipient: list[:class:`huaweicloudsdkprojectman.v4.UserUpdateAttribute`]
        """
        self._recipient = recipient

    @property
    def sys_no_develop_reason(self):
        r"""Gets the sys_no_develop_reason of this IssueUpdateAttribute.

        **参数解释**： 无需研发原因。RR（原始需求）类型工作项不需要进行研发的原因说明。 **约束限制**： 仅对RR类型工作项生效，非RR类型忽略此字段。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :return: The sys_no_develop_reason of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._sys_no_develop_reason

    @sys_no_develop_reason.setter
    def sys_no_develop_reason(self, sys_no_develop_reason):
        r"""Sets the sys_no_develop_reason of this IssueUpdateAttribute.

        **参数解释**： 无需研发原因。RR（原始需求）类型工作项不需要进行研发的原因说明。 **约束限制**： 仅对RR类型工作项生效，非RR类型忽略此字段。 **取值范围**： 0~50000个字符。 **默认取值**： 不涉及。

        :param sys_no_develop_reason: The sys_no_develop_reason of this IssueUpdateAttribute.
        :type sys_no_develop_reason: str
        """
        self._sys_no_develop_reason = sys_no_develop_reason

    @property
    def val_feature(self):
        r"""Gets the val_feature of this IssueUpdateAttribute.

        **参数解释**： 价值特性。SF/FE类型工作项对应的业务价值特性描述，用于关联业务价值和技术实现。 **约束限制**： 仅对SF/FE类型工作项生效，其他类型忽略此字段。 **取值范围**： - yes：是 - no：否 **默认取值**： 不涉及。

        :return: The val_feature of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._val_feature

    @val_feature.setter
    def val_feature(self, val_feature):
        r"""Sets the val_feature of this IssueUpdateAttribute.

        **参数解释**： 价值特性。SF/FE类型工作项对应的业务价值特性描述，用于关联业务价值和技术实现。 **约束限制**： 仅对SF/FE类型工作项生效，其他类型忽略此字段。 **取值范围**： - yes：是 - no：否 **默认取值**： 不涉及。

        :param val_feature: The val_feature of this IssueUpdateAttribute.
        :type val_feature: str
        """
        self._val_feature = val_feature

    @property
    def function_scene(self):
        r"""Gets the function_scene of this IssueUpdateAttribute.

        **参数解释**： 功能场景。SF/FE类型工作项的功能应用场景描述，用于说明特性的使用场景和用户故事。 **约束限制**： 仅对SF/FE类型工作项生效，其他类型忽略此字段。 **取值范围**： 0~512个字符。 **默认取值**： 不涉及。

        :return: The function_scene of this IssueUpdateAttribute.
        :rtype: str
        """
        return self._function_scene

    @function_scene.setter
    def function_scene(self, function_scene):
        r"""Sets the function_scene of this IssueUpdateAttribute.

        **参数解释**： 功能场景。SF/FE类型工作项的功能应用场景描述，用于说明特性的使用场景和用户故事。 **约束限制**： 仅对SF/FE类型工作项生效，其他类型忽略此字段。 **取值范围**： 0~512个字符。 **默认取值**： 不涉及。

        :param function_scene: The function_scene of this IssueUpdateAttribute.
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
        if not isinstance(other, IssueUpdateAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
