# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectorTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[SmartConnectTaskEntity]',
        'total_number': 'int',
        'max_tasks': 'int',
        'quota_tasks': 'int'
    }

    attribute_map = {
        'tasks': 'tasks',
        'total_number': 'total_number',
        'max_tasks': 'max_tasks',
        'quota_tasks': 'quota_tasks'
    }

    def __init__(self, tasks=None, total_number=None, max_tasks=None, quota_tasks=None):
        r"""ListConnectorTasksResponse

        The model defined in huaweicloud sdk

        :param tasks: Smart Connect任务详情。
        :type tasks: list[:class:`huaweicloudsdkkafka.v2.SmartConnectTaskEntity`]
        :param total_number: Smart Connect任务数。
        :type total_number: int
        :param max_tasks: Smart Connect最大任务数。
        :type max_tasks: int
        :param quota_tasks: Smart Connect任务配额。
        :type quota_tasks: int
        """
        
        super(ListConnectorTasksResponse, self).__init__()

        self._tasks = None
        self._total_number = None
        self._max_tasks = None
        self._quota_tasks = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if total_number is not None:
            self.total_number = total_number
        if max_tasks is not None:
            self.max_tasks = max_tasks
        if quota_tasks is not None:
            self.quota_tasks = quota_tasks

    @property
    def tasks(self):
        r"""Gets the tasks of this ListConnectorTasksResponse.

        Smart Connect任务详情。

        :return: The tasks of this ListConnectorTasksResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.SmartConnectTaskEntity`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListConnectorTasksResponse.

        Smart Connect任务详情。

        :param tasks: The tasks of this ListConnectorTasksResponse.
        :type tasks: list[:class:`huaweicloudsdkkafka.v2.SmartConnectTaskEntity`]
        """
        self._tasks = tasks

    @property
    def total_number(self):
        r"""Gets the total_number of this ListConnectorTasksResponse.

        Smart Connect任务数。

        :return: The total_number of this ListConnectorTasksResponse.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        r"""Sets the total_number of this ListConnectorTasksResponse.

        Smart Connect任务数。

        :param total_number: The total_number of this ListConnectorTasksResponse.
        :type total_number: int
        """
        self._total_number = total_number

    @property
    def max_tasks(self):
        r"""Gets the max_tasks of this ListConnectorTasksResponse.

        Smart Connect最大任务数。

        :return: The max_tasks of this ListConnectorTasksResponse.
        :rtype: int
        """
        return self._max_tasks

    @max_tasks.setter
    def max_tasks(self, max_tasks):
        r"""Sets the max_tasks of this ListConnectorTasksResponse.

        Smart Connect最大任务数。

        :param max_tasks: The max_tasks of this ListConnectorTasksResponse.
        :type max_tasks: int
        """
        self._max_tasks = max_tasks

    @property
    def quota_tasks(self):
        r"""Gets the quota_tasks of this ListConnectorTasksResponse.

        Smart Connect任务配额。

        :return: The quota_tasks of this ListConnectorTasksResponse.
        :rtype: int
        """
        return self._quota_tasks

    @quota_tasks.setter
    def quota_tasks(self, quota_tasks):
        r"""Sets the quota_tasks of this ListConnectorTasksResponse.

        Smart Connect任务配额。

        :param quota_tasks: The quota_tasks of this ListConnectorTasksResponse.
        :type quota_tasks: int
        """
        self._quota_tasks = quota_tasks

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
        if not isinstance(other, ListConnectorTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
