# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sys_analysis_conclusion': 'str',
        'sys_remark': 'str',
        'promised': 'OptionVO',
        'type': 'str',
        'belong_inside': 'str',
        'src_domain': 'DomainVO',
        'domain_id': 'DomainVO',
        'send_from': 'str',
        'number': 'str',
        'send_to': 'str',
        'path': 'str',
        'workload_man_day': 'str',
        'sys_check_conclusion': 'str',
        'id': 'str',
        'state': 'str',
        'stay_days': 'int',
        'assigned_cc': 'list[UserVO]',
        'submit_time': 'str',
        'workitem2label': 'list[WorkItemLabelVO]',
        'sys_return_conclusion': 'str',
        'close_time': 'str',
        'priority': 'OptionVO',
        'modified_date': 'str',
        'created_by': 'UserVO',
        'break_status': 'OptionVO',
        'status_modified_date': 'str',
        'expect_delivery_time': 'str',
        'parent_id': 'str',
        'assignee': 'UserVO',
        'region': 'str',
        'status': 'AlmStatus',
        'tenant_id': 'str',
        'plan_pi': 'PlanVO',
        'link': 'str',
        'description': 'str',
        'is_suspended': 'OptionVO',
        'change_status': 'OptionVO',
        'title': 'str',
        'sum_workload_man_day': 'str',
        'sys_close_reason': 'str',
        'sys_resubmit_reason': 'str',
        'plan_end_date': 'str',
        'rr2ir': 'str',
        'category_layer_id': 'str',
        'submitted_by': 'list[UserVO]',
        'rr2us': 'str',
        'sys_no_develop_reason': 'str',
        'plan_iteration': 'PlanVO',
        'sys_return_reason': 'str',
        'cascade_delete': 'str',
        'recipient': 'list[UserVO]',
        'modified_by': 'UserVO',
        'created_date': 'str',
        'category': 'str',
        'collaborative_status': 'list[str]',
        'project': 'DomainVO',
        'child_issues': 'dict(str, IssueVO)',
        'activate_times': 'int',
        'baseline': 'OptionVO',
        'business_domain': 'OptionVO',
        'children': 'str',
        'collaborative_history': 'str',
        'collaboratives': 'str',
        'convolution_actual_hours': 'str',
        'convolution_plan_hours': 'str',
        'develop_owner': 'str',
        'done_ratio': 'OptionVO',
        'expected_repair_date': 'str',
        'feature2ir': 'str',
        'feature_set': 'OptionVO',
        'found_env': 'OptionVO',
        'found_iteration': 'PlanVO',
        'found_pi': 'PlanVO',
        'function_scene': 'str',
        'ir2feature': 'str',
        'ir2rr': 'str',
        'issue_opinion_id': 'str',
        'issue_review_id': 'str',
        'module': 'OptionVO',
        'need_break': 'OptionVO',
        'need_develop': 'OptionVO',
        'no_break_reason': 'str',
        'no_develop_reason': 'str',
        'order': 'str',
        'plan_dev_end_date': 'str',
        'plan_processing_end_date': 'str',
        'plan_researchanddevelop_end_date': 'str',
        'plan_test_end_date': 'str',
        'position_float': 'str',
        'processing_owner': 'str',
        'reason_analysis': 'str',
        'regression_failure_number': 'int',
        'related_network_security': 'OptionVO',
        'repair_solution': 'str',
        'researchanddevelop_owner': 'str',
        'severity': 'OptionVO',
        'sys_activation_reason': 'str',
        'sys_no_repair_reason': 'str',
        'test_failures_times': 'int',
        'test_owner': 'str',
        'test_report': 'str',
        'val_feature': 'OptionVO',
        'workitem2ganttchart': 'str',
        'workitem2mindmap': 'str'
    }

    attribute_map = {
        'sys_analysis_conclusion': 'sys_analysis_conclusion',
        'sys_remark': 'sys_remark',
        'promised': 'promised',
        'type': 'type',
        'belong_inside': 'belong_inside',
        'src_domain': 'src_domain',
        'domain_id': 'domain_id',
        'send_from': 'send_from',
        'number': 'number',
        'send_to': 'send_to',
        'path': 'path',
        'workload_man_day': 'workload_man_day',
        'sys_check_conclusion': 'sys_check_conclusion',
        'id': 'id',
        'state': 'state',
        'stay_days': 'stay_days',
        'assigned_cc': 'assigned_cc',
        'submit_time': 'submit_time',
        'workitem2label': 'workitem2label',
        'sys_return_conclusion': 'sys_return_conclusion',
        'close_time': 'close_time',
        'priority': 'priority',
        'modified_date': 'modified_date',
        'created_by': 'created_by',
        'break_status': 'break_status',
        'status_modified_date': 'status_modified_date',
        'expect_delivery_time': 'expect_delivery_time',
        'parent_id': 'parent_id',
        'assignee': 'assignee',
        'region': 'region',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'plan_pi': 'plan_pi',
        'link': 'link',
        'description': 'description',
        'is_suspended': 'is_suspended',
        'change_status': 'change_status',
        'title': 'title',
        'sum_workload_man_day': 'sum_workload_man_day',
        'sys_close_reason': 'sys_close_reason',
        'sys_resubmit_reason': 'sys_resubmit_reason',
        'plan_end_date': 'plan_end_date',
        'rr2ir': 'rr2ir',
        'category_layer_id': 'category_layer_id',
        'submitted_by': 'submitted_by',
        'rr2us': 'rr2us',
        'sys_no_develop_reason': 'sys_no_develop_reason',
        'plan_iteration': 'plan_iteration',
        'sys_return_reason': 'sys_return_reason',
        'cascade_delete': 'cascade_delete',
        'recipient': 'recipient',
        'modified_by': 'modified_by',
        'created_date': 'created_date',
        'category': 'category',
        'collaborative_status': 'collaborative_status',
        'project': 'project',
        'child_issues': 'child_issues',
        'activate_times': 'activate_times',
        'baseline': 'baseline',
        'business_domain': 'business_domain',
        'children': 'children',
        'collaborative_history': 'collaborative_history',
        'collaboratives': 'collaboratives',
        'convolution_actual_hours': 'convolution_actual_hours',
        'convolution_plan_hours': 'convolution_plan_hours',
        'develop_owner': 'develop_owner',
        'done_ratio': 'done_ratio',
        'expected_repair_date': 'expected_repair_date',
        'feature2ir': 'feature2ir',
        'feature_set': 'feature_set',
        'found_env': 'found_env',
        'found_iteration': 'found_iteration',
        'found_pi': 'found_pi',
        'function_scene': 'function_scene',
        'ir2feature': 'ir2feature',
        'ir2rr': 'ir2rr',
        'issue_opinion_id': 'issue_opinion_id',
        'issue_review_id': 'issue_review_id',
        'module': 'module',
        'need_break': 'need_break',
        'need_develop': 'need_develop',
        'no_break_reason': 'no_break_reason',
        'no_develop_reason': 'no_develop_reason',
        'order': 'order',
        'plan_dev_end_date': 'plan_dev_end_date',
        'plan_processing_end_date': 'plan_processing_end_date',
        'plan_researchanddevelop_end_date': 'plan_researchanddevelop_end_date',
        'plan_test_end_date': 'plan_test_end_date',
        'position_float': 'position_float',
        'processing_owner': 'processing_owner',
        'reason_analysis': 'reason_analysis',
        'regression_failure_number': 'regression_failure_number',
        'related_network_security': 'related_network_security',
        'repair_solution': 'repair_solution',
        'researchanddevelop_owner': 'researchanddevelop_owner',
        'severity': 'severity',
        'sys_activation_reason': 'sys_activation_reason',
        'sys_no_repair_reason': 'sys_no_repair_reason',
        'test_failures_times': 'test_failures_times',
        'test_owner': 'test_owner',
        'test_report': 'test_report',
        'val_feature': 'val_feature',
        'workitem2ganttchart': 'workitem2ganttchart',
        'workitem2mindmap': 'workitem2mindmap'
    }

    def __init__(self, sys_analysis_conclusion=None, sys_remark=None, promised=None, type=None, belong_inside=None, src_domain=None, domain_id=None, send_from=None, number=None, send_to=None, path=None, workload_man_day=None, sys_check_conclusion=None, id=None, state=None, stay_days=None, assigned_cc=None, submit_time=None, workitem2label=None, sys_return_conclusion=None, close_time=None, priority=None, modified_date=None, created_by=None, break_status=None, status_modified_date=None, expect_delivery_time=None, parent_id=None, assignee=None, region=None, status=None, tenant_id=None, plan_pi=None, link=None, description=None, is_suspended=None, change_status=None, title=None, sum_workload_man_day=None, sys_close_reason=None, sys_resubmit_reason=None, plan_end_date=None, rr2ir=None, category_layer_id=None, submitted_by=None, rr2us=None, sys_no_develop_reason=None, plan_iteration=None, sys_return_reason=None, cascade_delete=None, recipient=None, modified_by=None, created_date=None, category=None, collaborative_status=None, project=None, child_issues=None, activate_times=None, baseline=None, business_domain=None, children=None, collaborative_history=None, collaboratives=None, convolution_actual_hours=None, convolution_plan_hours=None, develop_owner=None, done_ratio=None, expected_repair_date=None, feature2ir=None, feature_set=None, found_env=None, found_iteration=None, found_pi=None, function_scene=None, ir2feature=None, ir2rr=None, issue_opinion_id=None, issue_review_id=None, module=None, need_break=None, need_develop=None, no_break_reason=None, no_develop_reason=None, order=None, plan_dev_end_date=None, plan_processing_end_date=None, plan_researchanddevelop_end_date=None, plan_test_end_date=None, position_float=None, processing_owner=None, reason_analysis=None, regression_failure_number=None, related_network_security=None, repair_solution=None, researchanddevelop_owner=None, severity=None, sys_activation_reason=None, sys_no_repair_reason=None, test_failures_times=None, test_owner=None, test_report=None, val_feature=None, workitem2ganttchart=None, workitem2mindmap=None):
        r"""IssueVO

        The model defined in huaweicloud sdk

        :param sys_analysis_conclusion: **参数解释：**  分析结论，通常在接纳RR时填写。 **取值范围：**  不涉及。
        :type sys_analysis_conclusion: str
        :param sys_remark: **参数解释：**  备注。通常在提交验收RR时填写。 **取值范围：**  不涉及。
        :type sys_remark: str
        :param promised: 
        :type promised: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param type: **参数解释：**  工作项的分类。 **取值范围：**  - requirement - raw requirement - bug - task - feature
        :type type: str
        :param belong_inside: **参数解释：**  标识工作项是否跨项目提交。 **取值范围：**  - 1：跨项目提交工作项。 - 0：非跨项目提交工作项。
        :type belong_inside: str
        :param src_domain: 
        :type src_domain: :class:`huaweicloudsdkprojectman.v4.DomainVO`
        :param domain_id: 
        :type domain_id: :class:`huaweicloudsdkprojectman.v4.DomainVO`
        :param send_from: **参数解释：**  原始需求的协同上游需求Id。 **取值范围：**  不涉及。
        :type send_from: str
        :param number: **参数解释：**  工作项编号，由工作项类型+年月日+6位随机数组成。 **取值范围：**  不涉及。
        :type number: str
        :param send_to: **参数解释：**  原始需求的协同下游需求Id。 **取值范围：**  不涉及。
        :type send_to: str
        :param path: **参数解释：**  工作项父子挂载路径关系。 **取值范围：**  不涉及。
        :type path: str
        :param workload_man_day: **参数解释：**  工作项计划工时。 **取值范围：**  不涉及。
        :type workload_man_day: str
        :param sys_check_conclusion: **参数解释：**  验收结论。通常是验收RR时填写。 **取值范围：**  不涉及。
        :type sys_check_conclusion: str
        :param id: **参数解释：**  工作项唯一Id。 **取值范围：**  不涉及。
        :type id: str
        :param state: **参数解释：**  工作项生命周期。 **取值范围：**  - 正在工作：可正常操作的工作项； - 作废：软删除后的工作项，可在回收站恢复； - 删除：彻底删除后的工作项，无法恢复。
        :type state: str
        :param stay_days: **参数解释：**  工作项在当前状态的停留天数。 **取值范围：**  不涉及。
        :type stay_days: int
        :param assigned_cc: **参数解释：**  抄送人。 **取值范围：**  不涉及。
        :type assigned_cc: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        :param submit_time: **参数解释：**  工作项提交时间，指工作项进入工作流的时间，而不是创建时间。 **取值范围：**  不涉及。
        :type submit_time: str
        :param workitem2label: **参数解释：**  工作项标签。 **取值范围：**  不涉及。
        :type workitem2label: list[:class:`huaweicloudsdkprojectman.v4.WorkItemLabelVO`]
        :param sys_return_conclusion: **参数解释：**  退回原因。通常为退回RR/Bug时填写。 **取值范围：**  不涉及。
        :type sys_return_conclusion: str
        :param close_time: **参数解释：**  工作项完成时间。 **取值范围：**  不涉及。
        :type close_time: str
        :param priority: 
        :type priority: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param modified_date: **参数解释：**  工作项最新修改时间。 **取值范围：**  不涉及。
        :type modified_date: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param break_status: 
        :type break_status: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param status_modified_date: **参数解释：**  工作项上一次流转状态的时间，可用于计算停留天数。unix时间戳，单位为毫秒。 **取值范围：**  不涉及。
        :type status_modified_date: str
        :param expect_delivery_time: **参数解释：**  期望完成时间。Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。
        :type expect_delivery_time: str
        :param parent_id: **参数解释：**  工作项的父工作项Id。 **取值范围：**  不涉及。
        :type parent_id: str
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param region: **参数解释：**  工作项所属租户的域。 **取值范围：**  不涉及。
        :type region: str
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.AlmStatus`
        :param tenant_id: **参数解释：**  工作项所属租户Id。 **取值范围：**  不涉及。
        :type tenant_id: str
        :param plan_pi: 
        :type plan_pi: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        :param link: **参数解释：**  关联工作项的关系字段。多值使用英文逗号分隔。 **取值范围：**  不涉及。
        :type link: str
        :param description: **参数解释：**  工作项描述，最多支持50w字符。 **取值范围：**  不涉及。
        :type description: str
        :param is_suspended: 
        :type is_suspended: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param change_status: 
        :type change_status: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param title: **参数解释：**  工作项标题。 **取值范围：**  不涉及。
        :type title: str
        :param sum_workload_man_day: **参数解释：**  工作项实际工时。 **取值范围：**  不涉及。
        :type sum_workload_man_day: str
        :param sys_close_reason: **参数解释：**  工作项关闭原因。 **取值范围：**  不涉及。
        :type sys_close_reason: str
        :param sys_resubmit_reason: **参数解释：**  重新提交原因，通常用于RR/Bug退回后重新提交。 **取值范围：**  不涉及。
        :type sys_resubmit_reason: str
        :param plan_end_date: **参数解释：**  工作项计划完成时间。 **取值范围：**  不涉及。
        :type plan_end_date: str
        :param rr2ir: **参数解释：**  RR的子IR的id。多值使用英文逗号分隔。 **取值范围：**  不涉及。
        :type rr2ir: str
        :param category_layer_id: **参数解释：**  工作项类型层级id。 **取值范围：**  不涉及。
        :type category_layer_id: str
        :param submitted_by: **参数解释：**  工作项提交人。 **取值范围：**  不涉及。
        :type submitted_by: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        :param rr2us: **参数解释：**  RR的子US的id，多值使用英文逗号分隔。 **取值范围：**  不涉及。
        :type rr2us: str
        :param sys_no_develop_reason: **参数解释：**  工作项无需开发原因。 **取值范围：**  不涉及。
        :type sys_no_develop_reason: str
        :param plan_iteration: 
        :type plan_iteration: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        :param sys_return_reason: **参数解释：**  退回原因。通常用于RR/bug退回。 **取值范围：**  不涉及。
        :type sys_return_reason: str
        :param cascade_delete: **参数解释：**  是否级联删除标记。 **取值范围：**  不涉及。
        :type cascade_delete: str
        :param recipient: **参数解释：**  承接人。通常用于RR。 **取值范围：**  不涉及。
        :type recipient: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        :param modified_by: 
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param created_date: **参数解释：**  工作项创建时间。 **取值范围：**  不涉及。
        :type created_date: str
        :param category: **参数解释：**  工作项类型。 **取值范围：**  - 系统设备类项目：RR/SF/IR/SR/AR/Task/Bug。 - 独立软件类项目：RR/SF/IR/US/Task/Bug。 - 云服务类项目：RR/Epic/FE/US/Task/Bug。
        :type category: str
        :param collaborative_status: **参数解释：**  研发需求协同需求状态。 **取值范围：**  不涉及。
        :type collaborative_status: list[str]
        :param project: 
        :type project: :class:`huaweicloudsdkprojectman.v4.DomainVO`
        :param child_issues: **参数解释：**  子工作项列表。 **取值范围：**  不涉及。
        :type child_issues: dict(str, IssueVO)
        :param activate_times: **参数解释：**  激活次数。Bug激活时自动赋值。 **取值范围：**  不涉及。
        :type activate_times: int
        :param baseline: 
        :type baseline: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param business_domain: 
        :type business_domain: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param children: **参数解释：**  子工作项Id，多值使用英文逗号分隔。 **取值范围：**  不涉及。
        :type children: str
        :param collaborative_history: **参数解释：**  协同需求的状态变化历史记录，内容为Json字符串。 **取值范围：**  不涉及。
        :type collaborative_history: str
        :param collaboratives: **参数解释：**  协同需求中的记录Id。 **取值范围：**  不涉及。
        :type collaboratives: str
        :param convolution_actual_hours: **参数解释：**  卷积实际工时。父工作项中将子工作项/协同工作项的实际工时卷积得到。 **取值范围：**  不涉及。
        :type convolution_actual_hours: str
        :param convolution_plan_hours: **参数解释：**  卷积计划工时。父工作项中将子工作项/协同工作项的计划工时卷积得到。 **取值范围：**  不涉及。
        :type convolution_plan_hours: str
        :param develop_owner: **参数解释：**  开发责任人。通常用于“开发”状态节点责任人。 **取值范围：**  不涉及。
        :type develop_owner: str
        :param done_ratio: 
        :type done_ratio: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param expected_repair_date: **参数解释：**  期望修复时间。 **取值范围：**  不涉及。
        :type expected_repair_date: str
        :param feature2ir: **参数解释：**  SF的子IR的id。多值使用英文逗号分隔。 **取值范围：**  不涉及。
        :type feature2ir: str
        :param feature_set: 
        :type feature_set: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param found_env: 
        :type found_env: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param found_iteration: 
        :type found_iteration: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        :param found_pi: 
        :type found_pi: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        :param function_scene: **参数解释：**  功能场景。 **取值范围：**  不涉及。
        :type function_scene: str
        :param ir2feature: **参数解释：**  IR关联的SF的Id，一个IR仅能关联一个SF。 **取值范围：**  不涉及。
        :type ir2feature: str
        :param ir2rr: **参数解释：**  IR关联父RR的Id，多值使用英文逗号分隔。 **取值范围：**  不涉及。
        :type ir2rr: str
        :param issue_opinion_id: **参数解释：**  工作项关联的决策意见Id。 **取值范围：**  不涉及。
        :type issue_opinion_id: str
        :param issue_review_id: **参数解释：**  工作项关联的评审意见Id。 **取值范围：**  不涉及。
        :type issue_review_id: str
        :param module: 
        :type module: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param need_break: 
        :type need_break: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param need_develop: 
        :type need_develop: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param no_break_reason: **参数解释：**  无需分解原因。 **取值范围：**  不涉及。
        :type no_break_reason: str
        :param no_develop_reason: **参数解释：**  无需开发原因。 **取值范围：**  不涉及。
        :type no_develop_reason: str
        :param order: **参数解释：**  优先级顺序。 **取值范围：**  1~100。
        :type order: str
        :param plan_dev_end_date: **参数解释：**  计划开发结束时间。通常用于“开发”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。
        :type plan_dev_end_date: str
        :param plan_processing_end_date: **参数解释：**  计划处理中结束时间。通常用于“处理中”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。
        :type plan_processing_end_date: str
        :param plan_researchanddevelop_end_date: **参数解释：**  计划研发结束时间。通常用于“研发”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。
        :type plan_researchanddevelop_end_date: str
        :param plan_test_end_date: **参数解释：**  计划测试结束时间。通常用于“测试”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。
        :type plan_test_end_date: str
        :param position_float: **参数解释：**  标识工作项在列表中初始排序位置。 **取值范围：**  不涉及。
        :type position_float: str
        :param processing_owner: **参数解释：**  处理中责任人。通常用于“处理中”状态节点。 **取值范围：**  不涉及。
        :type processing_owner: str
        :param reason_analysis: **参数解释：**  分析原因。 **取值范围：**  不涉及。
        :type reason_analysis: str
        :param regression_failure_number: **参数解释：**  回归不通过次数。缺陷测试不通过时自动赋值。 **取值范围：**  不涉及。
        :type regression_failure_number: int
        :param related_network_security: 
        :type related_network_security: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param repair_solution: **参数解释：**  修复方案。常用于修复缺陷时。 **取值范围：**  不涉及。
        :type repair_solution: str
        :param researchanddevelop_owner: **参数解释：**  研发责任人。通常用于“研发”状态节点。 **取值范围：**  不涉及。
        :type researchanddevelop_owner: str
        :param severity: 
        :type severity: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param sys_activation_reason: **参数解释：**  严重程度。 **取值范围：**  不涉及。
        :type sys_activation_reason: str
        :param sys_no_repair_reason: **参数解释：**  无需修复原因。通常用于在缺陷无需修复时。 **取值范围：**  不涉及。
        :type sys_no_repair_reason: str
        :param test_failures_times: **参数解释：**  测试不通过次数。 **取值范围：**  不涉及。
        :type test_failures_times: int
        :param test_owner: **参数解释：**  测试责任人。通常用于“测试”状态节点。 **取值范围：**  不涉及。
        :type test_owner: str
        :param test_report: **参数解释：**  测试报告。 **取值范围：**  不涉及。
        :type test_report: str
        :param val_feature: 
        :type val_feature: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        :param workitem2ganttchart: **参数解释：**  工作项关联的甘特图Id。 **取值范围：**  不涉及。
        :type workitem2ganttchart: str
        :param workitem2mindmap: **参数解释：**  工作项关联的思维导图Id。 **取值范围：**  不涉及。
        :type workitem2mindmap: str
        """
        
        

        self._sys_analysis_conclusion = None
        self._sys_remark = None
        self._promised = None
        self._type = None
        self._belong_inside = None
        self._src_domain = None
        self._domain_id = None
        self._send_from = None
        self._number = None
        self._send_to = None
        self._path = None
        self._workload_man_day = None
        self._sys_check_conclusion = None
        self._id = None
        self._state = None
        self._stay_days = None
        self._assigned_cc = None
        self._submit_time = None
        self._workitem2label = None
        self._sys_return_conclusion = None
        self._close_time = None
        self._priority = None
        self._modified_date = None
        self._created_by = None
        self._break_status = None
        self._status_modified_date = None
        self._expect_delivery_time = None
        self._parent_id = None
        self._assignee = None
        self._region = None
        self._status = None
        self._tenant_id = None
        self._plan_pi = None
        self._link = None
        self._description = None
        self._is_suspended = None
        self._change_status = None
        self._title = None
        self._sum_workload_man_day = None
        self._sys_close_reason = None
        self._sys_resubmit_reason = None
        self._plan_end_date = None
        self._rr2ir = None
        self._category_layer_id = None
        self._submitted_by = None
        self._rr2us = None
        self._sys_no_develop_reason = None
        self._plan_iteration = None
        self._sys_return_reason = None
        self._cascade_delete = None
        self._recipient = None
        self._modified_by = None
        self._created_date = None
        self._category = None
        self._collaborative_status = None
        self._project = None
        self._child_issues = None
        self._activate_times = None
        self._baseline = None
        self._business_domain = None
        self._children = None
        self._collaborative_history = None
        self._collaboratives = None
        self._convolution_actual_hours = None
        self._convolution_plan_hours = None
        self._develop_owner = None
        self._done_ratio = None
        self._expected_repair_date = None
        self._feature2ir = None
        self._feature_set = None
        self._found_env = None
        self._found_iteration = None
        self._found_pi = None
        self._function_scene = None
        self._ir2feature = None
        self._ir2rr = None
        self._issue_opinion_id = None
        self._issue_review_id = None
        self._module = None
        self._need_break = None
        self._need_develop = None
        self._no_break_reason = None
        self._no_develop_reason = None
        self._order = None
        self._plan_dev_end_date = None
        self._plan_processing_end_date = None
        self._plan_researchanddevelop_end_date = None
        self._plan_test_end_date = None
        self._position_float = None
        self._processing_owner = None
        self._reason_analysis = None
        self._regression_failure_number = None
        self._related_network_security = None
        self._repair_solution = None
        self._researchanddevelop_owner = None
        self._severity = None
        self._sys_activation_reason = None
        self._sys_no_repair_reason = None
        self._test_failures_times = None
        self._test_owner = None
        self._test_report = None
        self._val_feature = None
        self._workitem2ganttchart = None
        self._workitem2mindmap = None
        self.discriminator = None

        if sys_analysis_conclusion is not None:
            self.sys_analysis_conclusion = sys_analysis_conclusion
        if sys_remark is not None:
            self.sys_remark = sys_remark
        if promised is not None:
            self.promised = promised
        if type is not None:
            self.type = type
        if belong_inside is not None:
            self.belong_inside = belong_inside
        if src_domain is not None:
            self.src_domain = src_domain
        if domain_id is not None:
            self.domain_id = domain_id
        if send_from is not None:
            self.send_from = send_from
        if number is not None:
            self.number = number
        if send_to is not None:
            self.send_to = send_to
        if path is not None:
            self.path = path
        if workload_man_day is not None:
            self.workload_man_day = workload_man_day
        if sys_check_conclusion is not None:
            self.sys_check_conclusion = sys_check_conclusion
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if stay_days is not None:
            self.stay_days = stay_days
        if assigned_cc is not None:
            self.assigned_cc = assigned_cc
        if submit_time is not None:
            self.submit_time = submit_time
        if workitem2label is not None:
            self.workitem2label = workitem2label
        if sys_return_conclusion is not None:
            self.sys_return_conclusion = sys_return_conclusion
        if close_time is not None:
            self.close_time = close_time
        if priority is not None:
            self.priority = priority
        if modified_date is not None:
            self.modified_date = modified_date
        if created_by is not None:
            self.created_by = created_by
        if break_status is not None:
            self.break_status = break_status
        if status_modified_date is not None:
            self.status_modified_date = status_modified_date
        if expect_delivery_time is not None:
            self.expect_delivery_time = expect_delivery_time
        if parent_id is not None:
            self.parent_id = parent_id
        if assignee is not None:
            self.assignee = assignee
        if region is not None:
            self.region = region
        if status is not None:
            self.status = status
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if plan_pi is not None:
            self.plan_pi = plan_pi
        if link is not None:
            self.link = link
        if description is not None:
            self.description = description
        if is_suspended is not None:
            self.is_suspended = is_suspended
        if change_status is not None:
            self.change_status = change_status
        if title is not None:
            self.title = title
        if sum_workload_man_day is not None:
            self.sum_workload_man_day = sum_workload_man_day
        if sys_close_reason is not None:
            self.sys_close_reason = sys_close_reason
        if sys_resubmit_reason is not None:
            self.sys_resubmit_reason = sys_resubmit_reason
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if rr2ir is not None:
            self.rr2ir = rr2ir
        if category_layer_id is not None:
            self.category_layer_id = category_layer_id
        if submitted_by is not None:
            self.submitted_by = submitted_by
        if rr2us is not None:
            self.rr2us = rr2us
        if sys_no_develop_reason is not None:
            self.sys_no_develop_reason = sys_no_develop_reason
        if plan_iteration is not None:
            self.plan_iteration = plan_iteration
        if sys_return_reason is not None:
            self.sys_return_reason = sys_return_reason
        if cascade_delete is not None:
            self.cascade_delete = cascade_delete
        if recipient is not None:
            self.recipient = recipient
        if modified_by is not None:
            self.modified_by = modified_by
        if created_date is not None:
            self.created_date = created_date
        if category is not None:
            self.category = category
        if collaborative_status is not None:
            self.collaborative_status = collaborative_status
        if project is not None:
            self.project = project
        if child_issues is not None:
            self.child_issues = child_issues
        if activate_times is not None:
            self.activate_times = activate_times
        if baseline is not None:
            self.baseline = baseline
        if business_domain is not None:
            self.business_domain = business_domain
        if children is not None:
            self.children = children
        if collaborative_history is not None:
            self.collaborative_history = collaborative_history
        if collaboratives is not None:
            self.collaboratives = collaboratives
        if convolution_actual_hours is not None:
            self.convolution_actual_hours = convolution_actual_hours
        if convolution_plan_hours is not None:
            self.convolution_plan_hours = convolution_plan_hours
        if develop_owner is not None:
            self.develop_owner = develop_owner
        if done_ratio is not None:
            self.done_ratio = done_ratio
        if expected_repair_date is not None:
            self.expected_repair_date = expected_repair_date
        if feature2ir is not None:
            self.feature2ir = feature2ir
        if feature_set is not None:
            self.feature_set = feature_set
        if found_env is not None:
            self.found_env = found_env
        if found_iteration is not None:
            self.found_iteration = found_iteration
        if found_pi is not None:
            self.found_pi = found_pi
        if function_scene is not None:
            self.function_scene = function_scene
        if ir2feature is not None:
            self.ir2feature = ir2feature
        if ir2rr is not None:
            self.ir2rr = ir2rr
        if issue_opinion_id is not None:
            self.issue_opinion_id = issue_opinion_id
        if issue_review_id is not None:
            self.issue_review_id = issue_review_id
        if module is not None:
            self.module = module
        if need_break is not None:
            self.need_break = need_break
        if need_develop is not None:
            self.need_develop = need_develop
        if no_break_reason is not None:
            self.no_break_reason = no_break_reason
        if no_develop_reason is not None:
            self.no_develop_reason = no_develop_reason
        if order is not None:
            self.order = order
        if plan_dev_end_date is not None:
            self.plan_dev_end_date = plan_dev_end_date
        if plan_processing_end_date is not None:
            self.plan_processing_end_date = plan_processing_end_date
        if plan_researchanddevelop_end_date is not None:
            self.plan_researchanddevelop_end_date = plan_researchanddevelop_end_date
        if plan_test_end_date is not None:
            self.plan_test_end_date = plan_test_end_date
        if position_float is not None:
            self.position_float = position_float
        if processing_owner is not None:
            self.processing_owner = processing_owner
        if reason_analysis is not None:
            self.reason_analysis = reason_analysis
        if regression_failure_number is not None:
            self.regression_failure_number = regression_failure_number
        if related_network_security is not None:
            self.related_network_security = related_network_security
        if repair_solution is not None:
            self.repair_solution = repair_solution
        if researchanddevelop_owner is not None:
            self.researchanddevelop_owner = researchanddevelop_owner
        if severity is not None:
            self.severity = severity
        if sys_activation_reason is not None:
            self.sys_activation_reason = sys_activation_reason
        if sys_no_repair_reason is not None:
            self.sys_no_repair_reason = sys_no_repair_reason
        if test_failures_times is not None:
            self.test_failures_times = test_failures_times
        if test_owner is not None:
            self.test_owner = test_owner
        if test_report is not None:
            self.test_report = test_report
        if val_feature is not None:
            self.val_feature = val_feature
        if workitem2ganttchart is not None:
            self.workitem2ganttchart = workitem2ganttchart
        if workitem2mindmap is not None:
            self.workitem2mindmap = workitem2mindmap

    @property
    def sys_analysis_conclusion(self):
        r"""Gets the sys_analysis_conclusion of this IssueVO.

        **参数解释：**  分析结论，通常在接纳RR时填写。 **取值范围：**  不涉及。

        :return: The sys_analysis_conclusion of this IssueVO.
        :rtype: str
        """
        return self._sys_analysis_conclusion

    @sys_analysis_conclusion.setter
    def sys_analysis_conclusion(self, sys_analysis_conclusion):
        r"""Sets the sys_analysis_conclusion of this IssueVO.

        **参数解释：**  分析结论，通常在接纳RR时填写。 **取值范围：**  不涉及。

        :param sys_analysis_conclusion: The sys_analysis_conclusion of this IssueVO.
        :type sys_analysis_conclusion: str
        """
        self._sys_analysis_conclusion = sys_analysis_conclusion

    @property
    def sys_remark(self):
        r"""Gets the sys_remark of this IssueVO.

        **参数解释：**  备注。通常在提交验收RR时填写。 **取值范围：**  不涉及。

        :return: The sys_remark of this IssueVO.
        :rtype: str
        """
        return self._sys_remark

    @sys_remark.setter
    def sys_remark(self, sys_remark):
        r"""Sets the sys_remark of this IssueVO.

        **参数解释：**  备注。通常在提交验收RR时填写。 **取值范围：**  不涉及。

        :param sys_remark: The sys_remark of this IssueVO.
        :type sys_remark: str
        """
        self._sys_remark = sys_remark

    @property
    def promised(self):
        r"""Gets the promised of this IssueVO.

        :return: The promised of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._promised

    @promised.setter
    def promised(self, promised):
        r"""Sets the promised of this IssueVO.

        :param promised: The promised of this IssueVO.
        :type promised: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._promised = promised

    @property
    def type(self):
        r"""Gets the type of this IssueVO.

        **参数解释：**  工作项的分类。 **取值范围：**  - requirement - raw requirement - bug - task - feature

        :return: The type of this IssueVO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IssueVO.

        **参数解释：**  工作项的分类。 **取值范围：**  - requirement - raw requirement - bug - task - feature

        :param type: The type of this IssueVO.
        :type type: str
        """
        self._type = type

    @property
    def belong_inside(self):
        r"""Gets the belong_inside of this IssueVO.

        **参数解释：**  标识工作项是否跨项目提交。 **取值范围：**  - 1：跨项目提交工作项。 - 0：非跨项目提交工作项。

        :return: The belong_inside of this IssueVO.
        :rtype: str
        """
        return self._belong_inside

    @belong_inside.setter
    def belong_inside(self, belong_inside):
        r"""Sets the belong_inside of this IssueVO.

        **参数解释：**  标识工作项是否跨项目提交。 **取值范围：**  - 1：跨项目提交工作项。 - 0：非跨项目提交工作项。

        :param belong_inside: The belong_inside of this IssueVO.
        :type belong_inside: str
        """
        self._belong_inside = belong_inside

    @property
    def src_domain(self):
        r"""Gets the src_domain of this IssueVO.

        :return: The src_domain of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.DomainVO`
        """
        return self._src_domain

    @src_domain.setter
    def src_domain(self, src_domain):
        r"""Sets the src_domain of this IssueVO.

        :param src_domain: The src_domain of this IssueVO.
        :type src_domain: :class:`huaweicloudsdkprojectman.v4.DomainVO`
        """
        self._src_domain = src_domain

    @property
    def domain_id(self):
        r"""Gets the domain_id of this IssueVO.

        :return: The domain_id of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.DomainVO`
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this IssueVO.

        :param domain_id: The domain_id of this IssueVO.
        :type domain_id: :class:`huaweicloudsdkprojectman.v4.DomainVO`
        """
        self._domain_id = domain_id

    @property
    def send_from(self):
        r"""Gets the send_from of this IssueVO.

        **参数解释：**  原始需求的协同上游需求Id。 **取值范围：**  不涉及。

        :return: The send_from of this IssueVO.
        :rtype: str
        """
        return self._send_from

    @send_from.setter
    def send_from(self, send_from):
        r"""Sets the send_from of this IssueVO.

        **参数解释：**  原始需求的协同上游需求Id。 **取值范围：**  不涉及。

        :param send_from: The send_from of this IssueVO.
        :type send_from: str
        """
        self._send_from = send_from

    @property
    def number(self):
        r"""Gets the number of this IssueVO.

        **参数解释：**  工作项编号，由工作项类型+年月日+6位随机数组成。 **取值范围：**  不涉及。

        :return: The number of this IssueVO.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this IssueVO.

        **参数解释：**  工作项编号，由工作项类型+年月日+6位随机数组成。 **取值范围：**  不涉及。

        :param number: The number of this IssueVO.
        :type number: str
        """
        self._number = number

    @property
    def send_to(self):
        r"""Gets the send_to of this IssueVO.

        **参数解释：**  原始需求的协同下游需求Id。 **取值范围：**  不涉及。

        :return: The send_to of this IssueVO.
        :rtype: str
        """
        return self._send_to

    @send_to.setter
    def send_to(self, send_to):
        r"""Sets the send_to of this IssueVO.

        **参数解释：**  原始需求的协同下游需求Id。 **取值范围：**  不涉及。

        :param send_to: The send_to of this IssueVO.
        :type send_to: str
        """
        self._send_to = send_to

    @property
    def path(self):
        r"""Gets the path of this IssueVO.

        **参数解释：**  工作项父子挂载路径关系。 **取值范围：**  不涉及。

        :return: The path of this IssueVO.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this IssueVO.

        **参数解释：**  工作项父子挂载路径关系。 **取值范围：**  不涉及。

        :param path: The path of this IssueVO.
        :type path: str
        """
        self._path = path

    @property
    def workload_man_day(self):
        r"""Gets the workload_man_day of this IssueVO.

        **参数解释：**  工作项计划工时。 **取值范围：**  不涉及。

        :return: The workload_man_day of this IssueVO.
        :rtype: str
        """
        return self._workload_man_day

    @workload_man_day.setter
    def workload_man_day(self, workload_man_day):
        r"""Sets the workload_man_day of this IssueVO.

        **参数解释：**  工作项计划工时。 **取值范围：**  不涉及。

        :param workload_man_day: The workload_man_day of this IssueVO.
        :type workload_man_day: str
        """
        self._workload_man_day = workload_man_day

    @property
    def sys_check_conclusion(self):
        r"""Gets the sys_check_conclusion of this IssueVO.

        **参数解释：**  验收结论。通常是验收RR时填写。 **取值范围：**  不涉及。

        :return: The sys_check_conclusion of this IssueVO.
        :rtype: str
        """
        return self._sys_check_conclusion

    @sys_check_conclusion.setter
    def sys_check_conclusion(self, sys_check_conclusion):
        r"""Sets the sys_check_conclusion of this IssueVO.

        **参数解释：**  验收结论。通常是验收RR时填写。 **取值范围：**  不涉及。

        :param sys_check_conclusion: The sys_check_conclusion of this IssueVO.
        :type sys_check_conclusion: str
        """
        self._sys_check_conclusion = sys_check_conclusion

    @property
    def id(self):
        r"""Gets the id of this IssueVO.

        **参数解释：**  工作项唯一Id。 **取值范围：**  不涉及。

        :return: The id of this IssueVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueVO.

        **参数解释：**  工作项唯一Id。 **取值范围：**  不涉及。

        :param id: The id of this IssueVO.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        r"""Gets the state of this IssueVO.

        **参数解释：**  工作项生命周期。 **取值范围：**  - 正在工作：可正常操作的工作项； - 作废：软删除后的工作项，可在回收站恢复； - 删除：彻底删除后的工作项，无法恢复。

        :return: The state of this IssueVO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this IssueVO.

        **参数解释：**  工作项生命周期。 **取值范围：**  - 正在工作：可正常操作的工作项； - 作废：软删除后的工作项，可在回收站恢复； - 删除：彻底删除后的工作项，无法恢复。

        :param state: The state of this IssueVO.
        :type state: str
        """
        self._state = state

    @property
    def stay_days(self):
        r"""Gets the stay_days of this IssueVO.

        **参数解释：**  工作项在当前状态的停留天数。 **取值范围：**  不涉及。

        :return: The stay_days of this IssueVO.
        :rtype: int
        """
        return self._stay_days

    @stay_days.setter
    def stay_days(self, stay_days):
        r"""Sets the stay_days of this IssueVO.

        **参数解释：**  工作项在当前状态的停留天数。 **取值范围：**  不涉及。

        :param stay_days: The stay_days of this IssueVO.
        :type stay_days: int
        """
        self._stay_days = stay_days

    @property
    def assigned_cc(self):
        r"""Gets the assigned_cc of this IssueVO.

        **参数解释：**  抄送人。 **取值范围：**  不涉及。

        :return: The assigned_cc of this IssueVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        """
        return self._assigned_cc

    @assigned_cc.setter
    def assigned_cc(self, assigned_cc):
        r"""Sets the assigned_cc of this IssueVO.

        **参数解释：**  抄送人。 **取值范围：**  不涉及。

        :param assigned_cc: The assigned_cc of this IssueVO.
        :type assigned_cc: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        """
        self._assigned_cc = assigned_cc

    @property
    def submit_time(self):
        r"""Gets the submit_time of this IssueVO.

        **参数解释：**  工作项提交时间，指工作项进入工作流的时间，而不是创建时间。 **取值范围：**  不涉及。

        :return: The submit_time of this IssueVO.
        :rtype: str
        """
        return self._submit_time

    @submit_time.setter
    def submit_time(self, submit_time):
        r"""Sets the submit_time of this IssueVO.

        **参数解释：**  工作项提交时间，指工作项进入工作流的时间，而不是创建时间。 **取值范围：**  不涉及。

        :param submit_time: The submit_time of this IssueVO.
        :type submit_time: str
        """
        self._submit_time = submit_time

    @property
    def workitem2label(self):
        r"""Gets the workitem2label of this IssueVO.

        **参数解释：**  工作项标签。 **取值范围：**  不涉及。

        :return: The workitem2label of this IssueVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.WorkItemLabelVO`]
        """
        return self._workitem2label

    @workitem2label.setter
    def workitem2label(self, workitem2label):
        r"""Sets the workitem2label of this IssueVO.

        **参数解释：**  工作项标签。 **取值范围：**  不涉及。

        :param workitem2label: The workitem2label of this IssueVO.
        :type workitem2label: list[:class:`huaweicloudsdkprojectman.v4.WorkItemLabelVO`]
        """
        self._workitem2label = workitem2label

    @property
    def sys_return_conclusion(self):
        r"""Gets the sys_return_conclusion of this IssueVO.

        **参数解释：**  退回原因。通常为退回RR/Bug时填写。 **取值范围：**  不涉及。

        :return: The sys_return_conclusion of this IssueVO.
        :rtype: str
        """
        return self._sys_return_conclusion

    @sys_return_conclusion.setter
    def sys_return_conclusion(self, sys_return_conclusion):
        r"""Sets the sys_return_conclusion of this IssueVO.

        **参数解释：**  退回原因。通常为退回RR/Bug时填写。 **取值范围：**  不涉及。

        :param sys_return_conclusion: The sys_return_conclusion of this IssueVO.
        :type sys_return_conclusion: str
        """
        self._sys_return_conclusion = sys_return_conclusion

    @property
    def close_time(self):
        r"""Gets the close_time of this IssueVO.

        **参数解释：**  工作项完成时间。 **取值范围：**  不涉及。

        :return: The close_time of this IssueVO.
        :rtype: str
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        r"""Sets the close_time of this IssueVO.

        **参数解释：**  工作项完成时间。 **取值范围：**  不涉及。

        :param close_time: The close_time of this IssueVO.
        :type close_time: str
        """
        self._close_time = close_time

    @property
    def priority(self):
        r"""Gets the priority of this IssueVO.

        :return: The priority of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this IssueVO.

        :param priority: The priority of this IssueVO.
        :type priority: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._priority = priority

    @property
    def modified_date(self):
        r"""Gets the modified_date of this IssueVO.

        **参数解释：**  工作项最新修改时间。 **取值范围：**  不涉及。

        :return: The modified_date of this IssueVO.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this IssueVO.

        **参数解释：**  工作项最新修改时间。 **取值范围：**  不涉及。

        :param modified_date: The modified_date of this IssueVO.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def created_by(self):
        r"""Gets the created_by of this IssueVO.

        :return: The created_by of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this IssueVO.

        :param created_by: The created_by of this IssueVO.
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._created_by = created_by

    @property
    def break_status(self):
        r"""Gets the break_status of this IssueVO.

        :return: The break_status of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._break_status

    @break_status.setter
    def break_status(self, break_status):
        r"""Sets the break_status of this IssueVO.

        :param break_status: The break_status of this IssueVO.
        :type break_status: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._break_status = break_status

    @property
    def status_modified_date(self):
        r"""Gets the status_modified_date of this IssueVO.

        **参数解释：**  工作项上一次流转状态的时间，可用于计算停留天数。unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :return: The status_modified_date of this IssueVO.
        :rtype: str
        """
        return self._status_modified_date

    @status_modified_date.setter
    def status_modified_date(self, status_modified_date):
        r"""Sets the status_modified_date of this IssueVO.

        **参数解释：**  工作项上一次流转状态的时间，可用于计算停留天数。unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :param status_modified_date: The status_modified_date of this IssueVO.
        :type status_modified_date: str
        """
        self._status_modified_date = status_modified_date

    @property
    def expect_delivery_time(self):
        r"""Gets the expect_delivery_time of this IssueVO.

        **参数解释：**  期望完成时间。Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :return: The expect_delivery_time of this IssueVO.
        :rtype: str
        """
        return self._expect_delivery_time

    @expect_delivery_time.setter
    def expect_delivery_time(self, expect_delivery_time):
        r"""Sets the expect_delivery_time of this IssueVO.

        **参数解释：**  期望完成时间。Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :param expect_delivery_time: The expect_delivery_time of this IssueVO.
        :type expect_delivery_time: str
        """
        self._expect_delivery_time = expect_delivery_time

    @property
    def parent_id(self):
        r"""Gets the parent_id of this IssueVO.

        **参数解释：**  工作项的父工作项Id。 **取值范围：**  不涉及。

        :return: The parent_id of this IssueVO.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this IssueVO.

        **参数解释：**  工作项的父工作项Id。 **取值范围：**  不涉及。

        :param parent_id: The parent_id of this IssueVO.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def assignee(self):
        r"""Gets the assignee of this IssueVO.

        :return: The assignee of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this IssueVO.

        :param assignee: The assignee of this IssueVO.
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._assignee = assignee

    @property
    def region(self):
        r"""Gets the region of this IssueVO.

        **参数解释：**  工作项所属租户的域。 **取值范围：**  不涉及。

        :return: The region of this IssueVO.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this IssueVO.

        **参数解释：**  工作项所属租户的域。 **取值范围：**  不涉及。

        :param region: The region of this IssueVO.
        :type region: str
        """
        self._region = region

    @property
    def status(self):
        r"""Gets the status of this IssueVO.

        :return: The status of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.AlmStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IssueVO.

        :param status: The status of this IssueVO.
        :type status: :class:`huaweicloudsdkprojectman.v4.AlmStatus`
        """
        self._status = status

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this IssueVO.

        **参数解释：**  工作项所属租户Id。 **取值范围：**  不涉及。

        :return: The tenant_id of this IssueVO.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this IssueVO.

        **参数解释：**  工作项所属租户Id。 **取值范围：**  不涉及。

        :param tenant_id: The tenant_id of this IssueVO.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def plan_pi(self):
        r"""Gets the plan_pi of this IssueVO.

        :return: The plan_pi of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        """
        return self._plan_pi

    @plan_pi.setter
    def plan_pi(self, plan_pi):
        r"""Sets the plan_pi of this IssueVO.

        :param plan_pi: The plan_pi of this IssueVO.
        :type plan_pi: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        """
        self._plan_pi = plan_pi

    @property
    def link(self):
        r"""Gets the link of this IssueVO.

        **参数解释：**  关联工作项的关系字段。多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :return: The link of this IssueVO.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this IssueVO.

        **参数解释：**  关联工作项的关系字段。多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :param link: The link of this IssueVO.
        :type link: str
        """
        self._link = link

    @property
    def description(self):
        r"""Gets the description of this IssueVO.

        **参数解释：**  工作项描述，最多支持50w字符。 **取值范围：**  不涉及。

        :return: The description of this IssueVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IssueVO.

        **参数解释：**  工作项描述，最多支持50w字符。 **取值范围：**  不涉及。

        :param description: The description of this IssueVO.
        :type description: str
        """
        self._description = description

    @property
    def is_suspended(self):
        r"""Gets the is_suspended of this IssueVO.

        :return: The is_suspended of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._is_suspended

    @is_suspended.setter
    def is_suspended(self, is_suspended):
        r"""Sets the is_suspended of this IssueVO.

        :param is_suspended: The is_suspended of this IssueVO.
        :type is_suspended: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._is_suspended = is_suspended

    @property
    def change_status(self):
        r"""Gets the change_status of this IssueVO.

        :return: The change_status of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._change_status

    @change_status.setter
    def change_status(self, change_status):
        r"""Sets the change_status of this IssueVO.

        :param change_status: The change_status of this IssueVO.
        :type change_status: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._change_status = change_status

    @property
    def title(self):
        r"""Gets the title of this IssueVO.

        **参数解释：**  工作项标题。 **取值范围：**  不涉及。

        :return: The title of this IssueVO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this IssueVO.

        **参数解释：**  工作项标题。 **取值范围：**  不涉及。

        :param title: The title of this IssueVO.
        :type title: str
        """
        self._title = title

    @property
    def sum_workload_man_day(self):
        r"""Gets the sum_workload_man_day of this IssueVO.

        **参数解释：**  工作项实际工时。 **取值范围：**  不涉及。

        :return: The sum_workload_man_day of this IssueVO.
        :rtype: str
        """
        return self._sum_workload_man_day

    @sum_workload_man_day.setter
    def sum_workload_man_day(self, sum_workload_man_day):
        r"""Sets the sum_workload_man_day of this IssueVO.

        **参数解释：**  工作项实际工时。 **取值范围：**  不涉及。

        :param sum_workload_man_day: The sum_workload_man_day of this IssueVO.
        :type sum_workload_man_day: str
        """
        self._sum_workload_man_day = sum_workload_man_day

    @property
    def sys_close_reason(self):
        r"""Gets the sys_close_reason of this IssueVO.

        **参数解释：**  工作项关闭原因。 **取值范围：**  不涉及。

        :return: The sys_close_reason of this IssueVO.
        :rtype: str
        """
        return self._sys_close_reason

    @sys_close_reason.setter
    def sys_close_reason(self, sys_close_reason):
        r"""Sets the sys_close_reason of this IssueVO.

        **参数解释：**  工作项关闭原因。 **取值范围：**  不涉及。

        :param sys_close_reason: The sys_close_reason of this IssueVO.
        :type sys_close_reason: str
        """
        self._sys_close_reason = sys_close_reason

    @property
    def sys_resubmit_reason(self):
        r"""Gets the sys_resubmit_reason of this IssueVO.

        **参数解释：**  重新提交原因，通常用于RR/Bug退回后重新提交。 **取值范围：**  不涉及。

        :return: The sys_resubmit_reason of this IssueVO.
        :rtype: str
        """
        return self._sys_resubmit_reason

    @sys_resubmit_reason.setter
    def sys_resubmit_reason(self, sys_resubmit_reason):
        r"""Sets the sys_resubmit_reason of this IssueVO.

        **参数解释：**  重新提交原因，通常用于RR/Bug退回后重新提交。 **取值范围：**  不涉及。

        :param sys_resubmit_reason: The sys_resubmit_reason of this IssueVO.
        :type sys_resubmit_reason: str
        """
        self._sys_resubmit_reason = sys_resubmit_reason

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this IssueVO.

        **参数解释：**  工作项计划完成时间。 **取值范围：**  不涉及。

        :return: The plan_end_date of this IssueVO.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this IssueVO.

        **参数解释：**  工作项计划完成时间。 **取值范围：**  不涉及。

        :param plan_end_date: The plan_end_date of this IssueVO.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def rr2ir(self):
        r"""Gets the rr2ir of this IssueVO.

        **参数解释：**  RR的子IR的id。多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :return: The rr2ir of this IssueVO.
        :rtype: str
        """
        return self._rr2ir

    @rr2ir.setter
    def rr2ir(self, rr2ir):
        r"""Sets the rr2ir of this IssueVO.

        **参数解释：**  RR的子IR的id。多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :param rr2ir: The rr2ir of this IssueVO.
        :type rr2ir: str
        """
        self._rr2ir = rr2ir

    @property
    def category_layer_id(self):
        r"""Gets the category_layer_id of this IssueVO.

        **参数解释：**  工作项类型层级id。 **取值范围：**  不涉及。

        :return: The category_layer_id of this IssueVO.
        :rtype: str
        """
        return self._category_layer_id

    @category_layer_id.setter
    def category_layer_id(self, category_layer_id):
        r"""Sets the category_layer_id of this IssueVO.

        **参数解释：**  工作项类型层级id。 **取值范围：**  不涉及。

        :param category_layer_id: The category_layer_id of this IssueVO.
        :type category_layer_id: str
        """
        self._category_layer_id = category_layer_id

    @property
    def submitted_by(self):
        r"""Gets the submitted_by of this IssueVO.

        **参数解释：**  工作项提交人。 **取值范围：**  不涉及。

        :return: The submitted_by of this IssueVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        r"""Sets the submitted_by of this IssueVO.

        **参数解释：**  工作项提交人。 **取值范围：**  不涉及。

        :param submitted_by: The submitted_by of this IssueVO.
        :type submitted_by: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        """
        self._submitted_by = submitted_by

    @property
    def rr2us(self):
        r"""Gets the rr2us of this IssueVO.

        **参数解释：**  RR的子US的id，多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :return: The rr2us of this IssueVO.
        :rtype: str
        """
        return self._rr2us

    @rr2us.setter
    def rr2us(self, rr2us):
        r"""Sets the rr2us of this IssueVO.

        **参数解释：**  RR的子US的id，多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :param rr2us: The rr2us of this IssueVO.
        :type rr2us: str
        """
        self._rr2us = rr2us

    @property
    def sys_no_develop_reason(self):
        r"""Gets the sys_no_develop_reason of this IssueVO.

        **参数解释：**  工作项无需开发原因。 **取值范围：**  不涉及。

        :return: The sys_no_develop_reason of this IssueVO.
        :rtype: str
        """
        return self._sys_no_develop_reason

    @sys_no_develop_reason.setter
    def sys_no_develop_reason(self, sys_no_develop_reason):
        r"""Sets the sys_no_develop_reason of this IssueVO.

        **参数解释：**  工作项无需开发原因。 **取值范围：**  不涉及。

        :param sys_no_develop_reason: The sys_no_develop_reason of this IssueVO.
        :type sys_no_develop_reason: str
        """
        self._sys_no_develop_reason = sys_no_develop_reason

    @property
    def plan_iteration(self):
        r"""Gets the plan_iteration of this IssueVO.

        :return: The plan_iteration of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        """
        return self._plan_iteration

    @plan_iteration.setter
    def plan_iteration(self, plan_iteration):
        r"""Sets the plan_iteration of this IssueVO.

        :param plan_iteration: The plan_iteration of this IssueVO.
        :type plan_iteration: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        """
        self._plan_iteration = plan_iteration

    @property
    def sys_return_reason(self):
        r"""Gets the sys_return_reason of this IssueVO.

        **参数解释：**  退回原因。通常用于RR/bug退回。 **取值范围：**  不涉及。

        :return: The sys_return_reason of this IssueVO.
        :rtype: str
        """
        return self._sys_return_reason

    @sys_return_reason.setter
    def sys_return_reason(self, sys_return_reason):
        r"""Sets the sys_return_reason of this IssueVO.

        **参数解释：**  退回原因。通常用于RR/bug退回。 **取值范围：**  不涉及。

        :param sys_return_reason: The sys_return_reason of this IssueVO.
        :type sys_return_reason: str
        """
        self._sys_return_reason = sys_return_reason

    @property
    def cascade_delete(self):
        r"""Gets the cascade_delete of this IssueVO.

        **参数解释：**  是否级联删除标记。 **取值范围：**  不涉及。

        :return: The cascade_delete of this IssueVO.
        :rtype: str
        """
        return self._cascade_delete

    @cascade_delete.setter
    def cascade_delete(self, cascade_delete):
        r"""Sets the cascade_delete of this IssueVO.

        **参数解释：**  是否级联删除标记。 **取值范围：**  不涉及。

        :param cascade_delete: The cascade_delete of this IssueVO.
        :type cascade_delete: str
        """
        self._cascade_delete = cascade_delete

    @property
    def recipient(self):
        r"""Gets the recipient of this IssueVO.

        **参数解释：**  承接人。通常用于RR。 **取值范围：**  不涉及。

        :return: The recipient of this IssueVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        r"""Sets the recipient of this IssueVO.

        **参数解释：**  承接人。通常用于RR。 **取值范围：**  不涉及。

        :param recipient: The recipient of this IssueVO.
        :type recipient: list[:class:`huaweicloudsdkprojectman.v4.UserVO`]
        """
        self._recipient = recipient

    @property
    def modified_by(self):
        r"""Gets the modified_by of this IssueVO.

        :return: The modified_by of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this IssueVO.

        :param modified_by: The modified_by of this IssueVO.
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._modified_by = modified_by

    @property
    def created_date(self):
        r"""Gets the created_date of this IssueVO.

        **参数解释：**  工作项创建时间。 **取值范围：**  不涉及。

        :return: The created_date of this IssueVO.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this IssueVO.

        **参数解释：**  工作项创建时间。 **取值范围：**  不涉及。

        :param created_date: The created_date of this IssueVO.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def category(self):
        r"""Gets the category of this IssueVO.

        **参数解释：**  工作项类型。 **取值范围：**  - 系统设备类项目：RR/SF/IR/SR/AR/Task/Bug。 - 独立软件类项目：RR/SF/IR/US/Task/Bug。 - 云服务类项目：RR/Epic/FE/US/Task/Bug。

        :return: The category of this IssueVO.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this IssueVO.

        **参数解释：**  工作项类型。 **取值范围：**  - 系统设备类项目：RR/SF/IR/SR/AR/Task/Bug。 - 独立软件类项目：RR/SF/IR/US/Task/Bug。 - 云服务类项目：RR/Epic/FE/US/Task/Bug。

        :param category: The category of this IssueVO.
        :type category: str
        """
        self._category = category

    @property
    def collaborative_status(self):
        r"""Gets the collaborative_status of this IssueVO.

        **参数解释：**  研发需求协同需求状态。 **取值范围：**  不涉及。

        :return: The collaborative_status of this IssueVO.
        :rtype: list[str]
        """
        return self._collaborative_status

    @collaborative_status.setter
    def collaborative_status(self, collaborative_status):
        r"""Sets the collaborative_status of this IssueVO.

        **参数解释：**  研发需求协同需求状态。 **取值范围：**  不涉及。

        :param collaborative_status: The collaborative_status of this IssueVO.
        :type collaborative_status: list[str]
        """
        self._collaborative_status = collaborative_status

    @property
    def project(self):
        r"""Gets the project of this IssueVO.

        :return: The project of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.DomainVO`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this IssueVO.

        :param project: The project of this IssueVO.
        :type project: :class:`huaweicloudsdkprojectman.v4.DomainVO`
        """
        self._project = project

    @property
    def child_issues(self):
        r"""Gets the child_issues of this IssueVO.

        **参数解释：**  子工作项列表。 **取值范围：**  不涉及。

        :return: The child_issues of this IssueVO.
        :rtype: dict(str, IssueVO)
        """
        return self._child_issues

    @child_issues.setter
    def child_issues(self, child_issues):
        r"""Sets the child_issues of this IssueVO.

        **参数解释：**  子工作项列表。 **取值范围：**  不涉及。

        :param child_issues: The child_issues of this IssueVO.
        :type child_issues: dict(str, IssueVO)
        """
        self._child_issues = child_issues

    @property
    def activate_times(self):
        r"""Gets the activate_times of this IssueVO.

        **参数解释：**  激活次数。Bug激活时自动赋值。 **取值范围：**  不涉及。

        :return: The activate_times of this IssueVO.
        :rtype: int
        """
        return self._activate_times

    @activate_times.setter
    def activate_times(self, activate_times):
        r"""Sets the activate_times of this IssueVO.

        **参数解释：**  激活次数。Bug激活时自动赋值。 **取值范围：**  不涉及。

        :param activate_times: The activate_times of this IssueVO.
        :type activate_times: int
        """
        self._activate_times = activate_times

    @property
    def baseline(self):
        r"""Gets the baseline of this IssueVO.

        :return: The baseline of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this IssueVO.

        :param baseline: The baseline of this IssueVO.
        :type baseline: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._baseline = baseline

    @property
    def business_domain(self):
        r"""Gets the business_domain of this IssueVO.

        :return: The business_domain of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._business_domain

    @business_domain.setter
    def business_domain(self, business_domain):
        r"""Sets the business_domain of this IssueVO.

        :param business_domain: The business_domain of this IssueVO.
        :type business_domain: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._business_domain = business_domain

    @property
    def children(self):
        r"""Gets the children of this IssueVO.

        **参数解释：**  子工作项Id，多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :return: The children of this IssueVO.
        :rtype: str
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this IssueVO.

        **参数解释：**  子工作项Id，多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :param children: The children of this IssueVO.
        :type children: str
        """
        self._children = children

    @property
    def collaborative_history(self):
        r"""Gets the collaborative_history of this IssueVO.

        **参数解释：**  协同需求的状态变化历史记录，内容为Json字符串。 **取值范围：**  不涉及。

        :return: The collaborative_history of this IssueVO.
        :rtype: str
        """
        return self._collaborative_history

    @collaborative_history.setter
    def collaborative_history(self, collaborative_history):
        r"""Sets the collaborative_history of this IssueVO.

        **参数解释：**  协同需求的状态变化历史记录，内容为Json字符串。 **取值范围：**  不涉及。

        :param collaborative_history: The collaborative_history of this IssueVO.
        :type collaborative_history: str
        """
        self._collaborative_history = collaborative_history

    @property
    def collaboratives(self):
        r"""Gets the collaboratives of this IssueVO.

        **参数解释：**  协同需求中的记录Id。 **取值范围：**  不涉及。

        :return: The collaboratives of this IssueVO.
        :rtype: str
        """
        return self._collaboratives

    @collaboratives.setter
    def collaboratives(self, collaboratives):
        r"""Sets the collaboratives of this IssueVO.

        **参数解释：**  协同需求中的记录Id。 **取值范围：**  不涉及。

        :param collaboratives: The collaboratives of this IssueVO.
        :type collaboratives: str
        """
        self._collaboratives = collaboratives

    @property
    def convolution_actual_hours(self):
        r"""Gets the convolution_actual_hours of this IssueVO.

        **参数解释：**  卷积实际工时。父工作项中将子工作项/协同工作项的实际工时卷积得到。 **取值范围：**  不涉及。

        :return: The convolution_actual_hours of this IssueVO.
        :rtype: str
        """
        return self._convolution_actual_hours

    @convolution_actual_hours.setter
    def convolution_actual_hours(self, convolution_actual_hours):
        r"""Sets the convolution_actual_hours of this IssueVO.

        **参数解释：**  卷积实际工时。父工作项中将子工作项/协同工作项的实际工时卷积得到。 **取值范围：**  不涉及。

        :param convolution_actual_hours: The convolution_actual_hours of this IssueVO.
        :type convolution_actual_hours: str
        """
        self._convolution_actual_hours = convolution_actual_hours

    @property
    def convolution_plan_hours(self):
        r"""Gets the convolution_plan_hours of this IssueVO.

        **参数解释：**  卷积计划工时。父工作项中将子工作项/协同工作项的计划工时卷积得到。 **取值范围：**  不涉及。

        :return: The convolution_plan_hours of this IssueVO.
        :rtype: str
        """
        return self._convolution_plan_hours

    @convolution_plan_hours.setter
    def convolution_plan_hours(self, convolution_plan_hours):
        r"""Sets the convolution_plan_hours of this IssueVO.

        **参数解释：**  卷积计划工时。父工作项中将子工作项/协同工作项的计划工时卷积得到。 **取值范围：**  不涉及。

        :param convolution_plan_hours: The convolution_plan_hours of this IssueVO.
        :type convolution_plan_hours: str
        """
        self._convolution_plan_hours = convolution_plan_hours

    @property
    def develop_owner(self):
        r"""Gets the develop_owner of this IssueVO.

        **参数解释：**  开发责任人。通常用于“开发”状态节点责任人。 **取值范围：**  不涉及。

        :return: The develop_owner of this IssueVO.
        :rtype: str
        """
        return self._develop_owner

    @develop_owner.setter
    def develop_owner(self, develop_owner):
        r"""Sets the develop_owner of this IssueVO.

        **参数解释：**  开发责任人。通常用于“开发”状态节点责任人。 **取值范围：**  不涉及。

        :param develop_owner: The develop_owner of this IssueVO.
        :type develop_owner: str
        """
        self._develop_owner = develop_owner

    @property
    def done_ratio(self):
        r"""Gets the done_ratio of this IssueVO.

        :return: The done_ratio of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._done_ratio

    @done_ratio.setter
    def done_ratio(self, done_ratio):
        r"""Sets the done_ratio of this IssueVO.

        :param done_ratio: The done_ratio of this IssueVO.
        :type done_ratio: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._done_ratio = done_ratio

    @property
    def expected_repair_date(self):
        r"""Gets the expected_repair_date of this IssueVO.

        **参数解释：**  期望修复时间。 **取值范围：**  不涉及。

        :return: The expected_repair_date of this IssueVO.
        :rtype: str
        """
        return self._expected_repair_date

    @expected_repair_date.setter
    def expected_repair_date(self, expected_repair_date):
        r"""Sets the expected_repair_date of this IssueVO.

        **参数解释：**  期望修复时间。 **取值范围：**  不涉及。

        :param expected_repair_date: The expected_repair_date of this IssueVO.
        :type expected_repair_date: str
        """
        self._expected_repair_date = expected_repair_date

    @property
    def feature2ir(self):
        r"""Gets the feature2ir of this IssueVO.

        **参数解释：**  SF的子IR的id。多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :return: The feature2ir of this IssueVO.
        :rtype: str
        """
        return self._feature2ir

    @feature2ir.setter
    def feature2ir(self, feature2ir):
        r"""Sets the feature2ir of this IssueVO.

        **参数解释：**  SF的子IR的id。多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :param feature2ir: The feature2ir of this IssueVO.
        :type feature2ir: str
        """
        self._feature2ir = feature2ir

    @property
    def feature_set(self):
        r"""Gets the feature_set of this IssueVO.

        :return: The feature_set of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._feature_set

    @feature_set.setter
    def feature_set(self, feature_set):
        r"""Sets the feature_set of this IssueVO.

        :param feature_set: The feature_set of this IssueVO.
        :type feature_set: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._feature_set = feature_set

    @property
    def found_env(self):
        r"""Gets the found_env of this IssueVO.

        :return: The found_env of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._found_env

    @found_env.setter
    def found_env(self, found_env):
        r"""Sets the found_env of this IssueVO.

        :param found_env: The found_env of this IssueVO.
        :type found_env: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._found_env = found_env

    @property
    def found_iteration(self):
        r"""Gets the found_iteration of this IssueVO.

        :return: The found_iteration of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        """
        return self._found_iteration

    @found_iteration.setter
    def found_iteration(self, found_iteration):
        r"""Sets the found_iteration of this IssueVO.

        :param found_iteration: The found_iteration of this IssueVO.
        :type found_iteration: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        """
        self._found_iteration = found_iteration

    @property
    def found_pi(self):
        r"""Gets the found_pi of this IssueVO.

        :return: The found_pi of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        """
        return self._found_pi

    @found_pi.setter
    def found_pi(self, found_pi):
        r"""Sets the found_pi of this IssueVO.

        :param found_pi: The found_pi of this IssueVO.
        :type found_pi: :class:`huaweicloudsdkprojectman.v4.PlanVO`
        """
        self._found_pi = found_pi

    @property
    def function_scene(self):
        r"""Gets the function_scene of this IssueVO.

        **参数解释：**  功能场景。 **取值范围：**  不涉及。

        :return: The function_scene of this IssueVO.
        :rtype: str
        """
        return self._function_scene

    @function_scene.setter
    def function_scene(self, function_scene):
        r"""Sets the function_scene of this IssueVO.

        **参数解释：**  功能场景。 **取值范围：**  不涉及。

        :param function_scene: The function_scene of this IssueVO.
        :type function_scene: str
        """
        self._function_scene = function_scene

    @property
    def ir2feature(self):
        r"""Gets the ir2feature of this IssueVO.

        **参数解释：**  IR关联的SF的Id，一个IR仅能关联一个SF。 **取值范围：**  不涉及。

        :return: The ir2feature of this IssueVO.
        :rtype: str
        """
        return self._ir2feature

    @ir2feature.setter
    def ir2feature(self, ir2feature):
        r"""Sets the ir2feature of this IssueVO.

        **参数解释：**  IR关联的SF的Id，一个IR仅能关联一个SF。 **取值范围：**  不涉及。

        :param ir2feature: The ir2feature of this IssueVO.
        :type ir2feature: str
        """
        self._ir2feature = ir2feature

    @property
    def ir2rr(self):
        r"""Gets the ir2rr of this IssueVO.

        **参数解释：**  IR关联父RR的Id，多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :return: The ir2rr of this IssueVO.
        :rtype: str
        """
        return self._ir2rr

    @ir2rr.setter
    def ir2rr(self, ir2rr):
        r"""Sets the ir2rr of this IssueVO.

        **参数解释：**  IR关联父RR的Id，多值使用英文逗号分隔。 **取值范围：**  不涉及。

        :param ir2rr: The ir2rr of this IssueVO.
        :type ir2rr: str
        """
        self._ir2rr = ir2rr

    @property
    def issue_opinion_id(self):
        r"""Gets the issue_opinion_id of this IssueVO.

        **参数解释：**  工作项关联的决策意见Id。 **取值范围：**  不涉及。

        :return: The issue_opinion_id of this IssueVO.
        :rtype: str
        """
        return self._issue_opinion_id

    @issue_opinion_id.setter
    def issue_opinion_id(self, issue_opinion_id):
        r"""Sets the issue_opinion_id of this IssueVO.

        **参数解释：**  工作项关联的决策意见Id。 **取值范围：**  不涉及。

        :param issue_opinion_id: The issue_opinion_id of this IssueVO.
        :type issue_opinion_id: str
        """
        self._issue_opinion_id = issue_opinion_id

    @property
    def issue_review_id(self):
        r"""Gets the issue_review_id of this IssueVO.

        **参数解释：**  工作项关联的评审意见Id。 **取值范围：**  不涉及。

        :return: The issue_review_id of this IssueVO.
        :rtype: str
        """
        return self._issue_review_id

    @issue_review_id.setter
    def issue_review_id(self, issue_review_id):
        r"""Sets the issue_review_id of this IssueVO.

        **参数解释：**  工作项关联的评审意见Id。 **取值范围：**  不涉及。

        :param issue_review_id: The issue_review_id of this IssueVO.
        :type issue_review_id: str
        """
        self._issue_review_id = issue_review_id

    @property
    def module(self):
        r"""Gets the module of this IssueVO.

        :return: The module of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._module

    @module.setter
    def module(self, module):
        r"""Sets the module of this IssueVO.

        :param module: The module of this IssueVO.
        :type module: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._module = module

    @property
    def need_break(self):
        r"""Gets the need_break of this IssueVO.

        :return: The need_break of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._need_break

    @need_break.setter
    def need_break(self, need_break):
        r"""Sets the need_break of this IssueVO.

        :param need_break: The need_break of this IssueVO.
        :type need_break: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._need_break = need_break

    @property
    def need_develop(self):
        r"""Gets the need_develop of this IssueVO.

        :return: The need_develop of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._need_develop

    @need_develop.setter
    def need_develop(self, need_develop):
        r"""Sets the need_develop of this IssueVO.

        :param need_develop: The need_develop of this IssueVO.
        :type need_develop: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._need_develop = need_develop

    @property
    def no_break_reason(self):
        r"""Gets the no_break_reason of this IssueVO.

        **参数解释：**  无需分解原因。 **取值范围：**  不涉及。

        :return: The no_break_reason of this IssueVO.
        :rtype: str
        """
        return self._no_break_reason

    @no_break_reason.setter
    def no_break_reason(self, no_break_reason):
        r"""Sets the no_break_reason of this IssueVO.

        **参数解释：**  无需分解原因。 **取值范围：**  不涉及。

        :param no_break_reason: The no_break_reason of this IssueVO.
        :type no_break_reason: str
        """
        self._no_break_reason = no_break_reason

    @property
    def no_develop_reason(self):
        r"""Gets the no_develop_reason of this IssueVO.

        **参数解释：**  无需开发原因。 **取值范围：**  不涉及。

        :return: The no_develop_reason of this IssueVO.
        :rtype: str
        """
        return self._no_develop_reason

    @no_develop_reason.setter
    def no_develop_reason(self, no_develop_reason):
        r"""Sets the no_develop_reason of this IssueVO.

        **参数解释：**  无需开发原因。 **取值范围：**  不涉及。

        :param no_develop_reason: The no_develop_reason of this IssueVO.
        :type no_develop_reason: str
        """
        self._no_develop_reason = no_develop_reason

    @property
    def order(self):
        r"""Gets the order of this IssueVO.

        **参数解释：**  优先级顺序。 **取值范围：**  1~100。

        :return: The order of this IssueVO.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this IssueVO.

        **参数解释：**  优先级顺序。 **取值范围：**  1~100。

        :param order: The order of this IssueVO.
        :type order: str
        """
        self._order = order

    @property
    def plan_dev_end_date(self):
        r"""Gets the plan_dev_end_date of this IssueVO.

        **参数解释：**  计划开发结束时间。通常用于“开发”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :return: The plan_dev_end_date of this IssueVO.
        :rtype: str
        """
        return self._plan_dev_end_date

    @plan_dev_end_date.setter
    def plan_dev_end_date(self, plan_dev_end_date):
        r"""Sets the plan_dev_end_date of this IssueVO.

        **参数解释：**  计划开发结束时间。通常用于“开发”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :param plan_dev_end_date: The plan_dev_end_date of this IssueVO.
        :type plan_dev_end_date: str
        """
        self._plan_dev_end_date = plan_dev_end_date

    @property
    def plan_processing_end_date(self):
        r"""Gets the plan_processing_end_date of this IssueVO.

        **参数解释：**  计划处理中结束时间。通常用于“处理中”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :return: The plan_processing_end_date of this IssueVO.
        :rtype: str
        """
        return self._plan_processing_end_date

    @plan_processing_end_date.setter
    def plan_processing_end_date(self, plan_processing_end_date):
        r"""Sets the plan_processing_end_date of this IssueVO.

        **参数解释：**  计划处理中结束时间。通常用于“处理中”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :param plan_processing_end_date: The plan_processing_end_date of this IssueVO.
        :type plan_processing_end_date: str
        """
        self._plan_processing_end_date = plan_processing_end_date

    @property
    def plan_researchanddevelop_end_date(self):
        r"""Gets the plan_researchanddevelop_end_date of this IssueVO.

        **参数解释：**  计划研发结束时间。通常用于“研发”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :return: The plan_researchanddevelop_end_date of this IssueVO.
        :rtype: str
        """
        return self._plan_researchanddevelop_end_date

    @plan_researchanddevelop_end_date.setter
    def plan_researchanddevelop_end_date(self, plan_researchanddevelop_end_date):
        r"""Sets the plan_researchanddevelop_end_date of this IssueVO.

        **参数解释：**  计划研发结束时间。通常用于“研发”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :param plan_researchanddevelop_end_date: The plan_researchanddevelop_end_date of this IssueVO.
        :type plan_researchanddevelop_end_date: str
        """
        self._plan_researchanddevelop_end_date = plan_researchanddevelop_end_date

    @property
    def plan_test_end_date(self):
        r"""Gets the plan_test_end_date of this IssueVO.

        **参数解释：**  计划测试结束时间。通常用于“测试”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :return: The plan_test_end_date of this IssueVO.
        :rtype: str
        """
        return self._plan_test_end_date

    @plan_test_end_date.setter
    def plan_test_end_date(self, plan_test_end_date):
        r"""Sets the plan_test_end_date of this IssueVO.

        **参数解释：**  计划测试结束时间。通常用于“测试”状态节点，Unix时间戳，单位为毫秒。 **取值范围：**  不涉及。

        :param plan_test_end_date: The plan_test_end_date of this IssueVO.
        :type plan_test_end_date: str
        """
        self._plan_test_end_date = plan_test_end_date

    @property
    def position_float(self):
        r"""Gets the position_float of this IssueVO.

        **参数解释：**  标识工作项在列表中初始排序位置。 **取值范围：**  不涉及。

        :return: The position_float of this IssueVO.
        :rtype: str
        """
        return self._position_float

    @position_float.setter
    def position_float(self, position_float):
        r"""Sets the position_float of this IssueVO.

        **参数解释：**  标识工作项在列表中初始排序位置。 **取值范围：**  不涉及。

        :param position_float: The position_float of this IssueVO.
        :type position_float: str
        """
        self._position_float = position_float

    @property
    def processing_owner(self):
        r"""Gets the processing_owner of this IssueVO.

        **参数解释：**  处理中责任人。通常用于“处理中”状态节点。 **取值范围：**  不涉及。

        :return: The processing_owner of this IssueVO.
        :rtype: str
        """
        return self._processing_owner

    @processing_owner.setter
    def processing_owner(self, processing_owner):
        r"""Sets the processing_owner of this IssueVO.

        **参数解释：**  处理中责任人。通常用于“处理中”状态节点。 **取值范围：**  不涉及。

        :param processing_owner: The processing_owner of this IssueVO.
        :type processing_owner: str
        """
        self._processing_owner = processing_owner

    @property
    def reason_analysis(self):
        r"""Gets the reason_analysis of this IssueVO.

        **参数解释：**  分析原因。 **取值范围：**  不涉及。

        :return: The reason_analysis of this IssueVO.
        :rtype: str
        """
        return self._reason_analysis

    @reason_analysis.setter
    def reason_analysis(self, reason_analysis):
        r"""Sets the reason_analysis of this IssueVO.

        **参数解释：**  分析原因。 **取值范围：**  不涉及。

        :param reason_analysis: The reason_analysis of this IssueVO.
        :type reason_analysis: str
        """
        self._reason_analysis = reason_analysis

    @property
    def regression_failure_number(self):
        r"""Gets the regression_failure_number of this IssueVO.

        **参数解释：**  回归不通过次数。缺陷测试不通过时自动赋值。 **取值范围：**  不涉及。

        :return: The regression_failure_number of this IssueVO.
        :rtype: int
        """
        return self._regression_failure_number

    @regression_failure_number.setter
    def regression_failure_number(self, regression_failure_number):
        r"""Sets the regression_failure_number of this IssueVO.

        **参数解释：**  回归不通过次数。缺陷测试不通过时自动赋值。 **取值范围：**  不涉及。

        :param regression_failure_number: The regression_failure_number of this IssueVO.
        :type regression_failure_number: int
        """
        self._regression_failure_number = regression_failure_number

    @property
    def related_network_security(self):
        r"""Gets the related_network_security of this IssueVO.

        :return: The related_network_security of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._related_network_security

    @related_network_security.setter
    def related_network_security(self, related_network_security):
        r"""Sets the related_network_security of this IssueVO.

        :param related_network_security: The related_network_security of this IssueVO.
        :type related_network_security: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._related_network_security = related_network_security

    @property
    def repair_solution(self):
        r"""Gets the repair_solution of this IssueVO.

        **参数解释：**  修复方案。常用于修复缺陷时。 **取值范围：**  不涉及。

        :return: The repair_solution of this IssueVO.
        :rtype: str
        """
        return self._repair_solution

    @repair_solution.setter
    def repair_solution(self, repair_solution):
        r"""Sets the repair_solution of this IssueVO.

        **参数解释：**  修复方案。常用于修复缺陷时。 **取值范围：**  不涉及。

        :param repair_solution: The repair_solution of this IssueVO.
        :type repair_solution: str
        """
        self._repair_solution = repair_solution

    @property
    def researchanddevelop_owner(self):
        r"""Gets the researchanddevelop_owner of this IssueVO.

        **参数解释：**  研发责任人。通常用于“研发”状态节点。 **取值范围：**  不涉及。

        :return: The researchanddevelop_owner of this IssueVO.
        :rtype: str
        """
        return self._researchanddevelop_owner

    @researchanddevelop_owner.setter
    def researchanddevelop_owner(self, researchanddevelop_owner):
        r"""Sets the researchanddevelop_owner of this IssueVO.

        **参数解释：**  研发责任人。通常用于“研发”状态节点。 **取值范围：**  不涉及。

        :param researchanddevelop_owner: The researchanddevelop_owner of this IssueVO.
        :type researchanddevelop_owner: str
        """
        self._researchanddevelop_owner = researchanddevelop_owner

    @property
    def severity(self):
        r"""Gets the severity of this IssueVO.

        :return: The severity of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this IssueVO.

        :param severity: The severity of this IssueVO.
        :type severity: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._severity = severity

    @property
    def sys_activation_reason(self):
        r"""Gets the sys_activation_reason of this IssueVO.

        **参数解释：**  严重程度。 **取值范围：**  不涉及。

        :return: The sys_activation_reason of this IssueVO.
        :rtype: str
        """
        return self._sys_activation_reason

    @sys_activation_reason.setter
    def sys_activation_reason(self, sys_activation_reason):
        r"""Sets the sys_activation_reason of this IssueVO.

        **参数解释：**  严重程度。 **取值范围：**  不涉及。

        :param sys_activation_reason: The sys_activation_reason of this IssueVO.
        :type sys_activation_reason: str
        """
        self._sys_activation_reason = sys_activation_reason

    @property
    def sys_no_repair_reason(self):
        r"""Gets the sys_no_repair_reason of this IssueVO.

        **参数解释：**  无需修复原因。通常用于在缺陷无需修复时。 **取值范围：**  不涉及。

        :return: The sys_no_repair_reason of this IssueVO.
        :rtype: str
        """
        return self._sys_no_repair_reason

    @sys_no_repair_reason.setter
    def sys_no_repair_reason(self, sys_no_repair_reason):
        r"""Sets the sys_no_repair_reason of this IssueVO.

        **参数解释：**  无需修复原因。通常用于在缺陷无需修复时。 **取值范围：**  不涉及。

        :param sys_no_repair_reason: The sys_no_repair_reason of this IssueVO.
        :type sys_no_repair_reason: str
        """
        self._sys_no_repair_reason = sys_no_repair_reason

    @property
    def test_failures_times(self):
        r"""Gets the test_failures_times of this IssueVO.

        **参数解释：**  测试不通过次数。 **取值范围：**  不涉及。

        :return: The test_failures_times of this IssueVO.
        :rtype: int
        """
        return self._test_failures_times

    @test_failures_times.setter
    def test_failures_times(self, test_failures_times):
        r"""Sets the test_failures_times of this IssueVO.

        **参数解释：**  测试不通过次数。 **取值范围：**  不涉及。

        :param test_failures_times: The test_failures_times of this IssueVO.
        :type test_failures_times: int
        """
        self._test_failures_times = test_failures_times

    @property
    def test_owner(self):
        r"""Gets the test_owner of this IssueVO.

        **参数解释：**  测试责任人。通常用于“测试”状态节点。 **取值范围：**  不涉及。

        :return: The test_owner of this IssueVO.
        :rtype: str
        """
        return self._test_owner

    @test_owner.setter
    def test_owner(self, test_owner):
        r"""Sets the test_owner of this IssueVO.

        **参数解释：**  测试责任人。通常用于“测试”状态节点。 **取值范围：**  不涉及。

        :param test_owner: The test_owner of this IssueVO.
        :type test_owner: str
        """
        self._test_owner = test_owner

    @property
    def test_report(self):
        r"""Gets the test_report of this IssueVO.

        **参数解释：**  测试报告。 **取值范围：**  不涉及。

        :return: The test_report of this IssueVO.
        :rtype: str
        """
        return self._test_report

    @test_report.setter
    def test_report(self, test_report):
        r"""Sets the test_report of this IssueVO.

        **参数解释：**  测试报告。 **取值范围：**  不涉及。

        :param test_report: The test_report of this IssueVO.
        :type test_report: str
        """
        self._test_report = test_report

    @property
    def val_feature(self):
        r"""Gets the val_feature of this IssueVO.

        :return: The val_feature of this IssueVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        return self._val_feature

    @val_feature.setter
    def val_feature(self, val_feature):
        r"""Sets the val_feature of this IssueVO.

        :param val_feature: The val_feature of this IssueVO.
        :type val_feature: :class:`huaweicloudsdkprojectman.v4.OptionVO`
        """
        self._val_feature = val_feature

    @property
    def workitem2ganttchart(self):
        r"""Gets the workitem2ganttchart of this IssueVO.

        **参数解释：**  工作项关联的甘特图Id。 **取值范围：**  不涉及。

        :return: The workitem2ganttchart of this IssueVO.
        :rtype: str
        """
        return self._workitem2ganttchart

    @workitem2ganttchart.setter
    def workitem2ganttchart(self, workitem2ganttchart):
        r"""Sets the workitem2ganttchart of this IssueVO.

        **参数解释：**  工作项关联的甘特图Id。 **取值范围：**  不涉及。

        :param workitem2ganttchart: The workitem2ganttchart of this IssueVO.
        :type workitem2ganttchart: str
        """
        self._workitem2ganttchart = workitem2ganttchart

    @property
    def workitem2mindmap(self):
        r"""Gets the workitem2mindmap of this IssueVO.

        **参数解释：**  工作项关联的思维导图Id。 **取值范围：**  不涉及。

        :return: The workitem2mindmap of this IssueVO.
        :rtype: str
        """
        return self._workitem2mindmap

    @workitem2mindmap.setter
    def workitem2mindmap(self, workitem2mindmap):
        r"""Sets the workitem2mindmap of this IssueVO.

        **参数解释：**  工作项关联的思维导图Id。 **取值范围：**  不涉及。

        :param workitem2mindmap: The workitem2mindmap of this IssueVO.
        :type workitem2mindmap: str
        """
        self._workitem2mindmap = workitem2mindmap

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
        if not isinstance(other, IssueVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
