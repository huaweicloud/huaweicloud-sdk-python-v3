# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncConfigV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'parent_task_id': 'str',
        'git_source_branch': 'str',
        'git_target_branch': 'str',
        'merge_id': 'str',
        'event_type': 'str',
        'action': 'str',
        'title': 'str'
    }

    attribute_map = {
        'parent_task_id': 'parent_task_id',
        'git_source_branch': 'git_source_branch',
        'git_target_branch': 'git_target_branch',
        'merge_id': 'merge_id',
        'event_type': 'event_type',
        'action': 'action',
        'title': 'title'
    }

    def __init__(self, parent_task_id=None, git_source_branch=None, git_target_branch=None, merge_id=None, event_type=None, action=None, title=None):
        """IncConfigV2

        The model defined in huaweicloud sdk

        :param parent_task_id: 需要关联的父任务ID，流水线创建或MR创建任务需要该参数
        :type parent_task_id: str
        :param git_source_branch: 增量检查代码源分支
        :type git_source_branch: str
        :param git_target_branch: 增量检查代码目标分支
        :type git_target_branch: str
        :param merge_id: MR唯一标示ID
        :type merge_id: str
        :param event_type: webhook触发事件类型,merge_request/push_request
        :type event_type: str
        :param action: webhook事件状态，open/close/update
        :type action: str
        :param title: MR标题
        :type title: str
        """
        
        

        self._parent_task_id = None
        self._git_source_branch = None
        self._git_target_branch = None
        self._merge_id = None
        self._event_type = None
        self._action = None
        self._title = None
        self.discriminator = None

        if parent_task_id is not None:
            self.parent_task_id = parent_task_id
        if git_source_branch is not None:
            self.git_source_branch = git_source_branch
        if git_target_branch is not None:
            self.git_target_branch = git_target_branch
        if merge_id is not None:
            self.merge_id = merge_id
        if event_type is not None:
            self.event_type = event_type
        if action is not None:
            self.action = action
        if title is not None:
            self.title = title

    @property
    def parent_task_id(self):
        """Gets the parent_task_id of this IncConfigV2.

        需要关联的父任务ID，流水线创建或MR创建任务需要该参数

        :return: The parent_task_id of this IncConfigV2.
        :rtype: str
        """
        return self._parent_task_id

    @parent_task_id.setter
    def parent_task_id(self, parent_task_id):
        """Sets the parent_task_id of this IncConfigV2.

        需要关联的父任务ID，流水线创建或MR创建任务需要该参数

        :param parent_task_id: The parent_task_id of this IncConfigV2.
        :type parent_task_id: str
        """
        self._parent_task_id = parent_task_id

    @property
    def git_source_branch(self):
        """Gets the git_source_branch of this IncConfigV2.

        增量检查代码源分支

        :return: The git_source_branch of this IncConfigV2.
        :rtype: str
        """
        return self._git_source_branch

    @git_source_branch.setter
    def git_source_branch(self, git_source_branch):
        """Sets the git_source_branch of this IncConfigV2.

        增量检查代码源分支

        :param git_source_branch: The git_source_branch of this IncConfigV2.
        :type git_source_branch: str
        """
        self._git_source_branch = git_source_branch

    @property
    def git_target_branch(self):
        """Gets the git_target_branch of this IncConfigV2.

        增量检查代码目标分支

        :return: The git_target_branch of this IncConfigV2.
        :rtype: str
        """
        return self._git_target_branch

    @git_target_branch.setter
    def git_target_branch(self, git_target_branch):
        """Sets the git_target_branch of this IncConfigV2.

        增量检查代码目标分支

        :param git_target_branch: The git_target_branch of this IncConfigV2.
        :type git_target_branch: str
        """
        self._git_target_branch = git_target_branch

    @property
    def merge_id(self):
        """Gets the merge_id of this IncConfigV2.

        MR唯一标示ID

        :return: The merge_id of this IncConfigV2.
        :rtype: str
        """
        return self._merge_id

    @merge_id.setter
    def merge_id(self, merge_id):
        """Sets the merge_id of this IncConfigV2.

        MR唯一标示ID

        :param merge_id: The merge_id of this IncConfigV2.
        :type merge_id: str
        """
        self._merge_id = merge_id

    @property
    def event_type(self):
        """Gets the event_type of this IncConfigV2.

        webhook触发事件类型,merge_request/push_request

        :return: The event_type of this IncConfigV2.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this IncConfigV2.

        webhook触发事件类型,merge_request/push_request

        :param event_type: The event_type of this IncConfigV2.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def action(self):
        """Gets the action of this IncConfigV2.

        webhook事件状态，open/close/update

        :return: The action of this IncConfigV2.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this IncConfigV2.

        webhook事件状态，open/close/update

        :param action: The action of this IncConfigV2.
        :type action: str
        """
        self._action = action

    @property
    def title(self):
        """Gets the title of this IncConfigV2.

        MR标题

        :return: The title of this IncConfigV2.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this IncConfigV2.

        MR标题

        :param title: The title of this IncConfigV2.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, IncConfigV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
