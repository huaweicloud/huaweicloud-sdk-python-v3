# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCenterTaskResponse(SdkResponse):

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
        'tasks': 'list[ListCenterTasksResp]'
    }

    attribute_map = {
        'task_count': 'task_count',
        'tasks': 'tasks'
    }

    def __init__(self, task_count=None, tasks=None):
        r"""ListCenterTaskResponse

        The model defined in huaweicloud sdk

        :param task_count: 任务个数
        :type task_count: str
        :param tasks: 中心任务详情数组
        :type tasks: list[:class:`huaweicloudsdkdcs.v2.ListCenterTasksResp`]
        """
        
        super(ListCenterTaskResponse, self).__init__()

        self._task_count = None
        self._tasks = None
        self.discriminator = None

        if task_count is not None:
            self.task_count = task_count
        if tasks is not None:
            self.tasks = tasks

    @property
    def task_count(self):
        r"""Gets the task_count of this ListCenterTaskResponse.

        任务个数

        :return: The task_count of this ListCenterTaskResponse.
        :rtype: str
        """
        return self._task_count

    @task_count.setter
    def task_count(self, task_count):
        r"""Sets the task_count of this ListCenterTaskResponse.

        任务个数

        :param task_count: The task_count of this ListCenterTaskResponse.
        :type task_count: str
        """
        self._task_count = task_count

    @property
    def tasks(self):
        r"""Gets the tasks of this ListCenterTaskResponse.

        中心任务详情数组

        :return: The tasks of this ListCenterTaskResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ListCenterTasksResp`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListCenterTaskResponse.

        中心任务详情数组

        :param tasks: The tasks of this ListCenterTaskResponse.
        :type tasks: list[:class:`huaweicloudsdkdcs.v2.ListCenterTasksResp`]
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
        if not isinstance(other, ListCenterTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
