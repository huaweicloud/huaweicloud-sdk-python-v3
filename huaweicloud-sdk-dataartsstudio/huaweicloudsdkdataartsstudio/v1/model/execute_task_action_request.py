# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteTaskActionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'task_id': 'str',
        'action': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'task_id': 'task_id',
        'action': 'action'
    }

    def __init__(self, workspace=None, task_id=None, action=None):
        """ExecuteTaskActionRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param task_id: 任务id
        :type task_id: str
        :param action: 启动、调度、停止操作标识
        :type action: str
        """
        
        

        self._workspace = None
        self._task_id = None
        self._action = None
        self.discriminator = None

        self.workspace = workspace
        self.task_id = task_id
        self.action = action

    @property
    def workspace(self):
        """Gets the workspace of this ExecuteTaskActionRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ExecuteTaskActionRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ExecuteTaskActionRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ExecuteTaskActionRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def task_id(self):
        """Gets the task_id of this ExecuteTaskActionRequest.

        任务id

        :return: The task_id of this ExecuteTaskActionRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ExecuteTaskActionRequest.

        任务id

        :param task_id: The task_id of this ExecuteTaskActionRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def action(self):
        """Gets the action of this ExecuteTaskActionRequest.

        启动、调度、停止操作标识

        :return: The action of this ExecuteTaskActionRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ExecuteTaskActionRequest.

        启动、调度、停止操作标识

        :param action: The action of this ExecuteTaskActionRequest.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, ExecuteTaskActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
