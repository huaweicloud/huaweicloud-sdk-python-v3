# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMergeRequestDiscussionResponse(SdkResponse):

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
        'type': 'str',
        'body': 'str',
        'attachment': 'str',
        'author': 'UserBasicDto',
        'created_at': 'str',
        'updated_at': 'str',
        'system': 'bool',
        'noteable_id': 'int',
        'noteable_type': 'str',
        'commit_id': 'str',
        'resolvable': 'bool',
        'is_reply': 'bool',
        'resolved_by': 'UserBasicDto',
        'noteable_iid': 'int',
        'discussion_id': 'str',
        'repository': 'str',
        'diff_file': 'str',
        'diff': 'str',
        'archived': 'bool',
        'review_categories': 'str',
        'review_categories_cn': 'str',
        'review_categories_en': 'str',
        'review_modules': 'str',
        'severity': 'str',
        'severity_cn': 'str',
        'severity_en': 'str',
        'file_path': 'str',
        'line': 'str',
        'assignee': 'UserBasicDto',
        'proposer': 'UserBasicDto',
        'position': 'PositionDto',
        'resolved': 'bool',
        'is_outdated': 'bool',
        'moderation_result': 'bool',
        'moderation_time': 'int',
        'moderation_status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'body': 'body',
        'attachment': 'attachment',
        'author': 'author',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'system': 'system',
        'noteable_id': 'noteable_id',
        'noteable_type': 'noteable_type',
        'commit_id': 'commit_id',
        'resolvable': 'resolvable',
        'is_reply': 'is_reply',
        'resolved_by': 'resolved_by',
        'noteable_iid': 'noteable_iid',
        'discussion_id': 'discussion_id',
        'repository': 'repository',
        'diff_file': 'diff_file',
        'diff': 'diff',
        'archived': 'archived',
        'review_categories': 'review_categories',
        'review_categories_cn': 'review_categories_cn',
        'review_categories_en': 'review_categories_en',
        'review_modules': 'review_modules',
        'severity': 'severity',
        'severity_cn': 'severity_cn',
        'severity_en': 'severity_en',
        'file_path': 'file_path',
        'line': 'line',
        'assignee': 'assignee',
        'proposer': 'proposer',
        'position': 'position',
        'resolved': 'resolved',
        'is_outdated': 'is_outdated',
        'moderation_result': 'moderation_result',
        'moderation_time': 'moderation_time',
        'moderation_status': 'moderation_status'
    }

    def __init__(self, id=None, type=None, body=None, attachment=None, author=None, created_at=None, updated_at=None, system=None, noteable_id=None, noteable_type=None, commit_id=None, resolvable=None, is_reply=None, resolved_by=None, noteable_iid=None, discussion_id=None, repository=None, diff_file=None, diff=None, archived=None, review_categories=None, review_categories_cn=None, review_categories_en=None, review_modules=None, severity=None, severity_cn=None, severity_en=None, file_path=None, line=None, assignee=None, proposer=None, position=None, resolved=None, is_outdated=None, moderation_result=None, moderation_time=None, moderation_status=None):
        r"""UpdateMergeRequestDiscussionResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 评论id(主评论和回复不共用)。
        :type id: int
        :param type: **参数解释：** 类型(普通评论、需要解决的普通评论、需要解决的关联代码行的评论)。
        :type type: str
        :param body: **参数解释：** 评论内容。
        :type body: str
        :param attachment: **参数解释：** 附件(弃用)。
        :type attachment: str
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。
        :type updated_at: str
        :param system: **参数解释：** 是否为系统添加的。
        :type system: bool
        :param noteable_id: **参数解释：** 合并请求id或issue id。
        :type noteable_id: int
        :param noteable_type: **参数解释：** 意见类型。
        :type noteable_type: str
        :param commit_id: **参数解释：** 提交记录id。
        :type commit_id: str
        :param resolvable: **参数解释：** 是否需要解决。
        :type resolvable: bool
        :param is_reply: **参数解释：** 是否为回复。
        :type is_reply: bool
        :param resolved_by: 
        :type resolved_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param noteable_iid: **参数解释：** 合并请求iid或issue iid。
        :type noteable_iid: int
        :param discussion_id: **参数解释：** 检视意见id(主评论和回复共用)。
        :type discussion_id: str
        :param repository: **参数解释：** 仓库路径。
        :type repository: str
        :param diff_file: **参数解释：** 关联代码行所在文件的文件名。
        :type diff_file: str
        :param diff: **参数解释：** 关联代码行的代码片段。
        :type diff: str
        :param archived: **参数解释：** 是否已归档。
        :type archived: bool
        :param review_categories: **参数解释：** 意见分类key。
        :type review_categories: str
        :param review_categories_cn: **参数解释：** 意见分类中文名。
        :type review_categories_cn: str
        :param review_categories_en: **参数解释：** 合并请求版本信息。
        :type review_categories_en: str
        :param review_modules: **参数解释：** 合并请求版本信息。
        :type review_modules: str
        :param severity: **参数解释：** 严重程度key。
        :type severity: str
        :param severity_cn: **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命
        :type severity_cn: str
        :param severity_en: **参数解释：** 严重程度英文。
        :type severity_en: str
        :param file_path: **参数解释：** 文件路径(弃用)。
        :type file_path: str
        :param line: **参数解释：** 行号(弃用)。
        :type line: str
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param proposer: 
        :type proposer: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param position: 
        :type position: :class:`huaweicloudsdkcodehub.v4.PositionDto`
        :param resolved: **参数解释：** 是否已解决。
        :type resolved: bool
        :param is_outdated: **参数解释：** 是否已过期。
        :type is_outdated: bool
        :param moderation_result: **参数解释：** 内容审核结果。
        :type moderation_result: bool
        :param moderation_time: **参数解释：** 内容审核时间。
        :type moderation_time: int
        :param moderation_status: **参数解释：** 内容审核状态。
        :type moderation_status: int
        """
        
        super(UpdateMergeRequestDiscussionResponse, self).__init__()

        self._id = None
        self._type = None
        self._body = None
        self._attachment = None
        self._author = None
        self._created_at = None
        self._updated_at = None
        self._system = None
        self._noteable_id = None
        self._noteable_type = None
        self._commit_id = None
        self._resolvable = None
        self._is_reply = None
        self._resolved_by = None
        self._noteable_iid = None
        self._discussion_id = None
        self._repository = None
        self._diff_file = None
        self._diff = None
        self._archived = None
        self._review_categories = None
        self._review_categories_cn = None
        self._review_categories_en = None
        self._review_modules = None
        self._severity = None
        self._severity_cn = None
        self._severity_en = None
        self._file_path = None
        self._line = None
        self._assignee = None
        self._proposer = None
        self._position = None
        self._resolved = None
        self._is_outdated = None
        self._moderation_result = None
        self._moderation_time = None
        self._moderation_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if body is not None:
            self.body = body
        if attachment is not None:
            self.attachment = attachment
        if author is not None:
            self.author = author
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if system is not None:
            self.system = system
        if noteable_id is not None:
            self.noteable_id = noteable_id
        if noteable_type is not None:
            self.noteable_type = noteable_type
        if commit_id is not None:
            self.commit_id = commit_id
        if resolvable is not None:
            self.resolvable = resolvable
        if is_reply is not None:
            self.is_reply = is_reply
        if resolved_by is not None:
            self.resolved_by = resolved_by
        if noteable_iid is not None:
            self.noteable_iid = noteable_iid
        if discussion_id is not None:
            self.discussion_id = discussion_id
        if repository is not None:
            self.repository = repository
        if diff_file is not None:
            self.diff_file = diff_file
        if diff is not None:
            self.diff = diff
        if archived is not None:
            self.archived = archived
        if review_categories is not None:
            self.review_categories = review_categories
        if review_categories_cn is not None:
            self.review_categories_cn = review_categories_cn
        if review_categories_en is not None:
            self.review_categories_en = review_categories_en
        if review_modules is not None:
            self.review_modules = review_modules
        if severity is not None:
            self.severity = severity
        if severity_cn is not None:
            self.severity_cn = severity_cn
        if severity_en is not None:
            self.severity_en = severity_en
        if file_path is not None:
            self.file_path = file_path
        if line is not None:
            self.line = line
        if assignee is not None:
            self.assignee = assignee
        if proposer is not None:
            self.proposer = proposer
        if position is not None:
            self.position = position
        if resolved is not None:
            self.resolved = resolved
        if is_outdated is not None:
            self.is_outdated = is_outdated
        if moderation_result is not None:
            self.moderation_result = moderation_result
        if moderation_time is not None:
            self.moderation_time = moderation_time
        if moderation_status is not None:
            self.moderation_status = moderation_status

    @property
    def id(self):
        r"""Gets the id of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 评论id(主评论和回复不共用)。

        :return: The id of this UpdateMergeRequestDiscussionResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 评论id(主评论和回复不共用)。

        :param id: The id of this UpdateMergeRequestDiscussionResponse.
        :type id: int
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 类型(普通评论、需要解决的普通评论、需要解决的关联代码行的评论)。

        :return: The type of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 类型(普通评论、需要解决的普通评论、需要解决的关联代码行的评论)。

        :param type: The type of this UpdateMergeRequestDiscussionResponse.
        :type type: str
        """
        self._type = type

    @property
    def body(self):
        r"""Gets the body of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 评论内容。

        :return: The body of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 评论内容。

        :param body: The body of this UpdateMergeRequestDiscussionResponse.
        :type body: str
        """
        self._body = body

    @property
    def attachment(self):
        r"""Gets the attachment of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 附件(弃用)。

        :return: The attachment of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        r"""Sets the attachment of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 附件(弃用)。

        :param attachment: The attachment of this UpdateMergeRequestDiscussionResponse.
        :type attachment: str
        """
        self._attachment = attachment

    @property
    def author(self):
        r"""Gets the author of this UpdateMergeRequestDiscussionResponse.

        :return: The author of this UpdateMergeRequestDiscussionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this UpdateMergeRequestDiscussionResponse.

        :param author: The author of this UpdateMergeRequestDiscussionResponse.
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._author = author

    @property
    def created_at(self):
        r"""Gets the created_at of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 创建时间。

        :return: The created_at of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this UpdateMergeRequestDiscussionResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 更新时间。

        :return: The updated_at of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 更新时间。

        :param updated_at: The updated_at of this UpdateMergeRequestDiscussionResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def system(self):
        r"""Gets the system of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否为系统添加的。

        :return: The system of this UpdateMergeRequestDiscussionResponse.
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        r"""Sets the system of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否为系统添加的。

        :param system: The system of this UpdateMergeRequestDiscussionResponse.
        :type system: bool
        """
        self._system = system

    @property
    def noteable_id(self):
        r"""Gets the noteable_id of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 合并请求id或issue id。

        :return: The noteable_id of this UpdateMergeRequestDiscussionResponse.
        :rtype: int
        """
        return self._noteable_id

    @noteable_id.setter
    def noteable_id(self, noteable_id):
        r"""Sets the noteable_id of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 合并请求id或issue id。

        :param noteable_id: The noteable_id of this UpdateMergeRequestDiscussionResponse.
        :type noteable_id: int
        """
        self._noteable_id = noteable_id

    @property
    def noteable_type(self):
        r"""Gets the noteable_type of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 意见类型。

        :return: The noteable_type of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._noteable_type

    @noteable_type.setter
    def noteable_type(self, noteable_type):
        r"""Sets the noteable_type of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 意见类型。

        :param noteable_type: The noteable_type of this UpdateMergeRequestDiscussionResponse.
        :type noteable_type: str
        """
        self._noteable_type = noteable_type

    @property
    def commit_id(self):
        r"""Gets the commit_id of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 提交记录id。

        :return: The commit_id of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 提交记录id。

        :param commit_id: The commit_id of this UpdateMergeRequestDiscussionResponse.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def resolvable(self):
        r"""Gets the resolvable of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否需要解决。

        :return: The resolvable of this UpdateMergeRequestDiscussionResponse.
        :rtype: bool
        """
        return self._resolvable

    @resolvable.setter
    def resolvable(self, resolvable):
        r"""Sets the resolvable of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否需要解决。

        :param resolvable: The resolvable of this UpdateMergeRequestDiscussionResponse.
        :type resolvable: bool
        """
        self._resolvable = resolvable

    @property
    def is_reply(self):
        r"""Gets the is_reply of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否为回复。

        :return: The is_reply of this UpdateMergeRequestDiscussionResponse.
        :rtype: bool
        """
        return self._is_reply

    @is_reply.setter
    def is_reply(self, is_reply):
        r"""Sets the is_reply of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否为回复。

        :param is_reply: The is_reply of this UpdateMergeRequestDiscussionResponse.
        :type is_reply: bool
        """
        self._is_reply = is_reply

    @property
    def resolved_by(self):
        r"""Gets the resolved_by of this UpdateMergeRequestDiscussionResponse.

        :return: The resolved_by of this UpdateMergeRequestDiscussionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._resolved_by

    @resolved_by.setter
    def resolved_by(self, resolved_by):
        r"""Sets the resolved_by of this UpdateMergeRequestDiscussionResponse.

        :param resolved_by: The resolved_by of this UpdateMergeRequestDiscussionResponse.
        :type resolved_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._resolved_by = resolved_by

    @property
    def noteable_iid(self):
        r"""Gets the noteable_iid of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 合并请求iid或issue iid。

        :return: The noteable_iid of this UpdateMergeRequestDiscussionResponse.
        :rtype: int
        """
        return self._noteable_iid

    @noteable_iid.setter
    def noteable_iid(self, noteable_iid):
        r"""Sets the noteable_iid of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 合并请求iid或issue iid。

        :param noteable_iid: The noteable_iid of this UpdateMergeRequestDiscussionResponse.
        :type noteable_iid: int
        """
        self._noteable_iid = noteable_iid

    @property
    def discussion_id(self):
        r"""Gets the discussion_id of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 检视意见id(主评论和回复共用)。

        :return: The discussion_id of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._discussion_id

    @discussion_id.setter
    def discussion_id(self, discussion_id):
        r"""Sets the discussion_id of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 检视意见id(主评论和回复共用)。

        :param discussion_id: The discussion_id of this UpdateMergeRequestDiscussionResponse.
        :type discussion_id: str
        """
        self._discussion_id = discussion_id

    @property
    def repository(self):
        r"""Gets the repository of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 仓库路径。

        :return: The repository of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 仓库路径。

        :param repository: The repository of this UpdateMergeRequestDiscussionResponse.
        :type repository: str
        """
        self._repository = repository

    @property
    def diff_file(self):
        r"""Gets the diff_file of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 关联代码行所在文件的文件名。

        :return: The diff_file of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._diff_file

    @diff_file.setter
    def diff_file(self, diff_file):
        r"""Sets the diff_file of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 关联代码行所在文件的文件名。

        :param diff_file: The diff_file of this UpdateMergeRequestDiscussionResponse.
        :type diff_file: str
        """
        self._diff_file = diff_file

    @property
    def diff(self):
        r"""Gets the diff of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 关联代码行的代码片段。

        :return: The diff of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        r"""Sets the diff of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 关联代码行的代码片段。

        :param diff: The diff of this UpdateMergeRequestDiscussionResponse.
        :type diff: str
        """
        self._diff = diff

    @property
    def archived(self):
        r"""Gets the archived of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否已归档。

        :return: The archived of this UpdateMergeRequestDiscussionResponse.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否已归档。

        :param archived: The archived of this UpdateMergeRequestDiscussionResponse.
        :type archived: bool
        """
        self._archived = archived

    @property
    def review_categories(self):
        r"""Gets the review_categories of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 意见分类key。

        :return: The review_categories of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._review_categories

    @review_categories.setter
    def review_categories(self, review_categories):
        r"""Sets the review_categories of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 意见分类key。

        :param review_categories: The review_categories of this UpdateMergeRequestDiscussionResponse.
        :type review_categories: str
        """
        self._review_categories = review_categories

    @property
    def review_categories_cn(self):
        r"""Gets the review_categories_cn of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 意见分类中文名。

        :return: The review_categories_cn of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._review_categories_cn

    @review_categories_cn.setter
    def review_categories_cn(self, review_categories_cn):
        r"""Sets the review_categories_cn of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 意见分类中文名。

        :param review_categories_cn: The review_categories_cn of this UpdateMergeRequestDiscussionResponse.
        :type review_categories_cn: str
        """
        self._review_categories_cn = review_categories_cn

    @property
    def review_categories_en(self):
        r"""Gets the review_categories_en of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 合并请求版本信息。

        :return: The review_categories_en of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._review_categories_en

    @review_categories_en.setter
    def review_categories_en(self, review_categories_en):
        r"""Sets the review_categories_en of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 合并请求版本信息。

        :param review_categories_en: The review_categories_en of this UpdateMergeRequestDiscussionResponse.
        :type review_categories_en: str
        """
        self._review_categories_en = review_categories_en

    @property
    def review_modules(self):
        r"""Gets the review_modules of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 合并请求版本信息。

        :return: The review_modules of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        r"""Sets the review_modules of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 合并请求版本信息。

        :param review_modules: The review_modules of this UpdateMergeRequestDiscussionResponse.
        :type review_modules: str
        """
        self._review_modules = review_modules

    @property
    def severity(self):
        r"""Gets the severity of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 严重程度key。

        :return: The severity of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 严重程度key。

        :param severity: The severity of this UpdateMergeRequestDiscussionResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def severity_cn(self):
        r"""Gets the severity_cn of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命

        :return: The severity_cn of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._severity_cn

    @severity_cn.setter
    def severity_cn(self, severity_cn):
        r"""Sets the severity_cn of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命

        :param severity_cn: The severity_cn of this UpdateMergeRequestDiscussionResponse.
        :type severity_cn: str
        """
        self._severity_cn = severity_cn

    @property
    def severity_en(self):
        r"""Gets the severity_en of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 严重程度英文。

        :return: The severity_en of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._severity_en

    @severity_en.setter
    def severity_en(self, severity_en):
        r"""Sets the severity_en of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 严重程度英文。

        :param severity_en: The severity_en of this UpdateMergeRequestDiscussionResponse.
        :type severity_en: str
        """
        self._severity_en = severity_en

    @property
    def file_path(self):
        r"""Gets the file_path of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 文件路径(弃用)。

        :return: The file_path of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 文件路径(弃用)。

        :param file_path: The file_path of this UpdateMergeRequestDiscussionResponse.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def line(self):
        r"""Gets the line of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 行号(弃用)。

        :return: The line of this UpdateMergeRequestDiscussionResponse.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        r"""Sets the line of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 行号(弃用)。

        :param line: The line of this UpdateMergeRequestDiscussionResponse.
        :type line: str
        """
        self._line = line

    @property
    def assignee(self):
        r"""Gets the assignee of this UpdateMergeRequestDiscussionResponse.

        :return: The assignee of this UpdateMergeRequestDiscussionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this UpdateMergeRequestDiscussionResponse.

        :param assignee: The assignee of this UpdateMergeRequestDiscussionResponse.
        :type assignee: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._assignee = assignee

    @property
    def proposer(self):
        r"""Gets the proposer of this UpdateMergeRequestDiscussionResponse.

        :return: The proposer of this UpdateMergeRequestDiscussionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._proposer

    @proposer.setter
    def proposer(self, proposer):
        r"""Sets the proposer of this UpdateMergeRequestDiscussionResponse.

        :param proposer: The proposer of this UpdateMergeRequestDiscussionResponse.
        :type proposer: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._proposer = proposer

    @property
    def position(self):
        r"""Gets the position of this UpdateMergeRequestDiscussionResponse.

        :return: The position of this UpdateMergeRequestDiscussionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.PositionDto`
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this UpdateMergeRequestDiscussionResponse.

        :param position: The position of this UpdateMergeRequestDiscussionResponse.
        :type position: :class:`huaweicloudsdkcodehub.v4.PositionDto`
        """
        self._position = position

    @property
    def resolved(self):
        r"""Gets the resolved of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否已解决。

        :return: The resolved of this UpdateMergeRequestDiscussionResponse.
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        r"""Sets the resolved of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否已解决。

        :param resolved: The resolved of this UpdateMergeRequestDiscussionResponse.
        :type resolved: bool
        """
        self._resolved = resolved

    @property
    def is_outdated(self):
        r"""Gets the is_outdated of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否已过期。

        :return: The is_outdated of this UpdateMergeRequestDiscussionResponse.
        :rtype: bool
        """
        return self._is_outdated

    @is_outdated.setter
    def is_outdated(self, is_outdated):
        r"""Sets the is_outdated of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 是否已过期。

        :param is_outdated: The is_outdated of this UpdateMergeRequestDiscussionResponse.
        :type is_outdated: bool
        """
        self._is_outdated = is_outdated

    @property
    def moderation_result(self):
        r"""Gets the moderation_result of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 内容审核结果。

        :return: The moderation_result of this UpdateMergeRequestDiscussionResponse.
        :rtype: bool
        """
        return self._moderation_result

    @moderation_result.setter
    def moderation_result(self, moderation_result):
        r"""Sets the moderation_result of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 内容审核结果。

        :param moderation_result: The moderation_result of this UpdateMergeRequestDiscussionResponse.
        :type moderation_result: bool
        """
        self._moderation_result = moderation_result

    @property
    def moderation_time(self):
        r"""Gets the moderation_time of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 内容审核时间。

        :return: The moderation_time of this UpdateMergeRequestDiscussionResponse.
        :rtype: int
        """
        return self._moderation_time

    @moderation_time.setter
    def moderation_time(self, moderation_time):
        r"""Sets the moderation_time of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 内容审核时间。

        :param moderation_time: The moderation_time of this UpdateMergeRequestDiscussionResponse.
        :type moderation_time: int
        """
        self._moderation_time = moderation_time

    @property
    def moderation_status(self):
        r"""Gets the moderation_status of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 内容审核状态。

        :return: The moderation_status of this UpdateMergeRequestDiscussionResponse.
        :rtype: int
        """
        return self._moderation_status

    @moderation_status.setter
    def moderation_status(self, moderation_status):
        r"""Sets the moderation_status of this UpdateMergeRequestDiscussionResponse.

        **参数解释：** 内容审核状态。

        :param moderation_status: The moderation_status of this UpdateMergeRequestDiscussionResponse.
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
        if not isinstance(other, UpdateMergeRequestDiscussionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
