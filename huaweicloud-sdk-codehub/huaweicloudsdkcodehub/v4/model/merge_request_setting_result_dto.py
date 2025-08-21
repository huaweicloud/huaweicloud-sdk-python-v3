# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestSettingResultDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'disable_merge_by_self': 'bool',
        'disable_approve_by_self': 'bool',
        'disable_review_by_self': 'bool',
        'created_at': 'str',
        'updated_at': 'str',
        'can_force_merge': 'bool',
        'disable_squash_merge': 'bool',
        'must_relate_issue': 'bool',
        'need_relate_issue_branches': 'str',
        'need_all_issues_check_passed': 'bool',
        'review_mode': 'str',
        'add_notes_after_merged': 'bool',
        'merged_commit_author': 'str',
        'evaluation_role': 'int',
        'evaluation_merge_gate': 'bool',
        'mark_auto_merged_mr_as_closed': 'bool',
        'delete_source_branch_when_merged': 'bool',
        'auto_squash_merge': 'bool',
        'squash_merge_with_no_merge_commit': 'bool',
        'only_allow_one_issue_check_passed': 'bool',
        'enable_custom_evaluation': 'bool',
        'evaluation_types': 'list[EvaluationTypeDto]',
        'can_reopen': 'bool',
        'only_allow_merge_if_all_discussions_are_resolved': 'bool',
        'merge_method': 'str',
        'only_allow_merge_if_vote_bigger_than': 'int',
        'only_assignee_can_merge': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'disable_merge_by_self': 'disable_merge_by_self',
        'disable_approve_by_self': 'disable_approve_by_self',
        'disable_review_by_self': 'disable_review_by_self',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'can_force_merge': 'can_force_merge',
        'disable_squash_merge': 'disable_squash_merge',
        'must_relate_issue': 'must_relate_issue',
        'need_relate_issue_branches': 'need_relate_issue_branches',
        'need_all_issues_check_passed': 'need_all_issues_check_passed',
        'review_mode': 'review_mode',
        'add_notes_after_merged': 'add_notes_after_merged',
        'merged_commit_author': 'merged_commit_author',
        'evaluation_role': 'evaluation_role',
        'evaluation_merge_gate': 'evaluation_merge_gate',
        'mark_auto_merged_mr_as_closed': 'mark_auto_merged_mr_as_closed',
        'delete_source_branch_when_merged': 'delete_source_branch_when_merged',
        'auto_squash_merge': 'auto_squash_merge',
        'squash_merge_with_no_merge_commit': 'squash_merge_with_no_merge_commit',
        'only_allow_one_issue_check_passed': 'only_allow_one_issue_check_passed',
        'enable_custom_evaluation': 'enable_custom_evaluation',
        'evaluation_types': 'evaluation_types',
        'can_reopen': 'can_reopen',
        'only_allow_merge_if_all_discussions_are_resolved': 'only_allow_merge_if_all_discussions_are_resolved',
        'merge_method': 'merge_method',
        'only_allow_merge_if_vote_bigger_than': 'only_allow_merge_if_vote_bigger_than',
        'only_assignee_can_merge': 'only_assignee_can_merge'
    }

    def __init__(self, id=None, disable_merge_by_self=None, disable_approve_by_self=None, disable_review_by_self=None, created_at=None, updated_at=None, can_force_merge=None, disable_squash_merge=None, must_relate_issue=None, need_relate_issue_branches=None, need_all_issues_check_passed=None, review_mode=None, add_notes_after_merged=None, merged_commit_author=None, evaluation_role=None, evaluation_merge_gate=None, mark_auto_merged_mr_as_closed=None, delete_source_branch_when_merged=None, auto_squash_merge=None, squash_merge_with_no_merge_commit=None, only_allow_one_issue_check_passed=None, enable_custom_evaluation=None, evaluation_types=None, can_reopen=None, only_allow_merge_if_all_discussions_are_resolved=None, merge_method=None, only_allow_merge_if_vote_bigger_than=None, only_assignee_can_merge=None):
        r"""MergeRequestSettingResultDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 主键id
        :type id: int
        :param disable_merge_by_self: **参数解释：** 禁止合入自己创建的合并请求
        :type disable_merge_by_self: bool
        :param disable_approve_by_self: **参数解释：** 禁止审核自己创建的合并请求
        :type disable_approve_by_self: bool
        :param disable_review_by_self: **参数解释：** 禁止检视自己创建的合并请求
        :type disable_review_by_self: bool
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。
        :type updated_at: str
        :param can_force_merge: **参数解释：** 允许仓库管理员及项目经理强制合入
        :type can_force_merge: bool
        :param disable_squash_merge: **参数解释：** 禁止Squash合并（合入MR时禁止Squash合并）
        :type disable_squash_merge: bool
        :param must_relate_issue: **参数解释：** 必须与CodeArts Req关联
        :type must_relate_issue: bool
        :param need_relate_issue_branches: **参数解释：** 必须与CodeArts Req关联-选择目标分支配置合并请求策略(分支以逗号分支的字符串)
        :type need_relate_issue_branches: str
        :param need_all_issues_check_passed: **参数解释：** 必须与CodeArts Req关联-所有E2E单号校验必须通过
        :type need_all_issues_check_passed: bool
        :param review_mode: **参数解释：** 合入模式
        :type review_mode: str
        :param add_notes_after_merged: **参数解释：** 允许合并请求合并或关闭后继续做代码检视和评论
        :type add_notes_after_merged: bool
        :param merged_commit_author: **参数解释：** merged_by：使用MR合入者生成Merge Commit created_by：使用MR创建者生成Merge Commit
        :type merged_commit_author: str
        :param evaluation_role: **参数解释：** 是否将星级评价作为合入门禁-参与星级评价角色。 29：勾选开发者 30：勾选开发者，Committer 35：勾选Committer 40：都不勾选
        :type evaluation_role: int
        :param evaluation_merge_gate: **参数解释：** 是否将星级评价作为合入门禁
        :type evaluation_merge_gate: bool
        :param mark_auto_merged_mr_as_closed: **参数解释：** 是否将自动合并的MR状态标记为关闭状态
        :type mark_auto_merged_mr_as_closed: bool
        :param delete_source_branch_when_merged: **参数解释：** 新建合并请求，默认开启合并后删除源分支
        :type delete_source_branch_when_merged: bool
        :param auto_squash_merge: **参数解释：** 新建合并请求，默认开启Squash合并
        :type auto_squash_merge: bool
        :param squash_merge_with_no_merge_commit: **参数解释：** Squash合并不产生Merge节点
        :type squash_merge_with_no_merge_commit: bool
        :param only_allow_one_issue_check_passed: **参数解释：** 只能关联一个单号
        :type only_allow_one_issue_check_passed: bool
        :param enable_custom_evaluation: **参数解释：** 启用MR自定义评价维度分类（MR评价设置）
        :type enable_custom_evaluation: bool
        :param evaluation_types: **参数解释：** 评价维度（MR评价设置）
        :type evaluation_types: list[:class:`huaweicloudsdkcodehub.v4.EvaluationTypeDto`]
        :param can_reopen: **参数解释：** 不能重新打开一个已经关闭的合并请求
        :type can_reopen: bool
        :param only_allow_merge_if_all_discussions_are_resolved: **参数解释：** 评审问题全部解决才能合入
        :type only_allow_merge_if_all_discussions_are_resolved: bool
        :param merge_method: **参数解释：** 合并模式。 merge：通过 Merge Commit 合并 rebase_merge：通过 Merge Commit 合并(记录半线性历史) ff：Fast-forward 合并
        :type merge_method: str
        :param only_allow_merge_if_vote_bigger_than: **参数解释：** 打分模式最低合入分数。
        :type only_allow_merge_if_vote_bigger_than: int
        :param only_assignee_can_merge: **参数解释：** 仅合并人和合并合并请求。
        :type only_assignee_can_merge: bool
        """
        
        

        self._id = None
        self._disable_merge_by_self = None
        self._disable_approve_by_self = None
        self._disable_review_by_self = None
        self._created_at = None
        self._updated_at = None
        self._can_force_merge = None
        self._disable_squash_merge = None
        self._must_relate_issue = None
        self._need_relate_issue_branches = None
        self._need_all_issues_check_passed = None
        self._review_mode = None
        self._add_notes_after_merged = None
        self._merged_commit_author = None
        self._evaluation_role = None
        self._evaluation_merge_gate = None
        self._mark_auto_merged_mr_as_closed = None
        self._delete_source_branch_when_merged = None
        self._auto_squash_merge = None
        self._squash_merge_with_no_merge_commit = None
        self._only_allow_one_issue_check_passed = None
        self._enable_custom_evaluation = None
        self._evaluation_types = None
        self._can_reopen = None
        self._only_allow_merge_if_all_discussions_are_resolved = None
        self._merge_method = None
        self._only_allow_merge_if_vote_bigger_than = None
        self._only_assignee_can_merge = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if disable_merge_by_self is not None:
            self.disable_merge_by_self = disable_merge_by_self
        if disable_approve_by_self is not None:
            self.disable_approve_by_self = disable_approve_by_self
        if disable_review_by_self is not None:
            self.disable_review_by_self = disable_review_by_self
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if can_force_merge is not None:
            self.can_force_merge = can_force_merge
        if disable_squash_merge is not None:
            self.disable_squash_merge = disable_squash_merge
        if must_relate_issue is not None:
            self.must_relate_issue = must_relate_issue
        if need_relate_issue_branches is not None:
            self.need_relate_issue_branches = need_relate_issue_branches
        if need_all_issues_check_passed is not None:
            self.need_all_issues_check_passed = need_all_issues_check_passed
        if review_mode is not None:
            self.review_mode = review_mode
        if add_notes_after_merged is not None:
            self.add_notes_after_merged = add_notes_after_merged
        if merged_commit_author is not None:
            self.merged_commit_author = merged_commit_author
        if evaluation_role is not None:
            self.evaluation_role = evaluation_role
        if evaluation_merge_gate is not None:
            self.evaluation_merge_gate = evaluation_merge_gate
        if mark_auto_merged_mr_as_closed is not None:
            self.mark_auto_merged_mr_as_closed = mark_auto_merged_mr_as_closed
        if delete_source_branch_when_merged is not None:
            self.delete_source_branch_when_merged = delete_source_branch_when_merged
        if auto_squash_merge is not None:
            self.auto_squash_merge = auto_squash_merge
        if squash_merge_with_no_merge_commit is not None:
            self.squash_merge_with_no_merge_commit = squash_merge_with_no_merge_commit
        if only_allow_one_issue_check_passed is not None:
            self.only_allow_one_issue_check_passed = only_allow_one_issue_check_passed
        if enable_custom_evaluation is not None:
            self.enable_custom_evaluation = enable_custom_evaluation
        if evaluation_types is not None:
            self.evaluation_types = evaluation_types
        if can_reopen is not None:
            self.can_reopen = can_reopen
        if only_allow_merge_if_all_discussions_are_resolved is not None:
            self.only_allow_merge_if_all_discussions_are_resolved = only_allow_merge_if_all_discussions_are_resolved
        if merge_method is not None:
            self.merge_method = merge_method
        if only_allow_merge_if_vote_bigger_than is not None:
            self.only_allow_merge_if_vote_bigger_than = only_allow_merge_if_vote_bigger_than
        if only_assignee_can_merge is not None:
            self.only_assignee_can_merge = only_assignee_can_merge

    @property
    def id(self):
        r"""Gets the id of this MergeRequestSettingResultDto.

        **参数解释：** 主键id

        :return: The id of this MergeRequestSettingResultDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MergeRequestSettingResultDto.

        **参数解释：** 主键id

        :param id: The id of this MergeRequestSettingResultDto.
        :type id: int
        """
        self._id = id

    @property
    def disable_merge_by_self(self):
        r"""Gets the disable_merge_by_self of this MergeRequestSettingResultDto.

        **参数解释：** 禁止合入自己创建的合并请求

        :return: The disable_merge_by_self of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._disable_merge_by_self

    @disable_merge_by_self.setter
    def disable_merge_by_self(self, disable_merge_by_self):
        r"""Sets the disable_merge_by_self of this MergeRequestSettingResultDto.

        **参数解释：** 禁止合入自己创建的合并请求

        :param disable_merge_by_self: The disable_merge_by_self of this MergeRequestSettingResultDto.
        :type disable_merge_by_self: bool
        """
        self._disable_merge_by_self = disable_merge_by_self

    @property
    def disable_approve_by_self(self):
        r"""Gets the disable_approve_by_self of this MergeRequestSettingResultDto.

        **参数解释：** 禁止审核自己创建的合并请求

        :return: The disable_approve_by_self of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._disable_approve_by_self

    @disable_approve_by_self.setter
    def disable_approve_by_self(self, disable_approve_by_self):
        r"""Sets the disable_approve_by_self of this MergeRequestSettingResultDto.

        **参数解释：** 禁止审核自己创建的合并请求

        :param disable_approve_by_self: The disable_approve_by_self of this MergeRequestSettingResultDto.
        :type disable_approve_by_self: bool
        """
        self._disable_approve_by_self = disable_approve_by_self

    @property
    def disable_review_by_self(self):
        r"""Gets the disable_review_by_self of this MergeRequestSettingResultDto.

        **参数解释：** 禁止检视自己创建的合并请求

        :return: The disable_review_by_self of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._disable_review_by_self

    @disable_review_by_self.setter
    def disable_review_by_self(self, disable_review_by_self):
        r"""Sets the disable_review_by_self of this MergeRequestSettingResultDto.

        **参数解释：** 禁止检视自己创建的合并请求

        :param disable_review_by_self: The disable_review_by_self of this MergeRequestSettingResultDto.
        :type disable_review_by_self: bool
        """
        self._disable_review_by_self = disable_review_by_self

    @property
    def created_at(self):
        r"""Gets the created_at of this MergeRequestSettingResultDto.

        **参数解释：** 创建时间。

        :return: The created_at of this MergeRequestSettingResultDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MergeRequestSettingResultDto.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this MergeRequestSettingResultDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this MergeRequestSettingResultDto.

        **参数解释：** 更新时间。

        :return: The updated_at of this MergeRequestSettingResultDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this MergeRequestSettingResultDto.

        **参数解释：** 更新时间。

        :param updated_at: The updated_at of this MergeRequestSettingResultDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def can_force_merge(self):
        r"""Gets the can_force_merge of this MergeRequestSettingResultDto.

        **参数解释：** 允许仓库管理员及项目经理强制合入

        :return: The can_force_merge of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._can_force_merge

    @can_force_merge.setter
    def can_force_merge(self, can_force_merge):
        r"""Sets the can_force_merge of this MergeRequestSettingResultDto.

        **参数解释：** 允许仓库管理员及项目经理强制合入

        :param can_force_merge: The can_force_merge of this MergeRequestSettingResultDto.
        :type can_force_merge: bool
        """
        self._can_force_merge = can_force_merge

    @property
    def disable_squash_merge(self):
        r"""Gets the disable_squash_merge of this MergeRequestSettingResultDto.

        **参数解释：** 禁止Squash合并（合入MR时禁止Squash合并）

        :return: The disable_squash_merge of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._disable_squash_merge

    @disable_squash_merge.setter
    def disable_squash_merge(self, disable_squash_merge):
        r"""Sets the disable_squash_merge of this MergeRequestSettingResultDto.

        **参数解释：** 禁止Squash合并（合入MR时禁止Squash合并）

        :param disable_squash_merge: The disable_squash_merge of this MergeRequestSettingResultDto.
        :type disable_squash_merge: bool
        """
        self._disable_squash_merge = disable_squash_merge

    @property
    def must_relate_issue(self):
        r"""Gets the must_relate_issue of this MergeRequestSettingResultDto.

        **参数解释：** 必须与CodeArts Req关联

        :return: The must_relate_issue of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._must_relate_issue

    @must_relate_issue.setter
    def must_relate_issue(self, must_relate_issue):
        r"""Sets the must_relate_issue of this MergeRequestSettingResultDto.

        **参数解释：** 必须与CodeArts Req关联

        :param must_relate_issue: The must_relate_issue of this MergeRequestSettingResultDto.
        :type must_relate_issue: bool
        """
        self._must_relate_issue = must_relate_issue

    @property
    def need_relate_issue_branches(self):
        r"""Gets the need_relate_issue_branches of this MergeRequestSettingResultDto.

        **参数解释：** 必须与CodeArts Req关联-选择目标分支配置合并请求策略(分支以逗号分支的字符串)

        :return: The need_relate_issue_branches of this MergeRequestSettingResultDto.
        :rtype: str
        """
        return self._need_relate_issue_branches

    @need_relate_issue_branches.setter
    def need_relate_issue_branches(self, need_relate_issue_branches):
        r"""Sets the need_relate_issue_branches of this MergeRequestSettingResultDto.

        **参数解释：** 必须与CodeArts Req关联-选择目标分支配置合并请求策略(分支以逗号分支的字符串)

        :param need_relate_issue_branches: The need_relate_issue_branches of this MergeRequestSettingResultDto.
        :type need_relate_issue_branches: str
        """
        self._need_relate_issue_branches = need_relate_issue_branches

    @property
    def need_all_issues_check_passed(self):
        r"""Gets the need_all_issues_check_passed of this MergeRequestSettingResultDto.

        **参数解释：** 必须与CodeArts Req关联-所有E2E单号校验必须通过

        :return: The need_all_issues_check_passed of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._need_all_issues_check_passed

    @need_all_issues_check_passed.setter
    def need_all_issues_check_passed(self, need_all_issues_check_passed):
        r"""Sets the need_all_issues_check_passed of this MergeRequestSettingResultDto.

        **参数解释：** 必须与CodeArts Req关联-所有E2E单号校验必须通过

        :param need_all_issues_check_passed: The need_all_issues_check_passed of this MergeRequestSettingResultDto.
        :type need_all_issues_check_passed: bool
        """
        self._need_all_issues_check_passed = need_all_issues_check_passed

    @property
    def review_mode(self):
        r"""Gets the review_mode of this MergeRequestSettingResultDto.

        **参数解释：** 合入模式

        :return: The review_mode of this MergeRequestSettingResultDto.
        :rtype: str
        """
        return self._review_mode

    @review_mode.setter
    def review_mode(self, review_mode):
        r"""Sets the review_mode of this MergeRequestSettingResultDto.

        **参数解释：** 合入模式

        :param review_mode: The review_mode of this MergeRequestSettingResultDto.
        :type review_mode: str
        """
        self._review_mode = review_mode

    @property
    def add_notes_after_merged(self):
        r"""Gets the add_notes_after_merged of this MergeRequestSettingResultDto.

        **参数解释：** 允许合并请求合并或关闭后继续做代码检视和评论

        :return: The add_notes_after_merged of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._add_notes_after_merged

    @add_notes_after_merged.setter
    def add_notes_after_merged(self, add_notes_after_merged):
        r"""Sets the add_notes_after_merged of this MergeRequestSettingResultDto.

        **参数解释：** 允许合并请求合并或关闭后继续做代码检视和评论

        :param add_notes_after_merged: The add_notes_after_merged of this MergeRequestSettingResultDto.
        :type add_notes_after_merged: bool
        """
        self._add_notes_after_merged = add_notes_after_merged

    @property
    def merged_commit_author(self):
        r"""Gets the merged_commit_author of this MergeRequestSettingResultDto.

        **参数解释：** merged_by：使用MR合入者生成Merge Commit created_by：使用MR创建者生成Merge Commit

        :return: The merged_commit_author of this MergeRequestSettingResultDto.
        :rtype: str
        """
        return self._merged_commit_author

    @merged_commit_author.setter
    def merged_commit_author(self, merged_commit_author):
        r"""Sets the merged_commit_author of this MergeRequestSettingResultDto.

        **参数解释：** merged_by：使用MR合入者生成Merge Commit created_by：使用MR创建者生成Merge Commit

        :param merged_commit_author: The merged_commit_author of this MergeRequestSettingResultDto.
        :type merged_commit_author: str
        """
        self._merged_commit_author = merged_commit_author

    @property
    def evaluation_role(self):
        r"""Gets the evaluation_role of this MergeRequestSettingResultDto.

        **参数解释：** 是否将星级评价作为合入门禁-参与星级评价角色。 29：勾选开发者 30：勾选开发者，Committer 35：勾选Committer 40：都不勾选

        :return: The evaluation_role of this MergeRequestSettingResultDto.
        :rtype: int
        """
        return self._evaluation_role

    @evaluation_role.setter
    def evaluation_role(self, evaluation_role):
        r"""Sets the evaluation_role of this MergeRequestSettingResultDto.

        **参数解释：** 是否将星级评价作为合入门禁-参与星级评价角色。 29：勾选开发者 30：勾选开发者，Committer 35：勾选Committer 40：都不勾选

        :param evaluation_role: The evaluation_role of this MergeRequestSettingResultDto.
        :type evaluation_role: int
        """
        self._evaluation_role = evaluation_role

    @property
    def evaluation_merge_gate(self):
        r"""Gets the evaluation_merge_gate of this MergeRequestSettingResultDto.

        **参数解释：** 是否将星级评价作为合入门禁

        :return: The evaluation_merge_gate of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._evaluation_merge_gate

    @evaluation_merge_gate.setter
    def evaluation_merge_gate(self, evaluation_merge_gate):
        r"""Sets the evaluation_merge_gate of this MergeRequestSettingResultDto.

        **参数解释：** 是否将星级评价作为合入门禁

        :param evaluation_merge_gate: The evaluation_merge_gate of this MergeRequestSettingResultDto.
        :type evaluation_merge_gate: bool
        """
        self._evaluation_merge_gate = evaluation_merge_gate

    @property
    def mark_auto_merged_mr_as_closed(self):
        r"""Gets the mark_auto_merged_mr_as_closed of this MergeRequestSettingResultDto.

        **参数解释：** 是否将自动合并的MR状态标记为关闭状态

        :return: The mark_auto_merged_mr_as_closed of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._mark_auto_merged_mr_as_closed

    @mark_auto_merged_mr_as_closed.setter
    def mark_auto_merged_mr_as_closed(self, mark_auto_merged_mr_as_closed):
        r"""Sets the mark_auto_merged_mr_as_closed of this MergeRequestSettingResultDto.

        **参数解释：** 是否将自动合并的MR状态标记为关闭状态

        :param mark_auto_merged_mr_as_closed: The mark_auto_merged_mr_as_closed of this MergeRequestSettingResultDto.
        :type mark_auto_merged_mr_as_closed: bool
        """
        self._mark_auto_merged_mr_as_closed = mark_auto_merged_mr_as_closed

    @property
    def delete_source_branch_when_merged(self):
        r"""Gets the delete_source_branch_when_merged of this MergeRequestSettingResultDto.

        **参数解释：** 新建合并请求，默认开启合并后删除源分支

        :return: The delete_source_branch_when_merged of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._delete_source_branch_when_merged

    @delete_source_branch_when_merged.setter
    def delete_source_branch_when_merged(self, delete_source_branch_when_merged):
        r"""Sets the delete_source_branch_when_merged of this MergeRequestSettingResultDto.

        **参数解释：** 新建合并请求，默认开启合并后删除源分支

        :param delete_source_branch_when_merged: The delete_source_branch_when_merged of this MergeRequestSettingResultDto.
        :type delete_source_branch_when_merged: bool
        """
        self._delete_source_branch_when_merged = delete_source_branch_when_merged

    @property
    def auto_squash_merge(self):
        r"""Gets the auto_squash_merge of this MergeRequestSettingResultDto.

        **参数解释：** 新建合并请求，默认开启Squash合并

        :return: The auto_squash_merge of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._auto_squash_merge

    @auto_squash_merge.setter
    def auto_squash_merge(self, auto_squash_merge):
        r"""Sets the auto_squash_merge of this MergeRequestSettingResultDto.

        **参数解释：** 新建合并请求，默认开启Squash合并

        :param auto_squash_merge: The auto_squash_merge of this MergeRequestSettingResultDto.
        :type auto_squash_merge: bool
        """
        self._auto_squash_merge = auto_squash_merge

    @property
    def squash_merge_with_no_merge_commit(self):
        r"""Gets the squash_merge_with_no_merge_commit of this MergeRequestSettingResultDto.

        **参数解释：** Squash合并不产生Merge节点

        :return: The squash_merge_with_no_merge_commit of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._squash_merge_with_no_merge_commit

    @squash_merge_with_no_merge_commit.setter
    def squash_merge_with_no_merge_commit(self, squash_merge_with_no_merge_commit):
        r"""Sets the squash_merge_with_no_merge_commit of this MergeRequestSettingResultDto.

        **参数解释：** Squash合并不产生Merge节点

        :param squash_merge_with_no_merge_commit: The squash_merge_with_no_merge_commit of this MergeRequestSettingResultDto.
        :type squash_merge_with_no_merge_commit: bool
        """
        self._squash_merge_with_no_merge_commit = squash_merge_with_no_merge_commit

    @property
    def only_allow_one_issue_check_passed(self):
        r"""Gets the only_allow_one_issue_check_passed of this MergeRequestSettingResultDto.

        **参数解释：** 只能关联一个单号

        :return: The only_allow_one_issue_check_passed of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._only_allow_one_issue_check_passed

    @only_allow_one_issue_check_passed.setter
    def only_allow_one_issue_check_passed(self, only_allow_one_issue_check_passed):
        r"""Sets the only_allow_one_issue_check_passed of this MergeRequestSettingResultDto.

        **参数解释：** 只能关联一个单号

        :param only_allow_one_issue_check_passed: The only_allow_one_issue_check_passed of this MergeRequestSettingResultDto.
        :type only_allow_one_issue_check_passed: bool
        """
        self._only_allow_one_issue_check_passed = only_allow_one_issue_check_passed

    @property
    def enable_custom_evaluation(self):
        r"""Gets the enable_custom_evaluation of this MergeRequestSettingResultDto.

        **参数解释：** 启用MR自定义评价维度分类（MR评价设置）

        :return: The enable_custom_evaluation of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._enable_custom_evaluation

    @enable_custom_evaluation.setter
    def enable_custom_evaluation(self, enable_custom_evaluation):
        r"""Sets the enable_custom_evaluation of this MergeRequestSettingResultDto.

        **参数解释：** 启用MR自定义评价维度分类（MR评价设置）

        :param enable_custom_evaluation: The enable_custom_evaluation of this MergeRequestSettingResultDto.
        :type enable_custom_evaluation: bool
        """
        self._enable_custom_evaluation = enable_custom_evaluation

    @property
    def evaluation_types(self):
        r"""Gets the evaluation_types of this MergeRequestSettingResultDto.

        **参数解释：** 评价维度（MR评价设置）

        :return: The evaluation_types of this MergeRequestSettingResultDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.EvaluationTypeDto`]
        """
        return self._evaluation_types

    @evaluation_types.setter
    def evaluation_types(self, evaluation_types):
        r"""Sets the evaluation_types of this MergeRequestSettingResultDto.

        **参数解释：** 评价维度（MR评价设置）

        :param evaluation_types: The evaluation_types of this MergeRequestSettingResultDto.
        :type evaluation_types: list[:class:`huaweicloudsdkcodehub.v4.EvaluationTypeDto`]
        """
        self._evaluation_types = evaluation_types

    @property
    def can_reopen(self):
        r"""Gets the can_reopen of this MergeRequestSettingResultDto.

        **参数解释：** 不能重新打开一个已经关闭的合并请求

        :return: The can_reopen of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._can_reopen

    @can_reopen.setter
    def can_reopen(self, can_reopen):
        r"""Sets the can_reopen of this MergeRequestSettingResultDto.

        **参数解释：** 不能重新打开一个已经关闭的合并请求

        :param can_reopen: The can_reopen of this MergeRequestSettingResultDto.
        :type can_reopen: bool
        """
        self._can_reopen = can_reopen

    @property
    def only_allow_merge_if_all_discussions_are_resolved(self):
        r"""Gets the only_allow_merge_if_all_discussions_are_resolved of this MergeRequestSettingResultDto.

        **参数解释：** 评审问题全部解决才能合入

        :return: The only_allow_merge_if_all_discussions_are_resolved of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._only_allow_merge_if_all_discussions_are_resolved

    @only_allow_merge_if_all_discussions_are_resolved.setter
    def only_allow_merge_if_all_discussions_are_resolved(self, only_allow_merge_if_all_discussions_are_resolved):
        r"""Sets the only_allow_merge_if_all_discussions_are_resolved of this MergeRequestSettingResultDto.

        **参数解释：** 评审问题全部解决才能合入

        :param only_allow_merge_if_all_discussions_are_resolved: The only_allow_merge_if_all_discussions_are_resolved of this MergeRequestSettingResultDto.
        :type only_allow_merge_if_all_discussions_are_resolved: bool
        """
        self._only_allow_merge_if_all_discussions_are_resolved = only_allow_merge_if_all_discussions_are_resolved

    @property
    def merge_method(self):
        r"""Gets the merge_method of this MergeRequestSettingResultDto.

        **参数解释：** 合并模式。 merge：通过 Merge Commit 合并 rebase_merge：通过 Merge Commit 合并(记录半线性历史) ff：Fast-forward 合并

        :return: The merge_method of this MergeRequestSettingResultDto.
        :rtype: str
        """
        return self._merge_method

    @merge_method.setter
    def merge_method(self, merge_method):
        r"""Sets the merge_method of this MergeRequestSettingResultDto.

        **参数解释：** 合并模式。 merge：通过 Merge Commit 合并 rebase_merge：通过 Merge Commit 合并(记录半线性历史) ff：Fast-forward 合并

        :param merge_method: The merge_method of this MergeRequestSettingResultDto.
        :type merge_method: str
        """
        self._merge_method = merge_method

    @property
    def only_allow_merge_if_vote_bigger_than(self):
        r"""Gets the only_allow_merge_if_vote_bigger_than of this MergeRequestSettingResultDto.

        **参数解释：** 打分模式最低合入分数。

        :return: The only_allow_merge_if_vote_bigger_than of this MergeRequestSettingResultDto.
        :rtype: int
        """
        return self._only_allow_merge_if_vote_bigger_than

    @only_allow_merge_if_vote_bigger_than.setter
    def only_allow_merge_if_vote_bigger_than(self, only_allow_merge_if_vote_bigger_than):
        r"""Sets the only_allow_merge_if_vote_bigger_than of this MergeRequestSettingResultDto.

        **参数解释：** 打分模式最低合入分数。

        :param only_allow_merge_if_vote_bigger_than: The only_allow_merge_if_vote_bigger_than of this MergeRequestSettingResultDto.
        :type only_allow_merge_if_vote_bigger_than: int
        """
        self._only_allow_merge_if_vote_bigger_than = only_allow_merge_if_vote_bigger_than

    @property
    def only_assignee_can_merge(self):
        r"""Gets the only_assignee_can_merge of this MergeRequestSettingResultDto.

        **参数解释：** 仅合并人和合并合并请求。

        :return: The only_assignee_can_merge of this MergeRequestSettingResultDto.
        :rtype: bool
        """
        return self._only_assignee_can_merge

    @only_assignee_can_merge.setter
    def only_assignee_can_merge(self, only_assignee_can_merge):
        r"""Sets the only_assignee_can_merge of this MergeRequestSettingResultDto.

        **参数解释：** 仅合并人和合并合并请求。

        :param only_assignee_can_merge: The only_assignee_can_merge of this MergeRequestSettingResultDto.
        :type only_assignee_can_merge: bool
        """
        self._only_assignee_can_merge = only_assignee_can_merge

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
        if not isinstance(other, MergeRequestSettingResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
