# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskListVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[TaskVo]',
        'running_count': 'int'
    }

    attribute_map = {
        'tasks': 'tasks',
        'running_count': 'running_count'
    }

    def __init__(self, tasks=None, running_count=None):
        """TaskListVo

        The model defined in huaweicloud sdk

        :param tasks: 测试任务集合
        :type tasks: list[:class:`huaweicloudsdkcloudtest.v1.TaskVo`]
        :param running_count: 正在执行任务数
        :type running_count: int
        """
        
        

        self._tasks = None
        self._running_count = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if running_count is not None:
            self.running_count = running_count

    @property
    def tasks(self):
        """Gets the tasks of this TaskListVo.

        测试任务集合

        :return: The tasks of this TaskListVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TaskVo`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this TaskListVo.

        测试任务集合

        :param tasks: The tasks of this TaskListVo.
        :type tasks: list[:class:`huaweicloudsdkcloudtest.v1.TaskVo`]
        """
        self._tasks = tasks

    @property
    def running_count(self):
        """Gets the running_count of this TaskListVo.

        正在执行任务数

        :return: The running_count of this TaskListVo.
        :rtype: int
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        """Sets the running_count of this TaskListVo.

        正在执行任务数

        :param running_count: The running_count of this TaskListVo.
        :type running_count: int
        """
        self._running_count = running_count

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
        if not isinstance(other, TaskListVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
