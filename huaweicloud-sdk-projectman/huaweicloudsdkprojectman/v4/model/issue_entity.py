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
        'parent_id': 'str',
        'project_id': 'str',
        'status': 'str',
        'state': 'str',
        'assignee': 'UserEntity',
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
        'change_status': 'str',
        'no_break_reason': 'str',
        'submitted_by': 'str',
        'ir2rr': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'type': 'type',
        'number': 'number',
        'category': 'category',
        'parent_id': 'parent_id',
        'project_id': 'project_id',
        'status': 'status',
        'state': 'state',
        'assignee': 'assignee',
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
        'change_status': 'change_status',
        'no_break_reason': 'no_break_reason',
        'submitted_by': 'submitted_by',
        'ir2rr': 'ir2rr'
    }

    def __init__(self, id=None, title=None, description=None, type=None, number=None, category=None, parent_id=None, project_id=None, status=None, state=None, assignee=None, created_by=None, created_time=None, modified_by=None, modified_time=None, plan_end_date=None, close_time=None, workload=None, workload_sum=None, tenant_id=None, link=None, suspended=None, status_modified_time=None, labels=None, custom_fields=None, children=None, path=None, ir2feature=None, need_break=None, break_status=None, baseline=None, priority=None, related_network_security=None, collaboratives=None, business_domain=None, plan_pi=None, change_status=None, no_break_reason=None, submitted_by=None, ir2rr=None):
        r"""IssueEntity

        The model defined in huaweicloud sdk

        :param id: 工作项id
        :type id: str
        :param title: 工作项标题
        :type title: str
        :param description: 工作项描述字段
        :type description: str
        :param type: 工作项大分类定义 requirement(研发需求)、bug(缺陷)、task(任务)、feature(特性)、raw_requirement(原始需求)
        :type type: str
        :param number: 工作项编号
        :type number: str
        :param category: 工作项类型，编辑工作项时，此字段必填、值为当前工作项正确的工作项类型，但不会更新此字段
        :type category: str
        :param parent_id: 父工作项id
        :type parent_id: str
        :param project_id: 工作项所属的项目id
        :type project_id: str
        :param status: 工作项状态code
        :type status: str
        :param state: 工作项的生命周期，可选值为\&quot;正在工作\&quot;,\&quot;作废\&quot;
        :type state: str
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param created_time: 工作项创建时间
        :type created_time: str
        :param modified_by: 
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param modified_time: 工作项最近更新时间
        :type modified_time: str
        :param plan_end_date: 工作项计划结束日期，时间戳
        :type plan_end_date: str
        :param close_time: 工作项关闭时间
        :type close_time: str
        :param workload: 工作项计划工时，保留一位小数，取值范围为0~999999999.9
        :type workload: str
        :param workload_sum: 工作项计划工时，保留一位小数，取值范围为0~999999999.9，不可编辑
        :type workload_sum: str
        :param tenant_id: 工作项所属租户id
        :type tenant_id: str
        :param link: 工作项关联项id，多个关联项用英文逗号分隔，同一工作项最多支持50个关联项
        :type link: str
        :param suspended: 工作项是否已挂起
        :type suspended: bool
        :param status_modified_time: 工作项状态改变时间，可用于计算工作项在当前状态停留天数
        :type status_modified_time: str
        :param labels: 工作项标签
        :type labels: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        :param custom_fields: 工作项自定义字段映射，用户添加的系统字段也在此列 { \&quot;code\&quot;:\&quot;字段code\&quot;, \&quot;value\&quot;:\&quot;字段值\&quot; }
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        :param children: 工作项的子工作项集合
        :type children: list[:class:`huaweicloudsdkprojectman.v4.IssueEntity`]
        :param path: 子工作项的路径
        :type path: str
        :param ir2feature: IR和FE的关联字段，工作项类型为IR时，有此字段
        :type ir2feature: str
        :param need_break: 工作项是否需要分解,仅可以分解的工作项类型有此字段
        :type need_break: str
        :param break_status: 分解状态 已分解—decomposed 未分解—undecomposed 不涉及— --
        :type break_status: str
        :param baseline: 工作项基线状态 未基线 —— null 已基线 —— baselined 基线评审中——baseline-reviewing
        :type baseline: str
        :param priority: 工作项优先级，部分工作项有此字段
        :type priority: str
        :param related_network_security: 是否涉及网络安全。预设字段中，仅研发需求有此字段
        :type related_network_security: str
        :param collaboratives: 研发需求协同信息，协同任务id
        :type collaboratives: str
        :param business_domain: 领域字段
        :type business_domain: str
        :param plan_pi: 工作项发布(老版本名为PI) id
        :type plan_pi: str
        :param change_status: 工作项变更状态 变更评审中——change-reviewing 已变更——changed 未变更-unchange或null
        :type change_status: str
        :param no_break_reason: 无需分解原因，need_break&#x3D;no时有此字段
        :type no_break_reason: str
        :param submitted_by: 提出人，部分工作项有此字段，多人时用英文逗号分隔
        :type submitted_by: str
        :param ir2rr: IR关联的RR id，多选时用英文逗号分隔
        :type ir2rr: str
        """
        
        

        self._id = None
        self._title = None
        self._description = None
        self._type = None
        self._number = None
        self._category = None
        self._parent_id = None
        self._project_id = None
        self._status = None
        self._state = None
        self._assignee = None
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
        self._change_status = None
        self._no_break_reason = None
        self._submitted_by = None
        self._ir2rr = None
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
        if category is not None:
            self.category = category
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
        if change_status is not None:
            self.change_status = change_status
        if no_break_reason is not None:
            self.no_break_reason = no_break_reason
        if submitted_by is not None:
            self.submitted_by = submitted_by
        if ir2rr is not None:
            self.ir2rr = ir2rr

    @property
    def id(self):
        r"""Gets the id of this IssueEntity.

        工作项id

        :return: The id of this IssueEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueEntity.

        工作项id

        :param id: The id of this IssueEntity.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this IssueEntity.

        工作项标题

        :return: The title of this IssueEntity.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this IssueEntity.

        工作项标题

        :param title: The title of this IssueEntity.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this IssueEntity.

        工作项描述字段

        :return: The description of this IssueEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IssueEntity.

        工作项描述字段

        :param description: The description of this IssueEntity.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this IssueEntity.

        工作项大分类定义 requirement(研发需求)、bug(缺陷)、task(任务)、feature(特性)、raw_requirement(原始需求)

        :return: The type of this IssueEntity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IssueEntity.

        工作项大分类定义 requirement(研发需求)、bug(缺陷)、task(任务)、feature(特性)、raw_requirement(原始需求)

        :param type: The type of this IssueEntity.
        :type type: str
        """
        self._type = type

    @property
    def number(self):
        r"""Gets the number of this IssueEntity.

        工作项编号

        :return: The number of this IssueEntity.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this IssueEntity.

        工作项编号

        :param number: The number of this IssueEntity.
        :type number: str
        """
        self._number = number

    @property
    def category(self):
        r"""Gets the category of this IssueEntity.

        工作项类型，编辑工作项时，此字段必填、值为当前工作项正确的工作项类型，但不会更新此字段

        :return: The category of this IssueEntity.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this IssueEntity.

        工作项类型，编辑工作项时，此字段必填、值为当前工作项正确的工作项类型，但不会更新此字段

        :param category: The category of this IssueEntity.
        :type category: str
        """
        self._category = category

    @property
    def parent_id(self):
        r"""Gets the parent_id of this IssueEntity.

        父工作项id

        :return: The parent_id of this IssueEntity.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this IssueEntity.

        父工作项id

        :param parent_id: The parent_id of this IssueEntity.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def project_id(self):
        r"""Gets the project_id of this IssueEntity.

        工作项所属的项目id

        :return: The project_id of this IssueEntity.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this IssueEntity.

        工作项所属的项目id

        :param project_id: The project_id of this IssueEntity.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def status(self):
        r"""Gets the status of this IssueEntity.

        工作项状态code

        :return: The status of this IssueEntity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IssueEntity.

        工作项状态code

        :param status: The status of this IssueEntity.
        :type status: str
        """
        self._status = status

    @property
    def state(self):
        r"""Gets the state of this IssueEntity.

        工作项的生命周期，可选值为\"正在工作\",\"作废\"

        :return: The state of this IssueEntity.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this IssueEntity.

        工作项的生命周期，可选值为\"正在工作\",\"作废\"

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

        工作项创建时间

        :return: The created_time of this IssueEntity.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this IssueEntity.

        工作项创建时间

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

        工作项最近更新时间

        :return: The modified_time of this IssueEntity.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this IssueEntity.

        工作项最近更新时间

        :param modified_time: The modified_time of this IssueEntity.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this IssueEntity.

        工作项计划结束日期，时间戳

        :return: The plan_end_date of this IssueEntity.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this IssueEntity.

        工作项计划结束日期，时间戳

        :param plan_end_date: The plan_end_date of this IssueEntity.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def close_time(self):
        r"""Gets the close_time of this IssueEntity.

        工作项关闭时间

        :return: The close_time of this IssueEntity.
        :rtype: str
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        r"""Sets the close_time of this IssueEntity.

        工作项关闭时间

        :param close_time: The close_time of this IssueEntity.
        :type close_time: str
        """
        self._close_time = close_time

    @property
    def workload(self):
        r"""Gets the workload of this IssueEntity.

        工作项计划工时，保留一位小数，取值范围为0~999999999.9

        :return: The workload of this IssueEntity.
        :rtype: str
        """
        return self._workload

    @workload.setter
    def workload(self, workload):
        r"""Sets the workload of this IssueEntity.

        工作项计划工时，保留一位小数，取值范围为0~999999999.9

        :param workload: The workload of this IssueEntity.
        :type workload: str
        """
        self._workload = workload

    @property
    def workload_sum(self):
        r"""Gets the workload_sum of this IssueEntity.

        工作项计划工时，保留一位小数，取值范围为0~999999999.9，不可编辑

        :return: The workload_sum of this IssueEntity.
        :rtype: str
        """
        return self._workload_sum

    @workload_sum.setter
    def workload_sum(self, workload_sum):
        r"""Sets the workload_sum of this IssueEntity.

        工作项计划工时，保留一位小数，取值范围为0~999999999.9，不可编辑

        :param workload_sum: The workload_sum of this IssueEntity.
        :type workload_sum: str
        """
        self._workload_sum = workload_sum

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this IssueEntity.

        工作项所属租户id

        :return: The tenant_id of this IssueEntity.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this IssueEntity.

        工作项所属租户id

        :param tenant_id: The tenant_id of this IssueEntity.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def link(self):
        r"""Gets the link of this IssueEntity.

        工作项关联项id，多个关联项用英文逗号分隔，同一工作项最多支持50个关联项

        :return: The link of this IssueEntity.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this IssueEntity.

        工作项关联项id，多个关联项用英文逗号分隔，同一工作项最多支持50个关联项

        :param link: The link of this IssueEntity.
        :type link: str
        """
        self._link = link

    @property
    def suspended(self):
        r"""Gets the suspended of this IssueEntity.

        工作项是否已挂起

        :return: The suspended of this IssueEntity.
        :rtype: bool
        """
        return self._suspended

    @suspended.setter
    def suspended(self, suspended):
        r"""Sets the suspended of this IssueEntity.

        工作项是否已挂起

        :param suspended: The suspended of this IssueEntity.
        :type suspended: bool
        """
        self._suspended = suspended

    @property
    def status_modified_time(self):
        r"""Gets the status_modified_time of this IssueEntity.

        工作项状态改变时间，可用于计算工作项在当前状态停留天数

        :return: The status_modified_time of this IssueEntity.
        :rtype: str
        """
        return self._status_modified_time

    @status_modified_time.setter
    def status_modified_time(self, status_modified_time):
        r"""Sets the status_modified_time of this IssueEntity.

        工作项状态改变时间，可用于计算工作项在当前状态停留天数

        :param status_modified_time: The status_modified_time of this IssueEntity.
        :type status_modified_time: str
        """
        self._status_modified_time = status_modified_time

    @property
    def labels(self):
        r"""Gets the labels of this IssueEntity.

        工作项标签

        :return: The labels of this IssueEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this IssueEntity.

        工作项标签

        :param labels: The labels of this IssueEntity.
        :type labels: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        """
        self._labels = labels

    @property
    def custom_fields(self):
        r"""Gets the custom_fields of this IssueEntity.

        工作项自定义字段映射，用户添加的系统字段也在此列 { \"code\":\"字段code\", \"value\":\"字段值\" }

        :return: The custom_fields of this IssueEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        r"""Sets the custom_fields of this IssueEntity.

        工作项自定义字段映射，用户添加的系统字段也在此列 { \"code\":\"字段code\", \"value\":\"字段值\" }

        :param custom_fields: The custom_fields of this IssueEntity.
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        """
        self._custom_fields = custom_fields

    @property
    def children(self):
        r"""Gets the children of this IssueEntity.

        工作项的子工作项集合

        :return: The children of this IssueEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueEntity`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this IssueEntity.

        工作项的子工作项集合

        :param children: The children of this IssueEntity.
        :type children: list[:class:`huaweicloudsdkprojectman.v4.IssueEntity`]
        """
        self._children = children

    @property
    def path(self):
        r"""Gets the path of this IssueEntity.

        子工作项的路径

        :return: The path of this IssueEntity.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this IssueEntity.

        子工作项的路径

        :param path: The path of this IssueEntity.
        :type path: str
        """
        self._path = path

    @property
    def ir2feature(self):
        r"""Gets the ir2feature of this IssueEntity.

        IR和FE的关联字段，工作项类型为IR时，有此字段

        :return: The ir2feature of this IssueEntity.
        :rtype: str
        """
        return self._ir2feature

    @ir2feature.setter
    def ir2feature(self, ir2feature):
        r"""Sets the ir2feature of this IssueEntity.

        IR和FE的关联字段，工作项类型为IR时，有此字段

        :param ir2feature: The ir2feature of this IssueEntity.
        :type ir2feature: str
        """
        self._ir2feature = ir2feature

    @property
    def need_break(self):
        r"""Gets the need_break of this IssueEntity.

        工作项是否需要分解,仅可以分解的工作项类型有此字段

        :return: The need_break of this IssueEntity.
        :rtype: str
        """
        return self._need_break

    @need_break.setter
    def need_break(self, need_break):
        r"""Sets the need_break of this IssueEntity.

        工作项是否需要分解,仅可以分解的工作项类型有此字段

        :param need_break: The need_break of this IssueEntity.
        :type need_break: str
        """
        self._need_break = need_break

    @property
    def break_status(self):
        r"""Gets the break_status of this IssueEntity.

        分解状态 已分解—decomposed 未分解—undecomposed 不涉及— --

        :return: The break_status of this IssueEntity.
        :rtype: str
        """
        return self._break_status

    @break_status.setter
    def break_status(self, break_status):
        r"""Sets the break_status of this IssueEntity.

        分解状态 已分解—decomposed 未分解—undecomposed 不涉及— --

        :param break_status: The break_status of this IssueEntity.
        :type break_status: str
        """
        self._break_status = break_status

    @property
    def baseline(self):
        r"""Gets the baseline of this IssueEntity.

        工作项基线状态 未基线 —— null 已基线 —— baselined 基线评审中——baseline-reviewing

        :return: The baseline of this IssueEntity.
        :rtype: str
        """
        return self._baseline

    @baseline.setter
    def baseline(self, baseline):
        r"""Sets the baseline of this IssueEntity.

        工作项基线状态 未基线 —— null 已基线 —— baselined 基线评审中——baseline-reviewing

        :param baseline: The baseline of this IssueEntity.
        :type baseline: str
        """
        self._baseline = baseline

    @property
    def priority(self):
        r"""Gets the priority of this IssueEntity.

        工作项优先级，部分工作项有此字段

        :return: The priority of this IssueEntity.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this IssueEntity.

        工作项优先级，部分工作项有此字段

        :param priority: The priority of this IssueEntity.
        :type priority: str
        """
        self._priority = priority

    @property
    def related_network_security(self):
        r"""Gets the related_network_security of this IssueEntity.

        是否涉及网络安全。预设字段中，仅研发需求有此字段

        :return: The related_network_security of this IssueEntity.
        :rtype: str
        """
        return self._related_network_security

    @related_network_security.setter
    def related_network_security(self, related_network_security):
        r"""Sets the related_network_security of this IssueEntity.

        是否涉及网络安全。预设字段中，仅研发需求有此字段

        :param related_network_security: The related_network_security of this IssueEntity.
        :type related_network_security: str
        """
        self._related_network_security = related_network_security

    @property
    def collaboratives(self):
        r"""Gets the collaboratives of this IssueEntity.

        研发需求协同信息，协同任务id

        :return: The collaboratives of this IssueEntity.
        :rtype: str
        """
        return self._collaboratives

    @collaboratives.setter
    def collaboratives(self, collaboratives):
        r"""Sets the collaboratives of this IssueEntity.

        研发需求协同信息，协同任务id

        :param collaboratives: The collaboratives of this IssueEntity.
        :type collaboratives: str
        """
        self._collaboratives = collaboratives

    @property
    def business_domain(self):
        r"""Gets the business_domain of this IssueEntity.

        领域字段

        :return: The business_domain of this IssueEntity.
        :rtype: str
        """
        return self._business_domain

    @business_domain.setter
    def business_domain(self, business_domain):
        r"""Sets the business_domain of this IssueEntity.

        领域字段

        :param business_domain: The business_domain of this IssueEntity.
        :type business_domain: str
        """
        self._business_domain = business_domain

    @property
    def plan_pi(self):
        r"""Gets the plan_pi of this IssueEntity.

        工作项发布(老版本名为PI) id

        :return: The plan_pi of this IssueEntity.
        :rtype: str
        """
        return self._plan_pi

    @plan_pi.setter
    def plan_pi(self, plan_pi):
        r"""Sets the plan_pi of this IssueEntity.

        工作项发布(老版本名为PI) id

        :param plan_pi: The plan_pi of this IssueEntity.
        :type plan_pi: str
        """
        self._plan_pi = plan_pi

    @property
    def change_status(self):
        r"""Gets the change_status of this IssueEntity.

        工作项变更状态 变更评审中——change-reviewing 已变更——changed 未变更-unchange或null

        :return: The change_status of this IssueEntity.
        :rtype: str
        """
        return self._change_status

    @change_status.setter
    def change_status(self, change_status):
        r"""Sets the change_status of this IssueEntity.

        工作项变更状态 变更评审中——change-reviewing 已变更——changed 未变更-unchange或null

        :param change_status: The change_status of this IssueEntity.
        :type change_status: str
        """
        self._change_status = change_status

    @property
    def no_break_reason(self):
        r"""Gets the no_break_reason of this IssueEntity.

        无需分解原因，need_break=no时有此字段

        :return: The no_break_reason of this IssueEntity.
        :rtype: str
        """
        return self._no_break_reason

    @no_break_reason.setter
    def no_break_reason(self, no_break_reason):
        r"""Sets the no_break_reason of this IssueEntity.

        无需分解原因，need_break=no时有此字段

        :param no_break_reason: The no_break_reason of this IssueEntity.
        :type no_break_reason: str
        """
        self._no_break_reason = no_break_reason

    @property
    def submitted_by(self):
        r"""Gets the submitted_by of this IssueEntity.

        提出人，部分工作项有此字段，多人时用英文逗号分隔

        :return: The submitted_by of this IssueEntity.
        :rtype: str
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        r"""Sets the submitted_by of this IssueEntity.

        提出人，部分工作项有此字段，多人时用英文逗号分隔

        :param submitted_by: The submitted_by of this IssueEntity.
        :type submitted_by: str
        """
        self._submitted_by = submitted_by

    @property
    def ir2rr(self):
        r"""Gets the ir2rr of this IssueEntity.

        IR关联的RR id，多选时用英文逗号分隔

        :return: The ir2rr of this IssueEntity.
        :rtype: str
        """
        return self._ir2rr

    @ir2rr.setter
    def ir2rr(self, ir2rr):
        r"""Sets the ir2rr of this IssueEntity.

        IR关联的RR id，多选时用英文逗号分隔

        :param ir2rr: The ir2rr of this IssueEntity.
        :type ir2rr: str
        """
        self._ir2rr = ir2rr

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
