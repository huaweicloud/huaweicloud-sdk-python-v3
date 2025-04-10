# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHpcCacheTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tasks': 'list[OneHpcCacheTaskInfoResp]',
        'count': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'tasks': 'tasks',
        'count': 'count',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, tasks=None, count=None, x_request_id=None):
        r"""ListHpcCacheTasksResponse

        The model defined in huaweicloud sdk

        :param tasks: 任务详情
        :type tasks: list[:class:`huaweicloudsdksfsturbo.v1.OneHpcCacheTaskInfoResp`]
        :param count: 任务数量
        :type count: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListHpcCacheTasksResponse, self).__init__()

        self._tasks = None
        self._count = None
        self._x_request_id = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if count is not None:
            self.count = count
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def tasks(self):
        r"""Gets the tasks of this ListHpcCacheTasksResponse.

        任务详情

        :return: The tasks of this ListHpcCacheTasksResponse.
        :rtype: list[:class:`huaweicloudsdksfsturbo.v1.OneHpcCacheTaskInfoResp`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListHpcCacheTasksResponse.

        任务详情

        :param tasks: The tasks of this ListHpcCacheTasksResponse.
        :type tasks: list[:class:`huaweicloudsdksfsturbo.v1.OneHpcCacheTaskInfoResp`]
        """
        self._tasks = tasks

    @property
    def count(self):
        r"""Gets the count of this ListHpcCacheTasksResponse.

        任务数量

        :return: The count of this ListHpcCacheTasksResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListHpcCacheTasksResponse.

        任务数量

        :param count: The count of this ListHpcCacheTasksResponse.
        :type count: int
        """
        self._count = count

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListHpcCacheTasksResponse.

        :return: The x_request_id of this ListHpcCacheTasksResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListHpcCacheTasksResponse.

        :param x_request_id: The x_request_id of this ListHpcCacheTasksResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListHpcCacheTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
