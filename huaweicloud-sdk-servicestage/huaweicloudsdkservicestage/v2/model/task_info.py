# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'last_health_check': 'str',
        'messages': 'str',
        'owner_id': 'str',
        'task_id': 'str',
        'task_index': 'int',
        'task_name': 'str',
        'task_status': 'str',
        'task_type': 'str'
    }

    attribute_map = {
        'created_at': 'CREATED_AT',
        'last_health_check': 'LAST_HEALTH_CHECK',
        'messages': 'MESSAGES',
        'owner_id': 'OWNER_ID',
        'task_id': 'TASK_ID',
        'task_index': 'TASK_INDEX',
        'task_name': 'TASK_NAME',
        'task_status': 'TASK_STATUS',
        'task_type': 'TASK_TYPE'
    }

    def __init__(self, created_at=None, last_health_check=None, messages=None, owner_id=None, task_id=None, task_index=None, task_name=None, task_status=None, task_type=None):
        """TaskInfo

        The model defined in huaweicloud sdk

        :param created_at: 创建时间。
        :type created_at: str
        :param last_health_check: 健康检查时间。
        :type last_health_check: str
        :param messages: 消息。
        :type messages: str
        :param owner_id: 创建用户ID。
        :type owner_id: str
        :param task_id: 任务ID。
        :type task_id: str
        :param task_index: 任务序号。
        :type task_index: int
        :param task_name: 任务名称。
        :type task_name: str
        :param task_status: 任务状态。
        :type task_status: str
        :param task_type: 任务类型。
        :type task_type: str
        """
        
        

        self._created_at = None
        self._last_health_check = None
        self._messages = None
        self._owner_id = None
        self._task_id = None
        self._task_index = None
        self._task_name = None
        self._task_status = None
        self._task_type = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if last_health_check is not None:
            self.last_health_check = last_health_check
        if messages is not None:
            self.messages = messages
        if owner_id is not None:
            self.owner_id = owner_id
        if task_id is not None:
            self.task_id = task_id
        if task_index is not None:
            self.task_index = task_index
        if task_name is not None:
            self.task_name = task_name
        if task_status is not None:
            self.task_status = task_status
        if task_type is not None:
            self.task_type = task_type

    @property
    def created_at(self):
        """Gets the created_at of this TaskInfo.

        创建时间。

        :return: The created_at of this TaskInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaskInfo.

        创建时间。

        :param created_at: The created_at of this TaskInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def last_health_check(self):
        """Gets the last_health_check of this TaskInfo.

        健康检查时间。

        :return: The last_health_check of this TaskInfo.
        :rtype: str
        """
        return self._last_health_check

    @last_health_check.setter
    def last_health_check(self, last_health_check):
        """Sets the last_health_check of this TaskInfo.

        健康检查时间。

        :param last_health_check: The last_health_check of this TaskInfo.
        :type last_health_check: str
        """
        self._last_health_check = last_health_check

    @property
    def messages(self):
        """Gets the messages of this TaskInfo.

        消息。

        :return: The messages of this TaskInfo.
        :rtype: str
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this TaskInfo.

        消息。

        :param messages: The messages of this TaskInfo.
        :type messages: str
        """
        self._messages = messages

    @property
    def owner_id(self):
        """Gets the owner_id of this TaskInfo.

        创建用户ID。

        :return: The owner_id of this TaskInfo.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this TaskInfo.

        创建用户ID。

        :param owner_id: The owner_id of this TaskInfo.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def task_id(self):
        """Gets the task_id of this TaskInfo.

        任务ID。

        :return: The task_id of this TaskInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskInfo.

        任务ID。

        :param task_id: The task_id of this TaskInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_index(self):
        """Gets the task_index of this TaskInfo.

        任务序号。

        :return: The task_index of this TaskInfo.
        :rtype: int
        """
        return self._task_index

    @task_index.setter
    def task_index(self, task_index):
        """Sets the task_index of this TaskInfo.

        任务序号。

        :param task_index: The task_index of this TaskInfo.
        :type task_index: int
        """
        self._task_index = task_index

    @property
    def task_name(self):
        """Gets the task_name of this TaskInfo.

        任务名称。

        :return: The task_name of this TaskInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskInfo.

        任务名称。

        :param task_name: The task_name of this TaskInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_status(self):
        """Gets the task_status of this TaskInfo.

        任务状态。

        :return: The task_status of this TaskInfo.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this TaskInfo.

        任务状态。

        :param task_status: The task_status of this TaskInfo.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def task_type(self):
        """Gets the task_type of this TaskInfo.

        任务类型。

        :return: The task_type of this TaskInfo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TaskInfo.

        任务类型。

        :param task_type: The task_type of this TaskInfo.
        :type task_type: str
        """
        self._task_type = task_type

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
        if not isinstance(other, TaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
