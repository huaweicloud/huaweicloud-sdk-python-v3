# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestListBasicDto:

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
        'source_branch': 'str',
        'target_branch': 'str',
        'state': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'source_repository_id': 'int',
        'review_mode': 'str',
        'author': 'UserBasicDto',
        'closed_at': 'str',
        'closed_by': 'UserBasicDto',
        'merged_at': 'str',
        'merged_by': 'UserBasicDto',
        'pipeline_status': 'str',
        'codequality_status': 'str',
        'pipeline_status_with_code_quality': 'str',
        'notes': 'int',
        'source_repository': 'ProjectSimpleDto',
        'target_repository': 'ProjectSimpleDto',
        'web_url': 'str',
        'added_lines': 'int',
        'removed_lines': 'int',
        'merge_request_type': 'str',
        'source_git_url': 'str',
        'labels': 'list[dict(str, object)]',
        'score': 'int',
        'min_merged_score': 'int',
        'source_product_id': 'str',
        'target_product_id': 'str',
        'product_name': 'str',
        'notes_count': 'NotesCountDto',
        'moderation_result': 'bool',
        'moderation_time': 'int',
        'moderation_status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'iid': 'iid',
        'title': 'title',
        'source_branch': 'source_branch',
        'target_branch': 'target_branch',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'source_repository_id': 'source_repository_id',
        'review_mode': 'review_mode',
        'author': 'author',
        'closed_at': 'closed_at',
        'closed_by': 'closed_by',
        'merged_at': 'merged_at',
        'merged_by': 'merged_by',
        'pipeline_status': 'pipeline_status',
        'codequality_status': 'codequality_status',
        'pipeline_status_with_code_quality': 'pipeline_status_with_code_quality',
        'notes': 'notes',
        'source_repository': 'source_repository',
        'target_repository': 'target_repository',
        'web_url': 'web_url',
        'added_lines': 'added_lines',
        'removed_lines': 'removed_lines',
        'merge_request_type': 'merge_request_type',
        'source_git_url': 'source_git_url',
        'labels': 'labels',
        'score': 'score',
        'min_merged_score': 'min_merged_score',
        'source_product_id': 'source_product_id',
        'target_product_id': 'target_product_id',
        'product_name': 'product_name',
        'notes_count': 'notes_count',
        'moderation_result': 'moderation_result',
        'moderation_time': 'moderation_time',
        'moderation_status': 'moderation_status'
    }

    def __init__(self, id=None, iid=None, title=None, source_branch=None, target_branch=None, state=None, created_at=None, updated_at=None, source_repository_id=None, review_mode=None, author=None, closed_at=None, closed_by=None, merged_at=None, merged_by=None, pipeline_status=None, codequality_status=None, pipeline_status_with_code_quality=None, notes=None, source_repository=None, target_repository=None, web_url=None, added_lines=None, removed_lines=None, merge_request_type=None, source_git_url=None, labels=None, score=None, min_merged_score=None, source_product_id=None, target_product_id=None, product_name=None, notes_count=None, moderation_result=None, moderation_time=None, moderation_status=None):
        r"""MergeRequestListBasicDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 合并请求ID。
        :type id: int
        :param iid: **参数解释：** 合并请求位于当前仓库序号。
        :type iid: int
        :param title: **参数解释：** 合并请求标题。
        :type title: str
        :param source_branch: **参数解释：** 合并请求源分支。
        :type source_branch: str
        :param target_branch: **参数解释：** 合并请求目标分支。
        :type target_branch: str
        :param state: **参数解释：** 合并请求状态。
        :type state: str
        :param created_at: **参数解释：** 合并请求创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 合并请求更新时间。
        :type updated_at: str
        :param source_repository_id: **参数解释：** 合并请求源仓库ID。
        :type source_repository_id: int
        :param review_mode: **参数解释：** 合并请求检视模式。
        :type review_mode: str
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param closed_at: **参数解释：** 合并请求关闭时间。
        :type closed_at: str
        :param closed_by: 
        :type closed_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param merged_at: **参数解释：** 合并请求合并时间。
        :type merged_at: str
        :param merged_by: 
        :type merged_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param pipeline_status: **参数解释：** 合并请求流水线状态。
        :type pipeline_status: str
        :param codequality_status: **参数解释：** 合并请求代码质量状态。
        :type codequality_status: str
        :param pipeline_status_with_code_quality: **参数解释：** 合并请求流水线状态。
        :type pipeline_status_with_code_quality: str
        :param notes: **参数解释：** 合并请求检视意见。
        :type notes: int
        :param source_repository: 
        :type source_repository: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        :param target_repository: 
        :type target_repository: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        :param web_url: **参数解释：** 合并请求URL地址。
        :type web_url: str
        :param added_lines: **参数解释：** 合并请求新增代码行数。
        :type added_lines: int
        :param removed_lines: **参数解释：** 合并请求删除代码行数。
        :type removed_lines: int
        :param merge_request_type: **参数解释：** 合并请求检视模式。
        :type merge_request_type: str
        :param source_git_url: **参数解释：** 合并请求git地址。
        :type source_git_url: str
        :param labels: **参数解释：** 合并请求标签。
        :type labels: list[dict(str, object)]
        :param score: **参数解释：** 合并请求分数。
        :type score: int
        :param min_merged_score: **参数解释：** 合并请求最小合入分数。
        :type min_merged_score: int
        :param source_product_id: **参数解释：** 合并请求源项目ID。
        :type source_product_id: str
        :param target_product_id: **参数解释：** 合并请求目标项目ID。
        :type target_product_id: str
        :param product_name: **参数解释：** 合并请求项目名。
        :type product_name: str
        :param notes_count: 
        :type notes_count: :class:`huaweicloudsdkcodehub.v4.NotesCountDto`
        :param moderation_result: **参数解释：** 合并请求审核结果。
        :type moderation_result: bool
        :param moderation_time: **参数解释：** 合并请求审核时间。
        :type moderation_time: int
        :param moderation_status: **参数解释：** 合并请求审核状态。
        :type moderation_status: int
        """
        
        

        self._id = None
        self._iid = None
        self._title = None
        self._source_branch = None
        self._target_branch = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._source_repository_id = None
        self._review_mode = None
        self._author = None
        self._closed_at = None
        self._closed_by = None
        self._merged_at = None
        self._merged_by = None
        self._pipeline_status = None
        self._codequality_status = None
        self._pipeline_status_with_code_quality = None
        self._notes = None
        self._source_repository = None
        self._target_repository = None
        self._web_url = None
        self._added_lines = None
        self._removed_lines = None
        self._merge_request_type = None
        self._source_git_url = None
        self._labels = None
        self._score = None
        self._min_merged_score = None
        self._source_product_id = None
        self._target_product_id = None
        self._product_name = None
        self._notes_count = None
        self._moderation_result = None
        self._moderation_time = None
        self._moderation_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if iid is not None:
            self.iid = iid
        if title is not None:
            self.title = title
        if source_branch is not None:
            self.source_branch = source_branch
        if target_branch is not None:
            self.target_branch = target_branch
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if source_repository_id is not None:
            self.source_repository_id = source_repository_id
        if review_mode is not None:
            self.review_mode = review_mode
        if author is not None:
            self.author = author
        if closed_at is not None:
            self.closed_at = closed_at
        if closed_by is not None:
            self.closed_by = closed_by
        if merged_at is not None:
            self.merged_at = merged_at
        if merged_by is not None:
            self.merged_by = merged_by
        if pipeline_status is not None:
            self.pipeline_status = pipeline_status
        if codequality_status is not None:
            self.codequality_status = codequality_status
        if pipeline_status_with_code_quality is not None:
            self.pipeline_status_with_code_quality = pipeline_status_with_code_quality
        if notes is not None:
            self.notes = notes
        if source_repository is not None:
            self.source_repository = source_repository
        if target_repository is not None:
            self.target_repository = target_repository
        if web_url is not None:
            self.web_url = web_url
        if added_lines is not None:
            self.added_lines = added_lines
        if removed_lines is not None:
            self.removed_lines = removed_lines
        if merge_request_type is not None:
            self.merge_request_type = merge_request_type
        if source_git_url is not None:
            self.source_git_url = source_git_url
        if labels is not None:
            self.labels = labels
        if score is not None:
            self.score = score
        if min_merged_score is not None:
            self.min_merged_score = min_merged_score
        if source_product_id is not None:
            self.source_product_id = source_product_id
        if target_product_id is not None:
            self.target_product_id = target_product_id
        if product_name is not None:
            self.product_name = product_name
        if notes_count is not None:
            self.notes_count = notes_count
        if moderation_result is not None:
            self.moderation_result = moderation_result
        if moderation_time is not None:
            self.moderation_time = moderation_time
        if moderation_status is not None:
            self.moderation_status = moderation_status

    @property
    def id(self):
        r"""Gets the id of this MergeRequestListBasicDto.

        **参数解释：** 合并请求ID。

        :return: The id of this MergeRequestListBasicDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MergeRequestListBasicDto.

        **参数解释：** 合并请求ID。

        :param id: The id of this MergeRequestListBasicDto.
        :type id: int
        """
        self._id = id

    @property
    def iid(self):
        r"""Gets the iid of this MergeRequestListBasicDto.

        **参数解释：** 合并请求位于当前仓库序号。

        :return: The iid of this MergeRequestListBasicDto.
        :rtype: int
        """
        return self._iid

    @iid.setter
    def iid(self, iid):
        r"""Sets the iid of this MergeRequestListBasicDto.

        **参数解释：** 合并请求位于当前仓库序号。

        :param iid: The iid of this MergeRequestListBasicDto.
        :type iid: int
        """
        self._iid = iid

    @property
    def title(self):
        r"""Gets the title of this MergeRequestListBasicDto.

        **参数解释：** 合并请求标题。

        :return: The title of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this MergeRequestListBasicDto.

        **参数解释：** 合并请求标题。

        :param title: The title of this MergeRequestListBasicDto.
        :type title: str
        """
        self._title = title

    @property
    def source_branch(self):
        r"""Gets the source_branch of this MergeRequestListBasicDto.

        **参数解释：** 合并请求源分支。

        :return: The source_branch of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this MergeRequestListBasicDto.

        **参数解释：** 合并请求源分支。

        :param source_branch: The source_branch of this MergeRequestListBasicDto.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def target_branch(self):
        r"""Gets the target_branch of this MergeRequestListBasicDto.

        **参数解释：** 合并请求目标分支。

        :return: The target_branch of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this MergeRequestListBasicDto.

        **参数解释：** 合并请求目标分支。

        :param target_branch: The target_branch of this MergeRequestListBasicDto.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def state(self):
        r"""Gets the state of this MergeRequestListBasicDto.

        **参数解释：** 合并请求状态。

        :return: The state of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this MergeRequestListBasicDto.

        **参数解释：** 合并请求状态。

        :param state: The state of this MergeRequestListBasicDto.
        :type state: str
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this MergeRequestListBasicDto.

        **参数解释：** 合并请求创建时间。

        :return: The created_at of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this MergeRequestListBasicDto.

        **参数解释：** 合并请求创建时间。

        :param created_at: The created_at of this MergeRequestListBasicDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this MergeRequestListBasicDto.

        **参数解释：** 合并请求更新时间。

        :return: The updated_at of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this MergeRequestListBasicDto.

        **参数解释：** 合并请求更新时间。

        :param updated_at: The updated_at of this MergeRequestListBasicDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def source_repository_id(self):
        r"""Gets the source_repository_id of this MergeRequestListBasicDto.

        **参数解释：** 合并请求源仓库ID。

        :return: The source_repository_id of this MergeRequestListBasicDto.
        :rtype: int
        """
        return self._source_repository_id

    @source_repository_id.setter
    def source_repository_id(self, source_repository_id):
        r"""Sets the source_repository_id of this MergeRequestListBasicDto.

        **参数解释：** 合并请求源仓库ID。

        :param source_repository_id: The source_repository_id of this MergeRequestListBasicDto.
        :type source_repository_id: int
        """
        self._source_repository_id = source_repository_id

    @property
    def review_mode(self):
        r"""Gets the review_mode of this MergeRequestListBasicDto.

        **参数解释：** 合并请求检视模式。

        :return: The review_mode of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._review_mode

    @review_mode.setter
    def review_mode(self, review_mode):
        r"""Sets the review_mode of this MergeRequestListBasicDto.

        **参数解释：** 合并请求检视模式。

        :param review_mode: The review_mode of this MergeRequestListBasicDto.
        :type review_mode: str
        """
        self._review_mode = review_mode

    @property
    def author(self):
        r"""Gets the author of this MergeRequestListBasicDto.

        :return: The author of this MergeRequestListBasicDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this MergeRequestListBasicDto.

        :param author: The author of this MergeRequestListBasicDto.
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._author = author

    @property
    def closed_at(self):
        r"""Gets the closed_at of this MergeRequestListBasicDto.

        **参数解释：** 合并请求关闭时间。

        :return: The closed_at of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        r"""Sets the closed_at of this MergeRequestListBasicDto.

        **参数解释：** 合并请求关闭时间。

        :param closed_at: The closed_at of this MergeRequestListBasicDto.
        :type closed_at: str
        """
        self._closed_at = closed_at

    @property
    def closed_by(self):
        r"""Gets the closed_by of this MergeRequestListBasicDto.

        :return: The closed_by of this MergeRequestListBasicDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._closed_by

    @closed_by.setter
    def closed_by(self, closed_by):
        r"""Sets the closed_by of this MergeRequestListBasicDto.

        :param closed_by: The closed_by of this MergeRequestListBasicDto.
        :type closed_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._closed_by = closed_by

    @property
    def merged_at(self):
        r"""Gets the merged_at of this MergeRequestListBasicDto.

        **参数解释：** 合并请求合并时间。

        :return: The merged_at of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._merged_at

    @merged_at.setter
    def merged_at(self, merged_at):
        r"""Sets the merged_at of this MergeRequestListBasicDto.

        **参数解释：** 合并请求合并时间。

        :param merged_at: The merged_at of this MergeRequestListBasicDto.
        :type merged_at: str
        """
        self._merged_at = merged_at

    @property
    def merged_by(self):
        r"""Gets the merged_by of this MergeRequestListBasicDto.

        :return: The merged_by of this MergeRequestListBasicDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._merged_by

    @merged_by.setter
    def merged_by(self, merged_by):
        r"""Sets the merged_by of this MergeRequestListBasicDto.

        :param merged_by: The merged_by of this MergeRequestListBasicDto.
        :type merged_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._merged_by = merged_by

    @property
    def pipeline_status(self):
        r"""Gets the pipeline_status of this MergeRequestListBasicDto.

        **参数解释：** 合并请求流水线状态。

        :return: The pipeline_status of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._pipeline_status

    @pipeline_status.setter
    def pipeline_status(self, pipeline_status):
        r"""Sets the pipeline_status of this MergeRequestListBasicDto.

        **参数解释：** 合并请求流水线状态。

        :param pipeline_status: The pipeline_status of this MergeRequestListBasicDto.
        :type pipeline_status: str
        """
        self._pipeline_status = pipeline_status

    @property
    def codequality_status(self):
        r"""Gets the codequality_status of this MergeRequestListBasicDto.

        **参数解释：** 合并请求代码质量状态。

        :return: The codequality_status of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._codequality_status

    @codequality_status.setter
    def codequality_status(self, codequality_status):
        r"""Sets the codequality_status of this MergeRequestListBasicDto.

        **参数解释：** 合并请求代码质量状态。

        :param codequality_status: The codequality_status of this MergeRequestListBasicDto.
        :type codequality_status: str
        """
        self._codequality_status = codequality_status

    @property
    def pipeline_status_with_code_quality(self):
        r"""Gets the pipeline_status_with_code_quality of this MergeRequestListBasicDto.

        **参数解释：** 合并请求流水线状态。

        :return: The pipeline_status_with_code_quality of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._pipeline_status_with_code_quality

    @pipeline_status_with_code_quality.setter
    def pipeline_status_with_code_quality(self, pipeline_status_with_code_quality):
        r"""Sets the pipeline_status_with_code_quality of this MergeRequestListBasicDto.

        **参数解释：** 合并请求流水线状态。

        :param pipeline_status_with_code_quality: The pipeline_status_with_code_quality of this MergeRequestListBasicDto.
        :type pipeline_status_with_code_quality: str
        """
        self._pipeline_status_with_code_quality = pipeline_status_with_code_quality

    @property
    def notes(self):
        r"""Gets the notes of this MergeRequestListBasicDto.

        **参数解释：** 合并请求检视意见。

        :return: The notes of this MergeRequestListBasicDto.
        :rtype: int
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this MergeRequestListBasicDto.

        **参数解释：** 合并请求检视意见。

        :param notes: The notes of this MergeRequestListBasicDto.
        :type notes: int
        """
        self._notes = notes

    @property
    def source_repository(self):
        r"""Gets the source_repository of this MergeRequestListBasicDto.

        :return: The source_repository of this MergeRequestListBasicDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        """
        return self._source_repository

    @source_repository.setter
    def source_repository(self, source_repository):
        r"""Sets the source_repository of this MergeRequestListBasicDto.

        :param source_repository: The source_repository of this MergeRequestListBasicDto.
        :type source_repository: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        """
        self._source_repository = source_repository

    @property
    def target_repository(self):
        r"""Gets the target_repository of this MergeRequestListBasicDto.

        :return: The target_repository of this MergeRequestListBasicDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        """
        return self._target_repository

    @target_repository.setter
    def target_repository(self, target_repository):
        r"""Sets the target_repository of this MergeRequestListBasicDto.

        :param target_repository: The target_repository of this MergeRequestListBasicDto.
        :type target_repository: :class:`huaweicloudsdkcodehub.v4.ProjectSimpleDto`
        """
        self._target_repository = target_repository

    @property
    def web_url(self):
        r"""Gets the web_url of this MergeRequestListBasicDto.

        **参数解释：** 合并请求URL地址。

        :return: The web_url of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this MergeRequestListBasicDto.

        **参数解释：** 合并请求URL地址。

        :param web_url: The web_url of this MergeRequestListBasicDto.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def added_lines(self):
        r"""Gets the added_lines of this MergeRequestListBasicDto.

        **参数解释：** 合并请求新增代码行数。

        :return: The added_lines of this MergeRequestListBasicDto.
        :rtype: int
        """
        return self._added_lines

    @added_lines.setter
    def added_lines(self, added_lines):
        r"""Sets the added_lines of this MergeRequestListBasicDto.

        **参数解释：** 合并请求新增代码行数。

        :param added_lines: The added_lines of this MergeRequestListBasicDto.
        :type added_lines: int
        """
        self._added_lines = added_lines

    @property
    def removed_lines(self):
        r"""Gets the removed_lines of this MergeRequestListBasicDto.

        **参数解释：** 合并请求删除代码行数。

        :return: The removed_lines of this MergeRequestListBasicDto.
        :rtype: int
        """
        return self._removed_lines

    @removed_lines.setter
    def removed_lines(self, removed_lines):
        r"""Sets the removed_lines of this MergeRequestListBasicDto.

        **参数解释：** 合并请求删除代码行数。

        :param removed_lines: The removed_lines of this MergeRequestListBasicDto.
        :type removed_lines: int
        """
        self._removed_lines = removed_lines

    @property
    def merge_request_type(self):
        r"""Gets the merge_request_type of this MergeRequestListBasicDto.

        **参数解释：** 合并请求检视模式。

        :return: The merge_request_type of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._merge_request_type

    @merge_request_type.setter
    def merge_request_type(self, merge_request_type):
        r"""Sets the merge_request_type of this MergeRequestListBasicDto.

        **参数解释：** 合并请求检视模式。

        :param merge_request_type: The merge_request_type of this MergeRequestListBasicDto.
        :type merge_request_type: str
        """
        self._merge_request_type = merge_request_type

    @property
    def source_git_url(self):
        r"""Gets the source_git_url of this MergeRequestListBasicDto.

        **参数解释：** 合并请求git地址。

        :return: The source_git_url of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._source_git_url

    @source_git_url.setter
    def source_git_url(self, source_git_url):
        r"""Sets the source_git_url of this MergeRequestListBasicDto.

        **参数解释：** 合并请求git地址。

        :param source_git_url: The source_git_url of this MergeRequestListBasicDto.
        :type source_git_url: str
        """
        self._source_git_url = source_git_url

    @property
    def labels(self):
        r"""Gets the labels of this MergeRequestListBasicDto.

        **参数解释：** 合并请求标签。

        :return: The labels of this MergeRequestListBasicDto.
        :rtype: list[dict(str, object)]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this MergeRequestListBasicDto.

        **参数解释：** 合并请求标签。

        :param labels: The labels of this MergeRequestListBasicDto.
        :type labels: list[dict(str, object)]
        """
        self._labels = labels

    @property
    def score(self):
        r"""Gets the score of this MergeRequestListBasicDto.

        **参数解释：** 合并请求分数。

        :return: The score of this MergeRequestListBasicDto.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this MergeRequestListBasicDto.

        **参数解释：** 合并请求分数。

        :param score: The score of this MergeRequestListBasicDto.
        :type score: int
        """
        self._score = score

    @property
    def min_merged_score(self):
        r"""Gets the min_merged_score of this MergeRequestListBasicDto.

        **参数解释：** 合并请求最小合入分数。

        :return: The min_merged_score of this MergeRequestListBasicDto.
        :rtype: int
        """
        return self._min_merged_score

    @min_merged_score.setter
    def min_merged_score(self, min_merged_score):
        r"""Sets the min_merged_score of this MergeRequestListBasicDto.

        **参数解释：** 合并请求最小合入分数。

        :param min_merged_score: The min_merged_score of this MergeRequestListBasicDto.
        :type min_merged_score: int
        """
        self._min_merged_score = min_merged_score

    @property
    def source_product_id(self):
        r"""Gets the source_product_id of this MergeRequestListBasicDto.

        **参数解释：** 合并请求源项目ID。

        :return: The source_product_id of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._source_product_id

    @source_product_id.setter
    def source_product_id(self, source_product_id):
        r"""Sets the source_product_id of this MergeRequestListBasicDto.

        **参数解释：** 合并请求源项目ID。

        :param source_product_id: The source_product_id of this MergeRequestListBasicDto.
        :type source_product_id: str
        """
        self._source_product_id = source_product_id

    @property
    def target_product_id(self):
        r"""Gets the target_product_id of this MergeRequestListBasicDto.

        **参数解释：** 合并请求目标项目ID。

        :return: The target_product_id of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._target_product_id

    @target_product_id.setter
    def target_product_id(self, target_product_id):
        r"""Sets the target_product_id of this MergeRequestListBasicDto.

        **参数解释：** 合并请求目标项目ID。

        :param target_product_id: The target_product_id of this MergeRequestListBasicDto.
        :type target_product_id: str
        """
        self._target_product_id = target_product_id

    @property
    def product_name(self):
        r"""Gets the product_name of this MergeRequestListBasicDto.

        **参数解释：** 合并请求项目名。

        :return: The product_name of this MergeRequestListBasicDto.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this MergeRequestListBasicDto.

        **参数解释：** 合并请求项目名。

        :param product_name: The product_name of this MergeRequestListBasicDto.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def notes_count(self):
        r"""Gets the notes_count of this MergeRequestListBasicDto.

        :return: The notes_count of this MergeRequestListBasicDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.NotesCountDto`
        """
        return self._notes_count

    @notes_count.setter
    def notes_count(self, notes_count):
        r"""Sets the notes_count of this MergeRequestListBasicDto.

        :param notes_count: The notes_count of this MergeRequestListBasicDto.
        :type notes_count: :class:`huaweicloudsdkcodehub.v4.NotesCountDto`
        """
        self._notes_count = notes_count

    @property
    def moderation_result(self):
        r"""Gets the moderation_result of this MergeRequestListBasicDto.

        **参数解释：** 合并请求审核结果。

        :return: The moderation_result of this MergeRequestListBasicDto.
        :rtype: bool
        """
        return self._moderation_result

    @moderation_result.setter
    def moderation_result(self, moderation_result):
        r"""Sets the moderation_result of this MergeRequestListBasicDto.

        **参数解释：** 合并请求审核结果。

        :param moderation_result: The moderation_result of this MergeRequestListBasicDto.
        :type moderation_result: bool
        """
        self._moderation_result = moderation_result

    @property
    def moderation_time(self):
        r"""Gets the moderation_time of this MergeRequestListBasicDto.

        **参数解释：** 合并请求审核时间。

        :return: The moderation_time of this MergeRequestListBasicDto.
        :rtype: int
        """
        return self._moderation_time

    @moderation_time.setter
    def moderation_time(self, moderation_time):
        r"""Sets the moderation_time of this MergeRequestListBasicDto.

        **参数解释：** 合并请求审核时间。

        :param moderation_time: The moderation_time of this MergeRequestListBasicDto.
        :type moderation_time: int
        """
        self._moderation_time = moderation_time

    @property
    def moderation_status(self):
        r"""Gets the moderation_status of this MergeRequestListBasicDto.

        **参数解释：** 合并请求审核状态。

        :return: The moderation_status of this MergeRequestListBasicDto.
        :rtype: int
        """
        return self._moderation_status

    @moderation_status.setter
    def moderation_status(self, moderation_status):
        r"""Sets the moderation_status of this MergeRequestListBasicDto.

        **参数解释：** 合并请求审核状态。

        :param moderation_status: The moderation_status of this MergeRequestListBasicDto.
        :type moderation_status: int
        """
        self._moderation_status = moderation_status

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
        if not isinstance(other, MergeRequestListBasicDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
