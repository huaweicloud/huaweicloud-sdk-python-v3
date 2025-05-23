# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduleTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'task_name': 'str',
        'task_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'task_name': 'task_name',
        'task_type': 'task_type'
    }

    def __init__(self, offset=None, limit=None, task_name=None, task_type=None):
        r"""ListScheduleTasksRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量。
        :type offset: int
        :param limit: 查询的数量，值区间[1-100]。
        :type limit: int
        :param task_name: 定时任务名称
        :type task_name: str
        :param task_type: 任务类型： * &#x60;RESTART_SERVER&#x60; - 定时重启服务器 * &#x60;START_SERVER&#x60; - 定时开机 * &#x60;STOP_SERVER&#x60; - 定时关机 * &#x60;REINSTALL_OS&#x60; - 定时重装操作系统
        :type task_type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._task_name = None
        self._task_type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type

    @property
    def offset(self):
        r"""Gets the offset of this ListScheduleTasksRequest.

        查询的偏移量。

        :return: The offset of this ListScheduleTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScheduleTasksRequest.

        查询的偏移量。

        :param offset: The offset of this ListScheduleTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduleTasksRequest.

        查询的数量，值区间[1-100]。

        :return: The limit of this ListScheduleTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduleTasksRequest.

        查询的数量，值区间[1-100]。

        :param limit: The limit of this ListScheduleTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def task_name(self):
        r"""Gets the task_name of this ListScheduleTasksRequest.

        定时任务名称

        :return: The task_name of this ListScheduleTasksRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListScheduleTasksRequest.

        定时任务名称

        :param task_name: The task_name of this ListScheduleTasksRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        r"""Gets the task_type of this ListScheduleTasksRequest.

        任务类型： * `RESTART_SERVER` - 定时重启服务器 * `START_SERVER` - 定时开机 * `STOP_SERVER` - 定时关机 * `REINSTALL_OS` - 定时重装操作系统

        :return: The task_type of this ListScheduleTasksRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListScheduleTasksRequest.

        任务类型： * `RESTART_SERVER` - 定时重启服务器 * `START_SERVER` - 定时开机 * `STOP_SERVER` - 定时关机 * `REINSTALL_OS` - 定时重装操作系统

        :param task_type: The task_type of this ListScheduleTasksRequest.
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
        if not isinstance(other, ListScheduleTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
