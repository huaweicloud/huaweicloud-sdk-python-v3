# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduleTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schedule_tasks': 'list[ScheduleTaskInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'schedule_tasks': 'schedule_tasks',
        'total_count': 'total_count'
    }

    def __init__(self, schedule_tasks=None, total_count=None):
        r"""ListScheduleTasksResponse

        The model defined in huaweicloud sdk

        :param schedule_tasks: 定时任务列表。
        :type schedule_tasks: list[:class:`huaweicloudsdkrds.v3.ScheduleTaskInfo`]
        :param total_count: 总任务数量。
        :type total_count: int
        """
        
        super(ListScheduleTasksResponse, self).__init__()

        self._schedule_tasks = None
        self._total_count = None
        self.discriminator = None

        if schedule_tasks is not None:
            self.schedule_tasks = schedule_tasks
        if total_count is not None:
            self.total_count = total_count

    @property
    def schedule_tasks(self):
        r"""Gets the schedule_tasks of this ListScheduleTasksResponse.

        定时任务列表。

        :return: The schedule_tasks of this ListScheduleTasksResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ScheduleTaskInfo`]
        """
        return self._schedule_tasks

    @schedule_tasks.setter
    def schedule_tasks(self, schedule_tasks):
        r"""Sets the schedule_tasks of this ListScheduleTasksResponse.

        定时任务列表。

        :param schedule_tasks: The schedule_tasks of this ListScheduleTasksResponse.
        :type schedule_tasks: list[:class:`huaweicloudsdkrds.v3.ScheduleTaskInfo`]
        """
        self._schedule_tasks = schedule_tasks

    @property
    def total_count(self):
        r"""Gets the total_count of this ListScheduleTasksResponse.

        总任务数量。

        :return: The total_count of this ListScheduleTasksResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListScheduleTasksResponse.

        总任务数量。

        :param total_count: The total_count of this ListScheduleTasksResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListScheduleTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
