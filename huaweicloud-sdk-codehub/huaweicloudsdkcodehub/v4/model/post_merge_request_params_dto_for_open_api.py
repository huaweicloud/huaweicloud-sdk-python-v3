# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostMergeRequestParamsDtoForOpenApi:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'source_branch': 'str',
        'target_branch': 'str',
        'target_repository_id': 'int',
        'reviewer_ids': 'str',
        'assignee_ids': 'str',
        'approval_reviewer_ids': 'str',
        'approval_approvers_ids': 'str',
        'description': 'str',
        'milestone_id': 'int',
        'labels': 'object',
        'force_remove_source_branch': 'bool',
        'squash': 'bool',
        'squash_commit_message': 'str',
        'work_item_ids': 'list[str]',
        'is_use_temp_branch': 'bool',
        'only_assignee_can_merge': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'source_branch': 'source_branch',
        'target_branch': 'target_branch',
        'target_repository_id': 'target_repository_id',
        'reviewer_ids': 'reviewer_ids',
        'assignee_ids': 'assignee_ids',
        'approval_reviewer_ids': 'approval_reviewer_ids',
        'approval_approvers_ids': 'approval_approvers_ids',
        'description': 'description',
        'milestone_id': 'milestone_id',
        'labels': 'labels',
        'force_remove_source_branch': 'force_remove_source_branch',
        'squash': 'squash',
        'squash_commit_message': 'squash_commit_message',
        'work_item_ids': 'work_item_ids',
        'is_use_temp_branch': 'is_use_temp_branch',
        'only_assignee_can_merge': 'only_assignee_can_merge'
    }

    def __init__(self, title=None, source_branch=None, target_branch=None, target_repository_id=None, reviewer_ids=None, assignee_ids=None, approval_reviewer_ids=None, approval_approvers_ids=None, description=None, milestone_id=None, labels=None, force_remove_source_branch=None, squash=None, squash_commit_message=None, work_item_ids=None, is_use_temp_branch=None, only_assignee_can_merge=None):
        r"""PostMergeRequestParamsDtoForOpenApi

        The model defined in huaweicloud sdk

        :param title: 合并请求标题
        :type title: str
        :param source_branch: 源分支
        :type source_branch: str
        :param target_branch: 目标分支
        :type target_branch: str
        :param target_repository_id: 目标仓库id
        :type target_repository_id: int
        :param reviewer_ids: 打分模式评审人ids，使用逗号分隔
        :type reviewer_ids: str
        :param assignee_ids: 合并人ids，使用逗号分隔
        :type assignee_ids: str
        :param approval_reviewer_ids: 审核模式检视人ids，使用逗号分隔
        :type approval_reviewer_ids: str
        :param approval_approvers_ids: 审核人ids，使用逗号分隔
        :type approval_approvers_ids: str
        :param description: 合并请求描述
        :type description: str
        :param milestone_id: 里程碑id
        :type milestone_id: int
        :param labels: 标签名称，使用逗号分隔
        :type labels: object
        :param force_remove_source_branch: 合入后自动删除源分支
        :type force_remove_source_branch: bool
        :param squash: 压缩合并
        :type squash: bool
        :param squash_commit_message: 压缩合并信息
        :type squash_commit_message: str
        :param work_item_ids: e2e单号
        :type work_item_ids: list[str]
        :param is_use_temp_branch: 使用临时分支创建合并请求
        :type is_use_temp_branch: bool
        :param only_assignee_can_merge: 只有合并人允许合入
        :type only_assignee_can_merge: bool
        """
        
        

        self._title = None
        self._source_branch = None
        self._target_branch = None
        self._target_repository_id = None
        self._reviewer_ids = None
        self._assignee_ids = None
        self._approval_reviewer_ids = None
        self._approval_approvers_ids = None
        self._description = None
        self._milestone_id = None
        self._labels = None
        self._force_remove_source_branch = None
        self._squash = None
        self._squash_commit_message = None
        self._work_item_ids = None
        self._is_use_temp_branch = None
        self._only_assignee_can_merge = None
        self.discriminator = None

        self.title = title
        self.source_branch = source_branch
        self.target_branch = target_branch
        if target_repository_id is not None:
            self.target_repository_id = target_repository_id
        if reviewer_ids is not None:
            self.reviewer_ids = reviewer_ids
        if assignee_ids is not None:
            self.assignee_ids = assignee_ids
        if approval_reviewer_ids is not None:
            self.approval_reviewer_ids = approval_reviewer_ids
        if approval_approvers_ids is not None:
            self.approval_approvers_ids = approval_approvers_ids
        if description is not None:
            self.description = description
        if milestone_id is not None:
            self.milestone_id = milestone_id
        if labels is not None:
            self.labels = labels
        if force_remove_source_branch is not None:
            self.force_remove_source_branch = force_remove_source_branch
        if squash is not None:
            self.squash = squash
        if squash_commit_message is not None:
            self.squash_commit_message = squash_commit_message
        if work_item_ids is not None:
            self.work_item_ids = work_item_ids
        if is_use_temp_branch is not None:
            self.is_use_temp_branch = is_use_temp_branch
        if only_assignee_can_merge is not None:
            self.only_assignee_can_merge = only_assignee_can_merge

    @property
    def title(self):
        r"""Gets the title of this PostMergeRequestParamsDtoForOpenApi.

        合并请求标题

        :return: The title of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this PostMergeRequestParamsDtoForOpenApi.

        合并请求标题

        :param title: The title of this PostMergeRequestParamsDtoForOpenApi.
        :type title: str
        """
        self._title = title

    @property
    def source_branch(self):
        r"""Gets the source_branch of this PostMergeRequestParamsDtoForOpenApi.

        源分支

        :return: The source_branch of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this PostMergeRequestParamsDtoForOpenApi.

        源分支

        :param source_branch: The source_branch of this PostMergeRequestParamsDtoForOpenApi.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def target_branch(self):
        r"""Gets the target_branch of this PostMergeRequestParamsDtoForOpenApi.

        目标分支

        :return: The target_branch of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this PostMergeRequestParamsDtoForOpenApi.

        目标分支

        :param target_branch: The target_branch of this PostMergeRequestParamsDtoForOpenApi.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def target_repository_id(self):
        r"""Gets the target_repository_id of this PostMergeRequestParamsDtoForOpenApi.

        目标仓库id

        :return: The target_repository_id of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: int
        """
        return self._target_repository_id

    @target_repository_id.setter
    def target_repository_id(self, target_repository_id):
        r"""Sets the target_repository_id of this PostMergeRequestParamsDtoForOpenApi.

        目标仓库id

        :param target_repository_id: The target_repository_id of this PostMergeRequestParamsDtoForOpenApi.
        :type target_repository_id: int
        """
        self._target_repository_id = target_repository_id

    @property
    def reviewer_ids(self):
        r"""Gets the reviewer_ids of this PostMergeRequestParamsDtoForOpenApi.

        打分模式评审人ids，使用逗号分隔

        :return: The reviewer_ids of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: str
        """
        return self._reviewer_ids

    @reviewer_ids.setter
    def reviewer_ids(self, reviewer_ids):
        r"""Sets the reviewer_ids of this PostMergeRequestParamsDtoForOpenApi.

        打分模式评审人ids，使用逗号分隔

        :param reviewer_ids: The reviewer_ids of this PostMergeRequestParamsDtoForOpenApi.
        :type reviewer_ids: str
        """
        self._reviewer_ids = reviewer_ids

    @property
    def assignee_ids(self):
        r"""Gets the assignee_ids of this PostMergeRequestParamsDtoForOpenApi.

        合并人ids，使用逗号分隔

        :return: The assignee_ids of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: str
        """
        return self._assignee_ids

    @assignee_ids.setter
    def assignee_ids(self, assignee_ids):
        r"""Sets the assignee_ids of this PostMergeRequestParamsDtoForOpenApi.

        合并人ids，使用逗号分隔

        :param assignee_ids: The assignee_ids of this PostMergeRequestParamsDtoForOpenApi.
        :type assignee_ids: str
        """
        self._assignee_ids = assignee_ids

    @property
    def approval_reviewer_ids(self):
        r"""Gets the approval_reviewer_ids of this PostMergeRequestParamsDtoForOpenApi.

        审核模式检视人ids，使用逗号分隔

        :return: The approval_reviewer_ids of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: str
        """
        return self._approval_reviewer_ids

    @approval_reviewer_ids.setter
    def approval_reviewer_ids(self, approval_reviewer_ids):
        r"""Sets the approval_reviewer_ids of this PostMergeRequestParamsDtoForOpenApi.

        审核模式检视人ids，使用逗号分隔

        :param approval_reviewer_ids: The approval_reviewer_ids of this PostMergeRequestParamsDtoForOpenApi.
        :type approval_reviewer_ids: str
        """
        self._approval_reviewer_ids = approval_reviewer_ids

    @property
    def approval_approvers_ids(self):
        r"""Gets the approval_approvers_ids of this PostMergeRequestParamsDtoForOpenApi.

        审核人ids，使用逗号分隔

        :return: The approval_approvers_ids of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: str
        """
        return self._approval_approvers_ids

    @approval_approvers_ids.setter
    def approval_approvers_ids(self, approval_approvers_ids):
        r"""Sets the approval_approvers_ids of this PostMergeRequestParamsDtoForOpenApi.

        审核人ids，使用逗号分隔

        :param approval_approvers_ids: The approval_approvers_ids of this PostMergeRequestParamsDtoForOpenApi.
        :type approval_approvers_ids: str
        """
        self._approval_approvers_ids = approval_approvers_ids

    @property
    def description(self):
        r"""Gets the description of this PostMergeRequestParamsDtoForOpenApi.

        合并请求描述

        :return: The description of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PostMergeRequestParamsDtoForOpenApi.

        合并请求描述

        :param description: The description of this PostMergeRequestParamsDtoForOpenApi.
        :type description: str
        """
        self._description = description

    @property
    def milestone_id(self):
        r"""Gets the milestone_id of this PostMergeRequestParamsDtoForOpenApi.

        里程碑id

        :return: The milestone_id of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: int
        """
        return self._milestone_id

    @milestone_id.setter
    def milestone_id(self, milestone_id):
        r"""Sets the milestone_id of this PostMergeRequestParamsDtoForOpenApi.

        里程碑id

        :param milestone_id: The milestone_id of this PostMergeRequestParamsDtoForOpenApi.
        :type milestone_id: int
        """
        self._milestone_id = milestone_id

    @property
    def labels(self):
        r"""Gets the labels of this PostMergeRequestParamsDtoForOpenApi.

        标签名称，使用逗号分隔

        :return: The labels of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this PostMergeRequestParamsDtoForOpenApi.

        标签名称，使用逗号分隔

        :param labels: The labels of this PostMergeRequestParamsDtoForOpenApi.
        :type labels: object
        """
        self._labels = labels

    @property
    def force_remove_source_branch(self):
        r"""Gets the force_remove_source_branch of this PostMergeRequestParamsDtoForOpenApi.

        合入后自动删除源分支

        :return: The force_remove_source_branch of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: bool
        """
        return self._force_remove_source_branch

    @force_remove_source_branch.setter
    def force_remove_source_branch(self, force_remove_source_branch):
        r"""Sets the force_remove_source_branch of this PostMergeRequestParamsDtoForOpenApi.

        合入后自动删除源分支

        :param force_remove_source_branch: The force_remove_source_branch of this PostMergeRequestParamsDtoForOpenApi.
        :type force_remove_source_branch: bool
        """
        self._force_remove_source_branch = force_remove_source_branch

    @property
    def squash(self):
        r"""Gets the squash of this PostMergeRequestParamsDtoForOpenApi.

        压缩合并

        :return: The squash of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: bool
        """
        return self._squash

    @squash.setter
    def squash(self, squash):
        r"""Sets the squash of this PostMergeRequestParamsDtoForOpenApi.

        压缩合并

        :param squash: The squash of this PostMergeRequestParamsDtoForOpenApi.
        :type squash: bool
        """
        self._squash = squash

    @property
    def squash_commit_message(self):
        r"""Gets the squash_commit_message of this PostMergeRequestParamsDtoForOpenApi.

        压缩合并信息

        :return: The squash_commit_message of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: str
        """
        return self._squash_commit_message

    @squash_commit_message.setter
    def squash_commit_message(self, squash_commit_message):
        r"""Sets the squash_commit_message of this PostMergeRequestParamsDtoForOpenApi.

        压缩合并信息

        :param squash_commit_message: The squash_commit_message of this PostMergeRequestParamsDtoForOpenApi.
        :type squash_commit_message: str
        """
        self._squash_commit_message = squash_commit_message

    @property
    def work_item_ids(self):
        r"""Gets the work_item_ids of this PostMergeRequestParamsDtoForOpenApi.

        e2e单号

        :return: The work_item_ids of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: list[str]
        """
        return self._work_item_ids

    @work_item_ids.setter
    def work_item_ids(self, work_item_ids):
        r"""Sets the work_item_ids of this PostMergeRequestParamsDtoForOpenApi.

        e2e单号

        :param work_item_ids: The work_item_ids of this PostMergeRequestParamsDtoForOpenApi.
        :type work_item_ids: list[str]
        """
        self._work_item_ids = work_item_ids

    @property
    def is_use_temp_branch(self):
        r"""Gets the is_use_temp_branch of this PostMergeRequestParamsDtoForOpenApi.

        使用临时分支创建合并请求

        :return: The is_use_temp_branch of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: bool
        """
        return self._is_use_temp_branch

    @is_use_temp_branch.setter
    def is_use_temp_branch(self, is_use_temp_branch):
        r"""Sets the is_use_temp_branch of this PostMergeRequestParamsDtoForOpenApi.

        使用临时分支创建合并请求

        :param is_use_temp_branch: The is_use_temp_branch of this PostMergeRequestParamsDtoForOpenApi.
        :type is_use_temp_branch: bool
        """
        self._is_use_temp_branch = is_use_temp_branch

    @property
    def only_assignee_can_merge(self):
        r"""Gets the only_assignee_can_merge of this PostMergeRequestParamsDtoForOpenApi.

        只有合并人允许合入

        :return: The only_assignee_can_merge of this PostMergeRequestParamsDtoForOpenApi.
        :rtype: bool
        """
        return self._only_assignee_can_merge

    @only_assignee_can_merge.setter
    def only_assignee_can_merge(self, only_assignee_can_merge):
        r"""Sets the only_assignee_can_merge of this PostMergeRequestParamsDtoForOpenApi.

        只有合并人允许合入

        :param only_assignee_can_merge: The only_assignee_can_merge of this PostMergeRequestParamsDtoForOpenApi.
        :type only_assignee_can_merge: bool
        """
        self._only_assignee_can_merge = only_assignee_can_merge

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
        if not isinstance(other, PostMergeRequestParamsDtoForOpenApi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
