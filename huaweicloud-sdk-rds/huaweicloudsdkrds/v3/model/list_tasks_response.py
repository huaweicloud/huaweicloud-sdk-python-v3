# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'actions': 'list[str]',
        'tasks': 'list[Task]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'actions': 'actions',
        'tasks': 'tasks'
    }

    def __init__(self, total_count=None, actions=None, tasks=None):
        r"""ListTasksResponse

        The model defined in huaweicloud sdk

        :param total_count: 任务总数。
        :type total_count: int
        :param actions: 任务名称列表。
        :type actions: list[str]
        :param tasks: 任务列表。
        :type tasks: list[:class:`huaweicloudsdkrds.v3.Task`]
        """
        
        super(ListTasksResponse, self).__init__()

        self._total_count = None
        self._actions = None
        self._tasks = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if actions is not None:
            self.actions = actions
        if tasks is not None:
            self.tasks = tasks

    @property
    def total_count(self):
        r"""Gets the total_count of this ListTasksResponse.

        任务总数。

        :return: The total_count of this ListTasksResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListTasksResponse.

        任务总数。

        :param total_count: The total_count of this ListTasksResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def actions(self):
        r"""Gets the actions of this ListTasksResponse.

        任务名称列表。

        :return: The actions of this ListTasksResponse.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this ListTasksResponse.

        任务名称列表。

        :param actions: The actions of this ListTasksResponse.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def tasks(self):
        r"""Gets the tasks of this ListTasksResponse.

        任务列表。

        :return: The tasks of this ListTasksResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.Task`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListTasksResponse.

        任务列表。

        :param tasks: The tasks of this ListTasksResponse.
        :type tasks: list[:class:`huaweicloudsdkrds.v3.Task`]
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
        if not isinstance(other, ListTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
