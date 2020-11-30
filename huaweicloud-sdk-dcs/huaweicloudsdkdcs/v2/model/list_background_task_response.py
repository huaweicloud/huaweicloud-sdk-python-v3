# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListBackgroundTaskResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_count': 'str',
        'tasks': 'list[SingleBackgroundTask]'
    }

    attribute_map = {
        'task_count': 'task_count',
        'tasks': 'tasks'
    }

    def __init__(self, task_count=None, tasks=None):
        """ListBackgroundTaskResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._task_count = None
        self._tasks = None
        self.discriminator = None

        if task_count is not None:
            self.task_count = task_count
        if tasks is not None:
            self.tasks = tasks

    @property
    def task_count(self):
        """Gets the task_count of this ListBackgroundTaskResponse.

        任务个数

        :return: The task_count of this ListBackgroundTaskResponse.
        :rtype: str
        """
        return self._task_count

    @task_count.setter
    def task_count(self, task_count):
        """Sets the task_count of this ListBackgroundTaskResponse.

        任务个数

        :param task_count: The task_count of this ListBackgroundTaskResponse.
        :type: str
        """
        self._task_count = task_count

    @property
    def tasks(self):
        """Gets the tasks of this ListBackgroundTaskResponse.

        任务详情数组

        :return: The tasks of this ListBackgroundTaskResponse.
        :rtype: list[SingleBackgroundTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ListBackgroundTaskResponse.

        任务详情数组

        :param tasks: The tasks of this ListBackgroundTaskResponse.
        :type: list[SingleBackgroundTask]
        """
        self._tasks = tasks

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
        if not isinstance(other, ListBackgroundTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
