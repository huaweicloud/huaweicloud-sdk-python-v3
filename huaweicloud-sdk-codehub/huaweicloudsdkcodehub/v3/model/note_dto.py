# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoteDto:

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
        'project': 'str',
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
        'is_outdated': 'bool'
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
        'project': 'project',
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
        'is_outdated': 'is_outdated'
    }

    def __init__(self, id=None, type=None, body=None, attachment=None, author=None, created_at=None, updated_at=None, system=None, noteable_id=None, noteable_type=None, commit_id=None, resolvable=None, is_reply=None, resolved_by=None, noteable_iid=None, discussion_id=None, project=None, diff_file=None, diff=None, archived=None, review_categories=None, review_categories_cn=None, review_categories_en=None, review_modules=None, severity=None, severity_cn=None, severity_en=None, file_path=None, line=None, assignee=None, proposer=None, position=None, resolved=None, is_outdated=None):
        """NoteDto

        The model defined in huaweicloud sdk

        :param id: note id
        :type id: int
        :param type: note类型
        :type type: str
        :param body: 检视意见内容
        :type body: str
        :param attachment: 附件
        :type attachment: str
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param system: 是否是系统生成的日志
        :type system: bool
        :param noteable_id: 目标id
        :type noteable_id: int
        :param noteable_type: 目标类型
        :type noteable_type: str
        :param commit_id: 关联的提交id
        :type commit_id: str
        :param resolvable: 是否可解决
        :type resolvable: bool
        :param is_reply: 是否是回复
        :type is_reply: bool
        :param resolved_by: 
        :type resolved_by: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        :param noteable_iid: 目标iid
        :type noteable_iid: int
        :param discussion_id: 讨论id
        :type discussion_id: str
        :param project: 所属项目
        :type project: str
        :param diff_file: 变更文件
        :type diff_file: str
        :param diff: 变更内容
        :type diff: str
        :param archived: 是否存档
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
        :param file_path: 文件路径
        :type file_path: str
        :param line: 行号
        :type line: str
        :param assignee: 
        :type assignee: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        :param proposer: 
        :type proposer: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        :param position: 
        :type position: :class:`huaweicloudsdkcodehub.v3.PositionDto`
        :param resolved: 是否解决
        :type resolved: bool
        :param is_outdated: 是否过时
        :type is_outdated: bool
        """
        
        

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
        self._project = None
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
        if project is not None:
            self.project = project
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

    @property
    def id(self):
        """Gets the id of this NoteDto.

        note id

        :return: The id of this NoteDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NoteDto.

        note id

        :param id: The id of this NoteDto.
        :type id: int
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this NoteDto.

        note类型

        :return: The type of this NoteDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NoteDto.

        note类型

        :param type: The type of this NoteDto.
        :type type: str
        """
        self._type = type

    @property
    def body(self):
        """Gets the body of this NoteDto.

        检视意见内容

        :return: The body of this NoteDto.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this NoteDto.

        检视意见内容

        :param body: The body of this NoteDto.
        :type body: str
        """
        self._body = body

    @property
    def attachment(self):
        """Gets the attachment of this NoteDto.

        附件

        :return: The attachment of this NoteDto.
        :rtype: str
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this NoteDto.

        附件

        :param attachment: The attachment of this NoteDto.
        :type attachment: str
        """
        self._attachment = attachment

    @property
    def author(self):
        """Gets the author of this NoteDto.

        :return: The author of this NoteDto.
        :rtype: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this NoteDto.

        :param author: The author of this NoteDto.
        :type author: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        self._author = author

    @property
    def created_at(self):
        """Gets the created_at of this NoteDto.

        创建时间

        :return: The created_at of this NoteDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this NoteDto.

        创建时间

        :param created_at: The created_at of this NoteDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this NoteDto.

        更新时间

        :return: The updated_at of this NoteDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this NoteDto.

        更新时间

        :param updated_at: The updated_at of this NoteDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def system(self):
        """Gets the system of this NoteDto.

        是否是系统生成的日志

        :return: The system of this NoteDto.
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this NoteDto.

        是否是系统生成的日志

        :param system: The system of this NoteDto.
        :type system: bool
        """
        self._system = system

    @property
    def noteable_id(self):
        """Gets the noteable_id of this NoteDto.

        目标id

        :return: The noteable_id of this NoteDto.
        :rtype: int
        """
        return self._noteable_id

    @noteable_id.setter
    def noteable_id(self, noteable_id):
        """Sets the noteable_id of this NoteDto.

        目标id

        :param noteable_id: The noteable_id of this NoteDto.
        :type noteable_id: int
        """
        self._noteable_id = noteable_id

    @property
    def noteable_type(self):
        """Gets the noteable_type of this NoteDto.

        目标类型

        :return: The noteable_type of this NoteDto.
        :rtype: str
        """
        return self._noteable_type

    @noteable_type.setter
    def noteable_type(self, noteable_type):
        """Sets the noteable_type of this NoteDto.

        目标类型

        :param noteable_type: The noteable_type of this NoteDto.
        :type noteable_type: str
        """
        self._noteable_type = noteable_type

    @property
    def commit_id(self):
        """Gets the commit_id of this NoteDto.

        关联的提交id

        :return: The commit_id of this NoteDto.
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this NoteDto.

        关联的提交id

        :param commit_id: The commit_id of this NoteDto.
        :type commit_id: str
        """
        self._commit_id = commit_id

    @property
    def resolvable(self):
        """Gets the resolvable of this NoteDto.

        是否可解决

        :return: The resolvable of this NoteDto.
        :rtype: bool
        """
        return self._resolvable

    @resolvable.setter
    def resolvable(self, resolvable):
        """Sets the resolvable of this NoteDto.

        是否可解决

        :param resolvable: The resolvable of this NoteDto.
        :type resolvable: bool
        """
        self._resolvable = resolvable

    @property
    def is_reply(self):
        """Gets the is_reply of this NoteDto.

        是否是回复

        :return: The is_reply of this NoteDto.
        :rtype: bool
        """
        return self._is_reply

    @is_reply.setter
    def is_reply(self, is_reply):
        """Sets the is_reply of this NoteDto.

        是否是回复

        :param is_reply: The is_reply of this NoteDto.
        :type is_reply: bool
        """
        self._is_reply = is_reply

    @property
    def resolved_by(self):
        """Gets the resolved_by of this NoteDto.

        :return: The resolved_by of this NoteDto.
        :rtype: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        return self._resolved_by

    @resolved_by.setter
    def resolved_by(self, resolved_by):
        """Sets the resolved_by of this NoteDto.

        :param resolved_by: The resolved_by of this NoteDto.
        :type resolved_by: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        self._resolved_by = resolved_by

    @property
    def noteable_iid(self):
        """Gets the noteable_iid of this NoteDto.

        目标iid

        :return: The noteable_iid of this NoteDto.
        :rtype: int
        """
        return self._noteable_iid

    @noteable_iid.setter
    def noteable_iid(self, noteable_iid):
        """Sets the noteable_iid of this NoteDto.

        目标iid

        :param noteable_iid: The noteable_iid of this NoteDto.
        :type noteable_iid: int
        """
        self._noteable_iid = noteable_iid

    @property
    def discussion_id(self):
        """Gets the discussion_id of this NoteDto.

        讨论id

        :return: The discussion_id of this NoteDto.
        :rtype: str
        """
        return self._discussion_id

    @discussion_id.setter
    def discussion_id(self, discussion_id):
        """Sets the discussion_id of this NoteDto.

        讨论id

        :param discussion_id: The discussion_id of this NoteDto.
        :type discussion_id: str
        """
        self._discussion_id = discussion_id

    @property
    def project(self):
        """Gets the project of this NoteDto.

        所属项目

        :return: The project of this NoteDto.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this NoteDto.

        所属项目

        :param project: The project of this NoteDto.
        :type project: str
        """
        self._project = project

    @property
    def diff_file(self):
        """Gets the diff_file of this NoteDto.

        变更文件

        :return: The diff_file of this NoteDto.
        :rtype: str
        """
        return self._diff_file

    @diff_file.setter
    def diff_file(self, diff_file):
        """Sets the diff_file of this NoteDto.

        变更文件

        :param diff_file: The diff_file of this NoteDto.
        :type diff_file: str
        """
        self._diff_file = diff_file

    @property
    def diff(self):
        """Gets the diff of this NoteDto.

        变更内容

        :return: The diff of this NoteDto.
        :rtype: str
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        """Sets the diff of this NoteDto.

        变更内容

        :param diff: The diff of this NoteDto.
        :type diff: str
        """
        self._diff = diff

    @property
    def archived(self):
        """Gets the archived of this NoteDto.

        是否存档

        :return: The archived of this NoteDto.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this NoteDto.

        是否存档

        :param archived: The archived of this NoteDto.
        :type archived: bool
        """
        self._archived = archived

    @property
    def review_categories(self):
        """Gets the review_categories of this NoteDto.

        检视意见分类

        :return: The review_categories of this NoteDto.
        :rtype: str
        """
        return self._review_categories

    @review_categories.setter
    def review_categories(self, review_categories):
        """Sets the review_categories of this NoteDto.

        检视意见分类

        :param review_categories: The review_categories of this NoteDto.
        :type review_categories: str
        """
        self._review_categories = review_categories

    @property
    def review_categories_cn(self):
        """Gets the review_categories_cn of this NoteDto.

        检视意见分类中文名

        :return: The review_categories_cn of this NoteDto.
        :rtype: str
        """
        return self._review_categories_cn

    @review_categories_cn.setter
    def review_categories_cn(self, review_categories_cn):
        """Sets the review_categories_cn of this NoteDto.

        检视意见分类中文名

        :param review_categories_cn: The review_categories_cn of this NoteDto.
        :type review_categories_cn: str
        """
        self._review_categories_cn = review_categories_cn

    @property
    def review_categories_en(self):
        """Gets the review_categories_en of this NoteDto.

        检视意见分类英文名

        :return: The review_categories_en of this NoteDto.
        :rtype: str
        """
        return self._review_categories_en

    @review_categories_en.setter
    def review_categories_en(self, review_categories_en):
        """Sets the review_categories_en of this NoteDto.

        检视意见分类英文名

        :param review_categories_en: The review_categories_en of this NoteDto.
        :type review_categories_en: str
        """
        self._review_categories_en = review_categories_en

    @property
    def review_modules(self):
        """Gets the review_modules of this NoteDto.

        检视意见模块

        :return: The review_modules of this NoteDto.
        :rtype: str
        """
        return self._review_modules

    @review_modules.setter
    def review_modules(self, review_modules):
        """Sets the review_modules of this NoteDto.

        检视意见模块

        :param review_modules: The review_modules of this NoteDto.
        :type review_modules: str
        """
        self._review_modules = review_modules

    @property
    def severity(self):
        """Gets the severity of this NoteDto.

        严重程度

        :return: The severity of this NoteDto.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this NoteDto.

        严重程度

        :param severity: The severity of this NoteDto.
        :type severity: str
        """
        self._severity = severity

    @property
    def severity_cn(self):
        """Gets the severity_cn of this NoteDto.

        严重程度中文名

        :return: The severity_cn of this NoteDto.
        :rtype: str
        """
        return self._severity_cn

    @severity_cn.setter
    def severity_cn(self, severity_cn):
        """Sets the severity_cn of this NoteDto.

        严重程度中文名

        :param severity_cn: The severity_cn of this NoteDto.
        :type severity_cn: str
        """
        self._severity_cn = severity_cn

    @property
    def severity_en(self):
        """Gets the severity_en of this NoteDto.

        严重程度英文名

        :return: The severity_en of this NoteDto.
        :rtype: str
        """
        return self._severity_en

    @severity_en.setter
    def severity_en(self, severity_en):
        """Sets the severity_en of this NoteDto.

        严重程度英文名

        :param severity_en: The severity_en of this NoteDto.
        :type severity_en: str
        """
        self._severity_en = severity_en

    @property
    def file_path(self):
        """Gets the file_path of this NoteDto.

        文件路径

        :return: The file_path of this NoteDto.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this NoteDto.

        文件路径

        :param file_path: The file_path of this NoteDto.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def line(self):
        """Gets the line of this NoteDto.

        行号

        :return: The line of this NoteDto.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this NoteDto.

        行号

        :param line: The line of this NoteDto.
        :type line: str
        """
        self._line = line

    @property
    def assignee(self):
        """Gets the assignee of this NoteDto.

        :return: The assignee of this NoteDto.
        :rtype: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        return self._assignee

    @assignee.setter
    def assignee(self, assignee):
        """Sets the assignee of this NoteDto.

        :param assignee: The assignee of this NoteDto.
        :type assignee: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        self._assignee = assignee

    @property
    def proposer(self):
        """Gets the proposer of this NoteDto.

        :return: The proposer of this NoteDto.
        :rtype: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        return self._proposer

    @proposer.setter
    def proposer(self, proposer):
        """Sets the proposer of this NoteDto.

        :param proposer: The proposer of this NoteDto.
        :type proposer: :class:`huaweicloudsdkcodehub.v3.UserBasicDto`
        """
        self._proposer = proposer

    @property
    def position(self):
        """Gets the position of this NoteDto.

        :return: The position of this NoteDto.
        :rtype: :class:`huaweicloudsdkcodehub.v3.PositionDto`
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this NoteDto.

        :param position: The position of this NoteDto.
        :type position: :class:`huaweicloudsdkcodehub.v3.PositionDto`
        """
        self._position = position

    @property
    def resolved(self):
        """Gets the resolved of this NoteDto.

        是否解决

        :return: The resolved of this NoteDto.
        :rtype: bool
        """
        return self._resolved

    @resolved.setter
    def resolved(self, resolved):
        """Sets the resolved of this NoteDto.

        是否解决

        :param resolved: The resolved of this NoteDto.
        :type resolved: bool
        """
        self._resolved = resolved

    @property
    def is_outdated(self):
        """Gets the is_outdated of this NoteDto.

        是否过时

        :return: The is_outdated of this NoteDto.
        :rtype: bool
        """
        return self._is_outdated

    @is_outdated.setter
    def is_outdated(self, is_outdated):
        """Sets the is_outdated of this NoteDto.

        是否过时

        :param is_outdated: The is_outdated of this NoteDto.
        :type is_outdated: bool
        """
        self._is_outdated = is_outdated

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
        if not isinstance(other, NoteDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
