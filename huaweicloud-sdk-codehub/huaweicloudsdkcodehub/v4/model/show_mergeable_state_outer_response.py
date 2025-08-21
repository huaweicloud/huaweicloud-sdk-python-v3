# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMergeableStateOuterResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'merge_request_id': 'int',
        'state': 'bool',
        'conflict_passed': 'bool',
        'non_ff_passed': 'bool',
        'merged_by_user_passed': 'bool',
        'work_in_progress_passed': 'bool',
        'resolve_discussion_passed': 'bool',
        'ci_state_passed': 'bool',
        'merge_by_self_passed': 'bool',
        'can_force_merge': 'bool',
        'vote_passed': 'bool',
        'e2e_check_passed': 'bool',
        'all_issues_passed': 'bool',
        'only_one_issue_passed': 'bool',
        'approval_reviewers_required_passed': 'bool',
        'approval_approvers_required_passed': 'bool',
        'evaluation_passed': 'bool'
    }

    attribute_map = {
        'merge_request_id': 'merge_request_id',
        'state': 'state',
        'conflict_passed': 'conflict_passed',
        'non_ff_passed': 'non_ff_passed',
        'merged_by_user_passed': 'merged_by_user_passed',
        'work_in_progress_passed': 'work_in_progress_passed',
        'resolve_discussion_passed': 'resolve_discussion_passed',
        'ci_state_passed': 'ci_state_passed',
        'merge_by_self_passed': 'merge_by_self_passed',
        'can_force_merge': 'can_force_merge',
        'vote_passed': 'vote_passed',
        'e2e_check_passed': 'e2e_check_passed',
        'all_issues_passed': 'all_issues_passed',
        'only_one_issue_passed': 'only_one_issue_passed',
        'approval_reviewers_required_passed': 'approval_reviewers_required_passed',
        'approval_approvers_required_passed': 'approval_approvers_required_passed',
        'evaluation_passed': 'evaluation_passed'
    }

    def __init__(self, merge_request_id=None, state=None, conflict_passed=None, non_ff_passed=None, merged_by_user_passed=None, work_in_progress_passed=None, resolve_discussion_passed=None, ci_state_passed=None, merge_by_self_passed=None, can_force_merge=None, vote_passed=None, e2e_check_passed=None, all_issues_passed=None, only_one_issue_passed=None, approval_reviewers_required_passed=None, approval_approvers_required_passed=None, evaluation_passed=None):
        r"""ShowMergeableStateOuterResponse

        The model defined in huaweicloud sdk

        :param merge_request_id: **参数解释：** 合并请求id。
        :type merge_request_id: int
        :param state: **参数解释：** 合并请求的可合入状态。 **约束限制：** - true，可合入。 - false，不可合入。
        :type state: bool
        :param conflict_passed: **参数解释：** 合并请求冲突门禁是否通过。 **约束限制：** - true，不存在冲突。 - false，存在冲突。
        :type conflict_passed: bool
        :param non_ff_passed: **参数解释：** 合并请求是否需要变基。 **约束限制：** - true，不需变基。 - false，需要变基。
        :type non_ff_passed: bool
        :param merged_by_user_passed: **参数解释：** 对当前用户是否有合入当前合并请求的权限判断。 **约束限制：** - true，有权限合入。 - false，无权限合入。
        :type merged_by_user_passed: bool
        :param work_in_progress_passed: **参数解释：** 合并请求WIP门禁是否通过。 **约束限制：** - true，非WIP状态。 - false，WIP状态。
        :type work_in_progress_passed: bool
        :param resolve_discussion_passed: **参数解释：** 合并请求检视意见门禁是否通过。 **约束限制：** - true，检视意见门禁通过。 - false，检视意见门禁不通过。
        :type resolve_discussion_passed: bool
        :param ci_state_passed: **参数解释：** 合并请求流水线门禁是否通过。 **约束限制：** - true，合并请求流水线门禁通过。 - false，合并请求流水线门禁不通过。
        :type ci_state_passed: bool
        :param merge_by_self_passed: **参数解释：** 对当前用户是否有合入自己创建的合并请求的判断。 **约束限制：** - true，非自己创建的mr可以合入。 - false，自己创建的mr不能合入。
        :type merge_by_self_passed: bool
        :param can_force_merge: **参数解释：** 当前用户是否可以强制合入当前合并请求。 **约束限制：** - true，可以强制合入。 - false，不能强制合入。
        :type can_force_merge: bool
        :param vote_passed: **参数解释：** 合并请求评分门禁是否通过。 **约束限制：** - true，评分门禁通过。 - false，评分门禁不通过。
        :type vote_passed: bool
        :param e2e_check_passed: **参数解释：** 合并请求必须与CodeArts Req关联门禁是否通过。 **约束限制：** - true，合并请求必须与CodeArts Req关联门禁通过。 - false，合并请求必须与CodeArts Req关联门禁不通过。
        :type e2e_check_passed: bool
        :param all_issues_passed: **参数解释：** 合并请求所有E2E单号校验必须通过门禁是否通过。 **约束限制：** - true，合并请求所有E2E单号校验必须通过门禁通过。 - false，合并请求所有E2E单号校验必须通过门禁不通过。
        :type all_issues_passed: bool
        :param only_one_issue_passed: **参数解释：** 合并请求只能关联一个单号门禁是否通过。 **约束限制：** - true，合并请求只能关联一个单号门禁通过。 - false，合并请求只能关联一个单号门禁不通过。
        :type only_one_issue_passed: bool
        :param approval_reviewers_required_passed: **参数解释：** 合并请求检视门禁是否通过。 **约束限制：** - true，合并请求检视门禁通过。 - false，合并请求检视门禁不通过。
        :type approval_reviewers_required_passed: bool
        :param approval_approvers_required_passed: **参数解释：** 合并请求审核门禁是否通过。 **约束限制：** - true，合并请求审核门禁通过。 - false，合并请求审核门禁不通过。
        :type approval_approvers_required_passed: bool
        :param evaluation_passed: **参数解释：** 合并请求星级评价门禁是否通过。 **约束限制：** - true，合并请求星级评价门禁通过。 - false，合并请求星级评价门禁不通过。
        :type evaluation_passed: bool
        """
        
        super(ShowMergeableStateOuterResponse, self).__init__()

        self._merge_request_id = None
        self._state = None
        self._conflict_passed = None
        self._non_ff_passed = None
        self._merged_by_user_passed = None
        self._work_in_progress_passed = None
        self._resolve_discussion_passed = None
        self._ci_state_passed = None
        self._merge_by_self_passed = None
        self._can_force_merge = None
        self._vote_passed = None
        self._e2e_check_passed = None
        self._all_issues_passed = None
        self._only_one_issue_passed = None
        self._approval_reviewers_required_passed = None
        self._approval_approvers_required_passed = None
        self._evaluation_passed = None
        self.discriminator = None

        if merge_request_id is not None:
            self.merge_request_id = merge_request_id
        if state is not None:
            self.state = state
        if conflict_passed is not None:
            self.conflict_passed = conflict_passed
        if non_ff_passed is not None:
            self.non_ff_passed = non_ff_passed
        if merged_by_user_passed is not None:
            self.merged_by_user_passed = merged_by_user_passed
        if work_in_progress_passed is not None:
            self.work_in_progress_passed = work_in_progress_passed
        if resolve_discussion_passed is not None:
            self.resolve_discussion_passed = resolve_discussion_passed
        if ci_state_passed is not None:
            self.ci_state_passed = ci_state_passed
        if merge_by_self_passed is not None:
            self.merge_by_self_passed = merge_by_self_passed
        if can_force_merge is not None:
            self.can_force_merge = can_force_merge
        if vote_passed is not None:
            self.vote_passed = vote_passed
        if e2e_check_passed is not None:
            self.e2e_check_passed = e2e_check_passed
        if all_issues_passed is not None:
            self.all_issues_passed = all_issues_passed
        if only_one_issue_passed is not None:
            self.only_one_issue_passed = only_one_issue_passed
        if approval_reviewers_required_passed is not None:
            self.approval_reviewers_required_passed = approval_reviewers_required_passed
        if approval_approvers_required_passed is not None:
            self.approval_approvers_required_passed = approval_approvers_required_passed
        if evaluation_passed is not None:
            self.evaluation_passed = evaluation_passed

    @property
    def merge_request_id(self):
        r"""Gets the merge_request_id of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求id。

        :return: The merge_request_id of this ShowMergeableStateOuterResponse.
        :rtype: int
        """
        return self._merge_request_id

    @merge_request_id.setter
    def merge_request_id(self, merge_request_id):
        r"""Sets the merge_request_id of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求id。

        :param merge_request_id: The merge_request_id of this ShowMergeableStateOuterResponse.
        :type merge_request_id: int
        """
        self._merge_request_id = merge_request_id

    @property
    def state(self):
        r"""Gets the state of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求的可合入状态。 **约束限制：** - true，可合入。 - false，不可合入。

        :return: The state of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求的可合入状态。 **约束限制：** - true，可合入。 - false，不可合入。

        :param state: The state of this ShowMergeableStateOuterResponse.
        :type state: bool
        """
        self._state = state

    @property
    def conflict_passed(self):
        r"""Gets the conflict_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求冲突门禁是否通过。 **约束限制：** - true，不存在冲突。 - false，存在冲突。

        :return: The conflict_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._conflict_passed

    @conflict_passed.setter
    def conflict_passed(self, conflict_passed):
        r"""Sets the conflict_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求冲突门禁是否通过。 **约束限制：** - true，不存在冲突。 - false，存在冲突。

        :param conflict_passed: The conflict_passed of this ShowMergeableStateOuterResponse.
        :type conflict_passed: bool
        """
        self._conflict_passed = conflict_passed

    @property
    def non_ff_passed(self):
        r"""Gets the non_ff_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求是否需要变基。 **约束限制：** - true，不需变基。 - false，需要变基。

        :return: The non_ff_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._non_ff_passed

    @non_ff_passed.setter
    def non_ff_passed(self, non_ff_passed):
        r"""Sets the non_ff_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求是否需要变基。 **约束限制：** - true，不需变基。 - false，需要变基。

        :param non_ff_passed: The non_ff_passed of this ShowMergeableStateOuterResponse.
        :type non_ff_passed: bool
        """
        self._non_ff_passed = non_ff_passed

    @property
    def merged_by_user_passed(self):
        r"""Gets the merged_by_user_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 对当前用户是否有合入当前合并请求的权限判断。 **约束限制：** - true，有权限合入。 - false，无权限合入。

        :return: The merged_by_user_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._merged_by_user_passed

    @merged_by_user_passed.setter
    def merged_by_user_passed(self, merged_by_user_passed):
        r"""Sets the merged_by_user_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 对当前用户是否有合入当前合并请求的权限判断。 **约束限制：** - true，有权限合入。 - false，无权限合入。

        :param merged_by_user_passed: The merged_by_user_passed of this ShowMergeableStateOuterResponse.
        :type merged_by_user_passed: bool
        """
        self._merged_by_user_passed = merged_by_user_passed

    @property
    def work_in_progress_passed(self):
        r"""Gets the work_in_progress_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求WIP门禁是否通过。 **约束限制：** - true，非WIP状态。 - false，WIP状态。

        :return: The work_in_progress_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._work_in_progress_passed

    @work_in_progress_passed.setter
    def work_in_progress_passed(self, work_in_progress_passed):
        r"""Sets the work_in_progress_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求WIP门禁是否通过。 **约束限制：** - true，非WIP状态。 - false，WIP状态。

        :param work_in_progress_passed: The work_in_progress_passed of this ShowMergeableStateOuterResponse.
        :type work_in_progress_passed: bool
        """
        self._work_in_progress_passed = work_in_progress_passed

    @property
    def resolve_discussion_passed(self):
        r"""Gets the resolve_discussion_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求检视意见门禁是否通过。 **约束限制：** - true，检视意见门禁通过。 - false，检视意见门禁不通过。

        :return: The resolve_discussion_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._resolve_discussion_passed

    @resolve_discussion_passed.setter
    def resolve_discussion_passed(self, resolve_discussion_passed):
        r"""Sets the resolve_discussion_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求检视意见门禁是否通过。 **约束限制：** - true，检视意见门禁通过。 - false，检视意见门禁不通过。

        :param resolve_discussion_passed: The resolve_discussion_passed of this ShowMergeableStateOuterResponse.
        :type resolve_discussion_passed: bool
        """
        self._resolve_discussion_passed = resolve_discussion_passed

    @property
    def ci_state_passed(self):
        r"""Gets the ci_state_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求流水线门禁是否通过。 **约束限制：** - true，合并请求流水线门禁通过。 - false，合并请求流水线门禁不通过。

        :return: The ci_state_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._ci_state_passed

    @ci_state_passed.setter
    def ci_state_passed(self, ci_state_passed):
        r"""Sets the ci_state_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求流水线门禁是否通过。 **约束限制：** - true，合并请求流水线门禁通过。 - false，合并请求流水线门禁不通过。

        :param ci_state_passed: The ci_state_passed of this ShowMergeableStateOuterResponse.
        :type ci_state_passed: bool
        """
        self._ci_state_passed = ci_state_passed

    @property
    def merge_by_self_passed(self):
        r"""Gets the merge_by_self_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 对当前用户是否有合入自己创建的合并请求的判断。 **约束限制：** - true，非自己创建的mr可以合入。 - false，自己创建的mr不能合入。

        :return: The merge_by_self_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._merge_by_self_passed

    @merge_by_self_passed.setter
    def merge_by_self_passed(self, merge_by_self_passed):
        r"""Sets the merge_by_self_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 对当前用户是否有合入自己创建的合并请求的判断。 **约束限制：** - true，非自己创建的mr可以合入。 - false，自己创建的mr不能合入。

        :param merge_by_self_passed: The merge_by_self_passed of this ShowMergeableStateOuterResponse.
        :type merge_by_self_passed: bool
        """
        self._merge_by_self_passed = merge_by_self_passed

    @property
    def can_force_merge(self):
        r"""Gets the can_force_merge of this ShowMergeableStateOuterResponse.

        **参数解释：** 当前用户是否可以强制合入当前合并请求。 **约束限制：** - true，可以强制合入。 - false，不能强制合入。

        :return: The can_force_merge of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._can_force_merge

    @can_force_merge.setter
    def can_force_merge(self, can_force_merge):
        r"""Sets the can_force_merge of this ShowMergeableStateOuterResponse.

        **参数解释：** 当前用户是否可以强制合入当前合并请求。 **约束限制：** - true，可以强制合入。 - false，不能强制合入。

        :param can_force_merge: The can_force_merge of this ShowMergeableStateOuterResponse.
        :type can_force_merge: bool
        """
        self._can_force_merge = can_force_merge

    @property
    def vote_passed(self):
        r"""Gets the vote_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求评分门禁是否通过。 **约束限制：** - true，评分门禁通过。 - false，评分门禁不通过。

        :return: The vote_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._vote_passed

    @vote_passed.setter
    def vote_passed(self, vote_passed):
        r"""Sets the vote_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求评分门禁是否通过。 **约束限制：** - true，评分门禁通过。 - false，评分门禁不通过。

        :param vote_passed: The vote_passed of this ShowMergeableStateOuterResponse.
        :type vote_passed: bool
        """
        self._vote_passed = vote_passed

    @property
    def e2e_check_passed(self):
        r"""Gets the e2e_check_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求必须与CodeArts Req关联门禁是否通过。 **约束限制：** - true，合并请求必须与CodeArts Req关联门禁通过。 - false，合并请求必须与CodeArts Req关联门禁不通过。

        :return: The e2e_check_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._e2e_check_passed

    @e2e_check_passed.setter
    def e2e_check_passed(self, e2e_check_passed):
        r"""Sets the e2e_check_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求必须与CodeArts Req关联门禁是否通过。 **约束限制：** - true，合并请求必须与CodeArts Req关联门禁通过。 - false，合并请求必须与CodeArts Req关联门禁不通过。

        :param e2e_check_passed: The e2e_check_passed of this ShowMergeableStateOuterResponse.
        :type e2e_check_passed: bool
        """
        self._e2e_check_passed = e2e_check_passed

    @property
    def all_issues_passed(self):
        r"""Gets the all_issues_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求所有E2E单号校验必须通过门禁是否通过。 **约束限制：** - true，合并请求所有E2E单号校验必须通过门禁通过。 - false，合并请求所有E2E单号校验必须通过门禁不通过。

        :return: The all_issues_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._all_issues_passed

    @all_issues_passed.setter
    def all_issues_passed(self, all_issues_passed):
        r"""Sets the all_issues_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求所有E2E单号校验必须通过门禁是否通过。 **约束限制：** - true，合并请求所有E2E单号校验必须通过门禁通过。 - false，合并请求所有E2E单号校验必须通过门禁不通过。

        :param all_issues_passed: The all_issues_passed of this ShowMergeableStateOuterResponse.
        :type all_issues_passed: bool
        """
        self._all_issues_passed = all_issues_passed

    @property
    def only_one_issue_passed(self):
        r"""Gets the only_one_issue_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求只能关联一个单号门禁是否通过。 **约束限制：** - true，合并请求只能关联一个单号门禁通过。 - false，合并请求只能关联一个单号门禁不通过。

        :return: The only_one_issue_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._only_one_issue_passed

    @only_one_issue_passed.setter
    def only_one_issue_passed(self, only_one_issue_passed):
        r"""Sets the only_one_issue_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求只能关联一个单号门禁是否通过。 **约束限制：** - true，合并请求只能关联一个单号门禁通过。 - false，合并请求只能关联一个单号门禁不通过。

        :param only_one_issue_passed: The only_one_issue_passed of this ShowMergeableStateOuterResponse.
        :type only_one_issue_passed: bool
        """
        self._only_one_issue_passed = only_one_issue_passed

    @property
    def approval_reviewers_required_passed(self):
        r"""Gets the approval_reviewers_required_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求检视门禁是否通过。 **约束限制：** - true，合并请求检视门禁通过。 - false，合并请求检视门禁不通过。

        :return: The approval_reviewers_required_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._approval_reviewers_required_passed

    @approval_reviewers_required_passed.setter
    def approval_reviewers_required_passed(self, approval_reviewers_required_passed):
        r"""Sets the approval_reviewers_required_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求检视门禁是否通过。 **约束限制：** - true，合并请求检视门禁通过。 - false，合并请求检视门禁不通过。

        :param approval_reviewers_required_passed: The approval_reviewers_required_passed of this ShowMergeableStateOuterResponse.
        :type approval_reviewers_required_passed: bool
        """
        self._approval_reviewers_required_passed = approval_reviewers_required_passed

    @property
    def approval_approvers_required_passed(self):
        r"""Gets the approval_approvers_required_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求审核门禁是否通过。 **约束限制：** - true，合并请求审核门禁通过。 - false，合并请求审核门禁不通过。

        :return: The approval_approvers_required_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._approval_approvers_required_passed

    @approval_approvers_required_passed.setter
    def approval_approvers_required_passed(self, approval_approvers_required_passed):
        r"""Sets the approval_approvers_required_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求审核门禁是否通过。 **约束限制：** - true，合并请求审核门禁通过。 - false，合并请求审核门禁不通过。

        :param approval_approvers_required_passed: The approval_approvers_required_passed of this ShowMergeableStateOuterResponse.
        :type approval_approvers_required_passed: bool
        """
        self._approval_approvers_required_passed = approval_approvers_required_passed

    @property
    def evaluation_passed(self):
        r"""Gets the evaluation_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求星级评价门禁是否通过。 **约束限制：** - true，合并请求星级评价门禁通过。 - false，合并请求星级评价门禁不通过。

        :return: The evaluation_passed of this ShowMergeableStateOuterResponse.
        :rtype: bool
        """
        return self._evaluation_passed

    @evaluation_passed.setter
    def evaluation_passed(self, evaluation_passed):
        r"""Sets the evaluation_passed of this ShowMergeableStateOuterResponse.

        **参数解释：** 合并请求星级评价门禁是否通过。 **约束限制：** - true，合并请求星级评价门禁通过。 - false，合并请求星级评价门禁不通过。

        :param evaluation_passed: The evaluation_passed of this ShowMergeableStateOuterResponse.
        :type evaluation_passed: bool
        """
        self._evaluation_passed = evaluation_passed

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
        if not isinstance(other, ShowMergeableStateOuterResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
