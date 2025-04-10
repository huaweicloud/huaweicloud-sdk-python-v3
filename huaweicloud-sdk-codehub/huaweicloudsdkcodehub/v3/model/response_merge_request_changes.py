# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseMergeRequestChanges:

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
        'project_id': 'int',
        'title': 'str',
        'description': 'str',
        'state': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'target_branch': 'str',
        'source_branch': 'str',
        'user_notes_count': 'int',
        'upvotes': 'int',
        'downvotes': 'int',
        'author': 'Author',
        'source_project_id': 'int',
        'target_project_id': 'int',
        'labels': 'list[str]',
        'work_in_progress': 'bool',
        'merge_when_pipeline_succeeds': 'bool',
        'merge_status': 'str',
        'sha': 'str',
        'should_remove_source_branch': 'bool',
        'force_remove_source_branch': 'bool',
        'web_url': 'str',
        'squash': 'bool',
        'merge_request_type': 'str',
        'subscribed': 'bool',
        'changes_count': 'str',
        'latest_build_started_at': 'str',
        'latest_build_finished_at': 'str',
        'first_deployed_to_production_at': 'str',
        'pipeline': 'PipelineBasicDto',
        'diff_refs': 'DiffRefsDto',
        'merge_error': 'str',
        'rebase_in_progress': 'bool',
        'diverged_commits_count': 'int',
        'user': 'MergeRequestListDtoUser',
        'added_lines': 'int',
        'removed_lines': 'int',
        'changes': 'list[MergeRequestDiffFileDto]',
        'source_project': 'ProjectSimpleDto'
    }

    attribute_map = {
        'id': 'id',
        'iid': 'iid',
        'project_id': 'project_id',
        'title': 'title',
        'description': 'description',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'target_branch': 'target_branch',
        'source_branch': 'source_branch',
        'user_notes_count': 'user_notes_count',
        'upvotes': 'upvotes',
        'downvotes': 'downvotes',
        'author': 'author',
        'source_project_id': 'source_project_id',
        'target_project_id': 'target_project_id',
        'labels': 'labels',
        'work_in_progress': 'work_in_progress',
        'merge_when_pipeline_succeeds': 'merge_when_pipeline_succeeds',
        'merge_status': 'merge_status',
        'sha': 'sha',
        'should_remove_source_branch': 'should_remove_source_branch',
        'force_remove_source_branch': 'force_remove_source_branch',
        'web_url': 'web_url',
        'squash': 'squash',
        'merge_request_type': 'merge_request_type',
        'subscribed': 'subscribed',
        'changes_count': 'changes_count',
        'latest_build_started_at': 'latest_build_started_at',
        'latest_build_finished_at': 'latest_build_finished_at',
        'first_deployed_to_production_at': 'first_deployed_to_production_at',
        'pipeline': 'pipeline',
        'diff_refs': 'diff_refs',
        'merge_error': 'merge_error',
        'rebase_in_progress': 'rebase_in_progress',
        'diverged_commits_count': 'diverged_commits_count',
        'user': 'user',
        'added_lines': 'added_lines',
        'removed_lines': 'removed_lines',
        'changes': 'changes',
        'source_project': 'source_project'
    }

    def __init__(self, id=None, iid=None, project_id=None, title=None, description=None, state=None, created_at=None, updated_at=None, target_branch=None, source_branch=None, user_notes_count=None, upvotes=None, downvotes=None, author=None, source_project_id=None, target_project_id=None, labels=None, work_in_progress=None, merge_when_pipeline_succeeds=None, merge_status=None, sha=None, should_remove_source_branch=None, force_remove_source_branch=None, web_url=None, squash=None, merge_request_type=None, subscribed=None, changes_count=None, latest_build_started_at=None, latest_build_finished_at=None, first_deployed_to_production_at=None, pipeline=None, diff_refs=None, merge_error=None, rebase_in_progress=None, diverged_commits_count=None, user=None, added_lines=None, removed_lines=None, changes=None, source_project=None):
        r"""ResponseMergeRequestChanges

        The model defined in huaweicloud sdk

        :param id: 合并请求id
        :type id: int
        :param iid: 合并请求iid
        :type iid: int
        :param project_id: 仓库id
        :type project_id: int
        :param title: 合并请求标题
        :type title: str
        :param description: 合并请求描述
        :type description: str
        :param state: 合并请求状态
        :type state: str
        :param created_at: 合并请求创建时间
        :type created_at: str
        :param updated_at: 合并请求更新时间
        :type updated_at: str
        :param target_branch: 合并请求目标分支
        :type target_branch: str
        :param source_branch: 合并请求源分支
        :type source_branch: str
        :param user_notes_count: 检视意见数量
        :type user_notes_count: int
        :param upvotes: upvotes
        :type upvotes: int
        :param downvotes: downvotes
        :type downvotes: int
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v3.Author`
        :param source_project_id: 合并请求源仓库id
        :type source_project_id: int
        :param target_project_id: 合并请求目标仓库id
        :type target_project_id: int
        :param labels: 指定仓库的标签列表
        :type labels: list[str]
        :param work_in_progress: 合并请求是否为wip状态
        :type work_in_progress: bool
        :param merge_when_pipeline_succeeds: 合并请求是否开启流水线成功后自动合入
        :type merge_when_pipeline_succeeds: bool
        :param merge_status: 合并请求合入状态
        :type merge_status: str
        :param sha: 合并请求的head sha
        :type sha: str
        :param should_remove_source_branch: 合并请求合入后是否应该移除源分支
        :type should_remove_source_branch: bool
        :param force_remove_source_branch: 合并请求合入后是否移除源分支
        :type force_remove_source_branch: bool
        :param web_url: 合并请求url
        :type web_url: str
        :param squash: 合并请求是否开启squash合并
        :type squash: bool
        :param merge_request_type: 合并请求类型
        :type merge_request_type: str
        :param subscribed: 是否订阅
        :type subscribed: bool
        :param changes_count: 合并请求变更文件数量
        :type changes_count: str
        :param latest_build_started_at: 合并请求最新构建开始时间
        :type latest_build_started_at: str
        :param latest_build_finished_at: 合并请求最新构建结束时间
        :type latest_build_finished_at: str
        :param first_deployed_to_production_at: first deployed to production at
        :type first_deployed_to_production_at: str
        :param pipeline: 
        :type pipeline: :class:`huaweicloudsdkcodehub.v3.PipelineBasicDto`
        :param diff_refs: 
        :type diff_refs: :class:`huaweicloudsdkcodehub.v3.DiffRefsDto`
        :param merge_error: 合并请求操作错误信息
        :type merge_error: str
        :param rebase_in_progress: 合并请求是否rebase中
        :type rebase_in_progress: bool
        :param diverged_commits_count: 合并请求落后提交数量
        :type diverged_commits_count: int
        :param user: 
        :type user: :class:`huaweicloudsdkcodehub.v3.MergeRequestListDtoUser`
        :param added_lines: 合并请求增加行数
        :type added_lines: int
        :param removed_lines: 合并请求删除行数
        :type removed_lines: int
        :param changes: 合并请求文件变更
        :type changes: list[:class:`huaweicloudsdkcodehub.v3.MergeRequestDiffFileDto`]
        :param source_project: 
        :type source_project: :class:`huaweicloudsdkcodehub.v3.ProjectSimpleDto`
        """
        
        

        self._id = None
        self._iid = None
        self._project_id = None
        self._title = None
        self._description = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._target_branch = None
        self._source_branch = None
        self._user_notes_count = None
        self._upvotes = None
        self._downvotes = None
        self._author = None
        self._source_project_id = None
        self._target_project_id = None
        self._labels = None
        self._work_in_progress = None
        self._merge_when_pipeline_succeeds = None
        self._merge_status = None
        self._sha = None
        self._should_remove_source_branch = None
        self._force_remove_source_branch = None
        self._web_url = None
        self._squash = None
        self._merge_request_type = None
        self._subscribed = None
        self._changes_count = None
        self._latest_build_started_at = None
        self._latest_build_finished_at = None
        self._first_deployed_to_production_at = None
        self._pipeline = None
        self._diff_refs = None
        self._merge_error = None
        self._rebase_in_progress = None
        self._diverged_commits_count = None
        self._user = None
        self._added_lines = None
        self._removed_lines = None
        self._changes = None
        self._source_project = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if iid is not None:
            self.iid = iid
        if project_id is not None:
            self.project_id = project_id
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
        if target_branch is not None:
            self.target_branch = target_branch
        if source_branch is not None:
            self.source_branch = source_branch
        if user_notes_count is not None:
            self.user_notes_count = user_notes_count
        if upvotes is not None:
            self.upvotes = upvotes
        if downvotes is not None:
            self.downvotes = downvotes
        if author is not None:
            self.author = author
        if source_project_id is not None:
            self.source_project_id = source_project_id
        if target_project_id is not None:
            self.target_project_id = target_project_id
        if labels is not None:
            self.labels = labels
        if work_in_progress is not None:
            self.work_in_progress = work_in_progress
        if merge_when_pipeline_succeeds is not None:
            self.merge_when_pipeline_succeeds = merge_when_pipeline_succeeds
        if merge_status is not None:
            self.merge_status = merge_status
        if sha is not None:
            self.sha = sha
        if should_remove_source_branch is not None:
            self.should_remove_source_branch = should_remove_source_branch
        if force_remove_source_branch is not None:
            self.force_remove_source_branch = force_remove_source_branch
        if web_url is not None:
            self.web_url = web_url
        if squash is not None:
            self.squash = squash
        if merge_request_type is not None:
            self.merge_request_type = merge_request_type
        if subscribed is not None:
            self.subscribed = subscribed
        if changes_count is not None:
            self.changes_count = changes_count
        if latest_build_started_at is not None:
            self.latest_build_started_at = latest_build_started_at
        if latest_build_finished_at is not None:
            self.latest_build_finished_at = latest_build_finished_at
        if first_deployed_to_production_at is not None:
            self.first_deployed_to_production_at = first_deployed_to_production_at
        if pipeline is not None:
            self.pipeline = pipeline
        if diff_refs is not None:
            self.diff_refs = diff_refs
        if merge_error is not None:
            self.merge_error = merge_error
        if rebase_in_progress is not None:
            self.rebase_in_progress = rebase_in_progress
        if diverged_commits_count is not None:
            self.diverged_commits_count = diverged_commits_count
        if user is not None:
            self.user = user
        if added_lines is not None:
            self.added_lines = added_lines
        if removed_lines is not None:
            self.removed_lines = removed_lines
        if changes is not None:
            self.changes = changes
        if source_project is not None:
            self.source_project = source_project

    @property
    def id(self):
        r"""Gets the id of this ResponseMergeRequestChanges.

        合并请求id

        :return: The id of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResponseMergeRequestChanges.

        合并请求id

        :param id: The id of this ResponseMergeRequestChanges.
        :type id: int
        """
        self._id = id

    @property
    def iid(self):
        r"""Gets the iid of this ResponseMergeRequestChanges.

        合并请求iid

        :return: The iid of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._iid

    @iid.setter
    def iid(self, iid):
        r"""Sets the iid of this ResponseMergeRequestChanges.

        合并请求iid

        :param iid: The iid of this ResponseMergeRequestChanges.
        :type iid: int
        """
        self._iid = iid

    @property
    def project_id(self):
        r"""Gets the project_id of this ResponseMergeRequestChanges.

        仓库id

        :return: The project_id of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ResponseMergeRequestChanges.

        仓库id

        :param project_id: The project_id of this ResponseMergeRequestChanges.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def title(self):
        r"""Gets the title of this ResponseMergeRequestChanges.

        合并请求标题

        :return: The title of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ResponseMergeRequestChanges.

        合并请求标题

        :param title: The title of this ResponseMergeRequestChanges.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this ResponseMergeRequestChanges.

        合并请求描述

        :return: The description of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ResponseMergeRequestChanges.

        合并请求描述

        :param description: The description of this ResponseMergeRequestChanges.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        r"""Gets the state of this ResponseMergeRequestChanges.

        合并请求状态

        :return: The state of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ResponseMergeRequestChanges.

        合并请求状态

        :param state: The state of this ResponseMergeRequestChanges.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this ResponseMergeRequestChanges.

        合并请求创建时间

        :return: The created_at of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ResponseMergeRequestChanges.

        合并请求创建时间

        :param created_at: The created_at of this ResponseMergeRequestChanges.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ResponseMergeRequestChanges.

        合并请求更新时间

        :return: The updated_at of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ResponseMergeRequestChanges.

        合并请求更新时间

        :param updated_at: The updated_at of this ResponseMergeRequestChanges.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def target_branch(self):
        r"""Gets the target_branch of this ResponseMergeRequestChanges.

        合并请求目标分支

        :return: The target_branch of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this ResponseMergeRequestChanges.

        合并请求目标分支

        :param target_branch: The target_branch of this ResponseMergeRequestChanges.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def source_branch(self):
        r"""Gets the source_branch of this ResponseMergeRequestChanges.

        合并请求源分支

        :return: The source_branch of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this ResponseMergeRequestChanges.

        合并请求源分支

        :param source_branch: The source_branch of this ResponseMergeRequestChanges.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def user_notes_count(self):
        r"""Gets the user_notes_count of this ResponseMergeRequestChanges.

        检视意见数量

        :return: The user_notes_count of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._user_notes_count

    @user_notes_count.setter
    def user_notes_count(self, user_notes_count):
        r"""Sets the user_notes_count of this ResponseMergeRequestChanges.

        检视意见数量

        :param user_notes_count: The user_notes_count of this ResponseMergeRequestChanges.
        :type user_notes_count: int
        """
        self._user_notes_count = user_notes_count

    @property
    def upvotes(self):
        r"""Gets the upvotes of this ResponseMergeRequestChanges.

        upvotes

        :return: The upvotes of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._upvotes

    @upvotes.setter
    def upvotes(self, upvotes):
        r"""Sets the upvotes of this ResponseMergeRequestChanges.

        upvotes

        :param upvotes: The upvotes of this ResponseMergeRequestChanges.
        :type upvotes: int
        """
        self._upvotes = upvotes

    @property
    def downvotes(self):
        r"""Gets the downvotes of this ResponseMergeRequestChanges.

        downvotes

        :return: The downvotes of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._downvotes

    @downvotes.setter
    def downvotes(self, downvotes):
        r"""Sets the downvotes of this ResponseMergeRequestChanges.

        downvotes

        :param downvotes: The downvotes of this ResponseMergeRequestChanges.
        :type downvotes: int
        """
        self._downvotes = downvotes

    @property
    def author(self):
        r"""Gets the author of this ResponseMergeRequestChanges.

        :return: The author of this ResponseMergeRequestChanges.
        :rtype: :class:`huaweicloudsdkcodehub.v3.Author`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this ResponseMergeRequestChanges.

        :param author: The author of this ResponseMergeRequestChanges.
        :type author: :class:`huaweicloudsdkcodehub.v3.Author`
        """
        self._author = author

    @property
    def source_project_id(self):
        r"""Gets the source_project_id of this ResponseMergeRequestChanges.

        合并请求源仓库id

        :return: The source_project_id of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._source_project_id

    @source_project_id.setter
    def source_project_id(self, source_project_id):
        r"""Sets the source_project_id of this ResponseMergeRequestChanges.

        合并请求源仓库id

        :param source_project_id: The source_project_id of this ResponseMergeRequestChanges.
        :type source_project_id: int
        """
        self._source_project_id = source_project_id

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this ResponseMergeRequestChanges.

        合并请求目标仓库id

        :return: The target_project_id of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this ResponseMergeRequestChanges.

        合并请求目标仓库id

        :param target_project_id: The target_project_id of this ResponseMergeRequestChanges.
        :type target_project_id: int
        """
        self._target_project_id = target_project_id

    @property
    def labels(self):
        r"""Gets the labels of this ResponseMergeRequestChanges.

        指定仓库的标签列表

        :return: The labels of this ResponseMergeRequestChanges.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ResponseMergeRequestChanges.

        指定仓库的标签列表

        :param labels: The labels of this ResponseMergeRequestChanges.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def work_in_progress(self):
        r"""Gets the work_in_progress of this ResponseMergeRequestChanges.

        合并请求是否为wip状态

        :return: The work_in_progress of this ResponseMergeRequestChanges.
        :rtype: bool
        """
        return self._work_in_progress

    @work_in_progress.setter
    def work_in_progress(self, work_in_progress):
        r"""Sets the work_in_progress of this ResponseMergeRequestChanges.

        合并请求是否为wip状态

        :param work_in_progress: The work_in_progress of this ResponseMergeRequestChanges.
        :type work_in_progress: bool
        """
        self._work_in_progress = work_in_progress

    @property
    def merge_when_pipeline_succeeds(self):
        r"""Gets the merge_when_pipeline_succeeds of this ResponseMergeRequestChanges.

        合并请求是否开启流水线成功后自动合入

        :return: The merge_when_pipeline_succeeds of this ResponseMergeRequestChanges.
        :rtype: bool
        """
        return self._merge_when_pipeline_succeeds

    @merge_when_pipeline_succeeds.setter
    def merge_when_pipeline_succeeds(self, merge_when_pipeline_succeeds):
        r"""Sets the merge_when_pipeline_succeeds of this ResponseMergeRequestChanges.

        合并请求是否开启流水线成功后自动合入

        :param merge_when_pipeline_succeeds: The merge_when_pipeline_succeeds of this ResponseMergeRequestChanges.
        :type merge_when_pipeline_succeeds: bool
        """
        self._merge_when_pipeline_succeeds = merge_when_pipeline_succeeds

    @property
    def merge_status(self):
        r"""Gets the merge_status of this ResponseMergeRequestChanges.

        合并请求合入状态

        :return: The merge_status of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._merge_status

    @merge_status.setter
    def merge_status(self, merge_status):
        r"""Sets the merge_status of this ResponseMergeRequestChanges.

        合并请求合入状态

        :param merge_status: The merge_status of this ResponseMergeRequestChanges.
        :type merge_status: str
        """
        self._merge_status = merge_status

    @property
    def sha(self):
        r"""Gets the sha of this ResponseMergeRequestChanges.

        合并请求的head sha

        :return: The sha of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        r"""Sets the sha of this ResponseMergeRequestChanges.

        合并请求的head sha

        :param sha: The sha of this ResponseMergeRequestChanges.
        :type sha: str
        """
        self._sha = sha

    @property
    def should_remove_source_branch(self):
        r"""Gets the should_remove_source_branch of this ResponseMergeRequestChanges.

        合并请求合入后是否应该移除源分支

        :return: The should_remove_source_branch of this ResponseMergeRequestChanges.
        :rtype: bool
        """
        return self._should_remove_source_branch

    @should_remove_source_branch.setter
    def should_remove_source_branch(self, should_remove_source_branch):
        r"""Sets the should_remove_source_branch of this ResponseMergeRequestChanges.

        合并请求合入后是否应该移除源分支

        :param should_remove_source_branch: The should_remove_source_branch of this ResponseMergeRequestChanges.
        :type should_remove_source_branch: bool
        """
        self._should_remove_source_branch = should_remove_source_branch

    @property
    def force_remove_source_branch(self):
        r"""Gets the force_remove_source_branch of this ResponseMergeRequestChanges.

        合并请求合入后是否移除源分支

        :return: The force_remove_source_branch of this ResponseMergeRequestChanges.
        :rtype: bool
        """
        return self._force_remove_source_branch

    @force_remove_source_branch.setter
    def force_remove_source_branch(self, force_remove_source_branch):
        r"""Sets the force_remove_source_branch of this ResponseMergeRequestChanges.

        合并请求合入后是否移除源分支

        :param force_remove_source_branch: The force_remove_source_branch of this ResponseMergeRequestChanges.
        :type force_remove_source_branch: bool
        """
        self._force_remove_source_branch = force_remove_source_branch

    @property
    def web_url(self):
        r"""Gets the web_url of this ResponseMergeRequestChanges.

        合并请求url

        :return: The web_url of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this ResponseMergeRequestChanges.

        合并请求url

        :param web_url: The web_url of this ResponseMergeRequestChanges.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def squash(self):
        r"""Gets the squash of this ResponseMergeRequestChanges.

        合并请求是否开启squash合并

        :return: The squash of this ResponseMergeRequestChanges.
        :rtype: bool
        """
        return self._squash

    @squash.setter
    def squash(self, squash):
        r"""Sets the squash of this ResponseMergeRequestChanges.

        合并请求是否开启squash合并

        :param squash: The squash of this ResponseMergeRequestChanges.
        :type squash: bool
        """
        self._squash = squash

    @property
    def merge_request_type(self):
        r"""Gets the merge_request_type of this ResponseMergeRequestChanges.

        合并请求类型

        :return: The merge_request_type of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._merge_request_type

    @merge_request_type.setter
    def merge_request_type(self, merge_request_type):
        r"""Sets the merge_request_type of this ResponseMergeRequestChanges.

        合并请求类型

        :param merge_request_type: The merge_request_type of this ResponseMergeRequestChanges.
        :type merge_request_type: str
        """
        self._merge_request_type = merge_request_type

    @property
    def subscribed(self):
        r"""Gets the subscribed of this ResponseMergeRequestChanges.

        是否订阅

        :return: The subscribed of this ResponseMergeRequestChanges.
        :rtype: bool
        """
        return self._subscribed

    @subscribed.setter
    def subscribed(self, subscribed):
        r"""Sets the subscribed of this ResponseMergeRequestChanges.

        是否订阅

        :param subscribed: The subscribed of this ResponseMergeRequestChanges.
        :type subscribed: bool
        """
        self._subscribed = subscribed

    @property
    def changes_count(self):
        r"""Gets the changes_count of this ResponseMergeRequestChanges.

        合并请求变更文件数量

        :return: The changes_count of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._changes_count

    @changes_count.setter
    def changes_count(self, changes_count):
        r"""Sets the changes_count of this ResponseMergeRequestChanges.

        合并请求变更文件数量

        :param changes_count: The changes_count of this ResponseMergeRequestChanges.
        :type changes_count: str
        """
        self._changes_count = changes_count

    @property
    def latest_build_started_at(self):
        r"""Gets the latest_build_started_at of this ResponseMergeRequestChanges.

        合并请求最新构建开始时间

        :return: The latest_build_started_at of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._latest_build_started_at

    @latest_build_started_at.setter
    def latest_build_started_at(self, latest_build_started_at):
        r"""Sets the latest_build_started_at of this ResponseMergeRequestChanges.

        合并请求最新构建开始时间

        :param latest_build_started_at: The latest_build_started_at of this ResponseMergeRequestChanges.
        :type latest_build_started_at: str
        """
        self._latest_build_started_at = latest_build_started_at

    @property
    def latest_build_finished_at(self):
        r"""Gets the latest_build_finished_at of this ResponseMergeRequestChanges.

        合并请求最新构建结束时间

        :return: The latest_build_finished_at of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._latest_build_finished_at

    @latest_build_finished_at.setter
    def latest_build_finished_at(self, latest_build_finished_at):
        r"""Sets the latest_build_finished_at of this ResponseMergeRequestChanges.

        合并请求最新构建结束时间

        :param latest_build_finished_at: The latest_build_finished_at of this ResponseMergeRequestChanges.
        :type latest_build_finished_at: str
        """
        self._latest_build_finished_at = latest_build_finished_at

    @property
    def first_deployed_to_production_at(self):
        r"""Gets the first_deployed_to_production_at of this ResponseMergeRequestChanges.

        first deployed to production at

        :return: The first_deployed_to_production_at of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._first_deployed_to_production_at

    @first_deployed_to_production_at.setter
    def first_deployed_to_production_at(self, first_deployed_to_production_at):
        r"""Sets the first_deployed_to_production_at of this ResponseMergeRequestChanges.

        first deployed to production at

        :param first_deployed_to_production_at: The first_deployed_to_production_at of this ResponseMergeRequestChanges.
        :type first_deployed_to_production_at: str
        """
        self._first_deployed_to_production_at = first_deployed_to_production_at

    @property
    def pipeline(self):
        r"""Gets the pipeline of this ResponseMergeRequestChanges.

        :return: The pipeline of this ResponseMergeRequestChanges.
        :rtype: :class:`huaweicloudsdkcodehub.v3.PipelineBasicDto`
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        r"""Sets the pipeline of this ResponseMergeRequestChanges.

        :param pipeline: The pipeline of this ResponseMergeRequestChanges.
        :type pipeline: :class:`huaweicloudsdkcodehub.v3.PipelineBasicDto`
        """
        self._pipeline = pipeline

    @property
    def diff_refs(self):
        r"""Gets the diff_refs of this ResponseMergeRequestChanges.

        :return: The diff_refs of this ResponseMergeRequestChanges.
        :rtype: :class:`huaweicloudsdkcodehub.v3.DiffRefsDto`
        """
        return self._diff_refs

    @diff_refs.setter
    def diff_refs(self, diff_refs):
        r"""Sets the diff_refs of this ResponseMergeRequestChanges.

        :param diff_refs: The diff_refs of this ResponseMergeRequestChanges.
        :type diff_refs: :class:`huaweicloudsdkcodehub.v3.DiffRefsDto`
        """
        self._diff_refs = diff_refs

    @property
    def merge_error(self):
        r"""Gets the merge_error of this ResponseMergeRequestChanges.

        合并请求操作错误信息

        :return: The merge_error of this ResponseMergeRequestChanges.
        :rtype: str
        """
        return self._merge_error

    @merge_error.setter
    def merge_error(self, merge_error):
        r"""Sets the merge_error of this ResponseMergeRequestChanges.

        合并请求操作错误信息

        :param merge_error: The merge_error of this ResponseMergeRequestChanges.
        :type merge_error: str
        """
        self._merge_error = merge_error

    @property
    def rebase_in_progress(self):
        r"""Gets the rebase_in_progress of this ResponseMergeRequestChanges.

        合并请求是否rebase中

        :return: The rebase_in_progress of this ResponseMergeRequestChanges.
        :rtype: bool
        """
        return self._rebase_in_progress

    @rebase_in_progress.setter
    def rebase_in_progress(self, rebase_in_progress):
        r"""Sets the rebase_in_progress of this ResponseMergeRequestChanges.

        合并请求是否rebase中

        :param rebase_in_progress: The rebase_in_progress of this ResponseMergeRequestChanges.
        :type rebase_in_progress: bool
        """
        self._rebase_in_progress = rebase_in_progress

    @property
    def diverged_commits_count(self):
        r"""Gets the diverged_commits_count of this ResponseMergeRequestChanges.

        合并请求落后提交数量

        :return: The diverged_commits_count of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._diverged_commits_count

    @diverged_commits_count.setter
    def diverged_commits_count(self, diverged_commits_count):
        r"""Sets the diverged_commits_count of this ResponseMergeRequestChanges.

        合并请求落后提交数量

        :param diverged_commits_count: The diverged_commits_count of this ResponseMergeRequestChanges.
        :type diverged_commits_count: int
        """
        self._diverged_commits_count = diverged_commits_count

    @property
    def user(self):
        r"""Gets the user of this ResponseMergeRequestChanges.

        :return: The user of this ResponseMergeRequestChanges.
        :rtype: :class:`huaweicloudsdkcodehub.v3.MergeRequestListDtoUser`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ResponseMergeRequestChanges.

        :param user: The user of this ResponseMergeRequestChanges.
        :type user: :class:`huaweicloudsdkcodehub.v3.MergeRequestListDtoUser`
        """
        self._user = user

    @property
    def added_lines(self):
        r"""Gets the added_lines of this ResponseMergeRequestChanges.

        合并请求增加行数

        :return: The added_lines of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._added_lines

    @added_lines.setter
    def added_lines(self, added_lines):
        r"""Sets the added_lines of this ResponseMergeRequestChanges.

        合并请求增加行数

        :param added_lines: The added_lines of this ResponseMergeRequestChanges.
        :type added_lines: int
        """
        self._added_lines = added_lines

    @property
    def removed_lines(self):
        r"""Gets the removed_lines of this ResponseMergeRequestChanges.

        合并请求删除行数

        :return: The removed_lines of this ResponseMergeRequestChanges.
        :rtype: int
        """
        return self._removed_lines

    @removed_lines.setter
    def removed_lines(self, removed_lines):
        r"""Sets the removed_lines of this ResponseMergeRequestChanges.

        合并请求删除行数

        :param removed_lines: The removed_lines of this ResponseMergeRequestChanges.
        :type removed_lines: int
        """
        self._removed_lines = removed_lines

    @property
    def changes(self):
        r"""Gets the changes of this ResponseMergeRequestChanges.

        合并请求文件变更

        :return: The changes of this ResponseMergeRequestChanges.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.MergeRequestDiffFileDto`]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        r"""Sets the changes of this ResponseMergeRequestChanges.

        合并请求文件变更

        :param changes: The changes of this ResponseMergeRequestChanges.
        :type changes: list[:class:`huaweicloudsdkcodehub.v3.MergeRequestDiffFileDto`]
        """
        self._changes = changes

    @property
    def source_project(self):
        r"""Gets the source_project of this ResponseMergeRequestChanges.

        :return: The source_project of this ResponseMergeRequestChanges.
        :rtype: :class:`huaweicloudsdkcodehub.v3.ProjectSimpleDto`
        """
        return self._source_project

    @source_project.setter
    def source_project(self, source_project):
        r"""Sets the source_project of this ResponseMergeRequestChanges.

        :param source_project: The source_project of this ResponseMergeRequestChanges.
        :type source_project: :class:`huaweicloudsdkcodehub.v3.ProjectSimpleDto`
        """
        self._source_project = source_project

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
        if not isinstance(other, ResponseMergeRequestChanges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
