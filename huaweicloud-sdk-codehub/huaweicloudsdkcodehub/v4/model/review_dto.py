# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReviewDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'assignee': 'UserBasicDto',
        'author': 'UserBasicDto',
        'note': 'str',
        'created_at': 'str',
        'is_reply': 'bool',
        'resolved_by': 'UserBasicDto',
        'discussion_id': 'str',
        'repository_path': 'str',
        'repository_id': 'int',
        'review_categories': 'str',
        'review_categories_cn': 'str',
        'review_categories_en': 'str',
        'review_modules': 'str',
        'severity': 'str',
        'severity_cn': 'str',
        'severity_en': 'str',
        'proposer': 'UserBasicDto',
        'reviewer': 'UserBasicDto',
        'resolved': 'bool',
        'resolved_at': 'str',
        'link': 'str',
        'moderation_result': 'bool',
        'moderation_time': 'int',
        'moderation_status': 'int',
        'merge_request_id': 'int',
        'merge_request_iid': 'int',
        'merge_request_title': 'str',
        'merge_request_state': 'str',
        'commit_id': 'str'
    }

    attribute_map = {
        'assignee': 'assignee',
        'author': 'author',
        'note': 'note',
        'created_at': 'created_at',
        'is_reply': 'is_reply',
        'resolved_by': 'resolved_by',
        'discussion_id': 'discussion_id',
        'repository_path': 'repository_path',
        'repository_id': 'repository_id',
        'review_categories': 'review_categories',
        'review_categories_cn': 'review_categories_cn',
        'review_categories_en': 'review_categories_en',
        'review_modules': 'review_modules',
        'severity': 'severity',
        'severity_cn': 'severity_cn',
        'severity_en': 'severity_en',
        'proposer': 'proposer',
        'reviewer': 'reviewer',
        'resolved': 'resolved',
        'resolved_at': 'resolved_at',
        'link': 'link',
        'moderation_result': 'moderation_result',
        'moderation_time': 'moderation_time',
        'moderation_status': 'moderation_status',
        'merge_request_id': 'merge_request_id',
        'merge_request_iid': 'merge_request_iid',
        'merge_request_title': 'merge_request_title',
        'merge_request_state': 'merge_request_state',
        'commit_id': 'commit_id'
    }

    def __init__(self, assignee=None, author=None, note=None, created_at=None, is_reply=None, resolved_by=None, discussion_id=None, repository_path=None, repository_id=None, review_categories=None, review_categories_cn=None, review_categories_en=None, review_modules=None, severity=None, severity_cn=None, severity_en=None, proposer=None, reviewer=None, resolved=None, resolved_at=None, link=None, moderation_result=None, moderation_time=None, moderation_status=None, merge_request_id=None, merge_request_iid=None, merge_request_title=None, merge_request_state=None, commit_id=None):
        r"""ReviewDto

        The model defined in huaweicloud sdk

        :param assignee: 
        :type assignee: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param note: **参数解释：** 评论内容。
        :type note: str
        :param created_at: **参数解释：** 创建时间。
        :type created_at: str
        :param is_reply: **参数解释：** 是否为回复。
        :type is_reply: bool
        :param resolved_by: 
        :type resolved_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param discussion_id: **参数解释：** 检视意见id(主评论和回复共用)。
        :type discussion_id: str
        :param repository_path: **参数解释：** 仓库路径。
        :type repository_path: str
        :param repository_id: **参数解释：** 仓库id。
        :type repository_id: int
        :param review_categories: **参数解释：** 意见分类key。
        :type review_categories: str
        :param review_categories_cn: **参数解释：** 意见分类中文。
        :type review_categories_cn: str
        :param review_categories_en: **参数解释：** 意见分类英文。
        :type review_categories_en: str
        :param review_modules: **参数解释：** 检视意见模块。
        :type review_modules: str
        :param severity: **参数解释：** 严重程度key。
        :type severity: str
        :param severity_cn: **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命
        :type severity_cn: str
        :param severity_en: **参数解释：** 严重程度英文。
        :type severity_en: str
        :param proposer: 
        :type proposer: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param reviewer: 
        :type reviewer: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param resolved: **参数解释：** 是否已解决。
        :type resolved: bool
        :param resolved_at: **参数解释：** 解决时间。
        :type resolved_at: str
        :param link: **参数解释：** 合并请求或commit链接。
        :type link: str
        :param moderation_result: **参数解释：** 内容审核结果。
        :type moderation_result: bool
        :param moderation_time: **参数解释：** 内容审核时间。
        :type moderation_time: int
        :param moderation_status: **参数解释：** 内容审核状态。
        :type moderation_status: int
        :param merge_request_id: **参数解释：** 合并请求id(noteable_type&#x3D;MergRequest时返回)。
        :type merge_request_id: int
        :param merge_request_iid: **参数解释：** 合并请求iid(noteable_type&#x3D;MergRequest时返回)。
        :type merge_request_iid: int
        :param merge_request_title: **参数解释：** 合并请求标题(noteable_type&#x3D;MergRequest时返回)。
        :type merge_request_title: str
        :param merge_request_state: **参数解释：** 合并请求状态(noteable_type&#x3D;MergRequest时返回)。
        :type merge_request_state: str
        :param commit_id: **参数解释：** commit id(noteable_type&#x3D;Commit时返回)。
        :type commit_id: str
        """
        
        

        self._assignee = None
        self._author = None
        self._note = None
        self._created_at = None
        self._is_reply = None
        self._resolved_by = None
        self._discussion_id = None
        self._repository_path = None
        self._repository_id = None
        self._review_categories = None
        self._review_categories_cn = None
        self._review_categories_en = None
        self._review_modules = None
        self._severity = None
        self._severity_cn = None
        self._severity_en = None
        self._proposer = None
        self._reviewer = None
        self._resolved = None
        self._resolved_at = None
        self._link = None
        self._moderation_result = None
        self._moderation_time = None
        self._moderation_status = None
        self._merge_request_id = None
        self._merge_request_iid = None
        self._merge_request_title = None
        self._merge_request_state = None
        self._commit_id = None
        self.discriminator = None

        if assignee is not None:
            self.assignee = assignee
        if author is not None:
            self.author = author
        if note is not None:
            self.note = note
        if created_at is not None:
            self.created_at = created_at
        if is_reply is not None:
            self.is_reply = is_reply
        if resolved_by is not None:
            self.resolved_by = resolved_by
        if discussion_id is not None:
            self.discussion_id = discussion_id
        if repository_path is not None:
            self.repository_path = repository_path
        if repository_id is not None:
            self.repository_id = repository_id
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
        if proposer is not None:
            self.proposer = proposer
        if reviewer is not None:
            self.reviewer = reviewer
        if resolved is not None:
            self.resolved = resolved
        if resolved_at is not None:
            self.resolved_at = resolved_at
        if link is not None:
            self.link = link
        if moderation_result is not None:
            self.moderation_result = moderation_result
        if moderation_time is not None:
            self.moderation_time = moderation_time
        if moderation_status is not None:
            self.moderation_status = moderation_status
        if merge_request_id is not None:
            self.merge_request_id = merge_request_id
        if merge_request_iid is not None:
            self.merge_request_iid = merge_request_iid
        if merge_request_title is not None:
            self.merge_request_title = merge_request_title
        if merge_request_state is not None:
            self.merge_request_state = merge_request_state
        if commit_id is not None:
            self.commit_id = commit_id

    @property
    def assignee(self):
        r"""Gets the assignee of this ReviewDto.

        :return: The assignee of this ReviewDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this ReviewDto.

        :param assignee: The assignee of this ReviewDto.
        :type assignee: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._assignee = assignee

    @property
    def author(self):
        r"""Gets the author of this ReviewDto.

        :return: The author of this ReviewDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        r"""Sets the author of this ReviewDto.

        :param author: The author of this ReviewDto.
        :type author: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._author = author

    @property
    def note(self):
        r"""Gets the note of this ReviewDto.

        **参数解释：** 评论内容。

        :return: The note of this ReviewDto.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        r"""Sets the note of this ReviewDto.

        **参数解释：** 评论内容。

        :param note: The note of this ReviewDto.
        :type note: str
        """
        self._note = note

    @property
    def created_at(self):
        r"""Gets the created_at of this ReviewDto.

        **参数解释：** 创建时间。

        :return: The created_at of this ReviewDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ReviewDto.

        **参数解释：** 创建时间。

        :param created_at: The created_at of this ReviewDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def is_reply(self):
        r"""Gets the is_reply of this ReviewDto.

        **参数解释：** 是否为回复。

        :return: The is_reply of this ReviewDto.
        :rtype: bool
        """
        return self._is_reply

    @is_reply.setter
    def is_reply(self, is_reply):
        r"""Sets the is_reply of this ReviewDto.

        **参数解释：** 是否为回复。

        :param is_reply: The is_reply of this ReviewDto.
        :type is_reply: bool
        """
        self._is_reply = is_reply

    @property
    def resolved_by(self):
        r"""Gets the resolved_by of this ReviewDto.

        :return: The resolved_by of this ReviewDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._resolved_by

    @resolved_by.setter
    def resolved_by(self, resolved_by):
        r"""Sets the resolved_by of this ReviewDto.

        :param resolved_by: The resolved_by of this ReviewDto.
        :type resolved_by: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._resolved_by = resolved_by

    @property
    def discussion_id(self):
        r"""Gets the discussion_id of this ReviewDto.

        **参数解释：** 检视意见id(主评论和回复共用)。

        :return: The discussion_id of this ReviewDto.
        :rtype: str
        """
        return self._discussion_id

    @discussion_id.setter
    def discussion_id(self, discussion_id):
        r"""Sets the discussion_id of this ReviewDto.

        **参数解释：** 检视意见id(主评论和回复共用)。

        :param discussion_id: The discussion_id of this ReviewDto.
        :type discussion_id: str
        """
        self._discussion_id = discussion_id

    @property
    def repository_path(self):
        r"""Gets the repository_path of this ReviewDto.

        **参数解释：** 仓库路径。

        :return: The repository_path of this ReviewDto.
        :rtype: str
        """
        return self._repository_path

    @repository_path.setter
    def repository_path(self, repository_path):
        r"""Sets the repository_path of this ReviewDto.

        **参数解释：** 仓库路径。

        :param repository_path: The repository_path of this ReviewDto.
        :type repository_path: str
        """
        self._repository_path = repository_path

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ReviewDto.

        **参数解释：** 仓库id。

        :return: The repository_id of this ReviewDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ReviewDto.

        **参数解释：** 仓库id。

        :param repository_id: The repository_id of this ReviewDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def review_categories(self):
        r"""Gets the review_categories of this ReviewDto.

        **参数解释：** 意见分类key。

        :return: The review_categories of this ReviewDto.
        :rtype: str
        """
        return self._review_categories

    @review_categories.setter
    def review_categories(self, review_categories):
        r"""Sets the review_categories of this ReviewDto.

        **参数解释：** 意见分类key。

        :param review_categories: The review_categories of this ReviewDto.
        :type review_categories: str
        """
        self._review_categories = review_categories

    @property
    def review_categories_cn(self):
        r"""Gets the review_categories_cn of this ReviewDto.

        **参数解释：** 意见分类中文。

        :return: The review_categories_cn of this ReviewDto.
        :rtype: str
        """
        return self._review_categories_cn

    @review_categories_cn.setter
    def review_categories_cn(self, review_categories_cn):
        r"""Sets the review_categories_cn of this ReviewDto.

        **参数解释：** 意见分类中文。

        :param review_categories_cn: The review_categories_cn of this ReviewDto.
        :type review_categories_cn: str
        """
        self._review_categories_cn = review_categories_cn

    @property
    def review_categories_en(self):
        r"""Gets the review_categories_en of this ReviewDto.

        **参数解释：** 意见分类英文。

        :return: The review_categories_en of this ReviewDto.
        :rtype: str
        """
        return self._review_categories_en

    @review_categories_en.setter
    def review_categories_en(self, review_categories_en):
        r"""Sets the review_categories_en of this ReviewDto.

        **参数解释：** 意见分类英文。

        :param review_categories_en: The review_categories_en of this ReviewDto.
        :type review_categories_en: str
        """
        self._review_categories_en = review_categories_en

    @property
    def review_modules(self):
        r"""Gets the review_modules of this ReviewDto.

        **参数解释：** 检视意见模块。

        :return: The review_modules of this ReviewDto.
        :rtype: str
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        r"""Sets the review_modules of this ReviewDto.

        **参数解释：** 检视意见模块。

        :param review_modules: The review_modules of this ReviewDto.
        :type review_modules: str
        """
        self._review_modules = review_modules

    @property
    def severity(self):
        r"""Gets the severity of this ReviewDto.

        **参数解释：** 严重程度key。

        :return: The severity of this ReviewDto.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ReviewDto.

        **参数解释：** 严重程度key。

        :param severity: The severity of this ReviewDto.
        :type severity: str
        """
        self._severity = severity

    @property
    def severity_cn(self):
        r"""Gets the severity_cn of this ReviewDto.

        **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命

        :return: The severity_cn of this ReviewDto.
        :rtype: str
        """
        return self._severity_cn

    @severity_cn.setter
    def severity_cn(self, severity_cn):
        r"""Sets the severity_cn of this ReviewDto.

        **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命

        :param severity_cn: The severity_cn of this ReviewDto.
        :type severity_cn: str
        """
        self._severity_cn = severity_cn

    @property
    def severity_en(self):
        r"""Gets the severity_en of this ReviewDto.

        **参数解释：** 严重程度英文。

        :return: The severity_en of this ReviewDto.
        :rtype: str
        """
        return self._severity_en

    @severity_en.setter
    def severity_en(self, severity_en):
        r"""Sets the severity_en of this ReviewDto.

        **参数解释：** 严重程度英文。

        :param severity_en: The severity_en of this ReviewDto.
        :type severity_en: str
        """
        self._severity_en = severity_en

    @property
    def proposer(self):
        r"""Gets the proposer of this ReviewDto.

        :return: The proposer of this ReviewDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._proposer

    @proposer.setter
    def proposer(self, proposer):
        r"""Sets the proposer of this ReviewDto.

        :param proposer: The proposer of this ReviewDto.
        :type proposer: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._proposer = proposer

    @property
    def reviewer(self):
        r"""Gets the reviewer of this ReviewDto.

        :return: The reviewer of this ReviewDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        r"""Sets the reviewer of this ReviewDto.

        :param reviewer: The reviewer of this ReviewDto.
        :type reviewer: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._reviewer = reviewer

    @property
    def resolved(self):
        r"""Gets the resolved of this ReviewDto.

        **参数解释：** 是否已解决。

        :return: The resolved of this ReviewDto.
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        r"""Sets the resolved of this ReviewDto.

        **参数解释：** 是否已解决。

        :param resolved: The resolved of this ReviewDto.
        :type resolved: bool
        """
        self._resolved = resolved

    @property
    def resolved_at(self):
        r"""Gets the resolved_at of this ReviewDto.

        **参数解释：** 解决时间。

        :return: The resolved_at of this ReviewDto.
        :rtype: str
        """
        return self._resolved_at

    @resolved_at.setter
    def resolved_at(self, resolved_at):
        r"""Sets the resolved_at of this ReviewDto.

        **参数解释：** 解决时间。

        :param resolved_at: The resolved_at of this ReviewDto.
        :type resolved_at: str
        """
        self._resolved_at = resolved_at

    @property
    def link(self):
        r"""Gets the link of this ReviewDto.

        **参数解释：** 合并请求或commit链接。

        :return: The link of this ReviewDto.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        r"""Sets the link of this ReviewDto.

        **参数解释：** 合并请求或commit链接。

        :param link: The link of this ReviewDto.
        :type link: str
        """
        self._link = link

    @property
    def moderation_result(self):
        r"""Gets the moderation_result of this ReviewDto.

        **参数解释：** 内容审核结果。

        :return: The moderation_result of this ReviewDto.
        :rtype: bool
        """
        return self._moderation_result

    @moderation_result.setter
    def moderation_result(self, moderation_result):
        r"""Sets the moderation_result of this ReviewDto.

        **参数解释：** 内容审核结果。

        :param moderation_result: The moderation_result of this ReviewDto.
        :type moderation_result: bool
        """
        self._moderation_result = moderation_result

    @property
    def moderation_time(self):
        r"""Gets the moderation_time of this ReviewDto.

        **参数解释：** 内容审核时间。

        :return: The moderation_time of this ReviewDto.
        :rtype: int
        """
        return self._moderation_time

    @moderation_time.setter
    def moderation_time(self, moderation_time):
        r"""Sets the moderation_time of this ReviewDto.

        **参数解释：** 内容审核时间。

        :param moderation_time: The moderation_time of this ReviewDto.
        :type moderation_time: int
        """
        self._moderation_time = moderation_time

    @property
    def moderation_status(self):
        r"""Gets the moderation_status of this ReviewDto.

        **参数解释：** 内容审核状态。

        :return: The moderation_status of this ReviewDto.
        :rtype: int
        """
        return self._moderation_status

    @moderation_status.setter
    def moderation_status(self, moderation_status):
        r"""Sets the moderation_status of this ReviewDto.

        **参数解释：** 内容审核状态。

        :param moderation_status: The moderation_status of this ReviewDto.
        :type moderation_status: int
        """
        self._moderation_status = moderation_status

    @property
    def merge_request_id(self):
        r"""Gets the merge_request_id of this ReviewDto.

        **参数解释：** 合并请求id(noteable_type=MergRequest时返回)。

        :return: The merge_request_id of this ReviewDto.
        :rtype: int
        """
        return self._merge_request_id

    @merge_request_id.setter
    def merge_request_id(self, merge_request_id):
        r"""Sets the merge_request_id of this ReviewDto.

        **参数解释：** 合并请求id(noteable_type=MergRequest时返回)。

        :param merge_request_id: The merge_request_id of this ReviewDto.
        :type merge_request_id: int
        """
        self._merge_request_id = merge_request_id

    @property
    def merge_request_iid(self):
        r"""Gets the merge_request_iid of this ReviewDto.

        **参数解释：** 合并请求iid(noteable_type=MergRequest时返回)。

        :return: The merge_request_iid of this ReviewDto.
        :rtype: int
        """
        return self._merge_request_iid

    @merge_request_iid.setter
    def merge_request_iid(self, merge_request_iid):
        r"""Sets the merge_request_iid of this ReviewDto.

        **参数解释：** 合并请求iid(noteable_type=MergRequest时返回)。

        :param merge_request_iid: The merge_request_iid of this ReviewDto.
        :type merge_request_iid: int
        """
        self._merge_request_iid = merge_request_iid

    @property
    def merge_request_title(self):
        r"""Gets the merge_request_title of this ReviewDto.

        **参数解释：** 合并请求标题(noteable_type=MergRequest时返回)。

        :return: The merge_request_title of this ReviewDto.
        :rtype: str
        """
        return self._merge_request_title

    @merge_request_title.setter
    def merge_request_title(self, merge_request_title):
        r"""Sets the merge_request_title of this ReviewDto.

        **参数解释：** 合并请求标题(noteable_type=MergRequest时返回)。

        :param merge_request_title: The merge_request_title of this ReviewDto.
        :type merge_request_title: str
        """
        self._merge_request_title = merge_request_title

    @property
    def merge_request_state(self):
        r"""Gets the merge_request_state of this ReviewDto.

        **参数解释：** 合并请求状态(noteable_type=MergRequest时返回)。

        :return: The merge_request_state of this ReviewDto.
        :rtype: str
        """
        return self._merge_request_state

    @merge_request_state.setter
    def merge_request_state(self, merge_request_state):
        r"""Sets the merge_request_state of this ReviewDto.

        **参数解释：** 合并请求状态(noteable_type=MergRequest时返回)。

        :param merge_request_state: The merge_request_state of this ReviewDto.
        :type merge_request_state: str
        """
        self._merge_request_state = merge_request_state

    @property
    def commit_id(self):
        r"""Gets the commit_id of this ReviewDto.

        **参数解释：** commit id(noteable_type=Commit时返回)。

        :return: The commit_id of this ReviewDto.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this ReviewDto.

        **参数解释：** commit id(noteable_type=Commit时返回)。

        :param commit_id: The commit_id of this ReviewDto.
        :type commit_id: str
        """
        self._commit_id = commit_id

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
        if not isinstance(other, ReviewDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
