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
        'instance_id': 'str',
        'instance_name': 'str',
        'status': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'status': 'status',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, offset=None, limit=None, instance_id=None, instance_name=None, status=None, start_time=None, end_time=None):
        r"""ListScheduleTasksRequest

        The model defined in huaweicloud sdk

        :param offset: 索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为50。
        :type limit: int
        :param instance_id: 实例id，按实例id过滤。
        :type instance_id: str
        :param instance_name: 实例名称，按实例名称过滤。
        :type instance_name: str
        :param status: 任务状态，按任务状态过滤。 Initing:初始化中 Pending:挂起 Running:运行中 Completed:已完成 Failed:已失败 Unauthorized:未授权 Canceled:已取消
        :type status: str
        :param start_time: 查询任务创建的开始时间，“start_time”有值时，“end_time”必选。格式为UTC时间戳。
        :type start_time: str
        :param end_time: 查询任务创建的结束时间，“start_time”有值时，“end_time”必选。格式为UTC时间戳。
        :type end_time: str
        """
        
        

        self._offset = None
        self._limit = None
        self._instance_id = None
        self._instance_name = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListScheduleTasksRequest.

        索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListScheduleTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScheduleTasksRequest.

        索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListScheduleTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduleTasksRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为50。

        :return: The limit of this ListScheduleTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduleTasksRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为50。

        :param limit: The limit of this ListScheduleTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListScheduleTasksRequest.

        实例id，按实例id过滤。

        :return: The instance_id of this ListScheduleTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListScheduleTasksRequest.

        实例id，按实例id过滤。

        :param instance_id: The instance_id of this ListScheduleTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ListScheduleTasksRequest.

        实例名称，按实例名称过滤。

        :return: The instance_name of this ListScheduleTasksRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ListScheduleTasksRequest.

        实例名称，按实例名称过滤。

        :param instance_name: The instance_name of this ListScheduleTasksRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def status(self):
        r"""Gets the status of this ListScheduleTasksRequest.

        任务状态，按任务状态过滤。 Initing:初始化中 Pending:挂起 Running:运行中 Completed:已完成 Failed:已失败 Unauthorized:未授权 Canceled:已取消

        :return: The status of this ListScheduleTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListScheduleTasksRequest.

        任务状态，按任务状态过滤。 Initing:初始化中 Pending:挂起 Running:运行中 Completed:已完成 Failed:已失败 Unauthorized:未授权 Canceled:已取消

        :param status: The status of this ListScheduleTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListScheduleTasksRequest.

        查询任务创建的开始时间，“start_time”有值时，“end_time”必选。格式为UTC时间戳。

        :return: The start_time of this ListScheduleTasksRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListScheduleTasksRequest.

        查询任务创建的开始时间，“start_time”有值时，“end_time”必选。格式为UTC时间戳。

        :param start_time: The start_time of this ListScheduleTasksRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListScheduleTasksRequest.

        查询任务创建的结束时间，“start_time”有值时，“end_time”必选。格式为UTC时间戳。

        :return: The end_time of this ListScheduleTasksRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListScheduleTasksRequest.

        查询任务创建的结束时间，“start_time”有值时，“end_time”必选。格式为UTC时间戳。

        :param end_time: The end_time of this ListScheduleTasksRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
