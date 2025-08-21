# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProjectMergeRequestApproverSettingResponse(SdkResponse):

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
        'target': 'str',
        'target_type': 'str',
        'is_use_approval': 'bool',
        'approval_required_reviewers': 'int',
        'approval_required_approvers': 'int',
        'reset_approvals_on_push': 'bool',
        'reset_reviewers_on_push': 'bool',
        'approvers_from_project': 'bool',
        'append_reviewer_ids': 'list[int]',
        'append_reviewers': 'list[UserBasicDto]',
        'append_approver_ids': 'list[int]',
        'append_approvers': 'list[UserBasicDto]',
        'only_merge_when_pipeline_pass': 'bool',
        'assignee_ids': 'list[int]',
        'assignees': 'list[UserBasicDto]',
        'approver_ids': 'list[int]',
        'approvers': 'list[UserBasicDto]',
        'reviewer_ids': 'list[int]',
        'reviewers': 'list[UserBasicDto]'
    }

    attribute_map = {
        'id': 'id',
        'target': 'target',
        'target_type': 'target_type',
        'is_use_approval': 'is_use_approval',
        'approval_required_reviewers': 'approval_required_reviewers',
        'approval_required_approvers': 'approval_required_approvers',
        'reset_approvals_on_push': 'reset_approvals_on_push',
        'reset_reviewers_on_push': 'reset_reviewers_on_push',
        'approvers_from_project': 'approvers_from_project',
        'append_reviewer_ids': 'append_reviewer_ids',
        'append_reviewers': 'append_reviewers',
        'append_approver_ids': 'append_approver_ids',
        'append_approvers': 'append_approvers',
        'only_merge_when_pipeline_pass': 'only_merge_when_pipeline_pass',
        'assignee_ids': 'assignee_ids',
        'assignees': 'assignees',
        'approver_ids': 'approver_ids',
        'approvers': 'approvers',
        'reviewer_ids': 'reviewer_ids',
        'reviewers': 'reviewers'
    }

    def __init__(self, id=None, target=None, target_type=None, is_use_approval=None, approval_required_reviewers=None, approval_required_approvers=None, reset_approvals_on_push=None, reset_reviewers_on_push=None, approvers_from_project=None, append_reviewer_ids=None, append_reviewers=None, append_approver_ids=None, append_approvers=None, only_merge_when_pipeline_pass=None, assignee_ids=None, assignees=None, approver_ids=None, approvers=None, reviewer_ids=None, reviewers=None):
        r"""CreateProjectMergeRequestApproverSettingResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：**  设置主键id。
        :type id: str
        :param target: **参数解释：**  分支，可使用*作为通配符使用，如：dev* 指以dev开头的所有分支
        :type target: str
        :param target_type: 设置类型，当前仅开放branch类型
        :type target_type: str
        :param is_use_approval: 是否为审核模式，审核模式：true 评分模式：false
        :type is_use_approval: bool
        :param approval_required_reviewers: 最小检视人数
        :type approval_required_reviewers: int
        :param approval_required_approvers: 最小审核人数
        :type approval_required_approvers: int
        :param reset_approvals_on_push: 推送时是否重置审核门禁状态
        :type reset_approvals_on_push: bool
        :param reset_reviewers_on_push: 推送时是否重置检视门禁状态
        :type reset_reviewers_on_push: bool
        :param approvers_from_project: 是否开启仅能从以下审核/检视人中追加审核人/检视人
        :type approvers_from_project: bool
        :param append_reviewer_ids: 追加检视人id列表
        :type append_reviewer_ids: list[int]
        :param append_reviewers: 追加检视人实体列表
        :type append_reviewers: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        :param append_approver_ids: 追加审核人id列表
        :type append_approver_ids: list[int]
        :param append_approvers: 追加审核人实体列表
        :type append_approvers: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        :param only_merge_when_pipeline_pass: 是否开启流水线门禁
        :type only_merge_when_pipeline_pass: bool
        :param assignee_ids: 合并人id列表
        :type assignee_ids: list[int]
        :param assignees: 合并人实体列表
        :type assignees: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        :param approver_ids: 审核人id列表
        :type approver_ids: list[int]
        :param approvers: 审核人实体列表
        :type approvers: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        :param reviewer_ids: 检视人id列表
        :type reviewer_ids: list[int]
        :param reviewers: 检视人实体列表
        :type reviewers: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        
        super(CreateProjectMergeRequestApproverSettingResponse, self).__init__()

        self._id = None
        self._target = None
        self._target_type = None
        self._is_use_approval = None
        self._approval_required_reviewers = None
        self._approval_required_approvers = None
        self._reset_approvals_on_push = None
        self._reset_reviewers_on_push = None
        self._approvers_from_project = None
        self._append_reviewer_ids = None
        self._append_reviewers = None
        self._append_approver_ids = None
        self._append_approvers = None
        self._only_merge_when_pipeline_pass = None
        self._assignee_ids = None
        self._assignees = None
        self._approver_ids = None
        self._approvers = None
        self._reviewer_ids = None
        self._reviewers = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if target is not None:
            self.target = target
        if target_type is not None:
            self.target_type = target_type
        if is_use_approval is not None:
            self.is_use_approval = is_use_approval
        if approval_required_reviewers is not None:
            self.approval_required_reviewers = approval_required_reviewers
        if approval_required_approvers is not None:
            self.approval_required_approvers = approval_required_approvers
        if reset_approvals_on_push is not None:
            self.reset_approvals_on_push = reset_approvals_on_push
        if reset_reviewers_on_push is not None:
            self.reset_reviewers_on_push = reset_reviewers_on_push
        if approvers_from_project is not None:
            self.approvers_from_project = approvers_from_project
        if append_reviewer_ids is not None:
            self.append_reviewer_ids = append_reviewer_ids
        if append_reviewers is not None:
            self.append_reviewers = append_reviewers
        if append_approver_ids is not None:
            self.append_approver_ids = append_approver_ids
        if append_approvers is not None:
            self.append_approvers = append_approvers
        if only_merge_when_pipeline_pass is not None:
            self.only_merge_when_pipeline_pass = only_merge_when_pipeline_pass
        if assignee_ids is not None:
            self.assignee_ids = assignee_ids
        if assignees is not None:
            self.assignees = assignees
        if approver_ids is not None:
            self.approver_ids = approver_ids
        if approvers is not None:
            self.approvers = approvers
        if reviewer_ids is not None:
            self.reviewer_ids = reviewer_ids
        if reviewers is not None:
            self.reviewers = reviewers

    @property
    def id(self):
        r"""Gets the id of this CreateProjectMergeRequestApproverSettingResponse.

        **参数解释：**  设置主键id。

        :return: The id of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateProjectMergeRequestApproverSettingResponse.

        **参数解释：**  设置主键id。

        :param id: The id of this CreateProjectMergeRequestApproverSettingResponse.
        :type id: str
        """
        self._id = id

    @property
    def target(self):
        r"""Gets the target of this CreateProjectMergeRequestApproverSettingResponse.

        **参数解释：**  分支，可使用*作为通配符使用，如：dev* 指以dev开头的所有分支

        :return: The target of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this CreateProjectMergeRequestApproverSettingResponse.

        **参数解释：**  分支，可使用*作为通配符使用，如：dev* 指以dev开头的所有分支

        :param target: The target of this CreateProjectMergeRequestApproverSettingResponse.
        :type target: str
        """
        self._target = target

    @property
    def target_type(self):
        r"""Gets the target_type of this CreateProjectMergeRequestApproverSettingResponse.

        设置类型，当前仅开放branch类型

        :return: The target_type of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this CreateProjectMergeRequestApproverSettingResponse.

        设置类型，当前仅开放branch类型

        :param target_type: The target_type of this CreateProjectMergeRequestApproverSettingResponse.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def is_use_approval(self):
        r"""Gets the is_use_approval of this CreateProjectMergeRequestApproverSettingResponse.

        是否为审核模式，审核模式：true 评分模式：false

        :return: The is_use_approval of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: bool
        """
        return self._is_use_approval

    @is_use_approval.setter
    def is_use_approval(self, is_use_approval):
        r"""Sets the is_use_approval of this CreateProjectMergeRequestApproverSettingResponse.

        是否为审核模式，审核模式：true 评分模式：false

        :param is_use_approval: The is_use_approval of this CreateProjectMergeRequestApproverSettingResponse.
        :type is_use_approval: bool
        """
        self._is_use_approval = is_use_approval

    @property
    def approval_required_reviewers(self):
        r"""Gets the approval_required_reviewers of this CreateProjectMergeRequestApproverSettingResponse.

        最小检视人数

        :return: The approval_required_reviewers of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: int
        """
        return self._approval_required_reviewers

    @approval_required_reviewers.setter
    def approval_required_reviewers(self, approval_required_reviewers):
        r"""Sets the approval_required_reviewers of this CreateProjectMergeRequestApproverSettingResponse.

        最小检视人数

        :param approval_required_reviewers: The approval_required_reviewers of this CreateProjectMergeRequestApproverSettingResponse.
        :type approval_required_reviewers: int
        """
        self._approval_required_reviewers = approval_required_reviewers

    @property
    def approval_required_approvers(self):
        r"""Gets the approval_required_approvers of this CreateProjectMergeRequestApproverSettingResponse.

        最小审核人数

        :return: The approval_required_approvers of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: int
        """
        return self._approval_required_approvers

    @approval_required_approvers.setter
    def approval_required_approvers(self, approval_required_approvers):
        r"""Sets the approval_required_approvers of this CreateProjectMergeRequestApproverSettingResponse.

        最小审核人数

        :param approval_required_approvers: The approval_required_approvers of this CreateProjectMergeRequestApproverSettingResponse.
        :type approval_required_approvers: int
        """
        self._approval_required_approvers = approval_required_approvers

    @property
    def reset_approvals_on_push(self):
        r"""Gets the reset_approvals_on_push of this CreateProjectMergeRequestApproverSettingResponse.

        推送时是否重置审核门禁状态

        :return: The reset_approvals_on_push of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: bool
        """
        return self._reset_approvals_on_push

    @reset_approvals_on_push.setter
    def reset_approvals_on_push(self, reset_approvals_on_push):
        r"""Sets the reset_approvals_on_push of this CreateProjectMergeRequestApproverSettingResponse.

        推送时是否重置审核门禁状态

        :param reset_approvals_on_push: The reset_approvals_on_push of this CreateProjectMergeRequestApproverSettingResponse.
        :type reset_approvals_on_push: bool
        """
        self._reset_approvals_on_push = reset_approvals_on_push

    @property
    def reset_reviewers_on_push(self):
        r"""Gets the reset_reviewers_on_push of this CreateProjectMergeRequestApproverSettingResponse.

        推送时是否重置检视门禁状态

        :return: The reset_reviewers_on_push of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: bool
        """
        return self._reset_reviewers_on_push

    @reset_reviewers_on_push.setter
    def reset_reviewers_on_push(self, reset_reviewers_on_push):
        r"""Sets the reset_reviewers_on_push of this CreateProjectMergeRequestApproverSettingResponse.

        推送时是否重置检视门禁状态

        :param reset_reviewers_on_push: The reset_reviewers_on_push of this CreateProjectMergeRequestApproverSettingResponse.
        :type reset_reviewers_on_push: bool
        """
        self._reset_reviewers_on_push = reset_reviewers_on_push

    @property
    def approvers_from_project(self):
        r"""Gets the approvers_from_project of this CreateProjectMergeRequestApproverSettingResponse.

        是否开启仅能从以下审核/检视人中追加审核人/检视人

        :return: The approvers_from_project of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: bool
        """
        return self._approvers_from_project

    @approvers_from_project.setter
    def approvers_from_project(self, approvers_from_project):
        r"""Sets the approvers_from_project of this CreateProjectMergeRequestApproverSettingResponse.

        是否开启仅能从以下审核/检视人中追加审核人/检视人

        :param approvers_from_project: The approvers_from_project of this CreateProjectMergeRequestApproverSettingResponse.
        :type approvers_from_project: bool
        """
        self._approvers_from_project = approvers_from_project

    @property
    def append_reviewer_ids(self):
        r"""Gets the append_reviewer_ids of this CreateProjectMergeRequestApproverSettingResponse.

        追加检视人id列表

        :return: The append_reviewer_ids of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: list[int]
        """
        return self._append_reviewer_ids

    @append_reviewer_ids.setter
    def append_reviewer_ids(self, append_reviewer_ids):
        r"""Sets the append_reviewer_ids of this CreateProjectMergeRequestApproverSettingResponse.

        追加检视人id列表

        :param append_reviewer_ids: The append_reviewer_ids of this CreateProjectMergeRequestApproverSettingResponse.
        :type append_reviewer_ids: list[int]
        """
        self._append_reviewer_ids = append_reviewer_ids

    @property
    def append_reviewers(self):
        r"""Gets the append_reviewers of this CreateProjectMergeRequestApproverSettingResponse.

        追加检视人实体列表

        :return: The append_reviewers of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        return self._append_reviewers

    @append_reviewers.setter
    def append_reviewers(self, append_reviewers):
        r"""Sets the append_reviewers of this CreateProjectMergeRequestApproverSettingResponse.

        追加检视人实体列表

        :param append_reviewers: The append_reviewers of this CreateProjectMergeRequestApproverSettingResponse.
        :type append_reviewers: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        self._append_reviewers = append_reviewers

    @property
    def append_approver_ids(self):
        r"""Gets the append_approver_ids of this CreateProjectMergeRequestApproverSettingResponse.

        追加审核人id列表

        :return: The append_approver_ids of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: list[int]
        """
        return self._append_approver_ids

    @append_approver_ids.setter
    def append_approver_ids(self, append_approver_ids):
        r"""Sets the append_approver_ids of this CreateProjectMergeRequestApproverSettingResponse.

        追加审核人id列表

        :param append_approver_ids: The append_approver_ids of this CreateProjectMergeRequestApproverSettingResponse.
        :type append_approver_ids: list[int]
        """
        self._append_approver_ids = append_approver_ids

    @property
    def append_approvers(self):
        r"""Gets the append_approvers of this CreateProjectMergeRequestApproverSettingResponse.

        追加审核人实体列表

        :return: The append_approvers of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        return self._append_approvers

    @append_approvers.setter
    def append_approvers(self, append_approvers):
        r"""Sets the append_approvers of this CreateProjectMergeRequestApproverSettingResponse.

        追加审核人实体列表

        :param append_approvers: The append_approvers of this CreateProjectMergeRequestApproverSettingResponse.
        :type append_approvers: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        self._append_approvers = append_approvers

    @property
    def only_merge_when_pipeline_pass(self):
        r"""Gets the only_merge_when_pipeline_pass of this CreateProjectMergeRequestApproverSettingResponse.

        是否开启流水线门禁

        :return: The only_merge_when_pipeline_pass of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: bool
        """
        return self._only_merge_when_pipeline_pass

    @only_merge_when_pipeline_pass.setter
    def only_merge_when_pipeline_pass(self, only_merge_when_pipeline_pass):
        r"""Sets the only_merge_when_pipeline_pass of this CreateProjectMergeRequestApproverSettingResponse.

        是否开启流水线门禁

        :param only_merge_when_pipeline_pass: The only_merge_when_pipeline_pass of this CreateProjectMergeRequestApproverSettingResponse.
        :type only_merge_when_pipeline_pass: bool
        """
        self._only_merge_when_pipeline_pass = only_merge_when_pipeline_pass

    @property
    def assignee_ids(self):
        r"""Gets the assignee_ids of this CreateProjectMergeRequestApproverSettingResponse.

        合并人id列表

        :return: The assignee_ids of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: list[int]
        """
        return self._assignee_ids

    @assignee_ids.setter
    def assignee_ids(self, assignee_ids):
        r"""Sets the assignee_ids of this CreateProjectMergeRequestApproverSettingResponse.

        合并人id列表

        :param assignee_ids: The assignee_ids of this CreateProjectMergeRequestApproverSettingResponse.
        :type assignee_ids: list[int]
        """
        self._assignee_ids = assignee_ids

    @property
    def assignees(self):
        r"""Gets the assignees of this CreateProjectMergeRequestApproverSettingResponse.

        合并人实体列表

        :return: The assignees of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        return self._assignees

    @assignees.setter
    def assignees(self, assignees):
        r"""Sets the assignees of this CreateProjectMergeRequestApproverSettingResponse.

        合并人实体列表

        :param assignees: The assignees of this CreateProjectMergeRequestApproverSettingResponse.
        :type assignees: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        self._assignees = assignees

    @property
    def approver_ids(self):
        r"""Gets the approver_ids of this CreateProjectMergeRequestApproverSettingResponse.

        审核人id列表

        :return: The approver_ids of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: list[int]
        """
        return self._approver_ids

    @approver_ids.setter
    def approver_ids(self, approver_ids):
        r"""Sets the approver_ids of this CreateProjectMergeRequestApproverSettingResponse.

        审核人id列表

        :param approver_ids: The approver_ids of this CreateProjectMergeRequestApproverSettingResponse.
        :type approver_ids: list[int]
        """
        self._approver_ids = approver_ids

    @property
    def approvers(self):
        r"""Gets the approvers of this CreateProjectMergeRequestApproverSettingResponse.

        审核人实体列表

        :return: The approvers of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        return self._approvers

    @approvers.setter
    def approvers(self, approvers):
        r"""Sets the approvers of this CreateProjectMergeRequestApproverSettingResponse.

        审核人实体列表

        :param approvers: The approvers of this CreateProjectMergeRequestApproverSettingResponse.
        :type approvers: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        self._approvers = approvers

    @property
    def reviewer_ids(self):
        r"""Gets the reviewer_ids of this CreateProjectMergeRequestApproverSettingResponse.

        检视人id列表

        :return: The reviewer_ids of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: list[int]
        """
        return self._reviewer_ids

    @reviewer_ids.setter
    def reviewer_ids(self, reviewer_ids):
        r"""Sets the reviewer_ids of this CreateProjectMergeRequestApproverSettingResponse.

        检视人id列表

        :param reviewer_ids: The reviewer_ids of this CreateProjectMergeRequestApproverSettingResponse.
        :type reviewer_ids: list[int]
        """
        self._reviewer_ids = reviewer_ids

    @property
    def reviewers(self):
        r"""Gets the reviewers of this CreateProjectMergeRequestApproverSettingResponse.

        检视人实体列表

        :return: The reviewers of this CreateProjectMergeRequestApproverSettingResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        return self._reviewers

    @reviewers.setter
    def reviewers(self, reviewers):
        r"""Sets the reviewers of this CreateProjectMergeRequestApproverSettingResponse.

        检视人实体列表

        :param reviewers: The reviewers of this CreateProjectMergeRequestApproverSettingResponse.
        :type reviewers: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        self._reviewers = reviewers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateProjectMergeRequestApproverSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
