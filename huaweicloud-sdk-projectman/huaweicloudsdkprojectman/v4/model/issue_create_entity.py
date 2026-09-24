# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueCreateEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'description': 'str',
        'category': 'str',
        'category_layer_id': 'str',
        'parent_id': 'str',
        'status': 'str',
        'assignee': 'UserEntity',
        'recipient': 'list[UserEntity]',
        'assigned_cc': 'list[UserEntity]',
        'plan_end_date': 'str',
        'workload': 'str',
        'link': 'str',
        'labels': 'list[LabelEntity]',
        'custom_fields': 'list[FieldCodeValuePair]',
        'ir2feature': 'str',
        'priority': 'str',
        'related_network_security': 'str',
        'collaboratives': 'str',
        'business_domain': 'str',
        'plan_pi': 'str',
        'submitted_by': 'list[UserEntity]',
        'ir2rr': 'str',
        'feature_set': 'str',
        'security_level': 'str'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'category': 'category',
        'category_layer_id': 'category_layer_id',
        'parent_id': 'parent_id',
        'status': 'status',
        'assignee': 'assignee',
        'recipient': 'recipient',
        'assigned_cc': 'assigned_cc',
        'plan_end_date': 'plan_end_date',
        'workload': 'workload',
        'link': 'link',
        'labels': 'labels',
        'custom_fields': 'custom_fields',
        'ir2feature': 'ir2feature',
        'priority': 'priority',
        'related_network_security': 'related_network_security',
        'collaboratives': 'collaboratives',
        'business_domain': 'business_domain',
        'plan_pi': 'plan_pi',
        'submitted_by': 'submitted_by',
        'ir2rr': 'ir2rr',
        'feature_set': 'feature_set',
        'security_level': 'security_level'
    }

    def __init__(self, title=None, description=None, category=None, category_layer_id=None, parent_id=None, status=None, assignee=None, recipient=None, assigned_cc=None, plan_end_date=None, workload=None, link=None, labels=None, custom_fields=None, ir2feature=None, priority=None, related_network_security=None, collaboratives=None, business_domain=None, plan_pi=None, submitted_by=None, ir2rr=None, feature_set=None, security_level=None):
        r"""IssueCreateEntity

        The model defined in huaweicloud sdk

        :param title: **参数解释**： 工作项标题。 **约束限制**：  不涉及。 **取值范围**： 2~256个字符。 **默认取值**： 不涉及。
        :type title: str
        :param description: **参数解释**： 工作项描述字段。 **约束限制**： 不涉及。 **取值范围**： 0~500000个字符。 **默认取值**： 不涉及。
        :type description: str
        :param category: **参数解释**： 工作项类型编码。编辑工作项时，此字段必填、值为当前工作项正确的工作项类型，但不会更新此字段。 **约束限制**： 不涉及。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug **默认取值**： 不涉及。
        :type category: str
        :param category_layer_id: **参数解释**： 工作项类型层级关系ID，此参数影响工作项的层级显示。通过[获取模型树配置信息](GetModelConfig.xml)获取，根据参数中的category在响应消息体中category_layer_config中找到对应的category_code，和category_code同级的id就是工作项类型层级关系ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type category_layer_id: str
        :param parent_id: **参数解释**： 父工作项ID。 **约束限制**： 创建子工作项时必填，其他场景非必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type parent_id: str
        :param status: **参数解释**： 工作项状态code。可通过[查询工作项状态](ListIssueStatues.xml)接口获取，响应消息体中的**code**字段的值就是工作项状态code。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type status: str
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param recipient: **参数解释**： 原始需求承接人。 **约束限制**： 当工作项类型为RR时字段必填，其他工作项类型无此字段。
        :type recipient: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        :param assigned_cc: **参数解释**： 工作项抄送人，支持多个抄送人。 **约束限制**： 同一工作项最多支持50个抄送人。
        :type assigned_cc: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        :param plan_end_date: **参数解释**： 工作项计划结束日期。 **约束限制**： 0~13个字符的数字字符串，可选负号前缀。 **取值范围**： 时间戳。 **默认取值**： 不涉及。
        :type plan_end_date: str
        :param workload: **参数解释**： 工作项计划工时。 **约束限制**： 不涉及。 **取值范围**： 0~999999999.9中的数字字符串。 **默认取值**： 不涉及。
        :type workload: str
        :param link: **参数解释**： 工作项关联项ID。 **约束限制**： 多个关联项用英文逗号分隔，同一工作项最多支持50个关联项。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type link: str
        :param labels: **参数解释**： 工作项标签。 **约束限制**： 不涉及。
        :type labels: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        :param custom_fields: **参数解释**： 工作项自定义字段映射。用户添加的系统字段也在此列。 **约束限制**： 不涉及。
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        :param ir2feature: **参数解释**： IR和SF的关联字段。 **约束限制**： IR可以填写该字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type ir2feature: str
        :param priority: **参数解释**： 工作项优先级。 **约束限制**： RR、SF、FE、IR、SR、AR、Task、Bug可以填写该字段。 **取值范围**： - 低：低优先级。 - 中：中优先级。 - 高：高优先级。 **默认取值**： 不涉及。
        :type priority: str
        :param related_network_security: **参数解释**： 是否涉及网络安全。 **约束限制**： 仅研发需求有此字段。 **取值范围**： - yes：涉及网络安全。 - no：不涉及网络安全。 **默认取值**： 不涉及。
        :type related_network_security: str
        :param collaboratives: **参数解释**： 研发需求协同信息，协同任务ID，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**collaboratives**字段的值就是研发需求协同信息，协同任务ID。 **约束限制**： 协同任务ID。IR、SR、AR、US有此字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type collaboratives: str
        :param business_domain: **参数解释**： 领域字段。 **约束限制**：  FE、SF、IR、SR、AR、Bug有此字段。 **取值范围**： - software - soft-hardware - hardware - 性能 - 功能 - 运维 - 运营 - 用户体验 - 隐私保护 - 合规 - 韧性(可靠性/可用性) - 韧性(危险检测与相应恢复) - 透明 - 无害 - 安全 - API - 成本 - 可维护性 - 其他DFX - 可用性 - others **默认取值**： 不涉及。
        :type business_domain: str
        :param plan_pi: **参数解释**： 工作项发布计划ID。 **约束限制**： 默认SR、AR、US、Task、Bug有此字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type plan_pi: str
        :param submitted_by: **参数解释**： 工作项提出人。 **约束限制**： 仅RR、Bug有此字段。
        :type submitted_by: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        :param ir2rr: **参数解释**： IR关联的RR的Id。 **约束限制**： 仅IR有此字段，多选时用英文逗号分隔。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type ir2rr: str
        :param feature_set: **参数解释**： 特性集ID。 **约束限制**： 仅SF/FE有此字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type feature_set: str
        :param security_level: **参数解释**： 密级。低密级权限者不能访问高密级的工作项。可以通过[[查询字段列表](ListIpdProjectFields.xml)]接口获取，响应消息体中密级的**option**字段的值就是密级字段的可选值。 **约束限制**： 仅在涉密环境（SM）下存在此字段，非涉密环境下无此字段。涉密环境下必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type security_level: str
        """
        
        

        self._title = None
        self._description = None
        self._category = None
        self._category_layer_id = None
        self._parent_id = None
        self._status = None
        self._assignee = None
        self._recipient = None
        self._assigned_cc = None
        self._plan_end_date = None
        self._workload = None
        self._link = None
        self._labels = None
        self._custom_fields = None
        self._ir2feature = None
        self._priority = None
        self._related_network_security = None
        self._collaboratives = None
        self._business_domain = None
        self._plan_pi = None
        self._submitted_by = None
        self._ir2rr = None
        self._feature_set = None
        self._security_level = None
        self.discriminator = None

        self.title = title
        self.description = description
        self.category = category
        self.category_layer_id = category_layer_id
        if parent_id is not None:
            self.parent_id = parent_id
        self.status = status
        self.assignee = assignee
        if recipient is not None:
            self.recipient = recipient
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
        if submitted_by is not None:
            self.submitted_by = submitted_by
        if ir2rr is not None:
            self.ir2rr = ir2rr
        if feature_set is not None:
            self.feature_set = feature_set
        if security_level is not None:
            self.security_level = security_level

    @property
    def title(self):
        r"""Gets the title of this IssueCreateEntity.

        **参数解释**： 工作项标题。 **约束限制**：  不涉及。 **取值范围**： 2~256个字符。 **默认取值**： 不涉及。

        :return: The title of this IssueCreateEntity.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this IssueCreateEntity.

        **参数解释**： 工作项标题。 **约束限制**：  不涉及。 **取值范围**： 2~256个字符。 **默认取值**： 不涉及。

        :param title: The title of this IssueCreateEntity.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this IssueCreateEntity.

        **参数解释**： 工作项描述字段。 **约束限制**： 不涉及。 **取值范围**： 0~500000个字符。 **默认取值**： 不涉及。

        :return: The description of this IssueCreateEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IssueCreateEntity.

        **参数解释**： 工作项描述字段。 **约束限制**： 不涉及。 **取值范围**： 0~500000个字符。 **默认取值**： 不涉及。

        :param description: The description of this IssueCreateEntity.
        :type description: str
        """
        self._description = description

    @property
    def category(self):
        r"""Gets the category of this IssueCreateEntity.

        **参数解释**： 工作项类型编码。编辑工作项时，此字段必填、值为当前工作项正确的工作项类型，但不会更新此字段。 **约束限制**： 不涉及。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug **默认取值**： 不涉及。

        :return: The category of this IssueCreateEntity.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this IssueCreateEntity.

        **参数解释**： 工作项类型编码。编辑工作项时，此字段必填、值为当前工作项正确的工作项类型，但不会更新此字段。 **约束限制**： 不涉及。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug **默认取值**： 不涉及。

        :param category: The category of this IssueCreateEntity.
        :type category: str
        """
        self._category = category

    @property
    def category_layer_id(self):
        r"""Gets the category_layer_id of this IssueCreateEntity.

        **参数解释**： 工作项类型层级关系ID，此参数影响工作项的层级显示。通过[获取模型树配置信息](GetModelConfig.xml)获取，根据参数中的category在响应消息体中category_layer_config中找到对应的category_code，和category_code同级的id就是工作项类型层级关系ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The category_layer_id of this IssueCreateEntity.
        :rtype: str
        """
        return self._category_layer_id

    @category_layer_id.setter
    def category_layer_id(self, category_layer_id):
        r"""Sets the category_layer_id of this IssueCreateEntity.

        **参数解释**： 工作项类型层级关系ID，此参数影响工作项的层级显示。通过[获取模型树配置信息](GetModelConfig.xml)获取，根据参数中的category在响应消息体中category_layer_config中找到对应的category_code，和category_code同级的id就是工作项类型层级关系ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param category_layer_id: The category_layer_id of this IssueCreateEntity.
        :type category_layer_id: str
        """
        self._category_layer_id = category_layer_id

    @property
    def parent_id(self):
        r"""Gets the parent_id of this IssueCreateEntity.

        **参数解释**： 父工作项ID。 **约束限制**： 创建子工作项时必填，其他场景非必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The parent_id of this IssueCreateEntity.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this IssueCreateEntity.

        **参数解释**： 父工作项ID。 **约束限制**： 创建子工作项时必填，其他场景非必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param parent_id: The parent_id of this IssueCreateEntity.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def status(self):
        r"""Gets the status of this IssueCreateEntity.

        **参数解释**： 工作项状态code。可通过[查询工作项状态](ListIssueStatues.xml)接口获取，响应消息体中的**code**字段的值就是工作项状态code。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The status of this IssueCreateEntity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this IssueCreateEntity.

        **参数解释**： 工作项状态code。可通过[查询工作项状态](ListIssueStatues.xml)接口获取，响应消息体中的**code**字段的值就是工作项状态code。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param status: The status of this IssueCreateEntity.
        :type status: str
        """
        self._status = status

    @property
    def assignee(self):
        r"""Gets the assignee of this IssueCreateEntity.

        :return: The assignee of this IssueCreateEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this IssueCreateEntity.

        :param assignee: The assignee of this IssueCreateEntity.
        :type assignee: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._assignee = assignee

    @property
    def recipient(self):
        r"""Gets the recipient of this IssueCreateEntity.

        **参数解释**： 原始需求承接人。 **约束限制**： 当工作项类型为RR时字段必填，其他工作项类型无此字段。

        :return: The recipient of this IssueCreateEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        r"""Sets the recipient of this IssueCreateEntity.

        **参数解释**： 原始需求承接人。 **约束限制**： 当工作项类型为RR时字段必填，其他工作项类型无此字段。

        :param recipient: The recipient of this IssueCreateEntity.
        :type recipient: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        self._recipient = recipient

    @property
    def assigned_cc(self):
        r"""Gets the assigned_cc of this IssueCreateEntity.

        **参数解释**： 工作项抄送人，支持多个抄送人。 **约束限制**： 同一工作项最多支持50个抄送人。

        :return: The assigned_cc of this IssueCreateEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        return self._assigned_cc

    @assigned_cc.setter
    def assigned_cc(self, assigned_cc):
        r"""Sets the assigned_cc of this IssueCreateEntity.

        **参数解释**： 工作项抄送人，支持多个抄送人。 **约束限制**： 同一工作项最多支持50个抄送人。

        :param assigned_cc: The assigned_cc of this IssueCreateEntity.
        :type assigned_cc: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        self._assigned_cc = assigned_cc

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this IssueCreateEntity.

        **参数解释**： 工作项计划结束日期。 **约束限制**： 0~13个字符的数字字符串，可选负号前缀。 **取值范围**： 时间戳。 **默认取值**： 不涉及。

        :return: The plan_end_date of this IssueCreateEntity.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this IssueCreateEntity.

        **参数解释**： 工作项计划结束日期。 **约束限制**： 0~13个字符的数字字符串，可选负号前缀。 **取值范围**： 时间戳。 **默认取值**： 不涉及。

        :param plan_end_date: The plan_end_date of this IssueCreateEntity.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def workload(self):
        r"""Gets the workload of this IssueCreateEntity.

        **参数解释**： 工作项计划工时。 **约束限制**： 不涉及。 **取值范围**： 0~999999999.9中的数字字符串。 **默认取值**： 不涉及。

        :return: The workload of this IssueCreateEntity.
        :rtype: str
        """
        return self._workload

    @workload.setter
    def workload(self, workload):
        r"""Sets the workload of this IssueCreateEntity.

        **参数解释**： 工作项计划工时。 **约束限制**： 不涉及。 **取值范围**： 0~999999999.9中的数字字符串。 **默认取值**： 不涉及。

        :param workload: The workload of this IssueCreateEntity.
        :type workload: str
        """
        self._workload = workload

    @property
    def link(self):
        r"""Gets the link of this IssueCreateEntity.

        **参数解释**： 工作项关联项ID。 **约束限制**： 多个关联项用英文逗号分隔，同一工作项最多支持50个关联项。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The link of this IssueCreateEntity.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this IssueCreateEntity.

        **参数解释**： 工作项关联项ID。 **约束限制**： 多个关联项用英文逗号分隔，同一工作项最多支持50个关联项。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param link: The link of this IssueCreateEntity.
        :type link: str
        """
        self._link = link

    @property
    def labels(self):
        r"""Gets the labels of this IssueCreateEntity.

        **参数解释**： 工作项标签。 **约束限制**： 不涉及。

        :return: The labels of this IssueCreateEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this IssueCreateEntity.

        **参数解释**： 工作项标签。 **约束限制**： 不涉及。

        :param labels: The labels of this IssueCreateEntity.
        :type labels: list[:class:`huaweicloudsdkprojectman.v4.LabelEntity`]
        """
        self._labels = labels

    @property
    def custom_fields(self):
        r"""Gets the custom_fields of this IssueCreateEntity.

        **参数解释**： 工作项自定义字段映射。用户添加的系统字段也在此列。 **约束限制**： 不涉及。

        :return: The custom_fields of this IssueCreateEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        r"""Sets the custom_fields of this IssueCreateEntity.

        **参数解释**： 工作项自定义字段映射。用户添加的系统字段也在此列。 **约束限制**： 不涉及。

        :param custom_fields: The custom_fields of this IssueCreateEntity.
        :type custom_fields: list[:class:`huaweicloudsdkprojectman.v4.FieldCodeValuePair`]
        """
        self._custom_fields = custom_fields

    @property
    def ir2feature(self):
        r"""Gets the ir2feature of this IssueCreateEntity.

        **参数解释**： IR和SF的关联字段。 **约束限制**： IR可以填写该字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The ir2feature of this IssueCreateEntity.
        :rtype: str
        """
        return self._ir2feature

    @ir2feature.setter
    def ir2feature(self, ir2feature):
        r"""Sets the ir2feature of this IssueCreateEntity.

        **参数解释**： IR和SF的关联字段。 **约束限制**： IR可以填写该字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param ir2feature: The ir2feature of this IssueCreateEntity.
        :type ir2feature: str
        """
        self._ir2feature = ir2feature

    @property
    def priority(self):
        r"""Gets the priority of this IssueCreateEntity.

        **参数解释**： 工作项优先级。 **约束限制**： RR、SF、FE、IR、SR、AR、Task、Bug可以填写该字段。 **取值范围**： - 低：低优先级。 - 中：中优先级。 - 高：高优先级。 **默认取值**： 不涉及。

        :return: The priority of this IssueCreateEntity.
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this IssueCreateEntity.

        **参数解释**： 工作项优先级。 **约束限制**： RR、SF、FE、IR、SR、AR、Task、Bug可以填写该字段。 **取值范围**： - 低：低优先级。 - 中：中优先级。 - 高：高优先级。 **默认取值**： 不涉及。

        :param priority: The priority of this IssueCreateEntity.
        :type priority: str
        """
        self._priority = priority

    @property
    def related_network_security(self):
        r"""Gets the related_network_security of this IssueCreateEntity.

        **参数解释**： 是否涉及网络安全。 **约束限制**： 仅研发需求有此字段。 **取值范围**： - yes：涉及网络安全。 - no：不涉及网络安全。 **默认取值**： 不涉及。

        :return: The related_network_security of this IssueCreateEntity.
        :rtype: str
        """
        return self._related_network_security

    @related_network_security.setter
    def related_network_security(self, related_network_security):
        r"""Sets the related_network_security of this IssueCreateEntity.

        **参数解释**： 是否涉及网络安全。 **约束限制**： 仅研发需求有此字段。 **取值范围**： - yes：涉及网络安全。 - no：不涉及网络安全。 **默认取值**： 不涉及。

        :param related_network_security: The related_network_security of this IssueCreateEntity.
        :type related_network_security: str
        """
        self._related_network_security = related_network_security

    @property
    def collaboratives(self):
        r"""Gets the collaboratives of this IssueCreateEntity.

        **参数解释**： 研发需求协同信息，协同任务ID，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**collaboratives**字段的值就是研发需求协同信息，协同任务ID。 **约束限制**： 协同任务ID。IR、SR、AR、US有此字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The collaboratives of this IssueCreateEntity.
        :rtype: str
        """
        return self._collaboratives

    @collaboratives.setter
    def collaboratives(self, collaboratives):
        r"""Sets the collaboratives of this IssueCreateEntity.

        **参数解释**： 研发需求协同信息，协同任务ID，可通过[查询树状工作项](ShowIpdIssueTree.xml)接口获取，响应消息体中的**collaboratives**字段的值就是研发需求协同信息，协同任务ID。 **约束限制**： 协同任务ID。IR、SR、AR、US有此字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param collaboratives: The collaboratives of this IssueCreateEntity.
        :type collaboratives: str
        """
        self._collaboratives = collaboratives

    @property
    def business_domain(self):
        r"""Gets the business_domain of this IssueCreateEntity.

        **参数解释**： 领域字段。 **约束限制**：  FE、SF、IR、SR、AR、Bug有此字段。 **取值范围**： - software - soft-hardware - hardware - 性能 - 功能 - 运维 - 运营 - 用户体验 - 隐私保护 - 合规 - 韧性(可靠性/可用性) - 韧性(危险检测与相应恢复) - 透明 - 无害 - 安全 - API - 成本 - 可维护性 - 其他DFX - 可用性 - others **默认取值**： 不涉及。

        :return: The business_domain of this IssueCreateEntity.
        :rtype: str
        """
        return self._business_domain

    @business_domain.setter
    def business_domain(self, business_domain):
        r"""Sets the business_domain of this IssueCreateEntity.

        **参数解释**： 领域字段。 **约束限制**：  FE、SF、IR、SR、AR、Bug有此字段。 **取值范围**： - software - soft-hardware - hardware - 性能 - 功能 - 运维 - 运营 - 用户体验 - 隐私保护 - 合规 - 韧性(可靠性/可用性) - 韧性(危险检测与相应恢复) - 透明 - 无害 - 安全 - API - 成本 - 可维护性 - 其他DFX - 可用性 - others **默认取值**： 不涉及。

        :param business_domain: The business_domain of this IssueCreateEntity.
        :type business_domain: str
        """
        self._business_domain = business_domain

    @property
    def plan_pi(self):
        r"""Gets the plan_pi of this IssueCreateEntity.

        **参数解释**： 工作项发布计划ID。 **约束限制**： 默认SR、AR、US、Task、Bug有此字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The plan_pi of this IssueCreateEntity.
        :rtype: str
        """
        return self._plan_pi

    @plan_pi.setter
    def plan_pi(self, plan_pi):
        r"""Sets the plan_pi of this IssueCreateEntity.

        **参数解释**： 工作项发布计划ID。 **约束限制**： 默认SR、AR、US、Task、Bug有此字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param plan_pi: The plan_pi of this IssueCreateEntity.
        :type plan_pi: str
        """
        self._plan_pi = plan_pi

    @property
    def submitted_by(self):
        r"""Gets the submitted_by of this IssueCreateEntity.

        **参数解释**： 工作项提出人。 **约束限制**： 仅RR、Bug有此字段。

        :return: The submitted_by of this IssueCreateEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        return self._submitted_by

    @submitted_by.setter
    def submitted_by(self, submitted_by):
        r"""Sets the submitted_by of this IssueCreateEntity.

        **参数解释**： 工作项提出人。 **约束限制**： 仅RR、Bug有此字段。

        :param submitted_by: The submitted_by of this IssueCreateEntity.
        :type submitted_by: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        self._submitted_by = submitted_by

    @property
    def ir2rr(self):
        r"""Gets the ir2rr of this IssueCreateEntity.

        **参数解释**： IR关联的RR的Id。 **约束限制**： 仅IR有此字段，多选时用英文逗号分隔。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The ir2rr of this IssueCreateEntity.
        :rtype: str
        """
        return self._ir2rr

    @ir2rr.setter
    def ir2rr(self, ir2rr):
        r"""Sets the ir2rr of this IssueCreateEntity.

        **参数解释**： IR关联的RR的Id。 **约束限制**： 仅IR有此字段，多选时用英文逗号分隔。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param ir2rr: The ir2rr of this IssueCreateEntity.
        :type ir2rr: str
        """
        self._ir2rr = ir2rr

    @property
    def feature_set(self):
        r"""Gets the feature_set of this IssueCreateEntity.

        **参数解释**： 特性集ID。 **约束限制**： 仅SF/FE有此字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The feature_set of this IssueCreateEntity.
        :rtype: str
        """
        return self._feature_set

    @feature_set.setter
    def feature_set(self, feature_set):
        r"""Sets the feature_set of this IssueCreateEntity.

        **参数解释**： 特性集ID。 **约束限制**： 仅SF/FE有此字段。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param feature_set: The feature_set of this IssueCreateEntity.
        :type feature_set: str
        """
        self._feature_set = feature_set

    @property
    def security_level(self):
        r"""Gets the security_level of this IssueCreateEntity.

        **参数解释**： 密级。低密级权限者不能访问高密级的工作项。可以通过[[查询字段列表](ListIpdProjectFields.xml)]接口获取，响应消息体中密级的**option**字段的值就是密级字段的可选值。 **约束限制**： 仅在涉密环境（SM）下存在此字段，非涉密环境下无此字段。涉密环境下必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The security_level of this IssueCreateEntity.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this IssueCreateEntity.

        **参数解释**： 密级。低密级权限者不能访问高密级的工作项。可以通过[[查询字段列表](ListIpdProjectFields.xml)]接口获取，响应消息体中密级的**option**字段的值就是密级字段的可选值。 **约束限制**： 仅在涉密环境（SM）下存在此字段，非涉密环境下无此字段。涉密环境下必填。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param security_level: The security_level of this IssueCreateEntity.
        :type security_level: str
        """
        self._security_level = security_level

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
        if not isinstance(other, IssueCreateEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
