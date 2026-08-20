# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class COEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'after_change': 'str',
        'review_complete_time': 'str',
        'review_phase_result': 'str',
        'review_time': 'str',
        'before_change': 'str',
        'category': 'str',
        'ccb_info': 'CcbEntity',
        'ccbs': 'list[UserEntity]',
        'change_type': 'str',
        'co2review': 'str',
        'created_by': 'str',
        'created_date': 'str',
        'description': 'str',
        'id': 'str',
        'issue_id': 'str',
        'issue_number': 'str',
        'issue_category': 'str',
        'modified_by': 'str',
        'modified_date': 'str',
        'opinions': 'list[UserEntity]',
        'opinion_comments': 'list[ReviewOpinionEntity]',
        'review_comments': 'list[ReviewCommentEntity]',
        'approval_comments': 'list[ReviewCommentEntity]',
        'reviewer': 'list[str]',
        'approver': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'after_change': 'after_change',
        'review_complete_time': 'review_complete_time',
        'review_phase_result': 'review_phase_result',
        'review_time': 'review_time',
        'before_change': 'before_change',
        'category': 'category',
        'ccb_info': 'ccb_info',
        'ccbs': 'ccbs',
        'change_type': 'change_type',
        'co2review': 'co2review',
        'created_by': 'created_by',
        'created_date': 'created_date',
        'description': 'description',
        'id': 'id',
        'issue_id': 'issue_id',
        'issue_number': 'issue_number',
        'issue_category': 'issue_category',
        'modified_by': 'modified_by',
        'modified_date': 'modified_date',
        'opinions': 'opinions',
        'opinion_comments': 'opinion_comments',
        'review_comments': 'review_comments',
        'approval_comments': 'approval_comments',
        'reviewer': 'reviewer',
        'approver': 'approver',
        'status': 'status'
    }

    def __init__(self, after_change=None, review_complete_time=None, review_phase_result=None, review_time=None, before_change=None, category=None, ccb_info=None, ccbs=None, change_type=None, co2review=None, created_by=None, created_date=None, description=None, id=None, issue_id=None, issue_number=None, issue_category=None, modified_by=None, modified_date=None, opinions=None, opinion_comments=None, review_comments=None, approval_comments=None, reviewer=None, approver=None, status=None):
        r"""COEntity

        The model defined in huaweicloud sdk

        :param after_change: 变更对象修改后内容。
        :type after_change: str
        :param review_complete_time: 变更对象评审完成时间。
        :type review_complete_time: str
        :param review_phase_result: 变更对象评审阶段结果。
        :type review_phase_result: str
        :param review_time: 变更对象评审时间。
        :type review_time: str
        :param before_change: 变更对象工作项修改前内容。
        :type before_change: str
        :param category: 变更对象工作项类型，此处固定为CO。
        :type category: str
        :param ccb_info: 
        :type ccb_info: :class:`huaweicloudsdkprojectman.v4.CcbEntity`
        :param ccbs: 变更对象决策人列表，列表中只有一个元素。
        :type ccbs: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        :param change_type: 变更类型。
        :type change_type: str
        :param co2review: 变更对象关联的评审单ID。
        :type co2review: str
        :param created_by: 变更对象的创建人ID。
        :type created_by: str
        :param created_date: 变更对象创建时间。
        :type created_date: str
        :param description: 变更对象描述信息。
        :type description: str
        :param id: 变更对象ID。
        :type id: str
        :param issue_id: 变更对象关联的工作项ID。
        :type issue_id: str
        :param issue_number: 变更对象关联的工作项编号。
        :type issue_number: str
        :param issue_category: 变更对象关联的工作项类型。
        :type issue_category: str
        :param modified_by: 变更对象最后修改人ID。
        :type modified_by: str
        :param modified_date: 变更对象最后修改时间。
        :type modified_date: str
        :param opinions: 变更对象评审专家Id列表（创建变更评审时使用）。
        :type opinions: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        :param opinion_comments: 变更对象评审意见。
        :type opinion_comments: list[:class:`huaweicloudsdkprojectman.v4.ReviewOpinionEntity`]
        :param review_comments: 变更对象评审意见（评审更新时使用）。
        :type review_comments: list[:class:`huaweicloudsdkprojectman.v4.ReviewCommentEntity`]
        :param approval_comments: 变更对象决策意见（决策更新时使用）。
        :type approval_comments: list[:class:`huaweicloudsdkprojectman.v4.ReviewCommentEntity`]
        :param reviewer: 变更对象评审专家Id列表。
        :type reviewer: list[str]
        :param approver: 变更对象决策人ID数组。
        :type approver: list[str]
        :param status: 变更对象状态。
        :type status: str
        """
        
        

        self._after_change = None
        self._review_complete_time = None
        self._review_phase_result = None
        self._review_time = None
        self._before_change = None
        self._category = None
        self._ccb_info = None
        self._ccbs = None
        self._change_type = None
        self._co2review = None
        self._created_by = None
        self._created_date = None
        self._description = None
        self._id = None
        self._issue_id = None
        self._issue_number = None
        self._issue_category = None
        self._modified_by = None
        self._modified_date = None
        self._opinions = None
        self._opinion_comments = None
        self._review_comments = None
        self._approval_comments = None
        self._reviewer = None
        self._approver = None
        self._status = None
        self.discriminator = None

        if after_change is not None:
            self.after_change = after_change
        if review_complete_time is not None:
            self.review_complete_time = review_complete_time
        if review_phase_result is not None:
            self.review_phase_result = review_phase_result
        if review_time is not None:
            self.review_time = review_time
        if before_change is not None:
            self.before_change = before_change
        if category is not None:
            self.category = category
        if ccb_info is not None:
            self.ccb_info = ccb_info
        if ccbs is not None:
            self.ccbs = ccbs
        if change_type is not None:
            self.change_type = change_type
        if co2review is not None:
            self.co2review = co2review
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if issue_id is not None:
            self.issue_id = issue_id
        if issue_number is not None:
            self.issue_number = issue_number
        if issue_category is not None:
            self.issue_category = issue_category
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_date is not None:
            self.modified_date = modified_date
        if opinions is not None:
            self.opinions = opinions
        if opinion_comments is not None:
            self.opinion_comments = opinion_comments
        if review_comments is not None:
            self.review_comments = review_comments
        if approval_comments is not None:
            self.approval_comments = approval_comments
        if reviewer is not None:
            self.reviewer = reviewer
        if approver is not None:
            self.approver = approver
        if status is not None:
            self.status = status

    @property
    def after_change(self):
        r"""Gets the after_change of this COEntity.

        变更对象修改后内容。

        :return: The after_change of this COEntity.
        :rtype: str
        """
        return self._after_change

    @after_change.setter
    def after_change(self, after_change):
        r"""Sets the after_change of this COEntity.

        变更对象修改后内容。

        :param after_change: The after_change of this COEntity.
        :type after_change: str
        """
        self._after_change = after_change

    @property
    def review_complete_time(self):
        r"""Gets the review_complete_time of this COEntity.

        变更对象评审完成时间。

        :return: The review_complete_time of this COEntity.
        :rtype: str
        """
        return self._review_complete_time

    @review_complete_time.setter
    def review_complete_time(self, review_complete_time):
        r"""Sets the review_complete_time of this COEntity.

        变更对象评审完成时间。

        :param review_complete_time: The review_complete_time of this COEntity.
        :type review_complete_time: str
        """
        self._review_complete_time = review_complete_time

    @property
    def review_phase_result(self):
        r"""Gets the review_phase_result of this COEntity.

        变更对象评审阶段结果。

        :return: The review_phase_result of this COEntity.
        :rtype: str
        """
        return self._review_phase_result

    @review_phase_result.setter
    def review_phase_result(self, review_phase_result):
        r"""Sets the review_phase_result of this COEntity.

        变更对象评审阶段结果。

        :param review_phase_result: The review_phase_result of this COEntity.
        :type review_phase_result: str
        """
        self._review_phase_result = review_phase_result

    @property
    def review_time(self):
        r"""Gets the review_time of this COEntity.

        变更对象评审时间。

        :return: The review_time of this COEntity.
        :rtype: str
        """
        return self._review_time

    @review_time.setter
    def review_time(self, review_time):
        r"""Sets the review_time of this COEntity.

        变更对象评审时间。

        :param review_time: The review_time of this COEntity.
        :type review_time: str
        """
        self._review_time = review_time

    @property
    def before_change(self):
        r"""Gets the before_change of this COEntity.

        变更对象工作项修改前内容。

        :return: The before_change of this COEntity.
        :rtype: str
        """
        return self._before_change

    @before_change.setter
    def before_change(self, before_change):
        r"""Sets the before_change of this COEntity.

        变更对象工作项修改前内容。

        :param before_change: The before_change of this COEntity.
        :type before_change: str
        """
        self._before_change = before_change

    @property
    def category(self):
        r"""Gets the category of this COEntity.

        变更对象工作项类型，此处固定为CO。

        :return: The category of this COEntity.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this COEntity.

        变更对象工作项类型，此处固定为CO。

        :param category: The category of this COEntity.
        :type category: str
        """
        self._category = category

    @property
    def ccb_info(self):
        r"""Gets the ccb_info of this COEntity.

        :return: The ccb_info of this COEntity.
        :rtype: :class:`huaweicloudsdkprojectman.v4.CcbEntity`
        """
        return self._ccb_info

    @ccb_info.setter
    def ccb_info(self, ccb_info):
        r"""Sets the ccb_info of this COEntity.

        :param ccb_info: The ccb_info of this COEntity.
        :type ccb_info: :class:`huaweicloudsdkprojectman.v4.CcbEntity`
        """
        self._ccb_info = ccb_info

    @property
    def ccbs(self):
        r"""Gets the ccbs of this COEntity.

        变更对象决策人列表，列表中只有一个元素。

        :return: The ccbs of this COEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        return self._ccbs

    @ccbs.setter
    def ccbs(self, ccbs):
        r"""Sets the ccbs of this COEntity.

        变更对象决策人列表，列表中只有一个元素。

        :param ccbs: The ccbs of this COEntity.
        :type ccbs: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        self._ccbs = ccbs

    @property
    def change_type(self):
        r"""Gets the change_type of this COEntity.

        变更类型。

        :return: The change_type of this COEntity.
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        r"""Sets the change_type of this COEntity.

        变更类型。

        :param change_type: The change_type of this COEntity.
        :type change_type: str
        """
        self._change_type = change_type

    @property
    def co2review(self):
        r"""Gets the co2review of this COEntity.

        变更对象关联的评审单ID。

        :return: The co2review of this COEntity.
        :rtype: str
        """
        return self._co2review

    @co2review.setter
    def co2review(self, co2review):
        r"""Sets the co2review of this COEntity.

        变更对象关联的评审单ID。

        :param co2review: The co2review of this COEntity.
        :type co2review: str
        """
        self._co2review = co2review

    @property
    def created_by(self):
        r"""Gets the created_by of this COEntity.

        变更对象的创建人ID。

        :return: The created_by of this COEntity.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this COEntity.

        变更对象的创建人ID。

        :param created_by: The created_by of this COEntity.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this COEntity.

        变更对象创建时间。

        :return: The created_date of this COEntity.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this COEntity.

        变更对象创建时间。

        :param created_date: The created_date of this COEntity.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def description(self):
        r"""Gets the description of this COEntity.

        变更对象描述信息。

        :return: The description of this COEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this COEntity.

        变更对象描述信息。

        :param description: The description of this COEntity.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this COEntity.

        变更对象ID。

        :return: The id of this COEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this COEntity.

        变更对象ID。

        :param id: The id of this COEntity.
        :type id: str
        """
        self._id = id

    @property
    def issue_id(self):
        r"""Gets the issue_id of this COEntity.

        变更对象关联的工作项ID。

        :return: The issue_id of this COEntity.
        :rtype: str
        """
        return self._issue_id

    @issue_id.setter
    def issue_id(self, issue_id):
        r"""Sets the issue_id of this COEntity.

        变更对象关联的工作项ID。

        :param issue_id: The issue_id of this COEntity.
        :type issue_id: str
        """
        self._issue_id = issue_id

    @property
    def issue_number(self):
        r"""Gets the issue_number of this COEntity.

        变更对象关联的工作项编号。

        :return: The issue_number of this COEntity.
        :rtype: str
        """
        return self._issue_number

    @issue_number.setter
    def issue_number(self, issue_number):
        r"""Sets the issue_number of this COEntity.

        变更对象关联的工作项编号。

        :param issue_number: The issue_number of this COEntity.
        :type issue_number: str
        """
        self._issue_number = issue_number

    @property
    def issue_category(self):
        r"""Gets the issue_category of this COEntity.

        变更对象关联的工作项类型。

        :return: The issue_category of this COEntity.
        :rtype: str
        """
        return self._issue_category

    @issue_category.setter
    def issue_category(self, issue_category):
        r"""Sets the issue_category of this COEntity.

        变更对象关联的工作项类型。

        :param issue_category: The issue_category of this COEntity.
        :type issue_category: str
        """
        self._issue_category = issue_category

    @property
    def modified_by(self):
        r"""Gets the modified_by of this COEntity.

        变更对象最后修改人ID。

        :return: The modified_by of this COEntity.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this COEntity.

        变更对象最后修改人ID。

        :param modified_by: The modified_by of this COEntity.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def modified_date(self):
        r"""Gets the modified_date of this COEntity.

        变更对象最后修改时间。

        :return: The modified_date of this COEntity.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this COEntity.

        变更对象最后修改时间。

        :param modified_date: The modified_date of this COEntity.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def opinions(self):
        r"""Gets the opinions of this COEntity.

        变更对象评审专家Id列表（创建变更评审时使用）。

        :return: The opinions of this COEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        return self._opinions

    @opinions.setter
    def opinions(self, opinions):
        r"""Sets the opinions of this COEntity.

        变更对象评审专家Id列表（创建变更评审时使用）。

        :param opinions: The opinions of this COEntity.
        :type opinions: list[:class:`huaweicloudsdkprojectman.v4.UserEntity`]
        """
        self._opinions = opinions

    @property
    def opinion_comments(self):
        r"""Gets the opinion_comments of this COEntity.

        变更对象评审意见。

        :return: The opinion_comments of this COEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ReviewOpinionEntity`]
        """
        return self._opinion_comments

    @opinion_comments.setter
    def opinion_comments(self, opinion_comments):
        r"""Sets the opinion_comments of this COEntity.

        变更对象评审意见。

        :param opinion_comments: The opinion_comments of this COEntity.
        :type opinion_comments: list[:class:`huaweicloudsdkprojectman.v4.ReviewOpinionEntity`]
        """
        self._opinion_comments = opinion_comments

    @property
    def review_comments(self):
        r"""Gets the review_comments of this COEntity.

        变更对象评审意见（评审更新时使用）。

        :return: The review_comments of this COEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ReviewCommentEntity`]
        """
        return self._review_comments

    @review_comments.setter
    def review_comments(self, review_comments):
        r"""Sets the review_comments of this COEntity.

        变更对象评审意见（评审更新时使用）。

        :param review_comments: The review_comments of this COEntity.
        :type review_comments: list[:class:`huaweicloudsdkprojectman.v4.ReviewCommentEntity`]
        """
        self._review_comments = review_comments

    @property
    def approval_comments(self):
        r"""Gets the approval_comments of this COEntity.

        变更对象决策意见（决策更新时使用）。

        :return: The approval_comments of this COEntity.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ReviewCommentEntity`]
        """
        return self._approval_comments

    @approval_comments.setter
    def approval_comments(self, approval_comments):
        r"""Sets the approval_comments of this COEntity.

        变更对象决策意见（决策更新时使用）。

        :param approval_comments: The approval_comments of this COEntity.
        :type approval_comments: list[:class:`huaweicloudsdkprojectman.v4.ReviewCommentEntity`]
        """
        self._approval_comments = approval_comments

    @property
    def reviewer(self):
        r"""Gets the reviewer of this COEntity.

        变更对象评审专家Id列表。

        :return: The reviewer of this COEntity.
        :rtype: list[str]
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        r"""Sets the reviewer of this COEntity.

        变更对象评审专家Id列表。

        :param reviewer: The reviewer of this COEntity.
        :type reviewer: list[str]
        """
        self._reviewer = reviewer

    @property
    def approver(self):
        r"""Gets the approver of this COEntity.

        变更对象决策人ID数组。

        :return: The approver of this COEntity.
        :rtype: list[str]
        """
        return self._approver

    @approver.setter
    def approver(self, approver):
        r"""Sets the approver of this COEntity.

        变更对象决策人ID数组。

        :param approver: The approver of this COEntity.
        :type approver: list[str]
        """
        self._approver = approver

    @property
    def status(self):
        r"""Gets the status of this COEntity.

        变更对象状态。

        :return: The status of this COEntity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this COEntity.

        变更对象状态。

        :param status: The status of this COEntity.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, COEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
