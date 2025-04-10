# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduleRecordTasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'offset': 'int',
        'limit': 'int',
        'tasks': 'list[ScheduleRecordTasks]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'offset': 'offset',
        'limit': 'limit',
        'tasks': 'tasks',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, total=None, offset=None, limit=None, tasks=None, x_request_id=None):
        r"""ListScheduleRecordTasksResponse

        The model defined in huaweicloud sdk

        :param total: 查询结果的总元素数量
        :type total: int
        :param offset: 记录偏移量
        :type offset: int
        :param limit: 当前页条目数
        :type limit: int
        :param tasks: 录制模板数组
        :type tasks: list[:class:`huaweicloudsdklive.v1.ScheduleRecordTasks`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListScheduleRecordTasksResponse, self).__init__()

        self._total = None
        self._offset = None
        self._limit = None
        self._tasks = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if tasks is not None:
            self.tasks = tasks
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        r"""Gets the total of this ListScheduleRecordTasksResponse.

        查询结果的总元素数量

        :return: The total of this ListScheduleRecordTasksResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListScheduleRecordTasksResponse.

        查询结果的总元素数量

        :param total: The total of this ListScheduleRecordTasksResponse.
        :type total: int
        """
        self._total = total

    @property
    def offset(self):
        r"""Gets the offset of this ListScheduleRecordTasksResponse.

        记录偏移量

        :return: The offset of this ListScheduleRecordTasksResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScheduleRecordTasksResponse.

        记录偏移量

        :param offset: The offset of this ListScheduleRecordTasksResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduleRecordTasksResponse.

        当前页条目数

        :return: The limit of this ListScheduleRecordTasksResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduleRecordTasksResponse.

        当前页条目数

        :param limit: The limit of this ListScheduleRecordTasksResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def tasks(self):
        r"""Gets the tasks of this ListScheduleRecordTasksResponse.

        录制模板数组

        :return: The tasks of this ListScheduleRecordTasksResponse.
        :rtype: list[:class:`huaweicloudsdklive.v1.ScheduleRecordTasks`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ListScheduleRecordTasksResponse.

        录制模板数组

        :param tasks: The tasks of this ListScheduleRecordTasksResponse.
        :type tasks: list[:class:`huaweicloudsdklive.v1.ScheduleRecordTasks`]
        """
        self._tasks = tasks

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListScheduleRecordTasksResponse.

        :return: The x_request_id of this ListScheduleRecordTasksResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListScheduleRecordTasksResponse.

        :param x_request_id: The x_request_id of this ListScheduleRecordTasksResponse.
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
        if not isinstance(other, ListScheduleRecordTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
