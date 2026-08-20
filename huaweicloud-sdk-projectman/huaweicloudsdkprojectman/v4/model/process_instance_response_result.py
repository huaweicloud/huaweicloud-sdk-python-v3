# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProcessInstanceResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cc': 'str',
        'approver': 'str',
        'description': 'str',
        'closed_time': 'str',
        'reviewer': 'str',
        'type': 'str',
        'title': 'str',
        'modified_date': 'str',
        'created_by': 'ProcessInstanceResponseResultCreatedBy',
        'domain_id': 'str',
        'number': 'str',
        'need_approval': 'bool',
        'br2co': 'str',
        'modified_by': 'ProcessInstanceResponseResultModifiedBy',
        'approval_time': 'str',
        'plan_end_date': 'str',
        'id': 'str',
        'state': 'str',
        'created_date': 'str',
        'category': 'str',
        'plan_start_date': 'str',
        'review_config': 'ProcessInstanceResponseResultReviewConfig',
        'status': 'ProcessInstanceResponseResultStatus',
        'stage': 'str',
        'opinions': 'list[ProcessInstanceResponseResultOpinions]',
        'opinion_comments': 'list[str]',
        'attachments': 'list[str]',
        'wikis': 'list[str]',
        'associatedocuments': 'list[str]',
        'cos': 'list[ProcessInstanceResponseResultCos]',
        'approval_phase_result': 'str',
        'ccbs': 'list[ProcessInstanceResponseResultCcbs]'
    }

    attribute_map = {
        'cc': 'cc',
        'approver': 'approver',
        'description': 'description',
        'closed_time': 'closed_time',
        'reviewer': 'reviewer',
        'type': 'type',
        'title': 'title',
        'modified_date': 'modified_date',
        'created_by': 'created_by',
        'domain_id': 'domain_id',
        'number': 'number',
        'need_approval': 'need_approval',
        'br2co': 'br2co',
        'modified_by': 'modified_by',
        'approval_time': 'approval_time',
        'plan_end_date': 'plan_end_date',
        'id': 'id',
        'state': 'state',
        'created_date': 'created_date',
        'category': 'category',
        'plan_start_date': 'plan_start_date',
        'review_config': 'review_config',
        'status': 'status',
        'stage': 'stage',
        'opinions': 'opinions',
        'opinion_comments': 'opinion_comments',
        'attachments': 'attachments',
        'wikis': 'wikis',
        'associatedocuments': 'associatedocuments',
        'cos': 'cos',
        'approval_phase_result': 'approval_phase_result',
        'ccbs': 'ccbs'
    }

    def __init__(self, cc=None, approver=None, description=None, closed_time=None, reviewer=None, type=None, title=None, modified_date=None, created_by=None, domain_id=None, number=None, need_approval=None, br2co=None, modified_by=None, approval_time=None, plan_end_date=None, id=None, state=None, created_date=None, category=None, plan_start_date=None, review_config=None, status=None, stage=None, opinions=None, opinion_comments=None, attachments=None, wikis=None, associatedocuments=None, cos=None, approval_phase_result=None, ccbs=None):
        r"""ProcessInstanceResponseResult

        The model defined in huaweicloud sdk

        :param cc: 抄送人列表
        :type cc: str
        :param approver: 决策人ID
        :type approver: str
        :param description: 评审单描述，列表接口不返回描述信息
        :type description: str
        :param closed_time: 评审单完成时间
        :type closed_time: str
        :param reviewer: 评审专家ID，逗号分隔
        :type reviewer: str
        :param type: 类型
        :type type: str
        :param title: 评审单标题
        :type title: str
        :param modified_date: 评审单最后修改时间戳
        :type modified_date: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultCreatedBy`
        :param domain_id: 租户id
        :type domain_id: str
        :param number: 评审单编号
        :type number: str
        :param need_approval: 是否需要审批
        :type need_approval: bool
        :param br2co: 基线评审对象
        :type br2co: str
        :param modified_by: 
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultModifiedBy`
        :param approval_time: 评审时间
        :type approval_time: str
        :param plan_end_date: 计划完成时间
        :type plan_end_date: str
        :param id: 评审单ID
        :type id: str
        :param state: 评审单工作状态，取值为\&quot;正在工作\&quot;,\&quot;作废\&quot;
        :type state: str
        :param created_date: 创建时间
        :type created_date: str
        :param category: 类别
        :type category: str
        :param plan_start_date: 计划开始时间
        :type plan_start_date: str
        :param review_config: 
        :type review_config: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultReviewConfig`
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultStatus`
        :param stage: 阶段
        :type stage: str
        :param opinions: 变更对象评审专家Id列表（创建变更评审时使用）
        :type opinions: list[:class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultOpinions`]
        :param opinion_comments: 评审意见
        :type opinion_comments: list[str]
        :param attachments: 附件
        :type attachments: list[str]
        :param wikis: 关联wiki
        :type wikis: list[str]
        :param associatedocuments: 关联文档
        :type associatedocuments: list[str]
        :param cos: 评审对象列表
        :type cos: list[:class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultCos`]
        :param approval_phase_result: 评审结果
        :type approval_phase_result: str
        :param ccbs: 审批信息列表
        :type ccbs: list[:class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultCcbs`]
        """
        
        

        self._cc = None
        self._approver = None
        self._description = None
        self._closed_time = None
        self._reviewer = None
        self._type = None
        self._title = None
        self._modified_date = None
        self._created_by = None
        self._domain_id = None
        self._number = None
        self._need_approval = None
        self._br2co = None
        self._modified_by = None
        self._approval_time = None
        self._plan_end_date = None
        self._id = None
        self._state = None
        self._created_date = None
        self._category = None
        self._plan_start_date = None
        self._review_config = None
        self._status = None
        self._stage = None
        self._opinions = None
        self._opinion_comments = None
        self._attachments = None
        self._wikis = None
        self._associatedocuments = None
        self._cos = None
        self._approval_phase_result = None
        self._ccbs = None
        self.discriminator = None

        if cc is not None:
            self.cc = cc
        if approver is not None:
            self.approver = approver
        if description is not None:
            self.description = description
        if closed_time is not None:
            self.closed_time = closed_time
        if reviewer is not None:
            self.reviewer = reviewer
        if type is not None:
            self.type = type
        if title is not None:
            self.title = title
        if modified_date is not None:
            self.modified_date = modified_date
        if created_by is not None:
            self.created_by = created_by
        if domain_id is not None:
            self.domain_id = domain_id
        if number is not None:
            self.number = number
        if need_approval is not None:
            self.need_approval = need_approval
        if br2co is not None:
            self.br2co = br2co
        if modified_by is not None:
            self.modified_by = modified_by
        if approval_time is not None:
            self.approval_time = approval_time
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if created_date is not None:
            self.created_date = created_date
        if category is not None:
            self.category = category
        if plan_start_date is not None:
            self.plan_start_date = plan_start_date
        if review_config is not None:
            self.review_config = review_config
        if status is not None:
            self.status = status
        if stage is not None:
            self.stage = stage
        if opinions is not None:
            self.opinions = opinions
        if opinion_comments is not None:
            self.opinion_comments = opinion_comments
        if attachments is not None:
            self.attachments = attachments
        if wikis is not None:
            self.wikis = wikis
        if associatedocuments is not None:
            self.associatedocuments = associatedocuments
        if cos is not None:
            self.cos = cos
        if approval_phase_result is not None:
            self.approval_phase_result = approval_phase_result
        if ccbs is not None:
            self.ccbs = ccbs

    @property
    def cc(self):
        r"""Gets the cc of this ProcessInstanceResponseResult.

        抄送人列表

        :return: The cc of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        r"""Sets the cc of this ProcessInstanceResponseResult.

        抄送人列表

        :param cc: The cc of this ProcessInstanceResponseResult.
        :type cc: str
        """
        self._cc = cc

    @property
    def approver(self):
        r"""Gets the approver of this ProcessInstanceResponseResult.

        决策人ID

        :return: The approver of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        r"""Sets the approver of this ProcessInstanceResponseResult.

        决策人ID

        :param approver: The approver of this ProcessInstanceResponseResult.
        :type approver: str
        """
        self._approver = approver

    @property
    def description(self):
        r"""Gets the description of this ProcessInstanceResponseResult.

        评审单描述，列表接口不返回描述信息

        :return: The description of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ProcessInstanceResponseResult.

        评审单描述，列表接口不返回描述信息

        :param description: The description of this ProcessInstanceResponseResult.
        :type description: str
        """
        self._description = description

    @property
    def closed_time(self):
        r"""Gets the closed_time of this ProcessInstanceResponseResult.

        评审单完成时间

        :return: The closed_time of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._closed_time

    @closed_time.setter
    def closed_time(self, closed_time):
        r"""Sets the closed_time of this ProcessInstanceResponseResult.

        评审单完成时间

        :param closed_time: The closed_time of this ProcessInstanceResponseResult.
        :type closed_time: str
        """
        self._closed_time = closed_time

    @property
    def reviewer(self):
        r"""Gets the reviewer of this ProcessInstanceResponseResult.

        评审专家ID，逗号分隔

        :return: The reviewer of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        r"""Sets the reviewer of this ProcessInstanceResponseResult.

        评审专家ID，逗号分隔

        :param reviewer: The reviewer of this ProcessInstanceResponseResult.
        :type reviewer: str
        """
        self._reviewer = reviewer

    @property
    def type(self):
        r"""Gets the type of this ProcessInstanceResponseResult.

        类型

        :return: The type of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ProcessInstanceResponseResult.

        类型

        :param type: The type of this ProcessInstanceResponseResult.
        :type type: str
        """
        self._type = type

    @property
    def title(self):
        r"""Gets the title of this ProcessInstanceResponseResult.

        评审单标题

        :return: The title of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ProcessInstanceResponseResult.

        评审单标题

        :param title: The title of this ProcessInstanceResponseResult.
        :type title: str
        """
        self._title = title

    @property
    def modified_date(self):
        r"""Gets the modified_date of this ProcessInstanceResponseResult.

        评审单最后修改时间戳

        :return: The modified_date of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this ProcessInstanceResponseResult.

        评审单最后修改时间戳

        :param modified_date: The modified_date of this ProcessInstanceResponseResult.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def created_by(self):
        r"""Gets the created_by of this ProcessInstanceResponseResult.

        :return: The created_by of this ProcessInstanceResponseResult.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultCreatedBy`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ProcessInstanceResponseResult.

        :param created_by: The created_by of this ProcessInstanceResponseResult.
        :type created_by: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultCreatedBy`
        """
        self._created_by = created_by

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ProcessInstanceResponseResult.

        租户id

        :return: The domain_id of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ProcessInstanceResponseResult.

        租户id

        :param domain_id: The domain_id of this ProcessInstanceResponseResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def number(self):
        r"""Gets the number of this ProcessInstanceResponseResult.

        评审单编号

        :return: The number of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ProcessInstanceResponseResult.

        评审单编号

        :param number: The number of this ProcessInstanceResponseResult.
        :type number: str
        """
        self._number = number

    @property
    def need_approval(self):
        r"""Gets the need_approval of this ProcessInstanceResponseResult.

        是否需要审批

        :return: The need_approval of this ProcessInstanceResponseResult.
        :rtype: bool
        """
        return self._need_approval

    @need_approval.setter
    def need_approval(self, need_approval):
        r"""Sets the need_approval of this ProcessInstanceResponseResult.

        是否需要审批

        :param need_approval: The need_approval of this ProcessInstanceResponseResult.
        :type need_approval: bool
        """
        self._need_approval = need_approval

    @property
    def br2co(self):
        r"""Gets the br2co of this ProcessInstanceResponseResult.

        基线评审对象

        :return: The br2co of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._br2co

    @br2co.setter
    def br2co(self, br2co):
        r"""Sets the br2co of this ProcessInstanceResponseResult.

        基线评审对象

        :param br2co: The br2co of this ProcessInstanceResponseResult.
        :type br2co: str
        """
        self._br2co = br2co

    @property
    def modified_by(self):
        r"""Gets the modified_by of this ProcessInstanceResponseResult.

        :return: The modified_by of this ProcessInstanceResponseResult.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultModifiedBy`
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this ProcessInstanceResponseResult.

        :param modified_by: The modified_by of this ProcessInstanceResponseResult.
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultModifiedBy`
        """
        self._modified_by = modified_by

    @property
    def approval_time(self):
        r"""Gets the approval_time of this ProcessInstanceResponseResult.

        评审时间

        :return: The approval_time of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._approval_time

    @approval_time.setter
    def approval_time(self, approval_time):
        r"""Sets the approval_time of this ProcessInstanceResponseResult.

        评审时间

        :param approval_time: The approval_time of this ProcessInstanceResponseResult.
        :type approval_time: str
        """
        self._approval_time = approval_time

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this ProcessInstanceResponseResult.

        计划完成时间

        :return: The plan_end_date of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this ProcessInstanceResponseResult.

        计划完成时间

        :param plan_end_date: The plan_end_date of this ProcessInstanceResponseResult.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def id(self):
        r"""Gets the id of this ProcessInstanceResponseResult.

        评审单ID

        :return: The id of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProcessInstanceResponseResult.

        评审单ID

        :param id: The id of this ProcessInstanceResponseResult.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        r"""Gets the state of this ProcessInstanceResponseResult.

        评审单工作状态，取值为\"正在工作\",\"作废\"

        :return: The state of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ProcessInstanceResponseResult.

        评审单工作状态，取值为\"正在工作\",\"作废\"

        :param state: The state of this ProcessInstanceResponseResult.
        :type state: str
        """
        self._state = state

    @property
    def created_date(self):
        r"""Gets the created_date of this ProcessInstanceResponseResult.

        创建时间

        :return: The created_date of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this ProcessInstanceResponseResult.

        创建时间

        :param created_date: The created_date of this ProcessInstanceResponseResult.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def category(self):
        r"""Gets the category of this ProcessInstanceResponseResult.

        类别

        :return: The category of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ProcessInstanceResponseResult.

        类别

        :param category: The category of this ProcessInstanceResponseResult.
        :type category: str
        """
        self._category = category

    @property
    def plan_start_date(self):
        r"""Gets the plan_start_date of this ProcessInstanceResponseResult.

        计划开始时间

        :return: The plan_start_date of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        r"""Sets the plan_start_date of this ProcessInstanceResponseResult.

        计划开始时间

        :param plan_start_date: The plan_start_date of this ProcessInstanceResponseResult.
        :type plan_start_date: str
        """
        self._plan_start_date = plan_start_date

    @property
    def review_config(self):
        r"""Gets the review_config of this ProcessInstanceResponseResult.

        :return: The review_config of this ProcessInstanceResponseResult.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultReviewConfig`
        """
        return self._review_config

    @review_config.setter
    def review_config(self, review_config):
        r"""Sets the review_config of this ProcessInstanceResponseResult.

        :param review_config: The review_config of this ProcessInstanceResponseResult.
        :type review_config: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultReviewConfig`
        """
        self._review_config = review_config

    @property
    def status(self):
        r"""Gets the status of this ProcessInstanceResponseResult.

        :return: The status of this ProcessInstanceResponseResult.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ProcessInstanceResponseResult.

        :param status: The status of this ProcessInstanceResponseResult.
        :type status: :class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultStatus`
        """
        self._status = status

    @property
    def stage(self):
        r"""Gets the stage of this ProcessInstanceResponseResult.

        阶段

        :return: The stage of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._stage

    @stage.setter
    def stage(self, stage):
        r"""Sets the stage of this ProcessInstanceResponseResult.

        阶段

        :param stage: The stage of this ProcessInstanceResponseResult.
        :type stage: str
        """
        self._stage = stage

    @property
    def opinions(self):
        r"""Gets the opinions of this ProcessInstanceResponseResult.

        变更对象评审专家Id列表（创建变更评审时使用）

        :return: The opinions of this ProcessInstanceResponseResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultOpinions`]
        """
        return self._opinions

    @opinions.setter
    def opinions(self, opinions):
        r"""Sets the opinions of this ProcessInstanceResponseResult.

        变更对象评审专家Id列表（创建变更评审时使用）

        :param opinions: The opinions of this ProcessInstanceResponseResult.
        :type opinions: list[:class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultOpinions`]
        """
        self._opinions = opinions

    @property
    def opinion_comments(self):
        r"""Gets the opinion_comments of this ProcessInstanceResponseResult.

        评审意见

        :return: The opinion_comments of this ProcessInstanceResponseResult.
        :rtype: list[str]
        """
        return self._opinion_comments

    @opinion_comments.setter
    def opinion_comments(self, opinion_comments):
        r"""Sets the opinion_comments of this ProcessInstanceResponseResult.

        评审意见

        :param opinion_comments: The opinion_comments of this ProcessInstanceResponseResult.
        :type opinion_comments: list[str]
        """
        self._opinion_comments = opinion_comments

    @property
    def attachments(self):
        r"""Gets the attachments of this ProcessInstanceResponseResult.

        附件

        :return: The attachments of this ProcessInstanceResponseResult.
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        r"""Sets the attachments of this ProcessInstanceResponseResult.

        附件

        :param attachments: The attachments of this ProcessInstanceResponseResult.
        :type attachments: list[str]
        """
        self._attachments = attachments

    @property
    def wikis(self):
        r"""Gets the wikis of this ProcessInstanceResponseResult.

        关联wiki

        :return: The wikis of this ProcessInstanceResponseResult.
        :rtype: list[str]
        """
        return self._wikis

    @wikis.setter
    def wikis(self, wikis):
        r"""Sets the wikis of this ProcessInstanceResponseResult.

        关联wiki

        :param wikis: The wikis of this ProcessInstanceResponseResult.
        :type wikis: list[str]
        """
        self._wikis = wikis

    @property
    def associatedocuments(self):
        r"""Gets the associatedocuments of this ProcessInstanceResponseResult.

        关联文档

        :return: The associatedocuments of this ProcessInstanceResponseResult.
        :rtype: list[str]
        """
        return self._associatedocuments

    @associatedocuments.setter
    def associatedocuments(self, associatedocuments):
        r"""Sets the associatedocuments of this ProcessInstanceResponseResult.

        关联文档

        :param associatedocuments: The associatedocuments of this ProcessInstanceResponseResult.
        :type associatedocuments: list[str]
        """
        self._associatedocuments = associatedocuments

    @property
    def cos(self):
        r"""Gets the cos of this ProcessInstanceResponseResult.

        评审对象列表

        :return: The cos of this ProcessInstanceResponseResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultCos`]
        """
        return self._cos

    @cos.setter
    def cos(self, cos):
        r"""Sets the cos of this ProcessInstanceResponseResult.

        评审对象列表

        :param cos: The cos of this ProcessInstanceResponseResult.
        :type cos: list[:class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultCos`]
        """
        self._cos = cos

    @property
    def approval_phase_result(self):
        r"""Gets the approval_phase_result of this ProcessInstanceResponseResult.

        评审结果

        :return: The approval_phase_result of this ProcessInstanceResponseResult.
        :rtype: str
        """
        return self._approval_phase_result

    @approval_phase_result.setter
    def approval_phase_result(self, approval_phase_result):
        r"""Sets the approval_phase_result of this ProcessInstanceResponseResult.

        评审结果

        :param approval_phase_result: The approval_phase_result of this ProcessInstanceResponseResult.
        :type approval_phase_result: str
        """
        self._approval_phase_result = approval_phase_result

    @property
    def ccbs(self):
        r"""Gets the ccbs of this ProcessInstanceResponseResult.

        审批信息列表

        :return: The ccbs of this ProcessInstanceResponseResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultCcbs`]
        """
        return self._ccbs

    @ccbs.setter
    def ccbs(self, ccbs):
        r"""Sets the ccbs of this ProcessInstanceResponseResult.

        审批信息列表

        :param ccbs: The ccbs of this ProcessInstanceResponseResult.
        :type ccbs: list[:class:`huaweicloudsdkprojectman.v4.ProcessInstanceResponseResultCcbs`]
        """
        self._ccbs = ccbs

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
        if not isinstance(other, ProcessInstanceResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
