# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMergeRequestApproverSettingDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target': 'str',
        'is_use_approval': 'bool',
        'approval_required_approvers': 'int',
        'approval_required_reviewers': 'int',
        'reset_approvals_on_push': 'bool',
        'reset_reviewers_on_push': 'bool',
        'approvers_from_project': 'bool',
        'append_reviewer_ids': 'list[int]',
        'append_approver_ids': 'list[int]',
        'only_merge_when_pipeline_pass': 'bool',
        'assignee_ids': 'list[int]',
        'approver_ids': 'list[int]',
        'reviewer_ids': 'list[int]'
    }

    attribute_map = {
        'target': 'target',
        'is_use_approval': 'is_use_approval',
        'approval_required_approvers': 'approval_required_approvers',
        'approval_required_reviewers': 'approval_required_reviewers',
        'reset_approvals_on_push': 'reset_approvals_on_push',
        'reset_reviewers_on_push': 'reset_reviewers_on_push',
        'approvers_from_project': 'approvers_from_project',
        'append_reviewer_ids': 'append_reviewer_ids',
        'append_approver_ids': 'append_approver_ids',
        'only_merge_when_pipeline_pass': 'only_merge_when_pipeline_pass',
        'assignee_ids': 'assignee_ids',
        'approver_ids': 'approver_ids',
        'reviewer_ids': 'reviewer_ids'
    }

    def __init__(self, target=None, is_use_approval=None, approval_required_approvers=None, approval_required_reviewers=None, reset_approvals_on_push=None, reset_reviewers_on_push=None, approvers_from_project=None, append_reviewer_ids=None, append_approver_ids=None, only_merge_when_pipeline_pass=None, assignee_ids=None, approver_ids=None, reviewer_ids=None):
        r"""CreateMergeRequestApproverSettingDto

        The model defined in huaweicloud sdk

        :param target: 配置分支，可使用*作为通配符使用，如：dev* 指以dev开头的所有分支
        :type target: str
        :param is_use_approval: 为false时，“最小检视人数”，“最小审核人数”，“重新推送代码时重置审核人”，“重新推送代码时重置检视人”，“仅能从以下审核人/检视人中追加审核人/检视人”置为默认
        :type is_use_approval: bool
        :param approval_required_approvers: 最小审核人数
        :type approval_required_approvers: int
        :param approval_required_reviewers: 最小检视人数
        :type approval_required_reviewers: int
        :param reset_approvals_on_push: 推送时是否重置审核门禁状态
        :type reset_approvals_on_push: bool
        :param reset_reviewers_on_push: 推送时是否重置检视门禁状态
        :type reset_reviewers_on_push: bool
        :param approvers_from_project: 是否开启仅能从以下审核/检视人中追加审核人/检视人
        :type approvers_from_project: bool
        :param append_reviewer_ids: 追加检视人人用户id列表
        :type append_reviewer_ids: list[int]
        :param append_approver_ids: 追加审核人用户id列表
        :type append_approver_ids: list[int]
        :param only_merge_when_pipeline_pass: 是否开启流水线门禁
        :type only_merge_when_pipeline_pass: bool
        :param assignee_ids: 合并人用户id列表
        :type assignee_ids: list[int]
        :param approver_ids: 审核人用户id列表
        :type approver_ids: list[int]
        :param reviewer_ids: 检视人用户id列表
        :type reviewer_ids: list[int]
        """
        
        

        self._target = None
        self._is_use_approval = None
        self._approval_required_approvers = None
        self._approval_required_reviewers = None
        self._reset_approvals_on_push = None
        self._reset_reviewers_on_push = None
        self._approvers_from_project = None
        self._append_reviewer_ids = None
        self._append_approver_ids = None
        self._only_merge_when_pipeline_pass = None
        self._assignee_ids = None
        self._approver_ids = None
        self._reviewer_ids = None
        self.discriminator = None

        if target is not None:
            self.target = target
        if is_use_approval is not None:
            self.is_use_approval = is_use_approval
        if approval_required_approvers is not None:
            self.approval_required_approvers = approval_required_approvers
        if approval_required_reviewers is not None:
            self.approval_required_reviewers = approval_required_reviewers
        if reset_approvals_on_push is not None:
            self.reset_approvals_on_push = reset_approvals_on_push
        if reset_reviewers_on_push is not None:
            self.reset_reviewers_on_push = reset_reviewers_on_push
        if approvers_from_project is not None:
            self.approvers_from_project = approvers_from_project
        if append_reviewer_ids is not None:
            self.append_reviewer_ids = append_reviewer_ids
        if append_approver_ids is not None:
            self.append_approver_ids = append_approver_ids
        if only_merge_when_pipeline_pass is not None:
            self.only_merge_when_pipeline_pass = only_merge_when_pipeline_pass
        if assignee_ids is not None:
            self.assignee_ids = assignee_ids
        if approver_ids is not None:
            self.approver_ids = approver_ids
        if reviewer_ids is not None:
            self.reviewer_ids = reviewer_ids

    @property
    def target(self):
        r"""Gets the target of this CreateMergeRequestApproverSettingDto.

        配置分支，可使用*作为通配符使用，如：dev* 指以dev开头的所有分支

        :return: The target of this CreateMergeRequestApproverSettingDto.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this CreateMergeRequestApproverSettingDto.

        配置分支，可使用*作为通配符使用，如：dev* 指以dev开头的所有分支

        :param target: The target of this CreateMergeRequestApproverSettingDto.
        :type target: str
        """
        self._target = target

    @property
    def is_use_approval(self):
        r"""Gets the is_use_approval of this CreateMergeRequestApproverSettingDto.

        为false时，“最小检视人数”，“最小审核人数”，“重新推送代码时重置审核人”，“重新推送代码时重置检视人”，“仅能从以下审核人/检视人中追加审核人/检视人”置为默认

        :return: The is_use_approval of this CreateMergeRequestApproverSettingDto.
        :rtype: bool
        """
        return self._is_use_approval

    @is_use_approval.setter
    def is_use_approval(self, is_use_approval):
        r"""Sets the is_use_approval of this CreateMergeRequestApproverSettingDto.

        为false时，“最小检视人数”，“最小审核人数”，“重新推送代码时重置审核人”，“重新推送代码时重置检视人”，“仅能从以下审核人/检视人中追加审核人/检视人”置为默认

        :param is_use_approval: The is_use_approval of this CreateMergeRequestApproverSettingDto.
        :type is_use_approval: bool
        """
        self._is_use_approval = is_use_approval

    @property
    def approval_required_approvers(self):
        r"""Gets the approval_required_approvers of this CreateMergeRequestApproverSettingDto.

        最小审核人数

        :return: The approval_required_approvers of this CreateMergeRequestApproverSettingDto.
        :rtype: int
        """
        return self._approval_required_approvers

    @approval_required_approvers.setter
    def approval_required_approvers(self, approval_required_approvers):
        r"""Sets the approval_required_approvers of this CreateMergeRequestApproverSettingDto.

        最小审核人数

        :param approval_required_approvers: The approval_required_approvers of this CreateMergeRequestApproverSettingDto.
        :type approval_required_approvers: int
        """
        self._approval_required_approvers = approval_required_approvers

    @property
    def approval_required_reviewers(self):
        r"""Gets the approval_required_reviewers of this CreateMergeRequestApproverSettingDto.

        最小检视人数

        :return: The approval_required_reviewers of this CreateMergeRequestApproverSettingDto.
        :rtype: int
        """
        return self._approval_required_reviewers

    @approval_required_reviewers.setter
    def approval_required_reviewers(self, approval_required_reviewers):
        r"""Sets the approval_required_reviewers of this CreateMergeRequestApproverSettingDto.

        最小检视人数

        :param approval_required_reviewers: The approval_required_reviewers of this CreateMergeRequestApproverSettingDto.
        :type approval_required_reviewers: int
        """
        self._approval_required_reviewers = approval_required_reviewers

    @property
    def reset_approvals_on_push(self):
        r"""Gets the reset_approvals_on_push of this CreateMergeRequestApproverSettingDto.

        推送时是否重置审核门禁状态

        :return: The reset_approvals_on_push of this CreateMergeRequestApproverSettingDto.
        :rtype: bool
        """
        return self._reset_approvals_on_push

    @reset_approvals_on_push.setter
    def reset_approvals_on_push(self, reset_approvals_on_push):
        r"""Sets the reset_approvals_on_push of this CreateMergeRequestApproverSettingDto.

        推送时是否重置审核门禁状态

        :param reset_approvals_on_push: The reset_approvals_on_push of this CreateMergeRequestApproverSettingDto.
        :type reset_approvals_on_push: bool
        """
        self._reset_approvals_on_push = reset_approvals_on_push

    @property
    def reset_reviewers_on_push(self):
        r"""Gets the reset_reviewers_on_push of this CreateMergeRequestApproverSettingDto.

        推送时是否重置检视门禁状态

        :return: The reset_reviewers_on_push of this CreateMergeRequestApproverSettingDto.
        :rtype: bool
        """
        return self._reset_reviewers_on_push

    @reset_reviewers_on_push.setter
    def reset_reviewers_on_push(self, reset_reviewers_on_push):
        r"""Sets the reset_reviewers_on_push of this CreateMergeRequestApproverSettingDto.

        推送时是否重置检视门禁状态

        :param reset_reviewers_on_push: The reset_reviewers_on_push of this CreateMergeRequestApproverSettingDto.
        :type reset_reviewers_on_push: bool
        """
        self._reset_reviewers_on_push = reset_reviewers_on_push

    @property
    def approvers_from_project(self):
        r"""Gets the approvers_from_project of this CreateMergeRequestApproverSettingDto.

        是否开启仅能从以下审核/检视人中追加审核人/检视人

        :return: The approvers_from_project of this CreateMergeRequestApproverSettingDto.
        :rtype: bool
        """
        return self._approvers_from_project

    @approvers_from_project.setter
    def approvers_from_project(self, approvers_from_project):
        r"""Sets the approvers_from_project of this CreateMergeRequestApproverSettingDto.

        是否开启仅能从以下审核/检视人中追加审核人/检视人

        :param approvers_from_project: The approvers_from_project of this CreateMergeRequestApproverSettingDto.
        :type approvers_from_project: bool
        """
        self._approvers_from_project = approvers_from_project

    @property
    def append_reviewer_ids(self):
        r"""Gets the append_reviewer_ids of this CreateMergeRequestApproverSettingDto.

        追加检视人人用户id列表

        :return: The append_reviewer_ids of this CreateMergeRequestApproverSettingDto.
        :rtype: list[int]
        """
        return self._append_reviewer_ids

    @append_reviewer_ids.setter
    def append_reviewer_ids(self, append_reviewer_ids):
        r"""Sets the append_reviewer_ids of this CreateMergeRequestApproverSettingDto.

        追加检视人人用户id列表

        :param append_reviewer_ids: The append_reviewer_ids of this CreateMergeRequestApproverSettingDto.
        :type append_reviewer_ids: list[int]
        """
        self._append_reviewer_ids = append_reviewer_ids

    @property
    def append_approver_ids(self):
        r"""Gets the append_approver_ids of this CreateMergeRequestApproverSettingDto.

        追加审核人用户id列表

        :return: The append_approver_ids of this CreateMergeRequestApproverSettingDto.
        :rtype: list[int]
        """
        return self._append_approver_ids

    @append_approver_ids.setter
    def append_approver_ids(self, append_approver_ids):
        r"""Sets the append_approver_ids of this CreateMergeRequestApproverSettingDto.

        追加审核人用户id列表

        :param append_approver_ids: The append_approver_ids of this CreateMergeRequestApproverSettingDto.
        :type append_approver_ids: list[int]
        """
        self._append_approver_ids = append_approver_ids

    @property
    def only_merge_when_pipeline_pass(self):
        r"""Gets the only_merge_when_pipeline_pass of this CreateMergeRequestApproverSettingDto.

        是否开启流水线门禁

        :return: The only_merge_when_pipeline_pass of this CreateMergeRequestApproverSettingDto.
        :rtype: bool
        """
        return self._only_merge_when_pipeline_pass

    @only_merge_when_pipeline_pass.setter
    def only_merge_when_pipeline_pass(self, only_merge_when_pipeline_pass):
        r"""Sets the only_merge_when_pipeline_pass of this CreateMergeRequestApproverSettingDto.

        是否开启流水线门禁

        :param only_merge_when_pipeline_pass: The only_merge_when_pipeline_pass of this CreateMergeRequestApproverSettingDto.
        :type only_merge_when_pipeline_pass: bool
        """
        self._only_merge_when_pipeline_pass = only_merge_when_pipeline_pass

    @property
    def assignee_ids(self):
        r"""Gets the assignee_ids of this CreateMergeRequestApproverSettingDto.

        合并人用户id列表

        :return: The assignee_ids of this CreateMergeRequestApproverSettingDto.
        :rtype: list[int]
        """
        return self._assignee_ids

    @assignee_ids.setter
    def assignee_ids(self, assignee_ids):
        r"""Sets the assignee_ids of this CreateMergeRequestApproverSettingDto.

        合并人用户id列表

        :param assignee_ids: The assignee_ids of this CreateMergeRequestApproverSettingDto.
        :type assignee_ids: list[int]
        """
        self._assignee_ids = assignee_ids

    @property
    def approver_ids(self):
        r"""Gets the approver_ids of this CreateMergeRequestApproverSettingDto.

        审核人用户id列表

        :return: The approver_ids of this CreateMergeRequestApproverSettingDto.
        :rtype: list[int]
        """
        return self._approver_ids

    @approver_ids.setter
    def approver_ids(self, approver_ids):
        r"""Sets the approver_ids of this CreateMergeRequestApproverSettingDto.

        审核人用户id列表

        :param approver_ids: The approver_ids of this CreateMergeRequestApproverSettingDto.
        :type approver_ids: list[int]
        """
        self._approver_ids = approver_ids

    @property
    def reviewer_ids(self):
        r"""Gets the reviewer_ids of this CreateMergeRequestApproverSettingDto.

        检视人用户id列表

        :return: The reviewer_ids of this CreateMergeRequestApproverSettingDto.
        :rtype: list[int]
        """
        return self._reviewer_ids

    @reviewer_ids.setter
    def reviewer_ids(self, reviewer_ids):
        r"""Sets the reviewer_ids of this CreateMergeRequestApproverSettingDto.

        检视人用户id列表

        :param reviewer_ids: The reviewer_ids of this CreateMergeRequestApproverSettingDto.
        :type reviewer_ids: list[int]
        """
        self._reviewer_ids = reviewer_ids

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
        if not isinstance(other, CreateMergeRequestApproverSettingDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
