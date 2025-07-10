# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteActionParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_id': 'str',
        'task_id': 'str',
        'action': 'str',
        'params': 'object'
    }

    attribute_map = {
        'ticket_id': 'ticket_id',
        'task_id': 'task_id',
        'action': 'action',
        'params': 'params'
    }

    def __init__(self, ticket_id=None, task_id=None, action=None, params=None):
        r"""ExecuteActionParams

        The model defined in huaweicloud sdk

        :param ticket_id: 执行当前操作的工单单号。
        :type ticket_id: str
        :param task_id: 任务ID
        :type task_id: str
        :param action: 动作名称
        :type action: str
        :param params: 当前执行的动作信息
        :type params: object
        """
        
        

        self._ticket_id = None
        self._task_id = None
        self._action = None
        self._params = None
        self.discriminator = None

        if ticket_id is not None:
            self.ticket_id = ticket_id
        if task_id is not None:
            self.task_id = task_id
        if action is not None:
            self.action = action
        if params is not None:
            self.params = params

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this ExecuteActionParams.

        执行当前操作的工单单号。

        :return: The ticket_id of this ExecuteActionParams.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this ExecuteActionParams.

        执行当前操作的工单单号。

        :param ticket_id: The ticket_id of this ExecuteActionParams.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ExecuteActionParams.

        任务ID

        :return: The task_id of this ExecuteActionParams.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ExecuteActionParams.

        任务ID

        :param task_id: The task_id of this ExecuteActionParams.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def action(self):
        r"""Gets the action of this ExecuteActionParams.

        动作名称

        :return: The action of this ExecuteActionParams.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExecuteActionParams.

        动作名称

        :param action: The action of this ExecuteActionParams.
        :type action: str
        """
        self._action = action

    @property
    def params(self):
        r"""Gets the params of this ExecuteActionParams.

        当前执行的动作信息

        :return: The params of this ExecuteActionParams.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this ExecuteActionParams.

        当前执行的动作信息

        :param params: The params of this ExecuteActionParams.
        :type params: object
        """
        self._params = params

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
        if not isinstance(other, ExecuteActionParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
