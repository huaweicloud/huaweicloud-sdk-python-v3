# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitDiscussionDto:

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
        'individual_note': 'bool',
        'notes': 'list[CommitNoteDto]',
        'repository_id': 'int',
        'noteable_type': 'str',
        'commit_id': 'str',
        'repository_full_path': 'str',
        'a_mode': 'str',
        'b_mode': 'str',
        'deleted_file': 'bool',
        'new_file': 'bool',
        'diff_file': 'bool',
        'added_lines': 'int',
        'removed_lines': 'int',
        'resolved': 'bool',
        'archived': 'bool',
        'review_categories': 'str',
        'review_categories_cn': 'str',
        'review_categories_en': 'str',
        'review_modules': 'str',
        'severity': 'str',
        'severity_cn': 'str',
        'severity_en': 'str',
        'assignee': 'UserBasicDto',
        'proposer': 'UserBasicDto'
    }

    attribute_map = {
        'id': 'id',
        'individual_note': 'individual_note',
        'notes': 'notes',
        'repository_id': 'repository_id',
        'noteable_type': 'noteable_type',
        'commit_id': 'commit_id',
        'repository_full_path': 'repository_full_path',
        'a_mode': 'a_mode',
        'b_mode': 'b_mode',
        'deleted_file': 'deleted_file',
        'new_file': 'new_file',
        'diff_file': 'diff_file',
        'added_lines': 'added_lines',
        'removed_lines': 'removed_lines',
        'resolved': 'resolved',
        'archived': 'archived',
        'review_categories': 'review_categories',
        'review_categories_cn': 'review_categories_cn',
        'review_categories_en': 'review_categories_en',
        'review_modules': 'review_modules',
        'severity': 'severity',
        'severity_cn': 'severity_cn',
        'severity_en': 'severity_en',
        'assignee': 'assignee',
        'proposer': 'proposer'
    }

    def __init__(self, id=None, individual_note=None, notes=None, repository_id=None, noteable_type=None, commit_id=None, repository_full_path=None, a_mode=None, b_mode=None, deleted_file=None, new_file=None, diff_file=None, added_lines=None, removed_lines=None, resolved=None, archived=None, review_categories=None, review_categories_cn=None, review_categories_en=None, review_modules=None, severity=None, severity_cn=None, severity_en=None, assignee=None, proposer=None):
        r"""CommitDiscussionDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 检视意见id(主评论和回复共用)。
        :type id: str
        :param individual_note: **参数解释：** 个人检视意见(不需要解决)。
        :type individual_note: bool
        :param notes: **参数解释：** 评论列表(主评+回复)。
        :type notes: list[:class:`huaweicloudsdkcodeartsrepo.v4.CommitNoteDto`]
        :param repository_id: **参数解释：** 仓库id。
        :type repository_id: int
        :param noteable_type: **参数解释：** 意见类型。
        :type noteable_type: str
        :param commit_id: **参数解释：** 提交记录id。
        :type commit_id: str
        :param repository_full_path: **参数解释：** 仓库路径。
        :type repository_full_path: str
        :param a_mode: **参数解释：** 文件旧权限(默认100644)。
        :type a_mode: str
        :param b_mode: **参数解释：** 文件新权限(默认100644)。
        :type b_mode: str
        :param deleted_file: **参数解释：** 是否为删除文件。
        :type deleted_file: bool
        :param new_file: **参数解释：** 是否为新增文件。
        :type new_file: bool
        :param diff_file: **参数解释：** 是否为修改文件。
        :type diff_file: bool
        :param added_lines: **参数解释：** 检视意见所在文件的新增行数量。
        :type added_lines: int
        :param removed_lines: **参数解释：** 检视意见所在文件的删除行数量。
        :type removed_lines: int
        :param resolved: **参数解释：** 是否已解决。
        :type resolved: bool
        :param archived: **参数解释：** 是否已归档。
        :type archived: bool
        :param review_categories: **参数解释：** 意见分类key。
        :type review_categories: str
        :param review_categories_cn: **参数解释：** 意见分类中文。
        :type review_categories_cn: str
        :param review_categories_en: **参数解释：** 意见分类英文。
        :type review_categories_en: str
        :param review_modules: **参数解释：** 意见模块。
        :type review_modules: str
        :param severity: **参数解释：** 严重程度key。
        :type severity: str
        :param severity_cn: **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命
        :type severity_cn: str
        :param severity_en: **参数解释：** 严重程度英文。
        :type severity_en: str
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkcodeartsrepo.v4.UserBasicDto`
        :param proposer: 
        :type proposer: :class:`huaweicloudsdkcodeartsrepo.v4.UserBasicDto`
        """
        
        

        self._id = None
        self._individual_note = None
        self._notes = None
        self._repository_id = None
        self._noteable_type = None
        self._commit_id = None
        self._repository_full_path = None
        self._a_mode = None
        self._b_mode = None
        self._deleted_file = None
        self._new_file = None
        self._diff_file = None
        self._added_lines = None
        self._removed_lines = None
        self._resolved = None
        self._archived = None
        self._review_categories = None
        self._review_categories_cn = None
        self._review_categories_en = None
        self._review_modules = None
        self._severity = None
        self._severity_cn = None
        self._severity_en = None
        self._assignee = None
        self._proposer = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if individual_note is not None:
            self.individual_note = individual_note
        if notes is not None:
            self.notes = notes
        if repository_id is not None:
            self.repository_id = repository_id
        if noteable_type is not None:
            self.noteable_type = noteable_type
        if commit_id is not None:
            self.commit_id = commit_id
        if repository_full_path is not None:
            self.repository_full_path = repository_full_path
        if a_mode is not None:
            self.a_mode = a_mode
        if b_mode is not None:
            self.b_mode = b_mode
        if deleted_file is not None:
            self.deleted_file = deleted_file
        if new_file is not None:
            self.new_file = new_file
        if diff_file is not None:
            self.diff_file = diff_file
        if added_lines is not None:
            self.added_lines = added_lines
        if removed_lines is not None:
            self.removed_lines = removed_lines
        if resolved is not None:
            self.resolved = resolved
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
        if assignee is not None:
            self.assignee = assignee
        if proposer is not None:
            self.proposer = proposer

    @property
    def id(self):
        r"""Gets the id of this CommitDiscussionDto.

        **参数解释：** 检视意见id(主评论和回复共用)。

        :return: The id of this CommitDiscussionDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CommitDiscussionDto.

        **参数解释：** 检视意见id(主评论和回复共用)。

        :param id: The id of this CommitDiscussionDto.
        :type id: str
        """
        self._id = id

    @property
    def individual_note(self):
        r"""Gets the individual_note of this CommitDiscussionDto.

        **参数解释：** 个人检视意见(不需要解决)。

        :return: The individual_note of this CommitDiscussionDto.
        :rtype: bool
        """
        return self._individual_note

    @individual_note.setter
    def individual_note(self, individual_note):
        r"""Sets the individual_note of this CommitDiscussionDto.

        **参数解释：** 个人检视意见(不需要解决)。

        :param individual_note: The individual_note of this CommitDiscussionDto.
        :type individual_note: bool
        """
        self._individual_note = individual_note

    @property
    def notes(self):
        r"""Gets the notes of this CommitDiscussionDto.

        **参数解释：** 评论列表(主评+回复)。

        :return: The notes of this CommitDiscussionDto.
        :rtype: list[:class:`huaweicloudsdkcodeartsrepo.v4.CommitNoteDto`]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this CommitDiscussionDto.

        **参数解释：** 评论列表(主评+回复)。

        :param notes: The notes of this CommitDiscussionDto.
        :type notes: list[:class:`huaweicloudsdkcodeartsrepo.v4.CommitNoteDto`]
        """
        self._notes = notes

    @property
    def repository_id(self):
        r"""Gets the repository_id of this CommitDiscussionDto.

        **参数解释：** 仓库id。

        :return: The repository_id of this CommitDiscussionDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this CommitDiscussionDto.

        **参数解释：** 仓库id。

        :param repository_id: The repository_id of this CommitDiscussionDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def noteable_type(self):
        r"""Gets the noteable_type of this CommitDiscussionDto.

        **参数解释：** 意见类型。

        :return: The noteable_type of this CommitDiscussionDto.
        :rtype: str
        """
        return self._noteable_type

    @noteable_type.setter
    def noteable_type(self, noteable_type):
        r"""Sets the noteable_type of this CommitDiscussionDto.

        **参数解释：** 意见类型。

        :param noteable_type: The noteable_type of this CommitDiscussionDto.
        :type noteable_type: str
        """
        self._noteable_type = noteable_type

    @property
    def commit_id(self):
        r"""Gets the commit_id of this CommitDiscussionDto.

        **参数解释：** 提交记录id。

        :return: The commit_id of this CommitDiscussionDto.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this CommitDiscussionDto.

        **参数解释：** 提交记录id。

        :param commit_id: The commit_id of this CommitDiscussionDto.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def repository_full_path(self):
        r"""Gets the repository_full_path of this CommitDiscussionDto.

        **参数解释：** 仓库路径。

        :return: The repository_full_path of this CommitDiscussionDto.
        :rtype: str
        """
        return self._repository_full_path

    @repository_full_path.setter
    def repository_full_path(self, repository_full_path):
        r"""Sets the repository_full_path of this CommitDiscussionDto.

        **参数解释：** 仓库路径。

        :param repository_full_path: The repository_full_path of this CommitDiscussionDto.
        :type repository_full_path: str
        """
        self._repository_full_path = repository_full_path

    @property
    def a_mode(self):
        r"""Gets the a_mode of this CommitDiscussionDto.

        **参数解释：** 文件旧权限(默认100644)。

        :return: The a_mode of this CommitDiscussionDto.
        :rtype: str
        """
        return self._a_mode

    @a_mode.setter
    def a_mode(self, a_mode):
        r"""Sets the a_mode of this CommitDiscussionDto.

        **参数解释：** 文件旧权限(默认100644)。

        :param a_mode: The a_mode of this CommitDiscussionDto.
        :type a_mode: str
        """
        self._a_mode = a_mode

    @property
    def b_mode(self):
        r"""Gets the b_mode of this CommitDiscussionDto.

        **参数解释：** 文件新权限(默认100644)。

        :return: The b_mode of this CommitDiscussionDto.
        :rtype: str
        """
        return self._b_mode

    @b_mode.setter
    def b_mode(self, b_mode):
        r"""Sets the b_mode of this CommitDiscussionDto.

        **参数解释：** 文件新权限(默认100644)。

        :param b_mode: The b_mode of this CommitDiscussionDto.
        :type b_mode: str
        """
        self._b_mode = b_mode

    @property
    def deleted_file(self):
        r"""Gets the deleted_file of this CommitDiscussionDto.

        **参数解释：** 是否为删除文件。

        :return: The deleted_file of this CommitDiscussionDto.
        :rtype: bool
        """
        return self._deleted_file

    @deleted_file.setter
    def deleted_file(self, deleted_file):
        r"""Sets the deleted_file of this CommitDiscussionDto.

        **参数解释：** 是否为删除文件。

        :param deleted_file: The deleted_file of this CommitDiscussionDto.
        :type deleted_file: bool
        """
        self._deleted_file = deleted_file

    @property
    def new_file(self):
        r"""Gets the new_file of this CommitDiscussionDto.

        **参数解释：** 是否为新增文件。

        :return: The new_file of this CommitDiscussionDto.
        :rtype: bool
        """
        return self._new_file

    @new_file.setter
    def new_file(self, new_file):
        r"""Sets the new_file of this CommitDiscussionDto.

        **参数解释：** 是否为新增文件。

        :param new_file: The new_file of this CommitDiscussionDto.
        :type new_file: bool
        """
        self._new_file = new_file

    @property
    def diff_file(self):
        r"""Gets the diff_file of this CommitDiscussionDto.

        **参数解释：** 是否为修改文件。

        :return: The diff_file of this CommitDiscussionDto.
        :rtype: bool
        """
        return self._diff_file

    @diff_file.setter
    def diff_file(self, diff_file):
        r"""Sets the diff_file of this CommitDiscussionDto.

        **参数解释：** 是否为修改文件。

        :param diff_file: The diff_file of this CommitDiscussionDto.
        :type diff_file: bool
        """
        self._diff_file = diff_file

    @property
    def added_lines(self):
        r"""Gets the added_lines of this CommitDiscussionDto.

        **参数解释：** 检视意见所在文件的新增行数量。

        :return: The added_lines of this CommitDiscussionDto.
        :rtype: int
        """
        return self._added_lines

    @added_lines.setter
    def added_lines(self, added_lines):
        r"""Sets the added_lines of this CommitDiscussionDto.

        **参数解释：** 检视意见所在文件的新增行数量。

        :param added_lines: The added_lines of this CommitDiscussionDto.
        :type added_lines: int
        """
        self._added_lines = added_lines

    @property
    def removed_lines(self):
        r"""Gets the removed_lines of this CommitDiscussionDto.

        **参数解释：** 检视意见所在文件的删除行数量。

        :return: The removed_lines of this CommitDiscussionDto.
        :rtype: int
        """
        return self._removed_lines

    @removed_lines.setter
    def removed_lines(self, removed_lines):
        r"""Sets the removed_lines of this CommitDiscussionDto.

        **参数解释：** 检视意见所在文件的删除行数量。

        :param removed_lines: The removed_lines of this CommitDiscussionDto.
        :type removed_lines: int
        """
        self._removed_lines = removed_lines

    @property
    def resolved(self):
        r"""Gets the resolved of this CommitDiscussionDto.

        **参数解释：** 是否已解决。

        :return: The resolved of this CommitDiscussionDto.
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        r"""Sets the resolved of this CommitDiscussionDto.

        **参数解释：** 是否已解决。

        :param resolved: The resolved of this CommitDiscussionDto.
        :type resolved: bool
        """
        self._resolved = resolved

    @property
    def archived(self):
        r"""Gets the archived of this CommitDiscussionDto.

        **参数解释：** 是否已归档。

        :return: The archived of this CommitDiscussionDto.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this CommitDiscussionDto.

        **参数解释：** 是否已归档。

        :param archived: The archived of this CommitDiscussionDto.
        :type archived: bool
        """
        self._archived = archived

    @property
    def review_categories(self):
        r"""Gets the review_categories of this CommitDiscussionDto.

        **参数解释：** 意见分类key。

        :return: The review_categories of this CommitDiscussionDto.
        :rtype: str
        """
        return self._review_categories

    @review_categories.setter
    def review_categories(self, review_categories):
        r"""Sets the review_categories of this CommitDiscussionDto.

        **参数解释：** 意见分类key。

        :param review_categories: The review_categories of this CommitDiscussionDto.
        :type review_categories: str
        """
        self._review_categories = review_categories

    @property
    def review_categories_cn(self):
        r"""Gets the review_categories_cn of this CommitDiscussionDto.

        **参数解释：** 意见分类中文。

        :return: The review_categories_cn of this CommitDiscussionDto.
        :rtype: str
        """
        return self._review_categories_cn

    @review_categories_cn.setter
    def review_categories_cn(self, review_categories_cn):
        r"""Sets the review_categories_cn of this CommitDiscussionDto.

        **参数解释：** 意见分类中文。

        :param review_categories_cn: The review_categories_cn of this CommitDiscussionDto.
        :type review_categories_cn: str
        """
        self._review_categories_cn = review_categories_cn

    @property
    def review_categories_en(self):
        r"""Gets the review_categories_en of this CommitDiscussionDto.

        **参数解释：** 意见分类英文。

        :return: The review_categories_en of this CommitDiscussionDto.
        :rtype: str
        """
        return self._review_categories_en

    @review_categories_en.setter
    def review_categories_en(self, review_categories_en):
        r"""Sets the review_categories_en of this CommitDiscussionDto.

        **参数解释：** 意见分类英文。

        :param review_categories_en: The review_categories_en of this CommitDiscussionDto.
        :type review_categories_en: str
        """
        self._review_categories_en = review_categories_en

    @property
    def review_modules(self):
        r"""Gets the review_modules of this CommitDiscussionDto.

        **参数解释：** 意见模块。

        :return: The review_modules of this CommitDiscussionDto.
        :rtype: str
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        r"""Sets the review_modules of this CommitDiscussionDto.

        **参数解释：** 意见模块。

        :param review_modules: The review_modules of this CommitDiscussionDto.
        :type review_modules: str
        """
        self._review_modules = review_modules

    @property
    def severity(self):
        r"""Gets the severity of this CommitDiscussionDto.

        **参数解释：** 严重程度key。

        :return: The severity of this CommitDiscussionDto.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this CommitDiscussionDto.

        **参数解释：** 严重程度key。

        :param severity: The severity of this CommitDiscussionDto.
        :type severity: str
        """
        self._severity = severity

    @property
    def severity_cn(self):
        r"""Gets the severity_cn of this CommitDiscussionDto.

        **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命

        :return: The severity_cn of this CommitDiscussionDto.
        :rtype: str
        """
        return self._severity_cn

    @severity_cn.setter
    def severity_cn(self, severity_cn):
        r"""Sets the severity_cn of this CommitDiscussionDto.

        **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命

        :param severity_cn: The severity_cn of this CommitDiscussionDto.
        :type severity_cn: str
        """
        self._severity_cn = severity_cn

    @property
    def severity_en(self):
        r"""Gets the severity_en of this CommitDiscussionDto.

        **参数解释：** 严重程度英文。

        :return: The severity_en of this CommitDiscussionDto.
        :rtype: str
        """
        return self._severity_en

    @severity_en.setter
    def severity_en(self, severity_en):
        r"""Sets the severity_en of this CommitDiscussionDto.

        **参数解释：** 严重程度英文。

        :param severity_en: The severity_en of this CommitDiscussionDto.
        :type severity_en: str
        """
        self._severity_en = severity_en

    @property
    def assignee(self):
        r"""Gets the assignee of this CommitDiscussionDto.

        :return: The assignee of this CommitDiscussionDto.
        :rtype: :class:`huaweicloudsdkcodeartsrepo.v4.UserBasicDto`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this CommitDiscussionDto.

        :param assignee: The assignee of this CommitDiscussionDto.
        :type assignee: :class:`huaweicloudsdkcodeartsrepo.v4.UserBasicDto`
        """
        self._assignee = assignee

    @property
    def proposer(self):
        r"""Gets the proposer of this CommitDiscussionDto.

        :return: The proposer of this CommitDiscussionDto.
        :rtype: :class:`huaweicloudsdkcodeartsrepo.v4.UserBasicDto`
        """
        return self._proposer

    @proposer.setter
    def proposer(self, proposer):
        r"""Sets the proposer of this CommitDiscussionDto.

        :param proposer: The proposer of this CommitDiscussionDto.
        :type proposer: :class:`huaweicloudsdkcodeartsrepo.v4.UserBasicDto`
        """
        self._proposer = proposer

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CommitDiscussionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
