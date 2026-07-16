# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskStatuses:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task': 'str',
        'exit_code': 'int',
        'message': 'str'
    }

    attribute_map = {
        'task': 'task',
        'exit_code': 'exit_code',
        'message': 'message'
    }

    def __init__(self, task=None, exit_code=None, message=None):
        r"""TaskStatuses

        The model defined in huaweicloud sdk

        :param task: 训练作业子任务名称。
        :type task: str
        :param exit_code: 训练作业子任务退出码。
        :type exit_code: int
        :param message: 训练作业子任务错误消息。
        :type message: str
        """
        
        

        self._task = None
        self._exit_code = None
        self._message = None
        self.discriminator = None

        if task is not None:
            self.task = task
        if exit_code is not None:
            self.exit_code = exit_code
        if message is not None:
            self.message = message

    @property
    def task(self):
        r"""Gets the task of this TaskStatuses.

        训练作业子任务名称。

        :return: The task of this TaskStatuses.
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        r"""Sets the task of this TaskStatuses.

        训练作业子任务名称。

        :param task: The task of this TaskStatuses.
        :type task: str
        """
        self._task = task

    @property
    def exit_code(self):
        r"""Gets the exit_code of this TaskStatuses.

        训练作业子任务退出码。

        :return: The exit_code of this TaskStatuses.
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        r"""Sets the exit_code of this TaskStatuses.

        训练作业子任务退出码。

        :param exit_code: The exit_code of this TaskStatuses.
        :type exit_code: int
        """
        self._exit_code = exit_code

    @property
    def message(self):
        r"""Gets the message of this TaskStatuses.

        训练作业子任务错误消息。

        :return: The message of this TaskStatuses.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this TaskStatuses.

        训练作业子任务错误消息。

        :param message: The message of this TaskStatuses.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, TaskStatuses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
