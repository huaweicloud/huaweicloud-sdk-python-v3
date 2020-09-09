# coding: utf-8

import pprint
import re

import six





class ListSinkTasksRespTasks:


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
        'task_name': 'str',
        'destination_type': 'str',
        'create_time': 'str',
        'status': 'str',
        'topics': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'destination_type': 'destination_type',
        'create_time': 'create_time',
        'status': 'status',
        'topics': 'topics'
    }

    def __init__(self, task_id=None, task_name=None, destination_type=None, create_time=None, status=None, topics=None):
        """ListSinkTasksRespTasks - a model defined in huaweicloud sdk"""
        
        

        self._task_id = None
        self._task_name = None
        self._destination_type = None
        self._create_time = None
        self._status = None
        self._topics = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if destination_type is not None:
            self.destination_type = destination_type
        if create_time is not None:
            self.create_time = create_time
        if status is not None:
            self.status = status
        if topics is not None:
            self.topics = topics

    @property
    def task_id(self):
        """Gets the task_id of this ListSinkTasksRespTasks.

        任务ID。

        :return: The task_id of this ListSinkTasksRespTasks.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListSinkTasksRespTasks.

        任务ID。

        :param task_id: The task_id of this ListSinkTasksRespTasks.
        :type: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this ListSinkTasksRespTasks.

        转储任务名称。

        :return: The task_name of this ListSinkTasksRespTasks.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ListSinkTasksRespTasks.

        转储任务名称。

        :param task_name: The task_name of this ListSinkTasksRespTasks.
        :type: str
        """
        self._task_name = task_name

    @property
    def destination_type(self):
        """Gets the destination_type of this ListSinkTasksRespTasks.

        转储任务类型。

        :return: The destination_type of this ListSinkTasksRespTasks.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this ListSinkTasksRespTasks.

        转储任务类型。

        :param destination_type: The destination_type of this ListSinkTasksRespTasks.
        :type: str
        """
        self._destination_type = destination_type

    @property
    def create_time(self):
        """Gets the create_time of this ListSinkTasksRespTasks.

        转储任务创建时间戳。

        :return: The create_time of this ListSinkTasksRespTasks.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListSinkTasksRespTasks.

        转储任务创建时间戳。

        :param create_time: The create_time of this ListSinkTasksRespTasks.
        :type: str
        """
        self._create_time = create_time

    @property
    def status(self):
        """Gets the status of this ListSinkTasksRespTasks.

        转储任务状态。

        :return: The status of this ListSinkTasksRespTasks.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListSinkTasksRespTasks.

        转储任务状态。

        :param status: The status of this ListSinkTasksRespTasks.
        :type: str
        """
        self._status = status

    @property
    def topics(self):
        """Gets the topics of this ListSinkTasksRespTasks.

        返回任务转存的topics列表或者正则表达式。

        :return: The topics of this ListSinkTasksRespTasks.
        :rtype: str
        """
        return self._topics

    @topics.setter
    def topics(self, topics):
        """Sets the topics of this ListSinkTasksRespTasks.

        返回任务转存的topics列表或者正则表达式。

        :param topics: The topics of this ListSinkTasksRespTasks.
        :type: str
        """
        self._topics = topics

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSinkTasksRespTasks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
