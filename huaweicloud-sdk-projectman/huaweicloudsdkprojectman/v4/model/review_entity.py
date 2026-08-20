# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReviewEntity:

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
        'number': 'str',
        'state': 'str',
        'title': 'str',
        'category': 'str',
        'created_by': 'UserEntity',
        'modified_by': 'UserEntity',
        'assigned_cc': 'list[UserEntity]',
        'created_time': 'str',
        'modified_time': 'str',
        'plan_end_date': 'str',
        'plan_start_date': 'str',
        'close_time': 'str',
        'status': 'StatusEntity',
        'description': 'str',
        'closed_time': 'str',
        'approver': 'str',
        'reviewer': 'str',
        'cos': 'list[COEntity]',
        'ccbs': 'list[CcbEntity]',
        'old_status': 'StatusEntity',
        'cc': 'list[UserEntity]'
    }

    attribute_map = {
        'id': 'id',
        'number': 'number',
        'state': 'state',
        'title': 'title',
        'category': 'category',
        'created_by': 'created_by',
        'modified_by': 'modified_by',
        'assigned_cc': 'assigned_cc',
        'created_time': 'created_time',
        'modified_time': 'modified_time',
        'plan_end_date': 'plan_end_date',
        'plan_start_date': 'plan_start_date',
        'close_time': 'close_time',
        'status': 'status',
        'description': 'description',
        'closed_time': 'closed_time',
        'approver': 'approver',
        'reviewer': 'reviewer',
        'cos': 'cos',
        'ccbs': 'ccbs',
        'old_status': 'old_status',
        'cc': 'cc'
    }

    def __init__(self, id=None, number=None, state=None, title=None, category=None, created_by=None, modified_by=None, assigned_cc=None, created_time=None, modified_time=None, plan_end_date=None, plan_start_date=None, close_time=None, status=None, description=None, closed_time=None, approver=None, reviewer=None, cos=None, ccbs=None, old_status=None, cc=None):
        r"""ReviewEntity

        The model defined in huaweicloud sdk

        :param id: 评审单ID。
        :type id: str
        :param number: 评审单编号。
        :type number: str
        :param state: 评审单的生命周期。
        :type state: str
        :param title: 评审单标题。
        :type title: str
        :param category: 评审单类别。
        :type category: str
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param modified_by: 
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        :param assigned_cc: 评审单抄送人。
        :type assigned_cc: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        :param created_time: 评审单创建时间戳。
        :type created_time: str
        :param modified_time: 评审单最后修改时间戳。
        :type modified_time: str
        :param plan_end_date: 计划完成日期时间戳。
        :type plan_end_date: str
        :param plan_start_date: 计划开始日期时间戳。
        :type plan_start_date: str
        :param close_time: 评审单完成时间。
        :type close_time: str
        :param status: 
        :type status: :class:`huaweicloudsdkprojectman.v4.StatusEntity`
        :param description: 评审单描述。
        :type description: str
        :param closed_time: 评审单完成时间。
        :type closed_time: str
        :param approver: 决策人ID。
        :type approver: str
        :param reviewer: 评审专家ID。
        :type reviewer: str
        :param cos: 评审对象列表。
        :type cos: list[:class:`huaweicloudsdkprojectman.v4.COEntity`]
        :param ccbs: 审批信息列表。
        :type ccbs: list[:class:`huaweicloudsdkprojectman.v4.CcbEntity`]
        :param old_status: 
        :type old_status: :class:`huaweicloudsdkprojectman.v4.StatusEntity`
        :param cc: 抄送人列表。
        :type cc: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        
        

        self._id = None
        self._number = None
        self._state = None
        self._title = None
        self._category = None
        self._created_by = None
        self._modified_by = None
        self._assigned_cc = None
        self._created_time = None
        self._modified_time = None
        self._plan_end_date = None
        self._plan_start_date = None
        self._close_time = None
        self._status = None
        self._description = None
        self._closed_time = None
        self._approver = None
        self._reviewer = None
        self._cos = None
        self._ccbs = None
        self._old_status = None
        self._cc = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if number is not None:
            self.number = number
        if state is not None:
            self.state = state
        if title is not None:
            self.title = title
        if category is not None:
            self.category = category
        if created_by is not None:
            self.created_by = created_by
        if modified_by is not None:
            self.modified_by = modified_by
        if assigned_cc is not None:
            self.assigned_cc = assigned_cc
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time
        if plan_end_date is not None:
            self.plan_end_date = plan_end_date
        if plan_start_date is not None:
            self.plan_start_date = plan_start_date
        if close_time is not None:
            self.close_time = close_time
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if closed_time is not None:
            self.closed_time = closed_time
        if approver is not None:
            self.approver = approver
        if reviewer is not None:
            self.reviewer = reviewer
        if cos is not None:
            self.cos = cos
        if ccbs is not None:
            self.ccbs = ccbs
        if old_status is not None:
            self.old_status = old_status
        if cc is not None:
            self.cc = cc

    @property
    def id(self):
        r"""Gets the id of this ReviewEntity.

        评审单ID。

        :return: The id of this ReviewEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ReviewEntity.

        评审单ID。

        :param id: The id of this ReviewEntity.
        :type id: str
        """
        self._id = id

    @property
    def number(self):
        r"""Gets the number of this ReviewEntity.

        评审单编号。

        :return: The number of this ReviewEntity.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ReviewEntity.

        评审单编号。

        :param number: The number of this ReviewEntity.
        :type number: str
        """
        self._number = number

    @property
    def state(self):
        r"""Gets the state of this ReviewEntity.

        评审单的生命周期。

        :return: The state of this ReviewEntity.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ReviewEntity.

        评审单的生命周期。

        :param state: The state of this ReviewEntity.
        :type state: str
        """
        self._state = state

    @property
    def title(self):
        r"""Gets the title of this ReviewEntity.

        评审单标题。

        :return: The title of this ReviewEntity.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ReviewEntity.

        评审单标题。

        :param title: The title of this ReviewEntity.
        :type title: str
        """
        self._title = title

    @property
    def category(self):
        r"""Gets the category of this ReviewEntity.

        评审单类别。

        :return: The category of this ReviewEntity.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ReviewEntity.

        评审单类别。

        :param category: The category of this ReviewEntity.
        :type category: str
        """
        self._category = category

    @property
    def created_by(self):
        r"""Gets the created_by of this ReviewEntity.

        :return: The created_by of this ReviewEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ReviewEntity.

        :param created_by: The created_by of this ReviewEntity.
        :type created_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._created_by = created_by

    @property
    def modified_by(self):
        r"""Gets the modified_by of this ReviewEntity.

        :return: The modified_by of this ReviewEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this ReviewEntity.

        :param modified_by: The modified_by of this ReviewEntity.
        :type modified_by: :class:`huaweicloudsdkprojectman.v4.UserEntity`
        """
        self._modified_by = modified_by

    @property
    def assigned_cc(self):
        r"""Gets the assigned_cc of this ReviewEntity.

        评审单抄送人。

        :return: The assigned_cc of this ReviewEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        return self._assigned_cc

    @assigned_cc.setter
    def assigned_cc(self, assigned_cc):
        r"""Sets the assigned_cc of this ReviewEntity.

        评审单抄送人。

        :param assigned_cc: The assigned_cc of this ReviewEntity.
        :type assigned_cc: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        self._assigned_cc = assigned_cc

    @property
    def created_time(self):
        r"""Gets the created_time of this ReviewEntity.

        评审单创建时间戳。

        :return: The created_time of this ReviewEntity.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ReviewEntity.

        评审单创建时间戳。

        :param created_time: The created_time of this ReviewEntity.
        :type created_time: str
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this ReviewEntity.

        评审单最后修改时间戳。

        :return: The modified_time of this ReviewEntity.
        :rtype: str
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this ReviewEntity.

        评审单最后修改时间戳。

        :param modified_time: The modified_time of this ReviewEntity.
        :type modified_time: str
        """
        self._modified_time = modified_time

    @property
    def plan_end_date(self):
        r"""Gets the plan_end_date of this ReviewEntity.

        计划完成日期时间戳。

        :return: The plan_end_date of this ReviewEntity.
        :rtype: str
        """
        return self._plan_end_date

    @plan_end_date.setter
    def plan_end_date(self, plan_end_date):
        r"""Sets the plan_end_date of this ReviewEntity.

        计划完成日期时间戳。

        :param plan_end_date: The plan_end_date of this ReviewEntity.
        :type plan_end_date: str
        """
        self._plan_end_date = plan_end_date

    @property
    def plan_start_date(self):
        r"""Gets the plan_start_date of this ReviewEntity.

        计划开始日期时间戳。

        :return: The plan_start_date of this ReviewEntity.
        :rtype: str
        """
        return self._plan_start_date

    @plan_start_date.setter
    def plan_start_date(self, plan_start_date):
        r"""Sets the plan_start_date of this ReviewEntity.

        计划开始日期时间戳。

        :param plan_start_date: The plan_start_date of this ReviewEntity.
        :type plan_start_date: str
        """
        self._plan_start_date = plan_start_date

    @property
    def close_time(self):
        r"""Gets the close_time of this ReviewEntity.

        评审单完成时间。

        :return: The close_time of this ReviewEntity.
        :rtype: str
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        r"""Sets the close_time of this ReviewEntity.

        评审单完成时间。

        :param close_time: The close_time of this ReviewEntity.
        :type close_time: str
        """
        self._close_time = close_time

    @property
    def status(self):
        r"""Gets the status of this ReviewEntity.

        :return: The status of this ReviewEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.StatusEntity`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ReviewEntity.

        :param status: The status of this ReviewEntity.
        :type status: :class:`huaweicloudsdkprojectman.v4.StatusEntity`
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this ReviewEntity.

        评审单描述。

        :return: The description of this ReviewEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ReviewEntity.

        评审单描述。

        :param description: The description of this ReviewEntity.
        :type description: str
        """
        self._description = description

    @property
    def closed_time(self):
        r"""Gets the closed_time of this ReviewEntity.

        评审单完成时间。

        :return: The closed_time of this ReviewEntity.
        :rtype: str
        """
        return self._closed_time

    @closed_time.setter
    def closed_time(self, closed_time):
        r"""Sets the closed_time of this ReviewEntity.

        评审单完成时间。

        :param closed_time: The closed_time of this ReviewEntity.
        :type closed_time: str
        """
        self._closed_time = closed_time

    @property
    def approver(self):
        r"""Gets the approver of this ReviewEntity.

        决策人ID。

        :return: The approver of this ReviewEntity.
        :rtype: str
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        r"""Sets the approver of this ReviewEntity.

        决策人ID。

        :param approver: The approver of this ReviewEntity.
        :type approver: str
        """
        self._approver = approver

    @property
    def reviewer(self):
        r"""Gets the reviewer of this ReviewEntity.

        评审专家ID。

        :return: The reviewer of this ReviewEntity.
        :rtype: str
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        r"""Sets the reviewer of this ReviewEntity.

        评审专家ID。

        :param reviewer: The reviewer of this ReviewEntity.
        :type reviewer: str
        """
        self._reviewer = reviewer

    @property
    def cos(self):
        r"""Gets the cos of this ReviewEntity.

        评审对象列表。

        :return: The cos of this ReviewEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.COEntity`]
        """
        return self._cos

    @cos.setter
    def cos(self, cos):
        r"""Sets the cos of this ReviewEntity.

        评审对象列表。

        :param cos: The cos of this ReviewEntity.
        :type cos: list[:class:`huaweicloudsdkprojectman.v4.COEntity`]
        """
        self._cos = cos

    @property
    def ccbs(self):
        r"""Gets the ccbs of this ReviewEntity.

        审批信息列表。

        :return: The ccbs of this ReviewEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CcbEntity`]
        """
        return self._ccbs

    @ccbs.setter
    def ccbs(self, ccbs):
        r"""Sets the ccbs of this ReviewEntity.

        审批信息列表。

        :param ccbs: The ccbs of this ReviewEntity.
        :type ccbs: list[:class:`huaweicloudsdkprojectman.v4.CcbEntity`]
        """
        self._ccbs = ccbs

    @property
    def old_status(self):
        r"""Gets the old_status of this ReviewEntity.

        :return: The old_status of this ReviewEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.StatusEntity`
        """
        return self._old_status

    @old_status.setter
    def old_status(self, old_status):
        r"""Sets the old_status of this ReviewEntity.

        :param old_status: The old_status of this ReviewEntity.
        :type old_status: :class:`huaweicloudsdkprojectman.v4.StatusEntity`
        """
        self._old_status = old_status

    @property
    def cc(self):
        r"""Gets the cc of this ReviewEntity.

        抄送人列表。

        :return: The cc of this ReviewEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        r"""Sets the cc of this ReviewEntity.

        抄送人列表。

        :param cc: The cc of this ReviewEntity.
        :type cc: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        self._cc = cc

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
        if not isinstance(other, ReviewEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
