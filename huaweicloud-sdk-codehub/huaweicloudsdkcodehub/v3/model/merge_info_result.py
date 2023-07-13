# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MergeInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'approval_merge_request_approvers': 'list[ApprovalMergeRequestApproversItem]',
        'author': 'Author',
        'closed_at': 'str',
        'created_at': 'str',
        'description': 'str',
        'devcloud_source_branch': 'str',
        'id': 'float',
        'iid': 'float',
        'is_source_branch_exist': 'bool',
        'merge_request_assignee_list': 'list[MergeRequestAssigneeListItem]',
        'merge_request_diff': 'MergeRequestDiff',
        'merge_status': 'str',
        'source_branch': 'str',
        'state': 'str',
        'target_branch': 'str',
        'title': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'approval_merge_request_approvers': 'approval_merge_request_approvers',
        'author': 'author',
        'closed_at': 'closed_at',
        'created_at': 'created_at',
        'description': 'description',
        'devcloud_source_branch': 'devcloud_source_branch',
        'id': 'id',
        'iid': 'iid',
        'is_source_branch_exist': 'is_source_branch_exist',
        'merge_request_assignee_list': 'merge_request_assignee_list',
        'merge_request_diff': 'merge_request_diff',
        'merge_status': 'merge_status',
        'source_branch': 'source_branch',
        'state': 'state',
        'target_branch': 'target_branch',
        'title': 'title',
        'updated_at': 'updated_at'
    }

    def __init__(self, approval_merge_request_approvers=None, author=None, closed_at=None, created_at=None, description=None, devcloud_source_branch=None, id=None, iid=None, is_source_branch_exist=None, merge_request_assignee_list=None, merge_request_diff=None, merge_status=None, source_branch=None, state=None, target_branch=None, title=None, updated_at=None):
        """MergeInfoResult

        The model defined in huaweicloud sdk

        :param approval_merge_request_approvers: 评审人
        :type approval_merge_request_approvers: list[:class:`huaweicloudsdkcodehub.v3.ApprovalMergeRequestApproversItem`]
        :param author: 
        :type author: :class:`huaweicloudsdkcodehub.v3.Author`
        :param closed_at: 关闭时间
        :type closed_at: str
        :param created_at: 创建时间
        :type created_at: str
        :param description: 合并请求描述
        :type description: str
        :param devcloud_source_branch: 源分支
        :type devcloud_source_branch: str
        :param id: 合并请求id
        :type id: float
        :param iid: 当前仓库内合并请求序号
        :type iid: float
        :param is_source_branch_exist: 源分支是否存在
        :type is_source_branch_exist: bool
        :param merge_request_assignee_list: 检视人
        :type merge_request_assignee_list: list[:class:`huaweicloudsdkcodehub.v3.MergeRequestAssigneeListItem`]
        :param merge_request_diff: 
        :type merge_request_diff: :class:`huaweicloudsdkcodehub.v3.MergeRequestDiff`
        :param merge_status: 是否可以被合并
        :type merge_status: str
        :param source_branch: 源分支
        :type source_branch: str
        :param state: 合并请求状态
        :type state: str
        :param target_branch: 目标分支
        :type target_branch: str
        :param title: 标题
        :type title: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._approval_merge_request_approvers = None
        self._author = None
        self._closed_at = None
        self._created_at = None
        self._description = None
        self._devcloud_source_branch = None
        self._id = None
        self._iid = None
        self._is_source_branch_exist = None
        self._merge_request_assignee_list = None
        self._merge_request_diff = None
        self._merge_status = None
        self._source_branch = None
        self._state = None
        self._target_branch = None
        self._title = None
        self._updated_at = None
        self.discriminator = None

        if approval_merge_request_approvers is not None:
            self.approval_merge_request_approvers = approval_merge_request_approvers
        if author is not None:
            self.author = author
        if closed_at is not None:
            self.closed_at = closed_at
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if devcloud_source_branch is not None:
            self.devcloud_source_branch = devcloud_source_branch
        if id is not None:
            self.id = id
        if iid is not None:
            self.iid = iid
        if is_source_branch_exist is not None:
            self.is_source_branch_exist = is_source_branch_exist
        if merge_request_assignee_list is not None:
            self.merge_request_assignee_list = merge_request_assignee_list
        if merge_request_diff is not None:
            self.merge_request_diff = merge_request_diff
        if merge_status is not None:
            self.merge_status = merge_status
        if source_branch is not None:
            self.source_branch = source_branch
        if state is not None:
            self.state = state
        if target_branch is not None:
            self.target_branch = target_branch
        if title is not None:
            self.title = title
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def approval_merge_request_approvers(self):
        """Gets the approval_merge_request_approvers of this MergeInfoResult.

        评审人

        :return: The approval_merge_request_approvers of this MergeInfoResult.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.ApprovalMergeRequestApproversItem`]
        """
        return self._approval_merge_request_approvers

    @approval_merge_request_approvers.setter
    def approval_merge_request_approvers(self, approval_merge_request_approvers):
        """Sets the approval_merge_request_approvers of this MergeInfoResult.

        评审人

        :param approval_merge_request_approvers: The approval_merge_request_approvers of this MergeInfoResult.
        :type approval_merge_request_approvers: list[:class:`huaweicloudsdkcodehub.v3.ApprovalMergeRequestApproversItem`]
        """
        self._approval_merge_request_approvers = approval_merge_request_approvers

    @property
    def author(self):
        """Gets the author of this MergeInfoResult.

        :return: The author of this MergeInfoResult.
        :rtype: :class:`huaweicloudsdkcodehub.v3.Author`
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this MergeInfoResult.

        :param author: The author of this MergeInfoResult.
        :type author: :class:`huaweicloudsdkcodehub.v3.Author`
        """
        self._author = author

    @property
    def closed_at(self):
        """Gets the closed_at of this MergeInfoResult.

        关闭时间

        :return: The closed_at of this MergeInfoResult.
        :rtype: str
        """
        return self._closed_at

    @closed_at.setter
    def closed_at(self, closed_at):
        """Sets the closed_at of this MergeInfoResult.

        关闭时间

        :param closed_at: The closed_at of this MergeInfoResult.
        :type closed_at: str
        """
        self._closed_at = closed_at

    @property
    def created_at(self):
        """Gets the created_at of this MergeInfoResult.

        创建时间

        :return: The created_at of this MergeInfoResult.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MergeInfoResult.

        创建时间

        :param created_at: The created_at of this MergeInfoResult.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this MergeInfoResult.

        合并请求描述

        :return: The description of this MergeInfoResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MergeInfoResult.

        合并请求描述

        :param description: The description of this MergeInfoResult.
        :type description: str
        """
        self._description = description

    @property
    def devcloud_source_branch(self):
        """Gets the devcloud_source_branch of this MergeInfoResult.

        源分支

        :return: The devcloud_source_branch of this MergeInfoResult.
        :rtype: str
        """
        return self._devcloud_source_branch

    @devcloud_source_branch.setter
    def devcloud_source_branch(self, devcloud_source_branch):
        """Sets the devcloud_source_branch of this MergeInfoResult.

        源分支

        :param devcloud_source_branch: The devcloud_source_branch of this MergeInfoResult.
        :type devcloud_source_branch: str
        """
        self._devcloud_source_branch = devcloud_source_branch

    @property
    def id(self):
        """Gets the id of this MergeInfoResult.

        合并请求id

        :return: The id of this MergeInfoResult.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MergeInfoResult.

        合并请求id

        :param id: The id of this MergeInfoResult.
        :type id: float
        """
        self._id = id

    @property
    def iid(self):
        """Gets the iid of this MergeInfoResult.

        当前仓库内合并请求序号

        :return: The iid of this MergeInfoResult.
        :rtype: float
        """
        return self._iid

    @iid.setter
    def iid(self, iid):
        """Sets the iid of this MergeInfoResult.

        当前仓库内合并请求序号

        :param iid: The iid of this MergeInfoResult.
        :type iid: float
        """
        self._iid = iid

    @property
    def is_source_branch_exist(self):
        """Gets the is_source_branch_exist of this MergeInfoResult.

        源分支是否存在

        :return: The is_source_branch_exist of this MergeInfoResult.
        :rtype: bool
        """
        return self._is_source_branch_exist

    @is_source_branch_exist.setter
    def is_source_branch_exist(self, is_source_branch_exist):
        """Sets the is_source_branch_exist of this MergeInfoResult.

        源分支是否存在

        :param is_source_branch_exist: The is_source_branch_exist of this MergeInfoResult.
        :type is_source_branch_exist: bool
        """
        self._is_source_branch_exist = is_source_branch_exist

    @property
    def merge_request_assignee_list(self):
        """Gets the merge_request_assignee_list of this MergeInfoResult.

        检视人

        :return: The merge_request_assignee_list of this MergeInfoResult.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.MergeRequestAssigneeListItem`]
        """
        return self._merge_request_assignee_list

    @merge_request_assignee_list.setter
    def merge_request_assignee_list(self, merge_request_assignee_list):
        """Sets the merge_request_assignee_list of this MergeInfoResult.

        检视人

        :param merge_request_assignee_list: The merge_request_assignee_list of this MergeInfoResult.
        :type merge_request_assignee_list: list[:class:`huaweicloudsdkcodehub.v3.MergeRequestAssigneeListItem`]
        """
        self._merge_request_assignee_list = merge_request_assignee_list

    @property
    def merge_request_diff(self):
        """Gets the merge_request_diff of this MergeInfoResult.

        :return: The merge_request_diff of this MergeInfoResult.
        :rtype: :class:`huaweicloudsdkcodehub.v3.MergeRequestDiff`
        """
        return self._merge_request_diff

    @merge_request_diff.setter
    def merge_request_diff(self, merge_request_diff):
        """Sets the merge_request_diff of this MergeInfoResult.

        :param merge_request_diff: The merge_request_diff of this MergeInfoResult.
        :type merge_request_diff: :class:`huaweicloudsdkcodehub.v3.MergeRequestDiff`
        """
        self._merge_request_diff = merge_request_diff

    @property
    def merge_status(self):
        """Gets the merge_status of this MergeInfoResult.

        是否可以被合并

        :return: The merge_status of this MergeInfoResult.
        :rtype: str
        """
        return self._merge_status

    @merge_status.setter
    def merge_status(self, merge_status):
        """Sets the merge_status of this MergeInfoResult.

        是否可以被合并

        :param merge_status: The merge_status of this MergeInfoResult.
        :type merge_status: str
        """
        self._merge_status = merge_status

    @property
    def source_branch(self):
        """Gets the source_branch of this MergeInfoResult.

        源分支

        :return: The source_branch of this MergeInfoResult.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        """Sets the source_branch of this MergeInfoResult.

        源分支

        :param source_branch: The source_branch of this MergeInfoResult.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def state(self):
        """Gets the state of this MergeInfoResult.

        合并请求状态

        :return: The state of this MergeInfoResult.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MergeInfoResult.

        合并请求状态

        :param state: The state of this MergeInfoResult.
        :type state: str
        """
        self._state = state

    @property
    def target_branch(self):
        """Gets the target_branch of this MergeInfoResult.

        目标分支

        :return: The target_branch of this MergeInfoResult.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        """Sets the target_branch of this MergeInfoResult.

        目标分支

        :param target_branch: The target_branch of this MergeInfoResult.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def title(self):
        """Gets the title of this MergeInfoResult.

        标题

        :return: The title of this MergeInfoResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MergeInfoResult.

        标题

        :param title: The title of this MergeInfoResult.
        :type title: str
        """
        self._title = title

    @property
    def updated_at(self):
        """Gets the updated_at of this MergeInfoResult.

        更新时间

        :return: The updated_at of this MergeInfoResult.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this MergeInfoResult.

        更新时间

        :param updated_at: The updated_at of this MergeInfoResult.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, MergeInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
