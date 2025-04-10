# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scheduled_tasks': 'list[ScheduledTask]',
        'total_count': 'int'
    }

    attribute_map = {
        'scheduled_tasks': 'scheduled_tasks',
        'total_count': 'total_count'
    }

    def __init__(self, scheduled_tasks=None, total_count=None):
        r"""ListScheduledTasksResponse

        The model defined in huaweicloud sdk

        :param scheduled_tasks: 定时任务列表。
        :type scheduled_tasks: list[:class:`huaweicloudsdkworkspace.v2.ScheduledTask`]
        :param total_count: 总个数。
        :type total_count: int
        """
        
        super(ListScheduledTasksResponse, self).__init__()

        self._scheduled_tasks = None
        self._total_count = None
        self.discriminator = None

        if scheduled_tasks is not None:
            self.scheduled_tasks = scheduled_tasks
        if total_count is not None:
            self.total_count = total_count

    @property
    def scheduled_tasks(self):
        r"""Gets the scheduled_tasks of this ListScheduledTasksResponse.

        定时任务列表。

        :return: The scheduled_tasks of this ListScheduledTasksResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ScheduledTask`]
        """
        return self._scheduled_tasks

    @scheduled_tasks.setter
    def scheduled_tasks(self, scheduled_tasks):
        r"""Sets the scheduled_tasks of this ListScheduledTasksResponse.

        定时任务列表。

        :param scheduled_tasks: The scheduled_tasks of this ListScheduledTasksResponse.
        :type scheduled_tasks: list[:class:`huaweicloudsdkworkspace.v2.ScheduledTask`]
        """
        self._scheduled_tasks = scheduled_tasks

    @property
    def total_count(self):
        r"""Gets the total_count of this ListScheduledTasksResponse.

        总个数。

        :return: The total_count of this ListScheduledTasksResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListScheduledTasksResponse.

        总个数。

        :param total_count: The total_count of this ListScheduledTasksResponse.
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
        if not isinstance(other, ListScheduledTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
