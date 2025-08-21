# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestBasicDiscussionDto:

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
        'notes': 'list[NoteDto]',
        'repository_id': 'int',
        'noteable_type': 'str',
        'commit_id': 'str',
        'repository_full_path': 'str',
        'a_mode': 'str',
        'b_mode': 'str',
        'deleted_file': 'bool',
        'new_file': 'bool',
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
        'proposer': 'UserBasicDto',
        'merge_request_version_params': 'MergeRequestVersionParamsDto'
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
        'proposer': 'proposer',
        'merge_request_version_params': 'merge_request_version_params'
    }

    def __init__(self, id=None, individual_note=None, notes=None, repository_id=None, noteable_type=None, commit_id=None, repository_full_path=None, a_mode=None, b_mode=None, deleted_file=None, new_file=None, resolved=None, archived=None, review_categories=None, review_categories_cn=None, review_categories_en=None, review_modules=None, severity=None, severity_cn=None, severity_en=None, assignee=None, proposer=None, merge_request_version_params=None):
        r"""MergeRequestBasicDiscussionDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 检视意见id(主评论和回复共用)。
        :type id: str
        :param individual_note: **参数解释：** 个人检视意见(不需要解决)。
        :type individual_note: bool
        :param notes: **参数解释：** 评论列表(主评+回复)。
        :type notes: list[:class:`huaweicloudsdkcodehub.v4.NoteDto`]
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
        :type assignee: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param proposer: 
        :type proposer: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param merge_request_version_params: 
        :type merge_request_version_params: :class:`huaweicloudsdkcodehub.v4.MergeRequestVersionParamsDto`
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
        self._merge_request_version_params = None
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
        if merge_request_version_params is not None:
            self.merge_request_version_params = merge_request_version_params

    @property
    def id(self):
        r"""Gets the id of this MergeRequestBasicDiscussionDto.

        **参数解释：** 检视意见id(主评论和回复共用)。

        :return: The id of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MergeRequestBasicDiscussionDto.

        **参数解释：** 检视意见id(主评论和回复共用)。

        :param id: The id of this MergeRequestBasicDiscussionDto.
        :type id: str
        """
        self._id = id

    @property
    def individual_note(self):
        r"""Gets the individual_note of this MergeRequestBasicDiscussionDto.

        **参数解释：** 个人检视意见(不需要解决)。

        :return: The individual_note of this MergeRequestBasicDiscussionDto.
        :rtype: bool
        """
        return self._individual_note

    @individual_note.setter
    def individual_note(self, individual_note):
        r"""Sets the individual_note of this MergeRequestBasicDiscussionDto.

        **参数解释：** 个人检视意见(不需要解决)。

        :param individual_note: The individual_note of this MergeRequestBasicDiscussionDto.
        :type individual_note: bool
        """
        self._individual_note = individual_note

    @property
    def notes(self):
        r"""Gets the notes of this MergeRequestBasicDiscussionDto.

        **参数解释：** 评论列表(主评+回复)。

        :return: The notes of this MergeRequestBasicDiscussionDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.NoteDto`]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this MergeRequestBasicDiscussionDto.

        **参数解释：** 评论列表(主评+回复)。

        :param notes: The notes of this MergeRequestBasicDiscussionDto.
        :type notes: list[:class:`huaweicloudsdkcodehub.v4.NoteDto`]
        """
        self._notes = notes

    @property
    def repository_id(self):
        r"""Gets the repository_id of this MergeRequestBasicDiscussionDto.

        **参数解释：** 仓库id。

        :return: The repository_id of this MergeRequestBasicDiscussionDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this MergeRequestBasicDiscussionDto.

        **参数解释：** 仓库id。

        :param repository_id: The repository_id of this MergeRequestBasicDiscussionDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def noteable_type(self):
        r"""Gets the noteable_type of this MergeRequestBasicDiscussionDto.

        **参数解释：** 意见类型。

        :return: The noteable_type of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._noteable_type

    @noteable_type.setter
    def noteable_type(self, noteable_type):
        r"""Sets the noteable_type of this MergeRequestBasicDiscussionDto.

        **参数解释：** 意见类型。

        :param noteable_type: The noteable_type of this MergeRequestBasicDiscussionDto.
        :type noteable_type: str
        """
        self._noteable_type = noteable_type

    @property
    def commit_id(self):
        r"""Gets the commit_id of this MergeRequestBasicDiscussionDto.

        **参数解释：** 提交记录id。

        :return: The commit_id of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        r"""Sets the commit_id of this MergeRequestBasicDiscussionDto.

        **参数解释：** 提交记录id。

        :param commit_id: The commit_id of this MergeRequestBasicDiscussionDto.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def repository_full_path(self):
        r"""Gets the repository_full_path of this MergeRequestBasicDiscussionDto.

        **参数解释：** 仓库路径。

        :return: The repository_full_path of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._repository_full_path

    @repository_full_path.setter
    def repository_full_path(self, repository_full_path):
        r"""Sets the repository_full_path of this MergeRequestBasicDiscussionDto.

        **参数解释：** 仓库路径。

        :param repository_full_path: The repository_full_path of this MergeRequestBasicDiscussionDto.
        :type repository_full_path: str
        """
        self._repository_full_path = repository_full_path

    @property
    def a_mode(self):
        r"""Gets the a_mode of this MergeRequestBasicDiscussionDto.

        **参数解释：** 文件旧权限(默认100644)。

        :return: The a_mode of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._a_mode

    @a_mode.setter
    def a_mode(self, a_mode):
        r"""Sets the a_mode of this MergeRequestBasicDiscussionDto.

        **参数解释：** 文件旧权限(默认100644)。

        :param a_mode: The a_mode of this MergeRequestBasicDiscussionDto.
        :type a_mode: str
        """
        self._a_mode = a_mode

    @property
    def b_mode(self):
        r"""Gets the b_mode of this MergeRequestBasicDiscussionDto.

        **参数解释：** 文件新权限(默认100644)。

        :return: The b_mode of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._b_mode

    @b_mode.setter
    def b_mode(self, b_mode):
        r"""Sets the b_mode of this MergeRequestBasicDiscussionDto.

        **参数解释：** 文件新权限(默认100644)。

        :param b_mode: The b_mode of this MergeRequestBasicDiscussionDto.
        :type b_mode: str
        """
        self._b_mode = b_mode

    @property
    def deleted_file(self):
        r"""Gets the deleted_file of this MergeRequestBasicDiscussionDto.

        **参数解释：** 是否为删除文件。

        :return: The deleted_file of this MergeRequestBasicDiscussionDto.
        :rtype: bool
        """
        return self._deleted_file

    @deleted_file.setter
    def deleted_file(self, deleted_file):
        r"""Sets the deleted_file of this MergeRequestBasicDiscussionDto.

        **参数解释：** 是否为删除文件。

        :param deleted_file: The deleted_file of this MergeRequestBasicDiscussionDto.
        :type deleted_file: bool
        """
        self._deleted_file = deleted_file

    @property
    def new_file(self):
        r"""Gets the new_file of this MergeRequestBasicDiscussionDto.

        **参数解释：** 是否为新增文件。

        :return: The new_file of this MergeRequestBasicDiscussionDto.
        :rtype: bool
        """
        return self._new_file

    @new_file.setter
    def new_file(self, new_file):
        r"""Sets the new_file of this MergeRequestBasicDiscussionDto.

        **参数解释：** 是否为新增文件。

        :param new_file: The new_file of this MergeRequestBasicDiscussionDto.
        :type new_file: bool
        """
        self._new_file = new_file

    @property
    def resolved(self):
        r"""Gets the resolved of this MergeRequestBasicDiscussionDto.

        **参数解释：** 是否已解决。

        :return: The resolved of this MergeRequestBasicDiscussionDto.
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        r"""Sets the resolved of this MergeRequestBasicDiscussionDto.

        **参数解释：** 是否已解决。

        :param resolved: The resolved of this MergeRequestBasicDiscussionDto.
        :type resolved: bool
        """
        self._resolved = resolved

    @property
    def archived(self):
        r"""Gets the archived of this MergeRequestBasicDiscussionDto.

        **参数解释：** 是否已归档。

        :return: The archived of this MergeRequestBasicDiscussionDto.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this MergeRequestBasicDiscussionDto.

        **参数解释：** 是否已归档。

        :param archived: The archived of this MergeRequestBasicDiscussionDto.
        :type archived: bool
        """
        self._archived = archived

    @property
    def review_categories(self):
        r"""Gets the review_categories of this MergeRequestBasicDiscussionDto.

        **参数解释：** 意见分类key。

        :return: The review_categories of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._review_categories

    @review_categories.setter
    def review_categories(self, review_categories):
        r"""Sets the review_categories of this MergeRequestBasicDiscussionDto.

        **参数解释：** 意见分类key。

        :param review_categories: The review_categories of this MergeRequestBasicDiscussionDto.
        :type review_categories: str
        """
        self._review_categories = review_categories

    @property
    def review_categories_cn(self):
        r"""Gets the review_categories_cn of this MergeRequestBasicDiscussionDto.

        **参数解释：** 意见分类中文。

        :return: The review_categories_cn of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._review_categories_cn

    @review_categories_cn.setter
    def review_categories_cn(self, review_categories_cn):
        r"""Sets the review_categories_cn of this MergeRequestBasicDiscussionDto.

        **参数解释：** 意见分类中文。

        :param review_categories_cn: The review_categories_cn of this MergeRequestBasicDiscussionDto.
        :type review_categories_cn: str
        """
        self._review_categories_cn = review_categories_cn

    @property
    def review_categories_en(self):
        r"""Gets the review_categories_en of this MergeRequestBasicDiscussionDto.

        **参数解释：** 意见分类英文。

        :return: The review_categories_en of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._review_categories_en

    @review_categories_en.setter
    def review_categories_en(self, review_categories_en):
        r"""Sets the review_categories_en of this MergeRequestBasicDiscussionDto.

        **参数解释：** 意见分类英文。

        :param review_categories_en: The review_categories_en of this MergeRequestBasicDiscussionDto.
        :type review_categories_en: str
        """
        self._review_categories_en = review_categories_en

    @property
    def review_modules(self):
        r"""Gets the review_modules of this MergeRequestBasicDiscussionDto.

        **参数解释：** 意见模块。

        :return: The review_modules of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        r"""Sets the review_modules of this MergeRequestBasicDiscussionDto.

        **参数解释：** 意见模块。

        :param review_modules: The review_modules of this MergeRequestBasicDiscussionDto.
        :type review_modules: str
        """
        self._review_modules = review_modules

    @property
    def severity(self):
        r"""Gets the severity of this MergeRequestBasicDiscussionDto.

        **参数解释：** 严重程度key。

        :return: The severity of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this MergeRequestBasicDiscussionDto.

        **参数解释：** 严重程度key。

        :param severity: The severity of this MergeRequestBasicDiscussionDto.
        :type severity: str
        """
        self._severity = severity

    @property
    def severity_cn(self):
        r"""Gets the severity_cn of this MergeRequestBasicDiscussionDto.

        **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命

        :return: The severity_cn of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._severity_cn

    @severity_cn.setter
    def severity_cn(self, severity_cn):
        r"""Sets the severity_cn of this MergeRequestBasicDiscussionDto.

        **参数解释：** 严重程度中文。 **约束限制：** - 建议 - 一般 - 严重 - 致命

        :param severity_cn: The severity_cn of this MergeRequestBasicDiscussionDto.
        :type severity_cn: str
        """
        self._severity_cn = severity_cn

    @property
    def severity_en(self):
        r"""Gets the severity_en of this MergeRequestBasicDiscussionDto.

        **参数解释：** 严重程度英文。

        :return: The severity_en of this MergeRequestBasicDiscussionDto.
        :rtype: str
        """
        return self._severity_en

    @severity_en.setter
    def severity_en(self, severity_en):
        r"""Sets the severity_en of this MergeRequestBasicDiscussionDto.

        **参数解释：** 严重程度英文。

        :param severity_en: The severity_en of this MergeRequestBasicDiscussionDto.
        :type severity_en: str
        """
        self._severity_en = severity_en

    @property
    def assignee(self):
        r"""Gets the assignee of this MergeRequestBasicDiscussionDto.

        :return: The assignee of this MergeRequestBasicDiscussionDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        r"""Sets the assignee of this MergeRequestBasicDiscussionDto.

        :param assignee: The assignee of this MergeRequestBasicDiscussionDto.
        :type assignee: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._assignee = assignee

    @property
    def proposer(self):
        r"""Gets the proposer of this MergeRequestBasicDiscussionDto.

        :return: The proposer of this MergeRequestBasicDiscussionDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._proposer

    @proposer.setter
    def proposer(self, proposer):
        r"""Sets the proposer of this MergeRequestBasicDiscussionDto.

        :param proposer: The proposer of this MergeRequestBasicDiscussionDto.
        :type proposer: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._proposer = proposer

    @property
    def merge_request_version_params(self):
        r"""Gets the merge_request_version_params of this MergeRequestBasicDiscussionDto.

        :return: The merge_request_version_params of this MergeRequestBasicDiscussionDto.
        :rtype: :class:`huaweicloudsdkcodehub.v4.MergeRequestVersionParamsDto`
        """
        return self._merge_request_version_params

    @merge_request_version_params.setter
    def merge_request_version_params(self, merge_request_version_params):
        r"""Sets the merge_request_version_params of this MergeRequestBasicDiscussionDto.

        :param merge_request_version_params: The merge_request_version_params of this MergeRequestBasicDiscussionDto.
        :type merge_request_version_params: :class:`huaweicloudsdkcodehub.v4.MergeRequestVersionParamsDto`
        """
        self._merge_request_version_params = merge_request_version_params

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
        if not isinstance(other, MergeRequestBasicDiscussionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
