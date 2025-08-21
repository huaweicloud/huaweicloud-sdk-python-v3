# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportMrParamsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iid': 'int',
        'source_uniq_key': 'str',
        'author_id': 'int',
        'state': 'str',
        'title': 'str',
        'description': 'str',
        'source_branch': 'str',
        'target_branch': 'str',
        'target_repository_id': 'str',
        'labels': 'object',
        'created_at': 'str',
        'updated_at': 'str',
        'merged_at': 'str',
        'closed_at': 'str',
        'approvers': 'list[ApproverParamDto]',
        'diff_refs': 'list[DiffRefsParamDto]',
        'squash': 'bool',
        'remove_source_branch': 'bool',
        'branch_is_deleted': 'bool',
        'fork': 'bool',
        'import_source_from': 'str'
    }

    attribute_map = {
        'iid': 'iid',
        'source_uniq_key': 'source_uniq_key',
        'author_id': 'author_id',
        'state': 'state',
        'title': 'title',
        'description': 'description',
        'source_branch': 'source_branch',
        'target_branch': 'target_branch',
        'target_repository_id': 'target_repository_id',
        'labels': 'labels',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'merged_at': 'merged_at',
        'closed_at': 'closed_at',
        'approvers': 'approvers',
        'diff_refs': 'diff_refs',
        'squash': 'squash',
        'remove_source_branch': 'remove_source_branch',
        'branch_is_deleted': 'branch_is_deleted',
        'fork': 'fork',
        'import_source_from': 'import_source_from'
    }

    def __init__(self, iid=None, source_uniq_key=None, author_id=None, state=None, title=None, description=None, source_branch=None, target_branch=None, target_repository_id=None, labels=None, created_at=None, updated_at=None, merged_at=None, closed_at=None, approvers=None, diff_refs=None, squash=None, remove_source_branch=None, branch_is_deleted=None, fork=None, import_source_from=None):
        r"""ImportMrParamsDto

        The model defined in huaweicloud sdk

        :param iid: 合并请求iid
        :type iid: int
        :param source_uniq_key: 导入唯一标识
        :type source_uniq_key: str
        :param author_id: 作者id
        :type author_id: int
        :param state: 状态
        :type state: str
        :param title: 标题
        :type title: str
        :param description: 描述
        :type description: str
        :param source_branch: 源分支
        :type source_branch: str
        :param target_branch: 目标分支
        :type target_branch: str
        :param target_repository_id: 目标仓库
        :type target_repository_id: str
        :param labels: 标签
        :type labels: object
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param merged_at: 合并时间
        :type merged_at: str
        :param closed_at: 关闭时间
        :type closed_at: str
        :param approvers: 审核人列表
        :type approvers: list[:class:`huaweicloudsdkcodehub.v4.ApproverParamDto`]
        :param diff_refs: 合并请求变更commit列表
        :type diff_refs: list[:class:`huaweicloudsdkcodehub.v4.DiffRefsParamDto`]
        :param squash: squash合并
        :type squash: bool
        :param remove_source_branch: 合并mr后删除源分支
        :type remove_source_branch: bool
        :param branch_is_deleted: 源分支是否被删除
        :type branch_is_deleted: bool
        :param fork: 源合并请求是否是fork合并请求
        :type fork: bool
        :param import_source_from: 导入来源
        :type import_source_from: str
        """
        
        

        self._iid = None
        self._source_uniq_key = None
        self._author_id = None
        self._state = None
        self._title = None
        self._description = None
        self._source_branch = None
        self._target_branch = None
        self._target_repository_id = None
        self._labels = None
        self._created_at = None
        self._updated_at = None
        self._merged_at = None
        self._closed_at = None
        self._approvers = None
        self._diff_refs = None
        self._squash = None
        self._remove_source_branch = None
        self._branch_is_deleted = None
        self._fork = None
        self._import_source_from = None
        self.discriminator = None

        self.iid = iid
        self.source_uniq_key = source_uniq_key
        if author_id is not None:
            self.author_id = author_id
        self.state = state
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        self.source_branch = source_branch
        self.target_branch = target_branch
        self.target_repository_id = target_repository_id
        if labels is not None:
            self.labels = labels
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if merged_at is not None:
            self.merged_at = merged_at
        if closed_at is not None:
            self.closed_at = closed_at
        if approvers is not None:
            self.approvers = approvers
        self.diff_refs = diff_refs
        if squash is not None:
            self.squash = squash
        if remove_source_branch is not None:
            self.remove_source_branch = remove_source_branch
        if branch_is_deleted is not None:
            self.branch_is_deleted = branch_is_deleted
        if fork is not None:
            self.fork = fork
        if import_source_from is not None:
            self.import_source_from = import_source_from

    @property
    def iid(self):
        r"""Gets the iid of this ImportMrParamsDto.

        合并请求iid

        :return: The iid of this ImportMrParamsDto.
        :rtype: int
        """
        return self._iid

    @iid.setter
    def iid(self, iid):
        r"""Sets the iid of this ImportMrParamsDto.

        合并请求iid

        :param iid: The iid of this ImportMrParamsDto.
        :type iid: int
        """
        self._iid = iid

    @property
    def source_uniq_key(self):
        r"""Gets the source_uniq_key of this ImportMrParamsDto.

        导入唯一标识

        :return: The source_uniq_key of this ImportMrParamsDto.
        :rtype: str
        """
        return self._source_uniq_key

    @source_uniq_key.setter
    def source_uniq_key(self, source_uniq_key):
        r"""Sets the source_uniq_key of this ImportMrParamsDto.

        导入唯一标识

        :param source_uniq_key: The source_uniq_key of this ImportMrParamsDto.
        :type source_uniq_key: str
        """
        self._source_uniq_key = source_uniq_key

    @property
    def author_id(self):
        r"""Gets the author_id of this ImportMrParamsDto.

        作者id

        :return: The author_id of this ImportMrParamsDto.
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        r"""Sets the author_id of this ImportMrParamsDto.

        作者id

        :param author_id: The author_id of this ImportMrParamsDto.
        :type author_id: int
        """
        self._author_id = author_id

    @property
    def state(self):
        r"""Gets the state of this ImportMrParamsDto.

        状态

        :return: The state of this ImportMrParamsDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ImportMrParamsDto.

        状态

        :param state: The state of this ImportMrParamsDto.
        :type state: str
        """
        self._state = state

    @property
    def title(self):
        r"""Gets the title of this ImportMrParamsDto.

        标题

        :return: The title of this ImportMrParamsDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ImportMrParamsDto.

        标题

        :param title: The title of this ImportMrParamsDto.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this ImportMrParamsDto.

        描述

        :return: The description of this ImportMrParamsDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImportMrParamsDto.

        描述

        :param description: The description of this ImportMrParamsDto.
        :type description: str
        """
        self._description = description

    @property
    def source_branch(self):
        r"""Gets the source_branch of this ImportMrParamsDto.

        源分支

        :return: The source_branch of this ImportMrParamsDto.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this ImportMrParamsDto.

        源分支

        :param source_branch: The source_branch of this ImportMrParamsDto.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def target_branch(self):
        r"""Gets the target_branch of this ImportMrParamsDto.

        目标分支

        :return: The target_branch of this ImportMrParamsDto.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this ImportMrParamsDto.

        目标分支

        :param target_branch: The target_branch of this ImportMrParamsDto.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def target_repository_id(self):
        r"""Gets the target_repository_id of this ImportMrParamsDto.

        目标仓库

        :return: The target_repository_id of this ImportMrParamsDto.
        :rtype: str
        """
        return self._target_repository_id

    @target_repository_id.setter
    def target_repository_id(self, target_repository_id):
        r"""Sets the target_repository_id of this ImportMrParamsDto.

        目标仓库

        :param target_repository_id: The target_repository_id of this ImportMrParamsDto.
        :type target_repository_id: str
        """
        self._target_repository_id = target_repository_id

    @property
    def labels(self):
        r"""Gets the labels of this ImportMrParamsDto.

        标签

        :return: The labels of this ImportMrParamsDto.
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ImportMrParamsDto.

        标签

        :param labels: The labels of this ImportMrParamsDto.
        :type labels: object
        """
        self._labels = labels

    @property
    def created_at(self):
        r"""Gets the created_at of this ImportMrParamsDto.

        创建时间

        :return: The created_at of this ImportMrParamsDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ImportMrParamsDto.

        创建时间

        :param created_at: The created_at of this ImportMrParamsDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ImportMrParamsDto.

        更新时间

        :return: The updated_at of this ImportMrParamsDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ImportMrParamsDto.

        更新时间

        :param updated_at: The updated_at of this ImportMrParamsDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def merged_at(self):
        r"""Gets the merged_at of this ImportMrParamsDto.

        合并时间

        :return: The merged_at of this ImportMrParamsDto.
        :rtype: str
        """
        return self._merged_at

    @merged_at.setter
    def merged_at(self, merged_at):
        r"""Sets the merged_at of this ImportMrParamsDto.

        合并时间

        :param merged_at: The merged_at of this ImportMrParamsDto.
        :type merged_at: str
        """
        self._merged_at = merged_at

    @property
    def closed_at(self):
        r"""Gets the closed_at of this ImportMrParamsDto.

        关闭时间

        :return: The closed_at of this ImportMrParamsDto.
        :rtype: str
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        r"""Sets the closed_at of this ImportMrParamsDto.

        关闭时间

        :param closed_at: The closed_at of this ImportMrParamsDto.
        :type closed_at: str
        """
        self._closed_at = closed_at

    @property
    def approvers(self):
        r"""Gets the approvers of this ImportMrParamsDto.

        审核人列表

        :return: The approvers of this ImportMrParamsDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ApproverParamDto`]
        """
        return self._approvers

    @approvers.setter
    def approvers(self, approvers):
        r"""Sets the approvers of this ImportMrParamsDto.

        审核人列表

        :param approvers: The approvers of this ImportMrParamsDto.
        :type approvers: list[:class:`huaweicloudsdkcodehub.v4.ApproverParamDto`]
        """
        self._approvers = approvers

    @property
    def diff_refs(self):
        r"""Gets the diff_refs of this ImportMrParamsDto.

        合并请求变更commit列表

        :return: The diff_refs of this ImportMrParamsDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.DiffRefsParamDto`]
        """
        return self._diff_refs

    @diff_refs.setter
    def diff_refs(self, diff_refs):
        r"""Sets the diff_refs of this ImportMrParamsDto.

        合并请求变更commit列表

        :param diff_refs: The diff_refs of this ImportMrParamsDto.
        :type diff_refs: list[:class:`huaweicloudsdkcodehub.v4.DiffRefsParamDto`]
        """
        self._diff_refs = diff_refs

    @property
    def squash(self):
        r"""Gets the squash of this ImportMrParamsDto.

        squash合并

        :return: The squash of this ImportMrParamsDto.
        :rtype: bool
        """
        return self._squash

    @squash.setter
    def squash(self, squash):
        r"""Sets the squash of this ImportMrParamsDto.

        squash合并

        :param squash: The squash of this ImportMrParamsDto.
        :type squash: bool
        """
        self._squash = squash

    @property
    def remove_source_branch(self):
        r"""Gets the remove_source_branch of this ImportMrParamsDto.

        合并mr后删除源分支

        :return: The remove_source_branch of this ImportMrParamsDto.
        :rtype: bool
        """
        return self._remove_source_branch

    @remove_source_branch.setter
    def remove_source_branch(self, remove_source_branch):
        r"""Sets the remove_source_branch of this ImportMrParamsDto.

        合并mr后删除源分支

        :param remove_source_branch: The remove_source_branch of this ImportMrParamsDto.
        :type remove_source_branch: bool
        """
        self._remove_source_branch = remove_source_branch

    @property
    def branch_is_deleted(self):
        r"""Gets the branch_is_deleted of this ImportMrParamsDto.

        源分支是否被删除

        :return: The branch_is_deleted of this ImportMrParamsDto.
        :rtype: bool
        """
        return self._branch_is_deleted

    @branch_is_deleted.setter
    def branch_is_deleted(self, branch_is_deleted):
        r"""Sets the branch_is_deleted of this ImportMrParamsDto.

        源分支是否被删除

        :param branch_is_deleted: The branch_is_deleted of this ImportMrParamsDto.
        :type branch_is_deleted: bool
        """
        self._branch_is_deleted = branch_is_deleted

    @property
    def fork(self):
        r"""Gets the fork of this ImportMrParamsDto.

        源合并请求是否是fork合并请求

        :return: The fork of this ImportMrParamsDto.
        :rtype: bool
        """
        return self._fork

    @fork.setter
    def fork(self, fork):
        r"""Sets the fork of this ImportMrParamsDto.

        源合并请求是否是fork合并请求

        :param fork: The fork of this ImportMrParamsDto.
        :type fork: bool
        """
        self._fork = fork

    @property
    def import_source_from(self):
        r"""Gets the import_source_from of this ImportMrParamsDto.

        导入来源

        :return: The import_source_from of this ImportMrParamsDto.
        :rtype: str
        """
        return self._import_source_from

    @import_source_from.setter
    def import_source_from(self, import_source_from):
        r"""Sets the import_source_from of this ImportMrParamsDto.

        导入来源

        :param import_source_from: The import_source_from of this ImportMrParamsDto.
        :type import_source_from: str
        """
        self._import_source_from = import_source_from

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
        if not isinstance(other, ImportMrParamsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
