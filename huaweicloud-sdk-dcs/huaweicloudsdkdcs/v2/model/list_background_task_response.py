# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'tasks': 'list[SingleBackgroundTask]',
        'updated_at': 'str',
        'created_at': 'str',
        'status': 'str'
    }

    attribute_map = {
        'task_count': 'task_count',
        'tasks': 'tasks',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'status': 'status'
    }

    def __init__(self, task_count=None, tasks=None, updated_at=None, created_at=None, status=None):
        """ListBackgroundTaskResponse

        The model defined in huaweicloud sdk

        :param task_count: 任务个数
        :type task_count: str
        :param tasks: 任务详情数组
        :type tasks: list[:class:`huaweicloudsdkdcs.v2.SingleBackgroundTask`]
        :param updated_at: 任务结束时间，格式为2020-06-17T07:38:42.503Z
        :type updated_at: str
        :param created_at: 任务启动时间，格式为2020-06-17T07:38:42.503Z
        :type created_at: str
        :param status: 任务状态
        :type status: str
        """
        
        super(ListBackgroundTaskResponse, self).__init__()

        self._task_count = None
        self._tasks = None
        self._updated_at = None
        self._created_at = None
        self._status = None
        self.discriminator = None

        if task_count is not None:
            self.task_count = task_count
        if tasks is not None:
            self.tasks = tasks
        if updated_at is not None:
            self.updated_at = updated_at
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status

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
        :type task_count: str
        """
        self._task_count = task_count

    @property
    def tasks(self):
        """Gets the tasks of this ListBackgroundTaskResponse.

        任务详情数组

        :return: The tasks of this ListBackgroundTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.SingleBackgroundTask`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ListBackgroundTaskResponse.

        任务详情数组

        :param tasks: The tasks of this ListBackgroundTaskResponse.
        :type tasks: list[:class:`huaweicloudsdkdcs.v2.SingleBackgroundTask`]
        """
        self._tasks = tasks

    @property
    def updated_at(self):
        """Gets the updated_at of this ListBackgroundTaskResponse.

        任务结束时间，格式为2020-06-17T07:38:42.503Z

        :return: The updated_at of this ListBackgroundTaskResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ListBackgroundTaskResponse.

        任务结束时间，格式为2020-06-17T07:38:42.503Z

        :param updated_at: The updated_at of this ListBackgroundTaskResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this ListBackgroundTaskResponse.

        任务启动时间，格式为2020-06-17T07:38:42.503Z

        :return: The created_at of this ListBackgroundTaskResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ListBackgroundTaskResponse.

        任务启动时间，格式为2020-06-17T07:38:42.503Z

        :param created_at: The created_at of this ListBackgroundTaskResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def status(self):
        """Gets the status of this ListBackgroundTaskResponse.

        任务状态

        :return: The status of this ListBackgroundTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListBackgroundTaskResponse.

        任务状态

        :param status: The status of this ListBackgroundTaskResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListBackgroundTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
