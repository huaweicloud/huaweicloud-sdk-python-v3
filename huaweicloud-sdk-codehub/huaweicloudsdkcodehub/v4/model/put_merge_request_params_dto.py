# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutMergeRequestParamsDto:

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
        'state_event': 'str',
        'assignee_ids': 'str',
        'reviewer_ids': 'str',
        'description': 'str',
        'milestone_id': 'int',
        'labels': 'object',
        'force_remove_source_branch': 'bool',
        'squash': 'bool',
        'squash_commit_message': 'str',
        'work_item_ids': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'state_event': 'state_event',
        'assignee_ids': 'assignee_ids',
        'reviewer_ids': 'reviewer_ids',
        'description': 'description',
        'milestone_id': 'milestone_id',
        'labels': 'labels',
        'force_remove_source_branch': 'force_remove_source_branch',
        'squash': 'squash',
        'squash_commit_message': 'squash_commit_message',
        'work_item_ids': 'work_item_ids'
    }

    def __init__(self, title=None, state_event=None, assignee_ids=None, reviewer_ids=None, description=None, milestone_id=None, labels=None, force_remove_source_branch=None, squash=None, squash_commit_message=None, work_item_ids=None):
        r"""PutMergeRequestParamsDto

        The model defined in huaweicloud sdk

        :param title: 合并请求标题
        :type title: str
        :param state_event: 合并请求状态
        :type state_event: str
        :param assignee_ids: 合并人id列表
        :type assignee_ids: str
        :param reviewer_ids: 评审人id列表
        :type reviewer_ids: str
        :param description: 合并请求描述
        :type description: str
        :param milestone_id: 里程碑id
        :type milestone_id: int
        :param labels: 标签
        :type labels: object
        :param force_remove_source_branch: 合入后删除源分支
        :type force_remove_source_branch: bool
        :param squash: squash合入
        :type squash: bool
        :param squash_commit_message: squash提交信息
        :type squash_commit_message: str
        :param work_item_ids: e2e单号
        :type work_item_ids: list[str]
        """
        
        

        self._title = None
        self._state_event = None
        self._assignee_ids = None
        self._reviewer_ids = None
        self._description = None
        self._milestone_id = None
        self._labels = None
        self._force_remove_source_branch = None
        self._squash = None
        self._squash_commit_message = None
        self._work_item_ids = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if state_event is not None:
            self.state_event = state_event
        if assignee_ids is not None:
            self.assignee_ids = assignee_ids
        if reviewer_ids is not None:
            self.reviewer_ids = reviewer_ids
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

    @property
    def title(self):
        r"""Gets the title of this PutMergeRequestParamsDto.

        合并请求标题

        :return: The title of this PutMergeRequestParamsDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this PutMergeRequestParamsDto.

        合并请求标题

        :param title: The title of this PutMergeRequestParamsDto.
        :type title: str
        """
        self._title = title

    @property
    def state_event(self):
        r"""Gets the state_event of this PutMergeRequestParamsDto.

        合并请求状态

        :return: The state_event of this PutMergeRequestParamsDto.
        :rtype: str
        """
        return self._state_event

    @state_event.setter
    def state_event(self, state_event):
        r"""Sets the state_event of this PutMergeRequestParamsDto.

        合并请求状态

        :param state_event: The state_event of this PutMergeRequestParamsDto.
        :type state_event: str
        """
        self._state_event = state_event

    @property
    def assignee_ids(self):
        r"""Gets the assignee_ids of this PutMergeRequestParamsDto.

        合并人id列表

        :return: The assignee_ids of this PutMergeRequestParamsDto.
        :rtype: str
        """
        return self._assignee_ids

    @assignee_ids.setter
    def assignee_ids(self, assignee_ids):
        r"""Sets the assignee_ids of this PutMergeRequestParamsDto.

        合并人id列表

        :param assignee_ids: The assignee_ids of this PutMergeRequestParamsDto.
        :type assignee_ids: str
        """
        self._assignee_ids = assignee_ids

    @property
    def reviewer_ids(self):
        r"""Gets the reviewer_ids of this PutMergeRequestParamsDto.

        评审人id列表

        :return: The reviewer_ids of this PutMergeRequestParamsDto.
        :rtype: str
        """
        return self._reviewer_ids

    @reviewer_ids.setter
    def reviewer_ids(self, reviewer_ids):
        r"""Sets the reviewer_ids of this PutMergeRequestParamsDto.

        评审人id列表

        :param reviewer_ids: The reviewer_ids of this PutMergeRequestParamsDto.
        :type reviewer_ids: str
        """
        self._reviewer_ids = reviewer_ids

    @property
    def description(self):
        r"""Gets the description of this PutMergeRequestParamsDto.

        合并请求描述

        :return: The description of this PutMergeRequestParamsDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PutMergeRequestParamsDto.

        合并请求描述

        :param description: The description of this PutMergeRequestParamsDto.
        :type description: str
        """
        self._description = description

    @property
    def milestone_id(self):
        r"""Gets the milestone_id of this PutMergeRequestParamsDto.

        里程碑id

        :return: The milestone_id of this PutMergeRequestParamsDto.
        :rtype: int
        """
        return self._milestone_id

    @milestone_id.setter
    def milestone_id(self, milestone_id):
        r"""Sets the milestone_id of this PutMergeRequestParamsDto.

        里程碑id

        :param milestone_id: The milestone_id of this PutMergeRequestParamsDto.
        :type milestone_id: int
        """
        self._milestone_id = milestone_id

    @property
    def labels(self):
        r"""Gets the labels of this PutMergeRequestParamsDto.

        标签

        :return: The labels of this PutMergeRequestParamsDto.
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this PutMergeRequestParamsDto.

        标签

        :param labels: The labels of this PutMergeRequestParamsDto.
        :type labels: object
        """
        self._labels = labels

    @property
    def force_remove_source_branch(self):
        r"""Gets the force_remove_source_branch of this PutMergeRequestParamsDto.

        合入后删除源分支

        :return: The force_remove_source_branch of this PutMergeRequestParamsDto.
        :rtype: bool
        """
        return self._force_remove_source_branch

    @force_remove_source_branch.setter
    def force_remove_source_branch(self, force_remove_source_branch):
        r"""Sets the force_remove_source_branch of this PutMergeRequestParamsDto.

        合入后删除源分支

        :param force_remove_source_branch: The force_remove_source_branch of this PutMergeRequestParamsDto.
        :type force_remove_source_branch: bool
        """
        self._force_remove_source_branch = force_remove_source_branch

    @property
    def squash(self):
        r"""Gets the squash of this PutMergeRequestParamsDto.

        squash合入

        :return: The squash of this PutMergeRequestParamsDto.
        :rtype: bool
        """
        return self._squash

    @squash.setter
    def squash(self, squash):
        r"""Sets the squash of this PutMergeRequestParamsDto.

        squash合入

        :param squash: The squash of this PutMergeRequestParamsDto.
        :type squash: bool
        """
        self._squash = squash

    @property
    def squash_commit_message(self):
        r"""Gets the squash_commit_message of this PutMergeRequestParamsDto.

        squash提交信息

        :return: The squash_commit_message of this PutMergeRequestParamsDto.
        :rtype: str
        """
        return self._squash_commit_message

    @squash_commit_message.setter
    def squash_commit_message(self, squash_commit_message):
        r"""Sets the squash_commit_message of this PutMergeRequestParamsDto.

        squash提交信息

        :param squash_commit_message: The squash_commit_message of this PutMergeRequestParamsDto.
        :type squash_commit_message: str
        """
        self._squash_commit_message = squash_commit_message

    @property
    def work_item_ids(self):
        r"""Gets the work_item_ids of this PutMergeRequestParamsDto.

        e2e单号

        :return: The work_item_ids of this PutMergeRequestParamsDto.
        :rtype: list[str]
        """
        return self._work_item_ids

    @work_item_ids.setter
    def work_item_ids(self, work_item_ids):
        r"""Sets the work_item_ids of this PutMergeRequestParamsDto.

        e2e单号

        :param work_item_ids: The work_item_ids of this PutMergeRequestParamsDto.
        :type work_item_ids: list[str]
        """
        self._work_item_ids = work_item_ids

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
        if not isinstance(other, PutMergeRequestParamsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
