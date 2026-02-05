# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskLogsVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'ddm_instance_id': 'str',
        'level': 'str',
        'created_time': 'float',
        'message': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'ddm_instance_id': 'ddm_instance_id',
        'level': 'level',
        'created_time': 'created_time',
        'message': 'message'
    }

    def __init__(self, task_id=None, ddm_instance_id=None, level=None, created_time=None, message=None):
        r"""TaskLogsVO

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**：  分片变更任务ID。  **参数范围**：  不涉及。
        :type task_id: str
        :param ddm_instance_id: **参数解释**：  DDM实例ID。  **参数范围**：  不涉及。
        :type ddm_instance_id: str
        :param level: **参数解释**：  等级。  **参数范围**：  不涉及。
        :type level: str
        :param created_time: **参数解释**：  创建时间。  **参数范围**：  不涉及。
        :type created_time: float
        :param message: **参数解释**：  消息。  **参数范围**：  不涉及。
        :type message: str
        """
        
        

        self._task_id = None
        self._ddm_instance_id = None
        self._level = None
        self._created_time = None
        self._message = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if ddm_instance_id is not None:
            self.ddm_instance_id = ddm_instance_id
        if level is not None:
            self.level = level
        if created_time is not None:
            self.created_time = created_time
        if message is not None:
            self.message = message

    @property
    def task_id(self):
        r"""Gets the task_id of this TaskLogsVO.

        **参数解释**：  分片变更任务ID。  **参数范围**：  不涉及。

        :return: The task_id of this TaskLogsVO.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this TaskLogsVO.

        **参数解释**：  分片变更任务ID。  **参数范围**：  不涉及。

        :param task_id: The task_id of this TaskLogsVO.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def ddm_instance_id(self):
        r"""Gets the ddm_instance_id of this TaskLogsVO.

        **参数解释**：  DDM实例ID。  **参数范围**：  不涉及。

        :return: The ddm_instance_id of this TaskLogsVO.
        :rtype: str
        """
        return self._ddm_instance_id

    @ddm_instance_id.setter
    def ddm_instance_id(self, ddm_instance_id):
        r"""Sets the ddm_instance_id of this TaskLogsVO.

        **参数解释**：  DDM实例ID。  **参数范围**：  不涉及。

        :param ddm_instance_id: The ddm_instance_id of this TaskLogsVO.
        :type ddm_instance_id: str
        """
        self._ddm_instance_id = ddm_instance_id

    @property
    def level(self):
        r"""Gets the level of this TaskLogsVO.

        **参数解释**：  等级。  **参数范围**：  不涉及。

        :return: The level of this TaskLogsVO.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this TaskLogsVO.

        **参数解释**：  等级。  **参数范围**：  不涉及。

        :param level: The level of this TaskLogsVO.
        :type level: str
        """
        self._level = level

    @property
    def created_time(self):
        r"""Gets the created_time of this TaskLogsVO.

        **参数解释**：  创建时间。  **参数范围**：  不涉及。

        :return: The created_time of this TaskLogsVO.
        :rtype: float
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this TaskLogsVO.

        **参数解释**：  创建时间。  **参数范围**：  不涉及。

        :param created_time: The created_time of this TaskLogsVO.
        :type created_time: float
        """
        self._created_time = created_time

    @property
    def message(self):
        r"""Gets the message of this TaskLogsVO.

        **参数解释**：  消息。  **参数范围**：  不涉及。

        :return: The message of this TaskLogsVO.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this TaskLogsVO.

        **参数解释**：  消息。  **参数范围**：  不涉及。

        :param message: The message of this TaskLogsVO.
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
        if not isinstance(other, TaskLogsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
