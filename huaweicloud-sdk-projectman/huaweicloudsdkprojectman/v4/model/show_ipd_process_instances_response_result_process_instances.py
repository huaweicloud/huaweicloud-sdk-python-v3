# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpdProcessInstancesResponseResultProcessInstances:

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
        'closed_time': 'str',
        'reviewer': 'str',
        'type': 'str',
        'title': 'str',
        'modified_date': 'str',
        'created_by': 'UserVO',
        'domain_id': 'str',
        'number': 'str',
        'need_approval': 'str',
        'modified_by': 'UserVO',
        'approval_time': 'str',
        'plan_end_date': 'str',
        'id': 'str',
        'state': 'str',
        'created_date': 'str',
        'category': 'str',
        'plan_start_date': 'str',
        'status': 'ShowIpdProcessInstancesResponseResultStatus',
        'ccbs': 'list[UserObject]',
        'opinions': 'list[ShowIpdProcessInstancesResponseResultOpinions]'
    }

    attribute_map = {
        'cc': 'cc',
        'approver': 'approver',
        'closed_time': 'closed_time',
        'reviewer': 'reviewer',
        'type': 'type',
        'title': 'title',
        'modified_date': 'modified_date',
        'created_by': 'created_by',
        'domain_id': 'domain_id',
        'number': 'number',
        'need_approval': 'need_approval',
        'modified_by': 'modified_by',
        'approval_time': 'approval_time',
        'plan_end_date': 'plan_end_date',
        'id': 'id',
        'state': 'state',
        'created_date': 'created_date',
        'category': 'category',
        'plan_start_date': 'plan_start_date',
        'status': 'status',
        'ccbs': 'ccbs',
        'opinions': 'opinions'
    }

    def __init__(self, cc=None, approver=None, closed_time=None, reviewer=None, type=None, title=None, modified_date=None, created_by=None, domain_id=None, number=None, need_approval=None, modified_by=None, approval_time=None, plan_end_date=None, id=None, state=None, created_date=None, category=None, plan_start_date=None, status=None, ccbs=None, opinions=None):
        r"""ShowIpdProcessInstancesResponseResultProcessInstances

        The model defined in huaweicloud sdk

        :param cc: 抄送人，多值使用英文逗号分隔。
        :type cc: str
        :param approver: 评审单决策人。
        :type approver: str
        :param closed_time: 评审单完成时间。
        :type closed_time: str
        :param reviewer: 评审专家。
        :type reviewer: str
        :param type: 评审分类。
        :type type: str
        :param title: 标题。
        :type title: str
        :param modified_date: 修改时间。
        :type modified_date: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param domain_id: 项目空间ID。
        :type domain_id: str
        :param number: 评审编号。
        :type number: str
        :param need_approval: 是否需要决策人审批。
        :type need_approval: str
        :param modified_by: 
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        :param approval_time: 审批时间。
        :type approval_time: str
        :param plan_end_date: 计划结束时间。
        :type plan_end_date: str
        :param id: 评审单ID。
        :type id: str
        :param state: 评审单数据状态。
        :type state: str
        :param created_date: 创建时间。
        :type created_date: str
        :param category: 评审单类型。
        :type category: str
        :param plan_start_date: 计划开始时间。
        :type plan_start_date: str
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.ShowIpdProcessInstancesResponseResultStatus`
        :param ccbs: 决策人对象列表。
        :type ccbs: list[:class:`huaweicloudsdkprojectman.v4.UserObject`]
        :param opinions: opinion对象列表。
        :type opinions: list[:class:`huaweicloudsdkprojectman.v4.ShowIpdProcessInstancesResponseResultOpinions`]
        """
        
        

        self._cc = None
        self._approver = None
        self._closed_time = None
        self._reviewer = None
        self._type = None
        self._title = None
        self._modified_date = None
        self._created_by = None
        self._domain_id = None
        self._number = None
        self._need_approval = None
        self._modified_by = None
        self._approval_time = None
        self._plan_end_date = None
        self._id = None
        self._state = None
        self._created_date = None
        self._category = None
        self._plan_start_date = None
        self._status = None
        self._ccbs = None
        self._opinions = None
        self.discriminator = None

        if cc is not None:
            self.cc = cc
        if approver is not None:
            self.approver = approver
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
        if status is not None:
            self.status = status
        if ccbs is not None:
            self.ccbs = ccbs
        if opinions is not None:
            self.opinions = opinions

    @property
    def cc(self):
        r"""Gets the cc of this ShowIpdProcessInstancesResponseResultProcessInstances.

        抄送人，多值使用英文逗号分隔。

        :return: The cc of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        r"""Sets the cc of this ShowIpdProcessInstancesResponseResultProcessInstances.

        抄送人，多值使用英文逗号分隔。

        :param cc: The cc of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type cc: str
        """
        self._cc = cc

    @property
    def approver(self):
        r"""Gets the approver of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审单决策人。

        :return: The approver of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        r"""Sets the approver of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审单决策人。

        :param approver: The approver of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type approver: str
        """
        self._approver = approver

    @property
    def closed_time(self):
        r"""Gets the closed_time of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审单完成时间。

        :return: The closed_time of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._closed_time

    @closed_time.setter
    def closed_time(self, closed_time):
        r"""Sets the closed_time of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审单完成时间。

        :param closed_time: The closed_time of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type closed_time: str
        """
        self._closed_time = closed_time

    @property
    def reviewer(self):
        r"""Gets the reviewer of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审专家。

        :return: The reviewer of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        r"""Sets the reviewer of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审专家。

        :param reviewer: The reviewer of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type reviewer: str
        """
        self._reviewer = reviewer

    @property
    def type(self):
        r"""Gets the type of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审分类。

        :return: The type of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审分类。

        :param type: The type of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type type: str
        """
        self._type = type

    @property
    def title(self):
        r"""Gets the title of this ShowIpdProcessInstancesResponseResultProcessInstances.

        标题。

        :return: The title of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowIpdProcessInstancesResponseResultProcessInstances.

        标题。

        :param title: The title of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type title: str
        """
        self._title = title

    @property
    def modified_date(self):
        r"""Gets the modified_date of this ShowIpdProcessInstancesResponseResultProcessInstances.

        修改时间。

        :return: The modified_date of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this ShowIpdProcessInstancesResponseResultProcessInstances.

        修改时间。

        :param modified_date: The modified_date of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def created_by(self):
        r"""Gets the created_by of this ShowIpdProcessInstancesResponseResultProcessInstances.

        :return: The created_by of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ShowIpdProcessInstancesResponseResultProcessInstances.

        :param created_by: The created_by of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._created_by = created_by

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowIpdProcessInstancesResponseResultProcessInstances.

        项目空间ID。

        :return: The domain_id of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowIpdProcessInstancesResponseResultProcessInstances.

        项目空间ID。

        :param domain_id: The domain_id of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def number(self):
        r"""Gets the number of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审编号。

        :return: The number of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审编号。

        :param number: The number of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type number: str
        """
        self._number = number

    @property
    def need_approval(self):
        r"""Gets the need_approval of this ShowIpdProcessInstancesResponseResultProcessInstances.

        是否需要决策人审批。

        :return: The need_approval of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._need_approval

    @need_approval.setter
    def need_approval(self, need_approval):
        r"""Sets the need_approval of this ShowIpdProcessInstancesResponseResultProcessInstances.

        是否需要决策人审批。

        :param need_approval: The need_approval of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type need_approval: str
        """
        self._need_approval = need_approval

    @property
    def modified_by(self):
        r"""Gets the modified_by of this ShowIpdProcessInstancesResponseResultProcessInstances.

        :return: The modified_by of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this ShowIpdProcessInstancesResponseResultProcessInstances.

        :param modified_by: The modified_by of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserVO`
        """
        self._modified_by = modified_by

    @property
    def approval_time(self):
        r"""Gets the approval_time of this ShowIpdProcessInstancesResponseResultProcessInstances.

        审批时间。

        :return: The approval_time of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._approval_time

    @approval_time.setter
    def approval_time(self, approval_time):
        r"""Sets the approval_time of this ShowIpdProcessInstancesResponseResultProcessInstances.

        审批时间。

        :param approval_time: The approval_time of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type approval_time: str
        """
        self._approval_time = approval_time

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this ShowIpdProcessInstancesResponseResultProcessInstances.

        计划结束时间。

        :return: The plan_end_date of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this ShowIpdProcessInstancesResponseResultProcessInstances.

        计划结束时间。

        :param plan_end_date: The plan_end_date of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def id(self):
        r"""Gets the id of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审单ID。

        :return: The id of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审单ID。

        :param id: The id of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        r"""Gets the state of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审单数据状态。

        :return: The state of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审单数据状态。

        :param state: The state of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type state: str
        """
        self._state = state

    @property
    def created_date(self):
        r"""Gets the created_date of this ShowIpdProcessInstancesResponseResultProcessInstances.

        创建时间。

        :return: The created_date of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this ShowIpdProcessInstancesResponseResultProcessInstances.

        创建时间。

        :param created_date: The created_date of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def category(self):
        r"""Gets the category of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审单类型。

        :return: The category of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowIpdProcessInstancesResponseResultProcessInstances.

        评审单类型。

        :param category: The category of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type category: str
        """
        self._category = category

    @property
    def plan_start_date(self):
        r"""Gets the plan_start_date of this ShowIpdProcessInstancesResponseResultProcessInstances.

        计划开始时间。

        :return: The plan_start_date of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        r"""Sets the plan_start_date of this ShowIpdProcessInstancesResponseResultProcessInstances.

        计划开始时间。

        :param plan_start_date: The plan_start_date of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type plan_start_date: str
        """
        self._plan_start_date = plan_start_date

    @property
    def status(self):
        r"""Gets the status of this ShowIpdProcessInstancesResponseResultProcessInstances.

        :return: The status of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: :class:`huaweicloudsdkprojectman.v4.ShowIpdProcessInstancesResponseResultStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowIpdProcessInstancesResponseResultProcessInstances.

        :param status: The status of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type status: :class:`huaweicloudsdkprojectman.v4.ShowIpdProcessInstancesResponseResultStatus`
        """
        self._status = status

    @property
    def ccbs(self):
        r"""Gets the ccbs of this ShowIpdProcessInstancesResponseResultProcessInstances.

        决策人对象列表。

        :return: The ccbs of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserObject`]
        """
        return self._ccbs

    @ccbs.setter
    def ccbs(self, ccbs):
        r"""Sets the ccbs of this ShowIpdProcessInstancesResponseResultProcessInstances.

        决策人对象列表。

        :param ccbs: The ccbs of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type ccbs: list[:class:`huaweicloudsdkprojectman.v4.UserObject`]
        """
        self._ccbs = ccbs

    @property
    def opinions(self):
        r"""Gets the opinions of this ShowIpdProcessInstancesResponseResultProcessInstances.

        opinion对象列表。

        :return: The opinions of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ShowIpdProcessInstancesResponseResultOpinions`]
        """
        return self._opinions

    @opinions.setter
    def opinions(self, opinions):
        r"""Sets the opinions of this ShowIpdProcessInstancesResponseResultProcessInstances.

        opinion对象列表。

        :param opinions: The opinions of this ShowIpdProcessInstancesResponseResultProcessInstances.
        :type opinions: list[:class:`huaweicloudsdkprojectman.v4.ShowIpdProcessInstancesResponseResultOpinions`]
        """
        self._opinions = opinions

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
        if not isinstance(other, ShowIpdProcessInstancesResponseResultProcessInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
