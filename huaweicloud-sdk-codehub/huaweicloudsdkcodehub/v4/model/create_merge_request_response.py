# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMergeRequestResponse(SdkResponse):

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
        'iid': 'int',
        'repository_id': 'int',
        'title': 'str',
        'description': 'str',
        'state': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'source_branch': 'str',
        'target_branch': 'str',
        'is_source_branch_protected': 'bool',
        'devcloud_source_branch': 'str',
        'author': 'UserBasicExternalDto',
        'source_repository_id': 'int',
        'target_repository_id': 'int',
        'source_project_id': 'str',
        'target_project_id': 'str',
        'labels': 'list[object]',
        'work_in_progress': 'bool',
        'milestone': 'MilestoneBasicDto',
        'merge_when_build_succeeds': 'bool',
        'merge_status': 'str',
        'sha': 'str',
        'merge_commit_sha': 'str',
        'subscribed': 'bool',
        'merged_by': 'UserBasicExternalDto',
        'merged_at': 'str',
        'closed_by': 'UserBasicExternalDto',
        'closed_at': 'str',
        'user_notes_count': 'int',
        'force_remove_source_branch': 'bool',
        'web_url': 'str',
        'merge_request_diff': 'MergeRequestDiffExternalDto',
        'merge_request_reviewers_count': 'int',
        'merge_request_review_count': 'int',
        'merge_request_reviewer_list': 'list[MergeRequestReviewerExternalDto]',
        'merge_request_assignee_list': 'list[UserBasicExternalDto]',
        'notes': 'int',
        'codecheck_state': 'int',
        'codecheck_defect_count': 'int',
        'merge_request_related_work_items': 'list[MergeRequestRelatedWorkItemDto]',
        'diverged_commits_count': 'int',
        'moderation_result': 'bool',
        'moderation_time': 'int',
        'moderation_status': 'int',
        'is_use_temp_branch': 'bool',
        'approval_merge_request_approvers': 'list[ApprovalUserDto]',
        'review_mode': 'str',
        'squash': 'bool',
        'squash_commit_message': 'str',
        'rebase_in_progress': 'bool',
        'source_repository': 'ProjectSimpleDto',
        'target_repository': 'ProjectSimpleDto',
        'is_source_branch_exist': 'bool',
        'merge_request_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'iid': 'iid',
        'repository_id': 'repository_id',
        'title': 'title',
        'description': 'description',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'source_branch': 'source_branch',
        'target_branch': 'target_branch',
        'is_source_branch_protected': 'is_source_branch_protected',
        'devcloud_source_branch': 'devcloud_source_branch',
        'author': 'author',
        'source_repository_id': 'source_repository_id',
        'target_repository_id': 'target_repository_id',
        'source_project_id': 'source_project_id',
        'target_project_id': 'target_project_id',
        'labels': 'labels',
        'work_in_progress': 'work_in_progress',
        'milestone': 'milestone',
        'merge_when_build_succeeds': 'merge_when_build_succeeds',
        'merge_status': 'merge_status',
        'sha': 'sha',
        'merge_commit_sha': 'merge_commit_sha',
        'subscribed': 'subscribed',
        'merged_by': 'merged_by',
        'merged_at': 'merged_at',
        'closed_by': 'closed_by',
        'closed_at': 'closed_at',
        'user_notes_count': 'user_notes_count',
        'force_remove_source_branch': 'force_remove_source_branch',
        'web_url': 'web_url',
        'merge_request_diff': 'merge_request_diff',
        'merge_request_reviewers_count': 'merge_request_reviewers_count',
        'merge_request_review_count': 'merge_request_review_count',
        'merge_request_reviewer_list': 'merge_request_reviewer_list',
        'merge_request_assignee_list': 'merge_request_assignee_list',
        'notes': 'notes',
        'codecheck_state': 'codecheck_state',
        'codecheck_defect_count': 'codecheck_defect_count',
        'merge_request_related_work_items': 'merge_request_related_work_items',
        'diverged_commits_count': 'diverged_commits_count',
        'moderation_result': 'moderation_result',
        'moderation_time': 'moderation_time',
        'moderation_status': 'moderation_status',
        'is_use_temp_branch': 'is_use_temp_branch',
        'approval_merge_request_approvers': 'approval_merge_request_approvers',
        'review_mode': 'review_mode',
        'squash': 'squash',
        'squash_commit_message': 'squash_commit_message',
        'rebase_in_progress': 'rebase_in_progress',
        'source_repository': 'source_repository',
        'target_repository': 'target_repository',
        'is_source_branch_exist': 'is_source_branch_exist',
        'merge_request_type': 'merge_request_type'
    }

    def __init__(self, id=None, iid=None, repository_id=None, title=None, description=None, state=None, created_at=None, updated_at=None, source_branch=None, target_branch=None, is_source_branch_protected=None, devcloud_source_branch=None, author=None, source_repository_id=None, target_repository_id=None, source_project_id=None, target_project_id=None, labels=None, work_in_progress=None, milestone=None, merge_when_build_succeeds=None, merge_status=None, sha=None, merge_commit_sha=None, subscribed=None, merged_by=None, merged_at=None, closed_by=None, closed_at=None, user_notes_count=None, force_remove_source_branch=None, web_url=None, merge_request_diff=None, merge_request_reviewers_count=None, merge_request_review_count=None, merge_request_reviewer_list=None, merge_request_assignee_list=None, notes=None, codecheck_state=None, codecheck_defect_count=None, merge_request_related_work_items=None, diverged_commits_count=None, moderation_result=None, moderation_time=None, moderation_status=None, is_use_temp_branch=None, approval_merge_request_approvers=None, review_mode=None, squash=None, squash_commit_message=None, rebase_in_progress=None, source_repository=None, target_repository=None, is_source_branch_exist=None, merge_request_type=None):
        r"""CreateMergeRequestResponse

        The model defined in huaweicloud sdk

        :param id: 合并请求id
        :type id: int
        :param iid: 合并请求iid
        :type iid: int
        :param repository_id: 目标仓库id
        :type repository_id: int
        :param title: 合并请求标题
        :type title: str
        :param description: 合并请求描述
        :type description: str
        :param state: 合并请求状态
        :type state: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param source_branch: 源分支
        :type source_branch: str
        :param target_branch: 目标分支
        :type target_branch: str
        :param is_source_branch_protected: 源分支是否为保护分支
        :type is_source_branch_protected: bool
        :param devcloud_source_branch: 源分支
        :type devcloud_source_branch: str
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`
        :param source_repository_id: 源仓库id
        :type source_repository_id: int
        :param target_repository_id: 目标仓库id
        :type target_repository_id: int
        :param source_project_id: 源项目id
        :type source_project_id: str
        :param target_project_id: 目标项目id
        :type target_project_id: str
        :param labels: 标签
        :type labels: list[object]
        :param work_in_progress: WIP状态
        :type work_in_progress: bool
        :param milestone: 
        :type milestone: :class:`huaweicloudsdkcodehub.v4.MilestoneBasicDto`
        :param merge_when_build_succeeds: 流水线成功后自动合入
        :type merge_when_build_succeeds: bool
        :param merge_status: 可合并状态
        :type merge_status: str
        :param sha: 当前合并请求最新commit
        :type sha: str
        :param merge_commit_sha: 合入commit节点
        :type merge_commit_sha: str
        :param subscribed: 订阅
        :type subscribed: bool
        :param merged_by: 
        :type merged_by: :class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`
        :param merged_at: 合并时间
        :type merged_at: str
        :param closed_by: 
        :type closed_by: :class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`
        :param closed_at: 关闭时间
        :type closed_at: str
        :param user_notes_count: 检视意见数量
        :type user_notes_count: int
        :param force_remove_source_branch: 合入后删除源分支
        :type force_remove_source_branch: bool
        :param web_url: 主页url
        :type web_url: str
        :param merge_request_diff: 
        :type merge_request_diff: :class:`huaweicloudsdkcodehub.v4.MergeRequestDiffExternalDto`
        :param merge_request_reviewers_count: 评审人数量
        :type merge_request_reviewers_count: int
        :param merge_request_review_count: 打分
        :type merge_request_review_count: int
        :param merge_request_reviewer_list: 评审人列表
        :type merge_request_reviewer_list: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestReviewerExternalDto`]
        :param merge_request_assignee_list: 合并人列表
        :type merge_request_assignee_list: list[:class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`]
        :param notes: 检视意见
        :type notes: int
        :param codecheck_state: 代码检查状态
        :type codecheck_state: int
        :param codecheck_defect_count: 代码检查问题数
        :type codecheck_defect_count: int
        :param merge_request_related_work_items: 合并请求关联单数量
        :type merge_request_related_work_items: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestRelatedWorkItemDto`]
        :param diverged_commits_count: 源分支落后commit数
        :type diverged_commits_count: int
        :param moderation_result: 送审结果
        :type moderation_result: bool
        :param moderation_time: 送审时间时间戳
        :type moderation_time: int
        :param moderation_status: 送审状态码
        :type moderation_status: int
        :param is_use_temp_branch: 是否使用临时分支
        :type is_use_temp_branch: bool
        :param approval_merge_request_approvers: 审核人
        :type approval_merge_request_approvers: list[:class:`huaweicloudsdkcodehub.v4.ApprovalUserDto`]
        :param review_mode: 合并请求模式
        :type review_mode: str
        :param squash: squash合入
        :type squash: bool
        :param squash_commit_message: squash提交信息
        :type squash_commit_message: str
        :param rebase_in_progress: 是否正在rebase
        :type rebase_in_progress: bool
        :param source_repository: 
        :type source_repository: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        :param target_repository: 
        :type target_repository: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        :param is_source_branch_exist: 源分支是否存在
        :type is_source_branch_exist: bool
        :param merge_request_type: 合并请求类型
        :type merge_request_type: str
        """
        
        super(CreateMergeRequestResponse, self).__init__()

        self._id = None
        self._iid = None
        self._repository_id = None
        self._title = None
        self._description = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._source_branch = None
        self._target_branch = None
        self._is_source_branch_protected = None
        self._devcloud_source_branch = None
        self._author = None
        self._source_repository_id = None
        self._target_repository_id = None
        self._source_project_id = None
        self._target_project_id = None
        self._labels = None
        self._work_in_progress = None
        self._milestone = None
        self._merge_when_build_succeeds = None
        self._merge_status = None
        self._sha = None
        self._merge_commit_sha = None
        self._subscribed = None
        self._merged_by = None
        self._merged_at = None
        self._closed_by = None
        self._closed_at = None
        self._user_notes_count = None
        self._force_remove_source_branch = None
        self._web_url = None
        self._merge_request_diff = None
        self._merge_request_reviewers_count = None
        self._merge_request_review_count = None
        self._merge_request_reviewer_list = None
        self._merge_request_assignee_list = None
        self._notes = None
        self._codecheck_state = None
        self._codecheck_defect_count = None
        self._merge_request_related_work_items = None
        self._diverged_commits_count = None
        self._moderation_result = None
        self._moderation_time = None
        self._moderation_status = None
        self._is_use_temp_branch = None
        self._approval_merge_request_approvers = None
        self._review_mode = None
        self._squash = None
        self._squash_commit_message = None
        self._rebase_in_progress = None
        self._source_repository = None
        self._target_repository = None
        self._is_source_branch_exist = None
        self._merge_request_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if iid is not None:
            self.iid = iid
        if repository_id is not None:
            self.repository_id = repository_id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if source_branch is not None:
            self.source_branch = source_branch
        if target_branch is not None:
            self.target_branch = target_branch
        if is_source_branch_protected is not None:
            self.is_source_branch_protected = is_source_branch_protected
        if devcloud_source_branch is not None:
            self.devcloud_source_branch = devcloud_source_branch
        if author is not None:
            self.author = author
        if source_repository_id is not None:
            self.source_repository_id = source_repository_id
        if target_repository_id is not None:
            self.target_repository_id = target_repository_id
        if source_project_id is not None:
            self.source_project_id = source_project_id
        if target_project_id is not None:
            self.target_project_id = target_project_id
        if labels is not None:
            self.labels = labels
        if work_in_progress is not None:
            self.work_in_progress = work_in_progress
        if milestone is not None:
            self.milestone = milestone
        if merge_when_build_succeeds is not None:
            self.merge_when_build_succeeds = merge_when_build_succeeds
        if merge_status is not None:
            self.merge_status = merge_status
        if sha is not None:
            self.sha = sha
        if merge_commit_sha is not None:
            self.merge_commit_sha = merge_commit_sha
        if subscribed is not None:
            self.subscribed = subscribed
        if merged_by is not None:
            self.merged_by = merged_by
        if merged_at is not None:
            self.merged_at = merged_at
        if closed_by is not None:
            self.closed_by = closed_by
        if closed_at is not None:
            self.closed_at = closed_at
        if user_notes_count is not None:
            self.user_notes_count = user_notes_count
        if force_remove_source_branch is not None:
            self.force_remove_source_branch = force_remove_source_branch
        if web_url is not None:
            self.web_url = web_url
        if merge_request_diff is not None:
            self.merge_request_diff = merge_request_diff
        if merge_request_reviewers_count is not None:
            self.merge_request_reviewers_count = merge_request_reviewers_count
        if merge_request_review_count is not None:
            self.merge_request_review_count = merge_request_review_count
        if merge_request_reviewer_list is not None:
            self.merge_request_reviewer_list = merge_request_reviewer_list
        if merge_request_assignee_list is not None:
            self.merge_request_assignee_list = merge_request_assignee_list
        if notes is not None:
            self.notes = notes
        if codecheck_state is not None:
            self.codecheck_state = codecheck_state
        if codecheck_defect_count is not None:
            self.codecheck_defect_count = codecheck_defect_count
        if merge_request_related_work_items is not None:
            self.merge_request_related_work_items = merge_request_related_work_items
        if diverged_commits_count is not None:
            self.diverged_commits_count = diverged_commits_count
        if moderation_result is not None:
            self.moderation_result = moderation_result
        if moderation_time is not None:
            self.moderation_time = moderation_time
        if moderation_status is not None:
            self.moderation_status = moderation_status
        if is_use_temp_branch is not None:
            self.is_use_temp_branch = is_use_temp_branch
        if approval_merge_request_approvers is not None:
            self.approval_merge_request_approvers = approval_merge_request_approvers
        if review_mode is not None:
            self.review_mode = review_mode
        if squash is not None:
            self.squash = squash
        if squash_commit_message is not None:
            self.squash_commit_message = squash_commit_message
        if rebase_in_progress is not None:
            self.rebase_in_progress = rebase_in_progress
        if source_repository is not None:
            self.source_repository = source_repository
        if target_repository is not None:
            self.target_repository = target_repository
        if is_source_branch_exist is not None:
            self.is_source_branch_exist = is_source_branch_exist
        if merge_request_type is not None:
            self.merge_request_type = merge_request_type

    @property
    def id(self):
        r"""Gets the id of this CreateMergeRequestResponse.

        合并请求id

        :return: The id of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateMergeRequestResponse.

        合并请求id

        :param id: The id of this CreateMergeRequestResponse.
        :type id: int
        """
        self._id = id

    @property
    def iid(self):
        r"""Gets the iid of this CreateMergeRequestResponse.

        合并请求iid

        :return: The iid of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._iid

    @iid.setter
    def iid(self, iid):
        r"""Sets the iid of this CreateMergeRequestResponse.

        合并请求iid

        :param iid: The iid of this CreateMergeRequestResponse.
        :type iid: int
        """
        self._iid = iid

    @property
    def repository_id(self):
        r"""Gets the repository_id of this CreateMergeRequestResponse.

        目标仓库id

        :return: The repository_id of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this CreateMergeRequestResponse.

        目标仓库id

        :param repository_id: The repository_id of this CreateMergeRequestResponse.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def title(self):
        r"""Gets the title of this CreateMergeRequestResponse.

        合并请求标题

        :return: The title of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateMergeRequestResponse.

        合并请求标题

        :param title: The title of this CreateMergeRequestResponse.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this CreateMergeRequestResponse.

        合并请求描述

        :return: The description of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateMergeRequestResponse.

        合并请求描述

        :param description: The description of this CreateMergeRequestResponse.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        r"""Gets the state of this CreateMergeRequestResponse.

        合并请求状态

        :return: The state of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CreateMergeRequestResponse.

        合并请求状态

        :param state: The state of this CreateMergeRequestResponse.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateMergeRequestResponse.

        创建时间

        :return: The created_at of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateMergeRequestResponse.

        创建时间

        :param created_at: The created_at of this CreateMergeRequestResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateMergeRequestResponse.

        更新时间

        :return: The updated_at of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateMergeRequestResponse.

        更新时间

        :param updated_at: The updated_at of this CreateMergeRequestResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def source_branch(self):
        r"""Gets the source_branch of this CreateMergeRequestResponse.

        源分支

        :return: The source_branch of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this CreateMergeRequestResponse.

        源分支

        :param source_branch: The source_branch of this CreateMergeRequestResponse.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def target_branch(self):
        r"""Gets the target_branch of this CreateMergeRequestResponse.

        目标分支

        :return: The target_branch of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this CreateMergeRequestResponse.

        目标分支

        :param target_branch: The target_branch of this CreateMergeRequestResponse.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def is_source_branch_protected(self):
        r"""Gets the is_source_branch_protected of this CreateMergeRequestResponse.

        源分支是否为保护分支

        :return: The is_source_branch_protected of this CreateMergeRequestResponse.
        :rtype: bool
        """
        return self._is_source_branch_protected

    @is_source_branch_protected.setter
    def is_source_branch_protected(self, is_source_branch_protected):
        r"""Sets the is_source_branch_protected of this CreateMergeRequestResponse.

        源分支是否为保护分支

        :param is_source_branch_protected: The is_source_branch_protected of this CreateMergeRequestResponse.
        :type is_source_branch_protected: bool
        """
        self._is_source_branch_protected = is_source_branch_protected

    @property
    def devcloud_source_branch(self):
        r"""Gets the devcloud_source_branch of this CreateMergeRequestResponse.

        源分支

        :return: The devcloud_source_branch of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._devcloud_source_branch

    @devcloud_source_branch.setter
    def devcloud_source_branch(self, devcloud_source_branch):
        r"""Sets the devcloud_source_branch of this CreateMergeRequestResponse.

        源分支

        :param devcloud_source_branch: The devcloud_source_branch of this CreateMergeRequestResponse.
        :type devcloud_source_branch: str
        """
        self._devcloud_source_branch = devcloud_source_branch

    @property
    def author(self):
        r"""Gets the author of this CreateMergeRequestResponse.

        :return: The author of this CreateMergeRequestResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this CreateMergeRequestResponse.

        :param author: The author of this CreateMergeRequestResponse.
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`
        """
        self._author = author

    @property
    def source_repository_id(self):
        r"""Gets the source_repository_id of this CreateMergeRequestResponse.

        源仓库id

        :return: The source_repository_id of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._source_repository_id

    @source_repository_id.setter
    def source_repository_id(self, source_repository_id):
        r"""Sets the source_repository_id of this CreateMergeRequestResponse.

        源仓库id

        :param source_repository_id: The source_repository_id of this CreateMergeRequestResponse.
        :type source_repository_id: int
        """
        self._source_repository_id = source_repository_id

    @property
    def target_repository_id(self):
        r"""Gets the target_repository_id of this CreateMergeRequestResponse.

        目标仓库id

        :return: The target_repository_id of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._target_repository_id

    @target_repository_id.setter
    def target_repository_id(self, target_repository_id):
        r"""Sets the target_repository_id of this CreateMergeRequestResponse.

        目标仓库id

        :param target_repository_id: The target_repository_id of this CreateMergeRequestResponse.
        :type target_repository_id: int
        """
        self._target_repository_id = target_repository_id

    @property
    def source_project_id(self):
        r"""Gets the source_project_id of this CreateMergeRequestResponse.

        源项目id

        :return: The source_project_id of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        r"""Sets the source_project_id of this CreateMergeRequestResponse.

        源项目id

        :param source_project_id: The source_project_id of this CreateMergeRequestResponse.
        :type source_project_id: str
        """
        self._source_project_id = source_project_id

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this CreateMergeRequestResponse.

        目标项目id

        :return: The target_project_id of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this CreateMergeRequestResponse.

        目标项目id

        :param target_project_id: The target_project_id of this CreateMergeRequestResponse.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

    @property
    def labels(self):
        r"""Gets the labels of this CreateMergeRequestResponse.

        标签

        :return: The labels of this CreateMergeRequestResponse.
        :rtype: list[object]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CreateMergeRequestResponse.

        标签

        :param labels: The labels of this CreateMergeRequestResponse.
        :type labels: list[object]
        """
        self._labels = labels

    @property
    def work_in_progress(self):
        r"""Gets the work_in_progress of this CreateMergeRequestResponse.

        WIP状态

        :return: The work_in_progress of this CreateMergeRequestResponse.
        :rtype: bool
        """
        return self._work_in_progress

    @work_in_progress.setter
    def work_in_progress(self, work_in_progress):
        r"""Sets the work_in_progress of this CreateMergeRequestResponse.

        WIP状态

        :param work_in_progress: The work_in_progress of this CreateMergeRequestResponse.
        :type work_in_progress: bool
        """
        self._work_in_progress = work_in_progress

    @property
    def milestone(self):
        r"""Gets the milestone of this CreateMergeRequestResponse.

        :return: The milestone of this CreateMergeRequestResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.MilestoneBasicDto`
        """
        return self._milestone

    @milestone.setter
    def milestone(self, milestone):
        r"""Sets the milestone of this CreateMergeRequestResponse.

        :param milestone: The milestone of this CreateMergeRequestResponse.
        :type milestone: :class:`huaweicloudsdkcodehub.v4.MilestoneBasicDto`
        """
        self._milestone = milestone

    @property
    def merge_when_build_succeeds(self):
        r"""Gets the merge_when_build_succeeds of this CreateMergeRequestResponse.

        流水线成功后自动合入

        :return: The merge_when_build_succeeds of this CreateMergeRequestResponse.
        :rtype: bool
        """
        return self._merge_when_build_succeeds

    @merge_when_build_succeeds.setter
    def merge_when_build_succeeds(self, merge_when_build_succeeds):
        r"""Sets the merge_when_build_succeeds of this CreateMergeRequestResponse.

        流水线成功后自动合入

        :param merge_when_build_succeeds: The merge_when_build_succeeds of this CreateMergeRequestResponse.
        :type merge_when_build_succeeds: bool
        """
        self._merge_when_build_succeeds = merge_when_build_succeeds

    @property
    def merge_status(self):
        r"""Gets the merge_status of this CreateMergeRequestResponse.

        可合并状态

        :return: The merge_status of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._merge_status

    @merge_status.setter
    def merge_status(self, merge_status):
        r"""Sets the merge_status of this CreateMergeRequestResponse.

        可合并状态

        :param merge_status: The merge_status of this CreateMergeRequestResponse.
        :type merge_status: str
        """
        self._merge_status = merge_status

    @property
    def sha(self):
        r"""Gets the sha of this CreateMergeRequestResponse.

        当前合并请求最新commit

        :return: The sha of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        r"""Sets the sha of this CreateMergeRequestResponse.

        当前合并请求最新commit

        :param sha: The sha of this CreateMergeRequestResponse.
        :type sha: str
        """
        self._sha = sha

    @property
    def merge_commit_sha(self):
        r"""Gets the merge_commit_sha of this CreateMergeRequestResponse.

        合入commit节点

        :return: The merge_commit_sha of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._merge_commit_sha

    @merge_commit_sha.setter
    def merge_commit_sha(self, merge_commit_sha):
        r"""Sets the merge_commit_sha of this CreateMergeRequestResponse.

        合入commit节点

        :param merge_commit_sha: The merge_commit_sha of this CreateMergeRequestResponse.
        :type merge_commit_sha: str
        """
        self._merge_commit_sha = merge_commit_sha

    @property
    def subscribed(self):
        r"""Gets the subscribed of this CreateMergeRequestResponse.

        订阅

        :return: The subscribed of this CreateMergeRequestResponse.
        :rtype: bool
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        r"""Sets the subscribed of this CreateMergeRequestResponse.

        订阅

        :param subscribed: The subscribed of this CreateMergeRequestResponse.
        :type subscribed: bool
        """
        self._subscribed = subscribed

    @property
    def merged_by(self):
        r"""Gets the merged_by of this CreateMergeRequestResponse.

        :return: The merged_by of this CreateMergeRequestResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`
        """
        return self._merged_by

    @merged_by.setter
    def merged_by(self, merged_by):
        r"""Sets the merged_by of this CreateMergeRequestResponse.

        :param merged_by: The merged_by of this CreateMergeRequestResponse.
        :type merged_by: :class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`
        """
        self._merged_by = merged_by

    @property
    def merged_at(self):
        r"""Gets the merged_at of this CreateMergeRequestResponse.

        合并时间

        :return: The merged_at of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._merged_at

    @merged_at.setter
    def merged_at(self, merged_at):
        r"""Sets the merged_at of this CreateMergeRequestResponse.

        合并时间

        :param merged_at: The merged_at of this CreateMergeRequestResponse.
        :type merged_at: str
        """
        self._merged_at = merged_at

    @property
    def closed_by(self):
        r"""Gets the closed_by of this CreateMergeRequestResponse.

        :return: The closed_by of this CreateMergeRequestResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`
        """
        return self._closed_by

    @closed_by.setter
    def closed_by(self, closed_by):
        r"""Sets the closed_by of this CreateMergeRequestResponse.

        :param closed_by: The closed_by of this CreateMergeRequestResponse.
        :type closed_by: :class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`
        """
        self._closed_by = closed_by

    @property
    def closed_at(self):
        r"""Gets the closed_at of this CreateMergeRequestResponse.

        关闭时间

        :return: The closed_at of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        r"""Sets the closed_at of this CreateMergeRequestResponse.

        关闭时间

        :param closed_at: The closed_at of this CreateMergeRequestResponse.
        :type closed_at: str
        """
        self._closed_at = closed_at

    @property
    def user_notes_count(self):
        r"""Gets the user_notes_count of this CreateMergeRequestResponse.

        检视意见数量

        :return: The user_notes_count of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._user_notes_count

    @user_notes_count.setter
    def user_notes_count(self, user_notes_count):
        r"""Sets the user_notes_count of this CreateMergeRequestResponse.

        检视意见数量

        :param user_notes_count: The user_notes_count of this CreateMergeRequestResponse.
        :type user_notes_count: int
        """
        self._user_notes_count = user_notes_count

    @property
    def force_remove_source_branch(self):
        r"""Gets the force_remove_source_branch of this CreateMergeRequestResponse.

        合入后删除源分支

        :return: The force_remove_source_branch of this CreateMergeRequestResponse.
        :rtype: bool
        """
        return self._force_remove_source_branch

    @force_remove_source_branch.setter
    def force_remove_source_branch(self, force_remove_source_branch):
        r"""Sets the force_remove_source_branch of this CreateMergeRequestResponse.

        合入后删除源分支

        :param force_remove_source_branch: The force_remove_source_branch of this CreateMergeRequestResponse.
        :type force_remove_source_branch: bool
        """
        self._force_remove_source_branch = force_remove_source_branch

    @property
    def web_url(self):
        r"""Gets the web_url of this CreateMergeRequestResponse.

        主页url

        :return: The web_url of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this CreateMergeRequestResponse.

        主页url

        :param web_url: The web_url of this CreateMergeRequestResponse.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def merge_request_diff(self):
        r"""Gets the merge_request_diff of this CreateMergeRequestResponse.

        :return: The merge_request_diff of this CreateMergeRequestResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.MergeRequestDiffExternalDto`
        """
        return self._merge_request_diff

    @merge_request_diff.setter
    def merge_request_diff(self, merge_request_diff):
        r"""Sets the merge_request_diff of this CreateMergeRequestResponse.

        :param merge_request_diff: The merge_request_diff of this CreateMergeRequestResponse.
        :type merge_request_diff: :class:`huaweicloudsdkcodehub.v4.MergeRequestDiffExternalDto`
        """
        self._merge_request_diff = merge_request_diff

    @property
    def merge_request_reviewers_count(self):
        r"""Gets the merge_request_reviewers_count of this CreateMergeRequestResponse.

        评审人数量

        :return: The merge_request_reviewers_count of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._merge_request_reviewers_count

    @merge_request_reviewers_count.setter
    def merge_request_reviewers_count(self, merge_request_reviewers_count):
        r"""Sets the merge_request_reviewers_count of this CreateMergeRequestResponse.

        评审人数量

        :param merge_request_reviewers_count: The merge_request_reviewers_count of this CreateMergeRequestResponse.
        :type merge_request_reviewers_count: int
        """
        self._merge_request_reviewers_count = merge_request_reviewers_count

    @property
    def merge_request_review_count(self):
        r"""Gets the merge_request_review_count of this CreateMergeRequestResponse.

        打分

        :return: The merge_request_review_count of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._merge_request_review_count

    @merge_request_review_count.setter
    def merge_request_review_count(self, merge_request_review_count):
        r"""Sets the merge_request_review_count of this CreateMergeRequestResponse.

        打分

        :param merge_request_review_count: The merge_request_review_count of this CreateMergeRequestResponse.
        :type merge_request_review_count: int
        """
        self._merge_request_review_count = merge_request_review_count

    @property
    def merge_request_reviewer_list(self):
        r"""Gets the merge_request_reviewer_list of this CreateMergeRequestResponse.

        评审人列表

        :return: The merge_request_reviewer_list of this CreateMergeRequestResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestReviewerExternalDto`]
        """
        return self._merge_request_reviewer_list

    @merge_request_reviewer_list.setter
    def merge_request_reviewer_list(self, merge_request_reviewer_list):
        r"""Sets the merge_request_reviewer_list of this CreateMergeRequestResponse.

        评审人列表

        :param merge_request_reviewer_list: The merge_request_reviewer_list of this CreateMergeRequestResponse.
        :type merge_request_reviewer_list: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestReviewerExternalDto`]
        """
        self._merge_request_reviewer_list = merge_request_reviewer_list

    @property
    def merge_request_assignee_list(self):
        r"""Gets the merge_request_assignee_list of this CreateMergeRequestResponse.

        合并人列表

        :return: The merge_request_assignee_list of this CreateMergeRequestResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`]
        """
        return self._merge_request_assignee_list

    @merge_request_assignee_list.setter
    def merge_request_assignee_list(self, merge_request_assignee_list):
        r"""Sets the merge_request_assignee_list of this CreateMergeRequestResponse.

        合并人列表

        :param merge_request_assignee_list: The merge_request_assignee_list of this CreateMergeRequestResponse.
        :type merge_request_assignee_list: list[:class:`huaweicloudsdkcodehub.v4.UserBasicExternalDto`]
        """
        self._merge_request_assignee_list = merge_request_assignee_list

    @property
    def notes(self):
        r"""Gets the notes of this CreateMergeRequestResponse.

        检视意见

        :return: The notes of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this CreateMergeRequestResponse.

        检视意见

        :param notes: The notes of this CreateMergeRequestResponse.
        :type notes: int
        """
        self._notes = notes

    @property
    def codecheck_state(self):
        r"""Gets the codecheck_state of this CreateMergeRequestResponse.

        代码检查状态

        :return: The codecheck_state of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._codecheck_state

    @codecheck_state.setter
    def codecheck_state(self, codecheck_state):
        r"""Sets the codecheck_state of this CreateMergeRequestResponse.

        代码检查状态

        :param codecheck_state: The codecheck_state of this CreateMergeRequestResponse.
        :type codecheck_state: int
        """
        self._codecheck_state = codecheck_state

    @property
    def codecheck_defect_count(self):
        r"""Gets the codecheck_defect_count of this CreateMergeRequestResponse.

        代码检查问题数

        :return: The codecheck_defect_count of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._codecheck_defect_count

    @codecheck_defect_count.setter
    def codecheck_defect_count(self, codecheck_defect_count):
        r"""Sets the codecheck_defect_count of this CreateMergeRequestResponse.

        代码检查问题数

        :param codecheck_defect_count: The codecheck_defect_count of this CreateMergeRequestResponse.
        :type codecheck_defect_count: int
        """
        self._codecheck_defect_count = codecheck_defect_count

    @property
    def merge_request_related_work_items(self):
        r"""Gets the merge_request_related_work_items of this CreateMergeRequestResponse.

        合并请求关联单数量

        :return: The merge_request_related_work_items of this CreateMergeRequestResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestRelatedWorkItemDto`]
        """
        return self._merge_request_related_work_items

    @merge_request_related_work_items.setter
    def merge_request_related_work_items(self, merge_request_related_work_items):
        r"""Sets the merge_request_related_work_items of this CreateMergeRequestResponse.

        合并请求关联单数量

        :param merge_request_related_work_items: The merge_request_related_work_items of this CreateMergeRequestResponse.
        :type merge_request_related_work_items: list[:class:`huaweicloudsdkcodehub.v4.MergeRequestRelatedWorkItemDto`]
        """
        self._merge_request_related_work_items = merge_request_related_work_items

    @property
    def diverged_commits_count(self):
        r"""Gets the diverged_commits_count of this CreateMergeRequestResponse.

        源分支落后commit数

        :return: The diverged_commits_count of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._diverged_commits_count

    @diverged_commits_count.setter
    def diverged_commits_count(self, diverged_commits_count):
        r"""Sets the diverged_commits_count of this CreateMergeRequestResponse.

        源分支落后commit数

        :param diverged_commits_count: The diverged_commits_count of this CreateMergeRequestResponse.
        :type diverged_commits_count: int
        """
        self._diverged_commits_count = diverged_commits_count

    @property
    def moderation_result(self):
        r"""Gets the moderation_result of this CreateMergeRequestResponse.

        送审结果

        :return: The moderation_result of this CreateMergeRequestResponse.
        :rtype: bool
        """
        return self._moderation_result

    @moderation_result.setter
    def moderation_result(self, moderation_result):
        r"""Sets the moderation_result of this CreateMergeRequestResponse.

        送审结果

        :param moderation_result: The moderation_result of this CreateMergeRequestResponse.
        :type moderation_result: bool
        """
        self._moderation_result = moderation_result

    @property
    def moderation_time(self):
        r"""Gets the moderation_time of this CreateMergeRequestResponse.

        送审时间时间戳

        :return: The moderation_time of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._moderation_time

    @moderation_time.setter
    def moderation_time(self, moderation_time):
        r"""Sets the moderation_time of this CreateMergeRequestResponse.

        送审时间时间戳

        :param moderation_time: The moderation_time of this CreateMergeRequestResponse.
        :type moderation_time: int
        """
        self._moderation_time = moderation_time

    @property
    def moderation_status(self):
        r"""Gets the moderation_status of this CreateMergeRequestResponse.

        送审状态码

        :return: The moderation_status of this CreateMergeRequestResponse.
        :rtype: int
        """
        return self._moderation_status

    @moderation_status.setter
    def moderation_status(self, moderation_status):
        r"""Sets the moderation_status of this CreateMergeRequestResponse.

        送审状态码

        :param moderation_status: The moderation_status of this CreateMergeRequestResponse.
        :type moderation_status: int
        """
        self._moderation_status = moderation_status

    @property
    def is_use_temp_branch(self):
        r"""Gets the is_use_temp_branch of this CreateMergeRequestResponse.

        是否使用临时分支

        :return: The is_use_temp_branch of this CreateMergeRequestResponse.
        :rtype: bool
        """
        return self._is_use_temp_branch

    @is_use_temp_branch.setter
    def is_use_temp_branch(self, is_use_temp_branch):
        r"""Sets the is_use_temp_branch of this CreateMergeRequestResponse.

        是否使用临时分支

        :param is_use_temp_branch: The is_use_temp_branch of this CreateMergeRequestResponse.
        :type is_use_temp_branch: bool
        """
        self._is_use_temp_branch = is_use_temp_branch

    @property
    def approval_merge_request_approvers(self):
        r"""Gets the approval_merge_request_approvers of this CreateMergeRequestResponse.

        审核人

        :return: The approval_merge_request_approvers of this CreateMergeRequestResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ApprovalUserDto`]
        """
        return self._approval_merge_request_approvers

    @approval_merge_request_approvers.setter
    def approval_merge_request_approvers(self, approval_merge_request_approvers):
        r"""Sets the approval_merge_request_approvers of this CreateMergeRequestResponse.

        审核人

        :param approval_merge_request_approvers: The approval_merge_request_approvers of this CreateMergeRequestResponse.
        :type approval_merge_request_approvers: list[:class:`huaweicloudsdkcodehub.v4.ApprovalUserDto`]
        """
        self._approval_merge_request_approvers = approval_merge_request_approvers

    @property
    def review_mode(self):
        r"""Gets the review_mode of this CreateMergeRequestResponse.

        合并请求模式

        :return: The review_mode of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._review_mode

    @review_mode.setter
    def review_mode(self, review_mode):
        r"""Sets the review_mode of this CreateMergeRequestResponse.

        合并请求模式

        :param review_mode: The review_mode of this CreateMergeRequestResponse.
        :type review_mode: str
        """
        self._review_mode = review_mode

    @property
    def squash(self):
        r"""Gets the squash of this CreateMergeRequestResponse.

        squash合入

        :return: The squash of this CreateMergeRequestResponse.
        :rtype: bool
        """
        return self._squash

    @squash.setter
    def squash(self, squash):
        r"""Sets the squash of this CreateMergeRequestResponse.

        squash合入

        :param squash: The squash of this CreateMergeRequestResponse.
        :type squash: bool
        """
        self._squash = squash

    @property
    def squash_commit_message(self):
        r"""Gets the squash_commit_message of this CreateMergeRequestResponse.

        squash提交信息

        :return: The squash_commit_message of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._squash_commit_message

    @squash_commit_message.setter
    def squash_commit_message(self, squash_commit_message):
        r"""Sets the squash_commit_message of this CreateMergeRequestResponse.

        squash提交信息

        :param squash_commit_message: The squash_commit_message of this CreateMergeRequestResponse.
        :type squash_commit_message: str
        """
        self._squash_commit_message = squash_commit_message

    @property
    def rebase_in_progress(self):
        r"""Gets the rebase_in_progress of this CreateMergeRequestResponse.

        是否正在rebase

        :return: The rebase_in_progress of this CreateMergeRequestResponse.
        :rtype: bool
        """
        return self._rebase_in_progress

    @rebase_in_progress.setter
    def rebase_in_progress(self, rebase_in_progress):
        r"""Sets the rebase_in_progress of this CreateMergeRequestResponse.

        是否正在rebase

        :param rebase_in_progress: The rebase_in_progress of this CreateMergeRequestResponse.
        :type rebase_in_progress: bool
        """
        self._rebase_in_progress = rebase_in_progress

    @property
    def source_repository(self):
        r"""Gets the source_repository of this CreateMergeRequestResponse.

        :return: The source_repository of this CreateMergeRequestResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        """
        return self._source_repository

    @source_repository.setter
    def source_repository(self, source_repository):
        r"""Sets the source_repository of this CreateMergeRequestResponse.

        :param source_repository: The source_repository of this CreateMergeRequestResponse.
        :type source_repository: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        """
        self._source_repository = source_repository

    @property
    def target_repository(self):
        r"""Gets the target_repository of this CreateMergeRequestResponse.

        :return: The target_repository of this CreateMergeRequestResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        """
        return self._target_repository

    @target_repository.setter
    def target_repository(self, target_repository):
        r"""Sets the target_repository of this CreateMergeRequestResponse.

        :param target_repository: The target_repository of this CreateMergeRequestResponse.
        :type target_repository: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        """
        self._target_repository = target_repository

    @property
    def is_source_branch_exist(self):
        r"""Gets the is_source_branch_exist of this CreateMergeRequestResponse.

        源分支是否存在

        :return: The is_source_branch_exist of this CreateMergeRequestResponse.
        :rtype: bool
        """
        return self._is_source_branch_exist

    @is_source_branch_exist.setter
    def is_source_branch_exist(self, is_source_branch_exist):
        r"""Sets the is_source_branch_exist of this CreateMergeRequestResponse.

        源分支是否存在

        :param is_source_branch_exist: The is_source_branch_exist of this CreateMergeRequestResponse.
        :type is_source_branch_exist: bool
        """
        self._is_source_branch_exist = is_source_branch_exist

    @property
    def merge_request_type(self):
        r"""Gets the merge_request_type of this CreateMergeRequestResponse.

        合并请求类型

        :return: The merge_request_type of this CreateMergeRequestResponse.
        :rtype: str
        """
        return self._merge_request_type

    @merge_request_type.setter
    def merge_request_type(self, merge_request_type):
        r"""Sets the merge_request_type of this CreateMergeRequestResponse.

        合并请求类型

        :param merge_request_type: The merge_request_type of this CreateMergeRequestResponse.
        :type merge_request_type: str
        """
        self._merge_request_type = merge_request_type

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
        if not isinstance(other, CreateMergeRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
