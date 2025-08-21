# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitMergeRequestDto:

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
        'title': 'str',
        'description': 'str',
        'state': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'merged_by': 'UserBasicDto',
        'merged_at': 'str',
        'closed_by': 'UserBasicDto',
        'closed_at': 'str',
        'target_branch': 'str',
        'source_branch': 'str',
        'user_notes_count': 'int',
        'upvotes': 'int',
        'downvotes': 'int',
        'author': 'UserBasicDto',
        'assignee': 'list[UserBasicDto]',
        'source_repository_id': 'int',
        'target_repository_id': 'int',
        'labels': 'list[str]',
        'work_in_progress': 'bool',
        'milestone': 'MilestoneBasicDto',
        'merge_when_pipeline_succeeds': 'bool',
        'merge_status': 'str',
        'sha': 'str',
        'merge_commit_sha': 'str',
        'discussion_locked': 'bool',
        'force_remove_source_branch': 'bool',
        'should_remove_source_branch': 'bool',
        'allow_collaboration': 'bool',
        'allow_maintainer_to_push': 'bool',
        'web_url': 'str',
        'time_stats': 'IssuableTimeStatsDto',
        'squash': 'bool',
        'merge_request_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'iid': 'iid',
        'title': 'title',
        'description': 'description',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'merged_by': 'merged_by',
        'merged_at': 'merged_at',
        'closed_by': 'closed_by',
        'closed_at': 'closed_at',
        'target_branch': 'target_branch',
        'source_branch': 'source_branch',
        'user_notes_count': 'user_notes_count',
        'upvotes': 'upvotes',
        'downvotes': 'downvotes',
        'author': 'author',
        'assignee': 'assignee',
        'source_repository_id': 'source_repository_id',
        'target_repository_id': 'target_repository_id',
        'labels': 'labels',
        'work_in_progress': 'work_in_progress',
        'milestone': 'milestone',
        'merge_when_pipeline_succeeds': 'merge_when_pipeline_succeeds',
        'merge_status': 'merge_status',
        'sha': 'sha',
        'merge_commit_sha': 'merge_commit_sha',
        'discussion_locked': 'discussion_locked',
        'force_remove_source_branch': 'force_remove_source_branch',
        'should_remove_source_branch': 'should_remove_source_branch',
        'allow_collaboration': 'allow_collaboration',
        'allow_maintainer_to_push': 'allow_maintainer_to_push',
        'web_url': 'web_url',
        'time_stats': 'time_stats',
        'squash': 'squash',
        'merge_request_type': 'merge_request_type'
    }

    def __init__(self, id=None, iid=None, title=None, description=None, state=None, created_at=None, updated_at=None, merged_by=None, merged_at=None, closed_by=None, closed_at=None, target_branch=None, source_branch=None, user_notes_count=None, upvotes=None, downvotes=None, author=None, assignee=None, source_repository_id=None, target_repository_id=None, labels=None, work_in_progress=None, milestone=None, merge_when_pipeline_succeeds=None, merge_status=None, sha=None, merge_commit_sha=None, discussion_locked=None, force_remove_source_branch=None, should_remove_source_branch=None, allow_collaboration=None, allow_maintainer_to_push=None, web_url=None, time_stats=None, squash=None, merge_request_type=None):
        r"""CommitMergeRequestDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 合并请求的ID。
        :type id: int
        :param iid: **参数解释：** 合并请求的序号。
        :type iid: int
        :param title: **参数解释：** 合并请求的标题。
        :type title: str
        :param description: **参数解释：** 合并请求的详细描述。
        :type description: str
        :param state: **参数解释：** 合并请求的状态。
        :type state: str
        :param created_at: **参数解释：** 合并请求创建的时间。
        :type created_at: str
        :param updated_at: **参数解释：** 合并请求最后一次更新的时间。
        :type updated_at: str
        :param merged_by: 
        :type merged_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param merged_at: **参数解释：** 合并请求被合并的时间。
        :type merged_at: str
        :param closed_by: 
        :type closed_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param closed_at: **参数解释：** 合并请求被关闭的时间。
        :type closed_at: str
        :param target_branch: **参数解释：** 合并请求的目标分支名称。
        :type target_branch: str
        :param source_branch: **参数解释：** 合并请求的源分支名称。
        :type source_branch: str
        :param user_notes_count: **参数解释：** 合并请求中检视意见的数量。
        :type user_notes_count: int
        :param upvotes: **参数解释：** 合并请求的正向评分数量。
        :type upvotes: int
        :param downvotes: **参数解释：** 合并请求的负向评分数量。
        :type downvotes: int
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param assignee: **参数解释：** 合并请求的可合并人列表。
        :type assignee: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        :param source_repository_id: **参数解释：** 源仓库的唯一标识符。
        :type source_repository_id: int
        :param target_repository_id: **参数解释：** 目标仓库的唯一标识符。
        :type target_repository_id: int
        :param labels: **参数解释：** 合并请求关联的标签列表。
        :type labels: list[str]
        :param work_in_progress: **参数解释：** 表示合并请求是否处于“工作进行中”状态。
        :type work_in_progress: bool
        :param milestone: 
        :type milestone: :class:`huaweicloudsdkcodehub.v4.MilestoneBasicDto`
        :param merge_when_pipeline_succeeds: **参数解释：** 表示是否在CI/CD管道成功时自动合并请求。
        :type merge_when_pipeline_succeeds: bool
        :param merge_status: **参数解释：** 合并请求的合并状态。
        :type merge_status: str
        :param sha: **参数解释：** 合并请求的提交哈希值。
        :type sha: str
        :param merge_commit_sha: **参数解释：** 合并提交的哈希值。
        :type merge_commit_sha: str
        :param discussion_locked: **参数解释：** 表示合并请求的讨论是否被锁定。
        :type discussion_locked: bool
        :param force_remove_source_branch: **参数解释：** 表示是否强制删除源分支。
        :type force_remove_source_branch: bool
        :param should_remove_source_branch: **参数解释：** 表示是否应该删除源分支。
        :type should_remove_source_branch: bool
        :param allow_collaboration: **参数解释：** 表示是否允许协作者参与。
        :type allow_collaboration: bool
        :param allow_maintainer_to_push: **参数解释：** 表示是否允许维护者推送代码。
        :type allow_maintainer_to_push: bool
        :param web_url: **参数解释：** 合并请求的网页URL链接。
        :type web_url: str
        :param time_stats: 
        :type time_stats: :class:`huaweicloudsdkcodehub.v4.IssuableTimeStatsDto`
        :param squash: **参数解释：** 表示是否在合并时将提交压缩为一个。
        :type squash: bool
        :param merge_request_type: **参数解释：** 合并请求的类型。
        :type merge_request_type: str
        """
        
        

        self._id = None
        self._iid = None
        self._title = None
        self._description = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._merged_by = None
        self._merged_at = None
        self._closed_by = None
        self._closed_at = None
        self._target_branch = None
        self._source_branch = None
        self._user_notes_count = None
        self._upvotes = None
        self._downvotes = None
        self._author = None
        self._assignee = None
        self._source_repository_id = None
        self._target_repository_id = None
        self._labels = None
        self._work_in_progress = None
        self._milestone = None
        self._merge_when_pipeline_succeeds = None
        self._merge_status = None
        self._sha = None
        self._merge_commit_sha = None
        self._discussion_locked = None
        self._force_remove_source_branch = None
        self._should_remove_source_branch = None
        self._allow_collaboration = None
        self._allow_maintainer_to_push = None
        self._web_url = None
        self._time_stats = None
        self._squash = None
        self._merge_request_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if iid is not None:
            self.iid = iid
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
        if merged_by is not None:
            self.merged_by = merged_by
        if merged_at is not None:
            self.merged_at = merged_at
        if closed_by is not None:
            self.closed_by = closed_by
        if closed_at is not None:
            self.closed_at = closed_at
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
        if assignee is not None:
            self.assignee = assignee
        if source_repository_id is not None:
            self.source_repository_id = source_repository_id
        if target_repository_id is not None:
            self.target_repository_id = target_repository_id
        if labels is not None:
            self.labels = labels
        if work_in_progress is not None:
            self.work_in_progress = work_in_progress
        if milestone is not None:
            self.milestone = milestone
        if merge_when_pipeline_succeeds is not None:
            self.merge_when_pipeline_succeeds = merge_when_pipeline_succeeds
        if merge_status is not None:
            self.merge_status = merge_status
        if sha is not None:
            self.sha = sha
        if merge_commit_sha is not None:
            self.merge_commit_sha = merge_commit_sha
        if discussion_locked is not None:
            self.discussion_locked = discussion_locked
        if force_remove_source_branch is not None:
            self.force_remove_source_branch = force_remove_source_branch
        if should_remove_source_branch is not None:
            self.should_remove_source_branch = should_remove_source_branch
        if allow_collaboration is not None:
            self.allow_collaboration = allow_collaboration
        if allow_maintainer_to_push is not None:
            self.allow_maintainer_to_push = allow_maintainer_to_push
        if web_url is not None:
            self.web_url = web_url
        if time_stats is not None:
            self.time_stats = time_stats
        if squash is not None:
            self.squash = squash
        if merge_request_type is not None:
            self.merge_request_type = merge_request_type

    @property
    def id(self):
        r"""Gets the id of this CommitMergeRequestDto.

        **参数解释：** 合并请求的ID。

        :return: The id of this CommitMergeRequestDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CommitMergeRequestDto.

        **参数解释：** 合并请求的ID。

        :param id: The id of this CommitMergeRequestDto.
        :type id: int
        """
        self._id = id

    @property
    def iid(self):
        r"""Gets the iid of this CommitMergeRequestDto.

        **参数解释：** 合并请求的序号。

        :return: The iid of this CommitMergeRequestDto.
        :rtype: int
        """
        return self._iid

    @iid.setter
    def iid(self, iid):
        r"""Sets the iid of this CommitMergeRequestDto.

        **参数解释：** 合并请求的序号。

        :param iid: The iid of this CommitMergeRequestDto.
        :type iid: int
        """
        self._iid = iid

    @property
    def title(self):
        r"""Gets the title of this CommitMergeRequestDto.

        **参数解释：** 合并请求的标题。

        :return: The title of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CommitMergeRequestDto.

        **参数解释：** 合并请求的标题。

        :param title: The title of this CommitMergeRequestDto.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this CommitMergeRequestDto.

        **参数解释：** 合并请求的详细描述。

        :return: The description of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CommitMergeRequestDto.

        **参数解释：** 合并请求的详细描述。

        :param description: The description of this CommitMergeRequestDto.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        r"""Gets the state of this CommitMergeRequestDto.

        **参数解释：** 合并请求的状态。

        :return: The state of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CommitMergeRequestDto.

        **参数解释：** 合并请求的状态。

        :param state: The state of this CommitMergeRequestDto.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this CommitMergeRequestDto.

        **参数解释：** 合并请求创建的时间。

        :return: The created_at of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CommitMergeRequestDto.

        **参数解释：** 合并请求创建的时间。

        :param created_at: The created_at of this CommitMergeRequestDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CommitMergeRequestDto.

        **参数解释：** 合并请求最后一次更新的时间。

        :return: The updated_at of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CommitMergeRequestDto.

        **参数解释：** 合并请求最后一次更新的时间。

        :param updated_at: The updated_at of this CommitMergeRequestDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def merged_by(self):
        r"""Gets the merged_by of this CommitMergeRequestDto.

        :return: The merged_by of this CommitMergeRequestDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._merged_by

    @merged_by.setter
    def merged_by(self, merged_by):
        r"""Sets the merged_by of this CommitMergeRequestDto.

        :param merged_by: The merged_by of this CommitMergeRequestDto.
        :type merged_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._merged_by = merged_by

    @property
    def merged_at(self):
        r"""Gets the merged_at of this CommitMergeRequestDto.

        **参数解释：** 合并请求被合并的时间。

        :return: The merged_at of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._merged_at

    @merged_at.setter
    def merged_at(self, merged_at):
        r"""Sets the merged_at of this CommitMergeRequestDto.

        **参数解释：** 合并请求被合并的时间。

        :param merged_at: The merged_at of this CommitMergeRequestDto.
        :type merged_at: str
        """
        self._merged_at = merged_at

    @property
    def closed_by(self):
        r"""Gets the closed_by of this CommitMergeRequestDto.

        :return: The closed_by of this CommitMergeRequestDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._closed_by

    @closed_by.setter
    def closed_by(self, closed_by):
        r"""Sets the closed_by of this CommitMergeRequestDto.

        :param closed_by: The closed_by of this CommitMergeRequestDto.
        :type closed_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._closed_by = closed_by

    @property
    def closed_at(self):
        r"""Gets the closed_at of this CommitMergeRequestDto.

        **参数解释：** 合并请求被关闭的时间。

        :return: The closed_at of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        r"""Sets the closed_at of this CommitMergeRequestDto.

        **参数解释：** 合并请求被关闭的时间。

        :param closed_at: The closed_at of this CommitMergeRequestDto.
        :type closed_at: str
        """
        self._closed_at = closed_at

    @property
    def target_branch(self):
        r"""Gets the target_branch of this CommitMergeRequestDto.

        **参数解释：** 合并请求的目标分支名称。

        :return: The target_branch of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this CommitMergeRequestDto.

        **参数解释：** 合并请求的目标分支名称。

        :param target_branch: The target_branch of this CommitMergeRequestDto.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def source_branch(self):
        r"""Gets the source_branch of this CommitMergeRequestDto.

        **参数解释：** 合并请求的源分支名称。

        :return: The source_branch of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this CommitMergeRequestDto.

        **参数解释：** 合并请求的源分支名称。

        :param source_branch: The source_branch of this CommitMergeRequestDto.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def user_notes_count(self):
        r"""Gets the user_notes_count of this CommitMergeRequestDto.

        **参数解释：** 合并请求中检视意见的数量。

        :return: The user_notes_count of this CommitMergeRequestDto.
        :rtype: int
        """
        return self._user_notes_count

    @user_notes_count.setter
    def user_notes_count(self, user_notes_count):
        r"""Sets the user_notes_count of this CommitMergeRequestDto.

        **参数解释：** 合并请求中检视意见的数量。

        :param user_notes_count: The user_notes_count of this CommitMergeRequestDto.
        :type user_notes_count: int
        """
        self._user_notes_count = user_notes_count

    @property
    def upvotes(self):
        r"""Gets the upvotes of this CommitMergeRequestDto.

        **参数解释：** 合并请求的正向评分数量。

        :return: The upvotes of this CommitMergeRequestDto.
        :rtype: int
        """
        return self._upvotes

    @upvotes.setter
    def upvotes(self, upvotes):
        r"""Sets the upvotes of this CommitMergeRequestDto.

        **参数解释：** 合并请求的正向评分数量。

        :param upvotes: The upvotes of this CommitMergeRequestDto.
        :type upvotes: int
        """
        self._upvotes = upvotes

    @property
    def downvotes(self):
        r"""Gets the downvotes of this CommitMergeRequestDto.

        **参数解释：** 合并请求的负向评分数量。

        :return: The downvotes of this CommitMergeRequestDto.
        :rtype: int
        """
        return self._downvotes

    @downvotes.setter
    def downvotes(self, downvotes):
        r"""Sets the downvotes of this CommitMergeRequestDto.

        **参数解释：** 合并请求的负向评分数量。

        :param downvotes: The downvotes of this CommitMergeRequestDto.
        :type downvotes: int
        """
        self._downvotes = downvotes

    @property
    def author(self):
        r"""Gets the author of this CommitMergeRequestDto.

        :return: The author of this CommitMergeRequestDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this CommitMergeRequestDto.

        :param author: The author of this CommitMergeRequestDto.
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._author = author

    @property
    def assignee(self):
        r"""Gets the assignee of this CommitMergeRequestDto.

        **参数解释：** 合并请求的可合并人列表。

        :return: The assignee of this CommitMergeRequestDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this CommitMergeRequestDto.

        **参数解释：** 合并请求的可合并人列表。

        :param assignee: The assignee of this CommitMergeRequestDto.
        :type assignee: list[:class:`huaweicloudsdkcodehub.v4.UserBasicDto`]
        """
        self._assignee = assignee

    @property
    def source_repository_id(self):
        r"""Gets the source_repository_id of this CommitMergeRequestDto.

        **参数解释：** 源仓库的唯一标识符。

        :return: The source_repository_id of this CommitMergeRequestDto.
        :rtype: int
        """
        return self._source_repository_id

    @source_repository_id.setter
    def source_repository_id(self, source_repository_id):
        r"""Sets the source_repository_id of this CommitMergeRequestDto.

        **参数解释：** 源仓库的唯一标识符。

        :param source_repository_id: The source_repository_id of this CommitMergeRequestDto.
        :type source_repository_id: int
        """
        self._source_repository_id = source_repository_id

    @property
    def target_repository_id(self):
        r"""Gets the target_repository_id of this CommitMergeRequestDto.

        **参数解释：** 目标仓库的唯一标识符。

        :return: The target_repository_id of this CommitMergeRequestDto.
        :rtype: int
        """
        return self._target_repository_id

    @target_repository_id.setter
    def target_repository_id(self, target_repository_id):
        r"""Sets the target_repository_id of this CommitMergeRequestDto.

        **参数解释：** 目标仓库的唯一标识符。

        :param target_repository_id: The target_repository_id of this CommitMergeRequestDto.
        :type target_repository_id: int
        """
        self._target_repository_id = target_repository_id

    @property
    def labels(self):
        r"""Gets the labels of this CommitMergeRequestDto.

        **参数解释：** 合并请求关联的标签列表。

        :return: The labels of this CommitMergeRequestDto.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this CommitMergeRequestDto.

        **参数解释：** 合并请求关联的标签列表。

        :param labels: The labels of this CommitMergeRequestDto.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def work_in_progress(self):
        r"""Gets the work_in_progress of this CommitMergeRequestDto.

        **参数解释：** 表示合并请求是否处于“工作进行中”状态。

        :return: The work_in_progress of this CommitMergeRequestDto.
        :rtype: bool
        """
        return self._work_in_progress

    @work_in_progress.setter
    def work_in_progress(self, work_in_progress):
        r"""Sets the work_in_progress of this CommitMergeRequestDto.

        **参数解释：** 表示合并请求是否处于“工作进行中”状态。

        :param work_in_progress: The work_in_progress of this CommitMergeRequestDto.
        :type work_in_progress: bool
        """
        self._work_in_progress = work_in_progress

    @property
    def milestone(self):
        r"""Gets the milestone of this CommitMergeRequestDto.

        :return: The milestone of this CommitMergeRequestDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.MilestoneBasicDto`
        """
        return self._milestone

    @milestone.setter
    def milestone(self, milestone):
        r"""Sets the milestone of this CommitMergeRequestDto.

        :param milestone: The milestone of this CommitMergeRequestDto.
        :type milestone: :class:`huaweicloudsdkcodehub.v4.MilestoneBasicDto`
        """
        self._milestone = milestone

    @property
    def merge_when_pipeline_succeeds(self):
        r"""Gets the merge_when_pipeline_succeeds of this CommitMergeRequestDto.

        **参数解释：** 表示是否在CI/CD管道成功时自动合并请求。

        :return: The merge_when_pipeline_succeeds of this CommitMergeRequestDto.
        :rtype: bool
        """
        return self._merge_when_pipeline_succeeds

    @merge_when_pipeline_succeeds.setter
    def merge_when_pipeline_succeeds(self, merge_when_pipeline_succeeds):
        r"""Sets the merge_when_pipeline_succeeds of this CommitMergeRequestDto.

        **参数解释：** 表示是否在CI/CD管道成功时自动合并请求。

        :param merge_when_pipeline_succeeds: The merge_when_pipeline_succeeds of this CommitMergeRequestDto.
        :type merge_when_pipeline_succeeds: bool
        """
        self._merge_when_pipeline_succeeds = merge_when_pipeline_succeeds

    @property
    def merge_status(self):
        r"""Gets the merge_status of this CommitMergeRequestDto.

        **参数解释：** 合并请求的合并状态。

        :return: The merge_status of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._merge_status

    @merge_status.setter
    def merge_status(self, merge_status):
        r"""Sets the merge_status of this CommitMergeRequestDto.

        **参数解释：** 合并请求的合并状态。

        :param merge_status: The merge_status of this CommitMergeRequestDto.
        :type merge_status: str
        """
        self._merge_status = merge_status

    @property
    def sha(self):
        r"""Gets the sha of this CommitMergeRequestDto.

        **参数解释：** 合并请求的提交哈希值。

        :return: The sha of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        r"""Sets the sha of this CommitMergeRequestDto.

        **参数解释：** 合并请求的提交哈希值。

        :param sha: The sha of this CommitMergeRequestDto.
        :type sha: str
        """
        self._sha = sha

    @property
    def merge_commit_sha(self):
        r"""Gets the merge_commit_sha of this CommitMergeRequestDto.

        **参数解释：** 合并提交的哈希值。

        :return: The merge_commit_sha of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._merge_commit_sha

    @merge_commit_sha.setter
    def merge_commit_sha(self, merge_commit_sha):
        r"""Sets the merge_commit_sha of this CommitMergeRequestDto.

        **参数解释：** 合并提交的哈希值。

        :param merge_commit_sha: The merge_commit_sha of this CommitMergeRequestDto.
        :type merge_commit_sha: str
        """
        self._merge_commit_sha = merge_commit_sha

    @property
    def discussion_locked(self):
        r"""Gets the discussion_locked of this CommitMergeRequestDto.

        **参数解释：** 表示合并请求的讨论是否被锁定。

        :return: The discussion_locked of this CommitMergeRequestDto.
        :rtype: bool
        """
        return self._discussion_locked

    @discussion_locked.setter
    def discussion_locked(self, discussion_locked):
        r"""Sets the discussion_locked of this CommitMergeRequestDto.

        **参数解释：** 表示合并请求的讨论是否被锁定。

        :param discussion_locked: The discussion_locked of this CommitMergeRequestDto.
        :type discussion_locked: bool
        """
        self._discussion_locked = discussion_locked

    @property
    def force_remove_source_branch(self):
        r"""Gets the force_remove_source_branch of this CommitMergeRequestDto.

        **参数解释：** 表示是否强制删除源分支。

        :return: The force_remove_source_branch of this CommitMergeRequestDto.
        :rtype: bool
        """
        return self._force_remove_source_branch

    @force_remove_source_branch.setter
    def force_remove_source_branch(self, force_remove_source_branch):
        r"""Sets the force_remove_source_branch of this CommitMergeRequestDto.

        **参数解释：** 表示是否强制删除源分支。

        :param force_remove_source_branch: The force_remove_source_branch of this CommitMergeRequestDto.
        :type force_remove_source_branch: bool
        """
        self._force_remove_source_branch = force_remove_source_branch

    @property
    def should_remove_source_branch(self):
        r"""Gets the should_remove_source_branch of this CommitMergeRequestDto.

        **参数解释：** 表示是否应该删除源分支。

        :return: The should_remove_source_branch of this CommitMergeRequestDto.
        :rtype: bool
        """
        return self._should_remove_source_branch

    @should_remove_source_branch.setter
    def should_remove_source_branch(self, should_remove_source_branch):
        r"""Sets the should_remove_source_branch of this CommitMergeRequestDto.

        **参数解释：** 表示是否应该删除源分支。

        :param should_remove_source_branch: The should_remove_source_branch of this CommitMergeRequestDto.
        :type should_remove_source_branch: bool
        """
        self._should_remove_source_branch = should_remove_source_branch

    @property
    def allow_collaboration(self):
        r"""Gets the allow_collaboration of this CommitMergeRequestDto.

        **参数解释：** 表示是否允许协作者参与。

        :return: The allow_collaboration of this CommitMergeRequestDto.
        :rtype: bool
        """
        return self._allow_collaboration

    @allow_collaboration.setter
    def allow_collaboration(self, allow_collaboration):
        r"""Sets the allow_collaboration of this CommitMergeRequestDto.

        **参数解释：** 表示是否允许协作者参与。

        :param allow_collaboration: The allow_collaboration of this CommitMergeRequestDto.
        :type allow_collaboration: bool
        """
        self._allow_collaboration = allow_collaboration

    @property
    def allow_maintainer_to_push(self):
        r"""Gets the allow_maintainer_to_push of this CommitMergeRequestDto.

        **参数解释：** 表示是否允许维护者推送代码。

        :return: The allow_maintainer_to_push of this CommitMergeRequestDto.
        :rtype: bool
        """
        return self._allow_maintainer_to_push

    @allow_maintainer_to_push.setter
    def allow_maintainer_to_push(self, allow_maintainer_to_push):
        r"""Sets the allow_maintainer_to_push of this CommitMergeRequestDto.

        **参数解释：** 表示是否允许维护者推送代码。

        :param allow_maintainer_to_push: The allow_maintainer_to_push of this CommitMergeRequestDto.
        :type allow_maintainer_to_push: bool
        """
        self._allow_maintainer_to_push = allow_maintainer_to_push

    @property
    def web_url(self):
        r"""Gets the web_url of this CommitMergeRequestDto.

        **参数解释：** 合并请求的网页URL链接。

        :return: The web_url of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this CommitMergeRequestDto.

        **参数解释：** 合并请求的网页URL链接。

        :param web_url: The web_url of this CommitMergeRequestDto.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def time_stats(self):
        r"""Gets the time_stats of this CommitMergeRequestDto.

        :return: The time_stats of this CommitMergeRequestDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.IssuableTimeStatsDto`
        """
        return self._time_stats

    @time_stats.setter
    def time_stats(self, time_stats):
        r"""Sets the time_stats of this CommitMergeRequestDto.

        :param time_stats: The time_stats of this CommitMergeRequestDto.
        :type time_stats: :class:`huaweicloudsdkcodehub.v4.IssuableTimeStatsDto`
        """
        self._time_stats = time_stats

    @property
    def squash(self):
        r"""Gets the squash of this CommitMergeRequestDto.

        **参数解释：** 表示是否在合并时将提交压缩为一个。

        :return: The squash of this CommitMergeRequestDto.
        :rtype: bool
        """
        return self._squash

    @squash.setter
    def squash(self, squash):
        r"""Sets the squash of this CommitMergeRequestDto.

        **参数解释：** 表示是否在合并时将提交压缩为一个。

        :param squash: The squash of this CommitMergeRequestDto.
        :type squash: bool
        """
        self._squash = squash

    @property
    def merge_request_type(self):
        r"""Gets the merge_request_type of this CommitMergeRequestDto.

        **参数解释：** 合并请求的类型。

        :return: The merge_request_type of this CommitMergeRequestDto.
        :rtype: str
        """
        return self._merge_request_type

    @merge_request_type.setter
    def merge_request_type(self, merge_request_type):
        r"""Sets the merge_request_type of this CommitMergeRequestDto.

        **参数解释：** 合并请求的类型。

        :param merge_request_type: The merge_request_type of this CommitMergeRequestDto.
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
        if not isinstance(other, CommitMergeRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
