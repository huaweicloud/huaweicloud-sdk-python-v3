# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessInstanceResponseResultCos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'category': 'str',
        'title': 'str',
        'status': 'str',
        'assignee': 'ProcessInstanceResponseResultAssignee',
        'description': 'str',
        'number': 'str',
        'order': 'str',
        'co2cr': 'str',
        'co2br': 'str',
        'co2gr': 'str',
        'id': 'str',
        'type': 'str',
        'state': 'str',
        'before_change': 'str',
        'after_change': 'str',
        'modified_by': 'str',
        'modified_date': 'str',
        'created_by': 'str',
        'created_date': 'str',
        'tenant_id': 'str',
        'status_map': 'str',
        'domain_id': 'str',
        'source_system': 'str',
        'source_system_link': 'str',
        'issue_category': 'str',
        'issue_id': 'str',
        'issue_status': 'ProcessInstanceResponseResultIssueStatus',
        'issue_severity': 'str',
        'issue_priority': 'ProcessInstanceResponseResultIssuePriority',
        'domain_title': 'str',
        'src_domain_title': 'str',
        'issue_assignee_name': 'str',
        'change_reason': 'str',
        'change_type': 'str',
        'source_system_id': 'str',
        'change_description': 'str',
        'has_deleted': 'str',
        'approval_phase_result': 'str',
        'approval_complete_time': 'str',
        'ccb_description': 'str',
        'actual_ccb': 'str',
        'ccbs': 'str',
        'ccb_info': 'str',
        'opinions': 'str',
        'opinion_comments': 'str',
        'approval_time': 'str',
        'src_domain_id': 'str',
        'cross_domain': 'str',
        'domain_moved': 'str',
        'reviewer': 'list[str]',
        'approver': 'list[str]',
        'rounds': 'str',
        'last_round_result': 'str'
    }

    attribute_map = {
        'region': 'region',
        'category': 'category',
        'title': 'title',
        'status': 'status',
        'assignee': 'assignee',
        'description': 'description',
        'number': 'number',
        'order': 'order',
        'co2cr': 'co2cr',
        'co2br': 'co2br',
        'co2gr': 'co2gr',
        'id': 'id',
        'type': 'type',
        'state': 'state',
        'before_change': 'before_change',
        'after_change': 'after_change',
        'modified_by': 'modified_by',
        'modified_date': 'modified_date',
        'created_by': 'created_by',
        'created_date': 'created_date',
        'tenant_id': 'tenant_id',
        'status_map': 'status_map',
        'domain_id': 'domain_id',
        'source_system': 'source_system',
        'source_system_link': 'source_system_link',
        'issue_category': 'issue_category',
        'issue_id': 'issue_id',
        'issue_status': 'issue_status',
        'issue_severity': 'issue_severity',
        'issue_priority': 'issue_priority',
        'domain_title': 'domain_title',
        'src_domain_title': 'src_domain_title',
        'issue_assignee_name': 'issue_assignee_name',
        'change_reason': 'change_reason',
        'change_type': 'change_type',
        'source_system_id': 'source_system_id',
        'change_description': 'change_description',
        'has_deleted': 'has_deleted',
        'approval_phase_result': 'approval_phase_result',
        'approval_complete_time': 'approval_complete_time',
        'ccb_description': 'ccb_description',
        'actual_ccb': 'actual_ccb',
        'ccbs': 'ccbs',
        'ccb_info': 'ccb_info',
        'opinions': 'opinions',
        'opinion_comments': 'opinion_comments',
        'approval_time': 'approval_time',
        'src_domain_id': 'src_domain_id',
        'cross_domain': 'cross_domain',
        'domain_moved': 'domain_moved',
        'reviewer': 'reviewer',
        'approver': 'approver',
        'rounds': 'rounds',
        'last_round_result': 'last_round_result'
    }

    def __init__(self, region=None, category=None, title=None, status=None, assignee=None, description=None, number=None, order=None, co2cr=None, co2br=None, co2gr=None, id=None, type=None, state=None, before_change=None, after_change=None, modified_by=None, modified_date=None, created_by=None, created_date=None, tenant_id=None, status_map=None, domain_id=None, source_system=None, source_system_link=None, issue_category=None, issue_id=None, issue_status=None, issue_severity=None, issue_priority=None, domain_title=None, src_domain_title=None, issue_assignee_name=None, change_reason=None, change_type=None, source_system_id=None, change_description=None, has_deleted=None, approval_phase_result=None, approval_complete_time=None, ccb_description=None, actual_ccb=None, ccbs=None, ccb_info=None, opinions=None, opinion_comments=None, approval_time=None, src_domain_id=None, cross_domain=None, domain_moved=None, reviewer=None, approver=None, rounds=None, last_round_result=None):
        r"""ProcessInstanceResponseResultCos

        The model defined in huaweicloud sdk

        :param region: 区域
        :type region: str
        :param category: 变更对象工作项类型，此处固定为CO
        :type category: str
        :param title: 评审单标题
        :type title: str
        :param status: 变更对象状态
        :type status: str
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultAssignee`
        :param description: 评审单描述
        :type description: str
        :param number: 变更对象关联的工作项编号
        :type number: str
        :param order: 排序
        :type order: str
        :param co2cr: 关联的变更评审标识
        :type co2cr: str
        :param co2br: 关联的基线评审标识
        :type co2br: str
        :param co2gr: 关联的通用评审标识
        :type co2gr: str
        :param id: 审批对象Id
        :type id: str
        :param type: 评审单类型
        :type type: str
        :param state: 评审单工作状态，取值为\&quot;正在工作\&quot;,\&quot;作废\&quot;
        :type state: str
        :param before_change: 变更对象工作项修改前内容
        :type before_change: str
        :param after_change: 变更对象修改后内容
        :type after_change: str
        :param modified_by: 评审单最后修改人
        :type modified_by: str
        :param modified_date: 评审单最后修改时间
        :type modified_date: str
        :param created_by: 评审单创建人
        :type created_by: str
        :param created_date: 评审单创建时间
        :type created_date: str
        :param tenant_id: 工作项所属租户ID，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**tenant_id**字段的值就是工作项所属租户id
        :type tenant_id: str
        :param status_map: 工作项状态
        :type status_map: str
        :param domain_id: 租户id
        :type domain_id: str
        :param source_system: 源系统
        :type source_system: str
        :param source_system_link: 源系统链接
        :type source_system_link: str
        :param issue_category: 变更对象关联的工作项类型
        :type issue_category: str
        :param issue_id: 工作项ID
        :type issue_id: str
        :param issue_status: 
        :type issue_status: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultIssueStatus`
        :param issue_severity: 工作项严重程度
        :type issue_severity: str
        :param issue_priority: 
        :type issue_priority: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultIssuePriority`
        :param domain_title: 归属项目名称
        :type domain_title: str
        :param src_domain_title: 提出项目名称
        :type src_domain_title: str
        :param issue_assignee_name: 责任人昵称
        :type issue_assignee_name: str
        :param change_reason: 评审原因
        :type change_reason: str
        :param change_type: 评审类型
        :type change_type: str
        :param source_system_id: 源系统id
        :type source_system_id: str
        :param change_description: 评审描述
        :type change_description: str
        :param has_deleted: 是否已删除
        :type has_deleted: str
        :param approval_phase_result: 评审结果
        :type approval_phase_result: str
        :param approval_complete_time: 评审完成时间
        :type approval_complete_time: str
        :param ccb_description: 评审描述
        :type ccb_description: str
        :param actual_ccb: 评审专家
        :type actual_ccb: str
        :param ccbs: 审批信息列表
        :type ccbs: str
        :param ccb_info: 评审信息
        :type ccb_info: str
        :param opinions: 变更对象评审专家Id列表（创建变更评审时使用）
        :type opinions: str
        :param opinion_comments: 评审意见
        :type opinion_comments: str
        :param approval_time: 审批时间
        :type approval_time: str
        :param src_domain_id: 租户id
        :type src_domain_id: str
        :param cross_domain: 是否跨租户
        :type cross_domain: str
        :param domain_moved: 归属项目是否迁移
        :type domain_moved: str
        :param reviewer: 评审专家
        :type reviewer: list[str]
        :param approver: 决策人
        :type approver: list[str]
        :param rounds: 评审轮次
        :type rounds: str
        :param last_round_result: 最近一轮决策结果
        :type last_round_result: str
        """
        
        

        self._region = None
        self._category = None
        self._title = None
        self._status = None
        self._assignee = None
        self._description = None
        self._number = None
        self._order = None
        self._co2cr = None
        self._co2br = None
        self._co2gr = None
        self._id = None
        self._type = None
        self._state = None
        self._before_change = None
        self._after_change = None
        self._modified_by = None
        self._modified_date = None
        self._created_by = None
        self._created_date = None
        self._tenant_id = None
        self._status_map = None
        self._domain_id = None
        self._source_system = None
        self._source_system_link = None
        self._issue_category = None
        self._issue_id = None
        self._issue_status = None
        self._issue_severity = None
        self._issue_priority = None
        self._domain_title = None
        self._src_domain_title = None
        self._issue_assignee_name = None
        self._change_reason = None
        self._change_type = None
        self._source_system_id = None
        self._change_description = None
        self._has_deleted = None
        self._approval_phase_result = None
        self._approval_complete_time = None
        self._ccb_description = None
        self._actual_ccb = None
        self._ccbs = None
        self._ccb_info = None
        self._opinions = None
        self._opinion_comments = None
        self._approval_time = None
        self._src_domain_id = None
        self._cross_domain = None
        self._domain_moved = None
        self._reviewer = None
        self._approver = None
        self._rounds = None
        self._last_round_result = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if category is not None:
            self.category = category
        if title is not None:
            self.title = title
        if status is not None:
            self.status = status
        if assignee is not None:
            self.assignee = assignee
        if description is not None:
            self.description = description
        if number is not None:
            self.number = number
        if order is not None:
            self.order = order
        if co2cr is not None:
            self.co2cr = co2cr
        if co2br is not None:
            self.co2br = co2br
        if co2gr is not None:
            self.co2gr = co2gr
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state
        if before_change is not None:
            self.before_change = before_change
        if after_change is not None:
            self.after_change = after_change
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_date is not None:
            self.modified_date = modified_date
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if status_map is not None:
            self.status_map = status_map
        if domain_id is not None:
            self.domain_id = domain_id
        if source_system is not None:
            self.source_system = source_system
        if source_system_link is not None:
            self.source_system_link = source_system_link
        if issue_category is not None:
            self.issue_category = issue_category
        if issue_id is not None:
            self.issue_id = issue_id
        if issue_status is not None:
            self.issue_status = issue_status
        if issue_severity is not None:
            self.issue_severity = issue_severity
        if issue_priority is not None:
            self.issue_priority = issue_priority
        if domain_title is not None:
            self.domain_title = domain_title
        if src_domain_title is not None:
            self.src_domain_title = src_domain_title
        if issue_assignee_name is not None:
            self.issue_assignee_name = issue_assignee_name
        if change_reason is not None:
            self.change_reason = change_reason
        if change_type is not None:
            self.change_type = change_type
        if source_system_id is not None:
            self.source_system_id = source_system_id
        if change_description is not None:
            self.change_description = change_description
        if has_deleted is not None:
            self.has_deleted = has_deleted
        if approval_phase_result is not None:
            self.approval_phase_result = approval_phase_result
        if approval_complete_time is not None:
            self.approval_complete_time = approval_complete_time
        if ccb_description is not None:
            self.ccb_description = ccb_description
        if actual_ccb is not None:
            self.actual_ccb = actual_ccb
        if ccbs is not None:
            self.ccbs = ccbs
        if ccb_info is not None:
            self.ccb_info = ccb_info
        if opinions is not None:
            self.opinions = opinions
        if opinion_comments is not None:
            self.opinion_comments = opinion_comments
        if approval_time is not None:
            self.approval_time = approval_time
        if src_domain_id is not None:
            self.src_domain_id = src_domain_id
        if cross_domain is not None:
            self.cross_domain = cross_domain
        if domain_moved is not None:
            self.domain_moved = domain_moved
        if reviewer is not None:
            self.reviewer = reviewer
        if approver is not None:
            self.approver = approver
        if rounds is not None:
            self.rounds = rounds
        if last_round_result is not None:
            self.last_round_result = last_round_result

    @property
    def region(self):
        r"""Gets the region of this ProcessInstanceResponseResultCos.

        区域

        :return: The region of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ProcessInstanceResponseResultCos.

        区域

        :param region: The region of this ProcessInstanceResponseResultCos.
        :type region: str
        """
        self._region = region

    @property
    def category(self):
        r"""Gets the category of this ProcessInstanceResponseResultCos.

        变更对象工作项类型，此处固定为CO

        :return: The category of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ProcessInstanceResponseResultCos.

        变更对象工作项类型，此处固定为CO

        :param category: The category of this ProcessInstanceResponseResultCos.
        :type category: str
        """
        self._category = category

    @property
    def title(self):
        r"""Gets the title of this ProcessInstanceResponseResultCos.

        评审单标题

        :return: The title of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ProcessInstanceResponseResultCos.

        评审单标题

        :param title: The title of this ProcessInstanceResponseResultCos.
        :type title: str
        """
        self._title = title

    @property
    def status(self):
        r"""Gets the status of this ProcessInstanceResponseResultCos.

        变更对象状态

        :return: The status of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ProcessInstanceResponseResultCos.

        变更对象状态

        :param status: The status of this ProcessInstanceResponseResultCos.
        :type status: str
        """
        self._status = status

    @property
    def assignee(self):
        r"""Gets the assignee of this ProcessInstanceResponseResultCos.

        :return: The assignee of this ProcessInstanceResponseResultCos.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultAssignee`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this ProcessInstanceResponseResultCos.

        :param assignee: The assignee of this ProcessInstanceResponseResultCos.
        :type assignee: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultAssignee`
        """
        self._assignee = assignee

    @property
    def description(self):
        r"""Gets the description of this ProcessInstanceResponseResultCos.

        评审单描述

        :return: The description of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProcessInstanceResponseResultCos.

        评审单描述

        :param description: The description of this ProcessInstanceResponseResultCos.
        :type description: str
        """
        self._description = description

    @property
    def number(self):
        r"""Gets the number of this ProcessInstanceResponseResultCos.

        变更对象关联的工作项编号

        :return: The number of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ProcessInstanceResponseResultCos.

        变更对象关联的工作项编号

        :param number: The number of this ProcessInstanceResponseResultCos.
        :type number: str
        """
        self._number = number

    @property
    def order(self):
        r"""Gets the order of this ProcessInstanceResponseResultCos.

        排序

        :return: The order of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ProcessInstanceResponseResultCos.

        排序

        :param order: The order of this ProcessInstanceResponseResultCos.
        :type order: str
        """
        self._order = order

    @property
    def co2cr(self):
        r"""Gets the co2cr of this ProcessInstanceResponseResultCos.

        关联的变更评审标识

        :return: The co2cr of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._co2cr

    @co2cr.setter
    def co2cr(self, co2cr):
        r"""Sets the co2cr of this ProcessInstanceResponseResultCos.

        关联的变更评审标识

        :param co2cr: The co2cr of this ProcessInstanceResponseResultCos.
        :type co2cr: str
        """
        self._co2cr = co2cr

    @property
    def co2br(self):
        r"""Gets the co2br of this ProcessInstanceResponseResultCos.

        关联的基线评审标识

        :return: The co2br of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._co2br

    @co2br.setter
    def co2br(self, co2br):
        r"""Sets the co2br of this ProcessInstanceResponseResultCos.

        关联的基线评审标识

        :param co2br: The co2br of this ProcessInstanceResponseResultCos.
        :type co2br: str
        """
        self._co2br = co2br

    @property
    def co2gr(self):
        r"""Gets the co2gr of this ProcessInstanceResponseResultCos.

        关联的通用评审标识

        :return: The co2gr of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._co2gr

    @co2gr.setter
    def co2gr(self, co2gr):
        r"""Sets the co2gr of this ProcessInstanceResponseResultCos.

        关联的通用评审标识

        :param co2gr: The co2gr of this ProcessInstanceResponseResultCos.
        :type co2gr: str
        """
        self._co2gr = co2gr

    @property
    def id(self):
        r"""Gets the id of this ProcessInstanceResponseResultCos.

        审批对象Id

        :return: The id of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProcessInstanceResponseResultCos.

        审批对象Id

        :param id: The id of this ProcessInstanceResponseResultCos.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ProcessInstanceResponseResultCos.

        评审单类型

        :return: The type of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ProcessInstanceResponseResultCos.

        评审单类型

        :param type: The type of this ProcessInstanceResponseResultCos.
        :type type: str
        """
        self._type = type

    @property
    def state(self):
        r"""Gets the state of this ProcessInstanceResponseResultCos.

        评审单工作状态，取值为\"正在工作\",\"作废\"

        :return: The state of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ProcessInstanceResponseResultCos.

        评审单工作状态，取值为\"正在工作\",\"作废\"

        :param state: The state of this ProcessInstanceResponseResultCos.
        :type state: str
        """
        self._state = state

    @property
    def before_change(self):
        r"""Gets the before_change of this ProcessInstanceResponseResultCos.

        变更对象工作项修改前内容

        :return: The before_change of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._before_change

    @before_change.setter
    def before_change(self, before_change):
        r"""Sets the before_change of this ProcessInstanceResponseResultCos.

        变更对象工作项修改前内容

        :param before_change: The before_change of this ProcessInstanceResponseResultCos.
        :type before_change: str
        """
        self._before_change = before_change

    @property
    def after_change(self):
        r"""Gets the after_change of this ProcessInstanceResponseResultCos.

        变更对象修改后内容

        :return: The after_change of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._after_change

    @after_change.setter
    def after_change(self, after_change):
        r"""Sets the after_change of this ProcessInstanceResponseResultCos.

        变更对象修改后内容

        :param after_change: The after_change of this ProcessInstanceResponseResultCos.
        :type after_change: str
        """
        self._after_change = after_change

    @property
    def modified_by(self):
        r"""Gets the modified_by of this ProcessInstanceResponseResultCos.

        评审单最后修改人

        :return: The modified_by of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this ProcessInstanceResponseResultCos.

        评审单最后修改人

        :param modified_by: The modified_by of this ProcessInstanceResponseResultCos.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def modified_date(self):
        r"""Gets the modified_date of this ProcessInstanceResponseResultCos.

        评审单最后修改时间

        :return: The modified_date of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this ProcessInstanceResponseResultCos.

        评审单最后修改时间

        :param modified_date: The modified_date of this ProcessInstanceResponseResultCos.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def created_by(self):
        r"""Gets the created_by of this ProcessInstanceResponseResultCos.

        评审单创建人

        :return: The created_by of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ProcessInstanceResponseResultCos.

        评审单创建人

        :param created_by: The created_by of this ProcessInstanceResponseResultCos.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this ProcessInstanceResponseResultCos.

        评审单创建时间

        :return: The created_date of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this ProcessInstanceResponseResultCos.

        评审单创建时间

        :param created_date: The created_date of this ProcessInstanceResponseResultCos.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ProcessInstanceResponseResultCos.

        工作项所属租户ID，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**tenant_id**字段的值就是工作项所属租户id

        :return: The tenant_id of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ProcessInstanceResponseResultCos.

        工作项所属租户ID，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**tenant_id**字段的值就是工作项所属租户id

        :param tenant_id: The tenant_id of this ProcessInstanceResponseResultCos.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def status_map(self):
        r"""Gets the status_map of this ProcessInstanceResponseResultCos.

        工作项状态

        :return: The status_map of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._status_map

    @status_map.setter
    def status_map(self, status_map):
        r"""Sets the status_map of this ProcessInstanceResponseResultCos.

        工作项状态

        :param status_map: The status_map of this ProcessInstanceResponseResultCos.
        :type status_map: str
        """
        self._status_map = status_map

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ProcessInstanceResponseResultCos.

        租户id

        :return: The domain_id of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ProcessInstanceResponseResultCos.

        租户id

        :param domain_id: The domain_id of this ProcessInstanceResponseResultCos.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def source_system(self):
        r"""Gets the source_system of this ProcessInstanceResponseResultCos.

        源系统

        :return: The source_system of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._source_system

    @source_system.setter
    def source_system(self, source_system):
        r"""Sets the source_system of this ProcessInstanceResponseResultCos.

        源系统

        :param source_system: The source_system of this ProcessInstanceResponseResultCos.
        :type source_system: str
        """
        self._source_system = source_system

    @property
    def source_system_link(self):
        r"""Gets the source_system_link of this ProcessInstanceResponseResultCos.

        源系统链接

        :return: The source_system_link of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._source_system_link

    @source_system_link.setter
    def source_system_link(self, source_system_link):
        r"""Sets the source_system_link of this ProcessInstanceResponseResultCos.

        源系统链接

        :param source_system_link: The source_system_link of this ProcessInstanceResponseResultCos.
        :type source_system_link: str
        """
        self._source_system_link = source_system_link

    @property
    def issue_category(self):
        r"""Gets the issue_category of this ProcessInstanceResponseResultCos.

        变更对象关联的工作项类型

        :return: The issue_category of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._issue_category

    @issue_category.setter
    def issue_category(self, issue_category):
        r"""Sets the issue_category of this ProcessInstanceResponseResultCos.

        变更对象关联的工作项类型

        :param issue_category: The issue_category of this ProcessInstanceResponseResultCos.
        :type issue_category: str
        """
        self._issue_category = issue_category

    @property
    def issue_id(self):
        r"""Gets the issue_id of this ProcessInstanceResponseResultCos.

        工作项ID

        :return: The issue_id of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this ProcessInstanceResponseResultCos.

        工作项ID

        :param issue_id: The issue_id of this ProcessInstanceResponseResultCos.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def issue_status(self):
        r"""Gets the issue_status of this ProcessInstanceResponseResultCos.

        :return: The issue_status of this ProcessInstanceResponseResultCos.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultIssueStatus`
        """
        return self._issue_status

    @issue_status.setter
    def issue_status(self, issue_status):
        r"""Sets the issue_status of this ProcessInstanceResponseResultCos.

        :param issue_status: The issue_status of this ProcessInstanceResponseResultCos.
        :type issue_status: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultIssueStatus`
        """
        self._issue_status = issue_status

    @property
    def issue_severity(self):
        r"""Gets the issue_severity of this ProcessInstanceResponseResultCos.

        工作项严重程度

        :return: The issue_severity of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._issue_severity

    @issue_severity.setter
    def issue_severity(self, issue_severity):
        r"""Sets the issue_severity of this ProcessInstanceResponseResultCos.

        工作项严重程度

        :param issue_severity: The issue_severity of this ProcessInstanceResponseResultCos.
        :type issue_severity: str
        """
        self._issue_severity = issue_severity

    @property
    def issue_priority(self):
        r"""Gets the issue_priority of this ProcessInstanceResponseResultCos.

        :return: The issue_priority of this ProcessInstanceResponseResultCos.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultIssuePriority`
        """
        return self._issue_priority

    @issue_priority.setter
    def issue_priority(self, issue_priority):
        r"""Sets the issue_priority of this ProcessInstanceResponseResultCos.

        :param issue_priority: The issue_priority of this ProcessInstanceResponseResultCos.
        :type issue_priority: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultIssuePriority`
        """
        self._issue_priority = issue_priority

    @property
    def domain_title(self):
        r"""Gets the domain_title of this ProcessInstanceResponseResultCos.

        归属项目名称

        :return: The domain_title of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._domain_title

    @domain_title.setter
    def domain_title(self, domain_title):
        r"""Sets the domain_title of this ProcessInstanceResponseResultCos.

        归属项目名称

        :param domain_title: The domain_title of this ProcessInstanceResponseResultCos.
        :type domain_title: str
        """
        self._domain_title = domain_title

    @property
    def src_domain_title(self):
        r"""Gets the src_domain_title of this ProcessInstanceResponseResultCos.

        提出项目名称

        :return: The src_domain_title of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._src_domain_title

    @src_domain_title.setter
    def src_domain_title(self, src_domain_title):
        r"""Sets the src_domain_title of this ProcessInstanceResponseResultCos.

        提出项目名称

        :param src_domain_title: The src_domain_title of this ProcessInstanceResponseResultCos.
        :type src_domain_title: str
        """
        self._src_domain_title = src_domain_title

    @property
    def issue_assignee_name(self):
        r"""Gets the issue_assignee_name of this ProcessInstanceResponseResultCos.

        责任人昵称

        :return: The issue_assignee_name of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._issue_assignee_name

    @issue_assignee_name.setter
    def issue_assignee_name(self, issue_assignee_name):
        r"""Sets the issue_assignee_name of this ProcessInstanceResponseResultCos.

        责任人昵称

        :param issue_assignee_name: The issue_assignee_name of this ProcessInstanceResponseResultCos.
        :type issue_assignee_name: str
        """
        self._issue_assignee_name = issue_assignee_name

    @property
    def change_reason(self):
        r"""Gets the change_reason of this ProcessInstanceResponseResultCos.

        评审原因

        :return: The change_reason of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._change_reason

    @change_reason.setter
    def change_reason(self, change_reason):
        r"""Sets the change_reason of this ProcessInstanceResponseResultCos.

        评审原因

        :param change_reason: The change_reason of this ProcessInstanceResponseResultCos.
        :type change_reason: str
        """
        self._change_reason = change_reason

    @property
    def change_type(self):
        r"""Gets the change_type of this ProcessInstanceResponseResultCos.

        评审类型

        :return: The change_type of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this ProcessInstanceResponseResultCos.

        评审类型

        :param change_type: The change_type of this ProcessInstanceResponseResultCos.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def source_system_id(self):
        r"""Gets the source_system_id of this ProcessInstanceResponseResultCos.

        源系统id

        :return: The source_system_id of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._source_system_id

    @source_system_id.setter
    def source_system_id(self, source_system_id):
        r"""Sets the source_system_id of this ProcessInstanceResponseResultCos.

        源系统id

        :param source_system_id: The source_system_id of this ProcessInstanceResponseResultCos.
        :type source_system_id: str
        """
        self._source_system_id = source_system_id

    @property
    def change_description(self):
        r"""Gets the change_description of this ProcessInstanceResponseResultCos.

        评审描述

        :return: The change_description of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._change_description

    @change_description.setter
    def change_description(self, change_description):
        r"""Sets the change_description of this ProcessInstanceResponseResultCos.

        评审描述

        :param change_description: The change_description of this ProcessInstanceResponseResultCos.
        :type change_description: str
        """
        self._change_description = change_description

    @property
    def has_deleted(self):
        r"""Gets the has_deleted of this ProcessInstanceResponseResultCos.

        是否已删除

        :return: The has_deleted of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._has_deleted

    @has_deleted.setter
    def has_deleted(self, has_deleted):
        r"""Sets the has_deleted of this ProcessInstanceResponseResultCos.

        是否已删除

        :param has_deleted: The has_deleted of this ProcessInstanceResponseResultCos.
        :type has_deleted: str
        """
        self._has_deleted = has_deleted

    @property
    def approval_phase_result(self):
        r"""Gets the approval_phase_result of this ProcessInstanceResponseResultCos.

        评审结果

        :return: The approval_phase_result of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._approval_phase_result

    @approval_phase_result.setter
    def approval_phase_result(self, approval_phase_result):
        r"""Sets the approval_phase_result of this ProcessInstanceResponseResultCos.

        评审结果

        :param approval_phase_result: The approval_phase_result of this ProcessInstanceResponseResultCos.
        :type approval_phase_result: str
        """
        self._approval_phase_result = approval_phase_result

    @property
    def approval_complete_time(self):
        r"""Gets the approval_complete_time of this ProcessInstanceResponseResultCos.

        评审完成时间

        :return: The approval_complete_time of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._approval_complete_time

    @approval_complete_time.setter
    def approval_complete_time(self, approval_complete_time):
        r"""Sets the approval_complete_time of this ProcessInstanceResponseResultCos.

        评审完成时间

        :param approval_complete_time: The approval_complete_time of this ProcessInstanceResponseResultCos.
        :type approval_complete_time: str
        """
        self._approval_complete_time = approval_complete_time

    @property
    def ccb_description(self):
        r"""Gets the ccb_description of this ProcessInstanceResponseResultCos.

        评审描述

        :return: The ccb_description of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._ccb_description

    @ccb_description.setter
    def ccb_description(self, ccb_description):
        r"""Sets the ccb_description of this ProcessInstanceResponseResultCos.

        评审描述

        :param ccb_description: The ccb_description of this ProcessInstanceResponseResultCos.
        :type ccb_description: str
        """
        self._ccb_description = ccb_description

    @property
    def actual_ccb(self):
        r"""Gets the actual_ccb of this ProcessInstanceResponseResultCos.

        评审专家

        :return: The actual_ccb of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._actual_ccb

    @actual_ccb.setter
    def actual_ccb(self, actual_ccb):
        r"""Sets the actual_ccb of this ProcessInstanceResponseResultCos.

        评审专家

        :param actual_ccb: The actual_ccb of this ProcessInstanceResponseResultCos.
        :type actual_ccb: str
        """
        self._actual_ccb = actual_ccb

    @property
    def ccbs(self):
        r"""Gets the ccbs of this ProcessInstanceResponseResultCos.

        审批信息列表

        :return: The ccbs of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._ccbs

    @ccbs.setter
    def ccbs(self, ccbs):
        r"""Sets the ccbs of this ProcessInstanceResponseResultCos.

        审批信息列表

        :param ccbs: The ccbs of this ProcessInstanceResponseResultCos.
        :type ccbs: str
        """
        self._ccbs = ccbs

    @property
    def ccb_info(self):
        r"""Gets the ccb_info of this ProcessInstanceResponseResultCos.

        评审信息

        :return: The ccb_info of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._ccb_info

    @ccb_info.setter
    def ccb_info(self, ccb_info):
        r"""Sets the ccb_info of this ProcessInstanceResponseResultCos.

        评审信息

        :param ccb_info: The ccb_info of this ProcessInstanceResponseResultCos.
        :type ccb_info: str
        """
        self._ccb_info = ccb_info

    @property
    def opinions(self):
        r"""Gets the opinions of this ProcessInstanceResponseResultCos.

        变更对象评审专家Id列表（创建变更评审时使用）

        :return: The opinions of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._opinions

    @opinions.setter
    def opinions(self, opinions):
        r"""Sets the opinions of this ProcessInstanceResponseResultCos.

        变更对象评审专家Id列表（创建变更评审时使用）

        :param opinions: The opinions of this ProcessInstanceResponseResultCos.
        :type opinions: str
        """
        self._opinions = opinions

    @property
    def opinion_comments(self):
        r"""Gets the opinion_comments of this ProcessInstanceResponseResultCos.

        评审意见

        :return: The opinion_comments of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._opinion_comments

    @opinion_comments.setter
    def opinion_comments(self, opinion_comments):
        r"""Sets the opinion_comments of this ProcessInstanceResponseResultCos.

        评审意见

        :param opinion_comments: The opinion_comments of this ProcessInstanceResponseResultCos.
        :type opinion_comments: str
        """
        self._opinion_comments = opinion_comments

    @property
    def approval_time(self):
        r"""Gets the approval_time of this ProcessInstanceResponseResultCos.

        审批时间

        :return: The approval_time of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._approval_time

    @approval_time.setter
    def approval_time(self, approval_time):
        r"""Sets the approval_time of this ProcessInstanceResponseResultCos.

        审批时间

        :param approval_time: The approval_time of this ProcessInstanceResponseResultCos.
        :type approval_time: str
        """
        self._approval_time = approval_time

    @property
    def src_domain_id(self):
        r"""Gets the src_domain_id of this ProcessInstanceResponseResultCos.

        租户id

        :return: The src_domain_id of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._src_domain_id

    @src_domain_id.setter
    def src_domain_id(self, src_domain_id):
        r"""Sets the src_domain_id of this ProcessInstanceResponseResultCos.

        租户id

        :param src_domain_id: The src_domain_id of this ProcessInstanceResponseResultCos.
        :type src_domain_id: str
        """
        self._src_domain_id = src_domain_id

    @property
    def cross_domain(self):
        r"""Gets the cross_domain of this ProcessInstanceResponseResultCos.

        是否跨租户

        :return: The cross_domain of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._cross_domain

    @cross_domain.setter
    def cross_domain(self, cross_domain):
        r"""Sets the cross_domain of this ProcessInstanceResponseResultCos.

        是否跨租户

        :param cross_domain: The cross_domain of this ProcessInstanceResponseResultCos.
        :type cross_domain: str
        """
        self._cross_domain = cross_domain

    @property
    def domain_moved(self):
        r"""Gets the domain_moved of this ProcessInstanceResponseResultCos.

        归属项目是否迁移

        :return: The domain_moved of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._domain_moved

    @domain_moved.setter
    def domain_moved(self, domain_moved):
        r"""Sets the domain_moved of this ProcessInstanceResponseResultCos.

        归属项目是否迁移

        :param domain_moved: The domain_moved of this ProcessInstanceResponseResultCos.
        :type domain_moved: str
        """
        self._domain_moved = domain_moved

    @property
    def reviewer(self):
        r"""Gets the reviewer of this ProcessInstanceResponseResultCos.

        评审专家

        :return: The reviewer of this ProcessInstanceResponseResultCos.
        :rtype: list[str]
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        r"""Sets the reviewer of this ProcessInstanceResponseResultCos.

        评审专家

        :param reviewer: The reviewer of this ProcessInstanceResponseResultCos.
        :type reviewer: list[str]
        """
        self._reviewer = reviewer

    @property
    def approver(self):
        r"""Gets the approver of this ProcessInstanceResponseResultCos.

        决策人

        :return: The approver of this ProcessInstanceResponseResultCos.
        :rtype: list[str]
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        r"""Sets the approver of this ProcessInstanceResponseResultCos.

        决策人

        :param approver: The approver of this ProcessInstanceResponseResultCos.
        :type approver: list[str]
        """
        self._approver = approver

    @property
    def rounds(self):
        r"""Gets the rounds of this ProcessInstanceResponseResultCos.

        评审轮次

        :return: The rounds of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._rounds

    @rounds.setter
    def rounds(self, rounds):
        r"""Sets the rounds of this ProcessInstanceResponseResultCos.

        评审轮次

        :param rounds: The rounds of this ProcessInstanceResponseResultCos.
        :type rounds: str
        """
        self._rounds = rounds

    @property
    def last_round_result(self):
        r"""Gets the last_round_result of this ProcessInstanceResponseResultCos.

        最近一轮决策结果

        :return: The last_round_result of this ProcessInstanceResponseResultCos.
        :rtype: str
        """
        return self._last_round_result

    @last_round_result.setter
    def last_round_result(self, last_round_result):
        r"""Sets the last_round_result of this ProcessInstanceResponseResultCos.

        最近一轮决策结果

        :param last_round_result: The last_round_result of this ProcessInstanceResponseResultCos.
        :type last_round_result: str
        """
        self._last_round_result = last_round_result

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
        if not isinstance(other, ProcessInstanceResponseResultCos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
