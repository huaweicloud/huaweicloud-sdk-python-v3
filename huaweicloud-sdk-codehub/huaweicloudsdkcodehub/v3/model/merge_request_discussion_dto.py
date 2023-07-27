# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeRequestDiscussionDto:

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
        'project_id': 'int',
        'noteable_type': 'str',
        'commit_id': 'str',
        'project_full_path': 'str',
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
        'merge_request_version_params': 'MergeRequestVersionParamsDto',
        'diff_file': 'str',
        'added_lines': 'int',
        'removed_lines': 'int'
    }

    attribute_map = {
        'id': 'id',
        'individual_note': 'individual_note',
        'notes': 'notes',
        'project_id': 'project_id',
        'noteable_type': 'noteable_type',
        'commit_id': 'commit_id',
        'project_full_path': 'project_full_path',
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
        'merge_request_version_params': 'merge_request_version_params',
        'diff_file': 'diff_file',
        'added_lines': 'added_lines',
        'removed_lines': 'removed_lines'
    }

    def __init__(self, id=None, individual_note=None, notes=None, project_id=None, noteable_type=None, commit_id=None, project_full_path=None, a_mode=None, b_mode=None, deleted_file=None, new_file=None, resolved=None, archived=None, review_categories=None, review_categories_cn=None, review_categories_en=None, review_modules=None, severity=None, severity_cn=None, severity_en=None, assignee=None, proposer=None, merge_request_version_params=None, diff_file=None, added_lines=None, removed_lines=None):
        """MergeRequestDiscussionDto

        The model defined in huaweicloud sdk

        :param id: 评论id
        :type id: str
        :param individual_note: individual_note
        :type individual_note: bool
        :param notes: 主评和回复列表
        :type notes: list[:class:`huaweicloudsdkcodehub.v3.NoteDto`]
        :param project_id: 仓库id
        :type project_id: int
        :param noteable_type: 目标类型
        :type noteable_type: str
        :param commit_id: 关联的提交id
        :type commit_id: str
        :param project_full_path: 仓库路径
        :type project_full_path: str
        :param a_mode: 变更前文件模式
        :type a_mode: str
        :param b_mode: 变更后文件模式
        :type b_mode: str
        :param deleted_file: 此次变更是否删除文件
        :type deleted_file: bool
        :param new_file: 此次变更是否新增文件
        :type new_file: bool
        :param resolved: 检视意见是否解决
        :type resolved: bool
        :param archived: 检视意见是否存档
        :type archived: bool
        :param review_categories: 检视意见分类
        :type review_categories: str
        :param review_categories_cn: 检视意见分类中文名
        :type review_categories_cn: str
        :param review_categories_en: 检视意见分类英文名
        :type review_categories_en: str
        :param review_modules: 检视意见模块
        :type review_modules: str
        :param severity: 严重程度
        :type severity: str
        :param severity_cn: 严重程度中文名
        :type severity_cn: str
        :param severity_en: 严重程度英文名
        :type severity_en: str
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        :param proposer: 
        :type proposer: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        :param merge_request_version_params: 
        :type merge_request_version_params: :class:`huaweicloudsdkcodehub.v3.MergeRequestVersionParamsDto`
        :param diff_file: 变更文件
        :type diff_file: str
        :param added_lines: 新增行数
        :type added_lines: int
        :param removed_lines: 删除行数
        :type removed_lines: int
        """
        
        

        self._id = None
        self._individual_note = None
        self._notes = None
        self._project_id = None
        self._noteable_type = None
        self._commit_id = None
        self._project_full_path = None
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
        self._diff_file = None
        self._added_lines = None
        self._removed_lines = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if individual_note is not None:
            self.individual_note = individual_note
        if notes is not None:
            self.notes = notes
        if project_id is not None:
            self.project_id = project_id
        if noteable_type is not None:
            self.noteable_type = noteable_type
        if commit_id is not None:
            self.commit_id = commit_id
        if project_full_path is not None:
            self.project_full_path = project_full_path
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
        if diff_file is not None:
            self.diff_file = diff_file
        if added_lines is not None:
            self.added_lines = added_lines
        if removed_lines is not None:
            self.removed_lines = removed_lines

    @property
    def id(self):
        """Gets the id of this MergeRequestDiscussionDto.

        评论id

        :return: The id of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MergeRequestDiscussionDto.

        评论id

        :param id: The id of this MergeRequestDiscussionDto.
        :type id: str
        """
        self._id = id

    @property
    def individual_note(self):
        """Gets the individual_note of this MergeRequestDiscussionDto.

        individual_note

        :return: The individual_note of this MergeRequestDiscussionDto.
        :rtype: bool
        """
        return self._individual_note

    @individual_note.setter
    def individual_note(self, individual_note):
        """Sets the individual_note of this MergeRequestDiscussionDto.

        individual_note

        :param individual_note: The individual_note of this MergeRequestDiscussionDto.
        :type individual_note: bool
        """
        self._individual_note = individual_note

    @property
    def notes(self):
        """Gets the notes of this MergeRequestDiscussionDto.

        主评和回复列表

        :return: The notes of this MergeRequestDiscussionDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.NoteDto`]
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this MergeRequestDiscussionDto.

        主评和回复列表

        :param notes: The notes of this MergeRequestDiscussionDto.
        :type notes: list[:class:`huaweicloudsdkcodehub.v3.NoteDto`]
        """
        self._notes = notes

    @property
    def project_id(self):
        """Gets the project_id of this MergeRequestDiscussionDto.

        仓库id

        :return: The project_id of this MergeRequestDiscussionDto.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this MergeRequestDiscussionDto.

        仓库id

        :param project_id: The project_id of this MergeRequestDiscussionDto.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def noteable_type(self):
        """Gets the noteable_type of this MergeRequestDiscussionDto.

        目标类型

        :return: The noteable_type of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._noteable_type

    @noteable_type.setter
    def noteable_type(self, noteable_type):
        """Sets the noteable_type of this MergeRequestDiscussionDto.

        目标类型

        :param noteable_type: The noteable_type of this MergeRequestDiscussionDto.
        :type noteable_type: str
        """
        self._noteable_type = noteable_type

    @property
    def commit_id(self):
        """Gets the commit_id of this MergeRequestDiscussionDto.

        关联的提交id

        :return: The commit_id of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this MergeRequestDiscussionDto.

        关联的提交id

        :param commit_id: The commit_id of this MergeRequestDiscussionDto.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def project_full_path(self):
        """Gets the project_full_path of this MergeRequestDiscussionDto.

        仓库路径

        :return: The project_full_path of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._project_full_path

    @project_full_path.setter
    def project_full_path(self, project_full_path):
        """Sets the project_full_path of this MergeRequestDiscussionDto.

        仓库路径

        :param project_full_path: The project_full_path of this MergeRequestDiscussionDto.
        :type project_full_path: str
        """
        self._project_full_path = project_full_path

    @property
    def a_mode(self):
        """Gets the a_mode of this MergeRequestDiscussionDto.

        变更前文件模式

        :return: The a_mode of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._a_mode

    @a_mode.setter
    def a_mode(self, a_mode):
        """Sets the a_mode of this MergeRequestDiscussionDto.

        变更前文件模式

        :param a_mode: The a_mode of this MergeRequestDiscussionDto.
        :type a_mode: str
        """
        self._a_mode = a_mode

    @property
    def b_mode(self):
        """Gets the b_mode of this MergeRequestDiscussionDto.

        变更后文件模式

        :return: The b_mode of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._b_mode

    @b_mode.setter
    def b_mode(self, b_mode):
        """Sets the b_mode of this MergeRequestDiscussionDto.

        变更后文件模式

        :param b_mode: The b_mode of this MergeRequestDiscussionDto.
        :type b_mode: str
        """
        self._b_mode = b_mode

    @property
    def deleted_file(self):
        """Gets the deleted_file of this MergeRequestDiscussionDto.

        此次变更是否删除文件

        :return: The deleted_file of this MergeRequestDiscussionDto.
        :rtype: bool
        """
        return self._deleted_file

    @deleted_file.setter
    def deleted_file(self, deleted_file):
        """Sets the deleted_file of this MergeRequestDiscussionDto.

        此次变更是否删除文件

        :param deleted_file: The deleted_file of this MergeRequestDiscussionDto.
        :type deleted_file: bool
        """
        self._deleted_file = deleted_file

    @property
    def new_file(self):
        """Gets the new_file of this MergeRequestDiscussionDto.

        此次变更是否新增文件

        :return: The new_file of this MergeRequestDiscussionDto.
        :rtype: bool
        """
        return self._new_file

    @new_file.setter
    def new_file(self, new_file):
        """Sets the new_file of this MergeRequestDiscussionDto.

        此次变更是否新增文件

        :param new_file: The new_file of this MergeRequestDiscussionDto.
        :type new_file: bool
        """
        self._new_file = new_file

    @property
    def resolved(self):
        """Gets the resolved of this MergeRequestDiscussionDto.

        检视意见是否解决

        :return: The resolved of this MergeRequestDiscussionDto.
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        """Sets the resolved of this MergeRequestDiscussionDto.

        检视意见是否解决

        :param resolved: The resolved of this MergeRequestDiscussionDto.
        :type resolved: bool
        """
        self._resolved = resolved

    @property
    def archived(self):
        """Gets the archived of this MergeRequestDiscussionDto.

        检视意见是否存档

        :return: The archived of this MergeRequestDiscussionDto.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this MergeRequestDiscussionDto.

        检视意见是否存档

        :param archived: The archived of this MergeRequestDiscussionDto.
        :type archived: bool
        """
        self._archived = archived

    @property
    def review_categories(self):
        """Gets the review_categories of this MergeRequestDiscussionDto.

        检视意见分类

        :return: The review_categories of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._review_categories

    @review_categories.setter
    def review_categories(self, review_categories):
        """Sets the review_categories of this MergeRequestDiscussionDto.

        检视意见分类

        :param review_categories: The review_categories of this MergeRequestDiscussionDto.
        :type review_categories: str
        """
        self._review_categories = review_categories

    @property
    def review_categories_cn(self):
        """Gets the review_categories_cn of this MergeRequestDiscussionDto.

        检视意见分类中文名

        :return: The review_categories_cn of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._review_categories_cn

    @review_categories_cn.setter
    def review_categories_cn(self, review_categories_cn):
        """Sets the review_categories_cn of this MergeRequestDiscussionDto.

        检视意见分类中文名

        :param review_categories_cn: The review_categories_cn of this MergeRequestDiscussionDto.
        :type review_categories_cn: str
        """
        self._review_categories_cn = review_categories_cn

    @property
    def review_categories_en(self):
        """Gets the review_categories_en of this MergeRequestDiscussionDto.

        检视意见分类英文名

        :return: The review_categories_en of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._review_categories_en

    @review_categories_en.setter
    def review_categories_en(self, review_categories_en):
        """Sets the review_categories_en of this MergeRequestDiscussionDto.

        检视意见分类英文名

        :param review_categories_en: The review_categories_en of this MergeRequestDiscussionDto.
        :type review_categories_en: str
        """
        self._review_categories_en = review_categories_en

    @property
    def review_modules(self):
        """Gets the review_modules of this MergeRequestDiscussionDto.

        检视意见模块

        :return: The review_modules of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        """Sets the review_modules of this MergeRequestDiscussionDto.

        检视意见模块

        :param review_modules: The review_modules of this MergeRequestDiscussionDto.
        :type review_modules: str
        """
        self._review_modules = review_modules

    @property
    def severity(self):
        """Gets the severity of this MergeRequestDiscussionDto.

        严重程度

        :return: The severity of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this MergeRequestDiscussionDto.

        严重程度

        :param severity: The severity of this MergeRequestDiscussionDto.
        :type severity: str
        """
        self._severity = severity

    @property
    def severity_cn(self):
        """Gets the severity_cn of this MergeRequestDiscussionDto.

        严重程度中文名

        :return: The severity_cn of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._severity_cn

    @severity_cn.setter
    def severity_cn(self, severity_cn):
        """Sets the severity_cn of this MergeRequestDiscussionDto.

        严重程度中文名

        :param severity_cn: The severity_cn of this MergeRequestDiscussionDto.
        :type severity_cn: str
        """
        self._severity_cn = severity_cn

    @property
    def severity_en(self):
        """Gets the severity_en of this MergeRequestDiscussionDto.

        严重程度英文名

        :return: The severity_en of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._severity_en

    @severity_en.setter
    def severity_en(self, severity_en):
        """Sets the severity_en of this MergeRequestDiscussionDto.

        严重程度英文名

        :param severity_en: The severity_en of this MergeRequestDiscussionDto.
        :type severity_en: str
        """
        self._severity_en = severity_en

    @property
    def assignee(self):
        """Gets the assignee of this MergeRequestDiscussionDto.

        :return: The assignee of this MergeRequestDiscussionDto.
        :rtype: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this MergeRequestDiscussionDto.

        :param assignee: The assignee of this MergeRequestDiscussionDto.
        :type assignee: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        self._assignee = assignee

    @property
    def proposer(self):
        """Gets the proposer of this MergeRequestDiscussionDto.

        :return: The proposer of this MergeRequestDiscussionDto.
        :rtype: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        return self._proposer

    @proposer.setter
    def proposer(self, proposer):
        """Sets the proposer of this MergeRequestDiscussionDto.

        :param proposer: The proposer of this MergeRequestDiscussionDto.
        :type proposer: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        self._proposer = proposer

    @property
    def merge_request_version_params(self):
        """Gets the merge_request_version_params of this MergeRequestDiscussionDto.

        :return: The merge_request_version_params of this MergeRequestDiscussionDto.
        :rtype: :class:`huaweicloudsdkcodehub.v3.MergeRequestVersionParamsDto`
        """
        return self._merge_request_version_params

    @merge_request_version_params.setter
    def merge_request_version_params(self, merge_request_version_params):
        """Sets the merge_request_version_params of this MergeRequestDiscussionDto.

        :param merge_request_version_params: The merge_request_version_params of this MergeRequestDiscussionDto.
        :type merge_request_version_params: :class:`huaweicloudsdkcodehub.v3.MergeRequestVersionParamsDto`
        """
        self._merge_request_version_params = merge_request_version_params

    @property
    def diff_file(self):
        """Gets the diff_file of this MergeRequestDiscussionDto.

        变更文件

        :return: The diff_file of this MergeRequestDiscussionDto.
        :rtype: str
        """
        return self._diff_file

    @diff_file.setter
    def diff_file(self, diff_file):
        """Sets the diff_file of this MergeRequestDiscussionDto.

        变更文件

        :param diff_file: The diff_file of this MergeRequestDiscussionDto.
        :type diff_file: str
        """
        self._diff_file = diff_file

    @property
    def added_lines(self):
        """Gets the added_lines of this MergeRequestDiscussionDto.

        新增行数

        :return: The added_lines of this MergeRequestDiscussionDto.
        :rtype: int
        """
        return self._added_lines

    @added_lines.setter
    def added_lines(self, added_lines):
        """Sets the added_lines of this MergeRequestDiscussionDto.

        新增行数

        :param added_lines: The added_lines of this MergeRequestDiscussionDto.
        :type added_lines: int
        """
        self._added_lines = added_lines

    @property
    def removed_lines(self):
        """Gets the removed_lines of this MergeRequestDiscussionDto.

        删除行数

        :return: The removed_lines of this MergeRequestDiscussionDto.
        :rtype: int
        """
        return self._removed_lines

    @removed_lines.setter
    def removed_lines(self, removed_lines):
        """Sets the removed_lines of this MergeRequestDiscussionDto.

        删除行数

        :param removed_lines: The removed_lines of this MergeRequestDiscussionDto.
        :type removed_lines: int
        """
        self._removed_lines = removed_lines

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
        if not isinstance(other, MergeRequestDiscussionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
