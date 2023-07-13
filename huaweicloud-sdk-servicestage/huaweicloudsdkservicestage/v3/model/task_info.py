# coding: utf-8

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
        'update_at': 'str',
        'messages': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'task_status': 'str',
        'task_type': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'update_at': 'update_at',
        'messages': 'messages',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_status': 'task_status',
        'task_type': 'task_type'
    }

    def __init__(self, created_at=None, update_at=None, messages=None, task_id=None, task_name=None, task_status=None, task_type=None):
        """TaskInfo

        The model defined in huaweicloud sdk

        :param created_at: 
        :type created_at: str
        :param update_at: 
        :type update_at: str
        :param messages: 
        :type messages: str
        :param task_id: 
        :type task_id: str
        :param task_name: 
        :type task_name: str
        :param task_status: 
        :type task_status: str
        :param task_type: 
        :type task_type: str
        """
        
        

        self._created_at = None
        self._update_at = None
        self._messages = None
        self._task_id = None
        self._task_name = None
        self._task_status = None
        self._task_type = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if update_at is not None:
            self.update_at = update_at
        if messages is not None:
            self.messages = messages
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_status is not None:
            self.task_status = task_status
        if task_type is not None:
            self.task_type = task_type

    @property
    def created_at(self):
        """Gets the created_at of this TaskInfo.

        :return: The created_at of this TaskInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaskInfo.

        :param created_at: The created_at of this TaskInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def update_at(self):
        """Gets the update_at of this TaskInfo.

        :return: The update_at of this TaskInfo.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this TaskInfo.

        :param update_at: The update_at of this TaskInfo.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def messages(self):
        """Gets the messages of this TaskInfo.

        :return: The messages of this TaskInfo.
        :rtype: str
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this TaskInfo.

        :param messages: The messages of this TaskInfo.
        :type messages: str
        """
        self._messages = messages

    @property
    def task_id(self):
        """Gets the task_id of this TaskInfo.

        :return: The task_id of this TaskInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this TaskInfo.

        :param task_id: The task_id of this TaskInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this TaskInfo.

        :return: The task_name of this TaskInfo.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskInfo.

        :param task_name: The task_name of this TaskInfo.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_status(self):
        """Gets the task_status of this TaskInfo.

        :return: The task_status of this TaskInfo.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this TaskInfo.

        :param task_status: The task_status of this TaskInfo.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def task_type(self):
        """Gets the task_type of this TaskInfo.

        :return: The task_type of this TaskInfo.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TaskInfo.

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
