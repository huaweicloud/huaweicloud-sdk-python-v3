# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionBrief:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_id': 'str',
        'created_at': 'str',
        'status': 'str',
        'running_steps': 'list[str]',
        'current_steps': 'list[str]',
        'duration': 'int'
    }

    attribute_map = {
        'execution_id': 'execution_id',
        'created_at': 'created_at',
        'status': 'status',
        'running_steps': 'running_steps',
        'current_steps': 'current_steps',
        'duration': 'duration'
    }

    def __init__(self, execution_id=None, created_at=None, status=None, running_steps=None, current_steps=None, duration=None):
        r"""ExecutionBrief

        The model defined in huaweicloud sdk

        :param execution_id: 工作流执行ID。
        :type execution_id: str
        :param created_at: 工作流执行的创建时间。
        :type created_at: str
        :param status: 工作流状态。
        :type status: str
        :param running_steps: 运行的节点。
        :type running_steps: list[str]
        :param current_steps: 当前节点。
        :type current_steps: list[str]
        :param duration: 运行时长。
        :type duration: int
        """
        
        

        self._execution_id = None
        self._created_at = None
        self._status = None
        self._running_steps = None
        self._current_steps = None
        self._duration = None
        self.discriminator = None

        if execution_id is not None:
            self.execution_id = execution_id
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status
        if running_steps is not None:
            self.running_steps = running_steps
        if current_steps is not None:
            self.current_steps = current_steps
        if duration is not None:
            self.duration = duration

    @property
    def execution_id(self):
        r"""Gets the execution_id of this ExecutionBrief.

        工作流执行ID。

        :return: The execution_id of this ExecutionBrief.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this ExecutionBrief.

        工作流执行ID。

        :param execution_id: The execution_id of this ExecutionBrief.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def created_at(self):
        r"""Gets the created_at of this ExecutionBrief.

        工作流执行的创建时间。

        :return: The created_at of this ExecutionBrief.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ExecutionBrief.

        工作流执行的创建时间。

        :param created_at: The created_at of this ExecutionBrief.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def status(self):
        r"""Gets the status of this ExecutionBrief.

        工作流状态。

        :return: The status of this ExecutionBrief.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExecutionBrief.

        工作流状态。

        :param status: The status of this ExecutionBrief.
        :type status: str
        """
        self._status = status

    @property
    def running_steps(self):
        r"""Gets the running_steps of this ExecutionBrief.

        运行的节点。

        :return: The running_steps of this ExecutionBrief.
        :rtype: list[str]
        """
        return self._running_steps

    @running_steps.setter
    def running_steps(self, running_steps):
        r"""Sets the running_steps of this ExecutionBrief.

        运行的节点。

        :param running_steps: The running_steps of this ExecutionBrief.
        :type running_steps: list[str]
        """
        self._running_steps = running_steps

    @property
    def current_steps(self):
        r"""Gets the current_steps of this ExecutionBrief.

        当前节点。

        :return: The current_steps of this ExecutionBrief.
        :rtype: list[str]
        """
        return self._current_steps

    @current_steps.setter
    def current_steps(self, current_steps):
        r"""Sets the current_steps of this ExecutionBrief.

        当前节点。

        :param current_steps: The current_steps of this ExecutionBrief.
        :type current_steps: list[str]
        """
        self._current_steps = current_steps

    @property
    def duration(self):
        r"""Gets the duration of this ExecutionBrief.

        运行时长。

        :return: The duration of this ExecutionBrief.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ExecutionBrief.

        运行时长。

        :param duration: The duration of this ExecutionBrief.
        :type duration: int
        """
        self._duration = duration

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExecutionBrief):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
